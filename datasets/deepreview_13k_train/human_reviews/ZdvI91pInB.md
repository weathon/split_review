# Discovering Logic-Informed Intrinsic Rewards to Explain Human Policies

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
In high-stakes systems like healthcare, it is essential to distill high-level strategic knowledge from top clinicians’ demonstrations. This paper aims to extract knowledge-driven reward functions from experts’ demonstrations, representing the knowledge as a set of logic rules. Our learning framework is built upon the classic inverse reinforcement learning (IRL), assuming that the experts, like clinicians, are rational and their executed treatments are the optimal planning results via maximizing their logic-informed utility function. Our algorithm can automatically extract these logic rules from demonstrations. Specifically, we formulate reward engineering as a backward reasoning procedure, where a rule generator is trained to sequentially generate predicates starting from the goal and then considering conditions and evidence. We interpret policy planning as a forward reasoning procedure, where the optimal policy is obtained by finding the best path to forward chaining the given rules. This sequential optimization process involves refining the policy function, Q-function, and reward function, ultimately leading to the discovery of the most effective strategic rules. In our experiments, we demonstrate the superior performance of our method in discovering meaningful logic rules within the context of a healthcare problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors introduce a method that learns a logic tree and a policy using inverse reinforcement learning from observational data from experts, which is ultimately presented as a set of logical rules. Further, this logic tree allows the recovery of the reward function, using q-function estimation, which is then used for the reward estimation. State-action demonstrations are used as the raw input of the method. The logic tree is then generated in a top-down manner, through a transformer based model, which is then fed to a GAN model to estimate the agent policy. Evaluation was done both on synthetic (3 datasets) and real-world (1) datasets. Authors evaluate the method in a healthcare context and use MIMIC-3 and MIMIC-4 datasets. The F1 score and recall is measured for the predictions of the diagnosis, across 6 baseline models.

### Strengths
-Extracting logic rules in high-stakes domains is valuable and can facilitate better decision making.
-A good selection of baseline methods are compared, showing the strength of the proposed model.

### Weaknesses
There are several weaknesses of the method, detailed below.

-The major weakness I see in the paper is in the framing of the problem as an interpretability problem, where authors acknowledge the lack of interpretability in black box policies and how in high-stakes domains. The logic rules are presented as the high level explanations that can provide interpretability. While this is a reasonable assumption, this is not detailed further in the paper, or discussed in the evaluation section. E.g. A large logic tree might not be inherently interpretable, where the selection of the rules to be explained can be important.
- While there is a good selection of baseline methods compared, the synthetic/toy datasets need further additions of planning domains/datasets.

### Questions
-What are the computation times for the MIMIC and synthetic datasets?  It will be helpful for the reader to understand the computation requirements.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new technique for Inverse Reinforcement Learning grounded in constructing Logic Trees that can help with interpreting a given expert policy dataset while also yielding the policies deployed by the expert. It does this by means of a neural rule generator that creates a tree in a top down fashion. These trees are modeled to fit the trajectory data by means of a logic-informed energy function which is further combined with a GAN-based framework to determine the parameters matching the data. This is then used to get a policy matching the logic tree following which the reward distribution can be estimated as well. Experimental results show the resulting policies are interpretable while also being more efficient in several RL-based settings. Real-world results on the MIMIC-III and MIMIC-IV datasets also demonstrate sufficient performance while maintaining interpretability.

### Strengths
- Logic based tree formulation is simple yet informative on the exact decision making process by the expert policies.
- Strong results in the RL-based experiments (Table 1) showing promise of performance while maintaining interpretability.

### Weaknesses
 - Results in Table 2 on Diagnosis Prediction may be too close to edge out competing methods (Chet [1]) albeit being more interpretable by means of the Logic Tree.
- It is not entirely clear how to determine the  predicates for any given problem. The quality of these predicates will largely determine the quality of the logic tree and output policy. Specifically, the method's reliance on manually defined predicates raises concerns about its generalizability and potential for bias, as the selection of predicates can significantly influence the learned logic rules and subsequent policy. Furthermore, the absence of a systematic procedure for predicate selection makes it difficult to replicate and validate the results across different domains.



### Questions
1. How does the algorithm handle redundant sets of nodes in a given Logic tree? Is there a pruning procedure?
2. How are the predicate variables determined? Are the functions of the observation space manually provided by the user for a given dataset? E.g. Above(x,y) in the Blockworld experiments
3. Could there be any additional experiments showing the effect of input predicate set choice on the final result?
4. How are the competing algorithms being shown fairly since they are not provided these informative predicates? Could they be included as part of the observation space and run again?

Minor Typos:

Introduction (paragraph 4) : “Our ILR involves”

Fig. 3 “Sucess”

Fig. 4 “Temperture”

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, a novel logic-informed Inverse Reinforcement Learning (IRL) framework is introduced. The approach embodies inverse optimal control through policy optimization, where logic rules are learned from expert trajectories and serve as the energy function. The policy is optimized to estimate the energy model's partition function. Essentially, the policy is trained to generate state-action trajectories that minimize the energy function encoded from the currently learned logic rules, ensuring better adherence to the logic rules. The paper employs a GAN-style training scheme to update these logic rules by discerning trajectories generated by the policy from expert trajectories. The framework utilizes a neural logic tree generator to sequentially derive logic rules from goal variables, mimicking backward reasoning, and employs policy learning to determine the most effective path to achieve the end goal based on the current logic rules, akin to forward reasoning. This alternating process of backward and forward reasoning continues until convergence is attained, enabling the method to potentially learn the optimal probabilistic distribution of logic trees and the policy.

### Strengths
* Interpretability: The paper introduces a novel Inverse Reinforcement Learning (IRL) framework that learns both logical reasoning processes employed by experts and policies from observational data. This dual-learning approach improves policy interpretability, distinguishing it from traditional black-box solutions. Logic rules learned from this framework can be used to explain the observational state-action trajectories from expert demonstrations.

* Reward Recovery: The paper introduces a reward learning framework that appears to be both manageable and effective. This framework facilitates the automatic exploration of intrinsic logical knowledge, as manifested in the symbolic logic trees implicitly employed by experts for guiding reward design.

* The experiment results regarding policy and logic rules learning seem convincing.

### Weaknesses
I have a positive view of this work. However, the reason for not assigning a positive score to the paper lies in the absence of a clear evaluation of the reward discovery aspect (as mentioned in Section 4.2, a claimed contribution of this paper). While Section 4.2 provides informative content and closely follows the prior work of deep PQR (Geng et al., 2020b), the central focus appears to be on the relationship between the discovered rewards and the learned logic rules. Unfortunately, the paper lacks concrete examples or evaluations to support this argument. Particularly, there is a lack of evaluation regarding whether it is possible to predict the decision-making of the experts using the estimated reward functions on benchmark tasks.

Similarly, there has been no evaluation conducted on the quality of the learned logic rules.

### Questions
For practical application of this approach, users are required to define predicate sets beforehand to facilitate the learning of logic rule-informed energy functions. I am curious whether there has been an ablation study conducted to assess the algorithm's performance concerning the quality and suitability of the provided predicates.

Is there any evaluation regarding predicting the decision-making of experts using the estimated reward functions on your benchmarks?

Could you assess the precision and recall of your learned logic rules in comparison to expert decisions on the provided benchmarks?

Why do Sec 5.1 and Sec 5.2 use different baselines?

Was the evaluation conducted in a fair manner for all the baselines? For instance, NLRL does not utilize expert trajectories and learns directly from an MDP. In contrast, your approach benefits from access to expert trajectories.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed an inverse reinforcement learning method to discover a logic-informed reward function. Assuming demonstrations were generated by experts following an optimal energy-based policy, it alternates between learning a neural logic tree and learning policy until convergence with a GAN-framework from a previous work. The energy function is parameterized using logic-informed features given a set of generated logic rules. Specifically, a transformer-based reader encodes the observed state-action demonstrations to a set of Boolean logic variables (predicates), then a decoder predicts the next predicate based on the previously generated partial symbolic tree. Experiments on toy games and two highly correlated real healthcare datasets show overall improvement from several benchmarks under two metrics each.

### Strengths
1. proposed a novel approach to IRL.
2. the way the logic rules inform the energy function and consequently the policy makes sense to me.

### Weaknesses
1. lack of clarity and justification. E.g., why is the traversal pre-order, how is the set of predefined labeling functions predefined, what is grounded predicate sequence, why grounded predicate is divided into characters by the 'first' block of the abstract symbolic tree reader. If the tree is based on transformer, perhaps the authors could focus more on how the tree is built upon transformer and the difference between the two. See more major ones in my questions.
2. since the contribution is on logic-informed IRL, would be good to show and analyze the logic rules discovered along a trajectory as opposed to a single snapshot.


### Questions
1. what is the numerical form of the tree? Eq. 6 only specifies the likelihood of the tree in terms of pre-order traversal sequence, but not the structure thereof (i.e. parent/children nodes).
2. are the cardinalities of the index sets $I_k^1$ and $I_k^0$ same across $k$?
3. how is the node chosen for expansion and how is it expanded? By what criterion you'd know the tree cannot be further expanded?
4. does the order of the predicates generated matter? at the same tree horizon?
5. how is the goal $X^0$ decided, is it always success v. fail? Is it constant throughout a trajectory or changing over timesteps? If it's the former how can you make sure it is the right goal for all timesteps (one step of mishap would not necessarily reasult in an overall failure and vice versa), if the latter then how is the step-wise goal specified without too much human knowledge?
6. in estimating the overall energy function, since the tree generator is amortized, why you can use the top-K logic trees with generated probabilities as the probabilities may change later? And can you not use unweighted trees (e.g. taking average of all trees) to approximate the expectation?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good
