# ET-Plan-Bench: Embodied Task-level Planning Benchmark Towards Spatial-Temporal Cognition with Foundation Models

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Recent advancements in Large Language Models (LLMs) have spurred numerous attempts to apply these technologies to embodied tasks, particularly focusing on high-level task planning and task decomposition. To further explore this area, we introduce a new embodied task planning benchmark, ET-Plan-Bench~\footnote{The benchmark and source code will be publicly released soon.}, which specifically targets embodied task planning using LLMs. It features a controllable and diverse set of embodied tasks varying in different levels of difficulties and complexities, and is designed to evaluate two critical dimensions of LLMs' application in embodied task understanding: spatial (relation constraint, occlusion for target objects) and temporal \& causal understanding of the sequence of actions in the environment. By using multi-source simulators as the backend simulator, it can provide immediate environment feedback to LLMs, which enables LLMs to interact dynamically with the environment and re-plan as necessary. We  evaluated the state-of-the-art open source and closed source foundation models, including GPT-4, LLAMA and Mistral on our proposed benchmark. While they perform adequately well on simple navigation tasks, their performance can significantly deteriorate when faced with tasks that require a deeper understanding of spatial, temporal, and causal relationships. Thus, our benchmark distinguishes itself as a large-scale, quantifiable, highly automated, and fine-grained diagnostic framework that presents a significant challenge to the latest foundation models. We hope it can spark and drive further research in embodied task planning using foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a benchmark for evaluating embodied task planning. The authors propose using LLMs to automatically generate new tasks, including their descriptions and completion criteria. A modular approach is introduced to solve the proposed task. This modular approach can be combined with different LLMs to evaluate their planning abilities.

### Strengths
1. This paper introduces a benchmark that can be scaled up using LLMs to automatically generate the tasks and their completion criteria.
2. Different LLM models are evaluated on the proposed tasks, and insights about the models and challenges introduced by different types of tasks are drawn.
3. The paper shows that after finetuning automatically generated data based on the tasks, the open-sourced model can perform on par with a proprietary model.

### Weaknesses
1. Although the paper claims that an infinite amount of tasks can be generated. It's unclear whether the diversity is bottlenecked by the scenes the simulator provides and the actions (including the transition models of the actions) the simulator supports.
2. It's unclear what new conclusions or insights can be drawn from this benchmark. I hope the authors can provide a more detailed analysis and categorize the failure modes.
3. In the proposed modular approach, there are perception modules. It's unclear whether the robustness of these perception modules is being evaluated.
4. The authors should justify the distribution of the generated tasks shown in Figure 1. It's unclear whether the distribution is directly from the generation pipeline or deliberately achieved.
5. Since the generated tasks themselves could be wrong. Are the incorrect tasks filtered? I hope the authors can provide details on how the incorrect tasks are accounted for, especially when the methods peform similarly.
6. It would be great to see qualitative examples of both positive and negative examples.
7. Some definitions of the tasks can be elaborated on: 1) it's unclear what difference between regular navigation and navigation due to the distant initial position. 2) how is the optimal path defined? 3) since there are different types of temporal and causal constraints, what is the percentage of these types in the generated tasks?
8. The definition of the task type "navigation with occlusion due to distant initial position" seems somewhat arbitrary, as it is based on the distance and the top 20th percentile. A more straightforward definition could involve directly checking whether the object is occluded by evaluating the agent's view in the simulation.

### Questions
I hope the authors can address my questions and comments above.

### Soundness
2

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
4

### Summary
The manuscript proposes an Embodied AI benchmark, meant to focus on assessing models' abilities to reason about spatial and temporal context. The manuscript proposes mechanisms for programmatic generation of tasks, within the VirtualHome environment, and automatic evaluation of agents — both, through the use of foundation models.

### Strengths
I like the setting considered by the manuscript — automatic generation and evaluation of embodied reasoning tasks.

### Weaknesses
Section 1 — The manuscript asserts that foundation models struggle with spatiotemporal reasoning; benchmarking Vision-Language-Action (VLA) models seems particularly relevant to this assertion.

Section 2 — The manuscript states, "We introduce a benchmark for household embodied task planning rather than question answering about the environment. It focuses on skill-level task decomposition rather than lower-level control." (L179-181). This is not sufficiently motivated. As better foundation models become available, skill-level task decomposition requires less analysis and optimisation, compared to spatiotemporal reasoning for low-level control.

Section 3 — Is there a risk that, if tasks and evaluations are performed by LLMs, methods that consist of the same LLMs may obtain inflated performance evaluations? The evaluations would then be in-domain. This phenomenon would be catastrophic, as agents' behaviors would be rewarded in ways that do not necessarily lead to improved behavior in the real-world. For validating the effectiveness of this benchmark for suitability in assessing model performance, the manuscript should establish that performance in this benchmark correlates with performance, e.g., on tasks extracted from multiple pre-existing benchmarks and/or on real-world tasks from large-scale datasets, (e.g., DROID, OXE). Furthermore, to further avoid the test-set leakage issue above, perhaps the proposed method for task generation should include some sort nondeterminism, e.g., through a set of structured perturbations, common in the safety-critical scenario generation literature.

Section 3 — Insufficient evaluation. The manuscript provides only very limited cross-simulator analysis. What would be better would be to take multiple representative model classes, identify similar cross-simulator tasks according to all the conditions that the manuscript proposes (Section 3.1), and benchmark the models in a principled way. Currently, it is difficult to extract insights about the relative usefulness of the proposed framework. Furthermore, direct comparisons/extensions with RoboGen are missing, despite the fact that RoboGen seems to share the same motivation.

Section 4 — The manuscript does not provide any new insights about *why* it asserts that foundation models have struggled with spatiotemporal reasoning. It would be useful if the manuscript could offer discussion there, perhaps through the task categorization proposed by the manuscript.

Section 4 — As new foundation models are introduced, they change sometimes-dramatically in their capabilities, and not always entirely for the better. How does the proposed framework limit the failure cases of foundation models from affecting the efficacy of, e.g., model evaluation in the proposed benchmark? It seems that the usefulness of the benchmark is directly tied to the underlying models’ abilities to perform task generation and evaluation flawlessly.

### Questions
No additional questions — please see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents ET-Plan-BENCH, a benchmark for evaluating large language models (LLMs) on embodied task planning. The benchmark includes navigation and manipulation tasks with varying spatial and temporal constraints, implemented in Virtual Home and Habitat simulators. The main contributions are: (1) A task generation pipeline using LLMs, (2) A benchmark focusing on spatial-temporal cognition, and (3) Baseline results comparing different LLM agents. The paper evaluates several metrics including success rate, action sequence length, and moving distance.

### Strengths
The paper presents an attempt to systematically evaluate LLMs on embodied planning tasks.

The paper proposes a method to use LLM to generate navigation and manipulation tasks from two simulated environments, Virtual-Home and Habitat.

The paper evaluates LLM agents including GPT-4 and open-source LLMs, LLAMA and Mixtral 8x7B using the proposed benchmark. Results show that a supervised fine-tuned (SFT) small-size LLAMA-7B model using the benchmark EQA data can match the state-of-the-art closed-source model GPT-4.

### Weaknesses
Limited novelty in contributions: Task generation using LLMs has been explored extensively in prior work The benchmark tasks are relatively simple and constrained

Significant limitations in the experimental setup: The simulators (Virtual Home and Habitat) are quite restricted in terms of task complexity and environmental interactions Agents do not have true perception - they receive text descriptions rather than visual input. The spatial and temporal constraints are quite basic

Lack of rigorous analysis and insights: The LLM agent comparison results are presented as they are without novel insights No clear framework for systematic task generation and evaluation Limited discussion of how the findings could improve embodied AI systems

Compared to recent work like "Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making https://arxiv.org/abs/2410.07166" (note that this is not considered part of related work as the submission is concurrent), this paper: Lacks a principled framework for formalizing different types of embodied tasks Does not provide fine-grained error analysis Misses systematic evaluation of different LLM capabilities

The writing is quite poor. It did not explain the setup clearly. I have to find information in the appendix to continue reading.

### Questions
How does the task generation ensure coverage of meaningful spatial-temporal constraints? It seems that only limited constraints, e.g. object A is on top of object B are considered. 

Why not implement true visual perception instead of text descriptions?

What insights can be drawn about LLMs' capabilities for embodied planning?

The authors have clarified a few things and made improvements. I upgraded my score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a new embodied task planning benchmark that uses language models to generate tasks.  They also present a language baseline agent for this task.

### Strengths
+ The work here appears large and comprehensive.
+ Exploring the extent to which language models can solve embodied tasks is extremely relevant.
+ Designing systems which can procedurally generate new data is useful.

### Weaknesses
 - Minor: two sentences from the abstract are nearly copied to the beginning of the introduction this is unnecessary and should be avoided.
- Major: At the moment, the presentation Is quite unclear.  While the overall goal, using LLMs to both generate tasks and solve embodied AI problems is apparent, the method, the primary assumptions and overall system are hard to understand.
- Major: It's not clear what using the LLM in task generation accomplishes.  Is the goal just to provide common sense reasoning over the larger task search space?  Otherwise, it seems like these tasks can be generated fairly mechanically as others have done in the past.  To be clear my complaint is not that the LLM serves no purpose, my complaint is that it is not well described (again a clarity issue), and that it's hard to tell how much this adds.
- Medium: It says that humans evaluated these tasks based on "reasonableness" which seems highly subjective and difficult to quantify.

### Questions
- What is the action space and observation space in this setting?
- How does the language model interact with the simulator?
- Is there any way to compare tasks generated with the LLM to tasks that are sampled some other way (randomly sampling objects and compatible containers for example)?  Is there any way to tell how much we are gaining by using the LLM in the data generation process?
- Are the LLM agents taking in the rendered images?  If so, shouldn't we be referring to these as VLMs to make this more clear?

My review for the moment is "5: marginally below the acceptance threshold" but I would really like to improve my score here.  There is clearly a lot of effort and good work that went into this paper, but at the moment, a lot of important components of this system are not clear.  To meet the bar for acceptance, it is necessary to be able to explain how an LLM interfaces with one of these 3D simulators to an audience that is familiar with RL and LLMs individually, but has never seen them combined, and this information should be clearly stated in the main text (the introduction should even give a rough sense of this) and not buried deep in the appendices.

### Soundness
2

### Presentation
1

### Contribution
3
