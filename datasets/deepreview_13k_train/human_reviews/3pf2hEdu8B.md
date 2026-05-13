# Rethinking the Uniformity Metric in Self-Supervised Learning

- Decision: Accept
- Scores: 8, 6, 5, 5

## Abstract
Uniformity plays an important role in evaluating learned representations, providing insights into self-supervised learning. In our quest for effective uniformity metrics, we pinpoint four principled properties that such metrics should possess. Namely, an effective uniformity metric should remain invariant to instance permutations and sample replications while accurately capturing feature redundancy and dimensional collapse. Surprisingly, we find that the uniformity metric proposed by \citet{Wang2020UnderstandingCR} fails to satisfy the majority of these properties. Specifically, their metric is sensitive to sample replications, and can not account for feature redundancy and  dimensional collapse correctly. To overcome these limitations, we introduce a new uniformity metric based on the Wasserstein distance, which satisfies all the aforementioned properties. Integrating this new metric in existing self-supervised learning methods effectively mitigates dimensional collapse and consistently improves their performance on downstream tasks involving CIFAR-10 and CIFAR-100 datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose criteria for a uniformity loss during representation learning. This criteria is met through the use of the quadratic Wasserstein distance between learned representations and a uniform Gaussian distribution as a loss function, promoting uniformity without reduction in rank of the learned representation. Empirically this is shown to improve performance on the CIFAR-10/100 for a variety of models.

### Strengths
The paper is very well written, clearly stating the desired criteria and showing the proposed approach meets these criteria. The overall motivation behind the desired properties for a representation learning loss seem reasonable with a combination of theoretical justification and intuitive explanation/visualization provided.

Empirically, the results show an improvement by adding the proposed loss function. The authors do a nice job of evaluating the impact of this additional loss term for a variety of approaches.

### Weaknesses
The main weakness of this paper is that experiments are only done for the CIFAR-10/100 datasets. Given the proposed approach is claiming that dimensional collapse represents a fundamental issue with representation learning, the impact/relevance of this claim would be significantly strengthened by showing dimensional collapse is a fundamental issue and not necessarily a product of the CIFAR datasets. The current experiments do not sufficiently demonstrate the generality of the proposed method to other datasets with varying complexities and modalities. It is unclear if the observed improvements are specific to the characteristics of CIFAR, such as its relatively low image resolution and limited number of classes, or if they would generalize to more complex, high-dimensional datasets like ImageNet or those found in other domains such as natural language processing or time series analysis. Furthermore, the absence of experiments on datasets where dimensional collapse is known to be a more pronounced problem makes it difficult to assess the true effectiveness of the proposed loss.

On a related note it would be interesting to see the impact of the proposed metric on differing representation dimensions. In particular would the performance improvements still be observed if the representation dimension was doubled or tripled given that property 5 penalizes constant dimensions, intuitively making it seem that this would require careful selection of the representation dimension. The paper does not explore the sensitivity of the method to the choice of representation dimension, which could be a critical hyperparameter. The lack of experiments varying the representation dimension leaves open the question of whether the observed improvements are robust across different representation sizes, and if the proposed loss might inadvertently hinder learning when the representation dimension is not optimally chosen. It is also unclear how the proposed loss interacts with the inherent dimensionality of the data itself.

### Questions
Are there any results for differing representation dimensions?

(Not a negative comment, just hoping to get some insight into the behavior of the loss) Is there any intuitive reason as to why the top-5 accuracy decreases for MoCo and BarlowTwins on CIFAR-10 using the proposed loss even though the top-1 accuracy increases?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explains the shortcomings of the existing uniformity metric and the potential dimensional collapse then the authors propose new metrics of uniformity. Numerous experiments have proved its effectiveness.

### Strengths
The uniformity metrics proposed in this paper are more comprehensive and their validity has been verified experimentally.

### Weaknesses
Can the authors further elaborate on the importance of ICC, FCC and FBC to better understand the difference between the proposed metric and previous metrics?

### Questions
Why the new metric has a relatively small performance increase on zero-CL?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the author revisits the alignment and uniformity property in Self-Supervised Learning and shows that the metric in [1] lacks the ability to measure dimensional collapse, which is a phenomenon where the representations learned through self-supervised learning span a low-dimensional subspace instead of being distributed uniformly in the representation space. Therefore, the author proposes a new metric utilizing the Wasserstein distance between the distribution of the representation space and the normalized isotropic Gaussian distribution.

[1] Tongzhou Wang and Phillip Isola. Understanding contrastive representation learning through alignment and uniformity on the hypersphere. In ICML, 2020.

### Strengths
1. The paper includes a lot of empirical analysis to demonstrate the effectiveness of the proposed metric.
2. The paper is well-written and easy to follow.

### Weaknesses
1. The font size of the figures is too small.
2. It should be made more clear why the original metric doesn't correspond to the proposed 5 properties and how these properties are related to dimensional collapse.
3. It should be made more clear why dimensional collapse is a undesired property in self-supervised learning.
4. Since $\mathcal{W}_2$ is also related to the covariance matrix of representation, what is the relationship between the proposed method and Barlow Twins/VICReg?
5. Why is the KL divergence of $Y$ and $\hat{Y}$ not presented for comparison as in Figure 3?
6. As in [2], the phenomenon of dimensional collapse happens in the embedding space. However, in [2], when the projector is presented, the representation space doesn't collapse. Therefore, why do the singular values of the representation in Figure 8 collapse?

### Questions
Please refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study develops a new metric assessing the robustness of learnt representations by measuring collapse degree of them. The authors first point out the weakness of previous metrics proposed by Wang & Isola (2020) in its insensitivity with dimensional collapse. In addition, five characteristics are determined as the criteria for the ideal metric. The new metric (*Wasserstein Distance* between normalized learnt representations’ distribution with zero-mean isotropic Gaussian distribution) is introduced satisfying all these criteria, and illustrates its sensitivity towards dimensional collapse. Empirically, this metric help boosting existing frameworks’ performance in downstream tasks.


Reference:

Wang, T., & Isola, P. (2020, November). Understanding contrastive representation learning through alignment and uniformity on the hypersphere. In *International Conference on Machine Learning* (pp. 9929-9939).

### Strengths
- Contribution:
    - This study stems from a good motivation: The lack of current researches explicitly dealing with representation collapse - here dimensional collapse.
    - 5 listed criteria for the ideal ‘uniformity’ metric are logically/mathematically sensible. By pointing out the failure of previous work’s metric (Wang & Isola, 2020), the authors clarify the need for a new metric.
    - The experiments (e.g. Table 2) compare various vanilla approaches with their variance with the proposed metric. These are representative frameworks following three existing directions in dealing with constant collapse. This suggest the potential robustness of proposed metrics when being incorporated to a wide range of models.

- Presentation:
    - The intuitive flow makes it easy catch on what the authors want to deliver.
    - The authors provide trackable mathematical notations and derivations.

### Weaknesses
 
- While the 5 criteria are sensible, they can be considered as **necessary conditions** for a good metric. However, no assessment made to ensure they are **sufficient** to construct an ideal one.
- The key contribution of the work - new ‘uniformity’, currently rely on the assumption that the learnt representations follow a Gaussian distribution, which, in turn, can fall apart and the metric can cause undesired effect. This assumption is particularly concerning given that the very problem the paper addresses is representation collapse, which could easily lead to non-Gaussian distributions. The authors should provide more justification for this assumption, especially in the context of collapsed representations.
- For experiments, only what related to collapse analysis there exists the comparison between Wang & Isola’s ‘uniformity’ metric with the proposed one. We can conclude nothing on the better performance of the proposed WD-based loss when fused with existing frameworks. It seems not convincing for developing a new loss if the existing loss still works better.


### Questions
- Can the authors empirically justify if the proposed loss outperform existing loss when being incorporated with other frameworks?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
