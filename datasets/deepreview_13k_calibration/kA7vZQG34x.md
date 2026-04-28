# Adversarial Imitation Learning from Visual Observations using Latent Information

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 3, 5

## Abstract
We focus on the problem of imitation learning from visual observations, where the learning agent has access to videos of experts as its sole learning source. The challenges of this framework include the absence of expert actions and the partial observability of the environment, as the ground-truth states can only be inferred from pixels. To tackle this problem, we first conduct a theoretical analysis of imitation learning in partially observable environments. We establish upper bounds on the suboptimality of the learning agent with respect to the divergence between the expert and the agent latent state-transition distributions. Motivated by this analysis, we introduce an algorithm called Latent Adversarial Imitation from Observations, which combines off-policy adversarial imitation techniques with a learned latent representation of the agent's state from sequences of observations. In experiments on high-dimensional continuous robotic tasks, we show that our model-free approach in latent space matches state-of-the-art performance. % while providing significant computational advantages. 
Additionally, we show how our method can be used to improve the efficiency of reinforcement learning from pixels by leveraging expert videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers the problem of imitation learning from visual demonstrations, where not only the actions are unobservable, but also---due to partial observability---the underlying state. An upper bound is presented, that shows that the suboptimality of the learner can be bounded based on the TV-distance of the respective distributions over transitions in a latent space that compresses a history of observations and is assumed to be a sufficient statistic of the complete history (including actions). Motivated by this bound, a method is presented that performs imitation learning by applying GaifO (GAIL with a state-transition discriminator) using the latent representations instead of the states. The latent representations are learned during imitation learning by backpropagating the Q-function loss of DDPG through the encoder (the Q-function is expressed as $Q(z(x\_{t^{-}:t}), a)$, with observation history $x_{t^{-}:t}$). No other losses (e.g. policy or discriminator loss) are backpropagated through the encoder.

This method is compared to the baseline PatchAIL in the "Visual imitation from Observeration" (V-IfO) setting and to LAIL in the visual imitation learning (VIL) setting, where expert actions are observed and their history is used for computing the embedding. In both settings, the proposed method LAIFO/LAIL compares favorable to the baseline methods in terms of stability, final performance and training time. Furthermore, the paper investigates the RL from demonstration setting, where the discriminator reward is augmented with a known reward function to guide exploration using demonstrations for vision-based locomotion tasks, which significantly improves performance compared to methods that do not make any use of demonstrations.

### Strengths
1. Soundness
------------------
- The overall approach of learning a latent representation and imitating the expert with respect to latent transitions is sound.

- The derived Theorems seem to be correct.

- The claims are substantiated, and the main weaknesses (e.g. that expert and learner act in the same POMDP) are clearly communicated.

2. Relevance
-----------------
- Imitation learning from (actual) observations is an important problem. Although I agree that learning under dynamic mismatch is still a key limitation, I think that the considered problem setting is still a useful step towards this objective.

3. Novelty
-------------
- The proposed method seems to be novel.

4. Presentation
--------------------
- The method was very well presented. The paper was a very read for me, which, however, is also partially due to the fact that the method is very straightforward.

5. Related work
---------------------
- I'm not very familiar with the particular problem setting of imitation learning in POMDPs with unobserved actions, so I am not sure that no important baseline is missing. But the paper certainly does discuss several important relevant works. I am only of a recent work by Al-Hafez et al. (2023) that performs imitation learning for locomotion without action observations, but does not consider partial observability due to visual observations.

Al-Hafez, F., Tateo, D., Arenz, O., Zhao, G., & Peters, J. (2023). LS-IQ: Implicit reward regularization for inverse reinforcement learning. (ICLR).

### Weaknesses
1. Experiments
--------------------
- The results presented in Table 2 do not seem to be statistically significant. I think it is misleading to highlight the best final performance in bold despite overlapping confidence intervals.

- The experiments in the imitation learning from demonstration setting are not fair as none of the baseline makes use of the expert demonstrations. It would be better to compare to methods that focus on this problem setting.

2. Originality
-----------------
While I think that the method is novel, it also very straightforward and simple. While I do believe that simple methods are good, I could not get many new insights from the paper (the theorems are also relatively straightforward variations of previous theorems that bound suboptimality based on TV distance in IL and RL).

### Questions
How can adding a reward objective to the imitation learning objective be justified? Can the detrimental effects of one objective on the other be bounded in some way?

It is common to not backpropagate through the actor in representation learning, and I also think that for similar reasons it makes sense to not backpropagate through the discriminator in the adversarial IL setting. However, did you consider addional (or alternate) methods to learn better representations? For example, many representation learning methods use additional objectives, e.g. contrastive losses, maximizing predictive information, which can significantly improve the downstream performance, in particular in RL from images.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the problem of "Visual Imitation from Observations" (V-IfO), where the only learning source is a set of RGB observations of a task. The theoretical contribution is establishing a new upper bound on the learner's suboptimality based on its divergence to the expert's state-transitions as encoded in some latent. Methodology-wise, the authors propose a new algorithm "Latent Adversarial Imitation from Observations" (LAIfO), which combines existing methodology from inverse RL (IRL) with observation stacking and data-augmentation from recent off-policy RL algorithms. Empirically, the authors show their algorithm trains in less wall-clock time while retaining the same performance to other recent state-of-the-art imitation algorithms on six DeepMind Control tasks. Moreover, they also show that incorporating demostrations with off-policy learning and rewards can speed up existing off-policy RL algorithms on three of the more challenging DeepMind Control tasks.

### Strengths
- Overall, the paper is well-written. In particular, the authors make an appreciated effort to clearly define notation and assumptions before delving into the analysis.

- The methodology is clear and simple and mostly reproducible.

- I appreciate the purpose of the paper, visual imitation is a relevant problem.

### Weaknesses
1. The proposed algorithm combines the adversarial imitation loss with gradient penalties from DAC [1] with the off-policy algorithm, stacking and  data-augmentation strategy from DrQv2 [2]. While both this papers are cited in text, the way the methodology is introduced in Section 5 never makes these connection explicit. As a consequence, I feel the way the algorithm is prevented can be quite misleading to an unfamiliar reader. Hence, I believe changing Section 5 to clarify which components come from DAC, which ones come from DrQv2 and that the novelty lies in *combining* them, would be extremely important before this work can be published.

2. I found the novelty of the theoretical analysis and methodology to be quite limited. While I believe this is not a mandatory aspect for a good paper, especially if the resulting algorithm is effective, I found the quality of the empirical evaluation insufficient to make such assessment (see point 3).

3. There are several aspects of the evaluation that left me unsatifsfied with its quality. First, the comparison with PatchAIL-W and VMAIL is only carried out on six tasks from three environments from the DeepMind Control (DMC) suite, while the comparison with DrQv2 and Dreamer-v2 is only carried out in three tasks from a single environment. I would have appreciated seeing a wider variety (e.g., including other complex environments from DMC such as quadruped/jaco arm and from alternative benchmarks e.g., car racing, claw rotate as considered in VMAIL). Furthermore, the current ablation seems very much limited as it could consider studying the effect of performance of many additional design choices (e.g. spectral norm v gradient penalty for Lipshitzeness/number of stacked frames/type of data augmentation...). Additionally, I think that reporting results also for a simple behavior cloning baseline with the same data-augmentation/architecture/optimization would help understand the contribution from the introduced IRL methodology. Most worryingly, however, when comparing LAlfO with Dreamerv2 and DrQv2 the performance of the baselines is considerably lower than what reported in prior work (e.g. see [2]). Even after 10x10^6 milion steps, the gains from incorporating expert demonstrations seem marginal at best (if any) when using the results from DrQv2. I would really appreciate it the authors could clarify this inconsistency. (also given that DrQv2 shares the data that produced their reported learning curves)

4. Again, related to the evaluation Section, I find some of the claims to be quite misleading. E.g. in connection to the humanoid results the authors state "we solve these tasks by using only 10^7 interactions" However, the reported performance on 2/3 tasks (walk and run) is still extremely low, and I would refrain from referring to any of these tasks as solved. Furthermore, I think to make the comparison fairer I would have also appreciated seeing results for DrQv2/Dreamerv2 adding the expert demonstrations to their respective replay buffer.

Minor:

I believe the visual imitation problem setting described is a special simpler case of the visual third-person/observational imitation learning setting tackled by prior methods [3 as cited, 4, 5]. Yet, in contrast to what stated in Related Work ("All of the aforementioned works consider fully observable environments"), also this line of work deals with visual observation. Hence, I believe there should be a clearer explicit connection.

### Questions
- Where can I find detail regarding the expert data (is it taken from a standard benchmark? Was it collected with any particular protocol?) I cannot find this important information in the main text.

- Can the authors provide learning curves for an increased number of steps for the Humanoid tasks, if available? (or at least also show the DrQv2 learning curves for the full 3x10^7 steps, shared in their repository to provide a refence for Figure 4)

In conclusion, while I mostly appreciate the nature of the contribution, the direction, and the presentation of the paper, I believe there are some current major flaws that make it not, yet, ready for publication. For this reason, I am currently leaning towards rejection. However, I am willing to change my score, in case the authors manage to properly address my criticism and questions.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper has proposed a visual imitation learning approach, where the agent learns from expert observations, but is not accessible to expert actions. To deal with the high-dimensional visual observations, the imitative rewards are defined in a latent space, and the latent state space is learned with the minimizing TV divergence objective. This paper is theoretically justified, and the proposed approach is evaluated in the mujoco domain.

### Strengths
This paper has a sound theoretical analysis.

### Weaknesses
Comparing the sample efficiency and the convergent return, the proposed approach has not shown much strength superior to the baseline methods.

This paper has missed important related works, which aims to define imitative rewards with sinkhorn distance, which is beyond the GAIL framework.



### Questions
Does the latent representation require pretraining? Or is it learned end-to-end with the policy network and Q network?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
