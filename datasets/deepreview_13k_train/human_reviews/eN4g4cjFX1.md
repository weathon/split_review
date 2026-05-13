# Spatio-Temporal Dependency-Aware Neuron Optimization for Spiking Neural Networks

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
As a biologically inspired computing paradigm, Spiking Neural Networks (SNNs) process information through discrete spike sequences, mimicking the brain's temporal dynamics and energy efficiency. The combination of backpropagation through time (BPTT) and direct input encoding (i.e., feeding decimal data directly into the network) has emerged as the mainstream training approach for SNNs. However, this combination introduces varying temporal dependency requirements across the network’s spatial dimension. These differences are often neglected in existing studies, which typically apply uniform temporal dependency configurations throughout the network. Consequently, this could result in missing key gradients or introducing redundant ones in the temporal dimension, ultimately affecting the network's performance. To address this gap, we propose a novel Spatio-Temporal Dependency-Aware Neuron Optimization (ST-DANO) method for SNNs, which consists of two key components: neuron design and neuron search. Specifically, to overcome the limitations of traditional Leaky Integrate-and-Fire (LIF) neurons in adapting to varying temporal dependencies, we designed two variants, Long-LIF and Short-LIF, which improve the neuron's ability to capture long-term and short-term dependencies, respectively, by dynamic modulation of membrane potential thresholds and time constants. After validating our neuron designs through ablation studies, we developed a layer-wise neuron search strategy that automatically selects the optimal neuron type for each layer to ensure optimal temporal dependency configurations across the network. Extensive experiments on static and neuromorphic datasets demonstrate that ST-DANO can effectively adapt to temporal dependency differences across the spatial dimension in SNNs under various time-step configurations. The resulting architectures surpass state-of-the-art performance, achieving a remarkable 83.90\% accuracy on the DVS-CIFAR-10 dataset—a more than 5\% improvement over the baseline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel Spatio-Temporal Dependency-Aware Neuron Optimization (ST-DANO) method for spiking neural networks (SNNs). The ST-DANO approach aims to address the limitations of uniform temporal dependency configurations in SNNs by adapting to varying temporal dependencies across the network's layers. Specifically, the authors propose two neuron variants, Long-LIF and Short-LIF, which are designed to capture long-term and short-term dependencies, respectively. These neuron types dynamically adjust membrane potential thresholds and time constants, enhancing the model’s adaptability to temporal variations in data. The authors validate their approach through ablation studies and layer-wise neuron selection strategies. Experimental results on static and neuromorphic datasets demonstrate that ST-DANO achieves notable improvements in accuracy, with a reported performance of 83.90% on the DVS-CIFAR-10 dataset, which is more than a 5% improvement over the baseline.

### Strengths
The paper addresses an important issue in SNNs by optimizing neuron behavior based on temporal dependencies, which could enhance the adaptability and performance of SNNs in time-sensitive applications. The introduction of Long-LIF and Short-LIF neurons is a valuable attempt to balance long-term and short-term dependencies in the network. The experimental results, particularly on neuromorphic datasets, demonstrate the potential of the proposed approach, showing notable improvements over baseline models.

### Weaknesses
There exists extensive research on neuron design that dynamically adjusts neuron parameters, such as thresholds and membrane potential constants, to optimize SNN performance. However, the authors did not review or compare their approach against this body of work, nor do they demonstrate clear advantages over these established methods. For example, previous studies have explored biologically inspired dynamic thresholds (Ding et al., 2022), synapse-threshold synergistic learning (Sun et al., 2023), and adaptive threshold plasticity (Zhang et al., 2023), which dynamically adjust neuron properties to improve network adaptability and efficiency:
1.	Ding J, Dong B, Heide F, et al. "Biologically inspired dynamic thresholds for spiking neural networks." Advances in Neural Information Processing Systems, 2022, 35: 6090-6103.
2.	Sun H, Cai W, Yang B, et al. "A synapse-threshold synergistic learning approach for spiking neural networks." IEEE Transactions on Cognitive and Developmental Systems, 2023, 16(2): 544-558.
3.	Zhang A, Shi J, Wu J, et al. "Low latency and sparse computing spiking neural networks with self-driven adaptive threshold plasticity." IEEE Transactions on Neural Networks and Learning Systems, 2023.
4.	Hassan A, Meng J, Seo J S. "Spiking Neural Network with Learnable Threshold for Event-based Classification and Object Detection." 2024 International Joint Conference on Neural Networks (IJCNN), IEEE, 2024: 1-8.
5.	Wei W, Zhang M, Qu H, et al. "Temporal-coded spiking neural networks with dynamic firing threshold: Learning with event-driven backpropagation." Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023: 10552-10562.
6.	Hao Z, Shi X, Pan Z, et al. "LM-HT SNN: Enhancing the Performance of SNN to ANN Counterpart through Learnable Multi-hierarchical Threshold Model." arXiv preprint arXiv:2402.00411, 2024.
7.	Wang S, Cheng T H, Lim M H. "LTMD: learning improvement of spiking neural networks with learnable thresholding neurons and moderate dropout." Advances in Neural Information Processing Systems, 2022, 35: 28350-28362.
8.	Yao X, Li F, Mo Z, et al. "Glif: A unified gated leaky integrate-and-fire neuron for spiking neural networks." Advances in Neural Information Processing Systems, 2022, 35: 32160-32171.
Furthermore, significant advancements have been made in the evolution of neuron and circuit design for SNNs, which allow networks to adaptively evolve neuron properties to suit different tasks and data distributions. Notable studies in this area include:
9.	Shen G, Zhao D, Dong Y, et al. "Brain-inspired neural circuit evolution for spiking neural networks." Proceedings of the National Academy of Sciences, 2023, 120(39): e2218173120.
10.	Che K, Zhou Z, Yuan L, et al. "Spatial-Temporal Search for Spiking Neural Networks." arXiv preprint arXiv:2410.18580, 2024.
11.	Zhang A, Han Y, Niu Y, et al. "Self-evolutionary neuron model for fast-response spiking neural networks." IEEE Transactions on Cognitive and Developmental Systems, 2021, 14(4): 1766-1777.
12.	Shen J, Xu Q, Liu J K, et al. "Esl-snns: An evolutionary structure learning strategy for spiking neural networks." Proceedings of the AAAI Conference on Artificial Intelligence, 2023, 37(1): 86-93.
The proposed method in this paper relies on predefined neuron types (Long-LIF and Short-LIF) and does not explore a generalized strategy that could dynamically balance temporal dependencies within the network. This reliance on fixed neuron types limits the flexibility and adaptability of the method, especially compared to recent approaches that evolve neuron designs or dynamically adjust neuron parameters. The study also lacks comparisons with state-of-the-art methods in Tab.2 and provides limited ablation studies on neuron combinations (such as only LIF and SLIF, LIF and LLIF, SLIF and LLIF) and verified on other encoding paradigms. Additionally, the method has not been validated on complex architectures, such as RNNs or Transformers, nor on large-scale datasets like ImageNet, which limits its generalizability and practical applicability.

### Questions
1.	Could the authors explore a generalized strategy for temporal adaptation that does not rely on predefined neuron types?
2.	How would the proposed ST-DANO method perform with other encoding paradigms?
3.	Could the authors conduct ablation studies to investigate neuron combinations, such as only Long-LIF or only Short-LIF?
4.	Would this approach work effectively on more complex architectures, such as RNNs or Transformers, and on large-scale datasets like ImageNet?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the varying temporal dependency requirements across the spatial dimension of SNNs and identifies the limitations of the LIF neuron in handling these dependencies. Then it designs two types of neurons, LLIF and SLIF, to address this problem. This paper use neuron search to determine where place these neurons. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The whole storyline of this work is complete and reasonable.
2. The conducted experiments have shown the effectiveness of LLIF and SLIF.

### Weaknesses
1. The performance on CIFAR-100 is relatively low.
2. Table 2 is too wide.
3. In Figure 2 a1 and a2, SLIF-4 fails to converge with ResNet-18 on CIFAR-10. Could the authors give explanations on this?
4. The authors say that SLIF captures short-term dependencies. However, in Eq.(9), $\tau[t]$ is decreased when a spike fires. In my opinion, instead of capturing short-term correlations, SLIF overlooks the correlations between different time steps by its mechanism.
5. For LLIF, the authors say ' To achieve stronger long-term dependencies, the contribution from early time steps must have a higher expected proportion in the total gradient compared to standard LIF neurons'. Could the authors give further explanations on this?
6. In table 3, Search Cost is measured in GPU days. Could the authors provide the ratio of search cost to the training time cost?

### Questions
1. In Figure 2 a1 and a2, SLIF-4 fails to converge with ResNet-18 on CIFAR-10. Could the authors give explanations on this?
2. The authors say that SLIF captures short-term dependencies. However, in Eq.(9), $\tau[t]$ is decreased when a spike fires. In my opinion, instead of capturing short-term correlations, SLIF overlooks the correlations between different time steps by its mechanism.
3. For LLIF, the authors say ' To achieve stronger long-term dependencies, the contribution from early time steps must have a higher expected proportion in the total gradient compared to standard LIF neurons'. Could the authors give further explanations on this?
4. In table 3, Search Cost is measured in GPU days. Could the authors provide the ratio of search cost to the training time cost?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method called Spatio-Temporal Dependency-Aware Neuron Optimization (ST-DANO) to adapt neuron behavior to account for different temporal dependencies across network layers. This is achieved by introducing two neuron types, Long-LIF (LLIF) and Short-LIF (SLIF), which a improve the model’s ability to capture long-term and short-term dependencies, respectively, across different network layers. The authors validate the effectiveness of this approach through extensive experiments, demonstrating state-of-the-art performance improvements on both static and neuromorphic datasets​.

### Strengths
The introduction of a novel neuron optimization method that adapts temporal dependencies for SNNs.
##
Significant performance improvements over existing models on both static and neuromorphic datasets.

### Weaknesses
The distinction between LLIF and SLIF is redundant. LLIF alters the long-term dependency capabilities of neurons by adjusting the threshold; consequently, it should also be able to modify the short-term dependency capabilities through threshold adjustment, transforming LLIF into SLIF. Adjusting the membrane potential constant and the threshold is not contradictory. 

The method has not been tested on tasks involving long continuous time-series data (like SMNIST), which would further validate the generalizability of the findings​.

### Questions
Why not combine LLIF and SLIF into one?  I suggest the authors provide experiments or analyses to demonstrate the necessity of distinguishing these two types of neurons.
##
Could you analyse the main differences between your model and other LIF variants in terms of neuron design?
##
How much ST-DANO requires extra training and inference cost, such as number of parameters, or FLOPs, compared to a baseline LIF network on the same tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes two variants of the LIF neuron, Long-LIF and Short-LIF. An ablation study is carried out to check neurons' prefered depth in the SNN. Then a NAS-based method is used to search the neuron type. The proposed methods are validated on various datasets.

### Strengths
This paper is written clearly and easy to be understood.
The experiments and details are abundant.

### Weaknesses
The proposed neurons use tanh activation in neuronal dynamics (Eq.7 and Eq.9), which involves exponential operations and can hardly be implemented in neuromorphic hardware. While previous methods often use different train/inference behaviors to avoid this problem. For example, the attention SNN uses sigmoid in training and Heaviside in inference. (Please refer to `Temporal-wise Attention Spiking Neural Networks for Event Streams Classification`). I suggest that the authors consider similar solutions.


In lines 232-247, the authors try to explain how the increasing of v_th will influence the gradient. This explaination is very weak and ambiguous. It is better to use a quantitative analysis. For example, the authors could show the derivative of Eq.4 with respect to V_th to prove the monotonicity of the gradient.

The design of Eq.6 and Eq.7 for the Long-LIF is discussed clearly that the negative inputs are regarded as the inhibitory signals and will increase the threshold. However, the motivation of Eq.9 for the Short-LIF neuron is not introduced. According to Eq.8, a large V_p will cause a smaller tau. How the short-term dependency is reflected in the neuronal dynamics?

The proposed neuron models focus on long/short-term dependency. In this context, the results of the experiment on memory tasks are more desirable. Previous research  such as `Accurate and efficient time-domain classification with adaptive spiking recurrent neural networks` uses the sequential/pixel classification to evaluate the learning ability of proposed models. I suggest that the authors report these results with comparison to previous neuron models.

### Questions
Please refer to `Weaknesses`.

### Soundness
3

### Presentation
3

### Contribution
2
