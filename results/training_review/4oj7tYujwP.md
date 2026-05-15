Now I have thoroughly read and cross-checked the paper against each reviewer claim. Let me compose the final consolidated review.

## Summary

This paper introduces the ERiC-UP³ benchmark for detecting patent infringement from multi-modal product data. It formulates a new task — retrieving potentially infringing patents given a product's images and text — and constructs a large-scale dataset with 13M patents, 1M products, and 13k expertly annotated infringement pairs. The paper provides baseline results using various pre-trained language models, proposes a two-stage pipeline (CPC classifier + contrastive retriever), and explores auxiliary techniques including text rewriting, image domain alignment, and cross-modal retrieval.

## Strengths

- **First large-scale, expert-annotated dataset for product-patent infringement detection.** The dataset fills a genuine gap: 13k infringement pairs labeled through three rounds of expert cross-validation, with 13M patents and 1M products at scale. This resource enables a previously unaddressed ML task with practical relevance.
- **Scale and comprehensiveness.** At 13M+ patents and 1M+ products with paired multimodal data, this is the largest multi-modal patent dataset and one of the largest multi-modal product datasets (Section 2.2, Table 1). The two-tier design (Base for rapid prototyping, Large for full-scale evaluation) is thoughtful.
- **Novel and practically useful finding about classifier transfer.** The paper discovers that a classifier trained on patent-to-CPC mappings generalizes to product-to-infringement-patent classification, outperforming both GPT-4-generated training sets and direct training on infringement pairs (Table 6, Section 4.2). This is a concrete, non-obvious insight.
- **Comprehensive baseline exploration.** The paper systematically evaluates multiple text sections, six pre-trained encoders, supervised contrastive fine-tuning, text rewriting strategies, stretch-based image alignment, cross-modal CLIP retrieval, and alternative similarity metrics (Sections 4.1–4.4). This provides a solid foundation for future work.
- **Significant empirical gains from the proposed pipeline.** The classifier+retriever pipeline improves mAR@500 by 24–28% over direct retrieval, and supervised contrastive learning boosts BGE by 52.24% over its pre-trained version (Table 5, Table 7), demonstrating that the dataset supports meaningful model training.

## Weaknesses

### Fatal
None.

### Major

- **No inter-annotator agreement statistics or detailed annotation quality metrics.** The paper states that pairs are "meticulously labeled by patent experts through three rounds of cross-validation" (Section 2.2) and describes the sources in Section 2.3, but provides no quantitative measures of label reliability — no Cohen's κ, no percentage agreement, no information on the number of annotators, their qualifications, or how disagreements were resolved. For a benchmark intended to be a gold standard, this omission weakens confidence in label quality. The paper would be substantially strengthened by reporting these statistics.

### Minor

- **Training hyperparameters are not reported.** The paper describes the loss functions and architecture choices (Section 3) but omits batch sizes, learning rates, optimizers, number of epochs, temperature τ values, and random seeds. While the core contribution is the dataset, the baseline experiments are harder to reproduce without these details.
- **No data or code release statement.** The paper does not include a URL or statement about dataset/code availability. For a benchmark paper, a clear release plan (even if conditional on publication) is important for the community to build on the work.
- **Metric reporting could benefit from more granularity.** The paper reports only mAR@500 and mRoM. While mAR@500 is a reasonable choice given the massive gallery (2.55M–13M), reporting mAR@1, @10, @100 would give a more complete picture of practical utility, especially since real-world reviewers would not want to examine 500 candidates.

### Trivial

- The paper jumps from Section 2.4 to Section 2.6 (Section 2.5 appears missing in the extracted text). Several sentences near the bottom of page 90 contain garbled formatting (e.g., "This tchormesbhionleddi nagp, pernoahcahn clienvge rbaogtehs etfhfeic iceonncsyis taenndc ya cocf thresholding").

## Nice-to-Haves

- Adding standard IR baselines (BM25, DPR) would further anchor the benchmark for the retrieval community, though the existing comparisons across six pre-trained models already provide meaningful reference points.
- An error analysis breaking down failures by CPC class or product type would help users understand dataset difficulty and model limitations.
- Providing dataset statistics on the proportion of pairs from each labeling source (VPM, pre-listing audits, historical cases) would help users understand potential biases.

## Removed Points

These points were raised by reviewers but are not included in the main weaknesses after verification against the paper.

1. **"No comparison to existing patent infringement detection methods"** — REMOVED. The existing methods cited (Yoon 2008; Lee et al. 2013; Park & Yoon 2014; Liu & Pei 2023) are all designed for **patent-to-patent** infringement detection, not **product-to-patent** retrieval. The paper introduces a fundamentally different task. Comparing against these methods would not be apples-to-apples. The paper does compare six pre-trained encoders (BERT, RoBERTa, T5, MPNET, BGE, LLaMa) with and without fine-tuning, which are appropriate baselines for a new task.

2. **"mAR@500 is a loose threshold"** — REMOVED. This is factually backward: 500 out of a pool of 2.55M (Base) is 0.02%, and 500 out of 13M (Large) is 0.004%. This is an extremely tight cutoff, not a loose one. The metric definition is clearly stated in Section 2.6 ("hit-one strategy" with explicit description), and mRoM provides a complementary ranking-based view.

3. **"Task formulation is a retrieval task not detection task"** — REMOVED. The paper's task is to retrieve potentially infringing candidates, which is a standard formulation for detection in large-scale settings (retrieve-then-review). The title and framing are consistent with this use case.

4. **"Source of negative patents not specified"** — REMOVED. The task is retrieval from a gallery — all patents are candidates and negatives are those not linked to the product. This is standard for retrieval benchmarks.

5. **"No quantitative statistics on VPM sources"** — REMOVED. Interesting supplementary information but not required for the paper's core contribution.

6. **"Claims about cosine similarity too strong without proper ablation"** — REMOVED. The paper presents this as an exploratory finding (Section 4.4, "Does Cosine Similarity Best Capture Semantic Relevance?") and describes the training setup (paired embeddings + binary labels as SFT). The claim is appropriately qualified.

7. Various claims about missing appendices, formatting issues, and parser artifacts — REMOVED per hard rules.

## Novel Insights

The most interesting finding that emerges from the paper — beyond the dataset itself — is that a classifier trained on **patent-to-CPC** mappings transfers effectively to **product-to-infringement-patent** classification, outperforming both GPT-4-generated training data and direct training on infringement pairs (Table 6). This suggests that the CPC classification structure learned from patent texts captures features that generalize across the product-patent domain gap, a non-obvious result that could inform how to bootstrap training data for similar cross-domain IP tasks. The paper's analysis of which textual sections work best (Abstract+Claims for patents, Title+Description for products) and the exploration of stretch-based image domain alignment also provide actionable guidance for practitioners.

## Suggestions

1. **Add inter-annotator agreement statistics** — report Cohen's κ or percentage agreement, number of annotators, qualifications, and how disagreements were resolved. This is the single most impactful improvement for establishing the dataset's credibility.
2. **Report mAR@1, @10, @100 alongside @500** — this is standard practice for retrieval benchmarks and gives a more complete view of practical utility.
3. **Include a data/code release statement** — even if contingent on publication, a clear plan helps the community.
4. **Add training hyperparameters** (batch size, learning rate, optimizer, epochs, temperature τ) in the main text or appendix.
5. **Provide a brief error analysis** — examples of hard cases or breakdown by CPC class would help users understand where the benchmark is most challenging.
6. **Add BM25 and DPR baselines** — these are standard IR references that would further anchor the benchmark.

## Score and Decision

**Originality:** 8/10 — Novel task formulation and first dataset of its kind.  
**Importance of research question:** 8/10 — Real-world IP detection need with practical consequences.  
**Claims supported:** 6/10 — Core dataset claim is supported; some presentation weaknesses reduce confidence.  
**Soundness of experiments:** 7/10 — Comprehensive baseline exploration, but missing annotation quality metrics and hyperparameter details.  
**Clarity of writing:** 7/10 — Task and methods are described clearly; metric definition is precise.  
**Value to the community:** 8/10 — Dataset fills a genuine gap and enables new research.

The paper's core contribution — the first large-scale, expert-annotated benchmark for product-patent infringement retrieval — is solid and practically important. The weaknesses (missing annotation quality metrics, sparse training details, narrow metric reporting) are addressable and do not undermine the central contribution. The dataset is a genuinely useful resource that should catalyze research in an underexplored area.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>