# QAEncoder: Towards Aligned Representation Learning in Question Answering System

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Modern QA systems entail retrieval-augmented generation (RAG) for accurate and trustworthy responses. However, the inherent gap between user queries and relevant documents hinders precise matching. Motivated by our conical distribution hypothesis, which posits that potential queries and documents form a cone-like structure in the embedding space, we introduce QAEncoder, a training-free approach to bridge this gap. Specifically, QAEncoder estimates the expectation of potential queries in the embedding space as a robust surrogate for the document embedding, and attaches document fingerprints to effectively distinguish these embeddings. Extensive experiments on fourteen embedding models across six languages and eight datasets validate QAEncoder's alignment capability, which offers a plug-and-play solution that seamlessly integrates with existing RAG architectures and training-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a simple but novel document encoding method based on a set of these corresponding (automatically generated) queries, QAEncoder, which generates a set of queries first given a document according to 5W1H, and considers the mean embedding of queries as a document embedding. The experiment results show that the retrieval performance is substantially improved.

### Strengths
1.	This paper proposes a simple but novel document embedding method to reduce the gap b/w query-document matching, based on a set of queries automatically generated for a given document. It is well-motivated, and it is interesting to see that the simple idea has not been suggested to my best of knowledge, while the work is indeed novel.
2.	The experiments show that the proposed QAencoding leads to improvements over the baseline dense retrieval, while more baselines need to be included.

### Weaknesses
1.	The paper assumes Hypothesis, but it is not clear how this hypothesis is connected to the final form of QAencoder. The hypothesis says “the document embedding lies in the perpendicular line intersecting the cluster center”, but it is not clear whether the final embedding vector (Eq. 3 and other equations) fulfills this condition, where lambda is positive. Specially, it seems that the conical assumption hypothesis is not important on this paper, because it doesn’t have a serious role to my understanding. All the methods could be presented, without the conical assumption hypothesis. More explanation is desirable, because this part makes the paper less-readable.  The core issue is that the paper does not clearly articulate how the geometric interpretation of the hypothesis translates into the specific mathematical operations used in the QAEncoder. The perpendicularity claim is not explicitly enforced in the equations, and the role of lambda as a positive scalar does not guarantee that the final embedding will lie on the perpendicular line. The connection between the hypothesis and the final form of the encoder is tenuous, making the theoretical motivation feel disconnected from the practical implementation.
2.	More baselines need to be provided. In particular, different from the proposed direction, the reverse direction (i.e. query2document style) also needs to be compared. Specifically, methods like HyDE, which generate pseudo-documents from queries, should be included as a baseline to provide a more comprehensive comparison. The current set of baselines is insufficient to fully evaluate the novelty and effectiveness of the proposed approach. A comparison with query-to-document methods would help to clarify the advantages and disadvantages of the proposed document-to-query approach.
3.	Only mean pooling of query embeddings is used. However, taking the mean pooling may make individual query semantics blurred. Advanced pooling or matching methods for query-to-query may be examined and discussed. The use of mean pooling may lead to a loss of fine-grained information present in individual query embeddings. More sophisticated methods, such as attention-based pooling or methods that consider the relationships between the different queries, should be explored to better capture the semantic nuances of the generated queries. The current approach may not be optimal for capturing the full semantic richness of the query set.

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
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces QAEncoder, a training-free method designed to enhance alignment in RAG systems by addressing the document-query gap. The approach is based on the conical distribution hypothesis, which suggests that potential queries and documents form a cone-like structure in embedding space. QAEncoder estimates the cluster center of potential queries as a surrogate for document embeddings, improving alignment without increasing storage or retrieval latency. The method integrates seamlessly with existing RAG architectures and includes strategies like document fingerprinting to maintain document distinguishability. Extensive experiments demonstrate QAEncoder's effectiveness across multiple languages and datasets.

### Strengths
1. Excellent architecture and visualization figures.
2. The main experiment includes many different models and hyperparameters.
3. A series of ablation experiments were conducted.
4. The proposed method is effective and allows pre-computation of the (without query) embedding part, accelerating the inference process.

### Weaknesses
1. The descriptions of several QAE fingerprints are somewhat confusing.
2. There are relatively many hyperparameters, and the model's performance varies significantly across different scenarios and hyperparameter settings.

### Questions
1. Why not combine $QAE_{emb}$ and $QAE_{txt}$?
2. How can you find the most suitable hyperparameters in different scenarios? Is it cumbersome to rely on repeated searches? Do you have any insights on simpler methods?
3. Maybe the QAEncoder framework can be used in retrieval model's training?

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
5

### Summary
This paper proposes QAEncoder, a training-free method aimed at bridging the semantic gap between user queries and documents in dense retrieval systems for question answering (QA). The authors introduce the conical distribution hypothesis, suggesting that potential queries and documents form a cone-like structure in the embedding space. By estimating the mean of potential query embeddings, QAEncoder generates a surrogate embedding for each document to improve alignment with user queries. Additionally, the paper introduces document fingerprint strategies to maintain document distinguishability. Extensive experiments across multiple datasets, languages, and embedding models demonstrate that QAEncoder enhances retrieval performance without additional training or significant computational overhead.

### Strengths
1. The paper introduces a training-free method to improve query-document alignment, which can be valuable for systems where retraining is impractical. It seems to improve the performance of unsupervised models more, helping the cases that fewer fine-tuning data is available.
2. The authors conduct experiments across various datasets, languages, and embedding models, demonstrating the general applicability of QAEncoder.
3. QAEncoder is designed as a plug-and-play solution, which can be easily integrated into existing systems without significant modifications.

### Weaknesses
1. The performance gain over supervised models is marginal. In certain cases, it seems to worsen the scores on MSMARCO and HotpotQA (shown in the appendix).
2. If I understand correctly, the pseudo-queries are generated based on the corpus used for testing. This is equivalent to domain adaptation, so I think more domain adaptation baselines should be included, such as GPL, Combination of AdaLM and IDF, AugTriever.
3. A basic but reasonable baseline setting is also missing, which fine-tunes each model using the pairs of generated queries and documents. Even though it is fine-tuned and domain-adapted, it saves the cost for serving new documents.
4. Although QAEncoder doesn’t require training, generating multiple queries and embeddings per document could lead to computational strain. A closer look at the resources required would help readers understand if this approach scales well. Need an extra table to show the time of usage.

### Questions
1. Is there any statistics showing pseudo queries generated by GPT-4o-mini for each dataset (total number, number per doc, length, etc.)? If each doc comes with multiple generated queries, it can also be costly.
2. Why was the study not run on more comprehensive benchmarks like BEIR?
3.  Could the authors provide more detail on the computational resources and time required during indexing? Insight into this would clarify its applicability to large-scale datasets.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose QAEncoder, a training-free approach that utilizes a large language model to generate a pseudo query set from each document in the corpus. They introduce various methods to augment the document representations embedded by the retriever (referred to as "document fingerprints" in the paper) based on the generated queries. The approach is evaluated on QA and cross-lingual retrieval benchmarks, comparing the performance of retrieval models augmented with this method to the original ones.

### Strengths
1. The authors propose several methods for augmenting document embeddings, which could be valuable. Some of their findings are interesting and may provide insights into more effective techniques for representation augmentation.

2. The authors also present various hypotheses and theories, thoughtfully connecting them in a manner that could serve as a useful reference for future research and exploration.

### Weaknesses
1. The evaluation process has several issues:

    - The evaluation metric does not align with the well-established metrics used in prior research, such as retrieval accuracy for NQ and SQuAD, or MRR@10 and NDCG@10 for MS MARCO. Changing it to MRR@8 seems unnecessary, and the authors should either justify this choice or also provide results using the well-established metrics.

    - Most of the retrieval baselines are outdated or unsupervised (e.g., Contriever) or are cross-lingual retrievers. It would strengthen the evaluation if more general neural retrieval models, such as DPR, were included. Additionally, some advanced models are evaluated only in their multilingual versions, and it’s not entirely clear how this focus aligns with the authors' overall motivation.

2. The improvements are minor, considering that the benchmarked retrievers are either weak due to limited training data in their multilingual versions or are outdated, unsupervised models. This is particularly concerning given that the authors use the most recent GPT-4-mini for their enhancements. From another perspective, the proposed solution does not appear to be cost-effective.

3. Some concepts are overly wrapped and lack consensus in the field. For example, the "conical distribution hypothesis" occupies a significant amount of space but does not appear relevant or convincing. Although it may not be false, it is not currently reflected or validated during the retriever’s pre-training or tuning process. Instead, the validity of this hypothesis and the proposed solution might heavily depend on the prompt used to generate the pseudo query and how well it aligns with downstream tasks. Additionally, the term "fingerprint" could benefit from further clarification, as it seems to refer to augmenting document embeddings with pseudo queries. If this interpretation is incorrect, additional explanation would help, as the term might be perceived as vague, making the concept harder to grasp. Demonstrating the solution in a simple, direct manner could enhance clarity.

### Questions
1. Could the authors please provide more clarity on the concept of the "document-query gap" discussed in this paper and how the proposed method addresses it? Is this gap intended to be reflected through performance improvements, or is it an issue that might not be fully captured by existing benchmarks?

2. I am asking Q1 because I am a bit unclear about the motivation behind this training-free augmentation approach. In what scenario is it necessary, and does it address an issue that benchmarks might not fully capture? While the idea is interesting, the improvement seems somewhat inconsistent and not particularly significant, especially considering the high cost involved (e.g., using GPT-4 to generate a pseudo query for each document).

3. Following Q2, could you provide the number of generated tokens or text chunks required to complete the tasks? Given a similar cost, would it be more effective to label a training set and conduct in-domain training instead?

4. Could you please share the reasoning behind focusing on the cross-lingual scenario rather than comparing the method using other well-established retrieval benchmark?

### Soundness
2

### Presentation
2

### Contribution
2
