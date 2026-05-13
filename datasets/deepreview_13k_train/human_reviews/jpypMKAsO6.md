# GridAgent: A 2D Grid-Based Game Framework And Benchmark For Multimodal Large Language Models

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) integrate the linguistic capabilities of LLMs with the ability to process multimodal data, enabling them to address a wider array of tasks. However, a comprehensive and standardized benchmark for evaluating MLLMs' complex visual reasoning performance in multimodal tasks has yet to be established. We introduce GridAgent, a versatile 2D grid-based framework that serves as a benchmark for assessing five essential capabilities of MLLMs: execution, perception reasoning, memory, learning, and planning. The framework includes twelve unique game tasks specifically designed to avoid overlap with the model's pre-training corpus. Each task targets at least one core competency and is enriched with diverse semantic information. Additionally, the game layouts are randomly generated, ensuring a more rigorous and authentic assessment of the MLLMs' capabilities. Experimental results indicate that although certain MLLMs excel in specific capabilities, none exhibit a comprehensive skill set comparable to the human baseline. Our work can be seen at: https://iclr2025gridagent.github.io/GridAgent-website.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce GridAgent, a new benchmark for evaluating "execution", "perception reasoning", "memory", "learning" and "planning" abilities of Multimodal Large Language Models. The authors base this taxonomy on the Wechsler Intelligence Test. The benchmark includes 15 different tasks setups targeting one or more of the abilities.

### Strengths
S1: The authors propose a taxonomy for evaluating visual abilities of MLLMs and ground it in existing intelligence test (Wechsler Intelligence Test) setup which has been used to evaluate human cognition

S2: The task setups and scenarios are reproducible and demonstrate the shortcoming of current MLLMs on visual reasoning

### Weaknesses
W1: This work provides limited insight compared to previous works. [1] Provides a more in-depth analysis of memory capabilities of MLLMs. Embodied and Computer control benchmarks like [2], [3], [4] provide more real-world insight into the planning and execution abilities of MLLMs in visual setups. [5] provides a detailed analysis of perception reasoning abilities of MLLMs including analysis of Visual, Text and Joint reasoning abilities and failure modes. 

W2: Reasoning strategies like Chain-of-Thought [6], Self-consistency [7] are necessary for invoking reasoning abilities of LLMs. Similarly multi-turn tasks (like the ones introduced in this environment) are more suited to agentic formulation of LLMs like ReAct [8], and Reflexion [9]. The results sections lacks these details (did you use COT?) and evaluations of agentic frameworks. 

W3: Human evaluation settings are unclear and not well-motivated. Firstly, “Five players (including two authors) participated in the games through the GridAgent interface, with each completing five rounds across all tasks. " It is not well motivated to have authors who are intimately familiar with the task setups to serve as testers. Secondly, "The results show that any adult, once familiar with the rules and putting in serious effort, is fully capable of completing all the games." Where are these results? Lastly, "Consequently, we set the human baseline to 1 for all tasks.” This implies that the human baselines were set to 1.0 without actually completing the same set of tasks that the MLLMs solved. These facts need to be clarified and more details about the human evaluation need to be mentioned. 

W4: Lack of Variability studies: Does the performance of MLLMs across multiple trials remain consistent? Authors could evaluate this on a subset of tasks. 

W5: Lack of studies about scaling with model sizes: Does the performance of MLLMs on these tasks improve with more model parameters? All considered models are 7B parameters or less providing no information about whether larger model sizes correlated with better performance.

### Questions
Q1: GPT-4o performs worse than random and other, much smaller MLLMs on PU, PL, and SO tasks. Can you provide a discussion on why this is the case? Can you also check if other models which are larger than 7B also similarly perform worse on these tasks? 

Q2: How does the Level of difficulty affect LLMs performance? Could you add results across different difficult levels for those MLLMs? 

Q3: Do agentic workflows like ReAct and Reflexion improve the performance of MLLMs in these multi-turn tasks? 

Q4: Could you provide more details about how those specific abilities are connected to the Wechsler Intelligence Test?

### Soundness
2

### Presentation
3

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
The paper presents GridAgent, a benchmark inspired by Wechsler Intelligence Test to  evaluate five MLLM capabilities: execution, perception reasoning, memory, learning, and planning. To do so, the paper proposes 12 games in 2D grid based environment which are diverse semantic environments, with randomized layouts and varying difficulty to test generalization and robustness of MLLM models. Proposed tasks evaluate multimodal reasoning and understanding abilities of existing MLLMs. Finally, the paper presents quantitative comparison of state-of-the-art proprietary and open-source MLLMs on the GridAgent benchmark and find that on majority of these tasks current MLLMs achieve performance closer to random chance performance. Additionally, the paper presents some preliminary analysis that suggests current MLLMs lack training for image-only perception tasks and it is difficult for these models to solve tasks that require contradictory knowledge from what is learned by these models.

### Strengths
1. The paper is well written and easy to follow
2. The tasks in the benchmark are thought through and carefully designed to test the five key capabilities the paper is focused on. I also like how authors created a set of tasks that require composing these capabilities to solve some of the tasks.
3. The experiments section covers most popular state-of-the-art MLLMs apart from Gemini. The zero-shot evaluation results on the tasks clearly demonstrate that these models are lacking zero-shot generalization ability to solve the proposed tasks.

### Weaknesses
1. For completeness I’d recommend authors to add results for latest Gemini model in comparison as well.
2. The results demonstrated in the paper are under zero-shot setting. I’d be curious to see how well all of these models ( or a subset of these  for which it is possible given constraints on context length) perform on these tasks with 1-2 in-context examples. We have seen remarkable results with In-Context learning for these long-context models and it’d be good to validate if these tasks can be solved with in-context examples. I believe it should help for SO, FI, and PL tasks. Adding these will also make paper stronger and help highlight the difficulty of tasks in the benchmark
3. Some details about the resolution of image input and how it is fed to each of these models is missing in the paper and supplementary. My understanding is - for all tasks where agent needed to take multiple actions to complete the task the input was fed to the model step by step. Is that the case? If yes, I’d recommend authors to add more details about how the evaluation was done, the resolution of image observations used, etc to the paper.
4. Did the authors ever run experiments with higher resolution image inputs for some of the tasks like Filing? I’d imagine these models should perform better on the task if input image is much higher resolution. If not, I think it would be a good experiment to add to the paper. This would clearly highlight the lack of perception reasoning ability if the input resolution is not a bottleneck.

### Questions
I’d also recommend authors to add evaluation examples where some of these models succeeded in supplementary. Examples from the best model should be good to add

I believe the benchmark is interesting and valuable to the community if authors address my concerns I'd be happy to increase my rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces GridAgent, a 2D grid-based benchmark framework designed to evaluate Multimodal Large Language Models (MLLMs) across five core capabilities: execution, perception reasoning, memory, learning, and planning. This is accomplished through twelve distinct game tasks. The results indicate that while models like GPT-4o perform well in specific tasks, none achieve human-level performance across all categories.

The article currently still has some obvious issues and writing structure that need to be addressed. Nonetheless, this contribution is significant, and with further clarification during the rebuttal phase, it could be accepted for the conference.

### Strengths
- The benchmark is well-structured, effectively targeting key competencies in MLLMs and providing a robust evaluation framework.
- The introduction of randomized game layouts enhances the test's generalization and robustness by minimizing overfitting to training data.
- The paper presents detailed empirical evaluations of multiple MLLMs, offering clear comparative insights.
- The use of diverse tasks ensures a comprehensive assessment of the models’ abilities, extending beyond simple task-solving to encompass more complex multimodal reasoning, while minimizing overlap with pre-training data, thus enhancing validity.

### Weaknesses
 - There is a limited discussion regarding the selection of specific game tasks and their comprehensive coverage of the intended capabilities.
- For some tasks, such as Puzzle and Sorting, model performance results close to random, raising questions about the alignment of task complexity with the current capabilities of models.
- Although the paper mentions the randomness in game layouts to avoid overfitting, it lacks sufficient analysis on how varying levels of task complexity affect model performance or whether simpler versions of the benchmark could serve as a more effective baseline. This introduces potential biases due to the artificial nature of the tasks.
- The comparison between MLLMs and human benchmarks appears overly simplistic, lacking a detailed exploration of potential improvements to models in order to bridge the performance gap.

### Questions
- The explanation of certain tasks, such as Perception Reasoning, lacks clarity regarding how performance metrics are derived and how these align with human cognition benchmarks.
- Section 5 exhibits some structural confusion, indicating significant issues in the writing structure of the Methodology section. The structure could be better organized to flow logically into the methodology and experimental analysis.
- The current comparative approach between MLLMs and humans is somewhat simplistic; exploring alternative comparison methods could provide deeper insights.

### Soundness
3

### Presentation
2

### Contribution
3
