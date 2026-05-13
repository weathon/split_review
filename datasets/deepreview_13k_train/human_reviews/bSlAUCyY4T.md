# Knowledge Graph Completion by Intermediate Variables Regularization

- Decision: Reject
- Scores: 5, 5, 3, 8

## Abstract
Knowledge graph completion (KGC) can be framed as a 3-order binary tensor completion task. Tensor decomposition-based (TDB) models have demonstrated strong performance in KGC. In this paper, we provide a summary of existing TDB models and derive a general form for them, serving as a foundation for further exploration of TDB models. Despite the expressiveness of TDB models, they are prone to overfitting. Existing regularization methods merely minimize the norms of embeddings to regularize the model, leading to suboptimal performance. Therefore, we propose a novel regularization method for TDB models that addresses this limitation. The regularization is applicable to most TDB models, incorporates existing regularization methods, and ensures tractable computation. Our method minimizes the norms of intermediate variables involved in the different ways of computing the predicted tensor. To support our regularization method, we provide a theoretical analysis that proves its effect in promoting low trace norm of the predicted tensor to reduce overfitting. Finally, we conduct experiments to verify the effectiveness of our regularization technique as well as the reliability of our theoretical analysis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses the tensor-decomposition based (TDB) methods on knowledge graph completion. It proposes a general form to unify previous TDB methods and proposes a new regularization to serve as a upper bound of previous regularizations. The proposed regularization is evaluated on three knowledge graph completion dataset.

### Strengths
1. The paper is very well-written. The reviewer enjoys reading the paper.

2. The proposed generic form of TDB unifies previous TDB-based KGC methods, which is not significant but a useful summary of the development of TDB-based methods on KGC. It would make the paper more useful if the authors could explain in detail how this generic form could benefit the community.

3. The reviewer appreciates the extensive evaluation on three datasets.

### Weaknesses
1. First, the experimental results look marginal. It might indicate that the new regularization is useful to prevent overfitting since it is a upper bound. However, what if we increase the coefficients of regularization in the baseline models? The experimental results does not show the effectiveness of the proposed new regularization.

2. Second, the proposed new regularization lacks motivation. The paper proves that the proposed new regularization is an upper bound of previous overlapped trace norm. However, the motivation of this new proposal is not well justified. Why an upper bound of the regularization is better in the optimization? It does not make sense to me.

3. The loss function in Section 3.2 is not well explained (Sorry, I do not see the parameters in the loss function). What are the parameters? W, H, T? I will assume $X$ indicates both the ground truth tensor value and the parameterized tensor value from W, H, T? Also, in the KGC applications, the loss function should have tensor mask to indicate the observed entries.

### Questions
See above. 

The reviewer likes the paper, however, the contributions and the usefulness of the proposal should be elaborated (the current version does not satisfy ICLR bar). I am willing to raise the score for further explanations.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The knowledge graph (KG) can be represented as a 3-way tensor. Hence, the knowledge graph completion can be naturally formed as a tensor completion task. In this paper, the author provided an overview of the tensor decomposition-based (TDB) models and derived a general form which is the summation of $D/P$ Tucker decompositions with shared core tensor $\boldsymbol{W} \in \mathbb{R}^{P \times P \times P}$. The main contribution of this paper is the proposed regularization term, which is applicable to the `general form' they proposed, by incorporating the existing regularization methods. The author claims that their novel regularization term minimizes the norms of intermediate variables for promoting low trace norm of predicted tensor. The theoretical analysis and experiments were provided to verify their claim.

### Strengths
Strengths:
1. Easy to read.
2. They provided numerical experiments on different datasets and methods.

### Weaknesses
Weaknesses:
The main focus should be the regularization term they proposed instead of the general form. The weakness is novelty and significance, which is limited by my point of view.
1. For the theoretical side, the nuclear p-norms and squared F-norm methods were well-studied. It's not a surprise that Equation 4 can generalize these, and this is not new. As the author claimed, they incorporated the N3 norm and DURA, where some of the analysis was established. Their weight IVR norm is not theoretically novel and significant. Could the author clarify what is the unique hardness and novelty of this proposed IVR norm?


2. For the experiment side, as the author claimed in the paper, their method promotes low rank. Do you actually see the zero columns in the factors, compared to the existing method?

### Questions
My question was put in the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the issue of overfitting in Tensor Decomposition-based (TDB) models used in Knowledge Graph Completion (KGC), where existing regularization methods, focused on minimizing the norms of embeddings, have led to suboptimal performance. A novel regularization method is proposed that minimizes the norms of intermediate variables involved in computing the predicted tensor, enhancing most TDB models by incorporating existing regularization techniques and ensuring tractable computation. Moreover, extensive evaluation verifies the effectiveness and superiority of the model.

### Strengths
1.	The authors propose a new KGC framework, establishing a general form to serve as a foundation for further TDB model analysis. which aims to tackle the issue of overfitting in Tensor Decomposition-based models.
2.	The authors provide a detailed theoretical analysis, e.g., showing the ability for its generality and effectiveness, which guarantees the validity of the method.

### Weaknesses
1. The paper is not organized clearly, which is not friendly for understanding. For instance, there are lack of an intuitive explanation for how this method can mitigate the overfitting issue.
2. The regularization approach as shown in Eq.(4) is too complex to use. Moreover, this paper miss some strong baselines such as [1][2]
[1] Low-Dimensional Hyperbolic Knowledge Graph Embeddings
[2] ER: equivariance regularizer for knowledge graph completion

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Tensor Decomposition-Based (TDB) models have been quite successful in the field of KGC. Despite the effectiveness of TDB models, they are susceptible to overfitting. Existing regularization methods typically focus on minimizing the norms of embeddings to control the model, resulting in suboptimal performance. To overcome this limitation, the authors introduce a novel regularization method tailored for TDB models. This regularization method can be applied to most TDB models, seamlessly integrating existing regularization techniques while maintaining computational efficiency.

The core of this method involves minimizing the norms of intermediate variables used in various ways to compute the predicted tensor. To support their proposed regularization approach, the authors provide a theoretical analysis that demonstrates its effectiveness in reducing overfitting by promoting a low trace norm of the predicted tensor.

### Strengths
The article is well-structured with detailed analysis and clear logic. The language is fluent and reader-friendly. The new regularization approach for TDB models demonstrates good performance.

### Weaknesses
The article is well-structured with detailed analysis and clear logic. The language is fluent and reader-friendly. The new regularization approach for TDB models demonstrates good performance.

The first contribution, which is a detailed overview of a wide range of TDB models, is somewhat limited in its actual content.
The experimental results could benefit from a more comprehensive comparison involving additional metrics such as efficiency and time-related measures.

### Questions
Could the authors further explain the difference between IVR and IVR-3 in Table 3? Need to clarify the metrics in the experiments. What do the results mean, like accuracy, error, or anything else?

Unclear meaning of the notation of (i, j, ?) above Section 3.3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
