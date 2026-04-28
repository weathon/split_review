# Harnessing Shallow Features in Pre-Trained Models for Out-of-Distribution Detection

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Recognizing out-of-distribution (OOD) samples is essential for deploying robust machine learning systems in the open-world environments. Conventional OOD detection approaches rely on feature representations from the final layer of neuron networks, often neglecting the rich information encapsulated in shallow layers. Leveraging the strengths of transformer-based architectures, we introduce an attention-based fusion module, which dynamically assigns importance weights to representations learned by each Transformer layer and detects OOD samples using the Mahalanobis distance. Compared to existing approaches, our method enables a lightweight fine-tuning of pre-trained models, and retains all feature representations that are beneficial to the OOD detection. We also thoroughly study various parameter-efficient fine-tuning strategies. Our experiments show the benefit of using shallow features, and demonstrate the influence of different Transformer layers. We fine-tune pre-trained models in both class-balanced and long-tailed in-distribution classification tasks, and show that our method achieves state-of-the-art OOD detection performance averaged across nine OOD datasets. The source code is provided in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a weighted feature fusion method from the top to bottom layers of a network for OOD detection. It argues that, instead of relying solely on the features of the penultimate layer in a deep network for OOD detection, incorporating features from shallow layers provides diversity in feature spaces, aiding in the separation of OOD examples from ID examples. The method uses the total variance of features across different neural network layers to estimate feature weights for OOD detection. Experiments are conducted on CIFAR-100 and Imagenet, two popular benchmarks for OOD detection, including a setup with a long-tail distribution in in-domain training examples. The experimental results show that the proposed method outperforms the compared method.

### Strengths
The paper is well-written and easy to follow.

Extensive experiments are presented to support the claims.

There are sufficient ablation studies.

### Weaknesses
I find the novelty of the method modest. There is a remark section in the paper highlighting that the idea of estimating layerwise importance is the contribution compared to the inspiring methods, Mahalanobis and TRUSTED. While I can see a performance comparison with Mahalanobis in the paper, I could not find one for TRUSTED. Moreover, based on Figures 4 and 5 from the ablation studies, it hardly supports any contribution of layerwise feature weighting in OOD detection. The last layer has significant weight, while the other layers have more or less similar weights. A baseline with uniform weighting across all feature layers is also important.

Although not directly related, a paper on the variance of gradients for estimating the difficulty of images for OOD detection [ref1] is relevant and would support the argument.

### Questions
I am not fully convinced that there is a significant role of layerwise weightage in OOD detection. Giving more weights for the penultimate layer and the same weight to other layers can still perform well.    A clarification with experiments may change my rating.

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
This paper works on out-of-distribution detection (OOD) questions and proposes to use the rich information contained in the shallow features to improve the detection of the OOD samples.  Experiments on both class-balanced and long-tailed datasets show the effectiveness of using such shallow features and the proposed method.

### Strengths
1. The writing is good and the idea is easy to follow.
2. The observation of existing methods neglecting the shallow features makes sense to me and Fig.1 well illustrates the comparison of using the fused features from all layers than only using the last layer. 
3. The achieved results are promising showing the proposed method outperforms other competitors.

### Weaknesses
1.  The contribution of using all features for OOD looks over-claimed given the fact that there are already two related works (Mahalanobis and TRUSTED) explored that for OOD.  Emphasis on the novel multiple-feature fuse method might be more suitable.  
2. The novelty part is not that new to me. Though the adaptive fuse for multiple features is not explored for OOD, what I understand of the key idea is to improve the discriminates of different image features, from this perspective,  the idea of using multilayer features simply or adaptively is quite explored as in [ref1-4] for example. 
3.  The proposed fusion method is not comprehensively studied. For example, what about the comparison results with some simple fuse method e.g., average or fixed ratios, and other proposed fusion methods e.g. [ref1-4]?
4. Open questions about the task motivation:  is it definitely better to detect all out-of-distribution data for the model training, or will the OOD data help with the model's generalization ability for the cross-domain testing which we can't ensure is always in the same domain with the training.  
5. Minor: the bold font is recommended to apply for tables to make it easier to read the results. 

### Questions
please see weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
With the favor of transformer architecture,  this work proposes an out-of-distribution (OOD) score based on the fused feature entailed from each layer. Further, it is empirically observed that parameter-efficient fine-tuning (PEFT) is more robust than fully fine-tuning when using different learning rates. Finally, it demonstrates the effectiveness of the proposed OOD score along with PEFT on the OOD benchmark and also long-tailed OOD benchmark.

### Strengths
- The proposed OOD score based on the fused feature from each layer is novel. 
- This work aims to tackle the OOD detection on both class-balanced benchmark and long-tailed benchmark.

### Weaknesses
 -  The title appears somewhat overstated, as the proposed method specifically requires transformer architectures. A more precise title, such as "... in pre-trained transformers for ...", would better reflect the scope of the method.
- Line 103-104: The mention of "measuring the degree of neural collapse of each layer" is unclear. Could the authors elaborate on this point and clarify how it relates to determining the importance weights for each layer.
- The proposed OOD score aligns with post-hoc OOD scores that require access to training data. To assess its effectiveness, the authors should consider evaluating it on a standard OOD benchmark, as outlined in [2].  Comparisons with other training-data-dependent OOD scores—such as KL matching, Residual, and ViM—would provide a more comprehensive evaluation (see Table 1 in [1] for reference).
- It is unclear why the authors chose to fine-tune a network pre-trained on ImageNet-21k. Why not instead use models pre-trained directly on ImageNet-1k or CIFAR-100 and then perform OOD detection on a standard benchmark[2]?
- Dependency on Fine-tuning: Could the authors discuss whether the proposed OOD score's effectiveness relies on the pre-trained models with extensive datasets? For instance, the selected models in this work is pre-trained ViT models on ImageNet-21k and  CLIP-ViT-B/16. Have you tested or considered testing with smaller pre-trained models or datasets to assess its effectiveness across different scales of pre-training.
- Comparison with MCM (Line 394): The comparison with MCM, in which the authors claim that SFM outperforms MCM by ~2%, may not be fair. The original MCM model was not fine-tuned on ImageNet-1k, which could impact the validity of this comparison.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2
