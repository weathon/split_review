# ProcBench: Benchmark for Multi-Step Reasoning and Following Procedure

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Reasoning is central to a wide range of intellectual activities, and while the capabilities of large language models (LLMs) continue to advance, their performance in reasoning tasks remains limited. The processes and mechanisms underlying reasoning are not yet fully understood, but key elements include path exploration, selection of relevant knowledge, and multi-step inference. Problems are solved through the synthesis of these components. In this paper, we propose a benchmark that focuses on a specific aspect of reasoning ability: the direct evaluation of multi-step inference. To this end, we design a special reasoning task where multi-step inference is specifically focused by largely eliminating path exploration and implicit knowledge utilization. Our dataset comprises pairs of explicit instructions and corresponding questions, where the procedures necessary for solving the questions are entirely detailed within the instructions. This setup allows models to solve problems solely by following the provided directives. By constructing problems that require varying numbers of steps to solve and evaluating responses at each step, we enable a thorough assessment of state-of-the-art LLMs' ability to follow instructions. To ensure the robustness of our evaluation, we include multiple distinct tasks. Furthermore, by comparing accuracy across tasks, utilizing step-aware metrics, and applying separately defined measures of complexity, we conduct experiments that offer insights into the capabilities and limitations of LLMs in reasoning tasks. Our findings have significant implications for the development of LLMs and highlight areas for future research in advancing their reasoning abilities. Our dataset is available at \url{https://huggingface.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ProcBench, a novel benchmark designed to evaluate the ability of large language models (LLMs) to accurately follow explicit, multi step instructions, a capability referred to as instruction followability. Unlike existing benchmarks that often require implicit knowledge or complex domain specific reasoning, ProcBench focuses on tasks where all necessary procedures and information are explicitly provided. This approach minimizes the reliance on implicit understanding and isolates the models' proficiency in procedural adherence.

ProcBench comprises 23 diverse tasks (e.g., DeleteChar, FillWord, Sort) that vary in complexity from short to long steps, emphasizing step-by-step correctness. The authors evaluate several state-of-the-art LLMs, including GPT-4 variants, Claude-3.5-Sonnet, Mistral-large, and Gemini-1.5-Pro, using newly introduced evaluation metrics: Prefix Accuracy (PA), Sequential Match (SM), and Final Match (FM). These metrics assess both intermediate and final outputs of multi-step sequences. The results reveal that while some models perform well on simpler tasks, their performance degrades significantly as task complexity and as the number of steps increase, highlighting current limitations in handling complex, multi-step procedural reasoning.

### Strengths
Novel Focus on Procedural Reasoning: The paper addresses a critical but underexplored aspect of LLM evaluation by isolating the ability to follow explicit, multi-step instructions without relying on implicit knowledge. This focus fills an important gap in existing benchmarks.

Comprehensive and Carefully Designed Controllable Benchmark: ProcBench includes 23 distinct tasks that cover a range of procedural challenges across different domains, involving string manipulation, list operations, and arithmetic computations. The tasks vary in length and complexity, providing a thorough and controllable assessment of models' capabilities.

Evaluation Metrics like Prefix Accuracy (PA) and Sequential Match (SM) capte not only the correctness of the final outcome but also adherence to each intermediate step.

Insightful Analysis: The study reveals significant performance drops in models as task complexity increases highlighting limitations of current LLMs and areas for future improvement.

Open-Source Dataset and Code Availability: Making ProcBench and the evaluation code publicly available promotes transparency, reproducibility, and encourages further research in this area.

### Weaknesses
Limited Real-World Applicability: While effective for isolating procedural reasoning, the tasks may not fully capture the complexities and nuances of real-world scenarios where implicit knowledge and domain-specific understanding are often required.

Focus on Specific Task Types: The benchmark predominantly includes tasks involving string manipulation, list operations, and basic arithmetic. This may limit the assessment of models' abilities in other types of procedures, such as complex logical reasoning, spatial reasoning, or tasks requiring hierarchical planning.

Insufficient Exploration of Prompting Strategies and Model Adaptability: The impact of different prompting techniques, chain-of-thought reasoning, or model fine-tuning on performance is not thoroughly investigated.

Insufficient explanation of causes of regression. It would be useful for the authors to dig into the actual model outputs and categorize failure cases (tokenization issue, format mismatch vs actual instruction followability issue).

### Questions
Exploration of Prompting Strategies and Model Fine-Tuning: Have you considered evaluating the impact of different prompting techniques, chain-of-thought reasoning, or fine-tuning strategies on model performance in ProcBench tasks?

Failure cases: Could you dig deeper into what are the failure cases of the models and what proportion of them are non-reasoning related (tokenization and formatting issues)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors develop a new benchmark, ProcBench, to assess the capacity of big language models to follow multi-step instructions taken from library of 23 text based tasks. They tested the performance of seven mostly closed source language models on ProcBench. The models need to construct sequences of intermediate and final states. Further, authors come up straightforward metrics in order to assess the performance of models for these tasks.

### Strengths
- I believe, this paper is clearly written and easy to understand.
- Various metrics to measure instruction following capabilities

### Weaknesses
 # Limitations


- Lack of Novelty : [1], [2] already demonstrate LLM's accuracy declines as, planning depth of procedurally generated problems increases. Paper doesn't propose any new technique that can improve/augment the instruction following capabilities.

- Insufficient Benchmarking: The paper fails to provide benchmarking insights across various model variants and sizes, which limits the usability of its benchmarking insights.

- Effect of tokenization : Given the tasks involve character manipulation, ablation about how different tokenization schemes (e.g., byte-level, subword-level, character-level) impact the models' ability to follow instructions and maintain coherence over long sequences would provide valuable insights into the relationship between input representation and procedural reasoning.

- Other techniques : techniques such as majority voting, self-consistency, self-refine [3] prompting to improve model adherence to instructions. Their analysis is completely absent.

### Questions
In addition to points stated in weaknesses, It would be good to include following analysis:

- Task Difficulty Analysis: In Figure 6, tasks are ordered by median accuracy without prior analysis or justification of what makes some tasks harder than others. A taxonomy based on task nature, required implicit knowledge, number of steps, etc., compared to empirical accuracy, would be informative. The paper mentions only 91 out of 5,520 examples had PA=0 across all models. Could you provide more details about these examples? Are there common patterns that make these particularly challenging?

- Robustness Analysis : Incorporating robustness checks such as perturbations in instructions or introducing minor distractions, It would add a practical dimension to ProcBench, aligning it more closely with real-world scenarios where instructions may not always be perfectly structured.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper first proposes that the general task of reasoning can be broken down into sub-capabilities (e.g. path exploration, selection of relevant knowledge, multi-step inference). The paper then adjusts the focus on evaluating multi-step inference capability in isolation. To achieve such evaluation, the authors construct 23 tasks that require manipulation of strings, integers, and lists such that the exact procedure to complete the task is explicitly provided, minimal implicit knowledge is required, and is straightforward for humans. Although these tasks provide some insight into a model’s capability of performing rote tasks, it does not provide sufficiently interesting tasks that separates itself from other instruction-following benchmarks. In order to gather some insights regarding task complexity and measure a model’s ability to follow precise instructions, the authors develop some metrics, namely, prefix match length, prefix accuracy, sequential match, and final match. These metrics provide some insight into the role task complexity (i.e. increasing the number of steps required for the task) plays in a model’s ability to perform extended precise instruction following. However, the findings are that the final match accuracy provides similar information as the prefix accuracy and sequential match metrics, thus, ultimately providing limited additional insights into models’ capabilities.

### Strengths
- The paper introduces new metrics such as prefix match length, prefix accuracy, sequential match, and final match which provide some interesting analysis of the role task complexity (i.e. increasing the number of steps required for the task) plays in a model’s ability to perform extended precise instruction following
- The benchmark creation process is clear and is constructed in a manner to assess the capability coined as “instruction follow-ability”

### Weaknesses
 - The 23 tasks created are not representative of real tasks that an LLM would perform in practice and there were no experiments that attempts to correlate the performance on this type of instruction followability task to general reasoning tasks
- The paper mentions that a novelty of their benchmark to other instruction following benchmarks is that they are able to assess the intermediate steps and not rely simply on the final outcome. However, their empirical findings show that FM is, in practice, similar to PA and SM, which begs the question of whether evaluating final outcome is already sufficient enough to assess step-by-step explicit instruction following.
- A lack of interesting ablations/error analysis. Some ideas could be to compare FM performance when the model is prompted to complete the set of steps in one go or error analysis on the types of mistake the model makes and a breakdown of which step (whether it is earlier or later steps) the model usually makes the wrong move. It would also be interesting to see if the mistakes are mostly just error in one step but the rest of the steps, conditioned on that error, are still accurate.

### Questions
- Is there some evidence that improving in this step-by-step instruction following where all the information is provided and the exact path is outlined is correlated with how well the LLM will be able to execute step-by-step instruction following when it needs to explore different paths + use implicit knowledge/world knowledge?
- Could you clarify how you transform the LLM output into a JSON format for assesement?
- Do you have a sense of how the model performance will vary if you don't prompt the model to do the task step by step but rather ask it to complete the steps in one go?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors interpret the reasoning process as the exploration of paths, the utilization of knowledge, and the following of multi-step instructions. They propose ProcBench, a benchmark consisting of 23 subtasks designed to evaluate the multi-step instruction-following capabilities of large language models (LLMs), aiming to assess the reasoning ability of LLMs from a specific perspective. The authors evaluated the performance of seven models on ProcBench and conducted corresponding analyses.

### Strengths
- The authors provided a reasonable breakdown of reasoning abilities and, under controlled variables, introduced ProcBench to focus on exploring the multi-step instruction-following capabilities of models.
- The authors proposed metrics such as PML, PA, SM, and FM to assist in analyzing the performance of LLMs on ProcBench.
- The authors presented some interesting insights, including that the o1 series models exhibit a more gradual decline in performance as task difficulty increases, reflecting a fundamental difference between this series and other LLMs.

### Weaknesses
 - When models engage in reasoning, they often do not follow a paradigm where they first plan all procedures and then execute them step by step, as typically reflected in benchmarks. Instead, they undergo a process of continuous exploration, following single-step instructions along the way. Therefore, the authors need to further verify the relationship between the multi-step instruction-following ability assessed by the benchmark and the actual reasoning ability. The experiments in the paper focus on ProcBench, but I suggest that the authors analyze the correlation between multi-step instruction-following ability and reasoning ability by statistically examining the reasoning performance of LLMs on relevant benchmarks and relating it to their performance on ProcBench.
- As the authors mentioned, 91 samples exhibit a PA of 0 across all models, which "could indicate not merely high difficulty but also potential flaws in task design." The authors are advised to conduct a case check to ensure the high quality of the benchmark.
- The authors provided quantitative statistics of LLM performance on ProcBench, but there is a lack of attribution analysis for model failures (as well as case studies), which is crucial for guiding model improvement.

### Questions
See Weaknesses



**After Rebuttal**

**Thanks for the author's response, although it was somewhat late. However, I noticed two points:**

1. The authors acknowledge that it is currently not possible to effectively establish the relationship between multi-step instruction-following ability and reasoning ability ("for future research"). However, this makes the mention of "MULTI-STEP REASONING" in the manuscript, particularly in the title, quite confusing. Since the relationship between ProcBench and reasoning ability cannot be validated, it raises the question of why reasoning ability is emphasized. I suggest the authors revise such phrasing, as it lacks rigor.

2. The authors have not responded to my third concern.

**Given these considerations, I believe the manuscript requires further refinement to meet the expected quality. Therefore, I have lowered my score.**

### Soundness
3

### Presentation
3

### Contribution
2
