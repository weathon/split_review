### Summary

This paper introduces a benchmark for evaluating the robustness of visual-language foundation models (VLMs) under low-resolution conditions. It finds that larger models, higher-quality pre-training datasets, and fine-tuning are more robust to low-resolution inputs. The paper also proposes a new metric, Weighted Aggregated Robustness (WAR), to better evaluate model performance across resolutions and datasets. Finally, it introduces a simple strategy, LR-TK0, to enhance model robustness against low-resolution inputs without altering pre-trained weights.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a comprehensive benchmark for evaluating the robustness of VLMs under low-resolution conditions.
3. The paper proposes a new metric, WAR, to better evaluate model performance across resolutions and datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why low-resolution images are important for evaluating the robustness of VLMs. While the authors mention that low-resolution images are common in real-world scenarios, they do not provide specific examples or use cases where this is particularly critical. For instance, it would be helpful to discuss scenarios where high-resolution information is not essential for accurate classification, and where low-resolution images are sufficient. The paper should also clarify why the specific resolutions used in the benchmark are relevant, and how they relate to real-world scenarios. For example, are these resolutions representative of typical low-resolution images encountered in practical applications, or are they chosen arbitrarily? A more detailed discussion of the practical relevance of the chosen resolutions would strengthen the paper's motivation.
2. The paper does not provide a clear explanation of how the proposed metric, WAR, is calculated. The authors should provide a detailed description of the metric, including the specific formulas and parameters used. It is also important to discuss the advantages of WAR over existing metrics, and how it addresses the limitations of previous evaluation methods. The paper should also provide a more detailed analysis of the results obtained using WAR, and how these results differ from those obtained using other metrics. For example, it would be helpful to show how WAR correlates with human performance on low-resolution images, and how it captures the robustness of different models more effectively than existing metrics.
3. The paper does not provide a clear explanation of how the proposed method, LR-TK0, works. The authors should provide a detailed description of the method, including the specific steps involved in adding trainable low-resolution tokens to the frozen transformer. It is also important to discuss the rationale behind this approach, and how it helps to improve the robustness of VLMs to low-resolution inputs. The paper should also provide a more detailed analysis of the results obtained using LR-TK0, and how these results compare to those obtained using other methods. For example, it would be helpful to show how LR-TK0 improves the performance of different models on different datasets, and how it compares to other methods in terms of computational cost and ease of implementation.

### Suggestions

The paper would benefit significantly from a more detailed discussion of the practical relevance of low-resolution images in real-world applications. While the authors mention that low-resolution images are common, they should provide specific examples where this is particularly critical. For instance, they could discuss scenarios in medical imaging, remote sensing, or surveillance where high-resolution information is not always available or where the primary challenge is to classify images with limited detail. They should also clarify why the specific resolutions used in the benchmark are relevant, and how they relate to real-world scenarios. For example, are these resolutions representative of typical low-resolution images encountered in practical applications, or are they chosen arbitrarily? A more detailed discussion of the practical relevance of the chosen resolutions would strengthen the paper's motivation. Furthermore, the authors should provide a more detailed analysis of the limitations of existing evaluation methods, and how their proposed metric, WAR, addresses these limitations. They should also provide a more detailed analysis of the results obtained using WAR, and how these results differ from those obtained using other metrics. For example, it would be helpful to show how WAR correlates with human performance on low-resolution images, and how it captures the robustness of different models more effectively than existing metrics. This would help to establish the value of WAR as a more reliable metric for evaluating the robustness of VLMs.

The paper should also provide a more detailed explanation of the proposed method, LR-TK0. The authors should provide a step-by-step description of how the trainable low-resolution tokens are added to the frozen transformer, and why this approach is effective in improving the robustness of VLMs to low-resolution inputs. They should also discuss the rationale behind this approach, and how it helps to preserve the semantic information of the low-resolution images. The paper should also provide a more detailed analysis of the results obtained using LR-TK0, and how these results compare to those obtained using other methods. For example, it would be helpful to show how LR-TK0 improves the performance of different models on different datasets, and how it compares to other methods in terms of computational cost and ease of implementation. This would help to establish the value of LR-TK0 as a practical solution for improving the robustness of VLMs to low-resolution inputs. The authors should also discuss the limitations of their approach, and how it could be improved in future work.

Finally, the paper should include a more detailed discussion of the limitations of the proposed benchmark and metric. The authors should discuss the potential biases in the dataset, and how these biases might affect the results. They should also discuss the limitations of the proposed metric, WAR, and how it might be improved in future work. For example, are there any scenarios where WAR might not be a reliable metric for evaluating the robustness of VLMs? The authors should also discuss the limitations of the proposed method, LR-TK0, and how it might be improved in future work. This would help to establish the scope of the paper and to identify areas for future research. By addressing these limitations, the paper would be more robust and would provide a more comprehensive understanding of the challenges and opportunities in evaluating the robustness of VLMs.

### Questions

Please see the weaknesses above.

### Rating

3

### Confidence

4

**********
