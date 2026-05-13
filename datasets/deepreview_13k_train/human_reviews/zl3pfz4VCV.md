# MMTEB: Massive Multilingual Text Embedding Benchmark

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Text embeddings are typically evaluated on a narrow set of tasks, limited in terms of languages, domains, and task types. To circumvent this limitation and to provide a more comprehensive evaluation, we introduce the Massive Multilingual Text Embedding Benchmark (MMTEB) -- a large-scale community-driven initiative expanding MTEB to over 500 \textit{quality controlled} evaluation tasks across 1,000+ languages. MMTEB includes a wide range of challenging novel tasks such as instruction following, long-document retrieval, and code retrieval, and represents the largest multilingual collection of evaluation tasks for embedding models to date. We use this collection to construct multiple highly multilingual benchmarks. We evaluate a representative set of models on these benchmarks.
Our findings indicate that, while LLM-based models can achieve state-of-the-art performance on a subset of languages, the best-performing publicly available model across languages is the notably smaller, multilingual-e5-large-instruct.

Massive benchmarks often impose high computational demands, limiting accessibility, particularly for low-resource communities. To address this, we downsample tasks based on inter-task correlation (i.e., selecting only a diverse set of tasks) while preserving relative rankings.
We further optimize tasks such as retrieval by sampling hard negatives, creating smaller but effective splits. These optimizations allow us to introduce benchmarks at a significantly lower computational cost. For instance, we introduce a new zero-shot English benchmark that maintains a similar ordering at a fraction of the cost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new set of benchmarks called "massive multilingual text embedding benchmark". This benchmark includes more than 500 tasks and covers a lot of low resource languages as well. They also introduce downsampling technique such that the resources required for the evaluation is minimized.

### Strengths
- The paper is well written and the main points are clearly communicated
- The dataset is a great extension to the MTEB and would be a good resource to research community towards building largescale multilingual embedding models
 - The coverage of the dataset is great

### Weaknesses
Based on table9, one limitation is that most of the crowd submissions are already based on existing public datasets from multiple language domains and not particularly for this dataset construction effort.

### Questions
- How do the top models on MTEB leaderboard do on this new dataset and whether this new dataset changes the ranking of the leaderboard?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
MMTEB addresses the limitations of traditional text embedding evaluations to extend the current popular MTEB benchmark to over 500 quality-controlled tasks across thousand languages, making it the largest multilingual collection for embedding model evaluation. MMTEB is a large-scale, open collaboration benchmark where the contributors have diverse backgrounds and introduce diverse and challenging tasks, such as instruction following, long-document retrieval, and code retrieval.

### Strengths
- Given that recent embedding models often shows the trends for optimized for MTEB benchmark tasks, it would be valuable to develop larger-scale benchmarks that include a broader range of tasks.
- Additionally, MMTEB downscales datasets and caches embeddings to help alleviate computational bottlenecks during evaluation.

### Weaknesses
In general, dataset information (such as sample numbers, multilingual types, etc) and relevant model benchmark numbers are missing. Find more details in questions.

- How does the evaluation score compare with other embedding benchmarks? For instance, since the AIR-Benchmark doesn’t disclose its evaluation sets, does this mean there might be no overlap with MMTEB?
- Why do smaller models perform better in multilingual contexts while larger models excel on English datasets? Is this pattern unique to comparisons involving only the e5 models?
- Could you provide more MMTEB benchmark results using LLM embedding models from literature, such as SFR-Embeddings, NV-Embed, bge, and Qwen models? Since some of these models are English-based, please include their results in Table 15.
- In Table 9, could you provide the sample counts (queries and documents) for each task? Additionally, please list the 1000 languages and 500 quality-controlled evaluation tasks with examples.
- What is the sample count for each language, and is there an imbalance in sample numbers between languages? Why is it necessary to collect samples exhaustively from native speakers? Could machine translation help address sample imbalance?
- Could you provide contributor statistics, such as distribution across countries, native speakers, domains, and similar tasks?
- Since MMTEB appears to cover most of existing public embedding evaluation datasets, has there been any further data collection, annotation, or synthetic dataset creation for MMTEB? If so, please provide details.
- Paper does not properly explain the code and long-document benchmarks. Could you provide details on these benchmarks and the performance numbers for models from the literature?

### Questions
- How does the evaluation score compare with other embedding benchmarks? For instance, since the AIR-Benchmark doesn’t disclose its evaluation sets, does this mean there might be no overlap with MMTEB?
- Why do smaller models perform better in multilingual contexts while larger models excel on English datasets? Is this pattern unique to comparisons involving only the e5 models?
- Could you provide more MMTEB benchmark results using LLM embedding models from literature, such as SFR-Embeddings, NV-Embed, bge, and Qwen models? Since some of these models are English-based, please include their results in Table 15.
- In Table 9, could you provide the sample counts (queries and documents) for each task? Additionally, please list the 1000 languages and 500 quality-controlled evaluation tasks with examples.
- What is the sample count for each language, and is there an imbalance in sample numbers between languages? Why is it necessary to collect samples exhaustively from native speakers? Could machine translation help address sample imbalance?
- Could you provide contributor statistics, such as distribution across countries, native speakers, domains, and similar tasks?
- Since MMTEB appears to cover most of existing public embedding evaluation datasets, has there been any further data collection, annotation, or synthetic dataset creation for MMTEB? If so, please provide details.
- Paper does not properly explain the code and long-document benchmarks. Could you provide details on these benchmarks and the performance numbers for models from the literature?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces MMTEB, a massive multilingual text embedding benchmark that covers over 500 tasks in more than 1,000 languages. Compared to previous benchmarks, MMTEB considers the “low-resource double bind” during its construction and significantly reduces the computational resources needed for evaluation through various strategies while preserving the relative ranking of models.

### Strengths
1. I believe the efforts to reduce the computational resources required for evaluation are very meaningful, as they will encourage more researchers from low-resource language regions to use this benchmark. If MMTEB had simply expanded the scale of MTEB, it could be expected that most strong baseline models would originate from commercial companies with high computational resources, which could hinder the rapid development of text embedding research.
2. Each computational resource optimization strategy is described in detail, and the methods are easy to implement, which facilitates the adaptation of custom datasets.

### Weaknesses
1. The depth of analysis across different datasets seems inconsistent. For instance, the “Clustering” section in 2.3.1 provides an average Spearman correlation, but the “Retrieval” and “Bitext Mining” sections lack similar metrics. Moreover, as seen from the results in Appendix C.1.2, the selection of “Retrieval” strategy is based on analyses from only the NQ and TREC-COVID datasets, which may lead to biased hyperparameter selection. Although the current level of detail is already quite high, given MMTEB’s potential impact, I believe further detail would only be beneficial.
2. The abstract mentions “a diverse set of challenging, novel tasks such as instruction following, long-document retrieval, and code retrieval,” but I saw little content related to these datasets in the paper. I think the authors should clearly explain:
-  **Why were these tasks included in MMTEB?** (This is a benchmark for multilingual text embeddings, yet instruction retrieval is currently available only in one language.)
- **How were these new tasks integrated into the benchmark?** (I believe directly including long-document retrieval under the “retrieval” category should be done with caution, as it would require researchers to consider incorporating long-document-related datasets in their training data, which to some extent runs counter to the goal of addressing the “low-resource double bind.”)
- **How will these new tasks impact model performance?** (The context length limitation of models such as multilingual-e5-large-instruct could hinder their performance on tasks like long-document retrieval. In the LongEmbed evaluations [1], it performs worse than the Mistral-based version. Additionally, the results in Table 16 show that the Mistral-based models perform better on MTEB (code). Thus, claiming the exceptional performance of multilingual-e5-large-instruct in the Introduction without further clarification may mislead readers.)

### Questions
1. In Lines 86 to 93, could you provide a more intuitive metric for comparing computational resources of different benchmarks, such as the time required to complete evaluations on a single A100 GPU?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces MMTEB, an extensive evaluation suite designed to assess text embedding models across over 1,000 languages and 500 tasks, serving as a multilingual extension to previous benchmarks like MTEB. MMTEB includes novel task categories, such as instruction following, long-document retrieval, and code retrieval. A significant contribution of MMTEB is its introduction of computational optimizations, including downsampling and hard negative sampling, which reduce compute requirements and enhance accessibility. The authors' findings reveal that smaller, instruction-tuned multilingual models outperform larger monolingual models in low-resource language settings.

### Strengths
(+++) MMTEB exemplifies a remarkable community-driven effort, engaging diverse contributors and fostering inclusivity.

(+++) Introduces computational optimizations like downsampling and hard negative sampling, reducing evaluation costs to 3.11 hours on a 7B model (H100 GPU), making it accessible to low-resource settings.

(++) Covers over 500 tasks across 10 categories in more than 1,000 languages, with a strong focus on low-resource languages and domains. But it lacks enough justification demonstrating the quality and value of each dataset. Provides an open-source, public leaderboard that encourages continuous contributions to advancing multilingual embedding research.

(+) Expands traditional benchmarks by including new task types like instruction following, long-document retrieval.

### Weaknesses
1. The study lacks a clear articulation of the specific knowledge gap that MMTEB addresses beyond what MTEB has already achieved in evaluating multi-task capabilities of embedding models. The results section suggests that multilingual scores are closely aligned with English, making it difficult to discern the unique value that MMTEB offers. Additional analysis could better exploit the benchmark's value and clarify its unique contributions.

2. While MMTEB aims to include as many relevant datasets as possible, it is unclear how these datasets were constructed or validated. Details on dataset quality, annotation methods (e.g., human vs. model-generated), and statistics (e.g., query-document ratios) would enhance transparency and reliability, especially given some datasets may be model-generated, such as FollowIR.

3. The paper mentions retaining the top 250 ranked documents per query for each dataset and model but does not specify which model(s) were used to select these hard negatives. Clarifying this would help assess the robustness of the benchmark's retrieval tasks.

4. The combination of 132 tasks makes it challenging to interpret a model's performance on specific languages or language families. While geopolitical categorization is helpful, further segmentation by language, domain, or specific capabilities could provide a more systematic and granular view of model performance. Expanding on the existing MTEB language families in Appendix H could offer researchers a clearer understanding of model weaknesses by language or domain.

### Questions
1. Should Section 3 be titled “Experimental Settings” instead of “Results” to better reflect its content?
2. The evaluation metrics and the main metrics for certain tasks are not described, e.g. instruction retrieval, reranking, multi-label classification.
3. Should bitext mining and STS be considered closely-related task categories in Figure 1?
4. Summarization showed minimal correlation with embedding performance in MTEB. If it is still included in MMTEB, what justifies its inclusion?
5. Does MMTEB include programming language benchmarks, such as CoIR? Additionally, what criteria of multilingualism are used to determine inclusion in the study?

### Soundness
3

### Presentation
2

### Contribution
3
