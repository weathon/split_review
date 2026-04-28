# Language models scale reliably with over-training and on downstream tasks

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Scaling laws are useful guides for derisking expensive training runs, as they predict performance of large models using cheaper, small-scale experiments.
However, there remain gaps between current scaling studies and how language models are ultimately trained and evaluated.
For instance, scaling is usually studied in the compute-optimal training regime (i.e., ``Chinchilla optimal'' regime).
In contrast, models are often over-trained to reduce inference costs.
Moreover, scaling laws mostly predict loss on next-token prediction, but models are usually compared on downstream task performance.
To address both shortcomings, we create a testbed of 104 models with 0.011B to 6.9B parameters trained with various numbers of tokens on three data distributions.
First, we fit scaling laws that extrapolate in both the amount of over-training and the number of model parameters.
This enables us to predict the validation loss of a 1.4B parameter, 900B token run (i.e., 32$\times$ over-trained) and a 6.9B parameter, 138B token run (i.e., a compute-optimal run)---each from experiments that take 300$\times$ less compute.
Second, we relate the perplexity of a language model to its downstream task performance by proposing a power law.
We use this law to predict top-1 error averaged over downstream tasks for the two aforementioned models, using experiments that take 20$\times$ less compute.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper highlights two issues overlooked in current discussions of scaling laws for large language models: (1) To reduce inference costs, smaller models are often trained on more data, and (2) scaling law research commonly uses perplexity to measure model performance, whereas real-world evaluations focus on task completion performance, such as accuracy. In response, this paper investigates and confirms scaling laws in large language models related to over-training and performance on downstream tasks.

### Strengths
- The motivation is clear and the investigation is significant. Exploring scaling laws that are closer to real-world application scenarios provides strong guidance for the experimental setup of pre-training large language models.
- The experimental logic is very clear. The authors first selected certain experimental settings to fit and obtain hyperparameters for the specific scaling law. Then, they validated its accuracy on over-training and downstream performance across additional experimental settings, which is a reasonable approach.

### Weaknesses
 - Some experiments are missing. The authors’ initial motivation for studying the scaling law in over-training was to reduce inference costs, but this raises a question: training smaller models on more data achieves performance comparable to larger models under the same compute budget. However, this issue is not well explained—are there relevant experiments or clear prior studies addressing this? Specifically, while the paper suggests that over-training a smaller model can match the performance of a larger model, it does not directly compare the inference costs of these two scenarios under a fixed compute budget. This comparison is crucial to validate the claim that over-training is a viable strategy for reducing inference costs.
- The experimental validation of the scaling law for downstream performance is not rigorous enough. As shown in Table 2, there is a significant gap between the predicted and actual values of downstream performance based on the scaling law for individual datasets, while the average gap across 17 tasks is relatively smaller. Does this indicate that predictions from the downstream performance scaling law carry substantial risk? More specifically, we do not know for which specific number or types of tasks this scaling law provides accurate predictions. The paper should provide a more detailed analysis of the variance in prediction accuracy across different tasks and explore potential reasons for these discrepancies. This analysis should include a discussion of the types of tasks where the scaling law is most reliable and those where it is not, along with potential mitigating strategies.

### Questions
- Line 69-70: "M = N/D" seems to be a typo. It should be "M = D/N."
- Is Figure 1 a log-log plot?

### Soundness
4

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
The paper investigates scaling laws for language models  (LM) in the over-trained regime, where models are trained with greater token-to-parameter ratios to lower inference costs.
They furthermore derive power-law scaling laws for downstream task performance (error rates) from the conventional laws using LM loss.
Using a testbed of 104 models (0.011B to 6.9B parameters) with varying token counts across three distinct datasets, they fit power-law scaling laws to predict validation loss and error rates, validating the consistency and reliability of the proposed laws.
The paper is well-motivated and addresses an important problem, with technically significant and practically valuable findings.

### Strengths
* The problem of scaling laws under over-training is practical and interesting, addressing gaps in existing literature around compute-optimal training, allowing for the efficient resource utilization in large-scale language modeling.
* The proposed laws appear logical
* The evaluation appears comprehensive, with a diverse and appropriate testbed to test the hypotheses around scaling laws under over-training. As a result, they achieved reasonably good performance: average top-1 error on 17 tasks within a 0.05% relative error and 0.7% relative error on validation loss.
* The paper is clearly presented, with detailed steps for law derivation,  model configuration, and scaling law fitting.

### Weaknesses
 - Performance of downstream task: Although average performance aligns with the laws, variability in individual predictions and occasional high errors may suggest that the scaling laws may not universally hold without further model or data refinements. Furthermore, the laws in equation 4 assume $\alpha =\beta$ which can limit the applicability. Specifically, the assumption that the exponents governing the relationship between loss and model size ($\alpha$) and loss and data size ($\beta$) are equal is a strong one and may not hold across diverse datasets or model architectures. This could lead to inaccurate predictions when these exponents diverge.
- The paper does not address how the scaling laws would hold under different architectural configurations or training optimizations, which are relevant to future model development. For example, the study does not explore the impact of different activation functions, attention mechanisms, or normalization techniques on the derived scaling laws. These architectural choices could significantly alter the training dynamics and the resulting scaling behavior.
- The paper explored limitations such as sensitivity in out-of-distribution settings, posing challenges for future refinement of scaling laws in varied training regimes and tasks. The observed high relative error in out-of-distribution settings, particularly on code domains, suggests that the current scaling laws may not generalize well to unseen data distributions. This limitation is critical for practical applications where models often encounter data that differs from the training distribution.
- The claim of "predictable downstream performance" seems somewhat misleading, as the performance for specific tasks can vary widely. A more precise phrasing could emphasize “predictable average performance” to better align with the actual findings. The variability in individual task performance undermines the claim of predictability, as practitioners are often interested in the performance of specific tasks rather than average performance across a suite of tasks.
- Presentation:
1. In Figure 1, the paper defines M = N/D (line 70) while D=MN (Fig 1 caption) and line 127
2. Figures need better visualization and explanation for understanding. For example, in Figure 1, colors for M=320 and M=640 are very similar.
3. Typos: Line 142: than in

### Questions
* Lines 142-144: can you elaborate on this sentence: "While loss should be higher than in the compute-optimal allocation for a given training budget, the resulting models have fewer parameters and thus incur less inference cost." and why it is "common practice to over-train smaller models" (line 44)?
* The exponential relationship between loss and error is motivated in Figure 3, but have you evaluated larger sets of tasks to validate the relationship?
* Does the paper assume that over-training effects remain uniform across model sizes and datasets?
* Could the authors elaborate on the characteristics of tasks where downstream predictions were less accurate? Are there specific aspects that tend to yield higher prediction errors? 
* As the paper mentions exploring out-of-distribution scaling, can you provide findings on how well the scaling laws hold when tested on domains or tasks different from the training dataset?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the implications of over-training in LLMs, and tries to fit a scaling law for extrapolating beyond the compute-optimal (Chinchilla optimal) regime. The proposed scaling law is able to predict the final validation loss of a model using 300x less compute than what would have been needed to fully train the model.

### Strengths
- Extensive experiments across many training datasets (C4, RedPajama and RefinedWeb) and model sizes.
- Comprehensive evaluations using diverse validation datasets.

### Weaknesses
 - As the field of LLMs is currently agressively expanding into multimodality (images, audio, video and data), the proposed method might soon not hold up anymore. There is no mention of early-fusion multimodal models or token-free language modeling. The method's reliance on a fixed token vocabulary and architecture limits its applicability to emerging multimodal models that may use different input representations or model structures. Furthermore, the scaling laws might not generalize to models that process multiple modalities jointly, as these models may exhibit different scaling behaviors due to the increased complexity of the input space and the need for cross-modal interactions.
- Lack of consideration for post-training, fine-tuning and inference-time compute scaling methods, which are now integral to all production-ready models. The paper does not address how overtraining during pre-training might affect the subsequent fine-tuning process, which is crucial for adapting models to specific downstream tasks. The absence of an analysis on how the proposed scaling law interacts with fine-tuning and inference-time optimizations leaves a gap in understanding the practical implications of the findings. For instance, the optimal pre-training regime might differ significantly if the goal is to achieve the best performance after fine-tuning, rather than solely minimizing pre-training loss.

### Questions
- How accurate would this method be for predicting the performance of much larger LLMs, such as 30B, 70B, 400B? Are there any special considerations in order to ensure the law stays accurate?
- Would this law also work on "efficient" LM architectures such as mixture-of-experts, approximate attention and attention-free models?
- How might overtraining affect post-training, fine-tuning or inference-time compute scaling methods? Would their benefits scale proportionally the same to the losses and evals?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This article investigates the behaviors of scaling laws in the regime of over-training and on downstream benchmarks. Through derivation and initial observations, the article provide empirical evidence that over-training largely follows a similar, tractable, and constant-slope scaling law. Through further investigations and experiments, the article derives the parameters in the scaling law for over-training. With that conclusions, the article is then able to derive a scaling law relating model size, training tokens, and average downstream task performance, for the first time proving that average performance across a subset of downstream tasks are tractable.

### Strengths
1. Originality: This work firstly investigates and tracks next-token prediction model performance under the over-training regime and on downstream benchmark evaluation tasks.
2. Strong experiment results: This work builds a test-bed with more than 100 models with different sizes and training tokens. Through predicting the scaling law, this work successfully predicts the performance of larger models trained with more tokens.
3. Theoretical relationship with prior work: This work provides a stimulating analysis (Section 2) between scaling laws under the over-training regime and existing Chinchilla/Kaplan scaling laws, providing strong theoretical evidence supporting the derived over-training scaling law.
4. Writing: This paper is well-written with a clear, logical presentation of motivation, derivation process, experiment result analysis, and conclusion.

### Weaknesses
1. This work suggests that "there remain gaps between current scaling studies and how language models are ultimately trained and evaluated" (Line 13-14), suggesting that over-trained regime is under-investigated. There is an interesting work [1] that investigates the pre-training process of language models. In [1], the authors predict the training outcomes using the gathered data from an initial training period, and they successfully predicts the training outcomes of relatively small models (<0.1B) trained on large number of tokens (400B tokens). In that case, $M>4000$ and falls into the over-training category. It would be interesting to investigate the difference between the proposed over-train scaling law and [1].

### Questions
There is only one thing that WILL NOT affect my overall rating towards this article. 

1. See Weakness [1], it is better to discuss the differences between the proposed over-train scaling law and [1]. 

I am willing to defend my overall rating in the rebuttal period.

[1] Temporal Scaling Law for Large Language Models

### Soundness
4

### Presentation
4

### Contribution
4
