### Summary

This paper investigates the impact of low-resolution (LR) images on the zero-shot classification performance of visual-language foundation models (FMs). The authors introduce LR0.FM, a benchmark that evaluates 10 foundation models across 66 backbones and 15 datasets. They propose a new metric, Weighted Aggregated Robustness (WAR), to address the limitations of existing metrics and better evaluate model performance across resolutions and datasets. The key findings reveal that larger models exhibit greater robustness to resolution degradation, pre-training dataset quality is more important than its size, and fine-tuned models are less robust against LR. The authors also introduce LR-TK0, a simple strategy that introduces LR-specific tokens to enhance robustness without altering pre-trained weights.

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

1. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed LR-TK0 method. It is unclear how the introduction of LR-specific tokens affects the inference time and memory requirements of the model. This is an important consideration for practical applications, especially in resource-constrained environments. A thorough analysis should include a comparison of the computational overhead of LR-TK0 against other methods for improving robustness, such as data augmentation or adversarial training.
2. The paper does not explore the potential of other techniques, such as data augmentation or adversarial training, to improve robustness under low-resolution conditions. A comparison of these techniques with LR-TK0 would provide a more comprehensive understanding of the landscape of methods for addressing low-resolution robustness and help to contextualize the effectiveness of the proposed approach. The lack of such comparisons makes it difficult to assess the relative strengths and weaknesses of LR-TK0.
3. The paper does not explore the impact of other image quality issues, such as noise, blur, or compression artifacts, on the performance of foundation models. These factors often co-occur with low resolution in real-world scenarios, and their combined effect on model performance is not addressed. It is important to understand how LR-TK0 performs under these more complex and realistic conditions.

### Suggestions

The paper would benefit from a more thorough investigation into the computational costs associated with the LR-TK0 method. The authors should provide a detailed analysis of the inference time and memory usage of models with and without LR-TK0, across different model sizes and input resolutions. This analysis should include a breakdown of the computational overhead introduced by the LR-specific tokens, and compare it to other methods for improving robustness, such as data augmentation or adversarial training. Furthermore, the authors should explore the trade-offs between robustness gains and computational costs, providing practical guidance for users who need to balance performance and efficiency. For example, it would be useful to see how the performance of LR-TK0 scales with different numbers of LR tokens, and whether there are diminishing returns with increasing numbers of tokens. This would allow practitioners to make informed decisions about the optimal configuration of LR-TK0 for their specific needs.

To better contextualize the effectiveness of LR-TK0, the authors should compare it with other techniques for improving robustness under low-resolution conditions. Specifically, they should investigate the performance of data augmentation techniques, such as random resizing and cropping, or the application of Gaussian blur, in comparison to LR-TK0. Additionally, the authors should explore the use of adversarial training methods, which have been shown to improve robustness against various types of input perturbations. A direct comparison of these methods would provide a more comprehensive understanding of the strengths and weaknesses of LR-TK0, and help to identify the scenarios where it is most effective. For example, it would be interesting to see if LR-TK0 is more effective than data augmentation for very low resolutions, or if adversarial training can achieve similar or better robustness with less computational overhead. Such comparisons would significantly enhance the practical value of the paper.

Finally, the authors should investigate the impact of other image quality issues, such as noise, blur, and compression artifacts, on the performance of foundation models. These factors often co-occur with low resolution in real-world scenarios, and their combined effect on model performance is not addressed. The authors should conduct experiments to evaluate the performance of LR-TK0 under these more complex and realistic conditions. For example, they could add Gaussian noise or motion blur to the low-resolution images, or simulate compression artifacts using JPEG compression. This would provide a more comprehensive understanding of the robustness of LR-TK0, and help to identify its limitations. Furthermore, the authors should explore whether LR-TK0 can be combined with other techniques, such as denoising or deblurring methods, to further improve robustness under these challenging conditions. This would make the paper more relevant to real-world applications, where images often suffer from multiple types of degradation.

### Questions

1. How does the performance of foundation models under low-resolution conditions affect their ability to generalize to real-world applications? Are there specific domains or tasks where the impact of low-resolution images is more pronounced?
2. The paper introduces the LR-TK0 method to enhance the robustness of models without altering pre-trained weights. However, it does not explore the potential of other techniques, such as data augmentation or adversarial training, to improve robustness under low-resolution conditions. How do these techniques compare to LR-TK0 in terms of effectiveness and efficiency?
3. The paper focuses on the impact of low-resolution images on zero-shot classification performance. However, it does not explore the impact of other image quality issues, such as noise, blur, or compression artifacts, on the performance of foundation models. How do these factors interact with low-resolution to affect model performance?
4. The paper provides insights into the relationship between model size, pre-training dataset quality, and robustness to low-resolution images. However, it does not provide specific recommendations for designing and training foundation models that are more robust to low-resolution conditions. What are the key considerations for developing more robust foundation models?

### Rating

6

### Confidence

4

**********
