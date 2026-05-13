# ZipIt! Merging Models from Different Tasks without Training

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
\vspace{-0.6em}
Typical deep visual recognition models are capable of performing the one task they were trained on.
In this paper, we tackle the extremely difficult problem of combining distinct models with different initializations, each solving a separate task, into one multi-task model \textbf{without any additional training}. Prior work in model merging permutes one model to the space of the other then averages them together. While this works for models trained on the same task, we find that this fails to account for the differences in models trained on disjoint tasks. Thus, we introduce ``ZipIt!'', a general method for merging two arbitrary models of the same architecture that incorporates two simple strategies. First, in order to account for features that aren't shared between models, we expand the model merging problem to allow for merging features \textit{within} each model by defining a general ``zip'' operation. Second, we add support for \textit{partially zipping} the models up until a specified layer, naturally creating a multi-head model. We find that these two changes combined account for 20-60\% improvement over prior work, 
making it more feasible to merge models trained on disjoint tasks \textit{without retraining}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to merge two different models sharing the same architecture, possibly with different initialization and for different tasks, without re-training. The key idea is to merge the weights whose outputs are highly correlated, both within and across models. The method also allows weights to be partially merged, adding flexibility to adjust the amount of merging depending on resource budget and accuracy requirements. Experiments show that ZipIt! outperforms the existing baselines in several settings, including merging classification models and merging across tasks.

### Strengths
1. This paper studies a new and interesting problem: merging differently initialized models trained on different tasks into a single model without retraining. This relaxes the condition of the model merging problem, recently studied in works such as Model Soups and Git Re-Basin, which assumes the same task over models. This makes the problem more challenging while allowing for broader use cases.

2. The idea of merging weights both within and across models is simple, but achieves reasonably good performance under different conditions in the experiments. It's great that experiments with merging tasks of different modalities (classification, segmentation) are also done and the method still achieves reasonable performances, showing that the method is generalizable to non-classification tasks. In addition, the ability to flexibly adjust the amount of merging is also a strong point.

3. The paper is well written. It was easy to follow. It is also great that the code is already publicly available.

### Weaknesses
1. My main concern is the stability of the method. I am not sure if the method works robustly across different settings, because empirical observations are reported in the github issues that a small change (e.g. changing the learning rate and epoch numbers when training the models to merge) can cause the merged model to crash to low accuracy.

2. These are not weaknesses but there are some limitations. The performance drop increase when merging multiple models. Accuracy drop looks large when merging models of different tasks (Table 8). All experiments used CNNs and transformers are not tested.

### Questions
1. The meaning of "ensemble" in the experiments is unclear to me. I don't think I understood how it works.

2. I would appreciate more experiments to test the stability of the method. It would also be nice to provide an analysis of when the method works and when it does not. Please see the weakness section for more details.

3. It would also be interesting to include additional experiments on more compact architectures such as Mobilenet for a more comprehensive analysis of the behavior of the method. It is great that ZipIt! is already evaluated on models with larger widths (x1.5 in Table 7). I think it might be harder to merge models where the architectures are already compact because there might be less overlap and less redundancy of features.

4. Can BN be removed before applying ZipIt by fusing it into Conv (using that BN is an affine transform when mean and variance are fixed)? I think then the process to reset BN after merge can be avoided.

### Soundness
3 good

### Presentation
4 excellent

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
This paper proposes a novel method for merging two different models trained from different tasks, maintaining the performance on both tasks. The method resolves the problem of decreasing performance on two disjoint tasks, where prior works fail, ﻿which ﻿permutes the model to another one and the average of them. Moreover, this paper proposed partially zipping to get the trade-off between the performance and the computational complexity.

### Strengths
This paper proposes a novel method named “ZipIt!” which can maintain the performance after merging two models trained from two disjoint tasks, which prior works fail. The partially zipping method can further give the option to do a trade-off between the performance and the FLOPs. Finally, a theoretical proof is given to ensure the existence of a transformation matrix.

### Weaknesses
The method seems not to be practical for real-world usage, while lacks insights and theoretical analysis of the model properties. The method works fine in the CIFAR dataset, but doesn’t have remarkable advantages in large datasets such as ImageNet, and disjoint tasks. Moreover, the paper lacks comparisons between its method and the model trained on both datasets directly, which limits its usage scenario.

### Questions
- I’ve noticed that the “permute” baseline is stronger than “Git Re-Basin”, which is a little strange. I’m wondering how it happens and what’s the experimental setting?
- The improvement on CIFAR is remarkable, while in the larger dataset ImageNet, the trade-off between the performance and FLOPs is debatable. Compared to the ensemble, the FLOPs don’t decrease a lot while getting lower accuracy.
- I’m curious about the comparison between “ZipIt!” method and a single model trained on both datasets. Did you think about this?
- The presentation for “Ensemble” results which uses light grey is a little misleading.
- Are there the results of Git Re-Basin method for ﻿Multi-Dataset in Table 3?
- Did you consider the time cost of computing transformation matrices in your method when comparing the FLOPs?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for merging trained models trained on different datasets without additional training based on feature correlations. The proposed method can further adjust the inference cost and accuracy by adjusting the number of layers to be merged.

### Strengths
1. This paper addresses the interesting research topic of merging models on different datasets without additional training.
2. Large-scale experiments such as imagenet1k confirm the effectiveness of the proposed method. This paper conducts experiments in multi-dataset merging, classification and segmentation merging. In particular, this is the first effort, to my knowledge, to merge the different modalities of classification and segmentation.
3. For reproducibility, the authors mentioned that they plan to publish the source code; the cost of replication experiments would go down significantly if the checkpoints of the trained models were made public since they involve large scale experiments such as cifar100, imagenet1k, and multidataset.

### Weaknesses
1. The paper extends feature matching between models to within the model in order to merging models across different datasets. Its contribution should be examined in more detail. In particular, there is no theoretical support as to why matching the feature would lower the loss after merging. I did not understand the connection between Theorem 1 and the fact that joint Acc can be sufficiently large for merging models on different datasets. Is the extension to "within merge" not only more flexible in alignment, but also suitable for merging models on different datasets?
2. The proposed method is inaccurate for meging of imagenet1k and multi dataset unless partial zip is used, while the inference cost increases as the number of models increases with partial zip.

### Questions
1. Is git-rebasin activation matching considered equivalent to zipit without wighin merge? I would like to know the difference between git rebasin, permute and zipit.
 2. Does merge by zipit keep the output strictly invariant like permutation, even when using pseudoinverse matrix?
 3. What is the same model budget and explain how beta is introduced as an equation?
 4. Three matching methods were proposed in git-rebasin: activation matching, weight matching, and STE. Which method is the baseline in Table 1 and 2? I doubt the claim that permutation alone makes it difficult to merge models on different datasets. According to [1], using STE, which is a permutation base, and Merge models with cifar10(5+5), it is reported that 90% accuracy is achieved, which is 10% more accurate than zipit. I think the conditions are the same as zipit!20/20 in terms of combining all layers.
 5. Sec 5.1 says " `If allow the last stage of the network to remain unzipped (i.e., zip up to 13 layers), our method obtains 83.8%, which is only 3.6% behind an ensemble of model A and model B (which is practically the upper bound for this setting)`", but how can ensemble be guaranteed to be uppper bound?  In [1], a merging model is reported that can achieve higher accuracy than an ensemble. The upper limit of joint accuracy is the accuracy of the model trained on all data, rather than the accuracy of the ensemble.
 6. Why is partially zipping more accurate than fully zipping?
 7. How much gpu is needed for Imagenet-1k (200+200)? I am concerned about the memory and computational cost required to compute the correlation matrix.  
[1]: https://arxiv.org/abs/2306.05641




===========================================

Comments after reading the rebuttal.

===========================================

Since I was unable to set the readers to everyone in the reply, I am writing my comments here.

Thank you for your kind reply.
I did not understand that merging models using loss like STE is outside the scope of this study.
Since this has been resolved in regards to many of my questions, I would like to raise my score.

As other reviwers have pointed out, it would be helpful to specify as a limitation in the camera-ready version of the paper that the model must be wide enough to perform.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of merging two models trained on different "tasks". Their best performing approach is two-fold: 1) identify redundant features within/across models and average those, and 2) only merge some layers. Combined they achieve performance which approaches the ensemble, but their improvements are most notable when the two "tasks" come from the same task, such as partitioning CIFAR in two parts.

### Strengths
- The presentation, including all Figures, is very clear!
- The idea of merging redundant features is interesting and effective. It seems to me that the authors should consider exploring this as a general way of speeding up inference and not just as a technique for merging models.

### Weaknesses
- I would appreciate more motivation for this problem. When would I find myself training from scratch on two different tasks?
- [Subjective] I suggest the authors are much more clear/transparent about their contributions early, because currently the readers get their hopes up a lot when in reality the best performance occurs either when the "tasks" really come from the same task like splitting CIFAR in half. I think there's still a long way to go for training individually on two distinct datasets that are ImageNet level difficulty.
- Figure 1a/b is not exactly clear with respect to related work, for instance [1] (Sec 3.3), and [2] (Appendix E) do consider merging models trained on different tasks, albeit from the same initialization.

[1] Merging Models with Fisher-Weighted Averaging (https://arxiv.org/abs/2111.09832)
[2] Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time (https://arxiv.org/abs/2203.05482)

### Questions
- I would be curious when the authors believe this approach is best applied, e.g., when would I find myself training from scratch on two different tasks?
- Does this approach improve accuracy in more traditional model merging settings? It's pitched for multi-task but is it more general?
- The "scaling" trend in Figure 6b is very interesting! I would be curious to hear if the authors would expect the same trend with a different method to increase FLOPs on the x-axis, such as depth scaling, or joint scaling, or training iterations.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
