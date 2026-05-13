# OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Large language models (LLMs) and large multimodal models (LMMs) have shown great potential in automating complex tasks like web browsing and gaming. However, their ability to generalize across diverse applications remains limited, hindering broader utility. To address this challenge, we present \textbf{\texttt{\texttt{OSCAR}}}: \textbf{\underline{O}}perating \textbf{\underline{S}}ystem \textbf{\underline{C}}ontrol via state-\textbf{\underline{A}}ware reasoning and \textbf{\underline{R}}e-planning. \texttt{\texttt{OSCAR}} is a generalist agent designed to autonomously navigate and interact with various desktop and mobile applications through standardized controls, such as mouse and keyboard inputs, while processing screen images to fulfill user commands.
\texttt{\texttt{OSCAR}} translates human instructions into executable Python code, enabling precise control over graphical user interfaces (GUIs). To enhance stability and adaptability, \texttt{\texttt{OSCAR}} operates as a state machine, equipped with error-handling mechanisms and task-driven re-planning, allowing it to efficiently adjust to real-time feedback and exceptions. We demonstrate \texttt{\texttt{OSCAR}}’s effectiveness through extensive experiments on diverse benchmarks across desktop and mobile platforms, where it transforms complex workflows into simple natural language commands, significantly boosting user productivity. Our code will be open-source upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
- This work presents an LLM+LMM-based agent to solve Desktop/Mobile OS tasks, including key modules such as GUI elements recognition and SoM prompting, plan/re-plan state machine and code execution for general mouse/keyboard control.
- Experiments on multiple, both static and dynamic, benchmarks demonstrate the proposed framework's efficacy and generalizability.

### Strengths
- This work shows a robust and efficient OS agent by resorting to a general purposed language models without fine-tuning. To cope with GUI recognition difficulties (beyond general vision tasks), SoM techniques are applied to improve reliability.
- Many baseline comparisons and detailed implementation are also provided.

### Weaknesses
 - Discussion on safety may be helpful since the agent has control over an OS.
- Although it uses a state machine and re-planning, OSCAR lacks a self-improvement mechanism. Do you have more insights on representing states, e.g. system errors/task failures, beyond pure text language?

### Questions
- What makes OSCAR outperform other baselines mostly (since many methods also have their feedback loop)?
- Will a fine-tuned LM be eventually required for the robustness in real-world scenarios beyond those benchmarks? To what degree is a user/expert required to supervise the agent's operation?
- Is plan -> execution -> error -> re-plan enough even for complex tasks or sampling-based methods such as evolutionary search (but costly and redundant) should be also considered.

### Soundness
3

### Presentation
4

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
The paper presents OSCAR, a generalist agent designed to autonomously navigate and interact with both desktop and mobile applications using standard controls like mouse and keyboard. The agent aims to interpret user commands, interact with graphical user interfaces, and adapt its strategies based on real-time feedback. OSCAR is constructed as a state transition process and integrated with a GUI dual-grounding observation and task-driven re-planning. Further, the authors evaluate OSCAR on three digital task benchmarks, OSWorld, GAIA and AndroidWorld, outperforming current SOTA AI systems in completing digital tasks.

### Strengths
1. The use of a task-driven re-planning strategy allows OSCAR to adjust its actions based on real-time feedback, which enhances its ability to correct itself, do the state-aware reasoning and complete complex tasks autonomously.
2. OSCAR is evaluated against a diverse set of benchmarks, demonstrating superior performance in both desktop and smartphone environments, which underscores its generalizability and effectiveness.
3. The state transition process in OSCAR allows for systematic handling of tasks by structuring operations into distinct phases, such as observation, planning, execution, and verification. This structured approach enhances error recovery and adaptability by enabling the agent to assess and resolve issues at each state

### Weaknesses
1. I think it would be better to give some detailed cases to explain how the state transition works to complete the task and handle the errors.
2. There could be more discussions about how to fit OSCAR into different OS envs and generalize it to more benchmarks and systems.

### Questions
1. In the dual-grounding observation approach, how do you add the labels to each element to provide explicit semantic grounding?
2. What does "evaluation scripts" in section 2.1 refer to? Do you leverage the task-specific evaluation scripts from OSWorld? You may make it more clear about how you evaluate OSCAR on each of the three benchmarks.
3. As you allow 4 attempts per run for the agent to finish the task, is it crucial for a better performance and higher score on the benchmark? Do they always learn from failures and need more attempts to do better?
4. A more detailed error analysis is needed to specifically analyze the reasons for failure cases of reaching step limits, as this may help further improve OSCAR's error handling mechanism.

### Soundness
4

### Presentation
3

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
This work introduces OSCAR, a generalist agent that autonomously navigates and interacts with desktop and mobile applications through standard controls like mouse and keyboard inputs. OSCAR’s framework includes state transitions that dynamically adapt to various environments and are equipped with error-handling mechanisms. OSCAR also addresses the challenge of VLM’s difficulty in interpreting GUI screenshots by grounding them with semantic symbols. Finally, OSCAR incorporates task-driven replanning for efficient real-time adjustments based on feedback and exceptions. OSCAR is evaluated on GAIA, OSWorld, and AndroidWorld benchmarks. The results show that OSCAR significantly outperforms other baseline methods.

### Strengths
1. OSCAR demonstrates strong performance on evaluated benchmarks, achieving an average success rate of 28.7% and a success rate of 13.5% on the most challenging Level 3 tasks in the GAIA benchmark.
2. OSCAR implements a state machine with well-defined behaviors to manage complex, dynamic environments effectively.
3. Grounding GUI images with semantic symbols offers a more systematic approach for VLM to interpret the current state of the OS environment.

### Weaknesses
The [Verify] state is crucial to OSCAR’s framework; however, its exact functionality remains unclear. For instance, what occurs when [Verify] yields a false positive, such as validating an invalid plan? Can the system recover from these failures? Conducting an in-depth analysis of the [Verify] step's failure modes and success rate would significantly enhance the paper's quality.

### Questions
No questions

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces OSCAR, a computer agent framework mainly focused on planning and aimed to generalize across diverse applications. The experiments demonstrate OSCAR’s effectiveness on GAIA, OSWorld, and AndroidWorld.

### Strengths
1. The proposed agent framework is formulated as a state machine, making it clear to follow.
2. OSCAR outperforms several baselines in both desktop and mobile environments.

### Weaknesses
1. The proposed modules (task-driven re-planning, context memory, GUI observations, and code actions) are not novel. Many closely related methods are not discussed, e.g.:
- Kim et al. "Language models can solve computer tasks." NeurIPS 2023.
- Sun et al. "Adaplanner: Adaptive planning from feedback with language models." NeurIPS 2023.
- Zheng et al. "Synapse: Trajectory-as-exemplar prompting with memory for computer control." ICLR 2024.

2. The experiments only ablate GUI observations and the replanning module. The analysis claims that the improvements come from “fewer re-planning attempts” and “smaller, more efficient steps”, but it is unclear how the proposed planning module contributes to this compared to the baselines. The ablation study lacks a comparison of different planning strategies within the OSCAR framework, making it difficult to isolate the impact of the proposed planning approach.

3. In Table 3, OSCAR outperforms baselines in medium and hard cases but is worse in easy cases, for which the authors should analyze the potential reasons. The lack of analysis on why OSCAR underperforms in easy cases raises concerns about the general applicability of the approach.

4. It is unclear how OSCAR leverages “real-time” feedback from the OS. Additional experiments on AgentStudio, a more complex, dynamic environment, are helpful. The paper does not provide sufficient detail on how the system handles asynchronous feedback from the operating system, which is crucial for real-time interaction.

5. The limitations of OSCAR are not discussed. A thorough discussion of limitations is essential for understanding the scope and potential drawbacks of the proposed method.

6. Minor: there are many typos, e.g.:
- line 300, “i.e. when” -> “i.e., when”; line 332, “(e.g. Chrome)” -> “(e.g., Chrome)”; and so on.
- missing or abundant space in Section 1 “(LLMs)(Ouyang …”, “(LMMs)(Li …”, Section 3 baselines “UFO(Zhang et al., 2024a)”, Table 1 caption “(i.e. GPT-4-turbo )”, etc.

### Questions
See Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
