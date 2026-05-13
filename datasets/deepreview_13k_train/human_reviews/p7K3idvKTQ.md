# Towards Understanding Domain Adapted Sentence Embeddings for Document Retrieval

- Decision: Reject
- Scores: 8, 3, 3, 3

## Abstract
A plethora of sentence embedding models makes it challenging to choose one, especially for technical domains rich with specialized vocabulary. In this work, we domain adapt embeddings using telecom, health and science datasets for question answering. We evaluate embeddings obtained from publicly available models and their domain-adapted variants, on both point retrieval accuracies, as well as their (95\%) confidence intervals.  We establish a systematic method to obtain thresholds for similarity scores for different embeddings. As expected, we observe that fine-tuning improves mean bootstrapped accuracies. We also observe that it results in tighter confidence intervals, which further improve when pre-training is preceded by fine-tuning. We introduce metrics which measure the distributional overlaps of top-$K$, correct and random document similarities with the question. Further, we show that these metrics are correlated with retrieval accuracy and similarity thresholds. Recent literature shows conflicting effects of isotropy on retrieval accuracies. Our experiments establish that the isotropy of embeddings (as measured by two independent state-of-the-art isotropy metric definitions) is poorly correlated with retrieval performance. We show that embeddings for domain-specific sentences have little overlap with those for domain-agnostic ones, and fine-tuning moves them further apart. Based on our results, we provide recommendations for use of our methodology and metrics by researchers and practitioners.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper reported mean bootstrapped retrieval accuracies along with confidence intervals for various SOTA embedding models with and without domain-adaptations. The results show that domain specific embedding show improved isotropy scores and move away from general domain embeddings. Overall, this is a solid study with reasonable technical contributions.

### Strengths
1. The paper is generally understandable and clearly explains the technical parts to a certain extent.
2. The figures and charts in the manuscript are exceptionally clear and well-presented.

### Weaknesses
1. This paper does not provide sufficient details on the ISOTROPY SCORES.
2. The paper does not sufficiently clarify the motivation behind its approach, especially regarding the "COMPUTATION OF THRESHOLDS". It lacks a detailed discussion on why existing methods struggle with this issue and how this paper effectively addresses it. it requires more illustrations and provements about this to help understanding the issue of existing methods and the motivation of the proposed new method in the paper.

### Questions
1. This paper does not provide sufficient details on the ISOTROPY SCORES.
2. The paper does not sufficiently clarify the motivation behind its approach, especially regarding the "COMPUTATION OF THRESHOLDS". It lacks a detailed discussion on why existing methods struggle with this issue and how this paper effectively addresses it. it requires more illustrations and provements about this to help understanding the issue of existing methods and the motivation of the proposed new method in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates different aspects of sentence encoders for domain-specific question-answer retrieval. It aims to address the limitations of cosine similarity in capturing true semantic similarity, especially for frequent words with homonyms or dependence on regularization. To improve retrieval evaluation, the authors use confidence intervals (CIs) over bootstrapped samples for models before and after pre-training and fine-tuning on specific domains. They introduce COE and ROE metrics to measure distributional overlaps between top-K, correct, and random document similarities with the query, showing these metrics correlate with accuracy and threshold values. The paper visualizes how domain adaptation shifts embeddings away from domain-agnostic spaces. It also shows isotropy scores have limited correlation with retrieval performance.

### Strengths
1. The paper proposes novel metrics (CI, COE and ROE) over batched samples to evaluate embeddings for technical domains.
2. The methodology and metrics introduced are well-explained.

### Weaknesses
1. The paper lacks specifics on the pre-training corpus for each domain. If models are pre-trained solely on training sets, this limits the utility of pre-training, affecting the reliability of conclusions. For instance, in the health domain, pre-training on a large corpus like PubMed abstracts is common to ensure domain knowledge. The current approach risks conflating the effects of pre-training with simply increasing model capacity or adapting to the training data distribution, rather than leveraging broad domain knowledge.
2. Comparisons are primarily with pre-trained models from BAAI and OpenAI; adding more state-of-the-art domain-specific baselines could strengthen the evaluation. The absence of comparisons against models specifically designed for the target domains makes it difficult to assess the true effectiveness of the proposed approach. For example, in the legal domain, models pre-trained on legal corpora should be included.
3. While the work presents interesting findings, the novelty is limited. Observations like tighter CIs with fine-tuning are expected since task-specific fine-tuning generally increases confidence for a specific task while potentially reducing generalizability. The paper does not sufficiently demonstrate that the observed tighter confidence intervals are a novel or unexpected finding, given the established understanding of fine-tuning.

### Questions
1. How does the test or dev set accuracy compare to bootstrapped accuracy? could you compare it with existing QA model results as a relaxed version of exact answer retrieval?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an empirical study of domain adapted embedding models for QA. The authors evaluate a range of existing models and their domain-adapted variants on point accuracy and confidence intervals of retrieval tasks. The main contributions of this study are using the following aspects to provide a recommendation to select retrieval thresholds for domain adapted models: 

1. A methodology for determining appropriate similarity score thresholds for different embedding models.
2. Introduction of new metrics that capture the distributional overlap between top-ranked, correct, and randomly selected document with respect to the input question.
3. Analysis of the relationship between embedding isotropy (uniformity of vector lengths) and retrieval accuracy.
4. Observations that domain-adapted embeddings exhibit little overlap with their domain-agnostic counterparts.

### Strengths
The authors define a relevant problem for RAG applications and show that fine-tuning can help to not only improve the retrieval performance but also increase the confidence intervals tightens. Thus, supporting that domain-adaptation is likely to also reduce the expected performance variance in that domain.

### Weaknesses
While the problem addressed is relevant and some of the findings hold intrinsic interest, the paper also presents several notable limitations that should be addressed.

First, the confidence interval (CI) estimation techniques employed are direct applications of common methodologies to measure CI for a given metric (in this case accuracy). 

Second, the paper does not provide a compelling justification for the proposed assessment to select the retrieval threshold, nor does it rigorously compare their performance to simpler approaches such as hyper-parameter cross-validation which is relatively inexpensive assuming the similarity matrix is computed only once. The added value of the new techniques is therefore unclear from the current presentation.

Third, while the paper cites prior studies on the concept of isotropy, there is insufficient explanation of how the experimental setup and findings in this work relate to or build upon those earlier investigations. The connection to the broader academic context is not well established.

Finally, the overall narrative lacks cohesion, as the sections are not clearly tied together, and the suggested methodology for assessing retrieval thresholds is not systematically contrasted against relevant baseline approaches. This makes it difficult for the reader to fully grasp the unique contributions of the work.

### Questions
The paper could benefit from a more cohesive narrative and clearer articulation of the benefits of the proposed assessment approach. While the common theme of domain adaptation links the various experiments, it is unclear what specific advantages the presented methodology offers.

To strengthen the paper, I would suggest addressing the following points:

Clearly define the end goal of the work. For example, if the aim is to provide guidance on setting appropriate retrieval thresholds, what is the current standard practice in this area? How does the proposed method improve upon existing approaches?

Explicitly highlight the key advantages of the new assessment technique. What performance gains or other benefits does it provide compared to baseline methods? 

Structure the paper to guide the reader seamlessly from the problem statement, to the methodological details, and finally to a clear conclusion about the merits and recommended use cases of the new assessment strategy.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates domain-adapted sentence embeddings for document retrieval. It proposes a systematic method to obtain thresholds for similarity scores for different embeddings, and proves that fine-tuning and pretraining-then-fine-tuning help improve retrieval accuracy through extensive experiments.

### Strengths
- This paper proposes a systematic method to introduce thresholds to improve document retrieval performance.
- Extensive experiments are conducted to demonstrate that fine-tuning and pretraining-then-fine-tuning help improve retrieval accuracy.

### Weaknesses
 - Lack of novelty: Much existing work has shown that fine-tuning or continued pretraining helps to improve domain performance [1]. The isotropy problem has been well studied in [2][3] and many other contrastive learning-based sentence embeddings.
- There are too many research questions in this paper. It looks like the RQ2 and RQ3 don't have a strong connection to the research topic, i.e., domain-adapted sentence embeddings.
- Poor organization. The current introductory section functions as a literature review. It is suggested to clarify the research problem, research gap and contribution in the introduction.

### Questions
- It is unclear why the CI is set to 95%. Is there any supporting evidence?
- The ndcg is widely used to evaluate information retrieval performance. Why not use it?

### Soundness
2

### Presentation
1

### Contribution
1
