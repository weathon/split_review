# Adaptive Self-Supervised Learning Strategies for Dynamic On-Device LLM Personalization

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Large language models (LLMs) have revolutionized how we interact with technology, but their personalization to individual user preferences remains a significant challenge, particularly in on-device applications. Traditional methods often depend heavily on labeled datasets and can be resource-intensive. To address these issues, we present Adaptive Self-Supervised Learning Strategies (ASLS), which utilizes self-supervised learning techniques to personalize LLMs dynamically. The framework comprises a user profiling layer for collecting interaction data and a neural adaptation layer for real-time model fine-tuning. This innovative approach enables continuous learning from user feedback, allowing the model to generate responses that align closely with user-specific contexts. The adaptive mechanisms of ASLS minimize computational demands and enhance personalization efficiency. Experimental results across various user scenarios illustrate the superior performance of ASLS in boosting user engagement and satisfaction, highlighting its potential to redefine LLMs as highly responsive and context-aware systems on-device.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an Adaptive Self-Supervised Learning Strategy (ASLS) framework for dynamic, on-device personalization of large language models (LLMs). The framework includes two layers: a user profiling layer that gathers interaction data and a neural adaptation layer that fine-tunes the model in real-time based on this data, enabling responses tailored to specific user contexts.

### Strengths
1.	Studying on-device LLM personalization has significant practical application significance.
2.	The author claimed that the proposed method can achieve real-time model fine-tuning.

### Weaknesses
1. The quality of writing in the method section needs improvement. In particular, inconsistent use of symbols and lack of explanations make the methodology difficult to understand. It is recommended that the authors revise this section and include an illustrative diagram to improve readability.
2. Equation (2) indicates that the personalization approach in this paper still relies on label fitting, suggesting it has not eliminated the dependence on extensive labeled data as claimed in the introduction.
3. This paper's general approach looks like customizing personalized parameters for LLMs based on user interaction data, and this core idea seems quite similar to HYDRA [1]. What are the main innovations presented in this paper, and what are its advantages?
4. The readability of the experimental results and analysis is poor. The experimental tables are difficult to understand; for example, in Table 1, why do different methods correspond to different datasets? Regarding the analysis of experiments, the statement "Significant enhancements observed in user engagement metrics" does not provide a clear definition of what engagement metrics are.
5. There is a lack of comparison with some baselines in the experiments, such as [1].
[1] HYDRA: Model Factorization Framework for Black-Box LLM Personalization.

### Questions
See the Weaknesses section for the main questions. How does the proposed method ensure real-time model fine-tuning?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a Self-Supervised Learning method to update LLMs by user interaction data for personalization on-device. The model contains two layers, a user layer to generate uer presentation by interaction data and a fine-tuning adaptation layer for dynamic modelling. The method is verified on various datesets.

### Strengths
1. The paper focus on decreasing computation as personalizing based on LLMs on-device.
 2. The paper conducts experiments on multiple datasets from various domains.

### Weaknesses
1. The definition of on-device personalization is not clear in the paper.
2. The metrics are not explained and defined, the reviewer cannot know what is the objective of this paper.
3. The comparison is not fair according to Table1 which compare various methods under different datasets, and no explain of such setting is provided.
4. The explain of layers of the method is vague, the review cannot follow due to lack of explanation and connection between section3.1-3.3

### Questions
In addition to the weakness:
1. what are the metrics of Eval Metric 1 Eval Metric 2 Eval Metric 3 Eval Metric 4 Eval Metric 5?
2. What's the definition of engagement score, satisfication rate and Importance Score in the evaluation?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an adaptive self-supervised learning strategy (ASLS), which consists of a user analysis layer for collecting interaction data and a neural adaptation layer for real-time model fine-tuning.

### Strengths
**S1.** The problem of "dynamically personalizing LLMs" is interesting and valuable.  
**S2.** The authors claim that the method does not require extensive labeled data.

### Weaknesses
**W1.** Regarding the introduction section, it does not provide a clear motivation and the logic is somewhat unclear. For example, the fourth paragraph is very confusing, as it includes too many disparate elements—recommendation, multi-modal object recognition, and fairness.

**W2.** The connections between different parts of the method are also unclear, with issues of inconsistent notation. Additionally, there is no clear demonstration of how it better addresses the problem of dynamic updates; it still seems that updates are needed for each proposed module when new data appears.

**W3.** The experiments are also confusing. For example, in Table 1, why do different methods correspond to different datasets? How does this ensure fair comparison?

**W4.** It is not clear how the paper demonstrates self-supervised learning. According to equation (2), it still appears to be supervised learning.

**W5.** The selection of baselines may also need improvement. For instance, the chosen recommendation baseline, PALR, is not the current state-of-the-art LLM-based recommendation method.

### Questions
The writing in this paper needs improvement. Currently, I do not clearly understand how the method works, and the experimental setup is also confusing. See the details in the Weaknesses section.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Adaptive Self-Supervised Learning Strategies (ASLS) to address the challenge of personalizing large language models (LLMs) for individual users, particularly in resource-constrained on-device applications. Traditional personalization approaches often require labeled datasets and substantial computational resources. In contrast, ASLS leverages self-supervised learning for dynamic personalization, using a user profiling layer to gather interaction data and a neural adaptation layer for real-time model fine-tuning. This setup enables continuous learning from user feedback, aligning model outputs more closely with user-specific contexts while minimizing resource demands. Experimental results demonstrate ASLS’s effectiveness in enhancing user engagement and satisfaction, positioning it as a promising approach for creating responsive, context-aware on-device LLMs.

### Strengths
1. The paper focuses on a interesting and promising problem: On-Device LLM Personalization
2. The structure of the paper is reasonable

### Weaknesses
1. It's hard to understand the whole workflow because the paper lacks a workflow figure
2. Method is simple. Althought I approve simple but effective method, I can't get where is the "self-supervised learning" and can't understand why it is for "on-device LLM". This does not seem to be a method designed specifically for on-device LLM.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2
