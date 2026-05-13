# Towards General-Purpose Model-Free Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Reinforcement learning (RL) promises a framework for near-universal problem-solving. In practice however, RL algorithms are often tailored to specific benchmarks, relying on carefully tuned hyperparameters and algorithmic choices. Recently, powerful model-based RL methods have shown impressive generalist results across benchmarks but come at the cost of increased complexity and slow run times, limiting their broader applicability. In this paper, we attempt to find a unifying model-free deep RL algorithm that can address a diverse class of domains and problem settings. To achieve this, we leverage model-based representations that approximately linearize the value function, taking advantage of the denser task objectives used by model-based RL while avoiding the costs associated with planning or simulated trajectories. We evaluate the resulting algorithm on a variety of common RL benchmarks with a single set of hyperparameters and show a competitive performance against domain-specific and generalist baselines, providing a concrete step towards building general-purpose model-free deep RL algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a generalist, model-free deep reinforcement learning algorithm named MR.Q, which integrates several advanced algorithmic techniques to achieve performance improvements and reduce training costs across multiple benchmark datasets.

### Strengths
1. MR.Q combines various state-of-the-art techniques and demonstrates promising performance gains with a single set of hyperparameters across multiple benchmarks, showing both efficacy and resource efficiency.
2. The paper provides detailed ablation studies, offering insights that may benefit future research in this field.

### Weaknesses
The theoretical motivation presented by the authors is somewhat confusing and challenging to interpret. Please refer to Question 3 for details.

1. What exactly is the objective of the model-based elements mentioned by the authors? It seems that all techniques described are already present in existing model-free reinforcement learning frameworks.
2. The authors only conducted experiments on the Gym, DMC, and Atari benchmarks, which are classic but relatively homogeneous environments. Claiming generality might be overstated given these limited evaluation. For example, the widely accepted generalist algorithm PPO has demonstrated its effectiveness across a broad range of tasks. To establish the generality of this method, additional testing on tasks with some heterogeneity from these benchmarks, such as fine-tuning on large models, would strengthen the claim.
3. Equation (7) seems to be derivable directly from Equation (3). Could you clarify the phrase "from this insight"?
4. The authors describe the linear decomposition of the value function as the motivation, yet the final algorithm design and ablation studies prefer using common nonlinear function approximations. The authors claim that Equations (5-6) are inspired by model-based representations, but related ideas have already appeared in existing model-free algorithms. While this work is innovative and effective from an algorithmic design perspective, the theoretical sections seem somewhat retrofitted to fit the empirical results.

### Questions
1. What exactly is the objective of the model-based elements mentioned by the authors? It seems that all techniques described are already present in existing model-free reinforcement learning frameworks.
2. The authors only conducted experiments on the Gym, DMC, and Atari benchmarks, which are classic but relatively homogeneous environments. Claiming generality might be overstated given these limited evaluation. For example, the widely accepted generalist algorithm PPO has demonstrated its effectiveness across a broad range of tasks. To establish the generality of this method, additional testing on tasks with some heterogeneity from these benchmarks, such as fine-tuning on large models, would strengthen the claim.
3. Equation (7) seems to be derivable directly from Equation (3). Could you clarify the phrase "from this insight"?
4. The authors describe the linear decomposition of the value function as the motivation, yet the final algorithm design and ablation studies prefer using common nonlinear function approximations. The authors claim that Equations (5-6) are inspired by model-based representations, but related ideas have already appeared in existing model-free algorithms. While this work is innovative and effective from an algorithmic design perspective, the theoretical sections seem somewhat retrofitted to fit the empirical results.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a model-free deep RL algorithm, designed to achieve consistently high performance across RL settings. The method (MR.Q) is based on the widely accepted principle that self-supervision (world models) can provide an effective state encoding for policy and value learning. Additional components are added to ensure hyperparameter robustness and the method is evaluated with a single set of hyperparameters in each setting. A theoretical analysis is provided, suggesting an approximately linear relationship between model-based and value-based representations. MR.Q is evaluated on MuJoCo, DMC, and Atari benchmarks, with comparisons to a handful of algorithms and an extensive number of ablations.

As detailed below, I was unable to find some key details regarding the author's experiments, so my current score is provisional. I am highly open to raising or lowering my score following discussion with the authors.

### Strengths
* The paper is very well presented and has a clear structure.
* The core approach - using world model representations to support policy learning - is sound and well-motivated in prior literature.
* Strong efforts are made to make the model hyperparameter-insensitive, which is particularly valuable in RL where hyperparameter tuning is often ignored or exploited to give the appearance of improved performance.
* The evaluation is extensive in the number of benchmarks and ablations. A consistent set of hyperparameters is used by the method, strengthening the claim of robustness.

### Weaknesses
## Hyperparameters
One of the primary aims of the paper is hyperparameter robustness, with multiple components being designed to improve robustness and a single set of hyperparameters being used to evaluate MR.Q. However, aiming for robustness does not allow hyperparameters to be ignored in evaluation. In fact, *more* attention should be paid to hyperparameters, to demonstrate that MR.Q is less sensitive hyperparameters than baseline methods, or performs better when all algorithms are constrained to a single hyperparameter setting.

Unfortunately, the paper does the opposite and provides no detail (that I could find) regarding the hyperparameter settings of the baseline algorithms, nor how or if they were tuned. This is a critical weakness of the paper, as the possibility of untuned baselines undermines the claimed performance improvements.

One example of this is that DreamerV3 outperforms MR.Q on only 1/4 benchmarks (Atari). Notably, Atari is also the only benchmark for which the results come from the reference work. For the remaining 3 benchmarks, the authors run DreamerV3 themselves. This does not imply that the authors failed to tune DreamerV3 or that the comparison was unfair, however, given the lack of detail regarding their tuning procedure or the hyperparameter sensitivity of the methods, the result is seriously undermined.

Another example is that the paper seems to maintain model sizes from the original implementations of each algorithm. However, the size of the model is not defined by the algorithm, so it would be much more convincing to normalize the parameter count between algorithms and show that MR.Q achieves superior performance at the *same* size, or has a better scaling curve.

## Baselines
Some key algorithms are missing, most notably PPO. It is not expected that the authors compare to every popular RL algorithm, but PPO is undoubtedly the closest thing to a "general-purpose" RL algorithm in current literature.* A number of recent methods have also claimed to serve as "general-purpose" RL algorithms (e.g. PQN, Gallici et al., 2025). These would make for valuable comparisons in future work but are not required for acceptance.

*As of 31st Oct, PPO has 5460 citations in 2024, compared to 269 (Dreamer v3), 32 (TD7), 39 (TD-MPC2), 1531 (TD3). Not a perfect proxy for the methods' generality, but certainly indicative.

## Ablation study
The ablation study fails to provide the statistical significance of the results and lacks analysis. Furthermore, the "reverting to theory" ablations are highly unsurprising so provide little contribution, and many of the remaining ablations show minimal performance gains. Some of these components are designed to handle edge cases (e.g. reward scaling handling environments without normalized reward), meaning the benefit is unclear from mean performance across a suite, but may be apparent by examining the performance distribution. For these in particular, further analysis of the results would strengthen the contribution of each component.

## Theory
The theory is based on highly constrained linear assumptions and provides little justification for the proposed method. The idea of using world model representations for policy learning is intuitive and can be explained much more clearly without sacrificing correctness. I understand there is a pressure on authors to provide "theoretical rigour", but in this case it adds little to the paper and would be better replaced with an extended analysis of the empirical results.

### Questions
Were the baselines tuned, and how was this done if so?

Do you have evidence that A) MR.Q is less hyperparameter sensitive than baselines, or B) the best single set of hyperparameters for MR.Q achieves higher performance than the equivalent for a baseline?

As far as I can tell, the proposed symexp loss will have higher resolution at higher reward values. This is counterintuitive, as one would expect precision to increase for values near 0. Can the authors explain this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes to leverage model-based representations for model-free reinforcement learning. Model-based approaches are only used for learning the representation, but no planning or simulation is employed. The authors integrate model-based representations in the proposed method MR.Q. They evaluate MR.Q on 3 benchmarks (Gym, DMC, Atari) and find that it leads to faster learning speed and improved performance compared to competitors, albeit not consistently across domains.

### Strengths
The authors propose an algorithm named, MR.Q that performs well across domains. They conduct well-selected ablations on MR.Q to highlight what effect their design decisions have on the algorithm. The empirical results are broad and seem sound. Generally, a useful contribution to the field.

### Weaknesses
The authors argue that the benefits of model-based approaches may stem from their learned representations, rather than from their planning abilities. While this may be true to some degree, we assume that this is highly specific to the domains they conduct experiments on. In particular, Gym and DMC environments and most Atari games do not require much planning to be solved. However, we know that in other domains planning plays a critical role. Therefore, we believe it is important for the authors to clarify that the benefits of model-based representations alone depend on the domain at hand, to avoid any misconceptions.

The authors refer to their method as “generalist”, which is a term commonly used for multi-task agents in the literature. However, all conducted experiments are in single task settings. Instead, “generalist” in the context of this paper refers to being robust to different environments (reward scales, dynamics, with the same hyperparameters). We therefore strongly encourage the authors to rethink this terminology to avoid confusions.

The results for Dreamerv3 are surprisingly bad on continuous control tasks. This suggests that this baseline is purely tuned for these environments. 

The proposed approach comes with a large list of hyperparameters, which may limits its practical applicability.

### Questions
- Could you clarify your use of “generalist”? 
- There seems to be a clear trend of Dreamerv3 underperforming on continuous control environments. Any intuitions why? 
- How do the Training FPS of MRQ. in Figure 1 compare to other non-planning baselines on DMC-Visual (TD7) and Atari (Rainbow, DQN)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MR.Q, a model-free RL algorithm that uses model-based representations to generalize across a variety of domains with the same set of hyper-parameters. MR.Q leverages the fact that the fixed-point between linear reconstructions of dynamics and value are the same. MR.Q relaxes the theory to show that non-linear value functions using this learned representation improve performance. The algorithm trains a policy by using a deterministic policy gradient similar to DDPG. To prevent trivial solutions, the dynamics reconstruction loss uses the next state as a target, as opposed to the next state-action encoding. A number of other tricks are used, including a two-hot representation of reward, target policy noise from TD3, pre-activation regularization, Huber loss, and scaling by the average reward. These components are tested in a series of ablations, and evaluations are conducted over Gym, DMC, and Atari, comparing to DreamerV3, TD-MPC2, TD7, Rainbow, and DQN.

### Strengths
This paper is well-written and address the import question of robustness of RL algorithms across various domains. The paper is theoretically motivated, and performs many ablations. The proposed algorithm is clear and if the evaluations hold, could prove to be of great interest to the community.

### Weaknesses
The primary weaknesses are evaluation and novelty. A few points are listed here, and some clarifying questions in the questions section:
1) While it is not possible to evaluate every benchmark, the Minecraft benchmark from Dreamer, which I believe tests long-term credit assignment, is notably missing. It could be great to see how this method holds up when reward is sparse, exploration is difficult, and policy gradient variance may be high. Procgen is also missing, which may be one of the harder domains in the Dreamer paper. The lack of these environments makes it difficult to assess the algorithm's robustness in challenging scenarios beyond standard benchmarks.
2) The model-based representations are not particularly novel. For example, consider VariBAD (Zintgraf et al., 2020), which reconstructs reward and dynamics functions. The paper does not sufficiently differentiate its approach from existing methods that use similar reconstruction techniques, raising concerns about the incremental contribution.
3) One piece of novelty is that the reconstruction of reward and transitions use a linear function of the same latent encoding. However, experiments show that a non-linear value reconstruction is useful, and it may be the same for the model-based objectives as well. Are there experiments testing this? The choice of a linear model for dynamics and reward reconstruction, while computationally efficient, may limit the model's capacity to capture complex relationships, especially since the value function benefits from non-linearity. This raises questions about the optimality of this design choice.
4) It would be great to see comparisons to other baselines here that use contrastive learning as well, e.g., Neural Predictive Belief Representations (Guo et al., 2018). The absence of comparisons to contrastive learning methods makes it difficult to understand the specific advantages of the proposed approach over other representation learning techniques.
5) I am also concerned that the method cannot handle general POMDPs. Is it true that only the state and action are passed the policy and not history? If you are only using a latent that reconstructs the reward and dynamics, this statistic must condition on history, and is not general enough for any POMDP, but only a distribution of MDPs, as in meta-RL (Zintgraf et al., 2020). The method's reliance on a Markovian assumption limits its applicability to environments with partial observability, which is a significant limitation in real-world scenarios.
6) It would be great to see a comparison to your method, but with additional synthetic trajectories simulated by your learned model. Without this experiment, it is hard to know if the compromise between model-based RL and model-free RL is the right trade-off. The lack of experiments using the learned model for planning or data augmentation makes it difficult to assess the true value of the learned dynamics model.

### Questions
Some questions:
1) Is there a reason that TD-MPC2 and TD7 were chosen over Truncated Quantile Critics (TQC) and Randomized Ensembled Double Q-Learning (REDQ)? Are there any papers showing your baselines to be superior?
2) Are there any experiments evaluating whether a non-linear reward and transition reconstruction might be superior?
3) Have you evaluated you algorithm with sequence models than can handle POMDPs?
4) Have you compared to other self-supervised model-based algorithms (esp. those using contrastive learning or those designed for POMDPs?)
5) You mention that the number of frames is not equal to the number of time-steps due to sticky actions. If you plot the number of frames on the x-axis, are the results still the same? Does your algorithm require more frames than others?
6) It looks like the curves for Atari are not converged. Could you run longer?

### Soundness
3

### Presentation
4

### Contribution
3
