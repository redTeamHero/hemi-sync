#!/usr/bin/env python3
"""
binaural_generator_v2.py
------------------------

Generate educational binaural-beat audio tracks safely and efficiently.
This rewrite creates the file in small chunks so it won’t run out of RAM
even on long sessions (30–60 min).

Requirements:
    pip install numpy soundfile
"""

import numpy as np
import soundfile as sf

def generate_binaural(
    base_freq: float = 200.0,
    offset: float = 7.83,
    duration_min: float = 5.0,
    fs: int = 44100,
    ambient: str = "none",
    filename: str = "output.wav",
    chunk_seconds: int = 10
):
    """
    Create a stereo WAV file containing a binaural-beat tone.

    Parameters
    ----------
    base_freq : float
        Left-ear carrier frequency in Hz.
    offset : float
        Frequency difference for right ear in Hz.
    duration_min : float
        Length of track in minutes.
    fs : int
        Sample rate in samples per second.
    ambient : str
        'white', 'pink', 'brown', or 'none' for optional noise bed.
    filename : str
        Output file name.
    chunk_seconds : int
        How many seconds of audio to process at once (reduces RAM use).
    """

    total_samples = int(duration_min * 60 * fs)
    chunk_size = chunk_seconds * fs

    # Open the output file for streaming writes
    with sf.SoundFile(filename, mode="w", samplerate=fs, channels=2) as f:
        samples_written = 0
        while samples_written < total_samples:
            # Determine time array for this chunk
            current_chunk = min(chunk_size, total_samples - samples_written)
            t = np.arange(current_chunk) / fs

            # Carrier tones
            left = np.sin(2 * np.pi * base_freq * t)
            right = np.sin(2 * np.pi * (base_freq + offset) * t)

            # Optional ambient noise
            if ambient != "none":
                noise = np.random.normal(0, 1, current_chunk)
                if ambient == "pink":
                    noise = np.cumsum(noise)
                elif ambient == "brown":
                    noise = np.cumsum(np.cumsum(noise))
                noise = noise / np.max(np.abs(noise))
                noise *= 0.2
                left += noise
                right += noise

            # Normalize and interleave stereo
            stereo = np.vstack((left, right)).T
            stereo /= np.max(np.abs(stereo) + 1e-9)

            # Write chunk to disk
            f.write(stereo)
            samples_written += current_chunk

            # Optional progress display
            pct = (samples_written / total_samples) * 100
            print(f"\rWriting {filename}: {pct:5.1f}% complete", end="")

    print(f"\nSaved {filename} ({offset:.2f} Hz beat, {duration_min} min)")


# Example playlist
playlist = [
    ("alpha_10hz.wav", 10, 20, "white"),
    ("schumann_7_83hz.wav", 7.83, 25, "pink"),
    ("theta_4hz.wav", 4, 35, "brown"),
    ("delta_1hz.wav", 1, 45, "brown"),
]

if __name__ == "__main__":
    for name, freq, mins, amb in playlist:
        generate_binaural(
            base_freq=200,
            offset=freq,
            duration_min=mins,
            ambient=amb,
            filename=name,
        )
