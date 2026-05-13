# Cross-domain Few-shot Classification via Invariant-content Feature Reconstruction

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
In \emph{cross-domain few-shot classification} (CFC), mainstream studies aim to fast train a new module to select or transform features~(a.k.a., the high-level semantic features) for previously unseen domains with a few labeled training data available on top of a powerful pre-trained model. These studies usually \emph{assume} that high-level semantic features are shared across these domains, and only simple feature selection or transformations are enough to adapt features to those unseen domains. However, in this paper, we find that the simply transformed features are too general to fully cover the key content features regarding each class. Thus, we propose \emph{invariant-content feature reconstruction} (IFR) to train a simple module that simultaneously consider high-level and fine-grained invariant-content features for the previously unseen domains. Specifically, the fine-grained invariant-content features are considered as a set of \emph{informative} and \emph{discriminative} features learned from a few labeled training data of tasks sampled from unseen domains, and are extracted by retrieving features that are invariant to style modifications from a set of content-preserving augmented data in pixel level with an attention module. Extensive experiments on the Meta-Dataset benchmark show that IFR achieves good generalization performance on unseen domains, which demonstrates the effectiveness of the fusion of the high-level features and the fine-grained invariant-content features. Specifically, IFR improves the average accuracy on unseen domains by 1.6\% and 6.5\% respectively under two different CFC experimental settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of cross-domain few-shot classification (CFC), where the objective is to perform classification tasks in previously unseen domains with limited labeled data. The authors propose a novel approach named Invariant-Content Feature Reconstruction (IFR), which aims to simultaneously consider high-level semantic features and fine-grained invariant-content features for unseen domains. The invariant-content features are extracted by retrieving features that are invariant to style modifications from a set of content-preserving augmented data at the pixel level using an attention module. The paper includes extensive experiments on the Meta-Dataset benchmark, demonstrating that IFR achieves superior generalization performance on unseen domains and improves average accuracy significantly under two different CFC experimental settings.

### Strengths
- Novel Approach: The paper introduces a unique method, IFR, which addresses the limitations of existing approaches by considering both high-level semantic features and fine-grained invariant-content features. This dual consideration is innovative and addresses a critical gap in cross-domain few-shot classification.

- Extensive Experiments: The authors have conducted comprehensive experiments on the Meta-Dataset benchmark, providing a robust evaluation of their proposed method. This adds credibility to their claims and demonstrates the practical applicability of their approach.

- Clear Problem Statement: The paper clearly articulates the challenges in cross-domain few-shot classification and provides a compelling argument for why existing methods are insufficient, setting a strong foundation for their proposed solution.

### Weaknesses
 - Limited Explanation of Methodology: While the paper provides a high-level overview of the IFR approach, it could benefit from a more detailed explanation of the methodology, including the attention module and how it specifically contributes to invariant-content feature extraction.

- Lack of Comparative Analysis: The paper presents experimental results demonstrating the effectiveness of IFR, but it lacks a thorough comparative analysis with existing methods, discussing in detail why IFR outperforms them. In addition, since this proposed work resembles [1][2], why not compare with these two methods in the Experiments Section?

- Potential for Overfitting: Given that the approach focuses on fine-grained features, there might be a risk of overfitting, especially when dealing with extremely limited data in few-shot scenarios. The paper does not address this potential issue or provide strategies to mitigate it.

### Questions
1. Can you provide a more detailed explanation of the attention module used in IFR and how it specifically contributes to the extraction of invariant-content features?

2. How does IFR compare to existing methods in terms of computational efficiency and scalability, especially when applied to large-scale datasets?

3. Given the focus on fine-grained features, how does IFR mitigate the risk of overfitting in few-shot scenarios? Are there any specific strategies or mechanisms in place to prevent this?

4. How well does IFR generalize to domains that are significantly different from those in the Meta-Dataset benchmark? Have there been any experiments conducted in this regard?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an invariant-content feature reconstruction (IFR) method, which combines high-level semantic features with fine-grained invariant-content features for cross-domain few-shot classification.
The high-level semantic features are extracted from the original images by the backbone, and the invariant-content features are reconstructed from the augmented images by the transformer attention head.
In a word, IFR performs cross-attention between the original images and their augmented images. 
The experimental results on the Meta-Dataset benchmark show the effectiveness of IFR in improving generalization performance on unseen domains.

### Strengths
1. The motivation and presentation are clear. 
2. The experimental results are good: The experimental results on the Meta-Dataset benchmark show the effectiveness of IFR in improving generalization performance on unseen domains.

### Weaknesses
1. The novelty of the proposed methodology is limited. The proposed IFR method only performs cross-attention between the original images and their augmented images. The transformer-based cross-attention has been widely used.


### Questions
1. The proposed IFR method only performs cross-attention between the original images and their augmented images. What is the limitation of cross-attention in obtaining the fine-grained-content features? Can authors make an improvement to the cross-attention structure?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper intends to combine high-level features and fine-grained invariant-content features to improve the performance of cross-domain few-shot classification. Specifically, the author proposes to extract invariant-content features via a single attention head and fuse the extracted invariant-content features and high-level features via the scaled dot-product attention mechanism of the Transformer. The proposed methodology recovers the key content features of the target class, which did not work well in existing meta-dataset works. Through extensive experiments, it is shown that the proposed method outperforms the baseline under various conditions.

### Strengths
1) This paper proposed a simple yet effective feature reconstruction method that significantly improves the performance.
2) This paper presents a theoretical analysis of the proposed attention modules.

### Weaknesses
1) The single attention head and scaled dot production attention mechanism proposed in this paper are not novel concepts and are so simple that the technical contribution is insufficient to acknowledge the quality.
2) The presented Theorem is just borrowed from the existing works. 
3) It is not easy to know exactly what “high-level features” and “invariant-content features” denote. It is not clearly explained in the manuscript, and from the caption in Figure 2, one can only guess that the output features of the backbone are high-level features, and the output features of the attention head are invariant-content features. 
3) Comparison with SoTA methods is insufficient. The baseline (URL, published in 2020) of the toy example in Figure 1 is outdated, and the experiment also needs to be compared with TSA[1] and TriM[2], which are currently recording higher performance than URL on the leaderboard.
4) Motivation is poor. The motivation of this paper is that prior works cannot capture representative key features, and the only evidence to support this is a comparison of the figure's activation map. This comparison alone is not sufficient to point out the shortcomings of prior works, and since it is a qualitative comparison, it is not accurate. As a result, the significant performance gains in Tables 1 and 2 are not credible, and even if it is true, the performance improvement cannot be sufficiently explained in the paper, so the contribution is greatly limited.
5) Citations are inconsistent. Some citations are contained within the parenthesis, while others are not.
There are redundant contents that are not very important. For example, Figure (4) is simple enough that it does not need to be shown as a figure, and there is no need to provide Theorem 2 since it is not proposed in this paper.

### Questions
1) In the second paragraph on page 2, it is said that the proposed method considers both informativeness and discriminativeness at the same time. However, it is not easy to tell the difference between the two concepts through the current introduction. How exactly are they different, and how does the proposed method use these two concepts at the same time?
2) It is questionable whether the feature reconstruction mentioned in this paper is really reconstruction. To me, it just looks like performing a scaled dot product, and considering that the α value in Equation (2) is about 1e-4, I'm not sure if it has much significance.
3) Page 7 says that query heads have Lipschitz continuous property and the author’s comment follows as: “we can reliably leverage IFR to find good representations…”. But isn't this explanation too insincere and uninformative? Although it is known that Lipschitz continuity improves robustness against perturbation, but more detailed analysis is needed to be provided.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
