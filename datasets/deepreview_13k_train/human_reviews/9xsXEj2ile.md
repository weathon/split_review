# BiAssemble: Learning Collaborative Affordance for Bimanual Geometric Assembly

- Decision: Reject
- Scores: 6, 8, 6, 6

## Abstract
Shape assembly, the process of combining parts into a complete whole, is a crucial skill for robots with broad real-world applications. Among the various assembly tasks, geometric assembly—where broken parts are reassembled into their original form (e.g., reconstructing a shattered bowl)—is particularly challenging. This requires the robot to recognize geometric cues for grasping, assembly, and subsequent bimanual collaborative manipulation on varied fragments. In this paper, we exploit the geometric generalization of point-level affordance, learning affordance aware of bimanual collaboration in geometric assembly with long-horizon action sequences. To address the evaluation ambiguity caused by geometry diversity  of broken parts, we introduce a real-world benchmark featuring geometric variety and global reproducibility. Extensive experiments demonstrate the superiority of our approach over both previous affordance-based and imitation-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the task of geometric assembly, which is a long-horizon task requiring pick-up, alignment, and assembly. The paper tackles this task through predicting collaborative affordance and gripper actions for bimanual geometric shape assembly. A real-world benchmark for re-assembling broken parts is created. Extensive evaluations demonstrate the effectiveness of the approach and shows generalizability to unseen object categories.

### Strengths
The paper addresses a useful task that has been under-explored in previous robotics works, and provides an effective approach to solve this challenging task.

A real-world benchmark on geometric assembly is created, which paves way for future research on this direction.

Thorough evaluations in both sim and real are carried out to demonstrate the effectiveness of the approach. The model is generalizable to shapes from unseen categories.

### Weaknesses
For real-world experiments, only qualitative results are presented, there is a lack of quantitative results on more object shapes and comparisons to other baselines. There is also a lack of more detailed sim2real transfer analysis, for example, comparing the results of an exact same set of shapes in simulation and the real world.

The paper only includes one ablation study on w/o SE(3), however, the approach is a combination of multiple components and more ablations would be helpful to better understand the effect of each component.

The task setup only considers objects with two fragments, however, in reality there could be an arbitrary number of fragments, but the proposed model cannot generalize to different numbers of parts.

### Questions
The provided website link seems broken?

Are evaluations in simulation carried out with floating grippers? It would be more realistic to control grippers mounted on bi-manual arms, as there could be singularity and arm-table collision issues that are not being taken into account with the floating grippers.

How would the accuracy of the pose estimator (line 288-289) affect the performance? If the pose estimation is a bit off due to occlusions or sensor noises in the real world, would the model be robust to it and still manage to succeed?

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
This work presents BiAssemble, a framework designed for bimanual robotic manipulation of fractured geometric shapes. The framework utilizes affordance learning to tackle complex long-horizon tasks involving multiple steps, including grasping, alignment, and final assembly. A disassembly prediction determines feasible disassembly directions and a bimanual affordance prediction enhances action planning for assembly. Results suggest significant improvements over baseline methods in both simulation and real-world experiments.

### Strengths
- Task itself is very novel.
- Addresses the challenging domain of geometric assembly with fractured parts, using a combination of affordance learning and collaborative action prediction. The proposed method became more valuable by supporting bimanual coordination and multi-step processes.
- The real-world benchmark offers a strong foundation for evaluating geometric assembly tasks, with a range of fractured objects and reproducible environments. 
- Affordance learning makes a lot of sense

### Weaknesses
 - Lacks a robust analysis of failure cases, which would provide insights into the system’s limitations and areas for improvement in real-world scenarios.
  - Specifically, consider adding a categorization of different types of failures, quantitative analysis of failure rates in different scenarios, or discussion of specific challenging cases. One example: is there a specific type of object that your policy fails to generalize to? or if there's ambiguity, how does the failure look?

### Questions
- how does the method handle symmetry? For example the fracture is a verticle cut? Maybe include an analysis or experiment specifically examining performance on symmetrical fractures, if you haven't already done so.
- how does the method compare with RL-based methods? Id suspect that reward hacking could work for this task. Maybe discuss why you chose the current approach over RL methods
- website does not work: link redirects to 404.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the shape assembly task for reconstructing broken objects. This paper proposes a multi-stage BiAssembly framework to complete this task. The BiAssembly framework first gets an imaginary assembled shape using SOTA methods, then predicts the disassembly direction, alignment pose transformation, pick-up affordance, and finally the gripper alignment and assembly poses. Additionally, this paper introduces a real-world framework. The experimental results show that the BiAssembly framework surpasses previous methods.

### Strengths
1. The paper is well-written overall, with technical points and experiments clearly articulated.
2. The framework is feasible for shape assembly, and its performance surpasses previous heuristic or policy-based methods, according to the outcomes in the paper.

### Weaknesses
1. The multi-stage framework involves some assumptions, such as the object having two broken parts, the imaginary assembled shape being obtainable in advance, and the robot needing to follow the alignment and assembly process. This means that the framework may work well in this specific task, perhaps benefiting from pre-set assumptions, but it may not generalize to other scenarios, such as a cup breaking into several pieces.

2. I believe that the performance of this framework is affected by the quality of the imaginary assembled shape, which may be more difficult to achieve than the subsequent processes. Discussing this aspect would be helpful for this paper.

3. Although the results show that the performance of this framework surpasses previous methods, they are not good enough (only an average of 24). Moreover, there are no quantitative experimental results available for real-world experiments.

### Questions
See Weaknesses.

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
This paper presents a method for dual-arm manipulation to attach two separated objects from one object on the separated surface. This method divides the manipulation procedure into pick-up, alignment, and assembly as subtasks. The affordance network gives the grasp poses, considering the alignment and assembly. The VN-DGCNN, cVAE, and PointNet++ generate the input of the affordance network from the observed point cloud. The proposed method outperformed other baselines in the experiments.

### Strengths
- The paper presents a novel manipulation learning problem using shape assembly tasks in computer vision.
- The paper proposed a manipulation learning framework to solve robotic shape assembly tasks.
- The paper tackles a challenging task: the dual-arm robot should accurately control the object's pose from the observed point cloud.

### Weaknesses
 - The paper claims that geometric assemblies can be used in practical applications. However, it needs to explain which application robotic geometric assemblies are used in. It is better to highlight the academic significance of the robotic geometric assemblies. This reviewer recommends the authors provide specific examples of potential real-world applications for robotic geometric assemblies and elaborate on how this work advances the field theoretically or methodologically, highlighting its academic contributions.
- The success ratio of the proposed method is 24.10 %. It looks low. Humans may be able to perform the task at 100 %. The task may be extremely challenging unlike 2D pushing tasks and pick and place.
- Robotic parts assembly includes peg insertion, furniture assembly, and geometry assembly. The paper lacks an explanation of the robotic geometry assembly in the robotic manipulation tasks. The reviewer recommends the paper include a brief comparison of different types of robotic assembly tasks, highlighting how geometric assembly differs from or relates to other assembly tasks like peg insertion or furniture assembly. This would help readers better understand the unique challenges and contributions of this work.

### Questions
- Why is the success ratio low? Is the task too challenging? Which component did fail, such as grasp planning and object recognition?  This reviewer recommends the authors provide a breakdown of failure modes or an ablation study showing the performance of individual components. This would help pinpoint where the main challenges lie and guide future improvements.
- Which application can the robotic geometric assembly be used in? 
- Did the affordance network output the grasp action stably? Or did it sometimes fail? Are there any metrics related to the stability of the affordance network's outputs, such as the variance in grasp predictions across multiple runs? The reviewer recommends the authors provide a more detailed error analysis for the affordance network specifically, which would give readers a better understanding of its performance and limitations.

### Soundness
3

### Presentation
3

### Contribution
2
