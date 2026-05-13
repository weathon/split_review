# CONSTRAINT-AWARE ZERO-SHOT VISION-LANGUAGE NAVIGATION IN CONTINUOUS ENVIRONMENTS

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
We present Constraint-Aware Navigator (CA-Nav), a zero-shot approach for Vision-Language Navigation in Continuous Environments (VLN-CE).
CA-Nav reframes the zero-shot VLN-CE task as a sequential constraint-aware sub-instruction completion process, continuously translating sub-instructions into navigation plans via a cross-modal value map. 
Central to our approach are two modules namely Constraint-aware Sub-instruction Manager (CSM) and Constraint-aware Value Mapper (CVM).
CSM defines the completion criteria of decomposed sub-instructions as constraints and tracks navigation progress by switching sub-instructions in a constraint-aware manner.
Based on the constraints identified
by CSM, CVM builds a value map on-the-fly and refines it using superpixel clustering to enhance navigation stability.
CA-Nav achieves the state-of-the-art performance on two VLN-CE benchmarks, surpassing the compared best method by 12\% on R2R-CE and 13\% on RxR-CE in terms of Success Rate on the validation unseen split.
Furthermore, CA-Nav demonstrates its effectiveness in real-world robot deployments across diverse indoor scenes and instructions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an LLM based approach for vision and language navigation in continuous environments. The major ideas are two folds: 1. they proposes an LLM-based constraint aware sub-instruction manager which decomposes instructions into location aware direction aware and object aware instructions. Second steps is performed online during navigation i.e. which builds a value map based on the landmark information from first step and segments that into regions. It then selects the most-optimal waypoints by switching to the most relevant sub-instruction.

### Strengths
In my opinion, below are the strengths of this paper:

1. Constraints based value map construction idea is promising and offers interpretability.

2. The paper compares to various relevant baselines and shows real world qualitative evaluation results which shows the method can generalize to real-world setting. 

4. The paper's presentation is clear, it's nicely written and easy to follow. It also shows a nice gap in zero-shot vision-and-language navigation showcasing it is a promising avenue for future research.

### Weaknesses
In my opinion, below are the main weakness of the paper:

1. From Table 1. the results are only slightly better than other zero-shot VLN based approaches, especially for the SPL metric. Can the author discuss this result more?

2. It seems like a heavily engineered approach. Appreciate the authors for including the ablations but it is still not clear if there is one major component that affects the results for the approach. Most of the ablated components (while do impact SR, largely remains the same for SPL and NE).

3. I am wondering if the authors took into account calls to BLIP-2 as well as Grounding-DINO in their inference time calculation i.e. Figure-4? since those would also impact the inference time.

### Questions
Please see my questions in the weakness section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents CA-Nav, a zero-shot method for Vision-Language Navigation in Continuous Environments (VLN-CE). It reframes VLN-CE as a sequential sub-instruction process, leveraging two modules: the Constraint-aware Sub-instruction Manager (CSM) and the Constraint-aware Value Mapper (CVM). CSM divides instructions into sub-instructions and tracks progress, while CVM builds value maps to enhance navigation stability. CA-Nav achieves sota results on R2R-CE and RxR-CE, and proves effective in real-world robot deployments.

### Strengths
1. The use of the Constraint-aware Sub-instruction Manager (CSM) to decompose instructions and generate constraints for landmarks, locations, or directions, and switch sub-instructions based on these constraints is an effective and simple mechanism that enhances the robustness of the navigation process.
2. Unlike simple map construction, the paper introduces the Constraint-aware Value Mapper (CVM), which calculates the similarity to constrained landmarks.
3. Performance: The method achieves state-of-the-art results on the R2R-CE and RxR-CE datasets, surpassing other methods in terms of success rate and success weighted by trajectory length (SPL). The paper also mentions that CA-Nav delivers 10x faster response times and 95% cost reduction compared to other approaches, which is crucial for real-world applications.
4. Real-world Application Potential: Tests in real-world robot deployments show that CA-Nav generalizes well across different environments and instructions, demonstrating its potential for practical use.

### Weaknesses
1. Lack of innovation: The CSM aims to leverage LLMs for instruction decomposition and track navigation progress through explicit sub-instruction switching, while the CVM constructs a constraint-based value map. However, these are existing approaches, including map building, value map, progress tracking, mileage information, landmarks, objects, and directions. The use of LLMs for decomposition and constraint extraction seems insufficient as a major point of innovation. The novelty of combining these existing components is not clearly articulated, and the specific way in which the LLM is used for decomposition lacks sufficient detail to assess its contribution beyond standard LLM applications.

2. Limited benchmark scope: Although the paper performs well on two VLN-CE benchmark datasets, its generalization ability is unclear. It is recommended to evaluate the method on more diverse datasets or different embodied tasks to further verify its general applicability. The current benchmarks, R2R-CE and RxR-CE, primarily focus on indoor navigation. Testing on more complex environments, such as outdoor or mixed indoor-outdoor settings, would provide a more robust evaluation of the method's generalization capabilities.

3. Lack of detail in instruction decomposition: Instruction decomposition is a key part of the system, but the paper does not provide enough details about the robustness of this process across different types of instructions. While the authors mention using a large language model (LLM), the handling of complex instructions has not been fully explored. The paper should include a more detailed analysis of how the LLM handles instructions with varying levels of complexity, including those with nested conditions or ambiguous references. The absence of a quantitative analysis of the decomposition process makes it difficult to assess the reliability of this crucial step.

4. Over-reliance on constraints: Although the constraint-aware approach is innovative, over-reliance on constraints in some cases may lead to suboptimal behavior. For example, if the robot incorrectly detects a landmark or misinterprets a constraint, it might switch sub-instructions prematurely or delay switching. The paper does not delve into failure cases or limitations of the method. The paper should discuss how the system handles noisy or ambiguous sensor data that could lead to incorrect constraint detection and subsequent navigation errors. A more thorough analysis of the system's robustness to such errors is needed.

5. Lack of some ablation studies: Despite strong experimental results, there is a lack of ablation studies to analyze the contribution of each module. For example, the impact of CSM, CVM, and superpixel clustering on overall performance has not been thoroughly analyzed. Such studies would help better understand the importance of each module. Specifically, the paper should include ablation studies that isolate the impact of each component, such as the CSM without the CVM, the CVM without superpixel clustering, and the system without the historical decay mechanism. This would provide a clearer understanding of the contribution of each component to the overall performance.

### Questions
1. Difference from VLFM: VLFM uses value mapping to identify the most promising boundaries for exploration to locate instances of a given target object class, and these mappings can be constructed in real time. In contrast, CA-Nav relies on a complete value mapping and subgoal switching mechanism.  Other than these aspects, there do not seem to be significant differences between CA-Nav and VLFM. 
2. Details and robustness of instruction decomposition:
You mentioned using a large language model (LLM) to decompose instructions and generate constraints for sub-instructions (e.g. landmarks, locations, directions, etc.). However, the paper does not explain in detail how LLM handles complex or ambiguous instructions. When faced with complex instructions (such as instructions that contain multiple actions or involve multiple constraints simultaneously), how does the system ensure the accuracy of sub-instruction decomposition? Is there a mechanism to handle possible decomposition errors? Can the decomposition process be quantitatively assessed? For example, testing instructions of different complexity for accuracy or robustness.
3. Timing selection for CSM neutron command switching:
The paper mentions that the constraint-aware subcommand manager (CSM) switches subcommands by evaluating the completion of the current constraints. How does CSM determine that a certain sub-instruction has been "completely" completed without switching to the next sub-instruction too early or too late? Does the system have some kind of buffering mechanism to avoid premature switching? Have you considered possible dependencies between subdirectives? Can you share more details about the subcommand switching strategy? For example, how to avoid premature or delayed switching? Have you evaluated the impact of incorrect switching on the overall path planning?
4. The role of CVM’s constraint value map construction and superpixel clustering:
Constraint-aware value mapper (CVM) builds value maps through superpixel clustering to enhance navigation stability. What exactly does superpixel clustering play here? Are there any actual comparative tests to prove that the addition of superpixel clustering brings significant performance improvements? How does CVM perform without superpixel clustering? Can ablation experiments be provided to demonstrate the impact of superpixel clustering on navigation stability and path planning? Furthermore, have other clustering algorithms or image segmentation techniques been considered as an alternative to superpixel clustering?
5. Error recovery mechanism in constraint detection:
The constraint-aware navigation process relies on constraints on landmarks, locations, and directions, and detection errors of these constraints may lead to navigation failure. If a robot detects a landmark incorrectly or fails to recognize constraints correctly, can the system automatically recover? Are there mechanisms in place to handle cases of false detections or incorrect constraint recognition? For example, how to ensure that navigation continues when the robot fails to correctly identify landmarks in the environment? Can you provide more details on the error detection recovery mechanism? For example, when a detection error occurs, does the system re-evaluate the current state or correct it through other visual cues.
6. Generalize to diverse environments and dynamic constraint changes:
Although the method performs well on the R2R-CE and RxR-CE datasets, the environmental diversity of these datasets is relatively limited. Do you plan to test performance in more diverse and dynamic environments? For example, will the challenges that robots need to deal with in dynamic environments (such as landmark occlusion, environmental changes) affect the accuracy of constraint detection? Can you provide more experimental results on dynamic environments? For example, when the environment changes (such as tables and chairs moving or roadblocks appearing), will the agent re-build a value map based on new observations, dynamically adjust constraints or re-evaluate the current navigation goal.

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
This paper addresses the challenging task of Vision-Language Navigation in Continuous Environments (VLN-CE). The task presents two main challenges: 1) Continuous Environments large state space 2) requires an understanding of visual observation details that are hard to summarize by language alone. 

The key idea is to perform the Constraint-aware Sub-instruction Manager (CSM) and define the completion criteria of decomposed sub-instructions as constraints, and track navigation progress. Then, the Constraintaware Value Mapper (CVM) builds a value map that is continually updated using a constraint prompt and semantic map.

### Strengths
The overall idea of using a pre-trained vision language model for navigation has been extensively studied in the recent literature. However, this paper's approach seems well thought out. The constraint formulation (direction, object, and location), while straightforward, does make sense and seems effective in breaking down complex navigation tasks. 

The superpixel clustering method for waypoint selection is a smart way to handle noisy and high dimensional value maps and allows continuous action space.  

I like that the comprehensive ablation studies validate all key design decisions. 

I also like the fact that the author provides real-world navigation results on real robots.

### Weaknesses
I'm not actively working in this field, and it is a bit hard for me to judge the technical novelty of the method. 
However, the high-level ideas seem standard, despite the naming differences: It contains high-level planning (called CSM in the paper) and low-level policy (called CVM in the paper). Using constraints in high-level planning and using them to inform low-level policy is also a typical approach for task and motion planning, but this time with VLM and LLM to better handle unstructured images.  Reading the paper method seems to be a straightforward combination of existing models. The majority of the performance improvement probably comes from the pre-trained models.

The performance seems a bit low (25% success rate in HM3D, despite already being higher than some of the baselines compared to). It seems that the system is not working most of the time. This makes me think? 1) What are the common failure cases? 2) Is the task naturally ambiguous or ill-defined? Can humans do this task with the same observation space?

### Questions
Question to the author: 

- Is LLM really needed here? The construction of the constraints based on instruction seems a pretty structured task; a simple rule-based method or small language model could work just fine. 

- The performance seems a bit low (25% success rate in HM3D, despite already being higher than some of the baselines compared to). It seems that the system is not working most of the time. This makes me think? 1) What are the common failure cases? 2) Is the task naturally ambiguous or ill-defined? Can humans do this task with the same observation space?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an LLM-based visual navigation agent CA-Nav, which is composed mainly of three parts - CSM, CVM, and Waypoint Selection Module. The CSM is a task-level planning module that decomposes the language instructions into sub-instructions.  Based on the sub-instructions, the CVM assigns the affordance values on the map, and finally, the Waypoint Selection Module translates the value maps into a collision-free navigation trajectory.  Foundation models such as GroundingDINO, SAM, and BLIP2 are used to provide a comprehensive environment perception. The proposed approach is fairly evaluated in the VLN-CE tasks, including both R2R-CE and RxR-CE, and achieves better performance with several zero-shot VLN-CE baseline methods. Real-world experiments are also conducted to support the effectiveness of the proposed method.

### Strengths
(1) This paper proposes a zero-shot LLM Agent for visual-language navigation in a continuous environment. Both the simulation results and the real-world videos prove the effectiveness of the proposed approach.

(2) This paper proposes a novel Superpixel-based Waypoint Selection module, which is able to deal with the inconsistency values in generating the value maps and generates a smoother navigation trajectory.

(3) The detailed ablation study and analysis help understand the function of each proposed approach.

(4) The real-world deployment shows the potential of the proposed approach.

### Weaknesses
(1) The technique contribution is limited. Using the LLM to decompose long-horizon navigation tasks into sub-instructions has been proposed in the work InstructNav[1], which also uses landmark, action as constraints for sub-tasks. Using BLIP-2 for generating the value map has been proposed in the paper VLFM[2]. It seems that the only difference is that VLFM uses the object goal as the language query but CA-Nav uses a decomposed instruction as the query.

(2) The overall performance on the VLN-CE benchmarks is not satisfying. The CA-Nav only got ~25% success rate which is relative lower than the recent LLM-based approaches such as InstructNav and Navid[3].

(3) The system is rather complicated and introduces multiple foundation models during the decision process, including . The decision frequency/speed is an important issue for robotics applications.

### Questions
(1) As mentioned in Section 3.2, there are three types of constraints including landmark, location, and action. Only when the constraints are satisfied or exceed the time limit, the next sub-instructions will be used for the next decision. However, it seems that in the subsequent steps such as value map generation and path planning, there are no explicit schemes to guarantee the navigation process will fulfill the constraints. The constraint attributes are only used for querying the BLIP-2. Does the BLIP-2 score enough to finish the sub-tasks and walk a perfect trajectory to solve all the constraints?

(2) There are clear pre-defined rules for deciding whether the sub-instructions are finished. But what if your agent mistakenly arrives at a proper next waypoint without satisfying the first sub-instructions, should it go back and try to complete the first step or directly skip the first and continue for the rest of the sub-tasks? Is there a more flexible framework for such scenarios in your method?

(3) How long does it take for the whole round of the planning process, including semantic mapping, generating sub-instructions, value maps, and path planning?

(4) Why does the success rate vary for the same instruction and same starting positions shown in the supplementary Table 7? What influences the performance and makes the approach sometimes can finish the task and sometimes can not.

### Soundness
3

### Presentation
3

### Contribution
1
