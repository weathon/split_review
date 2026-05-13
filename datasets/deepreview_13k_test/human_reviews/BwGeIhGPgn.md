# Evaluating Information Gathering Abilities of Large Language Models with QuestBench

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Large language models (LLMs) have mastered a wide range of reasoning tasks, with an underlying assumption that the tasks are well-specified for LLMs to reach solutions.
In reality, queries and instructions to LLMs often contain incomplete or underspecified information.
Therefore, LLMs need to be able to actively ac-quire missing information by asking clarifying questions, ideally seeking the minimally sufficient piece of information.
To assess whether LLMs possess this ability, we construct QUESTBENCH, a set of underspecified reasoning tasks that can be solved by asking at most a single question.
We frame the tasks as constraint satisfaction problems with missing variable assignments, where the exact model response cannot be determined unless certain variables’ values are acquired.
This framework specifically targets tasks where uncertainty stems from missing information, rather than semantic ambiguity in language.  QUESTBENCH includes (1) Logic-Q: Logical reasoning tasks where one proposition is missing, (2) Planning-Q: PDDL planning problems where the initial state is partially observed, and (3) GSM-Q: Grade school math problems where one variable assignment is missing.
Each task presents multiple choices of possible questions, only one of which is correct.
We evaluate Gemini and GPT-4o models and find that they achieve 20 – 30% accuracy in both zero-shot and few-shot settings. When evaluating GPT-4-o1on a subset of our data, we find that it is only 41 – 44% accurate, despite using state-of-the-art inference-time reasoning techniques.
When investigating characteristics of QuestBench, we find that LLMs struggle with tasks that are computationally expensive for traditional search-based CSP solvers. Our analyses reveal a negative correlation between LLM accuracy and solver runtime complexity, suggesting that LLMs may share similar limitations to CSP solvers

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Most practical problems require humans to operate in uncertain settings where uncertainty might arise from either ambiguity or underspecification of the problem. It then becomes imperative to obtain relevant information by asking clarification questions. While this is a common knowledge in human conversations, with the advent of LLMs, it is essential to evaluate their capacity to reason about uncertainty and actively acquire the necessary information for completing tasks. Existing benchmarks are limited in their scope and do not cover complex logic, planing, and math reasoning. The subjective nature of the problem where the information to acquire might vary based on individuals and population pose further challenges.
Towards that the authors present a collection of question asking benchmarks, that they call QuestBench, that cover logic, planning and grade school math. They specifically focus on problems that can be formulated as constrain specification problems (CSP) and, within that, limit the scope to problems that are underspecified. Their benchmark - QuestBench - leverages existing datasets - SimpleLogic, PyperPlan, and GSM-Plus and converts them into 1-sufficient CSP where the size of the smallest sufficient set (of variables required to solve the problem) is 1. They then evaluate some of the proprietary models on these benchmarks and find that while these models perform well in identifying missing information in GSM problems, they struggle with logic and planning problems. They also correlate this performance with different measures of search complexity and hypothesize that the LLMs might possess search skills similar to breadth-first search or brute-force approaches, which become less effective as the search space expands.

### Strengths
The ability of LLMs to ask clarification problems is important to advance their state-of-the-art and application to solving complex practical problems that are riddled with uncertainty. The authors attempt to address an important problem and take a step forward by presenting a quantitative benchmark to evaluate LLMs.
Through evaluation of top models, they highlight their inability in identifying missing information, especially in complex planning and logic reasoning tasks while doing relatively better on math. I also appreciate that the authors go a step further to correlate this performance with different measures of complexity. Their hypothesis around the limited search capability of current LLMs, derived from this correlation, seems intuitive and leads to a call for action for the LLM research community.

### Weaknesses
While the motivation is strong, by limiting the scope to 1-sufficient CSPs, I feel the scope is significantly limited. At least it is unclear how much of the practical problem space does this cover. 
I also found some gaps in writing that make it difficult to follow. For instance, the challenges around identifying necessary information to acquire and the lack of ground truth would have been better understood with some examples. The notion of constraint satisfaction problems is loosely defined. It is unclear what class of practical problems might fall in this category vs not.
The construction details of the datasets is omitted from the main paper and is delegated to the appendix. At least a brief description is expected in the main paper.
Overall, I think I am concerned about the limited scope of the benchmarks.

### Questions
I would encourage the authors to consider a larger scope beyond 1-sufficient CSPs or clearly articulate why this is a significant enough problem space.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces QUESTBENCH, a new benchmark designed to evaluate the ability of large language models (LLMs) to handle underspecified tasks by asking clarifying questions. QUESTBENCH frames these tasks as constraint satisfaction problems with missing information, focusing on scenarios where uncertainty arises due to missing variables rather than semantic ambiguity.
The benchmark consists of three categories:

1.	Logic-Q: Tasks involving logical reasoning where a missing proposition's value is needed.
2.	Planning-Q: Planning problems with undefined initial states requiring additional observations to reach a goal.
3.	GSM-Q: Grade school math problems lacking critical information for a solution.

The paper evaluates models like Gemini Pro 1.5, GPT-4o, and GPT-4-o1, finding significant room for improvement in their information-gathering abilities, with accuracy ranging from 20% to 44%.
Key contributions include:

1.	A framework for evaluating under-specification in LLMs.
2.	The creation of the QUESTBENCH benchmark for assessing LLMs' information-gathering skills.
3.	Analysis of LLM performance on QUESTBENCH, highlighting areas needing enhancement.

Overall, QUESTBENCH provides a structured approach to study how LLMs manage missing information and clarify underspecified instructions.

### Strengths
1. **Problem Formulation**: The paper introduces a novel benchmark, QUESTBENCH, designed to specifically assess the ability of LLMs to ask clarifying questions for underspecified tasks. This focus on missing information in constraint satisfaction problems distinguishes it from previous benchmarks. The use of constraint satisfaction as a method to frame underspecified tasks is an innovative approach, providing a structured way to evaluate models.
2. **Advancing LLM Capabilities**: By highlighting the current limitations of LLMs in handling underspecified tasks, the paper opens avenues for future research and development in enhancing model interactivity and problem-solving under uncertainty.	
3. **Well-Defined Categories**: The definition of transforming Logic-Q, Planning-Q, and GSM-Q categories into a CSP problem is clear and logical, making the benchmark easy to understand.

### Weaknesses
1. **Limited Scope of Evaluation**:
* Details: While the paper evaluates several state-of-the-art models, it may benefit from testing a broader range of LLM families, including smaller or emerging models, to provide a more comprehensive understanding.
* Suggestions: Expand the evaluation to include open-source models like LLaMA, Qwen, Mistral, or close-sourced model like Claude 3.5
2. **The evaluation metrics are not clearly present**: In Table 2, the author mentions Language model accuracies at predicting the right question. But how do you define if a generated question is accurate?
3. **Lack of insights to handle underspecified problems**:
* First, the authors have shown numerous works that aim to actively seek clarification through questions, as noted in Lines 47-48. However, the author does not evaluate these methods, merely presenting the scores of some basic prompting strategies. Therefore, it is hard to say whether the low performance on QUESTBENCH is caused by inappropriate prompting.
* Second, this paper hardly shows the way to overcome the underspecified task. Though the major goal is this paper is for evaluation purpose, offering some insights into overcoming such a challenge could enhance its contribution

### Questions
1. In Table 2, how do you define if a generated question is accurate?
2. Can you show the results of the methods mentioned in Lines 47-48?

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
3

### Summary
The paper investigates the capabilities of LLMs to ask clarifying questions when dealing with underspecified tasks. These tasks often lack sufficient information to generate an accurate response without additional clarification. To evaluate this, the authors introduce QuestBench, a benchmark of three tasks (Logic-Q, Planning-Q, and GSM-Q) that require one clarifying question to resolve underspecified queries. 

The study tested several SOTA models on QuestBench and found performance to be suboptimal. The findings reveal a gap in LLMs' ability to gather necessary information, particularly for complex logic and planning tasks.

The authors contribute by presenting a constraint satisfaction framework focused on evaluating underspecification and perform analyses on model performance correlations with reasoning mechanisms. Their results suggest LLMs struggle with larger solution spaces and deeper search requirements, showing potential limitations in the models' reasoning capabilities and highlighting areas for future improvements in question-asking and information-gathering skills in LLMs.

### Strengths
1. The paper presents a benchmark specifically aimed at evaluating the information-gathering abilities of LLMs when faced with underspecified tasks. The benchmark is well-designed and covers three types of tasks, including logic reasoning, planning, and math problems.

2. The paper provides various evaluations and insights into the types of reasoning mechanisms LLMs may currently lack, which could be useful in future improvements of the models.

### Weaknesses
1. The tasks in QuestBench are constructed to be solvable with only a single missing piece of information, which simplifies the challenges of real-world queries. This limited complexity limits the benchmark's applicability to real-world scenarios.

2. A potential weakness of the paper is the lack of natural language tasks in QuestBench. The current benchmark primarily includes structured tasks, such as logic reasoning, planning, and math problems, which lack the variability and richness of natural language interactions. This limits QuestBench’s ability to evaluate LLMs in more practical, real-world contexts where queries are often open-ended or conversational. Including natural language tasks would provide a more comprehensive assessment of LLMs’ information-gathering abilities, as these tasks better reflect the types of ambiguous and underspecified instructions encountered in everyday language use.

### Questions
1. In L415, why use four-shot settings.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on the ability of large language models to actively request information from users when faced with semantically clear but underspecified questions. To evaluate this ability, the authors created QuestBench, a benchmark of underspecified tasks that can be solved by asking at most one question. This dataset includes three tasks:

- Logic-Q: Logical reasoning tasks where one proposition is missing
- Planning-Q: PDDL planning problems where the initial state is underspecified
- GSM-Q: Grade school math problems where one variable assignment is missing

The GSM-Q task was manually annotated. The authors evaluated existing models such as GPT-4o, Gemini, and o1. They found that even o1, which has significantly better reasoning abilities, struggles to perform well on these tasks.
This research highlights the challenges large language models face when dealing with underspecified questions and their ability to ask for clarification.

### Strengths
1. The information-gathering ability is important for large language models. The authors provide a dataset to evaluate this capability.
2. The definitions of key concepts and the methods for constructing the dataset are described very clearly.
3. The authors evaluated several advanced models (GPT-4o, Gemini, o1) and conducted some correlation analyses between search complexity and LLM accuracy.

### Weaknesses
1. While some models were evaluated, there was a lack of valuable findings and insights. Specifically,
- What are the potential reasons why the existing model lacks the ability of "information gathering"? Is it data, algorithm, or other factors? 
- In what direction should we work further to improve the model's ability in this aspect?
- For the failure cases of the models, we can add some statistical analysis to summarize the types and causes of failures.

Thus, I suggest adding experiments about the following points that could be helpful:
- Select a subset of failure cases, summarize the reasons for model failure, and analyze the reasons that led to the failure.
- Discuss ways to improve the model's information-gathering capability. If possible, it would be better to conduct experiments to verify the feasibility of the methods.

2. There are important details missing in the evaluation process. Specifically, assessing the model's accuracy is a non-trivial task. This is because the correct behavior is to request the missing information in the underspecific question. However, the authors don't seem to describe this point in the paper. Overall, the author needs to provide details regarding how to judge whether the question asked by the model is correct.

### Questions
Could you please tell me how the accuracy was evaluated in this paper? Was it evaluated manually by humans or using an LLM? What were the specific evaluation criteria?

Could you please share some insights on how to improve the information-gathering capability of the model based on the evaluation results?

### Soundness
3

### Presentation
2

### Contribution
2
