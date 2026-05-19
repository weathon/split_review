### Summary

This paper proposes a graph-based framework for understanding both OOD generalization and detection, formalizing it by spectral decomposition of the graph containing ID, covariate-shift OOD data, and semantic-shift OOD data. The paper also provides theoretical insight by analyzing closed-form solutions for the OOD generalization and detection error, based on spectral analysis of the graph. The paper evaluates the model’s performance through a comprehensive set of experiments, providing empirical evidence of its robustness and its alignment with the theoretical analysis.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a novel graph-based framework for understanding both OOD generalization and detection, formalizing it by spectral decomposition of the graph containing ID, covariate-shift OOD data, and semantic-shift OOD data.
2. The paper provides theoretical insight by analyzing closed-form solutions for the OOD generalization and detection error, based on spectral analysis of the graph.
3. The paper evaluates the model’s performance through a comprehensive set of experiments, providing empirical evidence of its robustness and its alignment with the theoretical analysis.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is hard to follow. Section 4 (Theoretical Analysis) is particularly difficult to understand. For example, the meaning of the statement "We further define the top-k singular vectors of \tilde{A} as V_k \in R^{N × k}, so we have F_k = V_k \sqrt{\Sigma_k}, where \Sigma_k is a diagonal matrix of the top-k singular values of \tilde{A}" is unclear.
2. The empirical evaluation in Section 5 is not very convincing. The performance of the proposed method is not compared to that of existing methods. For example, the paper does not compare the proposed method to the method in "A unified out-of-distribution detection and generalization framework for pre-trained feature distributions" (Bai et al., 2023).
3. There are some typos in the paper. For example, in the caption of Figure 2, "ordered by: angel sketch, tiger sketch, tiger painting, angel painting, and panda" should be "ordered by: angel sketch, tiger sketch, angel painting, tiger painting, and panda". I am not sure if the theorem proofs are correct, as I have not checked them in detail.

### Suggestions

The theoretical analysis in Section 4 needs significant clarification to improve the paper's accessibility and impact. The current presentation lacks sufficient context and explanation, making it difficult to grasp the core ideas. Specifically, the introduction of the top-k singular vectors and their relationship to the low-rank approximation of the adjacency matrix needs to be more thoroughly explained. It would be beneficial to provide a more intuitive explanation of why the top-k singular vectors are used and how they relate to the graph structure and the OOD generalization and detection tasks. Furthermore, the connection between the spectral properties of the graph and the theoretical results should be made more explicit. The authors should consider adding illustrative examples or diagrams to help readers understand the theoretical framework. A more detailed explanation of the assumptions and limitations of the theoretical analysis would also be beneficial.

To strengthen the empirical evaluation, the authors should include a more comprehensive comparison with existing state-of-the-art methods. The absence of a comparison with the method proposed by Bai et al. (2023) is a significant oversight, given its relevance to the problem of OOD generalization and detection. The authors should also consider including other relevant baselines to provide a more complete picture of the performance of their proposed method. Furthermore, the experimental setup should be described in more detail, including the specific datasets used, the evaluation metrics, and the hyperparameter settings. It is also important to provide a more thorough analysis of the experimental results, including a discussion of the strengths and weaknesses of the proposed method compared to the baselines. The authors should also consider performing ablation studies to evaluate the impact of different components of their method.

Finally, the paper needs a thorough revision to address the identified typos and improve the overall clarity of the writing. The authors should carefully proofread the paper to ensure that there are no grammatical errors or typos. The proofs of the theorems should be carefully checked to ensure their correctness. The authors should also consider adding a table of notations to make it easier for the reader to follow the mathematical arguments. The paper would also benefit from a more structured presentation, with clear definitions, assumptions, and conclusions. The authors should also consider adding a more detailed discussion of the limitations of their method and potential directions for future research.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
