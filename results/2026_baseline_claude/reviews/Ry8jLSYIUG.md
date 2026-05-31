Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

This paper investigates the fundamental gap between the theoretical message-carrying capacity of images and the capacity achieved by current deep-learning-based watermarking models. The authors derive a family of upper bounds on watermarking capacity under PSNR and linear robustness constraints via a geometric (lattice-counting) approach, showing theoretical capacities are orders of magnitude above current practice. They then run controlled experiments demonstrating that the gap is not explained by real-world complexity (robustness, perceptual constraints, or data distribution) but by structural limitations of current architectures—a point reinforced by linear and handcrafted embedders that far outperform VideoSeal in simplified settings. Finally, they introduce Chunky Seal, a scaled-up VideoSeal that achieves 1024 bits (4× VideoSeal) with comparable quality and robustness.

---

## Strengths

- **Rigorous, layered theoretical analysis:** The paper derives ten-plus bounds under a systematic progression of scenarios—absolute capacity → PSNR-only (central vs. arbitrary cover) → linear robustness constraints. The geometry (ball-in-cube / cube-in-ball / partial overlap) is handled carefully, including both volume approximations and exact lattice counting via the Mitchell (1966) algorithm. The "at most 1 bpp penalty for arbitrary images" result (Section 2.4) is clean and useful.

- **Structured elimination of alternative hypotheses:** Section 3 is particularly well-structured. The authors propose five candidate explanations for the theory-practice gap, then systematically rule out A, B, C (real-world complexity) and D (bounds being wrong) via concrete experiments: retraining VideoSeal on a single gray image with no augmentations (still fails at 1024 bits), switching to a linear embedder/extractor that succeeds at 2048 bits, tiling 32×32 models to get 32,768 bits, and a handcrafted model reaching 456,509 bits at 42 dB. This chain of evidence is compelling.

- **Chunky Seal as practical proof-of-concept:** Achieves 1024-bit capacity vs. VideoSeal's 256 bits with nearly identical PSNR, SSIM, MS-SSIM, and per-attack bit accuracy. Doing this through simple scaling—without any hyperparameter tuning specifically for the 1024-bit target—is a strong signal that much more room exists.

- **Actionable sanity checks for the community (Section 5):** The proposed sanity checks (capacity scales linearly with image size, decreases linearly with PSNR, exceeds linear/handcrafted baselines, shows predictable drops under crop) are a useful and principled contribution that can steer future architectures. These are directly implied by the theory and had not been stated previously in this form.

- **Data-distribution section (2.6) is insightful:** Using neural compression codebook sizes to upper-bound the number of perceptually distinct images—and then showing the resulting capacity penalty is ≤ 0.05 bpp—neatly closes the loop on a subtle concern.

---

## Weaknesses

### Fatal
None.

### Major

- **Robustness bounds are heuristic, not formally proven.** Bounds 10–12 (for linear transformations including crop, rotation, LinJPEG) are derived from a singular-value heuristic and acknowledged by the authors to be neither true upper nor lower bounds. The only formally valid lower bound under robustness (Bound 13) is described as "extremely conservative and unrealistic" and is orders of magnitude lower than the heuristics. For example, under 75% crop on 256×256px images, the heuristic suggests ~0.5 bpp while Bound 13 gives only 904 bits (0.0014 bpp). This leaves a very large uncertainty in the core claim—"robustness constraints reduce but do not eliminate the large theoretical capacity gap"—and does not rule out the possibility that real robustness requirements are the primary bottleneck.

- **Chunky Seal's efficiency is deeply problematic.** The embedder is 90× larger (1022.7M vs. 11.0M parameters) and the extractor is 23× larger (773.7M vs. 33.0M parameters) than VideoSeal, achieving only 4× capacity improvement. This makes Chunky Seal unusable for virtually all deployment scenarios. The paper acknowledges this but frames it purely as a "proof of concept," without attempting smaller intermediate scales or efficiency-focused ablations. Given that the paper's central argument is that larger capacities are practically achievable, the presented model does not convincingly make that case for real-world use.

### Minor

- **VideoSeal-specific attribution of structural failure.** The empirical case for "current architectures have structural limitations" relies entirely on VideoSeal. While the controlled linear and handcrafted baselines provide a useful contrast, other architectures (e.g., TrustMark, HiDDeN, WAM) are not evaluated in the gray-image-no-augmentation setup. The conclusion that it is architecture rather than training that is the bottleneck would be strengthened by testing at least one other deep model in the same simplified setting.

- **LPIPS degradation in Chunky Seal is underanalyzed.** LPIPS increases 4.5× (0.0085 vs. 0.0019). While PSNR/SSIM/MS-SSIM are nearly identical, LPIPS captures perceptual distortions that matter in practice. The paper notes this briefly but does not investigate whether this is due to capacity increase, model size, or training differences.

### Trivial

- The paper uses the PSNR metric as the primary quality measure throughout both theory and experiments. For applications where perceptual quality is dominant, the theory's PSNR-centric view may not tightly predict practical achievable capacity, though the authors acknowledge this in limitations.

---

## Nice-to-Haves

- Intermediate-scale ablations of Chunky Seal (e.g., 2×, 10×, 50× larger than VideoSeal) would clarify the capacity-vs-size tradeoff and would make the "simple scaling unlocks more capacity" argument more convincing.
- An experiment verifying that the structural limitation is not training-time-related (e.g., training VideoSeal longer or with curriculum on bit count) would further strengthen the architecture critique.
- Applying the sanity checks (Section 5) explicitly to each evaluated method (VideoSeal, TrustMark, HiDDeN, etc.) would immediately demonstrate their diagnostic value.

---

## Novel Insights

The most genuinely novel insight is the combination of two findings: (1) the theoretical capacity gap is irreducible—data distribution, robustness, and perceptual constraints together still leave several orders of magnitude of unexploited capacity—and (2) the gap is demonstrably empirical, not theoretical, as proved by the linear and handcrafted baselines. The consequence—that current deep architectures fail to use the resolution of images they are trained on (VideoSeal at 256×256px behaves like a 20×20px model)—is surprising and not previously documented. Together, these redirect the community from assuming watermarking is a near-solved problem to recognizing it as an architectural and training challenge.

---

## Suggestions

- Provide a formal (non-heuristic) lower bound for at least one realistic robustness setting (e.g., crop 50%), even if it is loose. The gap between Bounds 10–12 and Bound 13 is so large that the paper cannot conclusively rule out robustness as the main bottleneck.
- Report capacity-vs-model-size Pareto curves for Chunky Seal variants to help the community understand where diminishing returns begin.
- Extend the gray-image, no-augmentation experiment to at least one other SOTA architecture (TrustMark or HiDDeN) to confirm the structural limitation is not VideoSeal-specific.

---

## Score and Decision

The paper makes a genuine, original contribution: it brings a rigorous geometric framework for watermarking capacity, systematically eliminates competing explanations for the theory-practice gap, and offers both theoretical and empirical evidence that current models are far from fundamental limits. The empirical finding that VideoSeal fails to use image resolution while a linear model succeeds is striking and independently valuable. Chunky Seal advances the state-of-the-art 4×, albeit at a large computational cost. The primary weakness—heuristic robustness bounds with a very wide uncertainty interval—leaves a material gap in the core argument for the robustness setting, but the simplified-setup experiments are convincing on their own. Overall this is a high-quality, well-organized paper that the community needs.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>