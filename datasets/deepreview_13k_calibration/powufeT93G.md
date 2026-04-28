# Do We Need Domain-Specific Embedding Models? An Empirical Investigation

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Embedding models play a crucial role in representing and retrieving information across various NLP applications. Recent advancements in Large Language Models (LLMs) have further enhanced the performance of embedding models, which are trained on massive amounts of text covering almost every domain. These models are often benchmarked on general-purpose datasets like Massive Text Embedding Benchmark (MTEB), where they demonstrate superior performance. However, a critical question arises: Is the development of domain-specific embedding models necessary when general-purpose models are trained on vast corpora that already include specialized domain texts?
In this paper, we empirically investigate this question, choosing the finance domain as an example. We introduce the Finance Massive Text Embedding Benchmark (FinMTEB), a counterpart to MTEB that consists of financial domain-specific text datasets. We evaluate the performance of seven state-of-the-art embedding models on FinMTEB and observe a significant performance drop compared to their performance on MTEB. To account for the possibility that this drop is driven by FinMTEB’s higher complexity, we propose four measures to quantify dataset complexity and control for this factor in our analysis. Our analysis provides compelling evidence that state-of-the-art embedding models struggle to capture domain-specific linguistic and semantic patterns. Moreover, we find that the performance of general-purpose embedding models on MTEB is not correlated with their performance on FinMTEB, indicating the need for domain-specific embedding benchmarks for domain-specific embedding models. This study sheds light on developing domain-specific embedding models in the LLM era

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FinMTEB, a massive text embedding benchmark specifically designed for the financial domain. Experimental results show that state-of-the-art models that perform well on MTEB exhibit a significant performance drop when evaluated on FinMTEB. The authors further quantify the complexity of both FinMTEB and MTEB and conduct control experiments. They find that, at the same complexity level, model performance on FinMTEB is much lower than on MTEB, which they argue provides evidence that the challenges arise from domain-specific linguistic and semantic patterns rather than dataset complexity. Additionally, the authors observe that performance on MTEB does not correlate well with performance on FinMTEB, highlighting the need for domain-specific embedding benchmarks.

### Strengths
1. **Valuable problem**: This paper focuses on a practical and important problem: creating high-quality text embeddings for the financial domain.

2. **Well-written paper**: The paper is clearly written and easy to follow.

3. **Comprehensive model evaluation**: The authors evaluate a diverse range of embedding models, providing a thorough overview of the current embedding model landscape. Additionally, the experimental results demonstrate the challenges posed by FinMTEB, highlighting the need for developing better financial embedding models.

### Weaknesses
1. **Should current general-purpose text embedding models perform well on financial embedding tasks?**: I have concerns about whether current SOTA text embedding models should be expected to perform effectively on financial embedding tasks. For example, the NV-Embed [1] model is trained on only a single finance-related dataset, FiQA. Given the limited financial data used in training, these embeddings may not perform well for finance-specific tasks. Furthermore, the fundamental task of text embedding differs significantly from language modeling tasks like text generation. While LLMs demonstrate strong general understanding, their embedding capabilities might not generalize across diverse domains without specific in-domain training. This is supported by recent studies showing that incorporating more in-domain data significantly improves embedding performance on benchmarks like MTEB.

2. **Unfair dataset language composition**: Most SOTA general-purpose text embeddings on the MTEB benchmark, including the models evaluated in this paper, are predominantly trained on English datasets. However, a substantial portion of FinMTEB is in Chinese, creating an imbalanced setting that may not be fair for evaluating these models. This language imbalance could disproportionately penalize models not trained on multilingual data, leading to skewed performance evaluations.

3. **Dataset complexity measurement**: I have concerns about the reliability of the authors’ approach to quantifying dataset complexity. A) Complexity is measured independently for queries and documents, but retrieval is fundamentally a pairwise task, where the relationship between query and document can significantly affect complexity. For example, the BRIGHT [2] dataset requires reasoning to map queries to documents, which current models struggle with. The interaction between query and document is crucial, and measuring their complexities separately fails to capture this. B) I question the validity of using ChatGPT’s error rate as a complexity measure. If ChatGPT cannot answer a question correctly, is it due to the complexity of the question or the model’s lack of question-specific knowledge? The error rate might reflect the model's knowledge gaps rather than inherent dataset complexity.

4. **Concerns about the argument of linguistic pattern**: I have concerns about the authors' claim that the higher token count in FinMTEB compared to MTEB indicates significant linguistic differences between the two benchmarks. While a higher token count might suggest longer sentences, it doesn't necessarily imply a fundamental difference in linguistic patterns. The increased length could be due to more verbose language rather than distinct semantic structures.

5. **High semantic diversity**: The inter-dataset semantic similarity is calculated using only 100 samples from each dataset. I question whether this sample size is sufficient to accurately represent the overall dataset’s characteristics. A larger sample size would be needed to ensure the semantic diversity is accurately captured.

6. **Unclear presentation of results**: This is a minor point, but only the average score across all FinMTEB tasks is shown. Without detailed results for each task type (e.g., clustering, retrieval), the performance of models on FinMTEB is not fully clear. A breakdown of performance by task type would provide a more nuanced understanding of model capabilities.

### Questions
Please see my comments in the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the performance of text embedding models on two distinct benchmarks: a general-domain benchmark and a finance-specific benchmark, which is a newly collected dataset. The findings highlight a performance gap and lack of correlation between the two, suggesting the need for domain-specific benchmarks and embedding models better to capture specialized linguistic patterns in domains like finance.

### Strengths
This paper explores a critical question―whether domain-specific embedding models are necessary in the era of general-purpose, large-scale language models.
This paper presents the Finance Massive Text Embedding Benchmark (FinMTEB), a collection of existing or newly constructed evaluation datasets.
The dataset may be useful for emphasizing the finance-specific abilities in benchmarking because the performances on the (general-domain) MTEB and FinMTEB seem less correlated.
This paper evaluates dataset complexity in addition to model performances.

### Weaknesses
The paper’s title question, "Do We Need Domain-Specific Embedding Models?" is not convincingly addressed. To conclude that domain-specific models are necessary, it would be important to demonstrate that (1) a domain-specific embedding model can outperform a general-purpose model within that domain and (2) the observed difference is specifically due to domain specialization. However, the paper does not provide such evidence. Therefore, the research question (and title) would be better phrased as "Do We Need Domain-Specific Embedding Benchmarks?" or "Are Current SoTA Embedding Models Sufficient for Domain-Specific Tasks?"

The analysis lacks sufficient logical rigor and is sometimes misleading. For example, describing the performance difference between FinMTEB and MTEB as a "significant performance drop" is misleading, as MTEB and FinMTEB are not directly comparable. These benchmarks differ in various aspects, making it speculative to attribute the performance difference primarily to financial domain knowledge. A clearer attribution of the observed effects is necessary. Even with additional analyses, it remains unclear whether any convincing conclusions can be drawn about the models solely based on this performance comparison.




### Questions
The paper claims that inter-dataset similarity scores below 0.6 indicate high semantic diversity. Could the authors clarify if this threshold reliably indicates diversity?

How were datasets divided into low, medium, and high complexity? Were the same thresholds used across datasets, or were they divided within each dataset independently? Further clarification here would enhance the validity of this categorization.

ChatGPT Error Rate as a Complexity Metric: Could the authors provide more details on how ChatGPT's error rate was used to categorize dataset complexity? Specifically, how was this metric interpreted to distinguish three complexity levels? An ChatGPT's judge (correct or wrong) might be able to be aligned with binary complexity in my understanding.

FinMTEB’s Dataset Source: In Tables 7 to 13, is the lack of citations for certain datasets indicative of new dataset construction? Clarifying this would help in assessing the novelty of FinMTEB.

In Section 5, the interpretation of p-values could be misleading. A large p-value indicates a lack of evidence for a relationship, not proof of no relationship. Rephrasing to clarify this distinction would avoid statistical misinterpretation.

The abstract mentions that the analysis provides "compelling evidence" of difficulties in capturing domain-specific patterns. Could the authors clarify where this evidence is presented in the analysis and summarize them, as it was not immediately apparent?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Finance Massive Text Embedding Benchmark (FinMTEB). As a domain-specific counterpart to the general-purpose MTEB, FinMTEB includes 64 financial datasets curated for the evaluation of embedding models in the financial domain. A comparative analysis of model performance on both MTEB and FinMTEB suggests the need for domain-specific embeddings and benchmarks.

### Strengths
- This paper presents a massive financial text embedding benchmark — FinMTEB, which consists of 64 financial datasets. I think it is a helpful resource for the financial NLP research community.
- This paper designs a novel and comprehensive evaluation framework to prove that the performance gap between MTEB and FinMTEB is due to the models’ capabilities rather than inherent dataset complexity.
- The paper is well organized and well written.

### Weaknesses
 - From my point of view, the title is not good because the main contribution of this paper is the benchmark. Why not refer to the benchmark directly in the title?
- The evidence may be insufficient to support that the general embedding is not good at domain application since only one domain, i.e., finance, is proven in this paper. The paper does not explore the potential for general-purpose embeddings to be effective in specialized domains with targeted fine-tuning or prompt engineering. The conclusion that domain-specific embeddings are necessary may be premature without exploring these avenues.
- Lack of novelty: According to the previous work [1][2][3], domain fine-tuning can improve domain-specific performance, which is well-accepted evidence. Based on this, the FinMTEB benchmark should be the main contribution of this paper, not the "byproduct" as claimed in the paper. The paper does not adequately address how the proposed benchmark differs from existing benchmarks in terms of task diversity, data quality, and scale, which are critical factors for establishing its novelty and utility.

### Questions
**Question:**

- From Table 7 to 13, I found that there are part of Chinese datasets in the benchmark. But the part of selected embedding models are English model, e.g. bge-large-en-v1.5 and bge-en-icl. Is this a potential problem?
- How long will it take to benchmark different scale models? It would be better to report the benchmarking time.

**Suggestions:**

- The related work on general-purpose embeddings is insufficient. More pilot and recent LLM sentence embeddings are encouraged to be considered in the related work, such as [1][2][3][4][5].
- According to the ICLR style, a table caption is better placed before the table, and a figure caption is better placed after the figure.

**Reference:**

[1] Li X, Li J. Angle-optimized text embeddings[J]. arXiv preprint arXiv:2309.12871, 2023.

[2] Lee J, Dai Z, Ren X, et al. Gecko: Versatile text embeddings distilled from large language models[J]. arXiv preprint arXiv:2403.20327, 2024.

[3] Li X, Li J. BeLLM: Backward Dependency Enhanced Large Language Model for Sentence Embeddings[C]//Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). 2024: 792-804.

[4] Springer J M, Kotha S, Fried D, et al. Repetition improves language model embeddings[J]. arXiv preprint arXiv:2402.15449, 2024.

[5] Lee C, Roy R, Xu M, et al. NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models[J]. arXiv preprint arXiv:2405.17428, 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the necessity of domain-specific embedding models given the prevalence of general-purpose embedding models. To address this, the authors first developed a financial domain benchmark, FinMTEB. Utilizing this benchmark, they observed a significant decline in performance and, through a series of experiments, ruled out the influence of the selected models and task complexity. This led to the conclusion that general-purpose models are inadequate for domain-specific tasks.

### Strengths
- The development of the FinMTEB benchmark provides a valuable tool for evaluating embedding models within the financial domain.
- The experimental design is highly rigorous, systematically eliminating the potential confounding factors related to the models used and the inherent complexity of the datasets. This enhances the credibility and reference value of the experimental conclusions.

### Weaknesses
 - The conclusion that general-purpose embedding models are not well-suited for specific domain tasks and that specialized models are necessary for particular domains is not particularly surprising.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2
