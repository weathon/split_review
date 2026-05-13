# Less is More: On the Feature Redundancy of Pretrained Models When Transferring to Few-shot Tasks

- Decision: Reject
- Scores: 8, 3, 6, 5

## Abstract
Transferring a pretrained model to a downstream task can be as easy as conducting linear probing with target data, that is, training a linear classifier upon frozen features extracted from the pretrained model. As there may exist significant gaps between pretraining and downstream datasets, one may ask whether all dimensions of the pretrained features are useful for a given downstream task. We show that, for linear probing, the pretrained features can be extremely redundant when the downstream data is scarce, or few-shot. For some cases such as 5-way 1-shot tasks, using only 1% of the most important feature dimensions is able to recover the performance achieved by using the full representation. Interestingly, most dimensions are redundant only under few-shot settings and gradually become useful when the number of shots increases, suggesting that feature redundancy may be the key to characterizing the "few-shot" nature of few-shot transfer problems. We give a theoretical understanding of this phenomenon and show how dimensions with high variance and small distance between class centroids can serve as confounding factors that severely disturb classification results under few-shot settings. As an attempt at solving this problem, we find that the redundant features are difficult to identify accurately with a small number of training samples, but we can instead adjust feature magnitude with a soft mask based on estimated feature importance. We show that this method can generally improve few-shot transfer performance across various pretrained models and downstream datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper explores the phenomenon of feature redundancy in pre-trained models when applied to few-shot learning tasks. The paper demonstrates that not all dimensions of the pre-trained features are useful for a given downstream task, especially when the data is scarce. In some cases, using only 1% of the most important feature dimensions can recover the performance achieved by using the full representation. This feature redundancy is particularly prominent in few-shot settings and diminishes as the number of samples increases.
The paper also delves into the theoretical understanding of this phenomenon, showing how dimensions with high variance and small distance between class centroids can serve as confounding factors that disturb classification results in few-shot settings. To address the issue of feature redundancy, the paper proposes adjusting feature magnitude with a soft mask based on estimated feature importance. This method is shown to generally improve few-shot transfer performance across various pre-trained models and downstream datasets.

### Strengths
1. This paper studies an interesting and important problem of feature redundancy, especially in the context of few-shot learning.
2. This paper provides a theoretical framework that sheds light on the complex phenomenon of feature redundancy.
3. This paper also proposes a novel solution to the problem of feature redundancy by adjusting feature magnitude with a soft mask based on estimated feature importance. This is a practical approach that shows promise in improving few-shot transfer performance.
4. The paper is well-structured and clearly written, making it accessible to both experts and those new to the field.

### Weaknesses
Despite the above strengths, this paper also has some drawbacks:

1. While this paper studies the few-shot problem, it mainly focuses on the nearest-centroid classifier (NCC) and employs Euclidean distance as the distance metric. However, it is worth noting that most practical few-shot methods use **cosine distance** rather than Euclidean distance. Therefore, to enhance precision and applicability, it is advisable for the paper to explicitly limit its claims to Euclidean distance-based scenarios. It would be beneficial for the authors to acknowledge this limitation and potentially explore how the theoretical and empirical analysis may adapt to cosine distance-based methods. This could provide a more comprehensive understanding of the practical implications of the work. The current analysis lacks a clear discussion on how the observed feature redundancy might vary under different distance metrics, which is crucial for the generalizability of the findings.

2. I understand that different features have different importance [1]. The central argument of this paper is that utilizing a reduced set of crucial features outperforms the use of all available features. However, I noticed another paper [2] providing empirical evidence to the contrary, suggesting that "tail" features are more important than the core features in the few-shot problem.   

- I wonder if the contradiction between these perspectives comes from the use of distinct distance metrics, as [2] employs Kendall distance. If so, this reminds us again that this work is primarily applicable within the context of Euclidean distance. It is critical to investigate whether the feature selection method proposed is robust to changes in the distance metric or if it is inherently tied to Euclidean distance.

3. The proposed solution relies on estimating feature importance, which itself can be challenging in a few-shot setting as mentioned in the paper. A compromise method is applying data augmentation to the training data. However, this is a little bit unfair for few-shot learning since it could be regarded as an implicit means of augmenting the number of shots through the incorporation of human knowledge. The paper should acknowledge that the use of data augmentation in this context might conflate the benefits of the proposed method with the benefits of increased data diversity, making it harder to isolate the true impact of feature selection.

4. The math part of this paper has many unclear areas:

- Page 6: $z$ depends on label $y$, and thus you should use different subscripts to distinguish them. For example, $z_y\sim N([\mu_{(y,1)},\mu_{(y,2)}]^T, diag(\sigma_1^2, \sigma_2^2))$. Moreover, you should remind readers that you use the same $\sigma_1$ and $\sigma_2$ for different $y$, since they are different in Eq. (1).

- Theorem 5.1: The formula of error rate in Eq. (3) is not intuitive enough. I suggest to use the equivalent form $\Pr[|(z_1,z_2)-(p_{(a,1)},p_{(a,2)})| > |(z_1,z_2)-(p_{(b,1)},p_{(b,2)})|]$ instead.

- Theorem 5.2: The simultaneous presence of both "with probability at least 0.9 (a certain number)" and "big O" renders this theorem meaningless. For example, choosing $999999999\sqrt{\log n/n}$ as $O(\sqrt{\log n/n})$ and choosing $0.0000001\sqrt{\log n/n}$ as $O(\sqrt{\log n/n})$ should have different probabilities. I believe it is possible to derive a closed-form expression for $O(\sqrt{\log n/n})$.

### Questions
Why are linear probing and NCC actually the same for 1-shot task? (Table 1)

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper highlights feature redundancy in transferring pretrained models to few-shot tasks using linear probing protocols. The study also offers theoretical analysis and proposes a data augmentation-based solution.

### Strengths
The paper provides a thorough evaluation of various downstream tasks using multiple pretrained models, both supervised and self-supervised. 

The paper is well-written.

### Weaknesses
The term *feature redundancy* in the paper is somewhat misleading, as it doesn't provide evidence of mutual information between feature distributions.  It is more like *some features are distinguishable for downstream tasks, while others are not*. The paper lacks a rigorous quantification of feature redundancy using measures like mutual information or other established metrics, which would strengthen the claim. It is unclear if the observed phenomenon is due to actual redundancy or simply varying relevance of features. 

The findings, from the perspective that *'some features are distinguishable'*, are not particularly surprising. It's expected that features in a pretrained model may vary in their relevance to downstream tasks, and different tasks may have distinct feature preferences. The idea that not all features are equally informative for a given downstream task is well-established in the literature. The paper does not adequately contextualize its findings within this existing body of work. The claim that identifying these distinguishable features is a novel contribution needs further justification. 

Sensitivity to linear classifiers on indistinguishable features with few samples is also a common expectation, and the improvement from data augmentation can be viewed as adding more data. The paper does not sufficiently address the potential confound of data augmentation, and it's not clear whether the observed improvements are due to the proposed method or simply the increased diversity of training data. The paper would benefit from more controlled experiments to isolate the effects of the proposed method from the effects of data augmentation.

### Questions
Is it possible to evaluate the mutual information of features?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper primarily addresses the issue of feature redundancy in pretrained models when transferring to downstream few-shot tasks. It then proceeds to conduct a thorough theoretical analysis to explain why this phenomenon specifically occurs in few-shot settings. Additionally, this paper introduces the concept of a soft mask based on feature importance to identify redundant dimensions. According to experimental results, this approach performs effectively in few-shot transfer scenarios.

### Strengths
+ This paper introduces a novel and interesting perspective suggesting that a select few feature dimensions can achieve performance comparable to using all dimensions in few-shot settings. Such a phenomenon of feature redundancy warrants deeper investigation.
+ Experimental results show that employing a soft mask based on feature importance is effective in most few-shot transfer scenarios. Additional examples in the appendix further underscore the efficacy of this method.
+ In-depth theoretical insights elucidate the reasons behind the existence of the feature redundancy phenomenon in few-shot settings. Figures like Fig 1 explicitly corroborate the idea that increasing the number of retained dimensions can initially enhance performance, then subsequently leads to a decline.

### Weaknesses
Identifying redundant dimensions more effectively with limited samples could be a potential avenue for future research. While this paper suggests estimating feature importance using augmented data, I have reservations about whether augmented data can genuinely replicate the true data distribution.If the data augmentation technique were altered, would it obviously influence the experimental outcomes?

As noted in the paper, the optimal data augmentation technique can vary significantly across different datasets. Is the cropping operation specifically recommended, or can other methods yield equally effective experimental results?

### Questions
Please refer to the weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work find a novel phenomenon for linear probing that the representation from large pre-trained model has dimension-redundancy problem for downstream few-shot tasks. Specificly, most dimensions are redundant only under few-shot settings and gradually become useful when the number of shots increases. The authors provide a theoritical analysis on toy experiments and use feature importance estimate to select the important dimensions for each few-shot task. The experiments on many datasets and pre-trained model verify this phenomenon and the effectiveness of the proposed method.

### Strengths
1. This work finds an interesting phenomenon about few-shot transfer and provides detailed analysis.  
2. The paper is organized and written well, and the motivation is clear to me.  
3. The toy experiments and theoretical analysis are meaningful and help to understand this work.  
4.The authors conduct extensive experments on many different datasets and different pre-trained models.

### Weaknesses
1. The proposed method is over-simple and more like a trick. And thus there are no ablation study. I suggest the method can be more systematic.  
2. Fine-tuning is typically a more preferred method and achieve better performance than linear probing, so it has a weak value to solve linear probling alone. How the proposed method perform for fine-tuning?  
2. As shown in Figure 2, the proposed phenomenon seems to disappear when way is large. In fact, I think the large way is more realistic and ractically useful.  
3. How the proposed method perform under many-way classification? The authors only provide the results on 5-way setting, how about the results on 20-way, 50-way setting?

### Questions
Please respond to the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
