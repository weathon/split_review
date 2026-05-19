- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces **Corr2Cause**, the first benchmark dataset designed to test *pure causal inference* in LLMs — the ability to determine, from a set of correlational statements, whether a hypothesized causal relation is necessarily true under the Markov equivalence class. The dataset (207K+ samples) is constructed systematically by enumerating all unique DAGs up to 6 nodes, computing d-separation sets, grouping into Markov equivalence classes, and assigning validity labels based on logical necessity across all graphs in the class. The paper evaluates 17 LLMs zero-shot and finetunes many of them, finding that off-the-shelf models perform near-random (best F1=33.38%), and while finetuning produces high in-distribution performance (up to 94.74% F1), it collapses under simple surface perturbations (paraphrasing, variable name reversal), demonstrating that models learn template patterns rather than robust causal reasoning.

## Strengths

- **Novel and well-motivated task formulation.** Section 3.1 defines a task that is fundamentally different from existing causal NLP benchmarks: it tests whether models can reason from formal correlational information to causal conclusions, independent of empirical/commonsense knowledge. This cleanly targets a genuine gap in the literature (Section 1, Figure 1, Related Work).

- **Rigorously grounded dataset construction.** The pipeline (Section 3, Figure 2) is built on formal causal discovery principles: DAG enumeration with isomorphism checks (Section 3.3), d-separation computation (Section 3.4), MEC clustering, and validity labeling by checking necessity across *all* graphs in the MEC (Section 3.5). Table 1 provides comprehensive statistics on unique DAGs (6,325), MECs (2,376), and DAGs per MEC (avg. 2.66), demonstrating systematic coverage.

- **Thorough zero-shot evaluation revealing near-random performance.** Table 2 evaluates 17 LLMs across diverse families (BERT-based NLI, GPT models, LLaMA-based). The best model (BART MNLI) achieves only 33.38% F1, marginally above the random uniform baseline (20.38% F1). Many models perform at or below this baseline, providing clear evidence that current LLMs lack pure causal inference skills.

- **Convincing demonstration of non-robust finetuning.** Table 3 shows that finetuned models achieve high in-distribution performance (RoBERTa-Large MNLI at 94.74% F1) but collapse under two minimal perturbations: paraphrasing (F1 drops to 55.45%) and variable name reversal (F1 drops to 67.87%). This cleanly separates memorization of surface patterns from genuine skill acquisition — the paper's most important finding.

- **Fine-grained analysis by causal relation type.** Tables 4a/4b break down performance across six causal relation types (Is-Parent, Has-Collider, etc.), revealing uneven robustness (e.g., Is-Descendant drops to 29.41% F1 after variable refactorization). This provides concrete diagnostic signal for future research.

- **Open-sourced data and perturbed test sets.** The dataset and perturbed variants are publicly released, enabling community benchmarking and reproducibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The reported experimental results are from a pre-deduplication version (v1.0), while the released dataset is v2.0.** The footnote on line 222 states that v2.0 is "a random sample half of the size" and that "the modeling results in the experiment section roughly hold." This hedge is somewhat imprecise — the exact numbers reported in Tables 2 and 3 may shift on the deduplicated version. While the core claims (near-random zero-shot, fragile finetuning) are robust enough that minor score changes would not alter the conclusions, the mismatch between reported and released data is a presentation concern that should be clarified.

- **The test set is relatively small (1,162 samples) given the diversity of graph sizes and relation types.** The paper explains this is due to API query costs, and the split strategy is reasonable. However, the small test set (particularly the 522 samples for N=6, which dominates the dataset) means that fine-grained comparisons (e.g., per-relation-type breakdowns) have limited statistical power. This does not undermine the main claims but is worth noting for users of the benchmark.

- **The OOD evaluation is limited to two surface-level perturbations (paraphrasing templates, reversing variable names).** The results are already striking, but the claim of "fragile generalization" would be strengthened by additional perturbation types (e.g., reordering correlation statements, adding irrelevant variables, modifying graph sizes unseen in training). The paper acknowledges this implicitly by recommending future work, so this is a scope limitation rather than a flaw.

### Trivial
- The note about v2.0 states "the current version is a random sample half of the size of the original version" — the phrase "random sample" here refers to dropping symmetric duplicates, not random subsampling, which could be phrased more precisely.
- There is a minor typo ("Precison" instead of "Precision" in Table 3 header).

## Nice-to-Haves
- Including results on the deduplicated v2.0 test set to exactly match the released data would improve reproducibility.
- A broader range of OOD perturbations (e.g., changing graph sizes, reordering correlation statements) would further strengthen the generalization analysis, though the current results are already convincing.
- Reporting whether zero-shot performance correlates with model scale within model families would be informative.

## Removed Points
- *Criticism about underspecification of zero-shot evaluation details (prompts, NLI model adaptation) in the main text.* The paper references the appendix (`\cref{appd:implementation}`, `\cref{appd:optimization}`) for these details. Since the appendix exists in the original submission and was stripped by the parser, this is not a valid weakness.
- *All generic or speculative concerns from the harsh critic (e.g., "could confounders be uncontrolled?", concerns about unverified experimental setup).* These were area-of-concern probes, not grounded in specific verified issues in the paper.
- *Generic "reproducibility" nitpicks* — the paper references appendix for implementation details, which is standard practice.

## Novel Insights
The most insightful finding from the review process is how the *contrast* between high in-distribution finetuning performance and near-random zero-shot performance creates a uniquely clear diagnostic: the fact that GPT-4 (29.08% F1) performs worse than several smaller models, and that finetuned models collapse under trivial variable-name reversal, together rule out the hypothesis that these models are doing any form of latent causal reasoning. The fine-grained analysis further reveals that certain relation types (Is-Descendant, Is-Ancestor) are disproportionately fragile under perturbation — a specific diagnosis that could guide architectural or training interventions. None of these insights go beyond the paper's own carefully presented findings, but the review confirms their evidentiary strength.

## Suggestions
1. **Explicitly retrain and report results on the v2.0 deduplicated data** so that the published numbers exactly match the released benchmark.
2. **Add at least one more OOD perturbation** (e.g., reorder the correlation statements, or increase the number of variables) to broaden the robustness analysis.
3. **Clarify the phrasing** around the v1.0→v2.0 transition so readers understand that the "random sample" refers to the effect of symmetry-based deduplication, not arbitrary subsampling.
