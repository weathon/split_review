# On the Embedding Collapse When Scaling up Recommendation Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Recent advances in foundation models have led to a promising trend of developing large recommendation models to leverage vast amounts of available data. \lms{Still}, mainstream models \lms{remain embarrassingly small in} size and na\"ive enlarging does not lead to sufficient performance gain, suggesting a deficiency in the \emph{model scalability}. In this paper, we identify the \emph{embedding collapse} phenomenon as the inhibition of scalability, wherein the embedding matrix tends to occupy a low-dimensional subspace. Through empirical and theoretical analysis, we demonstrate a \emph{two-sided effect} of feature interaction specific to recommendation models. On the one hand, interacting with collapsed embeddings restricts embedding learning and exacerbates the collapse issue. On the other hand, interaction is crucial in mitigating the fitting of spurious features as a scalability guarantee. Based on our analysis, we propose a simple yet effective \emph{multi-embedding} design incorporating embedding-set-specific interaction modules to learn embedding sets with large diversity and thus reduce collapse. Extensive experiments demonstrate that this proposed design provides consistent scalability and effective collapse mitigation for various recommendation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies recommendation model performance when scaling up the embedding layers of the model. The paper identifies a phenomenon of embedding collapse, wherein the embedding matrix tends to reside in a low-dimensional subspace. Through empirical experiments on FFM and DCNv2 and theoretical analysis on FM, the paper shows that the feature interaction process of recommendation models leads to embedding collapse and thus limits the model scalability. The paper also performed empirical experiments on regularized DCNv2 and DNN which led to less collapsed embeddings, but the model performance got worse. The paper proposes multi-embedding, which leads to better performance when scaling up the embedding layers. Experiments demonstrate that this proposed design provides consistent scalability for various recommendation models.

### Strengths
Originality: 
- The paper investigates the enlarged embedding layers of recommendation models and identifies a phenomenon of embedding collapse, wherein the embedding matrix tends to reside in a low-dimensional subspace. The discovery is novel as far as I know.
- The paper proposed information abundance to measure the degree of collapse for embedding matrices.

Quality:
- The paper is well-written. It starts with a novel finding of embedding collapse when increasing embedding dimension which might lead to poor scalability, performs empirical experiments and theoretical analysis to show that it is caused by feature interaction, and proposes a solution to increase scalability.

Significance:
- The scaling law of recommendation models is an important topic in both academia and industry. This paper investigates the scaling law of embedding layers and shows why naively increasing embedding dim is not sufficient for scalability. The paper proposed multi-embedding which could help alleviate the phenomenon of embedding collapse and improve scalability.

### Weaknesses
 - In section 3, the paper proposes Information Abundance to measure the degree of collapse of embedding matrices. As the paper focuses on the scaling law of embedding layers, the paper should discuss whether Information Abundance is a fair metric when comparing embedding matrices of different dimension sizes. Specifically, it's unclear if a higher Information Abundance value for a higher-dimensional embedding necessarily indicates a less collapsed state, or if it's simply an artifact of the increased dimensionality. The paper needs to address the inherent bias that might exist when comparing matrices of different sizes using this metric.
- In section 4.2, the paper uses regularized DCNv2 as an example to show that suppressing feature interaction is insufficient for scalability. It is unclear to me why feature interaction in regularized DCNv2 is suppressed. The paper should elaborate on the specific mechanisms within the regularized DCNv2 that lead to reduced feature interaction, and how these mechanisms relate to the observed changes in embedding collapse and model performance. A more detailed explanation of the regularization process and its effect on the interaction layers is needed.
- The performance of multi-embedding lacks ablation study. One example is that in Figure 7 (right), we can feed all 4 small embeddings into a single feature interaction layer, and test its performance against the proposed approach. We can also test the Information Abundance of such design versus the proposed multi-embedding design. This would provide a clearer understanding of whether the performance gains are due to the multi-embedding architecture itself, or simply due to the increased number of parameters. Furthermore, it would be beneficial to explore other ablation studies, such as varying the number of sub-embeddings, or their individual dimensions, to understand the sensitivity of the proposed approach to these parameters.
- It would be interesting to test the scaling law of embedding layers with increased feature interaction complexity. This can help us better understand whether the embedding collapse phenomenon is caused by insufficient feature interaction complexity. The paper should investigate whether increasing the number of cross layers or the hidden dimension of the interaction layers can further mitigate the embedding collapse and improve the model performance. It is crucial to isolate the effect of feature interaction complexity from other factors, such as embedding dimension, to draw more concrete conclusions about the cause of embedding collapse.

### Questions
My questions are listed in the weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper suggests that the embedding collapse phenomenon restricts the scalability of existing recommendation models. Empirical and theoretical analysis show that interaction with collapsed embeddings constrains embedding learning. Also, this paper proposes a multi-embedding design incorporating embedding-set-specific interaction modules to capture diverse patterns and reduce collapse.

### Strengths
S1. This paper provides empirical and theoretical analysis of the embedding collapse phenomenon.

S2. This paper provides information abundance for quantifying the degree of collapse for such matrices with low-rank tendencies.

### Weaknesses
W1. The novelty of this paper seems to be limited. The method of dividing the single embedding into multi-embedding sets is similar to DMRL [1] for disentangled representation learning. DMRL divides the feature representation of each modality into k chunks. As a result, the features of different factors are entangled. Specifically, the proposed multi-embedding design bears a resemblance to the chunked embedding approach used in DMRL, where each modality's feature representation is divided into multiple chunks to facilitate disentangled representation learning. While this approach aims to capture different factors of variation, it may inadvertently lead to entanglement between features belonging to different modalities. A more thorough comparison with DMRL, highlighting the differences in terms of handling feature interactions and mitigating embedding collapse, would strengthen the paper's contribution.

W2. The motivation is not completely solid. The reason for increasing the embedding size of the model is inappropriate. The paper argues for increasing the embedding size as a means to improve model scalability. However, simply increasing the embedding dimension without considering the potential drawbacks, such as increased computational cost and the risk of overfitting, is not well-justified. The authors should provide a more convincing rationale for why larger embedding sizes are necessary, especially in light of the embedding collapse phenomenon discussed in the paper. It would be beneficial to explore the trade-offs between embedding size, model performance, and computational efficiency.

W3. The experimental results of the paper are insufficient. When the embedding size was scaled up through multi-embedding, the experimental results show that performance increases. However, the performance improvement is marginal. The reported performance gains from scaling up the embedding size using the multi-embedding approach are relatively small. While the authors demonstrate that their method can lead to improvements, the magnitude of these gains does not appear to be substantial enough to warrant the added complexity of the multi-embedding design. A more comprehensive evaluation, including comparisons with alternative approaches for scaling up recommendation models, would be necessary to establish the practical significance of the proposed method.

### Questions
Depending on the model and dataset, the model will have an appropriate embedding size. Therefore, it seems reasonable that the performance will drop if the embedding size deviates from the proper value. Then. do we need to scale up the embedding size for the same dataset?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses challenges in scaling up recommendation models, identifying a phenomenon called "embedding collapse" while enlarging models. The authors introduce information abundance as a metric to measure and evaluate collapse. They show that embedding matrix reside mostly in a low-dimensional subspace in scaled up models. The study analyzes feature interactions in models, noting they reduce overfitting but can also exacerbate embedding collapse. To tackle this, the authors introduce a multi-embedding design, scaling independent embedding sets and integrating specific interaction modules. This approach claims to improve scalability across various recommendation models. Main contributions:
- Highlight non-scalability in recommendation models and define the "embedding collapse" phenomenon.
- Empirical and theoretical analysis reveals the dual impact of feature interaction on scalability.
- Introduction of the multi-embedding design to achieve scalability improvements for recommendation models.

### Strengths
Originality:
- ‘Information Abundance' as a quantitative novel measure to measure the embedding layer collapse.
- The 'Interaction-Collapse Law' and the two sided effect of feature interaction process helps improve the understanding of embeddings' behavior in recommendation systems.

Quality:
- The authors have detailed exploration of embeddings and their behavior, particularly in the context of information collapse with rigorous visualizations. 

Significance:
- Broad Implications for Recommendation Systems: Given the ubiquitous nature of recommendation systems in today's digital platforms, insights into their workings, particularly regarding embeddings, have widespread implications.
- Potential for Future Research: Introducing novel concepts and metrics invariably opens the door for future studies, both to validate and to build upon these ideas. The 'Interaction-Collapse Law', for instance, may become a focal point in subsequent research.

### Weaknesses
1. Insufficient Empirical Validation on Large-Scale Data: The authors have shown with empirical evidences that large scale recommendation models scale poorly. However it is a common knowledge that large scale models are inherently data hungry to achieve better model convergence. This is an important premise that the paper relies on, it would good if authors can follow up to prove/disprove this as additional data points in this paper. The experiments seem to be on same amount of training data on scaled up models which does not unlock the full power of the scaled up model

2. Studies on Collapse and its effect on scalability and overfitting seem to be limited to Single Embedding studies. To make a stronger case about the proposed method, it would be great if authors can provide discussion on the same for proposed Multi Embedding Design.

### Questions
1. How do you justify the experiment setup when we know that bigger models are inherently data hungry and need more training data to achieve full convergence?

2. From the experiment results shown, the single embedding and multi embedding cases show marginal improvement in AUC values. Can authors provide more context on the significance of the improvements here and if they are well outside the noise region?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper observes scaling the embedding dimensionality does not lead to satisfactory improvement in recommendation models and claims this is due to the dimensional collapse problem where the learned embedding vector spans only on lower dimensional subspace. The paper further claims such problem will propagate by feature interaction module when a feature embedding interacts with collapsed embeddings and regularization could mitigate collapse but harms the performance. Thus this paper proposes an alternative approach to address the embedding collapse issue, namely to replace single embedding in the original model with multiple embeddings. The paper shows the proposed approach lead to higher "information abundance" which is ratio between sum of absolute singular values and the largest singular value, indicate the "spreadness"/concentration of the singular value distribution. The paper also applied the proposed approach on several recommender models on two datasets, shows a absolute improvement of AUC on 1e-3 ~ 1e-4 level, when scaling the number of multi-embeddings. 

initial recommendation: weak reject, for reasons please see the weak points.

### Strengths
* The claim about the dimensional collapsing problem when scaling the dimensionality of feature embeddings in recommender system is reasonably supported in the paper and sound.
* The analysis about the trade off between feature embedding collapsing and the regularization level of feature interaction is interesting and reasonable. 
* The paper is easy to follow

### Weaknesses
 * The computation of "information abundance" for multi-embedding setting is not clearly defined in the paper. As show in the Figure 1.b for features with low predictive power would have embedding with low "information abundance" ratio, and scaling the dimensionality would further lower the ratio. Thus if the ratio for multi embedding is computed by averaging over the small embeddings, the lower ratios for some small embeddings will be compensated. This possibility makes the proposed abundance ratio less reliable. 
* The idea of multi-facet embedding or polysemy embedding has been studied quite extensively in the past. From network embedding (Liu et al. Is a single vector enough? exploring node polysemy for network embedding) to recommender systems (Weston et al. Nonlinear latent factorization by embedding multiple user interests). However, non of the related work on multi-embedding has been discussed in the paper.
* The finding 1 was claimed to "applicable to general recommendation models instead of only the models with sub-embeddings" without being linked to any evidences. Also, I personally find find 1 is much a theory rather than a "law".

### Questions
* How is the "information abundance" for multi-embeddings computed? 
* How would the proposed multi-embedding approach be positioned in the literature?
* Please point out the evidence for the claim quoted in the third weak point.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
