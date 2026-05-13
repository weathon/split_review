# Memory-Efficient Self-Supervised Contrastive Learning with a Supervised Loss

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Contrastive Learning (CL) is among the most popular methods for self-supervised representation learning. However, CL requires a large memory and sample size and careful hyperparameter tuning.
These factors make it difficult to
learn high-quality representations with limited amount of memory. In this work, we theoretically analyze a recently proposed \textit{supervised} approach, DIET, for self-supervised representation learning. DIET labels every example by its datum index and trains on the labeled data with a supervised loss. DIET does not require a large sample size 
or hyperparameter tuning. However, it falls short when using smaller encoders and is memory intensive due to its massive classifier head.
Given its remarkable simplicity, it is not obvious whether DIET can match the performance of CL methods, which explicitly model pairwise interactions between augmented examples. We prove that, perhaps surprisingly, for a linear encoder DIET with MSE loss is equivalent to spectral contrastive loss. Then, we prove that DIET is prone to learning less-noisy features and may not learn all features from the training data. We show feature normalization can provably address this shortcoming and use of a projection head can further boost the performance. Finally, we address the scalability issue of DIET by reducing its memory footprint.
The modified approach, namely S-DIET, substantially improves on the linear probe accuracy of DIET across a variety of datasets and models and 
outperforms other SSL methods,
all with limited memory and without extensive hyperparameter tuning. This makes S-DIET a promising alternative for simple, effective, and memory-efficient representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies DIET, which is a method that has rather few adoptions. This paper claims that DIET uses fewer memory than common contrastive learning approaches, and proved some theoretical results showing that DIET and spectral contrastive learning share the same solutions. Moreover, this paper proposes a new alternative S-DIET to further improve its performance.

### Strengths
1. This paper has theoretical claims that connects DIET to CL.
2. This paper has some empirical evidence that the proposed S-DIET can match the performance on benchmarks like CIFAR and ImageNet-100.

### Weaknesses
The method DIET studied in this paper has a fatal limitation, which is that the labels are essentially the sample index. As the dataset size increases, the classification head will need to increase linearly as well, which makes it impractical to use in large scale dataset training. Even though the proposed S-DIET does not require the classification head to be always loaded into the memory, it is still unnecessary to store such a large head, especially when one is training on millions of data. The core issue is that the classifier's weight matrix has dimensions of N x m, where N is the number of samples and m is the embedding dimension. This means that for a dataset like ImageNet with over a million images, the classifier head alone will have millions of rows, making it very cumbersome to store and manage, even if it's not all loaded into memory at once. This linear scaling with dataset size is a significant drawback compared to other contrastive learning methods that use a fixed-size classifier or projection head.

### Questions
None

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents S-DIET, a memory-efficient modification of DIET for self-supervised contrastive learning. It proves that DIET with a linear encoder and MSE loss is theoretically equivalent to spectral contrastive loss, and proposes feature normalization and projection head use to enhance performance. S-DIET significantly reduces DIET's memory requirements and achieves state-of-the-art performance without extensive hyperparameter tuning.

### Strengths
1. The paper provides comprehensive and rigorous theoretical proofs.
2. Addressing the high memory demand of DIET is a well-motivated objective with strong practical significance.
3. The experimental results presented in Table 5 demonstrate promising improvements.
4. The paper conducts a detailed and insightful ablation study.

### Weaknesses
1. The paper aims to address three issues: why DIET can perform comparably to CL, DIET's failure to learn all features, and its high memory demand. However, these issues are addressed in a fragmented manner without clear logical connections between them, making it difficult for readers to grasp the paper's central thesis. For instance, the theoretical analysis in Section 4 focuses on the equivalence of DIET and spectral contrastive loss under MSE, but this connection is not clearly tied to the practical modifications proposed in Section 5, which include feature normalization and a projection head. The paper lacks a cohesive narrative that integrates these different aspects into a unified argument.
2. The paper does not provide code or pseudocode, which hinders understanding of the proposed method and limits the ability to verify its effectiveness. While the authors describe the method, the lack of a concrete implementation makes it difficult to assess the practical implications of the proposed memory-efficient modifications. The absence of pseudocode, in particular, makes it challenging to understand the exact sequence of operations and data flow within the S-DIET algorithm.
3. It is well-known that MSE is not typically used as a loss function for classification tasks. In the original DIET paper, each sample is treated as a separate class in a classification problem using cross-entropy loss. Why, then, is MSE employed as the loss function in Section 4? Does Theorem 4.5 hold if cross-entropy loss is used instead? The choice of MSE seems arbitrary and lacks sufficient justification, especially given the standard use of cross-entropy in similar contexts. The theoretical analysis should address this discrepancy and explain why MSE is a suitable proxy for the intended learning objective.
4. Due to the use of W1, it is unclear how Theorem 4.3 is related to the proposed method. The introduction of W1 in the theorem statement seems disconnected from the practical implementation of S-DIET, which does not explicitly use such a term. This disconnect makes it difficult to understand the theoretical relevance of Theorem 4.3 to the overall contribution of the paper.
5. The theoretical analysis in the paper relies entirely on linear assumptions, while the proposed method (Equation 5) is based on empirical assumptions. These assumptions raise concerns about the rigor of this work. The theoretical results are derived under the assumption of linear models and MSE loss, which are not representative of the non-linear models and more complex loss functions typically used in self-supervised learning. The empirical modifications, such as feature normalization and the projection head, are not directly supported by the theoretical framework, raising questions about the validity of the theoretical analysis in the context of the proposed method.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The manuscript studied the property of a supervised representation learning, called DIET, and then propose an improved version of this method. Specifically, the authors show the equivalence between DIET and spectral contrastive loss proposed by HaoChen \& Ma under a linear case. In addition, the improvement is motivated by the insight derived from the model introduced in the setting of Section 5.1. Although it looks interesting when all the strong assumptions are true, it is unclear if the results presented in the manuscript can provide guidance in the practical settings.

### Strengths
The connection between DIET and spectral contrastive loss is interesting.

### Weaknesses
The analysis is built on some unrealistic assumptions. It is unclear whether the results and development in the manuscript can hold in practice.  It could be more meaningful to make assumptions more carefully.

The review in the manuscript is clearly incomplete. Some important literature are missing. The author may want to have a more comprehensive literature review.

The analysis in the Section 4 is not surprising due to the linear setting. Can the analysis be extended to the nonlinear case? The author may read the recent development under the nonlinear setting in Wang 2023.

Assuming $W_H$ is an isometry seems a very strong assumption. Do the authors put a constraint for $W_H$ in the loss function to enforce such isometry? Otherwise, the authors may consider removing this assumption.

The form of training example introduced in Section 5 is unrealistic. When does this assumption hold (at least approximately) in piratical example? Why are there two features, one is low noise and the other is high noise?

Can we generalize the results in Theorem 5.1 to a more realistic setting?

The idea in memory-efficient DIET is straightforward.

### Questions
1) The review in the manuscript is clearly incomplete. Some important literature are missing. The author may want to have a more comprehensive literature review. 

2) The analysis in the Section 4 is not surprising due to the linear setting. Can the analysis be extended to the nonlinear case? The author may read the recent development under the nonlinear setting in Wang 2023. 

3)Assuming $W_H$ is an isometry seems a very strong assumption. Do the authors put a constraint for $W_H$ in the loss function to enforce such isometry? Otherwise, the authors may consider removing this assumption.

4)The form of training example introduced in Section 5 is unrealistic. When does this assumption hold (at least approximately) in piratical example? Why are there two features, one is low noise and the other is high noise?

5)Can we generalize the results in Theorem 5.1 to a more realistic setting?

6) The idea in memory-efficient DIET is straightforward.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study provides a theoretical analysis of DIET, a recently proposed supervised approach for self-supervised learning. DIET, as a menthod of CL, labels each example by its datum index and employs a supervised loss for training. This work obtains several conclusions, including (i) for linear encoders, DIET with MSE loss is equivalent to spectral contrastive loss; (ii) DIET tends to learn features with less noise but may not capture all relevant aspects of the training data; (iii) feature normalization can help mitigate this issue, while incorporating a projection head can further enhance performance. This work further introduces SCALED-DIET (S-DIET) to improve the model's linear probe accuracy.

### Strengths
- This paper explore the limitation of DIET, an important method of CL, and obtain several conclusions: (i) for linear encoders, DIET with MSE loss is equivalent to spectral contrastive loss; (ii) DIET tends to learn features with less noise but may not capture all relevant aspects of the training data; (iii) feature normalization can help mitigate this issue, while incorporating a projection head can further enhance performance. 

- This work further introduces SCALED-DIET (S-DIET) to improve the model's linear probe accuracy, i.e., use batch cross entropy and the multistep update formula for AdamW.

- Some experiments demonstrate the effectiveness of the proposed S-DIET.

### Weaknesses
 - The motivation behind this paper is unclear. According to P2 in the Introduction, DIET's advantage lies in its ability to mitigate CL's reliance on large datasets, while requiring a smaller parameter dimension to balance with sample size. The claim that smaller encoder dimensions are a key drawback for handling large data is not well justified. Furthermore, the authors state, "not clear whether DIET can capture the pairwise similarities between views...SSL," yet DIET, as a CL algorithm utilizing supervised loss, does not explicitly depend on pairwise similarities; this is merely an implementation choice rather than a fundamental mechanism. I fail to see how this motivation strongly connects DIET with contrastive loss, is pairwise similarity closely related to memory? While exploring CL from an efficiency perspective do be valuable, a thorough reading of the paper reveals a lack of such information. Perhaps I overlooked some details, and I hope the authors can clarify their insights.

- The key conclusions in this work need further explanation in relation to the core ides, i.e., MEMORY-EFFICIENT. For instance, the relationships between memory and features, encoder parameter dimensions, and projection heads are not adequately described, leading to fragmented conclusions.

- The choice to study DIET is justified by its independence from large training data, but there are other CL algorithms that also do not rely on large datasets, such as few-shot SSL. Additionally, DIET requires labeled information. Can the analyses in this work be applied to these other methods? If so, what differentiates this work? A broader exploration of algorithms and their mechanisms might enhance the reliability of this study.

- A code that can reflect the idea of ​​algorithm implementation is encouraged, since it is currently only described in 6 lines. At the same time, the introduction of these modules will increase the computational overhead, and related experiments are also necessary, after all, the focus is on memory.

- (Minor) The paper's template appears to differ from the one provided on the official website, such as in the line numbering. Please consider making further corrections.

### Questions
Please see **Weaknesses**.

### Soundness
2

### Presentation
2

### Contribution
2
