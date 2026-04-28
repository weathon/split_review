# Risk Informed Policy Learning for Safer Exploration

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Reinforcement learning algorithms typically necessitate extensive exploration of the state space to find optimal policies. However, in safety-critical applications, the risks associated with such exploration can lead to catastrophic consequences. Existing safe exploration methods attempt to mitigate this by imposing constraints, which often result in overly conservative behaviours and inefficient learning. Heavy penalties for early constraint violations can trap agents in local optima, deterring exploration of risky yet high-reward regions of the state-space. To address this, we introduce a method that explicitly learns state-conditioned safety representations. By augmenting state features with these safety representations, our approach naturally encourages safer exploration without being excessively cautious, resulting
in more efficient and safer policy learning in safety-critical scenarios. Empirical evaluations across diverse environments show that our method significantly improves task performance while reducing constraint violations during training, underscoring its effectiveness in balancing exploration with safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the RIPL framework, which integrates state-conditioned risk representations into the agent’s state features. These risk representations help guide exploration more efficiently and reduce the risk of constraint violations without being overly conservative. Empirical results demonstrate that RIPL improves both task performance and safety.

### Strengths
1. The idea of state-conditioned risk representations is intuitive and reasonable, and is a novel approach in the community of safety RL.
2. The method is sound and shows significant improvements in multiple environments, and the transferability of the risk models are also tested.
3. The structure of the paper is clear and the writing is easy to follow.

### Weaknesses
1. The related works in the recent two years seem to be missing, and the latest baselines that the author compared with are CSC and TRPO-PID, which were published in 2020. Are there other more recent work in the safty RL literature? If time is not enough for experimental comparison, that's fine (though preferred); It would be nice to mention the most recent advances and the advantages of the proposed method compared with them. (I am not an expert in safety RL, but would love to see clarifications on whether there is/is not more recent works)
2. As is discussed in the limitation, the true relation between states' risks might not be genuinely captured (long-horizon dependency etc.). I agree that it is an important aspect to investigate about in future work, but how well can the current risk model reflect the risk? For example, consider providing a visualization of the output distribution of the risk model w.r.t. the constrained states. It'd be nice to have illustrations in the continuous case, similar to Fig.3.

### Questions
1. How sensitive does RIPL perform as we set different bin sizes for risk? How do we determine this value?
2. I think transfering the risk model between tasks is an interesting point. Currently, the authors freeze the risk model on the target task. Would it also be possible (and more reasonable) to fine-tune it in the target environment?

### Soundness
3

### Presentation
3

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
The main idea of the paper is to augment the state space with a distance to “unsafe” regions and use this augmented state-space to learn safe RL policy. The paper presents a number of experiments and comparisons to safe RL methods as well as an ablation study showcasing different aspects of the algorithm.

### Strengths
1. The paper is very well-written
2. The motivational example is great! I would recommend getting the message a bit more fleshed out. That is, that adding a distance measure in this example with sparse rewards made a huge difference for training. The paper tries to do the same trick in safe RL, where we often treat safety similarly to RL in the sparse reward setting - either safe or not safe.
3. The paper has a great ablation study

### Weaknesses
1. The CPO baseline is fine, but not amazing. I think it would be good to use at least one more baseline for demonstration. There are a few implementations in https://github.com/PKU-Alignment/safety-gymnasium
2. Ideally, it would be good to see more risk measure distances compared to the presented one.
3. The paper 
   > Jiang, H., Mai, T., Varakantham, P., & Hoang, M. H. (2023). Solving Richly Constrained Reinforcement Learning through State Augmentation and Reward Penalties. arXiv preprint arXiv:2301.11592.

is another example of state-space augmentation for safety.
4. The authors use a time-dependent risk measure. However, we have a different risk measure - accumulated costs. We more or less know that when the accumulated costs reach a certain level then we are likely to be unsafe soon. Why not use the costs as distance? Is there a benefit of using this specific risk measure?

### Questions
1. The paper 
   > Jiang, H., Mai, T., Varakantham, P., & Hoang, M. H. (2023). Solving Richly Constrained Reinforcement Learning through State Augmentation and Reward Penalties. arXiv preprint arXiv:2301.11592.

is another example of state-space augmentation for safety.

2. The authors use a time-dependent risk measure. However, we have a different risk measure - accumulated costs. We more or less know that when the accumulated costs reach a certain level then we are likely to be unsafe soon. Why not use the costs as distance? Is there a benefit of using this specific risk measure?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a safe RL method based on augmenting the state space with a learned safety representation, which is referred to as Risk-Informed Policy Learning. This state-conditioned representation is learned during training, and captures the probability of safety violations in each of the next several timesteps. The goal of incorporating this representation is to learn policies that satisfy safety constraints without being overly conservative in terms of task performance. Experiments across 4 different tasks evaluate task performance and safety metrics, where the learned state representation is combined with several different safe RL algorithms.

### Strengths
- **[S1] Important topic:** Safe / Constrained RL is an important topic, and training policies that satisfy safety constraints without being overly conservative is an important goal.
- **[S2] Compatible with many RL algorithms:** The proposed method augments the state with a learned representation, so it can be applied to many different RL algorithms. This is also demonstrated in the experiments, where it is applied to 4 different safe RL algorithms.
- **[S3] Experiments across diverse set of tasks and several base algorithms:** Experiments consider manipulation, locomotion, and navigation tasks, and the proposed state representation is combined with 4 different safe RL algorithms. Additional ablation analyses are also included, which consider different input modalities and alternate choices for the learned safety representation.

### Weaknesses
 **[W1] Confusing use of the term “risk” throughout the paper**
- A risk measure is a function that maps a random variable to a scalar value (e.g., CVaR). Risk-sensitive / risk-aware / risk-averse RL methods typically apply a risk measure over a distribution of future returns. This is very different from the ideas proposed in this work, where a “risk function” is mapping states to a distribution over timesteps. I strongly suggest that the authors change the term “risk-informed” to something different that better reflects what is being proposed in this paper.

**[W2] The definition of the risk model is inconsistent across the paper**
- The risk model is defined as a probability distribution over the number of steps to failure (i.e., constraint violation in (2)) in several places (lines 60-61, 172-173, 212, 256-257). I believe this formulation makes the most sense, as it captures information about constraint violation similar to the state augmentation proposed in [1]. However, in other places (lines 221-226, 461, 719-720, 791-792) the risk model is described as a probability distribution over the number of steps to an unsafe state (i.e., a state where $c=1$ but not necessarily a constraint violation).

**[W3] Experimental analysis is not clearly presented**
- The safety metrics presented in the Experiments section are difficult to interpret. I cannot tell what percentage of trajectories end in safety violations in the AdroitHandPen and Ant tasks based on the #failures metric, and I cannot tell whether the safety constraint is satisfied in PointGoal1 and PointButton1 tasks based on the Cost-rate metric. In Figure 5, it does not look like the safety constraint of $\beta=10$ is satisfied for these tasks. See [Q1].
- There is not enough detail on how the safety representation is implemented in the Experiments. There might be some information in Appendix A.6, but it is difficult to understand. See [Q1].
- I do not understand how the results in Figure 7 support the claims about transferability. Policy transfer works well both with and without the RI representation, and it does not look like transferring the risk model leads to better performance compared to just training RI-CPO from scratch as shown in Figure 5. See [Q1].
- I do not understand some of the presentation choices in Figures 5-7: returns and costs are shown for different numbers of total timesteps; some RI algorithms are shown while others are not; some algorithms show performance throughout training while others are just horizontal lines.

**[W4] Appendix is not well-written and does not present significant results**
- The results in the Appendix rely on unusual assumptions and do not provide significant insights into the main problem considered in the paper.
- Proposition 0.3 is not new. See Theorem 3 in [2].
- Assumptions / proofs are often not explained in an appropriate amount of detail: the definition of $r(s)$ in Proposition 0.1 does not seem to be directly used in the proof; $\eta$ introduced in lines 928-929 does not appear to be used, as (19) looks to just be a repeat of (18).
- Several incorrect, hardcoded equation references. Strange numbering of propositions.

### Questions
**[Q1] Experiment clarifications**
- Please provide the average total cost per trajectory for each experiment, and how this relates to the safety constraint budget $\beta$.
- Please describe the implementation of the risk model in more detail. What horizon is used? What network architecture is used? Other key details?
- Could you please provide more detail on how Figure 7 (and the RI-CPO training from scratch in Figure 5) support the claim about transferability? I also think that RI-CPO should be included in Figure 7 to more easily compare against it without needing to look back to Figure 5. 

**[Q2] Choice of RL algorithms**
- Why is CPO used as the main safe RL algorithm for most of the experiments? More recent safe RL algorithms have been shown to outperform CPO, such as CVPO [3] and LAMBDA [4]. 
- The approach in [1] also seems relevant to this work, since it incorporates information about safety constraint violation through state augmentation (this work considers a more detailed, learned state augmentation while [1] uses the remaining budget).

**Minor:**
- cost function notation is inconsistent: $c$ vs. $C$ vs. $\mathcal{C}$
- an index variable $i$ appears in (2) but is not used anywhere
- incorrect column / row references in lines 191-192
- floating quotation mark in the top left of Figure 3
- colors are not defined in Figures 3 and 9
- incorrect, hardcoded equations throughout Appendix
---

**References:**

[3] Liu et al. Constrained Variational Policy Optimization for Safe Reinforcement Learning. In ICML 2022.

[4] As et al. Constrained Policy Optimization via Bayesian World Models. In ICLR 2022.

### Soundness
3

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
4

### Summary
In this paper, the authors propose a new reinforcement learning framework with a specific focus on "safe exploration." The proposed framework, named RIPL, can be described as a data-augmentation method that introduces additional risk-related representations into the original state-space, leading to more efficient safe policy learning. The idea is intriguing, and the toy experiments illustrate the motivation behind it well. However, the paper faces some issues with clarity. Additionally, the experimental results are limited and not sufficiently convincing. I hope the authors can address the concerns I have outlined below.

### Strengths
1. The idea presented in this paper is interesting, and the implementation looks simple and practical.
2. The proposed framework, RIPL, is flexible and can easily be combined with many existing online safe RL algorithms.
3. The toy experiments do a good job of showing the motivation behind the approach.

### Weaknesses
1. As the authors describe, $R_H(s)$ represents the probability that the agent will remain safe for the entire episode. However, this probability is highly dependent on the policy being used. In Appendix A, it is derived based on the specific policy, which raises a concern: how is the risk buffer collected and updated to train $R_H(s)$? If all new trajectories are collected without discarding old ones, the estimation will be inaccurate. On the other hand, if only on-policy trajectories are used, the approach is not safe and requires a large number of samples for convergence. The paper lacks a clear explanation of how this buffer is managed, and the implications of using potentially outdated data for risk estimation are not addressed.

2. A similar idea of learning risk-related value estimation has been proposed in [1], with several works following this approach to learn Safe Q via a safe-Bellman operator. This method offers more solid theoretical guarantees. The paper does not adequately differentiate its approach from these existing methods, particularly in terms of theoretical underpinnings and practical advantages. The discussion should more clearly articulate the novelty and benefits of the proposed method compared to established techniques.

3. The caption for Figure 3 is unclear and does not align with the figure, which could cause confusion. The discrepancy between the figure and its description undermines the clarity of the presentation.

4. The baseline algorithms used in the experiments seem somewhat outdated, and the number of experimental results provided is too limited to fully demonstrate the advantages of the proposed algorithm. The choice of baselines does not represent the current state-of-the-art in safe reinforcement learning, and the limited number of environments makes it difficult to assess the generalizability of the proposed method.

### Questions
1. In this paper, the authors frequently claim that the "RL agent overfits the negative samples." However, it is unclear whether this "overfitting" refers to the representations, Q-functions, or actions. In Column 1 of Figure 1, how does the training curve reveal this "overfitting problem"? Could the authors provide a more detailed explanation, along with additional evidence?

2. In the experiments, are the environments image-based or state-based? Since all environments provide both versions, it would be helpful to clarify this in the figure/table captions.

3. The experimental results provided are too limited to convincingly demonstrate the algorithm's effectiveness. Could the authors present more results from Mujoco (hopper, halfcheetah, walker2d), Adroit (hammer, door), and Safe Gym (Point/Car/Doggo goal/button/push 1/2)? If possible, including results from MetaDrive, which is arguably the most challenging environment for testing algorithms with safety considerations, would strengthen the case.

4. Given that the focus of this work is "Safe Exploration," it would be beneficial to emphasize the safety-related results during the exploration process. Could the authors offer more insights on this aspect?

5. The key point for RIPL is the risk buffer, but it is not adequately discussed in the main text. How is the buffer updated? A very large number is assigned to the risk-batch-size. Does this imply that it never updates and contains all information throughout the training process? If so, the risk-distance probability estimation must be inaccurate since the dataset's policies vary significantly. The estimation should differ substantially for different policies.

6. Since $R_H(s)$ is a distribution, its dimension varies significantly across environments with different horizons. What happens if the total horizon timestep is extremely large? In most cases, we consider infinite-horizon MDPs. How can RIPL generalize to that?

### Soundness
2

### Presentation
2

### Contribution
2
