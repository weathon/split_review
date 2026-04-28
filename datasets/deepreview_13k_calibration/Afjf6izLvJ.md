# Grounding Robot Policies with Visuomotor Language Guidance

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Recent advances in the fields of natural language processing and computer vision have shown great potential in understanding the underlying dynamics of the world from large-scale internet data. However, translating this knowledge into robotic systems remains an open challenge, given the scarcity of human-robot interactions and the lack of large-scale datasets of real-world robotic data. Previous robot learning approaches such as behavior cloning and reinforcement learning have shown great capabilities in learning robotic skills from human demonstrations or from scratch in specific environments. However, these approaches often require task-specific demonstrations or designing complex simulation environments, which limits the development of generalizable and robust policies for new settings. Aiming to address these limitations, 
we propose an agent-based framework for grounding robot policies to the current context, considering the constraints of a current robot and its environment using visuomotor-grounded language guidance. The proposed framework is composed of a set of conversational agents designed for specific roles---namely, high-level advisor, visual grounding, monitoring, and robotic agents. Given a base policy, the agents collectively generate guidance at run time to shift the action distribution of the base policy towards more desirable future states. 
We demonstrate that our approach can effectively guide manipulation policies to achieve significantly higher success rates both in simulation and in real-world experiments without the need for additional human demonstrations or extensive exploration. Project videos at \url{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes g-MotorCortex, an agentic robot policy grounding framework that can self improve by generating the action-scoring guidance functions to update the action distribution of a base policy in an online manner. The paper presents experiments in both simulated and real-world robot settings and shows significant performance improvements on both adapting existing policies and learning new skills from scratch.
The proposed method is shown to be robust against cluttered and unseen environments, thanks to multi-granular object search, which enables flexible visuomotor grounding.
The authors also open source the code, models, and system prompts.

### Strengths
The paper is clearly written and well structured. It is easy to read and to follow through the contributions and components of the proposed method.
The experimental results are well presented as well and span across different axes of evaluations, which make it easier to appreciate the proposed method and contributions.
The results presented are interesting and significant to the field, and well demonstrate a nice integration of VLMs with robot control.

### Weaknesses
The experimental results show performance of three algorithms: Act3D, 3D Diffuser Actor, and a RandomPolicy. The reasons behind this choice is not clear and it would be helpful to understand what's behind this, and whether other types of algorithms would also be suitable and how their performance is expected to be.
The real robot evaluations is interesting, although the task defined is not interactive at a physical level, being only a reaching task. The results are interesting and valuable, however real-robot challenges arise often when interaction with environments exist.

### Questions
- Can you clarify the choice of algorithms chosen? Are results available from other algorithms too? Are there specific reasons behind this choice?
- What are the limitations of the learning from scratch? Can the system effectively incorporate preferences/demonstrations?
- Can you elaborate on why the self-improvement experiments plateau?

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
The authors propose a method to guide robot policy with the guidance of several Vision Language Models (VLM). Specifically, the authors use several VLMs to compute scores of actions during execution and use the score to improve/correct the policy. The authors evaluate their approach on the RLBench and real world tasks and show improved performance.

### Strengths
1. The high-level idea of this paper is interesting. Extracting VLM's knowledge to guide low level behavior is an interesting direction.
2. In the experiments, the authors evaluate their method on several realistic tasks and demonstrate the effectiveness of applying VLM guidance.

### Weaknesses
Major Weaknesses: Clarity of Presentation

The main weakness of this paper is the lack of clarity in presenting its concepts and methods. Many key ideas are not explained in sufficient detail, which makes it difficult to follow the proposed approach.

1. In Figure 2, numerous arrows connect concepts like Robotic Agent, Advisory Agent, and Grounding Agent, yet these elements are absent from Algorithm 1. Without these agents and connections represented in the algorithm, understanding the overall inference procedure becomes challenging. A clearer, more detailed explanation of the full inference process would be beneficial.

2. In Algorithm 1, it is unclear how to implement the "Generate_Guidance" and "Infer future state" steps in Line 9.

3. It appears that the authors sample action $a$ from a product distribution $\pi (a|o) * G(a|o, ...)$. This approach is challenging, particularly with complex probabilistic distributions. What are the parameterizations of $\pi$ and $G$? In experiments, it looks like $\pi(a|o)$ is primarily a diffusion-based policy. How is the computed score then used to guide diffusion sampling? Additionally, is $G_{\pi_t}$ or $G(a|o, ...)$ represented as a vector?

4. How is "iterative improvement" achieved, as referenced in Line 300 and Figure 4?

5. Figures 3 and 5 are difficult to interpret. The lack of clarity around score representation (as mentioned in point 3) may contribute to the difficulty in understanding these figures.

### Questions
See the weaknesses part. I would like to raise my score if the authors can resolve the clarity issues by more details and convince me the effectiveness of their approach.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an agent-based framework for grounding robotic policies in the current context by taking into account the constraints of both the robot and its environment, using visuomotor-grounded language guidance. The framework consists of a set of VLM-driven agents, each designed for specific roles, with the ultimate goal of improving existing policies.

### Strengths
+The paper proposed an agentic robot policy grounding framework that can self improve by generating the action-scoring guidance functions to update the action distribution of a base policy in an online manner. 
+Their experiments, conducted in both simulated and real-world robot environments, demonstrate significant performance improvements in adapting existing policies, as well as showcasing zero-shot capabilities.

### Weaknesses
- The main contribution of this work appears to be the guidance procedure, which stems from its ability to detect failures. Much of the pipeline focuses on object search using Vision-Language Models (VLM) to guide or refine the action distribution. However, the question arises as to how this approach compares to methods like AHA and RACER, which are instruction-tuned VLMs for failure detection and reasoning. In particular, AHA demonstrates that failure reasoning can improve base policies through a similar guidance mechanism.

- The paper claims that their approach is generalizable across various base policy classes, tasks, and environments. However, in the simulation experiments, evaluations were only conducted on a test set within the same domain distribution as the training data. No evidence was provided to demonstrate generalizability to different tasks or environmental perturbations.

- The authors also suggest that their approach can be used as a zero-shot policy to solve tasks without demonstrations. However, they did not provide any comparisons with other zero-shot methods, such as Manipulate-Anything, VoxPoser, or Code-as-Policies, which would strengthen their claim.

- In Figure 2, the example shows the need for granular object search due to the cluttered environment and large scene. However, this level of detail seems unnecessary for the real-world experiments presented in the paper. It would be beneficial to include more real-world experiments in complex, cluttered environments, where granular object search would be more impactful and better showcase the framework's strengths.

- The REFLECT framework [1], which focuses on failure reasoning, has publicly available code and would be a relevant baseline for comparison.

- The paper claims that the proposed framework enables robots to acquire skills through zero-shot learning or iterative self-improvement. To strengthen this claim, it would be beneficial to compare the approach with existing zero-shot methods, many of which have RLBench implementations and recovery mechanisms.

-Duan, Jiafei, Wilbert Pumacay, Nishanth Kumar, Yi Ru Wang, Shulin Tian, Wentao Yuan, Ranjay Krishna, Dieter Fox, Ajay Mandlekar, and Yijie Guo. "AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation." arXiv preprint arXiv:2410.00371 (2024).

-Dai, Yinpei, Jayjun Lee, Nima Fazeli, and Joyce Chai. "RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning." arXiv preprint arXiv:2409.14674 (2024).

-Duan, Jiafei, Wentao Yuan, Wilbert Pumacay, Yi Ru Wang, Kiana Ehsani, Dieter Fox, and Ranjay Krishna. "Manipulate-anything: Automating real-world robots using vision-language models." arXiv preprint arXiv:2406.18915 (2024).

-Huang, Wenlong, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, and Li Fei-Fei. "Voxposer: Composable 3d value maps for robotic manipulation with language models." arXiv preprint arXiv:2307.05973 (2023).

-Liang, Jacky, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, and Andy Zeng. "Code as policies: Language model programs for embodied control." In 2023 IEEE International Conference on Robotics and Automation (ICRA), pp. 9493-9500. IEEE, 2023.

-Liu, Zihao, Tianyu Chen, Siyuan Zhou, and Chelsea Finn. "Reflect: Iterative refinement of robot policies via failure explanation." In Conference on Robot Learning, pp. 115-126. PMLR, 2023.

### Questions
- The paper could benefit from a clearer explanation of the system through the figures. Providing more detailed descriptions, especially in figures like Figure 2, would help readers better understand the design principles and flow of the system.

- Additionally, the definitions of "1% and 10% guidance" are unclear and need further clarification. Explaining how these percentages are determined and applied in the system would provide valuable context for understanding their role in guiding the base policy.

-Why is ACT3D with 1% guidance outperforms the 10% guidance variant, it seems counterintuitive.

### Soundness
2

### Presentation
2

### Contribution
2
