# dEBORA: Efficient Bilevel Optimization-based low-Rank Adaptation

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Low-rank adaptation methods are a popular approach for parameter-efficient fine-tuning of large-scale neural networks. However, selecting the optimal rank for each layer remains a challenging problem that significantly affects both performance and efficiency. In this paper, we introduce a novel bilevel optimization strategy that simultaneously trains both matrix and tensor low-rank adapters, dynamically selecting the optimal rank for each layer. Our method avoids the use of implicit differentiation in the computation of the hypergradient, and integrates a stochastic away-step variant of the Frank-Wolfe algorithm, eliminating the need for projection and providing identifiability guarantees of the optimal rank structure. This results in a highly efficient and cost-effective training scheme that adaptively allocates the parameter budget across the network layers. On top of a detailed theoretical analysis of the method, we provide different numerical experiments showcasing its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces dEBORA, a bilevel optimization-based method that dynamically selects the optimal rank for each layer in parameter-efficient fine-tuning of large neural networks. By employing a hypergradient approximation that avoids large-scale computation, dEBORA significantly reduces the computational burden. Additionally, it integrates a stochastic away-step variant of the Frank-Wolfe algorithm, which eliminates the need for projection and ensures the identifiability of the optimal rank structure. Theoretical analysis confirms the convergence and optimality of the approach, while experimental results demonstrate that dEBORA outperforms existing low-rank adaptation methods in both efficiency and performance across various benchmarks.

### Strengths
- The paper presents a novel approach to low-rank adaptation by combining bilevel optimization with a dynamic rank-selection strategy, effectively addressing the challenge of parameter-efficient fine-tuning in large neural networks. Furthermore, the avoidance of implicit differentiation through an effective hypergradient approximation is a significant strength, as it reduces both computational costs and complexity.
- The experimental results are robust and cover a wide range of benchmarks.

### Weaknesses
 - Despite providing several theoretical guarantees, the paper lacks clarity in the use of some symbols and definitions of variables, making it difficult for readers to follow the authors' proofs. For instance, the notation $\otimes$ first appears in line 141, while $\odot$ is introduced for the first time in line 215 without prior definition. Similarly, $\Delta$ is introduced in Equation (8) but is only defined in Theorem 6.2, and the variable $V$ is not defined in Equation (21). Additionally, the definition of $\mu$ is missing in Theorem 6.5. The authors are encouraged to carefully review the paper and provide clear definitions or explanations for variables and symbols, either upon their first appearance or in a comprehensive notation table.
- Although the overall structure of the paper is reasonable, the authors should consider removing the numbering from equations that are not referenced, as excess numbering creates a cluttered appearance. Furthermore, Equations (30) and (31) are noticeably smaller than the other equations, leading to inconsistencies in formatting. Additionally, the various variables within these equations lack definitions, making it challenging and time-consuming for readers. A careful review of whether each equation requires numbering, along with a focus on maintaining uniform formatting, would enhance the readability of the paper.
- While the authors mention the recent work BiLoRA (Qiang et al., 2024) [1], no corresponding comparison is presented in the experiments. It would be valuable to understand the rationale behind this omission. Furthermore, while the authors state that they compare against the Pfeiffer adapter (Pfeiffer et al., 2021) [2] and Houlsby adapter (Houlsby et al., 2019) [3], the results do not clearly reflect these comparisons. Clarifying this point and providing results for these benchmarks would strengthen the experimental section.

### Questions
1. The paper introduces a strategy for dynamically selecting the optimal rank $r$ for each layer. However, it is unclear how rank $r$ is adjusted after determining the optimal solution $s$. Is $r$ recalibrated based on the optimal $s$, or is there a specific strategy for automatically tuning $r$? Could the authors clarify this process in detail?

2. In Theorem 4.1, the authors state, "assume that the gradient is locally approximately constant." However, the subsequent equations appear to be formulated in terms of the Hessian. Could the authors clarify the relationship between these two concepts?

3. Regarding equation (3), if the matrix $\mathcal{B}$ is constrained to lie on a manifold—as mentioned later in the experiments with the Oblique and Stiefel manifolds—would the first-order optimality condition still hold as stated? This consideration could significantly impact the approximations and key results presented in the paper. Could the authors clarify how the manifold constraints influence the formulation of the first-order optimality condition?

4. In equation (35), is it necessary for the authors to clarify the invertibility of the product $AB$? Providing a discussion on this aspect would enhance the understanding of the conditions under which the equation holds.

5. In line 755, the notation $||\partial_{\mathcal{B}}f_{2}^{\*}||$ should be revised to $||\partial_{\mathcal{B}}f_{1}^{\*}||$. Additionally, could the authors clarify where the boundedness of this term originates?

   

The article contains several typographical and punctuation errors that require careful review by the authors. For example:

- Punctuation errors: in lines 208, 240, 319, 401, and 407, there are missing commas. In line 686, there is an extra period.
- Line 679: "By" should be "by".

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the problem of optimal rank selection in low-rank adaptation methods, which is essential for efficient fine-tuning of large-scale neural networks. The authors propose a bilevel optimization strategy that trains matrix and tensor low-rank adapters while dynamically selecting the best rank per layer. Their approach avoids implicit differentiation, uses a stochastic variant of the Frank-Wolfe algorithm, and provides identifiability guarantees for the optimal rank structure. Theoretical analysis and numerical experiments support the method's efficiency and effectiveness, showcasing adaptive parameter allocation across network layers.

### Strengths
1.	This paper addresses a longstanding issue in LoRA: selecting the optimal rank for each low-rank adapter, a key factor in balancing model performance and computational efficiency. Whereas traditional PEFT algorithms require manual tuning of this parameter, the authors propose a criterion based on optimization.
2.	To address this issue, it introduces a bilinear optimization approach that alternates between optimizing the LoRA matrices and their ranks, presenting a novel contribution to the PEFT community.
3.	With fewer parameters, the proposed method demonstrates competitive or superior performance compared to existing approaches such as LoRA and AdaLoRA.

### Weaknesses
[key issue] While selecting the optimal rank is indeed critical for LoRA, in many practical applications, concerns about memory consumption and training time are often more pressing. The proposed bilinear optimization approach suggests a reduction in parameter count, but the practical impact on memory usage remains uncertain. A detailed comparison of peak memory consumption during training, particularly in scenarios involving large language models, would significantly strengthen the paper’s contribution. The current analysis does not adequately address the memory overhead associated with storing intermediate gradients and the sensitivity measure, which could be substantial.

[key issue] The proposed method has been evaluated on architectures such as DeBERTa and ResNet. However, the reviewer is interested in its applicability to even larger models. Specifically, would this bilevel optimization approach introduce significant additional computation time? The analysis of the Frank-Wolfe direction search is not sufficiently detailed. While the authors claim a low cost for finding the smallest entry in the hypergradient vector, the overall time complexity of the iterative rank selection process, especially when considering the hypergradient computation, needs further clarification. It would be beneficial if the authors could provide both theoretical analysis and empirical results addressing this question. For instance, a detailed breakdown of the computational cost of each step in the algorithm, including the hypergradient calculation and the Frank-Wolfe direction search, would be valuable. Furthermore, the practical implications of using a Frank-Wolfe optimization strategy on large-scale models such as LLaMA2, in terms of wall-clock time, remain unclear.

In Theorem 4.1, the condition K≥0 alone appears insufficient to ensure that the gradient is locally constant. Additionally, the assumptions regarding the uniform invertibility and boundedness of the bilinear operator merit further examination for practical feasibility. The practical implications of these assumptions, especially in the context of deep neural networks, are not fully discussed.
The parameter τ is tied to the rank selection process, yet its practical setting and impact on memory usage are not fully clarified. Could the authors discuss guidelines for selecting τ in practice and elaborate on its relationship with memory requirements?

In line 154, should the parameter s be restricted to nonnegative values? Further clarification on this point would be helpful.

### Questions
See the above "weakness".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces a compact bilevel optimization framework for low-rank adaptation, offering an efficient fine-tuning strategy for large-scale neural networks via dynamic rank selection. Theoretical analysis provides convergence guarantees, and numerical experiments demonstrate that proposed method achieves performance comparable to advanced approaches.

### Strengths
- A relatively fresh application of the Frank-Wolf method.

### Weaknesses
 - Line 150-151, maybe it's better to use a figure to visualize the bypass in the neural networks.
- Line 159, what's the intuition of splitting dataset to two parts?
- Line 249, I understand you are focusing on the (stochastic) Frank-Wolf with mini batch of data, have you considered the full batch size?
- Line 472, "randomly partitioned the dataset into equally sized subsets", did you ensure the label balance for both dataset?

### Questions
- Line 150-151, maybe it's better to use a figure to visualize the bypass in the neural networks.\
- Line 159, what's the intuition of splitting dataset to two parts?\
- Line 249, I understand you are focusing on the (stochastic) Frank-Wolf with mini batch of data, have you considered the full batch size?\
- Line 472, "randomly partitioned the dataset into equally sized subsets", did you ensure the label balance for both dataset?

### Soundness
3

### Presentation
3

### Contribution
3
