# Temporal Flexibility in Spiking Neural Networks: A Novel Training Method for Enhanced Generalization Across Time Steps

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Spiking Neural Networks (SNNs), models inspired by neural mechanisms in the brain, allow for an energy-efficient implementation on neuromorphic hardware. However, the limitation of current direct training approaches lies in their ability to only optimize parameters for an SNN operating at a specific time step. This leads to the necessity for fine-tuning when generalizing to additional time steps, resulting in considerable computational inefficiency. In this study, we initially examine the feasibility of parameter sharing across structurally identical SNNs operating at different time steps. Subsequently, we propose an innovative training methodology-mixed time step training (MTT) that facilitates the development of a temporal flexible SNN (TFSNN). Throughout the training process, various time steps are arbitrarily assigned to distinct SNN blocks, accompanied by the establishment of novel inter-block communication protocols. Following training, the TFSNN can be simplified to an SNN operating at any chosen fixed time step, eliminating the need for fine-tuning. Experimental results across all primary datasets demonstrate that the TFSNN exhibits robust generalization capabilities surpassing existing training methodologies reliant on a fixed time step. Notably, we achieved a 96.84% accuracy rate on the CIFAR10 dataset, an 81.98% accuracy rate on the CIFAR100 dataset, and a 68.34% accuracy rate on the ImageNet dataset with T = 6.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work endeavors to adapt SNNs to different inference timesteps in a single training run. Mixed time step training (MTT) samples from a series of timestep setups for different stages of SNNs. Temporal transformation modules are inserted between stages to align input/output between neighboring stages. The results show it indeed improves the flexibility when facing variable-length input temporal patterns in both static-image and DVS datasets. The authors also provide an overall estimation of the accuracy when applying a group of different timestep setups.

### Strengths
The MTT performs a wider search along the timestep setting by sampling different. Compared to naive NMT, MTT urges each layer of SNNs to learn feature that is weakly correlated to input length from the previous layer. Such a strong regularization causes an issue in assessing mean and variance within BN layers but is immediately resolved by calibration. Overall, I believe MTT marks a significant step forward in the right direction.

### Weaknesses
However, all datasets used in MTT are directly retrieved or derived from static images (CIFAR10-DVS & CIFAR10, N-Caltech101 & Caltech101). I'm worried that these datasets contain essentially time-invariant features along the time dimension. Even for CIFAR10-DVS or N-Caltech101, only simple movement of static images is recorded using the event cameras. The authors should validate their methods on those datasets with affluent temporal dynamics, like from DVS-Gesture to audio such as GSC (Google SpeechCommands) or SHD (Spiking Heidelberg Dataset) to strengthen their results.

The former concern raises the other issue that, mixing different timesteps is partially empirically based on the finding that the temporal gradients resemble each other when timestep stretches or shrinks, and we expect the training will be stable to some extent since gradients are relatively similar. If the input has invariant length and a different amount of temporal information in essence, will the MTT work as it is now? This is especially concerning given that the core idea of MTT is to allow the network to adapt to different temporal granularities, but the datasets used may not fully reflect the benefits of this.

### Questions
Could the authors demonstrate results on datasets with rich temporal information? This could bring some real challenges to the TFSNN.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes temporal flexible spiking neural networks (TFSNN) and mixed time step training (MTT) method to improve the performance of SNNs under different time steps. The paper first demonstrates the effectiveness of naïve mixture training with different time steps during training, and then, inspired by this, proposes TFSNN with different time steps for each block and MTT training method. Experiments on static and neuromorphic datasets demonstrate superior performance and temporal flexibility of the proposed method, as well as the potential to discover optimal combination of block time steps with energy constraint.

### Strengths
1. The paper proposes a new method to achieve superior experimental results on large-scale datasets. The paper also conducts extensive analysis experiments.

2. The idea of allocating different time steps to different blocks is interesting. It may adaptively allocate energy based on the contributions of different blocks and make a balanced combination.

### Weaknesses
1. The neuromorphic hardware may not support different time steps for different blocks. For the discovered optimal combination of block time steps {3,2,2,3,5,3,6,2}, it may not be deployed for the real energy efficiency of SNNs. There can also be more discussion on the compatibility of the layer-wise adaption of time steps and the thought of (asynchronous) parallelism for neuromorphic computing.

2. Theoretical analysis is limited and there are many informal claims. For example, in Section 4.2, “we believe … balance between SNN expressiveness and gradient accuracy …” --- what is the formal definition of “expressiveness” and “gradient accuracy” and what’s the quantitative measurement of them? And “the new training loss may not converge, leading SNN to jump out of the local minimum point” --- to which loss the “local minimum” refers and why not converging can certainly lead to “jump out of the local minimum point” rather than move surrounding it? Is there any formal theoretical definition and analysis for these claims?

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work aims to extend SNN learning adaptively to various time stamps. The proposed model is based on the discrete LIF neuron model and conduct the multi-step ResNet architectures in serial.

### Strengths
1. This paper provides lots of vivid plots for illustrating the workflow and topology of the proposed models, which is beneficial the understanding of readers.

2. The experimental results seem to be convincing. I have no doubts about the reproducibility of the experimental results.

### Weaknesses
1. This paper is hard to follow due to the poor organization and presence. For instance, it would be helpful to clearly state the purpose of the experiments and analyses in Subsections 4.2 and 4.3.

2. The language used in the paper is quite loose, leading to some confusion. For example, when the paper states that "Increasing the time step (T) enhances the SNN’s expressiveness," it would be beneficial to provide a precise description of "expressiveness." Additionally, the claim that "increasing the time step leads to an increase in the calculated surrogate gradient error" requires further explanation. The treatment of time steps in this work deviates from typical learning methodologies for SNNs, potentially causing confusion for readers, as $T$ here does not represent the length of a spike sequence.

2.1. The authors blur this concept here, making it difficult for readers to distinguish existing work from traditional practices.Clearly, the authors seem to aim to bolster the significance of their paper with this assertion. However, it must be acknowledged that this approach is not in line with standard practices, particularly for SNNs. When employing this method, SNNs may not showcase the capability to outperform conventional neural networks. Instead, their representational capacity may be limited to a subset of RNNs.

3. The title of the paper may be considered somewhat overstated. The claim of "temporal generalization" lacks substantial support throughout the paper. The assertion of theory verification in Section 5.3 requires clarification.

4. The temporal transformation module introduced in the paper bears similarity to existing concepts, such as multi-step RNNs. Providing a clear distinction or novelty in this module would enhance the paper's contribution.

### Questions
As mentioned above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
