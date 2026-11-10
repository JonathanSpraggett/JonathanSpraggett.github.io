#!/usr/bin/env python3
"""Irreversibly redact unpublished research from the public short CV PDF."""
from pathlib import Path
import fitz
import shutil
import sys

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
doc = fitz.open(src)
before = "\n".join(p.get_text() for p in doc)
if "VFS 2027" not in before:
    doc.close()
    shutil.copy2(src, dst)
    print("Public CV already sanitized.")
    sys.exit(0)
if len(doc) < 2:
    raise ValueError("Unexpected CV structure; review redaction coordinates.")

p = doc[0]
p.add_redact_annot(fitz.Rect(88.4, 449.3, 535, 490.4), fill=(1, 1, 1))
p.apply_redactions(images=0, graphics=0, text=0)
lines = [
    "• Developed flight-deck and telemetry tools for real-time aircraft monitoring, preflight",
    "   safety checks, command interfaces and postflight data analysis, enabling repeatable",
    "   validation of autonomy and flight-control systems.",
]
for i, line in enumerate(lines):
    p.insert_text((89 if i == 0 else 98, 460.7 + 13.55 * i), line,
                  fontsize=10.8, fontname="tiro", color=(0, 0, 0))

p = doc[1]
p.add_redact_annot(fitz.Rect(75.8, 512, 533.5, 653.1), fill=(1, 1, 1))
p.apply_redactions(images=0, graphics=0, text=0)
entries = [
    ("Flight-Validated Digital Filtering for Vibration Mitigation on a 250 kg eVTOL",
     "J. Spraggett, N. Pourmostaghim, Y. Sadat-Nejad", "AIAA SciTech 2026"),
    ("Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy",
     "J. Spraggett", "RoboCup Symposium 2025"),
    ("Sim2Real Reinforcement Learning for Soccer Skills",
     "J. Spraggett", "BASc Thesis, University of Toronto, 2023"),
]
for j, entry in enumerate(entries):
    y = 523.5 + 48.95 * j
    for k, line in enumerate(entry):
        x = 76.5 if k == 0 else 98.1
        size = 10.6 if k == 0 else 10.4
        measured = fitz.get_text_length(line, fontname="tiro", fontsize=size)
        if measured > 510 - x:
            size *= (510 - x) / measured * 0.98
        p.insert_text((x, y + 13.5 * k), line, fontsize=size,
                      fontname="tiro", color=(0, 0, 0))
dst.parent.mkdir(parents=True, exist_ok=True)
doc.save(dst, garbage=4, deflate=True, clean=True)
doc.close()
check = fitz.open(dst)
after = "\n".join(p.get_text() for p in check)
for forbidden in ("VFS 2027", "Payload-Aware Model Predictive Control for a Heavy-Lift", "28.4% to 15.2%", "4.3±1.3%"):
    if forbidden in after:
        raise ValueError("Confidential content remains: " + forbidden)
print("Public CV sanitized:", dst)
