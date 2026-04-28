# Towards a Better Theoretical Understanding of Independent Subnetwork Training

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Modern advancements in large-scale machine learning would be impossible without the paradigm of data-parallel distributed computing. Since distributed computing with large-scale models imparts excessive pressure on communication channels, significant recent research has been directed toward co-designing communication compression strategies and training algorithms with the goal of reducing communication costs. While pure data parallelism allows better data scaling, it suffers from poor model scaling properties. Indeed, compute nodes are severely limited by memory constraints, preventing further increases in model size. For this reason, the latest achievements in training giant neural network models also rely on some form of model parallelism. In this work, we take a closer theoretical look at Independent Subnetwork Training (IST), which is a recently proposed and highly effective technique for solving the aforementioned problems. We identify fundamental differences between IST and alternative approaches, such as distributed methods with compressed communication, and provide a precise analysis of its optimization performance on a quadratic model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a theoretical analysis framework to understand the behavior of independent subnetwork training. Expanding previous work, this work enables analysis of model parallelism, which is widely used for training massive-scale neural network models. The authors analyze homogeneous and heterogeneous scenarios and suggest settings for efficient convergence. The authors provide limited experimental support to validate their analysis.

### Strengths
- First in class to analyze distributed training scenarios for a better understanding of their success and failure, beyond data parallelism.

- Explain in detailed procedures for establishing the analysis framework for independent subnetwork training

### Weaknesses
 - Theoretical understanding seems to be constrained by the assumptions, which might separate the current analysis from the real use cases

- Although the suggested analysis of the convergence and bias sounds interesting and useful, the limited experimental validation would limit the application of the proposed observation in real distributed training scenarios. In particular, the authors have emphasized the need for the theoretical understanding of a wide-spread parallelization and co-design of communication and training algorithms for large-scale training, but the limited validation would hinder the application of the findings from this work.

### Questions
Can we see a more realistic distributed training scenario (e.g., training ImageNet deep neural networks) to validate the key observations of this work?

### Soundness
3 good

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
This paper tries to provide a theoretical understanding of IST’s optimization performance using a quadratic model under no restrictive/specific assumptions on sparsifiers. Both homogeneous and heterogeneous scenarios are discussed, and the latter one is closer to practical scenarios. It provides insights into when IST can optimize very efficiently or not converge to the optimal
solution with tight characterization.

### Strengths
* This paper develops a more rigorous theoretical analysis of IST convergence, although with a simple quadratic model.
* The paper is overall well-written and easy to follow. The assumptions are stated explicitly, and the notations are mostly clear.
* Identify the settings IST may not converge, which hopefully can have implications for NN training.

### Weaknesses
 * **Restrictive (maybe impractical) assumption the work uses that assumes performing only one gradient descent step during local training in IST**. Performing only one gradient computation at each node requires very frequent communication with the server, which will incur high communication costs. Hence, performing multiple gradient descent steps in the local mode is more desired as in the IST work [1] and [2]. I admit taking multiple steps may hurt the accuracy, while the main motivation of IST is saving communication costs under the accuracy-efficiency trade-off. The single gradient step assumption severely limits the practical relevance of the analysis, as real-world distributed training often employs multiple local updates to amortize communication overhead. This assumption needs to be better justified or the theoretical results need to be extended to more realistic scenarios.
*  **Why is the gradient sparsification introduced in Eq.6 for IST?** The original IST work formulated the IST training method as Eq(69)  without the gradient sparsification operator. The authors state that “it can create a significant disparity between theory and practice” in Appendix D. I didn’t notice that IST uses any form of gradient sparsification, as IST is orthogonal to gradient sparsification techniques.  The motivation for introducing this operator in IST formulation is unclear. The introduction of a gradient sparsification operator, when IST is fundamentally about sparsifying model parameters, requires more justification. It is not clear why the gradient itself needs to be sparsified, especially since the original IST formulation focuses on sparse model updates, not sparse gradients. The authors need to clarify how this modification aligns with the core principles of IST and why it is necessary for their theoretical analysis.

### Questions
* Can the author further discuss why the assumption that performing only one gradient computation is reasonable, as it is not a common choice for efficient IST? It would be better if the author could show the theoretic analysis still holds with a more relaxed assumption, like performing twice or more.
* Can the authors provide a clear discussion on the reason for introducing the gradient sparsification operator compared to the original formula? Why is this operator necessary when analyzing the convergence of IST if those two techniques are orthogonal?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a theoretical convergence analysis of the independent subnetwork training (IST) method on a quadratic model.

### Strengths
1. As a theoretical paper, the paper is well-organized and easy to follow. Proofs and more details are attached in the appendices.
2. This paper presents a theoretical analysis for the recent IST method.

### Weaknesses
### Major issues
1. Section 2.2 lists 3 assumptions for the theoretical analysis. The authors also discuss the necessity of each assumption. Could the authors try to remove one of them? Specifically, is it possible to discuss other problems other than the specific quadratic one? The analysis relies on strong assumptions, such as exact submodel gradient computation and a quadratic objective function. While the authors justify these choices, the practical relevance of the results is limited by these assumptions. It is unclear how the convergence results would be affected by noisy gradient estimates or more complex, non-convex loss functions that are typical in deep learning. The choice of a quadratic model, while simplifying the analysis, severely restricts the applicability of the theoretical findings to real-world scenarios.
2. The paper focuses on the theoretical aspects of IST. It would be insightful to discuss the practical implications of the findings for real-world applications and provide guidance on effectively utilizing IST in various distributed training scenarios.

### Minor issues
1. At the bottom of Page 2, $\mathbf{R}^d \rightarrow \mathbf{R}$
2. Figures 1a and 1b have different vertical axis, relative error and absolute error. Could the authors provide both relative and absolute error for these two cases.

### Questions
What are the limitations and potential negative impacts of the paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
> **TL;DR:** The paper provides a theoretical analysis on the IST algorithm. The analysis is more flexible than previous IST theoretical analysis works. However, I find the experimental work lacking. Addressing my concerns and questions can improve the score.

The paper presents a comprehensive analysis of Independent Subnetwork Training (IST) in the context of distributed machine learning with a focus on data and model parallelism. The study identifies the lack of a rigorous understanding of IST convergence as a motivation for the research. The main contributions of this work include a novel approach to analyzing distributed methods that combine data and model parallelism, an analysis of IST in both homogeneous and heterogeneous scenarios without restrictive gradient estimator assumptions, and the identification of settings where IST can optimize efficiently or converge to a well-characterized irreducible neighborhood. The research is supported by carefully designed experiments and provides valuable insights into the advantages and limitations of IST in large-scale machine learning.

### Strengths
* **S.1.** The paper provides an in-depth analysis on the IST algorithm which tackles an important problem.
* **S.2.** The paper provides a theoretical analysis with higher flexibility.
* **S.3.** The theoretical analysis includes both the Homogeneous and the Heterogeneous settings.

### Weaknesses
 * **W.1.** The provided experimental results are not conclusive enough and placed in the end of the Appendix.
* **W.2.** The work is mainly focused on the quadratic model.

### Questions
* **Q.1.** Can this work be extended to neural networks such as [1]?

[1] Dun, Chen, Cameron R. Wolfe, Christopher M. Jermaine, and Anastasios Kyrillidis. "Resist: Layer-wise decomposition of resnets for distributed training." In Uncertainty in Artificial Intelligence, pp. 610-620. PMLR, 2022.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
