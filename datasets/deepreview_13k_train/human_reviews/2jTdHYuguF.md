# MMMU-Pro: A More Robust  Multi-discipline Multimodal Understanding Benchmark

- Decision: Reject
- Scores: 6, 6, 5, 6, 6

## Abstract
This paper introduces MMMU-Pro, a robust version of the Massive Multi-discipline Multimodal Understanding and Reasoning (MMMU) benchmark. MMMU-Pro rigorously assesses multimodal models' true understanding and reasoning capabilities through a three-step process based on MMMU: (1) filtering out questions answerable by text-only models, (2) augmenting candidate options, and (3) introducing a vision-only input setting where questions are embedded within images. This setting challenges AI to truly ``see'' and ``read'' simultaneously, testing \textit{a fundamental human cognitive skill of seamlessly integrating visual and textual information}. Results show that model performance is substantially lower on MMMU-Pro than on MMMU, ranging from 16.8\% to 26.9\% across models. We explore the impact of OCR prompts and Chain of Thought (CoT) reasoning, finding that OCR prompts have minimal effect while CoT generally improves performance. MMMU-Pro provides a more rigorous evaluation tool, closely mimicking real-world scenarios and offering valuable directions for future research in multimodal AI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MMMU-Pro, a more robust version of the MMMU benchmark. MMMU-Pro aims to more accurately assess multimodal models' true understanding and reasoning capabilities across diverse academic domains by addressing limitations found in the original MMMU. The authors achieve this through three main enhancements: (1) filtering out questions that can be answered using only text, ensuring models rely on multimodal input; (2) expanding the number of answer options to reduce reliance on guessing; and (3) introducing a vision-only input setting where questions are embedded in images, challenging models to integrate visual and textual information. These modifications result in a more rigorous benchmark that better approximates real-world scenarios. Experimental results demonstrate that MMMU-Pro challenges existing models more, revealing performance drops across multiple models and encouraging further exploration in multimodal understanding and reasoning.

### Strengths
- Significance: MMMU-Pro addresses critical gaps in existing benchmarks, promoting deeper multimodal understanding over shallow pattern recognition. It sets a higher evaluation standard, likely to drive future research and model development.
- Quality: The paper rigorously evaluates MMMU-Pro across multiple state-of-the-art models, showing significant performance drops that underscore the benchmark’s challenge. 
- Insights: Experiments with methods like Chain of Thought reasoning and OCR prompts enrich the analysis, verifying the benchmark’s effectiveness in highlighting model limitations.

### Weaknesses
Unclear Justification for OCR Requirement: One of MMMU-Pro's main contributions is embedding text within images to increase difficulty by requiring OCR. However, this addition may detract from the benchmark’s core goal of evaluating multimodal understanding, as it primarily tests the model’s OCR capabilities rather than its deeper multimodal comprehension. Although it is true that embedding text within images is more realistic, whether the extra difficulty from OCR is significant for LMMs needs more justification, as the extra focus on OCR could potentially obscure the true reasoning ability of models that struggle with OCR but perform well in multimodal integration tasks.

Limited Impact on Model Performance Ranking: While it’s acceptable for a benchmark to yield similar performance scores, MMMU-Pro does not alter the ranking of current models, nor does it reveal new insights into their strengths and weaknesses. This lack of differentiation reduces the benchmark’s ability to provide fresh perspectives on model capabilities, potentially weakening its contribution as an evaluation tool.

### Questions
A more thorough justification for the OCR requirement and a clearer explanation of the new benchmark's significance could enhance the paper’s impact.

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
The paper introduces MMMU-Pro, an enhanced multimodal benchmark to rigorously test AI models’ understanding and reasoning by addressing limitations in the original MMMU benchmark. MMMU-Pro utilizes a three-step process to improve robustness: filtering questions answerable by text-only models, increasing candidate options to prevent guesswork, and implementing a vision-only input mode that embeds questions within images, thus requiring integrated visual and textual processing. Experimental results show a significant drop in model performance compared to MMMU, highlighting multimodal challenges. The study further investigates Chain of Thought prompting and OCR effectiveness, identifying areas where current models struggle, and setting directions for future multimodal research​.

### Strengths
- This paper addresses key limitations in existing benchmarks like MMMU. By introducing a vision-only input mode, MMMU-Pro uniquely challenges models to process visual and textual information in a more realistic, integrated manner. This work also enhances question difficulty and mitigates model reliance on shortcuts, providing an essential tool for testing and advancing multimodal AI.

- The clarity of the paper is strong, with well-organized sections detailing the benchmark's construction and evaluation.

- Additionally, the paper examines the impact of Chain of Thought prompting and OCR on performance within the proposed benchmark, further investigating the limitations present in current MLLMs.

### Weaknesses
 - One limitation is that in the vision-only setting, images are manually captured photos and screenshots over a simulated display environment, but only differences in backgrounds, font styles, and font sizes are considered. However, the diversity of real images should also account for factors such as varied lighting conditions and different camera angles (e.g., rotated text in photos).

- While the paper discusses the Chain of Thought (CoT) prompting and OCR’s impact, these evaluations could be expanded to clarify where CoT specifically improves performance. For example, breaking down CoT's impact across different question types or modalities could reveal deeper insights, guiding future model improvements.

- Moreover, the analysis would benefit from more nuanced evaluation metrics that go beyond accuracy, such as tracking misinterpretation rates or identifying where models are most prone to visual-textual integration issues. This additional layer of analysis could provide more actionable insights for researchers looking to address specific multimodal weaknesses.

### Questions
Please refer to weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is an extension of MMMU. The evaluation consists of three steps: 1) filtering out questions that can be answered by text-only models, 2) augmenting candidate options to reduce the chances of guessing correctly, and 3) introducing a "vision-only input" setting to challenge models to comprehend both visual and textual content simultaneously. 
Experimental results demonstrate a significant drop in model performance on MMMU-Pro

### Strengths
Rigorous Evaluation:Using multiple LLMs to vote and filter out questions that can be solved by text-only models does enhance the benchmark’s ability to reflect more accurate visual capabilities. Overall, this benchmark is indeed more complex and better demonstrates the model’s ability to integrate text and visual information.

The findings and detailed analysis suggest avenues for future improvements, such as better vision-text integration strategies.

### Weaknesses
1. Expanding the number of options is an obvious way to reduce model performance. The emphasis should be on demonstrating the quality of these expanded options. However, the authors only mention this briefly with a single example.
2. The work appears straightforward, with most of the effort concentrated on non-technical human labor, making the overall contribution less innovative.

### Questions
Regarding the quality of options: Expanding the number of options does indeed reduce model performance. How do you ensure the quality and diversity of these additional options? If there is a method, could you elaborate further on the validation process?
﻿
Given the high construction cost of the benchmark, is it possible to reduce human effort through automated data generation or other technical means? For instance, could models be used to create new visual inputs or options?

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
3

### Summary
This paper introduces a new benchmark MMMU-Pro for more accurately and rigorously assessment of a model’s true multimodal understanding and reasoning capabilities by filtering the question that can be answered by LLM dicrectly, adding more options and vision-only input. Experimental results using MMMU-Pro show a significant performance drop in existing model. This paper provides a  more rigorous evaluation tool,

### Strengths
1. The proposed benchmark assesses multimodal models’ understanding and reasoning capabilities in a more rigorous method.
2. The data collection pipeline are confidential due to the engagement of human.
3. Experiments are comprehensive, assessing current model's performance more accurate.

### Weaknesses
1. As the main contribution of this paper is a benchmark. The authors should provide more data analysis on the collected MMMU-Pro and give more insightful conclusion.
2. Apart from benchmark, the novelty is limited. This paper just tests many models on the proposed benchmark ( I don't think the exploration
 of OCR prompts and COT reasoning can be accounted as a novelty). On the other hand, the dataset collection pipeline is something more like engineering. That's the reason why I think this paper's novelty is limited. Of course, this is not the only criterion for determining whether this paper can be accepted. The proposed benchmark does make a contribution to MLLMs' understanding and reasoning capabilities. My main concern is that the workload and contribution may not be sufficient to be accepted by such a top-tier conference. I may change my rating based on the rebuttal.

### Questions
1. Can the author privode more insight anaysis on the proposed benchmark?
2. It's good to see the author's effort about how to improve the open-source model's performance on MMMU-Pro.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper MMMU-Pro presents an upgraded version of MMMU. MMMU-Pro improves MMMU via (1) filtering out questions answerable by text-only models, (2) augmenting candidate options, and (3) introducing a vision-only input setting where questions are embedded within images. All these are reasonable upgrades upon MMMU, and the paper also presents some nice insights based on existing models' performances. But the upgrades seem to be incremental and not sure whether the efforts are enough for one standalone work.

### Strengths
1/ The paper is easy to follow

2/ The three upgrades upon MMMU are reasonable and can better examine the MLLM's capability in making sense and reasoning about vision

3/ The paper evaluates a wide range of existing MLLMs and share some insights.

### Weaknesses
1/ Fig 1 compares almost 20 models, is it necessary to compare so many models? We can probably derive similar conclusions & insights based on comparing just some representative models. In this era, new MLLMs come out every a few days. I understand from the view of maintaining a benchmark/competition, it is good to be inclusive while seems not helpful to have giant table and figures like Table 1 and Fig 1.

2. Despite the 3 upgrades are reasonable, they seem to be incremental given the wonderful work of MMMU. I am not sure whether the efforts in this pro work are enough for one standalone paper. It could be just a nice technical report; while I guess if people want to pass it, I am also fine.

3. The last upgrade of vision-only input is interesting and the analysis of OCR/COT are good. While it feels to be only just scratching the surface, and if the authors would like to create a more solid work, I would expect some deeper contributions e.g. design new model/algorithm that can better make sense of such purely vision input question, create a training dataset that can power existing MLLM to do much better job on this task.

### Questions
Please see the above weakness

### Soundness
2

### Presentation
3

### Contribution
2
