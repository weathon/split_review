# Parameterization Agnostic RL

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Recent advances in learning decision-making policies can largely be attributed to training expressive policy models, largely via imitation learning. While imitation discards non-expert data, offline and/or online fine-tuning via reinforcement learning (RL) can still learn from suboptimal data. However, instantiating RL training of a new policy class often presents a different challenge: most deep RL machinery is co-developed with assumptions on the policy class, resulting in poor performance when the policy class changes. For e.g., SAC utilizes a low-variance reparameterization policy gradient for Gaussian policies, but this is unstable for diffusion policies and intractable for autoregressive (e.g., transformer) categorical policies. This implies that current RL algorithms may not perform well or may even not be applicable when the policy class changes. To address this issue, we develop an offline RL and online fine-tuning approach called **parameterization-agnostic RL** (**PA-RL**) that can effectively train multiple policy classes, with varying architectures. The basic idea is that a universal supervised learning loss can replace the policy improvement step in RL, as long as it is applied on "optimized" actions. To obtain these optimized actions, we first sample multiple actions from a base policy, and run global optimization (i.e., re-ranking multiple action samples using the Q-function) and local optimization (i.e., running gradient steps on an action sample) to maximize the critic on these candidates. PA-RL enables fine-tuning diffusion and autoregressive policies entirely via RL, while improving performance and sample-efficiency compared to existing online RL fine-tuning methods. PA-RL allows us to successfully fine-tune diffusion policies and OpenVLA, a 7B parameter generalist robot policy, on real robots.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Parameterization-Agnostic Reinforcement Learning (PA-RL) by addressing challenges in existing RL methods that often tailor their designs to specific policy types, leading to instability or poor generalization when adapting to new ones (e.g., diffusion models or transformers). The main contribution is in optimizing actions directly through a combination of global and local optimization processes, followed by supervised learning updates that train the policy to imitate these optimized actions. This approach simplifies the training, while maintaining stability and sample efficiency across different policy parameterizations. PA-RL achieved good performance in both simulated environments and real-world robotic tasks.

### Strengths
1. The paper studies a valid and important challenge, and addresses a major problem in current RL methods. Therefore, I believe the contribution can be impactful. 

2. The proposed method is straightforward, intuitive and practical. To my knowledge, the procedure for global and local optimization of actions based on the critic appears to be novel. 

3. The experimental results are comprehensive and are in favor of the method. The inclusion of real-world robotics experiments enhances the credibility and practical relevance.

### Weaknesses
1. The local optimization step needs further investigation,  as it is the primary distinction of this work compared to previous methods such as self-imitation learning [1]. I recommend that the authors provide plots and detailed results specifically for the gradient-based step. The implementation aspect is significant since computing $\nabla_a Q(s, a)$ requires forward mode automatic differentiation (AD), which is less common in practice and can be computationally expensive depending on the action space and model parameters. Additionally, it is unclear whether this gradient would be effective unless the Q function is well-trained. Even in that case, the gradient may not always indicate the direction toward optimal actions. Visualizing this gradient on toy examples would be beneficial for readers to better grasp its behavior.

2. The method is representing the policy as a categorical distribution over the “good” action candidates $\hat{\mathcal{A}}_{\pi, m}$ which is then optimized with supervised learning. It is unclear to me how this works exactly because the action candidates are changed from iteration to iteration.

### Questions
1. Could you include results or plots that illustrate the gradient-based optimization of the actions?
2. Did you use forward mode (AD) to compute $\nabla_a Q(s, a)$? If so, were there any specific challenges or intricacies in its implementation?
3. How do you manage the changes in the action set $\hat{\mathcal{A}}_{\pi, m}$ as it evolves between iterations?

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
5

### Summary
This paper trains policies in actor-critic RL with a supervised learning loss on "optimized" actions, i.e., sample actions from actor and pick the top Q-valued actions. This enables fine-tuning diffusion and autoregressive policies with better sample-efficiency than some prior ways to train the actor.

### Strengths
- The proposed approach is simple and intuitive, and shows good experiment results on the domains considered.
- The real robot experiments show meaningful improvement with RL fine-tuning, which is a good empirical contribution.

### Weaknesses
## Missing important prior works and baselines; lack of novelty
The insight to train the actor with a supervised learning loss is not a new one, and there is a vast literature in actor-critic RL that this paper ignores.

- [1] Neumann, Samuel, et al. "Greedy Actor-Critic: A New Conditional Cross-Entropy Method for Policy Improvement." The Eleventh International Conference on Learning Representations.
They propose an alternative update for the actor in actor-critic algorithms: "N ∈ N actions are sampled according to a proposal policy, the actions are sorted based on the magnitude of the action-values, and the policy is updated to increase the probability of the maximally valued actions".

- [2] Simmons-Edler, Riley, et al. "Q-learning for continuous actions with cross-entropy guided policies." arXiv preprint arXiv:1903.10605 (2019).
They learn a policy to minimize a squared error to the maximal action found by CEM (approximate global optimization). "CGP is a multi-stage algorithm that learns a Q-function using a heuristic Cross-Entropy Method (CEM) sampling policy to sample actions, while training a deterministic neural network policy in parallel to imitate the CEM policy. This learned policy is then used at inference time for fast and precise evaluation without expensive sample iteration"

- [3] Shao, Lin, et al. "Grac: Self-guided and self-regularized actor-critic." Conference on Robot Learning. PMLR, 2022.
"propose a self-guided policy improvement method by combining policy-gradient with zero-order optimization to search for actions associated with higher Q-values in a broad neighborhood."

- [4] Pourchot, Aloïs, and Olivier Sigaud. "CEM-RL: Combining evolutionary and gradient-based methods for policy search." arXiv preprint arXiv:1810.01222 (2018).

- [5] Kalashnikov, Dmitry, et al. "Scalable deep reinforcement learning for vision-based robotic manipulation." Conference on robot learning. PMLR, 2018.
While QT-Opt does not train an explicit actor network, it is a viable method to pick top Q-valued actions. This along with several other actor optimization methods (like listed above) are important prior work.

Based on these, it is clear that PA-RL idea of "sampling and training on top Q-value actions with supervised learning" is not novel. If there is indeed a significant difference, then this paper should compare against the above works as baselines.

## There is no "global optimization", it is just sampling
Why is the first action optmization step labeled as global optimization, when it is just sampling k actions? If I understand correctly, there is no need to evaluate or rank the Q-values of these samples, since anyway local optimization step is performing gradient updates to these samples, and then the policy is trained proportional to the Q-values of the locally-optimized actions. The algorithm is much simpler than it is shown to be. Being simpler would actually make the algorithm more applicable and transparent.


Additionally, the sampling step seems to do the most work in Table 4, instead of the local optimization step. This makes it more likely that a principled approach of training with CEM-searched actions (like in Greedy AC or CGP) performs even better, because it would be real global optimization.


## Soundness concern: No ablation to justify not imitating the max Q-value action
Section 4.2 labels actions by first sampling them according to the Q-values, but there is no ablation to show that the simpler alternative of taking highest Q-valued action is worse. Why would sampling be better when it adds noise to the policy improvement step? Not only does this lack any thereotical basis, it goes against the idea of generalized policy iteration, where the policy must be updated in the direction of arg max of Q-values.

## No convergence guarantees on the resultant RL algorithm
While I intuitively agree that supervised learning on an optimal action would lead to policy improvement, since this paper modifies the RL algorithm, it must have a theoretically guarantee that this change does not lose the convergence guarantees of the underlying algorithm it modifies in the tabular setting. Another alternative is to build on the guarantees of the prior works I have mentioned above. Though, the novelty of this paper would still remain unclear.

## No experiments on PA-RL + standard actor-critic RL like SAC and TD3
The most common actor-critic RL algorithms are SAC and TD3, but this paper does not show how PA-RL improves (or maintains performance) over these algorithms. I appreciate the results on offline and offline2online RL, but to justify this paper's general claims about "actor-critic RL", it should also be shown on off-policy online RL algorithms.

### Questions
Raised questions on novelty, prior work, lack of important baselines, soundness under Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an approach to Reinforcement Learning that is agnostic to the parameterization of the policy. The proposed framework can seamlessly work to train diffusion policies and transformer policies.

### Strengths
1. The paper investigates an important topic in RL. 

2. The presented algorithm performs strongly against several baselines on different offline, online fine-tuning, and hybrid RL tasks, including two real-world experiments.

### Weaknesses
1. How should the presented method be modified to work with unimodal policies like Gaussian policies? Currently, the presented method seems irrelevant for unimodal policies, as the optimized actions would converge to the same point. This assumption is not mentioned in the paper and makes the proposed method less RL-agnostic.

2. While the proposed method achieves high returns in the presented experiments, a discussion on the training time is missing. Plotting PA-RL's performances along with the baseline's performances as a function of the clock time for the offline experiments would increase the significance of the submission.

3. Many mistakes and issues alter the reading flow of the paper (see Remarks below).

4. The code is not provided, which limits the reliability of the experiments.

5. Some design choices are not justified (see Questions below).

6. An analysis of the distribution of the actions after the local optimization would be interesting as there is a risk that the distribution of the actions would not be multi-modal after the optimization, resulting in duplicated samples. As this property depends on the critic’s behavior, analyzing the critic’s landscape w.r.t. the actions would also be beneficial.


– Remarks –

A. Line 102, “compare EMaQ” should be “compared to EMaQ”.

B. Line 121, “self-tunign” should be “self-tuning”.

C. Line 137, the optimal policy attains the maximal cumulative discounted “reward” and not “value function”.

D. Most abbreviations used in the paper are not defined, which makes the paper less accessible to a broader community. For example, nearly all baseline abbreviations are not explained, and the abbreviation AWR is not explained either.

E. Equation $3.1$, $\bar{\alpha}$ is not defined.

F. Line 156, the definition of the action “a” is wrong. The action “a” is described as a sum of independent terms, while the reverse diffusion process is an iterative process where each term depends on the previous one.

G. Equation $3.3$, the $\alpha$ parameter plays no role in the minimization. Additionally, the minimization is not performed on the conservative regularizer alone. Finally, $\pi$ is only defined $2$ sentences after the equation is presented, which can be misleading.

H. Line 194, a space is missing in “RLalgorithm” between “RL” and “algorithm”.

I. Line 228, “maximize rewards” should be replaced by “maximize returns”.

J. Line 237, it might be beneficial to replace $\pi$ by $\phi$ in $\tilde{\mathcal{A}}_{\pi, m}$, to stress its dependency in the parameters of the learned policy.

K. In Line 6 of Algorithm $1$, the right side of the inequation should be $Q(s, a^{(i-1)})$ instead of $Q(s, a^{(i)})$.

L. In Line 2 of Algorithm $1$, I would replace “at every state” with “for every state s”.

M. Equation 4.5, I would add the dependency on $\theta$ as an input to the loss.

N. In Line 4 of Algorithm $2$, the loss is briefly explained in Section $3$ but not properly defined. Writing its definition would help.

O. In Line 5 of Algorithm $2$, the loss is not defined, making the pseudo-code harder to read. Additionally, the loss should take as input $\theta$ as it also relies on it.

P. Line 323, “a a set” can be replaced by “a set”.

Q. I found the last paragraph of Section $4.3$ unconvincing and unclear. Reformulating it more straightforwardly would help clarify the authors' argument. For example, the terms in Equation $4.6$ could be introduced before the equation is presented, and then its significance could be explained.

R. Line 353, “that train diffusion policies” could be replaced by “that also train diffusion policies”. This would make the sentence clearer.

S. The authors only report the archive versions of the paper, while a significant proportion of the cited works are peer-reviewed. Reporting the venue of the works would be more accurate.

T. The paper Li, Zechu, et al. "Learning Multimodal Behaviors from Scratch with Diffusion Policy Gradient." NeurIPS (2024) is close to the presented work. It would be worth including it in the Related Work.

### Questions
~1. The influence of the number of gradient steps $T$ performed for the local optimization is not discussed.~

~2. The appendix mentions that the critic of PA-RL was trained with a categorical loss for some experiments. Was the same mechanism applied to the baseline as well?~

3. Line 138, why did you choose to add the $\frac{1}{1 - \gamma}$ in the definition of $V^{\pi}$? The expectation over the transition dynamics is missing.

4. ~In Line 6 of Algorithm $1$, the authors verify that the locally optimized action yields a higher value when evaluated on the critic. Is this step needed? This operation adds a computing cost that is not justified in the paper.~ Moreover, in its current version, nothing is done to change the optimization process when the new action is worse than the previous one, which means that the following iteration of the for loop will be identical. 

~5. In Line 4 of Algorithm $2$, the Bellman backup is computed from the optimized action $\tilde{\mathcal{A}}_{\pi, m}$ instead of the action generated from the current policy. The authors do not show the benefit of this choice.~ 

– Remarks – 

~A. Line 102, “compare EMaQ” should be “compared to EMaQ”.~

~B. Line 121, “self-tunign” should be “self-tuning”.~ 

~C. Line 137, the optimal policy attains the maximal cumulative discounted “reward” and not “value function”.~ 

D. Most abbreviations used in the paper are not defined, which makes the paper less accessible to a broader community. For example, nearly all baseline abbreviations are not explained, and the abbreviation AWR is not explained either.

~E. Equation $3.1$, $\bar{\alpha}$ is not defined.~

~F. Line 156, the definition of the action “a” is wrong. The action “a” is described as a sum of independent terms, while the reverse diffusion process is an iterative process where each term depends on the previous one.~ 

~G. Equation $3.3$, the $\alpha$ parameter plays no role in the minimization. Additionally, the minimization is not performed on the conservative regularizer alone. Finally, $\pi$ is only defined $2$ sentences after the equation is presented, which can be misleading.~

~H. Line 194, a space is missing in “RLalgorithm” between “RL” and “algorithm”.~ 

~I. Line 228, “maximize rewards” should be replaced by “maximize returns”.~

~J. Line 237, it might be beneficial to replace $\pi$ by $\phi$ in $\tilde{\mathcal{A}}_{\pi, m}$, to stress its dependency in the parameters of the learned policy.~

~K. In Line 6 of Algorithm $1$, the right side of the inequation should be $Q(s, a^{(i-1)})$ instead of $Q(s, a^{(i)})$.~

~L. In Line 2 of Algorithm $1$, I would replace “at every state” with “for every state s”.~ 

~M. Equation 4.5, I would add the dependency on $\theta$ as an input to the loss.~

N. In Line 4 of Algorithm $2$, the loss is briefly explained in Section $3$ but not properly defined. Writing its definition would help.

O. In Line 5 of Algorithm $2$, the loss is not defined, making the pseudo-code harder to read. ~Additionally, the loss should take as input $\theta$ as it also relies on it.~

~P. Line 323, “a a set” can be replaced by “a set”.~

Q. I found the last paragraph of Section $4.3$ unconvincing and unclear. Reformulating it more straightforwardly would help clarify the authors' argument. For example, the terms in Equation $4.6$ could be introduced before the equation is presented, and then its significance could be explained.

~R. Line 353, “that train diffusion policies” could be replaced by “that also train diffusion policies”. This would make the sentence clearer.~

S. The authors only report the archive versions of the paper, while a significant proportion of the cited works are peer-reviewed. Reporting the venue of the works would be more accurate. 

~T. The paper Li, Zechu, et al. "Learning Multimodal Behaviors from Scratch with Diffusion Policy Gradient." NeurIPS (2024) is close to the presented work. It would be worth including it in the Related Work.~

### Soundness
3

### Presentation
2

### Contribution
3
