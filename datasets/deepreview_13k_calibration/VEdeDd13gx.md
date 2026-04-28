# ManiBox: Enhancing Spatial Grasping Generalization via Scalable Simulation Data Generation

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Learning a precise robotic grasping policy is crucial for embodied agents operating in complex real-world manipulation tasks. Despite significant advancements, most models still struggle with accurate spatial positioning of objects to be grasped. We first show that this spatial generalization challenge stems primarily from the extensive data requirements for adequate spatial understanding. However, collecting such data with real robots is prohibitively expensive, and relying on simulation data often leads to visual generalization gaps upon deployment. 
To overcome these challenges, we then focus on state-based policy generalization and present \textbf{ManiBox}, a novel bounding-box-guided manipulation method built on a simulation-based teacher-student framework. The teacher policy efficiently generates scalable simulation data using bounding boxes, which are proven to uniquely determine the objects' spatial positions. The student policy then utilizes these low-dimensional spatial states to enable zero-shot transfer to real robots. 
Through comprehensive evaluations in simulated and real-world environments, ManiBox demonstrates a marked improvement in spatial grasping generalization and adaptability to diverse objects and backgrounds.
Further, our empirical study into scaling laws for policy performance indicates that spatial volume generalization scales positively with data volume. For a certain level of spatial volume, the success rate of grasping empirically follows Michaelis-Menten kinetics relative to data volume, showing a saturation effect as data increases.
Our videos and code are available in the \href{https://thkkk.io/manibox}{project page}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors tackle the challenge of spatial generalization and sim-2-real transfer of vision based control policies for robotic manipulation using a teacher-student reinforcement learning framework. The teacher policy, which is trained using privileged information about object location, etc.. is used to generate large scale robot trajectory data which is then used to distill a student policy which achieves sim-2-real transfer to real-world tasks. The authors also shed some light on the amount of robot trajectory data required for a given volume of reachable space of a robot.

### Strengths
The paper is well written and easy to read. Aside from a few details that I mention in the questions section, In my opinion the authors provide sufficient details about the experimental set up for an interested reader. The supplementary video provided also supports the paper well.

The challenge being addressed is very relevant to robotic manipulation and the results and methodology presented in the paper are interesting and compelling enough to inspire future research along similar lines.

### Weaknesses
1) Pseudo algorithm - In my opinion, the readability of the paper can be improved by including a pseudo algorithm that describes how the teacher is trained --> the criteria for selecting the successful robot trajectory from teacher policy --> The distillation process that generates the student policy could be very useful for a reader. 
2) The paper lacks a section on the weaknesses of the current approach. Even in the supplementary video, I dont recall a scenario where the policy fails. I think its important to know some of the failure cases of the method as well. 
3) Although this might be common knowledge among RL researchers - more information regarding the reward design could be helpful. Im assuming it involves getting close to the object and then closing fingers, however, this clearly depends on the distance to object and how fast the robot is moving - describing the reward mathematically would be a good addition to the paper.

### Questions
The proposed method uses bounding box as object representation for grasping, however clearly bounding box does not capture local surface geometry of the object being manipulated. For example, an odd shape such as banana will not be represented by a bounding box well. Do the authors think that this could be a weakness of this approach? If so, how can it be addressed? I notice that most of the objects being manipulated are spherical/cylindrical in shape which might be easy to grasp, were any other objects used to test the policy? 
Another observation I had is that the grasping motion seems consistently similar regardless of the test scenario (be it different object, background), some objects might need grasping from the top, did the teacher policy ever learn this behavior?

Apologize if I missed this, but what is the history length of input observations for the LSTM student policy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method called ManiBox to train generalizable (to 3D location and object) grasping policies in simulation and successfully transfer them to the real world. The method works by:
1. First, a teacher policy is trained in simulation to grasp objects using Reinforcement Learning
2. A student policy is trained in simulation that uses as observation bounding boxes of the target object from multiple camera streams
3. Bounding boxes provide a low dimensional representation that transfers reasonably well between sim and real. Sim has privileged information so it's easy to get bounding boxes. In real, the YOLO world object detection module is used.

Using this method, the authors show successful sim-to-real transfer and generalization to different objects, backgrounds & 3D locations. The authors also present a study on scaling laws of success rate vs training dataset size.

### Strengths
1. Improvement over baseline in the given task of object grasping
2. Insightful study on data scaling laws for robotic object grasping

### Weaknesses
1. Lemma 2 is a well known result in 3D computer vision. Hartley, R. and Zisserman, A., 2003. Multiple view geometry in computer vision. Cambridge university press.
2. Limited comparison to baseline. Baseline scores are simply 0 even though there are numerous object-grasping methods (learning & heuristic based) that can grasp objects in different 3D locations.

### Questions
1. Line 492-493: Why does vision based ACT get a score of 0? Paper reports that vision based ACT "experiences a visible drop on success rate when spatial range scales up".  Is it because of the visual discrepancy between sim and real? 

Prior work has shown strong results of ACT with limited real world data.
Zhao, T.Z., Kumar, V., Levine, S. and Finn, C., 2023. Learning fine-grained bimanual manipulation with low-cost hardware. arXiv preprint arXiv:2304.13705.

2. Line 265: "ensure its dynamics are consistent with the real world". How was it ensured?

### Soundness
3

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
The paper introduces ManiBox, a framework for improving the generalization of robotic grasping through bounding-box-guided manipulation. Using a teacher-student policy setup, the teacher generates data in simulation, and the student learns to transfer this knowledge to real-world scenarios. Objects are represented with bounding boxes, aiming to reduce complexity and enhance generalization. A key finding is the scaling law that shows data requirements grow non-linearly with spatial volume. While the system demonstrates strong Sim2Real performance, some design choices and experimental setups leave room for clarification.

### Strengths
**Effective Sim2Real Transfer:**

The random masking strategy helps the system transfer successfully from simulation to real-world environments.

**Background Generalization:**

The system maintains good performance across diverse backgrounds, which adds practical robustness.

**Scaling Law Insight:**

The identified relationship between data volume and spatial generalization offers valuable guidance for data-driven models.

### Weaknesses
 **Limited Object Diversity:**

The experiments use similar and simple objects, which limits the demonstration of the full generalization potential. A wider variety of objects, with more complex geometries and material properties, might better highlight the benefits of the approach. For instance, the experiments could include deformable objects, objects with articulated parts, or objects with varying surface textures to truly assess the robustness of the method.

**Unclear Bounding Box Usage:**

The relationship between bounding boxes for object detection and manipulation is not clearly explained. It's unclear how the 2D bounding box detections are translated into 3D manipulation actions. This makes it hard to understand how they work together effectively, especially considering the robot's need for 3D positional information. The paper should clarify if the bounding box center is used as a direct target or if further processing is involved to infer the 3D pose of the object.


**Fixed Cubic Space Constraint:**

The use of fixed cubic spaces (b x b x b) seems arbitrary. It’s unclear if more flexible bounding volumes, such as oriented bounding boxes or bounding volumes that adapt to the object's shape, could improve results. The justification for using fixed cubic spaces is not well-supported, and it's unclear if this choice limits the system's ability to generalize to more complex spatial arrangements.

Complex Camera Setup:

The use of three cameras raises questions, as stereo vision with two cameras is often sufficient for localization. The necessity of the third camera is unclear, especially if the system is primarily relying on 2D bounding box detections. The paper should justify the need for three cameras and explain how the data from each camera is utilized in the system.

**Fragmented Descriptions of Settings:**

The simulation, real-world, and policy setups are described separately, making it difficult to compare them. A more structured comparison, perhaps using a table or a unified diagram, would improve clarity and allow readers to easily understand the differences and similarities between the different environments and setups.


**Lack of Vertical Variations:**

The experiments seem limited to flat surfaces. It’s unclear if the system can handle objects with more Z-axis variation or bounding boxes placed in mid-air. The paper should explicitly address how the system handles objects at varying heights and whether the bounding box representation is sufficient for such scenarios.

**Formula 4 Confusion:**

Equation 4 lacks clear explanations of some symbols and their meanings, making it harder to follow. The paper should provide a detailed explanation of each symbol and its role in the equation to ensure clarity and reproducibility.

### Questions
1. **Can Bounding Boxes Be Scaled or Combined?**
    - Would it be possible to **scale or combine multiple bounding boxes** to handle more complex objects and improve generalization?
2. **Why Use Fixed Cubic Spaces?**
    - Is there a reason for using **b x b x b cubes** as operational spaces, or could other bounding volumes work better?
3. **What Are the Camera Setups in Real-World Experiments?**
    - Are cameras mounted on the **robot arm and the environment**? What role does each camera play?
4. **Is the Bounding Box 2D or 3D?**
    - Are the bounding boxes used **2D projections** or full **3D representations**?
5. **Can Bounding Boxes Exist in Mid-Air?**
    - Could the system define **floating bounding boxes**, or are they constrained to surfaces?
6. **What Background Challenges Were Faced?**
    - Could the paper clarify the **specific challenges** from changing backgrounds and how they were addressed?
7. **What Are the Teacher Policy’s Hardware Requirements?**
    - What specific **hardware resources** are needed for the teacher policy?
8. **Where Are Random Points Placed?**
    - Are the **random points** generated at the **object’s center or across its surface**?
9. **What Are the Simulation Object Types and Task Settings?**
    - A more detailed description of the **simulation tasks and object setups** would help understand the system’s scope.
10. **How Is Trajectory Quality Linked to Rewards?**
    - What criteria are used to **distinguish good trajectories** from bad ones in the reward function?
11. **Need for Clearer Visuals**:
    - Including **bounding box annotations in simulation screenshots** would help readers, especially those without robotics experience, better understand the process.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a manipulation method called ManiBox, which operates using bounding-box inputs. The policy is trained using a student-teacher framework. Specifically, a teacher policy is trained with PPO using privileged information, such as the object's 3D position. A dataset of expert trajectories is then generated from this teacher policy, which is subsequently used to train a student policy through imitation learning. Isaac Lab is employed as the simulator to facilitate scalable data collection. The authors demonstrate that as the workspace size increases, a larger amount of expert data is required to train effective student policies. Finally, the trained student policies can be deployed on a real robot by using bounding boxes generated from an open-vocabulary object detection model.

### Strengths
**General Idea**
-  Leveraging vision-foundation models to train policies that can be deployed on real robots is an interesting and relevant approach for addressing many real-world manipulation tasks.

**Real-robot Deployment** 
- The proposed method is tested on a real robot, verifying that the inputs from the open-vocabulary detection model can be used to transfer the learned behaviors.

**Visual Presentation**
- The overview figures, particularly Figure 2, effectively clarify the proposed model.

### Weaknesses
 **Low Novelty**
- The paper does not introduce a novel method, but rather employs a specific student-teacher learning formulation, using bounding boxes in the student's input space. Additionally, the finding that the amount of expert data required to train a proficient student policy scales with the robot's workspace size is unsurprising.
- The method trains on a single object (with randomization in its scale) using a parallel gripper in an uncluttered tabletop scenario, which is a very simple task configuration that has been addressed without the need for interactive RL policies (see e.g. https://inria.hal.science/inria-00325794/document)

**Method Limitations**
- Representing objects through 2D bounding boxes provides only a rough approximation of an object’s convex hull, which is likely insufficient for generalizing to objects with diverse shapes. The method's reliance on bounding box centers for grasping, while simple, may not be robust for objects with complex geometries or varying mass distributions, where grasping at the center may not be optimal or even feasible.
- The method currently relies on multiple camera observations. Inferring object states from a single RGB-D camera or using the history of wrist-camera observations from different poses would make the approach easier to deploy.

**Results and Research Claims**
- The Abstract claims that the paper will demonstrate that most models’ spatial generalization challenges stem from high data requirements for spatial understanding. However, this is not substantiated, as dataset size is the only variable that is investigated in the experiments. Moreover, reformulating the problem from joint-space actions and observations to end-effector control, with object position relative to the robot's gripper, could reduce variability that is unnecessary for task completion.
- Object generalization is evaluated by testing on items different from those encountered by the teacher policy. It is mentioned that two objects are out of distribution, yet since the teacher policy training does not cover these objects, there is no reason to expect it to generalize to this configuration. Furthermore, details on how this experiment was conducted—such as the number of trials and object positions—are missing. While it is possible to learn a grasping strategy that is sufficiently general to cover the tested items, this is not a feature of the method since the teacher policy is never incentivized to do so.
- In the Background Generalization results section, the model's generalization ability is attributed to its integration of historical information, multi-camera data, and random masking, but none of these claims are verified.

### Questions
- Why is the teacher policy used to generate a dataset of expert trajectories from which the student policy is learned, instead of using DAgger, given that the teacher policy could be queried for expert actions at each state?
- Why does the teacher policy not have access to the ground-truth object size? If the student policy can infer the object size from detected bounding boxes, the teacher policy could also utilize this information to adapt its grasp for different object sizes.
- Following line 255, it is mentioned that the state space dimensionality is high, while one of the motivations for using student-teacher learning was to formulate a compact input space for the teacher policy to facilitate efficient learning. Furthermore, it is claimed that this reduces the exploration space of the RL environment, but the details are missing in Appendix B.1. Could you explain how the exploration space was reduced and why?
- In Figure 2, you state there is a bijective mapping between the privileged object representation and its bounding-box detections, implying that the inputs required to deploy the teacher policy could be computed directly from visual detections. If that is the case, why is the student-teacher framework necessary?
- If the model controls the robot via joint commands, how are self-collisions and collisions with the tabletop avoided?
- The data in Figure 3, showing the scaling relationship between spatial generalization and the amount of data, appears to deviate significantly from the expected trend, particularly in the 10cm x 10cm x 10cm workspace. Could you explain why this occurs, and whether the data points were reported for a single seed?

### Soundness
1

### Presentation
2

### Contribution
1
