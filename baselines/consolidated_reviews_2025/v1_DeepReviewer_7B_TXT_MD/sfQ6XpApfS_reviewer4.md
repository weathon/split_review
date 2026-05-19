### Summary

The paper introduces Peer Review, a novel unsupervised evaluation framework for large language models (LLMs) that uses peer review mechanisms to measure LLMs' capabilities. The framework assigns a learnable capability weight to each LLM and optimizes the weight ranking based on the consistency assumption. The authors propose three metrics—PEN, CIN, and LIS—to evaluate the gap in aligning human preferences. The framework demonstrates effectiveness across multiple datasets and metrics, validating its approach to unsupervised LLM evaluation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper presents a novel unsupervised evaluation framework that utilizes peer review mechanisms to measure the capabilities of large language models (LLMs). The framework assigns a learnable capability weight to each LLM and optimizes the weight ranking based on the consistency assumption. The authors propose three metrics—PEN, CIN, and LIS—to evaluate the gap in aligning human preferences. The framework demonstrates effectiveness across multiple datasets and metrics, validating its approach to unsupervised LLM evaluation.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost associated with the proposed framework. Given the complexity of the peer review mechanism and the optimization process, it would be beneficial to understand the computational resources required and the scalability of the framework to larger datasets or a greater number of LLMs.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed framework. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for each step of the peer review process, including the initial response generation, the pairwise evaluation by LLMs, and the subsequent optimization of capability weights. This analysis should consider the impact of various factors, such as the number of LLMs being evaluated, the size of the input datasets, and the complexity of the evaluation tasks. Furthermore, it would be beneficial to compare the computational cost of the proposed framework with that of existing evaluation methods, highlighting the trade-offs between accuracy and efficiency. This would allow readers to better understand the practical applicability of the framework in different resource-constrained environments. The authors should also discuss potential strategies for optimizing the computational efficiency of the framework, such as parallelization or approximation techniques.

To further strengthen the paper, the authors should conduct a more rigorous evaluation of the framework's performance under different expertise scenarios. This could involve creating synthetic datasets with LLMs that have different levels of knowledge or specialization, and then assessing how well the framework can differentiate between them. For example, the authors could evaluate the framework's ability to rank LLMs that are experts in specific technical domains versus those that are more general-purpose. Additionally, the authors should explore the impact of different weighting strategies on the framework's performance, as the current approach may not be optimal for all scenarios. A more detailed analysis of the framework's sensitivity to the initial weights assigned to each LLM would also be valuable. This would provide a more comprehensive understanding of the framework's robustness and its ability to handle diverse LLM populations. The authors should also consider the impact of different evaluation criteria on the framework's performance, as the current approach may be biased towards certain types of responses.

Finally, the paper needs a more in-depth discussion of the potential biases that may be introduced by the peer review mechanism. The authors should explore how the inherent biases of the LLM evaluators might affect the evaluation process and the resulting rankings. This could involve analyzing the types of errors that the LLMs make and how these errors might propagate through the peer review process. The authors should also consider the impact of different evaluation metrics on the framework's performance, as the current approach may be biased towards certain types of responses. A more detailed analysis of the framework's sensitivity to the choice of evaluation metrics would also be valuable. Furthermore, the authors should discuss potential mitigation strategies for addressing these biases, such as incorporating human feedback or using more robust evaluation metrics. This would help to ensure that the framework provides a fair and unbiased assessment of the capabilities of LLMs.

### Questions

How does the framework handle cases where the LLMs being evaluated have significantly different levels of expertise or knowledge?

What are the potential biases that may be introduced by the peer review mechanism, and how can they be mitigated?

How does the framework perform in scenarios where the evaluation tasks are highly subjective or require creative generation?

### Rating

6

### Confidence

4

**********
