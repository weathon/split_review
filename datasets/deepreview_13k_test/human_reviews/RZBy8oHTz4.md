# Zero-Mean Regularized Spectral Contrastive Learning: Implicitly Mitigating Wrong Connections in Positive-Pair Graphs

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Contrastive learning has emerged as a popular paradigm of self-supervised learning that learns representations by encouraging representations of positive pairs to be similar while representations of negative pairs to be far apart. The spectral contrastive loss, in synergy with the notion of positive-pair graphs, offers valuable theoretical insights into the empirical successes of contrastive learning. In this paper, we propose incorporating an additive factor into the term of spectral contrastive loss involving negative pairs. This simple modification can be equivalently viewed as introducing a regularization term that enforces the mean of representations to be zero, which thus is referred to as *zero-mean regularization*. It intuitively relaxes the orthogonality of representations between negative pairs and implicitly alleviates the adverse effect of wrong connections in the positive-pair graph, leading to better performance and robustness. To clarify this, we thoroughly investigate the role of zero-mean regularized spectral contrastive loss in both unsupervised and supervised scenarios with respect to theoretical analysis and quantitative evaluation. These results highlight the potential of zero-mean regularized spectral contrastive learning to be a promising approach in various tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this point, the authors try to extend spectral contrastive learning with negative pairs. By adding a zero-mean regularization, the loss function relaxes the orthogonality of representations between negative pairs and implicitly alleviates the adverse effect of wrong connections in the positive-pair graph, leading to better performance and robustness. Beyond that, this paper gives a solid theoretical analysis for the regularization.

### Strengths
1. This paper is very easy to follow. The motivation is very clear, and the methodology is elegant.

2. The perspective of UDA is novel. It provides a different way to observe contrastive learning.

3. The perspective of supervised classification with a noise label is also helpful for contrastive learning.

### Weaknesses
1. The novelty is an issue. According to the Equ 3.2, it is the same as contrastive laplacian eigenmaps (NeurIPS 2021). In contrastive laplacian eigenmaps, they have the same three terms. The main point is the fully connected adjacent matrix (the all-one matrix).

### Questions
I would like to hear from authors about the relationship between this one and contrastive laplacian eigenmaps. I think the authors give a totally different theoretical analysis based on a very similar thing.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide a new regularizer for (spectral) contrastive
learning which supposedly improves the quality of the representation.
The authors provide experiments to show the quantitative improvements
due to their method.

### Strengths
The regularization is well-motivated and intuitively explained.  The
experiments seem convincing and suggest that the improvement is
consisent across datasets.

The appendix is extensive.

### Weaknesses
The results on the CIFAR datasets are not state-of-the-art for
contrastive learning.  This begs the question whether the regularizer
could also be applied to other CL techniques such as SimCLR or others.
Hopefully the regularization would also help in that case.

Table 1 & 2 only report single numbers.  It would be more convincing
if there was a mean +- std reported or some other statisic computed
over multiple runs.

### Questions
Could the approach be extended to other CL techniques?  Do you expect
it to improve the results similarly?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
By incorporating an additive factor into the SpeCL term that involves negative pairs, this paper enforces the mean of representations to be zero. The experimental results and related theoretical analysis suggest that introducing $\tau$ can improve performance.

### Strengths
1.This paper addresses the issue of negative pairs in contrastive learning, which is a hot topic in the research community. The authors aim to provide a solution to this problem that arises in related CL works.

2.The authors of this paper present a theoretical foundation to support the proposed zero-mean regularization in both the unsupervised domain adaptation (UDA) task and supervised classification with noisy labels.

3.The proposed method's robustness is improved by the impressive results achieved on the supervised classification task, particularly when dealing with symmetric label noise.

### Weaknesses
1. This work appears to be relatively incremental based on Ref. [18] and [19]. Basically, what caught my interest is the representation of spectral embeddings using affinities and features; however, it was previously proposed in [18].

2. Although the authors describe the proposed additive factor as simple yet effective, this work can still be considered progressive research. However, when compared to [18] and [19], it is unclear whether significant progress has been made for this conference.

3. The effectiveness of the proposed method is demonstrated through experiments that involve fewer state-of-the-art methods.

### Questions
1. On page 4, there is a missing space in "thatSpeCL".

2. It is suggested to include more benchmark methods in the experiments to avoid categorizing it as an enhanced/improved version of SpeCL method, and instead position it as a robust SSL method.

3. The factor $τ$ effectively relaxes the orthogonal constraint on negative pairs. It would be interesting to explore the integration of other methods, such as Barlow Twin, in different ways.

4. In the experiments, it is recommended to analyze the results achieved with different values of $\tau$ due to its previous detailed analysis. This analysis can provide insights into what can be inferred from the results obtained with different $\tau$ values.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
