#!/usr/bin/env python3
"""
binaural_generator_v3.py
------------------------
Create educational binaural-beat tracks and automatically overlay
an ambience file (rainforest, rain, ocean, etc.).

Requirements:
    pip install numpy soundfile pydub
Supported ambience formats: WAV, MP3, FLAC, etc.
"""

import numpy as np
import soundfile as sf
from pydub import AudioSegment
import os

def generate_binaural(
    base_freq: float = 200.0,
    offset: float = 7.83,
    duration_min: float = 10.0,
    fs: int = 44100,
    ambient: str = "none",
    filename: str = "output.wav",
    chunk_seconds: int = 10
):
    """Stream-safe generation of a stereo binaural tone."""
    total_samples = int(duration_min * 60 * fs)
    chunk_size = chunk_seconds * fs

    with sf.SoundFile(filename, mode="w", samplerate=fs, channels=2) as f:
        samples_written = 0
        while samples_written < total_samples:
            n = min(chunk_size, total_samples - samples_written)
            t = np.arange(n) / fs

            left = np.sin(2 * np.pi * base_freq * t)
            right = np.sin(2 * np.pi * (base_freq + offset) * t)

            if ambient != "none":
                noise = np.random.normal(0, 1, n)
                if ambient == "pink":
                    noise = np.cumsum(noise)
                elif ambient == "brown":
                    noise = np.cumsum(np.cumsum(noise))
                noise /= np.max(np.abs(noise))
                noise *= 0.2
                left += noise
                right += noise

            stereo = np.vstack((left, right)).T
            stereo /= np.max(np.abs(stereo) + 1e-9)
            f.write(stereo)
            samples_written += n
            pct = (samples_written / total_samples) * 100
            print(f"\rWriting {filename}: {pct:5.1f}% complete", end="")
    print(f"\nSaved {filename} ({offset:.2f} Hz beat, {duration_min} min)")

def overlay_ambience(
    binaural_file: str,
    ambience_file: str,
    out_file: str = None,
    ambience_gain_db: float = -20.0,
):
    """
    Overlay an external ambience (rainforest, rain, ocean, etc.) under
    a generated binaural WAV.

    ambience_gain_db: negative value lowers ambience volume.
    """
    if out_file is None:
        root, ext = os.path.splitext(binaural_file)
        out_file = f"{root}_mix{ext}"

    print(f"Overlaying ambience '{ambience_file}' → {out_file}")

    tone = AudioSegment.from_wav(binaural_file)
    amb = AudioSegment.from_file(ambience_file)

    # loop ambience to match tone length
    if len(amb) < len(tone):
        amb *= (len(tone) // len(amb) + 1)

    amb = amb[: len(tone)]  # trim excess
    amb = amb - abs(ambience_gain_db)

    mixed = tone.overlay(amb)
    mixed.export(out_file, format="wav")
    print(f"Saved mixed track → {out_file}")

# --------------------------------------------------------------------
# Example playlist (base tone + ambient noise layer)
# --------------------------------------------------------------------
playlist = [
    ("alpha_10hz.wav", 10, 20, "white"),
    ("schumann_7_83hz.wav", 7.83, 25, "pink"),
    ("theta_4hz.wav", 4, 35, "brown"),
    ("delta_1hz.wav", 1, 45, "brown"),
]

if __name__ == "__main__":
    # Step 1 – Generate clean binaural files
    for name, freq, mins, amb in playlist:
        generate_binaural(
            base_freq=200,
            offset=freq,
            duration_min=mins,
            ambient=amb,
            filename=name,
        )

    # Step 2 – Optionally overlay ambience file(s)
    # Replace with the path to your actual ambience (rainforest.mp3, rain.wav, etc.)
    ambience_path = "rainforest.mp3"
    if os.path.exists(ambience_path):
        for name, *_ in playlist:
            overlay_ambience(name, ambience_path)
    else:
        print("\nNo ambience file found; skipped overlay stage.")
