# Zero-shot Quantization for Object Detection

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Zero-shot quantization (ZSQ) has achieved remarkable success in classification tasks by leveraging synthetic data for network quantization without accessing the original training data. However, when applied to object detection networks, current ZSQ methods fail due to the inherent complexity of the task, which encompasses both localization and classification challenges. On the one hand, the precise location and size of objects within the samples for object detection remain unknown and elusive in zero-shot scenarios, precluding artificial reconstruction without ground-truth information. On the other hand, object detection datasets typically exhibit category imbalance, and random category sampling methods designed for classification tasks cannot capture this information.
To tackle these challenges, we propose a novel ZSQ framework specifically tailored for object detection. The proposed framework comprises two key steps: First, we employ a novel bounding box and category sampling strategy in the calibration set generation process to infer the original training data from a pre-trained detection network and reconstruct the location, size and category distribution of objects within the data without any prior knowledge. Second, we incorporate feature-level alignment into the Quantization Aware Training (QAT) process, further amplifying its efficacy through the integration of feature-level distillation.
Extensive experiments conducted on the MS-COCO and Pascal VOC datasets demonstrate the efficiency and state-of-the-art performance of our method in low-bit-width quantization. For instance, when quantizing YOLOv5-m to 5-bit, we achieve a 4.2\% improvement in the mAP metric, utilizing only about 1/60 of the calibration data required by commonly used LSQ trained with full trainset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method for solving the problem of Network Quantization for Object Detection in the zero-shot setting. The contribution of this paper is an adaptive sampling method (Relabel), which is used in the Synthetic data generation phase of the zero-shot setting. The main idea of Relabel is to use the prediction from the pretrained full-precision detection model to refine the bounding box/ class label during the optimization of Synthetic data generation. With the adaptive sampling strategy, the model performance can be improved while using less synthetic data than the baselines.

### Strengths
- Except for the points pointed out in the weakness section, this paper has a clear structure, and running the experiments/ablation study to validate the effectiveness of the proposed methods.

- The idea of Relabel is good, and can effectively improve the generation quality of the Zero-shot Quantization method.

- The paper claims this strategy can reduce the number of samples, thus reducing the training time, which is essential for the Quantization problem.

### Weaknesses
 **Clarity**: There are some claims that need to clarify for the experiment/qualitative/quantitative analysis:
-  In L78 and L79, the paper claims category imbalance in the current detection dataset, can you provide some examples illustrating that the previous method is struggling with it? Also, can you provide visualization/analysis your method is capable of handling the imbalance problems? (For example, using some metric to show the class distribution of the generated samples of the previous method and your method.) Specifically, how does the proposed adaptive sampling method address the class imbalance issue during the synthetic data generation? It would be beneficial to see a comparison of class distributions of generated data by previous methods and the proposed method against the original dataset, perhaps using metrics like KL divergence or chi-squared statistic to quantify the differences. Furthermore, a visualization of these distributions would be helpful to understand the improvement.

- In L80 and L81, the paper claims "fine-tuning strategy for zero-shot quantized detection network with synthetic calibration data has not been studied". Can the author clarify more about this claim, since [1] also fine-tuning from synthetic data? What is the difference between your fine-tuning approach compared to [1] and how you can improve from [1]? The claim needs more elaboration, as [1] also uses synthetic data for fine-tuning. The authors should clarify the specific differences in their fine-tuning approach, such as the use of Straight-Through Estimator (STE) for quantized model training, and the use of intermediate feature maps for distillation, which are not explicitly mentioned in the original paper. A more detailed comparison of the distillation loss functions and training procedures would be beneficial to highlight the novelty of the proposed approach.

**Experiment**:
- In the main paper, the paper should include the qualitative results of the synthetic data, compared with the baseline and [1], and also include the qualitative results from the quantized network and the full-precision network. It is important to visually compare the quality of the synthetic data generated by the proposed method against baselines, including [1]. This should include examples of bounding box accuracy and class label correctness. Additionally, qualitative results comparing the performance of the quantized network with the full-precision network on real images would help to understand the effectiveness of the proposed method in preserving detection capabilities under low-precision settings.
- Table 5, why the False positive sample from [1] is not included? The absence of results using the false positive sampling method from [1] in Table 5 is a significant oversight. It is necessary to include this baseline for a fair comparison, especially since it is a relevant method for synthetic data generation in object detection. The authors should explain why this comparison was omitted and provide the results in the revised manuscript.
- What is the purpose of the weak baseline Gaussian in Table 5? The purpose of the weak baseline using Gaussian noise in Table 5 is unclear. The authors should provide a more detailed explanation of why this baseline was included and what it is intended to demonstrate. Specifically, how does the Gaussian noise input help to evaluate the effectiveness of the proposed adaptive sampling method, and what conclusions can be drawn from the results?

### Questions
All concerns and questions are listed in the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel zero-shot quantization (ZSQ) framework designed specifically for object detection tasks. Unlike existing ZSQ approaches that are mainly suited for classification, this framework tackles the unique challenges of object detection, including localization and class imbalance. The framework involves two main components: (1) a bounding box and category sampling method for generating a synthetic calibration set, which approximates the spatial and categorical distribution of the objects without any real data, and (2) a quantization-aware training (QAT) process that integrates feature-level distillation for effective knowledge transfer. The proposed method achieves impressive results, outperforming baselines like LSQ on MS-COCO and Pascal VOC with only 1/60 of the data size typically required.

### Strengths
1. The bounding box and category sampling strategy provide a data-efficient way to approximate real-world object distributions, making it suitable for privacy-sensitive applications.
2. Integrating feature-level distillation into the QAT stage improves knowledge transfer and performance in low-bit quantization settings, significantly narrowing the performance gap between full-precision and quantized networks.
3. The framework demonstrates superior performance on both MS-COCO and Pascal VOC datasets, even in ultra-low-bit scenarios, thus highlighting its robustness and practical utility.
4. By requiring only a fraction of the typical calibration data size, the method enhances scalability for deployment on resource-constrained devices.

### Weaknesses
1. The framework combines synthetic data generation, adaptive sampling, and feature-level distillation within quantization-aware training (QAT), creating a complex pipeline. This complexity may hinder practical adoption and implementation in real-world settings. The interaction between these components is not fully transparent, making it difficult to isolate the impact of each on the final performance. For instance, the adaptive sampling method's dependence on the pre-trained model's internal representations might introduce biases that are hard to diagnose or mitigate.

2. The framework relies heavily on the quality of synthetic data for calibration, which may introduce variability in performance, especially in challenging real-world environments. Ensuring consistency in synthetic data quality is critical for stable results. The paper does not provide a detailed analysis of how variations in synthetic data generation parameters (e.g., bounding box size distributions, category sampling probabilities) affect the final quantized model's accuracy. This lack of sensitivity analysis raises concerns about the robustness of the method.

3. While the paper demonstrates strong results with YOLOv5 and Mask R-CNN, it lacks testing across a wider range of object detection architectures. Broader experimentation would strengthen confidence in the framework's generalizability. The current evaluation is limited to two specific architectures, which may not fully represent the diversity of object detection models. For example, the framework's performance on transformer-based detectors or other single-stage models is unknown.

4. The method's reliance on synthetic category distribution for handling class imbalance may not fully capture the complexities of real-world distributions. This could impact performance in scenarios with highly skewed class distributions. The synthetic data generation process might not accurately reflect the long-tail distribution of real-world object categories, potentially leading to suboptimal performance on less frequent classes.

5. Although the paper suggests that a small calibration set suffices, a more granular analysis of the calibration set size across different bit-widths could provide insights into optimal data requirements and help streamline data efficiency. The paper lacks a systematic study of how the calibration set size affects the performance at different quantization levels. It is unclear whether a fixed calibration set size is optimal across all bit-widths.

6. The method's effectiveness largely depends on feature-level and prediction-matching distillation. Over-reliance on distillation may limit its flexibility for future developments in quantization techniques that don’t use distillation. The strong dependence on distillation might make it difficult to adapt the framework to scenarios where distillation is not feasible or desirable, such as in resource-constrained environments where the full-precision model is not available.

### Questions
Please refer to the Weaknesses box.

### Soundness
3

### Presentation
3

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
This work only uses the pre-trained object detection network to reconstruct the training samples without accessing any original data or labels, and realizes zero-shot quantization of the object detection network.

### Strengths
1. The problem raised by the paper is clearly expressed and the motivation is clearly stated.
2. This paper demonstrates the effectiveness of the proposed method through the extensive experiments.

### Weaknesses
Although the paper has demonstrated the effectiveness of the method in experiments, the explanation of the proposed method is difficult to follow.
1. In Section 3.2 and ‘Relabel’ paragraph, The supervision mentioned in formula 5 is done by GT. In my understanding, the role of GT is replaced by the generation of the "teacher" model. In the initial stage, all information such as image and position are initialized as Gaussian noise. How does the teacher model obtain information to complete this optimization? I still feel unclear about the establishment process of this optimization.
2. After this sentence, the author only mentioned that this is the 'teacher' model. Is it the model itself that is being quantized or is it a model with other requirements? The author did not elaborate.
3. It is recommended that the author add a detailed explanation of f_l after formula 7. What specific layers does the author distill?
4. In appendix C, the author only compared the amount of data and the cost of the training process. What is the time consumption of generating samples in the first stage?

### Questions
In page 1, the paper mentions that ‘Classification networks require only a randomly sampled category id label for data synthesizing’, which means that classification task also samples the gt labels. Why can not detection task methods take gt as label for location and size generation?

### Soundness
2

### Presentation
2

### Contribution
3
