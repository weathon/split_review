Now I have verified all reviewer claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper presents the first investigation of Linear Mode Connectivity (LMC) for soft tree ensembles. It identifies two tree-specific invariances — **subtree flip invariance** and **splitting order invariance** — beyond the standard permutation invariance shared with neural networks, and shows empirically that accounting for these invariances reduces the interpolation barrier to near zero across 16 tabular datasets. The paper also proposes a modified decision-list architecture that eliminates these additional invariances by design, allowing LMC through permutation-only matching. The core contribution — that architecture-specific invariances are necessary for LMC in tree ensembles — is novel, clearly demonstrated, and practically relevant for model merging.

## Strengths

- **First achievement of near-zero barriers for soft tree ensembles (genuine novelty):** Figure 4 (interpolation curves) shows test barriers dropping to ~0.2–0.5% after accounting for the proposed invariances, across 16 datasets. This is the first demonstration of LMC for tree-based differentiable models, an open question that the paper explicitly identifies.

- **Identification and empirical necessity of two tree-specific invariances:** Section 3.1 defines subtree flip invariance and splitting order invariance, which are unique to tree architectures and have no neural-network analog. Figure 2 (averaged barriers) quantitatively shows that permutation-only matching leaves barriers above 0.8% for oblivious trees at depth 2, while adding these invariances reduces them to ~0.35%, establishing that tree permutation alone is insufficient.

- **Systematic empirical investigation across architectures, depths, and model sizes:** Experiments vary tree depth (D=1–3), number of trees (M=64–1024), architecture type (non-oblivious, oblivious, decision list), and matching method (AM, WM) over 16 datasets. The qualitative trends (barrier decreases with more trees, increases with depth) match known neural-network LMC behavior (citing Entezari et al., Ainsworth et al.), reinforcing the validity of the approach.

- **Split-dataset interpolation shows practical benefits beyond barrier reduction:** Figure 5 demonstrates that interpolating models trained on disjoint class-ratio splits yields test accuracy *above* both individual models when additional invariances are considered — a practically meaningful result for model merging.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Accuracy as the sole barrier metric, without loss-based results, weakens the link to the optimization surface.** The paper defines the barrier C as a generic performance measure (Section 2.1, Eq. 1) and uses accuracy. While accuracy is standard in LMC literature (Ainsworth et al., Entezari et al. both primarily report accuracy barriers), the paper's theoretical motivation (stability of non-convex optimization) is fundamentally about the loss surface. Accuracy thresholds can hide loss humps. Reporting loss barriers would make the results directly comparable to the full LMC literature and strengthen the claim that the models lie in a connected basin of low loss. The interpolation curves (Figure 4) are flat and suggestive, but loss curves would be definitive.

- **Missing ablation of the node-wise weighting scheme in matching (Section 3.2).** The paper introduces a weighting strategy (weighting each splitting node by the number of leaves it affects) and states it is applied "for better matching" (line 149). However, no experiment compares barrier results *with* versus *without* this weighting. Since the matching cost already involves searching over flip/order patterns, an ablation is needed to attribute barrier reduction to the invariances rather than to the weighting heuristic. Fixable: run WM on a subset of datasets with and without weighting.

- **Decision-list efficiency claim is not supported by empirical measurements.** The paper motivates the modified decision list by stating that considering additional invariances is "computationally expensive" (line 45) and that the decision list enables "efficient matching" (line 176). However, all experiments use shallow trees (D ≤ 3) where brute-force over flips is trivial (2^(2^D−1) ≤ 128 patterns), and no runtime or wall-clock measurements are provided. The paper does provide theoretical complexity analysis (lines 161–163) and acknowledges that deep perfect binary trees are rarely used in practice (lines 310–311), but the efficiency claim remains an untested assertion rather than a demonstrated result. Adding runtime comparisons for at least one dataset at D=4 would resolve this.

### Trivial

- **No per-dataset results in the main text.** The main results are all averaged across 16 datasets. Showing representative per-dataset curves (as in Figure 4 for oblivious trees) is good, but the paper would benefit from a table or brief discussion of the range of barriers across datasets. (The authors note these are in supplementary material.)

- **No formal paired statistical test across datasets.** The paper reports means and standard deviations, but does not provide a paired test (e.g., Wilcoxon signed-rank) to confirm that the barrier reduction from additional invariances is significant across datasets. Some comparisons (e.g., Figure 2, depth 2 non-oblivious trees with WM: Perm 0.811±0.333 vs Ours 0.455±0.105) show overlapping error bars. Adding a sign test or effect size would preempt doubt.

## Nice-to-Haves

- **Loss-barrier results** would strengthen the connection to the optimization surface (as discussed above).
- **Ablation of the weighting scheme** to confirm that the barrier reduction is driven by the invariances, not the weighting heuristic.
- **Runtime measurements** for decision list vs. perfect binary tree matching at D≥4 to substantiate the efficiency claim.

## Removed Points

- **"LMC literature uniformly uses loss, not accuracy" (from Harsh Critic Point 1):** Factually incorrect. The cited literature (Ainsworth et al. 2023, Entezari et al. 2022) primarily reports accuracy barriers. The paper's barrier definition (Eq. 1) is general and explicitly notes that loss can be used by reversing the subtraction (line 71). This criticism has been removed and the valid kernel (loss would strengthen) is preserved in Minor weaknesses above.

- **Generic criticisms about hyperparameter selection, missing confidence intervals, and missing related work:** These are either standard practice in the field (single-run evaluation, training accuracy-based hyperparameter selection is common) or not verifiable without external sources. Removed per the filtering guidelines.

- **Criticism that MLP comparison is "not central" and should be de-emphasized:** The comparison is presented as a sanity check (Table tbl:mlp), and the paper explicitly notes the architectural differences. It is not overclaimed. Kept as presented is fine.

- **"No discussion of alternative matching algorithms":** Not necessary for the paper's scope. The use of LAP is standard and the paper acknowledges recent gradient-based alternatives (line 74). Removed.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder converge on the same assessment: the paper correctly identifies the key issue (tree-specific invariances beyond permutation are necessary for LMC), demonstrates it convincingly, and proposes a practical architectural variant. No reviewer uncovered a dimension or implication that the paper itself does not address.

## Suggestions

1. **Add loss-barrier results** (or at least a clear discussion of why accuracy is sufficient as a proxy) to address the standard metric concern.
2. **Run a weighting ablation** on 2–3 datasets (with vs. without leaf-count weighting in WM) to confirm that barrier reduction comes from invariances, not the weighting scheme.
3. **Provide runtime measurements** for decision list vs. perfect binary tree matching at depth 4 or 5 on one dataset, to substantiate the efficiency claim.
4. **Include a per-dataset barrier table** (even a small one) in the main text, and add a simple paired sign test across the 16 datasets for the Perm vs. Ours comparison.

## Score and Decision

This paper makes a genuine, novel contribution: it identifies tree-specific invariances and shows that accounting for them enables LMC for soft tree ensembles — a setting where LMC had not been previously achieved. The experimental design is thorough (16 datasets, multiple architectures, depths, tree counts, and matching methods). The weaknesses are addressable (missing ablation, missing loss results, missing runtime data for the decision list variant) and do not threaten the core contribution. No fatal or major issues exist.

**Score: 7.5**  
**Decision: Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>