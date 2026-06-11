Now I have sufficient calibration data. Let me finalize the review.

**Round 1 bracket:** Between ~3.5 and ~6.5 (clearly not in the very weak 3.0 band, clearly not in the 8.0 strong theory band).

**Round 2 narrowing:** 
- The paper is weaker than the 6.25-7.0 anchors (which have rigorous theory or controlled experiments)
- Comparable to the 5.0 PL-condition paper (incremental theory, partial experiments)
- Slightly stronger than the 4.2 GD-stability paper (broader scope, more tasks)

**Final score: 5.0**

Here is the final review:

---

## Summary
This paper argues that Multi-Grade Deep Learning (MGDL)—training shallow networks sequentially on residuals—outperforms standard end-to-end training (SGDL). It provides convergence guarantees, a convex decomposition result for single-layer ReLU grades, eigenvalue analysis of GD dynamics, and experiments on image regression/denoising/deblurring, CIFAR-100, CIFAR-10, and transformer-based time series.

## Strengths

1. **Eigenvalue analysis providing a testable mechanism (Section 7, Theorem 4, Figures 4–6).** The paper monitors eigenvalues of I − ηH during training and shows that SGDL's eigenvalues consistently drop below −1 (correlating with oscillatory loss) while MGDL's stay within (−1, 1). This pattern is demonstrated across synthetic regression, image regression, image denoising, and CIFAR-10. This is the paper's most concrete empirical contribution—it is a clean, reproducible observation that directly supports the central stability claim.

2. **Quantified learning-rate robustness (Section 6, lines 237–247).** The paper reports specific admissible intervals: on synthetic Setting 1, SGDL works only for η ∈ [0.03, 0.08] while MGDL works for η ∈ [0.01, 0.3]; on higher-frequency Setting 2, SGDL converges only at η ≈ 0.005 while MGDL remains stable for η ∈ [0.08, 0.3]. These are concrete numerical ranges, not qualitative claims.

3. **Multi-grade transformer results (Section 8, Tables 4–5).** MGT achieves substantially lower test MSE than SGT (16× on synthetic time series, 5× on SPX financial data) while using only 28–33% of the training time. This extends the MGDL advantage to a practically important architecture not covered in prior MGDL work.

## Weaknesses

### Fatal
None.

### Major

1. **Claimed experimental scope is not realized.** The abstract and contribution list claim experiments on "CIFAR-10 and CIFAR-100 classification, including fully connected networks, CNNs, and transformers." However: **(a)** The CIFAR-10 experiment (Section 7) uses a 10,000-image subsample with *fully connected* networks trained via full-batch GD and reports only training loss—no classification accuracy, no CNNs, no standard benchmark evaluation. **(b)** The CIFAR-100 experiments (Section 5) report only MSE loss with no classification accuracy. **(c)** Despite claiming "CNNs" in the abstract and stating "For classification, we use convolutional neural networks" (line 154), no CNN-specific results, architectures (beyond equation references to a stripped appendix), or ablations appear in the main text. The gap between what the paper advertises and what it delivers is substantial.

2. **SGDL vs. MGDL comparisons do not control for model capacity.** In every experiment, SGDL uses a deeper network (e.g., 8 hidden layers for image regression) while MGDL uses sequential shallower grades (4 grades of 2 hidden layers each). The paper does not report total parameter counts, does not control for capacity or computational budget, and does not verify that the observed gains are due to the training methodology rather than architectural differences. The transformer comparison (Section 8) has the same confound: SGT uses multi-block Transformers while MGT uses single blocks per grade.

3. **No error bars, standard deviations, or statistical significance for any reported result.** All PSNR values (Tables 1–3) and MSE values (Tables 4–5) are presented as point estimates with no variance across runs. For a paper whose central claim is that MGDL "outperforms" SGDL, the absence of any uncertainty quantification is a significant gap in the experimental methodology.

### Minor

1. **Theoretical novelty is modest.** Theorem 1 (SGDL convergence) and Theorem 2 (MGDL per-grade convergence) are standard gradient-descent convergence results for L-smooth functions, extended incrementally from Xu (2025) by allowing non-zero biases. Theorem 3 directly applies the known convexity result of Pilanci & Ergen (2020) to each shallow grade—the paper's claim that this "extends convexification from shallow to deep architectures" overstates what is actually shown, since each grade's subproblem is individually convex but the sequential composition is not proven to achieve the same solution as end-to-end deep training. The eigenvalue analysis (Section 7) linearizes GD by discarding the remainder term and attributes the resulting properties to the original nonlinear dynamics; Theorem 4 is essentially a tautology (if the linearized sequence converges and the original also converges, they converge to the same limit) rather than a proof that MGDL eigenvalues *must* stay in (−1,1).

2. **Theorems 1–2 assume twice continuously differentiable activations, but the paper exclusively uses ReLU.** The paper acknowledges this implicitly but does not address the disconnect.

3. **CIFAR-100 reports only MSE loss, not classification accuracy.** For a classification benchmark, reporting only MSE without top-1 accuracy is an incomplete evaluation that does not permit comparison with standard results.

4. **CIFAR-10 eigenvalue analysis uses a 10,000-image subsample with full-batch GD, not Adam.** The extent to which these stability findings transfer to practical training settings (stochastic optimization, larger datasets, standard architectures) is unclear.

### Trivial
None.

## Nice-to-Haves
- Reporting SSIM alongside PSNR for image reconstruction.
- Discussing the connection to gradient boosting for better positioning.

## Removed Points
- "Missing related works" — removed per instruction (cannot be verified from external sources).
- "Reproducibility concerns about undisclosed hyperparameters" — removed as nitpick.
- "Missing appendix content / proofs" — removed per instruction (parser strips appendices).
- "Not contextualized against BM3D or other SOTA denoisers" — outside the paper's stated scope.
- "Transfer learning / generalization analysis needed" — scope creep beyond the paper's claims.
- "Formatting/style/typo concerns" — parser artifacts, not author errors.
- "Relationship to boosting not discussed" — a nice-to-have, not a weakness.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Align claims with actual content.** Remove or rephrase claims about CIFAR-10 classification and CNN experiments that are not present in the paper. The empirical contribution is strong enough on its own terms (image reconstruction, learning rate robustness, eigenvalue analysis, transformer extension) without inflated scope claims.
2. **Add classification accuracy for CIFAR-100.** Report top-1 accuracy with standard cross-entropy loss to enable comparison with the literature.
3. **Control for model capacity.** Add controlled experiments where SGDL and MGDL have matched parameter counts, or explicitly report and discuss the capacity differences.
4. **Add error bars.** Report means and standard deviations across multiple random seeds for all tabular results.

## Score and Decision

**Round 1 bracket:** between ~3.5 and ~6.5. The paper is clearly stronger than simple architectural-tweak papers (typically scored 3.0), but not as strong as papers with rigorous controlled experiments or substantial theoretical advances (scored 6.5+).

**Round 2 anchors considered:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/zPaTnGjgpa.md` (score 4.20): GD stability paper with eigenvalue analysis; rejected for insufficient causal evidence. The current paper has broader empirical scope but similar theoretical limitations. → Current paper is slightly stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/O0FOVYV4yo.md` (score 5.00): PL-condition paper with incremental theory and limited experiments. Very comparable to the current paper in terms of incremental theory and partial empirical support. → Comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fAGEAEQvRr.md` (score 5.50): Matrix factorization convergence analysis; novel theory but limited experiments. → Current paper has broader experiments but weaker theory.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/iEfdvDTcZg.md` (score 6.25): Feature learning study with thorough empirical controls and systematic hyperparameter sweeps; accepted. → Current paper is weaker (no controls, no error bars, overclaimed scope).

**Final calibrated score:** 5.0 — the paper has genuine empirical contributions (eigenvalue mechanism, learning rate robustness, transformer extension) but is weakened by overclaimed scope, uncontrolled comparisons, and lack of statistical rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>