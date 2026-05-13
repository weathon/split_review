# On the Role of Discrete Tokenization in Visual Representation Learning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
In the realm of self-supervised learning (SSL), masked image modeling (MIM) has gained popularity alongside contrastive learning methods. MIM involves reconstructing masked regions of input images using their unmasked portions. A notable subset of MIM methodologies employs discrete tokens as the reconstruction target, but the theoretical underpinnings of this choice remain underexplored. In this paper, we explore the role of these discrete tokens, aiming to unravel their benefits and limitations. Building upon the connection between MIM and contrastive learning, we provide a comprehensive theoretical understanding on how discrete tokenization affects the model's generalization capabilities. Furthermore, we propose a novel metric named TCAS, which is specifically designed to assess the effectiveness of discrete tokens within the MIM framework. Inspired by this metric, we contribute an innovative tokenizer design and propose a corresponding MIM method named ClusterMIM. It demonstrates superior performance on a variety of benchmark datasets and ViT backbones.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the role of tokenization in Masked image modeling (MIM). It starts by discussing how discrete tokenization affects generalization performance on downstream tasks. For measuring the proficiency of different tokenization roles, this work designs the token-class alignment similarity (TCAS) metric. Based on the TCAS, they propose a MIM framework (K-MIM) with a cluster-based discrete tokenization scheme. Extensive experiments are conducted to validate the effectiveness of the proposed tokenization strategy.

### Strengths
- The main problem, "What is the role of tokenization in MIM? How does it affect downstream performance?", is interesting and necessary.
- The proposed token-class alignment similarity (TCAS) is a cheap but effective metric to measure the performance of tokenization roles.
- This paper theoretically and empirically demonstrates the superiority of class-wise tokenization.
- The paper is well-organized and easy to follow.

### Weaknesses
 - It would be better to show more ablation results about clustering numbers in Table 4.

### Questions
- Could you please show more ablation results about clustering numbers (e.g., K = 10, 25, 200) in Table 4?

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes the effect of discrete tokens as targets of masked image model (MIM) training. Using a graph-based view for MIM [A], the paper shows that discrete tokens change the graph of MIM. Also, it provides a theorem that discrete tokens similar to image class are the best for MIM targets. Based on the theorem, a metric to measure better tokenizer for MIM is proposed, named Token-Class Alignment Similarity (TCAS). Last, it is shown that simple K-means, which have a better TCAS score than other baselines, could improve the performance of MIM.

[A] How Mask Matters: Towards Theoretical Understandings of Masked Autoencoders, NeurIPS 2022

### Strengths
- Theoretical analysis on a discrete tokenization method looks novel and interesting.
- A metric for tokenization (TCAS) would help a lot of researchers to investigate MIM.

### Weaknesses
 - I think using discrete tokenization is not a mainstream of MIM. Representative methods, such as MAE, MaskFeat, and data2vec, demonstrate impressive performance without the discrete tokens. Thus, the contribution of the paper is hard to cover diverse variants of MIM.

- According to theorem 1, image classification training could be the best way to downstream error bound. But, in practice, MIM works better than classification training in a lot of cases. Thus, I doubt the general applicability of this theorem and the metric (TCAS) on diverse MIM tasks.

- Experimental results are limited to a small dataset (ImageNet-100) and short training (200 epochs on IN-1k). I think it is not enough to validate the effect of K-MIM. Reported numbers on TCAS are also limited.

- Discrete tokenizers like dVAE and VQGAN employ ConvNet or ViT, utilizing the entire image to create tokens. These tokens are interrelated, and a token from one location can incorporate patches from others. However, it looks like the paper handles these tokens as individual local information, which is not correct.

### Questions
- Using DINO as a target representation is similar to [B]. Is there any relation between the distillation target and the TCAS metric? I think the paper would be better to cite [B] and add a discussion on it.

[B] Exploring Target Representations for Masked Autoencoders, arxiv

- According to theorem 1, it looks like an image classifier would be the best tokenizer for MIM. What is the TCAS score and MIM performance when using an image classifier, such as DeiT, as a tokenizer?

- Section 3 is explained with tokenization for a group-of-tokens, i.e. $x_2 \in R^{n \times s}$. But, in Section 4, it seems the tokenization is conducted for a single token. Is it possible to generalize a theorem from the group-of-tokens case to the single-token scenario?

- Discrete tokenizers like dVAE and VQGAN employ ConvNet or ViT, utilizing the entire image to create tokens. These tokens are interrelated, and a token from one location can incorporate patches from others. However, it looks like the paper handles these tokens as individual local information, which is not correct. Is there any explanation for this?

- Although K-MIM has better TCAS than other tokenizers, it is hard to say that K-MIM is specially designed for TCAS. Is there any discrete tokenization method optimized for the TCAS metric?

### Soundness
4 excellent

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
This authors of this paper present theoretical analysis on the problem of masked image modeling (MIM), and study the impact of discrete tokenization in the MIM pipeline.

### Strengths
The authors present an intriguing tokenization approach using graph representation, and the paper is both technically robust and clearly articulated

### Weaknesses
The theoretical analysis is only considered for two classes. I wonder if this can be extended into multiple classes.

I also have a question regarding the downstream error bound. It would be helpful if the authors could provide more detail about the derivation, specifically how the graph connectivity metrics directly translate into the error bound. The current explanation lacks sufficient detail to fully understand the relationship.

### Questions
Other the generalization to multi-classes. I have another question regarding the downstream error bound, it would be helpful if you can talk more in detail about the derivation perhaps in the appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Masked image modeling methods (MIM) have started to employ discrete tokenization as a reconstruction target instead of raw pixel values. Yet, the role of tokenization and how it affects downstream performance is not well studied. This paper studies the impact of tokenizer design on downstream performance. The paper finds that that tokenizer that are more aligned with the downstream task labels (ie, more discriminative with respect to downstream classes) result in better performance, and design a metric to measure this similarity. The paper also introduces a new tokenizer based on clustering features to provide discretized reconstruction targets. Methods trained with the new tokenization achieve a better performance that existing approaches. The paper also includes some interesting analysis for the new tokenizer.

**Update (11/20):** I have raised my rating from 6 to 8 in respond to reading the other reviews and the author's response to all reviews. I think the paper presents an interesting study of the impact of discretization and proposes an interesting approach to representation learning.

### Strengths
- The framing of the equivalency structure induced by the tokenization was quite interesting. 

- The paper poses an interesting question regarding the impact of tokenization and provides several interesting observations and analysis to answer it. 

- The proposed metric is intersting and seems to have predictive power. Although, as noted in the weaknesses, it would be great to report it for all experiments. 

- The proposed tokenizer is fairly simple, especially for K-MIM pixel which achieves a significant performance gain without requiring any other models.

### Weaknesses
 - I found the name "Mixture Tokenizer" a bit confusing since it almost seems adversarial in nature, and wasn't sure if this naming is common in another sub-field. It seems to me that this would be an adversarial/worst-case tokenizer; one that implicitly learns a class structure that is "orthogonal" to the desired one (eg, one that learns backgrounds instead of foreground objects in a perfectly balanced datasets). If so, I would suggest naming it something that denotes this quality better simply a "mixture tokenizier." 

- The use of a pre-trained SSL models to create the tokenization seems a bit odd. I would argue that if you use the features of model X to generate the labels/tokens to train model Y, then model Y is effectively being supervised by model X. While this is okay since both models have similar training requirements, one would expect model Y to outperform model X for this strategy to be pragmatic. Yet, K-MIM DINO achieves a much lower linear probe accuracy than DINO. Furthermore, the efficiency argument made in Sec 5.2 would need to take into account the time taken to train DINO for the K-MIM DINO results (the argument for K-MIM PIXEL holds and is a very nice finding). 

- The introduction goes directly into specific methods that might not be known to the readers. Providing some smoother transition (eg, explaining what those methosd are doing first) could improve the readability of the introduction.

- The TCAS metric is only shown in Table 2, I think it would be nice to include it as a column in Tables 3 and 4 to see how well it explains variation in performance. Particularly, I am curious how much it changes with the choice of K in table 4, and whether that would explain some of the patterns there.

### Questions
- Could you explain why the bounds in equation 7 do not depend on $l$? Is it because each point is equivalent to an equal number of each class? 

- He et al (CVPR 2022) reported a fine-tuning performance of 83.6, yet Table 3 reports 82.9. Could you please comment on this discrepancy? 

- Table 3 notes that K-MIM DINO achieves a linear probe accuracy of 67.4, which is significantly lower than 78.2 reported by Caron et al (ICCV 2021), while outperforming them on fine-tuning (83.8 vs. 82.8). I was curious why you think the model underperforms this much despite being given being trained using the equivalency structure learned by DINO. 

- The results reported in Table 4 are quite interesting as they indicate that performance deteriorates quickly for larger token books, while a larger number of tokens seems to benefit DINO. Could you please comment on this result? I would be curious if TCAS could shed some light on this. 

- I think the finding that discretized features (HOG/DINO) provide better targets than raw pixels. DINO is an interesting target as it has been shown to be good local descriptor. I am curious if other features would be useful as well; eg, imagenet-supervised VIT features or MAE features. The first should be more aligned with the downstream task structure, while the latter is based on a model that seems to perform worse. I am curious if you had tried this or what your thoughts are on other features as targets for clustering.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
