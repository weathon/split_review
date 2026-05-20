Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper derives the first generalization bounds for Kolmogorov–Arnold Networks (KANs) in two settings: when activation functions are linear combinations of basis functions, and when they lie in a low-rank RKHS (Sobolev space). The bounds in the first setting scale with $l_1$ norms of coefficient matrices and per-layer Lipschitz constants while avoiding dependence on combinatorial parameters (number of nodes, basis functions) except logarithmic factors, and accommodate unbounded loss functions via a truncation argument. The low-rank analysis produces bounds scaling polynomially with rank. Numerical experiments on simulated and real data illustrate the correlation between the proposed complexity measure and the excess loss.

## Strengths

1. **First generalization bounds for KANs.** The paper provides rigorous covering-number-based bounds that are non-trivial extensions of MLP bounds (Bartlett et al., 2017) to KANs' additive function-matrix structure. The technical machinery (covering number decomposition in Proposition 1, Maurey's sparsification lemma in Proposition 2) is well-chosen for the KAN architecture. The low-rank RKHS analysis (Section 2.3) appears genuinely novel — the paper correctly notes that comparable results are not available even for MLPs.

2. **Bound avoids combinatorial parameters.** Theorem 1 shows the log covering number scales as $\tilde{\alpha}^3 \log(2\tilde{d}\tilde{p})/\epsilon^2$, where $\tilde{\alpha}$ depends on $l_1$ norms $B_i$ and Lipschitz constants $\rho_j$ but not on the number of nodes or basis functions except through a logarithmic factor. This directly delivers on claimed contributions (iii) and (iv).

3. **Unbounded loss functions handled via truncation.** Theorem 3 extends the bounds to a general class of unbounded regression-type losses (Assumption 4: squared loss, pinball loss, Huber loss) using a truncation argument — an improvement over the bounded-loss assumption required in Bartlett et al. (2017). Corollaries 1–2 provide excess risk bounds under weak moment conditions.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Empirical section lacks statistical rigor.** Only a single training run is reported per dataset with no error bars or multiple random seeds. For a claim that the complexity measure "tightly correlates" with excess loss, the absence of quantified correlation coefficients (e.g., Spearman rank correlation) and variance estimates weakens the empirical support. This does not undermine the theoretical contributions but does limit the strength of the empirical claims. The paper explicitly acknowledges the experiments as illustrative (Section 4 discusses this as future work), but the text describing Figure 2 overstates confidence.

2. **Figure labeling is ambiguous.** The paper defines excess loss as the difference between test loss and training loss (line 285), but the figure description (line 306) labels curves as "Test Loss (blue line), Train Loss (orange line), and KAN Complexity (yellow line)" — showing test and train loss separately rather than their difference. If the complexity curve is plotted against test loss rather than the gap, the relationship to the bound (which concerns excess risk) requires explicit justification. The normalization procedure (max of complexity = last value of excess loss) is a reasonable single-parameter scaling for visualization, but the paper should clarify what is actually plotted and why.

3. **Exponential depth dependence in bounds is acknowledged only implicitly.** The quantity $\tilde{\alpha}$ (and analogous terms in Theorems 4–5) contains products $\prod_{j=i+1}^L \rho_j$ that can grow exponentially in depth. This is a known limitation shared with comparable MLP bounds (Bartlett et al., 2017), but the paper would benefit from a brief discussion of when the bounds are informative (e.g., when per-layer Lipschitz constants are close to 1 or when depth is small) to help readers gauge practical applicability.

### Trivial

- The description of the normalization in Section 3 ("see Section A.4 for more details") cannot be verified because the appendix is omitted from the submission. Given the centrality of this figure to the empirical claims, the normalization procedure should be self-contained in the main text.

## Nice-to-Haves

- Report the raw (unnormalized) complexity measure values alongside the normalized ones so readers can assess scale relative to loss values.
- Add a brief discussion of how the Lipschitz constants $\rho_j$ are estimated in practice (Remark 5 gives an upper bound, but empirical tightness is unknown).
- Provide a concrete small-scale example (e.g., 2-layer KAN with B-splines) where the bound is computed explicitly and compared to the empirical generalization gap.

## Removed Points

- **Normalization as "fatal flaw" (Harsh Critic #1, main claim).** The criticism that normalizing the complexity measure so its maximum equals the last value of excess loss "trivially makes the curves appear aligned" is factually incorrect. A single scalar scaling factor cannot fabricate shape correlation over 1000 epochs — it only sets the y-axis scale. The curve shapes are entirely determined by the raw complexity values. *Removed as factually wrong.*

- **Lipschitz constant estimation concern (Harsh Critic #4).** The paper uses upper bounds from Remark 5 to estimate $\rho_j$, which is a principled and transparent approach. Asking whether this bound is "tight" is a reasonable question but not a weakness of the current paper — the estimation method is clearly stated. *Demoted to Nice-to-Have.*

- **"No reproducibility" / missing hyperparameters (Harsh Critic, implied).** The paper states clear experimental parameters (sample sizes, network shapes, 1000 epochs, SGD) and the appendix (stripped) presumably contains additional details. For a theory paper with illustrative experiments, this is sufficient. *Removed.*

- **Strength Finder strength #4 (Empirical validation).** The strength finder claimed the empirical validation as a core strength. Given the single-run nature and the normalization ambiguity, this is overstated. *Moved to Removed Points.*

## Novel Insights

The harsh critic and strength finder are largely in agreement on the core assessment: the theoretical contribution is solid and novel, while the empirical section is weak. Neither reviewer identified a hidden flaw in the proofs, and both acknowledged the extension of covering-number bounds to KANs as non-trivial. The main tension — whether the normalization invalidates the empirical claims — resolves in the paper's favor once one recognizes that a single scaling factor cannot manufacture curve-shape correlation. Beyond the paper's own contributions, no genuinely novel observation emerges from the reviews.

## Suggestions

1. Clarify what Figure 2 actually plots: if it shows excess loss (test − train), label it accordingly; if it shows test loss separately, explain why the complexity measure tracks test loss rather than the gap, and adjust the claim to match.
2. Add quantified correlation coefficients (Spearman rank correlation between the complexity measure and excess loss at each epoch) and include at least 3–5 random seeds with error bands to demonstrate reproducibility.
3. Add a brief paragraph in Section 2.2 or 4 discussing the exponential depth dependence — a single sentence noting that the bound is informative when the product of per-layer Lipschitz constants is moderate (as is typical in practice with normalized activations and small depths) would suffice.
4. Move the normalization description from the appendix into the main text to make Section 3 self-contained.

## Score and Decision

**Score calibration:** Round 1 bracketing placed this paper between the low-scoring KAN/neural-network papers (scores 2.3–3.0) and top-tier generalization theory papers (scores 7.6–8.5). The narrow band of plausible scores was [4, 7]. Round 2 narrowing against anchors in the 5.0–7.5 range produced the following comparisons:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| *Provable Data-driven Hyperparameter Tuning* (9D9VoONnn6) | 5.67 (Reject) | This paper has stronger, more coherent theory and addresses a more timely architecture; experiments are weaker but theory is the primary contribution. |
| *Slicing Mutual Information* (Piod76RSrx) | 5.50 (Reject) | Similar theoretical depth but this paper's KAN bounds are the first of their kind and more clearly executed. |
| *Compute-Optimal LLMs* (MF7ljU8xcf) | 6.00 (Poster) | Comparable structure: strong theory with flawed-but-illustrative experiments; the KAN paper has slightly less polished experiments but the theory is novel for the architecture. |
| *Generalizability of Neural Networks* (8wAL9ywQNB) | 6.60 (Poster) | More comprehensive empirical validation but less architectural novelty. |
| *Fantastic Generalization Measures* (NkmJotfL42) | 7.00 (Poster) | Tighter contribution with clean experiments and a provocative finding; the KAN paper is less impactful in its empirical message. |

The paper sits closest to the 6.0 anchor: genuine theoretical novelty (first KAN generalization bounds) with an empirical section that has real but correctable weaknesses. The theory is the primary contribution and it stands on solid ground.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>