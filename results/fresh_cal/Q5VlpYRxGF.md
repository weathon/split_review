Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes KVMerger, a KV cache compression method for LLMs that merges similar key-value states rather than discarding them. The approach consists of two components: (1) a greedy contiguous grouping algorithm that identifies sets of consecutive key states with high cosine similarity, and (2) a Gaussian kernel weighted merging function that uses aggregated attention scores to select a pivotal state and merge surrounding states toward it. Experiments on Llama2-7B/13B-chat and Mistral-7B-Instruct across LongBench, ZeroScrolls, and needle-in-a-haystack tests show consistent improvements over H2O and CaM at 50% and 35% cache budgets.

## Strengths

- **Empirically and theoretically grounded key-state similarity observation (Section 3.1):** The paper provides both visual evidence (Figure 2, Figure 3a) showing that key states within a single sequence exhibit high and localized cosine similarity (>90% for some tokens), and theoretical analysis via Lemmas 3.1–3.2 linking this property to RoPE. This observation is a novel complement to prior work on query-state similarity and intra-layer KV similarity, and it directly motivates the merging approach.

- **Demonstration of persistent KV cache sparsity at the model level (Section 3.2):** Figure 3(b) shows that layer-wise compression ratios obtained from the merging set identification algorithm are highly consistent across 200 samples from different LongBench tasks, supporting the claim that KV cache sparsity (from the similarity perspective) can be pre-determined without per-dataset tuning.

- **Consistent superiority over baselines on long-context benchmarks (Tables 1, 2; Figure 5):** KVMerger outperforms H2O and CaM across nearly all evaluated datasets on LongBench (9 tasks) and ZeroScrolls (7 tasks) under both 50% and 35% cache budgets, using three different models. The needle-in-a-haystack results (Figure 5) are particularly compelling, showing that KVMerger maintains high retrieval accuracy across document depths and context lengths where baselines degrade substantially.

- **Principled formulation and well-validated design choices:** The merging set identification is formalized as a constrained clustering problem (Definition 4.1) with temporal locality constraints. Ablation studies (Tables 4 and 5) clearly validate that the Gaussian kernel weighting and attention-based pivot selection each contribute meaningfully over naive alternatives, confirming the design is well-motivated rather than arbitrary.

## Weaknesses

### Fatal
None.

### Major
- **Missing comparison with D2O, a directly competing merging method.** The paper cites D2O (Wan et al., 2024) in the related work section and characterizes it as "highly dependent on previous eviction methods." However, D2O is an independent merging method that selectively merges both key and value states using cosine similarity with an EMA threshold — it is not a post-processing of eviction. Since KVMerger is also a key-and-value merging method, D2O is the most directly related baseline. Its omission from the experimental comparison (Tables 1–2) means the reader cannot assess whether KVMerger's improvements over H2O and CaM translate to advantages over a method that operates on the same principle (merging rather than eviction). The paper should either include D2O as a baseline or provide a principled justification for why comparison is not possible (e.g., different budget definitions).

- **Unclear mechanism for enforcing the exact cache budget.** The paper reports results at 50% and 35% budgets and specifies the proportion of "recent tokens" and "attention-selected tokens" reserved (e.g., 0.17% and 0.12% for 50%), with a fixed cosine similarity threshold of 0.75. However, it does not explain how these components jointly produce the exact target budget. The merging set identification algorithm's compression ratio depends on the distribution of similarity values in the sequence, which varies across layers and inputs. If the threshold is fixed and the achieved compression is merely *approximately* 50% (or post-hoc matched), then comparisons with H2O and CaM — which have well-defined mechanisms for hitting exact budgets via eviction — may not be at truly equal memory footprints. The paper should specify: (a) whether the budget is exact or approximate, (b) the achieved compression ratio per sequence and its variance, and (c) any post-matching procedure used.

- **Dataset selection without justification.** The paper uses 9 of 18 LongBench datasets and 7 of 10 ZeroScrolls datasets without explaining the selection criterion. Since results vary substantially across datasets (e.g., NarrativeQA F1 differences are small, while Mistral results show large gaps), the reader cannot assess whether the chosen subsets are representative or favorable to the proposed method.

### Minor
- **Greedy contiguous grouping mislabeled as "AHC variant."** Algorithm 1 is described as a variant of Agglomerative Hierarchical Clustering, but it is a simple linear backward scan that groups adjacent tokens whose similarity exceeds the threshold. There is no hierarchy, no merging history, and no dendrogram — it is a straightforward greedy contiguous grouping. This framing is unnecessary and potentially misleading; describing the algorithm directly would be clearer and more accurate.

- **Tension between criticizing attention scores as "biased" (Section 3.1) and using them for pivot selection (Section 4.2).** The paper argues that attention-score-driven approaches are "biased" because critical tokens vary across queries. Yet the pivot selection in Algorithm 2 uses exactly these aggregated attention scores. While the paper could argue that pivot selection within an already-identified set of highly similar states is less sensitive to this bias (since any token in the set carries similar information), this tension is not discussed. A brief justification would strengthen the presentation.

- **Broad claim about persistent sparsity based on limited evidence.** The claim that "KV cache sparsity... is independent of the dataset and remains persistent at the model level" is supported by only 200 samples from a single model (Llama2-7B-chat) on two tasks (Figure 3b). The evidence is consistent but the sample is narrow; the claim should be qualified (e.g., "persistent for the tested tasks and model").

- **No measure of statistical significance or variance.** Performance differences on some datasets are small (e.g., NarrativeQA: 18.50 vs. 17.48 with H2O on Llama2-7B at 50%). While the evaluation may be deterministic (given fixed seeds and model), this is not stated. Reporting standard deviations across multiple runs or documenting that results are deterministic with the same seed would allow the reader to assess whether small margins are meaningful.

### Trivial
- None.

## Nice-to-Haves
- Reporting actual memory savings in GB (beyond the percentage budget) would ground the evaluation for practitioners.
- Adding a brief discussion of computational overhead: is the merging set identification performed once after prefill or updated dynamically at each generation step?
- Extending to more recent baselines (e.g., quantization methods like KIVI, which are complementary) would broaden the positioning, though this is not required.

## Removed Points
These points were raised by the reviewers but are removed after verification and filtering:

- **Criticism about Lemma 3.2 not being fully fleshed out** — The lemma is labeled "informal" and provides necessary conditions for high similarity. The level of theoretical analysis is reasonable for an empirical systems paper.
- **Criticism about sigma distribution not being shown in ablation** — Six sigma values are tested and the paper reports that mean computed sigma fluctuates around 5. This is sufficient evidence for the design choice.
- **Criticism about the GQA analysis for H2O being absent** — The paper *does* analyze this on lines 283, explaining that a single averaged attention map dilutes the eviction signal for H2O.
- **Criticism about "the improvement over H2O on some individual datasets is negligible"** — Merged into the broader statistical significance point above.
- **Strength about "addressing an important problem"** — Generic; removed per filtering rules. The remaining strengths are concrete and evidence-grounded.
- **Criticism about computational overhead not being discussed** — This is a reasonable question but is a nice-to-have, not a weakness in the presented results.

## Novel Insights
None beyond the paper's own contributions. The reviewer inputs did not surface a genuinely novel perspective that goes beyond what the paper already demonstrates.

## Suggestions

1. **Add D2O as a baseline** in Tables 1 and 2, or provide a clear justification for why comparison is infeasible (e.g., incompatible budget definitions). This is the highest-priority improvement.
2. **Clarify the budget enforcement mechanism**: specify whether the 50%/35% budgets are exact or approximate; report the achieved compression ratio distribution (mean and range) across sequences for each dataset.
3. **Justify the dataset selection** for LongBench (9/18) and ZeroScrolls (7/10), or report results on the full benchmarks.
4. **Qualify the persistent-sparsity claim** (Section 3.2) to reflect the scope of evidence (one model, two tasks).
5. **Add a sentence addressing the tension** between criticizing attention scores and using them for pivot selection.
6. **Rename or clarify Algorithm 1** — describe it directly as a greedy contiguous grouping rather than an AHC variant.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>