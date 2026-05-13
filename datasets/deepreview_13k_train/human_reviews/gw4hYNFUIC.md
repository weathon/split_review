# S3E: Semantic Symbolic State Estimation With Vision-Language Foundation Models

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
In automated task planning, state estimation is the process of translating an agent's sensor input into a high-level task state. It is important because real-world environments are unpredictable, and actions often do not lead to expected outcomes. State estimation enables the agent to manage uncertainties, adjust its plans, and make more informed decisions. Traditionally, researchers and practitioners relied on hand-crafted and hard-coded state estimation functions to determine the abstract state defined in the task domain. Recent advancements in Vision Language Models (VLMs) enable autonomous retrieval of semantic information from visual input. We present Semantic Symbolic State Estimation (S3E), the first general-purpose symbolic state estimator based on VLMs that can be applied in various settings without specialized coding or additional exploration. S3E takes advantage of the foundation model's internal world model and semantic understanding to assess the likelihood of certain symbolic components of the environment's state. We analyze S3E as a multi-label classifier, reveal different kinds of uncertainties that arise when using it, and show how they can be mitigated using natural language and targeted environment design. We show that S3E can achieve over 90\% state estimation precision in our simulated and real-world robot experiments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the use of pre-trained VLM to classify symbolic states. Specifically, a symbolic predicate is first converted to language instruction and is then fed to a VLM together with the image; the token probabilities of the "yes" and "no" answers are used to determine the probability of the predicate state being true. The paper proposes to deal with two types of uncertainties that arise from partial observation and ambiguities in the definitions of the symbolic predicate. To combat this first type of uncertainty, the authors propose manipulating and moving the occluded objects to be in direct sight. For the second type of uncertainty, the authors propose to provide clearifying instructions.

### Strengths
Traditional methods for classifying symbolic states usually need to be manually designed by domain experts or trained with a large amount of data. This paper investigates using pre-trained VLMs to classify states in zero-shot. This approach can potentially improve the generalizability of task-planning methods.

### Weaknesses
1. It's unclear how the system automatically determines that there is uncertainty in the prediction, which then needs to be addressed by asking for clarifying instructions or better camera views.
2. The predicates this paper tests are limited to determining whether an object is on a specific table region or whether the object is in hand or in the air. These predicates probably can be determined using very simple heuristics based on gripper state or detected object bounding boxes. It's hard to assess whether the method can reliably classify more diverse predicates for real-world robotic tasks. I suggest the authors to look at other photo-realistic simulation environments that provide annotated object states.
3. Even though the authors motivate the paper for task planning, there is no evaluation of the method integrated with a task planning framework. It's unclear how the improvement in classification performance translates to the improvement in overall task success.
4. In line 176, the authors mention that the assumption is unrealistic. However, I think this assumption is valid if the action sequences are correct (e.g., if the robots are being teleoperated by a human user)
5. In general, the writing of the paper can also be improved. I found the discussion on uncertainty and experiment section a little confusing.

### Questions
I hope the authors can address my concerns above. I don't have additional questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces S3E, a novel approach that uses vision-language foundation models for automated state estimation in robotic task planning. While traditional approaches require hand-crafted state estimation functions for each task, S3E offers a zero-shot solution that translates symbolic predicates into natural language questions, uses vision-language models to answer these questions from visual input, and converts the answers back into symbolic states. The system's effectiveness is validated through experiments in grocery sorting tasks and photorealistic blocksworld domains, particularly when employing uncertainty mitigation strategies through natural language instruction and environment design.

### Strengths
The key strength of this paper lies in its practical approach to solving a significant challenge in robotics - automated state estimation. The authors present a solution that eliminates the need for hand-crafted state estimators, traditionally a major bottleneck in deploying robotic systems across different tasks. The authors propose an approach that bridges symbolic task planning with modern vision-language models through natural language as an intermediate representation. They provide practical mitigation strategies through natural language instruction and environment design, demonstrating strong empirical results with over 90% precision.

### Weaknesses
There are some major problems that concerns me:
1. While S3E is presented as a zero-shot solution, it still requires significant assumptions about the environment, including full observability, visually distinguishable objects, and unambiguous domain descriptions - constraints that may not hold in many real-world applications. The reliance on full observability, for instance, limits its applicability in scenarios with occlusions or sensor limitations. Furthermore, the requirement for visually distinguishable objects means that the system may struggle with objects that have similar appearances or are poorly lit. The need for unambiguous domain descriptions also poses a challenge, as real-world scenarios often involve inherent ambiguities that are difficult to capture in a formal description.

2. The experiments, while showing promising results, are limited to relatively controlled environments and simple manipulation tasks. The evaluation could be strengthened by exploring more challenging scenarios such as partial observability conditions, dynamic environments, or multi-agent interactions. This would help better understand the method's full potential. The current experiments do not adequately address the robustness of the system in the face of unexpected events or changes in the environment. For example, the system's performance in a cluttered environment or with objects that are not part of the training set remains unclear.

3. The paper's handling of uncertainty, while acknowledged, could be more rigorous - the proposed mitigation strategies of environment design and natural language instruction essentially sidestep rather than solve the underlying uncertainty challenges. Additionally, the method's heavy dependence on the quality of the vision-language model's training data suggests potential brittleness when encountering out-of-distribution scenarios, as evidenced by the poor performance with certain objects in the simulated environment. The reliance on natural language instruction for uncertainty mitigation, while practical, does not address the fundamental issue of the VLM's inherent uncertainty in interpreting visual inputs. The system's performance could degrade significantly if the VLM encounters visual inputs that are substantially different from its training data.

### Questions
1. Have you explored any cases where the domain descriptions contain partial or ambiguous information? What were the results?
2. Were there any failure cases in the controlled environments that could provide insights into the system's limitations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the problem of estimating the truth values of symbolic state predicates, which is essential for PDDL-style planning. While prior works has performed state estimation in a task-specific setting, the proposed approaches uses foundation models as universal estimator that can be conditioned on the task through prompts. First, natural language question is created for every for every possible grounded predicates in the given domain. The translated question along with the image is passed to a VQA model (a VLM) to get the truth value of the predicate. The evaluation is done on a table top manipulation environment which is fully observable and uncluttered, which shows that the proposed method can ground the symbolic predicates across different domain/tasks.

### Strengths
- The paper attempts to address an important problem for semantic state estimation. 
- The consideration of both the predicates and their uncertainty is a promising direction. 
- The evaluation is at a task level showing utility of the approach for realistic applications.

### Weaknesses
 - The proposed approach of determining the validity of predicates with VQA addresses only a part of the problem of estimating the symbolic state. The proposed approach is restricted to simple predicates in small clutter free settings. Scalability to scenarios with complex object arrangements and to higher-order predicates is limited. 
- The problem of eliciting uncertainty from LLMs has received attention in the past. The authors are requested to highlight the technical gap they are filling in this regard. Please refer to works such as https://arxiv.org/pdf/2307.01928 and https://arxiv.org/pdf/2306.13063.
- The problem of inferring semantic properties of the robot's environment has also been addressed in works that extract a scene graph from raw sensor data. Please see Maggio et al. for an example (https://arxiv.org/abs/2404.13696). I request authors to situate their work along side such efforts.

### Questions
1. Scalability of exhaustive enumeration. The translation stage of each predicate query involves posing predicate truth value assessment as answer to a textual question. It appears from the text that this conversion is done for each predicate independently and exhaustively. However, there may be correlation in the predicates. If the robot is far away from the table then it is far away from all blocks on the table. Does the approach take advantage of such logical connections?

2. Agent-dependent predicates. Robot interaction tasks require predicates such as in_hand, robot_close_to etc. predicates. How is the agent morphology and other aspects communicated to the VLM for accurate estimation of these predicates.  

3. Higher order predicates. Often in task planning there is a need for higher order predicates. For example, consider a stack of blocks. One would need to reason about the top of the stack as different from a block at the base. See Pasula et al. (https://people.csail.mit.edu/lpk/papers/zpk.pdf) for an example of such predicate (topstack()). Such predicates requires higher order reasoning over the atomic properties that may hold in the scene. Does the proposed method address computation of such predicates. 

4. Baseline VLM performance for direct plan synthesis. The authors have taken the symbolic planning view where knowledge of state predicates is fundamental. Alternatively, what if one asks the VLM to directly synthesise robot actions for a given goal without explicitly querying for the predicates. It would be insightful to analyse this approach as a baseline.

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
4

### Summary
This paper proposed a state estimator that leverages Vision Language Models to translate sensor data into high-level task states. However, this paper provides limited technical contribution or insight, as it is a straightforward application of VLMs.

### Strengths
The paper is easy to understand. 

The method is evaluated with both simulation and real-world images.

### Weaknesses
This paper proposed a state estimator that leverages Vision Language Models to translate sensor data into high-level task states. However, this paper provides limited technical contribution or insight, as it is a straightforward application of VLMs.

This paper is a straightforward application of VLMs. There is already a lot of work in robotics using VLM for state estimation, and some use symbolic representation to work with existing task and motion planning algorithms. [1,2,3]. These existing works often with much more complicated scenarios and systems than the ones demonstrated in this work. I don't think this provides much new insight or knowledge. 

The paper does not provide sufficient discussion on related work.  

The scenarios tested are very simple: only simple rigid objects on a tabletop setting with simple spatial relationships. "state estimator" should provide significantly richer information than just simple object class and their spatial relations. 

The state estimation is not used or evaluated in realistic robotics tasks or systems. It only performs offline evaluation.

### Questions
The paper is clear, I don't think answering any question would significantly change my evaluation. I think here is a few questions to think about. 
1) how to extend the state estimation to more general scenarios, e.g., non-rigid object, where the object state is beyond the location and spatial relationship? 
 2) What are some existing works in robotics using VLM as state estimation? Summary their approach and limitations and see how the proposed work can address them.

### Soundness
2

### Presentation
2

### Contribution
1
