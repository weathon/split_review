# Selective Mixup Helps with Distribution Shifts, But Not (Only) because of Mixup

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
\textbf{Context.}
Mixup is a highly successful technique to improve generalization of neural networks by augmenting the training data with combinations of random pairs. Selective mixup is a family of methods that apply mixup to specific pairs, e.g.~only combining examples across classes or domains. These methods have claimed remarkable improvements on benchmarks with distribution shifts, but their mechanisms and limitations remain poorly understood.
 
\vspace{4pt}\textbf{Findings.}
We examine an overlooked aspect of selective mixup that explains its success in a completely new light. We find that the non-random selection of pairs affects the training distribution and improve generalization by means completely unrelated to the mixing. For example in binary classification, mixup across classes implicitly resamples the data for a uniform class distribution ---~a classical solution to label shift. We show empirically that this implicit resampling explains much of the improvements in prior work. Theoretically, these results rely on a ``regression toward the mean'', an accidental property that we identify in several datasets.

\vspace{4pt}\textbf{Takeaways.}
We have found a new equivalence between two successful methods: selective mixup and resampling. We identify limits of the former, confirm the effectiveness of the latter, and find better combinations of their respective benefits.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the success of selective mixup on the out-of-distribution generalization problem and finds out that the effect of mixup and resampling due to selective mixup can be decoupled. They conduct several experiments and find that the main contribution to the effectiveness of selective mixup may result from resampling.

### Strengths
1. The paper is easy to follow
2. Conduct results on many ood datasets and compare the results of selective sampling without mixup with the selective mixup method. And figures like Figure 7 and Figure 15 is insightful for noting the decoupling between mixup and resampling.

### Weaknesses
1. Some of the notations are not so clear. Like in Table 1, what's the definition of Resampling (uniform cl.) + concatenated pairs, and why it has different proportion of majority class compared with "Resampling (uniform classes)"?

### Questions
1. What makes the difference in the sampling ratio between the selective sampling without mixup and resampling? Is this determined by the hyperparameter of mixup? When changing the lambda for the beta distribution of mixup, are similar results as Fig 15 hold? 
2. For this finding, what about using another mixup method like manifold mixup, which may help the old generalization ability by connecting samples from different domains/classes in the representation space?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of selective mixup, where the sample and labels are paired based on a certain criteria and the risk is minimised on the mixed up samples. The paper then demonstrates that when samples from different classes are mixed up the overall data distribution regresses towards a uniform distribution. Hence, the success of mixup under distribution shift  is attributed to both the resampling effect and regularization effect, where it is argued that resampling plays an important role. Some theoretical results are shown, which are supplemented with empirical results.

### Strengths
Relevant problem to be studied in detail.

Extensive experiments have been conducted for analysis.

### Weaknesses
Weak Theoretical Results: I find the theoretical result to be weak, as it only considers the mixup of the labels. For appropriate analysis of the mixup, the mixing of data points (x) should also be considered (i.e. covariates) to get the complete picture of the problem.

Empirical Results are Scattered: The authors explain the results of each of the datasets independently, which is a source of confusion due to the complexity involved. The datasets often demonstrate conflicting conclusions, for example, results on Arxiv are much different from the Waterbird. Hence, it’s hard to obtain final conclusions. The results on various datasets can be combined which contain similar problem settings and demonstrate consistent results.

Inconsistency in Experimental Setups: There is a difference between the number of methods considered for each dataset. Hence, it’s hard to parse which combination of methods is most effective on average across all the datasets.

Novelty: However, the authors have done a considerable amount of experiments. I find that the content is scattered and insufficient, to meet the bar for novelty and doesn’t provide insights different than existing works (Yao et al. 2023)

### Questions
As the method mainly considered label shift, have the authors considered the setting of long-tailed label shift mixup?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the mechanism of selective Mixup, with a particular emphasis on its resampling aspect. The authors suggest that the resampling effect plays a crucial role in achieving the notable performance. Furthermore, the paper provides theoretical results, demonstrating that specific selection criteria exhibit a "regression toward the mean" bias or help mitigate class imbalance bias. The study includes many empirical results, and the authors propose a novel combination of selective Mixup and resampling to boost the performance beyond that of the original selective Mixup.

### Strengths
The resampling effect of Selective Mixup has not been investigated in previous literature, which is definitely a crucial aspect to uncover the mysteries of Selective Mixup. Additionally, the authors introduce a novel technique to improve the performance of selective Mixup by enhancing the resampling effect.

### Weaknesses
A notable weakness is the misalignment between the explanations and claims provided and the empirical observations. Additionally, the paper appears to overlook certain important and interesting discussions based on observations. 

Further details can be found in the questions outlined below.

### Questions
1. In Figure 2, the authors mention that ''The ranking of various criteria for selective sampling is similar whether with or without Mixup''. However, claiming that the performance between selective sampling is similar to that of selective Mixup seems somewhat strained. For instance, in the case of "Diff. domain+ Same class," selective Mixup demonstrates a $6\%$ higher accuracy than selective sampling. What accounts for the superiority of selective Mixup over selective sampling in this scenario?

2. Similarly, in Figure 2, for ''Same domain'', ''Diff. class'' and ''Diff. domain + Diff. class'', selective sampling is much better than selective Mixup, does this indicate that vanilla Mixup is harmful in this case? Such observations are more evident in Figure 8. The authors have not discussed the reasons behind the occasional superiority of selective Mixup over selective sampling.

3. In Figure 6, given the effective performance of vanilla Mixup, it appears that vanilla Mixup is the main driver for the improvement in selective Mixup, even with the optimal criteria. This observation contradicts the third point outlined in the summarized contributions in the Introduction.

4. In Figure 6, it is observed that for the case of ''Diff. domain + Same class,'' selective Mixup performs worse than vanilla Mixup. Does this observation imply that the resampling effect may have a degrading impact on the performance of Mixup?

I would be willing to increase my score if the authors addressed my concerns.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to show the equivalence between selective mixup, where the pairwise samples are selected according to a specific distribution and are mixed up for training and resampling based on the derived sample distribution in the batches for the selective mixup. 
The authors argue that such mixups shift the underlying training distribution to a more uniform one and can show performance improvements when the test distribution is uniform in nature. The authors also show results for cases where there are multiple domains in the data.

### Strengths
The authors present a simple analysis of an intuitively known effect of the mixup on training data where there is an imbalance in the training data. They provide mathematical proof that such selective increases the entropy of the training distribution

### Weaknesses
1. The authors claim that the selective mixup yields a training distribution over those classes that is closer to the uniform distribution. The authors do not provide results for the imbalanced classification on standard datasets such as CIFAR-10LT, CIFAR-100 LT, and imagenet1k-LT. 
2. Since the authors claim that an equivalent resampling is just as good, an important baseline in long-tail would be to compare against MiSLAS.
3. Could you an analysis where the test distribution is also skewed, independent of the training distribution? How is the performance of existing methods and the derived resampling distribution from Selective Mixup one of the claims made is that these methods are useful because the balancing effect on the training distribution performs well when the testing data is uniform.
4. I find a lack of novelty in the finding that mixup yields a training distribution with higher entropy, i.e., closer to the uniform distribution, Could you provide any strong theoretical justification that the actual mixup is not contributing to an improvement in the performance since existing works such as MiSLAS do show superior performance to vanilla classifier retraining on training with class balanced samplers.

### Questions
See weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
