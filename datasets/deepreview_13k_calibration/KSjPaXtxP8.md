# Memorization in Self-Supervised Learning Improves Downstream Generalization

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Self-supervised learning (SSL) has recently received significant attention due to its ability to train high-performance encoders purely on unlabeled data---often scraped from the internet. This data can still be sensitive and empirical evidence suggests that SSL encoders memorize private information of their training data and can disclose them at inference time. Since existing theoretical definitions of memorization from supervised learning rely on labels, they do not transfer to SSL. To address this gap, we propose \name, a framework for defining memorization within SSL. Our definition compares the difference in alignment of representations for data points and their augmented views returned by both encoders that were trained on these data points and encoders that were not. Through comprehensive empirical analysis on diverse encoder architectures and datasets we highlight that even though SSL relies on large datasets and strong augmentations---both known in supervised learning as regularization techniques that reduce overfitting---still significant fractions of training data points experience high memorization. Through our empirical results, we show that this memorization is essential for encoders to achieve higher generalization performance on different downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors propose SSLMem, a framework for defining memorization within Self Supervise Learning (SSL). The authors base their framework analyzing the  difference in alignment of representations for data points and their augmented views returned by encoders. They show an empirical analysis on diverse encoder architectures and datasets, highlighting that significant fractions of training data points experience memorization, and highlight that memorization is essential for encoders to achieve generalization performance on downstream tasks.

### Strengths
-good presentation and writhing

-easy flow of argumentation

-interesting and valuable insights related to the interplay between memorization and generalization

### Weaknesses
 -importance and influence of the augmentations, it would have been nice to see does a particular or a set of augmentations plays a role in this empirical evaluation, also instead of the augmentations, how similar data samples play a role it would be interesting to analyze

-regarding the experiment considering differential privacy, only one algorithm was evaluated, I was not able to see other evidence (evaluation using different setups and algorithms) that supports the case about memorization in this context

### Questions
Does a particular augmentation or a set of augmentations plays a role in this empirical evaluation?

How does similar data samples play a role with respect to the memorization vs generalization claims?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a way to measure memorization at the representation level, which is applicable to SSL approaches, in contrast to previous work quantifying memorization in supervised learning. The memorization metric is based on measuring differences in alignment between different views of the same input point, between models trained with and without the specific point.
With their new measure, the authors investigate the degree of memorization in encoder models using different architectures, trained on different datasets and using different SSL approaches. They find that SSL-trained models exhibit memorization and that the degree of memorization benefits downstream performance.

### Strengths
- Relevance: Understanding memorization is an important problem, which is challenging and underexplored in the SSL domain. The paper makes an important contribution in conceptualizing memorization in this space, as well as proposing a corresponding measure. Further, a representation-level measure of memorization is a valuable tool that could be applied in other interesting ways as well, such as localizing memorization in models.
- Soundness: The experiments are thorough and the methodology is solid.
- Presentation: The paper is well written and easy to follow.

### Neutral:
- Novelty: The findings seem to be similar to those made for supervised learning, i.e. that memorization benefits generalization, as well as atypical points exhibiting more memorization. However, SSL approaches use a different learning paradigm, so it is not a priori clear whether one should expect similar trends to hold. It is therefore interesting to see that similar dynamics hold for SSL models as well.

### Weaknesses
 - The results seem to show that memorization benefits downstream performance. However, *why* this is happening is not quite clear to me. For instance, when removing points with high memorization scores from the training data, does the performance of the model primarily drop on points "similar" to the removed ones? If this was the case, memorization here might actually be more of a long-tail generalization phenomenon.
- In Section 4.4, Eq. (3) you limit the degree of alignment between representations. However, in addition to reducing memorization, this intervention might also degrade the representations in other ways. Therefore, it's not clear to me whether we can conclude that a reduction in memorization is causing a drop in accuracy, or whether both might just be consequences of a degradation in representation quality due to the regularization. Specifically, the regularization term in Eq. (3) directly penalizes alignment, which is also a core objective of SSL methods. It's difficult to disentangle whether the performance drop is due to reduced memorization or simply a degradation in the learned representations due to this conflicting objective.
- There are some smaller clarity issues:
    1. In Section 4, first paragraph, what is the normalization procedure applied to constrain memorization scores between -1 and 1?
    2. You say that experiments are repeated over three independent seeds. Does that mean you use different data splits for each seed or just different weight initializations of the models?
    3. Table 1, what is "Frac. Mem."? Is it the same as "Avg. Mem." defined in the caption?
    4. In 4.4, do you remove the 500, 1K, etc. datapoints with highest memorization from the set of 25K points, or from the full CIFAR10 training set?
    5. In 4.4, why do you use cosine similarity here vs l2 distance earlier?
    6. In 4.5, what does the term "exploited" in the context of Deja Vu mean? Would you expect MAE to exhibit higher memorization?

### Questions
- Does the metric agree with previous metrics for quantifying memorization in supervised learning? I.e. given a supervised learning model (where you can apply prior supervised learning work), would the metric highlight the same points as memorized as previous metrics for supervised learning?
- How dependent is the metric on the types of data augmentations used? I.e. if a model was trained with masking, would the metric also be able to quantify memorization under e.g. rotation or noise augmentations?
- What are atypical datapoints? Is the judgement of typicality just based on visual inspection or are there other indicators as well?
- The idea behind the metric is that quantifying memorization via alignment differences between different augmentations of the same input point is the common denominator between different SSL approaches (contrastive, non-contrastive, reconstruction-based). Would it be possible to define a "stronger" notion of memorization if one were to only consider one family of SSL approaches, e.g. contrastive ones?

### Suggestions:
- Giving the memorization metric a name would make it easier to refer to it.
- Given that the proposed metric operates at the representation level, it might be interesting to quantify memorization at intermediate layers in the model, to potentially localize where it is happening.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors address an interesting issue in self-supervised learning (SSL): the impact of memorization on both SSL and its effects on downstream tasks. They examine the dissimilarity in the representations alignment between augmented views produced by encoders trained on a specific point and those that were not. This problem statement holds relevance in light of the current privacy concerns surrounding deep learning models

### Strengths
- It is true that there are not many works addressing the memorization vs. generalization aspect of SSL. This paper aims to address this important issue.

- The proposed method is agnostic to SSL methods and augmentations, making it applicable in various cases.

- It is an insightful study in the right direction. Understanding memorization significantly impacts the generalization of SSL models. The authors have done an excellent job with their extensive empirical analysis.

### Weaknesses
 - There are several works discussing the issue of memorization in self-supervised learning, which haven't received thorough attention in the literature review. While I understand that not all of these works are directly related, a broader discussion of related literature would enhance the paper's readability (e.g., [1, 2]). Specifically, the authors should discuss how their approach relates to methods that analyze memorization through the lens of training dynamics or generalization gaps, and clarify the novelty of their memorization metric in light of existing work.

- In the machine learning research community, it's generally accepted that there exists a tension between memorization and generalization. However, I would appreciate more clarity and intuition from the authors regarding why memorization leads to improved generalization. The authors need to provide a more detailed explanation of the underlying mechanisms by which memorizing specific data points enhances the overall generalization performance, especially given the common understanding that memorization often hinders generalization.

- Although the memorization score is simple, model- and augmentation-agnostic, it lacks intuitive explanations and theoretical background. It would be beneficial for the authors to provide reasons for why this score measures memorization and offer any applicable theoretical support. The current justification is insufficient, and a more rigorous explanation grounded in theoretical principles is needed to validate the proposed metric as a reliable measure of memorization.

- Regarding the statement, "Our definition compares the difference in alignment of representations for data points and their augmented views returned by both encoders that were trained on these data points and encoders that were not," I'd like to seek clarification. It seems that the training sets of g and f overlap. Could you please provide a justification for this design choice? I had expected a distinct encoder with a different training set or random initialization. The authors should elaborate on why this specific overlap is necessary and how it impacts the memorization score. The current explanation lacks sufficient detail to justify this design choice.

- Considering the proposed metric and previous works in supervised learning, it appears that the contributions are more incremental than novel.

### Questions
- “we consider a data point as having a high level of memorization by an encoder $f$ if its alignment is significantly higher on $f$ than on encoder g that was not trained with the considered data point” – Why is this the case? Are there any exceptions where this doesn't hold true?

- I understand that the memorization score is relative. However, can one freely choose $g$ as our interest primarily lies in $f$? Have you conducted any ablation studies on the choice of model architectures for $g$ while keeping $f$ constant? Is it necessary for both $g$ and $f$ to share the same architecture?

- What if $g$ is pre-trained on a large but distinct dataset instead of being randomly initialized? Would that result in a reduced memorization score?"

- The training data is divided into 80%, 10%, and 10%. The last two sets do not overlap between $g$ and $f$. How does memorization change when we vary the overlapping ratios from 80% to 70%, 50%, and 30%?

- “We formally verify that data points from Sc (Si ) have statistically significantly higher (lower) memorization scores m than those from Ss and Se.”
“They support the claim that Sc (Si ) is substantially more (less) memorized than Ss and
Se”.
Why is it the case that Sc is substantially more memorized than Ss? Isn't this because memorization is a relative score, and Ss was used to train both $g$ and $f$?

I find this work quite interesting overall. However, in its current form, it lacks sufficient intuition to answer 'why' questions such as:

- Why does memorization lead to generalization?
- Why is the proposed metric suitable for measuring memorization?
- Why were certain design choices made, like training percentages and architecture selections for $g$ and $f$?

The authors need to provide more comprehensive reasoning for their results. Simply presenting empirical findings is insufficient and can lead to confusion for readers.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel framework that defines memorization within the context of self-supervised learning (SSL). This definition compares the difference in alignment of representations for data points and their augmented views returned by encoders that were trained on these data points and encoders that were not. Empirical analysis on diverse encoder architectures and data sets demonstrate that significant fractions of training data points experience high memorization in SSL, and memorization is essential for encoders to achieve higher generalization performance on different downstream tasks.

### Strengths
- The authors propose a novel definition that generalizes memorization effect to self-supervised learning, which can be useful for understanding model generalization
- This paper is easy to understand

### Weaknesses
 - The proposed framework lacks enough practical implications. It is not so clear how we should treat samples with higher/lower memorization scores differently. 
- Several claims are subject to challenge, as can be found in Questions part. 
- Empirical results may be further improved, including more different architectures and data sets.

### Questions
- The definition of (per-example) memorization score is a bit strange. From my perspective, a higher memorization score indicates that sample $x$ has larger impact to model performance. As such, it seems natural that pre-trained models with higher memorization perform well on downstream tasks: if not, it means all training samples do not contribute much to pre-training, and it will be strange that pre-training on such data set produces good models. Some more explanations may be needed on why we need to introduce memorization score here, instead of some other performance metrics. 
- Also, it would be better if the authors can show some connections between other metrics on generalization (examples may be found in [1]) and the proposed memorization score. It would be useful to see how good final performance comes from higher memorization scores beyond simply putting them together. 
- While the authors claimed that their experiments cover different architectures and downstream data sets, the experiments seem a bit restricted from my perspective. For architectures, it would be better if the authors can report i) same architecture (e.g., ResNet) with different depths, widths, etc. and ii) similar number of parameters with different architectures (ViT and ResNet here). That will make the experimental results more comprehensive and we may also gain some insights on how memorization differs across different architectural settings
- Also, downstream data sets used in current paper (CIFAR-10/100, SVHN, STL-10, ImageNet) are all coarse-grained general classification data sets. The authors may consider also adding some experiments on fine-grained data sets (e.g, Food-101 or Flower102, which are popularly used in literature) and see if their conclusions are changed. 
- Regarding experiments on removing samples for downstream tasks, the performance gap seems not so large. What will happen if we directly try to remove some samples to obtain largest performance drop? Will these samples found have larger memorization scores? Some additional experiments are welcome. 
- I also wonder how it is connected to research on coresets [2], which aims to find a (small) subset of training data that can help obtain models with performances close to full training data. The authors may report something opposite to Figure 3 and Table 3: solely train on samples with high memorization scores, and see how the model works.  

References: 

[1] Fantastic Generalization Measures and Where to Find Them. ICLR 2020

[2] Deep Learning on a Data Diet: Finding Important Examples Early in Training. NeurIPS 2021

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
