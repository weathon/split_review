# Physics-informed Temporal Difference Metric Learning for Robot Motion Planning

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 5, 8, 8

## Abstract
The motion planning problem involves finding a collision-free path from a robot's starting to its target configuration. Recently, self-supervised learning methods have emerged to tackle motion planning problems without requiring expensive expert demonstrations. They solve the Eikonal equation for training neural networks and lead to efficient solutions. However, these methods struggle in complex environments because they fail to maintain key properties of the Eikonal equation, such as optimal value functions and geodesic distances. To overcome these limitations, we propose a novel self-supervised temporal difference metric learning approach that solves the Eikonal equation more accurately and enhances performance in solving complex and unseen planning tasks. Our method enforces Bellman's principle of optimality over finite regions, using temporal difference learning to avoid spurious local minima while incorporating metric learning to preserve the Eikonal equation's essential geodesic properties. We demonstrate that our approach significantly outperforms existing self-supervised learning methods in handling complex environments and generalizing to unseen environments, with robot configurations ranging from 2 to 12 degrees of freedom (DOF).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new method to allow robots to use self-supervised learning to learn motion planners and use MPC for online path generation.

The proposed method is built on NTFields (Ni & Qureshi, 2023a), and proposes two improvements:
1. Novel loss
    1. View the self-supervised learning problem in NTFields as a solution to an optimal control problem, propose a discrete-time loss L_TD based on temporal difference learning in RL, and combine L_TD with NTFields's continuous-time loss L_E to capture both a coarse-grained view of value propagation and a fine-grained optimal physics structure.
    2. Another loss term L_N to avoid collision.
    3. Another loss term L_C to ensure causality (i.e., time only moves forward) based on (Wang et al., 2024b).
2. Metric learning: during NTFields's training, the structure of the learned travel-time function might violate triangle inequality, becoming no longer a geodesic distance on a Riemannian manifold. This paper proposes a neural network structure that preserves the key properties of such a metric.
3. Allow generalization to the new environments by conditioning the learning on the environment via the attention mechanism.
4. Use online MPC for path generation.

### Strengths
- The problem is well-motivated.
- Very clear discussion about related works, including traditional motion planning methods, learning from experts, and self-supervised learning.
- (Strength and also some weakness) I think the first improvement, using both continuous loss L_E from previous work and a novel TD loss is interesting. There is some discussion about the benefits of combining fine-grained and coarse-grained structures. The authors also used an example (Fig.1) to show that sometimes, only ensuring a low L_E does not imply good behavior. However, I don't quite get why L_E is 0 in both cases and why L_TD is high in the 2nd case. It would be great if the authors could provide more explanation about Fig.1. I think this could make the contribution more significant.
- The result is very comprehensive, with simulation and real-world benchmarks, and compared against many baseline methods.

### Weaknesses
 - I think the key weakness is that even though the various novel techniques improve NTFields, the empirical result does not seem to convey that impact. For example, in the ablation study (Fig.2 row 2), the errors discussed in line 403 convey that L_E, which was proposed in NTFields, is the most important component, and the other loss terms only provide small improvements (e.g., from 0.21 to 0.08 error). This makes me worry a bit about the effectiveness of the proposed techniques. In the real world, the proposed techniques increase the system's complexity, so it would be great if they provide a very strong performance boost to motivate people to adopt them. It would be great if the authors could discuss the importance of the proposed techniques, perhaps explaining how to interpret these results or using some other qualitative results to demonstrate.
    - Related to this, it seems that one major improvement of the proposed method compared to previous work in Tab.1 is faster plan generation, e.g., from 0.5 sec to 0.07 sec. I think it would be great if the authors could discuss the implications of why this could matter in the real world. Perhaps one way to show that this is significant is to consider scenarios where the robot has to keep replanning to adapt to dynamic obstacles.

- I think this paper did a good job introducing the technical key points about the previous work NTFields (Ni & Qureshi, 2023a) in Sec.3.2. However, I think it lacks some high-level description of how NTFields works as a motion planner. As a result, as a person outside this field of self-supervised motion planning, I found Sec.3.2 a bit hard to follow. For example, here are some points where I got confused:
    - It seems that S*(q) is a function that is manually defined that outputs the desired robot velocity when the robot is around obstacles.
    - Eq.3 seems to propose training the function S such that it matches S* at starting and goal configurations. Then, a perhaps naive question is why to learn S rather than just using S* as the motion planner?
    - How is the learned S used to generate motion plans during online inference time? Line 352 mentions that some previous methods do gradient descent to minimize T(qs,qg). So, I guess it is looking for some path that minimizes the time from qs to qg? It would be great to put this information earlier in Sec.3.2.
- Similar to the previous point, I think more intuition can help Sec.4.2.
    - I think the motivation for metric learning in Sec.4.2 is not so clear to me. I notice that the authors briefly mentioned the potential benefit of metric learning in line 114 by saying, "scale and generalize effectively in complex, cluttered, or unseen environments." But it is not so intuitive. Would there be some intuitive example, such as Fig.2, that can illustrate why metric learning is important?
    - Eq.10 seems to be the key contribution. However, the discussion around it from lines 304 to 313 is very abstract. It would be great if the authors could provide some high-level intuition about why L_inf distance is preferred to Euclidean distance.
- The contribution of Sec.4.3 - online MPC is interesting. It seems that the key benefit of this is faster online inference compared to (Ni et al., 2021; Ni & Qureshi, 2023b). However, the empirical results in Tab.1(a) show that the proposed method's computation time is 0.056 while NTF (Ni et al., 2021) is 0.074, with a small difference. Could the authors discuss the potential implications of why this difference could matter in the real world and how it will strengthen the contribution?
- Fig.2 is a key result. However, for people outside the field, it is unclear how to interpret it. It would be great to add some guidance.


### Questions
- Sec.2 discusses the relationship between RL and self-supervised learning using physics-informed neural networks. I wonder about the difference between them. Can I think of a self-supervised learning type of approach as doing offline RL but with specially designed network architecture? The reason why I ask this question is that I think Sec.3.1 and 3.2 could have some introduction about how self-supervised learning motion planners are trained. I think this could be very helpful for people who are not familiar with NTFields (Ni & Qureshi, 2023a).
- Sec.4.1.2 designs another loss for avoiding collisions. What is the relation between that and LE, where I think S* is also avoiding collisions based on the discussion around Eq.2?

### Soundness
3

### Presentation
2

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
This paper improves a prior physics-based neural motion planning method by proposing a new metric learning approach to better approximate the solution of the Eikonal equation. This is done by enforcing Bellman’s principle of optimality based on the observation that the solution to the Eikonal equation can be viewed as an optimal value function. Further, a new network architecture is proposed for generalizable metric learning. This approach is claimed to perform better than existing motion planning and learning-based planning methods.

### Strengths
- The method is significantly faster than sampling based motion planning.
    
- Compared to other learning-based planning methods that require an expensive data collection phase, this method is self-supervised and hence removes that requirement.

### Weaknesses
 - The proposed method has worse success rates than sampling-based planners. In particular, in the harder 7-DOF manipulator experiment, the proposed method is significantly worse (87%) than learning-free RRT-Connect (98%).
    
- I am not convinced by the claim in the abstract that the method significantly outperforms existing methods, particularly in the more complex 7-dof domain. While it is much faster and has decent success rates, the results are more mixed.
    
- The overall loss function has many hyperparameters.

### Questions
- Why is solving Eikonal equation more scalable than motion planning? What approximations or relaxations does it make? Does it satisfy the robot’s kinodynamic constraints?
    
- The MPC scheme being proposed for planning with the learned value function cannot back-track. Wouldn’t it be better to use a search algorithm, e.g. A\* with the value function as a heuristic to guarantee completeness. The proposed MPC-based planning may fail to solve hard planning problems which is somewhat supported by the low SR in 7-dof planning.
    
- In the 7-dof experiment, what is RRTC’s planning time on the problems solved successfully by the proposed method. It is possible that RRTC’s planning time is higher because it is solving harder problems that your methods fails at. For a fair comparison, it would be useful to know the average planning time for problems successfully solved by all methods.
    
- How did you tune the loss hyperparameters?

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
This paper introduces a self-supervised learning approach for robot motion planning. It builds upon prior work on physics-informed neural motion planning, namely NTFields, in order to tackle complex cluttered environments. This is done through the use of temporal difference (TD) learning to solve the Eikonal equation as an optimal value function, which enforces Bellman’s principle of optimality and enhances convergence. The authors also propose a novel neural network architecture for metric learning that preserves the properties of geodesic distance, and ensure that the triangle inequality, symmetry, and non-negativity are respected. This model is used to compute the cost-to-go in sampling based Model Predictive Control (MPC) to perform motion planning. Experiments are conducted using robots with different numbers of DOFs on various types of environments, and results support most of the authors claims.

### Strengths
- The paper tackles an important problem in robotics and does a good job of highlighting the challenges of performing motion planning in complex cluttered environments for high DOFs robots.
- The authors provide a comprehensive literature review and the approach proposed is well positioned compared to prior work in traditional and neural motion planning. 
- The proposed method is well thought-out and well detailed in the paper. The design choices are sufficiently justified.

### Weaknesses
 - The experimental methodology suffers from some weaknesses. First, the ablation study is conducted on a single 2D maze environment. While results highlight the importance of each loss and the chosen metric for this specific environment, they do not necessarily show that this importance/performance is maintained across different environments. The lack of quantitative results for the ablation study makes it difficult to assess the true impact of each component. Second, in the generalization to novel environments, both seen and unseen environments are used during testing, which in my opinion defeats the purpose of testing the generalization to unseen environments. The inclusion of seen environments in the generalization test inflates the reported performance and does not provide a clear picture of the method's ability to handle truly novel scenarios.
- The article is too technical and a bit complex to follow for a reader who is not completely familiar with this class of approaches. Moreover, the figures are hard to decrypt, captions should provide more details on how to read the figures with legends depicting what each element represents. The lack of clarity in figures and their captions makes it difficult to understand the method's behavior and results. Specifically, the meaning of colors, contour lines, and other visual elements are not clearly explained.
- The method uses a set of user-defined hyperparameters, their values are stated in Apprendix C, however, the paper does not provide any comment on the sensitivity of the approach to these hyperparameters and how to mitigate it, especially the $\Delta T$ parameter. The absence of a hyperparameter sensitivity analysis raises concerns about the robustness and practical applicability of the method. The paper should include a discussion on how the performance varies with different hyperparameter settings and provide guidance on how to choose appropriate values for different scenarios.

### Questions
- Is there a reason why the ablation study was not done in a quantitative manner showcasing that the obtained results are consistent across different environments ?
- Why are both seen and unseen environments used during testing for the evaluation of the generalization to novel environments ? 
- In Fig.1, what do the green points represent ? What about the black line ?
- In Fig.2, what does the color and the contour lines represent ?
- Why is the success rate lower for the 7DOF manipulator at 87% compared to the other experiments, especially since for the 12DOF dual-arm, the method achieves a 91% success rate ?
- Have you conducted a sensitivity analysis to measure the importance of the choice of hyperparameters, and how to set them for each case ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a self-supervised learning approach for robotic motion planning that is based on learning to approximate the Eikonal equation. The work addresses a key challenge in robotics, that of navigating complex environments without requiring costly, expert-generated training data. The authors propose a method that used the Eikonal equation to learn a cost-to-go function that represents both an optimal value function and a geodesic distance in the planning/configuration space.

### Strengths
The paper is well written and clearly presents the approach and evaluation on a set of relevant and reasonable datasets.

The method outperforms existing methods in terms of computational speed, with good performance in terms of success rate, and path length.

The main strength of the approach is the computational efficiency and that it generalizes to unseen environments, which according to the authors was not possible previously with prior self-supervised methods.

The approach is easy to setup and fast to train (few seconds to few minutes), though there are nuances about hyper-parameters as the authors point out.

The ablation part of the paper gives a clear picture of what and how contributes to the methods performance.

### Weaknesses
The main weakness of teh paper is the lack of quantitative analysis of the generalisation capability of the approach. The authors only present visualisations of successful paths in unseen environments. A more comprehensive analysis would be more appropriate, for example,  evaluating the performance across a wide range of unseen environments with varying complexities and against the sota approaches. This would provide a more objective measure of robustness/SR and identify specific types of environments where the approach might struggle.

For the ablation part, is it possible that using only one space configuration might be biasing your evaluations? Have you tried testing on different maze configurations or other types of spaces?

The claim of achieving hight SR in the comparisons in Table 1 could be made less strong or reworded. The SR of the method is consistently on par or lower from the top SR in all examples.

For table 1, clarify what you measure for time in the different cases.

Expand on and give examples on the failure cases you mention when generalizing to unseen environments.

"Superior speed" in s5.3, maybe reword to computational performance or similar.

### Questions
For the ablation part, is it possible that using only one space configuration might be biasing your evaluations? Have you tried testing on different maze configurations or other types of spaces?

The claim of achieving hight SR in the comparisons in Table 1 could be made less strong or reworded. The SR of the method is consistently on par or lower from the top SR in all examples.

For table 1, clarify what you measure for time in the different cases.

Expand on and give examples on the failure cases you mention when generalizing to unseen environments.

"Superior speed" in s5.3, maybe reword to computational performance or similar.

### Soundness
3

### Presentation
3

### Contribution
3
