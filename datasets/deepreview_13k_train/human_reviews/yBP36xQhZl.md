# Forward Gradient Training of Spiking Neural Networks

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Neuromorphic computing with spiking neural networks (SNNs) is promising for energy-efficient applications. However, the supervised learning of SNNs is challenging considering biological plausibility and neuromorphic hardware compatibility. Most existing successful methods rely on backpropagation (BP) through time and across layers for temporal and spatial credit assignments, which is hard to realize. While some online training methods tackle temporal credit assignment by eligibility traces, it remains an important problem for error signal propagation with proper spatial credit assignment. In this work, we propose a new method, forward gradient training (FGT), for spiking neural networks. FGT only leverages unidirectional forward propagation across layers and direct feedback signals from the top layer to calculate gradients for spatial credit assignment, and we improve the large variance of vanilla forward gradients by momentum feedback connections. FGT avoids layer-by-layer forward-backward calculation of BP with symmetric weights and separate phases, and has more theoretical guarantee and better performance compared with random feedback methods. When combined with online training methods, FGT enables forward and online training. This paves solid paths to on-chip SNN training. Extensive experiments demonstrate the effectiveness and robustness of FGT with similar performance as BP under both fully connected and convolutional networks on static and neuromorphic datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed forward gradient training (FGT) for spiking neural networks to perform biologically plausible and hardware friendly supervised learning. The key objective is how to deliver error signals at the last layer without backpropagating through previous layers. The authors developed forward surrogate gradient to address the non-differentiable functions of SNN and empirically demonstrated promising accuracy compared to BP and DFA. Also, FGT combined with local learning (LL), which optimizes the local loss estimated from local readout layers, shows more improved accuracy. Experiments are performed in various benchmark datasets, such as N-MNIST, DVS-Gesture, CIFAR-10, and CIFAR-100.

### Strengths
- The motivation of the authors is reasonable given many prior works on supervised SNN are still relying on backpropagation. Also, the biological plausibility and hardware compatibility are reasonable motivation to some extent to explore other supervised learning methods. 

- The differences between FGT, backpropagation (BP), and direct feedback alignment (DFA) are well described in the figure and mathematically formulated. The paper is generally well written and provides enough information to understand the proposed approach with detailed appendix. 

- FGT and LL couples the global and local supervised learning in SNN empirically showing good results. Table 3 and Figure 3 comprehensively summarize the performance of FGT and LL in the various datasets and comparison methods.

### Weaknesses
 - The main concern is the novelty of the proposed method. The key contribution will be the section 4.1, where the authors present forward surrogate gradient to make forward gradient applicable to SNN. However, forward gradient, auto differentiation, and local learning are still existing concepts in the prior works.

- Despite the repeated emphasis on hardware compatibility and importance of on-chip training, the relevant experimental results are not presented. Appendix E discusses the training costs, but FGT is still worse than BP.

- The discussion on why BP is biologically implausible is enough, but why FGT and LL are biologically plausible and what are not plausible are not discussed clearly.

### Questions
- The higher training cost of FGT and LL makes sense to some extent as CPU/GPU are not SNN-friendly architectures. However, SNN accelerators are still being developed, and it is difficult say there is a standard architecture for neuromorphic computing. For example, if there are dedicated hardware accelerators for BP-based supervised SNN, BP will be more hardware compatible than FGT.

- It is not easy to make connections to well-known biological or biologically-inspired learning rules such as Hebbian learning or spike-time dependent plasticity (STDP). If the layer-wise error propagation is the main difference with BP, the proposed method is loosely related to biological learning rules.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a FGT method for training SNNs that requires unidirectional FW prop and direct feedback from top layer.

### Strengths
The paper talks about bio-plausibility and hardware compatibility.

There are some theoretical guarantees that the paper talks about with performance better than random feedback.

The authors have shown their method works on simple datasets.

### Weaknesses
While the paper presents promising results, there may be an overstatement of the method's superiority without thorough comparison to a wide range of existing methods. There are substantial works [1-2] and many more that target hardware efficiency that have shown SOTA performance.
[1] Li, Yuhang, et al. "SEENN: Towards Temporal Spiking Early-Exit Neural Networks." arXiv preprint arXiv:2304.01230 (2023).
[2] Kim, Youngeun, et al. "Exploring lottery ticket hypothesis in spiking neural networks." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.
I am not sure if the authors have a quantitative way of suggesting their method's superiority to others in terms of accuracy or efficiency.

Finally, can the authors comment if their work has any limitations in terms of scalability or applicability to different data?

### Questions
See weaknesses above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article presents a novel approach for training Spiking Neural Networks (SNN) known as Forward Gradient Training (FGT). FGT introduces a spatial error signal allocation scheme, providing a solution to distribute errors across the network. By solely relying on forward propagation, FGT enables direct supervision signal transmission across layers, thus avoiding the layer-by-layer error propagation inherent in backpropagation. This methodology proves to be more conducive to online learning on chip architectures compared to traditional methods.

### Strengths
1. The writing in this article is commendable, exhibiting clear and fluid expression. The derivation of mathematical formulas is coherent, enhancing its readability significantly.
2. This article breaks free from the conventional framework of Backpropagation Through Time (BPTT) and boldly explores a new training approach. It introduces a more biologically plausible spatial error propagation method called Forward Gradient with Momentum Feedback Connections.

### Weaknesses
1. Compared to BPTT, FGT incurs larger training costs and is relatively slower on GPUs.
2. The article claims that this method takes a step forward towards online learning on chips, but it does not delve into the implementation of FGT on a chip or the associated storage and computational costs.
3. The current article only validates the effectiveness of FGT on shallow and simpler network structures, showing comparable results to BPTT. However, its performance on deeper and more complex networks remains unexplored. The limited performance on smaller networks suggests that if this method fails to scale well to larger networks, the significance of this work may be limited. For example, the authors could discuss why the proposed framework provides a more feasible implementation of synchronous circuits. Also, there are existing methods that estimate the FLOPS and energy cost of a given NN based on its memory and operation. The authors could provide such comparisons as well. In addition, it is also necessary to provide the comparison with other  training methods on CIFAR-100 as well as ImageNet.

### Questions
1. The current article only validates the effectiveness of FGT on shallow and simpler network structures, showing comparable results to BPTT. However, its performance on deeper and more complex networks remains unexplored. The limited performance on smaller networks suggests that if this method fails to scale well to larger networks, the significance of this work may be limited. For example, the authors could discuss why the proposed framework provides a more feasible implementation of synchronous circuits. Also, there are existing methods that estimate the FLOPS and energy cost of a given NN based on its memory and operation. The authors could provide such comparisons as well. In addition, it is also necessary to provide the comparison with other  training methods on CIFAR-100 as well as ImageNet.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
