# Efficient Imitation under Misspecification

- Decision: Accept
- Scores: 8, 5, 6, 8

## Abstract
Interactive imitation learning (IL) is a powerful paradigm for learning to make sequences of decisions from an expert demonstrating how to perform a task. Prior work in efficient imitation learning has focused on the realizable setting, where the expert's policy lies within the learner's policy class (i.e. the learner can perfectly imitate the expert in all states). However, in practice, perfect imitation of the expert perfectly is often impossible due to differences in state information and action space expressiveness (e.g. morphological differences between humans and humanoid robots.) In this paper, we consider the more general *misspecified* setting, where no assumptions are made about the expert policy's realizability. We introduce a novel structural condition, *reward-agnostic policy completeness*, and prove that it is sufficient for interactive IL algorithms to efficiently avoid the quadratically compounding errors that stymie offline approaches like behavioral cloning. We address an additional practical constraint---the case of limited expert data---and propose a principled method for using sub-optimal data to further improve the sample-efficiency of interactive IL algorithms. Finally, we corroborate our theory with experiments on a suite of continuous control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Define misspecification as the expected difference in advantage between an expert policy (taking the optimal action at each state), and a state conditioned policy. Then define an IRL algorithm which searchers for reward using a loss defined by the expected difference in reward under the expert and policy distribution with a divergence constraint to prevent stepping too far, and updating the policy with PSDP. Then, resetting to offline data is analyzed as a complement to resetting to expert data.

### Strengths
This work introduces a novel metric for misspecification.

The work offers an interesting perspective on the relationship between IRL and Offline RL

The proposed algorithm shows empirical results that match some of the theoretical claims

### Weaknesses
Some of the language is unclear. In particular, the use of sample efficiency and computational efficiency seem to be used interchangeably, but sample efficiency is the more valuable metric. Is computational efficiency even the problem here, and not sample efficiency?

The notation for the advantage function is not formally defined in the work, which makes it slightly more difficult to parse.

While the core definitions for policy completeness error are more or less well defined the GUITAR method itself is not self-contained. It is not obvious what the Bregman divergence or PSDP methods are, and probably more importantly, why these are preferable to other methods. I assume it is because of their theoretical properties, but it is not straightforward to draw the connection between the properties given and those proven in the paper. 

The organization of the paper make is more challenging to follow, as the issue of resetting is not the central focus of the work yet intrudes in the middle. If resetting is a core component of the method, then the confusion lies in expressing the connection between resetting and the misspecification problem. Furthermore, this section does not address the original problem of resetting to unreachable states, since the behavior policy may also be unreachable. 

The empirical analysis is quite limited. In particular, the performance on more generic tasks is not convincing for this method. In particular the FILTER baseline appears to match or exceed performance in all domains. In several domains, performance is comparable with BC as well. Furthermore, there is no comparison with non-resetting SOTA offline RL methods such as IQL or CQL. Finally, the number of environments for a straightforward, fundamental method is quite limited. In a somain such as this the expectation would be to cover a good portion of at least the deepmind control suite, especially the Franka Kitchen tasks.

### Questions
See Weaknesses

### Soundness
3

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
4

### Summary
The paper titled addresses a significant challenge in imitation learning (IL) by considering the setting when the expert's policy may not be fully realizable within the learner's policy class. This misspecified setting reflects real-world scenarios where the learner's capabilities may differ from the expert's, such as in robotic applications. It introduces reward-agnostic policy completeness to handle compounding errors even with this misspecification and proposes the GUITAR algorithm, which combines expert and offline data for efficient resets. Theoretical analysis and experiments on continuous control tasks are provided.

### Strengths
- The paper is theoretically robust, providing a thorough analysis of error sources in IL—optimization, finite sample, and misspecification errors—and offering a formal lower bound that emphasizes the challenges of efficient IRL under misspecification.

- By addressing both limited data and misspecification, the paper proposes practical improvements for settings where ideal conditions (perfect data, full realizability) are unattainable, a scenario commonly encountered in robotics and autonomous driving.

### Weaknesses
 - While the use of offline data is well-motivated, additional analysis of how different qualities and types of offline data affect performance could strengthen the results and offer practical insights for selecting such data.

- The GUITAR algorithm, with its dependence on multiple reset distributions and dual optimization steps, may be challenging to implement and deploy in resource-constrained environments. Simplifications or guidelines on choosing reset distributions could make it more accessible.

- The authors' choice of not including the codes during the review process make the claims less transparent.

- The main results are only provided in three MuJoCo environments. However, as has been understood in literature, compounding errors for offline IL algorithms like BC happen when the environment is stochastic. But the MuJoCo environments are almost deterministic where BC seems to perform really well [1] with very limited data. I wonder why no stochastic environments are used for evaluation.

### Questions
- What is happening in the AntMaze experiment provided in the Appendix? I don't get what the conclusion from that experiment is.

- The algorithm's design is notably complex, involving a dual optimization loop with reset-based IRL, reward updates via mirror descent, and policy updates that mix offline and expert data resets. Could you please talk a little bit about the computational complexity of the method?

- Could you include a brief description of PSDP in the main paper to make it more self-contained?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies inverse reinforcement learning (IRL) under the misspecification setup, i.e., the experts policy is not realizable within the policy class used for learning the policy. The paper presents a theoretical analysis of this case and introduces the measure of Reward-Agnostic Policy Completeness Error to quantify the misspecification under the imitation learning / IRL setup. This measure is used to obtain sample complexity bounds under the misspecification assumptions. Moreover, the paper argues that existing IRL algorithms that do not consider the misspecification assumption, rely on the expert's distribution for resetting, which is now in the misspecication setup not ideal any more as the expert distribution might contain states from which the learned policy can not reach the goal. For this case, the paper studies using additional offline data for the resetting the environment and the theoretical conditions when this is beneficial. The paper also contains limited experimental evaluation of this algorithm.

### Strengths
- the paper formalizes a so far less considered problem, policy misspecification. The paper also introduces new interesting quantities such as the reward agnostic  Policy Completeness Error
- the theoretical analysis of the paper is very interesting and looks sound. 
- the idea of using offline for the reset distribution is interesting

### Weaknesses
 - the assumptions made in the paper for formalizing misspecification do not really fit the motivation introduced in the introduction. Here, misspecification is motivated by (i) "distinct perception" and (ii) "distinct action spaces" due to different morphology. I am unsure whether (i) is really covered by the given theory and algorithm as this would require to use the partial observable setup (for both, expert and policy) where the theory probably does not hold any more. At least implementing resets to offline states might be very hard in the partial observable setup. Concerning (ii), while this could be covered by the theory as far as I understand, the experiments do not cover such a setup at all. This should be clarified in the paper. 
- misspecification is mainly considered if the policy  parametrization is not strong enough to take the optimal action in each state. However, as DNNs are very expressive representations, I am wondering how much this is really an issue in most setups (i.e. most DNN policies can reproduce the optimal policy, at least in the setups considered in the experiments of the paper).
- The experiments are rather limited and do not show any application under "misspecification", which is the main contribution of the paper. For all experiments, the experts policy can be realized by the learned policy, so I do not fully see the point if studying misspecifation in this setup. While (i) might be hard to realize, the authors could have presented experiments where (ii) is the case (see above). This can be done in gridworlds as well as for continuous control (i.e. the expert has other action limits then the behavior policy). Such experiments would be much better suited to illustrate the benefits of the approach.
- The presented experiments also hardly show any benefit of the presented method. E.g. I can not see any benefit in Figure 2. Alsothe experiment of Figure 3 is not well motivated. In this experiment, if I have the expert data, I can directly use it for the reset, why should I use less (I.e. the "short trajectories")? Seems to give the same performance...


### Questions
- Please clearly motivate in which setup of misspecification you oberate (different state observations or different actions)
- Provide a better motivation of the experiments and how they show a benefit in the misspecification setup
- Experiments with an actual misspecification between expert and learned policy (even if only gridworld) would really help the paper
- I was unclear about the mirror descent update rule for the reward. What the entropy of the reward R here? Is the rewward stochastic such that we can compute entropies? More information here would be useful (even though that might be described in previous papers, its not general knowledge and should be described in the paper as well briefly for self-consistency) 
- I was also unclear why in the case of approximate policy completeness, we have O(1) for the sample complexity error bounds. Please provide more detail here. 

In general I like the paper, but the experiments do not show any application where misspecifcation is an issue. This is the main motivation of the paper and hence this should also be part of the evaluation. Happy to raise my score if the authors can provide experimental insights there.

Post-Rebuttal: The new experiment show now a clear application in misspecification. Raised my score to 6.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the interactive imitation-learning setting where policy realizability is violated. The paper further considers the setting where the reset distribution is a mixture of expert and a suboptimal policy, a more practical setting than reset distribution induced by just the expert policy. Based on these assumptions, the paper provides theoretical results on when the former reset distribution is more beneficial. Finally, the paper conducts few experiments to validate the theoretical findings and also identify potential gaps for future analysis.

### Strengths
- The paper is well written and describes the theoretical results intuitively.
- The misspecification setting is definitely a setting where previous works did not consider.
- This work puts in a good effort to bridge the theory and application gap with experiments which I appreciate a lot

### Weaknesses
 - Small writing nitpicks:
	- Page 6, equation 10 (or Algorithm 2): Should $n$ be $N$ (or the other way around) for the reward regret?
	- Page 6, line 315: Perhaps there should be some statement indicating why we cannot be more aggressive on $\epsilon$ (e.g. $\epsilon = 1/H^2$) (or why it does not make sense for this to happen).
- While I see some value of this theoretical work, I have a concern about how this paper is positioned which influence the score by a lot:
	- For a theory paper, I feel this result is not groundbreaking, in the sense that the bounds seems to be very standard. Perhaps the authors can clarify this and whether I am missing anything. The analysis seems to follow a fairly standard regret decomposition, and it is not immediately clear what the key novel technical contribution is beyond applying it to this specific setting. The paper should highlight more clearly what the technical novelty is, and why the analysis is non-trivial.
	- For a empirical paper, (1) I have trouble convincing myself why rolling-in with BC policy is a valid approach (assuming the BC policy was trained with the scarce data provided in the dataset), and (2) there can be more analysis on the experiments including analyzing the extent of misspecification and the potential gap on "trajectory length" the paper has raised. Specifically, the paper should provide more details on how the BC policy is trained, how much data is used, and what the performance of the BC policy is. This is important to understand the quality of the reset distribution and the degree of misspecification.
- For experiments, an alternative to using $p_{tremble}$ is to have mixture like $\alpha \rho_E + (1 - \alpha) \mu$ which I believe can be a way more realistic setting than random actions during data collection. This would allow for a more controlled way to vary the quality of the offline data and the degree of misspecification.

### Questions
- To follow up on the previous point, I am curious how misspecification is validated in the experiments? Did the authors try running behavioural cloning on a large dataset and find that there is an inherit performance gap?
- On page 10, lines 515-516: "When we improve the roll-in distribution by adding offline data, we see..." I am having trouble relating this result with Figure 2, can the paper please clarify this statement?
	- Perhaps I am confused about whether the roll-in for `FILTER` is using $\pi_E$ rather than $BC(\pi_E)$?

### Soundness
3

### Presentation
3

### Contribution
3
