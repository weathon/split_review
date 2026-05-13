# Is Pre-training Truly Better Than Meta-Learning?

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
In the context of few-shot learning, it is currently believed that a fixed pre-trained (PT) model, along with fine-tuning the final layer during evaluation, outperforms standard meta-learning algorithms. 
We re-evaluate these claims under an in-depth empirical examination of an extensive set of formally diverse datasets and compare PT to Model Agnostic Meta-Learning (MAML). 
Unlike previous work, we emphasize a fair comparison by using: the same architecture, the same optimizer, and all models trained to convergence.
Crucially, we use a more rigorous statistical tool -- the effect size (Cohen's d) -- to determine the practical significance of the difference between a model trained with PT vs. a MAML.
We then use a previously proposed metric -- the diversity coefficient -- to compute the average formal diversity of a dataset.
Using this analysis, we demonstrate the following:
1. when the formal diversity of a data set is low, PT beats MAML on average and 
2. when the formal diversity is high, MAML beats PT on average. 
The caveat is that the magnitude of the average difference between a PT vs. MAML using the effect size is low (according to classical statistical thresholds) -- less than 0.2. 
Nevertheless, this observation is contrary to the currently held belief that a pre-trained model is always better than a meta-learning model.
Our extensive experiments consider 21 few-shot learning benchmarks, including the large-scale few-shot learning dataset Meta-Data set. 
We also show no significant difference between a MAML model vs. a PT model with GPT-2 on Openwebtext. 
We, therefore, conclude that a pre-trained model does not always beat a meta-learned model and that the formal diversity of a dataset is a driving factor.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an extensive set of empirical results comparing pre-training and meta-learning across numerous model choices and datasets. The paper also proposes a new statistic test based on the classical concept of effect size, which allows for comparison across different domains. 

The results show that on task space with low diversity, pre-training tends to perform better. Otherwise, meta-learning performs better based in the above statistical test.

Overall, the main contribution of this paper is an extensive empirical study that provides some interesting insights on when pre-training is better than MAML and vice versa.

### Strengths
The paper is sufficiently well-written. 

It experimental results are also quite extensive, reporting several insightful observations.

There is also the development of a new statistics test, which is both novel and interesting.

### Weaknesses
Despite the above strength, I still have a few doubts regarding the proposed evaluation scheme:

1. It would be better if the authors can elaborate more on why p-value and confidence interval become zero, which in turn motivates the development of the new test

2. What is the main principle behind the new test? Specifically, if it rejects a hypothesis, what can we tell about its confidence in doing so? For example, using t-test, we are implicitly assuming the performance differences follows a student-t distribution and the t-statistic basically tells us if we can reject the null hypothesis at a certain confidence level? Do we have a similar principle under the new test?

3. For the task space with high diversity, I tend to think that the pre-training would not be effective will small architecture for obvious reason. Thus, the statistic test should only be applied to the reported performance on the best model architecture for pre-training (but across different test domains) -- right now, it seems the performance report on ResNet50 would favor pre-training; and the conclusion that meta-learning is better is mostly likely caused by the included performance on lower-complexity ResNet structure.

### Questions
Based on my concerns above, the following questions were raised:

1. Can the authors elaborate more on why p-value & confidence interval would become zero on larger batch size?
2. Please elaborate on the main principle behind a new test (i.e., its underlying assumption regarding the distribution of performance difference between two algorithms + what can we say about the confidence in rejecting the null hypothesis)
3. For high diversity setting, I think the statistic test should be based only on the best model architecture. Please consider revising this part of the evaluation protocol

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* Paper examines the few-shot learning (FSL) paradigm, and studies the question of whether a pretrained (PT) model which then undergoes linear evaluation (finetuning of the final layer) is better than conducting meta-learning approaches such as MAML.
* This question has been studied before in different forms; the difference in this paper is that it standardizes the comparison using the same architecture for all methods, and trains models to convergence. A different statistical tool, Cohen's d, is used to assess performance differences. The usage of Cohen's d/effect sizes is because t-tests can result in very small p values/confidence intervals when the number of samples compared is large (which it is in this case).
* To study this question, the paper considers many different FSL datasets (21 totally) and compares the performance of PT models to MAML models.  The paper also evaluates the diversity score of datasets as a tool to help interpret the results, based on Task2vec (Miranda et al 2022). 
* The key finding is that PT models are not always better than MAML-styled metalearned models (based on the effect size score for the comparisons). in particular, one class may perform better than the other as a function of the diversity of the dataset considered.

### Strengths
* The problem studied has value, especially with the field moving towards PT and finetuning/linear evaluation over metalearning approaches. Studying the problem in the context of the task diversity is particularly interesting, and yields some intuitive results -- we would possibly expect metalearning to perform better in the context of high diversity (over pretraining). 

* discussion of why cohen's d was used is interesting -- paper has clearly put thought into choosing appropriate statistical measures to understand the results obtained.

* Diversity of datasets considered is valuable.

### Weaknesses
 * Choice of MAML model: the original MAML model has been developed significantly in recent years. It would be fairer to that class of methods to compare to one of these many developments, given they have demonstrated (in general) better performance. Specifically, the paper should consider more recent variants that incorporate techniques such as adaptive learning rates or improved gradient estimation, as these could significantly impact the performance of meta-learning, and thus the conclusions of the paper. A comparison against a vanilla MAML implementation is not sufficient to make broad claims about the efficacy of meta-learning approaches in general.

* A discussion of the drawbacks of effect size -- it is useful to understand where this may be inadequate (except the fact that one must choose a threshold level). Relatedly, the paper states that standard effect sizes are 0.2, 0.5, and 0.8, but it is unclear how the choice of 1% relates to these. The paper should discuss how effect size can be misleading when sample sizes are different, or when the underlying distributions are non-normal. Furthermore, the choice of 1% as a threshold for 'significant' effect size is arbitrary and not well-justified, especially given the context of standard effect size interpretations. The paper needs to provide a more rigorous justification for this choice, or consider using a more established threshold.

* Presentation of experimental setup: given this paper is primarily related to empirical benchmarking, a summary of the experimental setup in the main paper would help contextualise the investigation. This includes summary information about the datasets, abbreviations used (which reflect the results tables), training setup etc. For example, the paper should include details on the specific data splits used for training, validation, and testing, as well as the number of samples per class in each dataset. Furthermore, the specific optimization algorithms and hyperparameters used for both pre-training and meta-learning should be clearly stated in the main paper.

* Clarity in results exposition: when reporting the overall effect size, it is unclear how these are obtained -- my guess is an average over the cases where that hypothesis was determined correct. This is not mentioned (as far as I saw) -- it would help to do so. The paper should also include a discussion of the variance in effect sizes across different datasets, as this can provide valuable insights into the robustness of the findings. It is important to understand not just the average effect size, but also the distribution of effect sizes.

* Clarity in results table: The tables could be better presented, for example by having the captions clearly specify that MAML5 refers to 5 adaptation steps, and having the same formatting for the heading and the main body (like all uppercase). Also, the detail on seeds in Table 3 is hard to understand -- what are seed1 and seed1 vs seed2 comparisons? The caption mentions 5 layer CNNs but the table refers to Resnet12 and Resnet50? Overall, the results are interesting but the presentation is very hard to follow. The table should also include standard deviations or confidence intervals for the reported effect sizes, to allow for a more thorough evaluation of the results. The inconsistent use of model architectures across tables also makes it difficult to interpret the results.

* Training to convergence: Is this necessarily a good thing? If models experience some sort of overfitting, perhaps it makes sense to do early stopping? The paper should provide a justification for training to convergence, and discuss the potential impact of overfitting on the results. It would be useful to include learning curves for both pre-training and meta-learning to assess whether the models are indeed converging, and not overfitting.

* Minor: possibly missing citation in Section 5 when referring to feature reuse vs rapid learning

### Questions
See above; questions related to choice of MAML model, drawbacks of effect size, clarity in results tables.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the question of when meta-learning is suprior to pre-training, by using effect size (especially Cohen's d) as a statistical measure for comparison between the two approaches, on several few-shot classification benchmarks. The effect of task diversity in meta/pre-training is also considerred, which leads to findings that  pre-training (resp. meta-learning) tends to be suitable for low-diversity (resp. high-diversity) regime.

### Strengths
1. The paper uses an effect size to compare pre-training and meta-learning for the first time, which enables us to compare two methods quantitatively.
2. The paper empirically validates that the task diversity is a key property distinguishing pre-training and meta-learning, which is consistent with the motivation of meta-learning.

### Weaknesses
1. No novel methods are introduced in this paper, which itself is ok if the results are intriguing.
2. Presentation of the results is very poor. All results are just listed in tables, and there are no attempts to present the results in a comprehensible/impressive manner. Since I could not find any meaningful insight from the tables, I recommend adding more comprehensive figures which should be contributions of the paper.
3. The results of Cohen's d can be caused from (1) meta-training dataset, and/or (2) meta-test dataset, in addition to learning algorithms, but I could not find which factor causes the results of Cohen's d. In other words, which diversity of meta-training datasets or meta-testing datasets makes the difference between the two methods?

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper conducts a comprehensive examination of the effectiveness of pre-trained (PT) models in comparison to Model Agnostic Meta-Learning (MAML) within the realm of few-shot learning. Despite prevailing beliefs suggesting the dominance of PT models, this study provides an unbiased comparison by employing identical architecture and ensuring complete model training. The research uses a robust statistical methodology, specifically the effect size (Cohen’s d), to discern the practical differences between PT and MAML models. A "diversity coefficient" metric is used to define the formal diversity of datasets. Key findings highlight that for datasets with low formal diversity, PT models slightly outperform MAML. Conversely, in scenarios with high formal diversity, MAML tends to be more effective. However, the magnitude of these differences is marginal, with an effect size less than 0.2. When evaluating the overall performance across various dataset diversities, neither method exhibits a clear advantage. The authors conclude that the inherent diversity of datasets is an important factor in determining the efficacy of PT versus MAML models.

### Strengths
- The paper is well written and the methodology is clearly described and framed.

- The empirical assessment is robust and comprehensive. By employing a diverse set of statistical techniques beyond standard benchmarks, the authors have elevated the quality of model evaluation.

- The methods are compared on a large variety of datasets which are clustered in terms of diversity.

### Weaknesses
 - The paper is solid from the empirical point of view, presenting a large variety of results. However, it is somehow limited in terms of novelty as it does not introduce any new techniques or analyses.

- A significant limitation of the paper lies in its reliance on two methodologies, MAML and PT with fine-tuning restricted to the head, which may not represent the current best practices in the field. Firstly, while MAML is undoubtedly foundational in meta-learning, its relevance has waned over time. Contemporary advancements have introduced more efficient derivatives, such as MAML++ (Antoniou et al., 2018). Incorporating comparisons with these modern variants could have enriched the paper's insights. Secondly, the paper's approach to fine-tuning is notably narrow, focusing only on the head's parameter adjustments. Contrarily, cutting-edge methods today, like BiT (Kolesnikov et al., 20202), fine-tune the entirety of both body and head parameters, while others, like FiT (Shysheya et al., 2022), selectively adjust a subset of body parameters. A juxtaposition against these state-of-the-art techniques would have been insightful. These oversights are critical as the paper's primary conclusions might shift when evaluated against more contemporary, optimized methods.

- The presentation of data exclusively in tabular format, though beneficial for transparency, hinders a quick understanding of the trends. I recommend the authors to enhance data representation by incorporating visual aids, such as scatter plots. This would facilitate a more intuitive grasp of the data patterns. The tables could be conveniently relocated to the appendix to maintain thoroughness without overwhelming the main content.

- There are some formatting issues, e.g. (i) Table 6 should be within the body of the paper, (ii) in the text "Meta-Data set" should be replaced with "Meta-Dataset"

### Questions
Do the authors believe that a comparison between various methods, such as MAML++, BiT, or FiT, is feasible? Additionally, would such comparisons yield consistent conclusions with the current findings?

Please refer to the "Weaknesses" session for other potential points of discussion.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
