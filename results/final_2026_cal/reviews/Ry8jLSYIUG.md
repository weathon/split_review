Here is the final consolidated review.

---

## Summary

This paper derives geometric upper bounds on image watermarking capacity under PSNR constraints (rigorous) and linear robustness constraints (heuristic), revealing theoretical capacities orders of magnitude larger than what current deep learning models achieve. Controlled experiments strip away real-world complexity — training on a single gray image with only MSE loss — and show Video Seal still fails to embed 1024 bits, while a linear model achieves 2048 bits, tiling achieves 32,768 bits, and a handcrafted construction reaches 456,509 bits. These results point to architectural limitations rather than fundamental constraints. Chunky Seal, a scaled-up Video Seal, demonstrates that 4× capacity (1024 bits) is achievable with comparable robustness and quality, though still far from the theoretical bounds.

## Strengths

- **Novel geometric capacity bounds under PSNR and linear-robustness constraints.** The paper provides a family of bounds (Bounds 1–6, 10–12) grounded in counting lattice points inside the intersection of a PSNR ball and the image cube. For a 256×256 px image at 42 dB, the PSNR-only bound predicts ~600,000 bits — over 2 bpp — while existing methods operate below 0.001 bpp. This is the first systematic geometric analysis of watermarking capacity under realistic, non-Gaussian constraints (Section 2).

- **Controlled experiments isolate architecture as the bottleneck.** By training Video Seal on a single gray image with only MSE loss (no augmentations, no perceptual losses, no dataset), the paper shows the model cannot embed 1024 bits at acceptable PSNR (Table 1, Figure 5 left). A linear embedder/decoder achieves 100% bit accuracy for 2048 bits under identical conditions (Table 1, Figure 5 right). The tiling experiment (32×32 px → 256×256 px yields 32,768 bits) further confirms the problem is structural, not a fundamental limit (Section 3.1–3.2).

- **Handcrafted construction nearly achieves the PSNR-only bound.** Equation (2) gives a closed-form scheme reaching 456,509 bits at 42 dB for a 256×256 px image — within a small factor of the theoretical bound (Table 1, Figure 6). This rules out the concern that the bounds are unachievable (option D), though the scheme requires knowing the cover image (non-blind).

- **Chunky Seal demonstrates practical capacity gains.** Simply scaling Video Seal (embedder 90× larger, extractor 23× larger) yields 1024 bits vs. 256 bits while matching PSNR, SSIM, and robustness across 9 attack types (Table 3). This confirms that 4× capacity is achievable without sacrificing robustness, even if still far from theoretical limits.

- **Conservative lower bounds under robustness.** Bound 13, though extremely conservative, provides rigorous guarantees: e.g., 904 bits remain viable even under 75% cropping at 42 dB (Table 2). This shows that even worst-case analysis leaves room beyond current models.

## Weaknesses

### Major

- **The central quantitative claim about "orders of magnitude" gap under robustness rests on unvalidated heuristic bounds.** The paper's headline claim (Figure 1, abstract) relies on Bounds 10–12, which the paper explicitly says are "not valid lower bounds" and only heuristic (Section 2.5: "we believe that despite Bounds 10 to 12 not being valid lower bounds, they are much closer to the true capacity"). This belief is not empirically validated against any practical system. The only rigorous bound (Bound 13) is acknowledged as "extremely conservative and unrealistic" and gives much smaller gaps: for 75% cropping at 42 dB, only 904 bits — a gap that Chunky Seal's 1024 bits already closes. The paper's strongest claim (orders-of-magnitude under realistic robustness) therefore rests on heuristic estimates whose accuracy is untested. The authors acknowledge this limitation in Section 5, but it directly affects the paper's main contribution.

- **The handcrafted model is non-blind, limiting its relevance to the practical blind-watermarking setting.** The handcrafted scheme (Equation 2) embeds a message as a grid point in the PSNR ball and extracts by subtracting the known cover to recover the grid index. This requires the cover image at the decoder. While the paper scopes this experiment to "the solid gray image case with PSNR constraint and no robustness requirements" and uses it only to rule out option D (bounds unachievable), the schematic in Figure 1 and the abstract's phrasing ("orders of magnitude larger than what current models achieve") invite readers to interpret the handcrafted capacity as achievable in the same blind setting where Video Seal and Chunky Seal operate. The linear model (blind) reaches 2,048 bits — respectable but still two orders of magnitude below the bound — so the strongest empirical bridge to the theoretical bound is non-blind. The paper should state this limitation more prominently when presenting the handcrafted results.

### Minor

- **The controlled experiment only tests one learned architecture (Video Seal).** The paper attributes Video Seal's failure to "severe structural limitations," which is supported by the linear model and tiling succeeding under identical conditions. However, testing additional architectures (e.g., HiDDeN, TrustMark) in the same simplified setup would strengthen the claim that the limitation is generic across learned architectures rather than specific to Video Seal's design. As-is, the evidence is suggestive but not definitive.

- **Variance/statistical significance is not reported for the main simplified experiments.** Table 1 and Figure 5 report "best-performing runs" from hyperparameter sweeps. While Figure 5 shows multiple runs per setting, numerical variation across seeds is not quantified. Mean and standard deviation across seeds for the key metrics (bit accuracy, PSNR) would improve reliability assessment.

- **The "orders of magnitude" claim in the abstract conflates the PSNR-only and robustness settings.** The PSNR-only bound (rigorous) genuinely shows ~2500× gap at 45 dB. Under robustness, the gap depends on unvalidated heuristic bounds. The abstract should disambiguate which setting the headline figure refers to.

- **Chunky Seal's LPIPS increases 4.5× (0.0019 → 0.0085).** While the absolute values are low, the paper's phrasing "maintains nearly identical image quality… and only slightly higher LPIPS" downplays a non-trivial relative increase. The 1B parameter model also raises practical concerns about training cost and inference speed that are not discussed.

### Trivial

- The VQ-VAE estimate of data distribution effects (Section 2.6) is loose but the paper acknowledges it as an upper bound.
- The hyperparameter sweep for the gray-image experiment tests only 3 learning rates and 3 λᵢ values; coverage is adequate for a pilot study but not exhaustive.

## Nice-to-Haves

- Validate the heuristic robustness bounds (Bounds 10–12) against a simple practical system (e.g., spread-spectrum in a transformed domain) to establish whether they overestimate capacity by a small or large margin.
- Compare Chunky Seal's capacity against the conservative Bound 13 for the same distortion types, to see how close scaling already gets.
- Provide training time, GPU hours, and inference speed for Chunky Seal to assess practicality.

## Removed Points

*(These points were raised by reviewers but removed per the review guidelines. They are presented here for transparency only and should not factor into the assessment.)*

- **Reproducibility concerns about undisclosed hyperparameters or unavailable code** — removed because the paper states code and checkpoints will be released (footnote 1) and hyperparameters are adequately specified.
- **Criticism that the handcrafted model "invalidates the relevance to the blind watermarking problem"** — removed in severity (downgraded from fatal to Major) because the paper carefully scopes the handcrafted experiment to ruling out option D, not to showing blind achievability. The paper's argument structure is: (1) bounds → (2) models underperform → (3) simplified setup same result → (4) handcrafted/linear/tiling succeed → (5) therefore architecture is the bottleneck. The handcrafted model serves step (4) appropriately.
- **Request for missing related works** — removed because I cannot verify the existence of suggested references.
- **Formatting/style nitpicks and typo claims** — removed as parser artifacts.
- **"Missing proofs in appendix"** — removed because the parser strips appendix content.
- **Claim that the paper "overstates the conclusiveness" of the data-distribution analysis** — removed as the paper explicitly calls it an estimate.

## Novel Insights

None beyond the paper's own contributions. The key insight — that geometric lattice counting yields watermarking capacity bounds and reveals current architectures as the bottleneck — is well articulated in the paper itself.

## Suggestions

1. In the abstract and introduction, separate the "orders of magnitude" claim into two clear statements: one for the rigorous PSNR-only bound and one for the heuristic robustness bounds (with appropriate qualification).
2. Validate the heuristic robustness bounds experimentally using a handcrafted or linear system in the transformed domain (e.g., DCT spread-spectrum under cropping) to measure whether the heuristic is approximately tight or substantially overestimating.
3. Test at least one additional architecture (HiDDeN, TrustMark) in the single-gray-image setup to strengthen the claim that the capacity bottleneck is architectural and not specific to Video Seal.
4. Report mean and standard deviation across multiple seeds for the simplified experiments in Table 1.
5. Add a comparison between Chunky Seal's capacity and the conservative Bound 13 to clarify how large the remaining gap really is for different distortions.

## Calibration

**Round 1 bracket:** The paper sits between the weak anchor band (papers scoring ~3, which are withdrawn/rejected for methodological weaknesses) and the strong anchor band (papers scoring 8, which set new standards in their subfield). Initial bracket: **4.5 – 7.0**.

**Round 2 narrowing:** Compared against mid-band anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| *Watermark-based Attribution* (syOYjXqKnS) | 4.67 | R1 | Weaker: narrower scope, less novel theory. This paper has stronger theoretical contribution. |
| *Self-Re-Watermarking* (st1hrLTP14) | 6.00 | R1,R2 | Similar: both have clear novel contributions and honest limitations. SRW has cleaner empirical validation; this paper has stronger theory. |
| *PAI Watermarking* (wyucYNGPiW) | 6.50 | R2 | Slightly stronger: more comprehensive experiments and clearer practical impact. |
| *SynthID-Text Analysis* (4AfWqR3quK) | 5.50 | R1,R2 | Similar mixed reception. This paper has broader scope and more novel theory. |
| *LatentSeal* (TVSPV6D0co) | 4.67 | R2 | Weaker: less theoretical depth. |
| *SIGMark* (tKyAD2LhnI) | 5.33 | R2 | Comparable scope but less theoretical contribution. |

**Final score:** 6.0. The paper makes a genuinely novel theoretical contribution (geometric capacity bounds for image watermarking under PSNR), supported by well-designed controlled experiments. The weaknesses — unvalidated heuristic robustness bounds and the non-blind handcrafted comparison — are real but acknowledged, and do not invalidate the core PSNR-only findings nor the architectural-bottleneck hypothesis. It is stronger than the 4.67–5.33 anchors and comparable to the 6.0 anchor; it falls slightly below the 6.5 anchor, which had more comprehensive empirical validation.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>