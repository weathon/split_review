# EnvBridge: Bridging Diverse Environments with Cross-Environment Knowledge Transfer for Embodied AI

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
In recent years, Large Language Models (LLMs) have demonstrated high reasoning capabilities, drawing attention for their applications as agents in various decision-making processes. One notably promising application of LLM agents is robotic manipulation. Recent research has shown that LLMs can generate text planning or control code for robots, providing substantial flexibility and interaction capabilities.
However, these methods still face challenges in terms of flexibility and applicability across different environments, limiting their ability to adapt autonomously. Current approaches typically fall into two categories: those relying on environment-specific policy training, which restricts their transferability, and those generating code actions based on fixed prompts, which leads to diminished performance when confronted with new environments. These limitations significantly constrain the generalizability of agents in robotic manipulation.
To address these limitations, we propose a novel method called EnvBridge. This approach involves the retention and transfer of successful robot control codes from source environments to target environments. EnvBridge enhances the agent's adaptability and performance across diverse settings by leveraging insights from multiple environments. Notably, our approach alleviates environmental constraints, offering a more flexible and generalizable solution for robotic manipulation tasks.
We validated the effectiveness of our method using robotic manipulation benchmarks: RLBench, MetaWorld, and CALVIN. Our experiments demonstrate that LLM agents can successfully leverage diverse knowledge sources to solve complex tasks. Consequently, our approach significantly enhances the adaptability and robustness of robotic manipulation agents in planning across diverse environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents EnvBridge, a novel approach for computing robot trajectories via LLM-prompted code generation. The authors argue that transferring code across different environments, similar to human reasoning, can improve the success rate of task completion. EnvBridge extends existing methods like VoxPoser by adding a knowledge transfer mechanism to bridge across environments.

This process leverages a hierarchical code generation approach, dividing the task into subtasks (Planner) and generating 'language model programs' (LMPs) for each subtask (Composer). These LMPs produce value maps that guide the generation of an open-loop trajectory. I believe this trajectory is for the end-effector pose.

The system operates in several stages. First, an LLM generates code that outputs a trajectory, based on a language query describing the task. This is the same as VoxPoser. If unsuccessful, EnvBridge searches a repository for similar tasks where code generation failed at the same stage (Planner or Composer). Successful code from a similar task is then transferred to the target environment and used as an example in a revised prompt for the LLM, known as Knowledge Transfer and Re-planning.

### Strengths
The primary strength lies in its novel approach to knowledge transfer for robot code generation via appropriate prompt engineering. The idea is well-motivated by observations of human behavior and offers a promising direction for improving LLM performance in robotics. The paper is generally well-written and presents the approach with clarity. Furthermore, the authors conduct extensive experiments across multiple tasks and environments in simulation, demonstrating the effectiveness of EnvBridge.

### Weaknesses
1. EnvBridge generates open-loop trajectories, lacking the reactivity necessary for dynamic environments.
2. To my understanding, the system focuses solely on end-effector positions, neglecting possible collisions of the robot arm with the environment.
3. The user must explicitly provide information about objects to avoid in the scene, which could be automated through prompt engineering. For example, in the example memory shown in section A.3, the task is to "pick up the rubbish and leave it in the trash can.", and there are a bunch of objects given. The Planner level should create subtasks to avoid other objects (e.g. 'tomato1') while picking up the object named 'rubbish'.
4. The evaluation could be strengthened by comparing EnvBridge to other baselines like OpenVLA, which also generates end-effector poses from similar inputs.
5. The authors should provide further clarification regarding the performance discrepancies observed in Figure 2, where code from the same environment (RLBench) performs worse than transferred code from a different environment (CALVIN) - even though RLBench memory has more code examples than those in CALVIN. 
6. It would be good to have real-robot experiments, to improve the case for accepting any robotics paper.

Finally, to best understand the work, you need to see the prompts given in the appendix, and the type of prompt engineering used for each stage of EnvBridge. While this is not explicitly a weakness, these are important details worthy of being in the main paper.

A possible typo on line 57: "transfer ability" should likely be "transferability"??
Throughout the paper (e.g., line 694), the authors should explicitly clarify that curly braces in the prompts `{}` denote variables to be filled in.

### Questions
See above

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes EnvBridge, an LLM-based method that can leverage diverse knowledge to solve complex tasks. It contains several components to endow the agents with good generalization ability.

### Strengths
The proposed methods are evaluated on 3 benchmarks.

### Weaknesses
 - The Introduction section includes many discussions not related to LLMs for robotic manipulation, which appears redundant.

- The writing of the article is not very clear; concepts such as cross-embodiment and cross-environment need to be more distinctly defined. This significantly detracts from the overall logic of the paper.

- The quality of the figures in the paper is poor.

- I do not agree with the author's assertion that current LLM-based methods have significant generalization issues. Many LLM-based approaches have demonstrated strong generalization abilities in real-world applications. I also do not believe that the method proposed by the author addresses the existing issues effectively.

- I believe that this paper is not yet ready for submission to ICLR.

### Questions
Seen above.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces ENVBRIDGE, a method that leverages Large Language Models (LLMs) for cross-environment knowledge transfer in robotic manipulation. The core idea is to use the control code from source environments as prompts to generate suitable control actions in new target environments. The proposed approach is tested across three common robotic manipulation benchmarks: RLBench, MetaWorld, and CALVIN.

### Strengths
1. The use of LLMs for cross-environment task transfer is a creative and intriguing approach. I especially like the method of using previously successful control code as in-context prompts for generating control code in new tasks.
2. The experiments are conducted across three well-established manipulation benchmarks.

### Weaknesses
1. My primary concern is the practical applicability of the method. Why should we rely on LLMs to generate control code for simulated environments, and how feasible is it to extend this approach to real-world robotic systems? As far as I understand, the method depends on ground-truth states and simulation-specific API calls, which may not easily translate to real-world scenarios where such information is not readily available. Specifically, the reliance on precise, ground-truth state information, which is not accessible in real-world settings, severely limits the method's direct applicability. The paper does not address how noisy sensor data or partial observability would affect the performance of the LLM-generated control code.
2. Certain aspects of the experimental setup are not clearly explained. I have raised specific questions about this below.

### Questions
1. Could the authors clarify whether the method uses ground-truth states as input or camera inputs for perception?
2. The experimental protocol in Section 4.1 is somewhat ambiguous. In lines 340–341, the paper mentions “We sampled 10 tasks from it and conduct evaluations covering various tasks, instructions, and objects.” Does this imply different variations were introduced within these 10 tasks? More explanation would help.
3. In Section 4.2, why didn’t the authors use CALVIN as a source task, similar to the approach in Section 4.1?
4. In Section 4.3, what were the source tasks used for this experiment? Were they drawn from RLBench and MetaWorld?
5. The paper only compares ENVBRIDGE with VoxPoser, yet there are other related works that also utilize LLMs for generating robot control code. How does ENVBRIDGE compare to methods like Code as Policies?
6. Some minor formatting issues exist in the paper, such as mismatched quotation marks in lines 192 and 193.

### Soundness
2

### Presentation
3

### Contribution
2
