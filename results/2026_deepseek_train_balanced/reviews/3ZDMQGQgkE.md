## Summary

This paper introduces *preference discerning*, a paradigm for sequential recommendation where the model conditions on user preferences expressed in natural language within its context. The authors construct a five-axis benchmark (preference-based recommendation, sentiment following, fine-grained steering, coarse-grained steering, history consolidation) using LLM-generated preferences from user reviews. They propose Mender, a multimodal generative retrieval model that fuses pre-trained language encoders with semantic IDs (from RQ-VAE), and demonstrate that Mender improves over existing baselines with relative gains of up to 45% on recommendation and 70.5% on fine-grained steering.

## Strengths

- **Comprehensive five-axis benchmark with well-motivated axes.** The benchmark (Section 3.2) evaluates preference discerning across five distinct scenarios, each with a formally specified construction procedure. The sentiment-following axis is particularly well-designed, using a combined hit-rate metric $m = \mathbb{1}_{C^{+}}(i) \land \neg\mathbb{1}_{C^{-}}(i)$ that tests whether the model retrieves an item for a positive preference while withholding it for a negative preference—directly targeting a capability prior work (Sanner et al., 2023) found models lack.

- **Mender achieves substantial quantitative improvements.** MenderTok reports relative improvements of up to 45% on the recommendation axis and 70.5% on fine-grained steering over existing baselines (Section 4.2). These margins hold across four datasets (Beauty, Sports and Outdoors, Toys and Games, Steam) and across complementary metrics (NDCG@5, NDCG@10, Recall@5 reported in Table 1).

- **Fine-grained steering emerges without explicit training on certain datasets.** Section 4.2 and Figure 3 show that on Amazon datasets, fine-grained steering capability arises as a byproduct of training solely on preference-based recommendation data. This is a non-trivial finding, and the paper honestly distinguishes the Steam dataset where this emergence does not occur, offering a concrete hypothesis about data distribution differences.

- **Ablation studies cleanly isolate architectural contributions.** Section 4.3 (Figure 5 right) compares conditioning on preferences only, items only, or both, providing clear evidence that the full Mender architecture (preferences + items in language) outperforms either component in isolation.

- **Data mixture ablation provides actionable findings.** The experiments with MenderTok variants (Pos, Neg, Pos-Neg, Fine, Coarse, All) demonstrate that (a) sentiment following requires joint training on both positive and negative pairs, (b) coarse-grained steering requires dedicated training data and does not emerge naturally, and (c) training on all data maintains recommendation performance while improving all axes. These results inform future research on training composition.

## Weaknesses

### Fatal

None.

### Major

- **Representation-space overlap between benchmark construction and model creates an unresolved confound.** The benchmark matches preferences to ground-truth items via maximum cosine similarity in Sentence-T5 embedding space (Equation 1, Section 3.2). The steering axes use the same mechanism (Equations 2–3). Meanwhile, Mender operates in closely related representation spaces: MenderEmb explicitly uses a Sentence-T5 variant (Su et al., 2023) to encode preferences, and the semantic IDs used by *all* methods (including baselines like TIGER) are derived from Sentence-T5 item embeddings via RQ-VAE (Section 3.3). This creates a concern: to what extent does Mender's performance reflect genuine preference text understanding versus exploitation of embedding-space correlations that the benchmark's own construction encodes? The concern is partially mitigated by the fact that Mender generates discrete semantic IDs (not continuous embeddings), integrates sequential interaction history, and uses cross-attention between text and decoder—so the task is not simply "find the nearest embedding." However, the paper does not include a simple baseline that retrieves items by maximum cosine similarity between preference and item embeddings, which would directly quantify the extent of this shortcut. The authors should either (a) construct the benchmark using a different embedding space, (b) provide evidence the model does not rely on embedding-space matching (e.g., by testing with preferences whose embedding similarity to the target item is low but semantic content is predictive), or (c) include an explicit embedding-similarity retrieval baseline and show Mender outperforms it.

### Minor

- **Preference generation quality is documented without sufficient methodological detail.** The paper states "around 75% of the generated preferences correctly approximate the user's preferences" (Section 3.1) and attributes this to "participans" (participants) but provides no information on the number of annotators, the annotation protocol, inter-annotator agreement, or how items were sampled for evaluation. If a quarter of the training preferences are erroneous, understanding the impact on downstream training is important. The paper should clarify whether this 75% figure applies to the benchmark (where preferences are matched via cosine similarity, potentially filtering out erroneous ones) versus the raw training data.

- **LC-REC is evaluated without its standard auxiliary tasks.** The paper notes that "LC-REC usually requires auxiliary tasks to align the two spaces properly" and omits them (Section 4.1). While this choice is transparent and defensible (the comparison demonstrates Mender's advantage without requiring extra training objectives), the paper would benefit from reporting what LC-REC achieves *with* auxiliary tasks, or at minimum discussing how performance would change. As presented, the comparison shows Mender outperforms a stripped version of LC-REC rather than LC-REC as designed in prior work.

- **Preference importance ablation is reported only on Beauty.** The ablation studying the contribution of preferences vs. items vs. both (Section 4.3, Figure 5 right) is presented for Beauty only. Repeating this analysis on at least one additional dataset (e.g., Sports and Outdoors or Toys) would strengthen the claim that the findings are not dataset-specific.

- **Statistical variance is not reported.** Performance numbers are reported as single values without confidence intervals or error bars across runs. While this is common practice in large-scale sequential recommendation evaluation, the presence of variance would improve reliability assessment, particularly for axes where improvements are smaller (history consolidation, sentiment following).

- **What happens to the intermediate timestep preferences?** Algorithm 1 generates five preferences at *every* timestep $t$ for each user, producing $T_u$ preference sets per user. The benchmark uses only the last timestep's preferences. It is unclear whether the intermediate preferences are used in training, discarded, or employed in auxiliary ways—this should be clarified.

### Trivial

- Steam dataset results for sentiment following and steering axes are presented only in figures (Figure 4), making it difficult to extract exact numerical values. The paper should provide the numbers in a table.

## Nice-to-Haves

- A counterfactual experiment where Mender is provided with a preference that has low embedding similarity to the target item but is semantically relevant to the user's history would directly test whether the model genuinely discerns preferences or relies on embedding-space proximity.
- Cross-dataset generalization experiments (e.g., training on one Amazon subset and evaluating on another) could strengthen claims about the paradigm's generality.
- The limitations section (Section 5) could acknowledge the potential embedding-space confound discussed above.

## Removed Points

Points that were considered but removed per the filtering rules:

- **Criticism that sentiment following performance being low invalidates the paper's claims.** Removed because the paper is transparent about this limitation ("all current models struggle with sentiment following... presents an interesting avenue for future research"). This is a finding, not a flaw.
- **Criticism about novelty (distinction between generated preferences and raw text not clearly articulated).** Removed because the paper does distinguish this in the introduction ("these approaches do not allow the model to be dynamically steered by user preferences in their context during inference") and related work section.
- **Miscellaneous style/formatting nitpicks and parser artifacts (e.g., "participans," garbled equation formatting).** Removed per rule that these are parser errors, not author errors.
- **Suggestions about missing appendix content or unreleased artifacts.** Removed per rules about appendix stripping and existence assumptions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an explicit embedding-similarity retrieval baseline.** Compute the cosine similarity between the preference embedding (from Sentence-T5) and all candidate item embeddings, and retrieve the top-k items. This baseline will directly quantify how much of the performance gap can be explained by embedding-space correlations and provide a cleaner interpretation of Mender's gains.

2. **Report the 75% preference accuracy with proper methodological detail.** Include the number of annotators, annotation protocol, sampling procedure, inter-annotator agreement, and a breakdown by dataset. Also clarify whether this accuracy measure applies to raw generated preferences or to preferences after the cosine-similarity matching filter used in the benchmark.

3. **Document what language encoder MenderTok uses.** The paper states MenderTok uses a "pre-trained language encoder" but does not specify which one (e.g., T5, BERT, RoBERTa). Since the confound concern depends on whether this encoder shares a representation space with the benchmark's embedding model, specifying the encoder is essential for evaluation.

4. **Repeat the preference importance ablation on another dataset.** Showing that the "preferences + items > either alone" result holds across multiple datasets would strengthen the architectural claim.

5. **Discuss the choice of auxiliary tasks for LC-REC in more detail.** Specify what performance LC-REC would likely achieve with auxiliary tasks, or report those results, to ensure the comparison is informative for practitioners.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>