# UniContact:A Basic Model for Robotic Manipulation of Contact Synthesis on Rigid and Articulated Rigid Bodies with Arbitrary Manipulators

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
We posit that one fundamental, core component of robotic manipulation is inferring contacts with the environment, enabling the agent to exert control. In this work, we study a fundamental problem of contact synthesis in robotic manipulation to choose a set of contact positions and forces on a random rigid or articulated rigid object for an arbitrary robot manipulator to produce a specified external wrench.  Our framework first segments the point clouds with normals into feasible contact region sets. For each feasible contact region set, a model is trained to produce the feasible contact point within these region sets by taking as inputs the robot description, the target wrench, the object point cloud with normals, and the contact region set. After gathering the contact positions from the neural network model, we develop an optimization process to fine-tune the contact points and contact forces and generate the joint values for the robotic manipulator to exert contact forces on the object's surface without penetration.  We perform extensive experiments to verify the effectiveness of our proposed framework both in simulation and in real-world experiments. Supplementary and Videos are on the website.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces, UniContact, which is aiming for contact synthesis for robotic manipulationn. It addresses the challenge of choosing contact positions and forces on objects to produce specified wrenches, using point cloud segmentation and deep neural networks. The framework optimizes contact points and forces and generates collision-free joint values for manipulators. The approach is validated through both simulations and real-world experiments.

### Strengths
The authors have incorporated wrench consideration into the generation of contact points. They attempted a real-robot experiment, although they only provided a setup figure.

### Weaknesses
The proposed methodology makes some severly constraining assumptions:

-The examined setting seems to assume that no external forces are applied to the manipulated object at any time, other than the manipulation forces from the robot. In the vast majority of real-world manipulation tasks this assumption does not hold, as friction and gravity play an important role on the required manipulation forces (for complex tasks other than grasping, where the submissions aims to focus). For instance, when manipulating an object on a table, the normal force and friction from the table are crucial for maintaining stability and achieving the desired motion. The absence of consideration for these forces significantly limits the practical applicability of the method.

-The proposed Inverse Kinematic solution does not consider collisions with background (support) objects (e.g. a table), or clutter from other objects in the scene. This limits the applicability of the proposed approach in real-world environments and generic tasks. The IK solver should ideally incorporate collision checking with the environment, which would require a more sophisticated representation of the scene beyond just the manipulated object's point cloud. Without this, the robot's planned motions could easily lead to collisions, rendering the approach unusable in cluttered environments.

-Being mostly applied in simulation and pre-segmented object point cloud data, the resilience of the proposed approach to sensor noise, segmentation errors, partial observability etc is not evaluated. These factors can hinder its applicability to the real world. Additionally, the need for a segmented object pointcloud contradicts the motivation of manipulation arbitrary (previously unseen) objects. Real-world sensor data is inherently noisy and incomplete, and the performance of the proposed method needs to be evaluated under these conditions. The reliance on perfect segmentation also limits the method's ability to handle situations where the object is partially occluded or difficult to segment.

Additionally, In my opinion, the contributions of the proposed methodology are best suited to the robotics community, where the proposed framework can be most appreciated. In the context of an ML-venue, the representation learning-related contribution appears minimal.

### Questions
Typo: upper and lower limitations. Figure ?? on top of Page 7.
Why are there 2n+1 configurations? If for joint i, it has two possibilities L_i and H_i, while the rest are M_j, it seems there would be a total of 2n configurations.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission introduces a pipeline for contact synthesis in robot manipulation scenarios. Given a point cloud of the target object, along with a geometric representation of the robot’s end-effector and a description of the target manipulation task (in the form of desired linear and angular acceleration in 6 DoF (wrench)), the proposed pipeline identifies target contact positions and required forces (through a learnable approach) that are subsequently translated to robot joint positions via a two-stage inverse kinematic solution that ensures collision-free manipulation.  A large scale dataset of manipulation contacts with synthetic objects, featuring a large variety of different objects and robot end-effectors is also contributed.

### Strengths
-The examined manipulation problem is very ambitious and the provided solution contributes towards generic robot skills, in the sense that the proposed approach is aimed to be applicable on arbitrary robot end-effectors and is able to deal with previously unseen objects. 

-The provided problem formulation and contributed dataset can facilitate further research in the field.

-Overall the manuscript is well-written and easy to follow, and provides adequate context for non-expert readers.

### Weaknesses
The proposed methodology makes some severly constraining assumptions:

-The examined setting seems to assume that no external forces are applied to the manipulated object at any time, other than the manipulation forces from the robot. In the vast majority of real-world manipulation tasks this assumption does not hold, as friction and gravity play an important role on the required manipulation forces (for complex tasks other than grasping, where the submissions aims to focus). 

-The proposed Inverse Kinematic solution does not consider collisions with background (support) objects (e.g. a table), or clutter from other objects in the scene. This limits the applicability of the proposed approach in real-world environments and generic tasks.

-Being mostly applied in simulation and pre-segmented object point cloud data, the resilience of the proposed approach to sensor noise, segmentation errors, partial observability etc is not evaluated. These factors can hinder its applicability to the real world. Additionally, the need for a segmented object pointcloud contradicts the motivation of manipulation arbitrary (previously unseen) objects. 

Additionally, In my opinion, the contributions of the proposed methodology are best suited to the robotics community, where the proposed framework can be most appreciated. In the context of an ML-venue, the representation learning-related contribution appears minimal.

### Questions
-How can the proposed method be extended to deal with the presence of other external forces on the manipulated object?

-How can the proposed IK solution be extended to address collisions with other objects in the manipulation environment?

-How resilient is the proposed approach to RGB-D sensor noise and segmentation errors / partial observability of objects and occlusions. 


Presentation:
-Many of the figures are not reference in the text, which can disturb the flow.

Notes:
-The provided supplementary material file is identical to the main submission, on the reviewer's side.
-The manuscript makes several references to an anonymised website where supplementary information is stored, which at the moment is empty of content. 

Typos:
Sec.2: "Fricion Cone" -> Friction Cone
Sec.3: "Fig.??"  
Sec.3:  Fig missing caption.
Sec.6: "The proposed framework." (phrase cut (?)).


Post-Rebuttal Edit:  Score reduced from 5(BR) to 3(R), given the lack of a rebuttal submission by the authors, which leaves many of the raised concerns unaddressed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes UniContact framework to predict contact points and robot poses for arbitrary robotic manipulator to grasp rigid objects. The work extends the UniGrasp to concurrently predict both the contact points and robot (hand) poses, given by the more input of wrench.

### Strengths
1, This paper formulates the robotic grasping task as applying a wrench to the object, which is more physically intuitive. Given object point clouds, target wrenches and robot point clouds, the framework can output contact and robot poses directly.

2, The training data includes millions of training examples with diverse 100K+ object models from 1K+ categories and different kinds of manipulators. UniContact can produce valid contact point sets not only on novel objects but also generalizes to new robotic manipulator.

### Weaknesses
1, In inference stage, how can users obtain the target wrench of an object with specific task description? For the same object but different task requirement, the desired wrench might be different. The efforts to generate the target wrench should be discussed further in the paper to evaluate whether is realistic for robot manipulation.

2, It is not clear how this new formulation benefits autonomous robot manipulation. I have doubt that the delicate calculation of required wrench as in input for a manipulation task may make the task complex, which contradicts the purpose of learning-based approach.

3, Another concern about the paper is its technical novelty. The paper is mainly inspired by UniGrasp. As much as I appreciate the novel improvements including contact optimization and IK solver, I had a hard time justifying the technical novelty of this paper given that the main focus of the ICLR conference is on learning methods themselves.

4, The experiment part is weak and insufficient, where the baseline is only UniGrasp and there is no ablation study or detail analysis provided.

5, Some key information and experiments are stated in the manuscript to be provided in the website link. But until now, the website is still empty. With these, it makes the paper hard to understand.

6, There are some grammar errors in the paper, including the figure index in the first line of 7th page, the last sentence in RELATED WORK etc.

### Questions
1, I also have doubts about whether to generate the required wrench by hand kinematics and pose is meaningful. For example, to lift up the object, the hand/gripper can be just to exert the static friction force on the object; any force, motion speed can be externally applied by the robot instead of the hand/gripper? The concept of wrench will be only meaningful if considering the dynamics of object.

2, UniContact seems only focus on single object grasping. Can it also apply to more realistic task such multiple/stacked objects grasping in cluttered environment?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on generating gripper configurations using object point clouds, with a significant contribution being the optimization of the chosen grasp area to create collision-free gripper postures. The research notably includes tests across multiple gripper types, demonstrating versatility in applicability, an advancement in the robotics and computer vision fields.

### Strengths
This paper employs optimization techniques for contact and collision avoidance, enhancing the system's overall framework and presenting a clear and comprehensive logic.

### Weaknesses
The paper lacks sufficient comparative experiments, emphasizing the complexity of robotic hand inverse kinematics. However, recent studies have proliferated in generating desired human hand postures based on object models. There is a certain similarity between the collision-free generation of robotic gripper configurations on objects and that of human hands, which calls for comparative experiments to demonstrate the superiority of the proposed method.

Moreover, concerning novelty, the paper employs the Artificial Potential Field method, a classic collision avoidance algorithm, though there are more advanced methods that might perform better. This traditional approach, while reliable, is not necessarily at the forefront of current technological advancements in robotics. 

The author could strengthen the paper by comparing the proposed method with contemporary strategies that also aim for collision-free grasping. This comparison could highlight specific advantages in efficiency, accuracy, or applicability in diverse scenarios.

Additionally, while the paper highlights the intricacies of inverse kinematics in robotic grasping, a more in-depth exploration and comparison with human-like grasping techniques are advisable. These comparisons could offer insights into natural and intuitive grasping postures, potentially improving the robotic system's performance and versatility. It would be compelling to see if incorporating advanced techniques could further optimize collision avoidance and gripping efficiency, making a stronger case for the proposed method's applicability and superiority.

### Questions
The concerns you raised highlight significant areas in the research presentation that need improvement. First, the inability to access supplementary materials like the experimental demos, detailed network information, data, and video demonstrations that the paper references is a major drawback. These materials are often crucial for readers to fully understand, replicate, or even extend the research, and their absence can limit the paper's impact and credibility.

1. **Inaccessibility of Supplementary Materials**: The authors should ensure that all supplementary materials referenced in the paper are readily accessible. This may require updating the paper with working links or providing an alternative means of access, such as a supplementary appendix or a stable public repository. This accessibility is paramount, especially for readers and researchers who rely on these resources to deepen their understanding or build upon the existing work.

2. **Incomplete Sections**: Regarding the observation that the paper appears unfinished, particularly in the section on related work, this is a critical issue. The related work section is fundamental in any research paper as it situates the research within the context of existing literature, highlighting the unique contributions of the paper and building its premise on previously established concepts, techniques, and findings.

   - The authors must address any areas of the paper that appear incomplete by providing a comprehensive review of relevant literature, discussing how their work is different from and/or improves upon previous approaches. This is not only important for situating the research in its academic context but also for justifying the paper's contributions.

In conclusion, the authors need to address these significant shortcomings by ensuring the complete accessibility of supplementary resources and completing all sections of the paper thoroughly. These steps are necessary to enhance the paper's reliability, comprehensiveness, and overall contribution to the field.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
