Now I have all the information I need. Let me produce the consolidated review.

## Summary

Mirage proposes a novel graph dataset distillation method for graph classification that mines frequently co-occurring computation trees (as used by message-passing GNNs) and trains on those tree patterns instead of full graphs. The key innovation is that the distillation process is model-agnostic (works across GCN, GAT, GIN without re-distilling) and does not require training on the full dataset, unlike prior gradient-matching approaches. The paper demonstrates competitive accuracy, high compression, and substantial speedups (150× over DosCond, 500× over KIDD) on 6–7 graph classification datasets.

## Strengths

1. **Novel, principled distillation approach that avoids the "counter-objective" problem**: Unlike gradient-matching methods (DosCond, KIDD) that must train on the full dataset to distill, Mirage compresses by mining computation trees directly from the data. This is a genuine conceptual advance. The paper formalizes the problem constraints (Sections 2–3) and Mirage satisfies them: no full-data training needed for distillation, and the distilled set works across architectures.

2. **Model-agnostic results across three GNN architectures**: This is the first graph distillation study to evaluate across GCN, GAT, and GIN. Table 1 shows that a single Mirage-distilled set works for all three, whereas baselines like KIDD (GIN-only) and DosCond (architecture-specific) require re-distillation. The paper delivers on its core claim — a single distilled set suffices for multiple architectures.

3. **Superior compression with competitive accuracy**: Mirage achieves the highest compression in 5/7 datasets (Table 2), often by orders of magnitude (e.g., DD: 448 bytes vs. 209K–409K for baselines). Despite this aggressive compression, Mirage ranks top-1 or top-2 across all 17 dataset-architecture combinations in Table 1, often within 1–2% of full-dataset performance.

4. **Practical CPU-bound efficiency**: The entire distillation pipeline runs on CPU, whereas all baselines require GPU. Figure 1 shows 150× average speedup over DosCond and 500× over KIDD, making the method accessible in low-resource environments.

5. **Empirical validation of the motivating observation**: Figure 2 provides evidence that computation tree distributions are highly skewed (power-law) across diverse datasets, supporting the paper's central insight that a small set of frequent trees captures most of the information.

## Weaknesses

### Fatal
None.

### Major

1. **Orphan table with inconsistent full-dataset numbers (Section 4.3)**: A second, uncaptioned, unlabeled table appears at lines 498–526 (within an unfinished "Impact of Parameters" subsection) that contains full-dataset AUC-ROC numbers for ogbg-molhiv that are dramatically different from Table 1 (66.34/64.78/65.13 vs. 73.71/75.93/78.66). The Mirage values also differ slightly between the two tables (e.g., ogbg-molbace GAT: 70.77 vs. 72.71). This table has no caption or label, is not referenced in the text, and sits in a section with only one sentence of content. It appears to be a draft artifact that was accidentally included. While Table 1 is the properly captioned main results table and its numbers are internally consistent, the presence of a second, contradictory table makes it impossible for the reader to know which numbers to trust, and creates the appearance of carelessness. **This must be resolved — either remove the orphan table or explain what it represents (e.g., a different experimental condition, validation vs. test set).**

2. **Random(sum) baseline undercuts the necessity of tree co-occurrence mining**: In Table 1, the Random(sum) baseline (randomly selecting whole graphs, not trees) achieves top-1 or top-2 results in 2 of 17 settings and is competitive in several others (e.g., ogbg-molbace GAT: 73.75 vs. Mirage 70.77; DD GAT: 67.31 vs. Mirage 76.08 but with high variance). While the paper notes this and offers an explanation (label distribution differences preserved by SumPool), the explanation is not substantiated with evidence. If a simple random subsample of whole graphs performs nearly as well as the sophisticated tree-mining approach, the paper's motivating claim that careful selection of computation tree patterns is necessary is weakened. A proper ablation — comparing Mirage's frequent co-occurring tree sets against *randomly selected tree sets* of matched size (not whole graphs) — is needed to isolate the benefit of the mining step.

### Minor

3. **Training procedure is underspecified for reproducibility**: Algorithm 1 (`alg:dd_training`) is referenced at line 324 but not visible in the manuscript (presumably stripped). The text description says "sample a batch of frequent tree sets" and "utilize the Combine function on the embeddings of the root node," but several details are unclear: (a) How many tree sets constitute a batch? (b) How is the class label of a tree set determined when a set may contain trees from multiple graphs? (c) Is the loss computed per tree set (as a graph surrogate) or per individual tree? (d) How exactly is the sampling probability proportional to frequency implemented? Without these details, independent reproduction is difficult.

4. **No sensitivity analysis for the two distillation parameters ($\theta$ and $L$)**: The paper claims $\theta$ controls the size-accuracy tradeoff and $L$ should be set based on expected upper bound, but provides no empirical analysis of how varying these parameters affects accuracy, compression, or runtime. This is a gap even for a conference paper, as these are the only parameters the user must set.

5. **Missing statistical significance tests**: The paper reports means and standard deviations over 5 runs but does not perform any pairwise significance tests (e.g., t-test, Wilcoxon) to support claims like "Mirage consistently ranks among top-2 performers." Several comparisons involve overlapping error bars, and the reader cannot assess whether observed differences are meaningful.

6. **Random(sum) variability is high and under-discussed**: In Table 1, Random(sum) has much larger standard deviations (e.g., DD GAT: ±12.0, ogbg-molhiv GAT: ±8.43, NCI1 GAT: ±6.87) than Mirage (typically ±0.2–3.3). This suggests that random graph selection is unstable, which actually favors Mirage — but the paper does not make this argument or analyze whether Mirage's advantage is statistically significant given this variance.

7. **Unsubstantiated "30× faster than full dataset training" claim**: Line 479 references `tbl:fulltraintime` which is not present in the manuscript (likely appendix-stripped). The claim that Mirage is "30 times faster on average" than full-dataset training cannot be verified from the paper as presented.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing Mirage's frequent co-occurring tree sets against randomly selected tree sets (matched in size and count) would cleanly isolate the benefit of the co-occurrence mining step.
- Reporting distillation time broken down by phase (tree enumeration, canonical labeling, FPGrowth) would help users understand where the efficiency comes from.
- Discussion of how the method scales to very large or very dense graphs (e.g., IMDB-B average degree ~10; L=3 gives ~1000 paths per node) would be valuable.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "no code is provided" for reproducibility**: The paper does not cite code as existing. However, this is a common request in reviews and not a fatal flaw. Moved from Weaknesses because the rule says to remove criticisms questioning existence of cited artifacts — code is not cited.
- **Criticism about missing `tbl:fulltraintime`**: Per instructions, parser-stripped appendix content should not be penalized.
- **Criticism about cost shifted to preprocessing vs. eliminated**: The paper already quantifies the O(z × δ^L) preprocessing cost at line 336, so this was addressed.
- **Criticism that KIDD is at a disadvantage for GAT/GCN**: This is a limitation of KIDD's design, not the paper's fault. The paper transparently reports it.
- **Criticism that "Herding uses target GNN"**: The paper already states this (Section 4.1).
- **Criticism about the sufficiency experiment being "just a sanity check"**: The paper also provides independent training loss curves (Fig. 4b) showing training-from-scratch works, partially addressing this.
- **Strength Finder's claim about "robustness across three GNN architectures"** is kept; but its claim that Random(sum) analysis shows "authors understood why frequency alone may not suffice" is overstated — the analysis is a brief paragraph, not a thorough investigation.

## Novel Insights

None beyond the paper's own contributions. The reviewers raise standard concerns about experimental rigor (duplicate table, missing ablation, statistical testing) rather than identifying deep conceptual issues unseen by the authors. The most interesting observation from the reviews is the Random(sum) baseline challenge: the fact that a simple random subsample of whole graphs often competes with a sophisticated tree-mining approach suggests that distillation benchmarks may need to control for the "graph-size signal" more carefully. Neither the paper nor the reviewers fully unpack this.

## Suggestions

1. **Remove or explain the orphan table.** If it represents a different experimental condition (e.g., validation vs. test performance, different $\theta$/L), label it clearly and reference it in the text. Otherwise delete it.
2. **Add an ablation comparing Mirage against randomly selected tree sets** (not whole graphs), matched in size and count, to isolate the benefit of the co-occurrence mining step.
3. **Specify the training procedure in detail.** Include batching, label assignment, sampling mechanism, and loss computation — either in the main text or as pseudocode in a supplemental.
4. **Report sensitivity to $\theta$ and $L$** across 2–3 values each to ground the claim that $\theta$ controls the size-accuracy tradeoff.
5. **Add statistical significance tests** (e.g., paired t-test or Wilcoxon) comparing Mirage to the best baseline for each dataset-architecture setting.

## Score and Decision

This paper introduces a genuinely novel and well-motivated approach to graph distillation. The core idea — mining frequent co-occurring computation trees for model-agnostic distillation — is clever and the efficiency/compression results are impressive. However, the presence of an orphan table with contradictory numbers undermines trust in the reported results, and the finding that a simple random-subsample baseline is often competitive weakens the claimed advantage of the tree-mining procedure. Additional ablations and specification details are needed. The paper could become a strong contribution with revisions, but in its current form the empirical evidence is not sufficiently reliable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>