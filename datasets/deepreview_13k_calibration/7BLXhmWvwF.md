# Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Manipulating objects with varying geometries and deformable objects is a major challenge in robotics. Tasks such as insertion with different objects or cloth hanging require precise control and effective modelling of complex dynamics. In this work, we frame this problem through the lens of a heterogeneous graph that comprises smaller sub-graphs, such as actuators and objects, accompanied by different edge types describing their interactions. This graph representation serves as a unified structure for both rigid and deformable objects tasks, and can be extended further to tasks comprising multiple actuators. To evaluate this setup, we present a novel and challenging reinforcement learning benchmark, including rigid insertion of diverse objects, as well as rope and cloth manipulation with multiple end-effectors. These tasks present a large search space, as both the initial and target configurations are uniformly sampled in 3D space. To address this issue, we propose a novel graph-based policy model, dubbed Heterogeneous Equivariant Policy (HEPi), utilizing $SE(3)$ equivariant message passing networks as the main backbone to exploit the geometric symmetry. In addition, by modeling explicit heterogeneity, HEPi can outperform Transformer-based and non-heterogeneous equivariant policies in terms of average returns, sample efficiency, and generalization to unseen objects.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel setting for representing robotic manipulation problems as heterogeneous graph learning problems. The authors introduce a graph-based policy model, *Heterogeneous Equivariant Policy (HEPi)*, featuring multiple *SE(3)* equivariant message-passing networks (EMPNs) to model smaller sub-graphs like actuators and objects. HEPi explicitly models heterogeneity by assigning distinct network parameters for each interaction type to reduce message mixing and improve expressiveness. HEPi is claimed to be the first study of equivariant policies on 3D space within a reinforcement learning setting for robotic manipulation.

The authors theoretically prove that, for HEPi any two actuator and object nodes can exchange information while the graph network with locally connected actuators and object nodes can not. This justifies their design of actuator nodes as global virtual nodes to connect all object nodes

The authors test the proposed heterogeneous graph representation with reinforcement learning for 6 rigid and deformable object tasks, including Rigid-Sliding, Rigid-Insertion, Rigid-Insertion-Two-Agents, Rope-Closing, Rope-Shaping, Cloth-Hanging. Empirical results show that the proposed approach is more sample efficient and less likely to converge on sub-optimal solutions compared with the state-of-the-art Transformer and non-heterogeneous EMPN methods.

### Strengths
1. The paper is well-written and presents its ideas clearly with solid formulation.
2. The proposed approach of modeling robotic manipulation problems as heterogeneous graph learning problems is well-motivated and clever to unify the structure for both rigid and deformable object tasks using sub-graphs for actuators and objects.
3. The adaptation of *SE(3)* equivariant message passing networks is reasonable and suitable to exploit the geometric symmetry for improving the sample efficiency in the large 3D search space of configurations. As far as I know, HEPi is one of the first studies of equivariant policies on 3D space within a reinforcement learning setting for robotic manipulation.
4. The empirical experiments are comprehensive and sound to support the arguments. Most results are averaged over 10 seeds using
interquartile mean with 95% confidence intervals, which is also statistically robust.

### Weaknesses
1. The experiments are limited to simple geometric shapes like ropes, triangles, and stars, which can be easily modeled using a few nodes (< 100 in all the experiments). However, the target objects in most 3D manipulation tasks are more complex and sophisticated, e.g., cabinets or dresses, which require significantly more nodes to model. I doubt whether HEPi can still generalize to all those complicated geometries, which brings much computational complexity to graph learning. Specifically, the paper does not address the scaling of the graph construction and message passing with respect to the number of nodes. The computational cost of k-nearest neighbor search for graph construction, and the increased message passing overhead in larger graphs, are not discussed. This is a critical concern for real-world applicability where objects often have complex geometries requiring thousands of nodes for accurate representation.
2. The current framework assumes that the object coordinates are readily available in the observation, which is basically a simulation setting. In real applications without coordinates, such coordinates can only be extracted from other CV models in the wild. As a graph policy model, HEPi is likely to suffer from the cumulated error in the observation and fail the tasks compared to non graph learning methods. The paper does not discuss the impact of noisy or inaccurate keypoint detections on the performance of HEPi. The reliance on perfect keypoint coordinates is a significant limitation, as real-world perception systems are prone to errors and occlusions. This could lead to a mismatch between the graph structure used by the policy and the actual physical state of the environment, causing the policy to fail.
3. Some typos:
- L17: objects -> object.
- L182: “lifts”, the left quotation mark.
- L344: There should be a blank space before HEPi.

### Questions
1. Can HEPi generalize to more complicated geometries in the real world other than simple ropes or shapes like hearts and stars, which might bring much computational complexity to graph learning?
2. How sensitive is HEPi to the perturbation of the object coordinates from the observation?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a novel SE(3) equivariant RL method called HEPi, and introduce a new benchmark for future geometry-aware RL evaluations.  The paper use EMPNs as algorithm backbone to allow model generalize between poses and its heterogeneity. The paper use graph as representation and do thorough mathmetical analyze.

### Strengths
+ Clever Design: This paper includes several ingenious designs. 
   + The use of EMPNs The use of SE(3)-equivariant networks ensures that the model naturally possesses SE(3) generalization, thereby reducing the search space and complexity. 
   + The use of TRPL the introduction of TRPL in place of traditional PPO makes hyperparameter tuning easier, addressing a significant challenge in RL training.

+ Detailed Appendix Experimental Description: One of the major issues in RL is poor reproducibility. However, in this paper, the authors provide a detailed appendix that lists experimental information, including the reward function and hyperparameters. This makes the paper highly reproducible.

+ Benchmark Design: This paper provides a detailed demonstration of the proposed benchmark tasks in the video and clearly defines these tasks in the appendix. As a result, these tasks and environments can be easily adopted by the research community.

I am inclined to accept this paper.

### Weaknesses
 + Real-World Application: As the authors note, this paper uses ground-truth model inputs and does not incorporate a physical robot, which means it cannot be directly applied to real-world scenarios. However, given the significant contributions of this paper in terms of benchmarking and methodology, I do not consider this a critical issue. Nonetheless, I still recommend that the authors include some specific experiments to evaluate this aspect. I suggest author can simply add visual capture pipeline. The details are as follows:
    + For task like rigid insertion and rigid sliding, you can simply add camera to take picture then use a common pose estimation module to estimate the position. The potential errors in pose estimation can be used to test the robustness of the proposed method to input errors.
    + For tasks involving fabrics or ropes, you can directly use a camera to capture point clouds and then construct a graph using the point cloud data.
+ Geometry aware: This paper does not seem to have any special designs focused on geometry, although graphs do play a role. However, the primary focus of the paper appears to be on SE(3)-equivariant designs.

### Questions
Thank you for the detailed appendix, which has addressed my questions about the specifics. If the authors can supplement the experiments as suggested, I would be willing to increase my score.

### Soundness
3

### Presentation
4

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
This paper addresses the task of manipulating diverse rigid and deformable objects with geometry-aware rl policy.

A heterogeneous graph is proposed to represent rigid and deformable object manipulation tasks. To leverage geometric symmetry for better task performance and sample efficiency, a heterogeneous equivariant policy that utilizes SE(3) equivariant message passing networks is proposed. 

Evaluation is carried out on a self-curated rl benchmark, including rigid insertion of diverse objects, as well as rope and cloth manipulation with multiple end-effectors. The proposed method outperforms baseline methods in terms of average returns, sample efficiency, and generalizability.

### Strengths
The proposed heterogeneous graph representation is a general representation for both rigid and deformable object manipulation tasks, and captures the geometric structure of the object. HEPi is a novel formulation of graph-based equivariant policy build on top of the heterogeneous graph representation that enables rl for manipulation of diverse shapes and deformable objects.

The paper has demonstrated thorough evaluations and ablations in simulation, with convincing results proving that the proposed method has better performance, sample-efficiency, and generalizability. Detailed discussions are provided for the results, providing interesting insights.

### Weaknesses
The object model that contains vertices are required for the object node representation, which is the main observation for the policy. This might not be easy to get in the real world due to a lot of self-occlusions during deformable object manipulation.

The paper demonstrates thorough evaluations across various simulation benchmarks, but lacks real-world evaluations to make the method fully convincing in terms of it's usefulness to real-world robot applications.

typo at line 74: equivariacne->equivariance.

### Questions
Could the authors expand more on line 51-52 about attention making the optimization landscape more difficult to traverse?

Would the policy be able to generalize to objects with different physical properties?

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
2

### Summary
The paper trains policies for one or two end effectors to manipulate rigid and deformable objects (ropes and cloths). It models the actuator and object of interest with a heterogeneous graph and advocates for a heterogeneous equivariant policy (HEPi). The paper benchmarks its method on tasks including manipulating rigid and deformable objects in IsaacLab and reports its superior performance over typical baselines.

### Strengths
In general, I find the story in this paper intuitive and convincing. While the two core building blocks (heterogeneous graphs and equivariant policies) have been explored in prior arts, this paper presents a proper combination of both in the setting of rigid/deformable object manipulation. I feel the proposed method has the potential to be extended to manipulate fluid and rigid/soft/fluid-coupled systems, and it would be a pleasant surprise if the paper could demonstrate a fluid scene similar to the “Pour Water” task in Lin et al 2020. Of course, I understand this is outside the scope of the current submission.

### Weaknesses
I generally agree with the limitations listed in the paper. I think the paper can be improved in the following ways:

1. While the technical method and the story look promising, the benchmark scenes are still relatively simple because the setup only models a point-like end effector, ignoring kinematic and dynamic constraints in practical robotic hand/arm structures. Therefore, transferring the result to a real-world robot is not straightforward and probably requires more algorithmic development. Specifically, the point-like end effector lacks the degrees of freedom and physical constraints of a real robotic manipulator, such as joint limits, torque constraints, and the complex dynamics of a multi-link arm. This simplification makes it unclear how the learned policies would generalize to a system with more realistic actuation. The paper does not address how the proposed method would handle the complexities of inverse kinematics, dynamic control, and the potential for self-collisions that arise with real robotic manipulators.

2. From a dynamic perspective, the 2D rigid-sliding task is too trivial to be a valuable benchmark for evaluating this paper and its baselines. This is already reflected in the result: “HEPi and Transformer policies perform comparably, suggesting that the limited task complexity does not fully leverage the benefits of equivariant constraints. ” I suggest this experiment remove the suction gripper and try pushing the rigid object to its target position and orientation with one/two end effectors and their contact with the object, similar to the setup in http://sain.csail.mit.edu/. The current setup with a suction gripper essentially reduces the task to a pick-and-place problem, which does not fully test the capabilities of the proposed method in terms of contact dynamics and manipulation. A pushing task would introduce more complex interactions between the end effector and the object, requiring the policy to learn more nuanced control strategies.

3. Deformable objects can be classified by their dimensions: codimension-2 (e.g., ropes), codimension-1 (e.g., cloths), and codimension-0 (e.g., rubber balls). The paper seems to consider the first two categories only. Handling full-dimension soft objects in the proposed method may be non-trivial because it requires observations of object coordinates and cannot be easily obtained by “integrating state-of-the-art computer vision techniques to extract key points from cameras.” The paper should clarify that the method's reliance on keypoints may not be sufficient for representing the full state of 3D deformable objects, which require information about internal deformations. The method's ability to handle complex deformations such as twisting, bending, and compression in 3D volumetric objects is not demonstrated, and it's unclear how the proposed approach would extend to these scenarios.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2
