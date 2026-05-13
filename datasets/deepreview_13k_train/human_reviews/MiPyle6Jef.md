# QP-SNN: Quantized and Pruned Spiking Neural Networks

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Brain-inspired Spiking Neural Networks (SNNs) leverage sparse spikes to encode information and operate in an asynchronous event-driven manner, offering a highly energy-efficient paradigm for machine intelligence. However, the current SNN community focuses primarily on performance improvement by developing large-scale models, which limits the applicability of SNNs in resource-limited edge devices. In this paper, we propose a hardware-friendly and lightweight SNN, aimed at effectively deploying high-performance SNN in resource-limited scenarios. Specifically, we first develop a baseline model that integrates uniform quantization and structured pruning, called QP-SNN baseline. While this baseline significantly reduces storage demands and computational costs, it suffers from performance decline. To address this, we conduct an in-depth analysis of the challenges in quantization and pruning that lead to performance degradation and propose solutions to enhance the baseline's performance. For weight quantization, we propose a weight rescaling strategy that utilizes bit width more effectively to enhance the model's representation capability. For structured pruning, we propose a novel pruning criterion using the singular value of spatiotemporal spike activities to enable more accurate removal of redundant kernels. Extensive experiments demonstrate that integrating two proposed methods into the baseline allows QP-SNN to achieve state-of-the-art performance and efficiency, underscoring its potential for enhancing SNN deployment in edge intelligence computing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work focuses on the applicability of SNNs on edge devices, integrating weights quantization and structured pruning techniques, and providing an in-depth analysis of the main challenges in each respective area. Specifically, for weights quantization, the work proposes weight scaling; for structured pruning, it introduces a method to remove redundant convolutional kernels by analyzing the temporal-spatial spike activity singular values in the spike feature matrix. This is an effective joint exploration of weight quantization and pruning in SNNs. I appreciate the idea of leveraging quantization, pruning, and event-driven techniques—three approaches that accelerate, conserve energy, and enhance the efficiency of neural networks.

### Strengths
1. The illustrations are thoughtfully crafted.

2. The manuscript presents a clear structure, and maintains logical consistency.

3. A detailed analysis of the weight distribution in SNNs provides the motivation for the re-scaling method.

4. The experiments demonstrate the effectiveness of this method on both static and dynamic datasets.

### Weaknesses
1. Regarding the selection of the quantization scaling factor $\gamma$, this work employs three different sampling methods. Although experiments indicate that scaling with the 1-norm mean yields the best results, I believe there is still room for improvement, such as using a piecewise $\gamma$. The current justification for choosing the 1-norm mean is not sufficiently rigorous, and the potential benefits of a more adaptive, piecewise scaling approach, which could better accommodate the non-uniform distribution of weights, are not adequately explored. A more thorough analysis of how different scaling strategies impact the final performance is needed.

2. To my knowledge, when two or more model lightweigh techniques are employed, compatibility issues often arise, such as the order of applying these techniques and the training strategies involved. The manuscript lacks a detailed discussion on how the chosen order of quantization and pruning affects the final performance and convergence. Specifically, the interaction between the weight scaling method and the structured pruning approach is not fully explored, potentially leading to suboptimal results. Additional clarification is needed on these aspects, including a discussion of how the training process is adapted to accommodate both techniques.

3. At the end of Algorithm. 1, fine-tuning is required after pruning. The specific details of this fine-tuning process should be provided, including the optimizer used, learning rate schedule, and the number of epochs. Without these details, it is difficult to reproduce the results and assess the effectiveness of the proposed method. Furthermore, the impact of different fine-tuning strategies on the final performance should be discussed.

4. In Table. 2 of the experimental section, the baselines for A-F are not consistent. I suggest the authors provide a unified ablation study. Additionally, regarding the compatibility issues of interest, I encourage the authors to conduct an ablation study on the compatibility of quantization and pruning, including different orders of application and their impact on performance.

### Questions
1.To my knowledge, the highest-performing architecture in the SNN field is the Spiking Transformer [1-5]. Please discuss whether the proposed method can be effectively applied to the Spiking Transformer. If feasible, please provide some preliminary experimental results.

[1] Zhou, Z., Zhu, Y., He, C., Wang, Y., Shuicheng, Y. A. N., Tian, Y., & Yuan, L. Spikformer: When Spiking Neural Network Meets Transformer. In The Eleventh International Conference on Learning Representations.

[2] Yao, M., Hu, J., Zhou, Z., Yuan, L., Tian, Y., Xu, B., & Li, G. (2024). Spike-driven transformer. Advances in neural information processing systems, 36.

[3] Zhou, C., Yu, L., Zhou, Z., Ma, Z., Zhang, H., Zhou, H., & Tian, Y. (2023). Spikingformer: Spike-driven residual learning for transformer-based spiking neural network. arXiv preprint arXiv:2304.11954.

[4] Zhou, Z., Che, K., Fang, W., Tian, K., Zhu, Y., Yan, S., ... & Yuan, L. (2024). Spikformer v2: Join the high accuracy club on imagenet with an snn ticket. arXiv preprint arXiv:2401.02020.

[5] Yao, M., Hu, J., Hu, T., Xu, Y., Zhou, Z., Tian, Y., ... & Li, G. Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips. In The Twelfth International Conference on Learning Representations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents QP-SNN, which integrates quantization and structure pruning methods. The quantization approach is based on hardware-friendly uniform quantization, while the pruning method employs SVD techniques. QP-SNN has been validated on classification datasets, achieving state-of-the-art performance.

### Strengths
1. The writing of this paper is good and easy to read.

2. The experiments in the paper demonstrate the effectiveness of the proposed ReScaW algorithm and SVD-based pruning.

### Weaknesses
1. The ReScaW-based uniform quantization lacks innovation, as it is merely a combination of uniform quantization and weight scaling [1].

2. The SVD-based pruning appears to be an application of SVD pruning in SNNs. There are many methods utilizing SVD decomposition or selecting important singular values for pruning [2][3]. Please clarify the specific advantages of applying this in SNNs.

3. The SVD decomposition method introduces additional time complexity. How much does it specifically affect the training time?

4. The experiments are insufficient from several perspectives. Firstly, why use the 2021 SEW-ResNet and Spiking ResNet instead of the latest SNN models? Secondly, this method has only been tested on simple classification tasks; without testing on more complex downstream tasks. Thus, it is difficult to prove the potential applicability of this work.

5. As an efficiency-focused study, why does the paper not present sufficiently robust efficiency metrics, such as OPs/SOPs, training time, inference speed, and energy consumption?

6. Why there is no presentation of pruning ratio statistics in the main text, which obscures the specific effectiveness of this aspect?

### Questions
Please see the weaknesses.

### Soundness
2

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
4

### Summary
The paper proposes two technologies including a weight-rescaling strategy and an SVS-based pruning criterion for weight quantization and structured pruning of SNN respectively. These technologies reduce the model size significantly while maintains the SNN accuracy.

### Strengths
1. The paper develops a hardware-efficient and lightweight QP-SNN baseline by integrating uniform quantization and structured pruning.
2. The weight-rescaling strategy and the SVS-based pruning criterion works well on SNN benchmarks.

### Weaknesses
1. The proposed technologies including the weight-rescaling strategy and the SVS-based pruning criterion do not fully utilize the unique characteristics of SNN, such as the sparsity to reduce synaptic operation and temporal information to maintain the SNN accuracy. The technologies can also be used in ANN models.
2. The comparison with SNNs that are not compressed is missing, such as SEW-ResNet[1] and MS-ResNet[2]. Compared to these works, the accuracy degradation is still large.
3. The results that the saving of synaptic operation is missing.

### Questions
1. What is the effectiveness of this work in saving synaptic operation in SNN inference? The author can use the code in https://github.com/zhouchenlin2096/Spikingformer/tree/master/energy_consumption_calculation to provide the detailed number of synaptic operations of the compressed SNN in this work.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents QP-SNN, a novel approach to creating efficient and hardware-friendly Spiking Neural Networks (SNNs) by combining uniform quantization and structured pruning. The authors first develop a baseline model, then address its performance limitations through two key innovations: (1) a weight rescaling (ReScaW) strategy for more effective bit-width utilization in quantization, and (2) a novel pruning criterion based on the singular value of spatiotemporal spike activities (SVS). The experimental results demonstrate that QP-SNN achieves state-of-the-art performance while significantly reducing model size.
Strengths

### Strengths
1. Theoretical Foundation:
- The analysis of bit-width utilization provides clear theoretical justification for the ReScaW strategy.
- The proposed SVS criterion is well-grounded in mathematical principles.

2. Method Innovation:
- The paper presents two novel techniques (ReScaW and SVS) that effectively address specific limitations in existing quantization and pruning approaches.
- The solutions are well-motivated by careful analysis of the underlying problems.


3. Experimental Validation:
- Comprehensive experiments across multiple datasets and architectures.
- Detailed ablation studies that validate each component's contribution.

### Weaknesses
1.The selection process for pruning rates appears arbitrary and lacks systematic justification. 
2.This paper is only verified on the simple computer vision classification task.

### Questions
1. How does the computational cost of calculating singular values in the SVS criterion compare to existing pruning criteria? Is there a significant overhead during training?

2.What is the impact of the proposed methods on the network's spike sparsity?

3.How sensitive is the method to the choice of ε in the SVS-based pruning criterion?

How does the approach perform when applied to other types of neural networks beyond classification tasks, such as object detection?

### Soundness
3

### Presentation
3

### Contribution
3
