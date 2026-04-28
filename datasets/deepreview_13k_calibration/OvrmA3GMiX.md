# Learning Transferable Sub-goals by Hypothesizing Generalizing Features

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Transfer is a key promise of hierarchical reinforcement learning, but requires first learning transferable skills.
For an agent to effectively transfer a skill it must identify features that generalize and define the skill over this subset.
However, this task is under-specified from a single context as the agent has no prior knowledge of what future tasks may be introduced.
Since successful transfer requires a skill to reliably achieve a sub-goal from different states, we focus our attention on ensuring sub-goals are represented in a transferable way. 
For each sub-goal, we train an ensemble of classifiers while explicitly incentivizing them to use minimally overlapping features.
Each ensemble member represents a unique hypothesis about the transferable features of a sub-goal that the agent can use to learn a skill in previously unseen portions of the environment.
Environment reward then determines which hypothesis is most transferable for the given task, based on the intuition that useful sub-goals lead to better reward maximization.
We apply these reusable sub-goals to MiniGrid and Montezuma's Revenge, allowing us to learn previously defined skills in unseen parts of the state-space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Learn a collection of hypotheses which take in varying collections of features using D-BAT, a method which . Then identify the hypothesis that has the best transferability. Relies on labeled training data for subgoals. Then give the agent the transferable subgoals.

### Strengths
The problem of robust skill generalization is necessary.

The motivation for the problem is clear

### Weaknesses
This work makes several overgeneralizing claims about the positioning of HRL. Some examples include (line 36) that the options based framework utilizes subgoals (the termination condition does not need to be goal based). The termination condition must be a set (line 80), when it is often formulated as a probabilistic condition function. The equivalence between termination sets and subgoals (line 83), since a set might contain many subgoals. The use D-BAT to claim generalizability (line 162): While there may be some amount of robustness added, there is an implicit assumption that by learning a robust classifier of subgoals, this implies that the same assumptions can be applied to goals in RL, which is both a different context and not necessarily true. This point would need to be proven theoretically and the empirical results would need to support this claim more directly.

The most glaring weakness is the level of imprecision realted to the method itself. In particular, it is not clear what the algorithm actually is. It appears to be 1) run D-BAT to get some features. 2) learn an option to achieve good hypothesis classification. However, it is not made clear what the inputs are for D-BAT, the reward function for the skills, the hierarchy, or almost any other detail of the algorithm.

The experimental results lack several components. First, the baselines compared are deep RL algorithms, not state of the art HRL algorithms. Second, neither method uses factorization or exploration. Third, the main paper lacks even a complete coverage of the tasks, since downstream performance is only evaluated in one task.

Finally, the work is entirely not self contained, since it relies heavily on D-BAT, without actually providing an adaquate formalism to describe D-BAT. Instead, the reader is expected to read this work. Furthermore, it is not obvious why this particular hypothesis algorithm is chosen over others, nor are there any ablations to indicate that D-BAT is preferable to other robust hypothesis algorithms---only comparison to a CNN.

### Questions
See Weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new method for skill discovery in hierarchical reinforcement learning which is designed to find skills which can be effectively transferred between tasks.
In order to do this, the authors focus on learning sub-goals with representations that facilitate this transfer by training ensembles of diverse classifiers for use as sub-task termination predicates.
The authors detail several experiments which evaluate different aspects of their method.

### Strengths
The paper addresses the important topic of learning transferrable skills for hierarchical RL and is generally well-written.

The method presented is a novel and interesting application of a diversity-based classification method to skill discovery.

Several experiments are included which are each intended to answer a different useful question.

### Weaknesses
Some parts of the experiments are unclear and overall the presented results are not convincing. Specific points follow.

For the quantitative results (Figures 3, 4, 5), I don't think that three seeds per curve is sufficient to reasonably compare the methods. While there isn't a definitive way to determine how many are needed, I would expect to see at least five to assess the variance due to random model initialization when the environment is deterministic.

In section 4.1, it is not clear what the ensembles are being compared against to determine the accuracy. I'm also not sure I agree with the claim that the performance when only one ladder instance has been seen is the most important given how low the accuracy is for all three models at that point compared to the two-ladder case.

For the MiniGrid results in Section 4.3, I am concerned about the lack of success with DQN and PPO. This environment is not so large that DQN/PPO should be unable to succeed when trained over 1.5 million steps, so it makes me think there is an error in the evaluation. Based on the hyperparameters in the appendix, one potential major factor for DQN is a lack of exploration. The reported performance of DQN and PPO is so poor that it is difficult to accept the comparison as valid without further investigation into the hyperparameter settings and training procedure.

The training process in Section 4.3 is not clear. It seems to state that data is collected from the different seed runs and used together to train the classifier ensembles, but this doesn't make sense with results being aggregated across the three seeds. It is unclear how the data from different seeds is being used to train the classifier ensembles, and how this relates to the reported results which are averaged across seeds. This mixing of data across seeds raises concerns about the validity of the experimental design.



### Questions
As mentioned above, can you explain the baseline how the accuracy is calculated in section 4.1?

As mentioned above, can you better explain the training process for the MiniGrid environment in section 4.3?

In Figure 6, why is the standard error shown instead of standard deviation?

$ $

Minor Notes:

Line 320: I believe this is meant to be a reference to Figure 4 rather than Figure 5.

Manhattan is misspelled several times.

### Soundness
2

### Presentation
3

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
The paper argues for the use of an existing technique called DBAT to learn ensembles of state binary classifiers in the context of Reinforcement Learning (RL). The use of each classifier is to encode a goal, understood as a set of states, which can be used to train an option policy. Relying on the motivation for DBAT, the paper explains and motivates empirically the use of an ensemble of classifiers, rather than a single one. In particular, they show that the ensemble classifiers do generalize to unseen states and that option policies can indeed be learned from them in the environment Montezuma's Revenge, while this is not the case for single classifiers (referred to as CNNs in the text). Moreover, they show how a hierarchical use of the options learned from   an ensemble of classifiers can solve a MiniGrid task where standard end-to-end deep RL algorithms fail.

### Strengths
Originality (and significance):
- The paper highlights an important and typically overlooked aspect of the problem of learning transferable state and goal representations in RL: it is not possible to tell what information is useful to transfer and for this reason multiple hypothesis, or a similar flexible representation, should be used, as opposed to a single standard architecture that tries to identify "the best" features.
- The paper introduces the use of a non-standard method to learn state classifiers in RL.

Quality:
- The paper provides multiple pieces of empirical evidence (three, to be exact) to demonstrate that the chosen technique, DBAT, is useful to encode goals, or, more generally, sets of states. 

Clarity:
- The organization of the paper is good. The problem and its motivation are well motivated and the exposition of the proposed solution follows a logical order.
- The Results section contains an explicit list of questions to be answered and it does attempt to explicitly answer each and every one of them.

### Weaknesses
The Introduction states that "To fully realize the benefits of HRL, learned options should be transferable. (...) existing HRL methods are unable to generalize an option from one context to another. This is primarily because all three components of the option are conditioned on the entire state, which includes spurious features unnecessary for successful execution." From this, I identify a main goal and two claims. The goal is to provide a scalable method to learn transferable options, and the claims are that no HRL method does this, and that the reason for why they fail is that, whatever methods are being used to learn option policies, they result in architectures that rely on spurious correlations to components of the input sensory stream. In my opinion, the goal is not achieved and the claims are not supported.

Why is the main goal not achieved?
1. There is no mechanism to discover the goals. The images used to train DBAT were hand-picked. How can this process work in more general settings? The paper does not address how these subgoals are identified in the first place, which is a critical component for any practical application. The reliance on hand-picked images severely limits the scalability and applicability of the proposed method. A truly generalizable approach should include a mechanism for autonomous subgoal discovery.
2. It is necessary to train preliminary options to generate rich enough data to train the ensemble classifiers. Where do these options come from? How can we guarantee that they will generate rich enough data? In this case they were clearly well chosen, e.g., the MiniGrid environment case contains the three option policies that are required to complete the general task (CollectRedKey,
OpenRedDoor, and GoToGoal). This begs the additional question. Having those options already, why bother to use a classifier to learn options that carry out the same task as the original options? The paper does not provide a clear justification for why learning classifiers on top of existing options is beneficial, especially when the initial options are already well-suited for the task. The need for these preliminary options introduces a strong dependency on a potentially expensive and difficult-to-obtain set of initial skills.
3. The way in which the option policies are obtained from the classifiers is unclear and possibly does not scale to more general settings. In particular, for the Montezuma's Revenge environment, the manuscript mentions that an agent is manually placed at the top of some stairs and then it is supposed to learn to go down the stairs. What happens when the agent is not placed on top? More generally, what happens in other tasks where there is no control over this initial state? The paper lacks a detailed explanation of how the classifiers are used to derive option policies. The manual placement of the agent in Montezuma's Revenge highlights a significant limitation in the method's ability to handle arbitrary initial states, which is a common requirement for real-world applications.
4. There is no evidence of transfer under different reward functions or dynamics. For MiniGrid, the option GoToGoal arguably already encodes a lot of information about the original reward function. The experiments do not demonstrate the transferability of the learned options across different reward functions or environment dynamics. The fact that the GoToGoal option in MiniGrid already encodes significant information about the reward function raises concerns about the method's ability to generalize to tasks with different reward structures.

Why are the claims not supported?
1. The paper ignores relevant literature in reward-agnostic option discovery, representation learning for RL, and multi-task reinforcement learning that partially solve the main goal addressed in the paper. For example:
   a. Agarwal R., et al., Contrastive Behavioral Similarity Embeddings for Generalization in Reinforcement Learning, ICLR, 2021.
   b. Barreto A., et al., Combining Skills in Reinforcement Learning, NeurIPS, 2019.
   c. Eysenbach B. et al., Diversity is All You Need: Learning Skills without a Reward Function, ICLR, 2019.
   d. Frans K., et al. Meta Learning Shared Hierarchies, ICLR, 2018.
   e. Gomez D., et al. Information Optimization and Transferable State Abstractions in Deep Reinforcement Learning, IEEE TPAMI, 2022.
   f. Klissarov, M. et al., Deep Laplacian-Based Options for Temporally-Extended Exploration, ICML, 2023.
   g. Touati, A. et al., Does Zero-Shot Reinforcement Learning Exist?, ICLR, 2023.
   h. Zhang A., et al., Learning invariant representations for reinforcement learning without reconstruction, ICLR, 2021.
More specifically, a., e., and h. provide techniques to learn transferable representations, similar to the proposed ensemble of classifiers; b., c., d., and f. introduce techniques to learn transferable skills, and g., provides a global policy that solves any given task provided access to its reward function. The paper fails to acknowledge and compare against existing methods that address similar problems. Specifically, techniques for learning transferable representations and skills, as well as reward-agnostic approaches, are not adequately discussed or contrasted with the proposed method. The absence of such comparisons makes it difficult to assess the novelty and contribution of this work.
2. The paper makes no comparison with any other hierarchical method. Is there any advantage to the proposed approach? The lack of comparison with other hierarchical RL methods makes it impossible to determine if the proposed approach offers any practical advantages. Without such comparisons, it is unclear whether the proposed method is competitive with existing state-of-the-art techniques.
3. The paper makes no empirical attempt to prove that the reason why any of the papers mentioned in the Background and Related section fail is because of the poor state generalization. The paper does not provide any empirical evidence to support the claim that the failure of existing methods is due to poor state generalization. This lack of empirical validation weakens the paper's central argument.

### Questions
- How are the sub-goals being used to train the option policies? Do they define a sparse reward that is equal to 0 unless the goal set is reached? How can you guarantee that learning this is not just as difficult as solving the original task?
- For MiniGrid, did you try learning a high level policy with the options that were used to train the ensemble classifiers? If so, how does it compare to the one using the classifiers?
- For MiniGrid, in total how many interactions did it take to train the original 5 options and then the 15 option policies corresponding to the ensembles? What happens if you run DDQN or PPO for that many steps? 
- For MiniGrid again, what are the standard techniques used to solve these tasks? If not DDQN or PPO, why did you select them? Sounds like this is a hard exploration problem, so RND of DCEO (Klissarov et al., 2023) could be used instead. If it is them, how did you select their hyperparameters? 
- What is the false positive rate of the CNN? If it is small, how do you explain that the CNN has high accuracy and yet leads to bad option policies? To me, this means that there is some problem with your accuracy calculation that does not capture transferability.
- How exactly did you pick the selected data for the training of the classifiers? More explicitly, what type of procedure did you follow? It sounds cumbersome separating all the images generated from the interaction with the environment.
- The paper claims that the rightmost image in Figure 5 is evidence of the option generalizing the notion of going down the ladder, but it shows the opposite to me. It shows that the agent only learned to go down a few steps, a similar or smaller number of steps than when it goes down in the original shorter stairs. Am I interpreting erroneously the dots being displayed?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies transferable skills and sub-goal generalization in the hierarchical reinforcement learning framework; the authors propose that the RL agent maintain several, diverse hypotheses over which features of the state might generalize in the future, focusing their attention on ensuring sub-goals are represented in a transferable way. The agent then selects from among these hypotheses, tests one of them in the environment, and updates its beliefs over which member of the ensemble has learned transferable features. Their work focuses on generalizing forward from a single option instance instead of retroactively compressing previously learned skills. Their work differs from previous related research by learning multiple hypotheses, each of which is a unique state representation. They apply these reusable sub-goals and perform an empirical study to MINIGRID and MONTEZUMA’S REVENGE environments, allowing agents to relearn previously defined skills in unseen parts of the state-space. Lastly, the authors seek several essential questions and tend to look for answers with their experiments and to test a consolidated RL agent on a challenging sparse-reward problem. 
.

This paper is a magnificent algorithmic contribution to the hierarchical RL and reinforcement learning community in general and I strongly accept it as it is considered to be an authentic contribution to the ICLR conference.

The main contributions are the following:
- Forming each ensemble member as a unique hypothesis about the transferable features of a sub-goal that the agent can use to learn a skill in previously unseen portions of the environment.
- In contrast to previous methods that focus on the initial discovery of sub-goals their work focuses on transferring an existing subgoal and so can be used in tandem with any of these methods. 
- Presenting sub-goals in a transferable way and empirically performing sub-goal generalization.

### Strengths
This paper does a great job of presenting novel authentic contributions. For originality, the paper tackles an important problem: How can learned features be transferable in HRL? The authors propose a very revolutionary concept;“hypothesis” to learn about the transferable features of a sub-goal that the agent can then use to learn a skill in previously unseen portions of the environment. Furthermore, their work builds upon and intersects with different methods: 1. Identifying sub-goals by focusing on transferring an existing subgoal and so can be used in tandem with any of the existing methods. 2. Learning Transferable Skills by generalizing forward from a single option instance instead of retroactively compressing previously learned skills. 3. Unsupervised Representation Learning by learning multiple
hypotheses, each of which is a unique state representation. The use of the Diversity-By-Disagreement Training (D-BAT) Algorithm by generating a set of labeled data representative of the option sub-goal with the intention of generalizing this option to unseen contexts. Eventually, the authors build brilliantly upon the RL hypothesis, i.e. the most transferable hypothesis will lead to higher external reward, providing a high-level policy. When this high-level policy maximizes extrinsic reward, it will naturally begin selecting hypotheses that best support transfer.


The significance of their work is integrating D-BAT which leverages both labeled and unlabelled data to train an ensemble of classifiers, each attending to a different set of features. Each ensemble member is encouraged to reduce the labeled loss while also decreasing agreement on the unlabeled data. As a result, each ensemble classifier represents a unique hypothesis of what features will generalize to out-of-distribution data, informed by the unlabelled data that was provided. 

The empirical experiments were conducted to investigate and answer each question. The quality of their investigations is good and reflects each question considering both accuracy and the amount of labeled data required for successful sub-goal generalization as clearly shown in Figure 3. The authors succeed in validating each component of their algorithm. Additionally, experiments were done in MiniGrid DoorKey and MONTEZUMASREVENGE. Environments conclude that the D-BAT ensemble sub-goals can be used to learn policies that transfer the initial option as shown in Figure 5 and Figure 6. In general, this paper does a great job theoretically and empirically.

### Weaknesses
There seems no math or theorem that further explains your method or explains your formulation of "hypothesis" as a mathematical concept. This is particularly called into question due to the lack of math notations. In addition, no pseudocode was provided nor any clear statements about the connection with The Diversity-By-disAgreement Training (D-BAT) algorithm. More discussion on these areas would be much appreciated.

For the empirical study, the choice of baselines in the MONTEZUMA’S REVENGE Environment 
was restricted to the CNN classifiers without any clear explanation which makes it unclear for the reader. Similarly, there was no discussion of the choice of baselines in the MINIGRID DOORKEY Environment. 

Minor comments:
P.6, Line 1 “need to be” instead of “need be”.

### Questions
I am very interested in your formulation of “hypothesis” but at the same time was disappointed for not seeing enough explanation or theorem that covers your idea. How did you exactly formulate “hypothesis” in your code? Can you provide any theorem and/or math notations that support your formulation?

In what respect does your use of representation learning differ from using dimension reduction? How do you exactly provide the high-level policy? 

In Figure 3, you mentioned that “this performance is on a collected set of data and does not fully encompass all the possible states an agent may encounter during policy learning.” How would the result differ from not using a collected set of data or any suggestions to overcome this? Why did you use the PPO and DQN agents to compare with? Similarly, why did you choose the CNN classifiers to compare with? A bit more discussion on these choices would be helpful.

### Soundness
3

### Presentation
4

### Contribution
2
