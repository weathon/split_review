# Combating the Generalization-Forgetting Trade-off in Continual Learning: A Cautious Passive Low-Rank Approach

- Decision: Reject
- Scores: 3, 5, 5, 3, 6

## Abstract
Large Language Models (LLMs) have shown remarkable capabilities through wide-scale pre-training on a wide range of domains. However, they often suffer from catastrophic forgetting when learning sequential tasks. In this paper, we propose a novel parameter-efficient approach for continual learning in LLMs, which empirically explores the role of different effective layerwise ranks, leveraging lower ranks to mitigate catastrophic forgetting of previous tasks and higher ranks to enhance generalization on new tasks. By employing a subspace similarity metric that evaluates the orthogonality of low-rank subspaces between tasks, we gradually increase the rank of layerwise matrices for each new task, minimizing interference with previously learned tasks while enhancing generalization. Experimental results on standard continual learning benchmarks and challenging math benchmarks demonstrate that our method outperforms existing state-of-the-art approaches, effectively mitigating forgetting, improving task performance, and maintaining strong generalization to unseen tasks in a memory-efficient manner.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work addresses the problem of continual learning for large language models (LLMs) and designs a mechanism to gradually increase the rank for the continual fine-tuning of LLMs.

### Strengths
The problem considered in this paper is meaningful in continual learning, and the parameter-efficient fine-tuning method employed is also a mainstream research approach currently.

### Weaknesses
1. Using only T5-large is insufficient to verify the effectiveness of the model on large language models (LLMs). Specifically, this paper claims to address the issue of continual fine-tuning in large models. However, the largest model used is only T5-large, which has only 770M parameters, far fewer than many existing LLMs such as Llama-2-7b, Llama-2-13b. The author should follow existing continual learning works [1, 2] that consider LLMs and perform experiments using Llama-2-7b and Llama-2-13b. Furthermore, the experimental results are primarily focused on classification tasks, while large language models are capable of handling a wide range of natural language understanding and generation tasks. The authors should broaden the experimental scope to include more diverse tasks, such as those found in the SuperNI benchmark, to provide a more comprehensive evaluation of the method's capabilities.

2. According to Equation 5, the motivation of this work is to keep $tr(B_{i}A_{i}(B_{j}A_{j})^{T})$ for ($j<i$) as small as possible when learning the i-th task. However, the algorithm ultimately aims to keep Equation 7 as small as possible. Equation 7 and $tr(B_{i}A_{i}(B_{j}A_{j})^{T})$ are not equivalent, leading to a mismatch between the motivation and the algorithm in this paper. The authors provide a high-level intuition about the connection, but a rigorous mathematical proof, such as a theorem demonstrating the relationship between Equation 7 and Equation 5, is necessary to validate the connection between the motivation and the actual implementation.

3. How is the second regularization term in Equation 8 derived? Because the lora branch $B_{i}A_{i}$ needs to be gradually updated during the learning of the $i$-th task, each calculation of the regularization term in Equation 8 requires SVD decomposition of $B_{i}A_{i}$, which will incur significant computational overhead. The authors mention that SVD is already performed when determining rank increases, but this does not fully address the computational cost of repeatedly calculating the regularization term during training. A more detailed explanation of how this regularization term is efficiently computed is needed, especially considering the computational demands of large language models.

### Questions
Since the motivation of this algorithm is to maintain the orthogonality of $tr(B_{i}A_{i})$ and the lora branches of old tasks when learning a new task $i$, it is unreasonable to use a Gaussian distribution for random initialization of $B_{i}$. In other words, why not adopt some operations to maintain the orthogonality of $B_{i}A_{i}$ and the lora branches of old tasks during the initialization of $A_{i}$ and $B_{i}$?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a continual learning method called CP-RANK, which achieves a balance between mitigating catastrophic forgetting and enhancing generalization by adjusting the rank across different layers. CP-RANK assigns each task a LoRA module as its adapter, using SVD decomposition to obtain the left singular matrix to assess the similarity between task subspaces. By comparing this similarity to a threshold, it determines whether the tasks are orthogonal. If they are orthogonal, the rank is increased; otherwise, the rank is maintained. Additionally, the paper introduces an improved approach for orthogonal projection. Comparative experiments are conducted to demonstrate the effectiveness of this method, and a necessary discussion on the experiments is provided.

### Strengths
- This paper proposes that low ranks are beneficial for resisting catastrophic forgetting, while high ranks are advantageous for learning new knowledge, with experiments conducted to support this perspective.
- The paper introduces a continual learning method called CP-RANK, which assigns different ranks to matrices at different layers and leverages rank increase to achieve a balance between mitigating catastrophic forgetting and enhancing generalization. Notably, the method incorporates an orthogonal projection algorithm, yielding promising results in experiments.
- It introduces the use of the left singular matrix to calculate the similarity between different subspaces to assess their orthogonality.
- The experimental section specifically evaluates performance on mathematical tasks.
- The paper provides detailed algorithms and formulas relevant to the proposed methods.

### Weaknesses
 - The experimental results indicate that CP-RANK without orthogonal decomposition performs worse than O-LoRA, and in testing its resistance to catastrophic forgetting, the original CP-RANK setup was not included. This may be insufficient to demonstrate the effectiveness of rank adjustments for continual learning, as it still primarily relies on the orthogonal projection method used by O-LoRA. The core claim of the paper is that dynamic rank adjustment is key, but the experiments do not isolate this effect, making it difficult to ascertain the true contribution of the rank adjustment mechanism independent of the orthogonal projection.
- In Algorithm 2, for situations where rank increase is needed, the newly added matrix elements are initialized randomly. I find the explanation for this part of the algorithm unclear: after increasing the rank, is additional training required? Should orthogonality be reassessed? The paper does not specify if the newly added parameters are immediately incorporated into the orthogonality calculations or if they are treated differently during the initial training steps after rank expansion. This lack of clarity makes it difficult to understand the precise mechanism of the rank adjustment.
- I believe that using "plasticity" (the capacity to learn new knowledge) in place of "generalization" might be more appropriate in this context, as the paper does not include experiments specifically validating generalization. The term 'generalization' typically refers to a model's ability to perform well on unseen data, which is not explicitly tested in the provided experimental setup. The experiments focus on learning new tasks sequentially, which is more aligned with the concept of plasticity, or the ability to adapt to new information.

### Questions
- The paper claims that a major advantage of this model is that it can operate without relying on task IDs. I would like to understand how the model achieves task recognition and adapter selection in this case.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents CP-Rank, a parameter-efficient continual learning method that progressively increases the layer-wise rank of LoRAs for new tasks, guided by a low-rank subspace similarity metric between tasks. CP-Rank not only models the low-rank relationships between tasks' incremental LoRAs but also adapts to the unique low-rank dynamics across different layers of the model. This approach effectively prevents forgetting of previous tasks while improving generalization on new tasks, all within a memory-efficient framework. Extensive experiments on natural language processing and complex math reasoning tasks demonstrate that CP-Rank effectively captures rank patterns in continual learning and consistently outperforms existing approaches.

### Strengths
* This paper is easy to follow.

* The proposed approach is simple and easy to understand.

### Weaknesses
 * The method would benefit from evaluation on a larger language model, as T5-large may not be sufficiently large for comprehensive assessment.

* The approach for increasing the LoRA rank appears heuristic and lacks sufficient justification. A deeper explanation and analysis of the rank-increasing strategy would strengthen the paper.

* The proposed method introduces several hyperparameters (e.g., $k$, $\epsilon$, and the rank-increasing mechanism), which could complicate its practical application. A simpler or more streamlined approach might improve usability.

* The relationship between low rank and forgetting, and high rank and generalization, is not well-justified. While the introduction offers empirical evidence of this correlation, a formal explanation or theoretical foundation is missing. Additionally, there is no clear discussion of whether the method generalizes to larger models, such as Llama.

* Other:
The font size in Figure 1 is too small, making it difficult to read. Increasing the size would improve clarity.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes CP-Rank (Cautious Passive Low-Rank), a continual learning strategy for LLM to balance the trade-off between low ranks and high ranks to balance forgetting mitigation and generalization based on LORA. It is observed that updating a high-rank weight on new task is likely to contribute to better performance on the new-task but greater forgetting previous tasks, and vice versa. CP-Rank progressively and adaptively increase the rank of derivative weight matrix the new task according to its similarity with previous tasks'.
Experiments show that it is effective.

### Strengths
The method is intuitive and basically reasonable. It is shown that the method could result in significant advantage in empirical performance.

### Weaknesses
1. The most concerning weakness is the efficiency of CP-Rank. In terms of space complexity, it requires storing the derivative weight matrix for every layer of every task, leading to a memory footprint of NLd^2, where N is the number of tasks, L is the number of layers, and d is the dimension of the weight matrix. This is highly inefficient, especially for large language models with numerous layers and high-dimensional weight matrices. Furthermore, the time complexity is also problematic. Learning a single new task involves T/k iterations of referring to all NL matrices in memory, performing SVD, and evaluating Grassmann similarity. This repeated SVD computation and similarity calculation across all previous tasks makes the method computationally expensive and impractical for real-world applications.
2. The initial experiment demonstrating the trade-off between low-rank and high-rank updates is not sufficiently convincing. The results are based on a single pair of tasks, which is inadequate to establish a statistically significant pattern. While it is intuitive that low-rank updates might favor unforgetting and high-rank updates might favor new task performance, this observation needs more rigorous empirical validation across a wider range of tasks and datasets to be considered a reliable finding.
3. Equation (5) does not align well with the method's design. There is a significant disconnect between the problem setting and the similarity metric used in Equation (5) and the actual method design. The equation does not accurately represent the low-rank subspace similarity that the method aims to capture, leading to a theoretical gap in the justification of the approach. The connection between the trace of the product of weight matrices and the Grassmann distance is not clearly established.
4. There are several redundant contents and minor errors that hinder readability. For instance, Equations (2), (3), and (4) seem unnecessary for the core method description. The variable $T$ in Equation (2) is likely intended to be $N$, representing the number of tasks. Additionally, Equation (7) is unlikely to have a codomain of (0,1), as the Grassmann distance typically ranges from 0 to the square root of the rank of the subspace.

### Questions
There is one main question that the reviewer is curious about and would appreciate to discuss with the authors: Is there a correlation between the rank of the derivative matrix of the new task and its mean similarity with previous tasks? It is demonstrated that seems similarity and rank are two independent factors. CP-Rank progressively increase the rank under a similarity threshold, which means the similarity corresponding to unforgetting, is prior to the rank corresponding to better fitting. This is reasonable from a practical perspective to just adding untrained rows and columns to AB while not disturbing the existing rows and columns. But it is likely that there is such a correlation which can be exploit. 

For example, a positive correlation can guide the early-stopping during increasing the rank to be more efficient.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript focused on continual learning (CL) with Large Language Models (LLM). The authors proposed a parameter-efficient approach based on the low-rank adaptation (LoRA) and explored the role of layerwise ranks in the incremental learning of LoRA between different tasks for CL. Through some empirical results, the authors observed that a trade-off between low ranks and high ranks can be leveraged to balance forgetting mitigation and generalization. Based on this motivation, the authors proposed Cautious Passive Low-Rank (CP-Rank) that gradually increases the rank of layerwise weight matrices during training. Specifically, the similarity of between-task low-rank subspaces is measured to evaluate the orthogonality between subspaces, and then whether to cautiously increase the ranks or passively maintain the current ranks can be determined for each task. Experiments on several benchmarks were conducted to support the effectiveness of the proposed method CP-Rank.

### Strengths
1. The motivation of this manuscript is clear. Determining how to increase the ranks is also novel for the continual learning for LLM with LoRA strategy.
2. Extensive experiments on different benchmarks were conducted to demonstrate the effectiveness. The datasets adopted in this manuscript include a wide range of task types.
3. This paper is well-written and easy to follow.

### Weaknesses
1. The mathematical presentation can be further improved. There are some confusing points that need to be clarified. The derivation of Eq. (5) is not rigorous, relying on a simplified linear regression case that does not adequately justify its application to complex neural networks. The connection between the theoretical analysis and the practical algorithm is weak, raising concerns about the validity of the theoretical claims.
2. The paper’s focus is primarily on state-of-the-art low-rank methods, but including a few recent non-low-rank continual learning methods as baselines could provide a broader performance perspective.
3. In Line 198, the sentence "Eq. 7 uses the singular values captured by two different task subspaces, which matches our findings in Eq. 5" is hard to follow. It would be better if the authors could provide intuitive explanations about the connection with Eq. 5.
4. In Eq. (2), I guess there is a typo for the subscript before the minus sign. Should it be $\mathbf{\theta}_N$ instead of $\mathbf{\theta}_T$? Besides, in Eq. (2) and Eq. (3), the parenthesis can be added for the different terms of RHS to avoid confusion.
5. In Eq. (7), I wonder if there are some typos about the indices (e.g., $i,s$). This equation is confusing.
6. In Algorithm 1, I noticed that an interval $k$ was set to control the operations within Step 4. However, I didn't see any description of this point. Could the authors explain the role of this interval $k$?
7. Some superscripts in Section 2 are a little messy. For example, in Line 177, the superscript is adopted to indicate the layer $l$. However, in Algorithm 1 and Algorithm 2, the matrices $\mathbf{A}$ and $\mathbf{B}$ were subscripted with a time step $t$. This confusing part needs to be further clarified.
8. I noticed that other studies, such as InfLoRA [1], also considered orthogonality between the subspaces of different tasks during the LoRA adaptation. Could the authors summarize the main differences between their proposed CP-Rank ad InfLoRA?

### Questions
1. In Line 198, the sentence "Eq. 7 uses the singular values captured by two different task subspaces, which matches our findings in Eq. 5" is hard to follow. It would be better if the authors could provide intuitive explanations about the connection with Eq. 5.
2. In Eq. (2), I guess there is a typo for the subscript before the minus sign. Should it be $\mathbf{\theta}_N$ instead of $\mathbf{\theta}_T$? Besides, in Eq. (2) and Eq. (3), the parenthesis can be added for the different terms of RHS to avoid confusion.
3. In Eq. (7), I wonder if there are some typos about the indices (e.g., $i,s$). This equation is confusing.
4. In Algorithm 1, I noticed that an interval $k$ was set to control the operations within Step 4. However, I didn't see any description of this point. Could the authors explain the role of this interval $k$?
5. Some superscripts in Section 2 are a little messy. For example, in Line 177, the superscript is adopted to indicate the layer $l$. However, in Algorithm 1 and Algorithm 2, the matrices $\mathbf{A}$ and $\mathbf{B}$ were subscripted with a time step $t$. This confusing part needs to be further clarified.
6. I noticed that other studies, such as InfLoRA [1], also considered orthogonality between the subspaces of different tasks during the LoRA adaptation. Could the authors summarize the main differences between their proposed CP-Rank ad InfLoRA?

References;

[1] InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning. CVPR 2024.

### Soundness
3

### Presentation
3

### Contribution
3
