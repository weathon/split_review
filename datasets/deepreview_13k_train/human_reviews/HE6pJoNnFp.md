# Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection

- Decision: Accept
- Scores: 8, 8, 6, 6, 5

## Abstract
Large language models (LLMs) augmented with retrieval exhibit robust performance and extensive versatility by incorporating external contexts. However, the input length grows linearly in the number of retrieved documents, causing a dramatic increase in latency. In this paper, we propose a novel paradigm named Sparse RAG, which seeks to cut computation costs through sparsity. Speciﬁcally, Sparse RAG encodes retrieved documents in parallel, which eliminates latency introduced by long-range attention of retrieved documents. Then, LLMs selectively decode the output by only attending to highly relevant caches auto-regressively, which are chosen via prompting LLMs with special control tokens. It is notable that Sparse RAG combines the assessment of each individual document and the generation of the response into a single process. The designed sparse mechanism in a RAG system can facilitate the reduction of the number of documents loaded during decoding for accelerating the inference of the RAG system. Additionally, ﬁltering out undesirable contexts enhances the model’s focus on relevant context, inherently improving its generation quality. Evaluation results on four datasets show that Sparse RAG can be used to strike an optimal balance between generation quality and computational efﬁciency, demonstrating its generalizability across tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a sparse RAG which consists of two stages – 1) document assessment, and 2) generation, to improve the efficiency of RAG. The document assessment selects the relevant documents by individually checking their relevance, and generation part only uses the selected documents as a context to generate an answer, but in an efficient manner where documents are cached, and cross-attention b/w documents is not allowed. To my understanding, the efficiency is obtained here, because all previous information could be cached (no recomputation) after document assessment. Experiment results show that a sparse RAG leads to improvements in terms of both effectiveness and efficiency, i.e., it improves RAG, more efficiently than PCW RAG.

### Strengths
1.	The paper is clearly written and the proposed sparse RAG by appending document assessment stage is well validated. 
2.	In the experiments, the proposed method leads to additional improvements in terms of both RAG and sparse RAG. It is more efficient than RAG, and it is remarkable the sparse RAG shows improved performances over RAG.

### Weaknesses
1.	Some parts in the presentation are not clear. In multitasking data format, more details of the format need to be provided. E.g. What is the information of Rating field? In Figure 1, [ASSESS] and [GENERATE] are special tokens? Detailed position information for cached document representations used in document assessment and generation. Document assessment does not use the cached representations in input?  
2.	Context reduction methods have been widely studied for RAG. Document assessment method needs to be validated separately. Other context compression and reduction baselines (not only RAG) need to be compared.
3.	Given the restricted cross-attention manner across passages, there is concern that the general ability is still well-maintained. SparseRAG needs to be further validated under other advanced CoT, long chain of reasoning, and instruction following tasks. 
4.	Document assessment can also be parallelizable, using restricted cross-attention method? Still, it remains unclear whether the current decision of relevance for documents in an one-by-one manner is optimally designed.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents SparseRAG, an efficient framework designed to address the scaling challenges of traditional RAG models. The primary issue tackled is the significant increase in memory usage of the key-value (KV) cache when processing large amounts of retrieved lengthy documents. This issue hurts the ability of large language models (LLMs) to efficiently manage long-form context and capture essential content.

To overcome this, the authors propose SparseRAG, which utilizes a required LLM rater and an optional LLM critic to generate Per-Context-Assessment (PCA) training data. The LLM is then trained on this PCA data to enhance its capability in assessing the relevance of retrieved documents. During both training and inference, after retrieving the related contexts, the LLM first evaluates the relevance of each retrieved documents and simultaneously extracts the KV caches, which are then concatenated to generate the final outputs.

The experimental results indicate that SparseRAG significantly improves both prefill and decoding efficiency. Additionally, it outperforms all other baseline models in generating high-quality outputs. Further analysis and ablation studies confirm that SparseRAG is both an efficient and effective framework.

### Strengths
1. The writing is clear and easy to follow, addressing a genuine concern.

2. The proposed method demonstrates efficiency and effectiveness compared to the baselines.

3. Most ablation studies and analyses are convincing.

### Weaknesses
1. Ablation Study Suggestion: It would be beneficial to include an ablation study to evaluate the impact of concatenating selected KV caches instead of the corresponding raw contexts. This approach aims to save computation time, but it’s important to assess any potential performance loss compared to recalculating KVs with full attention on concatenated raw contexts. Understanding this trade-off is crucial, as certain applications might accept additional computation time if it results in significant improvements.

2. Comparison with KV Cache Compression Methods: Since the paper claims that SparseRAG enhances efficiency during the prefill and decoding stages by adopting context selection, it would be compelling to compare it with KV cache compression methods such as H2O, SnapKV, and KVMerger. Although these are typically training-free methods, and thus challenging to directly compare, such an analysis could provide valuable insights into the relative benefits and limitations of SparseRAG.

### Questions
See the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes "Sparse Retrieval-Augmented Generation" (Sparse RAG), a paradigm to accelerate large language model (LLM) inference by selectively loading only the most relevant retrieved contexts. This approach aims to improve computational efficiency and generation quality by filtering unnecessary documents during decoding, evaluated across diverse datasets with positive outcomes in both quality and speed.

### Strengths
1. Proposes an innovative sparsity-driven retrieval method (Sparse RAG) that enhances both inference efficiency and output quality.
2. Successfully demonstrates generalizability and adaptability through evaluations on multiple tasks and datasets.
3. Offers thorough comparative analysis against existing methods, providing clear evidence of computational and quality improvements.
4. Utilizes a practical on-device evaluation setting to substantiate real-world applicability, particularly on resource-constrained devices.

### Weaknesses
1. The paper does not provide experimental comparisons to validate that the absence of inter-document attention scores during inference does not lead to a significant decline in the quality of responses. This aspect could be further explored to strengthen the claims made regarding the effectiveness of the Sparse RAG approach.
2. The training process involves multi-tasking and parallel context encoding, which may introduce additional complexity and require careful tuning to ensure effectiveness.

### Questions
1. Does reusing the KV Cache during batch inference cause a decline in the quality of responses when the document-level attention scores are missing?
2. Why does the use of an external classifier in the CRAG method increase so much latency? (My understanding is that the classifier should be a model with relatively few parameters, and it should be able to perform batch inference.) Is the training data for the classifier consistent with the PCA task?

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
This paper proposes SparseRAG, a method to improve efficiency/effectiveness and reduce computation costs through sparsity. It encodes retrieved documents in parallel, which eliminates latency introduced by long-range attention of retrieved documents. Then, LLMs selectively decode the output by only attending to highly relevant caches auto-regressively.  This is via prompting LLMs with special control tokens. Sparse RAG can facilitate the reduction of the number of documents loaded during decoding for accelerating the inference of the RAG system. It filters out undesirable contexts and enhances the model’s focus on relevant context, improving its generation quality. Evaluations on four datasets show good results on improving generation quality and computational efficiency across multiple tasks.

### Strengths
1.	Overall, the paper is clearly written.  

2.	The motivation of SPARSE RAG is natural, and the design of the approach seems to be innovative and reasonable.

3.	The claim that “Sparse RAG combines the assessment of each individual context and the generation of the response into a single process, in which special control tokens are used to prompt the LLM to assess the relevance of each retrieved context, and then only the key-value caches of the most relevant contexts are loaded for decoding using another control token.”  This seems to be interesting and novel, but some detailed explanation is needed to help readers understand the process.  For example, it will be good to explain how the special control tokens work in practice, or to provide a step-by-step explanation of how the context assessment and response generation are combined.

### Weaknesses
1.	The design assumes that a good amount of RAG training data is accessible, which allows effective tailoring and adapting of existing LLMs to the specific needs. But this design relies on pretty heavy training data, for example, in the PoPQA testing, the dataset is split into training, validation and test sets with 8:1:1 ratio (and other testing follows a similar spirit).  I am wondering in practice, an LLM will take many kinds of queries and refer to different kinds of external data, where the training pairs may not be available.  How does your method work if such training data is not available, or when your data and applications do not match the statistics in your training data?  I would suggest that the authors conduct additional experiments with varying amounts of training data to demonstrate the method's robustness. Additionally, it will be useful to discuss potential strategies for adapting the method to domains where extensive training data is not available.

2.	The design does not do any concrete semantic analysis on query intent and nor does any concrete semantic analysis on the text to be retrieved.  It would be helpful to discuss the potential benefits and drawbacks of incorporating semantic analysis into this approach. The reviewer is wondering whether the authors should discuss the potential effect of semantic analysis of the queries and texts and why they chose not to include them in their current design.

### Questions
The points outlined in the “weakness” should be clarified in the rebuttal.

Also, in your appendix, you mentioned "We observed trends in questions and contexts shared in Table 12 that raised concerns about whether and how a human would be able to assess the relevance of the context. These concerns extend to expectations of how well LLMs would be able to do that as well." 

For example, you mentioned that in the dataset NQ, a query like "who is the president of USA right now", and you commented that "the answer will depend on when the question is asked".  

This is true but I assume that is exactly why RAG could be useful since RAG will retrieve additional information based on the context of the query, and in many cases, information in the query, its surrounding context and the supporting datasets should be able to disambiguate the time period and thus return the correct answer.   I think some discussion on this is necessary.  It would be helpful if the authors may elaborate on how the Sparse RAG approach specifically handles such time-sensitive or ambiguous queries. The authors may include examples or experiments demonstrating how their method performs on queries that require temporal context, or a discussion on how such capabilities can be incorporated in the Sparse RAG framework.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes Sparse RAG, a novel RAG framework that reduces computational costs by leveraging sparsity. Sparse RAG encodes retrieved documents in parallel and allows LLMs to selectively decode by attending only to the most relevant cached information. Experiments on four datasets demonstrate that Sparse RAG effectively balances generation quality with computational efficiency.

### Strengths
1. The proposed framework effectively balances generation quality with computational efficiency.

### Weaknesses
1. This work lacks novelty; the authors' primary contribution lies in scoring documents and using an existing framework with modified position encodings to achieve parallel encoding.
2. The experiments lack ablation studies for the module, especially an experiment where only Parallel Contexts is added to RAG (for only generation task).
3. Some parts of this work are not clearly written, making them difficult to understand. For example, lines 201 to 204, with line 204 being especially unclear.

### Questions
1. What is the detailed difference between Parallel Context Windows (PCW) and the Parallel Contexts the authors proposed? A specific example would be helpful.
2. In line 203, what is the {Relevant} token?
3. In Figure 1, do $c_{i}$ and $d_{i}$ represent the same thing? If not, what’s the difference between them?
4. Is Parallel Contexts used for both assessment and generation? The authors state that "we unify the generation of the special control tokens and regular vocabulary tokens with one single model," but line 188 mentions that Parallel Contexts is used only for the "generation task." Does this represent a contradiction?
5. In the section *Silver Labels vs. LLM Labels*, could an experiment be added to evaluate Corrective RAG using LLM Labels? The improvement shown in Table 5 appears minimal, which may be influenced by controllable or uncontrollable factors.

### Soundness
3

### Presentation
3

### Contribution
2
