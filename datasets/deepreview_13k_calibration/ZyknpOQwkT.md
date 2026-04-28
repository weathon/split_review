# Rethinking Spiking Neural Networks from an Ensemble Learning Perspective

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Spiking neural networks (SNNs) have gained widespread attention for their low power consumption and spatio-temporal dynamics. In this paper, we consider an SNN as an ensemble of multiple temporal subnetworks that share architecture and weights, but produce different outputs due to differences in initial states (neuron membrane potentials). We identify a key factor influencing ensemble performance: excessive differences in the initial state lead to unstable subnetwork outputs that degrade performance, especially in the first two timesteps. To mitigate this, we propose to adaptively smooth the membrane potential cross adjacent timesteps to reduce the initial state discrepancy. Membrane potential smoothing allows for more stable ensemble effects and brings an additional bonus: additional pathways for forward propagation of information and backward propagation of gradients, mitigating temporal gradient vanishing and thus improving performance. Furthermore, we propose the temporally adjacent subnetwork guidance to improve the output consistency of subnetworks through distillation, further enhancing the ensemble stability and performance. Extensive experiments have shown that our method can be applied to VGG, ResNet, and Transofrmer architectures with great versatility. Compared to existing methods, our method shows superior performance in neuromorphic/static object/gesture recognition and 3D point cloud classification tasks, achieving 80.60\% accuracy on the CIFAR10-DVS dataset with only 5 timesteps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed a method to improve the performance of SNN from a new perspective, ensemble learning, by membrane potential smoothing and temporally adjacent subnetwork guidance. The smoothing method solved the problem that if the differences between initial states of neuron membrane potentials is excessive, the performance of SNN in ensemble learning will be degraded. The knowledge distillation in temporally adjacent subnetworks also improves the consistency of the subnetworks’ output.

### Strengths
1.The proposed membrane potential smoothing not only mitigates the difference in membrane potential distribution, which degrades the performance in ensemble learning of SNN, but also reduces the influence of the temporal gradient vanishing.

### Weaknesses
1.Some spelling errors. In ABSTRACT, line 25, “Transofrmer” -> “Transformer”.

2.The differences in the membrane potential distribution may not be easily observed. Adding quantitative data tables may be better.

3.The proposed method does not change the core of previous methods, the novelty compared with existing architectures and neuron models should be explained further, and how to improve the overall performance by these proposed approaches.

4. To be honest, the performance of the proposed model on CIFAR10-DVS and DVS-GESTURE is not higher compared to most of the existing spiking models (proposed in the last six months) based on VGG or ResNet backbone, Thus I could not determine the novelty and effectiveness of the proposed model.

### Questions
1.The proposed method does not change the core of previous methods, the novelty compared with existing architectures and neuron models should be explained further, and how to improve the overall performance by these proposed approach.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to adaptively smooth the membrane potential cross adjacent timesteps to reduce the initial state discrepancy.  They propose the temporally adjacent subnetwork guidance to improve the output consistency of subnetworks through distillation. Compared to existing methods, their method shows superior performance in neuromorphic/static object/gesture recognition and 3D
point cloud classification tasks.

### Strengths
***1.*** This paper is well-structured with high-quality figures, tables, and formulas.

***2.*** The paper includes relatively adequate analysis, comparative experiments, and ablation studies.

### Weaknesses
 ***1.*** This paper is not the first to view SNNs as a form of ensemble learning; it should reference prior works that have held this perspective.

***2.*** One of the motivations of this paper is to make instances at each time step more consistent; however, this has been demonstrated in many previous works and cannot be considered a novel contribution. But the method is novel. Author should change the focus when the write the paper.

### Questions
***1.*** The text in the figures is too small; please enlarge it to improve readability.

***2.*** Why perform 3D point cloud classification experiments. How does this validate the method's characteristics and effectiveness?

***3.*** The authors' method aims for the membrane potential distribution to become more consistent over time. However, at timestep 0, the method still shows a significant difference compared to other timesteps, with this difference being greater than that between other timesteps. This discrepancy makes it difficult for the method to support the argument of achieving consistent membrane potentials.

### Soundness
3

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
4

### Summary
This work rethinks spiking neural networks (SNNs) from the perspective of an ensemble of multiple temporal subnetworks and argues that improving the stability of the membrane potential and the output of each subnetwork would benefit the performance of SNNs. Based on these motives, this work proposes an approach of membrane potential smoothing and a well-designed learning objective with temporally adjacent subnetwork guidance to improve stability. When applied to several SNNs, the proposed method achieves higher performance across multiple datasets and tasks.

### Strengths
1. Most commendable is the match between the motivation and the proposed methodology of this work. The stability of temporal subnetworks is a meaningful research focus, and both membrane potential smoothing and temporally adjacent subnetwork guidance intuitively fit well with the goal of improving stability, especially since the smoothing design is concise and sufficiently novel.
2. The method efficiently improves several SNNs' performance across multiple datasets and tasks, demonstrating its effectiveness and generalizability.
3. The ablation studies are very comprehensive, illustrating the contribution of the methods and the influence of the hyperparameters. The visualization results show graphically the advantages of the method for improving stability.
4. The paper is well-written and easy to follow.

### Weaknesses
Major points:
1. The view of SNNs as an ensemble of temporal subnetworks actually originates from Spiking PointNet [1], and they proposed this view because the point cloud data is static and does not involve time dependence. One of the great features of SNNs is their ability to handle temporal data. Therefore, it is doubted whether the ensemble view is still justified when SNNs process data with strong time dependence, and whether membrane potential smoothing is necessary, as more varied potentials seem to be more conducive to representing the dynamic information of the input. Specifically, the smoothing operation might inadvertently suppress crucial temporal variations in the membrane potential, which could be essential for capturing complex temporal patterns in the input data. This raises concerns about the method's applicability to datasets with rich temporal dynamics.
2. The idea of promoting the consistency of SNN instances at different timesteps has been proposed in previous work [2]. While they used contrastive learning to bring network features closer at different time steps, this work uses KL divergence to bring the probability distribution of outputs closer at different time steps. The former design has broader applicability, while the latter is limited to classification tasks. The use of KL divergence, while effective for classification, inherently restricts the method's potential for broader applications where the output is not a probability distribution, such as regression or sequence generation tasks. This limitation significantly reduces the generalizability of the proposed approach.
3. Given that all experiments in this work are performed on classification tasks, the lack of ImageNet results makes the method somewhat unconvincing. The absence of large-scale image classification results on a benchmark like ImageNet makes it difficult to assess the scalability and robustness of the proposed method. The method's performance on smaller datasets may not translate to more complex and high-dimensional data, which is a critical factor in evaluating its practical applicability.

Minor point:
1. The statement that membrane potential smoothing is effective in other neurons is reckless (lines 278-279) and there is a lack of experiments to prove this.

### Questions
1. How does the method perform when applied to some more time-dependent datasets, such as spiking Heidelberg digits (SHD) [3]? Does membrane potential smoothing still benefit the performance in such cases?
2. How does temporally adjacent subnetwork guidance compare to or improve upon the contrastive learning method [2]? In addition, how can the loss function be adapted for non-classification tasks, such as object detection which requires the output of coordinates?
3. Please provide results on ImageNet or explain why ImageNet experiments are not included.

[3] Benjamin Cramer, Yannik Stradmann, Johannes Schemmel, and Friedemann Zenke. The Heidelberg Spiking Data Sets for the Systematic Evaluation of Spiking Neural Networks. IEEE Transactions on Neural Networks and Learning Systems. 2020.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper conducts a thorough investigation into the common issues faced by Spiking Neural Networks (SNNs) and identifies that SNNs primarily suffer from performance degradation due to excessive differences in membrane potential between time steps and uneven feature distribution across time steps. To address these issues, the paper proposes two approaches: **subnetwork guidance** (where each step of the model may be considered as a subnet) and **membrane potential smoothing**. Additionally, ablation experiments are presented to demonstrate the effectiveness of both methods, showing significant improvements in model performance.

### Strengths
* The paper is well-written, with a clear and easily understandable motivation. This clarity allows readers to quickly grasp the purpose and significance of the proposed methods.
* The effectiveness of the proposed methods is thoroughly validated on both static image datasets (CIFAR10/CIFAR100) and dynamic vision sensor (DVS) datasets, demonstrating strong performance across different data types.
* Experimental results indicate that the proposed methods are compatible with both CNN-based and Transformer architectures, highlighting their robust generalizability. This versatility suggests that the methods could serve as a widely applicable paradigm in SNN research.

### Weaknesses
* The paper mentions the efficiency of Spiking Neural Networks (SNNs) but does not provide experimental evidence on whether the proposed method retains this efficiency. It is recommended to evaluate energy consumption, preferably on hardware platforms such as GPUs, FPGAs, or neuromorphic chips, or to provide theoretical calculations as an alternative. Relevant computation methods can be referenced from prior works [1–4].

* The current experiments are limited to smaller datasets and do not include evaluations on larger, static datasets such as ImageNet. This limitation raises concerns about the method's generalizability and scalability. To strengthen the paper, I suggest including experiments on larger datasets or, at minimum, providing a theoretical analysis of expected performance on large-scale data. Such an evaluation would support the paper's claims of generalizability and effectiveness.

* In Figure 1, the paper shows the membrane potential distribution in a spiking VGG-9 model on the CIFAR10-DVS dataset, comparing the vanilla SNN with the proposed method. Although the figure aims to demonstrate a more stable membrane potential distribution across timesteps with the proposed approach, the visual difference between the two distributions is unclear, making it challenging to assess stability improvements. To clarify this, I recommend including quantitative measures of distribution stability across timesteps, such as mean and variance, or other relevant statistical characteristics. Additionally, a side-by-side comparison of these statistics could highlight any notable differences, making the figure’s intended message more accessible to readers.


[1] Horowitz, M. "1.1 Computing's energy problem (and what we can do about it)." *IEEE International Solid-State Circuits Conference Digest of Technical Papers (ISSCC)*, 2014.

[2] Luo, X. et al. "Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection." *arXiv preprint arXiv:2407.20708*, 2024.

[3] Yao, M. et al. "Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips." *Twelfth International Conference on Learning Representations (ICLR)*.

[4] Shen, G. et al. "Are Conventional SNNs Really Efficient? A Perspective from Network Quantization." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 2024.

### Questions
* The study lacks experiments on large-scale static datasets, such as ImageNet. Can the authors provide additional validation on these datasets to better assess the generalizability of their methods?

* For the spiking transformer model, the commonly used timesteps are 4, 10, or 16. Could the authors clarify the rationale behind selecting a timestep of 5, and discuss any observed impact on performance or efficiency?

* While the paper highlights the efficiency of Spiking Neural Networks (SNNs), there is no evaluation of the proposed method’s energy consumption. Could the authors provide insights into whether this method might lead to high energy consumption, potentially offsetting the efficiency benefits typically associated with SNNs? A practical energy consumption assessment on hardware platforms such as GPUs, FPGAs, or neuromorphic chips would strengthen this aspect.

* In Figure 1, the paper compares the membrane potential distribution of a spiking VGG-9 model on the CIFAR10-DVS dataset, contrasting the vanilla SNN with the proposed method. The figure suggests that the proposed method stabilizes the membrane potential distribution across timesteps. However, the distinction between the two distributions is not clearly evident, making it difficult to interpret the extent of improvement. Could the authors provide further clarification or additional visualizations to better illustrate this difference?

### Soundness
2

### Presentation
3

### Contribution
2
