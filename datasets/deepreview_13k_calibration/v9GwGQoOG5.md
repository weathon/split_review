# Beyond Markov Assumption: Improving Sample Efficiency in MDPs by Historical Augmentation

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Under the Markov assumption of Markov Decision Processes (MDPs), an optimal stationary policy does not need to consider history and is no worse than any non-stationary or history-dependent policy. Therefore, existing Deep Reinforcement Learning (DRL) algorithms usually model sequential decision-making as an MDP and then try to optimize a stationary policy by single-step state transitions. However, such optimization is often faced with sample inefficiency when the causal relationships of state transitions are complex. To address the above problem, this paper investigates if augmenting the states with their historical information can simplify the complex causal relationships in MDPs and thus improve the sample efficiency of DRL. First, we demonstrate that a complex causal relationship of single-step state transitions may be inferred by a simple causal function of the historically augmented states. Then, we propose a convolutional neural network architecture to learn the representation of the current state and its historical trajectory. The main idea of this representation learning is to compress the high-dimensional historical trajectories into a low-dimensional space. In this way, we can extract the simple causal relationships from historical information and avoid the overfitting caused by high-dimensional data. Finally, we formulate Historical Augmentation Aided Actor-Critic (HA3C) algorithm by adding the learned representations to the actor-critic method. The experiment on standard MDP tasks demonstrates that HA3C outperforms current state-of-the-art methods in terms of both sample efficiency and performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
For deep reinforcement learning, the paper proposes to augment the state with compressed historical to improve sample efficiency and performance. Some theoretical analysis provides optimality and convergence properties for the proposed state augmentation when certain conditions are satisfied. Numerical experiments show decent performance for the proposed method compared to some existing methods.

### Strengths
- Having an appropriate representation is important for RL agents. For problems with the Markov property, it is typically for a RL agent to consider only the current state as the state is known to be sufficient to make optimal decisions. The proposed idea to augment history to help the agent to improve its representation learning is an very interesting ideas and sounds promising from simple examples as discussed.

- The proposed method shows decent performance in numerical experiments, and the effectiveness of history augmentation is numerically illustrated in the ablation study.

### Weaknesses
- Although the paper provides some analysis for optimality and convergence properties of the proposed provided, these properties do not provide any insight into why the history augmentation helps representation learning. And there is no analysis on potential sample complexity reduction. Since it is assumed that the state is kept and completely uncompressed in the encoder output, most of the results are expected. It is likely that simpler arguments may be available by arguing that the original state-dependent optimal policy is also a feasible policy with the augmentation. Specifically, the theoretical guarantees in Section 4.1 seem to hold even without any history augmentation, raising questions about the necessity of the proposed approach. A more rigorous analysis demonstrating the impact of history augmentation on the learned representation's quality and subsequent sample efficiency improvements would significantly strengthen the paper.

- In both the analysis of Section 4.1 and the algorithm design in Section 4.2, it is not clear whether we non trivial augmentation is needed. For example, the analysis seems to completely go through when $f(s_{k, t}) = s_t$ in Section 4.1, and nothing seems to prevent the HA3C algorithm to ignore the history and ending up getting $z^{s^{k, t}_\alpha} = s_t$. This implies that the proposed method might be equivalent to simply using the current state, which contradicts the core idea of leveraging historical information. A clear demonstration of scenarios where history augmentation provably leads to different and better representations compared to using only the current state is crucial.

- Although the ablation study shows better performance with the proposed history augmentation, the improvement does not seem significant given those largely overlapping confidence areas. Additional experiments like showing how performance varies by varying the length of the history augmentation may provide some trends that could be more convincing. The current results do not provide strong evidence for the effectiveness of the proposed method. Varying the length of the history and analyzing the resulting performance could reveal an optimal history length or demonstrate a clear trend of improvement with increasing history length, which would provide more compelling evidence.

- Comparing to existing methods, the proposed seem to perform decently in the numerical experiments, but the improvement is not that significant especially compared with TD7. Without additional analysis on the quality of the learned representation, it is not clear if the performance benefits indeed come from the proposed history augmentation. The paper lacks a thorough investigation into whether the observed improvements are actually due to better representation learning facilitated by history augmentation or simply due to other factors. A more detailed analysis of the learned representations, potentially through visualization or comparison of representation similarity, is needed to establish a clear link between history augmentation and performance gains.

### Questions
- Beyond the simple examples, are there theoretical or numerical analysis showing sample complexity benefits with history augmentation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides an interesting viewpoint on learning a policy that not only depends on the current state but also on the history in Markov decision processes. The key motivation is that, by conditioning on the history, the underlying pattern may be simpler than only conditioning on the current state. The Fibonacci example nicely demonstrates this point. Later, the authors identified two challenges when we want to learn a policy depending on the history: 1) How to ensure we learn a simple pattern based on the history? 2) How to avoid overfitting to the high-dimensional historical data? The core solution proposed by this paper is to learn two encoders - one is used to compress the history into a low-dimensional embedding and the other serves as a latent world model to predict the embedding of the next state based on the action.

### Strengths
The overall idea is novel but sound. The proposed method is reasonable from an intuitive perspective.

### Weaknesses
- While the Fibonacci example is persuasive, I do not quite understand the example provided in Figure 1. Why the causal function in Figure 1 (b) is simpler than the causal function in Figure 1 (a)? Or this is just a illustrative figure for historical augmentation but not for providing a solid sample? If this is the case, I would like to see a less artificial example to demonstrate on this point (depending on the history can lead to a simpler causal relationship).
- After I go through the algorithmic design of HA3C, I feel this algorithm is closer to “representation learning for RL” such as Dreamer. (By the way, Dreamer lacks citation in L128.) HA3C essentially learns encoders that can compress the state (plus history) in to a latent space and learns an additional latent world model (g) that can predict the dynamics in this latent space. From this perspective, HA3C would better to also compare with other “representation learning for RL” baselines.
- On the experimental results, the improvement of HA3C is marginal over the baseline algorithms on MuJoCo control tasks. From my point of view, this does not indicate that HA3C is ineffective. I think the benefit of HA3C relies on the structure of the problem: the causal relationship based on only the current state is complex but the causal relationship based on the history can be simple. MuJoCo tasks may not be good environment for HA3C. I strongly suggest the authors to find other tasks (or even artificial tasks to demonstrate the effectiveness of HA3C).
- I do not quite understand the significance of the point demonstrated in Figure 5. Do I understand correctly? HA3C has more points in the red circle. This indicates that HA3C can reach the high-rewarding states more often (or robustly). This information seems a little  duplicated to the training curves demonstrated in Figure 6 or Table 1.
- In L171, should the formula depend on $s_t$ but not $t$ since we are talking about predicting $s_{t+1}$ from $s_t$ but not $t$.
- The citation format is incorrect.

### Questions
- I do not quite understand the significance of the point demonstrated in Figure 5. Do I understand correctly? HA3C has more points in the red circle. This indicates that HA3C can reach the high-rewarding states more often (or robustly). This information seems a little  duplicated to the training curves demonstrated in Figure 6 or Table 1.
- In L171, should the formula depend on $s_t$ but not $t$ since we are talking about predicting $s_{t+1}$ from $s_t$ but not $t$.
- The citation format is incorrect.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new algorithm to improve sample efficiency in reinforcement learning by integrating historically augmented states, and presents a series of experiments conducted to validate the effectiveness of this algorithm.

### Strengths
1. The examples given in the Section 3 and Appendix B help readers understand the motivation of using historical information.
2. The paper is generally well-organized, making it easy for readers to follow.
3. The proposed method is shown to have strong empirical performance on Mujoco and DMC.

### Weaknesses
1. To improve reproducibility, it would be beneficial to supplement the implementation details about the inputs and the parameters of networks such as CNNs used in the encoder. Specifically, the dimensions of the input state vectors, the number of layers and units in the CNN, the activation functions used, and the specific optimization algorithm and its parameters should be detailed. The lack of this information makes it difficult to replicate the results.
2. I believe the paper would read more easily after reorganizing the Appendix A and Appendix D, as abbreviations like SkD and MkD may be confusing for those unfamiliar with them. The current organization makes it difficult to quickly grasp the differences between the various policy types. A more structured approach, perhaps with a table summarizing all abbreviations and their corresponding policy types at the beginning of the appendix, would be beneficial.
3. An in-depth analysis of the parameters k and N in the ablation study would greatly enhance readers' understanding of the algorithm. Specifically, the ablation study should explore a wider range of values for k and N, and analyze the impact of these parameters on both the performance and the stability of the algorithm. Additionally, I believe more analysis of the running time or the complexity would be helpful, for example, the impact of the parameters k and N on the running time. The current analysis lacks detail on how these parameters affect computational cost and convergence speed.

Minor comments
1. Is there a mismatch between the Figure 2 and the corresponding description “the dimensionality reduction is only performed on $s_{k−1,t−1}$”? The figure seems to indicate that dimensionality reduction is applied to other states as well.
2. Is there a typo in the results for TD7 on HalfCheetah shown in Table 1 (the reward of 156325)? Additionally, the reward of 45074 for TD3+OFE on Walker2d should also be checked.
3. Formatting: 
         a) When the authors or the publication are not part of the sentence, the citation should be in parenthesis by using ‘\citep{}’.
         b) The format for referencing figures should be consistent in the Section 3.

### Questions
1. While the proposed historically augmented states can theoretically improve actor-critic methods, could you provide more evidence that demonstrates their applicability to other existing RL methods, aside from the current used TD3?
2. Is the input to HA3C images while the authors mention high-dimensional historical trajectories frequently?

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
4

### Summary
This paper posits that, even when operating under the Markov assumption, it is beneficial for policy formulation to take into account not only current states but also historical information. This is based on the assumption that single-step state transitions might have complex causal relationships. Introducing historical data could potentially simplify these causal relationships, making them easier for neural networks to learn. On this basis, a novel Reinforcement Learning (RL) algorithm named HA3C is proposed, which has demonstrated superior performance over other advanced algorithms, such as TD3 and TD7, in five MuJoCo control tasks.

### Strengths
1. The perspective of causal relationships is interesting to understand why one should use historical information as additional inputs.
2. The theoretical formulation is precise and comprehensive.

### Weaknesses
1. The improvement of HA3C over baselines on the five Mujoco tasks appears to be subtle rather than significant.
2. It would be beneficial to devise a demonstrative environment and characterize the causal relationships, thereby facilitating a clear comparison between the two options.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2
