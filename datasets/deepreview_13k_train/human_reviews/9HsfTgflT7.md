# Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness

- Decision: Accept
- Scores: 5, 6, 6, 8, 6

## Abstract
Spiking Neural Networks (SNNs), models inspired by neural mechanisms in the brain, allow for energy-efficient implementation on neuromorphic hardware. However, SNNs trained with current direct training approaches are constrained to a specific time step. This "temporal inflexibility" 1) hinders SNNs' deployment on time-step-free fully event-driven chips and 2) prevents energy-performance balance based on dynamic inference time steps. In this study, we first explore the feasibility of training SNNs that generalize across different time steps. We then introduce Mixed Time-step Training (MTT), a novel method that improves the temporal flexibility of SNNs, making SNNs adaptive to diverse temporal structures. During each iteration of MTT, random time steps are assigned to different SNN stages, with spikes transmitted between stages via communication modules. After training, the weights are deployed and evaluated on both time-stepped and fully event-driven platforms. Experimental results show that models trained by MTT gain remarkable temporal flexibility, friendliness for both event-driven and clock-driven deployment (nearly lossless on N-MNIST and 10.1\% higher than standard methods on CIFAR10-DVS), enhanced network generalization, and near SOTA performance. To the best of our knowledge, this is the first work to report the results of large-scale SNN deployment on fully event-driven scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a training method, Mixed Time-step Training (MTT), aimed at improving the temporal flexibility of Spiking Neural Networks (SNNs) for more versatile deployment. The training method allows SNNs to adapt across diverse time steps by assigning random time steps to different stages of the network in each iteration. After training, TFSNNs are deployed and evaluated on both time-step-based and event-driven platforms. The authors compare their method on static and DVS datasets with ANN-SNN conversion methods (Jiang et al.2023) and SEENN (Li et al., 2023), emphasize its generalization to different time steps.

### Strengths
1.	The paper introduces a novel training method to address the side effects of temporal 
inflexibility caused by the prevailing training paradigms.
2.	The paper conducts intensive experiments on GPU, neuromorphic chips, and event-
driven simulator to testify to its effectiveness.

### Weaknesses
1. The proposed method aims to enhance the model's temporal flexibility through mixture training. However, the authors do not provide a clear analysis of the training complexity or computational costs involved. Table 9 highlights the relationship between the sampling frequency and training epochs, yet further details are needed to elucidate these aspects comprehensively. Specifically, the analysis lacks a breakdown of the computational overhead introduced by the mixed time-step training, such as the increased memory usage or the impact on convergence speed compared to standard direct training (SDT). A more detailed analysis should quantify the additional computational cost incurred by sampling multiple time steps per iteration, including the forward and backward passes for each sampled time step, and how this scales with the number of sampled time steps and network size.
2. Some performance improvements reported by the authors appear less substantial upon closer examination. For example, in Table 4, the addition of MTT has a very limited effect on improving overall performance. Similarly, in the generalization comparison involving Gaussian noise-injected inputs (Figure 5), while the accuracy of the MTT method consistently exceeds that of SDT, the margin is minimal compared to the overall drop in accuracy as noise intensity increases. These observations make it challenging to substantiate the claim that the model’s generalization is significantly enhanced. The performance differences, particularly in Table 4, are marginal, raising questions about the practical significance of MTT in scenarios where the baseline performance is already high. Furthermore, the noise generalization experiments show that while MTT offers a slight advantage, the overall robustness to noise is still limited, suggesting that the method's impact on generalization is not as substantial as claimed.


### Questions
Please refer to the weaknesses section. Additionally, there are two more questions:
1. The authors suggest that their models can infer across various time steps without additional fine-tuning. However, whether flexibility across all time steps is necessary, especially outside of event-driven scenarios, remains an open question. Given the potential complexity of the proposed training approach (see Weakness 1 for details), it may be more efficient and focused to fine-tune the model for specific possible platforms rather than attempting universal temporal flexibility.
2.The authors compare their method to the current state-of-the-art (SOTA) in ANN-to-SNN conversion (Table 3) and report improved performance when T is low. However, performance declines slightly as T increases. Likewise, in Table 4, although naïve mixture training demonstrates some advantage over standard direct training at smaller T values, this benefit diminishes as T approaches 5 or 6. This raises an question: given that SNNs have limited capacity to capture temporal dynamics across time steps when T is very small, is this improvement practically significant?

### Soundness
3

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
3

### Summary
The paper proposes the Mixed Time - step Training (MTT) method, which is utilized to train Spiking Neural Networks, thereby achieving generalization across distinct time steps. This method empowers SNNs to accommodate diverse temporal structures. Furthermore, the paper conducts validation experiments to confirm the effectiveness of MTT. The method devises specific loss, a temporal transformation module, and network partitioning to fulfill the above-mentioned objective.

### Strengths
The paper presents a promising SNN training approach, namely MTT, which attains remarkable outcomes in terms of temporal adaptability and model performance, possessing definite innovation and practical value. The co-training method involving multiple time steps is both rational and effective. The experiments are comprehensive, having been conducted on diverse datasets, and there are also tests on event - driven neuromorphic systems.

### Weaknesses
1.The writing in this paper has room for improvement. The authors ought to place greater emphasis on the key points throughout the article. For instance, concerning the temporal flexibility across time steps, the experiment should stress that different time steps perform well in general. Avoid delving too deeply into which particular time step works well, as this may obscure the aim of the work. The authors should focus on presenting the overall performance trend across various time steps instead of detailing the results for each separate time step. This would enhance the emphasis on the key point of generalization across time steps.

2. Some additional details regarding the experiment and the method are required. Specifically, an explanation must be given as to why the time steps in Table 4 are represented as decimals. Moreover, the meanings of the symbols used should be clearly elucidated.

### Questions
Could you provide a clear definition of V(t) when it is first introduced in section 3.1, and explain its significance in the context of the neuron model？

### Soundness
3

### Presentation
2

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
This paper identifies the temporal flexibility problem for spiking neural networks (SNNs) that is important for SNNs’ deployment on time-step-free fully event-driven chips, and proposes a novel mixed time-step training method to alleviate the problem under current direct training approaches. For evaluation, the trained models are tested under both time-step-based and fully event-driven settings, where the latter includes both the Speck chip and a developed simulator. Experiments show promising performance for temporal flexibility, robustness, deployment to the fully event-driven setting, and commonly used static and neuromorphic datasets.

### Strengths
1. This paper considers an important problem in bridging algorithms of SNNs and the real deployment on fully event-driven neuromorphic hardware. It is significant for real applications.

2. Experiments are comprehensive, covering not only the commonly adopted GPU simulation settings but also real chips or a similar event-driven simulator. Various datasets including static images, neuromorphic images, and audio, have been considered to verify the good performance of the proposed method.

3. Results show that the proposed method can achieve near SOTA performance and has much better performance when deployed under the fully event-driven setting.

### Weaknesses
1. The paper lacks sufficient details for the considered fully event-driven setting. For example, what are the precise specifications of the Speck chip, such as the number of neurons, supported network architectures, and communication protocols? Similarly, the developed simulator needs more clarification regarding its implementation of asynchronous operations, how it handles event propagation, and its validation against real hardware. The description of input and output formulations should specify the encoding scheme used for events (e.g., Address-Event Representation) and how the network interprets these events. Furthermore, the influence of asynchronization on network behavior, particularly concerning the order of event processing and its potential impact on performance, is not sufficiently discussed. The claim of “large-scale SNNs on fully event-driven scenarios” is not fully supported by the experiments, as only N-MNIST is verified on the real chip, and the other experiments rely on the simulator, whose fidelity to real-world asynchronous hardware is not fully established.

2. For the presentation, there are some not fully discussed logical gaps.

First, there is a gap between the identified temporal inflexibility problem and deployment on fully event-driven chips. The paper frames temporal inflexibility within a time-step-based setting, yet the target deployment is time-step-free. The connection between the flexibility observed under synchronized conditions and its benefits in asynchronous settings needs more explanation. Specifically, it is unclear how the proposed method addresses the challenges of asynchronization, such as variable delays and non-deterministic event arrival times. The paper should clarify why training with varied time steps in a synchronous environment translates to robustness against the inherent asynchrony of event-driven hardware.

Second, the motivation for transitioning from NMT to MTT is not clearly articulated. The paper should explicitly state the limitations of NMT that MTT aims to address, such as the computational cost or the inability to explore a wider range of temporal structures.

Third, the definition of temporal flexibility lacks rigor. The paper acknowledges that SNNs trained with a specific T can operate at different time steps, albeit with performance degradation. The concept of flexibility is presented as a quantitative improvement rather than a qualitative distinction. A more precise definition is needed, perhaps based on the degree of performance variation across different temporal structures. The paper should clarify what constitutes a flexible model versus an inflexible one, beyond a simple performance comparison, and why the proposed method can be said to “exhibit temporal flexibility” rather than simply reduce performance degradation.

### Questions
To alleviate the influence of time steps, will it be better to consider the combination with some online-through-time training methods with instantaneous losses [1,2] rather than backpropagation through time, since the former can naturally consider information from different time steps and may be suitable for on-chip training to better adapt to real settings?

[1] Online training through time for spiking neural networks. NeurIPS, 2022.

[2] A solution to the learning dilemma for recurrent networks of spiking neurons. Nature Communications, 2020.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work first addresses the limitations of using fixed time steps in conventional SNN training, which lead to low generalization capability and performance degradation during practical deployment. Additionally, it highlights the challenges in dynamically balancing energy-performance trade-offs under this constraint. Starting from the Naive Mixture Training, this manuscript incrementally develops a framework that incorporates hybrid time-step and temporal flexibility training methods. By applying a strategic up/down rounding technique, the authors group the stages of networks like VGG and ResNet into multiple dynamic time-step segments for training. Notably, the paper presents results on neuromorphic hardware (Speck V2) and simulation results on asynchronous platforms, offering fresh insights into the practical advantages of dynamic time-step strategies.
The manuscript is logically clear and coherent, with the methodology presented in a gradual and systematic manner.
However, I still have a few questions and suggestions for modifications (and additions).

### Strengths
1. The manuscript is well-structured, logically coherent, and clearly articulated.

2. The figures are well-designed.

3. The defined spike difference has practical significance, offering a valuable metric for optimizing GPU training and on-chip deployment.

4. Experimental results demonstrate that the proposed MTT-enabled TFSNN outperforms the baseline in accuracy and exhibits stronger generalization capabilities.

### Weaknesses
1. In line 234 of the manuscript, the time step range is described as "$T_{max}$ to $G^{T_{max}}$" Should  $G^{T_{max}}$ be corrected to ${T_{max}}^{G}$ here?

2. What is the difference between $T=a_i$ and $T=t_i$ in Figure 1? Are they referring to different sample sets? If so, please clarify this in the caption.

3. The time step serves as a search space, which has a certain relationship with Neural Architecture Search (NAS). Please provide some discussion on the connection between the two.

4. Although it is understood that the focus of this paper is on reducing the gap between training and deployment, the sampling of samples and the grouped calculation of loss evidently increase training overhead. Please provide some discussion on this in the appendix.

### Questions
1. To my knowledge, the highest-performing architecture in the SNN field is the Spiking Transformer [1-5]. Please discuss whether the proposed method can be effectively applied to the Spiking Transformer. If feasible, please provide some preliminary experimental results.

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

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduces a new method, MTT, for training spiking neural networks (SNNs) that perform well across different numbers of timesteps during inference. These SNNs are referred to as Temporally Flexible SNNs (TFSNNs). The proposed method divides an SNN model into multiple stages, assigns each stage a random number of timesteps, and conducts multiple forward passes on the same data batch. The outputs are aggregated into a single loss function, and backpropagation through time (BPTT) is used to update the weights. Experimental results demonstrate that this approach enables the SNN model to perform consistently across varying timesteps during inference. Additionally, models trained using this method show enhanced generalization and robustness to noise, as well as high accuracy across multiple static and dynamic image classification datasets.

### Strengths
The manuscript identifies an interesting issue with direct training methods for SNNs: their limited performance when performing inference under a different timestep configuration than the one used during training. It proposes a solution that allows models to perform well across a range of timesteps, enhancing their flexibility and robustness. The models trained under this approach demonstrate improved generalization and competitive accuracy compared to SOTA direct training methods. Furthermore, the manuscript is overall well-written, with a clear and accessible description of the proposed method.

### Weaknesses
The problem definition and the proposed method's alignment with it remain somewhat unclear. The manuscript introduces the problem of "temporal inflexibility" in standard direct training methods, suggesting that this limitation could affect SNN deployment on fully event-driven hardware. However, the manuscript's focus is primarily on synchronous discrete models trained on static image datasets, with only a minor experiment (Table 5) dedicated to event-driven models, which lacks sufficient detail. Thus, the manuscript does not fully address the implications of "temporal inflexibility" for event-driven hardware deployment, instead centering on the need for inference performance consistency across multiple timesteps, a goal that may not directly relate to event-driven applications. The core issue is that the paper does not clearly distinguish between the need for temporal flexibility in synchronous, time-stepped SNNs and the requirements of truly asynchronous, event-driven hardware. The experiments are predominantly focused on the former, while the motivation seems to lean towards the latter, creating a disconnect.

If the objective is to facilitate SNN deployment on event-driven hardware, the manuscript should clarify the differences between models described in Section 3.1 and fully event-driven models. For instance, Section 5.1 mentions that SPECK removes time-step-wise operations like clocked bias addition. How does the LIF model change after removing such operations? It is unclear how the standard LIF model, with its time-dependent membrane potential decay, translates to a fully event-driven model where updates are only triggered by incoming spikes. Conversely, if the goal is multi-timestep inference, further explanation is needed to justify its relevance for static image classification tasks. In these cases, where temporal information is absent, the optimal approach would be to achieve accurate inference with the minimum number of timesteps (ideally $T=1$, as in ANNs). The paper does not adequately explain why varying T is beneficial for static image classification, especially when the goal should be to minimize latency and computational cost.

The experimental setup and results presentation require further clarification. For example, in Section 5.1, "Temporal Flexibility Across Time Steps", Table 2 is not referenced in the text, making it unclear what these results indicate. Additionally, in Table 3, which compares the proposed method with SOTA ANN-SNN methods, the settings for the ANN-SNN methods are unclear, was the conversion applied once for a single $T$ value, then tested across various $ T $ values, or was the conversion performed individually for each $ T $ value in Table 3? Similar issues with experimental descriptions and discussions are present in Sections 5.1 and 5.3. The lack of clarity in experimental details makes it difficult to assess the validity and reproducibility of the results. For instance, the specific parameters used for the ANN-SNN conversion, such as the time constant for the LIF neurons, are not mentioned, which are crucial for understanding the performance of these methods.

### Questions
- What specific problem is the manuscript addressing, deployment on event-driven hardware or inference consistency across multiple timesteps? How does the proposed method align with this problem?
- What are the differences between the LIF models in Section 3.1 and those used in event-driven simulations?
- How does the method generalize to values of  $T $ outside the range used during training ($ [T_{\text{min}}, T_{\text{max}}] $) on event-based datasets?
- How was Figure 9 generated?
- What is the distinction between SDT and SDT* in Table 1?
- Could you clarify the "specific application scenarios" referenced in line 208?

### Soundness
2

### Presentation
2

### Contribution
3
