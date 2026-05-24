## Summary

This paper studies multi-grade deep learning (MGDL), a sequential training scheme where shallow networks are trained grade-by-grade on residual errors. It attempts to explain MGDL's empirical advantages over standard end-to-end training (SGDL) through convergence theorems (Theorems 1–2), a convexity result for ReLU grades (Theorem 3), and an eigenvalue analysis of the GD iteration matrix (Section 7). Experiments span image regression, denoising, deblurring, CIFAR-10/100 classification, and transformer-based time series. The core idea — training shallow networks sequentially on residuals — is interesting and the empirical coverage is broad, but the paper's theoretical contributions are substantially weaker than claimed, and key experimental comparisons lack sufficient controls to support the strong conclusions drawn.

## Strengths

- **Broad experimental scope and consistent empirical improvements.** Tables 1–3 report PSNR gains of 0.42–3.94 dB across six image regression tasks, 0.16–4.23 dB across three denoising tasks at six noise levels, and 0.85–2.84 dB across three deblurring levels. The multi-grade transformer (MGT) achieves test MSE 0.16 vs. SGT's 2.6 on synthetic time series and 0.018 vs. 0.089 on SPX financial data, at 28–33% of the training time. These gains are quantitatively documented across multiple domains.

- **Learning-rate robustness evidence.** Section 6 provides synthetic experiments (Figure 2) showing that MGDL maintains stable training over a wider range of learning rates than SGDL. For example, on a high-frequency target, SGDL converges only at η≈0.005 while MGDL is stable for η∈[0.08,0.3]. This is one of the paper's cleaner empirical results.

- **Eigenvalue visualization as an explanatory tool.** Figures 4–6 track eigenvalues of I−ηH(W) during training. The observation that MGDL's eigenvalues stay within (−1,1) while SGDL's dip below −1, correlating with loss oscillations, provides useful intuition for MGDL's training stability. Although this analysis is empirical rather than theoretical, the visual evidence across synthetic regression, image regression, and CIFAR-10 is informative.

- **Convexity connection for shallow ReLU grades.** Theorem 3 shows that when each grade is a single hidden-layer ReLU network, the grade-level optimization reduces to a convex program (via Pilanci & Ergen 2020). This bridges MGDL to the well-studied convex reformulation literature, though the novelty is limited (see weakness below).

## Weaknesses

### Major

- **Central theoretical claim is unproven.** The paper's key argument for MGDL's advantage is the assertion that α_l ≪ α (the Hessian spectral norm is much smaller for MGDL's shallow grades than for a deep SGDL network), which would imply a wider admissible learning-rate range η_l∈(0,2/α_l) vs. η∈(0,2/α). No proof, analysis relating network depth to Hessian spectral norms, or empirical verification of this inequality is provided. The paper simply states it (line 170: "α_l ≪ α"). Theorem 1 and Theorem 2 themselves are standard gradient-descent convergence guarantees under Lipschitz smoothness — the distinction between MGDL and SGDL rests entirely on the unsubstantiated α_l ≪ α claim.

- **Eigenvalue analysis is empirical, not theoretical.** Section 7 presents the eigenvalue analysis as a theoretical explanation, but Theorem 4 is a standard contraction result that assumes τ<1 without proving that MGDL necessarily satisfies this condition while SGDL does not. The claim that MGDL's eigenvalues stay in (−1,1) is supported only by empirical plots (Figures 4–6), not by any theoretical derivation tying grade depth to eigenvalue confinement. The paper conflates "empirical observation" with "theoretical explanation."

- **CIFAR-100: no test accuracy, non-standard loss.** For CIFAR-100 classification: (a) the paper uses MSE loss rather than cross-entropy, which is non-standard for multi-class classification; (b) only training loss curves are reported (Figure 3), **not test accuracy**; (c) yet the paper claims "MGDL delivers superior accuracy" (line 283). Lower training MSE does not imply better classification accuracy. Without test accuracy, the classification claims are unsupported. This is a significant gap for a paper that lists CIFAR-100 as a key benchmark.

- **Architecture comparisons not controlled for capacity.** The paper compares SGDL (depth-8 network) against MGDL (4 grades, each depth-2, effective total depth 5 per the paper's formula ∑D_l = D+L−1) for image reconstruction. Total parameter counts are not reported for either method. For the transformer experiments, MGT (L single-block grades) is compared against SGT (one multi-block transformer) without controlling for total depth, parameter count, or computational budget. The observed differences cannot be cleanly attributed to the training strategy versus model capacity differences. This limits the strength of the comparative claims.

- **No statistical confidence measures.** Every numerical result (Tables 1–5) is a single number. No standard deviations, confidence intervals, or multiple-trial statistics are reported anywhere. For a paper claiming MGDL "consistently outperforms" SGDL, the lack of any variability measure is a serious omission — observed differences could be within run-to-run noise.

### Minor

- **ReLU mismatch with smoothness assumptions.** Theorems 1 and 2 assume σ is twice continuously differentiable, but ReLU (used throughout the experiments) is not differentiable at zero and has zero second derivative everywhere else. The paper acknowledges the assumption but does not discuss whether or how the theorems extend to ReLU, leaving a gap between theory and practice.

- **Convexity result novelty is limited.** Theorem 3 is adapted from Pilanci & Ergen (2020) with minor modifications. The claimed extension to deep architectures is achieved by decomposition: each grade IS a shallow network, so the convexification applies trivially to each subproblem individually. The deep network as a whole is not convexified — it is decomposed into shallow pieces that are individually convex. The required condition m_l ≥ P_l is acknowledged but its practical implications (P_l grows combinatorially with dimension) are not discussed, limiting the result's practical relevance.

- **Transformer comparison lacks architecture details.** The paper reports dramatic improvements (MGT test MSE 0.16 vs. SGT 2.6) but does not specify model sizes (d_model, n_heads, number of parameters) for either method. The data source for the SPX experiment is given as "Yahoo Finance or Bloomberg" — an imprecise attribution for a reproducibility-critical detail.

- **Training procedure descriptions are sparse.** Key hyperparameters (number of epochs, batch sizes, learning rate schedules, early stopping criteria, optimizer settings beyond "Adam") are not reported for the main experiments, limiting reproducibility.

### Trivial

- Several figure captions and image descriptions are duplicated (e.g., the long caption repeats verbatim as alt text), a parsing artifact that should be cleaned.

## Nice-to-Haves

- Including SSIM alongside PSNR for image reconstruction would strengthen the evaluation.
- Reporting test accuracy on CIFAR-10 (which already uses MSE loss) would help calibrate how well training MSE correlates with actual classification performance for this setup.
- A discussion of when MGDL might be worse than SGDL (e.g., when features learned in early grades are insufficient for later grades, or when end-to-end finetuning of the full stack would help) would make the paper more balanced.

## Removed Points

These points were flagged for removal from the harsh critic's review; treat them with caution:

- Criticism that the CIFAR-10 fully-connected-on-raw-pixels setup is a "toy setting" — this is a judgment call, and the setup is valid for eigenvalue analysis even if not SOTA. Removed as opinionated scope-creep.
- Criticism that Section 7's linearization "drops higher-order terms without justification" — the paper explicitly acknowledges this (line 309: "Neglecting r^{k−1} gives the linearized update"). Removed as already addressed.
- Criticism about the paper's tone being "advocacy rather than dispassionate analysis" — removed as a stylistic judgment rather than a concrete weakness.
- Implication that "SGT collapses under distribution shift" is poorly defined — the paper shows SGT's test error is 16× higher, which is clear evidence of test-time degradation regardless of semantic label. Removed as the specific claim about "distribution shift" is a reasonable interpretation of the observed results.
- The claim that Theorem 3's convexity result is "trivial" because each grade is a shallow network — while the novelty is limited, the decomposition itself is a valid connection. Demoted to Minor rather than removed.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the eigenvalue analysis (the paper's most distinctive claim) is empirical rather than theoretical is accurate and should be carefully considered by the authors.

## Suggestions

1. **Either prove α_l ≪ α or reframe the theoretical contribution honestly.** If a proof relating grade depth to Hessian spectral norm is not possible, present the convergence theorems as standard background and reframe the eigenvalue analysis as an empirical diagnostic, not a theoretical proof.

2. **Report test accuracy for CIFAR-100 (and ideally CIFAR-10) using standard cross-entropy loss.** This is essential to support any claim about classification performance.

3. **Report parameter counts and/or FLOPs for all SGDL vs. MGDL comparisons.** If architectures differ in capacity, either match them or acknowledge the disparity and discuss which direction the confound cuts.

4. **Repeat key experiments (at minimum, CIFAR-100 and one image task) over 5+ seeds** and report mean ± std to support the claim of "consistent" improvement.

5. **Make the data source precise** for the SPX experiment rather than "Yahoo Finance or Bloomberg."

## Score and Decision

I assign scores relative to the following calibration anchors:

| Anchor | Path | Avg Human Score | Round | Comparison |
|--------|------|----------------|-------|------------|
| Fixed point iterations in DNNs | YoEFNqMNmG.md | 4.00 | R1 bracket | Similar weaknesses: limited practical validation, theory-presentation gap. This paper has broader experiments but more overclaimed theory. Comparable quality. |
| Dynamics of learning dynamics | T65jHpSX7i.md | 4.50 | R1 bracket | Stronger theoretical rigor, fewer experiments. This paper experiments more broadly but theoretical claims are weaker. Slightly below. |
| Shapley explanations | 3zOZXcn4YR.md | 5.00 | R2 narrow | Better experimental methodology (multiple metrics, standard datasets). This paper has more domains but less rigorous controls. Below. |
| Multi-index models | 2Q0U2rV2Jz.md | 5.50 | R1 bracket | Strong theoretical contribution with rigorous proofs; no experiments. Incomparable methodology. |
| Seq vs Seq encoders/decoders | z5Mn8Rxi3l.md | 5.33 | R2 narrow | Clean controlled comparisons with careful architecture matching. This paper lacks such controls. Below. |

**Round 1 bracket:** 3.0–5.5  
**Round 2 narrowing:** Compared against the 4.00 fixed-point paper (similar theory-presentation gap, similar practical limitations) and the 5.00–5.50 papers (better experimental controls or more rigorous theory), this paper sits at the lower end of the bracket due to unproven core theoretical claims and uncontrolled experimental comparisons.

**MY FINAL SCORE: 4.0**
**MY FINAL DECISION: Reject**