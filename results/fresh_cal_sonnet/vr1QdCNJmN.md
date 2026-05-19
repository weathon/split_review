Now I have a thorough understanding of the paper. Let me run calibration searches to anchor the score.**Round 1 Bracket: 4.5–6.5** (most relevant anchor is REKRLIXtQG at 5.0, a related set-function decomposition paper that was rejected; the paper has stronger theory but weaker experiments than mid-range accepted papers like eepoE7iLpL at 5.67)

Let me read a couple of anchors and then narrow.Now I have sufficient anchors. Let me write the full review.

**Round 1 Bracket: 4.5–6.5** (REKRLIXtQG at 5.0 is the most topically similar anchor).

**Round 2 Narrowing:** The DBD paper has stronger and more applicable theory than REKRLIXtQG (5.0, Rejected), is comparable in theory-to-experiment ratio to udO3k28bEw (5.50, Accepted) and eepoE7iLpL (5.67, Accepted). However, unlike those accepted papers, DBD's experimental design has a structural confound (no general NN baseline) and uses only one real-world dataset with non-standard metrics. The closest anchor is **5.0–5.5**.

---

## Summary

This paper introduces the "difference-of-submodular Bregman divergence" (DBD), which generalizes submodular-Bregman divergences of Iyer & Bilmes (2012b) to arbitrary (non-submodular) set functions via the strong DS decomposition. The key theoretical contributions are: (1) formally establishing that strict submodularity is necessary and sufficient for the identifiability condition of the divergence (Theorem 3.1); (2) extending the divergence to any set function (Theorem 3.1'); and (3) proving that richer generating function classes yield strictly more expressive DBDs (Theorem 3.4). A learnable instantiation via ε-PointNet is proposed and evaluated on MNIST and ModelNet40.

---

## Strengths

- **Theorem 3.1' generalizes to all set functions:** By leveraging the strong DS decomposition (Theorem 3.2, Li & Du 2020), the paper proves that a valid Bregman-like divergence (satisfying non-negativity and identifiability) can be constructed for *any* set function — not just submodular ones. This is a meaningful extension of the prior framework.

- **Theorem 3.4 provides strict expressive-power hierarchy:** The proof that if function class C ⊊ C′ then the induced DBD class D_C ⊊ D_{C′} is clean and uses a clever argument via D_f(X, ∅). This gives formal justification for using richer architectures to obtain more capable divergences.

- **Proposition 2.5 fills a gap in prior work:** The paper explicitly proves that the grow, shrink, and bar supergradients of Iyer & Bilmes (2012b) satisfy the *strict* supergradient condition under strict supermodularity — a condition that the prior work left implicit. This is a necessary correction for the identifiability guarantee.

- **Ablation (Table 2) isolates the benefit of DS decomposition:** For all three supergradient types, "w/ decomposition" consistently outperforms "w/o decomposition" (e.g., grow: 0.675 vs. 0.580 for ε=0), with reduced variance as well. This directly attributes the performance gain to the two-function architecture rather than mere neural capacity.

- **Large empirical improvement over fixed divergences on ModelNet40:** The DBD (e.g., grow supergradient, ε=0.001) achieves Rand index 0.683 vs. 0.046 for facility location and 0.018 for graph cut, confirming that learned divergences substantially outperform fixed set-intersection-based ones on point cloud data where element-level overlap is essentially zero.

---

## Weaknesses

### Fatal
None.

### Major

- **No general permutation-invariant NN baseline — the central empirical comparison is confounded.** The paper compares a *learned* DBD (trained with triplet loss) against *fixed, non-learned* submodular-Bregman divergences from Iyer & Bilmes (2012b). This comparison tests *learning vs. not learning*, not *DBD vs. a general learned alternative*. Any permutation-invariant NN trained identically with triplet loss (e.g., vanilla Deep Sets or Set Transformer of equivalent parameter count) would be expected to vastly outperform the fixed divergences by the same margin. The conclusion in Section 6 that "the PointNet-based difference-of-submodular Bregman divergence … significantly outperformed existing submodular Bregman divergences" is factually correct but is framed as evidence for the DBD *framework*, which is not what the comparison shows. To isolate the contribution of the Bregman/submodular inductive bias, a general learned set-distance baseline trained under identical conditions is essential. This missing baseline is the single most important issue in the paper and currently prevents attributing the observed gains to the framework's structural properties.

### Minor

- **The theoretical necessity of strict submodularity (ε > 0) has no measurable practical consequence.** Theorems 3.1 and 3.1' establish that strict subgradients/supergradients (requiring strict submodularity) are necessary for the identifiability condition. This is the formal backbone of the entire framework. Yet Table 2 shows that ε=0 (not strictly submodular, no identifiability guarantee) performs comparably to ε=0.001, with the paper noting "not statistically significant." The paper briefly acknowledges this but does not discuss its implications — e.g., whether practical near-strict submodularity suffices, or what this tells us about identifiability on finite point clouds. The disconnect between the theoretical necessity and empirical irrelevance of strict submodularity is left unaddressed.

- **The Rand index is used without specifying k, and ARI would be more informative.** Section 5.2 uses raw Rand index as the evaluation metric without ever stating the value of k in k-means. With 40 ground-truth classes and 2,468 test instances, k substantially affects reported values. Additionally, raw Rand index is inflated relative to chance; Adjusted Rand Index (ARI) is the standard in clustering evaluation and would be more interpretable.

- **Quantitative comparison to state-of-the-art clustering methods is absent from the main text.** Line 276 references "(Hamdi et al., 2021)" and "(Liu et al., 2019)" with the qualitative claim that the proposed method "closely approaches" the former and "achieves better performance than" the latter, but no numbers appear in the main text. The parser artifact "C)" at the start of that sentence suggests these numbers are deferred to an appendix table. Without the numbers in context, the significance of the comparison cannot be evaluated.

### Trivial

- None beyond the minor issues above.

---

## Nice-to-Haves

- An empirical hierarchy experiment — training DBDs at each level of the function-class hierarchy (modular → facility location → submodular → DS function) and measuring clustering performance — would directly validate Theorem 3.4's expressive-power claim in a controlled way. This would strengthen the theory-experiment connection considerably.
- Discussion of computational cost (O(N log N) for greedy Edmonds subgradient computation, repeated for all set pairs in k-means) would aid practitioners.
- The K=1 choice in ε-PointNet is restrictive; a brief study varying K (noted as future work in Section 6) would connect the architecture to Theorem 3.4's hierarchy in a more concrete way.

---

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Section 3.2 proof gap (Harsh Critic):** The critic flags that the construction h_Y = h_Y^1 − g_Y^2 ∈ ∂̃_f(Y) is "stated but not proved in the main text." The paper does state "This fact enables us to consider..." (Section 3.2), and the argument follows directly from combining strict subgradient of f^1 with strict supergradient of f^2. A full proof is almost certainly in the appendix (which is stripped by the parser). REMOVED: speculation about missing appendix proof.

- **K=1 restriction as a gap (Harsh Critic):** The paper acknowledges in Section 6 ("optimal hyperparameters … dimension K … were not discussed") that K=1 is a simplification. Treating this as a gap rather than a known limitation is scope creep. REMOVED as a weakness; mentioned in Nice-to-Haves.

- **Missing comparison to Chamfer distance / EMD (Harsh Critic):** The paper does not claim to be a general point-cloud distance learning method; it proposes a theoretical framework for discrete Bregman divergences. Requiring comparison to Chamfer distance is out-of-scope. REMOVED.

- **Figure 1 is "not independent validation" (Harsh Critic):** True by construction, but Figure 1 is explicitly labeled "Illustrative Example" and makes no quantitative claim. Its role is to confirm the learned divergence behaves qualitatively as expected. Removing it from the paper would provide no additional information. REMOVED as a substantive weakness.

- **Abstract overclaims (Harsh Critic):** The phrase "significantly improves performance of existing methods" refers specifically to existing submodular-Bregman divergences; this is factually supported. While framing could be more precise, this is a minor wording issue and not a substantive weakness. REMOVED as a standalone point; merged into the Major weakness.

- **Strength: "addresses an important problem" (Strength Finder):** Generic importance claim without paper-specific evidence. REMOVED.

---

## Novel Insights

The most genuinely novel observation from the combined reviews is the *theory-experiment coherence gap*: the strict submodularity condition (ε > 0) is the formal load-bearing element of the framework — without it, identifiability is not guaranteed — yet Table 2 demonstrates that ε=0 and ε=0.001 are statistically indistinguishable in practice. This pattern is not unique to this paper; it suggests that for point cloud data where sets have many elements, the effective strict submodularity of the smooth ε-PointNet approximation may be functionally satisfied even at ε=0, raising the question of whether the formal strict submodularity requirement matters beyond a measure-zero set of degenerate configurations. This is worth a careful theoretical discussion.

---

## Suggestions

1. **Add a general permutation-invariant NN baseline** (Deep Sets or Set Transformer of equivalent parameter count) trained with identical triplet loss on ModelNet40. This single addition would transform the empirical section from suggestive to convincing.
2. **Report ARI alongside Rand index**, and state the value of k used in k-means clustering.
3. **Add the quantitative comparison to Hamdi et al. (2021) and Liu et al. (2019) in the main text**, not just in an appendix reference.
4. **Discuss the practical implications of ε=0 vs. ε=0.001** in the context of the identifiability theorem — acknowledge what the null result means for the theory-practice gap.

---

## Score and Decision

**Anchor comparison summary:**

| Path | Avg Score | Round | Comparison to paper under review |
|---|---|---|---|
| REKRLIXtQG (Supermodular Rank) | 5.00 | R1 | Similar topic (set function decomposition); this paper has stronger, more applicable theory but similarly limited experiments. Paper is roughly comparable or slightly better. |
| eepoE7iLpL (Neural Subset Selection) | 5.67 | R1 | Accepted; stronger experiments (multiple baselines), weaker theory. Paper has stronger theory but lacks critical NN baseline. |
| udO3k28bEw (Hard Negative Mining) | 5.50 | R2 | Accepted; theory-plus-limited-experiments paper; experiments are more diverse but theory depth comparable. Paper is roughly at this level. |
| jOVfFAxBf6 (SE(2) invariants point clouds) | 5.75 | R2 | Rejected; strong theory, weaker presentation. Paper has comparable theory quality but stronger experiments, similar limitations. |
| t8vJSIsLhC (SMPE) | 6.00 | R2 | Rejected; permutation-equivariance theory paper; stronger empirical breadth. Paper is slightly below this level due to the confounded baseline. |
| 20oxNYWQl9 (Sensitivity Sampling) | 5.75 | R2 | Rejected; theory-plus-experiments paper. Comparable overall quality. |

**Round 1 bracket:** 4.5–6.5.  
**Round 2 narrowing:** The paper sits between udO3k28bEw (5.50) and t8vJSIsLhC (6.00). Its theoretical contributions are genuine and above REKRLIXtQG (5.0), but the missing general NN baseline is a real structural gap — not just a missing ablation. This pulls it closer to the lower end of the bracket relative to accepted papers at 5.5–6.0. Final score: **5.0**.

**Axes evaluation:**
- *Originality:* Good. Extending Bregman divergences to non-submodular set functions via DS decomposition is a genuine and non-obvious contribution.
- *Importance:* Moderate. The problem of defining divergences on discrete sets is real; the practical payoff relative to simpler learned metrics is undemonstrated.
- *Claims vs. support:* Weak on the empirical side — the claimed benefit is over non-learned baselines, not a controlled comparison.
- *Soundness of experiments:* The ablation is sound; the main comparison is confounded.
- *Clarity:* Good overall; some notation is dense but followable.
- *Community value:* The theoretical framework is a useful contribution to submodular ML; the experimental story needs revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>