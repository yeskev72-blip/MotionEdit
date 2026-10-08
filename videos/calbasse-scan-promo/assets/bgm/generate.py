"""Generate the music bed for the Calbasse promo with MusicGen, offline.

Adapted from media-use's inline MusicGen recipe (audio/scripts/lib/bgm.mjs),
with one change: torch is seeded, so re-running this reproduces the same take.
The upstream recipe leaves sampling unseeded, which makes a regenerated bed a
different piece of music.

    python3 -I assets/bgm/generate.py

Writes assets/bgm/track.wav at the composition's exact length, so the bed needs
no trimming in the timeline.
"""

import math
import os
import sys
import traceback
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# The product is a calorie scanner for West African plates; the bed should feel
# like the food, not like a SaaS explainer. Instruments named explicitly —
# MusicGen responds to instrument and tempo words far better than to moods.
PROMPT = (
    "warm afrobeat instrumental groove, kalimba and marimba melody over soft "
    "log drum and shaker percussion, 105 bpm, bright and confident, clean "
    "modern production, no vocals"
)

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "track.wav")
TARGET_S = 26.2  # the composition's root data-duration
SEED_S = 26.2  # one seed clip covers it: under the decoder's ~30s limit, so
# there is no crossfade loop and therefore no seam
TOKEN_RATE = 50
TORCH_SEED = 20261008


def apply_fade(arr, sr, fade_in_s=0.9, fade_out_s=1.6):
    """Longer fades than the upstream default: this bed opens under a hook and
    has to clear the end card without a hard stop."""
    n_in = min(int(round(fade_in_s * sr)), arr.shape[0] // 2)
    n_out = min(int(round(fade_out_s * sr)), arr.shape[0] // 2)
    if n_in > 1:
        arr[:n_in] *= np.linspace(0.0, 1.0, n_in, dtype="float32")
    if n_out > 1:
        arr[-n_out:] *= np.linspace(1.0, 0.0, n_out, dtype="float32")
    return arr


def main():
    Path(os.path.dirname(OUT_PATH)).mkdir(parents=True, exist_ok=True)
    torch.manual_seed(TORCH_SEED)

    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    model.eval()

    sr = int(model.config.audio_encoder.sampling_rate)
    gen_s = min(SEED_S, TARGET_S)
    tokens = max(1, int(math.ceil(gen_s * TOKEN_RATE)))
    print(f"[musicgen] seed dur={gen_s:.2f}s tokens={tokens} sr={sr}", flush=True)

    inputs = processor(text=[PROMPT], padding=True, return_tensors="pt")
    with torch.no_grad():
        audio = model.generate(**inputs, max_new_tokens=tokens)

    seed = audio[0, 0].detach().cpu().numpy().astype("float32")
    peak = float(np.max(np.abs(seed)))
    if peak > 1e-6:
        seed = seed * (0.89 / peak)

    want = max(1, int(round(TARGET_S * sr)))
    final = seed[:want].copy() if seed.shape[0] >= want else np.pad(
        seed, (0, want - seed.shape[0])
    )
    final = apply_fade(final, sr)

    peak = float(np.max(np.abs(final)))
    if peak > 1.0:
        final = final / peak

    sf.write(OUT_PATH, final, sr)
    print(f"[musicgen] wrote {OUT_PATH} samples={final.shape[0]} sr={sr}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
