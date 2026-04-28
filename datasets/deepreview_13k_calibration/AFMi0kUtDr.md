# PruneFuse: Efficient Data Selection via Weight Pruning and Network Fusion

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Efficient data selection is crucial for enhancing the training efficiency of deep neural networks and minimizing annotation requirements. Traditional methods often face high computational costs, limiting their scalability and practical use. We introduce PruneFuse, a novel strategy that leverages pruned networks for data selection and later fuses them with the original network to optimize training. 
PruneFuse operates in two stages: First, it applies structured pruning to create a smaller pruned network that, due to its structural coherence with the original network, is well-suited for the data selection task. This small network is then trained and selects the most informative samples from the dataset.
Second, the trained pruned network is seamlessly fused with the original network. This integration leverages the insights gained during the training of the pruned network to facilitate the learning process of the fused network while leaving room for the network to discover more robust solutions. 
Extensive experimentation on various datasets demonstrates that PruneFuse significantly reduces computational costs for data selection, achieves better performance than baselines, and accelerates the overall training process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an approach to accelerate the sample selection process in active learning by leveraging network pruning. To further exploit the power of pruned network, several additional modules, such as network fusion and knowledge distillation, are introduced.

### Strengths
- The use of a pruned network as a proxy for selecting informative, unlabeled samples in model training is rational and effective. Although the idea is straightforward, the authors present a well-structured framework incorporating modules such as network fusion for accelerating convergence, knowledge distillation for maintaining performance, and PruneFuse V2 to achieve a favorable accuracy-efficiency balance.
- The paper is well-presented, with clear motivations behind each proposed module and informative visuals, such as Figure 2.

### Weaknesses
 - In Section 4.1, the pruning process appears to involve removing channels with a low L2 norm from a randomly initialized network. If the network is initialized without training, layers with fewer parameters may naturally have lower L2 norms, resulting in the straightforward removal of those layers. Is this approach widely accepted and theoretically sound? Are there existing studies to support this strategy? Furthermore, the L2 norm of a randomly initialized weight may not be a reliable indicator of the importance of a channel, as the magnitude of the weights is not directly correlated to the information content or contribution to the network's learning capacity. This raises concerns about the effectiveness of using such a simple metric for pruning.
- The motivation behind knowledge distillation is unclear, and its effectiveness is not validated experimentally. An ablation study and further discussion on the role of knowledge distillation in the framework are recommended. Specifically, it is unclear why the logits from the pruned model are used as the teacher, given that the pruned model is expected to have lower performance than the original model. This choice needs to be justified, and the impact of using a different teacher model, such as the original unpruned model, should be explored.
- The performance improvements shown in Tables 1 and 2 are marginal in many cases. Although Params and FLOPS are reduced, the method’s complexity in terms of parameters and operations, such as model fusion and knowledge distillation, raises questions. A direct runtime comparison between the proposed method and baseline methods would be insightful. The reported reductions in parameters and FLOPs do not necessarily translate to actual runtime improvements, especially considering the overhead of the fusion and distillation processes. A practical evaluation of the end-to-end runtime is needed to demonstrate the real-world benefits of the proposed approach.
- The comparative methods used are somewhat outdated, with BALD and SVP originating from 2019. More recent methods should be included in the comparison. The field of active learning has seen significant advancements since 2019, and the lack of comparison with state-of-the-art methods makes it difficult to assess the true contribution of the proposed approach. It is important to benchmark against more recent and competitive active learning strategies to demonstrate the novelty and effectiveness of the proposed method.

### Questions
- In Algorithm 1, define \( D_j \) in line 6 before using it in line 7.
- Typographical error in Figure 1: “fusiowith.”
- In line 410, clarify the rationale for the unusual training epoch number (181) used for CIFAR.

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
4

### Summary
This paper proposes PruneFuse to address the issue that traditional methods often face high computational costs. PruneFuse operates in two stages: pruning a network and training the pruned network with knowledge distillation, which will be used to select data. The trained network is fused with the original network and fine-tuned on the selected datasets.

### Strengths
1. The proposed method mitigates the need for continuous large model training prior to data selection.
2. This work introduces a new pipeline, fusing the trained network with the original untrained model.
3. Experiments are conducted on CIFAR-10/100, Tiny-ImageNet, and ImageNet-1k.

### Weaknesses
1. As emphasized in the Abstract, the primary motivation of this work is to address the high computational costs of traditional methods. However, IMHO, neural network pruning typically has high training costs. Meanwhile, the pruned network is also trained for fusion, which increases the training costs. So, I doubt the actual computational costs of the proposed method. Can the proposed method really obtain lower computational costs?
2. As far as I know, many selection methods have relatively low computational costs, such as Moderate [1], CCS[2]. Without reporting and comparing the training costs of each module of the proposed method, I don’t think this contribution is significant.
3. How is the Figure 2 drawer? Did the authors track the gradient direction and values? What is the meaning of different colors? More clarifications are needed.
4. The models experience pruning and then training. What if directly using pretrained models? This can denote the sample scores, as the forward pass can be finished very efficiently.
5. In experiments, authors only compare with several different score functions, while many state-of-the-art methods are not compared. I have doubts about the practical performance of the proposed methods. I recommend discussing and comparing with more advanced existing STOA methods, such as [1-6].
6. I highly recommend that the authors report the training costs of each specific module of the proposed method. Especially the overall training costs to obtain a selected model and obtain the trained model on the selected datasets.
7. Since the model is fused with a pretrained model (which is trained on the whole dataset), the knowledge acquired from the entire dataset is introduced. Therefore, it is unfair to compare directly with another selection method. For a fair comparison, authors are suggested to use the fused models to fine-tune different selected datasets from different baselines. This could significantly enhance the effectiveness of the proposed method.
8. Why do the experiments use some seldomly used architecture, such as ResNet-56, ResNet-14, ResNet-8, and ResNet-20? Authors are suggested to evaluate using more widely used models, such as ResNet-50, ResNet-18, Wide-ResNet, ViT, etc.

### Questions
Please see weakness.

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel strategy, PruneFuse, for efficient data selection in active learning setting. It employs model pruning to reduce the complexity of neural networks while preserving the accuracy. PruneFuse uses a pruned model for data selection and employs it to train the final model through a fusion process which can accelerate convergence and improve the generalization of the final model.

### Strengths
The method is to train a pruned model and fuse it with the original one to get a large mode while saving time, which is useful in continuous large model training.

### Weaknesses
 - I'm a bit confused about Figure 2, which seems somewhat too idealized. Using actual training trajectories would make this figure clearer and more convincing.
- The initialization process seems quite random and seems to be unstable.
- The Baseline in Table 2 doesn't correspond to each other between Tsync = 1 and Tsync = 2 when label budget is 50%, which also unmatch the data in Table 1.
- The motivation for using pruned networks is not very clear, as it seems other teacher-student models with similar structures can achieve comparable effects.
- The parameter counts for PruneFuse in Table 1 do not seem to correspond proportionally to the pruning rates, given that the final model has the same parameter count as the original model. The reported parameter counts appear to be for the pruned selector network, but this is not clearly stated.
- The performance of PruneFuse shown in Table 1 seems unstable and lacks a clear pattern, particularly for smaller datasets. It is unclear why performance fluctuates so much with different pruning rates, and the authors should investigate this further.
- The paper does not explore pruning ratios below 50%, despite the fact that 50% yielded the best results. It is unclear if the performance would continue to improve with lower pruning ratios, and this should be investigated.
- The paper uses static structural pruning, while many dynamic pruning methods are available. The authors should explore these methods and justify why static pruning was chosen.

### Questions
- My understanding is that the final model output by Prunefuse is a model with the same parameter number as the original, so I'm a little confused about the parameter count for Prunefuse in Table 1,  The changes in parameter counts don't correspond proportionally to the pruning rates.
- The performance of Prunefuse shown in Table 1 seems unstable and lacks a clear pattern, have the authors investigated potential reasons for this?
- Also, since Prunefuse achieved good results at p=50%, did the authors try experiments with p=40% or lower?
- I notice that the pruning method used in this paper is static structural pruning. While there are many dynamic pruning methods available nowadays. I wonder if the authors have tried any of these methods?

### Soundness
2

### Presentation
2

### Contribution
2
