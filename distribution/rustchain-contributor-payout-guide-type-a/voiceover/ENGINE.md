# Voiceover engine

The WAV narration files in this package are generated from the adjacent `.txt` files with **eSpeak** on the GitHub-hosted Ubuntu runner.

Settings used by `build_assets.py`:
- voice: `en-gb`
- speed: 150 words/minute
- output: uncompressed WAV, one file per section

Rebuild:

```bash
sudo apt-get update
sudo apt-get install -y espeak
python -m pip install pillow
python build_assets.py
```

The voiceover source text is versioned so the audio can be regenerated deterministically enough for editorial use. No cloned or impersonated human voice is used.
