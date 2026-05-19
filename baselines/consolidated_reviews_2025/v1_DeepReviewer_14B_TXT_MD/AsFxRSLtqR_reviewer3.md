### Summary

This paper investigates the impact of low-resolution (LR) images on the zero-shot classification performance of visual-language foundation models (FMs). The authors introduce LR0.FM, a benchmark that evaluates 10 foundation models across 66 backbones and 15 datasets. They propose a new metric, Weighted Aggregated Robustness (WAR), to address the limitations of existing metrics. The key findings reveal that larger models exhibit greater robustness to resolution degradation, pre-training dataset quality is more important than its size, and fine-tuned models are less robust against LR. The authors also introduce LR-TK0, a simple strategy that introduces LR-specific tokens to enhance robustness without altering pre-trained weights.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new benchmark, LR0.FM, for evaluating the impact of low-resolution images on the zero-shot classification performance of visual-language foundation models. This is a novel contribution to the field, as it addresses an underexplored aspect of foundation models.
2. The authors propose a novel metric, Weighted Aggregated Robustness (WAR), to address the limitations of existing metrics and better evaluate model performance across resolutions and datasets. This is a significant contribution, as it provides a more comprehensive evaluation of model resilience.
3. The paper provides several key insights, such as the correlation between model size and robustness, the importance of pre-training dataset quality, and the impact of fine-tuning and input resolution on performance. These insights are valuable for the research community.
4. The authors introduce a simple yet effective solution, LR-TK0, which introduces low-resolution-specific tokens to enhance robustness without altering the pre-trained weights. This is a practical contribution that can be easily adopted by practitioners.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on zero-shot classification performance under LR conditions. However, it does not explore the impact of LR on other tasks that foundation models are capable of, such as object detection, image segmentation, or image generation. This limits the scope of the study and its generalizability to other tasks. The analysis is confined to classification, and it remains unclear how the observed robustness trends would translate to tasks with different output structures and requirements. For instance, object detection relies on bounding box predictions, which might be affected differently by low-resolution inputs compared to classification logits.
2. The paper introduces a new metric, Weighted Aggregated Robustness (WAR), but it does not provide a detailed comparison with other existing metrics for evaluating model robustness. It is not clear how WAR compares to metrics like accuracy drop, relative robustness, or other established measures. The lack of a thorough comparison makes it difficult to assess the true value and novelty of the proposed metric. It is also unclear if WAR is sensitive to different types of robustness challenges, such as adversarial attacks or common corruptions, which are often considered in robustness evaluations.
3. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed LR-TK0 method. It is not clear how the introduction of LR-specific tokens affects the inference time and memory requirements of the model. This is an important consideration for practical applications, especially in resource-constrained environments. The paper should include a quantitative analysis of the overhead introduced by the LR-TK0 method, including the number of additional parameters and the impact on inference speed.

### Suggestions

The paper makes a valuable contribution by exploring the impact of low-resolution images on the zero-shot classification performance of visual-language foundation models. However, the study could be significantly strengthened by expanding its scope to include other tasks that foundation models are capable of. Specifically, the authors should investigate how low-resolution inputs affect object detection, image segmentation, and image generation tasks. This would provide a more comprehensive understanding of the robustness of foundation models under low-resolution conditions and would increase the generalizability of the findings. For example, in object detection, the authors could evaluate the performance of the models in terms of mean Average Precision (mAP) at different resolutions, and analyze how the bounding box predictions are affected by the resolution degradation. Similarly, for image segmentation, the authors could evaluate the performance using metrics like Intersection over Union (IoU) and analyze how the segmentation masks are affected by low-resolution inputs. For image generation, the authors could evaluate the quality of generated images using metrics like Fréchet Inception Distance (FID) and Inception Score (IS) at different resolutions. This would provide a more complete picture of the impact of low-resolution inputs on the overall performance of foundation models.

Furthermore, the paper should provide a more detailed comparison of the proposed Weighted Aggregated Robustness (WAR) metric with other existing metrics for evaluating model robustness. The authors should compare WAR with metrics like accuracy drop, relative robustness, and other established measures, and discuss the advantages and disadvantages of each metric. This would help to clarify the novelty and value of the proposed metric and would provide a more solid foundation for its use in future research. The authors should also investigate the sensitivity of WAR to different types of robustness challenges, such as adversarial attacks and common corruptions. This would help to determine the applicability of WAR in different scenarios and would provide a more comprehensive evaluation of model robustness. For example, the authors could evaluate the performance of the models under adversarial attacks using metrics like robust accuracy and compare the results with the WAR metric. Similarly, the authors could evaluate the performance of the models under common corruptions like noise, blur, and compression using metrics like mean corruption error and compare the results with the WAR metric.

Finally, the paper should provide a more detailed analysis of the computational cost and efficiency of the proposed LR-TK0 method. The authors should quantify the overhead introduced by the LR-specific tokens, including the number of additional parameters and the impact on inference speed. This is an important consideration for practical applications, especially in resource-constrained environments. The authors should also compare the computational cost of LR-TK0 with other methods for improving robustness, such as data augmentation and adversarial training. This would help to determine the practicality of the proposed method and would provide a more complete picture of its trade-offs. For example, the authors could measure the inference time of the models with and without LR-TK0 and compare the results. Similarly, the authors could measure the memory requirements of the models with and without LR-TK0 and compare the results. This would provide a more comprehensive evaluation of the computational cost of the proposed method.

### Questions

1. How does the performance of foundation models under low-resolution conditions affect their ability to generalize to real-world applications? Are there specific domains or tasks where the impact of low-resolution images is more pronounced?
2. The paper introduces the LR-TK0 method to enhance the robustness of models without altering pre-trained weights. However, it does not explore the potential of other techniques, such as data augmentation or adversarial training, to improve robustness under low-resolution conditions. How do these techniques compare to LR-TK0 in terms of effectiveness and efficiency?
3. The paper focuses on the impact of low-resolution images on zero-shot classification performance. However, it does not explore the impact of other image quality issues, such as noise, blur, or compression artifacts, on the performance of foundation models. How do these factors interact with low-resolution to affect model performance?
4. The paper provides insights into the relationship between model size, pre-training dataset quality, and robustness to low-resolution images. However, it does not provide specific recommendations for designing and training foundation models that are more robust to low-resolution conditions. What are the key considerations for developing more robust foundation models?

### Rating

6

### Confidence

3

**********
