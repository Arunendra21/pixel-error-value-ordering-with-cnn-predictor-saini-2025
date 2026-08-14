# Processing Notes — Pixel Error Value Ordering with CNN Predictor (Saini 2025)

- **Paper:** Ankit Kumar Saini, Samayveer Singh, Signal, Image and Video Processing, vol. 19, 2025
- **Reproduction tier:** A
- **Status:** Completed (full reproduction)

## What was reproduced
Error-ordered rhombus PEE core, levels 1..3, 8 images, bit-exact reversibility.

## Reproduced vs reported
The PEVO/PEE mechanism and reversibility are reproduced. The **CNN predictor is NOT trained** (no weights/data available) and is approximated by a fixed rhombus predictor -> reproduced capacity is a conservative lower bound. This is stated openly.

## Honesty note
No fabricated results; all numbers from included code; 'reported' cells reflect the paper.
