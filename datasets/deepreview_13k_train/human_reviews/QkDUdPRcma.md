# H-Direct: Homeostasis-aware Direct Spike Encoding for Deep Spiking Neural Networks

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Deep spiking neural networks (SNNs) have been expected to enable energy-efficient artificial intelligence as a next-generation artificial neural network. Recently, with the development of various algorithms, such as direct spike encoding, many applications have been successfully implemented in deep SNNs. Notably, most state-of-the-art deep SNNs have greatly improved their performance by adopting direct spike encoding, which expresses input information as discrete spikes, thereby exerting substantial influence. Despite the importance of the encoding, efficient encoding methods have not been studied. As the first attempt to our knowledge, we thoroughly analyzed the conventional direct encoding. Our analysis revealed that the existing encoding restricts the training performance and efficiency due to inappropriate encoding. To address this limitation by maintaining an appropriate encoding, we introduced a concept of homeostasis to the direct spike encoding. With this concept, we presented a homeostasis-aware direct spike encoding (H-Direct), which consists of dynamic feature encoding loss, adaptive threshold, and feature diversity loss. Our experimental results demonstrate that the proposed encoding achieves higher performance and efficiency compared to conventional direct encoding across several image classification datasets on various architectures. We have validated that brain-inspired algorithms have the potential to enhance the performance and efficiency of deep SNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a homeostasis-aware direct spike encoding method (H-Direct) for spiking neural networks (SNNs) to improve encoding efficiency and stability. The authors introduce three novel components: Dynamic Feature Encoding (DFE) Loss, Adaptive Threshold (AT), and Feature Diversity (FD) Loss. Extensive experiments across multiple datasets demonstrate the effectiveness of H-Direct in enhancing the performance of deep SNNs, and the ablation study further shows the contribution of each component.

### Strengths
The experimental validation is thorough, with tests conducted on multiple datasets and network architectures, providing strong evidence for the proposed method’s efficacy. The authors also conducted an ablation study that helps to highlight the importance of each component within H-Direct, particularly in enhancing encoding stability and feature diversity. The overall approach is well-motivated and provides an innovative solution to improve SNN encoding by borrowing the concept of homeostasis from biological systems.

### Weaknesses
While H-Direct addresses important encoding issues in the encoding layer, similar issues may also exist in deeper layers, raising the question of why these corrections are not applied throughout the network. Additionally, the ablation study in Table 4 only shows improvements on CIFAR-10 with VGG16, while ResNet20 shows decreased performance for certain modules. This inconsistency brings the role of each module into question. DFE is also heavily dependent on BN, raising concerns about its applicability to networks without BN. Further clarification on why FD Loss fits a probability density function and how H-Direct performs on architectures like RNNs or Transformers is also needed. If the authors are unable to sufficiently address these concerns, I may consider lowering my score. However, should the authors provide thorough explanations and additional experiments that address these points, I would raise my score.

### Questions
1.	Why are the corrective mechanisms not applied beyond the encoding layer, given that over-firing and under-firing issues may also exist in deeper layers?
2.	In Table 4, why do certain modules of H-Direct decrease performance in ResNet20 compared to the baseline? Does this suggest limitations in module effectiveness across architectures?
3.	How would DFE perform in networks without Batch Normalization?
4.	What is the purpose of fitting FD to a probability density function, and which PDF is used? What is the impact of different PDFs?
5.	Does H-Direct show improvements in other architectures, such as RNNs or Transformers?
6.	Could the authors analyze the robustness of hyperparameters for the DFE, AT, and FD losses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an analysis of direct encoding and introduces a concept of homeostasis to direct spike encoding, including feature encoding loss, adaptive threshold, and feature diversity loss. The experimental results demonstrate that the proposed encoding improves performance and efficiency, but performance improvements are limited.

### Strengths
The direct encoding issue of SNN that the article focuses on is valuable, and the experiments are also sufficient.

### Weaknesses
1. Many statements in the paper lack sufficient persuasiveness,  such as those described in the abstract and introduction.
- 'Despite the importance of the encoding, efficient encoding methods HAVE NOT BEEN studied.' 
As far as I know, the time-to-first-spike (TTFS) method that utilizes the first spike time to encode information is regarded as a highly energy-efficient encoding method.
- 'Thus, the energy problem has become the MOST urgent issue to be addressed for sustainable development and utilization of AI in our lives.'
Aside from the energy problem, the sustainable development of AI also faces multiple challenges, such as data security, interpretability, model generalization, and regulatory and formal laws.
- 'Direct encoding learns encoding methods from data, which leads to superior performance over other encoding approaches.'
Can the author elaborate on this?

2. The proposed method lacks sufficient innovation, since the approach of setting dynamic neuronal thresholds and adjusting loss functions to enhance performance is widely used.

3. The experimental results do not demonstrate a substantial improvement in accuracy, and as model size and dataset scale increase, this improvement diminishes further. This raises concerns about the practical utility of the proposed method.

4. Does the performance improvement depend on a large number of training epochs? Could the authors provide more experimental details? Additionally, does the introduction of the proposed loss function add computational overhead?

### Questions
In addition to the problem mentioned in weakness, I have the following questions:
1. In Figure 1, in the image to the left of (b), the red box denotes OFE (Over-fired Encoding). Why is the RED box filled with ORANGE blocks (Orange represents normal spike counts)?

2. The criteria for the divisions are not clearly articulated. For instance, what spike count corresponds to DSE? Furthermore, when the spike count is zero, how to distinguish between OFE and DSE?

3. Given that the performance improvements demonstrated in the experimental results are not substantial, the motivation behind this work raises questions. Intuitively, not all spiking neurons contribute to the output; some neurons at specific pixels may not respond or fire, which is also a reflection of the “sparseness” advantage of SNN. Therefore, is it necessary to activate all neurons associated with OFE and UFE?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This study addresses the limitations of existing direct spike encoding by first analyzing traditional direct spike encoding methods and categorizing the encoded spike channels into four types: over-activated, under-activated, dynamically selective, and persistent encoding. Subsequently, the concept of homeostasis was introduced into direct spike encoding, and this paper proposes a homeostasis-aware direct spike encoding method called H-Direct. This method achieves stable and appropriate encoding by suppressing over- and under-activation while encouraging dynamic feature selection.

### Strengths
1. Experiments show that the proposed steady-state mechanism improves the training performance and efficiency of deep SNNs on various datasets, models, and training algorithms, demonstrating the effectiveness and universality of the method.
2. A coding method inspired by the human brain is proposed.

### Weaknesses
1. This paper significantly reduces the number of spike data, but lacks theoretical power consumption calculation. Can it give specific power consumption results and compare them with some advanced works [1]?
2. The experimental effect of this paper is limited, and it is not compared with some advanced works [2][3] on many datasets.
I hope the author can introduce why H-direct works from a theoretical perspective.

### Questions
see weakness below.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes H-Direct, a homeostasis-aware spike encoding technique for deep Spiking Neural Networks (SNNs). It incorporates mechanisms like dynamic feature encoding loss, adaptive thresholding, and feature diversity loss to improve the performance and efficiency of deep SNNs. While the method shows potential in improving spike encoding performance, there are several concerns that prevent this work from being accepted at this stage.

### Strengths
The concept of integrating homeostasis to regulate spike encoding is interesting and innovative. The proposed approach seems to achieve meaningful improvements in terms of classification accuracy and energy efficiency in the experiments conducted.

### Weaknesses
While the introduction of homeostasis in spike encoding is intriguing, the overall novelty of the approach is limited. Many of the techniques applied, such as adaptive thresholds and feature diversity loss, have been explored in various forms in prior works on SNNs and neuromorphic computing. There is insufficient discussion on how this method truly differentiates itself from previous work like direct encoding approaches and surrogate gradients. The proposed method lacks a strong theoretical foundation. Although the paper discusses homeostasis from a biological perspective, the paper does not thoroughly justify the mathematical and theoretical basis for why introducing homeostasis in the encoding stage would lead to significant improvements in SNN performance. A deeper explanation of the relationship between the proposed encoding mechanisms and their impact on network learning dynamics is needed.

The experiments focus heavily on classification tasks using typical SNN benchmarks (CIFAR-10, CIFAR-100, etc.), which limits the generalization of the proposed approach. There are no experiments on more challenging neuromorphic datasets or tasks beyond classification, which could better validate the robustness and applicability of H-Direct. The performance gains, while present, are relatively marginal compared to existing state-of-the-art methods, especially when considering the complexity introduced by the additional loss functions and adaptive mechanisms. The paper’s presentation could be significantly improved. The descriptions of the core methods (like dynamic feature encoding loss and adaptive thresholds) are somewhat unclear and hard to follow without repeated reading. Additionally, the figures do not always effectively support the key points being made and could benefit from clearer labeling and explanations. The related work section does not adequately cover recent advances in energy-efficient SNN training or alternative spike encoding methods. Key works on the use of advanced encoding strategies and their implications on energy efficiency should be cited and discussed.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1
