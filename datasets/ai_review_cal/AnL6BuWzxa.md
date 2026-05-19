- Decision: Accept
- Avg Score: 6.60
- Scores: 5, 6, 8, 6, 8
Now I have verified the paper's claims thoroughly. Let me produce the final consolidated review.

---

## Summary

This paper extends the CPCC regularizer (previously used with ℓ₂ centroid distances between classes) to a family of Optimal Transport-based distances (OT-CPCC), enabling the regularizer to capture multi-modal class-conditional distributions. The authors propose EMD-CPCC as the exact generalization, show it recovers ℓ₂-CPCC under Gaussian assumptions, and introduce Fast FlowTree (FastFT), a linear-time approximation that leverages the available label tree to skip tree construction. Empirical results across 7 datasets show that OT-CPCC variants often yield higher TestCPCC (hierarchical precision) than ℓ₂-CPCC, with modest gains on fine-level classification under subpopulation shift.

---

## Strengths

1. **Principled generalization of ℓ₂-CPCC.** Proposition 1 establishes that EMD between two Gaussians with identical covariance equals the ℓ₂ distance between their means, proving that EMD-CPCC subsumes ℓ₂-CPCC as a special case (Section 3.1, Prop. 1). This is mathematically correct — the 1-Wasserstein distance with L₂ ground cost between equal-covariance Gaussians indeed reduces to the mean distance — and cleanly motivates the approach.

2. **More informative gradient signal.** Section 3.3 derives that EMD-CPCC assigns per-pair importance weights (∂ρ\_EMD/∂Z\_{i·} = Σⱼ P\_{ij} (Z\_{i·} – Z'ⱼ·)/‖·‖) whereas ℓ₂-CPCC's gradient is identical for all samples in a class. This difference is concretely demonstrated and provides a sound theoretical reason to expect OT methods to better handle multi-modal distributions.

3. **Novel linear-time FastFT with practical speedups.** Theorem 1 claims Θ((m+n)d) time for FastFT by avoiding quadtree construction (using the given label tree instead). Table 1 confirms it is orders of magnitude faster than exact EMD and competitive with other approximations. On synthetic data (Fig. 3), FastFT shows strong approximation quality at low computational cost.

4. **Consistent improvement in hierarchical precision.** TestCPCC scores (Table 2 / Tab. tab:testcpcc) show OT-CPCC variants achieving the best score on 5 out of 7 datasets, with substantial margins on some (e.g., CIFAR100: ℓ₂ 83.08 → FastFT 93.85). Ablation studies (Fig. 4) across batch size, regularization strength, and architecture consistently show FastFT > EMD > ℓ₂, supporting the robustness of the trend.

---

## Weaknesses

### Fatal
None.

### Major

1. **TestCPCC evaluation compares different ρ metrics across methods, undermining the interpretability claim.**  
   In Table 2 (tab:testcpcc), ℓ₂-CPCC's CPCC is computed using ℓ₂ distances between class means, while OT methods' CPCC is computed using their respective OT distances. Since CPCC measures correlation between the tree metric and the method's *own* ρ, a higher score for OT-CPCC may partially reflect that the OT distance is simply easier to align with the tree metric (e.g., because it uses per-sample information rather than a single centroid), rather than the learned representation being more hierarchically faithful. A method-independent evaluation (e.g., computing CPCC with ℓ₂ distances for all methods, or rank-correlation metrics like Kendall's τ) would be needed to support the claim that OT-CPCC "preserves more hierarchical information" (Section 4.4). The classification/retrieval tables (Tab. 3, 4) are not affected by this bias, but the paper's headline interpretability claim rests partly on the TestCPCC table.

2. **FastFT algorithm description is underspecified.**  
   The paper states that because the tree metric between any two samples from different classes is constant per class pair in the augmented tree, the flow matrix computation reduces to "1d OT greedy flow matching using Alg. 1" (Section 3.2). However, Alg. 1 (Greedy Flow Matching) operates on sorted 1D data — but the paper does not specify *what values* are being sorted or how the constant tree metric per class pair leads to a 1D OT problem. The connection between the constant tree metric and the ordering required by Alg. 1 is not explained. While Theorem 1 asserts equivalence between Alg. 1 and Alg. 2 (bottom-up tree matching), the proof is deferred to the appendix, and the main text does not provide intuition for the reduction. This makes it difficult for readers to assess the algorithm's correctness without the appendix.

3. **Empirical gains on classification/retrieval are modest and inconsistent.**  
   While the TestCPCC gains are substantial, improvements on fine-level accuracy (Table 4) are typically 1–3 points (e.g., CIFAR100 tAcc: ℓ₂ 23.76 → SWD 26.18; BREEDS tAcc: ℓ₂ 45.95 → Sinkhorn 46.87). On coarse-level tasks, OT methods are competitive but not uniformly better (e.g., BREEDS coarse sMAP: ℓ₂ 74.47 → FastFT 92.84 is a large improvement, but on other settings the gains are small). On E13 and E30 TestCPCC (Table 2), ℓ₂ outperforms all OT methods. Standard deviations are referenced to detailed tables but not shown in the main tables, making it hard to assess significance. The paper acknowledges the mixed results on E13/E30 but does not provide a quantitative verification of the hypothesized cause (less multi-modal distributions).

### Minor

1. **GMM multi-modality analysis has a causal ambiguity.**  
   Section 4.2 shows that learned features exhibit multi-modal structure (average optimal GMM components > 1). The paper argues this supports the use of OT distances. However, the GMM analysis is performed *after* training with CPCC, so the multi-modality could be an artifact of the training process itself, not a pre-existing property of the data. The causal direction is unclear.

2. **Gradient heuristic for approximation methods is not ablated.**  
   Section 3.4 states that for SWD, TWD, FT, and FastFT, gradients are computed by treating the flow matrix as constant (stopping gradients through P). The paper acknowledges this is a heuristic (not justified by Danskin's theorem for non-optimal flows) but does not ablate this choice — e.g., by comparing against the full gradient where feasible (Sinkhorn is differentiable) or analyzing the impact of this approximation.

3. **The "lower bounded by ℓ₂" claim is unclearly justified.**  
   The paper states "since all approximation methods provide a P satisfying constraints in Eq. 4 and since EMD is lower bounded by ℓ₂... all OT-CPCC methods are still lower bounded by ℓ₂" (Section 3.1). A proof is referenced to the appendix, but in the main text it is not clear what "lower bounded" means operationally for the approximation methods — an approximate EMD could in principle be smaller than ℓ₂.

### Trivial
None.

---

## Nice-to-Haves

- Report standard deviations in the main classification/retrieval tables (they are currently relegated to supplementary tables).
- Report wall-clock training times for FastFT vs. other OT methods on real datasets, not just synthetic.
- Include a brief intuition in the main text for why the constant tree metric per class pair enables the 1D greedy algorithm, to make the paper self-contained without the appendix.

---

## Removed Points

These points were identified as incorrect, speculative, or out of scope and have been removed from the main review:

1. **"Proposition 1 is mathematically incorrect for the 1-Wasserstein distance."** — This is factually wrong. The 1-Wasserstein distance (with L₂ ground cost) between two Gaussians with identical covariance *does* equal the L₂ distance between their means; a basic result in OT. The critic appears to have confused this with the 2-Wasserstein distance, which has a covariance term.

2. **"The optimal transport plan is not unique, so Alg. 1 and Alg. 2 may give different results without proof."** — While non-uniqueness is technically true, the theorem claims equivalence and proof is in the appendix. This is a speculative claim about material that is not available for review, not a verifiable error in the paper as written.

3. **"Complexity is O(k²·n·d), not linear."** — The paper explicitly acknowledges the min(b², k²) factor is shared by all methods due to batch computation (caption of Table 1). This is standard practice.

4. **"Missing comparisons with other hierarchical methods (hyperbolic embeddings, SEAL, etc.)."** — The paper discusses these in Section 5 (Related Work) and references additional comparisons in the appendix. Per instructions, missing related works are not to be included.

5. **All formatting/style nitpicks and critiques about missing appendix content.** — Parser artifacts and missing appendices (which are present in the original submission) are excluded per instructions.

6. **"Could the metric be measuring a proxy?" and similar speculative concerns without specific anchoring in the paper's content.** — These are general area sweeps, not specific verified weaknesses.

7. **"Gains are within standard deviation (not shown)."** — The paper explicitly references detailed tables with standard deviations (Tab. 4, 5 detailed versions). The main tables report means; this is standard practice for multi-table papers.

---

## Novel Insights

The critical reviews do not surface genuinely novel observations beyond the paper's own contributions. The main tension — that the interpretability evaluation uses method-specific metrics — is a standard evaluation concern, not a novel insight.

---

## Suggestions

1. **Clarify the FastFT algorithm** in the main text: specify what ordering/values Alg. 1 operates on when the tree metric is constant per class pair, and provide a brief sketch of why the reduction to 1D greedy matching works.
2. **Add a common-metric CPCC evaluation** (e.g., compute TestCPCC using ℓ₂ distances for all methods, or use rank correlation) to decouple optimization success from representation quality.
3. **Include standard deviations in the main classification tables** and a brief discussion of statistical significance.
4. **Ablate the gradient-stopping heuristic** for at least one approximation method (e.g., compare against full differentiation through Sinkhorn) to validate the approach.

---
