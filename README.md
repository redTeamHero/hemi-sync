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

📖 Appendix: Background & Theory

🔹 1.  Origins — Robert Monroe & the Gateway Studies

Beginning in the late 1950s, Robert A. Monroe (founder of The Monroe Institute) experimented with using stereo tones to help people reach deep-relaxation states.
He discovered that playing slightly different frequencies in each ear (for example 200 Hz left / 208 Hz right) produced a perceived rhythmic pulse equal to the difference (8 Hz).
He called this method Hemi-Sync®, short for Hemispheric Synchronization.

In the 1970s–80s Monroe’s team produced a structured audio program called The Gateway Experience.
It combined:
	•	precisely tuned binaural-beat pairs,
	•	gentle pink or brown noise backgrounds,
	•	and guided-relaxation voice scripts.

The goal was to teach users to relax the body while maintaining alert awareness, exploring how balanced brain-hemisphere activity might support focus, creativity, and deep meditative states.
A 1983 U.S. Army report later summarized these sessions under the term “Gateway Process.”

⸻

🔹 2.  Scientific Principle

Both Monroe’s recordings and this Python generator rely on the same physiological idea:

Component	Purpose
Left / Right tones	Deliver slightly different carrier frequencies to each ear.
Perceived beat	Brainstem auditory circuits detect the frequency difference, producing an internal “beat” pattern.
Neural entrainment	Repetitive stimulation can encourage certain EEG frequency bands (alpha ≈ 8–12 Hz, theta ≈ 4–8 Hz, delta ≈ 0.5–4 Hz) associated with relaxation, focus, or sleep.

Research using electroencephalography (EEG) has shown modest entrainment effects: the brain’s electrical activity can align transiently with the beat frequency, improving attention, relaxation, or sleep onset in some listeners.
Results vary widely between individuals; effects are gentle rather than dramatic.

⸻

🔹 3.  Relationship to This Project

Your script implements the core acoustic principle—stereo sine-wave generation with adjustable beat offsets—without Monroe’s proprietary voice tracks or metaphysical framing.
It is therefore:
	•	Educational: demonstrates the physics of auditory beats.
	•	Safe: no subliminal or hypnotic messaging.
	•	Customizable: you select the offset (e.g., 4 Hz for theta) and ambient style (white/pink/brown noise).

In other words, it provides the laboratory tone bed upon which guided-relaxation or learning scripts can be layered.

⸻

🔹 4.  Modern Research Context

Recent peer-reviewed findings include:
	•	Padmanabhan et al., 2005 – Anesth Analg 101(3): 675-7.
→ 4 Hz binaural beats modestly reduced pre-operative anxiety.
	•	Beauchene et al., 2016 – Front Hum Neurosci 10: 170.
→ Gamma-range beats enhanced selective attention in cognitive tasks.
	•	Jirakittayakorn & Wongsawat, 2017 – Front Hum Neurosci 11: 365.
→ Theta beats increased frontal-midline theta power linked to meditative focus.

These studies support binaural-beat entrainment as a gentle adjunct for relaxation or concentration, not as a therapeutic or paranormal tool.

⸻

🔹 5.  Ethical & Practical Scope
	•	Always present recordings as transparent and optional, never as hidden or “subliminal.”
	•	Keep listening sessions under about 45 minutes to avoid auditory fatigue.
	•	Use at comfortable volume and only when it’s safe to close your eyes and relax.
	•	Treat this as mind-gym equipment, not as medical treatment or consciousness manipulation.

⸻

 Appendix B – Integrating Binaural Entrainment with Mind-Palace Training

🔹 1. Overview

This project can be paired with the classical Method of Loci—often called a mind palace—to build stronger memory and focus skills.
The combination follows a simple logic:

Technique	Function	Synergy
Binaural entrainment	Uses two slightly different tones in each ear to nudge brain activity toward a relaxed, rhythmic state (alpha ≈ 10 Hz or theta ≈ 7–8 Hz).	Creates a calm, imagery-friendly mental environment.
Mind palace visualization	Stores information by linking it to vivid locations in a familiar spatial map.	Supplies structured imagery to fill that receptive mental state.

Together they support state-dependent learning—information encoded in a calm, focused rhythm is easier to recall later when you return to that same rhythm.

⸻

🔹 2. Suggested Session Flow
	1.	Preparation (Alpha ≈ 10 Hz):
	•	Listen 2–3 min to an alpha track.
	•	Slow your breathing, release tension.
	2.	Encoding (Theta ≈ 7.83 Hz):
	•	Switch to a theta track.
	•	Walk through your chosen mental space—a house, school, or landscape.
	•	At each landmark, place one idea or fact as a vivid image.
	3.	Consolidation:
	•	Stop the sound.
	•	Mentally retrace the route, recalling each stored item aloud or in writing.
	4.	Reinforcement:
	•	Revisit the same path in later sessions while playing a short alpha track to refresh recall.

⸻

🔹 3. Neuroscience Background
	•	Theta (4–8 Hz) rhythms dominate during deep focus, meditation, and hippocampal memory consolidation.
	•	Spatial imagery activates parietal and hippocampal networks—the same regions modulated by theta activity.
	•	Aligning rhythmic relaxation with spatial visualization strengthens encoding and retrieval.

⸻

🔹 4. Practical Setup

Element	Recommendation
Tone generation	Use binaural_playlist_generator.py with offset=7.83, ambient='pink', 25 min
Ambience	Optional jungle or rain layer (–20 dB)
Headphones	Stereo; comfortable, low volume
Session length	25–30 min; do not exceed ≈45 min
Best time	Early morning or evening quiet hours


⸻

🔹 5. Example Self-Guided Script

“As the gentle tone pulses, imagine walking through your mind-palace.
At the first doorway, place the concept you wish to remember.
With each beat, move to the next room, linking each idea to a clear image.
When the tone fades, retrace your steps and recall every detail.”

Record your own narration or use a preset TTS voice, then mix it over your 7.83 Hz track with pydub or Audacity.

⸻

🔹 6. Ethical and Safety Guidelines
	•	This integration is for education, study, and creative focus, not therapy or hypnosis.
	•	Keep all voice suggestions explicit and audible—never “subliminal.”
	•	Use at safe listening levels and only when you can sit or lie quietly.
	•	Stop immediately if you feel dizzy, overstimulated, or drowsy.
	•	Respect the intellectual property of Monroe Institute and other creators; this project demonstrates open-source educational principles only.

⸻

🔹 7. Summary

By pairing gentle rhythmic entrainment with structured mental imagery, you create a practical cognitive-training tool:
	•	Relax the mind → open the memory channels
	•	Visualize → encode deeply
	•	Revisit calmly → recall easily

The result is a clear, ethical, research-inspired approach to focused learning and mindset development.

⸻

📄  License

MIT License (for code).
All generated audio is your property to use in personal or educational projects.

⸻

