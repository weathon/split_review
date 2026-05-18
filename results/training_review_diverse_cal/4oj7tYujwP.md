Here is the final consolidated review:

---

## Summary

This paper formulates a new task — detecting potentially infringing utility patents for e-commerce products based on multi-modal data (images + text) — and introduces the ERiC-UP³ benchmark, a large-scale expert-annotated dataset comprising 13M+ patents, 1M+ products, and 13,000 rigorously validated infringement pairs. The authors propose a two-stage pipeline (CPC classifier + supervised contrastive retriever), provide extensive baselines, and explore text rewriting, image domain alignment, and cross-modal retrieval. The benchmark is the first of its kind for product-patent infringement detection and is likely to spur ML research in an underexplored application area.

## Strengths

1. **First large-scale, expert-annotated benchmark for a novel task.** The paper formulates a previously unaddressed ML task — detecting potentially infringing patents from multi-modal product data — and delivers ERiC-UP³, with 13M+ patents, 1M+ products, and 13,000 infringement pairs verified by patent experts through three rounds of cross-validation (Section 2.2). This fills a genuine gap: no comparable dataset existed for this problem.

2. **Effective two-stage pipeline with substantial gains.** The proposed classifier-then-retriever pipeline reduces the patent search space via CPC classification (137 classes) followed by supervised contrastive learning. On the Large benchmark, it improves mAR@500 by 24.05% and reduces mRoM from 110.00 to 102.28; on the Base benchmark, improvements are 28.37% in mAR@500 and mRoM drops from 124.75 to 93.15 (Table 7). These double-digit improvements validate that the pipeline approach meaningfully addresses the core challenge of an enormous search space.

3. **Comprehensive multi-modal analysis.** The paper systematically explores text rewriting (summarization vs. stylistic alignment, Table 8), image domain alignment via stretch detection (21.42% improvement over raw images, Table 9), and cross-modal CLIP-based retrieval (57.14% mAR@500, surpassing sketch-based retrieval by 14.29%). This provides actionable insights for future work on multi-modal infringement detection.

4. **Transferable CPC classifier discovery** — finding that a classifier trained on patent text (patent → CPC) transfers effectively to product CPC classification, outperforming both GPT-4-generated training data and direct infringement-pair training (Table 6). This is a practically useful, non-obvious finding.

## Weaknesses

### Fatal
None.

### Major

1. **Reconciliation between classifier accuracy and pipeline recall is missing.** The pipeline achieves mAR@500 of 92.44% (Large) and 93.58% (Base) in Table 7, while the best CPC classifier achieves only 79.42% Top-2 accuracy on Large (Table 6). The classifier uses Top-K=5 and λ=0.2, so the relevant question is whether the Top-5 accuracy is high enough to explain the recall figures — but the paper does not report Top-5 accuracy on the Large set (it reports Top-1, 2, and 5 on Large but only the Top-1&2 values are explicitly discussed for the patent-trained classifier). The paper also does not provide a per-query analysis of when the classifier includes vs. misses the correct CPC class, nor does it report the size of the reduced pool after classification or quantify how often the correct patent is excluded before retrieval begins. This gap makes it difficult for readers to verify whether the reported recall is consistent with the classifier's performance. The likely explanation (Top-5 accuracy is substantially higher than Top-2) is plausible but should be explicitly demonstrated.

2. **No inter-annotator agreement metric for the gold-standard labels.** The paper states that labels were produced by patent experts through "three rounds of cross-validation" (Section 2.2), but no quantitative agreement measure (Cohen's κ, percentage agreement, etc.) is reported. Since the dataset is the paper's primary contribution, and labeling product-patent infringement pairs is acknowledged to be difficult (Section 2.3), the community needs a trust metric for the gold standard. Reporting even a simple agreement statistic on a held-out subset of pairs would substantially strengthen confidence in the benchmark.

### Minor

3. **The value of *h* in the hierarchical text-to-image retrieval is not specified.** In Section 4.4 (line 169–170), the paper describes using text matching to filter the "Top-*h* most likely patent candidates" before image-based or cross-modal retrieval. The result (57.14% mAR@500 for cross-modal retrieval) cannot be properly interpreted without knowing *h*. If *h* is large, the text stage does most of the work and the cross-modal contribution is small; if *h* is small, the 57.14% is more impressive. This parameter must be disclosed.

4. **The "three rewritten subsets" in Table 8 are not described.** The paper reports mAR@500 results on "three rewritten subsets" but never specifies what they are — their size, CPC distribution, or how they relate to the two rewriting strategies (summarization and stylistic alignment). This makes the results in Table 8 uninterpretable and unreproducible.

5. **Missing baselines on the full Large test set for standard embedding models.** Table 5 reports mAR@500 for pre-trained and fine-tuned models only on the Base set (and the "ALL" condition). The Large test set is used only in Table 7, where the comparison is pipeline-with-classifier vs. pipeline-without-classifier — not a direct comparison of unmodified off-the-shelf models on the full 13M-patent pool. The paper acknowledges computational constraints (line 119), but for a benchmark designed to support future ML research, providing even one or two representative baselines (e.g., BGE, RoBERTa) on the full Large set would set a clear starting point for the community.

6. **Hard-negative mining is mentioned but not ablated.** Section 3.2 states that negative samples are "periodically updated with patents that the model currently finds challenging," but there is no ablation study isolating the effect of this strategy. Since hard-negative mining is known to be impactful for retrieval, showing whether it helps on this specific dataset would be a direct contribution.

### Trivial
- The paper claims the dataset is "the largest multi-modal patent dataset" and "one of the largest multi-modal product datasets available" but does not provide a direct quantitative comparison to prior datasets (e.g., HUPD, BIGPATENT). A brief comparison table would substantiate this claim.
- Dataset availability and license terms are not mentioned. Prospective users need to know how to access the data and under what conditions.

## Nice-to-Haves
- A data sheet (per Gebru et al., 2021) documenting annotation procedures, class balance, known biases, and train/test splits would establish ERiC-UP³ as a durable community resource.
- An analysis of per-query recall decomposed by whether the classifier included the correct CPC class would both validate the pipeline and reveal the true bottleneck.
- An ablation of the hard-negative mining strategy would clarify its contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism about mAR@500 terminology being "unusual"/"confusing"** — This is a pure style nitpick. The metric is clearly defined and standard hit-one recall. *Reason: formatting/style nitpick.*
- **Concern that A63 validation set may not generalize** (sub-issue of Critical Issue 3a from harsh reviewer) — Using a single CPC class as a validation set to select hyperparameters (text section combinations) and then evaluating on the full test set is standard practice. There is no reason to expect the optimal text section combination to be class-specific. *Reason: not a genuine problem; standard experimental design.*
- **"Image preprocessing details too sketchy to replicate"** — The paper cites Zhou et al. (2024) for the underlying stretch-detection method and describes its application at a high level. For a benchmark paper where image retrieval is an exploratory analysis (not the core contribution), this level of detail is adequate. *Reason: reasonable citation practice, not a core methodological gap.*

## Novel Insights
The most interesting finding that emerges across the reviews is that the paper's two main claims — (a) the pipeline is highly effective (92%+ recall) and (b) the CPC classifier only achieves ~79% Top-2 accuracy — appear to conflict, but this tension is resolved if the classifier's Top-5 accuracy is substantially higher than its Top-2 accuracy. This creates a concrete, answerable question that the authors can address with a simple additional analysis, and it highlights a broader lesson for benchmark + pipeline papers: whenever a pipeline has a filtering stage, the accuracy at the filtering stage's operating k must be reported, not just a lower-k metric. The paper could be strengthened by reporting Top-5 accuracy alongside Top-2, and showing the distribution of pool sizes after filtering.

## Suggestions
1. Report Top-5 accuracy for the CPC classifier on the Large test set (Table 6), and provide a per-query breakdown of whether the correct patent was in the reduced pool vs. excluded by the classifier. This single analysis would resolve the most concerning weakness in the paper.
2. Report inter-annotator agreement (even a simple percentage agreement on a held-out subset) for the infringement labels.
3. Disclose the value of *h* used in the hierarchical text-to-image and cross-modal retrieval experiments.
4. Describe the composition of the "three rewritten subsets" used in Table 8.
5. Add at least one representative baseline (e.g., off-the-shelf BGE-large) evaluated on the full Large test set to the benchmark results.

## Score and Decision

The paper introduces a genuinely novel task and a large-scale, expertly annotated benchmark that fills a clear gap. The baseline experiments are reasonably extensive, the pipeline shows meaningful improvements, and the multi-modal analysis provides useful insights. The major weaknesses — unexplained recall discrepancy, missing annotation reliability metric — are real but addressable and do not invalidate the core contribution. The minor omissions (missing *h*, unspecified subsets, absent ablations) are fixable. Overall, this is a solid benchmark paper whose contribution outweighs its presentational gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>