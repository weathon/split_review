# Dynamic Contrastive Skill Learning with State-Transition Based Skill Clustering and Dynamic Length Adjustment

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Reinforcement learning (RL) has made significant progress in various domains, but scaling it to long-horizon tasks with complex decision-making remains challenging. Skill learning attempts to address this by abstracting actions into higher-level behaviors. However, current approaches often fail to recognize semantically similar behaviors as the same skill and use fixed skill lengths, limiting flexibility and generalization. To address this, we propose Dynamic Contrastive Skill Learning (DCSL), a novel framework that redefines skill representation and learning. DCSL introduces three key ideas: state-transition based skill definition, skill similarity function learning, and dynamic skill length adjustment. By focusing on state transitions and leveraging contrastive learning, DCSL effectively captures the semantic context of behaviors and adapts skill lengths to match the appropriate temporal extent of behaviors. Our approach enables more flexible and adaptive skill extraction, particularly in complex or noisy datasets, and demonstrates competitive performance compared to existing methods in task completion and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Use discriminability to identify skills, then use a skill similarity function trained using contrastive learning with a state-skill embedding and a state embedding. The representation is then used as an input to the termination condition, which compares the current autoencoded state to the skill embedding. The model is then trained as a joint objective. Compute skill duration as the maximum number of steps where the skill similarity is greater than a threshold value.

### Strengths
Investigates some of the core questions in skill learning, including variable-length skills and skill differentiability.

Offline skill learning is an increasingly appplicable field, especially as large robotics datasets become more prevalent

Provides a mostly clear and understandable description of a complex method and motivation for each algorithmic choice.

### Weaknesses
Of the original claims made in the introduction, there is a disconnect between those and the empricial results. In particular, while it is clear that the skills appear to be more effective for downstream tasks the original claims do not appear to be verified. It is not as obvious that the skills capture ``more semantic context'', as the only experiment in this context is antmaze (Figure 6), and while this appears to show some separation, it is not particularly semantic. It would be more useful to provide some clearly semantic task transfer, such as opening multiple different drawers in franka kitchen with the same skill. Similarly, it is not clear the how the skill lengths are used for performance, in particular the effect of skill length relabeling appears to be marginally significant. It would be valuable to have some analysis indicating that for some tasks shorter/longer skills are assigned appropriately. Finally, it is not actually that obvious why this method takes advantage of the offline RL setting and could not be directly applied to unsupervised skill learning.

The method itself is straightforward, but there are a substantial number of models that must be trained together (two encoders in the similarity measure, and encoder-decoder in the state encoder, target state model, skill prior, policy). Training these together appears to have been done using a few objectives without any hyperparameters. In practice, combining these kinds of models often requires some kind of tuning, which seems like it would be a limitation. How is this done in practice for this method?

In the formulation of the skill embeddings, two randomly sampled intermediate states are used to identify the skill embedding. This seems like it could introduce a significant amount of variance. Also, it is not clear how that number of intermediate states is decided. A more careful analysis of this design choice seems appropriate (is this something used by related work? How does a different number of intermediate states compare? What are the theoretical ramifications of such a choice?) and is missing from the paper. 
The level of comparison is a little bit limited. In particular, this method seems at least peripherially related to unsupervised skill learning work, so it seems appropriate to make at least some comparison to that work. I expect that without access to the advantage of offline data those methods would not perform particularly well, but in a domain like antmaze, they may exihibit better skill differentiation. 

As mentioned before, a more in-depth analysis of skill length would be valuable in this work. Even in the domains where additional skill length showed performance benefit, it is not obvious why it would, since these are pick and place tasks. Some kind of analysis which indicated how much time was wasted without skill length relabeling would probably be demonstrative.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes DCSL - a method for learning skills based on state sequences from offline data, using a contrastive loss. A similarity function is parameterized by a neural network and learned, which is then used to cluster similar skills together. In addition, the approach also allows for flexible learning skills of various durations by relabelling the duration of each skill based on the same similarity function. The results show better performance on downstream tasks when these skills are used with a model-based or model-free high-level controller.

### Strengths
- Skills are more general and less overfitting to specific types of behaviors due to the similarity function.
- Dynamic relabelling allows for skills for different lengths and the paper shows cases where that's beneficial.
- Significantly better performance than baselines on downstream tasks.
- Seems more robust than baselines to lower quality demonstrations in the dataset as shown by the PP ME dataset.

### Weaknesses
 - Comparisons are only done with variations of two methods (SPiRL and SkiMo), which makes it harder to judge the strength of the method.
- Since the method uses Behavior cloning to learn the skills, I’m not sure how well it will perform in datasets with large amounts of sub-optimal data. While the results show that it outperforms BC-based baselines, there’s no comparison with non-BC methods like offline RL.
- Qualitative comparisons (videos) of the behaviors would be appreciated.


### Questions
## Questions
1. The second contribution mentions that the similarity function “clusters semantically similar behaviors into the same skill category.” Just to clarify, is “skill category” used loosely here? As I understand the skills are continuous N dimensional vectors and similar behaviors (in terms of state sequences) will be encoded to similar skills, but there are no discrete groups or categories of skills?


2. Are semantically similar skills close to each other in Z space? For example in Fig. 6c), would behaviors moving in more or less the same direction have similar skill value?


3. The skill prior is used for both the embedding loss and to guide exploration for downstream tasks. How is this skill prior learned (as mentioned in line 687)?


4. Have you done any ablation on the number of key states - is there a specific reason for choosing 4?


5. It is a bit unclear to me how key states are sampled and associated with skills. Each trajectory tau_I contains T state-action pairs. 
Does each trajectory have one or several skills associated with it? From line 4 on Algorithm 1 it seems that each trajectory has one skill associated with it and the skill duration H for each trajectory then changes based on the relabelling (Algorithm 2)? What if a single trajectory contains multiple behaviors? 

6. How does this method compare to works like OPAL [1] or to using unsupervised skill discovery with offline RL to learn skills from a dataset  [2], [3]? If possible, a comparison could strengthen the contributions.

## Review summary:
Overall I think this is a high quality work and the proposed method is promising. The paper is well-written and easy to follow (with a couple of caveats mentioned above). The main concern is that I think more comparisons should be made with other relevant methods which learn skills from offline datasets with or without behavior cloning.

References:

[1]	A. Ajay, A. Kumar, P. Agrawal, S. Levine, and O. Nachum, “OPAL: Offline Primitive Discovery for Accelerating Offline Reinforcement Learning,” May 04, 2021, arXiv: arXiv:2010.13611.

[2]	S. Park, T. Kreiman, and S. Levine, “Foundation Policies with Hilbert Representations,” presented at the Forty-first International Conference on Machine Learning, Jun. 2024.

[3]	J. Kim, S. Park, and S. Levine, “Unsupervised-to-Online Reinforcement Learning,” Aug. 27, 2024, arXiv: arXiv:2408.14785. doi: 10.48550/arXiv.2408.14785.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates skill learning in reinforcement learning (RL) and proposes Dynamic Contrastive Skill Learning (DCSL), a method to learn skill embeddings based on state transitions. The approach uses contrastive learning to cluster semantically similar skills and dynamically adjusts skill length during the learning process. Experiments are conducted on Ant-Maze, D4RL Kitchen, and Meta-World Pick-and-Place environments, demonstrating that DCSL, combined with the downstream RL algorithm SAC, outperforms previous skill learning methods.

### Strengths
* The approach is well-motivated, addressing important challenges in capturing semantically similar skills and adapting skill lengths across different tasks.  
* The experiments across multiple benchmarks and tasks provide strong empirical support for the benefits of DCSL over baseline methods.

### Weaknesses
 * The experimental and ablative studies could be more comprehensive, covering a broader range of tasks and datasets within D4RL and Meta-World.  
* The paper’s writing could be clearer and more accessible (see clarification questions below).  
* While the paper offers some theoretical insights in Appendix A, DCSL lacks a rigorous theoretical foundation with formal mathematical derivations and analysis.  
* The paper does not discuss its limitations, which is essential for understanding the boundaries of its applicability.

### Questions
1. **Performance of SPiRL in Figure 4(c)**: The performance of the SPiRL baseline appears significantly worse than reported in the original SPiRL paper on D4RL Kitchen tasks. Could this discrepancy be due to differences in the datasets used in D4RL Kitchen environments?  
2. **Definition of training steps (Figure 4\)**: In Figure 4, the x-axis refers to the number of training steps, but RL research typically focuses on environment steps to measure sample efficiency. Could you clarify the meaning of "training steps" in this context? Additionally, would it be possible to provide a comparison of different methods based on sample efficiency?  
3. **Additional datasets in D4RL Kitchen**: The experiments in the D4RL Kitchen environment are conducted using only the mixed dataset, but this benchmark includes two additional datasets. Could you extend the comparisons to these datasets? Will DCSL maintain its advantage across different datasets?  
4. **Meta-World experiments**: While DCSL performs well on the pick-and-place task in Meta-World, could you test it on more challenging tasks within Meta-World to fully validate its robustness and generalization?  
5. **Ablation without similarity function**: In the ablation study, could you include a variant of DCSL that omits the similarity function? This would result in a method that relies purely on state-transition-based skill learning. How would this variant compare to SPiRL, which is action-based skill learning?  
6. **Skill target state in continuous space (Line 262\)**: The sentence mentions that a skill target state is considered "reached" during downstream execution, but how do you determine whether a target state is reached in continuous state spaces? Is there a threshold used to make this determination?  
7. **Definition of skill trajectory (Line 248\)**: The sentence refers to the "trajectory of skill z." Could you provide a formal definition of what constitutes the trajectory of a given skill?  
8. **Negative sampling in contrastive learning (Equation 5\)**: In Equation 5, how is z′≠z determined, given that z lies in a continuous space? For any trajectory other than the anchor trajectory, the skill embedding z’ will always differ from z, so does this mean any state from other trajectories would serve as a negative sample?  
9. **Sensitivity to similarity threshold ϵ\\epsilonϵ (Equation 9\)**: How sensitive is DCSL’s performance to the value of the hyperparameter \\epsilon in Equation 9? A sensitivity analysis would be useful to understand the robustness of the method.  
10. **Sparse reward problem (Line 369\)**: The paper claims that DCSL addresses the sparse reward problem better, but there is no detailed explanation of the sparse reward issue in the Ant-Maze environments. Moreover, conducting experiments on more tasks with sparse rewards would strengthen this claim.  
11. **Generalization to unseen tasks**: Can the skills learned during training be transferred to unseen tasks that are relevant to the training tasks? For example, SPiRL demonstrated generalization by applying learned skills to more complex mazes. Does DCSL exhibit similar generalization capabilities?

### Soundness
2

### Presentation
2

### Contribution
2
