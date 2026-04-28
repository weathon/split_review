# Plasticity-Driven Sparsity Training for Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
While the increasing complexity and model size of Deep Reinforcement Learning (DRL) networks promise potential for real-world applications, these same attributes can hinder deployment in scenarios that require efficient, low-latency models. The sparse-to-sparse training paradigm has gained traction in DRL for memory compression as it reduces peak memory usage and per-iteration computation. However, this approach may escalate the overall computational cost throughout the training process. Additionally, we establish a connection between sparsity and the loss of neural plasticity. Our findings indicate that the sparse-to-sparse training paradigm may compromise network plasticity early on due to an initially high degree of sparsity, potentially undermining policy performance. In this study, we present a novel sparse DRL training approach, building upon the naïve dense-to-sparse training method, i.e., iterative magnitude pruning, aimed to enhance network plasticity during sparse training. Our proposed approach, namely Plasticity-Driven Sparsity Training (PlaD), incorporates memory reset mechanisms to improve the consistency of the replay buffer, thereby enhancing network plasticity. Furthermore, it utilizes dynamic weight rescaling to mitigate the training instability that can arise from the interplay between sparse training and memory reset. We assess PlaD on various MuJoCo locomotion tasks. We assess PlaD on various MuJoCo locomotion tasks. Remarkably, it delivers performance on par with the dense model, even at sparsity levels exceeding 90%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents Plasticity-Driven Sparsity Training (PlaD), a new approach in Deep Reinforcement Learning (DRL) that improves the performance of sparse networks by maintaining plasticity through periodic memory resets and dynamic weight rescaling. PlaD enables sparse models to match the performance of dense models even with over 90% sparsity. This work links increased sparsity in training with plasticity loss and demonstrates the effectiveness of PlaD on MuJoCo tasks using a basic pruning algorithm.

### Strengths
- **Novel Method:** The paper introduces Plasticity-Driven Sparsity Training (PlaD), a novel approach that strategically addresses the challenge of sparsity-induced plasticity loss in Deep Reinforcement Learning. By innovatively combining periodic memory resets and dynamic weight rescaling, PlaD counters the negative effects of non-stationarity on network plasticity. This method represents a significant departure from traditional sparsity training techniques, providing a fresh perspective on how to manage the trade-off between model size and learning capability in neural networks.

- **Enhanced Performance and Applicability:** The paper not only establishes PlaD's superiority in maintaining high-performance levels, rivaling dense network models under considerable sparsity constraints but also underscores its broad applicability. The proposed PlaD framework is designed to be easily integrated with a wide array of existing DRL algorithms and pruning methods, making it a versatile tool for researchers and practitioners. The method’s effectiveness has been thoroughly validated across multiple tasks in the MuJoCo environment, indicating its potential for enhancing the efficiency and scalability of DRL applications across diverse and computationally demanding domains.

### Weaknesses
This paper contributes valuable insights and presents experimental results that advance the understanding of sparse-to-sparse training in reinforcement learning. However, the motivations behind this research are not entirely clear to me, and I believe they warrant further clarification.

- **The motivation of the sparse-to-sparse training.**

My expertise lies in the reinforcement learning domain, but my acquaintance with pruning and sparsity is comparatively limited. I comprehend that pruning is theoretically posited to lessen computational demands, yet practically, it might not effectively reduce computational burdens on contemporary hardware due to the intricacies of batching processes. This discrepancy prompts me to question the drive behind adopting sparse-to-sparse training methodologies within reinforcement learning. It is evident that memory conservation during the training of large models like GPT or LLama is advantageous, yet it is less obvious why such a strategy is beneficial or necessary when dealing with the typically smaller models used in reinforcement learning.

Moreover, advocating for sparsity-based training in RL solely on the grounds that it is an established area of investigation does not constitute a convincing argument. A specific, tangible benefit of sparsity in reinforcement learning needs to be identified. Is there a particular aspect of reinforcement learning where sparsity could lead to significant improvements? Could sparsity-based training contribute to advancements in efficiency or performance that are not possible with dense models? These questions need to be addressed to establish a strong motivation for this research direction.

While I recognize that my limited familiarity with sparsity-based training might color my perspective, I encourage the authors to provide a more robust justification for the focus on sparsity in the RL domain. Establishing this foundation is crucial for appreciating the importance and potential impact of the proposed Plasticity-Driven Sparsity Training (PlaD) approach.

- **Concerns to periodic memory reset.**

Regarding the strategy of periodic replay buffer resets to preserve network plasticity, there is a prevailing belief, both theoretical and empirical, that larger memory sizes correlate with enhanced performance. This is attributed to their ability to avert local optima and prevent catastrophic forgetting. Additionally, it is thought that a more extensive memory can mitigate shifts in data distribution during training, thus potentially preventing the loss of plasticity. 

Given these considerations, the efficacy of periodically resetting the replay buffer as a means to improve plasticity or performance remains uncertain. The adoption of this technique appears counterintuitive and warrants a more in-depth justification. How does this method reconcile with the commonly held view that more extensive memory benefits learning? The paper would greatly benefit from a detailed discussion of the trade-offs involved in this approach and its overall impact on the performance of reinforcement learning models.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
# Summary
This paper attempts to claim that sparsity can lead to loss of plasticity and motivates moving away from sparse-to-sparse training and towards dense-to-sparse training. They further motivate this by claiming that sparse-to-sparse training can be computationally ineffient, which undermines the reasons for sparsity in the first place. With this motivaiton, the authors propose to modify RL algorithms to periodically reset their replay buffer and to perform layer normalization while ignoring zero activations that arise from sparsification (referred to as "Dynamic Weight Rescaling"). They claim that their algorithm, PlaD+SAC, is an improvement over the mean performance of other sparse-to-sparse and dense-to-sparse (but lack statistical significance) on 4 mujoco tasks. They further ablate showing that both components contribute to the performance of their algorithm and that the reset mechanism is statistically significant imporovement over a smaller replay buffer in one of the mujoco tasks.
# Decision
I recommend that this paper be rejected, primarily due to confusing motivation, unsubstantiated claims about its connection to plasticity and partially due to the weakness of its empirical results.
There are some interesting ideas in this paper that can and should be developed, such as the connection between sparsity and plasticity. This link between sparsity and plasticity is described as a contribution, but I do not see any connection to plasticity in either the algorithm, nor in the experiments. There are also some hints that the proposed algorithm is benefitting from dynamic weight rescaling and a periodic memory reset in the ablation study. Unfortunately, this alone is not enough because the comparisons against the baselines do not show statistically significant improvement over the baselines.

### Strengths
- The paper has a few ideas that are genuinely interesting, such as the weight shrinkage ratio which provides a lens into the weight dynamics of deep reinforcement learning algorithms. I also thought that the idea of dynamic weight rescaling is an interesting approach to normalization for sparse networks.

- PlaD, the proposed algorithm, does seem to benefit from the two components as shown in the ablation. While I do not agree with the experimental methodology, nor the motivation behind the periodic replay reset, it does seem to have an effect on learning with a sparse network in this isolated finding.

### Weaknesses
 - Overall, the motivation is confusing. It began with claims about computational efficiency, but this is not experimentally explored at all. Then there was some discussion about a connection between plasticity and sparsity, which was not evidenced in reference, nor in the text through experiment or theory.
- There are several erroneous claims surrounding this papers connection to plasticity, which I have detailed below.
- Empirical results are hard to intepret, lacking statistical significance (overlapping error bars), while also overclaiming the benefit of the proposed algorithm against the baseline.

 # Detailed Comments
- Abstract and introduction: Several claims are made but little evidence or context is provided. For example, what exactly about sparse-to-sparse training "may escalate overall computationa cost"? The introduction gives some details, giving references to RLx2 that sparse training is 3x more expensive than dense training. But this is not sufficient evidence of an increase in computational cost, because the sparse models per iteration cost may be more than 3x lower than the dense model. The authors need to clarify whether they are referring to wall-clock time, FLOPs, or some other measure of computational cost, and provide evidence to support their claims.
  Why should sparsity necessarily contribute to less plasticity, there has been no concrete evidence of this connection in the literature beyond very specific forms of (double and triple) sparsity [cite:@zilly21]. Neither the neuron dormancy and primacy bias papers do not provide evidence for this fact. Neuron dormancy, while seemingly related, is about relative mangnitude of activations and provides no evidence that lower magnitude activations can or should be removed.
- Section 1 (Comments on plasticity): It is stated that the replay buffer is the source of non-stationrity. In a certain sense, the replay buffer may contain information from previous distributions and be a contributing factor to non-stationrity but to state that it is the primary source of non-stationarity is over-claiming. I do not think periodically removing such a large source of experience is worth it, when you can instead just use an on-policy learning algorithm. The authors should provide a more rigorous justification for why this is the primary source of non-stationarity, and why an off-policy method with a periodic reset is superior to an on-policy method.
- Section 2.2 (NN Plasiticty): Plasiticty and generalization are two separate problems. The ash and adams paper, for example, has no non-stationarity in the traditional sense, and their results do not demonstrate loss of plasticity. Training error can be minimized, but generalization suffers. Whereas plasiticty is about an inability to minimize the errro. There is a conncetion between the two, but the nature of this connection has not yet been made clear. The authors need to clearly define what they mean by plasticity in the context of their work, and how it relates to generalization and non-stationarity.
- Section 2.2 (Non-stationarity in DRL): There are transient sources of non-stationarity in deep RL that are present even in stationary MDPs. But, explicitly addressing these is not necessary to design successful DRL algorithm. It remains unclear why this is a particular concern in the training of sparse networks in DRL. The authors should provide evidence that non-stationarity is a more significant problem for sparse networks than for dense networks, and that addressing it leads to improved performance.
- Section 4: Equating increased sparsity with increased plasticity is not supported by any previous work, and is not clearly demonstrated in this section. The authors need to provide a clear definition of plasticity and demonstrate how their method increases it, either through empirical results or theoretical analysis.
- Section 4: (Weight Shrinkage Ratio): I do not understand how WSR can "serve as an approximation of the first order gradient of shrinkage / shrinkage speed". First of all, what is the "first-order gradient of shrinkage"? What is shrinkage speed, and what is this speed with respect to? I also do not see how this exposition has anything to do with the study of neural network weights because they are not normally distributed besides at initialization. The authors need to provide a more precise definition of the weight shrinkage ratio, and explain its relationship to the gradient of shrinkage and the speed of shrinkage. They also need to justify why they are using a normal distribution to model the weights, when they are not normally distributed after initialization.
- Section 4: (Activation function concerns): Why is this referred to as the weight shrinkage ratio when it is defined over activations? If this were about weights, I do not see why the relu activation would drive the weights to zero. If all the relu activations saturate at zero, then the weights remain unchanged and the weight shrinkage ratio would be 0. This would only be a concern for a "Activation shrinkage ratio". The authors need to clarify whether the weight shrinkage ratio is defined over weights or activations, and explain why they are using the term "weight shrinkage" when it seems to be related to activations. They also need to address the case where ReLU activations saturate at zero, and how this affects the weight shrinkage ratio.
- Section 4: (Gradient shrinkage ratio): While the details on this are sparse, I also do not see how this has anything to do with plasticity. Gradient shrinkage is a desirable property for achieving a local minimum. The authors need to explain why gradient shrinkage is relevant to plasticity, and how it relates to the weight shrinkage ratio.
- Section 4 (Conclusion and connection to sparsity): This section demonstrated that neural network weights shrink over the course of training, but this does not indicate loss of plasticity and you have provided no evidence for a reduced ability for learning. The authors need to provide evidence that weight shrinkage leads to a loss of plasticity, and that their method can mitigate this loss.
- Section 5 (Periodic Memory Reset): While resetting the neural network may be computationally wasteful, the primacy bias paper demonstrates that there is far more value in the experience stored in the replay buffer than in the neural network being learned. Furthermore, if plasticity is being lost then it is a property of the neural network and it is not clear at all whether that issue can be alleviated by resetting the replay buffer and using more on-policy experience. Furthermore, these methods use a higher replay ratio because their goal is sample efficiency rather than computational efficiency. The authors need to justify why resetting the replay buffer is a good approach to address plasticity loss, and why it is superior to simply using a larger replay buffer or an on-policy method. They also need to address the computational cost of resetting the replay buffer.
- Section 6 (Results, fig 5): I am not able to discern any significant differences from this plot, as many of the error bars are overlapping. The authors need to provide statistically significant results to support their claims.
- Section 6 (Results, fig 6): There is only statistically significant evidence of the reset buffer surpassing the small buffer in one task (hopper-v4). While you study off-policy algorithms (SAC), it would be interesting to show how this compares to an on-policy algorithm. The authors need to provide more evidence that their method is superior to existing approaches, and they should consider comparing their method to an on-policy algorithm.
- Section 7 (Conclusion): No link between loss of plasticity or sparse training was established.
 # Minor Comments
- Section 5 (Dynamic weight rescaling): While this is described by weight rescaling, you are rescaling activations? The benefit is that certian weights that are zerod can lead to zero activations, but it is more accurate to call this somthing like "dynamically sparsified layer normalization"

### Questions
# Detailed Comments
- Abstract and introduction: Several claims are made but little evidence or context is provided. For example, what exactly about sparse-to-sparse training "may escalate overall computationa cost"? The introduction gives some details, giving references to RLx2 that sparse training is 3x more expensive than dense training. But this is not sufficient evidence of an increase in computational cost, because the sparse models per iteration cost may be more than 3x lower than the dense model.
  Why should sparsity necessarily contribute to less plasticity, there has been no concrete evidence of this connection in the literature beyond very specific forms of (double and triple) sparsity [cite:@zilly21]. Neither the neuron dormancy and primacy bias papers do not provide evidence for this fact. Neuron dormancy, while seemingly related, is about relative mangnitude of activations and provides no evidence that lower magnitude activations can or should be removed.
- Section 1 (Comments on plasticity): It is stated that the replay buffer is the source of non-stationrity. In a certain sense, the replay buffer may contain information from previous distributions and be a contributing factor to non-stationrity but to state that it is the primary source of non-stationarity is over-claiming. I do not think periodically removing such a large source of experience is worth it, when you can instead just use an on-policy learning algorithm.
- Section 2.2 (NN Plasiticty): Plasiticty and generalization are two separate problems. The ash and adams paper, for example, has no non-stationarity in the traditional sense, and their results do not demonstrate loss of plasticity. Training error can be minimized, but generalization suffers. Whereas plasiticty is about an inability to minimize the errro. There is a conncetion between the two, but the nature of this connection has not yet been made clear.
- Section 2.2 (Non-stationarity in DRL): There are transient sources of non-stationarity in deep RL that are present even in stationary MDPs. But, explicitly addressing these is not necessary to design successful DRL algorithm. It remains unclear why this is a particular concern in the training of sparse networks in DRL.
- Section 4: Equating increased sparsity with increased plasticity is not supported by any previous work, and is not clearly demonstrated in this section.
- Section 4: (Weight Shrinkage Ratio): I do not understand how WSR can "serve as an approximation of the first order gradient of shrinkage / shrinkage speed". First of all, what is the "first-order gradient of shrinkage"? What is shrinkage speed, and what is this speed with respect to? I also do not see how this exposition has anything to do with the study of neural network weights because they are not normally distributed besides at initialization.
- Section 4: (Activation function concerns): Why is this referred to as the weight shrinkage ratio when it is defined over activations? If this were about weights, I do not see why the relu activation would drive the weights to zero. If all the relu activations saturate at zero, then the weights remain unchanged and the weight shrinkage ratio would be 0. This would only be a concern for a "Activation shrinkage ratio".
- Section 4: (Gradient shrinkage ratio): While the details on this are sparse, I also do not see how this has anything to do with plasticity. Gradient shrinkage is a desirable property for achieving a local minimum.
- Section 4 (Conclusion and connection to sparsity): This section demonstrated that neural network weights shrink over the course of training, but this does not indicate loss of plasticity and you have provided no evidence for a reduced ability for learning.
- Section 5 (Periodic Memory Reset): While resetting the neural network may be computationally wasteful, the primacy bias paper demonstrates that there is far more value in the experience stored in the replay buffer than in the neural network being learned. Furthermore, if plasticity is being lost then it is a property of the neural network and it is not clear at all whether that issue can be alleviated by resetting the replay buffer and using more on-policy experience. Furthermore, these methods use a higher replay ratio because their goal is sample efficiency rather than computational efficiency.
- Section 6 (Results, fig 5): I am not able to discern any significant differences from this plot, as many of the error bars are overlapping.
- Section 6 (Results, fig 6): There is only statistically significant evidence of the reset buffer surpassing the small buffer in one task (hopper-v4). While you study off-policy algorithms (SAC), it would be interesting to show how this compares to an on-policy algorithm.
- Section 7 (Conclusion): No link between loss of plasticity or sparse training was established.
# Minor Comments
- Section 5 (Dynamic weight rescaling): While this is described by weight rescaling, you are rescaling activations? The benefit is that certian weights that are zerod can lead to zero activations, but it is more accurate to call this somthing like "dynamically sparsified layer normalization"

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Plasticity-Driven Sparsity Training (PlaD), a sparse deep RL training method. The method is the standard iterative magnitude training along with memory reset and dynamic weight rescaling. The results show that PlaD outperforms existing sparse training methods.

### Strengths
The paper studies an exciting direction of research. I agree with the general idea that sparsity can be helpful to maintain plasticity.

### Weaknesses
The paper has multiple significant problems:
- **Unclear writing** There are many points in the paper (particularly where mathematical definitions are provided) where terms are used ambiguously. Here are some examples:
    - *Definition of Weight Shrinkage Ratio (WSR)*. Just below the definition of WSR, a line says, "The purpose of WSR is to quantify the ratio of neurons..." But the definition says "proportion of weights ...". Which one is it? The ratio of weights or neurons. In the same definition, the term $h_t^l$ is used, but it is never defined. What is it? It should be clarified whether WSR pertains to the proportion of weights that shrink below a certain threshold or the proportion of neurons whose output is affected by these shrinking weights. Furthermore, the introduction of $h_t^l$ without a proper definition adds to the confusion. Is it the activation of a neuron at a specific layer and time step? If so, this should be explicitly stated and defined within the context of the WSR calculation.
    - *Definition of Dynamic Weight Rescaling (DWR)*. Again, the paper uses a definition $a^l=h^{l-1} \odot \gamma^l$, but $\gamma^l$ is not defined anywhere. My guess is that it is $\Gamma^l$. But if that is the case and $h^{l-1}$ is the output from the previous layer, how can we have an element-wise product of $h^{l-1}$ and $\Gamma^l$? One is a vector, and the other is a matrix. $\Gamma^l$ is the mask over weights, not neurons? The paper needs to clearly define $\gamma^l$ and clarify the operation being performed. If $\gamma^l$ represents the mask $\Gamma^l$, the paper should explain how the element-wise product is applied in the context of a vector ($h^{l-1}$) and a matrix ($\Gamma^l$).
- **Wrong conclusions** The first claim in section 4.2 is that "shrinkage speed increases." But, there is no shrinkage. The weights will only shrink, on average, if the shrinkage ratio is more than 0.5, but the shrinkage ratio is never more than 0.5. So there is no shrinkage; the weights are always getting bigger. The plots show that the weights get larger, not smaller, as training progresses, which is the exact opposite of the main motivation of introducing sparsity. The statement that "shrinkage speed increases" appears to be incorrect based on the provided definition of WSR and the observed behavior in the plots. For weights to shrink on average, the WSR would need to exceed 0.5, indicating that more than half of the weights are decreasing below the defined threshold. However, the paper states that the WSR never surpasses 0.5, implying that weights are, on average, increasing. This contradicts the claim of increasing shrinkage speed and the overall motivation for sparsity presented in the paper.
- **Improper statistical reporting** There are many instances where wrong statistical conclusions are drawn. For instance, Figure 6 says that "Reset buffer distinctly outperforms the Small Buffer strategy in 3 out of 4 tasks, with 2 of these improvements being statistically significant." This is wrong. There is no statistically significant difference between the two algorithms in any of the four cases. We can not conclude that one algorithm is better than the other. I refer the authors to the paper by Patterson et al. (2023) on how to do proper empirical studies in deep RL [1].

### Questions
What is the difference between DWR and layer normalization? They seem exactly the same to me. And is it weight rescaling or pre-activation rescaling? If it is pre-activation rescaling, then the term *weight* rescaling is misleading.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper argued that maintaining plasticity is an important way to maintain high performance under high sparsity. Based on this hypothesis, this paper introduced two mechanisms,  Periodic Memory Reset and Dynamic Weight Rescaling. Periodic Memory Reset aims to preserve the plasticity of neural networks. And DWR is employed to reduce the training instability.

### Strengths
The empirical verification is good and the results show that the method is better than the baseline method.

The paper considers a dense to sparse training that, while not necessarily reducing peak memory cost, a purely sparse inference model is important enough for current reinforcement learning applications.

### Weaknesses
The lack of theoretical analysis of the relationship between plasticity and feasible pruning ratio seriously weakens the motivation of this paper.

The relationship between Weight Shrinkage Ratio proposed in this paper and the plasticity of the neural network is not clear. The increased trend of WSR cannot be totally explained by the loss of plasticity. There are other common reasons, e.g. the high absolute value of initial parameters, weight decay in the optimizer, and implicit regularization in SGD. Causation cannot be inferred simply from correlation.

minor: I think there is a typo, $L$ in $M_s$ is the number of layers of neural networks, $L$ in calculating mean and variance is the number of neurons of $l$-th layer, and they should not be the same.

### Questions
What criteria were chosen in the experiment to determine the distance of the policy when collecting the necessary data into the empty buffer?

I am curious about the necessity to maintain plasticity because if plasticity is low, it means that more neurons are useless and can be removed[2], which is a good thing for creating a sparse network. Increased plasticity may also make pruning more difficult. 

[2] Sokar G, Agarwal R, Castro P S, et al. The dormant neuron phenomenon in deep reinforcement learning[J]. arXiv preprint arXiv:2302.12902, 2023.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
