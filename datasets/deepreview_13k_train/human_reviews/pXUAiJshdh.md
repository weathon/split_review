# SciKnowEval: Evaluating Multi-level Scientific Knowledge of Large Language Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Large language models (LLMs) have gained increasing prominence in scientific research, but there is a lack of comprehensive benchmarks to fully evaluate their proficiency in understanding and mastering scientific knowledge.
To address this need, we introduce the SciKnowEval benchmark, a novel framework that systematically evaluates LLMs across five progressive levels of scientific knowledge: \textit{studying extensively}, \textit{inquiring earnestly}, \textit{thinking profoundly}, \textit{discerning clearly}, and \textit{practicing assiduously.} 
These levels aim to assess the breadth and depth of scientific knowledge in LLMs, including memory, comprehension, reasoning, discernment, and application.
Specifically, we first construct a large-scale evaluation dataset encompassing 70K multi-level scientific problems and solutions in the domains of biology, chemistry, physics, and materials science.
By leveraging this dataset, we benchmark 26 advanced open-source and proprietary LLMs using zero-shot and few-shot prompting strategies. The results reveal that despite the state-of-the-art performance of proprietary LLMs,   there is still significant room for improvement, particularly in addressing scientific reasoning and applications. 
We anticipate that SciKnowEval will establish a standard for benchmarking LLMs in science research and promote the development of stronger scientific LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper constructs a benchmark to evaluate LLM's scientific knowledge and tests many LLM's performance on the benchmark.
Specifically, the benchmark is designed based on five levels: Studying extensively, Enquiring earnestly, Thinking profoundly, Discerning clearly, and Practicing assiduously. The five levels are based on an ancient Chinese book.

The benchmark is collected from existing literatures, existing QAs, and science databases.

### Strengths
1. This is a multi-level benchmark covering multiple disciplines. Thousands to tens of thousands of questions are collected at each level. It could be comprehensive.
2. This paper compares many LLM's performance on the benchmark.

### Weaknesses
1. Although with a good starting point, it is unclear whether the five levels listed in this paper truly reflect how humans think and understand this world. The five levels are from an old Chineses book, but it is unclear whether it has been tested by modern cognitive science. I would suggest the authors to find cognitive science findings to support to classification into the five levels.
2. It is not persuading how the data collected can fully represent the five levels. Particularly, level 4 is only about safety. But is safety a necessary step for the learning process? It seems the 5 levels are a mixture of different requirements, but not focused on reasoning levels. I would suggest the authors to provide a clear difference on the five levels, and also the why it is necessary to classify them to five levels: there's no need to add more complexity if it is not necessary. 
3. The insights are a bit limited from the paper. The discussions in section 4.3 do not seem surprising. It is unclear what knowledge can be learned from the paper. For example, a takeaway knowledge could be how fundamentally are the difficulties and challenges differ in five levels? And LLMs can be adapted to deal with the challenges?

### Questions
See above

### Soundness
3

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
The paper proposes a new SciKnowEval benchmark to evaluate the LLMs across five levels of scientific knowledge, including knowledge memory, knowledge comprehension, knowledge reasoning, knowledge discernment, and knowledge application. The benchmark includes 70k multi-level scientific problems and solutions in the domains of biology, chemistry, and material science. The paper generates benchmarks from three sources: new QAs from the literature corpus, existing QAs, and scientific databases. The paper controls the quality first through LLMs, then through human evaluation, and finally, post-screening by LLMs. The paper tests and ranks 26 LLMs. The paper also shows some interesting findings.

### Strengths
1. The paper is clearly written. Each section has figures or tables to help the reader understand how datasets are constructed. 
2. The experiment is comprehensive. The paper provides a summary for each level of task. The paper also lists four interesting findings in the discussion section, which can be useful in future research directions.
3. The paper released data and code. In the Appendix, it provides additional results, detailed model descriptions, data sources, and sample prompts.

### Weaknesses
1. Some differences between the five levels are not very clear. For example, in Table 3, I did not see a very clear difference between L3 and L4. Additionally, from the definition of section 3.1, it seems that L4 and L5 are very close. The whole level categorization seems to be a little bit artificial. It might be better to create some LLM-based model/human reasoning process instructions to categorize different levels to ensure generalization ability.
2. The paper seems to only provide a ranking for the benchmark. It might be hard to generalize into additional new models.
3. The paper mainly tests 0-shot and 3-shot. Incorporating some additional strategies such as RAG, etc. Given the paper still has half page, the paper can move some of its appendix to the main paper.

### Questions
1. How do we determine the level of each task? Are there some standard, replicable instructions?
2. Can you provide more explicit criteria or examples that distinguish between each level?

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
4

### Summary
This work introduces a scientific benchmark called SciKnowEval for evaluating Large Language Models (LLMs) in scientific topics. Various sources have been used such as literature, existing QAs, and scientific databases. Based on the generated benchmark, 26 LLMs are evaluated in 5 levels of scientific knowledge which are memory, comprehension, reasoning, discernment, and application.

### Strengths
- The paper is well-written and easy to read.
- Extensive examples and experiments are presented.
- The paper provides a valuable benchmark for evaluating LLMs in scientific topics.

### Weaknesses
 - Various sources, such as literature, existing QAs, and scientific databases, have been used, but the questions included in the dataset are generated from LLMs. This might entail risks of hallucination.  
- While methods for evaluating these questions are included, these rely greatly on LLMs, as well. Only 5% of the questions are assessed by a human expert. This might not be sufficient for ensuring safety. Perhaps, it would be helpful that domain experts review a larger sample of the generated questions, 
- The experiment results of the 26 LLM comparisons are also rated based on a specific LLM. This can lead to potential biases that could be introduced by using a single LLM for rating.

### Questions
- What are some possible limitations of this work? 
- How was it determined that 5% was an appropriate sample size for human evaluation?
- Why GPT-4o was chosen to rate LLMs on level 5 - knowledge application? Were there other solutions, such as multiple LLMs, considered?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents SciKnowEval, a novel benchmark framework designed to assess the scientific knowledge capabilities of large language models (LLMs). Its distinctive five-level knowledge philosophy encompasses a broad spectrum of knowledge, ranging from knowledge memory to knowledge utilization. The dataset is meticulously curated from diverse sources and employs a combination of LLM screening techniques and sampled human evaluation to ensure data quality and efficiency. Through the evaluation of both proprietary and open-source models using SciKnowEval, the paper demonstrates that sota models still have considerable room for improvement in their scientific knowledge capabilities.

### Strengths
The dataset curated by the authors encompasses various facets of scientific knowledge, allowing for the evaluation of models in specific aspects of science. This enables a more granular understanding of how models perform at different levels, from knowledge awareness to knowledge application. The dataset's size is relatively significant within its domain, and the quality control measures employed, involving both human involvement for sampled questions and LLM screening for all questions, enhance efficiency while maintaining credibility.

### Weaknesses
While the benchmark aims to assess scientific reasoning abilities, it's crucial to acknowledge that QA-like tasks might not be comprehensive enough to evaluate models' scientific reasoning capabilities, even with categorized levels. Assessing models' scientific reasoning capabilities may require more complex setups, including tool usage, task planning, and end-to-end experiment conducting. It's worth mentioning these limitations in order to provide a more nuanced expectation for readers. For example, the authors can add a paragraph or short description as a limitation section, acknowledging that while their benchmark provides valuable insights, fully assessing scientific reasoning may require more complex setups. This would help set more accurate expectations for readers about what the benchmark can and cannot evaluate.

Nitpicks:
Make sure left quotation marks are used correctly, such as in table A10.

### Questions
Can you provide some clarification on Appendix A7:

Are the figures of 2.1% and 0.2% referring to the low-quality rate with the same standard?

Do these numbers represent the rates before and after LLM post-screening?

If so, why is the 2.1% described as "ultimate" when the 0.2% seems to be the final number after post-screening?

### Soundness
3

### Presentation
3

### Contribution
2
