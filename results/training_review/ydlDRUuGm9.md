Now I have all the information needed. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me now produce the final review.

---

## Summary

This paper provides a theoretical and empirical comparison of Kolmogorov-Arnold Networks (KANs) and MLPs. Theoretically, it proves that any ReLU$^k$ MLP can be exactly represented by a KAN of comparable size (Theorem 1), and conversely that any KAN without SiLU can be represented by an MLP with width scaling $O(GW)$ (Theorem 2), establishing that KANs are at least as expressive as MLPs and potentially more parameter-efficient for large grid sizes. Empirically, the paper investigates spectral bias, showing through experiments on 1D frequency fitting, Gaussian random field regression, and PDE solving that KANs appear to learn high-frequency components faster than MLPs, with a theoretical analysis (Theorem 3) of a simplified single-layer KAN providing a bound on the Hessian condition number.

## Strengths

1. **Exact representation theorem (Theorem 1)** — Proves that any ReLU$^k$ MLP (width $W$, depth $L$) can be exactly represented by a KAN (width $W$, depth $\leq 2L$, grid size $G=2$). This is a clean, non-trivial construction establishing that KANs are at least as expressive as MLPs, providing a rigorous foundation for comparing their approximation capabilities.

2. **Parameter-efficiency insight (Theorem 2)** — Shows that a KAN without SiLU can be represented by an MLP only if the MLP width scales as $O(GW)$. Since the KAN parameter count scales as $O(GW^2L)$ versus $O(G^2W^2L)$ for the MLP, this provides concrete theoretical evidence that KANs with large grid sizes can be more parameter-efficient for certain function classes.

3. **Approximation rates for KANs on Sobolev spaces (Corollary)** — By combining Theorem 1 with existing optimal approximation rates for ReLU networks, obtains $O(L^{-2s/d})$ convergence for very deep KANs, matching the superconvergence phenomenon known for ReLU$^k$ networks and placing KAN theory within the broader approximation theory literature.

4. **Hessian eigenvalue bound (Theorem 3)** — For a single-layer KAN without SiLU, proves the condition number of the least-squares Hessian is bounded by $Cd$ (independent of grid size $G$), contrasting with the $n^4$ scaling reported for two-layer ReLU MLPs. While the relevance of this simplified model to practical KANs is debated, the result itself is mathematically sound and provides a starting point for understanding KAN optimization.

5. **Experimental investigation of spectral bias** — The paper conducts experiments across three distinct settings (1D waves, Gaussian random fields, PDE solving) that consistently show KANs achieving better performance on high-frequency components than comparably-sized MLPs. The PDE example in particular shows KAN errors remaining stable as frequency increases from $k=2$ to $k=32$, while MLP errors degrade sharply. The paper also provides practical observations about grid size selection and overfitting behavior.

## Weaknesses

### Fatal
None.

### Major

1. **The spectral bias theory (Theorem 3) analyzes a model that does not reflect the KAN architecture used in experiments.** The analysis considers a single-layer KAN with no SiLU nonlinearity ($w_b=0$), which is a linear model (Equation 4.1). This is fundamentally different from the multi-layer KANs with SiLU activations used throughout the experimental sections. The paper acknowledges this on line 155 ("necessarily highly simplified and heuristic"), but the gap is not merely one of complexity: it compares a *linear* basis-function model to a *nonlinear* multi-layer network, and the comparison to a two-layer ReLU MLP's $n^4$ condition number (line 151) is between models at fundamentally different levels of nonlinearity. The analysis therefore does not establish that the specific architectural innovations of KANs (compositional depth, SiLU nonlinearity) are responsible for reduced spectral bias — it only establishes that B-spline basis regression is well-conditioned, which is a known property of splines.

2. **No ablation isolates grid extension from the KAN architecture itself.** The GRF and PDE experiments use grid extension as part of the KAN training procedure (line 248: KANs trained with grid sizes $(10,20,30,40,50)$, each for 100 LBFGS iterations), but there is no control experiment comparing KANs with and without grid extension. Similarly, the 1D wave experiment does not separate whether the reduced spectral bias comes from the B-spline basis, the SiLU, the compositional depth, or the grid extension. Without such ablations, the paper cannot attribute the observed performance differences to a specific architectural property of KANs rather than to the well-known multi-resolution capability of spline bases.

### Minor

1. **No discussion of how the SiLU nonlinearity affects the spectral bias picture.** The theory explicitly assumes $w_b=0$ (no SiLU) because it needs a linear model, but the experiments use the standard pykan implementation which includes the SiLU term. The paper does not address whether the SiLU (a smooth nonlinearity that could introduce spectral bias similar to MLPs) alters the theoretical conclusions, nor does it experiment with $w_b=0$ KANs to test whether reduced spectral bias persists without SiLU. This creates an unaddressed disconnect between theory and experiments.

2. **The experimental comparisons, while favoring KANs, do not control for model capacity or training procedures.** Across all experiments, KANs and MLPs have vastly different architectures (e.g., 1D wave: MLPs width 128–256, depth 6–10, 80k iterations vs. KANs width 10, depth 3–4, 8k iterations; PDE: MLPs 6×256, 200 iterations vs. KANs 2×10, 200 iterations with grid extension). While the asymmetry in training steps and parameter counts *favors* the MLP baseline (making the KAN result more striking), the lack of controlled experiments means performance differences could arise from any of these confounding factors rather than from spectral bias specifically. The paper would benefit from a setting where parameter counts, depths, and training budgets are matched.

3. **Theorem 3's bound has caveats that are not fully discussed.** The condition number bound is $Cd$ after removing $d'(d-1)$ degenerate eigenvectors. The number of removed eigenvectors grows quadratically with input dimension when $d'>1$, and the effective condition number scales linearly with $d$, which could still pose challenges in high-dimensional problems. The paper notes the degeneracy is "not an artifact" (line 153) but does not discuss how these caveats affect the practical implications of the result.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing KANs with and without grid extension on the 1D wave or PDE task would help isolate whether improved high-frequency learning is due to the multi-level refinement strategy or the KAN structure itself.
- Computing the empirical NTK eigenvalues for a small two-layer KAN (with and without SiLU) would help bridge the gap between the simplified theory and the practical architecture.
- Visualizing the learned B-spline functions after training would provide intuition for how individual activation functions specialize to frequency bands.

## Removed Points

- **Unfair comparison / uncontrolled experiments regarding training iterations**: The harsh critic argued the comparisons are unfair because MLPs get more iterations (80k vs 8k in 1D wave). However, this asymmetry *favors the baseline* (MLP), making the KAN result stronger. Per the hard rule, this criticism is removed. The remaining experimental design concerns (lack of capacity matching, missing ablations) are kept but downgraded to minor.

- **General criticisms about missing appendix, proofs, or references**: These are parser artifacts; the original submission includes them.

- **Generic strengths from Strength Finder** (e.g., "the paper identifies an important open question"): These are generic and do not add specific value; moved here.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's two main results. The representation theorems (Theorems 1–2) suggest KANs and MLPs are surprisingly similar from an approximation perspective — each can be embedded in the other with modest overhead. Yet the empirical results suggest they behave very differently during training. If this disparity is genuine (which remains uncertain given the experimental confounds), it would imply that inductive biases from optimization dynamics can create meaningful practical differences between architectures that are theoretically nearly equivalent in representation capacity. This highlights the importance of studying *training dynamics* rather than just approximation theory when comparing architectures — a point the paper itself raises but does not fully resolve.

## Suggestions

1. Add a controlled experiment matching KAN and MLP parameter counts and training budgets (at least one setting) to isolate the effect of architecture from capacity and optimization. Even if KANs still outperform, this would substantially strengthen the claim.
2. Include an ablation with $w_b = 0$ (no SiLU) on the 1D wave task to test whether the reduced spectral bias depends on the SiLU or arises from the spline basis alone.
3. Include an ablation of grid extension (fixed grid vs. progressive refinement) to separate the contribution of multi-level training from the KAN structure.
4. Soften the claim in the abstract and conclusion from "KANs do not exhibit the same spectral bias" to "KANs exhibit reduced spectral bias in our experiments, and a simplified theoretical analysis provides a candidate explanation," to better reflect the level of support.

## Score and Decision

The paper has a solid core in its representation-theoretic results (Theorems 1–2, Corollary), which are well-stated and constitute a genuine theoretical contribution. The spectral bias investigation is timely and addresses an important question, but the theoretical analysis is overclaimed (it studies a linear model, not KANs as used in practice), and the experiments, while suggestive, lack the controlled comparisons and ablations needed to attribute the observed differences to spectral bias specifically rather than to confounds. The paper would benefit from a more measured framing and targeted additional experiments. In its current form, the spectral bias contributions are not as well-supported as the representation theory.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>