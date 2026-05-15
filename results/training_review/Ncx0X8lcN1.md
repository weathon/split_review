Now I have a thorough understanding of the paper and can verify all claims against the source text. Let me produce the final consolidated review.

## Summary

This paper presents HiReview, a two-stage framework for automatic literature review generation. First, it retrieves the most relevant sub-community from a citation network using graph-context-aware BM25 retrieval (aggregating neighbor relevance scores). Then it builds a hierarchical taxonomy tree via GNN-based clustering (with a soft-to-hard transition across levels) and generates topics bottom-up using a fine-tuned LLaMA with a graph adapter. Finally, GPT-4o generates review content for each topic. Experiments on a dataset of 518 arXiv reviews show improvements over AutoSurvey and other baselines across Coverage, Structure, Relevance, and BertScore.

## Strengths

- **Novel taxonomy-then-generation framework**: HiReview is the first end-to-end system that explicitly constructs a hierarchical taxonomy from the citation graph before generating review content, directly addressing the limitation of prior outline-then-generation approaches (Section 4, Figure 2). The soft-to-hard clustering transition (soft at level 1, hard at higher levels) is a principled design that mirrors how literature reviews organize overlapping subtopics into disjoint higher-level categories.

- **Strong empirical results with reduced variance**: HiReview outperforms all baselines on every metric in Table 1 (Coverage 0.9163±0.03 vs. AutoSurvey 0.8646±0.07; Structure 0.9484±0.02 vs. 0.9122±0.05). Critically, its standard deviations are 2–7× smaller than competing methods, demonstrating substantially more consistent generation quality.

- **Clean ablation confirms retrieval matters**: The w/o retrieval variant (which keeps the same fine-tuned LLaMA backbone) shows cataclysmic drops: Coverage 0.9163→0.6705, Relevance 0.9428→0.7073 (Table 2). This cleanly demonstrates that the graph-context-aware retrieval module is essential — removing it floods the pipeline with noise, and the performance collapse cannot be attributed to backbone changes since the backbone is held constant in this variant.

- **Large curated dataset**: The paper constructs a dataset of 518 literature reviews with annotated taxonomy trees and 2-hop citation networks (average 6,658 papers and 11,632 edges per review), representing a non-trivial resource for the community.

## Weaknesses

### Fatal
None. The paper's core claims — that the full HiReview system outperforms baselines and that the retrieval and taxonomy modules contribute to its performance — are supported by evidence. The evaluation framework is standard for the NLG literature (reference-based evaluation with LLM-as-judge) and the comparisons, while imperfect, are not fundamentally invalid.

### Major

- **Confounded ablations for two of three variants**: The w/o clustering* and w/o taxonomy ablations both replace the fine-tuned LLaMA topic generator with a prompted GPT-4o (the paper acknowledges this with a * marker and a note). This means the performance drops observed for these two ablations (Coverage 0.9163→0.8612 for w/o taxonomy; Structure 0.9484→0.8790) confound the removal of the component with the change of LLM backbone. The paper cannot cleanly attribute these drops to the absence of clustering or taxonomy rather than to the weaker backbone. The w/o retrieval ablation is clean (same backbone), but it alone doesn't isolate the taxonomy contribution. The authors should run all ablations with the same backbone (e.g., prompted GPT-4o for all variants) to allow proper attribution.

- **Clustering accuracy metric is undefined and comparison is asymmetric**: Table 3 reports "Accuracy of hierarchical clustering" without defining what "accuracy" means, what ground-truth labels are, or how the metric is computed. The comparison pits a supervised GNN (trained on ground-truth cluster labels from human reviews) against zero-shot K-means and LLM clustering. This asymmetric setup does not demonstrate that the proposed clustering method is intrinsically better — it only shows that supervised clustering outperforms unsupervised baselines, which is expected. A proper evaluation would use held-out cluster labels or evaluate clustering quality on unlabeled data via intrinsic metrics (e.g., silhouette score, modularity).

### Minor

- **No explicit train/test split reported**: The paper describes 518 reviews but never states how they are partitioned for training, validation, and testing. It says the data "serves as the foundation for training and evaluating" but omits the split sizes. Without this, it is impossible to assess potential data leakage or the generalization difficulty of the evaluation.

- **No human evaluation of generated reviews**: The paper relies exclusively on LLMScore and BertScore. While citing prior work (Wang et al.) that LLM-based evaluation aligns with human preferences for this task, the authors do not conduct their own human evaluation. Given that the core contribution is a new review generation framework, having even a small human study (e.g., domain experts comparing HiReview vs. AutoSurvey outputs blind) would substantially strengthen the validity of the conclusions.

- **Missing experimental details**: Several hyperparameters are referenced but never reported: the neighbor-weighting factor α (Eq. 1), the edge connection threshold p_τ (Eq. 5), the temperature τ for contrastive loss (Eq. 9), and the number of hierarchical levels L. The method for extracting taxonomy trees from human-written reviews is also not described.

- **The paper's framing oversells relative to the experimental setup**: The Introduction motivates the task as generating a review from "vast citation networks," but the experiments operate on a pre-defined 2-hop citation subgraph centered on an existing review paper. While this is a reasonable operationalization (6,658 papers per review is not small), the paper should acknowledge this scope limitation explicitly rather than implying fully open-ended retrieval.

### Trivial

- The α value for neighbor-weighted retrieval is said to be set "empirically" but never reported — a minor but easily fixable omission.

## Nice-to-Haves

- Statistical significance tests (e.g., bootstrapped confidence intervals for differences) between HiReview and AutoSurvey would quantify whether the gaps are reliable, especially given the small absolute differences in some metrics (e.g., BertScore 0.8449 vs. 0.8256).
- A case study with a side-by-side generated vs. human taxonomy tree for one example query would help readers qualitatively assess the taxonomy quality.
- Evaluating whether the generated taxonomy generalizes across domains (train on one domain, test on another) would strengthen the claim that the model learns general structural patterns rather than memorizing domain-specific topic groupings.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Evaluation framework is fundamentally circular / measures reconstruction fidelity"**: The critic claimed the setup reduces the task to "regenerating an existing review's taxonomy." This mischaracterizes the evaluation. The human-written review is used as a reference text for LLMScore (standard practice in NLG), not as a training target to be reconstructed. The model generates a taxonomy from the citation graph, not from the review text. The potential concern about no documented train/test split is real (kept as Minor above), but the critic's characterization of circularity is not supported by the paper's actual methodology.

- **"w/o retrieval confound"**: The critic claimed w/o retrieval is also a "compound failure" because changing the input changes downstream processing. This is not a confound — it is the intended test of whether retrieval matters. The ablation cleanly shows that adding noise to the input (all papers) harms performance, which is the expected and informative outcome.

- **"Challenge 1 is sidestepped"**: The critic claimed the method sidesteps Challenge 1 because the input is a "pre-defined 2-hop subgraph." Operating on a citation subgraph of ~6,658 papers is a valid and non-trivial instantiation of "retrieval from large networks." The retrieval module then selects from these 6,658 papers.

- **"HiReview uses a separate fine-tuned model, giving it a hardware advantage over AutoSurvey"**: The comparison in Table 1 is between two complete systems. HiReview uses fine-tuned LLaMA for topic generation + GPT-4o for content generation, while AutoSurvey uses GPT-4o throughout. Both systems are compared as-published. This is a fair system-level comparison, not a controlled LLM backbone experiment. The paper even states "The LLM backbone of AutoSurvey and HiReview are both GPT-4o" — referring to the content generation backbone.

- **"The model learns to replicate a single annotator's perspective"**: This criticism applies to virtually all supervised learning from human annotations and is not unique to this paper. The dataset contains 518 reviews from different authors, and with a proper train/test split, the model would learn generalizable patterns.

- **"Standard deviations overlap casts doubt on improvements"**: The std dev ranges for HiReview (0.01–0.03) are far tighter than baselines, and the gaps between means (e.g., Coverage 0.9163 vs 0.8646, Structure 0.9484 vs 0.9122) are consistent across all four metrics. While significance tests would be nice, claiming the improvements are unreliable based on std overlap alone is not justified.

- **"LLMScore is a black-box" / "no evidence the score captures factual accuracy"**: The paper cites Wang et al. (2024) which validated LLM-based evaluation against human preferences for this specific task. This is standard practice. The criticism is not a weakness of the current paper.

- **Various formatting/style nitpicks** and claims about missing appendix sections (parser artifacts).

## Novel Insights

The most interesting finding from the ablation is the magnitude of the drop when the graph retrieval module is removed: Coverage falls to 0.6705, which is *worse than zero-shot GPT-4o* (0.7430). This shows that when the system is given the full 2-hop citation network without retrieval, the clustering module fails catastrophically — it cannot separate signal from noise. This suggests that the GNN-based clustering is highly sensitive to input quality and may not generalize well to uncurated citation graphs. Conversely, the w/o taxonomy ablation (Coverage 0.8612) still beats zero-shot and naive RAG baselines, suggesting that even flat (non-hierarchical) paper clusters plus GPT-4o generation produce reasonable reviews. The weakest link in the pipeline is clearly the lack of robust retrieval, not the taxonomy structure. This is a useful insight for future work: improving the robustness of the clustering module to noisy inputs may be more impactful than refining the hierarchical taxonomy generation.

## Suggestions

1. **Run a cleaner ablation**: Hold the LLM backbone constant (e.g., prompted GPT-4o for topic generation in all variants) to isolate the contribution of the clustering and taxonomy modules from the contribution of fine-tuning LLaMA. This is the single most important fix.

2. **Define the clustering accuracy metric** in Table 3: specify the ground truth, the scoring function, and report on a held-out test set. Also add unsupervised clustering quality metrics (silhouette score, modularity) for a fair comparison with baselines.

3. **Report the train/test split** and consider releasing explicit split indices with the dataset.

4. **Report key hyperparameters**: α, p_τ, τ, number of levels L, and the description of how taxonomy trees were extracted from human-written reviews.

5. **Conduct a small human evaluation**: Even 10–20 examples rated by 2–3 domain experts on coverage, structure, and factual accuracy would substantially strengthen the credibility of the results.

6. **Tone down the "vast citation networks" framing** in the Introduction to match the experimental setup (2-hop subgraphs centered on existing reviews).

## Score and Decision

**Score**: 6.5 — The paper introduces a novel and well-motivated framework, produces strong empirical results, and provides a useful dataset. The core claims are supported despite presentation gaps. The major weaknesses (confounded ablations, undefined clustering metric) are addressable and do not invalidate the main contribution. Accept.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>