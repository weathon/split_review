# A Unified Framework for Heterogeneous Semi-supervised Learning

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
In this work, we introduce a novel problem setup termed as Heterogeneous Semi-
Supervised Learning (HSSL), which presents unique challenges by bridging the
semi-supervised learning (SSL) task and the unsupervised domain adaptation
(UDA) task, and expanding standard semi-supervised learning to cope with heterogeneous training data. At its core, HSSL aims to learn a prediction model
using a combination of labeled and unlabeled training data drawn separately from
heterogeneous domains that share a common set of semantic categories; this model
is intended to differentiate the semantic categories of test instances sampled from
both the labeled and unlabeled domains. In particular, the labeled and unlabeled
domains have dissimilar label distributions and class feature distributions. This
heterogeneity, coupled with the assorted sources of the test data, introduces significant challenges to standard SSL and UDA methods. Therefore, we propose a
novel method, Unified Framework for Heterogeneous Semi-supervised Learning
(Uni-HSSL), to address HSSL by directly learning a fine-grained classifier from the
heterogeneous data, which adaptively handles the inter-domain heterogeneity while
leveraging both the unlabeled data and the inter-domain semantic class relationships
for cross-domain knowledge transfer and adaptation. We conduct comprehensive
experiments and the experimental results validate the efficacy and superior performance of the proposed Uni-HSSL over state-of-the-art semi-supervised learning
and unsupervised domain adaptation methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a unified framework for Heterogeneous Semi-supervised Learning (Uni-HSSL), where the labeled and unlabeled data come from heterogeneous domains. It designs a weighted moving average pseudo-labeling component, a cross-domain prototype alignment component and an inter-domain mixup component to address the distribution inconsistency issue. The experiments validate the efficacy of the proposed framework.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The paper solves semi-supervised learning under distribution inconsistency, an important ML problem in practice.
3.	Empirical results demonstrate that Uni-HSSL can achieve SOTA results on several benchmark SSL settings.

### Weaknesses
1.	The distribution mismatch between labeled and unlabeled data has been widely explored [1-5]. In this paper, it is crucial for the authors to discuss and compare these existing approaches to provide a comprehensive understanding of this field.
2.	The novelty is limited. This paper proposes three parts to address distribution mismatch issue: weighted moving average pseudo-labeling component, a cross-domain prototype alignment component and an inter-domain mixup component. However, the idea of moving pseudo-labels and mixup has been widely explored in semi-supervised learning [6][7]. And the prototype alignment is also widely used in UDA [8]. So in my opinion, this paper did not introduce new insight to SSL area. 
3.	The paper only considers the DA dataset. I suggest authors could further investigate the effectiveness of their proposed framework in additional settings, such as imbalanced SSL with different imbalance ratios between labeled and unlabeled data on CIFAR10/100-LT benchmark.
4.	Some robust SSL methods are not compared, such as [5][9] in the experimental setting. And the authors only compare two UDA methods. The recent SOTA UDA methods [10] are missed.

### Questions
See weakness for detail.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses a heterogeneous semi-supervised learning problem involving labeled and unlabeled data from different domains. The authors propose a framework called Uni-HSSL, which consists of three technical components: a weighted moving average pseudo-labeling component, a cross-domain prototype alignment component, and a progressive inter-domain mixup component. The proposed approach outperforms several SSL and UDA baselines on various benchmarks.

### Strengths
1. The problem being considered is interesting and important in real-world SSL applications.
2. The author has integrated several SSL technologies into a framework and in the experiments, the proposal has shown better performance compared to some baselines.
3. The overall proposal is well-presented and easy to follow.

### Weaknesses
1. The proposal seems to be a direct combination of existing technologies. The novelty of this proposal seems limited, and I am concerned that it may not bring new insights to the SSL community. The effectiveness of these techniques, such as using weighted moving averaging to reduce noise in pseudo-label updates, contrastive learning to strengthen prototype representation learning, and mixup to mitigate domain gaps, has been widely validated in the SSL/UDA community. It is foreseeable that combining them can improve the performance of SSL in a heterogeneous setting. However, the current version of the paper does not provide further analysis to explain or evaluate their effectiveness/reliability. More in-depth analysis, especially regarding their roles in heterogeneous SSL, can further improve this paper. For example, different technologies could be employed to handle noisy pseudo labels, such as ensemble, confidence-based selection, and entropy-based selection. Why did the current framework choose EMA, and what special capabilities does it have for heterogeneous SSL?
2. I also suggest that the author focus more on the issues in heterogeneous SSL rather than presenting the proposal from a technical perspective. From my understanding, in this article, the author uses three techniques to handle noisy pseudo labels and the misalignment of representation learning when facing cross-domain data. Defining the key problems in heterogeneous SSL may have a more positive impact on the community. For example, what difficulties do existing SSL techniques encounter due to the domain gap? Furthermore, the proposed Uni-HSSL achieves better heterogeneous SSL by addressing these problems separately.
3. In the experiment, the author only compared some previous baseline algorithms, and the SOTA method is missing. As mentioned by the author in the text, the ICML23 work considered the same problem, and it should be included in the comparison process of the experiment.

### Questions
1. The key problems in the heterogeneous SSL problem, and how to deal with these problems in the proposal? [See Weakness part]
2. How does the performance of Uni-HSSL compare to the ICML23 work?

Bidirectional adaptation for robust semi-supervised learning with inconsistent data distributions. ICML'23

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces a novel problem setup termed Heterogeneous Semi-Supervised Learning (HSSL), where the labeled and unlabeled domains have dissimilar label distributions and class feature distributions.

### Strengths
The paper is generally written in a clear way.

### Weaknesses
The authors claim that they propose a novel method termed "Unified Framework for Heterogeneous Semi-supervised Learning (Uni-HSSL)". However, such setting has already been studied in previous works, such as "universal semi-supervised learning" (NeurIPS 21). The authors may not aware of this previous work, as they did not cite or compare this work. Therefore, I think the authors cannot claim that they "introduce a novel problem setup".

### Questions
I do not have specific questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
