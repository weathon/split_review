### Summary

This paper proposes a benchmark to evaluate the robustness of visual-language foundation models (FMs) under low-resolution conditions. The authors find that model size positively correlates with robustness to resolution degradation, pre-training dataset quality is more important than size, and fine-tuned and higher resolution models are less robust against LR. They also propose a new metric, Weighted Aggregated Robustness (WAR), and a simple strategy, LR-TK0, to enhance robustness against low-resolution inputs without altering the pre-trained weights.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed benchmark covers a wide range of foundation models and datasets, providing a comprehensive evaluation of model robustness to low-resolution inputs.
3. The proposed metric, WAR, addresses the limitations of existing robustness metrics, offering a more balanced evaluation of model performance across resolutions and datasets.
4. The proposed method, LR-TK0, is simple yet effective in enhancing model robustness against low-resolution inputs without altering the pre-trained weights.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why low-resolution images are important for evaluating the robustness of visual-language foundation models. While the authors mention that low-resolution images are common in real-world scenarios, they do not provide specific examples or use cases where this is particularly critical. For instance, it would be helpful to discuss scenarios where high-resolution information is not essential for accurate classification, and where low-resolution images are sufficient. The paper should also clarify why the specific resolutions used in the benchmark are relevant, and how they relate to real-world scenarios. For example, are these resolutions representative of typical low-resolution images encountered in practical applications, or are they chosen arbitrarily? A more detailed discussion of the practical relevance of the chosen resolutions would strengthen the paper's motivation.
2. The paper does not provide a clear explanation of how the proposed metric, WAR, is calculated. The authors should provide a detailed description of the metric, including the specific formulas and parameters used. It is also important to discuss the advantages of WAR over existing metrics, and how it addresses the limitations of previous evaluation methods. The paper should also provide a more detailed analysis of the results obtained using WAR, and how these results differ from those obtained using other metrics. For example, it would be helpful to show how WAR correlates with human performance on low-resolution images, and how it captures the robustness of different models more effectively than existing metrics.
3. The paper does not provide a clear explanation of how the proposed method, LR-TK0, works. The authors should provide a detailed description of the method, including the specific steps involved in adding trainable low-resolution tokens to the frozen transformer. It is also important to discuss the rationale behind this approach, and how it helps to improve the robustness of VLMs to low-resolution inputs. The paper should also provide a more detailed analysis of the results obtained using LR-TK0, and how these results compare to those obtained using other methods. For example, it would be helpful to show how LR-TK0 improves the performance of different models on different datasets, and how it compares to other methods in terms of computational cost and ease of implementation.

### Suggestions

The paper would benefit significantly from a more detailed discussion of the practical relevance of low-resolution images in real-world applications. While the authors mention that low-resolution images are common, they should provide specific examples where this is particularly critical. For instance, in medical imaging, high-resolution details might be less important than identifying the presence of a disease, which can often be detected from a lower-resolution image. Similarly, in surveillance, the overall scene might be more important than fine-grained details. The authors should also clarify why the specific resolutions used in the benchmark are relevant, and how they relate to real-world scenarios. For example, are these resolutions representative of typical low-resolution images encountered in practical applications, or are they chosen arbitrarily? A more detailed discussion of the practical relevance of the chosen resolutions would strengthen the paper's motivation and make the benchmark more impactful. This would help to justify the focus on low-resolution images and highlight the practical significance of the proposed benchmark.

Furthermore, the paper needs to provide a more thorough explanation of the proposed metric, WAR, and its advantages over existing metrics. The authors should include the specific formulas and parameters used in the calculation of WAR, and discuss how it addresses the limitations of previous evaluation methods. For example, how does WAR handle the varying performance of models across different resolutions, and how does it compare to metrics like SAR and WAR? It would be beneficial to show how WAR correlates with human performance on low-resolution images, and how it captures the robustness of different models more effectively than existing metrics. A more detailed analysis of the results obtained using WAR, and how these results differ from those obtained using other metrics, would also be valuable. This would help to establish the value of WAR as a more reliable metric for evaluating the robustness of VLMs.

Finally, the paper should provide a more detailed explanation of the proposed method, LR-TK0. The authors should describe the specific steps involved in adding trainable low-resolution tokens to the frozen transformer, and discuss the rationale behind this approach. How does LR-TK0 help to improve the robustness of VLMs to low-resolution inputs, and what are the advantages of this approach compared to other methods? The paper should also provide a more detailed analysis of the results obtained using LR-TK0, and how these results compare to those obtained using other methods. For example, how does LR-TK0 improve the performance of different models on different datasets, and how does it compare to other methods in terms of computational cost and ease of implementation? A more thorough explanation of the method and its results would help to establish the effectiveness of LR-TK0 as a practical solution for improving the robustness of VLMs to low-resolution inputs.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
