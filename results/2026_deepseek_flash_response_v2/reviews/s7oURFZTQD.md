## Summary

This paper provides theoretical and empirical analysis of Multi-Grade Deep Learning (MGDL), which decomposes deep network training into sequential shallow subproblems, each trained on residuals from previous grades. The contributions include convergence guarantees for GD on MGDL, a proof that single-layer ReLU grades yield convex subproblems (extending Pilanci & Ergen 2020), an eigenvalue-based analysis of GD stability, and experiments on image regression, denoising, deblurring, CIFAR-10/100, and time-series transformers.

## Strengths

- **Theorem 3 extends convexification from shallow to deep ReLU networks via the multi-grade decomposition.** The paper proves that when each grade uses a single ReLU layer, the nonconvex deep problem decomposes into a sequence of convex subproblems (Section 4, Theorem 3). This explicitly extends Pilanci & Ergen (2020), which only convexified single hidden-layer networks, and the proof is concise and appears sound given its framing.

- **Eigenvalue analysis across multiple distinct tasks empirically identifies a spectral mechanism for MGDL's stability advantage.** Section 7 tracks eigenvalues of the linearized iteration matrix I−ηH(W) during training and shows across synthetic regression, image regression, denoising, and CIFAR-10 that MGDL's eigenvalues stay within (−1,1) while SGDL's exit this range, directly correlating with oscillatory vs. smooth loss decay (Figures 4–6). The consistency of this pattern across four different task types strengthens the correlational evidence.

- **Multi-grade transformers (MGT) demonstrate that MGDL benefits generalize beyond fully-connected and CNN architectures.** On synthetic time series, MGT achieves TeMSE 1.6×10⁻¹ vs. SGT's 2.6 (16× improvement) with 28% training time; on SPX financial data, TeMSE 1.8×10⁻² vs. SGT's 8.9×10⁻² with 33% time (Tables 4–5).

- **Quantified learning-rate robustness intervals provide concrete evidence for MGDL's stability advantage.** Section 6 reports specific ranges: on a low-frequency synthetic task, MGDL sustains loss < 0.001 for η∈[0.01,0.3] while SGDL only succeeds for η∈[0.03,0.08]; on a high-frequency task, MGDL remains stable for η∈[0.08,0.3] while SGDL diverges at all larger rates.

## Weaknesses

### Major

- **No classification accuracy reported for CIFAR-10/100 — only MSE loss, yet the paper claims "superior accuracy."** The CIFAR-100 experiment (Section 5, lines 223–227) reports only training MSE loss curves; the CIFAR-10 experiment (Section 7, line 289) reports only final loss values. Neither reports top-1 or top-5 accuracy — the standard metric for these datasets. The claim that MGDL "delivers superior accuracy" (line 225) is supported only by lower MSE, which does not necessarily translate to better classification (e.g., a model could shrink all logits toward zero, reducing MSE while producing near-uniform predictions). Since the paper lists "extensive experiments on CIFAR-10 and CIFAR-100 classification" as a key contribution (contributions list, item 3), this is a consequential evidential gap. The image reconstruction experiments (which use appropriate PSNR metrics) are not affected by this criticism.

- **Transformer evaluation is confined to time-series regression, not standard Transformer benchmarks.** The abstract and introduction claim coverage of "transformers," but Section 8 evaluates only synthetic time-series regression and S&P 500 prediction. There are no experiments on language tasks (GLUE, translation), vision transformers (ImageNet), or other standard Transformer benchmarks. The SGT baseline collapses catastrophically (TeMSE 2.6 vs. MGT's 0.16 on synthetic data, line 322), which is not explained — a standard single Transformer with reasonable tuning should not generalize this poorly on a 1,024-point time-series task, suggesting the baseline may be undertuned. Either the "transformers" scope should be narrowed or the benchmark should be expanded.

### Minor

- **No error bars, multiple seeds, or statistical significance reported.** Every experimental table (Tables 1–5) reports single numbers. Given that some PSNR gains are modest (e.g., 0.42 dB test PSNR for Cameraman), variance information is essential for assessing reliability.

- **Convexity result (Theorem 3) requires m_l ≥ P_l, where P_l can be enormous.** P_l is the number of possible ReLU activation patterns, growing as O(N^{d_l}) for d_l-dimensional data (Cover, 2006). For N=1024 this condition is unlikely to hold in practice, and the paper does not verify whether it is satisfied in any experiment. The theoretical connection is interesting but its practical relevance is unclear.

- **The claim α_l ≪ α is stated without formal derivation.** Line 112 states that MGDL "allows a broader admissible learning-rate range (η_l ∈ (0,2/α_l) with α_l ≪ α)" but provides no bound on α_l relative to α. The convergence theorems (Theorems 1–2) are standard GD guarantees; the novel insight would come from quantifying why α_l is smaller, which is not done.

- **Learning-rate experiments train for 10^6 epochs** (Section 6), which is far from practical usage. While this may be necessary to clearly demonstrate stability differences, it limits the practical relevance of those results.

### Trivial

- Table 3 column headers "3, 5, 7" are not explicitly labeled in the main text as blur kernel sizes (line 204).

## Nice-to-Haves

- Report top-1 / top-5 classification accuracy for CIFAR-10 and CIFAR-100.
- Include error bars / multiple runs for all reported metrics.
- Add a formal bound relating α_l to α (even under simplifying assumptions).
- Ablate MGDL design choices: grade depth D_l, number of grades L, and the feature propagation mechanism vs. simpler residual fitting.
- Demonstrate the convex program (8) being solved on a small-scale problem to show practical relevance of Theorem 3.

## Removed Points

These points were flagged during filtering and should be treated with caution; they are excluded from the main review for the stated reasons.

- **"Missing CNN architecture details for CIFAR-100" (Harsh Critic):** The paper references equations 28–29 (in the appendix, stripped by the parser). Removed per the rule that missing appendix content is not a valid criticism.

- **"SPX data extends to August 2025, which is forward-looking" (Harsh Critic):** The review date is June 2026 and the submission is to ICLR 2026, making data through August 2025 entirely reasonable. Removed as factually irrelevant.

- **"The claim α_l ≪ α formally justifies the broader range" (Strength Finder):** This strength conflicts with the verified weakness that α_l ≪ α is stated without proof. Per the rule, when a strength and a verified weakness disagree, the weakness wins. Removed.

- **"CIFAR-10 uses a subset of data and fully connected network, not CNN" (Harsh Critic):** The CIFAR-10 experiment in Section 7 is explicitly part of the eigenvalue analysis, which requires smaller models for Hessian computation. The paper is clear about this. Removed as a strawman.

## Novel Insights

The intersection of the two reviews reveals that the paper's strongest evidence (learning-rate robustness intervals in Section 6 and eigenvalue tracking across four task types in Section 7) comes from carefully controlled small-scale experiments, while the weakest evidence (CIFAR classification without accuracy metrics, limited Transformer evaluation) comes from larger-scale benchmarks presented as core contributions. This tension suggests the paper would benefit from either (a) strengthening the weak benchmarks to match the rigor of the small-scale experiments, or (b) honestly scoping down the claims to match what the current evidence supports. The eigenvalue analysis is noteworthy for tracking the same spectral mechanism across synthetic regression, image regression, denoising, and classification — this consistency across task types lends credence to the explanatory story even if the linearization's validity for ReLU networks is imperfect.

## Suggestions

1. **Report top-1 classification accuracy on CIFAR-10 and CIFAR-100.** This is the single highest-priority fix and directly addresses the most consequential weakness.
2. **Add error bars (multiple seeds) to all quantitative results.**
3. **Either broaden the Transformer evaluation** to include a standard benchmark (e.g., a GLUE subset or image classification with ViT), **or explicitly scope down** the claim in the abstract and introduction.
4. **Explain the SGT baseline collapse** on synthetic time series (TeMSE 2.6) — if the baseline is reasonably tuned, why does it perform this poorly on a simple 1,024-point regression task?

**Calibration summary (all retrieved anchors):**

**Round 1 — Bracketing anchors:**
- 2.33 (Reject, deep linear networks): much weaker, had serious proof issues
- 2.50 (Reject, batch size/LR): much weaker, narrow focus
- 3.00 (Reject, non-differentiability): weaker, narrow analysis
- 4.00 (Reject, BCD): slightly weaker, actual proof errors (circular argument)
- 5.25 (Reject, multitask rep learning): comparable; strong theory but experiments didn't validate claims
- 5.50 (Reject, feature learning): comparable; rigorous theory but strong assumptions, limited validation
- 6.00 (Accept, teacher-student): stronger; rigorous multi-phase convergence analysis, well-received
- 8.00 (Accept, multiple papers): much stronger

**Round 2 — Narrowing anchors:**
- 4.20 (Reject, stability/detrimental): weaker
- 4.75 (Reject, large LR singularities): slightly weaker; too empirical, weak theory-method link
- 4.75 (Reject, video deblurring): slightly weaker
- 5.25 (Reject, image statistics): comparable
- 5.33 (Accept, EMCCD denoising): comparable; methods paper with decent experiments
- 6.00 (Reject, spike camera): stronger for specialized reconstruction task
- 6.25 (Reject, spectral dynamics): stronger breadth but rejected for "lacking solid insights"
- 6.25 (Accept, continual learning spectral reg.): stronger, well-received

**Initial bracket:** [4.0, 6.5] → **Narrowed to:** 5.0. The paper has genuine contributions (convexity extension across multiple tasks, eigenvalue analysis) but the missing classification accuracy and limited Transformer evaluation are significant gaps that real papers scoring ≥6.0 in the calibration set do not exhibit. It is clearly stronger than the 4.0–4.75 anchors (which had proof errors or excessively weak theory) and comparable to the 5.25–5.50 anchors, placing it at **5.0**.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>