Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Summary

This paper provides a theoretical and empirical analysis of multi-grade deep learning (MGDL), a training paradigm where deep networks are built incrementally by training shallow sub-networks ("grades") on residuals of previous grades. The authors establish convergence guarantees for gradient descent under smoothness assumptions, prove that MGDL with single-layer ReLU grades reduces to a sequence of convex programs, and analyze eigenvalue distributions of the linearized GD Jacobian to explain MGDL's superior stability over single-grade deep learning (SGDL). Experiments across image regression, denoising, deblurring, and time-series prediction show consistent improvements in stability and accuracy.

## Strengths

- **Genuine theoretical machinery spanning multiple angles:** The paper provides three distinct theoretical perspectives — convergence theorems (1, 2, 5), a convex reformulation for ReLU grades (Theorem 3, Section 4), and eigenvalue-based stability analysis (Theorem 4, Section 7). The convex reformulation correctly extends Pilanci & Ergen (2020) to the sequential multi-grade setting, showing that each grade of a ReLU network admits a convex program when the number of neurons exceeds the number of hyperplane arrangement regions. This is a non-trivial theoretical contribution that gives a principled explanation for MGDL's improved trainability.

- **Consistent and broad empirical gains:** Across image regression (Table 1: 0.42–3.94 dB PSNR gains on 6 images), denoising (Table 2: 0.16–4.23 dB across 3 images × 6 noise levels), deblurring (Table 3: 0.85–2.84 dB), and time-series prediction (Tables 4–5), MGDL consistently outperforms SGDL. The learning-rate robustness analysis (Section 6, Figure 2) demonstrates that MGDL maintains effective training over a wider range of learning rates than SGDL, aligning with the theoretical prediction that α_l ≪ α.

- **Eigenvalue monitoring provides mechanistic insight:** The eigenvalue traces (Figures 4–6) showing SGDL's eigenvalues dropping below −1 while MGDL's remain in (−1, 1) offer a concrete, visualizable explanation for why SGDL oscillates and MGDL converges smoothly. The CIFAR-10 experiment in Section 7, using full-batch GD on 10K samples with explicit Hessian computation, directly validates this spectral explanation at the level of the optimization dynamics.

## Weaknesses

### Major

- **Theory–practice gap: smoothness assumptions vs. ReLU + Adam experiments.** Theorems 1, 2, 5, and 4 all require twice continuously differentiable activation functions. The paper explicitly states this requirement (e.g., line 146-148, line 512). However, all experiments in Sections 5–8 use ReLU activations and the Adam optimizer — not full-batch GD on a twice-differentiable activation. This creates a structural mismatch: the convergence theorems that form the theoretical backbone do not directly apply to the experimental regime that demonstrates the method's benefits. The paper partially addresses this through the convex reformulation (Section 4), which handles ReLU rigorously but only for single-hidden-layer grades, and through the eigenvalue analysis (Section 7), which the paper claims computes Hessians for ReLU explicitly (line 519-520). However, the Hessian of a ReLU network is zero almost everywhere, and the paper defers the construction to supplementary material without explaining how the second derivative is handled — ordinary differentiability does not provide a well-defined Hessian at the kink points that ReLU networks necessarily encounter at initialization and during training. The paper would be substantially strengthened by either (a) bounding the error introduced by the smoothness assumption for ReLU networks in practice, or (b) restricting theoretical claims to the specific settings where they provably hold and clarifying what is empirical observation vs. theoretical explanation.

- **Uncontrolled parameter budgets confound the comparison.** The MGDL architectures (Eq. 27) add a new output layer at each grade. Even when hidden-layer counts are matched (e.g., SGDL 8 layers vs. MGDL 4 grades × 2 layers), MGDL has more total parameters because each grade's sub-network includes its own output connection to [nout]. The paper never reports or controls for total parameter counts, so the observed performance improvements may partially reflect increased model capacity rather than a superior training scheme. An equal-parameter-budget comparison (e.g., widening SGDL or narrowing MGDL grades) is needed to isolate the effect of the multi-grade decomposition itself.

- **CIFAR-100 results are uninterpretable as classification evidence.** The paper uses MSE loss (rather than cross-entropy) for CIFAR-100 classification and reports only loss values, not accuracy (Section 5, Figure 3). MSE loss on one-hot targets reaching 10⁻⁴ could correspond to near-perfect accuracy but could also reflect the network learning to output near-zero vectors. Without accuracy metrics, the CIFAR-100 experiments do not function as classification evidence, and the paper's claim that "MGDL delivers superior accuracy" (line 437) is unsupported for this task.

### Minor

- **Limited scope of transformer experiments.** The multi-grade transformer (Section 8) is evaluated on one synthetic series and one financial series (SPX). While the results are encouraging (33% of training time, lower test error), two datasets cannot establish a general claim about transformer training. The paper should either expand the transformer evaluation or temper the claims about generalizability.

- **The eigenvalue analysis in Section 7 uses small networks** (width 32–48) to make Hessian computation feasible. The extrapolation of these spectral observations to the larger networks used in Sections 5 and 8 is asserted but not justified. A brief discussion of how width affects eigenvalue distributions would strengthen confidence.

- **Missing positioning against related training paradigms.** The paper does not discuss relationships to greedy layer-wise pretraining (Bengio et al., 2006), progressive networks, or cascade correlation. While the core idea of multi-grade training is distinct from these (training on residuals rather than layer-by-layer), a brief discussion would contextualize the contribution and help readers understand where MGDL fits in the landscape of non-end-to-end training methods.

### Trivial

- The paper states the CIFAR-100 learning rate as "5 × 10⁻⁵" in Figure 3's caption but "5 × 10⁻⁴" in the main text (line 433) — a minor inconsistency.
- The claim that MGDL "requires only 33% of the training time" (line 636) lacks detail about the timing protocol and whether both methods were run on identical hardware with matched batch sizes.

## Nice-to-Haves

- An analysis showing cases where MGDL does *not* outperform SGDL would provide a more balanced view and help characterize the conditions under which multi-grade training is beneficial.
- Experiments with equal parameter budgets would isolate the effect of the training scheme from model capacity.
- Standard classification metrics (accuracy, cross-entropy loss) for CIFAR-100 would make those results interpretable.

## Removed Points

These points are flagged to be removed, treat them with caution.

**From the Harsh Critic:**

1. **"Disconnect between theoretical assumptions and experimental reality (Structural)" — claim of structural brokenness:** The critic argues the paper is "structurally broken" because the theory assumes twice-differentiable activations while experiments use ReLU. While the theory-practice gap is real (kept as a Major weakness above), the claim that it "collapses" the entire contribution is overstated. The paper offers separate theoretical treatments for ReLU (convex reformulation, Section 4; explicit ReLU Hessians for eigenvalue analysis, Section 7), and the eigenvalue analysis is empirically validated with ReLU networks trained with full-batch GD (Section 7, CIFAR-10). The paper's contribution is a composite of theoretical analysis and empirical demonstration, not a single chain where all links must hold simultaneously for the paper to have value. The critic's characterization as "structurally broken" ignores the independent value of the convex reformulation and the empirical eigenvalue findings.

2. **"Model capacity... MGDL almost certainly has more total parameters":** Kept the core concern but removed the assertion that this is certain without evidence. The paper does not report parameter counts, so the direction of the confound is plausible but not proven either way.

3. **"The convex reformulation...is a direct application of Pilanci & Ergen (2020)":** This is acknowledged in the paper (line 298: "Following Pilanci & Ergen (2020)"). The contribution is extending convexification to the multi-grade sequential setting, which the paper explicitly claims (line 332-334). While the extension is conceptually straightforward, it is correctly presented and fills a gap. The harsh critic's dismissal ignores that the paper does not claim to invent convexification from scratch.

4. **"The condition m_l ≥ P_l is stated without discussing its growth with N, which for image-sized datasets would be huge":** The paper applies the convex reformulation conceptually to explain why MGDL can be tractable, not as a practical algorithm for large-scale image data. This is scope creep — the convex program is a theoretical tool, not claimed as a practical training method.

5. **"Reproducibility... lacks sufficient detail":** Removed. The paper provides a link to an anonymous repository (line 670) and includes architecture specifications in Appendix D. The harsh critic demands optimizer settings and batch sizes that are standard and readily available in the code. This is a minor nitpick, not a substantive reproducibility concern.

6. **"Eigenvalue analysis is heuristic, not theoretical":** The paper does provide Theorem 4 (a rigorous theorem under smoothness assumptions) and then applies it heuristically to ReLU. The paper is transparent that the eigenvalue traces are empirical observations — line 523-525 says "We next monitor the eigenvalues" (monitoring, not proving). The harsh critic's characterization as "misleading" is itself misleading; the paper distinguishes between the theorem (Theorem 4) and the empirical monitoring exercise.

7. **"The Hessian of a ReLU network is not a well-defined function":** The Hessian exists almost everywhere for ReLU (zero in the interior of linear regions). Computing it piecewise and treating the kink points as measure-zero is standard in the Edge of Stability literature the paper cites. This concern is captured in the Major weakness but the harsh critic's framing as fundamentally invalid is disproportionate.

**From the Strength Finder:**

1. **"Rigorous convergence analysis with sharper learning-rate conditions for MGDL":** Kept conceptually in strengths but softened "rigorous" since the analysis relies on smoothness assumptions not met by all experiments.

2. **Generic/superficial strengths:** Removed individual listing as separate items, integrated into the consolidated strength list.

## Novel Insights

The most novel insight to emerge is the spectral explanation for why multi-grade training is more stable: because each grade optimizes a shallower subproblem, the Hessian eigenvalues of the linearized GD iteration remain bounded within (−1, 1), preventing the oscillatory dynamics that arise when SGDL eigenvalues cross below −1. While the eigenvalue analysis itself is not entirely novel (it connects to the Edge of Stability literature), the application to explain the mechanism behind multi-grade training's empirical success is a genuine contribution that unifies the theoretical framework with the observed behavior.

## Suggestions

1. The authors should clearly delineate which theoretical results are proven under smoothness assumptions and which are empirical observations for ReLU networks. A subsection titled "Scope of Theoretical Results" would help readers navigate the theory-practice relationship.

2. Report parameter counts for all SGDL/MGDL pairs and include at least one equal-parameter-budget comparison.

3. Replace MSE-only CIFAR-100 evaluation with standard cross-entropy loss and report top-1 accuracy, or remove the classification claim and restrict CIFAR-100 to a demonstration of training dynamics.

4. Add a brief "Related Work" paragraph positioning MGDL relative to greedy layer-wise pretraining, progressive networks, and other non-end-to-end training paradigms.

5. For the transformer experiments, either add a standard benchmark or explicitly scope the claim as preliminary evidence on toy and financial time series.

## Score and Decision

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/3YKeB9R1g9.md` (avg 8.0): Strong empirical-theory integration, well-validated claims. Our paper is substantially below this — the theory-practice gap and experimental gaps are more significant.  
- `/home/wg25r/review_agent/human_reviews_2026/Q3yLIIkt7z.md` (avg 7.0): Rigorous theory with solid empirical backing. Our paper's theory is less tightly coupled to its experiments. Below this.  
- `/home/wg25r/review_agent/human_reviews_2026/dSdLqg02tx.md` (avg 6.0): Theory with empirical validation but notable assumption-practice gaps and presentation issues. Our paper has a similar profile but somewhat broader experiments and a larger theory-practice disconnect. Slightly below.  
- `/home/wg25r/review_agent/human_reviews_2026/2Q0U2rV2Jz.md` (avg 5.50): Theory paper with some empirical backing. Our paper has more diverse experiments but similar theory-practice tension.  
- `/home/wg25r/review_agent/human_reviews_2026/Vhohl7EcvO.md` (avg 5.0): Theory with some validation, concerns about assumptions. Our paper has similar breadth of contribution but with more experimental evidence.  
- `/home/wg25r/review_agent/human_reviews_2026/4T65jHpSX7i.md` (avg 4.50): Theory paper rejected for limited novelty and scope. Our paper has more breadth and empirical validation.  
- `/home/wg25r/review_agent/human_reviews_2026/k3Lnh6jp0w.md` (avg 4.0): Eigenvalue analysis with limited practical impact. Our paper has broader empirical evaluation across more tasks. Above this.  
- `/home/wg25r/review_agent/human_reviews_2026/68DwQWtdwr.md` (avg 4.0): Layer-wise training with conceptual confusion. Our paper is clearer and has better theory. Above this.  
- `/home/wg25r/review_agent/human_reviews_2026/b36drMoKir.md` (avg 0.50): Fundamentally broken theory. Our paper is far above this.

The paper under review has real theoretical contributions (convex reformulation, convergence analysis, eigenvalue framework) and consistent empirical gains across diverse tasks. However, the theory-practice gap (smoothness assumptions vs. ReLU+Adam), uncontrolled parameter budgets, and uninterpretable CIFAR-100 results prevent it from being a strong acceptance. It is stronger than the 4.0-rejected papers but does not reach the 6.0 level. I place it at **5.0**, a borderline paper that could be improved to acceptance with targeted revisions addressing the major weaknesses.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>