# Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Optimistic value estimates provide one mechanism for directed exploration in reinforcement learning (RL). The agent acts greedily with respect to an estimate of the value plus what can be seen as a \emph{value bonus}. The value bonus can be learned by estimating a value function on \emph{reward bonuses}, propagating local uncertainties around rewards. This approach, however, only increases the value bonus for an action retroactively, after seeing a higher reward bonus from that state and action. Such an approach does not encourage the agent to visit a state and action for the first time. In this work, we introduce an algorithm for exploration called Value Bonuses with Ensemble errors (VBE), that maintains an ensemble of random action-value functions (RQFs). VBE uses the errors in the estimation of these RQFs for designing value bonuses that provide first-visit optimism and deep exploration. The key idea is to design the rewards for these RQFs in such a way that the value bonus can decrease to zero. We show that VBE outperforms Bootstrap DQN and two reward bonus approaches (RND and ACB) on several classic environments used to test exploration and provide demonstrative experiments that it learns faster in several Atari environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to conduct exploration over states, which is typically not done with value based exploration methods from previous works. The authors provide justifications on the convergence of their proposed VBE method and conduct experiments to show that VBE outperforms SOTA algorithms on standard testing environments.

### Strengths
The paper is well written with clear motivation and discussion on the relationship between VBE and BDQN. The proposed algorithm is novel to me and is interesting. Experimentation also shows that proposed VBE performs better than SOTA algorithms.

### Weaknesses
Regarding the claim that the proposed bonus “ensures that bonus goes to zero” when environment is sufficiently explored. In other UCB-stype work and the BDQN setup, theoretically, bonus will also goes to zero if actions are sufficiently explored.

Overall I find this work interesting but contribution is relatively marginal, given existing algorithms including BDQN, RND, ICM [1], numerous self-supervised exploration method of this style (e.g., [1][2], to name a few), and numerous theoretical analysis on UCB-styled exploration (e.g, [1] and plenty of follow-up works). In fact, [3] explicitly show that the proposed bonus function scales with an upper confidence bound in the linear setup (Lemma 4.3 of [3]). The core issue is that while the method proposes a different way to calculate the bonus, it is not clear that this method provides a significant advantage over existing methods. Specifically, the bonus is still a function of the frequency of visits, similar to count-based methods, and it is not clear why directly learning a bonus function as a value function will provide a significant advantage over existing methods that use a two-step process of calculating a local bonus and then propagating it through the value function.

Furthermore, the empirical evaluation does not sufficiently demonstrate the advantage of the proposed method. While the method outperforms SOTA algorithms, the environments tested are relatively simple, and the performance gains are not substantial. It is not clear if the method will be able to scale to more complex environments or tasks. Additionally, the paper lacks a thorough ablation study to investigate the impact of different components of the proposed method. It would be helpful to see how the performance changes with different bonus functions or different update rules for the value function.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

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
This paper introduces a new approach for exploration in RL. The proposed method generates random action-value functions (RQFs) to define consistent rewards. Specifically, it asks the agent to act greedily according to $\operatorname{argmax}_a q(s, a)+b(s, a)$, where $b(s, a)$ corresponds to the value bonuses in VBE.

### Strengths
- Originality: The paper attempts to address exploration in reinforcement learning by introducing the Value Bonuses with Ensemble Errors (VBE). The use of random action-value functions (RQFs) to determine consistent rewards represents a departure from conventional ensemble-based methods in deep reinforcement learning.

- Quality: While there are areas in need of further clarity, the paper provides some mathematical formulations, particularly around the stochastic ensemble reward, suggesting an effort to ground the approach in theoretical foundations.

- Significance: The attempt to distinguish their method from Bootstrapped DQN shows an effort to position the paper within the broader context of ensemble-based methods in reinforcement learning. The idea of leveraging ensemble errors for deep exploration is a direction that might be worth further exploration in the future, even if this paper's execution might not fully capture the potential of the idea.

In sum, while the paper has its challenges, there is merit in the core idea it attempts to present and its potential implications for ensemble-based methods in reinforcement learning.

### Weaknesses
This paper describes a simple idea in a somewhat convoluted manner. Here are specific areas of concern:

- Clarity and Presentation: The paper tends to obfuscate what could be explained more simply. While there is value in rigorous mathematical explanations, these should be accompanied by intuitive explanations and clearer definitions for broader accessibility. For example, the distinction between equation 2 and the actual bonus used in algorithm 1 are not clearly demarcated, leading to potential confusion. The paper introduces the concept of Random Action-value Functions (RQFs) but does not clearly explain how these are generated or what their specific properties are, making it difficult to understand the core mechanism of the proposed approach. The connection between the ensemble of RQFs and the final bonus is also not clearly articulated, leaving the reader to guess how the individual RQF predictions are combined to produce the exploration bonus.

- Novelty Concerns: Upon close examination, the proposed method seems to be essentially a variant of the classical UCB exploration strategy, replacing the count based bonus to ensemble error based bonus; as well as a variant to RND, with difference in ensembles. Moreover, there are clear parallels with the bootstrapped DQN approach, which already encourages first-visit optimism. While the paper does acknowledge the connection to bootstrapped DQN, the explanation is not well-presented, and readers may find it challenging to discern the true novelty of the proposed method. The paper does not adequately address how the proposed method differs from other ensemble-based exploration techniques, particularly in terms of the specific type of uncertainty being captured and how this translates to improved exploration. The use of ensemble error as a bonus is not novel in itself, and the paper needs to clearly articulate what makes their approach unique.

- Significance of Contribution: Given the above, one might argue that the paper's primary contribution is an amalgamation of previously explored ideas. The ensemble error as an exploration bonus, though interesting, might not be substantial enough to warrant a separate methodology, especially given the similarities to existing methods. The paper does not provide a compelling argument for why this particular method of combining ensemble errors is superior to other existing approaches, and it lacks a clear theoretical justification for why this method should lead to better exploration. The lack of a clear theoretical framework makes it difficult to assess the potential impact of the proposed method.

- Experimental Validation: Although not explicitly discussed earlier, it would be essential for such a paper to provide comprehensive experimental results to validate its claims, especially when the theoretical distinction from existing methods is subtle. Without this, it's challenging to gauge the real-world efficacy of the proposed approach. The paper needs to demonstrate the performance of the proposed method on a diverse set of environments, including those with sparse rewards and long horizons, to show its practical applicability. The experimental results should also be compared against a wider range of baselines, including both count-based and ensemble-based exploration methods.

### Questions
Please address the concerns in the weaknesses part.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Current SOTA exploration bonuses are only retroactive: that is they reward states *infrequently* visited, and then rely on randomness around those infrequent states to constantly expand the horizon of exploration. This paper proposes an exploration bonus that rewards states *never* visited through uncertainty in an ensemble of Q-functions. The ensemble is trained to approximate the next-state of a random target function, not the current state like RND, and during rollout, the behavior is taken as a max over actions for the current value for the problem reward and the bonus derived from the ensemble disagreement. There is some discussion of the theory, and some small-scale and mid-scale experiments to support the method, with strong results.

### Strengths
- Exploration bonuses seem underexplored as of late, especially given that RND suffers from only rewarding infrequent states and can collapse like the authors show (I have personal experience with this as well), if we are interested in settings where behavior data is not available, we will need better exploration methods
- The method seems quite sample efficient in empirical evaluations, and the authors correctly note that RND takes an extremely large number of samples to converge (2 billion in the original paper), which is very undesirable if we want to move out of simulation
- Discussion surrounding related literature and motivation of the argument is very sound

### Weaknesses
 - The experiments are a bit small-scale (only ~400k environment steps at most in the Atari domains)
- There is no experiment in the main text on the larger domains that runs to completion, only the early exploration behavior, while I agree that early exploration behavior is more informative for our understanding, it would be good to have an example of how more frames changes behavior in more difficult settings (currently in the Appendix Figure 7, but doesn't show baselines as well)
- There is little discussion on the relatively worse performance in Pitfall and Gravitar in Figure 4, I believe some closer qualitative analysis is merited
- It would be nice to have a showcase result on Montezuma's revenge, or perhaps one of the Antmaze tasks for a more difficult sparse-reward setting?
- There is no explicit objective given for q_w in Algorithm 1, even though the reward has been relabeled in line 12, when we aren't in the pure exploration setting are we using the original reward? I think it would be worthwhile in the main text to give the exact objectives for all components in one place
- It's possible that the really bad failures of RND in Mountain Car are due to the simplicity of the state space, which leads to an early collapse in the bonus, it would be nice to have some discussion of why this occurs in Figure 3.

Minor Comments:
- Section 3, the paragraph "We need to define rewards..." does not have a lot of content and could probably be cut or shortened
- Footnote on page 3: "baring the issue" -> "barring the issue"
- Section 3, discussion on theory "We provide a more complete discussion..." it would be nice to have some specifics in the main text in the form of conclusions, otherwise this takes space and distracts from the main argument
- Algorithm 1, define f_i vs. f_{w_i}
- Algorithm 1, define objective for q_w as well as for f_{w_i}
- Section 5.1, "hard exploration environments" is a subjective claim and probably deserves a citation, I don't consider these to be hard exploration environments, but maybe I should and I don't know why
- Section 5.2, "For Mountain Car, w ereport" -> "For Mountain Car, we report"

### Questions
- see Weaknesses above, mostly I want some more clarity around the exact objective for q_w vs. f_{w_i}
- also in Weaknesses, how does performance vs. RND and ACB change with more frames

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an approach to improving the exploration capabilities of value-based reinforcement learning (RL) algorithms by incorporating a value bonus. Unlike previous studies that define exploration bonuses as reward distributions, this method offers optimistic exploratory value even for unvisited state-action pairs. The technique involves maintaining an ensemble of random Q-functions and predictors that estimate the underlying reward. The behavior policy then selects greedy actions based on the augmented Q-function.

The experimental results demonstrate the effectiveness of this bonus when applied to the Double Deep Q-Network (DDQN) algorithm in both classical environments and some games in the Atari suite. The agent optimizes state coverage, leading to improved rewards. Overall, the paper presents a promising approach to enabling deep exploration in RL algorithms.

### Strengths
The paper proposes a method to facilitate deep exploration in RL by combining an ensemble of Q-functions and random target functions. This method, which builds on prior research in uncertainty estimation and exploration strategies, offers a straightforward implementation of DQN variants and enhances exploration more effectively than traditional strategies like epsilon-greedy. The paper highlights a key strength: the ability to allocate optimistic value estimates to unvisited state-action pairs, a feature that methods that rely solely on reward bonuses do not offer.

While the experiments are somewhat limited in terms of computational requirements, they are designed to support the paper's claims. VBE achieves promising results in some interesting classical experiments. These experiments show that VBE can potentially replace undirected exploration strategies in value-based RL algorithms. However, the overall narrative in the experiments section becomes unclear due to the non-standard experimental settings. The comparisons between VBE and the baselines are further complicated by the differences in RL algorithms (DDQN vs. PPO) and allowed environment steps, where DDQN's superior sample efficiency makes the comparisons unfair.

In summary, the paper presents a promising method for deep exploration in RL, although further clarification and additional experiments comparing different RL algorithms could strengthen the paper's overall argument.

### Weaknesses
The initial sections of the paper are well presented, providing a clear introduction to the research. However, a more comprehensive contextualization with existing prior work on deep exploration, specifically related to value bonuses, would enhance the paper's relevance. A thorough literature review would help readers understand the specific problem and knowledge gap this work addresses.

The experiments section, while exploring interesting environments, falls short of the standards expected for empirical studies in deep RL. While the selected environments are interesting for validating the proposed method, a more impactful study would involve challenging and widely recognized hard-exploration tasks. Additionally, the experimental settings do not align with the standard parameters for fair evaluation of deep RL algorithms, particularly in the context of hard-exploration tasks. The comparison between different RL algorithms (DDQN, PPO) under such limited environment interaction raises concerns about the fairness of the evaluation. It remains unclear whether the observed learning curve superiority of VBE after 50k steps is due to DDQN's known sample efficiency compared to PPO.

In summary, the paper introduces an interesting idea and presents it effectively. However, the current experiments, while promising, lack the necessary impact due to the limitations in experimental design and evaluation. Addressing these concerns and conducting experiments on more challenging and standard hard-exploration tasks would significantly enhance the paper's significance.

### Questions
I am curious about the author's choice to allocate computational resources to run 30 different experiments, a number significantly higher than the typical 5-10 runs in deep RL. Instead, I would suggest using some of these resources for longer experiments, which might have offered a more fair analysis given the well-known sample inefficiency of deep RL algorithms.

I appreciate the authors' effort in providing the reference codebase for implementing the RND and ACB baselines. However, I am not convinced about the effectiveness of this particular implementation, given the limited popularity of the codebase. I am concerned that this implementation might not be able to replicate the results of the proposed baselines, especially for RND. I would suggest using the official implementations or more widely validated ones.

Additionally, I wonder if the authors had considered exploring other environments that offer challenging exploration tasks. Environments involving 3D navigation or procedurally generated maps could potentially provide a more impactful evaluation of the proposed method. Including such environments in the experimental setup could strengthen the paper's contribution.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
