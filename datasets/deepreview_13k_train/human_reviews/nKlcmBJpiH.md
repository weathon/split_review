# Optimistic Gradient Learning with Hessian Corrections for High-Dimensional Black-Box Optimization

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Black-box algorithms are designed to optimize functions without relying on their underlying analytical structure or gradient information, making them essential when gradients are inaccessible or difficult to compute. Traditional methods for solving black-box optimization (BBO) problems predominantly rely on non-parametric models and struggle to scale to large input spaces. Conversely, parametric methods that model the function with neural estimators and obtain gradient signals via backpropagation may suffer from significant gradient errors. A recent alternative, Explicit Gradient Learning (EGL), which directly learns the gradient using a first-order Taylor approximation, has demonstrated superior performance over both parametric and non-parametric methods. In this work, we propose two novel gradient learning variants to address the robustness challenges posed by high-dimensional, complex, and highly non-linear problems. Optimistic Gradient Learning (OGL) introduces a bias toward lower regions in the function landscape, while Higher-order Gradient Learning (HGL) incorporates second-order Taylor corrections to improve gradient accuracy. We combine these approaches into the unified OHGL algorithm, achieving state-of-the-art (SOTA) performance on the synthetic COCO suite. Additionally, we demonstrate OHGL’s applicability to high-dimensional real-world machine learning (ML) tasks such as adversarial training and code generation. Our results highlight OHGL's ability to generate stronger candidates, offering a valuable tool for ML researchers and practitioners tackling high-dimensional, non-linear optimization challenges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an enhanced method for black-box optimization (BBO) by specifically addressing challenges in high-dimensional and complex optimization landscapes. The proposed approach, termed Optimistic Higher-Order Gradient Learning (OHGL), builds on previous methods like Explicit Gradient Learning (EGL) by incorporating both optimistic gradient estimation and Hessian corrections. By leveraging second-order Taylor expansions and Hessian information, the method improves gradient accuracy. The authors propose a sampling profiler to reduce required samples and refine trust region adjustments for enhanced convergence efficiency. It demonstrates strong potential in machine learning tasks where gradient information is inaccessible or costly to compute.

### Strengths
The paper appears to be well-grounded in both theoretical and experimental methodologies. The use of both first- and second-order gradient information for better accuracy in high-dimensional spaces is a technically sound choice, demonstrating an understanding of gradient approximation complexities in BBO.

The breakdown of components like Optimistic Gradient Learning and Higher-Order Gradient Learning helps clarify how each extension builds on EGL, and the inclusion of figures and empirical results assists in understanding performance benefits. However, a possible point for improvement might be adding more intuitive explanations or visual aids for readers less familiar with gradient learning concepts.

### Weaknesses
1. Computational Complexity and Efficiency:
The inclusion of Hessian corrections, while beneficial for accuracy, introduces substantial computational cost, particularly in high-dimensional spaces. The paper does not provide a detailed analysis of the computational scaling with respect to the dimensionality of the problem, which is crucial for assessing its practical applicability. Specifically, the cost of computing and inverting the Hessian matrix, even with approximations, can become prohibitive as the number of parameters increases. This aspect requires further investigation and discussion.

2. Generalization of Results:
The results focus heavily on the COCO test suite and two specific applications. However, broader generalizability to other complex, black-box settings, such as reinforcement learning or sequential decision-making tasks, remains unaddressed. The paper lacks a discussion on the limitations of the proposed method in scenarios where the objective function might have different properties than those observed in the tested benchmarks. For example, the performance of the method in non-convex and noisy environments needs to be explored.

3. Trust Region's Limitations:
The algorithm's handling of boundary conditions may slow down convergence in real-world, high-dimensional applications due to excessive shrinking, which could be inefficient in practice. The paper does not provide a clear explanation of how the trust region is adapted in response to different types of objective function landscapes, nor does it discuss the potential for premature convergence due to overly conservative trust region updates.

### Questions
1. The inclusion of comparisons to more recent methods like Bayesian optimization frameworks or evolutionary algorithms would strengthen the claims regarding OHGL’s effectiveness.

2. The organization could be refined for flow, as several sections (like trust region management and adaptive sampling) feel slightly disjointed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes Optimistic Higher-Order Gradient Learning (OHGL), using second-order Taylor approximation, for solving black-box optimization (BBO) problems. Furthermore, the authors refine EGL's sampling strategy and loss function to improve its efficiency in high-dimensional settings. The proposed OHGL method is validated through experiments on the synthetic COCO suite and applied to two real-world machine learning tasks: adversarial training and code generation. The experimental results indicate that OHGL generates stronger candidate solutions, positioning it as a valuable tool for machine learning researchers and practitioners addressing high-dimensional, non-linear optimization challenges.

### Strengths
1. The concept of enhancing Explicit Gradient Learning (EGL) with second-order corrections is both interesting and novel, to the best of my knowledge.
2. The paper is generally well-written and presents its ideas in a clear and accessible manner.

### Weaknesses
1. My primary concern relates to the computational cost associated with Hessian computation or approximation, which may hinder the scalability of the proposed method. Given that memory- and computation-efficient Hessian approximation techniques are well-established in the literature, I strongly recommend that the authors evaluate their proposed method using more efficient approximations at larger scales.

2. The enhancements over EGL are attained through the integration of several design elements; however, a thorough ablation study is notably absent from the paper.

### Questions
See weaknesses.

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
3

### Summary
This work proposes an OHGL framework to solve black-box optimization. It improves the previous EGL framework by incorporating second-order Taylor corrections via the function’s Hessian and assigning higher weights to samples with lower objective values. Experiments on adversarial attack and code generation show its potential in high-dimension real-world problems.

### Strengths
1. The proposed Hessian corrections and weighed gradient are well-motivated, effectively addressing the limitations of the previous EGL framework.
2. Real-world high-dimension examples, including adversarial attacks and code generation, demonstrate the scalability and efficiency of this framework.

### Weaknesses
1. Compared to previous work, such as EGL or model-based methods [1], the theoretical understanding of the proposed Hessian corrections and weighted gradients is lacking. A more rigorous theoretical analysis would help justify the design choices, specifically regarding the convergence properties of the weighted gradient learning and the conditions under which the Hessian approximation is beneficial. It is unclear how the approximation error in the Hessian affects the overall optimization process, and whether the proposed method is guaranteed to converge to a local minimum, or if it might oscillate or diverge under certain conditions.

2. The work introduces several algorithm-level designs in Sec. 5, such as adaptive sampling size and trust-region management. The tolerance analysis in Section 6.2 suggests that the influence of these designs can accumulate over time, potentially leading to significant changes in performance. However, the paper does not provide clear guidance on how to tune these parameters for different black-box optimization tasks with a limited budget. The interaction between these parameters is not well-defined, making it difficult to understand which parameter is most critical for different types of optimization problems, and how to set them appropriately without extensive experimentation.

### Questions
1. The OHGL framework incorporates Hessian information during the training stage. However, it is unclear why the second-order information is not utilized when updating the next point (line 278).
2. Is the hyperparameter tuning process conducted for all baselines? 
3. Which design in the OHGL framework contributes the most to the observed performance improvements?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper extends the gradient descent learning method by incorporating second-order Taylor corrections through the function's Hessian, enhancing robustness in complex, highly non-linear problems. The OGL, HGL, and OHGL algorithms are presented and validated on the synthetic COCO suite, as well as in two scenarios: adversarial attacks and code generation.

### Strengths
1. The idea of Optimistic Gradient Learning and Higher-Order Gradient Learning is novel.
2. These new algorithms have achieved better results in experiments.

### Weaknesses
1. The reference format is not uniform. I suggest the authors improve them.
2. There are some mistakes in this paper, for example, the CE loss in the title of Table 3 is not reflected in the table. Specifically, the table presents results for a different loss function than indicated in the title, which is a significant discrepancy.
3. It seems that the most recommended algorithm in this paper, OHGL, has not been applied in real-world scenarios. The experiments are limited to synthetic data and a few specific applications, but lack a broader evaluation on more diverse and complex real-world datasets.

### Questions
1. I think the experiments of HGL and OHGL in adversarial attacks and code generations can further enhance persuasiveness.
2. Format modification is necessary, reference and appendix are confusing.

### Soundness
3

### Presentation
3

### Contribution
3
