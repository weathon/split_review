### Summary

This paper introduces MultiIoT, a large-scale IoT benchmark designed to advance machine learning for IoT applications. It includes over 1.15 million samples from 12 modalities and 8 tasks, addressing challenges like learning from multiple sensory modalities, fine-grained interactions, and extreme heterogeneity. The authors provide empirical comparisons of modeling paradigms on this benchmark, highlighting the importance of multimodal and multitask learning for IoT data.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive review of related work and present a large-scale benchmark that could be useful for the community.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks novelty in its contributions. The benchmark is large-scale, but it primarily aggregates existing datasets from various modalities. While the paper does not claim to be a benchmark paper, it would be beneficial to provide a more in-depth analysis of the dataset. For instance, it would be helpful to understand the distribution of each modality and how they relate to each other. Additionally, the paper does not provide a clear explanation of how the tasks are defined and why they are relevant to IoT applications.
2. The paper does not provide a clear motivation for the proposed benchmark. While the authors mention the challenges of learning from multiple sensory modalities, fine-grained multisensory interactions across long temporal ranges, and extreme heterogeneity in real-world sensors, they do not provide concrete examples of how these challenges manifest in real-world IoT applications. It would be helpful to provide specific use cases or scenarios where these challenges are particularly relevant.
3. The paper does not provide a clear explanation of the modeling paradigms used in the experiments. While the authors mention that they evaluate a range of modeling approaches, they do not provide details on the specific models used, their architectures, and their training procedures. This makes it difficult to reproduce the results and to understand the strengths and weaknesses of each modeling approach.

### Suggestions

The authors should provide a more detailed analysis of the dataset, including the distribution of each modality and how they relate to each other. For example, they could analyze the correlation between different modalities to understand how they interact. They should also provide a more detailed explanation of how the tasks are defined and why they are relevant to IoT applications. For instance, they could provide specific examples of how the tasks are used in real-world IoT scenarios. Furthermore, the authors should provide a more detailed explanation of the modeling paradigms used in the experiments, including the specific models used, their architectures, and their training procedures. This would make it easier for other researchers to reproduce the results and to understand the strengths and weaknesses of each modeling approach. The authors should also consider providing a more detailed analysis of the performance of different modeling approaches on different tasks, which would help to identify the most effective modeling strategies for each task.

To enhance the paper's contribution, the authors should consider exploring the potential of using the benchmark to develop new modeling techniques that are specifically designed for IoT data. For example, they could investigate the use of graph neural networks or transformers for modeling the relationships between different modalities. They could also explore the use of multi-task learning to improve the performance of models on multiple tasks simultaneously. The authors should also consider providing a more detailed analysis of the limitations of the benchmark, such as the size of the dataset and the diversity of the modalities. This would help to identify areas where future research is needed. The authors should also consider providing a more detailed analysis of the computational cost of the different modeling approaches, which would help to identify the most efficient models for resource-constrained IoT devices.

Finally, the authors should consider providing a more detailed comparison of their benchmark with existing IoT datasets. This would help to highlight the unique contributions of their benchmark and to identify areas where it could be used to advance the state of the art in IoT research. The authors should also consider providing a more detailed analysis of the potential impact of their benchmark on real-world IoT applications. For example, they could investigate the use of their benchmark to develop new algorithms for activity recognition or anomaly detection. The authors should also consider providing a more detailed analysis of the ethical implications of using their benchmark, such as the potential for bias in the data or the use of sensitive information. This would help to ensure that the benchmark is used responsibly and ethically.

### Questions

1. How do the authors plan to address the limitations of the benchmark in future work?
2. What are the potential applications of the benchmark in real-world IoT scenarios?

### Rating

3

### Confidence

3

**********
