# LUMOS: Towards Language Agents that are Unified, Modular, and Open Source

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
In this paper, we present LUMOS, **L**anguage agents with **U**nified formats, **M**odular design, and **O**pen **S**ource LLMs. LUMOS features a modular architecture consisting of planning, grounding, and execution modules built based on open-source LLMs such as LLAMA-2. The planning module decomposes a task into a sequence of high-level subgoals; the grounding module then grounds the generated subgoals to a series of low-level actions that can then be executed by the execution module. To obtain high-quality annotations for training these modules, we leverage LLMs to convert ground-truth intermediate reasoning steps in existing benchmarks into a unified format that can be used in the LUMOS framework. LUMOS achieves competitive or superior performance compared to the state of the art on a variety of complex interactive tasks. We observe: (1) LUMOS is competitive with the LLM agents that are 2 − 4× larger on maths tasks, and outperforms GPT-4/3.5-based agents on complex QA and web agent tasks; (2) LUMOS shows superior performance against open-source agent baseline formulations including chain-of-thoughts fine-tuning and unmodularized training; (3) LUMOS surpasses larger LLM-based agents on an unseen interactive task, WebShop, and achieves 5-10 reward improvement over domain-specific agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes LUMOS, Language agents with Unified formats, Modular design, and Open Source LLMs to solve complex tasks with planning, grounding, and execution modules fine-tuned from LLAMA-7B on high-quality annotations collected by leveraging LLMs to convert ground truth reasoning steps in existing benchmarks into a unified format. LUMOS achieves competitive performance with agents of larger size and outperforms GPT-4/3.5-based agents on complex QA and web agent tasks.

### Strengths
- The proposed modular framework is well-motivated.

- The converted dataset can contribute to training better small open models for complex tasks.

- The results show the proposed method is effective and promising for its generalizability on unseen tasks.

- The paper is well-written and presented clearly.

### Weaknesses
 - Why is LUMOS-O better than LUMOS-I on Math benchmarks?

- Some discussion on the performance-efficiency tradeoff between LUMOS-O and LUMOS-I would provide further insights.

- Figure 3 (a) in the Final planning module annotation "**No**, I will keep planning. Subgoal 2: Query the living
period of Jonathan Kaplan." Is that a typo?

- Some related work on modular language agents framework for complex tasks
  - _Cognitive Architectures for Language Agents_
  - _Building Cooperative Embodied Agents Modularly with Large Language Models_

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents LUMOS, a language agent framework built for open source LLMs with unified formats and modular design. LUMOS divide the framework into separate modules for planning, grounding and execution. The obtain high-quality annotations for training the modules, the authors leverage LLMs to convert ground truth intermediate reasoning steps in existing benchmarks into a unified format. LUMOS demonstrates competitive or superior performance compared to SOTA systems on a variety of interactions including web agent, math reasoning and complex QA.

### Strengths
1. The paper studies an important problem of developing language agents, and a unified framework and format is much needed in the field.
2. The overall description of the method is clear and easy to follow.
3. Experiment covers both regular fine-tuning setting, and generalization to unseen task.

### Weaknesses
1. My main concern is regarding the claim on LUMOS achieving superior performance than other LLM-based agents:
    1. LUMOS is trained on top of LLAMA-2, while some of the baselines are based on LLAMA. For example in Table 1, according to the latest results from AgentBench, updated vicuna-13B v1.5 based on LLAMA-2 now has 41.7 on WebShop, even outperform LUMOS. To make a fair comparison, I would recommend to keep it consistent across models, reporting both LUMOS and baselines with LLAMA, or update the baseline results to the version using LLAMA-2. This should also be made more clear in the paper.
    2. In most experiments, LUMOS is tuned with data from downstream tasks, while if I understand correctly other LLM baselines are tested under few-shot or in-context learning settings. If this is correct, it should be made more clear in the paper, and the comparison seem a little unfair.
2. With the baseline systems mostly evaluated under few-shot, I feel it is important to understand the efficiency of LUMOS and how well it generalizes. It is great that the authors have the generalization on WebShop, but I feel more emphasis on this direction, with additional few-shot experiments would be much better.
3. A modular design, in particular divide the agent into planning, grounding and execution has been studied in various previous works as well. This limits the novelty of the proposed method. Also there is some missing reference to relevant work, e.g., Saycan: Grounding Language in Robotic Affordances
4. Many of the baseline results are directly taken from results reported in other papers. While I understand that running experiments with LLMs are costly, this causes some in-consistency in the baselines that are compared in different datasets. And the comparison might also get affected by the implementation details of different papers.

### Questions
1. Is it true that most other baseline LLM agents are applied under few-shot / in-context learning setting?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new framework to train LLMs for certain tasks such as answering questions related to maths, textual comprehension and outputting actions for a website (click). The new framework has three parts (“modules”):

- “planning”, which converts a prompt to (simpler, but still human language-like) queries (“subgoals”), e.g. “Query the living period of Lowell Sherman”

- “grounding”, which converts the subgoals to “actions”: function-call type queries, e.g. “KnowledgeQuery(Lowell Sherman)”

- “execution”, which executes those actions

For both planning and the grounding phases (“modules”) GPT-4 is used to generate annotated examples for the given task at hand to train LLAMA-7B with.

Two versions are suggested: LUMOS-O (which goes through the above three parts/modules sequentially) and LUMOS-I (which iterates through each subgoal until the execution of that subgoal, the result of which is then used for the next planning the next subgoal).The framework is applied to the open source LLAMA 7B LLM and claims superior or competitive performance on larger LLMs without or with techniques to improve their performance such as Chain of Thought prompting, SelfInstruct, ReWOO-Planner-7B (an improvement of React) and for this claim provides experiment details on these tasks.

### Strengths
The paper proposes a new framework/pipeline to achieve better results with prompting LLMs in a nascent field, which could be seen as original.

Quality: The methodology of the paper is well-documented, the experiment section contains results on relevant datasets.

Clarity: the paper follows the ICLR formatting style, images are mostly clearly captioned, there is an attempt to place the work in the (very recent) literature. Large sections of the paper are easy to understand.

In terms of significance, using their particular setting a 7B-parameter open-source LLM outperforms larger LLMs queried by previous techniques.

### Weaknesses
Having said the above in terms of strengths, in my opinion the paper includes a fair bit of weaknesses.
The paper’s claim that LUMOS outperforms or is competitive compared to larger LLMs is not well justified by evidence. A list of issues are:
- F1-scores are not reported, and to the best of my knowledge that is the primary metric in this field of AI. While the paper focuses on task completion rates and average rewards, the absence of F1-scores makes it difficult to directly compare performance against other methods, especially those that utilize different evaluation metrics. This omission is particularly significant given that many established benchmarks and studies in the field rely on F1 as a core metric.
- The LLM is fine-tuned for the specific tasks (for subgoal and action generation), whereas the baselines use publicly available APIs at best, hence they are more general. This discrepancy in training methodology raises concerns about the fairness of the comparison. Fine-tuning on specific tasks can lead to significant performance improvements, and it is unclear whether the reported gains are due to the inherent superiority of the LUMOS framework or simply the advantage of task-specific fine-tuning.
- Unless I am mistaken: on GSM8K, ReWOO achieves 62.4% accuracy (as opposed to the reported ~38) in Xu et al. 2023 and is significantly better than LUMOS (50.5%). This discrepancy suggests a potential misinterpretation or misrepresentation of the baseline results, which undermines the credibility of the comparative analysis presented in the paper. 
- I could be wrong, but to me it looks like ReWOO trained a 7B model, they only used GPT-3.5 for the QA tool. I also cannot find the claimed LLAMA-7B results in Xu et al. 2023. Also, ReWOO-7B uses GPT-3.5-turbo as a QA tool, achieves 66.6% accuracy on StrategyQA, which is better than all LUMOS agents that used GPT-3.5-turbo as QA. These inconsistencies further highlight the need for a more thorough and accurate comparison against existing methods. The paper should clearly delineate the experimental setups of each baseline and provide a detailed justification for any deviations from the original implementations.
- Mind2Web baselines were not fine-tuned at all, hence comparing them to LUMOS is not that fair. Comparing a fine-tuned model against a zero-shot baseline introduces a significant bias. The paper should either compare against fine-tuned versions of the Mind2Web baselines or acknowledge the limitations of this comparison.
I also have concerns about the significance of this contribution. React and Self-Instruct defined ways to improve the performance of LLM agents with little to no fine-tuning, only publicly available API calls. The concept that large neural networks can be fine-tuned with additional task-specific training data for better performance on those tasks is fairly well-known in the community. 
In terms of clarity, the paper has a lot of typos, odd sentences and style issues that made it much more difficult to understand than it should have been. Although they ultimately did not affect the score of this paper, they were close to it. I will list some of the found issues below:
In the abstract: showd -> showed
Introduction
2nd paragraph: However, Lie et al… citations ideally should not be used as nouns.
Beginning of 3rd paragraph: There should be an introductory sentence to ask the question. Then instead of “to this end”” write to answer this question”
In Figure 1, the prompt should be included in the Figure.
End of 3rd paragraph: What are environment states? They are never defined.
4th paragraph: “[...] language agents to acquire these skills [...]” what skills?
2.2
2nd paragraph: “[...] part of grounding module’s input” -> the missing before grounding
2.2 and 2.3 general comment: the difference between LUMOS-I and LUMOS-O should be demonstrated with the same example for easier comprehension (e.g. with the Obama example)
Figure 3a right image:
<|user|> Should we keep planning?
<|assistant|> No I will keep planning.
Shouldn’t the user say “Should we stop planning?”
3.2
3rd paragraph
The subsequent conversation is constructed in the similar patterns. -> remove the
“We assume ourselves as user” -> as the user
“Tell the execution results” -> provide the execution results
“To planning module” -> to the planning module
4th paragraph
“[...] play a user role to provide the task” -> provide to what? Do you mean get/acquire/obtain?
“In the rest conversations” -> remaining, of rest of the
4.4
“Achieves 5-10 average reward than” -> odd sentence
“Than using Self-Instruct method” -> missing the
“Annotation is
 beneficial than” -> more beneficial
Related Work
“We notice that directly generating annotation with for training planning and grounding modules may introduce large number of errors” -> “We notice that directly generating annotations for the training, planning and grounding modules may introduce a large number of errors”
“LLMs transform the gold reasoning steps” -> I don’t understand what you mean, but I am fairly certain not what is written here

### Questions
The Self-Instruct paper lists a lot more related work. How are those related to the work presented in this paper?

In the Introduction this sentence is written: “Together, our proposed framework and unified model provides valuable resource and direction for advancing open-source interactive language agents.” (resource -> resources)

But it is never elaborated upon and you do not mention potential future work in the conclusion either.
What future work do you envision after this paper? How could the community successfully build on top of this new framework that was proposed?

What are the limitations of the work you suggested?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an overview of the LLM Agent architecture, with: planning, execution and grounding. The method is competitive for math, QA, and WebShop tasks with significantly smaller model size. The proposed framework is generally applicable to tasks where Language Models are used as an agent.

### Strengths
1. The paper demonstrated a solid framework for using smaller models as LLM agents.
2. The presentation of the paper is easy to follow and the figure is straightforward. 
3. I do appreciate the paper does some detailed ablations of the method, making it stronger.

### Weaknesses
1. My first question for the authors is: the agent framework has been discussed quite often (there have been some follow-ups since the ReACT paper came out). Although the author claimed they are mostly based on close-source API based models (not the open-source ones), it seems the architecture is quite similar?
2. Why on math tasks, LUMOS-O significantly outperforms LUMOS-I while in the other two tasks, the results seem to reverse? Some more analysis on the error patterns would be preferred to give some more insights.
3. Why LUMOS in general outperforms UA-T? Does this mean some tasks jointly fine-tuned together can result in some conflict? Does this imply that we should train multiple smaller models each fine-tuned for a specific task?

### Questions
Please see above for comments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
