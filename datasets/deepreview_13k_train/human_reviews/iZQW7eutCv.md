# pEBR: A Probabilistic Approach to Embedding Based Retrieval

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Embedding retrieval aims to learn a shared semantic representation space for both queries and items, thus enabling efficient and effective item retrieval using approximate nearest neighbor (ANN) algorithms. In current industrial practice, retrieval systems typically retrieve a fixed number of items for different queries, which actually leads to insufficient retrieval (low recall) for head queries and  irrelevant retrieval (low precision) for tail queries. Mostly due to the trend of frequentist approach to loss function designs, till now there is no satisfactory solution to holistically address this challenge in the industry.
    In this paper, 
    we move away from
    the 
    frequentist approach,
    and 
    take a novel \textbf{p}robabilistic approach to \textbf{e}mbedding \textbf{b}ased \textbf{r}etrieval (namely \textbf{pEBR}) by learning the item distribution for different queries, which    
    enables a dynamic cosine similarity threshold calculated by the probabilistic cumulative distribution function (CDF) value. The experimental results show that our approach improves both the retrieval precision and recall significantly.
    Ablation studies also illustrate how the probabilistic approach is able to capture the differences between head and tail queries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a probabilistic approach to embedding-based retrieval, which allows for the design of a dynamic retrieval cutoff strategy tailored to different types of queries.

### Strengths
The paper is generally well-written with a clear motivation from the weaknesses of existing frameworks. The authors present empirical evidence to the central research problem.

### Weaknesses
1. The authors claim that the paper is the first to introduce probabilistic modelling into embedding based retrieval, which remains doubtful to me. Probabilistic embedding has a long history in machine learning, as well as probabilistic information retrieval, at least dating back to probabilistic ranking principle (Robertson, 1977), which essentially seeks to model the relevance of items to a query. Such literature was not reviewed in the paper. Furthermore, this formulation for modelling the retrieval probability and learning embeddings based on contrastive losses is not new to the community (see [1] and the references therein). 

2. Given the development of embedding retrieval models, the chosen baseline DSSM is quite old (2013). which cannot substantiate the usefulness of the proposed method over existing approaches.

### Questions
1. In Section 3.3.2, the current model pEBR also relies on the chosen threshold $t$. Could the authors explain how sensitive it is to the model performance and at what value one should set it in practice? 

2. The choice of fixed threshold for $K$ items is mainly for saving inference cost. As detailed in Appendix A, it seems that computing the probabilistic CDF threshold can be slow, thus practically undesirable given the time constraints. If this system is in place, could the authors verify this has little impact on the product experience? 

3. The authors claim that without the probabilistic assumption, the model can fall short of generalisation ability. Any empirical evidence to support this, in comparison with the frequentist approaches?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a probabilistic framework for performing retrieval with embedding models. The rationale is that standard techniques that usually employ fixed number of items to retrieve or with a tuned score will impact precision and recall metrics for different queries. The authors propose a probabilistic approach in the setting of two-tower approaches, by extending the InfoNCE loss. The approach is evaluated in a dataset of user click logs and compared with two baselines.

### Strengths
The work is around dense embedding retrieval which is an important topic specially in industrial applications with large catalogs of items.
It is interesting to see this probabilistic approach for retrieving items as it avoids using standard approaches which may bring inefficiencies.

### Weaknesses
It would be great if the authors could enhance the related work with probabilistic embedding approaches especially few from the domain of images and metric learning and also draw some parallels.For example, Probabilistic Embeddings for Cross-Modal Retrieval, CVPR 2021.
One could use such an approach for performing retrieval tasks as it models uncertainty.

Is very difficult to assess the result. Could you please give more details for the dataset? What type of user log are these? How the model that you train looks like? What features do you have? How large is the set of unique items? The dataset as well as the architecture used is described very briefly.

Why you select such a large number for k? Does this artificially inflate the metrics you measure? Usually we would try to retrieve a small set of elements to feed to a ranker.

How significant is the result that you achieve? How this affects the ranking stage?

The experimentation part is very weak and is hard to assess the effectiveness of the approach.

### Questions
Please previous comments.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers a MLE rather than frequentist approach to training retrieval embeddings. The model posits a PDF for the relevance of a document to a query based on the inner product of the representation of the query and the document (Beta distribution). Subsequent optimization for the model parameters yields the vector representation. The dataset used contains 87M clicks and the result improves over the DSSM model on both precision (by small largin) and recall (by a bigger margin, especially on tail data).

### Strengths
1. Improved precision compared to DSSM, especially on tail queries. Recall is better than DSSM but by a small margin.
2. The model produces a variable number of results based on relevance cutoff. So where there are more results relevant to a query, the model can retrieve more of them compared to DSSM.

### Weaknesses
1. Assessment is sparse. The baseline chosen, DSSM, is rather old (from 2013). The lack of comparison against more recent models makes it difficult to assess the true contribution of the proposed method. The improvements over DSSM, while present, might not be significant when compared to state-of-the-art retrieval models that incorporate more advanced techniques such as attention mechanisms or transformer architectures. The paper would benefit from a more thorough evaluation against a wider range of baselines.
2. Comparison on one dataset and its unclear if it is public. The evaluation on a single dataset limits the generalizability of the findings. Without knowing the characteristics of this dataset, it's hard to determine if the observed improvements are specific to this dataset or if they would hold across different domains or data distributions. The lack of public availability of the dataset also hinders reproducibility and independent verification of the results.

### Questions
1. Can you comment on the dependence on the amount of training data? Would the precision and recall be higher with much smaller click data than 87M clicks?
2. Why not compare to SoTa model for retrieval?
3. Have you tried evaluated it on other public datsets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
