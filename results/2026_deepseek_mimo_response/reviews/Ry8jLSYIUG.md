Now let me write the final review and score based on these comparisons.

My bracket from Round 1: between 6.0 and 7.0.

Round 2 anchors narrowed this to around 6.0-7.0:
- "Undetectable watermark" (6.50): Accepted, provides cryptographic undetectability guarantees — this paper provides different but comparable theoretical contributions
- "Lightweight Deep Watermarking" (7.60): Rejected at 7.60, solves a narrower problem (loss mismatch) — this paper's question is broader but the practical contribution is more modest
- "WIND" (5.83): Accepted, two-stage framework — this paper is clearly stronger

The paper is clearly above the 5.5-6.0 watermarking papers (incremental methods), and comparable to the "Undetectable Watermark" paper (6.50). Both have strong theoretical components and practical demonstrations. The "Undetectable Watermark" achieves clean guarantees in a narrower setting; this paper addresses a broader and arguably more fundamental question but with heuristic robustness bounds and a modest 4× practical improvement. The paper falls slightly below the "Lightweight Deep Watermarking" (7.60) paper that had more unanimous high ratings and a cleaner practical contribution.

**Score: 6.5** — comparable to the undetectable watermark paper; strong theoretical framing with practical results, but bounded by the modest practical improvement and heuristic robustness analysis.

---

## Summary
This paper derives geometric upper bounds on image watermarking capacity under PSNR and robustness constraints, demonstrating that theoretical capacity (~2 bpp at 40 dB) is orders of magnitude higher than what current models achieve (~0.001 bpp). Through controlled experiments on a simplified gray-image setting, the authors show Video Seal has structural architectural limitations (a linear model embeds 2048 bits where Video Seal fails at 1024), and a handcrafted embedder achieves 456,509 bits near the theoretical bounds. They train Chunky Seal, a scaled-up Video Seal achieving 1024-bit capacity (4× over Video Seal's 256 bits) with comparable quality and robustness on real images.

## Strengths
- **Well-structured theoretical framework (Bounds 1–13)** covering distinct PSNR regimes and robustness conditions. The geometric approach—counting integer lattice points in the intersection of PSNR ℓ₂-balls with the pixel-value cube—is cleanly motivated, with Equation (1) connecting PSNR to ℓ₂ distance and Figures 3–4 visualizing bounds across parameter ranges. The paper is transparent about validity conditions for each bound.
- **Systematic elimination of alternative hypotheses (A–E)**: Five hypotheses for the theory-practice gap are enumerated (Section 3, lines 176–184) and systematically ruled out. Training Video Seal on a single gray image rules out A, B, C (Section 3.1, Table 1); the handcrafted model achieving 456,509 bits at 42 dB rules out D (Equation 2). This chain of reasoning is rigorous and well-designed.
- **Linear model outperforming SOTA architecture**: A single linear layer achieves 100% bit accuracy for 2048 bits at 40.40 dB PSNR (Table 1, Figure 5 right), while Video Seal fails at 1024 bits on the identical task. This is a striking demonstration that the bottleneck is architectural, not fundamental.
- **Handcrafted embedder nearly matching theoretical bounds**: The scheme in Equation (2) achieves 456,509 bits at 42 dB on 256×256 images with 100% accuracy (Table 1), proving the geometric bounds are nearly achievable and eliminating the concern that they are vacuously loose.
- **Resolution-blindness discovery**: Video Seal achieves nearly identical performance at 32×32 and 256×256 resolution (Table 1: 512 bits at 41.66 dB vs. 51.45 dB), revealing the architecture cannot exploit additional spatial degrees of freedom—a novel and actionable diagnostic.
- **Tiling strategy**: Independently watermarking 64 tiles of a 256×256 image achieves 32,768 bits at the same PSNR (Section 3.2), demonstrating a 64× capacity increase with a simple modification.
- **Proposed sanity checks for the field** (Section 5): Concrete, testable criteria—capacity scaling linearly with image size, predictable degradation under stronger augmentations, outperforming simple baselines—providing practical evaluation methodology for the community.

## Weaknesses

### Fatal
None

### Major
- **Heuristic robustness bounds weaken the core claim for aggressive augmentations**: The paper's key claim that robustness cannot explain the low capacity of current models rests on Bounds 10–12 (Section 2.5), which the authors acknowledge are not proven lower bounds: "We can show cases where these heuristic bounds under-approximate and cases where they over-approximate the true capacity." The only rigorous lower bound (Bound 13) is "extremely conservative and unrealistic." For Crop&Rescale 75%, Bound 13 gives 904 bits at 256×256px (Table 2), while Chunky Seal achieves 1024 bits at 98.25% bit accuracy—but without error correction, ~8–9 bits are wrong per message, so effective reliable capacity may be below the conservative bound. The paper would be substantially strengthened by an empirical measurement of the handcrafted model's capacity under specific robustness constraints.

- **The gap between orders-of-magnitude theory and 4× practice**: The narrative progresses from "orders of magnitude gap" in theory (~2 bpp vs. ~0.001 bpp) to "4× improvement" in practice (Chunky Seal: 1024 vs. 256 bits). The simplified gray-image experiments convincingly demonstrate architectural limitations, but the practical result is more modest. The transition between Section 3's simplified experiments and Section 4's practical model should be more explicitly discussed rather than letting the theoretical framing dominate.

### Minor
- **No discussion of error correction impact on effective capacity**: At 99.15% overall bit accuracy on 1024 bits, approximately 8–9 bits are wrong per message. Any practical deployment needs ECC, reducing effective payload. The paper would benefit from discussing this or reporting effective capacity after ECC.

- **Scale-up costs underplayed**: The embedder is ~93× larger and extractor ~23× larger for 4× capacity. While the paper acknowledges this, the quality/robustness tradeoffs (LPIPS 0.0085 vs. 0.0019, identity bit accuracy 99.74% vs. 99.90%) are somewhat underplayed by the "comparable quality and robustness" framing.

### Trivial
None

## Nice-to-Haves
- An empirical capacity measurement under robustness constraints (e.g., training the handcrafted model under PSNR + crop constraints) to validate Bounds 10–12.
- Characterizing how the gray-image gap transfers when minimal augmentations are added to the linear model.
- Reporting effective capacity after error correction for Chunky Seal.
- More complete training details for Chunky Seal (dataset, epochs, augmentation schedule, loss weights) for reproducibility.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's "missing comparison to recent high-capacity or ECC-integrated methods" — the paper compares to HiDDeN, TrustMark, WAM, MiRRE, etc. (Figure 1); whether any use ECC is a nice-to-have discussion, not a missing baseline.
- Missing appendix concerns — parser artifact.
- Criticisms about hyperparameter sweep completeness (Table 1 shows "best-performing runs") — this is standard practice and the supplementary likely contains full sweeps.

## Novel Insights
The resolution-blindness finding—that Video Seal achieves nearly identical capacity at 32×32 and 256×256 resolution—is a genuinely novel architectural diagnostic revealing that the model cannot exploit spatial degrees of freedom. Combined with the linear model's success, this provides a clear, actionable signal about where architectural innovation is needed. The proposed sanity checks for watermarking evaluation methodology (capacity scaling with image size, predictable degradation under augmentations, outperforming simple baselines) are also a novel and practical contribution to how the field evaluates progress.

## Suggestions
- Add an empirical capacity measurement under robustness constraints to strengthen the Bounds 10–12 claims.
- Discuss error correction impact on effective payload for Chunky Seal.
- Make the transition from theoretical gap to practical improvement more explicit—perhaps a paragraph in Section 4 directly addressing why only 4× is achieved when the theoretical gap is orders of magnitude.

---

## Calibration Report

### Anchors Retrieved

**Round 1:**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| Z1E0EahS5w.md (Limits to Reservoir Learning) | 3.33 | Weak | Different topic; this paper is much stronger |
| S3zKrEQpRr.md (GNN as noisy channels) | 3.00 | Weak | Different topic; this paper is much stronger |
| 6j0GH40mFt.md (Image compression) | 3.40 | Weak | Incremental; this paper is much stronger |
| jbfDg4DgAk.md (Sparse Watermark LLMs) | 3.00 | Weak | Incremental LLM watermarking; this paper is much stronger |
| T0ebbDO60R.md (SuperMark) | 3.75 | Weak/Mid | Training-free watermarking, limited novelty; this paper is stronger |
| ETFfXGM3e4.md (SAT-LDM) | 5.50 | Mid | Incremental watermarking for LDMs; this paper is clearly stronger |
| HexshmBu0P.md (Recipe for Watermarking DMs) | 5.33 | Mid | Empirical recipe; this paper is substantially stronger |
| PCm1oT8pZI.md (Safe OoD Watermark) | 5.75 | Mid | Model watermarking; different domain but this paper is stronger |
| j7b4mm7Ec9.md (Lightweight Watermarking) | 7.60 | Strong | Identifies key loss mismatch, clean practical contribution; comparable novelty but this paper has broader ambition |
| CxXGvKRDnL.md (Progressive Compression) | 8.00 | Strong | Novel compression method; this paper is slightly below this level |
| uAFHCZRmXk.md (Modality Gap VLMs) | 8.00 | Strong | Analysis paper in different domain; comparable analytical depth |
| Tzh6xAJSll.md (Scaling Laws Memories) | 7.60 | Strong | Theory paper; this paper is below this level of rigor |

**Round 2:**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| jlhBFm7T2J.md (Undetectable Watermark) | 6.50 | Mid-Strong | First undetectable scheme with crypto guarantees; comparable theoretical contribution |
| hzxvMqYYMA.md (BIQA Generalization) | 5.75 | Mid | Different topic; this paper is stronger |
| ll2nz6qwRG.md (WIND Two-Stage) | 5.83 | Mid | Watermarking framework; this paper is clearly stronger |
| UchRjcf4z7.md (Transfer Attack) | 6.50 | Mid-Strong | Attack paper with theory; this paper has complementary strength |
| mDKxlfraAn.md (Removable Watermarks) | 6.40 | Mid-Strong | Watermark removal; this paper's contribution is broader |

### Bracket Narrowing
- **Round 1 bracket**: 6.0–7.0. The paper is clearly above the 5.3–5.8 incremental watermarking papers, and slightly below the 7.6 "Lightweight Watermarking" that had all-8 reviews.
- **Round 2 narrowing**: 6.0–7.0. The "Undetectable Watermark" (6.50) is the closest comparison—a strong theoretical contribution with practical demonstrations in watermarking. Both provide novel theoretical framing, but the "Undetectable Watermark" achieves cleaner guarantees in its setting. This paper addresses a broader and more fundamental question but with a more modest practical result (4× improvement).
- **Final score**: 6.5. Comparable to the "Undetectable Watermark" (6.50). Strong theoretical contribution, carefully controlled experiments, actionable insights, but bounded by heuristic robustness bounds and a modest practical improvement gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <score>Accept</score>