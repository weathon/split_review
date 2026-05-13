# AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Autonomous agents that execute human tasks by controlling computers can enhance human productivity and application accessibility. However, progress in this field will be driven by realistic and reproducible benchmarks. We present \system, a fully functional Android environment that provides reward signals for \ntasks programmatic tasks across \napps real-world Android apps. Unlike existing interactive environments, which provide a static test set, \system dynamically constructs tasks that are parameterized and expressed in natural language in unlimited ways, thus enabling testing on a much larger and more realistic suite of tasks. To ensure reproducibility, each task includes dedicated initialization, success-checking, and tear-down logic, which modifies and inspects the device's system state.

We experiment with baseline agents to test \system and provide initial results on the benchmark. Our best agent can complete \mthreearesult\% of \system's tasks, leaving ample room for future work. Furthermore, we adapt a popular desktop web agent to work on Android, which we find to be less effective on mobile, suggesting future research is needed to achieve universal, cross-platform agents. Finally, we also conduct a robustness analysis, showing that task variations can significantly affect agent performance, demonstrating that without such testing, agent performance metrics may not fully reflect practical challenges.
\system and the experiments in this paper are available at \location.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces AndroidWorld, a benchmarking environment for autonomous agents interacting with Android devices. This environment enables testing on various apps by dynamically constructing parameterized tasks expressed in natural language. AndroidWorld supports a more realistic and varied testing experience than static environments, enabling agents to engage with numerous unique task goals and environmental conditions. Initial experiments using baseline agents indicate significant room for improvement in task completion rates, with top-performing agents achieving a 30.6% success rate. This highlights the challenges and research opportunities in building robust, cross-platform autonomous agents.

### Strengths
- AndroidWorld’s dynamic task construction introduces extensive variability in task conditions, offering a realistic and reproducible environment for testing autonomous agents on Android.
- The paper provides a robust baseline evaluation and a thorough performance analysis across real-world conditions.
- Extensive experiments provide essential insights into current agents' limitations and suggest potential pathways for improvement in future cross-platform agent designs.

### Weaknesses
 - The agents achieve a low overall success rate (30.6%), which, while reflecting the environment’s complexity, suggests that current methods may need significant refinement to handle mobile platforms effectively. This low success rate, while indicative of the challenges, also raises questions about the practical utility of the current agent implementations and the benchmark itself if the gap is too large to bridge with current methods.
- Though this paper introduces extensive task parameterization, it does not provide a detailed explanation of how specific parameter variations impact agent performance. There is also no analysis of performance changes across different task components or parameters. For example, it's unclear how varying the number of steps in a task, the complexity of the UI elements involved, or the specific app being used affects the agent's success rate. A more granular analysis of these factors would be beneficial.
- Large foundation models integrated into the agents exhibit high latency, taking significantly longer than humans to complete tasks, which may limit the practical applicability of these agents in real-time scenarios. The paper does not explore potential optimizations or alternative architectures that could mitigate this latency issue, which is a critical factor for real-world deployment.

### Questions
- How might AndroidWorld be expanded or adapted to include tasks that require specific contextual understanding, such as personalized interactions with app data?
- How might agent performance improve if AndroidWorld incorporated multimodal feedback mechanisms, such as sound or haptic responses, beyond the visual and text-based cues currently used?
- B-MoCA, like AndroidWorld, operates in Android environments and also employs various randomization schemes for task variability. How does your approach to task diversity, randomization, and reproducibility compare to B-MoCA? What unique advantages does AndroidWorld offer regarding its benchmarking scope, real-world applicability, and parameterized task generation? Additionally, are there specific aspects of your design that provide it with a distinct edge in evaluating agent robustness?
- Could the authors provide a full list of the tasks included in AndroidWorld, along with the initialization logic and success evaluation codes for each task?

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
4

### Summary
A benchmark for LLM (or LMM) agents controlling mobile devices is introduced, focusing on the necessity of interactive evaluation (as common benchmarks in this domain have mainly focused on static datasets so far) and the agents’ generalization ability in terms of task instructions. The tasks regard applications in Android commonly used in daily life as well as tasks in MiniWob++, which have been a common benchmark in digital device control. The study also proposes a new prompting approach to enhance agentic capabilities in foundation models and presents a detailed analysis of agent performance. The analyses include comparisons across different input modalities, robustness across varied task parameters, and their common errors. 

The main contributions of this work are the introduction of a new benchmark, tasks that can be randomized via instruction parametrization, and a new algorithm enhancing the capability of LLM agents for mobile device control.

### Strengths
S1 - This work presents a foundational contribution that advances the AI community's understanding of **mobile device control**, offering a robust framework for evaluating LLM agents in interactive environments.

S2 - The related work and comparisons to existing benchmarks are well-organized and comprehensive. This provides a clear context of how this benchmark builds upon and differentiates itself from prior studies.

S3 - The benchmark introduces an important challenge related to task generalization by implementing parametrized tasks. This effectively assesses the generalizability of agents across varying task instructions.

### Weaknesses
W1 - The explanation of the action space could be more detailed. For instance, in the ACTION_TYPE section described in Appendix B.2, further clarification on the purpose of the "STATUS" action would be helpful. Additionally, what is the rationale behind the necessity of a "SWIPE" action, despite the existence of "SCROLL", could be further justified. It is unclear how these actions are differentiated in practice, and what specific scenarios necessitate one over the other. A more granular explanation of the action space is needed to fully assess the agent's capabilities.

W2 - Although line 257 mentions a limited set of high-level APIs, Appendix B lacks specific details on these APIs. More explanation would help us understand the scope of actions. Without a clear understanding of these APIs, it's difficult to evaluate the full potential of the proposed framework. The lack of detail makes it challenging to determine the practical limitations and capabilities of the agent.

W3 - The rationale behind the task categorization tags could be elaborated on further. Expanding on the justification for the categorization approach would clarify its significance and enhance the robustness of the framework. The current explanation is insufficient to understand the underlying principles guiding the task categorization, making it difficult to assess the framework's ability to cover a wide range of mobile interaction scenarios.

W4 - I believe that this work could benefit from the inclusion of more baseline comparisons. Presenting results from a basic version of the agent, without any prompting methods for example, would provide valuable reference points. While the current results demonstrate that M3A is a strong baseline, additional baselines would enrich the study and offer further insights into performance. The absence of simpler baselines makes it harder to isolate the impact of the proposed prompting techniques.

### Questions
Q1 - Could the authors explain the rationale for integrating MiniWoB++ into a mobile environment, as this incorporation seems highly auxiliary? What unique challenges do these MiniWob++ tasks present, especially compared to tasks involving typical applications in AndroidWorld?

Q2 - While the unique aspects of the mobile action space are described, not all are represented in the current action space (e.g., multi-finger actions). Could the authors comment on the extensibility of M3A/AndroidWorld to accommodate different action spaces, or do they plan to incorporate a broader range of actions in the future?

Q3 - Could the authors provide a guideline on the training and testing configuration, such as a split of task categories? Additional details would aid in understanding the optimal configuration for achieving reliable results.

Q4 - (Minor) Would the authors consider providing results using Claude’s newly proposed models (considering that the relevant developers are interested in digital device usage)? This addition would offer a timely perspective on how recent advancements perform within this framework.

Q5 - The authors mention that using multiple random seeds and averaging the results would provide a fair representation of the results (line 493). Could the authors confirm if the results in Table 3 are also based on averaged results across different seeds? If not, might it be beneficial to conduct the experiments across multiple seeds, as task randomness can significantly impact agent performance?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AndroidWorld, an executable, reproducible, and realistic benchmark for evaluating Android device control agents. The authors also present results from several baseline agents and human.

### Strengths
1. Solid contribution: this benchmarks fills the gap for solid, reproducible, and executable benchmarks for Android device control tasks.
2. Good presentation: the presentation is clear, discussions in related works are comprehensive
3. Interesting experiments: the experiments presents a few good baselines and shows how human performs on the tasks. The robustness analysis also provides new information to the community.

### Weaknesses
1. Lack of many real-world apps and tasks: The benchmark lacks many real-world applications and tasks, as ensuring full reproducibility and automated evaluation makes it impossible to include closed-source apps like YouTube, Twitter (X), Amazon, or actual real-web browsing. This results in inherent sim-to-real gaps.
2. Lack of device diversity on android device/OS: The emulated device is fixed as a Pixel 6 running Android 13. However, in practice, what we care about is agents' performance across various devices and OS versions. Adding more OS/device options would potentially make the benchmark more correlated with real world use cases.
3. Lack of open-source baselines: All baselines in the paper appear to be based on proprietary models. Including some open-source models as baselines would be beneficial, as it would provide researchers a baseline they can iterate on.

### Questions
1. How was the confidence interval in Figure 3 calculated? I couldn’t find details on how these intervals were derived. Did you run the same model on these tasks multiple times to obtain them?

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
4

### Summary
This paper presents AndroidWorld, a realistic and reproducible Android benchmark that provides functional rewards for 116 dynamically constructed tasks across 20 real-world Android apps. The experiments show that the developed agent M3A can complete only 30.6% of the tasks, and existing web agents struggle to transfer well in Android environments.

### Strengths
1. The paper is overall clear and well-written.
2. The environment is lightweight and compatible with task random parameterization.
3. Detailed examples and error analysis are provided in the appendix.
4. I appreciate the effort to implement the initialization and teardown process for each task to ensure reliability and reproducibility.

### Weaknesses
1. The experimental setup is not very clear. Specifically:
- What specific stop criteria are used for the experiments (e.g., step limits or time limits)? How is the task-specific step budget set for each task?
- What decoding temperature is applied?
- How is human performance measured?

2. It would be helpful to include results from more models, including recent APIs and open-source models. The ablation study only investigates the observation space and does not consider the impact of other agent design choices, such as Reflexion.

3. Are all tasks and apps offline? If not, how to ensure reproducibility? For example:
- Does the SendSms task send actual messages?
- Could real-world time and date affect the evaluation results and reproducibility in calendar/timer tasks within AndroidWorld and MobileMiniWoB++?

4. More discussion of related work, e.g.:
- Zheng et al., "Agentstudio: A toolkit for building general virtual agents," arXiv preprint arXiv:2403.17918.
- You et al., "Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs." arXiv preprint arXiv:2404.05719.

### Questions
1. What is the number of human hours required to develop the environment and configure the tasks?
2. In your initialization and teardown process, have you considered scenarios where the agent performs actions outside the defined teardown process, potentially altering system states and resulting in non-identical states across different experiment trials?

### Soundness
3

### Presentation
3

### Contribution
3
