# Towards Understanding Why FixMatch Generalizes Better Than Supervised Learning

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Semi-supervised learning (SSL), exemplified by FixMatch \citep{sohn2020fixmatch}, has shown significant generalization advantages over supervised learning (SL), particularly in the context of deep neural networks (DNNs). However, it is still unclear, from a theoretical standpoint, why FixMatch-like SSL algorithms generalize  better than SL on DNNs. In this work, we present the first theoretical justification for the enhanced test accuracy observed in  FixMatch-like SSL applied to DNNs by taking  convolutional neural networks (CNNs) on classification tasks as an example. Our theoretical analysis reveals that the semantic feature learning processes in FixMatch and SL are rather different. In particular, FixMatch learns all the discriminative features of each semantic class, while SL only randomly captures a subset of features due to the well-known lottery ticket hypothesis. Furthermore, we show that our analysis framework can be applied to other FixMatch-like SSL methods, e.g., FlexMatch, FreeMatch, Dash, and SoftMatch. Inspired by our theoretical analysis, we develop an improved variant of FixMatch, termed Semantic-Aware FixMatch (SA-FixMatch). Experimental results corroborate our theoretical findings and the enhanced generalization capability of SA-FixMatch.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the feature learning process of neural networks trained with the FixMatch method, which is a semi-supervised learning method, demonstrating its theoretical advantages on data distributions with a “multi-view” structure. The authors characterize the FixMatch learning process as a two-stage process: initially, the model learns like supervised learning and learns most of the features, followed by a second stage where it learns the missing features through unsupervised learning from augmented data. Based on these theoretical insights, the authors introduce a semantic-aware augmentation in FixMatch to enhance its performance.

### Strengths
1. This paper provides a new theoretical analysis of the FixMatch method, particularly on multi-view structured data distributions, demonstrating its effectiveness in learning features and its advantages over supervised learning. The characterization of FixMatch's two-stage learning process is insightful, offering a clearer understanding of how the model learns from both supervised and unsupervised data.

2. The authors propose a new semantic-aware augmentation technique that aligns with their theoretical findings, which improved the performance of FixMatch.

### Weaknesses
1. The assumptions regarding data augmentation appear artificial. The augmentation method knows which feature is in each patch and can distinguish between feature and noise patches. The augmentation randomly mask the noise patch and one of the feature, to enable the FixMatch to focus on the unlearned features. Even though such augmentation can be easily achieved in the theoretical setting, it is smarter than what is originally used in FixMatch. Specifically, the assumption that augmentation can selectively remove either noise or one of the two feature views, while retaining the other, is unrealistic. In practice, augmentations like random cropping or masking would affect all patches indiscriminately, making the theoretical analysis less applicable to real-world scenarios. The assumption of perfect separation between feature and noise patches is also a strong simplification that doesn't reflect the complexity of natural images.
2. The proposed SA-FixMatch, although is interesting and shares closer connection to the theory, introduces added complexity by using Grad-CAM for augmentation, which can slow down training. The use of Grad-CAM, while providing semantic awareness, adds a significant computational overhead, especially during training. This overhead might limit the scalability of the method to larger datasets or more complex models. Furthermore, the reliance on Grad-CAM introduces another hyperparameter to tune, which could make the method harder to use in practice.

### Questions
1. Why can’t the augmentation be agnostic about what the patch contains, what is the theoretical bottleneck here? What impact would a uniformly random mask have? Could there be a more realistic setting where distribution-agnostic data augmentation could still achieve similar results?
2. While the theory here follows very closely to that of AllenZhu and Li [2023], it seem to have missed some previous works exploring the effects of augmentation on feature learning process [1,2]. The authors can refer to the designs of augmentations and their corresponding analysis in these papers.

[1] Toward Understanding the Feature Learning Process of Self-supervised Contrastive Learning. Zixin Wen, Yuanzhi Li [ICML 2021]

[2] The Mechanism of Prediction Head in Non-contrastive Self-supervised Learning. Zixin Wen, Yuanzhi Li [NeurIPS 2022]

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes two contributions:
1. A theoretical analysis to explain why semi-supervised learning (SSL) techniques such as FixMatch generalize better than classical supervising learning (SL).
2. A new method FixMatch-SA (semantically aware) which builds on the analysis to further enhance FixMatch.
The improved performance of FixMatch serves to experimentally corroborate the theoretical analysis.

I understood the substantiating argument of the theoretical analysis as follows: the correct classification of sample is typically based on multiple features (at least 2). In SL, learning of all features is not necessary to minimize the loss. Meanwhile, in FixMatch, the strong augmentation drops some features and therefore requires the network to learn all the features to minimize the loss. 

Disclaimer: the theoretical analysis felt above my skill, mathematically speaking. I tried to follow it to the best of my ability but there could be alternate conjectures which I am not aware of to explain the observed generalization gains.

### Strengths
1. The paper is well-written and gave me the impression that I was able to follow its goal.
2. The results from FixMatch-SA seem to confirm the pertinence of the analysis, and intuitively I found it made logical sense.
   - Some gains from CutOut-SA are truly impressive, including for recent FixMatch derivatives.
3. I particularly liked that the paper didn't limit itself to a theoretical analysis but also provided an experimental validation on common SSL benchmarks.
4. I find the FixMatch-SA method very elegant and effective and appears simple to implement which I consider a quality.

### Weaknesses
1. My own lack of knowledge on the theoretical side made it hard for me to estimate the originality of the approach. Specifically, while the core idea of leveraging strong augmentations to enforce the learning of all relevant features is intuitive, I am not sure whether prior work has explored similar concepts, perhaps in a different guise. It's not per-se a weakness of the paper but rather a warning that I simply don't know.

Typos (obviously this didn't influence my rating, it's for authors to polish their manuscript)
- Line 87, wrong citation "FixMatch (Xie)" => "FixMatch (Sohn)"

### Questions
1. Do you feel there is more potential to be extracted from the CutOut-SA line of thinking? For example, could doing multiple cutouts on the image to enforce exactly one classifying feature being present in the strong augmentation be a future avenue of improvement? Or did you already try multiple variants of such schemes and found the one you eventually presented in the paper to be the best?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
- This paper provides a theoretical analysis, aimed at answering why FixMatch-like algorithms (for Semi-Supervised Learning, or, SSL) generalizes better than supervised learning. 
- The analysis is focused on CNNs (unlike previous comparison works that provide analysis by using linear model assumptions)
- The paper proposes a improvement to FixMatch, called Semantic-Aware FixMatch (SA-FixMatch). The SA-FixMatch essentially masks out the semantically relevant parts of a high-confidence image sample (the region that is identified by GradCAM) in a CutOut-like fashion.

### Strengths
- The presentation of this work is impressive. The paper is not only easy to read, but the authors do a good job of highlighting their contributions and how it differs from previous works. The writing is clear and concise, and the figures and tables (although there are not that many) are not needlessly overcomplicated.
- The proposed SA-FixMatch seems like a intuitive improvement to FixMatch, and does show to improve on the performance of FixMatch.
- The theoretical justification in Section 4 seem to be sound.

### Weaknesses
 - My main concern of this paper is the overall motivation. My main question for the authors is: Why do we need to have a good theoretical understanding of why FixMatch generalizes better than Supervised Learning? The following is my thought process: Let's say we have a dataset that is fully labeled. In this case, we would obviously use supervised learning (since we have all labels) to train the model. But now, let's consider the case where only 10% of the data is labeled. Obviously, given that SSL can leverage 90% of the dataset while SL can only leverage 10% (9x the size), we would apply SSL to train the model. We already know that leveraging more data will lead to better performance - so then what is the point of trying to theoretically understand why FixMatch generalizes better then SL, given that SL in this case is using a subset of the data that FixMatch is using? The worst case for SSL is that it performs equally as SL. As shown in the paper, FixMatch learns more semantic features, but that seems a bit obvious, since FixMatch is able to utilize the unlabeled samples, while SL receives no training from these unlabeled samples. Perhaps a fairer (and more interesting) setting would be to compare SSL vs Supervised learning, given the same number of total training samples (where the 'unlabeled' samples of the SSL dataset is labeled for SL). I hope I am not coming across as too offensive with this comment, but I am just trying to understand the significance of such analysis. I hope the authors can convince me otherwise. 

- The implications of the analysis is somewhat underwhelming. 
  - The proposed SA-Cutout does not feel like a novel contribution, given that there are previous works that use guided data augmentation for other tasks (e.g., "Crafting Better Contrastive Views for Siamese Representation Learning" in CVPR 2022). Also, there are some gradient-based masking techniques, such as "Adversarial Dropout for Supervised and Semi-supervised Learning" in AAAI 2018 that have very similar motivations as SA-Cutout, and the resulting solution is quite similar as well (masking out highly semantic regions).
  - Are there any other takeaways from this analysis? For example, could this type of analysis be extended to a broader scope?

### Questions
Questions were asked in the section above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the theoretical aspects of why the SSL method FixMatch outperforms supervised learning method in generalization for deep neural networks (DNNs). Previous studies have shown that SSL methods like FixMatch achieve higher test accuracy, but the mechanisms behind this advantage are not obvious. The authors provide theoretical justification for the enhanced generalization of FixMatch for convolutional neural networks. Their analysis reveals that FixMatch captures all relevant discriminative features for each class, whereas SL approaches tend to capture only a random subset of features, an effect attributed to the lottery ticket hypothesis. This framework is shown to extend to other SSL methods similar to FixMatch, such as FlexMatch, FreeMatch, Dash, and SoftMatch. Based on these findings, the authors propose an enhanced version of FixMatch, called Semantic-Aware FixMatch (SA-FixMatch), which is validated experimentally, demonstrating improved generalization.

### Strengths
The theory presented is compelling. The authors provide a strong argument, without relying on overly strict assumptions, that training a realistic neural network (a 3-layer ConvNet) with FixMatch-type algorithms allows us to (1) fit the training data and (2) generalize well to unseen samples. This stands in contrast to supervised learning, where the model often fails to generalize well to certain types of samples within the distribution.

Additionally, the authors propose an improved variation of a FixMatch algorithm, demonstrating that their theory not only explains the success of this family of algorithms but also predicts new results.

### Weaknesses
The main weakness of this paper lies in its technical presentation, particularly regarding notation consistency, variable usage, and the clarity of complex definitions.

While I appreciate that the theoretical framework developed here is complex, making it challenging to present in an accessible way, I believe certain aspects could have been significantly improved for clarity. Specific areas that require attention include:

1. **Non-standard notations:** The authors use symbols like $Z_l$ to denote a labeled dataset, whereas $\mathcal{S}$ is typically used for sample sets in machine learning literature. This deviation from standard notation can hinder readers' ability to quickly grasp the concepts, especially those familiar with common practices in the field.
2. **Ambiguous variable usage:** In lines 126-128, the symbol $i$ is used to index both patches and classes. This overloaded usage creates ambiguity and makes it difficult to follow the mathematical derivations. For example, in the expression $F_i^{(t)}(X) = \sum_{l \in [2]} \left( \Phi_{i,l}^{(t)} \times Z_{i,l}^{(t)}(X) \right) \pm O\left(\frac{1}{\text{polylog}(k)}\right)$, it is unclear whether $i$ refers to a patch or a class, necessitating careful scrutiny of the surrounding context.
3. **Opaque definitions:** Definition 1, which introduces the multi-view data assumption, is particularly dense and challenging to parse. It would benefit from a more gradual introduction, with each component explained in detail. For instance, the distinction between single-view samples ($D_s$) and multi-view samples ($D_m$) could be illustrated with concrete examples. Providing an example of a distribution that satisfies these conditions would further clarify the implications of the assumptions and help readers appreciate the significance of the conclusions stated in lines 284-287, regarding the ability of FixMatch to learn all relevant features.

Minor comment:
In the theorems (e.g., Theorem 4), instead of writing "for any \((x,y) \sim D\) with probability ..., we have ...," I would suggest phrasing it as "with probability ... over the selection of \((x,y) \sim D\), we have ...". It is just more mathematically accurate and is consistent with the appendix.

### Questions
1. The theory relies on 3-layer ConvNets. However, the experiments obviously hold for a wider range of architectures. Is it possible to extend it to more sophisticated architectures. For example, ConvNets with residual connections, additional layers, ViTs? If so, would it change the results somehow? Can we derive conclusions that certain architectures generalize better with SL compared to other architectures? That could be really exciting!

2. Can you explain in theorem 4 why the margin scales as log(k) (where k is the number of classes). How come we get better classification margin for a more complex task with more classes? 

3. In theorem 4 you use $T=poly(k)/\eta$ to represent the amount of iterations until convergence. What should I expect the degree of the polynomial and its leading coefficient to be? I want to have some concept of how many iterations we need.

### Soundness
3

### Presentation
3

### Contribution
4
