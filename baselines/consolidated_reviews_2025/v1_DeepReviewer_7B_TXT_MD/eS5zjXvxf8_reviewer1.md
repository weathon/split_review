### Summary

The paper presents a new benchmark for IoT data, Multiiot, which contains data from 12 modalities and 8 tasks. The authors also provide a set of baselines for the benchmark.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and present a large-scale benchmark that could be useful for the community.

### Weaknesses

#### Some Related Works


#### comment

The paper lacks novelty in its contributions. The benchmark is large-scale, but it primarily aggregates existing datasets from various modalities. While the paper does not claim to be a benchmark paper, it would be beneficial to provide a more in-depth analysis of the dataset. For instance, it would be helpful to understand the distribution of each modality and how they relate to each other. Additionally, the paper does not provide a clear explanation of how the tasks are defined and why they are relevant to IoT applications. The paper also lacks a discussion on the limitations of the benchmark, such as potential biases in the data or the tasks, and how these limitations might affect the performance of models trained on the benchmark.

### Suggestions

To enhance the paper's contribution, the authors should conduct a more thorough analysis of the Multiiot benchmark. This should include a detailed statistical analysis of each modality, including the distribution of data points, the range of values, and any potential outliers. Furthermore, the authors should explore the relationships between different modalities, perhaps using correlation analysis or other statistical methods to understand how they interact. This analysis should go beyond simply listing the datasets and should provide insights into the nature of the data itself. For example, if certain modalities are highly correlated, this could have implications for how models are trained and evaluated on the benchmark.

In addition to the statistical analysis, the authors should provide a more detailed explanation of the tasks defined on the benchmark. This should include a clear description of the problem being addressed by each task, the evaluation metrics used, and the rationale for choosing these specific tasks. The authors should also discuss how these tasks relate to real-world IoT applications. For example, if one of the tasks is activity recognition, the authors should explain why this task is relevant to IoT and how the benchmark data can be used to develop effective models for this task. This discussion should also include a comparison of the tasks to those used in other IoT benchmarks, highlighting the unique aspects of the Multiiot benchmark.

Finally, the authors should address the limitations of the benchmark. This should include a discussion of potential biases in the data, such as differences in the demographics of the participants or the characteristics of the environments in which the data was collected. The authors should also discuss the limitations of the tasks, such as the complexity of the problems being addressed and the potential for overfitting. Furthermore, the authors should discuss the limitations of the evaluation metrics, such as their sensitivity to noise or their inability to capture certain aspects of model performance. By acknowledging these limitations, the authors can provide a more balanced and realistic assessment of the benchmark and its potential for future research.

### Questions

What is the motivation behind the tasks defined on the benchmark?

### Rating

3

### Confidence

4

**********
