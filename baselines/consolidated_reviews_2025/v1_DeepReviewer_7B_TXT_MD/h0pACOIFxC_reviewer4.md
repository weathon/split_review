### Summary

This paper proposes a meta-learning approach to improve the generalization of foundation models (FMs) when fine-tuned on unseen tasks. The authors identify that standard two-phase fine-tuning (retraining followed by LoRA) can lead to suboptimal adaptation, as the retrained model may not be universally adaptable to future tasks. To address this, they introduce a meta-learning objective that explicitly considers the fine-tuning process and the low-rank adapter parameters. They provide theoretical analysis showing that their approach can provably recover the ground-truth parameters and improve performance on unseen tasks. Empirical results on synthetic data and the ConvAI2 dataset demonstrate the effectiveness of their method, showing significant performance gains over standard retraining.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with a clear motivation and a well-structured presentation of the proposed method and theoretical results.
- The authors provide a rigorous theoretical analysis, proving that their meta-learning objective can provably recover the ground-truth parameters and improve performance on unseen tasks. This adds a strong foundation to their approach.
- The empirical results on both synthetic data and the ConvAI2 dataset are compelling, demonstrating the effectiveness of the proposed method over standard retraining. The experiments are well-designed and provide clear evidence of the benefits of the meta-learning approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on the effectiveness of the proposed method but lacks a detailed analysis of its computational cost and scalability. It would be beneficial to understand how the method scales with the number of tasks, the size of the foundation model, and the dimensionality of the low-rank adapters. The absence of a thorough computational analysis makes it difficult to assess the practical feasibility of the method for large-scale applications, especially when compared to standard retraining approaches. The paper should include a breakdown of the time and memory requirements for each step of the meta-learning process, including the retraining phase, the fine-tuning phase, and the meta-learning phase. This would provide a more complete picture of the method's strengths and limitations.
- The experiments are conducted on a limited set of tasks and datasets. While the ConvAI2 dataset is relevant, it would be helpful to see results on a broader range of tasks and datasets to assess the generalizability of the proposed method. The current evaluation does not fully demonstrate the robustness of the approach across diverse problem settings. For example, it would be beneficial to see results on tasks with different modalities (e.g., image, audio) or tasks with varying levels of complexity.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their meta-learning approach. This should include a breakdown of the time and memory requirements for each step of the process, such as the retraining phase, the fine-tuning phase, and the meta-learning phase. Specifically, the authors should report the training time per epoch, the memory usage for storing model parameters, and the computational cost of the meta-learning updates. This analysis should be conducted on different hardware configurations to provide a more comprehensive understanding of the method's scalability. Furthermore, the authors should compare the computational cost of their method with that of standard retraining approaches, providing a clear picture of the trade-offs involved. This would allow practitioners to make informed decisions about the applicability of the proposed method in different scenarios. For example, the authors could include a table showing the training time and memory usage for different numbers of tasks, model sizes, and adapter dimensions.

To enhance the generalizability of the experimental results, the authors should evaluate their method on a broader range of tasks and datasets. This should include tasks with different modalities, such as image classification, object detection, and natural language processing. The authors should also consider tasks with varying levels of complexity, such as those involving sequential data or graph-structured data. This would provide a more robust assessment of the method's performance across diverse problem settings. Additionally, the authors should report the performance of their method on datasets with varying sizes and complexities, to understand how the method scales with the amount of training data. This would help to identify the limitations of the method and provide guidance for future research. For example, the authors could include results on datasets with different numbers of classes, different image resolutions, and different text lengths.

Finally, the authors should provide more insights into the practical implications of using meta-learning for fine-tuning foundation models. This should include a discussion of the ease of implementation, the sensitivity to hyperparameter choices, and the potential for overfitting. The authors should also compare their method with other meta-learning approaches for fine-tuning foundation models, highlighting the advantages and disadvantages of each approach. This would provide a more comprehensive understanding of the proposed method and its place within the broader landscape of meta-learning techniques. For example, the authors could discuss the challenges of tuning the meta-learning hyperparameters and how these choices affect the performance of the method. They could also discuss the potential for overfitting to the specific tasks in the meta-training set and how to mitigate this risk.

### Questions

- Could the authors provide more insights into the computational cost of their meta-learning approach compared to standard retraining? Specifically, how does the method scale with the number of tasks, the size of the foundation model, and the dimensionality of the low-rank adapters?
- Have the authors considered evaluating their method on a broader range of tasks and datasets, beyond the ConvAI2 dataset? If so, what were the results, and if not, what are the challenges in extending the evaluation to other domains?

### Rating

8

### Confidence

3

**********
