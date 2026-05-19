- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6
Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

The paper addresses neural subset selection — predicting an optimal subset \(S \subseteq V\) — and argues that prior methods do not fully leverage superset \(V\) information when modeling the utility function. The authors develop a theoretical framework using invariant sufficient representations under a nested permutation symmetry group, and propose **INSET**, which adds an explicit pooled representation of \(V\) to the representation of \(S\). Experiments on product recommendation show strong improvements (10/12 categories), with additional qualitative results on anomaly detection and compound selection.

## Strengths

- **Theoretically grounded motivation for including superset information.** The paper formally defines the wreath-product symmetry group for \((S,V)\), connects it to invariant sufficient representations (Definitions 3.1–3.3, Theorem 1, Corollary 1), and shows that modeling \(P(Y|S,V)\) reduces to learning a function of an invariant sufficient statistic \(M(S,V)\). This provides a principled justification — not merely a heuristic — for why the superset should be explicitly incorporated. The paper acknowledges (lines 128–144) that the specific construction is simple and related to prior empirical approaches, but derives it from first principles.

- **Consistent and often large-margin empirical gains on the fully visible task.** On product recommendation (Table 1, 12 Amazon categories), INSET outperforms all baselines in 10/12 categories, with substantial margins (e.g., Toys: 0.769 vs. 0.684 for EquiVSet; Bath: 0.862 vs. 0.764; Feeding: 0.885 vs. 0.819). These results are complete with means and standard deviations over 5 runs, and directly validate the paper's central claim.

- **Ablation study isolating the effect of information aggregation from parameter count.** Table 3 (CelebA) shows that increasing EquiVSet's capacity (EquiVSet v1/v2) yields marginal gains (0.549 → 0.560), while INSET achieves 0.580 with fewer parameters than the larger variant. This rules out the alternative explanation that gains are simply due to added capacity.

- **Demonstrated faster convergence.** Section 4.5 reports (qualitatively, with figures) that INSET reaches EquiVSet's best performance by epoch ~18 and approaches its own optimum by epoch ~25, whereas baselines require ~40 epochs. This is a practical benefit beyond final accuracy.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by visible evidence and the theoretical framework is sound, though some presentation issues exist (see Minor).

### Minor

- **The theoretical apparatus is disproportionate to the actual method.** The paper develops sophisticated machinery (wreath-product groups, invariant sufficient representations, Theorem 1) but the implementation reduces to \(\theta(S,V)=\sigma(\theta_1(\sum_{s\in S}\phi(s))+\theta_2(\sum_{v\in V}\phi(v)))\). This is effectively a DeepSet over \(S\) plus a DeepSet over \(V\), combined via addition. Proposition 4 permits any combination that yields an invariant representation; the choice of addition is not derived from the theory. The paper acknowledges this (lines 144) but the abstract and introduction frame the contribution as theory-driven in a way that overstates the gap between prior work and the proposed method. This mismatch weakens the narrative.

- **The claim that prior methods "overlook" superset information is imprecise.** The paper states that baselines "approximate the function \(F(S_i,V)\) using only the explicit subsets \(S_i\)" (line 61). However, in practice, DeepSet for set selection encodes **all** elements of \(V\) and then selects \(S\); Set Transformer uses self-attention over all elements of \(V\); EquiVSet learns \(P(S|V)\) conditioned on \(V\) via an equivariant encoder. The distinction is real — these methods do not explicitly pass a pooled representation of \(V\) into the function modeling \(S\) — but saying they "overlook" or "disregard" \(V\) (abstract, line 38) is an overstatement. A more precise framing would be that they do not *explicitly and jointly* model \(F(S,V)\) with a dedicated superset stream. This does not invalidate the contribution, but it inflates the claimed gap.

- **The experimental table for anomaly detection and compound selection is not present in the parsed text.** Table `\input{tabs/anomaly_protein.tex}` (line 199) is loaded via an external file that the parser did not resolve. This table contains the full numerical results for both set anomaly detection (double MNIST, CelebA, F-MNIST) and compound selection (PDBBind, BindingDB). The paper does report qualitative results (e.g., "23% improvement over EquiVSet on double MNIST," line 197), so the claims are not unsupported, but the full numbers, standard deviations, and per-dataset breakdowns are not verifiable from the provided text. This appears to be a parser artifact rather than an author omission, but it limits the empirical evidence that can be assessed.

- **Limited ablation scope.** The parameter-count ablation (Table 3) is performed only on CelebA. Repeating it on at least one product recommendation dataset would strengthen the claim that gains are from information aggregation, not capacity. Similarly, no ablation compares different combination methods (addition vs. concatenation vs. attention), even though the paper mentions both possibilities (line 144).

- **Limited implementation and hyperparameter details.** The paper does not report network architectures, learning rates, batch sizes, optimizers, training epochs, or whether baselines were re-tuned. While not every detail is required, the absence of basic training configuration information makes reproduction difficult.

### Trivial

- Figure 1 caption refers to "Left" and "Right" but the illustration itself is not visible in the parsed text.

## Nice-to-Haves

- An ablation comparing addition vs. concatenation vs. more complex interaction (e.g., gating or attention) for combining the \(S\) and \(V\) representations would ground the architectural choice in evidence.
- Repeating the parameter-count ablation on a product recommendation dataset would strengthen the generality of the finding.
- Including confidence intervals or significance tests (e.g., paired t-tests) for the product recommendation results, especially on categories with small margins (e.g., Furniture: 0.169 vs. 0.162), would clarify which improvements are statistically meaningful.
- Discussing the connection to PointNet's global descriptor (which similarly pools all elements) would provide useful context given the architectural similarity.

## Removed Points

- **Missing table as a "fatal flaw":** The harsh critic called the missing Table `\input{tabs/anomaly_protein.tex}` a fatal structural failure. This is a parser artifact — the `\input` directive was not resolved by the text extraction, but the table exists in the original submission. The paper also provides qualitative results (23% improvement on double MNIST) without the table. Moved to Minor as a verifiability limitation.

- **"Prior methods ignore V entirely" as a factual error:** The harsh critic argued this is "misleading" and fundamentally wrong. However, the paper specifically states (line 61) that baselines "directly select \(S_i\) from the encoding embeddings of all elements in \(V\), and then input \(S_i\) into feed-forward networks" — i.e., the paper does acknowledge V is used for encoding. The claim is about what function is *approximated* (\(F(S)\) vs. \(F(S,V)\)), not about whether V is used at all. This is a nuanced framing issue, not a factual error. Moved to Minor with a clearer articulation.

- **"The theory does not prescribe addition specifically":** Retained as part of the "disproportionate theory" minor weakness. Not removed, just reframed.

- **Reproducibility nitpicks about undisclosed hyperparameters:** The harsh critic lists missing hyperparameters as a major issue. Per instructions, I weakened this — basic training details are useful but the absence doesn't invalidate the results. Kept as Minor.

- **Strength Finder claim about "empirical superiority across three distinct tasks":** The missing table means this can only be fully verified for product recommendation. However, the paper does report the 23% improvement on double MNIST qualitatively. The strength is retained but I qualified it to "on the fully visible task."

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not make. The key practical insight — that an explicit pooled superset representation improves subset selection — is the paper's own contribution, not a novel synthesis from the reviews.

## Suggestions

1. **Reframe the contribution more precisely.** Replace "overlook superset information" language with a more accurate statement: existing methods use V only implicitly via encoding and do not explicitly condition \(F(S,V)\) on a representation of the full superset. This preserves the novelty claim without overstating the gap.

2. **Provide the missing table** with full results for anomaly detection and compound selection, including means and standard deviations for all baselines.

3. **Add an ablation on combination method** (addition vs. concatenation vs. attention) to justify the architectural choice empirically.

4. **Report basic training details** (architectures, learning rate, batch size, optimizer, epochs, hyperparameter search ranges) to improve reproducibility.

5. **Extend the parameter-count ablation** to at least one product recommendation category to show the finding generalizes beyond CelebA.
