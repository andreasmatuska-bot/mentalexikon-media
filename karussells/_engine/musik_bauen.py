"""Erzeugt kurze, fröhliche eigene Musikstücke (4,2 Sekunden) für die Listen Videos von Mindsetologie.
Alles wird hier berechnet (Ukulele Zupfen, Glockenspiel, Klatschen, Shaker), es wird keine fremde Musik verwendet.
Aufruf: python3 musik_bauen.py   -> musik/froehlich_1.wav ...
"""
import numpy as np, wave, os
SR = 44100
def pluck(freq, dur, seed, bright=0.5):
    n = int(SR * dur); p = int(SR / freq)
    rng = np.random.default_rng(seed); buf = rng.uniform(-1, 1, p)
    out = np.empty(n); 
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = (bright * buf[i % p] + (1 - bright) * buf[(i + 1) % p]) * 0.996
    return out * np.exp(-np.linspace(0, 3.2, n))
def bell(freq, dur):
    t = np.arange(int(SR * dur)) / SR
    return (np.sin(2*np.pi*freq*t) + 0.45*np.sin(2*np.pi*freq*2.76*t)*np.exp(-9*t) + 0.25*np.sin(2*np.pi*freq*4*t)*np.exp(-14*t)) * np.exp(-5.5*t)
def kick(dur=0.22):
    t = np.arange(int(SR * dur)) / SR
    return np.sin(2*np.pi*(55 + 70*np.exp(-28*t))*t) * np.exp(-13*t)
def clap(seed, dur=0.14):
    rng = np.random.default_rng(seed); n = int(SR*dur); x = rng.normal(0, 1, n)
    x = np.convolve(x, [1, -0.9], 'same'); t = np.arange(n)/SR
    env = np.exp(-38*t) + 0.6*np.exp(-38*np.clip(t-0.012, 0, 1))*(t > 0.012)
    return x * env * 0.5
def shaker(seed, dur=0.06):
    rng = np.random.default_rng(seed); n = int(SR*dur); x = rng.normal(0, 1, n)
    x = np.diff(np.concatenate([[0], x])); return x * np.exp(-np.linspace(0, 7, n)) * 0.3
def add(mix, x, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR); n = min(len(x), mix.shape[0] - i)
    if n <= 0: return
    mix[i:i+n, 0] += x[:n] * gain * (1 - max(pan, 0)); mix[i:i+n, 1] += x[:n] * gain * (1 + min(pan, 0))
N = {'C':261.63,'D':293.66,'E':329.63,'F':349.23,'G':392.0,'A':440.0,'B':493.88}
def fr(semi, base): return base * 2 ** (semi / 12)
MAJ = [0, 4, 7, 12]; MIN = [0, 3, 7, 12]
def stueck(nr, base, bpm, prog, melodie):
    beat = 60 / bpm; total = 4.2; mix = np.zeros((int(SR*total), 2))
    for b in range(8):
        root, typ = prog[(b // 2) % len(prog)]; t0 = b * beat
        for half in (0, 0.5):
            if half and b % 2 == 0 and nr % 2: continue
            for k, s in enumerate(typ if not half else typ[::-1]):
                add(mix, pluck(fr(root + s, base), 0.9, nr*100 + b*10 + k), t0 + half*beat + k*0.014, 0.16 if not half else 0.11, pan=-0.25)
        if b % 2 == 0: add(mix, kick(), t0, 0.55)
        else: add(mix, clap(nr*7 + b), t0, 0.5, pan=0.15)
        for h in (0, 0.5): add(mix, shaker(nr*13 + b*2 + int(h*2)), t0 + h*beat, 0.5 if h else 0.3, pan=0.35)
    for (b, semi) in melodie: add(mix, bell(fr(semi + 12, base), 0.8), b * beat, 0.2, pan=0.2)
    mix /= max(1e-9, np.abs(mix).max()) / 0.82
    f = np.ones(len(mix)); k = int(0.45*SR); f[-k:] = np.linspace(1, 0, k) ** 1.5; mix *= f[:, None]
    os.makedirs('musik', exist_ok=True)
    w = wave.open(f'musik/froehlich_{nr}.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes()); w.close()
I, IV, V, VI = (0, MAJ), (5, MAJ), (7, MAJ), (9, MIN)
stueck(1, N['C'], 116, [I, V, VI, IV], [(0,4),(0.5,7),(1,12),(2,11),(2.5,7),(3,9),(4,12),(4.5,9),(5,7),(6,5),(6.5,9),(7,12)])
stueck(2, N['D']/2*2, 118, [I, IV, V, I], [(0,12),(1,7),(1.5,9),(2,12),(3,9),(4,11),(4.5,14),(5,11),(6,12),(7,16)])
stueck(3, N['F'], 112, [I, VI, IV, V], [(0,7),(0.5,9),(1,7),(2,4),(3,7),(4,5),(4.5,9),(5.5,12),(6,11),(7,7)])
stueck(4, N['G']/2, 120, [IV, I, V, VI], [(0,17),(1,16),(1.5,12),(2,16),(3,19),(4,19),(5,14),(5.5,16),(6,21),(7,19)])
print('ok')
