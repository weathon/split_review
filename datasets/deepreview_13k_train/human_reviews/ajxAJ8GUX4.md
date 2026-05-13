# Learning Geometric Reasoning Networks For Robot Task And Motion Planning

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Task and Motion Planning (TAMP) is a computationally challenging robotics problem due to the tight coupling of discrete symbolic planning and continuous geometric planning of robot motions. In particular, planning manipulation tasks in complex 3D environments leads to a large number of costly geometric planner queries to verify the feasibility of considered actions and plan their motions. To address this issue, we propose Geometric Reasoning Networks (GRN), a graph neural network (GNN)-based model for action and grasp feasibility prediction, designed to significantly reduce the dependency on the geometric planner. Moreover, we introduce two key interpretability mechanisms: inverse kinematics (IK) feasibility prediction and grasp obstruction (GO) estimation. These modules not only improve feasibility predictions accuracy, but also explain why certain actions or grasps are infeasible, thus allowing a more efficient search for a feasible solution. Through extensive experimental results, we show that our model outperforms state-of-the-art methods, while maintaining generalizability to more complex environments, diverse object shapes, multi-robot settings, and real-world robots.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Geometric Reasoning Networks (GRN), a graph neural network-based approach to enhance efficiency in Task and Motion Planning (TAMP) for robotic manipulation. An incremental GNN-based model is introduced with two mechanisms: inverse kinematics (IK) feasibility prediction, and grasp obstruction (GO) estimation using full-state knowledge. Experimental validation demonstrates GRN's applicability to various environments and configurations.

### Strengths
- The study tackles a significant challenge in TAMP arising from the bottleneck in geometric planning within complex 3D environments and proposes a novel, though incremental, architecture to predict action and grasp feasibility to reduce the need for costly geometric planning queries.  

- The model is more generalizable in complex environments compared to prior works (Table 4).

- The proposed model is evaluated and compared against prior works and an ablation study is conducted.

- The authors conducted real-robot experiments, and shared their code.

### Weaknesses
Below is the list of the issues I observed, and my suggestions for this work:

1.  **Strong Assumptions on Object Knowledge and Static Scene Conditions**: The model assumes complete knowledge of object shape, dimensions, and pose, as well as static conditions where objects remain stationary unless moved by the robot (lines 153–154). This is a considerable simplification for real-world scenarios, where partial observability and dynamic conditions are typical. By contrast, some baselines used for comparison assume partial observability and predict feasibility based on images rather than full state knowledge, making these comparisons less directly fair. Addressing this by either relaxing these assumptions or comparing only with baselines under similar assumptions would improve applicability and fairness.

2.  **Limited Integration and Short Planning Horizons**: While some baselines are fully integrated within TAMP solvers, GRN’s integration is relatively basic and tested only on shorter-horizon problems. The scenarios addressed in the experiments are limited in complexity, lacking tasks that demand multi-step, long-horizon planning (e.g., removal of obstructing objects or inter-robot handovers). Expanding the evaluation to more complex, long-horizon planning tasks would better demonstrate GRN's practical utility in handling realistic TAMP challenges.

3.  **Improvement for TAMP**: Since the paper do not include a full-fledge TAMP solver, it remains unclear how it improves traditional/existing solvers. It'd have been really useful to see how many geometrical computations were skipped (so computational time was gained) when GRN was used vs. not used. Inference time comparison to some of the baselines is not fair, as they use image-based input while this work relies on a significantly smaller full-state information of the environment.

4.  **Incremental Advancement and Limited Impact of IK Infeasibility Module**: While GRN introduces small adjustments on Edge-Featured Graph Attention Network (EGAT), these additions are incremental and rely heavily on prior EGAT methods. Furthermore, as shown in Table 3, the IK infeasibility module does not significantly impact overall performance. Adding a deeper analysis or improvement in these areas could strengthen the contribution. It seems like GO by itself is already a good estimator of feasibility. This could also be due to problem settings where there might not be (enough) cases when there is no grasp obstruction IK was still infeasible (e.g., due to reachability). A more nuanced analysis of scenarios where IK feasibility alone might be crucial (e.g., environments with tighter spaces or more complex robot configurations) that would help clarify when this module provides substantial benefits.

5.  **Restricted Grasp Representation**: The model simplifies grasp feasibility by considering only five grasp types, which may limit its effectiveness in real-world settings where grasp variety and adaptability are crucial. Even for grasping box-shaped objects requires 24 (or 20 if it lies flat on a surface) different configurations with a parallel jaw gripper, much higher than 5 as used in this work. Exploring a more flexible grasp representation that could handle diverse object shapes and placements would make the model more versatile for practical robotics applications.

6.  **Limited Interpretability Support**: While the authors claim that GRN allows interpretation of feasibility (or infeasibility) of actions, this claim lacks follow-up discussion or specific experimental support. Including experiments or qualitative analysis to illustrate interpretability (e.g., showing how grasp obstruction information directly affects planning decisions) would make this feature more convincing and actionable.

7.  **Clarity and Organization of Paper Structure**: The organization could be improved for readability and logical flow. For example, Figure 2 is never referenced in the text, and Figure 1, which appears on page 3, is not mentioned until Section 6.4 on page 10. Figures in the Appendix (e.g., Figures 7 and 8) are not referenced or explained, leaving the reader without context for understanding their relevance.

### Questions
I've listed my main concerns under _weaknesses_ section, and here are some further questions (some overlapping with the points above):

- **Self-loop Edge Representation in 4.1**: What is the rationale for using the self-loop edge to store IK feasibility instead of treating it as a node feature? How does this choice affect the overall model performance or its ability to generalize to unseen environments?

- **Effectiveness and Necessity of the IK Module**: In the ablation study (Table 3), the results show minimal difference between the full model and the one without the IK module. Given this, is the IK module truly necessary? What are the specific cases where IK adds value? Also, could you provide the inference time for the IK module to understand its overhead?

- **Access Task Success Rate in Section 6.4**: The success rate for the Access task in Table 5 is slightly lower than Bouhsain et al. (2024). What are the main reasons for this reduction? Are there particular scenarios where GRN struggles, or is this a result of experimental variance?

- **Inference Time in Table 5**: Could you provide more detailed inference times for Table 5, including how the times break down between GRN predictions and geometric planning? Understanding the computational cost of each component would provide a clearer picture of where time savings are realized.

- **Handling Dynamic Scenes**: The current assumptions restrict the model to static scenes, which is not always practical in real-world tasks. How would this approach be extended to handle dynamic environments?
  
- **Real-world Evaluation of Long-horizon Tasks**: The paper would benefit from showing how GRN scales to more challenging multi-step tasks, such as multi-robot collaboration or handling non-prehensile manipulation. Can the authors comment on future steps for validating GRN on these scenarios?

- **Simplified Grasp Types**: The use of only five grasp types is limiting. Are there plans to extend the grasp representation, or can the authors justify why five types were sufficient for the tasks tested in this paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a graph neural network model for efficient Task and Motion Planning (TAMP). It uses a scene graph to represent 3D environments, incorporating Inverse Kinematics (IK) and Grasp Obstruction (GO) modules. Experiments show its superiority over state-of-the-art methods in accuracy, generalization, and speed. It reduces the reliance on computationally expensive geometric planners while remaining robust across diverse robots and complex scenes.

### Strengths
1. It incorporates explainable modules within the GNN, such as inverse kinematics and grasp obstruction estimations, to predict feasibility. This interpretability enhances decision-making by providing insights into why certain actions are infeasible.

2. Experiments demonstrate that GRN significantly lowers computational costs compared to traditional geometric planners, making it a more efficient solution for real-time TAMP applications.

### Weaknesses
1. The method's reliance on simplified bounding box representations and discrete grasp feasibility may limit its effectiveness in real-world TAMP problems, especially in dynamic, cluttered environments with irregular objects or sensor noise. The use of bounding boxes, while computationally efficient, may not accurately capture the complex geometries of many real-world objects, leading to inaccurate feasibility predictions. Furthermore, the discretization of grasp feasibility into binary outcomes (feasible/infeasible) neglects the nuanced nature of grasps, where a continuous spectrum of feasibility exists, potentially overlooking near-optimal grasps that are not strictly classified as feasible. This simplification could lead to suboptimal planning outcomes, particularly in scenarios requiring fine manipulation.

2. The method only assesses discrete feasibility without motion planning, restricting its ability to handle complex cases where motion feasibility [1] is crucial. By focusing solely on the feasibility of the final grasp configuration, the method ignores the path required to reach that configuration. This is a significant limitation, as many seemingly feasible grasps may be unreachable due to kinematic constraints or collisions along the robot's trajectory. The absence of motion planning considerations makes the method unsuitable for scenarios where the robot's path is non-trivial, such as navigating through narrow passages or around obstacles, which are common in real-world manipulation tasks.

### Questions
1. How would the performance of GRN be affected if the Inverse Kinematics (IK) and Grasp Obstruction (GO) modules were replaced with traditional methods, such as standard inverse kinematics solvers or simpler distance-based obstruction checks? Specifically, how would this change impact prediction accuracy, interpretability, and computational efficiency in various environments?

2. What is the maximum level of environmental complexity that GRN can handle effectively? For example, how many fixed nodes or objects can it support while maintaining accuracy and efficiency? Could GRN scale to environments with thousands of nodes, akin to point cloud representations, and still perform well in highly cluttered scenes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Geometric Reasoning Networks (GRN), a GNN model for predicting action and grasp feasibility. Technical Innovations of the paper includes:
- Novel scene representation using directed graphs
- Edge-Enhanced Graph Attention Network (EGAT) that leverages both node and edge features
- Ability to explain why actions are infeasible, enabling more efficient planning

### Strengths
1. Outperforms state-of-the-art methods in both action and grasp feasibility prediction
2. Lower inference time compared to traditional geometric planning
3. Generalization to more complex environments and different robot types
4. Writing is very clear and detailed

### Weaknesses
1. Some details for the experiment setting needed to be discussed further to correctly evaluate the approach. See the questions.

1a. How imbalanced is the dataset? Is it nearly composed of 50% feasible cases and 50% infeasible cases? It would be appreciated if some ratio of the dataset could be shared as a table.

1b. Since RRT is a random algorithm, I think it doesn't necessarily mean one task is truly infeasible, if RRT couldn't generate a plan. What is the definition of the feasibility in this paper's scope?

2. Regarding training, why is pre-trained needed before jointly fine-tuning? Was there any training instability if we directly train all the modules?

3. The generalization experiment is interesting. What I'm expecting is that the graph representation should be powerful enough to achieve a significantly better generalization. However, it seems that the MLP method is also good enough to generalize to 20 obstacles. Is there any specific reason why this is the case? Or are we also facing the imbalanced dataset issue here? Sampling a feasible case for 20 obstacles sounds challenging, right?

4. I am not very familiar with TAMP problem. Just as a discussion, in general, when would a learning-based feasibility checker be preferred compared to a learning-based end-to-end planner, that directly generates a plan? And when vice versa?

### Questions
1a. How imbalanced is the dataset? Is it nearly composed of 50% feasible cases and 50% infeasible cases? It would be appreciated if some ratio of the dataset could be shared as a table.

1b. Since RRT is a random algorithm, I think it doesn't necessarily mean one task is truly infeasible, if RRT couldn't generate a plan. What is the definition of the feasibility in this paper's scope?

2. Regarding training, why is pre-trained needed before jointly fine-tuning? Was there any training instability if we directly train all the modules?

3. The generalization experiment is interesting. What I'm expecting is that the graph representation should be powerful enough to achieve a significantly better generalization. However, it seems that the MLP method is also good enough to generalize to 20 obstacles. Is there any specific reason why this is the case? Or are we also facing the imbalanced dataset issue here? Sampling a feasible case for 20 obstacles sounds challenging, right?

4. I am not very familiar with TAMP problem. Just as a discussion, in general, when would a learning-based feasibility checker be preferred compared to a learning-based end-to-end planner, that directly generates a plan? And when vice versa?

### Soundness
3

### Presentation
3

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
This paper proposes to use GNN-based methods to predict action and grasp feasibility, which can speed up the geometric planner in task and motion planning. Furthermore, the authors propose to predict the inverse kinematics feasibility and grasp obstruction to improve the interpretability. Through quantitative and qualitative experiments, the authors verify the effectiveness of the proposed approach.

### Strengths
1: This paper is well-motivated. The efficiency of task and motion planning is a significant issue and how to improve it is an important research question. 

2: Predicting geometric dependencies and feasibility with a graph neural network makes sense to me. 

3: This paper contains an extensive experiments section and compares the method to several baselines, which is nice. 

4: The paper shows some real-world demos.

### Weaknesses
1: My first concern is the limited discussion and comparison to related works in geometric feasibility reasoning [1, 2, 3] and graph neural networks in task and motion planning [4, 5, 6]. In particular, [2] also uses feasibility-related predicates to improve the efficiency of the task planning.

[1]: K. Lin, C. Agia, T. Migimatsu, M. Pavone, and J. Bohg. Text2motion: From natural language instructions to feasible plans. Autonomous Robots, 47(8):1345–1365, 2023.

[2]: Y. Huang, C. Agia, J. Wu, T. Hermans, and J. Bohg. Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics, ArXiv, 2024. 

[3]: C. Agia, T. Migimatsu, J. Wu, and J. Bohg. Stap: Sequencing task-agnostic policies. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages 7951–7958. IEEE, 2023.

[4]: Planning for Multi-Object Manipulation with Graph Neural Network Relational Classifiers. In IEEE International Conference on Robotics and Automation (ICRA), 2023.

[5]: H. Shi, H. Xu, Z. Huang, Y. Li, and J. Wu. Robocraft: Learning to see, simulate, and shape elastoplastic objects in 3d with graph networks. The International Journal of Robotics Research. 

[6]: H. Chen, Y. Niu, K. Hong, S. Liu, Y. Wang, Y. Li, and K. R. Driggs-Campbell, “Predicting object interactions with behavior primitives: An application in stowing tasks,” in 7th Annual Conference on Robot Learning, 2023.

2: The videos and figures for this paper are hard to follow. For example, in Figure 1, I can only understand green represents feasible and red represents feasible. However, there are other colored objects like blue ones. Furthermore, why robots are sometimes grey and sometimes red?  

3: This paper makes several strong assumptions including known object shapes and poses, and all objects remain static except the robot grasps them.

### Questions
1: how would your proposed approach compare to related works in geometric feasibility reasoning [1, 2, 3] and graph neural networks in task and motion planning [4, 5, 6]? 

2: Is there any noise when you estimate the object's shape and pose in the real world? If there is noise, would your proposed approach be robust to the noise? 

3: Could you train one more for all robots? Training one model for each robot limits the generalization ability of your proposed system.  

4: For the Panda-3D-4 dataset, the MLP achieves a 0.558 F1 score but the Panda-3D-20 achieves a 0.609 F1 score, why does MLP perform better in a more complex dataset? This is weird. 

5: In Table 5, why does your proposed approach perform worse than the baseline in the “Access” problem? Why does the baseline always achieve a 100% success rate? I guess your task is too easy.

### Soundness
3

### Presentation
2

### Contribution
3
