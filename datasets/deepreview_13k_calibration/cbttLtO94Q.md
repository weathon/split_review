# How to Evaluate Reward Models for RLHF

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
We introduce a new benchmark for reward models that quantifies their ability to produce strong language models through RLHF (Reinforcement Learning from Human Feedback).
The gold-standard approach is to run a full RLHF training pipeline and directly probe downstream LLM performance.
However, this process is prohibitively expensive.
To address this, we build a predictive model of downstream LLM performance by evaluating the reward model on proxy tasks. 
These proxy tasks consist of a large-scale human preference and a verifiable correctness preference dataset, in which we measure 12 metrics across 12 domains.
To investigate which reward model metrics are most correlated to gold-standard RLHF outcomes, we launch an end-to-end RLHF experiment on a large-scale crowdsourced human preference platform to view real reward model downstream performance as ground truth.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Preference Proxy Evaluations (PPE), the first reward model benchmark explicitly connected to real-world human preference performance after RLHF. Unlike benchmarks like RewardBench that primarily perform reward evaluations, PPE facilitates investigation into which reward model metrics correlate most closely with RLHF outcomes.

Studying the impact of reward models on post-RLHF model performance is important. This paper involves significant work on this topic. Although I am inclined to accept it, there are still some important shortcomings (see the **Weaknesses**). I hope the authors can address my concerns.

### Strengths
- This paper addresses an important topic: the effectiveness of a reward model should ultimately be assessed by the performance of LLMs after RLHF. The study offers valuable insights into the evaluation of existing reward models.
- The paper includes extensive experiments and evaluates models using real-world human preferences.

### Weaknesses
 - The study employs DPO as the RLHF algorithm to evaluate post-RLHF performance. However, the offline DPO algorithm may face generalization issues, particularly when the reward model is trained on a limited set of preferences. Utilizing an online PPO algorithm, which allows for iterative policy updates based on ongoing reward feedback, would offer a more robust and comprehensive evaluation of various reward models. This is crucial because the performance of a reward model should be assessed not only on its ability to predict preferences on a static dataset, but also on its capacity to guide the policy model toward better performance during the RLHF process. The current offline approach might not fully capture this dynamic interaction, which is essential to support the authors’ core claim of being “the first reward model benchmark explicitly linked to post-RLHF performance.”
- The paper utilizes Llama-3.1-8B-Instruct as the base model for RLHF, which presents two potential concerns: 1) The paper should explore a broader range of base model scales, including both smaller and significantly larger models, rather than exclusively using the 8B model. This is important because the effectiveness of reward models and their correlation with post-RLHF performance might vary across different model sizes due to varying inductive biases and learning capacities. 2) Llama-3.1-8B-Instruct itself has undergone DPO RLHF training, which could confound the results. The pre-existing RLHF alignment might interact with the new reward models in unpredictable ways. I recommend that the authors use a purely SFT-trained Llama-SFT model as the base model to isolate the effect of the new reward models.
- The paper would benefit from more detailed descriptions and discussions regarding Figure 4. For example, it should provide intuitive explanations for why metrics from RewardBench fail to reflect post-RLHF preference performance. Specifically, the paper should delve into the potential reasons why reward models that perform well on RewardBench do not necessarily translate to improved performance after RLHF. This could involve analyzing the types of preferences captured by RewardBench versus those that are important for effective RLHF, and discussing potential overfitting issues of reward models to the RewardBench dataset.

### Questions
- I am unclear about why the Pearson correlation for “chat hard” in Figure 4 is so low. Does this imply that most RewardBench metrics do not reflect post-RLHF performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
It proposes Preference Proxy Evaluations (PPE), a novel benchmark designed to evaluate reward models based on their ability to predict post-RLHF outcomes. They use a crowdsourced human preferences and a verifiable correctness dataset for the RM evaluation.

### Strengths
- Achieves 77% Pearson correlation with human preference ELO. 
- Well motivates why best-of-K scores, row-wise Pearson correlation, & accuracy are relevant for downstream RLHF success. 
- Human preference dataset is large and useful in producing statistically significant outcomes (16,038 labeled preference pairs).

### Weaknesses
 - Underdiscusses the possibility that the RM evals are computationally very expensive to run in the the PPE framework. Best-of-K performance curves and pairwise accuracy have a huge computational burden, especially as K increases. Please provide runtime estimates for different K values or discuss strategies for making the evaluations more computationally efficient.
- Does not discusses the findings (e.g. low quantile aggregation correlation) in any depth. Please explore potential explanations for this correlation or discuss its implications for reward model design and training.



### Questions
- Why, intuitively or theoretically, is low quantile aggregation correlation correlatedmore strongly with downstream RLHF performance? Please provide hypotheses or conduct additional analyses to investigate this relationship further.
- How does inference cost scale with K, and what's a feasible value of K for training a large language model today? Please provide a table or graph showing inference costs for different K values, and discuss how these costs might impact real-world applications of the method.
- Why do pairwise accuracy-like metrics suffer from overfitting? Discuss this in more detail and provide empirical evidence of overfitting in pairwise accuracy metrics if possible.
- Is there a predictive accuracy plateau after a certain K-value? Is it possible to include a graph demonstrating diminishing returns/values of predictive accuracy with K?

### Soundness
3

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
3

### Summary
The paper tackles the problem of evaluating reward models without having to run the expensive evaluation of downstream LLM performance. The authors compare metrics that are predictive of actual human evaluations on downstream performance, when employed directly at the reward model stage. Different metrics across preference and correctness are compared to down-stream performance, and rew. model accuracy is identified as the best metric predicting downstream human preferences. Correctness is default benchmarks is also a reasonable indicator of LLM performance.

### Strengths
Strengths:
- The problem is highly relevant, the evaluation of reward models and RLHF workflows is a challenging problem
- The collection of human preferences and release as open-source is a valuable contribution to the community, the amount of collected human data is impressive (especially including multi-lingual queries)
- The approach of grounding metrics with human data is highly appreciated, and can be a valuable tool for future reward model development
- The selection of models, prompts and correctness metrics is well motivated

### Weaknesses
Weaknesses
- Some of the results seem pretty surprising (e.g. the low correlation with reward bench), for me it’s a bit unclear why we observe them. It would be great if the authors could try to reason more about these observations (as outlined below)
- Clarity of writing and presentation could be improved
- "Reward Model Accuracy" as the best metric is not a novel contribution in itself, you may argue that it’s good to have it validated towards human preferences
- Overall, i find the findings a bit weak, i.e. i don't find it easy to draw clear lessons for reward model design (larger vs. smaller models), i think it would have been very helpful to discuss these results more
- I would have liked some more information about variance/stds., e.g. spread of accuracy across sub datasets, etc., best-of-k curves, etc.

Minor
- Some formulations feel a bit clunky, e.g. P6, L.318. “We use the reward models to RLHF Llama-1.1-8B using..”, P8, L.327: “Mean across all metrics is well correlated across all metrics”	 I think the paper could profit from one additional pass of copy editing
- I think adding some figures/plots would help readability, e.g. turning table 3 into a chart

### Questions
Needs clarification
- Section 4 felt a bit out of place (so the first section), especially “The human preference dataset contains human-labeled preferences for 16,038 pairwise comparisons between 20 selected top models”: How is this dataset used?  In the paper, there are references to multiple datasets and collections, and I find it a bit confusing to follow how many datasets exist, and for which experiment they are used (e.g. 16,038 preferences in section 4, 12,190 votes in section 6, 50.000 votes in sec 6.1.
- I think the structuring of sections 4 and 5 could be improved a bit, in particular I was a bit confused about the content of section 4, I think a figure showing the workflow/process would help to clarify this
- I would like to ask the authors opinion on using already RLHF fine-tuned models as the source of data. Does it introduce its own biases, in particular to the distribution of responses? Doesn’t it implicitly reward similarity to already existing RLHF strategies?
- Can the caption of Figure 2 be improved? I’m not sure what I see in the right plot compared to the left one, how does the message differ?
- The inverse correlation between reward bench and human elo (Figure 4) is interesting, I would really like the authors to provide a hypothesis for this

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents PPE, a reward model benchmark explicitly tied to post-RLHF outcomes based on real human preferences. Previous reward model benchmarks focused solely on evaluating the reward models themselves, without assessing their post-RLHF performance. PPE fills this gap. More importantly, the paper analyzes which metrics best reflect post-RLHF performance, providing valuable insights for improving reward model evaluation methods.

### Strengths
- Compared to previous reward model benchmarks, PPE directly evaluates the post-RLHF performance of models, which more accurately reflects the positive impact of reward models on LLM tuning.
- PPE offers more diverse and larger-scale datasets than earlier benchmarks, making it a highly robust benchmark.
- The paper is very detailed and easy to follow, allowing readers to clearly understand the evaluation process. The explanations for each metric and evaluation method are convincing.
- I personally appreciate Section 7 of the paper. The analyses can help researchers predict the performance of fine-tuned LLMs using high-confidence metrics when they lack the resources to conduct full post-RLHF evaluations.

### Weaknesses
 - I believe this work fills a significant gap in reward model evaluation by addressing post-RLHF performance testing. The effort is substantial and thorough. I do not observe any obvious weaknesses.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
