# Overcoming Slow Decision Frequencies in Continuous Control: Model-Based Sequence Reinforcement Learning for Model-Free Control

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Reinforcement learning (RL) is rapidly reaching and surpassing human-level control capabilities. However, state-of-the-art RL algorithms often require timesteps and reaction times significantly faster than human capabilities, which is impractical in real-world settings and typically necessitates specialized hardware. Such speeds are difficult to achieve in the real world and often requires specialized hardware. We introduce Sequence Reinforcement Learning (SRL), an RL algorithm designed to produce a sequence of actions for a given input state, enabling effective control at lower decision frequencies. SRL addresses the challenges of learning action sequences by employing both a model and an actor-critic architecture operating at different temporal scales. We propose a "temporal recall" mechanism, where the critic uses the model to estimate intermediate states between primitive actions, providing a learning signal for each individual action within the sequence. Once training is complete, the actor can generate action sequences independently of the model, achieving model-free control at a slower frequency. We evaluate SRL on a suite of continuous control tasks, demonstrating that it achieves performance comparable to state-of-the-art algorithms while significantly reducing actor sample complexity. To better assess performance across varying decision frequencies, we introduce the Frequency-Averaged Score (FAS) metric. Our results show that SRL significantly outperforms traditional RL algorithms in terms of FAS, making it particularly suitable for applications requiring variable decision frequencies. Additionally, we compare SRL with model-based online planning, showing that SRL achieves superior FAS while leveraging the same model during training that online planners use for planning. Lastly, we highlight the biological relevance of SRL, showing that it replicates the "action chunking" behavior observed in the basal ganglia, offering insights into brain-inspired control mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new model-based RL method that enables a lower frequency for action decision-making, slower than the frequency of sensing and execution. To accomplish this, the proposed method, Sequence RL (SRL), predicts a sequence of actions at each decision step, allowing for a lower decision frequency while employing a high-frequency dynamic model learner and action-value estimator. This setup mimics biological behavior, where the brain’s computation frequency is lower than that of sensing and actuating processes. Additionally, the paper introduces a new metric, FAS, to assess an RL method’s robustness and adaptability across different frequency settings, demonstrating that SRL achieves a high FAS score.

### Strengths
- The research motivation of the paper, specifically the comparison of decision patterns and frequencies between RL and humans, is compelling.
- The paper establishes a strong connection to biological fundamentals, providing relevant examples and insights throughout.
- The main idea—designing an RL algorithm inspired by biological principles, where each component operates at different frequencies—is novel, and the storyline leading up to the experiment section is smooth and easy to follow.

### Weaknesses
## Lack of related works
- This paper primarily focuses on its connection to biological insights and motivation but overlooks relevant efforts in the RL literature addressing frame-skipping, action repetition, long-horizon exploration, and action correlations. Several studies, such as [1,2,3,4], have explored similar topics from different perspectives. Although these works are not biologically motivated, their contributions are highly relevant to this paper and should not be ignored. Specifically, the paper fails to adequately discuss how methods that use action repetition or frame skipping could be used in the proposed Frequency-Averaged Score (FAS) setting, where actions must be taken even when observations are missing. The paper also neglects to discuss how its approach relates to methods that explicitly model temporal correlations in actions or explore long-horizon action sequences.

- The way of using GRUs in sequence action generation is very similar to the work in [4], please consider adding discussion.

## Technical Issues
- From line 252 to line 259, it is unclear that why using max entropy RL techniques, such as SAC, can address the issue of additive noise and automatically lower entropy for deeper actions arther from the observation. The explanation lacks a clear connection between the entropy regularization of SAC and the specific challenges of generating action sequences with increasing depth, particularly how this addresses the accumulation of noise or uncertainty in the predicted actions.

- Inproper declaration from line 292 to 296. There are several works that focus on credit assignment for action sequences, such as [2, 5]. The paper does not clearly distinguish its approach to credit assignment from these existing methods, especially concerning how it handles the temporal credit assignment problem when actions are predicted over a sequence and executed at a lower frequency.

- Does the current work fully address the issues listet in line 93? Namely the sparse rewards, jerky control, high compute cost, and catastrophic failure due to missing inputs. If not, it is better to remove this misleading content. The paper should clarify which specific issues from line 93 are directly addressed and which are not, avoiding overclaims about the method's capabilities.

## Poor Experiment Quality (Critical Issue for this Paper)
- The empirical results only include SAC as a baseline method, which was introduced in 2018. This is clearly insufficient. All the methods mentioned above have demonstrated advantages over SAC by employing different techniques for modeling action sequences or predicting temporally correlated actions. These approaches should theoretically achieve good FAS scores as well. Please consider including some of these methods to enrich the experiments and enhance the technical rigor of the paper. The lack of comparison with more recent and relevant methods makes it difficult to assess the true novelty and effectiveness of the proposed approach.

- Even with SAC as the only baseline, the proposed method, SRL, only outperforms SAC in 6 out of 10 tasks. Despite its advantage in the proposed FAS metric, SRL's performance over SAC is marginal and unconvincing. The paper needs to demonstrate more significant and consistent performance gains over existing methods to justify its contribution.

- In 5 out of 10 tasks (InvPendulum, Hopper, InvDPendulum, Reacher, and Swimmer), the Online Planning method outperforms SRL, contradicting the description in the caption of the "second Table 3" on page 9. This discrepancy undermines the claims made about the superiority of SRL over model-based online planning.

- Many important results are placed in the appendix, while the main paper is disproportionately occupied by the introduction to biological concepts. This imbalance detracts from the technical depth of the paper and makes it harder to evaluate the core contributions.

## Excessive Discussion of Biological Concepts
- Section 6 should be either removed entirely or moved to the appendix, as it detracts from the paper’s main focus on learning representation rather than biology. The extensive discussion of biological concepts is not directly relevant to the core technical contributions of the paper and dilutes its focus.

## Minor issues
- It is better to use different math symbols to distinguish the macro action and per-step action, especially in equation 1. Both sides used $a_{t'}$
- There are two "Table 3" captions in the paper: one on page 8 and another on page 9.
- The layout of figures and text in the paper is of low quality and requires adjustments and proofreading. For example, the title of Section 6 is oddly placed.

### Questions
Please address the issues outlined in the weaknesses section. The effectiveness of the proposed method is significantly limited by the low quality of the experiments, particularly the empirical results. It is essential to include extensive comparisons with related works to more convincingly demonstrate the method’s effectiveness, beyond merely relying on the proposed frequency metric.

### Soundness
2

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
2

### Summary
This model introduces Sequence Reinforcement Learning (SRL), a framework inspired by biological learning agents that allows prediction of action sequences of variable length. The method builds on the Soft-Actor-Critic algorithm, comprising a policy and a state-action-value function. Additionally, a model of the environment is trained and used for updating the policy. The policy includes a GRU RNN allowing the computation of arbitrary length action sequences starting from a single observation. While the model and the critic are trained on truly experienced trajectories only, training of the policy is done by predicting intermediate states using the model and the critic for assigning state-action-values. The method is evaluated on several continuous control tasks. The authors introduce a metric they call Frequence-Averaged Score (FAS) which is defined as the area under the curve of the reward vs decision frequency plot, and find that the SRL framework achieves significantly higher FAS-scores compared to the SAC baseline. They show that this metric is useful in predicting the average reward achieved on a randomized timestep version of the environment, arguing that a policy trained with SRL is better equipped for bridging the sim-to-real gap. The paper ends with a comprehensive comparison to structures found in the mammalian brain.

### Strengths
The introduced SRL method is explained well and is easy to understand while also showing significant improvement in the introduced FAS score.  Experimental evaluation is good and the usefulness of the FAS score is adequately demonstrated. The proposed SRL framework is well motivated using recent neuroscientific discoveries.

### Weaknesses
Demonstrating the improvement in sim-to-real transfer would add to the quality of the paper.
Likewise, including methods that use action repetition and macro-actions could be an interesting addition.

Minor mistakes:
- Line 104: demonstrate**s**
- Line 376: performance of the policy **in** when the frequency is not constant
- Line 535: we introduce**s** the Frequency-Averaged-Score (FAS) metric

Finally, I can't say that I fully agree with the statement "simple tasks like walking can be performed without input states if learned properly". Biological agents also use a range of inputs to maintain gait.

### Questions
1. Like SAC, SRL is using batched experience replay. Can you elaborate on how this interferes with biological plausibility of the method?
2. What is the $\alpha$ that shows up in eq. 3? What does the $\alpha \log \pi$ term represent?

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
This paper proposes Sequence Reinforcement Learning (SRL) as a method to lower effective control frequency by predicting multi-step open-loop action sequences. The action sequences are optimized on model rollouts at the given low-level frequency, while the policy only needs to be queried at a lower rate during deployment. The policy can then be deployed over the full open-loop horizon, or re-queried at intermediate points, where total reward obtained across action sequence lengths favors longer SRL variations over SAC.

### Strengths
The paper investigates an interesting problem, considering learning of temporally consistent open-loop action sequences that require fewer queries to the policy during deployment. While the approach is reliant on the quality of the underlying learned model, this enables learned MPC-like control at one end (deterministic 1-step) while also accommodating stochastic sampling periods by using open-loop actions until the next query is possible. The authors evaluate the method across several environments, and compare across 5 seeds against the strong SAC baseline. The paper is generally well-written and clearly motivated.

### Weaknesses
- The selection of baselines and or environments should be expanded, as the paper makes a quantitative argument of performance. Other model-free agents (e.g. D4PG, etc.) as well as model-based agents would help to better put the results into perspective. It could furthermore be interesting to run these experiments on the DeepMind Control suite as well, as Gym and DMC tasks have interesting differences in their underlying dynamics and resulting agent performance.
- It would be very informative to see how SAC performs when learning actions at the same rates as SRL-J, e.g. by applying action repeats of J steps. If “SAC-J” would significantly underperform SRL-J, it would provide a stronger argument for adding complexity via model learning.
- Potential inspiration for additional real-world-inspired environment modifications can be found in [1]
- I partially agree with the statement in line 334 that SRL-J is at a disadvantage. However, the agent still uses access to J=1 information via model and critic learning and so the learning curves do provide an accurate comparison across time steps.
- Instead of a learned model, it would be interesting to see an ablation with the ground-truth dynamics to determine how well SRL-J works w/o this “handicap” (ideal model)
- The sentence starting in line 160 highlights that SRL has a model complexity of zero after training. It should be made more clear that this actually applies to many MBRL algorithms (e.g. references in lines 138-143).
- Line 204: consider providing a brief summary of the insights of Section 6 here, or moving Section 6 forward. Otherwise it’s difficult to follow insights that have not been presented, yet.
- Sentence repetition in abstract lines 17-19
- Minor: line 49 —> missing period; line 265 —> model not subscripted

### Questions
- What variations of SRL are included in “all the policies” in line 374? If e.g., SRL-2 is included how would it provide open-loop actions for 16 steps if 16 is sampled from the uniform distribution in line 376?
- The setting on Figure 2 when considering the left-most action sequence length appears similar to an MPC setting for the SRL-J agents, where performance over model-rollouts is learned but only the first action is executed before predicting a new sequence. Could you elaborate on the performance delta of SRL-8/16 to SAC? Is this due to poor model fit?
- Could you elaborate on what you mean by the following sentence: “The SAC algorithm addresses this by maximizing the entropy of each action in addition to the expected return, allowing our algorithm to automatically lower entropy for deeper actions farther from the observation.” How does this lower the entropy of “deeper” actions?
- Is there a good argument of why Gym-v2 versions of the tasks were chosen?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper argues that the application of current reinforcement learning (RL) methods to real-world problems is hampered by the assumption that the actor can be executed at a high frequency (matching that of the actuators). Depending on the architecture of the policy, this can lead to a high computational burden. The authors take inspiration from action chunking observed in the brain to propose an RL algorithm that directly predicts action sequences (or macro actions). After training, it can thus run at slower frequencies than the environment MDP.  Experiments on several simulated continuous control benchmarks demonstrate good performance when predicting macro actions at frequencies lower than that of the MDP, as well as for variable stochastic time steps. The paper furthermore discusses connections of macro actions to neuroscience.

### Strengths
The paper relates problems that robotics researchers encounter in a creative way with insights from neuroscience. The issue of high computational demands of modern RL and imitation learning algorithms is quite relevant for the robotics community. The writing is furthermore clear and easy to understand. The proposed algorithm is simple, and easy to understand and implement.

### Weaknesses
The paper shifts its motivation from real-time control for robotics to biological plausibility over the course of the paper. The requirements of robotics and biological plausibility are not aligned well, however. Running policies at high frequencies is not necessarily an issue in robotics as long as the computational resources are sufficient. Furthermore, RL algorithms like Soft Actor Critic (SAC) usually do not aim at being biologically plausible, and the use of backpropagation through time in SRL could be viewed as not biologically plausible.

In particular, the small MLP policies trained with SAC should run at about 1 ms on modern hardware (or thereabouts). What is more, even when running them with an action repeat corresponding to a policy execution frequency of 50 Hz, the resulting policies usually perform fine. Hence, the computational load of the experimental set up does not pose a challenge to modern hardware and is therefore not well aligned with the motivation. 

What is furthermore absent from the discussion of the results is actual inference times. According to the abstract, reducing the time it takes to produce an action is a main motivation for the paper. However, it is entirely unclear why computing the first action of the macro action should be faster with the proposed algorithm than with vanilla SAC. Hence, it is unclear which advantage the algorithm in its current form offers in a real-world scenario where primitive actions have to be supplied at a fixed frequency to the actuators. It might be possible to run at a higher frequency if a delay is introduced to account for the time needed to calculate the first action of a macro action. Discussing this trade off would be interesting.

The motivation of the paper moreover hinges on the claim that existing methods cannot deal well with low control frequencies in the presence of multiple action dimensions (line 197). In my opinion, this claim is unsubstantiated for two reasons: (i) There is a complete lack of baselines targeted at low control frequencies in the experiments. At the very least showing results for SAC with action repeat is an absolute necessity to put the results into perspective, in my opinion. (ii) The two prior works mentioned (FiGAR and TempoRL) do have experiments on continuous control environments with multiple action dimensions in which they do achieve competitive performance. They should also be included as baselines (TempoRL makes an appearance in the appendix and performs well but is not shown in the main text). The evaluation of SAC is furthermore entirely unfair as it was trained without any action repetition but is then evaluated at a substantially lower frequency. This cannot work and is not a relevant baseline (unlike SAC with action repeat, training with randomized time steps, FiGAR, and TempoRL). For these reasons, I think the experimental results lack relevant baselines and cannot be evaluated properly without them. I would suggest adding these baselines (in the main text).

The field of hierarchical RL is only mentioned in passing in the paper but offers many relevant approaches to easing the computational requirements for control. A higher level (or manager) modulates the lower level (or worker) which produces primitive actions. As the worker may have a simpler architecture, it can run at a higher frequency, while the manager runs at a lower frequency. The worker can be both open loop or closed loop. In practice, simple PD controllers are often used in conjunction with low-frequency policies in robotics and often provide good results. Discussing the hierarchical RL literature to some extent therefore seems necessary.

In line 055 the claim “When RL agents are constrained to human-like reaction times, even state-of-the-art algorithms struggle to perform in simple environments.” is made. This needs a citations or experiments to back this up.

### Questions
* In line 098 the claim “Our model learns open-loop control utilizing a slow hardware and low attention, and hence also low energy.” is made. Why should that be true?
* In line 150 the claim that online planning is not feasible in robotics or the brain is made. In my experience this is not true. How did the authors come to this conclusion?
* What is meant by “reducing actor sample complexity” in line 028 in the abstract? Sample complexity usually refers to the amount of transitions needed for training.
* In the paragraph starting in line 050, the authors compare the performance of RL agents on MuJoCo tasks with the performance of humans on complex tasks and relate to reaction times. Why would these settings be comparable as the embodiment, action representation, and tasks are completely different?
* In table one the < sign in the last row should be >.
* What is meant by online planning in the paper? And how is it separate from MPC? It is not clear to me what online planning means.
* In line 054 there seems to be a typo, a redundant “the shows”.
* In line 169 the statement that MPC is limited to systems that have already been modeled accurately is made. However, algorithms like TD-MPC2 use MPC successfully with (partially) learned models.
* The next paragraph states that MPC requires very short timesteps to work. However, that many robotics papers use high frequencies does not mean that it is strictly required. For example, [1] does MPC over skills which has a very low frequency.
* The training curves in the appendix are plotted on top of each other such that it is almost impossible to make out some of the algorithms. Would it be possible to improve these plots?
* Would it be possible to visualize the action sequences predicted by SRL compared to those of SAC?
* In line 516 the claim “In deterministic environments, a capable agent should achieve infinite horizon control for tasks like walking and hopping from a single state.” is made. This is infeasible in environments with complex, possibly unstable dynamics since errors do not disappear but can instead compound and blow up. I would recommend revising this paragraph.

[1] Shi, Lucy Xiaoyang, Joseph J. Lim, and Youngwoon Lee. "Skill-based model-based reinforcement learning." arXiv preprint arXiv:2207.07560 (2022).

### Soundness
3

### Presentation
3

### Contribution
3
