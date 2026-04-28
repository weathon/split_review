# Stay Hungry, Keep Learning: Sustainable Plasticity for Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
The integration of Deep Neural Networks (DNNs) in Reinforcement Learning (RL) systems has led to remarkable progress in solving complex tasks but also introduced challenges like primacy bias and dead neurons. Primacy bias skews learning towards early experiences, while dead neurons diminish the network's capacity to acquire new knowledge. Traditional reset mechanisms aimed at addressing these issues often involve maintaining large replay buffers to train new networks or selectively resetting subsets of neurons. However, These approaches either incur substantial computational costs or fail to effectively reset the entire network, resulting in underutilization of network plasticity and reduced learning efficiency. In this work, we introduce the novel concept of neuron regeneration, which combines reset mechanisms with knowledge recovery techniques. We also propose a new framework called Sustainable Backup Propagation (SBP) that effectively maintains plasticity in neural networks through this neuron regeneration process. The SBP framework achieves whole network neuron regeneration through two key procedures: cycle reset and inner distillation. Cycle reset involves a scheduled renewal of neurons, while inner distillation functions as a knowledge recovery mechanism at the neuron level. To validate our framework, we integrate SBP with Proximal Policy Optimization (PPO) and propose a novel distillation function for inner distillation. This integration results in Plastic PPO (P3O), a new algorithm that enables efficient cyclic regeneration of all neurons in the actor network. This approach facilitates neuron regeneration while maintaining policy plasticity and sample efficiency. Extensive experiments demonstrate that, with proper neuron regeneration methods, the SBP framework can effectively maintain plasticity and improve sample efficiency in reinforcement learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper targets plasticity loss in reinforcement learning. Specifically, the widely-used periodic resetting technique was used, which is re-named as "Cycle Reset" in this paper. The authors then adopted a knowledge distillation method to distill knowledge from policy before resetting to alleviate performance degradation from resetting. The authors applied the proposed method to PPO and conducted experiments in the MuJoCo and DMC benchmarks. Overall, the technical contribution of this paper is minor and the experimental setting is not convincing, which will be detailed below.

### Strengths
1. The authors introduce knowledge distillation into the resetting process of RL to alleviate performance drop after each resetting step, which shows good results in their experiments.

### Weaknesses
1. The technical contribution is minor.

1.1. First of all, I see no essential difference between the introduced "Cycle Reset mechanism" and the existing widely-used resetting mechanism [1]. It is inappropriate for the authors to claim this as their own contribution. 

1.2. Secondly, the authors used an established knowledge distillation (KD) method in their distillation module, leaving the contribution of their method to be introducing KD into the resetting procedure. 

2. The major research challenge this paper targets is the performance degradation after resetting. However, it has been well shown in previous works [1,2] that the reset model can quickly recover the lost ability after a few training steps, which makes the "performance degradation" not a significant problem from my point of view. On the other hand, the introduced KD module in this paper also involves additional cost in the overall RL procedure, which is not compared in the paper.

3. The experiment setting which only uses PPO is not convincing. 

3.1. First of all, in [2], it has been revealed that the critic suffers much more than the actor w.r.t. plasticity loss, indicating that value-based or hybrid methods like DQN and SAC are more suited for plasticity loss study than policy-gradient methods like PPO. In Figure 4, PPO+Cycle also brings no benefit compared with PPO, showing that the proposed Cycle Reset does not help plasticity loss in this setting.

3.2. PPO is known for the difficulty in training, requiring potentially careful hyperparameter tuning. The results provided by the authors seem sub-optimal which may be due to this reason. Additionally, the results reported are highly likely to be unfair for previous methods due to a different experiment setting. In comparison, in [1], the performance of SAC / SAC+ReDo for HalfCheetah (MuJoco) can achieve a return over 10000, which is much higher than the reported on in Figure 4. And in [2], their proposed adaptive replay ratio can achieve a return of ~800 in Quadruped Run (DMC) which is also much higher than the reported result in Figure 9. Therefore, I highly recommend the authors to implement their methods on RL backbones used by previous works such as DQN, SAC, or DrQ.

### Questions
1. Could the authors provide comparison on the extra cost introduced by (1) continually training the model after reset to recover the performance and (2) using knowledge distillation?

2. Could the authors provide experiment results on other RL methods other than PPO, such as DQN or SAC for a fair comparison with previous works on plasticity loss in RL?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
A neural network’s ability to learn diminishes over time due to primacy bias and dead neurons. In order to maintain network plasticity, the authors propose a method of neuron regeneration that combines reset mechanisms and knowledge recovery. The approach, Sustainable Back Propagation, resets random neurons and trains the remaining neurons with knowledge/policy distillation from the pre-reset network. This approach is implemented with PPO as P3O and is tested against multiple RL environments.

### Strengths
This paper provides good framing and a clear picture of the issues in neuron plasticity. It provides good theoretical backing with neuron regeneration.

Descriptions are clear and concise, visuals are also clear and aid in understanding.

The approach improves on baseline PPO performance in all tested environments, beats the other methods in most experiments, and greatly surpasses the other methods in several experiments.

### Weaknesses
While you do an ablation of alpha values (for forward vs backward KL), you don’t test alpha=0.5, which represents a common way to turn KL divergence into a symmetrical distance function. You should test alpha=0.5, because if it is optimal, you wouldn’t need to explain the alpha-DKL as much, as symmetrical KL distance is well-established.

While the improved plasticity is clear with the sustained upward trend of the approach’s reward curves, it is unclear how to quantify plasticity. This may be out-of-scope for this paper, but a measure of plasticity could greatly strengthen the claims made. These could include analyzing the slope of the reward curve, the magnitude of the gradient, or perhaps there is an information theoretic angle to plasticity. You analyzed the magnitude of weights, but it is unclear if lower magnitude weights captures meaningful plasticity.

This is a minor gripe, but the explanation of PPO clipping in 2.1. is incorrect. The clip function does not simply limit the magnitude of policy updates. Instead, the clipping essentially sets the gradient to 0 and is used to prevent the model from learning a policy update that would take it further outside rt(theta) +/- epsilon. Using a similar explanation would be more accurate to the mechanics of PPO.

Minor formatting error: the PPO reference paper Schulman et al. 2017 appears twice in the Reference section.

### Questions
How can plasticity be calculated? Are lower magnitude weights always more plastic than higher magnitude weights?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the concept of "neuron regeneration" - a mechanism designed to maintain neural network plasticity while preserving stability in deep reinforcement learning systems. The core contribution is the Sustainable Back Propagation (SBP) framework, which implements neuron regeneration through two complementary mechanisms: cycle reset and inner distillation. The cycle reset component periodically reinitializes selected neurons, while inner distillation ensures the preservation of essential knowledge during the reset process.
The authors integrate SBP with Proximal Policy Optimization (PPO) to create Plastic PPO (P3O), demonstrating the practical application of their framework. The experimental results show that P3O achieves superior performance in both standard single-task environments and non-stationary scenarios, suggesting effective maintenance of plasticity without compromising stability. The empirical evaluation spans multiple environments, including MuJoCo benchmarks and custom non-stationary tasks, providing evidence for the framework's effectiveness in addressing the plasticity-stability trade-off in deep reinforcement learning.

### Strengths
1. The key innovation lies in the inner distillation mechanism, which effectively mitigates the potential negative impacts of reset. This approach represents a promising solution to preserve critical knowledge during the reset process.

2. The paper presents a novel neuron-level reset approach that periodically refreshes different neurons on a cyclical basis, rather than specifically identifying neurons for reset (as in ReDo). While this represents an interesting direction that warrants further investigation (see weaknesses and questions), it introduces a fresh perspective on maintaining network plasticity.

3. The experimental validation is comprehensive, encompassing both standard control tasks and non-stationary scenarios. This breadth of evaluation, particularly the inclusion of environments with changing dynamics, strengthens the empirical support for the proposed method.

4. The use of weight norm and gradient norm as analytical metrics provides valuable insights into network characteristics. These measurements offer a quantitative lens for understanding how the proposed method affects network behavior and learning dynamics.

### Weaknesses
1. The necessity of introducing "neuron regeneration" as a new concept is questionable, as it heavily overlaps with the established plasticity-stability trade-off. The proposed approach essentially describes enhanced plasticity without stability degradation, which could be framed within existing theoretical frameworks. The authors' focus on neuron-level operations doesn't inherently justify a new term; the core idea remains within the scope of managing the plasticity-stability balance, and the specific mechanisms could be described without this new terminology. The emphasis on biological inspiration, while potentially intuitive, doesn't provide a strong technical justification for a new concept, especially when existing frameworks adequately cover the same ground.

2. Several terminological choices appear disconnected from their underlying methods. The title "Stay Hungry, Keep Learning" shows little relation to cycle reset and inner distillation. The framework name "Sustainable Back Propagation (SBP)" is potentially misleading as it doesn't directly involve modifications to backpropagation. Moreover, the inconsistent reference to SBP as "Sustainable Brain Plasticity" in the abstract raises concerns about terminology precision. The change to "Sustainable Backup Propagation" is still problematic, as the term 'backup' is vague and doesn't clearly describe the distillation process. A more descriptive name that reflects the core mechanisms would be beneficial.

3. While neuron-level cyclic reset is a key component, the paper lacks sufficient justification for its superiority over targeted reset approaches. Although ReDo comparison is included, a more comprehensive analysis is needed, particularly with aligned reset frequency and magnitude between methods. This is crucial given the central role of the cyclic reset strategy in the paper's contribution. The current comparison does not adequately address whether the observed performance gains are due to the cyclic nature of the reset or simply the increased frequency of neuron reinitialization. A more controlled experiment is needed to isolate the effect of the cyclic reset strategy.

4. Despite the paper's ambitious claim of achieving "Sustainable Plasticity", the choice of metrics (weight norm and gradient norm) as indirect indicators is less convincing than currently preferred measures in the community, such as fraction of active units or dormant ratio. These more direct plasticity metrics would provide stronger support for the paper's claims. While weight and gradient norms can provide some insights, they do not directly measure the network's ability to adapt to new information, which is the core of plasticity. The absence of direct measures of neuronal activity and their changes over time is a significant limitation.

5. A significant limitation is the framework's validation being restricted to PPO. To demonstrate the effectiveness and generality of SBP, testing on DQN-based methods and other off-policy actor-critic algorithms is essential. This broader validation would substantially strengthen the paper's contribution to the field. The current focus on PPO, while understandable given its on-policy nature, limits the generalizability of the findings. The lack of evaluation on off-policy methods, which have different learning dynamics, leaves open the question of whether the observed benefits are specific to PPO or applicable more broadly.

### Questions
I believe each weakness identified above requires careful consideration and substantive response from the authors. A clear path to acceptance would involve addressing these concerns with concrete solutions and additional empirical evidence where necessary. I am open to further discussion during the rebuttal period and would be willing to revise my assessment positively if the authors can effectively address these issues.

For acceptance, I would particularly emphasize the need for:
- Better justification of the neuron regeneration concept
- More comprehensive comparison with targeted reset approaches
- Additional plasticity metrics
- Broader algorithmic validation

I look forward to the authors' response and am prepared to engage in constructive dialogue during the rebuttal period. A thorough addressing of these concerns would warrant a more favorable evaluation.

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
This paper proposes a straightforward and reasonable method, to improve the performance of reset, which is one of the most reliable methods to mitigate plasticity loss, in Gym-mujoco and DMC.

### Strengths
This paper is well-written and has clear insight.

The method is introduced in a reasonable and theatrical way.

The experimental scenarios are diverse and convincing.

### Weaknesses
1. Regarding the experiments with DMC, I couldn't find how you built the module for encoding image input. Could you describe it in detail?

2. Using the original PPO is rarly in DMC testing. Because it is difficult to learn effective policies, it cannot provide algorithm effectiveness support. Examples are Dog Walk and Hopper Hop in the paper. The learning curve shows that none of the methods learned an effective strategy (the highest score is below 0.1). This only adds to my doubts about P3O's performance.

3. The full paper does not say how many seeds were used for each experiment. In addition, the large difference in the variance shading of each curve in Figure 5 calls into question the fairness of its experimental design (0 variance for PPO+CBP).

4. This paper lacks the comparison of the methods on plasticity evaluation metrics, such as covariance metric [1].

5.  Most of the results on Mujoco in Fig 14 show that the proposed method performs significantly worse than other methods on mainstream plasticity evaluation metrics. The reasons given are confusing and reinforce my suspicions about the mismatch between P3O and motivation. I would advise authors to replace the middle layer activation function with ReLU and re-record the metric and learning curve (generally it doesn't influence much). It's very limiting if your approach works on tanh activation functions.

### Questions
Please see the above suggestions.

### Soundness
2

### Presentation
3

### Contribution
2
