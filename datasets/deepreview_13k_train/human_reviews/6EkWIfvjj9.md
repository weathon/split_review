# RARe: Retrieval Augmented Retrieval with In-Context Examples

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
We investigate whether in-context examples, widely used in decoder-only language models (LLMs), can improve embedding model performance in retrieval tasks. Unlike in LLMs, naively prepending in-context examples (query-document pairs) to the target query at inference time does not work out of the box. We introduce a simple approach to enable retrievers to use in-context examples. Our approach, \texttt{RARe}, finetunes a pre-trained model with in-context examples whose query is semantically similar to the target query. This can be applied to adapt various base architectures (i.e., decoder-only language models, retriever models) and consistently achieves performance gains of up to +2.72\% nDCG across various open-domain retrieval datasets (BeIR, RAR-b). In particular, we find \texttt{RARe} exhibits stronger out-of-domain generalization compared to models using queries without in-context examples, similar to what is seen for in-context learning in LLMs. We further provide analysis on the design choices of in-context example augmentation and lay the foundation for future work in this space.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the application of in-context learning to improve the performance of retriever models in information retrieval tasks. The authors introduce RARe, a method where in-context examples (query-document pairs related to the target query) are used during the fine-tuning of retriever models. This approach differs from direct application in LLMs where in-context examples are prepended at inference time. RARe enhances retrieval performance by up to 2.72% in nDCG across various datasets.

### Strengths
- While in-context learning is not new, its application to retriever models in this specific manner is new. The paper creatively adapts this technique, showing potential new directions for retrieval model improvements.

### Weaknesses
 - While in-context learning is not new, its application to retriever models in this specific manner is new. The paper creatively adapts this technique, showing potential new directions for retrieval model improvements.

 - While the application of in-context learning to retrievers is new, it might not strike everyone as a groundbreaking shift.
- The approach, as well as the performance gain, looks a bit incremental. There might also be a tradeoff between efficiency, accuracy, and ease of use of the method.
- Discussion on how RARe might scale or face challenges in real-world applications beyond the benchmarks used could be expanded.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper employs BM25 to retrieve top-k relevant queries and their associated documents as in-context examples, enhancing query representation when using an LLM as the retrieval encoder. Extensive experiments, including comprehensive ablation studies, were conducted to demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-structured and easy to follow.
2. Extensive experiments were conducted on recent base models and popular datasets, such as MS-MARCO, BeIR, and RAR-b, demonstrating that the proposed RARe method enhances baseline models, including Llama and other LLM-based retrievers.
3. Detailed ablation studies investigate critical questions, such as the impact of retrieved vs random in-context examples and whether semantically closer in-context examples are more beneficial.

### Weaknesses
1. There are no statistical significance tests to confirm that the improvements over baselines in Tables 1 and 2 are meaningful.
2. Only a basic retriever, BM25, was applied.
3. In Figure 3, the performance of ArguAna’s Retrieved/Random setup is worse than Random/Random, which is inconsistent with other datasets and lacks an explanation.
4. Figure 4 appears to contradict the paper’s premise, which relies on similar queries and their associated documents to enhance query representation. When score@Top-1 improves, relative improvement drops are observed on NFCorpus and FiQA2018, without further clarification. Additionally, only relative results are reported, making it difficult to discern the actual trend of NDCG against score@Top-1.

### Questions
1) What are the actual trends of NDCG in Figure 4?
2) Can you explain why ArguAna’s Retrieved/Random setup is worse than Random/Random in Figure 3?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores adding in context examples in the query for retriever. It first retrieves related pairs using BM25 and then explores different methods, such as LLM based methods as well as based on existing well trained retriever methods. The idea is quite natural to explore and it is a good plus for the retrieval community with its positive results as well as its extensive ablation study.

### Strengths
1. Studying adding in context examples for the query is a under explored topic for retrieval community.
2. The results are positive and the ablations are quite extensive.

### Weaknesses
1 The baselines are a bit weak where I am not sure how much value will the less than 2% improvement add. There are other leading models on BEIR benchmark and how will the proposed methods compare to those and will those method get improved after adding in context example?

### Questions
Why the search time for DBPedia is much lower than Quora even if DBPedia has much larger corpora in Table 6?

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
4

### Summary
This paper investigates whether training with in-context examples can enhance the in-domain performance of LLM-based retriever models and improve their generalization to different unseen tasks. It introduces a simple training strategy that identifies examples using BM25 during training and performs inference with in-context examples. Experiments were conducted on the BEIR benchmark and a reasoning-intensive retrieval benchmark, RAR-b.

### Strengths
1. The paper explores in-context examples for retrieval, which are widely employed in decoder-only LLMs, to enable the model to incorporate the semantic and pattern information of examples for adjusting its output embeddings across various retrieval tasks with differing user intents. This approach could potentially be a step forward from instruction-based retrieval models to ICL-based retrieval models.
2. Despite the simplicity of the training method, the paper provides an extensive analysis of how the quality, quantity, and selection of in-context examples impact the model's performance.

### Weaknesses
1. It is unclear whether the in-context examples truly contribute during training: Since all examples are retrieved using BM25, it raises the question of whether they merely act as a form of query expansion. Deeper experimentation is needed to address this, such as retrieving only similar passages based on semantic similarity, not just lexical overlap, and incorporating them into the training process. As shown in Table 4, using only documents during inference sometimes yields good results; thus, what happens if doc-only is used during training as well? The paper should explore training with document-only inputs to isolate the impact of in-context examples.
2. This paper lacks an in-depth analysis of the generated embeddings. For instance, why does adding examples lead to performance declines on some test sets, such as ArguAna and ClimateFEVER? Further attribution analysis, like exploring the impact of examples on attention patterns, or examining the cosine similarity of embeddings with and without context, could deepen the study and enhance its contributions to the research community. The paper needs to provide a more granular analysis of the embedding space.
3. The training strategy is too simplistic: A more sophisticated training strategy could be explored. The current approach is too basic. For example, the impact of using in-batch negatives, a commonly employed technique in retrieval training, remains unexplored. Specifically, if in-batch negatives come from different tasks, could they help in better training the ICL capabilities due to differing examples and retrieval intents? The paper should investigate more advanced training techniques, such as hard negative mining or curriculum learning, to improve the model's ability to leverage in-context examples.
4. The analytical experiments should include results on the complete BEIR benchmark or at least all out-of-domain (OOD) results. The current selection of OOD datasets is limited and may not fully represent the model's generalization capabilities.

### Questions
1. In Figure 3, only part of OOD test sets from BEIR are selected. Could you supplement with the complete set to observe trends, especially since these selected test sets are relatively short?
2. In Table 4, the performance with doc-only is also quite good for several test sets, such as CQA, NFCorpus, and Touche2020. Given that examples can be viewed as a form of query expansion, how do you explain the improvement brought by doc-only, and what is its relationship with ICL training? Can training with doc-only also bring performance gain?
3. To truly demonstrate the ICL capabilities, evaluating more embedding tasks and scenarios, such as classification, reranking, and clustering, might be necessary. Have you considered adding other tasks from METB that can better test the ICL ability?

### Soundness
2

### Presentation
3

### Contribution
3
