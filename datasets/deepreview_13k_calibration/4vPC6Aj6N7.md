# Multi-Agent Reinforcement Learning from Human Feedback: Data Coverage and Algorithmic Techniques

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
We initiate the study of Multi-Agent Reinforcement Learning from Human Feedback (MARLHF), exploring both theoretical foundations and empirical validations. We define the task as identifying Nash equilibrium from a preference-only offline dataset in general-sum games, a problem marked by the challenge of sparse feedback signals. Our theory establishes the upper complexity bounds for Nash Equilibrium in effective MARLHF, demonstrating that single-policy coverage is inadequate and highlighting the importance of unilateral dataset coverage. These theoretical insights are verified through comprehensive experiments.
To enhance the practical performance, we further introduce two algorithmic techniques. 
(1) We propose a Mean Squared Error (MSE) regularization along the time axis to achieve a more uniform reward distribution and improve reward learning outcomes. (2) We utilize imitation learning to approximate the reference policy, ensuring stability and effectiveness in training.
Our findings underscore the multifaceted approach required for MARLHF, paving the way for effective preference-based multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the important and timely problem of multi-agent reinforcement learning from human feedback (MARLHF). The authors examine both theoretical and practical aspects of MARLHF, demonstrating that single policy coverage is insufficient and emphasizing the need for unilateral dataset coverage. To address the issues of sparse and spiky reward learning typical in standard RLHF, they propose two primary techniques: (1) mean squared error regularization to promote uniform reward distribution, and (2) an additional reward term based on state-action pair density within the dataset to introduce pessimism, using an imitation learning-based approach for density modeling. The final policy is then trained using the VDN algorithm. Overall, this MARLHF approach represents a significant step toward preference-based reinforcement learning in multi-agent systems.

### Strengths
* This paper makes novel contributions to RLHF within multi-agent systems by framing the task as finding a Nash equilibrium in general-sum games and introducing innovative techniques for reward regularization and dataset distribution-based pessimism.
* The theoretical results are comprehensive and well-justified, effectively supporting the paper’s claims.
* The paper is generally well-written and easy to follow.

### Weaknesses
 * The empirical validation of the approach is limited, as the paper only includes experiments on three simple MPE environments. Since the authors utilized JAXMARL, testing on more realistic and complex environments from the JAXMARL API, such as Overcooked, Hanabi, or StarCraft, would strengthen the paper’s claims. The current environments, while useful for initial testing, lack the complexity to fully demonstrate the method's robustness in more challenging scenarios with longer time horizons and more intricate agent interactions. Specifically, the limited action and state spaces in the MPE environments might not fully expose potential issues related to reward function approximation and policy learning.
* The comparison with MARL baselines is insufficient, focusing only on VDN despite its known limitations in representation capacity. Conducting ablation studies with other MARL algorithms, such as MAPPO[1], IPPO[2], and QMIX[3], would provide more validations. The choice of VDN, a relatively simple algorithm, might not fully reveal the potential of the proposed reward shaping and pessimism techniques when combined with more sophisticated MARL methods. Furthermore, the lack of comparisons with other offline MARL algorithms limits the assessment of the method's performance in the offline setting.

### Questions
1. Why was VDN specifically chosen as the base MARL algorithm, given its known limitations in representation capacity? How would the proposed approach perform with more advanced MARL algorithms like MAPPO, IPPO, or QMIX?
2. Given that the experiments were conducted only on MPE environments (Spread-v3, Tag-v3, Reference-v3), how would the method perform on more complex MARL benchmarks? What challenges do you anticipate, and how sensitive might performance be to the choice of hyperparameters $\alpha$ and $\beta$?
3. What policy was used to generate responses for collecting preference feedback?
4. How was the preference feedback collected? Was it synthetic, based on true environment rewards, or did it come from real human preferences? These details are crucial for reproducibility, a deeper understanding of the approach, and identifying potential biases in the preference data.
5. The inherent dependence between the policy used to train the reward model and the policy being learned is not addressed in the paper. For instance, in the single-agent setting (see [4]), this dependence can be significant. How does the proposed approach handle this issue?
6. How does the quality of the learned reward function vary with different levels of expertise and sparsity in preference feedback?

[1] Yu, Chao, et al. "The surprising effectiveness of ppo in cooperative multi-agent games." Advances in Neural Information Processing Systems 35 (2022): 24611-24624.

[2] De Witt, Christian Schroeder, et al. "Is independent learning all you need in the starcraft multi-agent challenge?." arXiv preprint arXiv:2011.09533 (2020).

[3] Rashid, Tabish, et al. "Monotonic value function factorisation for deep multi-agent reinforcement learning." Journal of Machine Learning Research 21.178 (2020): 1-51.

[4]  Chakraborty, Souradip, et al. "PARL: A Unified Framework for Policy Alignment in Reinforcement Learning from Human Feedback." The Twelfth International Conference on Learning Representations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the problem of trying to learn human preferences (this behaviour is better than that behaviour) in a multi agent RL setup. In this case satisfactory learning means a Nash-equilibrium is reached between all policies. The authors positions the paper as an initial study into Multiagent Reinforcement Learning from Human Feedback.

The paper shows how pure expert policies are not always the best for maximising overall score, and that mixing in less expert policies in some cases causes an overall higher score to be reached in the MARLHF case. This is proved, theoretically. They also show that it is often easier to learn what policies score higher by having unilaterally divergent policies acting in the environment, where a single agent is using a sub-optimal policy. The authors call this approach unilateral coverage. By having this unilateral agent in the environment it becomes simpler to observe what policies may be truly optimal within the environment. In addition upper complexity bounds are established for Nash Equilibrium in effective MARLHF.

The process to implement this approach is to learn a reward function from a preference dataset while mitigating extrapolation errors with a pessimism term and then determining a final policy. Human Feedback is itself simulated using the Bradley-Terry-Luce model to rank solutions.

The authors make 2 particular contributions to implement their insights:
Applying MSE regularisation to the training data to distribute rewards more evenly across timesteps, which helps to avoid temporal concentration. This essentially takes the sparse reward signals from the Bradley-Terry-Luce model and spread them out to produce reward over more timesteps.
Dataset distribution-based penalties are used to constrain exploration to known regions of the state space

Their empirical evaluation spans three multi-agent scenarios: cooperative target coverage, coordinated pursuit, and communication-dependent navigation. They show that incorporating imperfect policies is helpful for learning higher scoring policies during training. In harder tasks, unilateral coverage and diversity become more important and more diverse datasets led to lower variance in training outcomes. The authors also introduce a principled standardization technique for hyperparameter tuning across environments.

### Strengths
In terms of the proofs, there is a simple but convincing proof by counterexample provided for theorem 1 (not contradiction, as stated).
There is an explicit bounds found on the Nash-gap. 

Hyperparameters used in the training are provided, multiple seeds are used and results that don’t support the desired conclusion are presented. Multiple environments are tested, and clear ablation studies are done.

The paper makes an interesting theoretical contribution by establishing fundamental results about Multi-Agent Reinforcement Learning from Human Feedback (MARLHF). The authors prove why single-policy coverage is insufficient and demonstrate that unilateral coverage is both necessary and sufficient for learning Nash equilibria. These theoretical foundations are presented with clear proofs that are well constructed. These theoretical results then explicitly inform the design of the framework which is clearly stated and explained.

The empirical work is comprehensive and well-designed, testing their approach across three distinct multi-agent scenarios that each present different challenges (cooperative target coverage, coordinated pursuit, and communication-dependent navigation). The experiments validate both the theoretical insights about dataset coverage and the effectiveness of their algorithmic innovations. Their ablation studies are thorough and give clear evidence for the value of their MSE regularization and dataset distribution-related penalties. The authors also introduce a practical standardization technique for hyperparameter tuning that works across different environments.

The clarity of the experimental setup makes the work also highly reproducible

### Weaknesses
The main weakness is that despite the paper's title and framing, there is no actual human feedback involved in any of the experiments. Instead, the authors simulate preferences using the Bradley-Terry-Luce model based on known reward functions from the environments. This is a significant limitation because real human preferences are likely to be much noisier, inconsistent, and potentially non-transitive compared to their simulated preferences. The paper would be more accurately titled as "Multi-Agent Reinforcement Learning from Simulated Preferences" or similar, and should more explicitly acknowledge this limitation and discuss how their approach might need to be modified for real human feedback.

While thorough, the theoretical results rely heavily on assumptions that may not hold in practice. The paper assumes linear Markov games and works with known feature mappings, but doesn't discuss enough how these assumptions might limit real-world applicability. Additionally, although the paper proves that their theoretical algorithm converges to Nash equilibria, the practical implementation uses different algorithms (VDN-based) with no theoretical guarantees. This gap between theory and practice is not sufficiently discussed. The paper also doesn't explore whether the Nash equilibrium is actually desirable in all cases - in some scenarios, other solution concepts might better align with human preferences. This again is one of the major weaknesses with the unclear framing.

The experimental evaluation, while systematic, is limited to relatively simple environments in the Multi-Agent Particle Environment (MPE) framework. These environments, while useful for testing basic concepts, are far simpler than real-world multi-agent scenarios. The paper doesn't adequately discuss how their approach might scale to more complex environments or to scenarios with larger numbers of agents. Their results showing that mixed-skill policies can outperform pure expert policies raise questions about whether their reward modeling approach is capturing the true objectives of the tasks. It's unclear if the learned reward function accurately reflects the underlying task goals, especially when suboptimal policies lead to better overall performance.

Another important weakness in the paper's empirical evaluation is the absence of statistical significance testing. Although results with means and standard deviations across 5 random seeds are given, they don't perform any statistical analysis to validate the conclusions. This is particularly problematic given the small sample size - with only 5 seeds, the reliability of their comparisons is questionable. The paper lacks hypothesis tests. This makes it difficult to determine if the reported differences between approaches are statistically significant, especially in cases where the differences appear small relative to their standard deviations. For example, in Spread-v3, it's unclear whether the difference between "Mix-Unilateral" (-20.98 ± 0.56) and "Mix-Expert" (-21.11 ± 1.16) is meaningful. The lack of statistical rigor undermines the strength of the paper's empirical conclusions and the claims made about the benefits of their approaches.

### Questions
How would your approach need to be modified to handle inconsistent or non-transitive preferences that often occur with real human feedback?
Why do you call the paper MARLHF when there is clearly no HF?
The practical implementation differs significantly from the theoretical algorithm - can you explain this gap and discuss whether any theoretical guarantees carry over?
Given the relative simplicity of the tasks, why were only 5 random seeds used for the experiments?
Why weren't statistical significance tests performed to validate the comparative results?
How well does your approach scale with increasing numbers of agents? 
In cases where mixed-skill policies outperform pure expert policies, can you verify that this reflects genuine improvement rather than issues with reward modeling?
Have you tested MARL algorithms other than VDN?

### Soundness
3

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
This study introduces Multi-Agent Reinforcement Learning from Human Feedback (MARLHF) to find Nash equilibria from preference-based data with sparse feedback. A key technique in this paper is to use the MSE regularization for uniform rewards and a pessimism-based penalty—to improve stability and performance, enabling more effective preference-based multi-agent systems.

### Strengths
The theoretical analysis presented in this paper is solid and clear, providing a sound theoretical bound for the proposed method to solve MARLHF. Additionally, the authors conduct various experiments to demonstrate the effectiveness of the proposed method, even when applied to offline datasets lacking uniform coverage.

### Weaknesses
1. The discussion section on related works is incomplete. The authors should provide a more thorough discussion of recent advancements in MARL and offline RLHF. Specifically, the paper should discuss how the proposed method compares to recent approaches in decentralized multi-agent RL with function approximation [1], sample-efficient multi-agent RL [2], and methods that address overoptimization in RLHF [3] and value-incentivized preference optimization [4]. Additionally, the paper emphasizes the importance of incorporating reward regularization in the objective function for the current task. However, similar ideas have been adopted in different contexts and should be discussed carefully [5,6], including reward-biased maximum likelihood estimation and Bellman-consistent pessimism.

2. The current experiments primarily showcase different variants of the proposed methods and include an ablation study. Could the authors include more baseline methods for comparison? Specifically, it would be beneficial to compare against established offline MARL algorithms and preference-based learning methods. Additionally, incorporating more tasks (e.g., five tasks) would strengthen the findings and provide greater convincing power for readers. The current set of experiments, while thorough in ablating the proposed method, lacks breadth in terms of task diversity and comparison to existing baselines.

3. The theoretical analysis currently focuses solely on the linear function approximation setting, which may not be realistic given the use of neural networks in the experiments. Could the authors extend the analysis to accommodate general function approximations, or clarify how the experimental setup meets the requirements of linear function approximation? The gap between the theoretical assumptions and the practical implementation using neural networks raises concerns about the applicability of the theoretical results.

4. In Line 300, it seems that someone even left comments colored in blue, which may leak the information of the authors. It is suggested that the authors should double-check the submitted draft to avoid this careless mistake.

5. In Line 276, the reference to "an approximate Nash equilibrium policy" in the theorem lacks clarity, as it does not illustrate the approximation error in relation to the size of the offline dataset. The authors should expand on the implications of the derived bound and compare their results with existing theoretical findings in the offline RL and MARL literature, specifically addressing how the bound scales with the amount of offline data and how it compares to existing convergence rates in similar settings.

### Questions
1. This paper analyzes the RLHF setting; however, the definition of the performance metric remains unchanged from the RL setting without KL regularization. Could the authors provide further clarification on this?

2. Could the authors highlight the novel aspects of the current theoretical analysis that differentiate it from the offline MARL setting?

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
3

### Summary
The paper seeks to establish theoretical foundations and make empirical validations for the new research field, Multi-Agent Reinforcement Learning from Human Feedback (MARLHF). The core theoretical contribution is proving that single-policy coverage is insufficient for learning approximate Nash equilibrium policies and that unilateral policy coverage is sufficient to do so. The empirical contribution lies in two techniques, namely, reward regularization which smoothens the reward distribution, and dataset distribution-based pessimism which handles the extrapolation errors. The experiments are designed to verify the correctness of the theoretical claims and the effectiveness of the empirical techniques.

### Strengths
- I am not an expert in RLHF, but to my best knowledge, this is the first work for aligning multi-agent systems with human feedback.
- The theoretical claims are concise and seems to be practically useful.
- The experiments are well designed for the purpose of verifying the proposed theoretical claims and empirical techniques.

### Weaknesses
The experiments are conducted on a limited range of tasks, which may not be sufficient to verify the generality of the theoretical claims and empirical techniques.

As far as I can tell, there are no other obvious weaknesses of this paper. Potential weaknesses concerning the consistency between the experiment results and the corresponding conclusions are listed as questions below.

- Figure 1: $\pi_{ref}$, while mentioned in the caption, doesn't seem to be appearing in the figure. Do you mean $\pi_b$?
- What does the blue text mean in Lines 300-301?
- Table 2: The claim in the capture, namely, "in more challenging environments, such as Tag-v3, dataset diversity plays a substantially more significant role", seems inconsistent with the data in the table, where both the mean and the variance of the return of Tag-v3 reach their best in the Pure-Expert dataset which has the least diversity.
- Table 2: The claim in Lines 419-420, namely, "In more challenging tasks, as reflected by higher MSE, the importance of unilateral coverage and diversity becomes more pronounced.", does not seem very obvious from the table, where the diversified and the mix-unilateral dataset achieve the best performance when (Spread-v3 for Mix-unilateral and Reference-v3 for Diversified) the corresponding MSE is low.
- Table 3: Why does setting $\beta$ to a magnitude as large as 100 yield such good results? Doesn't the penalty term completely dominate the loss? Further, it seems strange to me that setting $\beta$ across such a wide range (from 1 to 100) can yield almost the same result, especially when the dataset is the diversified one which contains a large fraction of low-return trajectories.
- Figure 2: What does the x-axis represent?

### Questions
- Figure 1: $\pi_{ref}$, while mentioned in the caption, doesn't seem to be appearing in the figure. Do you mean $\pi_b$?
- What does the blue text mean in Lines 300-301?
- Table 2: The claim in the capture, namely, "in more challenging environments, such as Tag-v3, dataset diversity plays a substantially more significant role", seems inconsistent with the data in the table, where both the mean and the variance of the return of Tag-v3 reach their best in the Pure-Expert dataset which has the least diversity.
- Table 2: The claim in Lines 419-420, namely, "In more challenging tasks, as reflected by higher MSE, the importance of unilateral coverage and diversity becomes more pronounced.", does not seem very obvious from the table, where the diversified and the mix-unilateral dataset achieve the best performance when (Spread-v3 for Mix-unilateral and Reference-v3 for Diversified) the corresponding MSE is low.
- Table 3: Why does setting $\beta$ to a magnitude as large as 100 yield such good results? Doesn't the penalty term completely dominate the loss? Further, it seems strange to me that setting $\beta$ across such a wide range (from 1 to 100) can yield almost the same result, especially when the dataset is the diversified one which contains a large fraction of low-return trajectories.
- Figure 2: What does the x-axis represent?

### Soundness
2

### Presentation
2

### Contribution
3
