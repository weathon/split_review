# Evaluating Hallucinations in Chinese Large Language Models

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
In this paper, we establish a benchmark named HalluQA (Chinese Hallucination Question-Answering) to measure the hallucination phenomenon in Chinese large language models. 
HalluQA contains 450 meticulously designed adversarial questions, spanning multiple domains, and takes into account Chinese historical culture, customs, and social phenomena. 
During the construction of HalluQA, we consider two types of hallucinations: imitative falsehoods and factual errors, and we construct adversarial samples based on GLM-130B and ChatGPT.
For evaluation, we design an automated evaluation method using GPT-4 to judge whether a model output is hallucinated.
We conduct extensive experiments on 24 large language models, including ERNIE-Bot, Baichuan2, ChatGLM, Qwen, SparkDesk and etc. 
Out of the 24 models, 18 achieved non-hallucination rates lower than 50\%. 
This indicates that HalluQA is highly challenging.
We analyze the primary types of hallucinations in different types of models and their causes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a benchmark named HalluQA to measure the hallucination phenomenon in Chinese LLMs. HalluQA contains 450 adversarial questions, covering various Chinese historical cultures, customs, and social phenomena. Both imitative falsehoods and factual errors are considered. GPT-4 is integrated into an automated framework to judge whether a model output is hallucinated. Extensive experiments on 24 large language models are presented, and18 achieved non-hallucination rates lower than 50%, showing that HalluQA is quite difficult. Some insights on causes are also provided.

### Strengths
1. The authors made serious efforts in conducting a comprehensive study on hallucinations in Chinese LLMs.

2. Some interesting insights are provided. 

3. It is important to establish some benchmark for studying hallucinations in Chinese LLMs, and this work is quite timely in this sense.

### Weaknesses
The novelty of this work is not very clear to me. The results are kind of expected.

### Questions
1. Can the authors clarify the unique novelty of this work? On the conceptual and technical levels?

2. Is any part of the results particularly surprising to the authors?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a benchmark called HalluQA, which aims to measure the hallucination phenomenon in Chinese large language models. HalluQA consists of meticulously designed adversarial questions that cover various domains and take into account Chinese historical culture, customs, and social phenomena. The authors identify two types of hallucinations: imitative falsehoods and factual errors, and construct adversarial samples accordingly with LLMs. An automated evaluation method using GPT-4 is designed to judge whether a model's output is hallucinated.

### Strengths
This paper built an adversarial evaluation benchmark aligned with the Chinese-specific context

### Weaknesses
The details of human expert evaluations are not provided in this paper, so it is difficult to determine the reliability of its high correlation with GPT-4 evaluations. Furthermore, a richer variety of LLMs can be used to generate examples, ensuring coverage of various forms of hallucination and fairness of evaluations.

### Questions
1. In Figure 4, the non-hallucination rate performance of GPT-4 is not optimal. Is it appropriate to use it for evaluating the existence of potential issues?
2. In the GPT-4 automated evaluation method, if the temperature of the GPT-4 evaluator is set to 0, are its outputs still random? And how does the voting part work if the outputs are deterministic?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A Chinese hallucination question-answering dataset named HalluQA is introduced for evaluating hallucination issues in large Chinese language models. The paper also provides a detailed description of the dataset's construction process and evaluation methodology.The experimental results demonstrate that all models exhibit non-hallucination rates of less than 70% on HalluQA, highlighting the dataset's challenging nature. The paper also discusses the primary types of hallucinations exhibited by different models and offers recommendations for model improvement.

### Strengths
At present, there is a significant difference in capabilities between open-source Chinese large models and English large models. Meanwhile, there are fewer people focusing on hallucinations in Chinese large models. This paper introduces a Chinese dataset for hallucination benchmarking and evaluates and analyzes current Chinese large models. It is of great significance. Meanwhile,this paper has ample experiments, and the data presented in the text is also very sufficient.

### Weaknesses
1、Based on the Figure 2 included in the work, question examples  look not natural. For example, in real world scenario, no one would ask a question like “?”  In short, the reviewer has doubt about the similarity between such generated queries and human written queries. Although I know this is to ask difficult questions to test LLM, is this kind of question really meaningful?

2、There is limited description of how the human filtering is performed. Is there any training process for those annotators? Quantitatively, how much data are removed in the process? Why are they being removed? Is there a list of examples for removed cases? Are more than one annotators working on the same datapoint? What is the agreement?

3、Regarding the evaluation issue, as a reviewer, what I would like to see more is a practical offline evaluation method. As we know, the GPT4 API is very expensive, and using GPT4 to evaluate the illusion of other LLMs does not seem feasible from a practical application perspective.

### Questions
Could you clearly introduce factors such as the price of using GPT4 evaluation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
