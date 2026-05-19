### Summary

This paper proposes a graph-based framework for out-of-distribution (OOD) generalization and detection. The framework utilizes spectral learning with wild data (SLW), which involves constructing a graph from the data and performing spectral decomposition on it. The paper shows that minimizing the SLW objective is equivalent to performing spectral decomposition, which allows for quantifying OOD generalization and detection performance. The paper also provides empirical results demonstrating the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method is novel and theoretically grounded, with a clear equivalence shown between minimizing the SLW objective and performing spectral decomposition on the graph.
- The paper provides a unified framework for OOD generalization and detection, which are often addressed separately in the literature.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is hard to follow. Section 4 (Theoretical Analysis) is particularly difficult to understand. For example, the meaning of the statement "We further define the top-k singular vectors of \tilde{A} as V_k \in R^{N × k}, so we have F_k = V_k \sqrt{\Sigma_k}, where \Sigma_k is a diagonal matrix of the top-k singular values of \tilde{A}" is unclear. Specifically, the relationship between the low-rank approximation of the adjacency matrix and the singular value decomposition is not well explained. The connection between the graph Laplacian (implicitly used through spectral decomposition) and the desired OOD properties is also not made explicit, leaving the reader to guess how the spectral properties relate to generalization and detection.
- The empirical evaluation in Section 5 is not very convincing. The performance of the proposed method is not compared to that of existing methods. For example, the paper does not compare the proposed method to the method in "A unified out-of-distribution detection and generalization framework for pre-trained feature distributions" (Bai et al., 2023). It is unclear if the baselines are properly tuned, and the choice of datasets seems limited, potentially affecting the generalizability of the results. The paper also lacks a thorough ablation study to justify the design choices of the proposed method.
- There are some typos in the paper. For example, in the caption of Figure 2, "ordered by: angel sketch, tiger sketch, tiger painting, angel painting, and panda" should be "ordered by: angel sketch, tiger sketch, angel painting, tiger painting, and panda". I am not sure if the theorem proofs are correct, as I have not checked them in detail.

### Suggestions

The paper needs a more detailed explanation of the theoretical framework in Section 4. The connection between the graph construction, spectral decomposition, and OOD generalization/detection should be made more explicit. For instance, the authors should clarify how the spectral properties of the graph Laplacian relate to the desired OOD properties. A more thorough explanation of the low-rank approximation and its connection to the singular value decomposition is needed. It would be beneficial to include a toy example to illustrate the theoretical concepts and make them more accessible to the reader. The authors should also provide more intuition behind the choice of the graph construction method and how it relates to the problem at hand. Furthermore, the authors should clarify the assumptions made about the data distribution and how these assumptions affect the theoretical results. The current presentation leaves the reader struggling to connect the theoretical framework to the practical application.

The empirical evaluation needs significant improvement. The authors should compare their method against a wider range of existing OOD generalization and detection methods, including the method proposed by Bai et al. (2023). The baselines should be properly tuned, and the tuning process should be described in detail. The choice of datasets should be expanded to include more diverse and challenging benchmarks. A thorough ablation study is necessary to justify the design choices of the proposed method, such as the graph construction parameters and the choice of spectral decomposition method. The authors should also provide a more detailed analysis of the results, including error bars and statistical significance tests. The current evaluation lacks the necessary rigor to support the claims made in the paper. It is also important to clarify how the proposed method performs on different types of OOD shifts, such as covariate shift and concept shift.

Finally, the paper needs a thorough revision to fix the typos and improve the overall clarity. The authors should ensure that all mathematical notations are consistent and well-defined. The proofs of the theorems should be carefully checked and clearly explained. The paper would benefit from a more structured presentation, with clear definitions, assumptions, and conclusions. The authors should also consider adding a table of notations to make it easier for the reader to follow the mathematical arguments. The current writing style is not sufficiently clear and precise, making it difficult for the reader to fully understand the proposed method and its theoretical underpinnings. The authors should also consider adding a more detailed discussion of the limitations of the proposed method and potential directions for future research.

### Questions

See the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
