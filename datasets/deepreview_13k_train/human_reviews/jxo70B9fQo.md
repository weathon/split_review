# Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
LLM self-evaluation relies on the LLM's own ability to estimate response correctness, which can greatly improve its deployment reliability. 
In this research track, we propose the {\bf Chain-of-Embedding (CoE)} in the latent space to enable LLMs to perform output-free self-evaluation.
CoE consists of all progressive hidden states produced during the inference time, which can be treated as the latent thinking path of LLMs. We find that when LLMs respond correctly and incorrectly, their CoE features differ, these discrepancies assist us in estimating LLM response correctness.
Experiments in four diverse domains and seven LLMs fully demonstrate the effectiveness of our method. Meanwhile, its label-free design intent without any training and millisecond-level computational cost ensure real-time feedback in large-scale scenarios.
More importantly, we provide interesting insights into LLM response correctness from the perspective of hidden state changes inside LLMs

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose the Chain-of-Embedding (CoE) in the latent space to enable LLMs to perform output-free self-evaluation, and find that when LLMs respond correctly and incorrectly, their CoE features differ, these discrepancies assist us in estimating LLM response correctness.

### Strengths
It is quite interesting to discover that the hidden states of LLMs can be utilized to estimate the LLM response correctness without any label, which inspires me a lot.

Moreover, it is also reasonable to treat the progressive hidden states as the latent thinking path of LLMs, leading to the following
assumption: CoE discrepancies may happen when LLMs generate correct and incorrect responses.

Overall, it is quite inspireable paper and give the readers a lot of insights on the thinking system of LLMs

### Weaknesses
I donot think this paper have any significant weaknesses

### Questions
My only question is,  there are a a lot of interesting findings in this paper, such as
1. Hidden states to estimate the LLM response correctness without any label
2. CoE discrepancies may happen when LLMs generate correct and incorrect responses,
how can these findings be used to improve the reasoning accuracy of LLMs during pre-training or post-training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a metric for label-free LLM self-evaluation, that utilizes the observed discrepancies in progressive hidden states when LLMs generate correct and incorrect responses. Intuited by the cognitive phenomenon in human thinking, the authors measure the CoE discrepancy in the two sets, responding correctly and incorrectly. Based on the obvious discrepancies in Magnitude and Angle, the authors give the two metrics, CoE-R and CoE-C. Finally, the authors achieved SOTA in various datasets and backbone LLMs. Furthermore, there are other analyses in many aspects, e.g., efficiency and multilingual scalability.

### Strengths
1. The literature of this paper is comprehensive.

2. The exploration is structured and natural. From intuitive cognitive phenomenon to observation, the authors verify the assumpted discrepancy between correct and incorrect generation. Then, the authors proposed a metric and then demonstrated the effectiveness of the metric. The idea is well-founded.

3. The authors verify their proposed metrics on various backbones and datasets.

4. The authors give a detailed analysis of many aspects.

### Weaknesses
1. Missing critical statistic analysis of discrepancies. The foundation of the proposed metrics is based on the existence of the discrepancy between correct and incorrect generation. However, only visualizing this discrepancy is not enough. A rigorous statistical analysis, including measures of central tendency, variance, and statistical significance tests (e.g., t-tests or ANOVA), is needed to validate the observed differences. The lack of such analysis makes it difficult to ascertain whether the observed discrepancies are statistically meaningful or simply due to random variation.

2. Why is the targeted task self-evaluation? self-evaluation is a task that seems appealing but is quite ambiguous and questionable; even if the reviewer reads the reference paper cited by authors for self-evaluation, there is no task definition of self-evaluation. In the authors' presentation, based on the experiment setting and references cited by the authors, self-evaluation is highly associated with uncertainty estimation, but the authors don't mention their targeted method for uncertainty estimation; furthermore, the authors present self-evaluation as a potential method enabling evaluating LLM's responses without labels in the introduction section, which is associated with llm-as-a-judge and self-rewarding. There is a big gap between the two tasks. For label-free self-evaluation, I advise authors to compare their metrics with llm-as-a-judge or self-rewarding methods (label-based self-evaluation) in some instruction-following tasks, even not sota.

3. Missing verifying on some key datasets, for example, triviaQA and TruthfulQA, which have been tested in many previous works cited by authors;

4. Missing critical robustness analysis on adversarial samples, especially uncertainty estimation. The proposed method's sensitivity to adversarial perturbations is not explored, which is a critical aspect for real-world applicability. It is important to understand how the method behaves when the input is slightly altered, especially in the context of uncertainty estimation where robustness is paramount.

### Questions
a. How does this metric work? Is there a threshold to decide the classification using metrics? If so, what is this threshold?

b. In line 104, why does the average embedding at layer l represent the l-th sentence hidden state?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The Chain-of-Embedding (CoE) is a novel approach that allows LLMs to self-evaluate correctness by analyzing their hidden states during inference, forming a latent "thinking path." This label-free method reveals distinct patterns for correct and incorrect responses, enabling real-time, output-free accuracy estimation across various domains. CoE’s minimal computational cost and interpretability make it effective for large-scale applications.

### Strengths
1. CoE uses internal hidden states rather than output-based confidence, enhancing adaptability to new tasks without training data.

2. With millisecond-level computation, CoE scales effectively, offering quick feedback for large-scale deployments.

3. CoE provides insights into LLM decision-making by tracing hidden states, offering a transparent, human-like assessment of response correctness.

### Weaknesses
1. My major concern is the scenario and the necessity for the label-free scenario. If we limited the LLM query into only math question, commonQA questions, then the label-free scenario may not be necessary. A few-shot human labeling can achieve satisfied performance. The key reason for the label-free is the open-world scenario, which the query can be arbitrary from various domains.  It is impossible for us to label across queries with different purposes. Considering the open-world assumption, there are two following-up question as follows:  
1.1. The figure 2 and 3 try to distinguish the discrepancy between the positive and negative samples. When we consider the open-world assumption, there can be more questions with different distributions from a single domain, which may not be able to distinguish. 
1.2. The positive samples from different domains show different trajectories, is it possible for the method to distinguish them given queries from different domains

2. The motivation in the introduction part seems confusing. There is no evidence to indicate the correspondence between the human thinking path and LLM intermediate path. Moreover, there may many knowledge-intensive task may not need the thinking path. 

3. The evaluation part (especially how to identify the correctness) is not so clear to me. I would like to kindly ask the authors provide a more detailed explanation on it. 

4. The path length is related with the number of layer. I think an additional analysis on how the number of layer influence the performance of the proposed method could make the paper more solid.

### Questions
1. How does the proposed method handle distributional differences across open-world queries?

2. Can the method reliably distinguish trajectories across diverse domains?

3. What is the evidence for aligning human thinking paths with LLM intermediate paths?

4. How does layer count affect the method's performance?

### Soundness
3

### Presentation
3

### Contribution
2
