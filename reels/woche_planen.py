"""Legt den Reel Plan für beide Mindset Seiten an: 8 Reels pro Tag und Seite.
Aufruf im Ordner reels:  python3 woche_planen.py <Starttag JJJJ-MM-TT> [Tage=7] [--ab HH:MM]
Schreibt plan/<Starttag>.json (eine Liste für beide Seiten). Danach: node reel_bauen.js plan/<Starttag>.json

Prinzip (von Andreas am 09.10.2026 festgelegt): die erfolgreichsten Listen immer wieder posten und jedes Mal
nur ein bisschen abändern. Jede Liste aus pool.json läuft pro Woche zweimal je Seite, mit anderer Überschrift,
anderer Frage, anderer Caption, anderer Reihenfolge der Punkte und anderer Musik. Die beiden Seiten bekommen
nie zur selben Zeit dieselbe Liste und in derselben Woche nie dieselbe Fassung.
"""
import json, random, sys, datetime, os
ZEITEN = ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00']   # Zeit in Zypern (Asia/Nicosia)
SEITEN = {'mindsetologie': dict(marke='MINDSETOLOGIE', handle='@mindsetologie'),
          'mentalexikon': dict(marke='MENTALEXIKON', handle='@mentalexikon')}
KOMBI = [(0, 0, 0), (1, 1, 1), (2, 1, 0), (1, 0, 0), (2, 0, 1), (0, 1, 1)]   # (Überschrift, Frage, Caption)

def reihenfolge(pool, slots, rng, sperre):
    """Verteilt die Listen auf die Termine: gleiche Liste frühestens nach 2 Tagen wieder,
    pro Tag kein Themenfeld doppelt, und nie dieselbe Liste wie die andere Seite zur selben Zeit."""
    ids = [b['id'] for b in pool]; feld = {b['id']: b['feld'] for b in pool}
    best = None
    for versuch in range(4000):
        frei = {i: 0 for i in ids}; letzte = {}; folge = []; ok = True
        for n, (tag, zeit) in enumerate(slots):
            heute = {feld[folge[k]] for k in range(len(folge)) if slots[k][0] == tag}
            min_n = min(frei.values())
            kand = [i for i in ids if frei[i] == min_n and feld[i] not in heute and n - letzte.get(i, -99) >= 16 and sperre.get((tag, zeit)) != i]
            if not kand:
                kand = [i for i in ids if frei[i] <= min_n + 1 and feld[i] not in heute and n - letzte.get(i, -99) >= 12 and sperre.get((tag, zeit)) != i]
            if not kand: ok = False; break
            i = rng.choice(kand); folge.append(i); frei[i] += 1; letzte[i] = n
        if ok: return folge
    raise SystemExit('keine gültige Verteilung gefunden')

def main():
    start = datetime.date.fromisoformat(sys.argv[1])
    arg = [a for a in sys.argv[2:] if not a.startswith('--')]
    tage = int(arg[0]) if arg else 7
    ab = sys.argv[sys.argv.index('--ab') + 1] if '--ab' in sys.argv else '00:00'
    pool = json.load(open('pool.json')); P = {b['id']: b for b in pool}
    pool = [b for b in pool if not b.get('pause')]
    woche = start.toordinal() // 7
    slots = [(start + datetime.timedelta(days=d), z) for d in range(tage) for z in ZEITEN if not (d == 0 and z < ab)]
    plan = []; sperre = {}; zaehler = 0
    for s, (seite, S) in enumerate(SEITEN.items()):
        rng = random.Random(f'{start}-{seite}')
        folge = reihenfolge(pool, slots, rng, sperre)
        mal = {}
        for (tag, zeit), i in zip(slots, folge):
            sperre[(tag, zeit)] = i
            b = P[i]; u = mal.get(i, 0); mal[i] = u + 1
            k, f, c = KOMBI[(2 * woche + u + 3 * s) % len(KOMBI)]
            punkte = list(b['punkte'])
            if not b.get('fest'): random.Random(f'{start}-{seite}-{i}-{u}').shuffle(punkte)
            frage = b['frage'][f % len(b['frage'])]
            e = dict(seite=seite, termin=f'{tag} {zeit}', basis=i, fassung=[k, f, c],
                     datei=f'{seite}/{tag}/{zeit.replace(":", "")}_{b["slug"]}', marke=S['marke'], musik=zaehler,
                     typ=b['typ'], kopf=b['kopf'][k % len(b['kopf'])], punkte=punkte, frage=frage,
                     caption=f'{b["caption"][c % len(b["caption"])]}\n\n{frage} Folg {S["handle"]} für mehr davon.')
            if b.get('schluss'): e['schluss'] = b['schluss']
            plan.append(e); zaehler += 1
    os.makedirs('plan', exist_ok=True)
    json.dump(plan, open(f'plan/{start}.json', 'w'), ensure_ascii=False, indent=1)
    print(len(plan), 'Reels geplant, Datei', f'plan/{start}.json')
main()
