# ImplicitSLIM and How it Improves Embedding-based Collaborative Filtering

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 3, 8, 6

## Abstract
We present ImplicitSLIM, a novel unsupervised learning approach for sparse high-dimensional data, with applications to collaborative filtering. Sparse linear methods (SLIM) and their variations show outstanding performance, but they are memory-intensive and hard to scale. ImplicitSLIM improves embedding-based models by extracting embeddings from SLIM-like models in a computationally cheap and memory-efficient way, without explicit learning of heavy SLIM-like models. We show that ImplicitSLIM improves performance and speeds up convergence for both state of the art and classical collaborative filtering methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a method named implictSLIM that can be integrated with other embedding-based methods.

### Strengths
Strengths:

-	The approaches addresses the memory-intensive and scalability issues of SLIM-like models in collaborative filtering.
-	The authors provided various experiments on publicly available benchmark datasets 
-	Source code is also provided 
-	Many appendices were given for more explanation

### Weaknesses
Weaknesses:

- In Section 3 Proposed Approach, the justification for specific formula choices in the development of ImplicitSLIM requires further elaboration. For instance, the rationale behind employing LLE while utilizing the neighborhood of NN(i) = {1,2,…,I} \ {i} to achieve a 'global' scope (Section 3.1) is not adequately explained. Furthermore, the decision to omit the sum-to-one constraint (Section 3.2) lacks a compelling justification. The authors acknowledge the absence of strong reasons, but a more in-depth discussion is necessary. Section 3 is pivotal to the paper, and a more thorough explanation and analysis of these design choices are crucial to enhance the persuasiveness of the proposed approach.

- The claim in the first paragraph after Figure 2 regarding ALS applied to MF being "about 5x faster" lacks supporting evidence. The location of this '5x faster' comparison within the paper is unclear and needs to be explicitly referenced or further detailed in the appendix.

- Figure 1 does not provide results for ImplicitSLIM init + SLIM reg and SLIM-LLE init with embedding dimensions greater than 500. The paper should elaborate on the 'high computational costs' associated with these configurations, potentially through an appendix dedicated to computational complexity analysis.

- The statement in Section 4.1, last sentence, regarding the potential instability of the procedure and its relation to fewer calls to ImplicitSLIM needs clarification. The connection between instability and the frequency of ImplicitSLIM calls is not immediately obvious and requires a more detailed explanation.

- The performance results presented in Table 1 are not particularly compelling. For example, in Appendix E.1, the authors suggest that "ImplicitSLIM is also faster than EASE… could replace EASE in some cases due to lower computational time and comparable performance." However, the specific scenarios where ImplicitSLIM could effectively replace EASE are not clearly defined. A more concrete delineation of these cases is needed.

- In Appendix E.3, Table 5, it is unclear why RecVAE + ImplicitSLIM fails to outperform RecVAE. A more detailed analysis of this result would be beneficial.

- The current ordering of references makes it difficult to follow. A standardized sorting approach would improve readability (minor).

Overall, more works need to be done.

### Questions
Please refer to the above comments.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper proposes a novel unsupervised learning approach for sparse high-dimensional data. The method learns local structure of data (embeddings) in the embedding space where the embeddings of similar objects to be similar.

### Strengths
This paper learns embeddings with closed form solutions.
Good Experimental study.

### Weaknesses
 - not a standalone approach which makes training less straightforward
- applicable to embedding-based models only
- the source code is not provided

### Questions
This paper is too theoretical than any other submissions on NeurIPS and ICLR. I hardly follow the content.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces ImplicitSLIM, an approach leveraging insights from established linear models such as EASE and LLE. The authors advocate its use for initializing and regularizing item and user embeddings across various collaborative filtering architectures. ImplicitSLIM streamlines the process of extracting embeddings, exhibits robust generalization capabilities, and accelerates convergence of the downstream models. As a comparatively lightweight and effective solution, it has the potential to become a valuable tool in representation learning for collaborative filtering, contributing to both theoretical understanding and practical implementation. 

The text is well-written and easy to follow. The presentation of the approach is transparent and mathematically sound. The obtained results are convincing and demonstrate the advantages of the proposed solution. I'd vote to accept the paper.

### Strengths
- mathematically sound approach with a closed-form solution
- showcases practical efficiency in the standard collaborative filtering task
- good generalization capabilities

### Weaknesses
 - The paper introduces various settings for ImplicitSLIM, but it would be beneficial to analyze and summarize the computational complexity of different variants respectively to provide a clearer understanding of their efficiency.
- The paper could benefit from more detailed experimental studies on the influence of hyperparameters. Given the presence of multiple regularization and optimization items in the method, it would be more illustrative to have the model performance w.r.t. different parameter settings.
- Although ImplicitSLIM has shown competitive performance against traditional linear encoders, it shows limitted improvement on deeper models like UltraGCN and RecVAE.

### Questions
There's a promise to provide empirical comparison with more natural-looking regularizer in Appendix E.2. However, not much information is provided there. The promise creates an expectation that there will be a more substantial comparative data with numbers and graphs. Is it planned to be provided?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on an influencial autoencoder-based collaborative filtering model SLIM and draws inspiration from its optimization objective and correspondingly proposes ImplicitSLIM. ImplicitSLIM combines the advantages of SLIM's objective function and Locally Linear Embeddings. ImplicitSLIM also introduces a novel regularization item and an initialization method for embedding-based collaborative filtering models. Experimental results are presented to demonstrate the effectiveness of the proposed model.

### Strengths
+ The authors propose a novel and general method that enhances performance of embedding-based CF models, which has practical significance.
+ The theoretical analysis of existing works on autoencoder-based models is persuasive and easy to follow. The paper provides a clear and insightful review of existing methods from an optimization perspective.
+ ImplicitSLIM is well-motivated and presents a novel solution for embedding-based CF.
+ The paper is generally well-written, ensuring readability and clarity.

### Weaknesses
- The paper introduces various settings for ImplicitSLIM, but it would be beneficial to analyze and summarize the computational complexity of different variants respectively to provide a clearer understanding of their efficiency.
- The paper could benefit from more detailed experimental studies on the influence of hyperparameters. Given the presence of multiple regularization and optimization items in the method, it would be more illustrative to have the model performance w.r.t. different parameter settings.
- Although ImplicitSLIM has shown competitive performance against traditional linear encoders, it shows limitted improvement on deeper models like UltraGCN and RecVAE.

### Questions
Please refer to the weaknesses.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
