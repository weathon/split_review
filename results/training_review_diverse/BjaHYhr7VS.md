Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes Hi-DLR, a method that automatically sets per-group learning rates by fitting a diagonal quadratic model using only forward passes (no backpropagation through the Hessian). The same machinery yields a Per-Parameter Influence (PPI) metric, which the paper uses to design an adaptive parameter-efficient training (PET) framework that identifies which parameter groups to train and which to freeze. Experiments span image classification, multi-task learning, tabular regression, and language understanding with LoRA.

## Strengths

1. **Principled extension of GeN to the DLR setting.** The paper generalizes the Hessian-informed learning-rate computation of GeN (Bu & Xu, 2024) from a single uniform learning rate to K per-group learning rates. The derivation (Section 2.3–2.4) cleanly connects the Newton step, preconditioned gradient methods, and DLR within a unified local quadratic framework.

2. **Backpropagation-free computation of Hessian-informed quantities.** Algorithm 1 avoids instantiating the Hessian by using 4K forward passes every Φ iterations to fit a diagonal quadratic (Equation 3.1). This design choice keeps the per-iteration overhead to forward passes only, making it practical for large models where second-order backpropagation is prohibitive.

3. **Consistent convergence improvement over uniform learning rate (ULR) baselines.** Across five image classification datasets (Table 1), Hi-DLR outperforms the best ULR (Constant, Cosine, Linear, GeN, Prodigy, D-Adaptation) on 4/5 settings. On GLUE with LoRA (Table 2), Hi-DLR beats Hi-ULR and widely-used PET methods on 4/5 datasets.

4. **Novel PPI metric enables adaptive PET.** Equation 5.1 defines per-parameter influence derived from the same quadratic model. Figures 6–7 show that PPI differs substantially across parameter groups and tasks. Tables 3–4 demonstrate that a PET method identified on a small model via PPI (at ψ=10) transfers successfully to larger models, achieving ~1.5× training speed with <0.5% trainable parameters while maintaining performance close to full-model training.

5. **Verification of the quadratic approximation's accuracy.** Figure 1 plots actual losses and the fitted quadratic at a training iteration, showing that the second-order Taylor approximation (Equation 3.1) is accurate for the learning rates used in practice.

## Weaknesses

### Fatal
None.

### Major

1. **No runtime or computational overhead analysis despite explicit efficiency claims.** The paper repeatedly states that Hi-DLR is "almost as fast as standard optimization" (Section 3) and "almost as fast as ULR" (Section 1), but provides zero wall-clock time, forward-pass counts relative to total training, or overhead percentage in any experiment. The algorithm requires 4K forward passes per update with updates every Φ iterations — a transparent cost in theory, but the practical efficiency claim is unsubstantiated without timing data. A practitioner cannot judge whether the gains from better learning rates justify the extra computation. **Why it matters:** The efficiency claim is part of the paper's central narrative; without empirical support, the method's practical advantage is unclear.

2. **Missing comparison to simple DLR heuristics.** The main experiments (Table 1, Figure 4, Figure 5) compare Hi-DLR almost exclusively to ULR methods. The only DLR baselines appear in Table 2 (LoRA-FA, LoRA+). No comparisons are made to simple fixed-ratio per-group heuristics (e.g., η_bias = 2× η_weight, or per-task learning rates in the CelebA multi-task setting). Since the paper's central claim is that Hi-DLR *adaptively* sets per-group learning rates better than a uniform baseline, the reader cannot tell whether the improvement comes from the Hessian-informed adaptation or simply from having multiple degrees of freedom. A grid search over a few fixed ratios would address this. **Why it matters:** Without this baseline, the contribution of the Hessian computation specifically (vs. any DLR scheme) is not isolated.

### Minor

1. **Diagonal approximation of A* is not validated.** The paper replaces the full K×K matrix A* with its diagonal (Equation 3.1), stating "negligible accuracy degradation empirically" (line 151), but provides no experiment to support this. The quadratic approximation itself is validated in Figure 1, but the diagonal simplification is a separate step. An experiment comparing diagonal vs. full A* on a small model with few groups (K=3–5) would be straightforward and would increase confidence in the method.

2. **No statistical significance or multi-run variance reported.** The paper does not state how many random seeds were used. With close results (e.g., Hi-DLR 44.2 vs. LoRA+ 44.5 on CoLA in Table 2), a single run could reverse the ranking. Standard deviations over 3–5 runs are needed for all main tables.

3. **Sampling distribution of ξ_j is not specified.** Algorithm 1 uses 4K perturbations ξ_j ∈ ℝ^K to fit the quadratic (line 159), but the paper never states how ξ_j are sampled (random directions? coordinate axes? Gaussian?). This affects the quality of the fit and is needed for reproducibility.

4. **Hyperparameter Φ (update frequency) is not reported.** The paper mentions updating "every Φ iterations" and that "Φ = O(K)" would make overhead O(1), but the actual Φ values used in experiments are not given. This is needed for reproducibility and to assess the real computational cost.

5. **PPI transfer claim across model sizes uses only visual evidence.** The statement that "different model sizes have similar PPI by parameter groups" (Section 5.2) is supported only by visual inspection of heatmaps in Figure 7. While the downstream transfer results (Tables 3–4) provide indirect validation, a quantitative similarity measure (e.g., Spearman rank correlation between PPI vectors of small and large models) would directly support the claim.

### Trivial

- The two "O(1)" claims (from O(K²) to O(K) via diagonalization, and from O(K) to O(1) via infrequent updates) could be stated more precisely to avoid confusion.
- The "Constant lr" baseline in Figure 4 is not described — it is presumably the best constant learning rate averaged over all tasks, but this should be stated.
- The synthetic NAM dataset (Section 4.3) is not described (generative process, dimensionality).

## Nice-to-Haves

- Report the actual learning rates found by Hi-DLR in the LoRA experiment (for A, B, head) to check whether the method recovers the known pattern of higher lr for B than A (as in LoRA+).
- In the CelebA multi-task experiment, compare to per-task learning rates tuned individually (even on a subset) to confirm that Hi-DLR's improvement is not solely from having multiple degrees of freedom.
- Discuss how PPI is computed when a_k ≤ 0 (non-convex quadratic) — the paper skips the update in that case, but it is unclear how PPI handles those iterations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing comparison to Howard & Ruder (2018) and You et al. (2019)."** The paper's experimental setups (K=2 groups: bias vs. rest, head vs. rest) do not naturally align with layer-wise or block-wise methods that assign one learning rate per layer. The critic's expectation compares against the wrong granularity. The relevant DLR heuristics for the paper's group definitions are simple fixed-ratio per-group schemes, not depth-wise scaling. (Moved from Major to Minor point #2 above, reformulated as a request for fixed-ratio heuristics.)

- **"The paper claims 'no one PET can fit all tasks' but does not show that Hi-DLR is consistently the best."** This misreads the paper. The claim "no one PET can fit all tasks" (line 226) is an observation motivating adaptive PET, not a claim that Hi-DLR dominates. The paper shows Hi-DLR is best on 4/5 datasets, which is consistent with the claim.

- **"The 'almost as fast as ULR' claim is unsubstantiated."** Kept as Major weakness #1 (properly framed).

- **"Section 4.4 - the paper claims 'no one PET can fit all tasks' but does not show Hi-DLR is consistently best."** This was a duplicate of the above. Removed.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: that the paper's taxonomy framing PET, layer-wise learning rates, and adaptive optimizers all as instances of DLR (Section 1) provides a useful unifying perspective. The harsh critic's call for runtime analysis and DLR baselines highlights that the paper's practical narrative ("almost as fast as ULR") is significantly ahead of its evidence — a gap that is common in papers proposing Hessian-aware methods but worth emphasizing as a general lesson for the community. However, no reviewer offered novel technical insights the authors missed.

## Suggestions

1. **Add a runtime table.** Report wall-clock time per 1000 iterations and total training time for at least one medium-scale experiment (e.g., ViT on CIFAR-100 or RoBERTa on CoLA). Compare Hi-DLR, Hi-ULR, and a standard ULR baseline. This single addition would address the most significant gap.
2. **Add a fixed-ratio DLR baseline.** For each experimental setup, test 2–3 reasonable fixed ratios between groups (e.g., η_bias = 2× η_weight, η_head = 5× η_rest) to isolate whether Hi-DLR's adaptive selection improves over heuristic guessing.
3. **Validate the diagonal approximation.** Compare diagonal Hi-DLR vs. full-matrix Hi-DLR on a small model (e.g., 2-layer MLP, K=3 groups) — show that per-group learning rates and convergence are similar.
4. **Report Φ and ξ sampling in the main text or appendix.**
5. **Add standard deviations over 3–5 seeds for main results (Tables 1–4).**

## Score and Decision

The paper introduces a well-motivated, principled method for adaptive per-group learning rate scheduling and a derived PPI metric for PET. The core ideas are novel and the experimental scope is diverse. However, two substantial gaps weaken the evidence: (1) the practical efficiency claim ("almost as fast as ULR") is entirely unsupported by timing data, and (2) the method is not compared to simple DLR heuristics, making it unclear whether the Hessian information is the source of improvement or merely having per-group flexibility. These are fixable in a revision. On balance, the paper's contributions are above the acceptance threshold, but the current form would benefit from addressing these gaps before publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>