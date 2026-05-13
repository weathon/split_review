# State Combinatorial Generalization In Decision Making With Conditional Diffusion Models

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Many real-world decision-making problems are combinatorial in nature, where states (e.g., surrounding traffic of a self-driving car) can be seen as a combination of basic elements (e.g., pedestrians, trees, and other cars). Due to combinatorial complexity, observing all combinations of basic elements in the training set is infeasible, which leads to an essential yet understudied problem of $\textit{zero-shot generalization to states that are unseen combinations of previously seen elements.}$ In this work, we first formalize this problem and then demonstrate how existing value-based reinforcement learning (RL) algorithms struggle due to unreliable value predictions in unseen states. We argue that this problem cannot be addressed with exploration alone, but requires more expressive and generalizable models. We demonstrate that behavior cloning with a conditioned diffusion model trained on expert trajectory generalizes better to states formed by new combinations of seen elements than traditional RL methods. Through experiments in maze, driving, and multiagent environments, we show that conditioned diffusion models outperform traditional RL techniques and highlight the broad applicability of our problem formulation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the problem of RL generalization from a state distribution covering only certain combinations of objects to a state distribution covering new combinations of objects.
The key contribution is to use a conditional diffusion model, where the diffusion model is given information about the objects in a state.
Using this model in RL amounts to planning, where the model is used to generate a trajectory and select the first action in the trajectory.
Evaluation is performed on an autonomous driving simulator, the starcraft multi-agent challenge and various maze environments.
Relative to a behavioral cloning baseline, constrained Q-learning and vanilla PPO, the diffusion model seems to improve generalization to the test environment that contains unseen combinations.

### Strengths
- The problem of out-of-combination generalization is motivated clearly, and it's relevance to RL is demonstrated across a few problems.
- Relative to the baseline considered, the proposed conditional diffusion model is clearly an improvement across an autonomous driving simulator, starcraft multi-agent challenge and various maze problems.

### Weaknesses
 - The proposed method of using a conditional diffusion model for planning is not detailed very clearly.
- The experiments lack any strong baseline to accurately judge the proposed method. The authors cite a few prior works on combinatorial generalization in RL, but the experiments do not include any representative baselines. It is not clear whether the benefit of the proposed approach is due to the larger model used by the diffusion model, or the specific combination of offline RL with expert data and the proposed model. While some ablations are performed over the type of conditioning, these results do not seem entirely conclusive, except that no conditioning is always worst.

- Figure 2 and discussion of subtasks: I am not sure I understand the difference between the proposed definition of combinatorial generalization and trajectory stitching. With trajectory stitching, there can also be a combinatorial generalization problem if the stitched trajectories include some trajectories with some subtask and another trajectory with another subtask. The policy on the stitched trajectory would have seen each subtask separately, but not together.
- Problem Formulation and scope of experiments: By construction the problem setting requires some notion of "object identity" for the model to be conditioned on. I consider this a serious limitation of the wide applicability of this approach, as very few RL environments come with predefined objects. One way to demonstrate wider applicability is if the proposed approach could also be combined with a method that performs image segmentation to identify objects.
- Problem formulation and test mismatch: How can a practitioner know whether the test distribution differs from the train distribution in the combination sense? Is it possible that the proposed approach can improve over the baseline on problems where there is no out-of-combination distribution? (e.g., without any objects, or when all the combinations are covered)
- Wouldn't section 4 be better titled "Why Offline RL Fails"? Even this requires further qualification. It is not clear how CQL is trained here and what information is provided to it in terms of conditioning.
- Section 4 (Offline RL focus): Is there necessarily a case for studying this problem exclusively with offline RL? For example, better OOC generalization can contribute to faster learning with PPO on the previously unseen environment.
- Section 4 conclusion: Again, while it is true that offline RL methods are not well-suited to the problem where the training environment is different from the testing environment, this is to be expected. The problem of RL is solving an MDP, not transferring from one MDP to another.
- Section 5.2 (linear manifold): this section is confusing, why is the latent space a linear subspace in maze naviation?
- Section 5.2 (manifold hypothesis) The manifold hypothesis, that the latent space is much smaller, has only really been demonstrated in the case of supervised or self-supervised learning. Is there evidence that suggests a similar hypothesis  holds true for problems involving sequential decision making? (Even if a low dimensional representation exists for one-step prediction, the representation for long-term value estimation needs to account for expected future state occupancy.)
- Section 6: this section is critical to understanding the proposed method, but many of the details (Figure and Algorithm Pseudocode) are in the appendix. Why is the specific architecture chosen (Diffusion UNet), and what contributed to the use of only expert trajectories? What does it mean to model the action (Algorithm 1 does not seem to model the action)?
- Section 7.1 and Figure 4: I think a stronger and more representative baseline must be included to make meaningful conclusions here. Additional details on how PPO/CQL was trained and evaluated are needed. For example, did PPO and CQL have the conditioning information? Was PPO trained online (appendix mentions 2 different instances of PPO were used to gather data in the all-car or all-bike environment, unclear if this was used for PPO performance in Figure 2)?
- Section 7.2 and Figure 5: The use of even fewer baselines here makes any conclusions difficult to make. Additionally, error bars seem to be missing.
- Section 7.3 and Figure 6: I am not sure that these qualitative results demonstrate "how" conditional diffusion models generalize, but rather that they do generalize. I have a hard time understanding what Figure 6 is meant to convey. Would other models not identify the dynamics of specific units? A quantitative analysis, showing correlations between trajectories for specific conditionings, may be more clear.
- Section 8.1 and Figure 7: Can you comment on how this evaluation differs from other work on trajectory stitching?
- Section 8.2 and Figure 8: It is not clear that cross attention is large improvement over concatenation without error bars. The performance difference can also be explained by additional parameters introduced by attention.

** Minor Comments
- I believe the pseudocode in the appendix has a typo: there is an "x_{t-1}" variable on line 995 that should probably be "s_{t-1}"
- Measure theoretic definition: because you work with a finite, countable set of latents, the measure theoretic definitions do not seem necessary. I think Section 3 can be made more clear and concise by focusing on the discrete setting.

### Questions
- Figure 2 and discussion of subtasks: I am not sure I understand the difference between the proposed definition of combinatorial generalization and trajectory stitching. With trajectory stitching, there can also be a combinatorial generalization problem if the stitched trajectories include some trajectories with some subtask and another trajectory with another subtask. The policy on the stitched trajectory would have seen each subtask separately, but not together.
- Problem Formulation and scope of experiments: By construction the problem setting requires some notion of "object identity" for the model to be conditioned on. I consider this a serious limitation of the wide applicability of this approach, as very few RL environments come with predefined objects. One way to demonstrate wider applicability is if the proposed approach could also be combined with a method that performs image segmentation to identify objects.
- Problem formulation and test mismatch: How can a practitioner know whether the test distribution differs from the train distribution in the combination sense? Is it possible that the proposed approach can improve over the baseline on problems where there is no out-of-combination distribution? (e.g., without any objects, or when all the combinations are covered)
- Wouldn't section 4 be better titled "Why Offline RL Fails"? Even this requires further qualification. It is not clear how CQL is trained here and what information is provided to it in terms of conditioning.
- Section 4 (Offline RL focus): Is there necessarily a case for studying this problem exclusively with offline RL? For example, better OOC generalization can contribute to faster learning with PPO on the previously unseen environment.
- Section 4 conclusion: Again, while it is true that offline RL methods are not well-suited to the problem where the training environment is different from the testing environment, this is to be expected. The problem of RL is solving an MDP, not transferring from one MDP to another.
- Section 5.2 (linear manifold): this section is confusing, why is the latent space a linear subspace in maze naviation?
- Section 5.2 (manifold hypothesis) The manifold hypothesis, that the latent space is much smaller, has only really been demonstrated in the case of supervised or self-supervised learning. Is there evidence that suggests a similar hypothesis  holds true for problems involving sequential decision making? (Even if a low dimensional representation exists for one-step prediction, the representation for long-term value estimation needs to account for expected future state occupancy.)
- Section 6: this section is critical to understanding the proposed method, but many of the details (Figure and Algorithm Pseudocode) are in the appendix. Why is the specific architecture chosen (Diffusion UNet), and what contributed to the use of only expert trajectories? What does it mean to model the action (Algorithm 1 does not seem to model the action)?
- Section 7.1 and Figure 4: I think a stronger and more representative baseline must be included to make meaningful conclusions here. Additional details on how PPO/CQL was trained and evaluated are needed. For example, did PPO and CQL have the conditioning information? Was PPO trained online (appendix mentions 2 different instances of PPO were used to gather data in the all-car or all-bike environment, unclear if this was used for PPO performance in Figure 2)?
- Section 7.2 and Figure 5: The use of even fewer baselines here makes any conclusions difficult to make. Additionally, error bars seem to be missing.
- Section 7.3 and Figure 6: I am not sure that these qualitative results demonstrate "how" conditional diffusion models generalize, but rather that they do generalize. I have a hard time understanding what Figure 6 is meant to convey. Would other models not identify the dynamics of specific units? A quantitative analysis, showing correlations between trajectories for specific conditionings, may be more clear.
- Section 8.1 and Figure 7: Can you comment on how this evaluation differs from other work on trajectory stitching?
- Section 8.2 and Figure 8: It is not clear that cross attention is large improvement over concatenation without error bars. The performance difference can also be explained by additional parameters introduced by attention.


** Minor Comments
- I believe the pseudocode in the appendix has a typo: there is an "x_{t-1}" variable on line 995 that should probably be "s_{t-1}"
- Measure theoretic definition: because you work with a finite, countable set of latents, the measure theoretic definitions do not seem necessary. I think Section 3 can be made more clear and concise by focusing on the discrete setting.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose to describe RL tasks using a framework that generalizes in a combinatorial way, meaning they construct states as latent vectors, each constructed themselves from fixed elements. Such vectors lend themselves to generalization to differently sized sets. The authors argue that RL models are inherently ill suited to deal with such a framework, whereas diffusion models are inherently better suited for such a task. They demonstrate their claims through a series of experiments on RL environments.

### Strengths
- Combinatorial complexity is a problem that seems often overlooked in machine learning topics. I am happy to see the authors address the subject.
- I think the understanding of why diffusion models seem to generalize better is of great importance to the progress of many fields.

### Weaknesses
While the paper addresses an important and timely topic, I have some questions and concerns about the technical content of the paper. 
- The authors argue that a state can be composed of base elements, and attributes to those base elements. While they do not explicitly specify what constitutes those base elements beyond "car" and "bike", they do mention that there are also attributes, which are not relevant to the state as it pertains to the decission making, but only to the rendering function. I disagree with that statement. Certainly the velocity of a car would be important to ones decission making. It is not clear where "position" falls in this framework. Both these variables are important to the state, and would thereby invalidate the authors assumption in most realistic scenarios, since the "finite base set" requirement can not be satisfied.
- Central to the authors claims seems to be that the sampled diffusion variables can be represented by a combinatorial set of finite elements. However, the approach in Janner et al. uses diffusion for to sample future states and actions, conditioned upon the current state. In this case, the combinatorial state is not sampled, but rather it is an input to the model.
- I fail to see why the states defined by Z lie on a manifold. While there is indeed some prior work about manifolds in the dataspace, this specifically concerns an assumption for images. The dataspace that the authors present does not to fall into that category. In particular, lines 304 to 309 say that because there is a countable number of elements, their data lies on a manifold. If I understand the setup correctly, Z is a cartesian product of the base set E. This would not constitute a manifold. The manifold assumption seems like a central assumption to the paper, but it is not defended. It also seems that Z has a varying dimension, which seems incompatible with the assumption they lie on a manifold. As a matter of fact it is unclear even if n is varying in the setup. The abstract and title seem to suggest that, but I do not see any information in the paper (one way or another) on whether it varies or not.
- In the absence of strong theoretical results, I would hope to see very compelling experimental results, but strong experimental results are lacking. PPO, the most competitive of the baseline methods, seems to have been trained with 100x less parameters than the diffusion models. 

Minor points that would be good to address:
- An "ODE" trajectory as the authors use in their proof precludes noise, as the authors use later on. This would be an SDE trajecotry.
- In the proof sigma_t is not specified
- In the corollary it is not clear what the purpose of s is. It does not seem needed for the argument that is made in there. The symbol is used in the proof, but it seems unrelated to the statement in the corollary.

### Questions
- I would hope the authors could addreess and clarify all the points brought up under weaknesses. Of particular importance are: can they clarify the setup (does n vary or not)? Can they give a more rigorous defense on why cartesian products of sets lie on a manifold?
- In the proof, it seems like the bottom line is, diffusion models put mass everywhere, therefore they generalize better. This is not at all a unique property to diffusion models, does this mean the authors' proof holds for other probabilistic models with that property too?
- The authors themselves point out in the proof under appendix B that non-zero probability does not prevent poor behavior, and propose to use data augmentation during training. Is there a reason that this data augmentation would not suffer from the same problems the authors point out in the case of RL?

### Soundness
1

### Presentation
3

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
This paper describes the zero-shot generalization problem in reinforcement learning for novel states using the combinatorial property of states, introducing the concept of out-of-combination (OOC) generalization. Based on this formulation, it explains why traditional RL methods tend to fail in such scenarios and proposes that diffusion models can effectively sample OOC states, enhancing zero-shot generalization in OOC cases.

### Strengths
1. This paper proposes a novel perspective in introducing the diffusion model as a planner for RL, leveraging its combinatorial genearalization capabilities. It proposes the concept of combinatorial states to illustrate the effectiveness of the diffusion model planner in this specific scenario.
2. The authors conduct experiments in several environments and test the effects of different conditioning on the diffusion model. And the formulaiton of the experiment is quite easy to follow.

### Weaknesses
1. Presentation. (1) The paper’s organization is overly segmented, creating a somewhat confusing structure. For instance, Section 4 contains only one subsection (4.1), which could be merged with Section 5, as Section 4 is fairly brief. Additionally, the introduction to diffusion models would be more appropriately placed in the “Preliminaries” rather than within the methodology description. The main methodology appears to be in Section 6, yet it occupies only a single paragraph, offering minimal explanation of the approach. (2) The content is not properly distributed. In the related work section, too many subcategories dilute the focus. This section should concentrate on three main categories that are closely related to this work: state generalization, state decomposition, and diffusion models for RL generalization. Other less related studies could be briefly summarized. Notably, the role of diffusion models in decision-making, a central theme of this paper, lacks sufficient discussion both in the related work and in the main content. I recommend the authors consider these points to improve the manuscript’s readability.

2. Technical Contribution. (1) While this paper emphasizes the combinatorial property of states in RL, it lacks explanation on how to determine the basic elements for each environment and how to extract the compositional information behind the observation, which is important for readers to understand the combinatorial property. The paper does not provide a clear methodology for identifying these base elements, making it difficult to assess the general applicability of the approach. (2) The paper does not effectively convey the importance of its setting, nor does it fully address the first question posed in the experimental section, "Does the state space of different existing RL environments exhibit a compositional nature?" The notion of "wide applicability" for this setting needs clearer articulation. For example, beyond the environments discussed in the experiment section, if the observation is a 2D image, can this approach still reliably identify the fundamental elements? In a game like *CoinRun*, where level differences lie in map layouts, how would one define the basic elements across varied terrains? (3) The paper mentions the point that "other work addresses only the situation where states have the same support but different probability density", I would ask the authors to provide more evidence supporting this claim. This claim is not adequately supported and requires further justification, as many existing works address distribution shifts beyond simple density changes.

### Questions
* While this may extend beyond the scope of the paper, I would still like to discuss with the authors: if novel states are introduced during testing, the environment dynamics are likely to vary as well. Would your method remain applicable under these varying dynamics?
*  In Algorithm 1, it appears that after the diffusion model generates an action, the state transition is carries out by the environment simulator. Given this, why does the trajectory produced by the unconditional diffusion model violate the maze constraints, as shown in Figure 7(c)? My understanding is that the state transition constraints should be enforced by the environment simulator.
* Regarding the conditioning of the diffusion model, how is an appropriate conditioning determined for a specific environment? For instance, in Figure 7(d), the prior with 3 waypoints appears too strong, as these waypoints essentially outline the optimal path.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of out-of-combination  (OOC) generalization in RL. The authors first define OOC generalization mathematically and show that classical behavioral cloning methods struggle when tested on OOC examples. They then propose a Diffusion model to better tackle OOC generalization, and show that implementing the policy through a Diffusion model conditioned on ground truth information about the environment's objects/entities improves generalization in three environments.

### Strengths
* Clearly defines an interesting problem and identifies a possible solution.
* Exposition is easy to follow and conceptually simple
* Proposed method yields considerable improvements in several environments
* Good ablations to show what parts of the diffusion approach are important.

### Weaknesses
While the proposed approach gives important performance improvements in these OOC domains, two potential weaknesses come to mind:
* The diffusion model requires ground-truth information about the entities/object types that compose the environment's state space to work effectively. This type of information is not always available, and it can be a considerable challenge to learn such representations in an unsupervised manner. Is it possible to show how important having reliable information about the compositional latent variable is in, for instance, the Roundabout environment? 
* A second concern is the complexity and run-time of the algorithm. In the SMACv2 5v5 environment the Diffusion model has a ~10x longer train time than PPO. Maybe there are methods that lie in-between in terms of complexity, and potentially also performance. Are there ways in which the diffusion model could be sped up for faster training?

Some minor comments:
* In the Roundabout environment, it would be interesting to compare the model to an off-policy algorithm that collects its own training data, like SAC. 
* Limitations can be discussed more extensively. For example, the definition of OOC generalization/support supposes a well-defined set of entities (e.g. cars and bikes). In the real world, object type distinctions are not always clear. Should motorized bikes count as a bike with slightly different dynamics or as a whole new entity? Not a major concern, but could be good to discuss these types of limitations.

### Questions
* Not sure why corollary 5.1 adds to the exposition? I think simply stating that Diffusion models have been successful at combinatorial generalization in the past is sufficient for motivating this.

### Soundness
3

### Presentation
3

### Contribution
3
