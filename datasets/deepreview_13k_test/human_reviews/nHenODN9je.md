# Preference Data Annotation with Guided Density Ratios

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Preference tuning of large language models (LLMs) relies on high-quality human preference data, which is often expensive and time-consuming to gather. While existing methods can use trained reward models or proprietary model as judges for preference annotation, they have notable drawbacks: training reward models remain dependent on initial human data, and using proprietary model imposes license restrictions that inhibits commercial usage.  In this paper, we introduce Guided Density Ratio, a training-free and highly effective method that leverages off-the-shelf LLMs for preference data annotation. Our approach uses the log-density ratio between a better-aligned LLM and a less aligned LLM as a reward signal. We explores 221 different LLMs pairs and empirically demonstrate that increasing the performance gap between paired LLMs correlates with better reward generalization. Furthermore, we show that tailoring the density ratio reward function with specific criteria and preference exemplars enhances performance across domains and within target areas.

In our experiment using density ratio from a pair of Mistral-7B models, Guided Density Ratio achieves a RewardBench score of 82.6, outperforming the best trained reward functions from same model class and demonstrating competitive performance against SoTA models in Safety (91.0) and Reasoning (88.0) domains. We use Guided Density Ratio to annotate an on-policy preference dataset with which we preference tune \textit{Llama-3-8B-Instruct} with SimPO. Using reward signals from two relatively weak models, our approach pushes Llama-3-8B to achieve a 37.4\% ($+$15.1\%) win rate on ArenaHard and a 40.7\% ($+$17.8\%) win rate on Length-Controlled AlpacaEval 2.0, along with a score of 8.0 on MT-Bench.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper interprets the use of a strong v/s weak LLM as a human preference proxy. However, their main contribution is designing prompt templates with relevant domain specific exemplars (IC examples) and domain specific system prompts - to show that the resulting density ratio is more helpful.

### Strengths
The paper does a good job in explaining their contribution, and the examples are helpful. The direction of LLM as a preference / human proxy is topical and being investigated by various groups - which makes it aligned to the venue.

### Weaknesses
I find the work to be an incremental advancement over previous discussions on using LLMs as a reward proxy. The key contribution of the work is the manually designed prompt templates, T(x), which are composed of system and in-context examples - both of which are domain dependent. The work's key argument is to favor a domain specific prompt design that influences density ratio - with limited discussions on why this template must work. 

Few questions to the authors : 
1. What is the cost of designing these templates? How can one extend this work to an arbitrary domain where the preferences may not be "safety". 
2. In line 048, authors say that human preferences can be complicated. How are the preferences anymore complicated or undefined when they they pen down the preferences as part of their system prompt. Can the authors point out to examples where these prompt templates helped with other user preferences not explicitly mentioned in the prompt. 
3. Can the authors compare the cost of prompt design with collecting more feedback? 
4. What are the guarantees that this prompt template won't work adversarially to the model. For instance, its possible that the system prompt conflicts with some preferences specified in the query. What are some alternatives to the system prompt that the authors considered? The authors provide some discussion in A.1, however, the following questions remain unanswered :  how did the authors generate SYSTEM1, 2... versions; what are the domain specific principles and how were those generated?; what other principles did the authors experiment with? Which principles, while "plausible" and "aligned" with typical human preferences did not yield expected results. 
5. Many a times IC examples have hampered model's performance. The authors discuss ICL example selection strategy in A.1, but the discussion seems to to justify the use of IC examples in their setup anecdotally. 
6. The argument for why a baseline calibration is needed (lines 205 - 211) seem anecdotal. Can the authors provide stronger theoretical / empirical result on what are the properties of this weaker model for such a calibration, and what must the relationship between weaker and stronger model be in the scope of their work.

### Questions
Please see Weaknesses section. 

I believe that addition of answers to the above questions can help with a stronger submission.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a scalable, training-free method for preference data annotation in large language models by using guided density ratios between pre-trained models. This approach, which employs domain-specific prompts and few-shot examples, enhances alignment in areas like safety and reasoning without requiring costly human feedback. The method achieves competitive results on benchmarks such as RewardBench and MT-Bench, demonstrating its potential as an effective and resource-efficient alternative for preference tuning in LLMs.

### Strengths
1. The results on RewardBench and other benchmarks demonstrate that the proposed method can compete with or even outperform larger, more resource-intensive models, making it a cost-effective solution for preference alignment.

2. The paper includes comprehensive experiments across multiple domains and benchmarks, providing robust evidence for the effectiveness of the method.

3. The paper introduces a scalable, training-free preference annotation method using density ratios, a concept that could significantly reduce the cost and time typically required for human feedback data collection.

### Weaknesses
1. While prompt-based guidance improves performance, designing effective prompts and in-context examples for different domains could be labor-intensive and may not generalize well across all tasks.

2. I think evaluation across different model size should be included. For example, including 7B, 13B, and 70B.

### Questions
1. Could the density ratio approach be adapted to work with multi-modal data, like vision language models / LLaVA, or is it inherently limited to language models?

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
The paper investigates the preference tunning in LLM and proposes the challenge that it depends on paired human feedback data and the collection is costly in time and resources. Then the authors propose a novel data annotation technique that improves the density ratio rewards annotation accuracy and enhances the effectiveness of preference tuning using a new annotated dataset.

### Strengths
+ The paper explores the challenge of data scarcity in preference tuning, a significant question in the LLM era.

+ The author proposes a novel data annotation technique based on the prompt density ratio, which has advanced community skills and tunning-free advantages.

+ Extensive experiments include multiple settings on the cutting-edged open-source and close-resource MLLM to improve the solidity of the paper.

### Weaknesses
- While the proposed prompt-based density ratio method exhibits some improvements, the design of prompt templates for system prompts and few-shot prompts is widely used in broad scenarios with less innovation.

- Prompt-density ratio compared to vanilla-density ratio decreases the model’s bias, but if the model itself with some bias, it will accumulate to the updated modal, it should expand some discussion about the difference of bias between source and target model.

- The experiment section should expand a paragraph to summarise the setting and the experiment description is unclear. While I was confused by some of the questions listed below. 

What is the generative reward in Table 1? 

Why the second to last only include safety and reasoning? 

Why are the results of NousResearch/Nous-Hermes-2-Mistral-7B-DPO not included in the Table, which is also an instruction-tuned model? 

Why is only one setting included with a base or without a base that corresponds to two different weak models?

Does the experiment include a domain-specific prompt that should also include the comparison?

- There is a lack of ablation studies on the functionality of system prompts and few-shot prompts.

- Some sentences contain long-tail expressions, and several equations need improvement, particularly by adding appropriate punctuation marks.

### Questions
- How to ensure the annotate quality in the prompt routing for category-specific prompts and preference tunning data creation?

### Soundness
3

### Presentation
3

### Contribution
2
