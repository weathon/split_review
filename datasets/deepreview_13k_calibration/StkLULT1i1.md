# Learning a Diffusion Model Policy from Rewards via Q-Score Matching

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Diffusion models have become a popular choice for representing actor policies in behavior cloning and offline reinforcement learning. This is due to their natural ability to optimize an expressive class of distributions over a continuous space. However, previous works fail to exploit the score-based structure of diffusion models, and instead utilize a simple behavior cloning term to train the actor, limiting their ability in the actor-critic setting. In this paper, we present a theoretical framework linking the structure of diffusion model policies to a learned Q-function, by linking the structure between the score of the policy to the action gradient of the Q-function. We focus on off-policy reinforcement learning and propose a new policy update method from this theory, which we denote \emph{Q-score matching}. Notably, this algorithm only needs to differentiate through the denoising model rather than the entire diffusion model evaluation, and converged policies through Q-score matching are implicitly multi-modal and explorative in continuous domains. We conduct experiments in simulated environments to demonstrate the viability of our proposed method and compare to popular baselines. Source code is available from the project website: \url{https://michaelpsenka.io/qsm}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Q-score matching, a new methodology for off-policy reinforcement learning that harnesses the score-based structure of diffusion model policies to align with the action gradients of the Q-function. This approach aims to overcome the limitations of simple behavior cloning in actor-critic settings by integrating the score of the policy with the Q-function's action gradient. Theoretical justification is provided for the proposed method. Effectiveness is demonstrated through comparative experiments in simulated environments.

### Strengths
1. The approach of conceptualizing the reinforcement learning problem as a dynamic process is thought-provoking, and employing a diffusion model to ascertain the action progression for each discretization step is an innovative and logical step.

2. A comprehensive theoretical analysis is provided.

### Weaknesses
1. **Theory-Practice Disparity** The theoretical framework suggests that the score of optimal policies $\Psi^*$ aligns with the action gradient of the optimal Q-function ($\nabla_a Q^{\Psi^*}$). While conceptually sound, the challenge arises in practical scenarios where the optimal Q-function is unknown. In your case, you goal is to move $\Psi$ to $\Psi^*$, and you use the $\nabla _a Q$ but not $\nabla_a Q^*$ as the direction to update $\Psi$. The theorem, while insightful, does not appear to significantly contribute to the algorithm's practical efficacy.

2. **Implementation Clarification Needed** There seems to be a discrepancy between the methodology described and its implementation. The paper suggests using a diffusion model to learn the discrete action sequence from $a_{t-1}$ to $a_t$ as indicated in section 2.3. Nonetheless, the algorithm presents the derivation of $a_t$ through iterative denoising from random noise, rather than using $a_{t-1}$ as a starting point. This aspect of the implementation calls for further clarification.

3. **Comparative Methodology Concerns** The implementation closely resembles the one in Diffusion-QL [1], where actions are also sampled by denoising from noise through a trained score function, and this function is refined under the guidance of the Q-value. While Diffusion-QL optimizes the score function by directly maximizing the Q-value, your method minimizes the L2 norm between the score and the action gradient of Q. These methods seem to conceptually converge, raising questions about the distinctiveness of your approach.

4. **Insufficient Experimentation** The range of experiments conducted lacks breadth, especially in the domain of online continuous control tasks where environments like Ant and Humanoid are benchmarks. Incorporating these could enhance the empirical validation of the proposed method.

### Questions
1. Confused in the Algorithm box. What is the $\pi_\phi$ in the algorithm? The score network $\Psi$ depends on $(s, a)$. Why the sampling of $a_t$ doesn’t depend on $a_{t-1}$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel reinforcement learning algorithm based on the diffusion model. It matches the score of the policy with the gradient of the Q-function, which better exploits the score-based structure of diffusion models. Both theoretical analysis and empirical evaluation are provided to support the advantage of the proposed method.

### Strengths
1. The idea introduced in this paper is quite novel compared with previous works in utilizing the diffusion model in decision-making, which I think may have a profound impact on future works.
2. The paper is well-written. A clear motivation is presented and thorough theoretical analyses are provided to support the model. Figure 1 gives a clear illustration of the effect of Q-score matching.
3. The empirical evaluation shows promising results.

### Weaknesses
I feel the experimental part is not well performed by the authors, without much analysis. If the authors can address my concerns below, I'd be happy to raise my score.

First, the authors only visualize the learned action distribution in Figure 4, where a comparison with baselines is missing. SAC is also designed to improve its exploration ability, how is the strategy of QSM compared to that?

Second, QSM only performs the best 3 out of 6 environments, with the comparison to 2 baselines. My suggestion is to add more baselines like policy-gradient methods, and other RL+diffusion models if any. Also, does QSM still gain an advantage in the environment with a discrete action space?

Finally, I'm not sure if the authors have an explanation for the inferior performance of QSM on the Cheetah Run and Walker Run, there seems to exist a clear saturated stage for QSM.

### Questions
See questions in the last part.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article proposes learning a diffusion model policy that exploits the linked structure between the score of the policy and the action gradient of the Q-function. The proposed algorithm, called Q-score matching (QSM),  iteratively matches the parameterized score of the policy to the action gradient of its Q-function, giving a more geometric viewpoint on optimizing such policies. The authors provide theoretical justification for the proposed method, revealing the connection between the QSM update rule and the soft policy iteration.

### Strengths
1. The authors introduce a novel perspective for policy optimization, which involves learning the score of the policy by utilizing the action gradient of the Q-function.
2. The authors provide rigorous mathematical derivations and theoretical support for the proposed method, establishing its solid foundation.
3. The authors define the decision-making process from the perspective of "score," offering a fresh angle that may inspire further research in this area.

### Weaknesses
1. The authors introduce a novel perspective for policy optimization, which involves learning the score of the policy by utilizing the action gradient of the Q-function.
2. The authors provide rigorous mathematical derivations and theoretical support for the proposed method, establishing its solid foundation.
3. The authors define the decision-making process from the perspective of "score," offering a fresh angle that may inspire further research in this area.

1. Compared to the rigorous theoretical aspect, the experimental section of the paper appears relatively weak. It only compares the proposed method with two relatively outdated baselines, SAC and TD3, on six simple tasks from the deepmind control suite.
2. In the current experiments, the performance of QSM does not seem to be as impressive. Except for the "Hopper Hop" environment, the baselines seem to be able to outperform QSM in terms of convergence on other environments.
3. QSM is not the first algorithm that utilizes the Q function to guide policy updates. Diffusion-QL proposed by Wang et al. and QGPO proposed by Lu et al. both employ different approaches to leverage the Q function for policy learning. Although QSM is an off-policy online RL algorithm, it would be better to compare it with other methods in an offline setting to evaluate the strengths and weaknesses of different ways to utilize the Q function.

### Questions
Can the authors test the performance of the QSM in more challenging environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
