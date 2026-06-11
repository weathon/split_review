Now I have sufficient calibration data. Let me write the final consolidated review.

**Calibration Reasoning:**

**Round 1 — Bracketing:** I first searched across five score bands. Strong reject anchors (avg 2.00-2.33, e.g., WM5G2NWSYC at 2.00) showed fundamentally flawed or poorly executed work — our paper is clearly above these. Weak anchors (avg 3.50-4.20) like zPaTnGjgpa (4.20, eigenvalue/stability) and OZZYqfplS3 (4.00, stability bounds) share topical overlap and similar combination of theory + experiments. Middle anchors (avg 5.50-6.00) like 8wAL9ywQNB (6.00, generalization bounds) have stronger theoretical depth or tighter evaluations. The paper sits between the weak and middle bands — it has genuine contributions but significant gaps (missing accuracy, uncontrolled baseline) that prevent it from reaching the middle tier. **Round 1 bracket: 3.5–5.5.**

**Round 2 — Narrowing:** I pulled anchors within (3.0, 5.0), (4.0, 5.5), and (3.5, 5.5). Key comparisons: kkVTeMvC9D (3.40, Jacobian analysis) — our paper has broader experiments and more theory; clearly better. n2RIkaf1S4 (4.00, BCD convergence) — our paper has similar quality but fewer fatal theoretical flaws. zPaTnGjgpa (4.20, eigenvalue/stability) — our paper has similar eigenvalue diagnostics but broader experimental scope; however, the missing classification accuracy is a significant weakness that the stability paper does not share (it reports test accuracy). On balance, our paper is comparable to these 4.0-4.2 anchors — slightly stronger in empirical breadth, slightly weaker in reporting standards and baseline control. **Final score: 4.0.**

---

## Summary

This paper studies Multi-Grade Deep Learning (MGDL), which decomposes end-to-end deep network training into a sequence of shallow networks trained sequentially on residuals. The authors provide convergence theory for GD in both SGDL and MGDL settings (Theorems 1–2), show that with single-layer ReLU grades the optimization decomposes into convex subproblems (Theorem 3), analyze eigenvalue distributions of the GD iteration matrix to explain stability advantages of MGDL, and benchmark MGDL against SGDL on image regression, denoising, deblurring, CIFAR-10/100, and transformer-based time series.

## Strengths

1. **Eigenvalue-based diagnostic linking shallow architecture to stable training (Section 7, Figures 4–6):** The paper directly monitors eigenvalues of I − ηH(W) during training and shows that MGDL's eigenvalues stay within (−1, 1) while SGDL's drop below −1, correlating with oscillatory loss. This is demonstrated across synthetic regression, image regression, image denoising, and CIFAR-10, providing a visual, mechanistic explanation that goes beyond simply observing that MGDL "works better."

2. **Quantified learning-rate robustness (Section 6):** The paper provides concrete intervals showing MGDL's advantage — e.g., for high-frequency synthetic data, SGDL converges only at η≈0.005 while MGDL remains stable for η∈[0.08, 0.3]. For image regression, MGDL remains stable for η up to 1 while SGDL fails on several images at large learning rates.

3. **Broad empirical evaluation spanning multiple tasks and architectures:** Experiments cover image regression (6 images), denoising (3 noise levels × 3 images), deblurring (3 blur levels), CIFAR-100 classification, CIFAR-10 eigenvalue analysis, and transformer-based time series on both synthetic and financial (SPX) data. This breadth strengthens the generality of the claims.

4. **Connection between multi-grade decomposition and convex subproblems (Theorem 3, Section 4):** The paper shows that when each grade is a single-layer ReLU network, the nonconvex deep learning problem decomposes into a sequence of convex programs. While the result builds on known convex reformulations (Pilanci & Ergen, 2020), the multi-grade framing as a sequence of such problems is a clean extension.

## Weaknesses

### Major

1. **No classification accuracy reported for CIFAR-10 or CIFAR-100 — only MSE loss:** The paper claims superiority on classification benchmarks but reports only MSE loss, not top-1 or top-5 accuracy. Loss is not a meaningful metric for comparing classification quality in isolation. For CIFAR-100 (Section 5), the paper states it evaluates "in terms of both accuracy and training dynamics" but only presents loss curves. For CIFAR-10 (Section 7), it uses only 10,000 subsampled images with squared loss and full-batch GD. Without accuracy numbers, the classification results cannot be compared against standard benchmarks, and the claim that MGDL improves "classification" performance is unsubstantiated.

2. **Transformer baseline (SGT) comparison is uncontrolled for model size:** In Section 8, MGT uses 4 single-block transformers while SGT uses an unspecified number (n_h) of Transformer blocks. The training time differences (741s vs 2,693s on synthetic data, 972s vs 1,712s on SPX) suggest substantially different model capacities. Without specifying SGT's architecture or matching for parameter count, the large test MSE gaps (MGT 0.16 vs SGT 2.6 on synthetic; MGT 0.018 vs SGT 0.089 on SPX) cannot be confidently attributed to the multi-grade approach rather than a capacity mismatch or poor SGT tuning.

3. **No variance or statistical significance reporting:** All results (PSNR, MSE) are reported as point values with no standard errors or confidence intervals. Given that some gains are modest (e.g., Cameraman TePSNR: 24.79 → 25.21, a 1.7% relative improvement), it is unclear whether the observed differences are reproducible or due to initialization/optimization noise.

### Minor

4. **CIFAR-100 learning rate inconsistency:** The main text (line 225) states learning rates 5×10⁻⁴ and 1×10⁻⁴, but the Figure 3 caption (line 233) states η = 5×10⁻⁵ and η = 1×10⁻⁴. This factor-of-10 discrepancy for the first learning rate should be corrected.

5. **Convexity result (Theorem 3) requires single-layer ReLU grades, while experiments use multi-layer grades:** The convexity decomposition requires each grade to be a single hidden ReLU layer, and the proof requires m_l ≥ P_l (where P_l grows exponentially with input dimension in the worst case). The experiments use grades with 2–3 hidden layers where the convexity theory does not directly apply. The paper acknowledges this scope but does not discuss what theoretical guarantees hold in the practical multi-layer setting.

6. **The eigenvalue analysis is correlational rather than causal:** Section 7 shows that when MGDL's eigenvalues stay in (−1, 1), training is stable, and when SGDL's exit this range, loss oscillates. While a useful diagnostic, the analysis does not predict when eigenvalues will exit (−1, 1) or provide a causal mechanism — it describes the correlation post-hoc.

### Trivial

7. **Use of MSE loss for classification:** The paper uses MSE loss for CIFAR-10/100 rather than cross-entropy. This is non-standard for classification tasks and warrants justification.

## Nice-to-Haves

- Variance reporting (standard errors over multiple runs) would substantially strengthen the empirical claims, especially for the smaller PSNR gains.
- A discussion of failure modes of MGDL (e.g., error accumulation across sequential grades) would improve the paper's completeness.

## Removed Points

These points were considered and removed with justification:

- **"Structural uncontrolled comparison — architectures not matched for capacity"**: The harsh critic claimed no attempt was made to match architectures. In fact, the total number of hidden layers is consistently matched across all experiments: image regression (SGDL: 8 hidden layers, MGDL: 4 grades × 2 = 8), denoising (SGDL: 12, MGDL: 4×3 = 12), synthetic data (SGDL: 4, MGDL: 4×1 = 4), CIFAR-10 eigenvalues (SGDL: 8, MGDL: 4×2 = 8). Given matched hidden dimensions, parameter counts are comparable. This criticism is factually incorrect.

- **"Abstract misleads about convexity"**: The abstract explicitly qualifies with "In the case of ReLU activations with single-layer grades." This is accurate.

- **"SGT test MSE of 2.6 suggests a bug"**: Speculative. The paper attributes this to distribution shift, a plausible phenomenon in time series. The legitimate concern about uncontrolled model size is retained above.

- **"ReLU not twice differentiable"**: Standard technical assumption in optimization theory, acknowledged by the paper. Does not invalidate the theoretical analysis.

- **"No comparison to boosting"**: Missing related work should not be included per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report top-1 accuracy for CIFAR-10 and CIFAR-100 (using both MSE and cross-entropy loss) and standardize against published baselines.
2. Specify SGT's number of blocks (n_h) and match total parameter count or compute budget between MGT and SGT.
3. Add standard errors or confidence intervals over multiple random seeds for key results.
4. Resolve the CIFAR-100 learning rate discrepancy (5×10⁻⁴ vs 5×10⁻⁵).
5. Discuss what theoretical guarantees apply when grades have multiple hidden layers (beyond the single-layer convexity result).
6. Add a subsection on MGDL's limitations, particularly error accumulation across grades.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>