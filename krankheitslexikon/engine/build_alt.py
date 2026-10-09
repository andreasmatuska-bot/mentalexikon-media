#!/usr/bin/env python3
"""Krankheitslexikon, Bau im ALTEN STIL (Julias Originale vor dem 04.10.2026).
Aufbau A "Papier": beiges Papier, Ueberschrift fett schwarz auf neongruenem Marker (linksbuendig),
nummerierte Liste (Zahl normal, Begriff fett mit Doppelpunkt, darunter 2 bis 3 Zeilen Fliesstext),
kleines Wasserzeichen rechts in der Mitte, Fusszeile "Folge mir, ...".
Aufruf: python3 build_alt.py inhalt.json ausgabeordner musik.mp3
inhalt.json: {"name":"Krankheitslexikon_09_Thema","titel":"Was dir deine Krankheit sagen will:",
              "punkte":[["Begriff","Text"],...], "fuss":"Folge mir, um die Sprache deines Körpers zu verstehen."}
Aufbau B "Zwei Spalten" (seit 07.10.2026): im JSON "aufbau":"spalten" setzen, Funktion bau_spalten.
Erzeugt: <name>.png, <name>_Titelbild.jpg, <name>.mp4, <name>_IG.mp4
"""
import json,sys,os,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=1080,1920
HERE=os.path.dirname(os.path.abspath(__file__))
F=lambda n,s: ImageFont.truetype(os.path.join(HERE,'fonts',n+'.ttf'),s)

def papier(seed=7):
    rng=np.random.default_rng(seed)
    base=np.array([239,234,223],dtype=np.float32)
    fine=rng.normal(0,5.0,(H,W,1)).astype(np.float32)
    small=rng.normal(0,1,(H//6,W//6)).astype(np.float32)
    big=np.asarray(Image.fromarray(((small-small.min())/(small.max()-small.min())*255).astype(np.uint8)).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(3)),dtype=np.float32)
    big=((big-128)/128*5)[...,None]
    arr=np.clip(base+fine+big,0,255).astype(np.uint8)
    return Image.fromarray(arr,'RGB').filter(ImageFilter.GaussianBlur(0.6))

def wrap(d,text,font,maxw):
    lines=[];cur=''
    for w in text.split():
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur);cur=w
    if cur: lines.append(cur)
    return lines

def bau_papier(c,out):
    im=papier(); d=ImageDraw.Draw(im)
    X=110; MAXW=830
    # Ueberschrift mit Marker
    fs=60
    while True:
        ft=F('LeagueSpartan-Bold',fs); tl=wrap(d,c['titel'],ft,MAXW+40)
        if len(tl)<=2 or fs<56: break
        fs-=2
    lh=int(fs*1.12); y=268
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    for i,l in enumerate(tl):
        w=d.textlength(l,font=ft)
        od.rounded_rectangle([X-22,y+i*lh-14,X+w+22,y+(i+1)*lh+4],radius=16,fill=(200,247,140,235))
    im.paste(ov,(0,0),ov); d=ImageDraw.Draw(im)
    for i,l in enumerate(tl): d.text((X,y+i*lh+2),l,font=ft,fill=(8,8,8))
    y=y+len(tl)*lh+62
    fr=F('OpenSans-Regular',31); fb=F('OpenSans-Bold',31); L=45; col=(34,34,34)
    n=len(c['punkte']); 
    blocks=[(b,wrap(d,t,fr,MAXW)) for b,t in c['punkte']]
    tot=sum(L*(1+len(ls)) for _,ls in blocks)
    gap=min(52,max(30,(1530-y-tot)//max(1,n-1)))
    wm_y=None
    for i,(b,ls) in enumerate(blocks,1):
        num=f'{i}.'; d.text((X+24,y),num,font=fr,fill=col)
        nx=X+24+d.textlength(num,font=fr)+3
        d.text((nx,y),b,font=fb,fill=(10,10,10)); d.text((nx+d.textlength(b,font=fb),y),':',font=fr,fill=col)
        y+=L
        for l in ls: d.text((X,y),l,font=fr,fill=col); y+=L
        if i==n//2: wm_y=y+gap//2-14
        y+=gap
    y=y-gap+46
    fw=F('LeagueSpartan-Regular',22); wm='@krankheitslexikon'
    d.text((W-70-d.textlength(wm,font=fw),wm_y),wm,font=fw,fill=(70,70,70))
    ff=F('Oswald-Regular',30); d.text((X-50,max(y,1560)),c.get('fuss','Folge mir, um die Sprache deines Körpers zu verstehen.'),font=ff,fill=(20,20,20))
    assert max(y,1560)+40<1640, 'Inhalt zu lang'
    png=os.path.join(out,c['name']+'.png'); im.save(png)
    im.save(os.path.join(out,c['name']+'_Titelbild.jpg'),quality=93)
    return png

def verlauf_grau():
    # heller, grauer Verlauf wie bei Julias Zwei Spalten Beitraegen
    a=np.linspace(0,1,H,dtype=np.float32)[:,None,None]
    top=np.array([246,246,247],dtype=np.float32); bot=np.array([226,226,229],dtype=np.float32)
    arr=np.repeat(top*(1-a)+bot*a,W,axis=1)
    return Image.fromarray(arr.astype(np.uint8),'RGB')

def pfeil(d,x,y,size,col):
    # einfacher Pfeil nach rechts, falls die Schrift keinen hat
    w=int(size*0.62); my=y+int(size*0.74); t=max(2,size//12)
    d.line([x,my,x+w,my],fill=col,width=t)
    d.line([x+w-size//5,my-size//5,x+w,my],fill=col,width=t); d.line([x+w-size//5,my+size//5,x+w,my],fill=col,width=t)
    return w

def bau_spalten(c,out):
    """Aufbau B "Zwei Spalten": hellgrauer Verlauf, Ueberschrift rot auf rosa Kasten (mittig),
    darunter rot "(Und was die wenigsten wissen…)", zwei Spalten dichter Fliesstext
    (Begriff fett, Pfeil, Bedeutung normal), Wasserzeichen klein mitten im Bild, Fusszeile rot."""
    im=verlauf_grau(); d=ImageDraw.Draw(im)
    ROT=(200,40,60); ROSA=(250,208,216)
    fs=68
    while True:
        ft=F('LeagueSpartan-Bold',fs); tl=wrap(d,c['titel'],ft,860)
        if len(tl)<=2 or fs<54: break
        fs-=2
    lh=int(fs*1.22); y=262
    for i,l in enumerate(tl):
        w=d.textlength(l,font=ft); x=(W-w)//2
        d.rounded_rectangle([x-24,y+i*lh-10,x+w+24,y+(i+1)*lh-6],radius=10,fill=ROSA)
    for i,l in enumerate(tl):
        w=d.textlength(l,font=ft); d.text(((W-w)//2,y+i*lh+4),l,font=ft,fill=ROT)
    y=y+len(tl)*lh+22
    fu=F('OpenSans-Regular',32); u=c.get('unter','(Und was die wenigsten wissen…)')
    d.text(((W-d.textlength(u,font=fu))//2,y),u,font=fu,fill=ROT)
    y0=y+86
    S=c.get('schrift',29); fr=F('OpenSans-Regular',S); fb=F('OpenSans-Bold',S); L=int(S*1.38); col=(34,34,34)
    CW=438; XS=[76,566]; gap=c.get('abstand',24)
    def setze(x,y,b,t,zeichnen=True):
        # fliessender Text: Begriff fett, Pfeil, Bedeutung normal
        cx=x; sp=d.textlength(' ',font=fr)
        teile=[(w,fb) for w in b.split()]+[('->',None)]+[(w,fr) for w in t.split()]
        for w,f in teile:
            ww=int(S*0.62) if f is None else d.textlength(w,font=f)
            if cx>x and cx+ww>x+CW: cx=x; y+=L
            if zeichnen:
                if f is None: pfeil(d,cx,y,S,col)
                else: d.text((cx,y),w,font=f,fill=(10,10,10) if f is fb else col)
            cx+=ww+sp
        return y+L,cx,y
    n=len(c['punkte']); h=(n+1)//2; spalten=[c['punkte'][:h],c['punkte'][h:]]
    ende=[]; kand=[]
    for k,sp_ in enumerate(spalten):
        y=y0
        for i,(b,t) in enumerate(sp_):
            y,ex,ly=setze(XS[k],y,b,t); y+=gap
            if k==1 and 0<i<len(sp_)-1: kand.append((ex,ly))
        ende.append(y-gap)
    yb=max(ende)
    fw=F('LeagueSpartan-Regular',22); wm='@krankheitslexikon'
    # Wasserzeichen klein und grau mitten im Bild, unter der kuerzeren Spalte bzw. zwischen Text und Fusszeile
    wx=XS[1]+CW-d.textlength(wm,font=fw); frei=[k_ for k_ in kand if k_[0]+24<wx]
    if frei: ex,ly=min(frei); d.text((wx,ly+int(S*0.42)),wm,font=fw,fill=(110,110,110))
    else: d.text((wx,yb+26),wm,font=fw,fill=(110,110,110))
    ff=F('OpenSans-Bold',31); fz=c.get('fuss','Folge mir, um die Sprache deines Körpers zu verstehen.')
    yf=max(yb+84,1500)
    d.text(((W-d.textlength(fz,font=ff))//2,yf),fz,font=ff,fill=ROT)
    assert yf+44<1640, 'Inhalt zu lang: %d'%yf
    png=os.path.join(out,c['name']+'.png'); im.save(png)
    im.save(os.path.join(out,c['name']+'_Titelbild.jpg'),quality=93)
    return png

def video(png,name,out,musik):
    mp4=os.path.join(out,name+'.mp4'); ig=os.path.join(out,name+'_IG.mp4')
    # stehendes Bild ohne Zoom wie bei Julias Originalen (seit 07.10.2026, vorher Zoom 1,5 Prozent), Musik mit Ein und Ausblendung, minus 16 LUFS
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-i',png,'-ss','2','-t','6','-i',musik,
      '-filter_complex',"[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1[v];[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.4,afade=t=out:st=5.2:d=0.8[a]",
      '-map','[v]','-map','[a]','-t','6','-r','30','-c:v','libx264','-pix_fmt','yuv420p','-profile:v','high','-level','4.2','-crf','17','-preset','slow','-c:a','aac','-b:a','128k','-ar','48000','-movflags','+faststart',mp4],check=True)
    # _IG: Titelbild steht 0,10 s voll, blendet in 0,25 s ins Video ueber, Gesamtlaenge bleibt 6 s
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t','0.35','-i',png,'-i',mp4,
      '-filter_complex',"[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1,settb=1/30[c];[1:v]trim=start=0.10,setpts=PTS-STARTPTS,fps=30,format=yuv420p,setsar=1,settb=1/30[m];[c][m]xfade=transition=fade:duration=0.25:offset=0.10,format=yuv420p[v]",
      '-map','[v]','-map','1:a','-t','6','-r','30','-c:v','libx264','-pix_fmt','yuv420p','-profile:v','high','-level','4.2','-crf','17','-preset','slow','-c:a','copy','-movflags','+faststart',ig],check=True)
    return mp4,ig

if __name__=='__main__':
    c=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
    png=(bau_spalten if c.get('aufbau')=='spalten' else bau_papier)(c,out); video(png,c['name'],out,sys.argv[3])
    print('fertig',c['name'])
