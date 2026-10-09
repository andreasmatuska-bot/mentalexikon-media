"""Erzeugt ruhige, entspannte eigene Musikstücke (gut 6 Sekunden) für die Listen Videos.
Von Andreas am 09.10.2026 verlangt: die fröhliche Musik (Ukulele, Klatschen, Glockenspiel) klang nervig,
die neue Melodie soll entspannter sein. Deshalb: langsames Tempo, weiches E Piano, warme Fläche,
kein Schlagzeug, kein Klatschen, keine hellen Glocken. Alles wird hier berechnet, keine fremde Musik.
Aufruf: python3 musik_ruhig_bauen.py   -> musik/ruhig_1.wav ...
"""
import numpy as np, wave, os
SR = 44100
def ep(freq, dur, vel=1.0):
    """Weiches E Piano (sanfte FM, schnell ausklingender Glanz, langer warmer Ton)."""
    t = np.arange(int(SR * dur)) / SR
    idx = 1.1 * vel * np.exp(-6 * t) + 0.12
    x = np.sin(2*np.pi*freq*t + idx*np.sin(2*np.pi*freq*t))
    x += 0.18 * np.sin(2*np.pi*2*freq*t) * np.exp(-5*t)
    env = (1 - np.exp(-t / 0.012)) * np.exp(-t * 1.25)
    return x * env * vel
def pad(freq, dur):
    """Warme Fläche: zwei leicht verstimmte Sinustöne, langsam ein und aus."""
    t = np.arange(int(SR * dur)) / SR
    x = np.sin(2*np.pi*freq*1.002*t) + np.sin(2*np.pi*freq*0.998*t) + 0.25*np.sin(2*np.pi*2*freq*t)
    a = np.clip(t / 1.1, 0, 1); r = np.clip((dur - t) / 1.2, 0, 1)
    return x * a * r / 2.25
def lowpass(x, fc):
    a = np.exp(-2*np.pi*fc/SR); y = np.empty_like(x); z = 0.0
    for i in range(len(x)):
        z = (1-a)*x[i] + a*z; y[i] = z
    return y
def add(mix, x, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR); n = min(len(x), mix.shape[0] - i)
    if n <= 0: return
    mix[i:i+n, 0] += x[:n] * gain * (1 - max(pan, 0)); mix[i:i+n, 1] += x[:n] * gain * (1 + min(pan, 0))
def fr(semi, base): return base * 2 ** (semi / 12)
def hall(mix):
    out = mix.copy()
    for d, g in ((0.071, 0.30), (0.113, 0.24), (0.167, 0.19), (0.251, 0.15), (0.359, 0.11), (0.487, 0.08)):
        k = int(d * SR); out[k:, 0] += mix[:-k, 1] * g; out[k:, 1] += mix[:-k, 0] * g
    return out
def stueck(nr, base, bpm, akkorde, melodie):
    beat = 60 / bpm; total = 6.1; mix = np.zeros((int(SR*total), 2))
    takt = 2 * beat
    for k, (root, toene) in enumerate(akkorde):
        t0 = k * takt
        if t0 >= total: break
        add(mix, pad(fr(root - 12, base), takt + 1.3), t0, 0.20)
        add(mix, pad(fr(root + toene[1], base), takt + 1.3), t0, 0.09, pan=0.2)
        for j, s in enumerate(toene):           # sanft gebrochener Akkord
            add(mix, ep(fr(root + s, base), 2.6, 0.55), t0 + j * 0.055, 0.15, pan=-0.2 + 0.13*j)
        add(mix, ep(fr(root + toene[2], base), 2.0, 0.4), t0 + beat, 0.10, pan=0.25)
    for (b, semi) in melodie:
        if b * beat < total - 0.4: add(mix, ep(fr(semi + 12, base), 2.4, 0.6), b * beat, 0.17, pan=0.1)
    mix = hall(mix)
    mix[:, 0] = lowpass(mix[:, 0], 2600); mix[:, 1] = lowpass(mix[:, 1], 2600)
    mix /= max(1e-9, np.abs(mix).max()) / 0.6
    f = np.ones(len(mix)); a = int(0.25*SR); f[:a] = np.linspace(0, 1, a); k = int(1.3*SR); f[-k:] = np.linspace(1, 0, k) ** 1.6
    mix *= f[:, None]
    os.makedirs('musik', exist_ok=True)
    w = wave.open(f'musik/ruhig_{nr}.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype('<i2').tobytes()); w.close()
M7 = [0, 4, 7, 11]; m7 = [0, 3, 7, 10]; add9 = [0, 4, 7, 14]; m9 = [0, 3, 7, 14]
N = {'C':261.63,'D':293.66,'Eb':311.13,'F':349.23,'G':392.0,'A':440.0,'Bb':466.16}
# (Grundton in Halbtönen, Akkordtöne); Melodie als (Zählzeit, Halbton), wenige lange Töne
stueck(1, N['F']/2,  66, [(0, M7), (-3, m7), (5, M7), (0, add9)], [(1, 7), (3, 4), (5, 9), (6.5, 7)])
stueck(2, N['C']/2,  62, [(0, add9), (9-12, m7), (5, M7), (7, add9)], [(1.5, 16), (3.5, 14), (5, 12)])
stueck(3, N['Eb']/2, 64, [(0, M7), (5, M7), (-3, m9), (-5, add9)], [(1, 14), (2.5, 11), (4.5, 7), (6, 9)])
stueck(4, N['G']/2,  60, [(5, M7), (0, add9), (-3, m7), (0, M7)], [(1, 11), (3, 12), (4.5, 7)])
stueck(5, N['D']/2,  63, [(0, add9), (5, M7), (-3, m7), (5, add9)], [(1.5, 9), (3, 7), (5, 4), (6, 7)])
stueck(6, N['Bb']/4, 60, [(0, M7), (-3, m9), (5, add9), (0, M7)], [(1, 16), (3.5, 14), (5.5, 11)])
print('ok')
