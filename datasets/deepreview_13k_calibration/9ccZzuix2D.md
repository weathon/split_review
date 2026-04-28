# Distilling the Knowledge in Data Pruning

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
With the increasing size of datasets used for training neural networks, data pruning becomes an attractive field of research.
However, most current data pruning algorithms are limited in their ability to preserve accuracy compared to models trained on the full data, especially in high pruning regimes. 
In this paper we explore the application of data pruning while incorporating knowledge distillation (KD) when training on a pruned subset. 
That is, rather than relying solely on ground-truth labels, we also use the soft predictions from a teacher network pre-trained on the complete data.
By integrating KD into training, we demonstrate significant improvement across datasets, pruning methods, and on all pruning fractions. 
We first establish a theoretical motivation for employing self-distillation to improve training on pruned data.
Then, we empirically make a compelling and highly practical observation: using KD, simple random pruning is comparable or superior to sophisticated pruning methods across all pruning regimes.
On ImageNet for example, we achieve superior accuracy despite training on a random subset of only 50\% of the data. 
Additionally, we demonstrate a crucial connection between the pruning factor and the optimal knowledge distillation weight. This helps mitigate the impact of samples with noisy labels and low-quality images retained by typical pruning algorithms.
Finally, we make an intriguing observation: when using lower pruning fractions, larger teachers lead to accuracy degradation, while surprisingly, employing teachers with a smaller capacity than the student's may improve results.
Our code will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an in-depth investigation into the use of knowledge distillation (KD) for training models on pruned datasets. It provides a comprehensive analysis of the performance of models trained using various dataset pruning strategies and pruning factors across multiple datasets, both with and without the application of KD from their pretrained teachers. Based on the experimental findings, the authors demonstrate that employing a teacher model trained on the full dataset can effectively enhance the performance of student models trained on pruned datasets.

### Strengths
1. The experiments in this are comprehensive and sufficient.

2. The theoretical motivation is well-written and reasonable.

3. The paper is easy to read and follow.

### Weaknesses
1. The paper has a reference formatting issue. According to the ICLR submission guidelines, `\citep{}` should be used instead of `\cite{}`.

2. The motivation is confusing and needs more clarification. Specifically, this study proposes training a model on a pruned dataset using knowledge distillation from the same model that has already been trained on the full dataset. However, if a well-performing model has already been obtained through training on the complete dataset, it raises the question of __why it is necessary to train the same model from scratch on a pruned dataset__. Providing a stronger rationale for this approach would enhance the clarity and relevance of the study.

3. Although this paper has provided a large volume of experimental results, there lack of insightful analysis. For instance, how different dataset pruning approaches behave differently under the same self-distillation schema can be explained.

4. In Figures 4 and 5, only hard dataset pruning approaches have been compared, while the easy (such as herding) and moderate (such as MoDS) pruning methods are not compared.

5. In Section 4.2, the experiments on adaptive KD weights and pruning factors are only conducted on the CIFAR-100 dataset. The results indicate varying optimal KD weight choices for different pruning factors: a smaller KD weight is preferred when the pruning factor is close to 1, whereas a larger KD weight is favoured when the factor is around 0.1. However, there does not appear to be a consistent pattern underlying this behaviour, making it less practical in real-world datasets. Furthermore, the accuracy gap between different KD weights can exceed 8% from 0.5 to 1.0. It is reasonable to anticipate this accuracy gap escalates on a larger dataset, such as ImageNet-1k. In this case, it is unclear how to choose the optimal weight for a large dataset.

### Questions
1. According to W2 and W3, the authors should provide more concrete motivation on why this study is contributive and in what real-world scenarios this analysis can be applied.

2. According to W4 and W5, the authors should provide more experiments to demonstrate the generalizability and practicality of the proposed self-distillation approach.

I'm willing to raise my rating to positive if the authors can provide convincing motivations and necessary experimental results.

### Soundness
3

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
4

### Summary
Accompanied by a theoretical motivation, the major goal of the paper is to incorporate knowledge distillation to boost the model trained on the pruned dataset. With experiments conducted in image classification, the authors make some observations regarding, e.g., the connection between the pruning factor and the KD weight.

### Strengths
1.	The paper is well-organized and easy to follow.
2.	Some empirical observations are intriguing, e.g., distilling with pruned data will exacerbate the gap problem [1], which may provide some insights for further research regarding data pruning and knowledge distillation.
3.	[1] Improved Knowledge Distillation via Teacher Assistant, 2019, AAAI.

### Weaknesses
1.It seems the paper is a simple combination of two well-established techniques, and KD has been successfully utilized to boost the model performance. In this way, the overall novelty and contribution are limited. Do the authors have deeper insights regarding the interplay between KD and data pruning, e.g., pruning certain data leads to a better distillation performance (such as [1]), or if can KD be leveraged to identify important samples in data pruning.
[1] Teach Less, Learn More: On the Undistillable Classes in Knowledge Distillation, 2022, NeurIPS.
2.The evaluated KD and data pruning methods are rather outdated. It's necessary to include the latest methods, e.g., [2][3][4].
[2] Decoupled Knowledge Distillation, 2022, CVPR.
[3] Knowledge Distillation from A Stronger Teacher, 2022, NeurIPS. 
[4] Data Pruning via Moving-one-Sample-Out, 2023, NeurIPS.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to apply knowledge distillation techniques when a model is trained on a pruned dataset. The authors provide theoretical analysis stating that error distilling from a teacher model trained with full data will be smaller than that from a teacher trained with pruned data. Experiments on CIFAR, SVHN, and ImageNet demonstrate that applying distillation can largely enhance the performance.

### Strengths
1. The proposed solution is simple but effective. Merely applying dataset distillation can result in a lot of benefit on performance.
2. The writing is logical and clear. I am able to follow the method descriptions, experiments, and theoretical validation.

### Weaknesses
1. Although the solution is indeed simple yet effective, I do not find it surprising. After all, it is a well-known trick to apply knowledge distillation to enhance the performance, especially in the industrial community when there are insufficient data. In the academic community, there are indeed works putting forward similar insights, like [a], which also focuses on data pruning. The difference is only on sample-wise pruning in this paper and patch-wise pruning in [a].
2. It seems that the experiments are not closely aligned with the theoretical analysis. Theorem 1 would like to convey that, error distilling from a teacher model trained with full data will be smaller than that from a teacher trained with pruned data. Therefore, I expect the experiments would try to validate this point by changing $f_t$. However, almost all the experiments currently are conducted with respect to $f$.
3. Following 2, according to the proof of Theorem in the appendix, the error would monotonically decrease with the increasing of $f_t$, the data amount used for training teacher models. It seems that it cannot support the experimental finding that using a teacher model with limited capacity is better. I understand that $f_t$ indicates the data portion, which may be different from the perspective of model architecture used in experiments for various capacity. Anyway, more experimental validation with respect to $f_t$ is necessary here to support Theorem 1.

### Questions
See weaknesses.

### Soundness
2

### Presentation
4

### Contribution
2
