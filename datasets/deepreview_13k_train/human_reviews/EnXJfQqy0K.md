# Building Cooperative Embodied Agents Modularly with Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
In this work, we address challenging multi-agent cooperation problems with decentralized control, raw sensory observations, costly communication, and multi-objective tasks instantiated in various embodied environments. 
While previous research either presupposes a cost-free communication channel or relies on a centralized controller with shared observations, 
we harness the commonsense knowledge, reasoning ability, language comprehension, and text generation prowess of LLMs and seamlessly incorporate them into a cognitive-inspired modular framework that integrates with perception, memory, and execution. Thus building a \textbf{Co}operative \textbf{E}mbodied \textbf{L}anguage \textbf{A}gent \textit{CoELA}, who can plan, communicate, and cooperate with others to accomplish long-horizon tasks efficiently. 
Our experiments on C-WAH and TDW-MAT demonstrate that \textit{CoELA} driven by GPT-4 can surpass strong planning-based methods and exhibit emergent effective communication. 
Though current Open LMs like LLAMA-2 still underperform, we fine-tune a \textit{CoLLAMA} with data collected with our agents and show how they can achieve promising performance. 
We also conducted a user study for human-agent interaction and discovered that \textit{CoELA} communicating in natural language can earn more trust and cooperate more effectively with humans. 
Our research underscores the potential of LLMs for future research in multi-agent cooperation. Videos can be found on the project website \url{https://vis-www.cs.umass.edu/Co-LLM-Agents/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript presents a comprehensive study on constructing cooperative embodied agents using Large Language Models (LLMs), aiming to address multi-agent collaboration in decentralized settings with challenges like raw sensory observations, costly communication, and multi-objective tasks. The authors introduce CoELA, a Cooperative Embodied Language Agent, which integrates the LLMs' capabilities with a modular framework encompassing perception, memory, execution, communication, and planning. The system's performance is evaluated in two embodied environments: C-WAH and TDW-MAT, demonstrating its ability to outperform planning-based methods, particularly when driven by GPT-4. The use of natural language for agent communication is highlighted as a significant advantage, fostering trust and effectiveness in human-agent interactions.

### Strengths
**Robust Motivation:** The paper is grounded in a strong and compelling motivation to enhance agent collaboration in complex environments. By addressing the need for agents to effectively communicate and plan their actions in a coordinated manner, the authors establish a solid foundation for their research, showcasing a clear understanding of the challenges and opportunities in the field.

**Carefully Designed Pipeline:** The system architecture demonstrates a thoughtful and meticulous design, integrating multiple modules and dual language models to manage both communication and planning. This comprehensive approach ensures that each aspect of the agent's interaction is given due consideration, resulting in a pipeline that is both balanced and well-reasoned. The deliberate inclusion of separate models for different functions reflects the authors' dedication to creating a system that is tailored to meet the specific demands of agent collaboration.

**Thorough Analysis and Discussion:** The paper excels in providing an in-depth analysis and discussion of the results, helping readers to fully grasp the implications and nuances of the study. The authors do not shy away from addressing the limitations of their work, offering a balanced view that adds credibility to their findings. This level of detail ensures that the paper serves not only as a presentation of the proposed framework but also as a valuable resource for future research, encouraging further investigation and innovation in the field of agent collaboration.

### Weaknesses
 **Complex Model and System Design:** The architecture of the system is intricate, requiring each agent to manage five different modules and two distinct LLMs for handling communication and planning. This complexity can lead to instability in the LLM's performance, especially when processing lengthy textual inputs describing complicated scenarios. Furthermore, the challenge to maintain scalability becomes apparent as the addition of objects and details can potentially overwhelm the system, limiting its extendability. The intricate design also indirectly contributes to the limited utilization of spatial information and the difficulty in effective reasoning over low-level actions, as these scenarios would require even longer prompts. Specifically, the reliance on textual descriptions of the environment, rather than direct spatial reasoning, means that the system may struggle with tasks requiring precise manipulation or navigation in cluttered environments. The need to encode all relevant spatial information into text for the LLM to process introduces a bottleneck, potentially leading to inaccuracies and inefficiencies.

**Effectiveness of Communication:** The effectiveness of communication within the system seems to be suboptimal according to the ablation study. Therefore, a natural question is whether there is a possible improvement for the communication module. Personally, I am interested in the issues in Figure 5a. I am curious if Alice misinterprets Bob's actions due to an incorrect perception or what. Will bi-directed communication, such as Alice asking Bob if he has placed the object in the container when she needs to know, plus Bob telling Alice what he is doing at the beginning and the end of one mission, might serve as a straightforward solution to the problems, highlighting the need for a more responsive and interactive communication system. The current communication protocol appears to be primarily one-way, with agents broadcasting their intentions or observations but not actively engaging in dialogues to clarify ambiguities or confirm shared understanding. This limitation could lead to misinterpretations and coordination failures, especially in complex scenarios where the agents' actions are interdependent.

### Questions
1. How to evaluate the communication cost? Is there any tradeoff study on communication cost and effectiveness?
2. How does the system perform in scenarios with an increased number of objects and more complex interactions, and what measures are in place to maintain scalability?
3. For turning left/right, what will happen if the object in interest is on the back of the agent? How is the visual-related textual input organized? Did the work try to use the oracle information of the whole environment, including objects and relations?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an innovative approach to address multi-agent cooperation challenges in decentralized settings with costly communication and raw sensory observations. The authors introduce a modular framework integrating Large Language Models (LLMs), resulting in the Cooperative Embodied Language Agent (CoELA), capable of efficient planning, communication, and cooperation.

### Strengths
1. The paper introduces a unique integration of Large Language Models within a modular framework for decentralized multi-agent cooperation, addressing practical challenges in varied embodied environments.
2. Robust empirical support is provided through comprehensive experiments and a user study, showcasing the effectiveness of the approach and its positive impact on human-agent cooperation.
3. The paper is well-articulated and structured, offering clear insights and setting a strong foundation for future research in multi-agent cooperation with embodied agents.

### Weaknesses
1. This method assumes a skill library that is manually defined for a specific domain, i.e. execution module. However, this limits its applicability in other domains where predefined skill libraries are not available. Specifically, the reliance on motion planning as a source for low-level skills restricts the generalizability of the approach to environments where such planning is not readily available or computationally feasible. The paper does not address how the system would adapt to novel environments requiring different types of low-level control.

2. The pipeline appears to be quite complex and relies on several hand-defined modules, including perception modules, three memory modules, planning, and execution. Are all of these modules necessary? Conducting an ablation study would provide better understanding. The interactions and dependencies between these modules are not clearly explained, making it difficult to assess the necessity of each component. For instance, the specific roles of the three memory modules and their individual contributions to the overall performance are unclear. A more detailed breakdown of the information flow and module interactions is needed.

3. The experimental design lacks breadth as it only considers one scenario. Including evaluations across multiple scenarios would strengthen the findings. The evaluation is limited to a single rearrangement task, which may not fully capture the challenges of multi-agent cooperation in diverse settings. The paper should include experiments in different environments with varying complexities, such as different object types, agent configurations, and task goals, to demonstrate the robustness of the proposed approach.

4. There is some ambiguity regarding the execution module, memory module, and perception module details. Were they all designed by humans using language-based approaches? The paper lacks sufficient detail on the implementation of these modules, particularly the perception module. It is unclear how the Mask-RCNN is integrated with depth information to create the 3D voxel semantic map, and the specific parameters and training data used for this process are not provided. Similarly, the A-star based planner in the execution module is not described in sufficient detail, making it difficult to reproduce the results.

### Questions
See in weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a modular framework that integrates the Large Language Models to build Cooperative Embodied Language Agents CoELA, which focuses on the multi-agent setting with decentralized control, complex partial observation, costly communication and multi-objective tasks. Empirical experiments on C-WAH and TDW-MAT show that CoELA can achieve promising cooperative performance. Additional experiments with real humans demonstrate that CoELA can earn more trust and cooperate more effectively with humans.

### Strengths
1. This work proposes one feasible approach to building embodied agents with Large Language Models which seems to be sound. This demonstrates the prosiming potential of LLMs to build cooperative embodied agents and inspires future research well.
2. The experimental setup is relatively comprehensive, including cooperative evaluation  with AI agents and real humans. Besides, the discussion of the experimental results is also very interesting and thorough.
3. The discussions about failure cases and limitations are appreciated.

### Weaknesses
1. Despite the fact that the structure of the manuscript is organized well, the description of the method is relatively brief, with some details not sufficiently elaborated. For example, the manuscript states that, for the execution module, CoELA will utilize the procedure stored in its Memory Module to execute the high-level plan. However, it is unclear what form these procedures take and how they are obtained for a specific environment. Specifically, the description lacks detail on the exact mechanisms for translating high-level plans into executable actions within the environment. Are these procedures pre-defined scripts, learned policies, or something else? The paper does not provide sufficient detail on the representation and implementation of these procedures, making it difficult to assess the practical feasibility and generality of the approach.
2. If I'm not mistaken, given a specific environment, CoELA needs to manually design/list the possible high-level plans, which may be a relatively tedious workload. Similar issues may arise when determining the possible high-level plans on each state and defining the procedure for each plan. This significantly influences the generality of the method and it may be challenging to implement these manual work in complex problems. Besides, listing the possible plans may significantly increase the prompt length, which might influence the performance. The process of manually defining high-level plans and their corresponding procedures seems to be a significant bottleneck in the proposed framework. The lack of an automated or semi-automated approach for this step limits the scalability and applicability of CoELA to more complex and dynamic environments. The paper does not discuss the potential impact of this manual effort on the overall performance and robustness of the system.
3. The baselines in the experiments are relatively simple and heuristic. More baselines, especially methods designed for embodied agents, are recommended. The current baselines do not provide a strong comparison point to demonstrate the effectiveness of the proposed method. It is essential to compare CoELA against state-of-the-art approaches in embodied agent research to properly evaluate its performance and contribution. The paper should include comparisons to established methods that address similar challenges in multi-agent cooperation and embodied interaction.

### Questions
1. How does CoELA determine the valid high-level plans at each state? Is it determined manually?
2. Have there been previous works using LLM for implementing embodied agents? Can more discussion or even experimental comparisons be made with these works? What are the core contributions and innovations of CoELA compared to them?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a framework called Cooperative Embodied Language Agent (CoELA), which explores the potential of Large Language Models (LLMs) for multi-agent communication. The framework is composed of five modules, among which the communication module helps the agent cooperate more effectively than traditional methods. Experiments conducted on TDW-MAT and C-WAH have demonstrated the effectiveness of CoELA when compared to strong planning-based methods, showcasing effective communication. Furthermore, the authors also explore the potential of using open LMs as LLMs, which is an impressive aspect of their work.

### Strengths
1. The comprehensive experiments demonstrate that the proposed method can efficiently cooperate with other agents, which is very impressive.
2. The presentation is clear.

### Weaknesses
1. Details regarding how CoELA cooperates with other agents are lacking. Sections 4 and 5 do not mention the mechanisms for cooperation between agents, such as how one MHP cooperates with another MHP or with CoELA. Specifically, it is unclear how the agents' internal states are shared or if they are even explicitly represented during the cooperative process. The paper would benefit from a more detailed explanation of the information exchange, if any, between agents. It remains unclear if the agents are simply reacting to the environment or actively coordinating their actions via communication.
2. Section 5.3.1 is missing the results of CoELA when driven by CoLLAMA. This omission makes it difficult to fully assess the impact of different LLMs on the overall performance of the framework. The lack of these results hinders the ability to draw comprehensive conclusions about the robustness of CoELA across various LLM backbones. It is crucial to understand how the choice of LLM affects the performance of the cooperative framework.
3. The authors appear to be focused on exploring the potential of using Large Language Models (LLMs) in the Discrete Execution setting through communication. However, it's important to consider that communication may lead to challenges in certain scenarios, such as agents failing to reach a consensus. The paper lacks discussion on potential failure modes arising from communication breakdowns, such as conflicting goals or misinterpretations of messages. A more thorough investigation of the limitations of communication within this framework is needed, especially considering scenarios where reaching an agreement is not straightforward.

### Questions
1. How does the traditional MHP cooperate with MHP or CoELA?
2. How does CoELA handle the scenario where no consensus is reached? For example, Alice wants Bob to goto A and Bob wants Alice to goto B.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
