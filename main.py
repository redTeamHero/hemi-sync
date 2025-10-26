"""
binaural_playlist_generator.py
Create educational binaural-beat tracks for focus or relaxation.

Requirements:
pip install numpy scipy soundfile
"""

import numpy as np
import soundfile as sf

def generate_binaural(base_freq=200.0, offset=7.83, duration_min=5,
                      fs=44100, ambient='none', filename='output.wav'):
    """
    base_freq: tone in left ear (Hz)
    offset: difference to right ear (Hz)
    duration_min: length of track
    fs: sample rate
    ambient: 'white', 'pink', 'brown', or 'none'
    filename: name of file to save
    """
    duration = duration_min * 60
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # left/right carrier waves
    left = np.sin(2 * np.pi * base_freq * t)
    right = np.sin(2 * np.pi * (base_freq + offset) * t)

    # optional ambient layer
    if ambient != 'none':
        noise = np.random.normal(0, 1, len(t))
        if ambient == 'pink':
            # simple pink-noise approximation
            b = np.cumsum(noise)
            noise = b / np.max(np.abs(b))
        elif ambient == 'brown':
            b = np.cumsum(np.cumsum(noise))
            noise = b / np.max(np.abs(b))
        noise = noise * 0.2  # keep ambient subtle
        left += noise
        right += noise

    stereo = np.vstack((left, right)).T
    stereo /= np.max(np.abs(stereo))  # normalize
    sf.write(filename, stereo, fs)
    print(f"Saved {filename} ({offset:.2f} Hz beat)")

# Example playlist generation
playlist = [
    ("alpha_10hz.wav", 10, 10, 'white'),
    ("schumann_7_83hz.wav", 7.83, 15, 'pink'),
    ("theta_4hz.wav", 4, 20, 'brown'),
    ("delta_1hz.wav", 1, 30, 'brown')
]
for name, freq, mins, amb in playlist:
    generate_binaural(base_freq=200, offset=freq,
                      duration_min=mins, ambient=amb,
                      filename=name)
