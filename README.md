🎧 binaural_playlist_generator.py

Generate educational binaural-beat tracks for relaxation, focus, meditation, or study.
This script creates stereo audio files that blend gentle tones and optional ambient noise (white, pink, or brown).
Use it to explore how different frequency offsets affect mood and concentration — safely and consciously.

⸻

🧠 What It Does

The script builds stereo WAV files where:
	•	Left ear → base frequency (e.g., 200 Hz)
	•	Right ear → base + offset (e.g., +7.83 Hz)

Your brain perceives the small difference as a rhythmic “beat.”
Different offsets correspond to commonly studied brain-wave ranges:

Mode	Offset (Hz)	Typical Effect *
Alpha	10 Hz	relaxed focus
Schumann / low Alpha	7.83 Hz	calm awareness
Theta	4 Hz	creative flow / meditative
Delta	1 Hz	deep rest / sleep

*Educational use only — not a medical claim.

⸻

⚙️ Requirements

pip install numpy scipy soundfile

Optional (for mixing your voice or jungle ambience):

pip install pydub


⸻

▶️  Quick Start

python3 binaural_playlist_generator.py

This generates four tracks in the same folder:

alpha_10hz.wav
schumann_7_83hz.wav
theta_4hz.wav
delta_1hz.wav

🎧 Listen with stereo headphones at a comfortable, low volume.
Sessions of 20–45 minutes are plenty.

⸻

🎚️  Customize Your Own Tracks

Edit the playlist near the bottom:

playlist = [
    ("focus_12hz.wav", 12, 15, 'white'),
    ("meditation_6hz.wav", 6, 30, 'pink')
]

or call the generator directly:

generate_binaural(base_freq=220, offset=8, duration_min=10,
                  ambient='pink', filename='custom_alpha.wav')

Parameter	Description
base_freq	Base tone for the left channel (Hz)
offset	Difference for right channel (Hz)
duration_min	Track length in minutes
fs	Sample rate (default 44 100 Hz)
ambient	'white', 'pink', 'brown', or 'none'
filename	Output WAV file name


⸻

🌿  Add Voice or Jungle Background Automatically

You can overlay narration (your recorded affirmations) or ambience (rainforest, rain, etc.) using pydub.

Example Mixer Script

from pydub import AudioSegment

# load generated binaural tone
binaural = AudioSegment.from_wav("theta_4hz.wav")

# load background audio (MP3 or WAV)
# e.g., your voice track or jungle ambience
background = AudioSegment.from_file("jungle_ambience.mp3")

# extend / loop background to match
if len(background) < len(binaural):
    background = background * (len(binaural) // len(background) + 1)

# mix: lower background volume so tones remain audible
mixed = binaural.overlay(background - 20)
mixed.export("theta_4hz_jungle_mix.wav", format="wav")

print("Saved theta_4hz_jungle_mix.wav")

Tips
	•	Voice track ≈ –12 dB, ambience ≈ –20 dB below tone.
	•	Use Audacity for fine volume balancing and fade-ins.
	•	Keep total loudness comfortable; subtle is better.

⸻

🌈  Ambient Choices

Type	Character	Sounds Like
White	even energy across spectrum	steady hiss
Pink	more low-end energy	rainfall
Brown	deep, rumbling bass	ocean surf / earthy


⸻

🧩  Safety & Ethics
	•	This project is for education and relaxation, not therapy or treatment.
	•	Keep volumes low to avoid ear fatigue.
	•	People with epilepsy or auditory sensitivity should consult a clinician first.
	•	Never use while driving or operating machinery.
	•	Do not embed hidden or subliminal content; all suggestions should be fully audible and transparent.

⸻

🪶  Example Workflow
	1.	Generate base tones with this script.
	2.	Mix with jungle ambience or your own spoken guidance.
	3.	Export final track (.wav or .mp3).
	4.	Listen during study, meditation, or creative work.

⸻

📄  License

MIT License (for code).
All generated audio is your property to use in personal or educational projects.

⸻

