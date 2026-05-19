### Summary

This paper proposes LICO, a novel approach that leverages large language models (LLMs) for black-box optimization (BBO) in molecular optimization. LICO extends LLMs by adding embedding and prediction layers for molecules and their scores, enabling it to perform in-context learning on molecular optimization tasks. The model is trained on a semi-synthetic dataset that combines intrinsic molecular properties and synthetic functions, allowing it to generalize to unseen molecular properties. The authors demonstrate that LICO achieves state-of-the-art performance on the Practical Molecular Optimization (PMO) benchmark, outperforming existing methods in terms of sample efficiency and accuracy.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the methodology and results.
2. The authors provide a thorough evaluation of LICO on the PMO benchmark, comparing it against several state-of-the-art methods. The results show that LICO achieves superior performance in terms of sample efficiency and accuracy.
3. The authors conduct ablation studies to analyze the impact of different components and design choices in LICO, providing insights into the model's behavior and performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost and scalability of LICO, which is an important factor for practical applications. Specifically, the paper lacks a breakdown of the time and memory requirements for both training and inference, especially as the size of the molecular dataset and the length of the molecular sequences increase. This makes it difficult to assess the feasibility of deploying LICO in resource-constrained environments.
2. The paper does not explore the robustness of LICO to noisy or incomplete data, which is common in real-world molecular optimization tasks. The evaluation is limited to the PMO benchmark, which may not fully represent the challenges encountered in practical applications. For example, the paper does not investigate how LICO performs when the molecular data contains errors or missing values, which are frequently encountered in experimental settings.
3. The paper does not provide a comprehensive comparison with other LLM-based methods for molecular optimization, which makes it difficult to assess the relative advantages and disadvantages of LICO. While the paper compares LICO against several state-of-the-art methods, it does not include a detailed comparison with other LLM-based approaches, such as those that use LLMs for property prediction or molecular generation. This makes it difficult to understand the specific contributions of LICO in the context of other LLM-based methods.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and memory requirements for both training and inference of LICO. This should include a discussion of how the computational cost scales with the size of the molecular dataset and the length of the molecular sequences. It would be beneficial to include a comparison of the computational cost of LICO with other state-of-the-art methods for molecular optimization. Furthermore, the authors should investigate the impact of different hardware configurations on the performance of LICO, such as the number of GPUs and the amount of memory available. This would provide a more comprehensive understanding of the practical feasibility of deploying LICO in different environments. The authors should also consider providing guidelines for selecting appropriate hardware configurations based on the size and complexity of the molecular optimization task.

To improve the robustness analysis, the authors should evaluate LICO on datasets that contain noisy or incomplete molecular data. This could involve introducing errors or missing values into the molecular data and assessing how these errors affect the performance of LICO. The authors should also investigate the impact of different types of noise and missing data patterns on the performance of LICO. For example, they could explore the effect of random errors in the molecular data, as well as more realistic errors that are common in experimental settings. This would provide a more realistic assessment of the performance of LICO in practical applications. The authors should also consider using techniques such as data augmentation or imputation to improve the robustness of LICO to noisy or incomplete data.

To provide a more comprehensive comparison with other LLM-based methods, the authors should include a detailed comparison with other LLM-based approaches for molecular optimization. This should include a discussion of the specific advantages and disadvantages of LICO compared to other methods, such as those that use LLMs for property prediction or molecular generation. The authors should also investigate the performance of LICO on different types of molecular optimization tasks, such as molecular property optimization and molecular generation. This would provide a more comprehensive understanding of the strengths and weaknesses of LICO in the context of other LLM-based methods. Furthermore, the authors should consider including a comparison with other state-of-the-art methods for molecular optimization, such as those based on reinforcement learning or evolutionary algorithms, to provide a more complete picture of the performance of LICO.

### Questions

1. How does the performance of LICO scale with the size of the molecular dataset and the length of the molecular sequences?
2. How robust is LICO to noisy or incomplete molecular data, and what techniques can be used to improve its robustness?
3. How does LICO compare to other LLM-based methods for molecular optimization, and what are the specific advantages and disadvantages of each approach?

### Rating

6

### Confidence

4

**********
