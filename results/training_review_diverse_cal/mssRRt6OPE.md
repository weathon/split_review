Now I have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

---

## Summary

This paper proposes Relevance-Based Embeddings (RBE), a framework where queries and items are represented by their relevance scores to a small set of pre-selected support items, then transformed via simple trainable MLPs to produce dot-product-compatible embeddings for efficient nearest-neighbor search. The paper provides a theorem (in parser-stripped sections) motivating the approach, and empirically evaluates it on ZESHEL (entity linking) and proprietary recommendation datasets, using AnnCUR (Yadav et al., 2022) as the primary baseline. The key findings are that (a) support item selection strategy dramatically affects performance — far from the random selection used in prior work — and (b) a neural transformation on top of relevance vectors yields further improvements.

## Strengths

- **Demonstration that support-item selection is critical and non-random strategies yield large gains (Table 2).** The paper systematically compares random selection, clustering-based methods (KMeans, SpectralClustering, AgglomerativeClustering), popularity-based selection, and a greedy algorithm. Results show that even simple clustering strategies substantially outperform random selection — e.g., on AmericanFootball, greedy selection nearly doubles the HitRate from 0.57 (random) to 0.80. This is a clear and practically valuable finding with immediate applicability.

- **Consistent empirical gains over the AnnCUR baseline (Table 3).** Averaged across five ZESHEL domains and two RecSys datasets, the neural RBE achieves a reported average 33% improvement in HitRate(100) over AnnCUR, with gains ranging from 8% to 69%. The improvement holds across both textual (cross-encoder heavy ranker) and recommendation (gradient boosting heavy ranker) settings, supporting the method's generality.

- **Generality across tasks and heavy ranker types.** The paper evaluates on both zero-shot entity linking (ZESHEL) with a neural cross-encoder as the heavy ranker, and on production recommendation data with a gradient boosting model (CatBoost). Consistent improvements across these diverse settings strengthen the claim that the approach is broadly applicable, not tied to a specific ranker architecture.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the presented experiments, and the identified issues do not invalidate the main results.

### Minor

- **No analysis of support set size sensitivity.** All experiments use |S_I| = 100, but the trade-off between the number of heavy ranker calls (computational cost) and retrieval quality is never explored. Without a sweep of |S_I| (e.g., 10, 50, 100, 200), the reader cannot assess whether the chosen value is near-optimal or whether smaller support sets would suffice for practical deployments. This is the most significant missing analysis.

- **Dual encoder comparison is narrowly scoped and under-specified.** The comparison in Section 4.4 is conducted on only one dataset (RecSysLT), and the dual encoder is described only as "the one that is proved to be the best in this task" — its architecture, training procedure, and feature inputs are not specified. This limits the reader's ability to assess the generality of the comparison or to reproduce it. The paper also relies on prior work (Yadav et al., 2022) for dual encoder comparisons on ZESHEL rather than providing them directly. None of this invalidates the results, but it narrows the evidence base.

- **Headline improvement conflates multiple sources.** The "33% average improvement" cited in the abstract and introduction compares the full neural RBE against AnnCUR (presumably with random support selection, as in the original baseline). However, Table 2 shows that simply improving support selection (e.g., KMeans) already yields 10–20%+ improvements on some datasets, and the neural mapping adds further gains on top. The paper separately analyzes these effects (Tables 2 and 3), which is good practice, but the headline number would benefit from a clearer decomposition to avoid giving the impression that the neural transformation alone accounts for the full 33%.

- **Hyperparameters of the neural RBE are not reported.** The paper uses a 2-layer MLP with ELU activations but does not state the hidden dimension, learning rate, batch size, training epochs, or early stopping criteria. While the paper does not claim optimality ("the transformation that we use is not claimed to be optimal"), the absence of these details makes full reproduction difficult and leaves open the question of whether the reported results are sensitive to these choices.

### Trivial

None that are not parser artifacts.

## Nice-to-Haves

- A sensitivity analysis for |S_I| on at least one dataset, showing the HitRate as a function of support set size and the resulting cost-quality trade-off.
- A comparison on ZESHEL explicitly showing dual encoder results (rather than deferring entirely to Yadav et al., 2022), to make the paper more self-contained.
- Pseudocode or an algorithmic description of the greedy support selection algorithm.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing theorem statement / theoretical gap (Harsh Critic Issue 1):** The reviewer criticizes the absence of a theorem statement and proof. However, Sections 3.1–3.2 were stripped by the PDF parser (line 196 references "Section 3.2," confirming it exists in the original). Per the instructions, weaknesses about parser-stripped content are removed. The speculative concern that the theorem's guarantees would not apply to small support sets is unverifiable from the available text and should not be held against the paper.

- **Demand for additional baselines (distilled dual encoders, ColBERT, cross-encoder+ANN pruning):** The paper's main baseline is AnnCUR, which the authors explicitly note has already been compared against a range of dual encoders in prior work (Section 4.1.3). The paper's stated scope is a method that fits into the standard "embed then search" pipeline without changing the index structure (Section 2, line 41). Methods that change the search index structure (Morozov & Babenko, 2019) are explicitly scoped out. Demanding each of these as baselines amounts to asking for a different, broader paper.

- **Dual encoder comparison is fundamentally "unfair" (Harsh Critic Issue 2, partially):** The reviewer claims the comparison disadvantages the dual encoder. In fact, the paper explicitly gives the dual encoder an advantage — retrieving X+100 items vs. RBE's X items — and states "which gives the former an advantage with small top sizes" (line 220). The comparison is designed to test whether relevance vectors are more useful input features than dual encoder embeddings, not to compare complete retrieval pipelines. The experiment design is reasonable for this purpose.

- **Formatting/style nitpicks (loss function typo `\dot{(}`, notation issues with embedded spaces in `B e s t_{P}`, `H i t R a t e`):** These are PDF extraction artifacts, not errors in the original submission. Removed per instructions.

- **Scalability discussion lacking evidence about downsampling:** The paper mentions "our preliminary experiments show" which is a reasonable non-core claim. This does not constitute a substantive weakness.

- **Reproducibility of AnnCUR baseline:** The paper states that recalculated metrics "are comparable with the metrics from the original paper" (line 140). This is an adequate statement for a non-central detail.

## Novel Insights

The reviews collectively highlight that the paper's most impactful empirical finding — that support item selection strategy dramatically affects performance — is somewhat at odds with the paper's framing as primarily about "relevance-based embeddings as a new paradigm." The 33% headline improvement is a compound effect: better support selection plus neural refinement. The dual encoder comparison, while scoped narrowly, reveals an interesting regime effect: RBE trails at small K (where the dual encoder's 100-item handicap advantage dominates) but overtakes at larger K (where the quality of the relevance-derived representations prevails). This suggests that RBE is most valuable in applications requiring large candidate pools (K ≥ 200–300), which the paper notes matches their production setting. An important insight not fully explored is whether the optimal support set size |S_I| depends on the diversity of the item catalog — clustering-based selection may work well when items naturally cluster (e.g., by category), while greedy selection may be preferable for more homogeneous item sets.

## Suggestions

1. Add a sweep of |S_I| on at least one dataset (e.g., one ZESHEL domain and one RecSys dataset) to show the cost-quality trade-off. This single addition would substantially strengthen the practical utility of the paper.
2. Disambiguate the "33% improvement" claim in the abstract/introduction by noting that it combines the effect of better support selection and the neural refinement. A phrase such as "combining better support selection with neural relevance-based embeddings yields an average 33% improvement" would be more precise.
3. Either specify the dual encoder architecture and training details for the Section 4.4 comparison, or acknowledge the limitations of the vague description. If possible, extend the comparison to at least one ZESHEL domain as well.
4. Report the key hyperparameters (hidden size, learning rate, training epochs) for the neural RBE's 2-layer MLP in the main text or a brief appendix note.

## Score and Decision

The paper presents a well-motivated idea with clearly demonstrated empirical improvements over a strong baseline (AnnCUR). The core finding that support item selection matters is convincingly shown across multiple datasets. The weaknesses are real but incremental — missing ablation on |S_I|, narrow dual encoder comparison scope, and modest specification gaps — none of which threaten the paper's central claims. The paper makes a useful contribution to the relevance retrieval literature.

**Score:** 6.0 — A solid paper with clear contributions and minor limitations addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>