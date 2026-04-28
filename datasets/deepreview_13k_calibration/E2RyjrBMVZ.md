# Quantifying Variance in Evaluation Benchmarks

- Decision: Reject
- Avg Score: 4.17
- Scores: 3, 5, 6, 5, 3, 3

## Abstract
Evaluation benchmarks are the cornerstone of measuring capabilities of large language models (LLMs), as well as driving progress in said capabilities.
Originally designed to make claims about capabilities (or lack thereof) in fully pretrained models, evaluation benchmarks are now also extensively used to decide between various training choices. % (e.g.\ hyperparameters, datasets, architectures).
Despite this widespread usage, we rarely quantify the variance in our evaluation benchmarks, which dictates whether differences in performance are meaningful.
Here, we define and measure a range of metrics geared towards measuring variance in evaluation benchmarks, including seed variance across initialisations, and monotonicity during training.
By studying a large number of models -- both openly available and pretrained from scratch -- we provide empirical estimates for a variety of variance metrics, with considerations and recommendations for practitioners. 
We also evaluate the utility and tradeoffs of continuous versus discrete performance measures and explore options for better understanding and reducing this variance. 
We find that simple changes, such as framing choice tasks (like MMLU) as completion tasks, can often reduce variance for smaller scale ($\sim$7B) models, while more involved methods inspired from human testing literature (such as item analysis and item response theory) struggle to meaningfully reduce variance.
Overall, our work provides insights into variance in evaluation benchmarks, suggests LM-specific techniques to reduce variance, and more generally encourages practitioners to carefully factor in variance when comparing models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work aims to quantify evaluation benchmark variance across a range of settings (from pretraining intermediate checkpoints, to the largest frontier LLMs) using a diverse set of metrics (seed variance, confidence intervals, and monotonicity). Beyond quantifying variance, the paper also explores item response theory.

### Strengths
The paper is clearly written and easy to understand.

### Weaknesses
The key problem for me is that I do not get the value proposition of this work. It's difficult to see how this work could develop relevance/impact for the evaluation of foundation models. Since that's why I am hesitant to support the paper I focus my review and questions below fully on this point.

Specifically, the paper does not clearly articulate how quantifying variance, as they propose, directly addresses the most pressing challenges in evaluating foundation models. While understanding variance is important in any statistical analysis, the paper fails to demonstrate how this particular analysis leads to more reliable or actionable insights in the context of LLM evaluation. The metrics they use (seed variance, confidence intervals, and monotonicity) are not novel, and the paper does not show how their application to LLMs provides a significant advancement over existing practices. The connection to practical improvements in model evaluation is weak, and it's not clear how this work would change how we evaluate or develop foundation models in practice.

### Questions
1. What is the most striking example with which you can demonstrate the potential impact of this work?
2. There are many challenges to evaluating foundation models and it is clearly also a matter of how much money (time, compute) to invest in which aspect to arrive at a conclusive result. So evaluation is inherently a trade-off and it is important to understand and acknowledge this trade-off. In my opinion there seem to be much more critical aspects that need to be addressed than the variance studied in this paper. For example, the paper "EVALUATING LLMS’ MATHEMATICAL AND CODING COMPETENCY THROUGH ONTOLOGY-GUIDED INTERVENTIONS" by Pengfei Hong et al seems to be a good route towards useful evaluations. I would rather invest time and compute into that direction and not bother about the methods proposed in this submission. Are you advocating for the opposite strategy?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses the problem in current evaluation and reporting practices where performance may vary across different development choices. This variance is scoped for training initialization seed and monotonicity. The paper also discusses ways to reduce this variance, in particular for choice based benchmarks.

### Strengths
- The paper explores how to make evaluations more precise by reporting variance.
- Provides estimates for the expected variance across several benchmarks and models.
- An important finding is made on the unreliability of IRT-based methods for evaluation comparisons across models. This is very relevant for evaluation reporting.

### Weaknesses
 - The framing of ‘variance’ in the paper seems too broad. There are other possible kinds of variance worth exploring or mentioning, such as variance introduced by data augmentation strategies, or different optimization algorithms. The current scope is too narrow to be considered a general study of variance in evaluations.
- The title of the paper and general framing suggests a general focus on variance in evaluations, but the paper currently fails to contextualize two very distinct types of variance: training and inference. For example, the (training) seed variance discussed falls within training. Other possible sources of variance for each should be mentioned where possible. A basic example of the inference type can be found in prompt sampling, but also in decoding strategies such as beam search or nucleus sampling, which can introduce significant variability in the generated outputs and thus the evaluation scores. The paper should at least acknowledge these other sources of variance.
- While studying the training seed variance is useful, this is really only feasible for smaller models, as it would be too expensive for larger models. This may reduce the utility of the results in large model comparisons. Furthermore, the paper does not discuss the potential interaction between seed variance and other hyperparameters, such as learning rate or batch size, which could further complicate the analysis. It is also unclear if the observed variance is consistent across different model architectures or pre-training datasets, limiting the generalizability of the findings.

The paper could mention previous work such as Picard 2021 (https://arxiv.org/abs/2109.08203) on the impact of training initialization seed variance, or fine tuning seed variance [Dodge 2020 (https://arxiv.org/abs/2002.06305)]. And also extended discussions on how obscuring or not disclosing these variances can be harmful to the evaluation process (e.g. [Leech 2024 (https://arxiv.org/abs/2407.12220)]).

### Questions
- Are there any other kinds of variance that could have been used for this study instead of initialization seed?
- Only training-based sources of variance are discussed, what about inference-based?
- Section 3.3 outlines a very interesting case of differences in evaluation results after a reformulation of the setup, could this be shown for other benchmarks? perhaps a similar pair?

### Soundness
2

### Presentation
2

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
This paper aims to quantify the amount of variance prevalent in popular LLM evaluation benchmarks, mainly by varying the random seeds for model training. The paper makes an important point about how we currently consider benchmark scores to only be point estimates rather than considering several other different factors of stochasticity while doing model comparisons. The paper conducts several experiments to quantify this seed variance across different benchmarks, and provides practical guidance on what metrics and evaluations to use during pretraining to provide most signal.

### Strengths
- The paper presents a timely and important topic of variance in evaluation benchmarks, that should be widely considered while reporting benchmark performance. 
- The paper is cogently written and presents convincing demonstrations of the importance of considering variance in evaluations while doing model comparisons.
- The paper showcases results and cautions against using sample efficient benchmarking methods while doing model pretraining, since they are likely to provide a higher-variance signal during training.

### Weaknesses
 - The provided variance numbers in Tab. 1, while being important as a reference, cannot be used directly for making comparisons across different model scales or training durations since it is not clear how those numbers would change with those factors, and whether we’d expect larger or smaller deviations in performance.

- Some important empirical details are missing, for example, could you provide more details on how you compute the SNRs for both discrete and continuous? Specifically, what is the precise definition of the signal and noise components used in the calculation? This is important since you are making the claim that Cont SNRs being larger than Disc SNRs suggests that we should shift towards continuous metrics for making model comparison decisions, and this claim can only be validated if the precise method of computing these SNRs is justified. It's also unclear if the mean and standard deviation used in the SNR calculation are computed across seeds, or across some other dimension of the data.

- Another important question that is critical for the takeaways of the paper: Is the unnormalised monotonocity the best metric here to capture the “stableness” of a benchmark? Shouldn’t that monotonicity be weighted by the monotonicity you would expect by chance? So something like a cohen’s kappa coefficient here seems more appropriate rather than just the direct unnormalised monotonicity. For eg, see the analysis in Geirhos et al, Beyond accuracy: quantifying trial-by-trial behaviour of CNNs and humans by measuring error consistency. I appreciate that this might be hard to formalise since its unclear what the “monotonoicty expected by chance is” but I believe this is worth at least a discussion point, and would like to hear the author’s thoughts on this. Also worth mentioning here that monotonicity was also explored for doing benchmark selection as good validation datasets for the fine-web training recipe. The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.

- Suggestion on formatting the paper: the results sections in 3 and 4 have some very important insights / takeaways for practitioners to adopt for pretraining and actual evaluation. I think it would majorly improve the paper if these could be highlighted at the end of each subsection in bold, or even better, a small box signifying the key takeaway.

- There are other kinds of variance inducing factors that haven't been investigated. For example, how does task type affect this variance? How does number of shots and choice of shots affect variance? How does model size impact variance? Does it increase as we scale up the model? There should be a discussion added about the other variance inducing factors which haven't been considered in the current work, and it must be made clear in the paper that "seed variance" is the only type of variance being investigated in this work.



### Questions
I have quite a few questions that I think would improve the quality of the paper, and for my own clarifications:
 
- Why are the Disc Std in tab 2 and std in tab 1 different? Aren’t they computing the same metric over the same set of models? The means are exactly the same for the discrete metrics so I presume the stds should be too?

- In tab. 2 what decoding strategy do you use for the generative tasks? The difference between GSM8k (0.99) and HumanEval (0.21) seems quite high for a difference in log-likelihoods. Are these token-length normalised likelihoods or unnormalised likelihoods?

- Comment: Typo in fig 3 caption, should be item difficulty (y-axis) and item discriminability (x-axis).

- For the analysis in fig 3, how does the correlation between item discrimination b/w train and test look like for another randomly selected set of train and test models? The key question is what the variance in the correlation obtained for a random split of random train-test models would be? This would make the conclusion (that the low correlation between train and test item discriminability is due to the differences in model capability) more strong and robust.

- The “best" and “worst” models used for creating the train and test splits do not share the same training data mixtures right? So I would expect that the takeaways from fig 3, especially the ones involving the difficulty split are also confounded by different levels of data contamination with respect to the test sets? 

- For the points in section 5, the main claims revolve around using the IRT benchmarks themselves. How much of that can be explained by the increased variance from just having a smaller number of test samples? i.e. how would the results look like if instead of the IRT test set, a random set of evaluation points of the same size as the IRT set were used for the analyses?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the variance present in current evaluation benchmarks by repeating the training of models with different random seeds. It demonstrates the variance caused by random factors in benchmarks, providing valuable references for assessing model evaluation results, particularly for the MMLU evaluation of smaller-scale models. The paper attempts to reduce evaluation variance using methods inspired by human testing literature, such as item analysis and item response theory, but finds that these methods have limited effectiveness.

### Strengths
- By training different models from scratch, the paper provides the most direct results for evaluating the variance brought by randomness. Based on these results, it offers valuable suggestions for assessing smaller-scale models.
- The paper introduces methods from human testing literature and explains the reasons for their limited success, providing insights for future work.

### Weaknesses
 - The paper focuses only on the variance caused by model random seeds and does not compare or combine this with existing work on the analysis of evaluation result variance. For example:
  1. It does not compare the variance caused by random seeds with the impact of other random factors during evaluation (such as option order, prompts, etc.).
  2. It does not explore whether the variance is further amplified when models with different seeds encounter situations like randomized options.
- The paper primarily showcases the overall variance of 210 7B model checkpoints. Given that models of different sizes exhibit significant differences in performance when trained with varying numbers of tokens, the overall variance statistics may have limited reference value for models trained with fewer or more data. Specifically, the paper does not address whether the observed variance in the 7B model is representative of other model sizes trained under similar FLOPs budgets, or if the variance scales differently with model size and training data volume. This is a critical limitation, as the variance observed in a 7B model trained with 210B tokens may not generalize to smaller models trained with fewer tokens or larger models trained with more data, even if the total FLOPs are similar. The paper lacks a comparative analysis of variance across different model sizes and training regimes, making it difficult to assess the generalizability of the findings.

### Questions
- Considering that the author trained different models from scratch, such as Hellaswag, which consistently outperformed random choice across a wide range of checkpoints, it would be beneficial if the author could use intermediate checkpoints to demonstrate the benchmark variance at different stages of training and performance. Furthermore, showing how benchmark variance changes with training progress could be helpful for models of various sizes and training data volumes.
- When calculating Seed Variance, would it be more reasonable to exclude checkpoints that are clearly still within the random result range from the statistical analysis?
- When models of different sizes achieve the same performance after being trained with different numbers of tokens (e.g., a 7B model trained with 120B tokens and a 1.5B model trained with 400B tokens), do they exhibit significant differences in benchmark variance?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper quantifies and highlights the important issue of seed variance, amongst different sources of variance, in evaluating language model performance *during pretraining*, emphasizing how insufficient variance quantification in benchmarks can obscure statistically significant performance differences within the same pretraining run.

**Methodology**: It retrains 10 LLaMA 7B models from scratch, and then studies the seed variance along with different metrics throughout the pretraining runs, such as-- 95% confidence intervals, and monotonicity across diverse benchmarks, offering a reference for understanding performance variation across setups.

**Claim 1**: Continuous metrics exhibit higher monotonicity and lower variance than discrete metrics and should be used more widely.

*Application*: Continuous metrics and cloze formats show lower variance and higher signal-to-noise ratios compared to traditional discrete measures, especially in smaller LLaMA 7B models. Simple modifications, such as reframing choice tasks as completion tasks, appear promising for reducing variance.


**Claim 2**: Efficient benchmarking methods can inadvertently increase variance, and it’s essential to verify if methods are distinguishable before using them.

*Application*: Techniques from standardized testing, such as item analysis and item response theory, are found ineffective in meaningfully reducing variance for large language models.

### Strengths
Key takeaways I appreciated:

- Continuous metrics show higher monotonicity and lower variance than discrete metrics, making them preferable. I really like this point!
- Variance (likely from benchmarking, not seed variance) could obscure the effectiveness of pretraining by making it harder to track performance improvements.

Benchmarking variance is a promising and underexplored area, especially given the recent focus on reasoning and the close performance of current models on benchmarks-- and seed variance can have a lot of effect.

### Weaknesses
See Weaknesses in the order of importance. If there is lack of time, please prioritize the earlier questions:

**P1: Seed Variance and Its Impact on Benchmark Scores**

> We provide a comprehensive reference guide for what magnitudes of variance are expected for what benchmarks across various circumstances

I worry the paper title/abstract/contribution1 is overclaiming as the evidence does not support the above claim-- It seems to me that paper focuses only on a single source of variance: seed variance. Given that studying variance is a common practice (the most popular benchmark, Chatbot Arena provides variance along with scores: https://lmsys.org/blog/2024-04-19-arena-hard/) and previous research on variance sources such as benchmarking details [1] and prompt design [2], the question studied here becomes: Does seed variance contribute overwhelmingly to the overall variance which makes it a critical factor to study, beyond [1,2,Arena]? 

I would appreciate:

a) A comparative analysis showing the relative impact of seed variance versus other variance sources on benchmark results.

b) A better distinction in the work for why studying seed variance specifically is important, given the existing literature on other variance sources.

Since the authors claim:
>  if we cannot ‘trust’ our evaluation results or do not understand what improvements are statistically significant, we cannot make sound comparisons, thus making it more challenging to reliably use benchmarks during model development.

a) I could not see the results of the 32 models apart from Llama-2-7B seed runs anywhere. Would be great to know whether the variance obtained Llama-7B seed runs can demonstrate that improvements reported in those models being deemed not-significant on some benchmarks.
b) To what degree are these variance estimates transferable beyond the Llama-2-7B model?.

**Overall:** Currently, it seems to me that, variances from [1] and [2] are critical but easy-to-obtain, while seed variance is compute-heavy to obtain and potentially not as significant source given different prompts and small benchmark details can cause far larger performance shifts. I request authors to present evidence or arguments suggesting this is not the case, and I am open to changing my mind.

[1] When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards

[2] Quantifying language models’ sensitivity to spurious features in prompt design or: How I learned to start worrying about prompt formatting.

**P2: Efficient Benchmarking in High-Variance Contexts**

(a) The rationale here is unclear.
Q1. If variance preservation is a priority, why subsample to an extreme degree of 100 samples? What are the trade-offs between efficiency and variance preservation in benchmarking? 

Q2. Conversely, does aggregating several 100 sample estimates reduce variance while still providing efficiency gains compared to evaluating on the whole dataset? Or in most concrete scenarios, efficient benchmarking just might be limited? 

(b) The paper says:
> While these negative results suggest item discriminations may not be the most informative means of understanding (or reducing) variance on stronger models 

> we overall would not suggest the use of item analysis-based methods for understanding variance in language model evaluations 

I doubt those papers claim their methods are intended to reduce or understand variance. Could the authors provide a citation for this claim? If no direct claims about variance reduction exist in the cited works, could the authors discuss in the work why they believe these methods should be evaluated in terms of variance reduction.

(c) While I agree with the authors that generally, subsampling might lead to critical issues in benchmarking – the results presented seem underwhelming given I fully buy the claim of using continuous metrics to reduce variance.

Specifically, the results in Table 7 indicate that Kendall’s tau still remains quite high and relatively stable. Do the authors believe this is damning evidence against efficient benchmarking methods? (I agree in principle there will be cases where this is damning, but the shown results do not seem to be those cases.) Similarly, Table3 and Table 4 show variance and monotonicity increases but the increase in variance/decrease in monotonicity remains quite small post-subsampling compared to the relative gains in benchmarking efficiency (except in the case of GSM-8k discrete metric).

**P3: MMLU Evaluation and Metric Selection**

I fully agree that continuous metrics may indeed have lower variance than discrete metrics (Table 2 demonstrates convincing gains in PSNR), the emphasis on MMLU in this context feels misplaced as one metric is near random. 

Metrics that perform near random chance are unreliable indicators of progress, while those consistently above random are more dependable. However, for smaller models, this reliability may simply stem from selecting a metric that surpasses random performance earlier in training, rather than addressing the broader variance concerns noted above. I don't know why this specific example was picked.

P4. **Poor Writing** 

The writing lacks clarity and precision, with ambiguous and poorly articulated claims scattered throughout the paper. This made the review difficult. In the summary, I’ve tried my best to interpret the paper’s main claims — please let me know if my summary underclaims compared to the intended or the claims differ from those presented in the work.

### Questions
See weaknesses above please. 

Overall, I think we should definitely report variance in benchmark estimates to compare significance of improvement, however I believe retraining $k$ times to obtain seed variance might not be the critical factor in total variance, and hugely expensive. I do think the recommendation of using continuous metrics makes a lot of sense. 

I think there are important shortcomings in my view, although I might likely be wrong. If weakness 1 is adequately alleviated, I would upgrade my score. Note: Weakness 3 and 4 are minor and have little effect on rating.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors address the question of measuring variance in standardized evaluation benchmarks. They do so by constructing various ways to assess variance including variance due to different init seeds and looking at evaluation monotonicity at checkpoints in course of pre-training. Authors study a number of already pre-trained models and also train Llama like models from scratch on 7B scales, varying their init seed and obtaining intermediate checkpoints to use for variance estimation. Authors show evidence for continuous metrics delivering better signal-to-noise ratio across all benchmarks, also showing better monotonicity for continuous metrics than for discrete ones. Authors also look into techniques used in human performance testing like item analysis and item response theory and find those not useful for assessing model performance and improving SNR.

### Strengths
Question of which metrics used for benchmarking model capabilities are properly reflecting model performance and allow differentiation of models already in early training stage or on smaller scales in general, where performance signal is weak, is very important, as it also leads to better methods for scaling law derivation and proper model comparison via derived scaling laws.

### Weaknesses
- Claims put forward by authors are made by experimenting with base models only. Especially when taking benchmarks that have certain question formatting at their core - MMLU, ARC, HellaSwag - it seems to me a strong confound when attempting to make a statement about ability of a benchmark to measure model capabilities. Base models do not handle instruction format well, in general struggling with handling question-answer interaction. This is usually installed via instruction tuning, after which models adhere to various instruction like interactions. I think thus to make proper statements about effect of variance or in general about how to render benchmark signal useful for predictions about model quality, benchmarks that do not rely on certain instruction template are not a good choice when dealing with base models. In my opinion, when working with such benchmarks, authors should have instruction-tuned base models, conducting measurements after that. Benefit of continuous metrics might be thus due to base models not handling instruction like benchs and not due to actual benchmark content related to complexity of problems posed in it. Same might hold for the "curious MMLU" case presented by authors, where cloze variant shows smaller variance and better SNR than multiple choice format standard MMLU form - this might be again just due to base models not being able to handle problem formulation template.

- Further weakness in my opinion is that many of the claims are based on pre-training from scratch done only on one model scale of 7B. It might be more insightful to see trends across scales, even smaller ones. Experiments on larger scale are though expensive, even if going bit further to 13B.

- It is also not quite clear how the claim of better suitability of continuous metrics is backed up. It seems to me there is no clear evidence presented by authors that using those metrics eg indeed allows better prediction from earlier to later training stages or from smaller to larger scale pretraining.

### Questions
Can authors show similar evidence for instruction tuned models? It seems to me that it is not expensive to instruction tune base models authors already have obtained, or at least use already available instruction tuned models. Alternatively, can authors present more benchs that do not heavily rely on instruction like templates?

Can authors present evidence that using continuous metrics they can do better on predicting either end model performance from early training phases or larger scale model performance from smaller scale pretraining?

### Soundness
3

### Presentation
2

### Contribution
2
