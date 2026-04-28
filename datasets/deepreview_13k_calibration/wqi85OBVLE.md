# Reward Adaptation Via Q-Manipulation

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
In this paper, we introduce reward adaptation (RA), the problem where the learning agent adapts to a target reward function based on one or multiple existing behaviors learned a priori based on their corresponding source reward functions, providing a new perspective of modular reinforcement learning.  Reward adaptation has many applications, such as adapting an autonomous driving agent that can already operate either fast or safe to operating both fast and safe. Learning the target behavior from scratch is possible but inefficient given the source behaviors available. Assuming that the target reward function is a polynomial function of the source reward functions,  we propose an approach to reward adaptation by manipulating variants of the Q function for the source behaviors, which are assumed to be accessible and obtained when learning the source behaviors prior to learning the target behavior. It results in a novel method named ``Q-Manipulation'' that enables action pruning before learning the target. We formally prove that our pruning strategy for improving sample complexity does not affect the optimality of the returned policy. Comparison with baselines is performed in a variety of synthetic and simulation domains to demonstrate its effectiveness and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a problem they call "Reward adaptation", where an agent which has been previously trained on a set of different reward functions can be more quickly trained on a new reward function. A method is proposed to compute upper and lower bounds on the Q function for a new reward function, given that the reward function is expressed as a polynomial of the existing reward functions and the system had previously kept the q values and the q values of the negative reward from every state in the environment. These upper and lower bounds are used to eliminate actions during exploration for the new reward.

### Strengths
The paper looks at an important problem of transfer learning in RL. The justification for the proposed method in 2.2 seems correct, and it should have few downsides if the domain satisfies the assumptions that make the approach possible.

### Weaknesses
Section 2.3 appears to have several errors. In particular, Lemma5 appears to be wrong. A counter-example would be adding a constant potential to every state, which should not increase the min Q value. This is straightforward to check in the 1-state, 1-action where all policies are the same; the min and max Q-values would be the same even after a potential shaping term was added, contradicting Lemma 5.

I believe the error is on the second line of the derivation of (14). -{R_F} after reward shaping is -R + -F, so once we apply Ng et al.1999 we get a + phi(s) term rather than a negative due to the double negative. There is then another negative remaining outside the square brackets, which makes (14) match (13).

Another hint that this has to be wrong is that the constraint is added to (15) to ensure "the upper bound remains greater than or equal to the lower bound", but that should be mathematically impossible if the theorem was valid.

Another issue with this section is that the Ng. 1999 paper requires SAS rewards, but this paper is written with SA rewards, so the theory does not apply directly as stated.

In addition, the paper could also be made significantly more clear. For instance, rather than defining the minimum achievable reward as Q_{-R}, there is a new symbol introduced (which confusingly includes mu), and then it is immediately pointed out that this is the same as Q_{-R}. It seems like this observation is so straightforward as to not need a Lemma, and the added notation not only uses a lot of space but makes the rest of the paper much more difficult to follow.

Many of the methods are also redefined as acronyms halfway through, in a way that is not self-documenting. It becomes excessively difficult to keep track of the differences between Q-M, RS, Q-D, and Q.

Finally, the method is quite difficult to motivate. The main example they point to is if you had a self-driving car that was trained to "either be fast or safe", you could warm-start it to learn the other, but this is far from how self-driving cars work. Even so, it is hard to imagine how "fast" or "safe" could be expressed as a polynomial of the other, as is required by their method.

### Questions
How do you think the method could be extended past polynomial combinations of existing reward functions?

### Soundness
1 poor

### Presentation
2 fair

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
This paper addresses the reward adaptation problem, where an agent with access to optimal behavior in source MDPs must quickly learn optimal behavior in a target MDP with a new reward function. The authors assume the target reward function is a polynomial function of the source reward functions in a finite MDP setting and propose the "Q-Manipulation" method to enable action pruning before learning the target behavior.

### Strengths
The paper is overall well-written.  

The proposed method is novel and interesting.

### Weaknesses
As a core contribution, the authors claim that “We introduce the problem of reward adaptation”. However, I am not sure that it is valid. It seems to me the reward adaptation formulation in Section 2.1 of this paper is an extension of the “Transfer via successor features” problem of [1], where the authors assumed the target reward function to be the linear combination of source reward functions (see Section 4 of [1]). If this is not the case, please clarify. If this is the case, it is important to refer to the successor features literature, and compare your method with the methods proposed in [1], both conceptually and empirically. 

Based on the derivations in Sections 2.2 and 2.3, the action pruning strategy is heavily reliant on the assumption that the target reward function is a polynomial function of the source reward functions. In the settings where this assumption is violated, there is a risk that even the optimal actions in the target MDP are pruned. The transfer learning techniques that use potential-based shaping ideas can safely avoid this optimality issue. 

In a single source MDP setting, for the reward adaptation problem, the technique proposed in [2] can be applied. Here, the Q-value function in the source domain can serve as a potential function to shape the reward function in the target domain. In this case, the target reward function does not need to be a polynomial function of the source reward function. In the case of multiple source MDP setting, we can use a weighted combination of the Q-values as a potential function to shape the reward function in the target domain. One can learn better weights for combining via the bi-level optimization framework proposed in [3]. It is important to compare your approach to this transfer via shaping technique, both conceptually and empirically.

### Questions
Minor comments:

In Section 2.2, the authors state that the influence of discounting can be safely ignored, e.g., when MDPs with absorbing states are considered. In the proofs of Lemma 2 and 3, the discounting factor is ignored; whereas, in the proof of Lemma 4, it is not ignored. Please formally/explicitly write the type of MDPs considered in the proofs. 

Due to high/overlapping variance in the convergence plots, it is not very clear that the proposed method outperforms the current set of baselines. The authors could consider additional presentation of the results (e.g. in a tabular form).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce the reward adaptation (RA) problem where the agent learns to adapt to a _target_ reward function while having access to behaviors learned from multiple _source_ reward functions. The authors then focus on a restricted scenario where the target reward function is a polynomial function of the source reward functions. They introduce a method, Q-Manipulation, for action pruning in learning the target task by employing the optimal Q-function from the source tasks, with the hope that learning will be more efficient with the reduced action set. Q-Manipulation estimates the upper bound and the lower bound of the Q-value for each action from its Q-values from the source tasks. An action is then pruned when its Q-value upper bound is below the Q-value lower bound of another action. The authors also introduce a reward shaping based method to tighten the upper bounds and the lower bounds to further facilitate pruning. Tabular experiments demonstrate the effectiveness of Q-Manipulation at action pruning, and further show accelerated learning on the target task.

### Strengths
* This work addresses an important question of how to learn more efficiently on a target task by leveraging knowledge from related source tasks. Progress on this question can further broaden the applicability of reinforcement learning to real-world applications.

* Overall the paper is easy to follow. The problem of RA is well motivated and the main idea behind Q-Manipulation is straightforward.

* The experiments are well-designed to test the key attributes of the Q-Manipulation algorithm, such as the portion of pruned action and the downstream impact on learning efficiency.

### Weaknesses
 * I am afraid that the theoretical results for reward shaping is incorrect. Specifically, I have doubts regarding the correctness of Lemma 5. When reward shaping is applied, $Q_{R_{F}}^{\*}$ and $Q_{R_{F}}^{\mu}$ should be offset towards the same direction, not the opposite directions. In fact, as the authors note in Eq. (15), Lemma 5 implies that $Q^{\*}$ can be smaller than $Q^{\mu}$ after reward shaping, meaning that the optimal policy changes, which conflicts with the theory built in [3]. This is a critical flaw as it undermines the theoretical justification for the proposed reward shaping method. The core issue lies in the assumption that shaping will consistently shift the Q-values in a way that preserves the optimal policy, which Lemma 5, as currently stated, fails to guarantee. The potential for the shaped Q-values to alter the optimal policy makes the action pruning strategy unreliable.

* The novelty of the RA problem is questionable. In the second paragraph of the Introduction section, the authors write "In this paper, we introduce Reward Adaptation (RA), ..." However, this problem has been widely studied by existing works such as [1] and [2]. Discussion on the connection to these existing works is missing in the manuscript. Specifically, the authors should clarify how their formulation of RA differs from existing transfer learning paradigms, such as those using successor features or options. The lack of discussion makes it difficult to assess the true contribution of this work.

* All experiments were conducted in tabular toy environments and the improvement in learning efficiency is marginal. The authors did not comment on the scalability of Q-Manipulation to the function approximation settings. It would be more convincing if the authors can provide more empirical evidence supporting the effectiveness of Q-Manipulation in larger environments. The current experiments do not adequately demonstrate the practical applicability of the proposed method. The absence of experiments with function approximation, such as neural networks, leaves a significant gap in the evaluation. Furthermore, the marginal improvement observed in the tabular setting raises concerns about the practical impact of Q-Manipulation in more complex scenarios.

### Questions
* Could the authors address my question regarding the correctness of Lemma 5?
* Could the authors comment on the scalability of Q-Manipulation?
* Could the author clarify the connections to existing works such as GPI [1] and Option Keyboards [2]?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel training schema called "reward adaptation" to leverage existing learned Q functions (with pre-defined source reward settings) to expedite learning a target Q function(in a new and target reward setting). The key idea is to maintain two Q-function variants (Q* and Q-min) for each source reward setting and use them to compute bounds on the expected return under the target reward function. Using reward shaping to tighten the bounds, many actions can be safely pruned before learning the target Q function. This "Q-Manipulation" approach is proven to retain optimality. Empirical results in a variety of domains show faster convergence compared to baselines.

### Strengths
1) The problem of reward adaptation provides a new perspective on transfer learning and modular RL. Being able to leverage existing behaviors to learn new ones more efficiently has many useful applications.

2) Theoretical analysis of computing bounds on the expected return and the effects of reward shaping is thorough. The proof of retained optimality after pruning is important.

3) Empirical results demonstrate significantly faster convergence across different domains, validating the effectiveness of Q-Manipulation for pruning unpromising actions. Comparisons to relevant baselines are adequate.

### Weaknesses
1) The linear programming formulation for computing the reward shaping function does not scale well. Approximation methods need to be considered for large state/action spaces. Specifically, the computational cost of solving the linear program for each state to determine the shaping reward could become prohibitive in complex environments with large state and action spaces, making the approach impractical without approximations. The paper should discuss the computational complexity of this step and propose concrete solutions for large-scale problems.

2) Requiring both Q* and Q-min doubles the learning cost for source behaviors. It would be useful to analyze if pruning is possible with just Q* and π*. The need to learn and store two separate Q-functions for each source task significantly increases the memory and computational overhead during the pre-training phase. An analysis on whether the pruning can be achieved with only the optimal Q-function (Q*) and the optimal policy (π*) could potentially reduce the pre-training cost and make the method more efficient. The paper should explore this possibility and provide theoretical or empirical evidence.

3) The assumption of target reward being an exact polynomial of source rewards is limiting. More analysis on effectiveness when the target can only be approximated is needed. The assumption that the target reward can be expressed as an exact polynomial of the source rewards is a strong limitation. In real-world scenarios, this assumption is unlikely to hold, and the target reward might only be approximated by a polynomial. The paper needs to analyze the impact of this approximation on the performance of the proposed method. Specifically, the paper should investigate how the approximation error affects the tightness of the bounds and the effectiveness of the pruning strategy. It should also provide guidelines on how to choose the polynomial degree to balance approximation accuracy and computational cost.

4) Comparisons to a broader variety of baselines (e.g., transfer learning methods) could be more informative about the relative merits of this approach. More results on complex environments, such as Atari Games, should be better inducted to show that this method is effective. The empirical evaluation should include comparisons with established transfer learning techniques to better demonstrate the advantages of the proposed approach. Furthermore, the current evaluation is limited to relatively simple environments. The paper should include results on more complex and challenging environments, such as Atari games, to validate the robustness and scalability of the method.

### Questions
1) According to Algorithm 1, Is Q* and Q-min pre-learned in an offline form? If so, prune action with steps 1-4 may be considered to be inefficient. 

2) The advantage baseline in A2C seems low-cost; how about considering it for pruning action?

3) When does action pruning occur? In the exploration, in the target Q update, or both. It seems that the prune behavior is conservative. 

4) Could you visualize the pruned action space in the training process and compare it to the original action space?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
