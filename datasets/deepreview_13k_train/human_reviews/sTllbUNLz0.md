# Incorporating Human Preferences into Interpretable Reinforcement Learning with Tree Policies

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Interpretable reinforcement learning (RL) seeks to create agents that are efficient, transparent, and understandable to the populations that they impact. A significant gap in current approaches is the underutilization of human feedback, which is typically employed only for post-hoc evaluation. We propose to center the needs of end users by incorporating the feedback that would be obtained in a user study directly into the training of interpretable RL algorithms.  Our approach involves preference learning, where we learn preferences over high-level features that are not directly optimizable during the RL training process. We introduce an evolutionary algorithm that leverages user feedback to guide training toward interpretable decision-tree policies that are better-aligned with human preferences. We demonstrate the effectiveness of our method through experiments using synthetic preference data. Our results show an improvement in preference alignment compared to baselines, yielding policies that are more aligned with underlying user preferences but does so with sample efficiency in the number of user queries, thereby decreasing the burden on the user in providing such data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a framework that can construct decision-tree policies based on human preferences, i.e. paired comparisons. This framework first generates a pool of candidate tree policies using an imitation learning algorithm and then iteratively refine its estimate of the optimal one using an evolution strategy. During the iterative refinement, humans are required to compared policies, which is used to optimize a weighting vector of criteria for policies. The authors validate their method on CartPole and PotholeWorld, showing that their method generates policies that are better aligned with synthetic preferences.

### Strengths
1. The proposed framework is clearly presented in the paper.
2. The motivation is clear and persuasive.

### Weaknesses
The main weakness of this paper is the set of assumptions used for simplifying the learning problem, which I think are unrealistic. In specific:

1. It is assumed that humans can compare two tree policies and give reliable feedback. While I agree that, tree policies are interpretable in the sense that decision rules can be read from visualizations, it is questionable if humans can compare two trees reliably. For example, this requires humans to precisely predict the consequences of any change in single or multiple leafs. On the contrary, in recent literature of PbRL, humans are only require to compare trajectories, which is much less demanding than comparing policies directly.

2. It is assumed that a d-dimensional feature vector $f_\pi$ can not only summarize the structure of a tree but also all information required for decision-making. This assumption significantly restricts the applicability of this method.

In addition, though interpretability is considered as the motivation of this paper, there is no qualitative results on the extent of interpretability of learned policies.

### Questions
1. Can this method be applied to more complex domains, such as the Mujoco tasks (Ant, HalfCheetah, or Humanoid)?
2. Could you provide some examples of preference queries (for both simple and complex tasks) and learned policies as evidence for applicability of this method?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Policies that are decision trees are convenient because they are interpretable. People may also have preferences between such policies, and one may want to elicit preferences from users while learning policies. This work identifies this combination as a novel problem and presents one way to incorporate human preferences as part of the policy training process to favor more interpretable policies parameterized by decision trees.

This paper is essentially doing active learning for user preferences (with a fixed budget for querying users) on decision trees, and also learning decision trees according to these preferences. Each component of the proposed method (how to choose which examples to query user preferences for, how to fit trees to preferences, how to model user preferences) is some sort of heuristic, some of which have been used previously in other settings. The authors demonstrate their method on two synthetic settings, with synthetic preferences.

### Strengths
I had not seen this problem setting before, so it seems original to me. The formulation of the setting is written in a clear way. In terms of clarity, the proposed method is explained in the text in a way that is reasonably clear.

### Weaknesses
 * **Motivation** Although it seems reasonable to want to have preferences over decision trees policies, I am not convinced that the framing as an active learning problem setting is important and realistic (a strong concrete motivating example is not present), and the synthetic nature of the experiments do not help. Also, see questions. The work seems inspired by RL with human feedback, and in that literature, methods are typically developed using preference datasets that are collected offline in a batch, rather than online.

* **Method is entirely heuristic (and evaluations are not realistic)** The proposed method is entirely heuristic and a lot of choices are not really justified (see questions section). This, combined with limited experiments, makes it difficult to understand under what settings it could perform well vs not. Also see questions on hyperparameter choice. I think this would be fine if either the problem setting and experiments were very convincing, or if the method is principled, or you can prove its performance. 

* **Experiments are not realistic** The experiments assume that a user's utility is linear in {reward, depth, num leaves, state feature used}, which seems unrealistic. Is there a realistic setting where someone would want a linear tradeoff between reward vs e.g. depth, rather than e.g. put a limit on depth and then maximize reward (which you could do very simply)? 

* **Presentation** Although the method is reasonably clear from reading the text, there are still many issues with presentation: the notation is inconsistent, and I found Figure 1 difficult to understand, even though it is visually pleasing. 
    * Notation in (3) is inconsistent: sup vs subscripts for $i,j$
    * Notation inconsistency for (4); the text suggests it should be $\hat\Pi_T$ not $\hat\Pi$
    * Indexing for $\hat\theta=\hat\theta_i,\ldots,\hat\theta_N$: what is $i$?
    * Line 213: preference estimates $\Theta=\theta_1,\ldots,\theta_N$. Why the sudden change from $\hat\theta$ (line 194-195) to $\Theta$?
    * Line 200-201: $\hat\theta_t$ where $t$ indexes timestep, not which estimate within a set (ensemble?) of estimates
    * Even more inconsistent notation with line 1 in Algorithm 1
    * What is $m$ in (7)? It does not seem to be the mapping $m$ from (1).
    * Figure 1 would benefit from the thetas being labeled as preference estimates, and the blue stuff being labeled as policy estimates (or similar). I'm not sure what "feature vectors" in Figure 1 refers to. It also has way too many arrows for me to know how I should be reading it. It only made sense after reading the rest of the paper. I don't understand what the grey box is in relation to the rest of the diagram.

### Questions
* **Problem setting motivation** What is a concrete and realistic motivating example for this problem setting? Why does the data collection about human policy preferences need to be done at the same time as training? When would this be useful and also realistic? 

* **Hyperparameters** How were the hyperparameters (for each of the heuristic components) chosen in the experiments, and how they would be chosen in a real-world setting?

* **Heuristic choice**
    * Why is this novel selection process a good idea? Why does it use the updated $\theta_j^{(i)}$ vs $\theta_j^{(k)}$ rather than the gradient updates $\eta\nabla \mathcal L$ instead? Why is this preference update a good idea? Are there reasons besides that it seems kind of reasonable and seems to perform ok? 
    * Why is pareto frontier filtering a good idea besides that it seems reasonable? Are there better alternatives? 
    * In practice, how did you choose the hyperparameter $c$ in (9)? Why is a UCB-inspired bound a good idea, besides that it seems reasonable? 
    * In what settings would which parts of this method work vs not?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an attempt to incorporate human preferences into the training of interpretable decision-tree (DT) policies for reinforcement learning (RL) using an evolutionary strategy.
They present PASTEL (Preference Aligned Selection of Trees via Evolutionary Learning), a method that employs an evolutionary algorithm to optimise tree policies using feedback from users.
Through iterative comparisons, it adapts policies to improve interpretability and alignment with user preferences, while maintaining good performance on the task at end. The paper includes an experimental evaluation in two RL environments, CartPole-v1 and PotholeWorld-v0, demonstrating that PASTEL produces policies that are preference-aligned and interpretable with high sample efficiency.

### Strengths
- The paper and writing are fairly clear
- I thought the Preference Elicitation and Bayesian Experimental Design related literature section was comprehensive and well done
- The authors discuss the issue of balancing optimising human preferences but also succeed at the task at hand, and design an algorithm that takes this into consideration, generating (via the evolution algorithm) diverse methods of solving the task so to get feedback on the preferred method from humans.
- The evolutionary algorithm and the use of Pareto frontier filtering to reduce the number of candidate policies are clever strategies that improve the sample efficiency of the preference elicitation process. This approach minimises the burden on users while still aiming to produce high-quality, preference-aligned policies with limited data points.
- While the use of evolutionary strategies is not groundbreaking, it is nonetheless an interesting application for generating interpretable policies that can adapt based on user feedback. The method effectively addresses the non-differentiability of decision trees, showcasing a practical approach for optimising such structures in an RL setting.

### Weaknesses
I believe the work has significant issues in terms of positioning within the broader literature

- The paper fails to connect with key frameworks and research in preference optimization, especially in the context of reinforcement learning from human feedback and large language models. The authors mention that they use preferences during training to align policies with human feedback, but they omit the well-known fact that leveraging preferences is common practice in LLM fine-tuning. Even though this work focuses on interpretable policies rather than neural networks, this comparison is important for understanding the relevance of their suggested approach. Given the work’s emphasis on preference alignment, it is surprising that methods from preference optimization and alignment strategies in LLMs are not discussed at all. The omission creates a significant gap in situating the proposed method in the current research landscape.
- Unclear Scalability and Limited Experiments: The choice of evolutionary strategies to optimise decision trees is interesting but not particularly novel. The experimental validation is also highly limited, featuring only CartPole and PotholeWorld. This narrow scope raises serious questions about the method’s scalability and effectiveness on more complex, real-world problems, and this was not even mentioned in the limitations section. I think a real-world application example where DTs could be effectively used to solve the issue is an important missing point. 
- Mention of Imitation Learning / Inverse Reinforcement Learning: I think this is less important than the other weaknesses I listed above, but it is interesting the authors use VIPER (based on DAgger) and Imitation Learning / Inverse Reinforcement Learning are not discussed at all in the background or related work. I think it would have also been interesting to compare or have a comment on preference elicitation vs recovering rewards using Inverse Reinforcement Learning. But this is a nit.
- A nit but I didn't really think the 2 papers referenced on lines 101-102 were particularly related to what was being discussed in that sentence, or were particularly good examples.

### Questions
- How does this method scale to more complex environments? And non-synthetic human feedback?
- Why an evolutionary algorithm? Why this choice and what else was considered?
- Decision trees have known limitation in complex / high dimensional data settings, would this apply to complex user feedback too?

### Soundness
2

### Presentation
1

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
Motivated by interpretability in reinforcement learning, this work proposes a method (PASTEL) for injecting human preferences into decision-tree policies. The general method uses an evolutionary strategy guided by user feedback, iteratively refining its estimate of user preferences and generating new candidate policies. Overall, experiments on CartPole and PotholeWorld demonstrate that PASTEL produces policies that are more aligned with user preferences, and are also more sample efficient compared to baselines like VIPER.

### Strengths
The paper clearly defines the problem, user preference model, and learning objective.
The paper has a well designed and modular algorithmic framework (though it is quite complex). Particularly: (1) the interpretable policy generation uses an evolutionary algorithm tailored to user preferences, generating new candidate policies that progressively align with user desires; and (2) PASTEL's Pareto frontier filtering and adaptive policy evaluation mechanisms aim to minimize the number of user queries.

### Weaknesses
1. The authors acknowledge the limitation of using synthetic data and assuming static user preferences, suggesting future work to address this using real-world data and models of evolving preferences. Still, I find it significantly limits the generalizability of the results. Particularly, the authors propose an extremely complicated algorithm, yet only demonstrate it on synthetic simple environments. While the motivation of their method is clear, the complexity of their approach calls for much more involved experiments, to test the scalability of PASTEL on larger and more complex RL environments with higher dimensional feature spaces. I would also strongly recommend adding user studies with actual human participants to validate the effectiveness and user experience of PASTEL.

2. Real user preferences are likely far more complex, potentially involving non-linear relationships, inconsistencies, and individual variations that are not captured by the simple linear utility model employed with synthetic data. The authors should incorporate user studies with real human participants, evaluating the algorithm's ability to generalize to their utility functions.

3. The experiments use a relatively small and pre-defined feature set for representing DT policies. A broader or automatically discovered feature set could better capture user preferences.

4. The use of an RL agent for initializing the DT policy population has a potential to introduce bias in the initial policy. This initialization could steer the search process toward a region in the policy space that neglects user preferences in favor of higher reward. Although diversity is introduced through modifications to VIPER, the underlying influence of the reward-based initialization could limit the exploration of policies that maximize user utility.

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2
