# CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 8, 5

## Abstract
Recent developments in large language models (LLMs) have been impressive. However, these models sometimes show inconsistencies and problematic behavior, such as hallucinating facts, generating flawed code, or creating offensive and toxic content. Unlike these models, humans typically utilize external tools to cross-check and refine their initial content, like using a search engine for fact-checking, or a code interpreter for debugging.
Inspired by this observation, we introduce a framework called \modelt that allows LLMs, which are essentially ``black boxes'' to validate and progressively amend their own outputs in a manner similar to human interaction with tools. 
More specifically, starting with an initial output, \modelt interacts with appropriate tools to evaluate certain aspects of the text, and then revises the output based on the feedback obtained during this validation process.
Comprehensive evaluations involving free-form question answering, mathematical program synthesis, and toxicity reduction demonstrate that \modelt consistently enhances the performance of LLMs.}.\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces CRITIC, a method for improving  the outputs of language models by leveraging external feedback from various tools. The idea is to generate an initial output with the language model and then refine this output using feedback from an external tool, such as a Python interpreter, search engines, or toxicity detection APIs. Notably, this approach relies solely on in-context learning without the need for specialized training. Results across various tasks, including question answering, mathematical reasoning, and toxicity reduction, show that CRITIC improves over baselines.

### Strengths
- The experiments demonstrate the effectiveness of the proposed approach across a diverse set of tasks, indicating its potential to significantly improve the performance of large language models (LLMs).

- Utilizing external feedback as a means of improving LLM outputs is practical. The simplicity of the approach is a plus, as it facilitates widespread application.

### Weaknesses
 - The primary concern with this work is its novelty. Several studies have previously demonstrated that external feedback can be instrumental in correcting LLM outputs. In fact, there is existing work within each domain addressed in this paper, such as Self-Correct ([1], using external APIs), Self-Ask ([2], employing a search engine), and Self-Debug ([3], via a Python interpreter). Notably, Self-Debug and Self-Ask have a striking resemblance to CRITIC but are not referenced.


- The settings that rely on an oracle are somewhat idealistic, and detract from the core message of the paper. It may be more appropriate to move these results to an appendix (as done by other works) to facilitate a clearer understanding.




### Questions
- The emphasis in Table 1 seems inconsistent. For instance, the AmbigNQ EM score of 50.0 is highlighted for Text-Davinci-003, but it is not the highest. Is this a bug or am I missing something?

- Regarding the GSM task in a non-oracle setting, it appears that feedback from the interpreter is limited to syntactic correctness. Given the improvements, it suggests that many of the programs were initially syntactically wrong. Is this the case?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a framework called CRITIC that enables large language models (LLMs) to self-verify and self-correct their outputs by interacting with external tools. The authors demonstrate the effectiveness of CRITIC in improving the performance of LLMs across multiple tasks, including free-form question answering, mathematical program synthesis, and toxicity reduction. The paper highlights the importance of external feedback in promoting the ongoing self-improvement of LLMs.

### Strengths
1) The paper introduces a novel framework, CRITIC, which addresses the limitations of LLMs by allowing them to verify and correct their outputs through interaction with external tools.

2) The authors provide comprehensive evaluations of CRITIC on different tasks and datasets, demonstrating its consistent performance improvement over baseline methods.

3) The paper highlights the crucial role of external feedback in the self-improvement of LLMs and emphasizes the unreliability of LLMs in self-verification.

### Weaknesses
1) I think this is a good paper. The motivation is strong: utilizing external feedback to enhance the model's ability. However, some recent studies [1] reported that large language models cannot self-correct themselves.  I acknowledge that [1] did not involve external tools, which is different from CRITIC's setting and it is a paper after CRITIC which is not necessarily be included, but it would be more comprehensive to include a discussion with these new studies in such a fast-moving field.

2) How much of the additional costs? Since calling external tools costs money. The authors should report the cost for each experiment.

3) In Appendix C.2, an important work active-prompt [2] should be included, which applies uncertainty estimation to chain-of-thought prompting.

### Questions
How much of the additional costs? Since calling external tools costs money. The authors should report the cost for each experiment.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a framework called CRITIC to progressively validate and revise the output based on the feedback from tools. Six different external tools are used including Knowledge base, code interpreter, Text APIs, Wiki, Calculator and Search Engine. Evaluations are done on free-form question answering, mathematical program synthesis, and toxicity reduction. CRITIC was shown to have superior performance on these benchmarks compared to strong baselines including CoT, Self-Consistency, ReAct, and PoT.

### Strengths
1. LLM Tool Use is a very timely research topic, and it is an important research area to use external feedback for the self-improvement of LLMs. This paper covers a wider range of tools compared to many prior works which typically employ one single type of tools.
2. The results are rather strong with universal improvements across most tasks evaluated with several different model families and sizes.
3. The ablation against CRITIC w/o Tool shows the importance of external feedback from Tools, which is an important learning for the community.
4. The paper is very well written and is easy to understand with comprehensive comparisons to strong baselines.

### Weaknesses
Error analysis is missing on what are the failure modes after using Tools for feedback.

### Questions
1. It is unclear how important each Tool is to each task. Such analysis will provide further insight into where the improvements come from.
2. The authors used different sampling config for the experiments for different tasks: e.g. p=0.9 was used for section 4.3 which is different from p=0.5 in 4.1 and 4.2.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The papers proposes CRITIC, a framework for composing programs involving LMs self-correcting themselves using external tools. The authors conduct experiments with question answering, program synthesis and toxicity reduction show that CRITIC consistently improves the performance of LLMs.

### Strengths
1. The paper is written clearly and easy to follow.
2. I found the comparison with ReAct interesting, i.e. the role of parameter knowledge vs language feedback.

### Weaknesses
1. I'm not convinced the CRITIC framework is novel enough to count as a contribution. The idea idea of using natural language feedback [1, 2, 3, 4] that guides LMs in revising their responses is pretty old as is the idea of using tools [5,6]. I agree the authors provide a nice unifying framework and some new downstream tasks (e.g. toxicity with PerspectiveAPI), but these don't seem to be pass the bar for ICLR. 

2. The authors don't compare with other frameworks endowing LMs with self-correction and tool use, like the ones listed above.

3. I think the claim that tool use "mimic[s] human thinking and behavior" is overblown. Humans use think and work with tools very differently, typically not through a text-only interface.

### Questions
How does the paper compare with other frameworks endowing LMs with self-correction and tool use?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
