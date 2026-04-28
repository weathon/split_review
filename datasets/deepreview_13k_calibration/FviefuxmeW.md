# Beyond-Expert Performance with Limited Demonstrations: Efficient Imitation Learning with Double Exploration

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 3, 8

## Abstract
learning where the goal is to learn a policy that mimics the expert's behavior. In practice, it is often challenging to learn the expert policy from a limited number of demonstrations accurately due to the complexity of the state space. Moreover, it is essential to explore the environment and collect data to achieve beyond-expert performance. To overcome these challenges, we propose a novel imitation learning algorithm namely Imitation Learning with Double Exploration (ILDE), which implements exploration in two aspects: (1) optimistic policy optimization via an exploration bonus that rewards state-action pairs with high uncertainty to potentially improve the convergence to the expert policy, and (2) curiosity-driven exploration of the states that deviate from the demonstration trajectories to potentially yield beyond-expert performance. Empirically, we demonstrate that ILDE outperforms the state-of-the-art imitation learning algorithms in terms of sample efficiency and achieves beyond-expert performance on Atari and MuJoCo tasks with fewer demonstrations than those in previous work. We also provide theoretical justification of ILDE as an uncertainty-regularized policy optimization method with optimistic exploration, leading to a regret growing sublinearly in the number of episodes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the challenge of surpassing expert performance through imitation learning. The authors propose ILDE which modifies the Generative Adversarial Imitation Learning (GAIL) framework by incorporating an intrinsic reward term to encourage exploration. The method is supported by theoretical analysis quantifying the algorithm's regret bounds. Empirical evaluation on 6 Atari games and 4 MuJoCo tasks demonstrates ILDE's improvements over baseline methods.

### Strengths
- This paper studies a seemingly interesting problem of learning a policy with imitation learning to be much better than the demonstration.
- The paper offer some theoretical analysis of the proposed method.

### Weaknesses
 - The problem formulation of optimizing the GAIL loss + intrinsic reward to achieve a better performance than the expert is not convincing.
- The proposed method is only evaluated on limited tasks and the results lack explanation.

 - As mentioned in the weakness part, the biggest concern from me is the formulation. Could you please elaborate why, intuitively, adding an intrinsic reward term to the GAIL objective (Eq. 3.3) can help the policy to achieve a better performance than the expert? I think to achieve a better performance than the expert, the agent must understand the intention of the expert and extrapolate it. I cannot see how an intrinsic reward guarantee to help for this. Maybe there are some hidden assumptions about the task or the demonstrations?
- In the introduction, you list the formulation of the problem itself as one of the contribution, but you write the formulation in the Preliminary section. Could you elaborate what is the difference between the formulation in this paper with previous works, for example [1]?
- From the results in Table 1, ILDE w/o $r^k$ is much better than ILDE w/o $b$. Is this a desired behaviour that using only the intrinsic reward allows achieving a better performance than the imitation reward? Does this not imply that the selected 6 Atari tasks can be solved by only doing exploration?

- In line 41, your citation of GAIL is wrong.
- No number is bold in the Qbert line of Table 1.
- In the result section, you only include Table 1 in the main text but spend the majority of the text discussing the results on Tables 9 and 10 in the appendix. Can you reorganize the paper to make the text and table better align with each other?

### Questions
Majors:
- As mentioned in the weakness part, the biggest concern from me is the formulation. Could you please elaborate why, intuitively, adding an intrinsic reward term to the GAIL objective (Eq. 3.3) can help the policy to achieve a better performance than the expert? I think to achieve a better performance than the expert, the agent must understand the intention of the expert and extrapolate it. I cannot see how an intrinsic reward guarantee to help for this. Maybe there are some hidden assumptions about the task or the demonstrations?
- In the introduction, you list the formulation of the problem itself as one of the contribution, but you write the formulation in the Preliminary section. Could you elaborate what is the difference between the formulation in this paper with previous works, for example [1]?
- From the results in Table 1, ILDE w/o $r^k$ is much better than ILDE w/o $b$. Is this a desired behaviour that using only the intrinsic reward allows achieving a better performance than the imitation reward? Does this not imply that the selected 6 Atari tasks can be solved by only doing exploration?

Minors:
- In line 41, your citation of GAIL is wrong.
- No number is bold in the Qbert line of Table 1.
- In the result section, you only include Table 1 in the main text but spend the majority of the text discussing the results on Tables 9 and 10 in the appendix. Can you reorganize the paper to make the text and table better align with each other?

[1] Yu *et al.*, Intrinsic Reward Driven Imitation Learning via Generative Model, ICML 2020

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
4

### Summary
This paper focuses on imitation learning from limited demonstrations, where the goal is to learn a policy that either imitates the expert directly or learns a policy that is better than the expert. Prior techniques focused on exploration-based approaches for this problem, with the goal of designing useful intrinsic motivation bonuses to incentivize the agent to explore its (large) state space to ultimately learn a better-than-expert policy. This paper proposes the use of two bonuses: an exploration bonus that encourages the agent to visit novel state-action pairs in the environment, and another bonus that incentivizes the agent to deviate from the expert trajectories themselves. The authors propose theoretical justification of their method, achieving a poly(H, T) regret w.r.t. the true expert.

### Strengths
I am not the best theoretician by any means, but this paper is very theoretically sound. I think the regret analysis was done well, which is the main theoretical contribution of this work.

Experimental results were quite expansive and good. The authors seemed to ablate the right variables (e.g. what happens if we turn our state-action based exploration bonus off, what happens if we turn our imitation reward off) to analyze exactly what is different about their method compared to a standard baseline (e.g. GIRIL). In terms of domains of interest, the authors also covered a variety of benchmarks across a variety of RL benchmarks, including Atari and MuJoCo tasks.

### Weaknesses
It would be interesting to see how just the state-action exploration bonus does as well (e.g. the state entropy bonus stays, but the GIRIL-like intrinsic reward is not used). To me, both of these methods seem to be doing the same thing (one on the state-action space as a whole, and one focusing on the expert trajectories), so it would be good to see an experiment that keeps the state entropy bonus, doesn't use the demonstration-based intrinsic reward, and keeps the standard imitation learning reward, which I understand is different from GIRIL (where their intrinsic reward bakes in both the true demonstration actions and the demonstration-based intrinsic reward). This is pretty minor, but would love to see this myself.

### Questions
I don't have any additional questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel imitation learning algorithm, ILDE (Imitation Learning with Double Exploration). The goal of ILDE is to achieve beyond-expert performance by improving sample efficiency and addressing the challenges posed by limited demonstrations. ILDE implements two exploration strategies: (1) optimistic policy optimization with an exploration bonus that encourages the exploration of high-uncertainty state-action pairs, and (2) curiosity-driven exploration that rewards states deviating from the expert’s demonstration trajectory. Empirical results show that ILDE outperforms state-of-the-art algorithms in terms of sample efficiency and return on Atari and MuJoCo tasks. The authors also provide a theoretical framework, showing that ILDE’s regret grows sublinearly with the number of episodes.

### Strengths
1. This paper proposes a novel ILDE framework, which combines optimistic exploration with curiosity-driven exploration for imitation learning.

### Weaknesses
1. **Theoretical Limitations**
    1. First, the assumptions made in this paper are overly strong. In Assumption 4.2, the authors directly assume that the statistical error resulting from using a finite set of expert demonstrations is small. This assumption is both strong and unreasonable, as a primary goal in imitation learning theory is to examine the relationship between the number of expert trajectories and the error bound [1]. Specifically, the assumption that the error $\epsilon_E$ is small without relating it to the number of expert trajectories $n$ makes the theoretical results less informative. Additionally, Assumption 4.1 presumes that the loss function is convex with respect to the reward parameters, making the reward optimization a straightforward online convex optimization problem. In practice, however, the reward optimization problem may be highly non-convex due to the use of neural networks, and this assumption significantly limits the applicability of the theoretical results to practical scenarios involving neural networks or other non-convex function approximators.
    2. Second, the proposed method in Algorithm 1 requires knowledge of the entire MDP transition function. In line 7 of Algorithm 2, computing the intrinsic reward $\mathcal{L}_{\tau^{E}, h}$ depends on the true transition function, specifically requiring the expectation over next states sampled from the true transition function. This is problematic because if the true transition function were known, online exploration would no longer be necessary, and the core challenge of imitation learning in unknown environments would be bypassed.
2. **Experimental Limitations**
    
    In the experiments, this paper does not compare its approach with current state-of-the-art (SOTA) imitation learning (IL) methods. In Atari games, the SOTA method is IQ-Learn [2]. In MuJoCo environments, the SOTA methods include IQ-Learn and HyPE [3]. The absence of these methods in the experiments makes it unclear whether the proposed approach outperforms current methods.
    
3. **Unsubstantiated Conjecture**
    
    The goal of this paper is to develop an IL approach capable of achieving performance beyond the expert level. To this end, the paper is based on the conjecture that optimizing the uncertainty-regularized loss shown in Eq. (3.6) enables performance surpassing the expert’s. However, no evidence or justification is provided to support this conjecture. Furthermore, the assumption that seeking novelty aligns with the target task is not always valid, and in many practical scenarios, novelty-seeking behavior can raise safety concerns. The paper does not address this potential misalignment or provide a formal definition of this assumption, which makes it unclear how the proposed algorithm can achieve beyond-expert performance in principle.

### Questions
Typos:

1. In line 41, the reference of GAIL is wrong.
2. In line 256, “desccent” should be descent.

### Soundness
1

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
This paper proposes a new framework for imitation learning, which succinctly, leverage informed interaction to improve policy performance in the absence of an abundance of expert demonstrations. In particular, two exploration strategies are considered: optimistic policy optimization with an exploration bonus, and curiosity-driven exploration of states beyond the demonstration trajectories. The authors provide extensive theoretical justification and prove performance bounds to support their algorithm, and also provide empirical results to support their method, testing metrics in both sample efficiency and final performance.

### Strengths
* The proposed method seems novel and to be well-grounded in theoretical derivations. While learning from limited expert demonstrations has been explored in prior work, this work introduces a unique combination of two exploration strategies to tackle this regime. 
* The paper provides solid theoretical foundations for ILDR, and is thorough in stating their assumptions. As noted, Theorem 4.7 is the first theoretical guarantee for imitation learning in MDPs with nonlinear
function approximation.
* The problem is well motivated, and algorithms are well presented. Particularly, the integration of optimistic policy optimization and curiosity-driven exploration are clearly labeled. The empirical experiments also do a good job ablating on these two exploration models, highlighting both are needed for best performance.
* Relatedly, the empirical results are promising, demonstrating that ILDE achieves better performance over baselines on metrics such as final reward, # games better than expert, and average performance against experts over the considered environments.

### Weaknesses
 * There are more modern baselines that come to mind when looking at the few expert-demonstration regime, such as IQLearn [1], which also demonstrate reasonable performance in the low expert-data regime, or the model-free and/or model-based inverse RL algorithms in Hybrid Inverse Reinforcement Learning [2], which also prove competitive sample complexity bounds. The experiments section could benefit from slightly more baselines.
* Although the theoretical framework is well-explained, the practical implementation details could use a bit more clarity. In particular, how are exploration bonuses computed in practice, and how much work is involved in hyperparameter search (i.e. the original ranges considered, type of search used, and how the authors recommend searching over these hyperparameters when faced with a new environment/dataset)? (Relatedly, see Question 2 below.) The paper mentions using k-NN for state entropy calculation, but it's unclear how the neighborhood size 'k' is chosen and whether this is sensitive to the choice of k. Furthermore, the implementation details of the conditional VAE for the novelty bonus are not fully specified, such as the architecture and training procedure.
* Relatedly, I personally felt the tradeoff between exploration and imitation could have been explored a bit more thoroughly in the paper. For example, I'm curious how algorithms may perform in situations where the demonstrations may not be fully optimal. (Relatedly, see Question 3 below.) The paper does not discuss how the algorithm would behave if the expert demonstrations are suboptimal or contain noisy actions. This is a crucial aspect to consider for real-world applicability, as expert demonstrations are rarely perfect.
* The ILDR-NPG variant as I understood it seems susceptible to incur large computational costs due to using natural policy gradients for policy optimization. The paper doesn't seem to fully address this issue/potential ways to mitigate it.

### Questions
1. While the authors provide a practical instantiation, I am under the impression that proposed ILDE framework should be flexible, and can be generalized to other empirical instantiations. If this is true, have the authors explored applying these exploration bonuses on top of existing methods and seeing how they fair?
2. How sensitive is ILDE to the choice of hyperparameters, such as the exploration bonus weight and the learning rate for curiosity-driven exploration? What is the amount of hyperparameter tuning that one had to search over in order to reach the optimal performance for these exploration bonus trainings? 
3. How does ILDE perform in environments where the expert demonstrations are noisy or imperfect? What is the consequence of data quality on the two exploration bonuses, and how much additional tuning may be needed to stabilize performance? This would provide insight into ILDE’s robustness in real-world settings.
4. I'm wondering whether ILDE could be combined with techniques in model-based (inverse) reinforcement learning to further improve sample efficiency?

### Soundness
3

### Presentation
4

### Contribution
3
