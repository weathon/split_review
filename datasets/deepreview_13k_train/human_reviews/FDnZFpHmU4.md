# Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Large language models (LLMs) exhibit varying strengths and weaknesses across different tasks, prompting recent studies to explore the benefits of ensembling models to leverage their complementary advantages. However, existing LLM ensembling methods often overlook model compatibility and struggle with inefficient alignment of probabilities across the entire vocabulary. In this study, we empirically investigate the factors influencing ensemble performance, identifying model performance, vocabulary size, and response style as key determinants, revealing that compatibility among models is essential for effective ensembling. This analysis leads to the development of a simple yet effective model selection strategy that identifies compatible models. Additionally, we introduce the \textsc{Uni}on \textsc{T}op-$k$ \textsc{E}nsembling (\textsc{UniTE}), a novel approach that efficiently combines models by focusing on the union of the top-k tokens from each model, thereby avoiding the need for full vocabulary alignment and reducing computational overhead. Extensive evaluations across multiple benchmarks demonstrate that \textsc{UniTE} significantly enhances performance compared to existing methods, offering a more efficient framework for LLM ensembling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel ensembling approach, UNITE (Union Top-k Ensembling), that efficiently integrates large language models (LLMs) by focusing on the union of top-k tokens from each model rather than aligning the full vocabulary. It seeks to improve the computational efficiency and effectiveness of LLM ensembles by addressing key issues of compatibility, vocabulary size, and response styles. The authors propose a model selection strategy to identify compatible models, limiting the influence of incompatible LLMs on the ensemble's performance. Experimental results across multiple benchmarks validate the benefits of UNITE in enhancing performance, reducing latency, and decreasing the computational burden.

### Strengths
- The paper identifies compatibility challenges in LLM ensembling and focuses on top-k tokens, aligning this strategy with empirical evidence that vocabulary alignment often introduces computational inefficiencies. 
- The authors conduct extensive experiments on multiple models and benchmarks, analyzing factors like vocabulary size, response style, and latency. The results support UNITE’s superiority in maintaining high performance while minimizing latency and token manipulation.
-  The proposed determine-then-ensemble strategy offers a generalizable framework for selecting compatible models, making the findings applicable to real-world LLM applications that require efficient model collaboration.

### Weaknesses
 - While the paper addresses task-specific challenges, it could benefit from deeper exploration into why certain tasks (like MMLU) see greater performance improvements than others. Further insight into how task characteristics impact ensembling effectiveness would add depth to the analysis. Specifically, the paper lacks a detailed analysis of the types of questions or sub-tasks within MMLU where the ensemble approach shows the most significant gains. It would be beneficial to understand if the improvements are concentrated in specific subject areas or question formats, which could provide clues about the underlying mechanisms of the ensemble's success. For example, does the method perform better on knowledge-based questions versus reasoning-based questions within MMLU?
- The model selection process relies on response style consistency and performance alignment within a 10% range, which may limit scalability when dealing with a large pool of candidate models. The method would benefit from a more automated or quantitative metric for determining compatibility. The current approach requires manual inspection of response styles, which is not scalable. A more rigorous approach, such as using a similarity metric on the embedding space of the responses, or a metric that quantifies the level of agreement between the models, would be more appropriate for large-scale model selection. Furthermore, the 10% performance alignment criteria seems arbitrary and lacks a theoretical justification. A more principled approach would involve analyzing the performance distribution of candidate models and selecting models based on statistical significance.
- While UNITE is evaluated across standard datasets, some benchmarks like GSM8K and TriviaQA may not fully capture the diverse range of LLM applications. Including more varied tasks could strengthen the argument for UNITE’s general applicability. The paper should consider incorporating tasks that assess different aspects of LLM capabilities, such as creative writing, code generation, or complex dialogue. The current benchmarks primarily focus on question-answering and reasoning, which may not fully represent the breadth of LLM applications. Expanding the evaluation to include tasks with different input and output modalities would provide a more comprehensive assessment of the method's generalizability.

### Questions
- Could you provide more theoretical support or intuition for why limiting alignment to the top-k tokens effectively enhances ensemble performance? How does this approach balance between accuracy and computational efficiency at a probabilistic level?
- How does UNITE handle models with markedly different response styles in practice? Would introducing a preprocessing step to standardize response formats (e.g., for tasks like QA or summarization) enhance compatibility?
- Since UNITE is partially motivated by efficiency, adding a comparative breakdown of memory and latency for each method would clarify the computational trade-offs involved. Including charts or tables that detail average and worst-case latency per token would help underscore UNITE’s operational benefits.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper identifies and tests three hypotheses about importance factors that influence the performance of logit-based LLM ensembles: performance discrepancy, vocabulary size differences, and stylistic response differences, and provides guidelines for choosing models to ensemble with. The authors propose UNITE, an ensembling method that uses the top-k logits from each model, and show that it outperforms numerous ensembling baselines while being significantly cheaper.

### Strengths
- The paper presents concrete empirical conclusions about what factors are actually important for ensembling (performance gap, response style) or not (vocabulary size difference.)
- It presents UNITE, a novel top-k union ensembling approach that drops the computational overhead tremendously by using the top-k tokens of each model instead of the full vocabulary, and that obviates the need for full vocabulary alignment.
- UNITE significantly outperforms the baselines (LLM-Blender, DeePen, GAC) in average accuracy across six popular benchmarks for question-answering, reasoning, and knowledge.  
- The paper is clear and well written.

### Weaknesses
 - The analysis in Conclusion II on vocabulary size differences is restricted to English language tasks. It may benefit from a discussion of multilinguality, where tokenization might be less consistent between models, potentially impacting the conclusions drawn. For instance, models trained on different languages or using different tokenization algorithms might exhibit more significant performance variations due to vocabulary mismatches than what is observed in the English-only experiments.
- In Conclusion III the paper identifies differences in response style as a major problem for ensembling models. The proposed solution of limiting longer responses to 2x the length of shorter ones would benefit from theoretical justification. A robust solution to this problem which enables ensembling of models with different response styles would be ideal, as the current approach limits the practicality of the method. The current approach does not address the underlying issue of stylistic variation, and may lead to suboptimal results if the truncated responses lose crucial information. Furthermore, the 2x length limit seems arbitrary and lacks a clear rationale.

### Questions
Does the optimal value of k for the top-k tokens vary across tasks and domains? Is there a principled way to determine k?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed an LLM ensemble method, which is to ensemble among only top-k tokens probability.

### Strengths
1. It includes good analysis and preliminary experiments for LLM ensembling.
2. Based on the preliminary analysis, they reduce the vocabulary for the previous method into the top-k selection for the model ensembling.

### Weaknesses
1. I believe the experiments should include the efficiency compared to the previous approach.
2. It seems, in theory, that including the whole vocabulary should work better, although maybe marginally or at least the same compared to top-k, since it includes the whole picture of the token distribution. I am questioning your experimental results because top-k is better in every dataset, which logically cannot be the case.

### Questions
Like Weaknesses#2 above, can you provide reasons or analysis why the top-k approach is better in performance than the whole vocabulary on performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Paper has two main contributions:

1. Presents a thorough analysis of features affecting ensemble performance: bade model performance gap, vocabulary size, and response style consistency.
2. A new ensembling method, UNITE, that focuses on combining only the top-k tokens instead of the entire vocabulary. The method is efficient in runtime and shows a high performance across multiple benchmarks.

### Strengths
1. UNITE’s token-level aggregation without full vocabulary alignment is an innovative method which reduced computational needs and making ensembling more efficient.
2. Empirical results are shown over a concrete set of benchmarks.
3. Their focus on model selection strategy brings up insightful practical guidelines which are very useful in practice.
4. They present clear results comparing latency against existing methods.

### Weaknesses
1. Lack of analysis on possible limitations or settings or benchmarks where topk-k token alignment fails to improve base models perf.
2. Figures and tables could have more detailed captions with information to be self-contained. (ex figures 4,5 and 6)
3. Figures and plots' font size are very small. Consider increasing the font size to assists readers.

### Questions
1. Do you have an insight about why increasing k beyond 10 does not improve perf? I think this result is counter-intuitive, and needs more analysis.
2. What is the impact of base model perf difference when using UNITE?

### Soundness
3

### Presentation
3

### Contribution
3
