# ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Reasoning about Actions and Change (RAC) has historically played a pivotal role in solving foundational AI problems, such as the frame problem. It has driven advancements in AI fields, such as non-monotonic and commonsense reasoning. RAC remains crucial for AI systems that operate in dynamic environments, engage in interactive scenarios, or rely on commonsense reasoning. Despite substantial advances made by Large Language Models (LLMs) in various AI domains, their performance in RAC remains underexplored. To address this gap, we introduce a new diagnostic benchmark, \textsc{\datasetname}, which encompasses 8 domains and includes questions for up to 19 action sequences. This benchmark rigorously evaluates LLMs across six key RAC dimensions: \textit{Fluent Tracking}, \textit{State Tracking}, \textit{Action Executability}, \textit{Effects of Actions}, \textit{Numerical RAC}, and \textit{Composite Questions}. LLMs demonstrate average accuracy rates of 73.55\%, 65.63\%, 58.73\%, and 62.38\% on the former four dimensions, which are frequently discussed in RAC literature. However, the performance on the latter two dimensions, which introduce complex and novel reasoning questions, the average performance of LLMs is lowered to 33.16\% and 51.19\%, respectively, reflecting a 17.9\% performance decline. We also introduce new ramification constraints to capture the indirect effects of actions, providing deeper insights into RAC challenges. Our evaluation of state-of-the-art LLMs, including both open-source and commercial models, reveals challenges across all RAC dimensions, particularly in handling ramifications, with GPT-4o failing to solve any question and o1-preview achieving a score of only 18.4\%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ActionReasoningBench, which evaluates LLMs' ability to reason about actions and change in PDDL-based domains. The benchmark introduces novel ramification fluents which require deeper reasoning to infer correctly, such as fluents which are dependent on combinations of other properties, and other properties like "if object is at location a, it cannot also be at location b". The results show that LLMs predict the standard fluents well, but are almost completely failing at such ramification fluents.

### Strengths
- The paper studies an important but overlooked problem of evaluating RAC capabilities of LLMs in a systematic way, beyond measuring surface RAC. The paper demonstrates through the difference in performance on basic fluents and the ramification fluents, that this is indeed a weakness of current LLMs.

- The paper's conceptualization and discussion of ramification fluents is useful, and the benchmark has potential to lead to interesting new research such as entirely new models for RAC.

### Weaknesses
I have two main concerns with the paper in its current form:

- Organization: The organization of the paper could be improved, as the main results of the paper appears to be Table 5 (the ramification results), but these experiments are conducted on a smaller set of models and limited to free-answer. The experiments seem a bit incomplete. Other sections like "Performance across Fluent Categories" (l415) should be shown as table/figure. 
- Human baseline: It's difficult to gauge the human upper bound on the benchmark with ramifications, and I would suggest that a human baseline would offer a better way to contextualize the low numbers shown by LLMs.

### Questions
- In Table 3, are only the base fluents inclulded in the "Fluent tracking" category?
- Is my understanding correct that when you refer to "introducing ramification constraints", it indicates introducing the ramification fluents in the benchmark?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a reasoning benchmark for reasoning about actions and changes. The focus of this benchmark is specifically on tasks that require state tracking and commonsense, which often requires a full understanding of the current state. The paper aggregates this benchmark using the IPC advance planning competition challenge, by using a pipeline to convert them to natural language and testing it on the latest LLMs. The benchmark reveals headroom for LLMs in the context of state tracking, specifically when ramification constraints are incorporated in the challenge.

### Strengths
- The paper is a step forward towards producing a more challenging benchmark in the domain of reasoning about actions and changes, compared to the previous PlanBench and TRAC work. 

- It also incorporates additional metrics in state tracking that is not part of previous benchmarks. 

- The latest models are also thoroughly evaluated with a good sense of headroom, and will provide a meaningful resource for making progress in this domain.

### Weaknesses
 - Related work is poorly written. It doesn’t cover the nature of the dataset in the context of existing benchmarks (I had to read the other papers to get a good context). It was hard to identify why this benchmark was the right direction to continue as a benchmark. I highly recommend the authors to expand the related work section placing the contribution in context (particularly for readers like me, who don’t have the full context).

 - Regarding the benchmark itself, the paper doesn’t give enough details on how challenging the individual domains are. It is hard to judge the contribution of the paper well, without those details. Specifically, how were these tasks solved before LLMs were used for these domains? What progress have they made ? While LLMs can be a general model for these tasks, how would they different from building custom models for these tasks ?

Note: I still very much like this paper, and happy to increase the score if these points above are addressed well.

### Questions
- Why should an LLM alone be used to solve this and not in combination with other systems ? What aspects of the challenges in these individual domains are LLMs most suitable ? Could you please elaborate a bit on this ? 

- What are the current state-of-art (including non-LLM) methods for this ? How do LLMs perform in comparison to them ? 

- Are there any Insights into why numerical RAC performance doesn't seem to improve even after fine-tuning? I was wondering if it was because “number of possible states” is a well-posed problem ? Love to know the authors’ opinion on this 

- (Line 193) What are negative fluents ?

- What happens if we don’t convert the examples into natural language ?  Does the LLM perform any well at all in this task without the natural language conversion step ?

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
This paper introduces ActionReasoningBench, a benchmark for measuring LM reasoning on action sequences across multiple categories. The benchmark is created by adapting 8 planning domains from the International Planning Competition, and translating them into natural language using a combination of templates and language models. The natural language descriptions and questions are reviewed by annotators. The authors evaluate 4 models on these datasets: GPT-4o, Llama-8b-instruct, LLama-70B-instruct, and fine-tuned Llama-8b. They find that performance generally decreases as a function of action sequence length, and state-of-the-art LMs cannot solve the benchmark, performing particularly poorly on tasks that require numerical reasoning or a combination of other types of action-sequence reasoning (e.g. fluent tracking and action executability). Even GPT4 o1-preview struggles to perform well on inferring ramifications of actions.

### Strengths
A strength of this paper is in its comprehensiveness and quantity of analysis. The benchmark  explores many different aspects and ways of querying for action reasoning capabilities, and discovers many interesting trends. The dataset is very large and is able to identify reasoning capabilities which even the most state-of-the-art LLMs do not possess. The method for creating the dataset seems sound as there is a programmatic solution to these types of questions, and humans are used to validate paraphrases. The paper is overall clearly written.

### Weaknesses
1. The choices of tasks in the paper could be better motivated -- why are the 8 tasks present a representative survey of the important types of action reasoning? Why do we care about these 8 specifically? What are the consequences of LMs being able (or not able) to perform some of these types of reasoning? Why is numerical reasoning included (which is not fully related to action sequences), but not other types of reasoning (e.g. logical)?
2. Without a larger takeaway, this paper risks reading like simply a collection of empirical facts. This paper presents 7-8 separate takeaways in section 5, without too deeply investigating any single one. For example, what kind of errors do LLMs make on ramification fluents? What kind of intuition can we gain about LLMs and their limitations in reasoning from these errors. Having a more coherent high-level claim about all the takeaways from these results can be enlightening. Also having a table summarizing the limitations of LLMs in these 8 aspects could be useful.

### Questions
1. The use of Llama to generate question translations (into natural language) may affect the reasoning capabilities of LLMs, in particular requiring LLMs to use verbal reasoning skills to comprehend the questions. Are LLMs better at handling questions in natural language compared to templated?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new benchmark, ActionReasoningBench, to evaluate LLMs ability to reason about actions and change. This benchmark covers various RAC dimensions, including fluent tracking, state tracking, action executability, effects of actions, numerical RAC, and composite questions. Additionally, the authors introduce a new ramifications constrains to the reasoning task. The paper presents the evaluation of several sota LLMs across the proposed RAC dimensions proving that there is a significant margin of improvement for advanced LLMs such as GPT-4o and o1-preview.

### Strengths
- The paper is well written and easy to follow. 
- It provides a comprehensive evaluation framework for LLMs' RAC capabilities, covering a wide range of tasks and difficulties. This benchmark allows for a thorough assessment of LLM performance and identifies areas for improvement such as new key challenges and LLMs limitations.

### Weaknesses
 - I am not sure about the exclusive use of LLM to evaluate the free-form answers. It may introduce inaccuracies due to the limitations of language models. While the correlation between Llama-3.1-70B-Instruct and human evaluations is reported, it would be of interest to report evaluation from automatic metrics based on semantic similarity such as Bertscore (among others).
- The fine-grained methodology for evaluating RAC could be further enriched considering aspects such as causal reasoning (this is partially covered by “effects of actions”) and temporal reasoning (for example reasoning about concurrent actions).
- A short discussion beyond the examples provided in the appendix on how/why LLMs fail (with error analysis) the task would help better motivate the study beyond the performance in term of accuracy.

### Questions
Have you considered incorporating a combination of automatic evaluation metrics (e.g., BertScore) alongside the current evaluation?

### Soundness
3

### Presentation
3

### Contribution
3
