# RL$^3$: Boosting Meta Reinforcement Learning via RL inside RL$^2$

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5

## Abstract
Meta reinforcement learning (meta-RL) methods such as \rlsquare have emerged as promising approaches for learning data-efficient RL algorithms tailored to a given task distribution. However, they show poor asymptotic performance and struggle with out-of-distribution tasks because they rely on sequence models, such as recurrent neural networks or transformers, to process experiences rather than summarize them using general-purpose RL components such as value functions. In contrast, traditional RL algorithms are data-inefficient as they do not use domain knowledge, but they do converge to an optimal policy in the limit. We propose \rlcubex, a principled hybrid approach that incorporates action-values, learned per task through traditional RL, in the inputs to meta-RL. We show that \rlcube earns greater cumulative reward in the long term, compared to \rlsquarex, while maintaining data-efficiency in the short term, and generalizes better to out-of-distribution tasks. Experiments are conducted on both custom and benchmark discrete domains from the meta-RL literature that exhibit a range of short-term, long-term, and complex dependencies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes RL^{3}, a novel method designed to enhance out-of-distribution (OOD) generalization and reduce meta-training time in meta-reinforcement learning (meta-RL) by integrating Q-estimates as additional input information for the meta-RL agent. The approach is implemented within the RL^{2} framework using transformers and is evaluated against RL^{2} across several benchmark tasks, including bandits, random MDPs, and gridworld.

### Strengths
- By adding Q-estimates, RL^{3} demonstrates improved efficiency over RL^{2} by requiring fewer PPO iterations and delivering better OOD performance on the selected benchmarks.

### Weaknesses
 - The experimental benchmarks focus on tasks with limited state spaces, which may restrict the applicability of the findings.
- Additional experiments on benchmarks with continuous state spaces, such as parameterized MuJoCo environments, are necessary to fully evaluate RL^{3}’s practical benefits over RL^{2} in terms of sample efficiency. The results based on tabular Q-function estimation in small state spaces do not directly indicate performance gains in more complex, real-world settings.

### Questions
1. Could cumulative reward plots over timesteps for each method be added to visualize meta-training progress?
2. What rollout length was used for RL^{2} in the experiments?

### Soundness
3

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
The paper presents a modification of meta-RL that incorporates additional information in the form of Q-estimates and state counts (and possibly other things as well) in order to improve training times, data requirements and possibly asymptomatic performance.  The approach is motivated with both empirical and theoretical arguments and validated on three artificial test domains.

### Strengths
1. The paper is *very* well-presented.  It was easy to understand and enjoyable to read.
2. The work is well-situated in the literature.
3. The paper provides both empirical and theoretical analyses that both motivate and justify the approach and design decisions.
4. Reported results are good and convince the reader that the proposed approach does provide (some of) the improvements hypothesized.  In particular, rewards are comparable or better than RL^2 while (meta)training time is decreased and OOD generalization seems also to be improved to some extent.

### Weaknesses
1. Experimental results are obtained on only toy problems.  It seems likely that the approach may not scale to more difficult/larger/real-world problems.  How does this work on a modestly more difficult domain like Atari, for example?
2. Some claims are not really supported.  For example, while the following statement from Sec. 5 seems like it could be true, there is no supporting evidence given: "VAMDPs can be plugged into any base meta-RL algorithm with a reasonable expectation of improving it."  As another example, it is also suggested that RL^3 might enjoy convergence guarantees, but this is also not supported in any way.
3. Performance improvement results seem like they don't include the overhead for computing q-values and state counts and are therefore potentially somewhat misleading.  This is addressed to some degree in the Sec 6, "Computation Overhead Considerations" subsection, but the discussion is too brief to be convincing; in particular, it is not clear that the claim will hold if scaled to larger/real-world problems.
4. The paper doesn't compare RL^3 with any other meta-RL approaches, other than RL^2, the one it modifies.

### Questions
1. Several places in the paper seem to suggest that one of the benefits of RL^3 will be asymptotic guarantees of convergence.  Does RL^3 in fact, gain asymptotic performance guarantees?  

2. In Section 4.2 it states, "In practice, we provide action advantages along with the max Q-value (value function) and optionally, standard errors, instead of just Q-estimates".  How critical is this to RL^3's success?  How much does this affect the results?

3. Sec 5 talks about using PPO as the metalearner, but earlier the paper talks about using a blackbox/NN for the metalearner.  I'm a bit confused here---is PPO used just for augmented RL^2?

4. Is Fig 3b comparing only meta-training time (as the last sentence of the MDP results subsection seems to suggest)? Or does it include all required computation?  How are the q-values and counts obtained? How much does this cost? How would this scale for larger/real-world problems?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents RL3, a novel approach to meta reinforcement learning that combines traditional RL techniques with meta-RL methods. The authors propose incorporating Q-value estimates from traditional RL as additional inputs to a meta-RL architecture, aiming to improve long-term performance and out-of-distribution generalization while maintaining short-term efficiency.

### Strengths
- Novel approach: The paper introduces an innovative method that combines the strengths of traditional RL and meta-RL, potentially addressing some limitations of existing meta-RL approaches.
- Theoretical foundation: The authors provide theoretical insights into why incorporating Q-value estimates can be beneficial, linking them to the optimal meta-value function.
- Improved performance: RL3 demonstrates better long-term returns and out-of-distribution generalization than RL2, while maintaining short-term efficiency.
- Flexibility: The approach can be applied to various meta-RL algorithms, not just RL2.

### Weaknesses
 - Limited baselines: The paper would benefit from comparing RL3 to more state-of-the-art meta-RL approaches beyond just RL2. In particular, comparing RL3 to hypernetwork-based approaches would provide valuable insights into its relative performance. Specifically, the lack of comparison to methods that explicitly learn task embeddings or use attention mechanisms limits the understanding of RL3's unique contributions. 
- Scope of experiments: The experiments are limited to discrete domains. As suggested, it would be valuable to see how RL3 performs in high-dimensional state spaces and with continuous action spaces. This limitation restricts the applicability of the current results to more complex, real-world scenarios. The absence of experiments in environments with partial observability also raises concerns about the robustness of the approach.
- Compute budget dependency: The performance of RL3 relative to RL2 seems to depend on the compute budget (H), which appears to be environment-dependent. The paper would benefit from providing guidelines or heuristics for selecting an appropriate range of H values for different environments. The current analysis lacks a systematic study of how H affects the trade-off between short-term and long-term performance.
- Generalizability: While the paper demonstrates improved out-of-distribution generalization, it's unclear how well this generalizes across a wider range of task distributions or more complex domains. The experiments do not explore the sensitivity of RL3 to changes in the task distribution's parameters, which is crucial for assessing its practical applicability.
- Computational overhead: The paper doesn't thoroughly discuss the potential computational overhead of computing Q-value estimates alongside the meta-RL process, which could be a significant factor in practical applications with high dimensional state spaces. The analysis should include a detailed breakdown of the computational costs associated with each component of RL3, including the value iteration step and the meta-learning process.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel hybrid approach, RL3, that integrates value-augmented MDP into meta reinforcement learning (meta-RL) frameworks RL2. The authors aim to address limitations in current meta-RL models, such as poor asymptotic performance and weak out-of-distribution (OOD) generalization. RL3 introduces object-level Q-value estimates computed using traditional RL, which are integrated into the meta-RL model to improve cumulative reward, speed up meta-training, and enhance OOD generalization.

### Strengths
1) RL3 may reduces meta-training time, which has potential practical implications for scaling meta-RL systems.

2) The authors provide theoretical foundation, including proofs that support the efficacy of incorporating Q-value estimates into meta-RL, explaining the potential advantages in handling OOD tasks and long-term planning.

### Weaknesses
1) The author’s understanding of RL2 appears to remain questionable. Specifically, the claim made in the discussion of RL3 suggests that 
"For object-level RL, we use model estimation followed by value iteration (with discount factor
γ = 1) to obtain Q-estimates."
However, in reality, RL2 also employs Q-value estimation in a similar manner to predict the future expectation of reward using the discount factor γ. Specifically, both RL2 and RL3 optimize the same equation mentioned as Equation (1) in the paper. They both employ the idea of optimizing across multiple episodes simultaneously, and there does not appear to be a fundamental difference between the two approaches.

This similarity raises concerns about the novelty of the author's argument regarding RL3's distinct capabilities.

2) Authors mentioned "To test OOD generalization, we vary parameters including the stochasticity of actions, density of obstacles, and the number of dangerous tiles." Although this level of variation is commonly considered a new task in meta-learning settings, the actual changes introduced are relatively minor. Furthermore, GridWorld is a relatively simple environment. 

Whether you have plans to test on more complex domains in future work, such as vision-based RL tasks or robotic control tasks (for example DMC or Atari)?

3) The authors did not provide a clear definition of the RL3 algorithm in a formalized manner, nor did they present a direct comparison with the formulation of the RL2 algorithm. This lack of precise algorithmic definitions makes it difficult for readers to fully understand how RL3 operates and differs from RL2.

Could authors  include a side-by-side comparison with RL2 to highlight the key differences.

4) I not sure that simply feeding the entire sequence of states and actions from a whole task continuously into an LSTM or transformer, as done in RL3, will necessarily enhance OOD generalization and long-term performance. A more promising approach would involve training on trajectories of both short and long lengths. Whether authors have considered alternative methods combining varying trajectory lengths.

### Questions
1) What is a VAMDP? Is there a clear and formal definition?

2) Could the authors outline the fundamental differences in the implementation of RL2 and RL3? Are there any precise mathematical formulations that highlight these differences? As presented, Equation 1 only expresses the meta-learning objective but does not distinguish RL2 from RL3.

3) Why is RL2 unable to address OOD generalization problems? Additionally, why does RL2, compared to RL, lack long-term performance? If RL methods have OOD generalization capabilities, why does RL2 not inherit them?

4) What is the difference between the Q-value in RL, RL2, and the Q-estimates used in RL3?

5) In Figure 3b, why are the performance results of RL2 and RL3 equal when the budget is set to 128? Which specific setting in the experiments is responsible for this outcome?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Discerning that RL$^2$ shows poor asymptotic and ood performance while general RL demonstrates short-term efficiency, this paper constructively combines the general RL with the previous meta-RL algorithm RL$^2$ and calls it RL$^3$. To be specific, the paper seeks to add an extra signal as input, namely the action-value function. Though seems to be straightforward, adding this input would give a useful compression compared to trajectory history. To validate the effectiveness, the paper provides the theoretical proof for recovering the optimal meta-level value function. Finally, some experiments on discrete domains are performed.

### Strengths
1. The paper constructively combines the previous meta-RL algorithms called RL$^2$ and general RL signal to absorb the advantage and avoid the disadvantage of both sides.
2. The paper adopts extra action value as the auxiliary input and provides some theoretical evidence to show rationality.
3. Compared to RL$^2$, which uses the history trajectory rather than the RL$^3$ using the action value, the latter can learn more efficiently and easily. I appreciate the authors' thorough explanation.

### Weaknesses
1. The biggest concern for me is that as shown in Appendix A.4, $\textbf{based on the extra input action-value}$, the iteration process would lead to two cases either the belief distribution collapses rapidly to zero for tasks $j\ne i$ or the belief distribution will reduce to zero for tasks not compatible with the observed Q-values. $\textbf{Does this mean that whatever is capable of distinguishing tasks as input should meet this proof and the action value is only a feasible case?}$ If so, what is the advantage of this over adopting the task representation as input like the context-based meta-RL algorithms [1] ? Note that these algorithms can also hold a good compression w.r.t the transition / trajectory. Also, these algorithms can resolve the continuous domain rather than be limited to the discrete domain. The core issue is that the paper's theoretical justification seems to apply to any task-discriminating input, not specifically Q-values, and the paper does not provide a compelling reason to prefer Q-values over other task representations, especially given the limitations to discrete action spaces.
2. In my view, why RL$^3$ holds better OOD performance can not be interpreted by the theoretical justification. The theoretical argument focuses on recovering the optimal meta-level value function, but it does not explain why using Q-values as input should lead to better generalization to unseen tasks, especially when the Q-values themselves might be inaccurate under distribution shifts. The paper lacks a clear explanation of how the Q-value input contributes to OOD generalization beyond the theoretical proof.
3. RL$^2$ is a very early meta-RL algorithm, incrementally building upon RL$^2$ may still have a large gap with SOTA algorithms. As some context-based meta-RL algorithms hold the SOTA, I believe the authors can move RL$^3$ onto the context-based meta-RL algorithms to show further superiority or at least add some comparison. The paper needs to demonstrate its performance against more recent and advanced meta-RL algorithms, particularly those that use context-based approaches, to establish its relevance and competitiveness in the current landscape of meta-RL research.
4. This is related to problem 3, some lately-published papers regarding advanced meta RL should be discussed.
5. Some unclear definitions and typos: what are object-level and meta-level? What is Figure b) trying to show? Why does any permutation of transitions yield the same Q-estimates? For testing OOD generalization, MDPs are generated from distributions with different parameters than in training, what does the "parameters" mean here? How do the authors generate the OOD data? VeriBAD -> VariBAD
6. Unclear pseudo-code: Does the $ONEHOT(s)\cdot Q(s) \cdot N(s)$ denote the results after concatenation?

### Questions
See Weakness above.

### Soundness
2

### Presentation
2

### Contribution
2
