# CMMLU: Measuring massive multitask language understanding in Chinese

- Decision: Reject
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
As the capabilities of large language models (LLMs) continue to advance, evaluating their performance is becoming simultaneously more important and more challenging. This paper aims to address this issue for Mandarin Chinese in the form of CMMLU, a comprehensive Chinese benchmark that covers various subjects, including natural sciences, social sciences, engineering, and the humanities. We conduct a thorough evaluation of more than 20 contemporary multilingual and Chinese LLMs, assessing their performance across different
subjects and settings.
The results reveal that most existing LLMs struggle to achieve an accuracy of 60\% even, which is the pass mark for Chinese exams. This highlights that there is significant room for improvement in the capabilities of LLMs. Additionally, we conduct extensive experiments to identify factors impacting the models' performance and propose directions for enhancing LLMs. CMMLU fills the gap in evaluating the knowledge and reasoning capabilities of large language models in the Chinese context

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced CMMLU, a benchmark designed to assess the multi-task language understanding capabilities in Chinese. The authors ran the benchmark on various open-source and API-based models and performed extensive analysis to identify several factors that impact model performance and propose actionable directions for enhancing LLMs.

### Strengths
1. The CMMLU benchmark is very comprehensive, covering a wide range of subjects.

2. The paper addresses the significant gap in evaluating Chinese language and cultural context understanding, a critical aspect given the dominance of English-centric benchmarks.

3. The work can be very useful for Chinese LLM community.

4. The paper provides an in-depth analysis of the performance of various LLMs, under different evaluation settings.

5. The paper also provides very interesting findings in terms of chain-of-thought, SFT/RLHF, etc.

### Weaknesses
1. A human baseline is lacking for the benchmark. It'd be great to see what level of accuracy human can get on the benchmark.

2. There's no discussion on the difficulty distribution of questions in each subset. A well designed benchmark or test should cover questions spanning all difficulty levels from the easiest to the hardest. It's unknown what the difficulty distribution is for each subset. If difficulty distribution is very centric (for example, all samples in a subset are all very easy or very hard), then models will be likely to get them all correct or all wrong, which cannot provide a **smooth** estimation of the model's ability. A non-smooth evaluation can also be related to the phenomenon of "emergent ability". See me question 2.

### Questions
1. In page 1, "numerous tasks within CMMLU have answers speciﬁc to China, which may not be universally applicable or considered correct in other regions or languages.". Do you think it would be a good idea to have questions **with answers that are not generally agreed upon worldwide** in the datasets? How many samples of this kind are there in the benchmark?

2. When you evaluate open-source models, have you seen "emergent ability" in terms of model's size? More precisely, are there some tasks that can only be solved by a large model? If so, then what are the difficulty distributions of those tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced a fully Sinicized Chinese test benchmark, CMMLU, specifically designed to evaluate the knowledge and reasoning capabilities of language models in a Chinese context. CMMLU covered 67 topics ranging from basic disciplines to advanced professional levels, with answers specific to the Chinese region.

### Strengths
The paper conducted extensive experiments, including on the proprietary GPT-4 (even though OpenAI consistently updated GPT versions without much fanfare). 

The content was detailed and held significant practical value for the Chinese domain.

### Weaknesses
However, an LLM passing professional exams doesn't necessarily indicate its true capabilities, raising concerns about construct validity. 

The crisis of research replication based on language models was severe, and the evaluation methods had limitations. 

Assessing the political biases inherent in the language models presented in the benchmark was challenging and required naturalistic observation.

### Questions
1. One concern I had was that this Chinese test benchmark did not include evaluation criteria for Chinese machine translation. Many studies are now focusing on evaluating the generalized machine translation capabilities of LLMs. Given the extensive work the authors did on this benchmark, how did authors view the evaluation criteria for Chinese translations?

2. The outputs of LLMs were uncertain. Even a minor change in a prompt could lead to variations in the output. In light of this benchmarking paper, how did the authors perceive this issue? How should the benchmark address the inherent unpredictability of LLMs?

3. Typically, the Chain-of-Thought method had proven successful on LLMs. However, this paper concluded that the Chain-of-Thought was not effective in enhancing model performance, which contradicted the feedback received from practical use of LLMs with the Chain-of-Thought. A more detailed analysis and explanation were requested.

4. LLMs demonstrated strong In-Context Learning capabilities. It would be worth exploring whether adding appropriate knowledge to the prompt could answer benchmark questions to validate the benchmark's effectiveness.

5. It was known that LLMs would respond cautiously to safety questions when posed in English. However, when asked in less common languages, they might provide bolder answers, potentially bypassing restrictions. Did the CMMLU safety benchmark consider addressing this phenomenon?

6. How did the authors ensure that the proposed test benchmark was free from data contamination?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a  Chinese multi-task benchmark dataset CMMLU  for better evaluating the language understanding ability of LLMs in the context of Chinese. Compared to previous benchmark datasets, besides the general tasks, CMMLU consists of many Chinese-specific tasks.

Meanwhile, this work has also conducted a lot of experiments to check the performance of the 20 most popular non-Chinese-specific and Chinese-specific LLMs.  The experimental results provide a good reference for developers to choose the LLM in the context of Chinese.

### Strengths
1. CMMLU is specifically designed for evaluating Chinese LLMs. It not only consists of general natural language understanding tasks, but also some region-specific tasks such as Chinese driving rules, food culture, and qualifications. Thus, CMMLU can better reveal the real LLM performance in the Chinese scenarios.

2. This work invested many efforts in collecting non-publicly available questions to reduce the possibility that the collected questions have already been learned by LLMs.

3. This work has evaluated many multilingual LLMs and many Chinese LLMs at the same time. Meanwhile, the authors also compare the best Chinese LLM Baichuan2-13B with the best LLM GPT4 by subjects. This comparison can answer the question of why we need Chinese LLMs/benchmarks in the Chinese scenarios.

4. Many deep analyses have shown many interesting and useful findings.

### Weaknesses
1. Although this work is technically sound and solid, CMMLU lacks enough novelty or other special contributions.  The major highlight is that CMMLU consists of some Chinese-specific tasks. This is more or less like an A+B incremental work.

2. All questions are formatted as multiple-choice with 4 choices.   This may make it difficult to comprehensively test the performance of LLMs.

3. The experimental methodology of most experiments is language-agnostic.  It only simply compares general LLMs vs Chinese LLMs and non-Chinese-specific tasks vs  Chinese-specific tasks.  I think more experiments should be deeply combined with the Chinese cultural and Chinese linguistic characteristics.

4. This work needs to analyze the correlation between the performance reported by CMMLU and the real performance measured in the representative downstream NLU tasks. Otherwise, it is difficult to determine whether CMMLU can reflect the NLU performance of a LLM.

### Questions
Besides the questions in Weakness, there are some minor questions:

1) What form will this dataset be released in the future?

2) Besides the Chinese-specific tasks and data source, is there any other Chinese-specific feature that has been considered in CMMLU?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
