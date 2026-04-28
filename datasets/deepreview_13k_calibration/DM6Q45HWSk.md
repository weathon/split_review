# One Initialization to Rule them All: Fine-tuning via Explained Variance Adaptation

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Foundation models (FMs) are pre-trained on
large-scale datasets and then
fine-tuned on a downstream task for a specific application.
The most successful and most commonly used
fine-tuning method is to update the pre-trained weights
via a low-rank adaptation (LoRA).
LoRA introduces new weight matrices that are usually initialized at random with a uniform rank distribution across the model weights.
Recent works focus on different initialization schemes or the learning of adaptive ranks during fine-tuning.
Both approaches have only been investigated in isolation, resulting in slow convergence or a uniform rank distribution, in turn leading to suboptimal performance.
We propose to improve LoRA by initializing
the new weights in a \emph{data-driven} manner by computing 
singular value decomposition (SVD) on minibatches of activation vectors.
Then, we initialize the LoRA matrices with the obtained right-singular vectors and redistribute ranks among all weight matrices to provably store the maximum amount of information of the downstream data in the newly introduced weights.
In this way, only what information to maintain or neglect during the fine-tuning process needs to be learned.
We call our new method \textbf{E}xplained \textbf{V}ariance \textbf{A}daptation (EVA).
We apply EVA to a variety of fine-tuning tasks ranging from
language generation and understanding to image classification and reinforcement learning.
EVA exhibits faster convergence than competitors and achieves the highest average score across a multitude of tasks per domain while reducing the number of trainable parameters via rank redistribution.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an enhancement to LoRA by initializing new weights through a data-driven approach. It computes singular value decomposition on mini-batches of activation vectors, using the resulting right-singular vectors to initialize the LoRA matrices. Additionally, ranks are re-distributed among weight matrices to maximize explained variance across layers, followed by standard LoRA fine-tuning. This new method, called Explained Variance Adaptation (EVA), is tested across various fine-tuning tasks, including language generation, understanding, image classification, and reinforcement learning. EVA demonstrates faster convergence and achieves the highest average performance across a range of tasks in each domain.

### Strengths
1.	The proposed idea is quite straightforward, which I consider a strength rather than a limitation.

### Weaknesses
1.	It's unclear why performing SVD on activation vectors for the initial mini-batches is beneficial for initializing the LoRA matrix. Specifically, the connection between the principal components of the activation space and the optimal initialization for the low-rank adaptation matrices is not well-established. The paper does not provide a theoretical justification or a clear intuition as to why this approach should lead to faster convergence or better performance compared to random initialization.
2.	The visualizations in the paper could be improved for professionalism, for instance, the text in Figure 1 is too large, while in the left part of Figure 2, it is too small. The figures lack clarity and visual appeal, making it difficult to quickly grasp the proposed method and its results. The inconsistent text sizes and overall aesthetic detract from the paper's presentation.
3.	The improvement achieved by the proposed method is minimal in most of the tables, which raises doubts about its true effectiveness. The reported gains are often marginal, and it is not clear if these small improvements are statistically significant or practically meaningful. Given the limited number of parameters in LoRA, it is questionable whether the initialization strategy would have a substantial impact on the final performance.

### Questions
1. Why is performing SVD on activation vectors for the initial mini-batches beneficial for initializing the LoRA matrix? This could be explained further, either from a theoretical or experimental perspective.

2. In most experiments, the improvement achieved by the proposed method is minimal. How can it be demonstrated that the proposed initialization is indeed effective? From my perspective, given the limited parameters in the LoRA adapter, the influence of different initializations on the final performance should be relatively small.

3. Computing the SVD introduces additional computational overhead, which diminishes the efficiency advantage of vanilla LoRA.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel initialization method called EVA for Low-Rank Adaptation (LoRA), which combines a weight-driven SVD with rank redistribution. The authors initialize matrix A by applying SVD to the input data X and then utilize a pruning method to implement rank redistribution. They further demonstrate the effectiveness of the EVA method through experiments on a variety of downstream tasks.

### Strengths
1.	This paper is well-written.
2.	The authors evaluate the method from multiple aspects, including language understanding, language generation, and image classification.

### Weaknesses
1.	Although the authors validate the effectiveness of EVA in various aspects, they do not provide insights into the reasoning behind their method. Specifically, they explain the process of initializing via SVD decomposition of activation values but fail to elaborate on the underlying principles. I would like the authors to clarify the rationale behind the EVA method. The connection between the SVD of activation matrices and effective weight initialization remains unclear. It is not obvious why the principal components of the activation space should provide a good initialization for the low-rank matrices, and the paper lacks a theoretical justification for this choice.
2.	Using rank redistribution within the same budget may lead to unfair comparisons; the effects of increasing the rank in small matrices versus large matrices differ significantly. For instance, adjusting (16, 512) to (17, 512) versus (16, 4096) to (17, 4096) increases the rank by one, but the latter clearly introduces more parameters. Additionally, the authors perform hyperparameter searches for $\rho$ at {1, 2}, and results with $\rho=1$ (uniform rank) sometimes yield better outcomes, suggesting that rank redistribution may not be as effective. The paper does not provide a clear analysis of when and why rank redistribution is beneficial, and the experimental results do not consistently support its use.
3.	There is a lack of comparisons with related works, such as rsLoRA[1], LoRA+[2], and LoRA-GA[3] (also a data-driven initialization). The absence of these comparisons makes it difficult to assess the novelty and practical advantages of the proposed method. A thorough comparison with existing data-driven initialization techniques is necessary to properly contextualize the contribution of this work.
4.	The experimental setting of $\alpha=1$ seems unusual; for a rank of 16, a more common setting would be $\alpha=32$. A specific comparison of their results would be beneficial. The choice of $\alpha=1$ is not well-motivated, and the paper should provide a comparison with more standard settings to demonstrate the robustness of the proposed method.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the parameter-efficient fine-tuning of foundation models (FMs). Based on the commonly used low-rank adaptation (LoRA), the authors propose a new method called Explained Variance Adaptation (EVA) to fine-tuning FMs faster and better. Specifically, they emphasize the data-driven initialization and the adaptive ranks within EVA. The former is implemented via computing singular value decomposition on minibatches of activation vectors. The latter is based on explained variance. Extensive empirical results across various fine-tuning tasks have shown the effectiveness of their approaches.

### Strengths
1.The experiments in this paper are comprehensive, spanning multiple fields and validating the generalizability of the method sufficiently.

2.The method in this paper seems to be straightforward and easy to reproduce.

3.The data-driven manner proposed in this paper appears to be promising.

### Weaknesses
1.The clarity of the figures and formulas need further improvement. Figure 1 seems rough, failing to clearly illustrate the method presented in this paper. The authors can illustrate the following details in Figure 1: constructing matrix A from right singular vectors obtained through SVD decomposition; the incremental update process; and the procedure of adaptive rank allocation. Additionally, the mathematical formulation of "incrementally update" in sec 3.2 is necessary.

2.The "faster convergence" claimed by the authors in the Abstract and Figure 2 seems not sufficiently significant. Adding experiments with other models and tasks could enhance the persuasiveness, not only Llama-3.1-8B on the MetaMathQA dataset. Similar to validating the method's effectiveness on language generation, language understanding, image classification, and decision making, the author can evaluate the "faster convergence" by selecting one dataset from these tasks. Additionally, regarding the relationship between gradient norm and convergence speed, more references should be included. Furthermore, the presented loss curves do not show a substantial difference in convergence speed, and the random fluctuations in loss appear to be of a similar magnitude as the claimed faster convergence. The gradient norm plot in Figure 2 also presents a contradictory example, where PiSSA exhibits a larger gradient norm but does not show faster convergence compared to Random.

3.This paper provides extensive experiments but lacks sufficient theoretical analysis or intuitive explanations. What makes this work is more interesting to the community. A thorough analytical discussion and interpretation of the initialization technique presented in Section 3.2 is needed, along with relevant supporting references when appropriate. This will be further discussed in “Questions”.

### Questions
1.The proposed method is named “Explained Variance Adaptation” that also be included in the title. However, what is the relationship between "Data-driven Initialization" in sec 3.2 and “Explained Variance”? The key point of the proposed method seems to be about mining and utilizing downstream data information. “Explained Variance” appears to be just one part of it.
Furthermore, the authors should provide more detailed explanations for the operations in sec 3.2 - How does using right singular vectors for initialization affect fine-tuning? Why does it lead to better performance?

2.The author points out the performance of different variants of EVA on various types of data (natural, specialized, and structured) in Table 7. However, there is a lack of in-depth analysis. For example, what makes the differences in EVA's performance across natural, specialized, and structured data? Could an appropriate explanation for this result be provided based on the analysis about sec 3.2?

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
The paper proposes a novel method, Explained Variance Adaptation (EVA), to improve the fine-tuning process of foundation models. EVA builds upon LoRA (Low-Rank Adaptation) by introducing a data-driven initialization strategy that leverages the singular value decomposition (SVD) of activation vectors during training. This method aims to optimize the initialization of LoRA weights based on the explained variance of activation patterns in the downstream task data. EVA also incorporates adaptive rank allocation, allowing ranks to be distributed across layers in a way that maximizes the variance explained by the model. The paper demonstrates that EVA consistently outperforms existing methods across various tasks, including language generation, image classification, and reinforcement learning, by improving convergence speed and overall performance.

### Strengths
1. The proposed pipeline is easy to understand.
2. Comprehensive experiments are done, including language generation and understanding, image classification, and reinforcement learning.
3. Additional computational burden is clearly stated in the paper.

### Weaknesses
1. The paper's novelty is limited, as it applies SVD for LoRA initialization and rank distribution—approaches already explored in previous works. Specifically, SVD has been used for initialization in PiSSA [1] and for rank distribution in AdaLoRA [2]. The only incremental contribution appears to be applying SVD to activations, a technique previously examined in the pruning [3] and quantization [4] literature. However, the core idea of leveraging activation patterns for parameter initialization, while not directly using SVD, has been explored in prior work, which diminishes the novelty of this approach.

2. I question the motivation for initializing matrix A with right-singular vectors, despite the authors' claim that they capture the directions of variance. More analytical evidence is needed to substantiate this conjecture (i.e., why the direction of variance results in better fine-tuning performance?). The paper lacks a clear theoretical justification for why initializing with the right singular vectors, which correspond to the directions of maximal variance in the activation space, should lead to better optimization or faster convergence. It is not obvious that aligning the initialization with the principal components of the activation data will necessarily translate to improved performance on the downstream task. The connection between maximizing variance in the activation space and optimizing for a specific downstream task is not well established.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
