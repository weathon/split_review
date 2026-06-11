Now I'll write the complete final review.

## Summary

This paper establishes a mathematical duality between activation steering and influence functions, showing that to first order, any steering vector can be represented as a signed measure over training data and vice versa. The key contributions are: (i) the Influence-Aligned Steering (IAS) vector Δh* = J_{h→y}† J_{θ→y} Δθ, (ii) the γ diagnostic quantifying subspace alignment between activation and parameter Jacobians, (iii) spectral optimality results for principled steering direction selection, and (iv) generalization bounds for low-rank steering interventions.

## Strengths

1. **Novel formal duality bridging two disconnected fields**: The paper constructs an explicit, mathematically rigorous bridge between activation steering and influence functions — two previously separate research areas. Theorem 4.2 and the IAS construction provide the first closed-form mapping that shows steering vectors and influence-based data weightings are, to first order, projections of the same underlying sensitivity structure. This is a genuinely non-obvious theoretical insight.

2. **γ diagnostic with quantitative bounds and impossibility results**: Theorem 5.1 bounds the relative logit error of steering by √(1−γ²), where γ is the smallest principal-angle cosine between Im(J_{θ→y}) and Im(J_{h→y}). Theorem 6.2 (No-Free-Lunch) proves the converse: when γ is small, no activation-space edit can replicate the effect of data re-weighting. Figure 2 validates this empirically, showing γ increasing from 0.64 at layer 0 to 0.94 at layer 11 in GPT-2 Medium, consistent with the theory's prediction that later layers offer better subspace overlap.

3. **Rademacher-complexity guarantee for low-rank steering**: Theorem 6.1 provides a generalization bound showing that the excess risk from a rank-k IAS correction is bounded by αL√(2k/dn), which vanishes with layer width d and sample size n — a non-trivial guarantee not established in prior steering literature.

4. **Spectral optimality as a principled alternative to ad-hoc vectors**: Theorem 5.3 identifies the top eigenvector of a Fisher-influence matrix Σ as the direction maximizing expected first-order logit change under an ℓ₂ budget, replacing heuristic steering vector construction with a theoretically grounded recipe.

## Weaknesses

### Major

1. **Unexplained slope discrepancy in Figure 1 (1.50 vs. 1.0).** The paper's central empirical validation (Fig. 1) shows a regression slope of 1.50 — the actual logit shift is systematically 50% larger than the first-order prediction. The paper describes this as "consistent with the expected linear regime" and relies only on cosine similarity (0.978) to claim "nearly collinear." However, a slope of 1.50 means the magnitude prediction is off by 50%, which is a large systematic error. Cosine measures only direction agreement, not scale. Since the theory predicts that the IAS vector should match the influence-derived logit shift at first order, a slope of 1.0 would be expected. The paper provides no explanation for this discrepancy (e.g., whether it stems from κ-Lipschitz constant being non-negligible, or whether the "small edit" regime is already violated). Without an explanation, the accuracy of the first-order approximation in the tested regime is in doubt.

2. **Steering-to-data mapping (ρ_s) is advertised but never demonstrated.** The paper prominently claims (Abstract, Introduction, Section 4, Conclusion) that given a steering vector, one can trace back to the "most causal training documents" via the signed measure ρ_s — arguably the most practically valuable contribution. Yet no experiment computes ρ_s, inspects top-weighted examples, or compares against any existing data attribution method (e.g., TracIn, gradient dot products, Koh & Liang's influence functions). This is a major gap between claims and evidence for the paper's flagship practical application.

### Minor

3. **Missing experimental detail for IAS in detoxification (Table 1).** IAS is defined as J_{h→y}† J_{θ→y} Δθ, but the paper never specifies what Δθ is in this experiment. The experimental setup uses 100 prompts (50 toxic, 50 neutral), not training data with influence-based updates, so the source of Δθ is unclear. This makes the experiment unreproducible. Additionally, IAS slightly underperforms CAA on both toxicity (0.0164 vs. 0.0150) and perplexity (13701 vs. 13291), with no standard deviations or significance tests reported.

4. **Spectral direction compared only against random baselines.** Figure 3 compares the spectral direction from Theorem 5.3 only against random directions (p=0.00498, ResNet-50 horse class). There is no comparison against any existing steering construction method (e.g., CAA, difference-in-means, PCA-based directions). Showing that the spectral direction beats random is a minimal sanity check; it does not establish practical utility.

5. **The "small-edit" regime is never precisely quantified.** The paper's scope depends on the "small-edit regime" being valid, but no threshold, condition, or quantitative guidance is given for how small is "small" relative to model scales or how a practitioner can check whether they are operating within it.

6. **Key assumptions stated but not validated.** The paper invokes affine independence (Corollary 1), κ-Lipschitz smoothness (Corollary 2), and the inclusion Im(J_{θ→y}) ⊆ Im(J_{h→y}) for exact matching, but none are empirically checked or discussed. The paper does not indicate how often the inclusion approximately holds across different layers, models, or inputs beyond the single γ curve in Figure 2.

7. **Computational cost of γ is understated.** The paper says γ requires "two small SVDs" (line 154). Computing principal angles between subspaces of logit space (ℝ^m, m ≈ 50k) is more involved — estimating bases for Im(J_{θ→y}) at scale requires multiple Jacobian-vector products beyond the two cited in the cost model. The number of passes needed for a reliable estimate is not stated.

8. **Theorem 6.1's connection to activation steering is tenuous.** The theorem analyzes a weight-space low-rank modification (f̃ = f_θ + αUV^T), claiming it as a "rank-k IAS correction at layer ℓ." Activation steering modifies activations at inference, not weights. The paper does not justify why a bound on weight-space modifications applies to the paper's main activation-steering setting.

### Trivial

9. **No standard deviations in Table 1.** Point estimates alone are insufficient for method comparison.

## Nice-to-Haves

- Demonstrate the ρ_s mapping on a concrete example (e.g., pick a steering vector for detoxification, compute ρ_s, and show/inspect top-weighted training examples).
- Validate the γ diagnostic as a decision rule (test whether steering task performance correlates with γ across layers, using the suggested γ ≥ 0.7 threshold).
- Compare the spectral direction against at least one meaningful steering baseline (not just random).
- Provide pseudo-code for the end-to-end workflow.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing NTK discussion**: The harsh critic faults the paper for not discussing Neural Tangent Kernel. This is a "missing related works" criticism, excluded per policy.
- **"GPT-2 Medium only" as a general criticism**: The paper also uses ResNet-50, and the core contributions are theoretical. The experimental scope is appropriate for a theory paper with supporting experiments. This criticism is weakened.
- **No code/pseudo-code**: Nitpick about reproducibility; excluded per policy.
- **Framing IAS should be "optimal" and outperforming CAA**: The critic claims IAS should not be worse than CAA if it is theoretically optimal. However, the paper does not claim IAS produces better detoxification — it claims IAS provides a principled mapping. This is a strawman criticism.
- **Framing slope 1.50 as "fatal" and "undermines the central empirical claim"**: The central claim is about the theoretical duality and direction alignment, not about achieving unit slope. The cosine of 0.978 supports the direction alignment claim. The slope issue is real and serious (kept as Major weakness #1) but does not invalidate the entire framework.
- **Strength: "Empirical validation of first-order equivalence"** from Strength Finder: The strength findser claims Figure 1 is strong evidence. Given the slope 1.50 issue, this strength is weakened. Removed as it conflicts with a verified weakness.
- **Generic strength framings**: "addressed an important problem" — too generic, removed.

## Novel Insights

The reviewers' most insightful observation is that the slope of 1.50 in Figure 1, if confirmed, reveals that second-order effects systematically amplify the first-order prediction rather than canceling it. This is a non-obvious finding that the paper does not discuss and that has implications for the practical reliability of the first-order approximation. Additionally, the gap between the paper's most touted practical contribution (mapping steering back to training data) and the complete absence of any experiment demonstrating it is a significant disconnect that weakens the paper's impact.

## Suggestions

1. **Explain the slope of 1.50 in Figure 1.** Is the Lipschitz constant κ large? Does the slope approach 1.0 for progressively smaller steering magnitudes? Addressing this is essential for the empirical credibility of the first-order framework.

2. **Demonstrate the ρ_s mapping.** The paper's most referenced practical contribution — mapping steering vectors to causal training examples — must be tested, even qualitatively. Without this, a central advertised application remains purely theoretical.

3. **Specify Δθ in the detoxification experiment** and add error bars or confidence intervals to Table 1.

4. **Compare the spectral direction against meaningful baselines** (e.g., CAA, difference-in-means vectors) rather than only random directions.

5. **Quantify the "small-edit" regime** — provide guidance on how small edits must be for the first-order approximation to hold with known accuracy.

## Score and Decision

**Round-1 bracket**: 4.0 – 6.5 (paper sits between weak anchors at 3.0–3.4 and strong anchors at 7.0–8.0).

**Round-2 anchors** (all read in full):
- "Steering Language Models with Activation Engineering" (5.0, Reject) — Similar topic (activation steering) but is an empirical methods paper. My paper has stronger theory but weaker empirical validation.
- "From Steering Vectors to Conceptors..." (5.0, Reject) — Theoretical steering framework with limited experiments. Similar type of contribution but the duality connection in my paper is more novel.
- "Jet Expansions of Residual Computation" (5.5, Reject) — Closest comparator: theoretical framework (jets/Taylor expansions) with experiments that were deemed insufficient. My paper has better writing and more experiments, but similar experimental gaps.
- "Closed-Form Interpretation of Neural Network Latent Spaces" (5.0, Reject) — Theory paper with limited experiments on simple tasks. My paper has broader scope and stronger experiments.
- "DataInf" (6.0, Accept) — Applied influence function method with thorough experiments across multiple large models. My paper has stronger theory but much weaker experiments.
- "What Data Benefits My Classifier?" (6.4, Accept) — Empirical paper on influence-based data selection with extensive experiments. Much stronger empirical validation than my paper.
- "NeurFlow" (6.5, Accept) — Neural network interpretability framework with thorough validation. More complete experimental story.
- "Incidental Polysemanticity" (5.67, Reject) — Theory+experiments paper on mechanistic interpretability; similar score band but rejected, suggesting ICLR bar is above this range.

**Round-3 anchors**:
- "How DNNs break the Curse of Dimensionality" (6.25, Accept) — Strong theory with rigorous analysis. My paper is less mathematically deep but more directly applicable.
- "Near-Optimal Solutions of Constrained Learning Problems" (5.8, Accept) — Theory paper accepted despite mixed reviews.

**Final judgment**: The paper's theoretical contribution — the formal duality between activation steering and influence functions — is genuinely novel and well-developed. However, the experimental validation has two significant gaps: (1) the unexplained slope of 1.50 in Figure 1 undermines confidence in the first-order approximation's accuracy, and (2) the most advertised practical application (mapping steering to data provenance via ρ_s) is never demonstrated. Compared to accepted papers in the 6.0+ range, the empirical support is insufficiently thorough. The paper is stronger than typical 5.0 reject-level papers due to its novel theory and clean mathematical development, but falls short of the empirical rigor expected for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>