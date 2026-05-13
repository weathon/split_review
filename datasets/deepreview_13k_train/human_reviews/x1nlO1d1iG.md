# CogMath: Evaluating LLMs' Authentic Mathematical Ability from a Cognitive Perspective

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
As large language models (LLMs) exhibit potential in solving complex mathematical tasks, increasing attention has been directed toward constructing benchmarks to evaluate their mathematical capabilities. However, existing benchmarks are either limited to specific task types (e.g., long-text problem understanding) or rely solely on a coarse measure of answer accuracy, making them insufficient for assessing a model's authentic mathematical proficiency. In this paper, we propose CogMath, which provides a comprehensive assessment of LLMs' mathematical abilities based on human cognitive processes. Specifically, inspired by cognitive theories, CogMath formalizes the reasoning process into 3 stages that align with human cognition: problem comprehension, problem solving, and solution summarization, and encompasses 9 fine-grained evaluation dimensions from perspectives such as numerical calculation, knowledge, and counterfactuals. In each dimension, to carry out a scientific evaluation, we develop an ``Inquiry-Judge-Reference'' multi-agent system, where the Inquiry agent generates inquiries that assess LLMs' mastery from this dimension, the Judge agent ensures the inquiry quality, and the Reference agent provides correct responses for comparison with the LLMs' actual performances. A LLM is considered to truly master a problem only when excelling in all inquiries from the 9 dimensions. In experiments, we evaluate 7 mainstream LLMs by applying CogMath to three benchmarks, which cover the full K-12 mathematical curriculum. The results reveal that the authentic mathematical capabilities of current LLMs are overestimated by 30-40%. Moreover, we locate their strengths and weaknesses across different stages/dimensions, offering constructive insights to further enhance their reasoning abilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work introduces a CogMath framework that consists of nine agents to evaluate the mathematical reasoning ability of large language models from the perspective of comprehension, problem solving and solution summarization. 

Specifically, in the comprehension stage, the agents attempt to rephrase, disrupt (permute word ordering), remove condition and add condition of the original question. In the problem solving stage, the agents attempt to conduct analogical reasoning, numerical transformation and knowledge refinement (reshape the semantics of 'half') of the original question. In the solution summarization stage, agents attempt to question the information in the intermediate steps of the solution, and conduct backward reasoning of the question. The experimental results demonstrate that the abilities of current strong LLMs on GSM8K and MATH are overestimated by 30-40% by the calibration of those agents. Besides, CogMath may not serve as an effective prompt-based reasoning enhancement and the problem difficulty and lengths in MATH are negatively correlated with the pass rates in CogMath.

### Strengths
This work includes a CogMath framework that could be helpful in evaluating the math reasoning abilities of LLMs more robustly, and covers several dimensions that may introduce perturbation to the stability of reasoning.

### Weaknesses
It is not easy to imagine how a handful of agents included in CogMath can be generalized to more challenging questions. For example, how does the backward reasoning being feasible in mathematical proofs. The knowledge redefinition only limits its scope to 'half' and the questions contain the word, where works like FRoG (Li et al. 2024) includes richer quantifier-based variants of GSM8K. It is not surprised to see that the current figures of LLMs in reasoning is not a stable display, but attempts like one-time numerical transformation might make it more robust, but only marginally. Besides, I didn't find enough evidence regarding efforts to make sure the agents faithfully finish their jobs.

This work also collects MExam. However, I know nothing about it from the contents.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a multi-agent framework, CogMath, to evaluate the mathematical abilities of LLMs from a cognitive perspective. CogMath breaks down mathematical problem-solving into 3 stages: problem comprehension, problem solving, and solution summarization with nine evaluation dimensions. CogMath generates test samples cross multiple cognitive perspectives using a multi-agent system and reveals that current LLMs' math capabilities are overestimated, which demonstrates the strengths and weaknesses of different models at different evaluation dimensions.

### Strengths
- Comprehensive evaluation across nine dimensions can enhance the current math benchmarks.
- Extensive experiments with multiple representative LLMs demonstrate the limitations of current LLMs on math reasoning capabilities.

### Weaknesses
 - CogMath uses LLMs to construct test samples and evaluate the model-generated answers across multiple dimensions. However, the correctness of generated test cases and the evaluation quality can be a major concern. It would be helpful to add human evaluation on the generated test samples and the judging process.
- The performance degradation can be a regular case instead of an interpretation of overestimation, as the CogMath test questions can be harder than the original questions after processing across multiple dimensions.

### Questions
How can the inquiry agents ensure that they generate good questions that meet the dimension requirements? Is there any filtering process involved?

### Soundness
2

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
4

### Summary
This paper proposes a benchmark for comprehensively evaluating the mathematical abilities of LLMs by examining three cognitive reasoning stages: problem comprehension, problem solving, and solution summarization. Experiments indicate that we may overestimate the capabilities of current LLMs, primarily due to their excessive imitation of superficial reasoning patterns.

### Strengths
1.	A comprehensive and scientific benchmark that deeply investigates the flexible reasoning of LLMs is essential for the community.
2.	The authors consider nine dimensions across problem comprehension, solving, and solution summarization, which aids in identifying the main challenges faced by current models.

### Weaknesses
1.	While this work addresses cognitive mathematical dimensions comprehensively, I have a question regarding the motivation. Why do the authors believe that previous works introducing perturbations into existing benchmarks are task-specific?
2.	More details are needed about the dataset construction procedure, including how the judge agent is used to ensure the quality of $q_i$, how multiple reference agents are negotiated to finalize the answer, and which foundation models are utilized behind these agents. Specifically, the process for ensuring the quality of the generated questions $q_i$ across different dimensions needs further clarification. The role and implementation of the judge agent, including its prompting strategy and criteria for approving or rejecting generated questions, should be detailed. Furthermore, the mechanism for answer finalization, particularly when multiple reference agents are involved, requires a more thorough explanation. The specific models used for these agents should also be explicitly stated.
3.	For Figure 2, it would be clearer to replace the dimension index with the dimension name. Additionally, for Figure 3, it would be more straightforward if each group of bars represents the same model.
4.	In Section 4.6, the current experiment uses a one-shot setting. Have the authors considered a nine-shot setting, where each demonstration represents one dimension?
5.	In Section 4.7, how are the five tiers of difficulty defined?
6. In Table 1: Should $21 be 21?

### Questions
Please refer to the weaknesses section

### Soundness
3

### Presentation
3

### Contribution
3
