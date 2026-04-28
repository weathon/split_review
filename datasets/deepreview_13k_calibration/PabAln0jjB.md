# Right Now, Wrong Then: Non-Stationary Direct Preference Optimization under Preference Drift

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Reinforcement learning from human feedback (RLHF) aligns Large Language Models (LLMs) with human preferences. However, these preferences can often change over time due to external factors (e.g. environment change and societal influence) – consequently, what was wrong then might be right now.~Current preference optimization algorithms do not account for temporal preference drift in their modeling, which can lead to severe misalignment. To address this limitation, we use a Dynamic Bradley-Terry model that models preferences via time-dependent reward functions, and propose \textit{Non-Stationary Direct Preference Optimisation} (NS-DPO). 
By introducing a discount parameter in the loss function, NS-DPO applies exponential weighting, which proportionally focuses learning on more time-relevant datapoints.
We theoretically analyse the convergence of NS-DPO in the offline setting, providing upper bounds on the estimation error caused by non-stationary preferences. By simulating preference drift using renowned reward models and modifying popular LLM datasets accordingly, we show that NS-DPO fine-tuned LLMs remain robust under non-stationarity, significantly outperforming baseline algorithms that ignore temporal preference changes, without sacrificing performance in stationary cases.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses temporal preference drift - a phenomenon where preferences in datasets collected over long periods undergo gradual or sudden changes. They also proposed Non-Stationary Direct Preference Optimization (NS-DPO) algorithm to  handle this preference drift.

### Strengths
- Addressing temporal preference drift is an important and interesting problem.
- The paper is well written.
- The work provides both theoretical and experimental results.

### Weaknesses
 - While temporal preference drift is important, NS-DPO makes a strong assumption: that older data has a higher probability of changed preference labels, regardless of topic. However, this assumption may not hold in reality. For example, preferences for factual topics (like "What is the capital of France?") remain constant over time. This assumption is problematic because the algorithm discounts older data even when the preferences are stable, potentially leading to suboptimal performance in scenarios with mixed stationary and non-stationary preferences.

- The experiments are conducted only on synthetic setups. The use of semi-synthetic datasets, while incorporating real-world prompts and responses, still relies on artificially introduced preference drift patterns. This limits the generalizability of the findings to real-world scenarios where the nature and timing of preference shifts are unknown and potentially more complex than the predefined patterns used in the experiments.

- What are the benefits of the algorithm compared to this alternative approach: first training the model on the newest data, then using this trained model to generate new preference annotations for older data, and finally training on the combined dataset? This baseline approach, while potentially more computationally expensive, could provide a more robust comparison by adapting to the changing preferences and re-evaluating older data, rather than simply discounting it based on its age.

### Questions
Please refer to weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new algorithm, NS-DPO (Non-Stationary Direct Preference Optimization), which extends DPO to address the temporal drift of preferences. The authors provide both theoretical and empirical support for this algorithm. The theoretical analysis derives a regret bound for the algorithm’s convergence in the offline setting. Empirically, NS-DPO is tested on both synthetic and LLM experiments under conditions where preference data shifts over time.

### Strengths
1. The paper is well-presented, highly readable, and organized effectively.
2. The theoretical analysis is comprehensive, and the resulting bound, expressed in terms of a drift measure, is particularly insightful.

### Weaknesses
1. The study lacks strong motivation. Are there any advantages to incorporating older preference data instead of relying solely on the most recent data, which is more relevant for the model? Considering that RLHF uses much less data compared to pre-training or SFT and that binary preference data is relatively inexpensive to collect, would it be more effective to gather fresh data for model training? Or alternatively, could we focus on collecting only the updated opinions to align the model?
2. It appears that all older data is discounted. How would the algorithm handle a mixture of drifting and fixed preference data, especially if some of the fixed data—though collected long ago—still holds true? Would this data be overly discounted? Is there a mechanism to ensure that genuinely stable preferences aren't unfairly penalized over time?

### Questions
1. As noted in the weaknesses section, is all older data— even the valuable data—significantly discounted?
2. In the results presented, $\rho_{diff}$ values are above 0.7. This may or may not be true given real-world preference data. What would the results look like for much smaller values of $\rho_{diff}$?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Non-Stationary Direct Preference Optimization (NS-DPO), addressing the issue of time-varying preferences in Large Language Models (LLMs). Unlike existing methods, NS-DPO accounts for preference drift by incorporating a Dynamic Bradley-Terry model and exponential weighting in the loss function. Theoretical analysis provides bounds on estimation errors and regret due to non-stationary preferences. Empirical results demonstrate that NS-DPO effectively maintains robustness under preference drift, outperforming baseline algorithms while preserving performance in stationary settings.

### Strengths
1. **Method Simplicity and Clarity**: The proposed NS-DPO method is straightforward and easy to follow, making it accessible for implementation.
2. **Theoretical Support**: Rigorous theoretical analysis provides bounds on estimation errors, ensuring the method's reliability.
3. **Robust Experimental Design**: The experiments are well-designed and comprehensive, effectively demonstrating the method's robustness and effectiveness.

### Weaknesses
1. **Baseline Considerations**: The paper could benefit from a more comprehensive comparison with alternative methods. Specifically, the most straightforward approach to handling non-stationary preferences would be to re-finetune the model on new data. Adjusting the $\beta$ parameter to control the model update speed or using a retrieval-based system (e.g. RAG) to update memory could also address the issues illustrated in Figure 1. Incorporating these methods as baselines would provide a more robust evaluation of NS-DPO's advantages.

2. **Reward Accuracy Metric**: While reward accuracy is used as the primary evaluation metric, it is important to note that recent study [1] have shown that reward accuracy does not always correlate directly with model performance. Win rate, which measures the proportion of times the model outperforms a baseline, is often a more meaningful metric in practice. Including win rate alongside reward accuracy would provide a more comprehensive assessment of the model's effectiveness.

3. **Model Fine-Tuning Approach**: The paper uses Llama-2-7b-chat-hf as the base model, which is large enough to support full fine-tuning. However, the experiments only explore LoRA fine-tuning. Conducting experiments with full fine-tuning would offer deeper insights into the performance gains and potential limitations of NS-DPO. This could help determine whether the benefits of NS-DPO are consistent across different fine-tuning strategies.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
