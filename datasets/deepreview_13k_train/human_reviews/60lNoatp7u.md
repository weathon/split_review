# NeurRev: Train Better Sparse Neural Network Practically via Neuron Revitalization

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Dynamic Sparse Training (DST) employs a greedy search mechanism to identify an optimal sparse subnetwork by periodically pruning and growing network connections during training. To guarantee effectiveness, DST algorithms rely on high search frequency, which consequently, requires large learning rate and batch size to enforce stable neuron learning. Such settings demand extreme memory consumption, as well as generating significant system overheads that limit the wide deployment of deep learning-based applications on resource-constraint platforms. To reconcile such, we propose $\underline{Neur}$on $\underline{Rev}$italization framework for DST (NeurRev), based on an innovative finding that dormant neurons exist with the presence of weight sparsity, and cannot be revitalized (i.e., activated for learning) even with high sparse mask search frequency. These dormant neurons produce a large quantity of zeros during training, which contribute relatively little to the outputs of succeeding layers or to the final results. Different from most existing DST algorithms that spare no effort designing weight growing criteria, NeurRev focuses on optimizing the long-neglected pruning part, which awakes dormant neurons by pruning and incurs no additional computation costs. As such, NeurRev advances more effective neuron learning, which not only achieves outperforming accuracy in a variety of networks and datasets, but also promoting a low-cost dynamism at system-level. Systematical evaluations on training speed and system overhead are conducted on the mobile devices, where the proposed NeurRev framework consistently outperforms representative state-of-the-arts. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies the issue of "dormant neuron" in the weight-sparse training process, which hinders the performance of DST-trained models. The paper proposes a delta-based criteria to search the dormant neurons and prune them to move them out of the dormant stage, therefore helping the convergence of the sparse model. Results on multiple models and datasets show the proposed method can make DST more stable and improve the final training performance.

### Strengths
1. From the novelty prespective, the paper makes novel observation on the dormant neuron, and provide novel solution of delta-based pruning criteria in DST
2. From the quality prespective, the paper is technically sound. The proposed method is well motivated, and adequate experiments are performed to show the effectiveness of the proposed method
3. The paper is overal clearly written and easy to follow
4. The inclusion of runtime overhead on real hardware further improves the significance of this paper

### Weaknesses
1. A relavent previous work, "Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask" (NeurIPS 2019) may be worth discussing. The paper explored multiple pruning criteria for LTH, including the proposed movement criteria and a similar "magnitude increase" criteria.  It would be beneficial to explicitly compare and contrast the proposed delta-based criteria with the magnitude increase criteria, highlighting the specific differences in how they identify and address dormant neurons, and why the proposed method is superior in this context. A more detailed analysis of the similarities and differences between these approaches would strengthen the paper's contribution. 
2. The paper focus it's discussion on CNN models, exploring models with ReLU activations and some variants. However, transformer-based models with GeLU activation is dominating SOTA architectures. It would be great to also try the proposed method on transformer model. The current evaluation is limited to CNNs, and it is unclear whether the proposed method would generalize well to other architectures, especially those with different activation functions and structural properties. The lack of experiments on transformer models leaves a gap in the evaluation and limits the impact of the paper.

### Questions
See Weakness

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a framework for Dynamic Sparse Training (DST), referred to as NeurRev (Neuron Revitalization). The paper addresses the dormant neuron issue in DST, a problem that has been generally overlooked in existing DST frameworks. By employing weight pruning, NeurRev revitalizes dormant neurons, leading to more effective learning during deep neural network (DNN) training. The paper also highlights the practicality of implementing NeurRev on resource-constrained edge devices due to reduced system overhead. The work is comprehensive and places itself well within the existing literature on sparse training methods, discussing both static and dynamic approaches.

### Strengths
1. This work identifies the interesting dormant neuron problems. 
2. The authors also draw a connection between DST's update frequency and its system overhead. 
3. To address the above observations, this work innovatively uses post-Relu results to prune convolution weights.

### Weaknesses
1. The paper would gain considerable strength from a more comprehensive set of empirical benchmarks. Specifically, the inclusion of real-world scenarios or case studies would offer a more holistic assessment of the method's efficacy and applicability. Furthermore, the method's robustness to different data distributions remains unexplored, leaving these as gaps in the experimental design.
2. The NeurRev is very limited as it seems to only work in Relu-based CNNs. Experiments only show results on the Resnet family. Would it work on more compressed networks such as Mobilenet?

### Questions
1. The Search and Awake process only prunes negative weights, what would happen if there are not enough non-zero negative weights to prune? How do you identify the proportion of dormant neurons to prune?
2. Other activation layers such as leaky-Relu may not set the negative input to zero but also a very small magnitude. According to the NeurRev algorithm, it should probably work the same as the original ones. Are there any limitations on the types of DNN architectures where NeurRev can be applied? Is there any plan to extend NeurRev to other types of networks? More experiments would be helpful to understand its applicability to broader cases. 
3. Could you provide more details on the computational overhead introduced by the NeurRev framework? The evaluation setup is not very clear. Explain more details about the simulation. 
4. What are the computational complexities involved in NeurRev in terms of both time and space? Are there any trade-offs?
5. How robust is NeurRev to different optimization algorithms? Is it specifically designed to work best with certain optimizers?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces NeurRev, a novel pruning method that targets dormant neurons by assessing the change in weights during training. The authors have demonstrated the effectiveness of NeurRev through extensive software results and simulations on edge devices, showcasing its superior performance in comparison to various baselines.

### Strengths
1. The edge device simulations is a strength, as it demonstrates the practical applicability of NeurRev in real-world scenarios.
2. NeurRev is well-motivated and is supported by visualizations of neuron outputs. The experimental results further solidify NeurRev’s promising performance across different benchmarks.

### Weaknesses
My primary concern is about unfair comparison. It seems that results of Table 2 are mainly from the original papers. And I see a rarely-seen learning rate of 1.024 and an optimized cosine learning rate scheduler for the ImageNet. I am worried that the performance boost is due to the optimized training recipe. Could the authors confirm that at least Table 1 is conducted with the same training recipe?

Minor issues:
1. Page 8 Section 3.2: Figure D -> Figure 5.

### Questions
1. Could the authors clarify why the weight change is zero for some weights? I ask the question sice the author mentions that weight decay is used (See appendix A).
2. For Figure 5, how are the update frequency chosen for baselines?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
