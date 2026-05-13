# Towards Robust Multimodal Open-set Test-time Adaptation via Adaptive Entropy-aware Optimization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Test-time adaptation (TTA) has demonstrated significant potential in addressing distribution shifts between training and testing data. Open-set test-time adaptation (OSTTA) aims to adapt a source pre-trained model online to an unlabeled target domain that contains unknown classes. This task becomes more challenging when multiple modalities are involved. Existing methods have primarily focused on unimodal OSTTA, often filtering out low-confidence samples without addressing the complexities of multimodal data. In this work, we present Adaptive Entropy-aware Optimization (AEO), a novel framework specifically designed to tackle Multimodal Open-set Test-time Adaptation (MM-OSTTA) for the first time. Our analysis shows that the entropy difference between known and unknown samples in the target domain strongly correlates with MM-OSTTA performance. To leverage this, we propose two key components: Unknown-aware Adaptive Entropy Optimization (UAE) and Adaptive Modality Prediction Discrepancy Optimization (AMP). These components enhance the model’s ability to distinguish unknown class samples during online adaptation by amplifying the entropy difference between known and unknown samples. To thoroughly evaluate our proposed methods in the MM-OSTTA setting, we establish a new benchmark derived from existing datasets. This benchmark includes two downstream tasks – action recognition and 3D semantic segmentation – and incorporates five modalities: video, audio, and optical flow for action recognition, as well as LiDAR and camera for 3D semantic segmentation. Extensive experiments across various domain shift situations demonstrate the efficacy and versatility of the AEO framework. Additionally, we highlight the strong performance of AEO in long-term and continual MM-OSTTA settings, both of which are challenging and highly relevant to real-world applications. This underscores AEO’s robustness and adaptability in dynamic environments. Our source code and benchmarks will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the multi-modal open-set TTA setting, a challenging and less-explored area within TTA research. It aims to adapt a source pre-trained multi-modal model to an unseen target domain containing samples from unknown classes. They propose an Adaptive Entropy-aware Optimization (AEO) framework, which encourages the adapted model to amplify entropy difference between known and unknown samples. Specifially, UAE dynamically determines whether to minimize or maximize the entropy of each sample through a sample-wise weighting scheme, while AMP considers modalities to encourage diverse predictions for unknown samples and consistent predictions for known samples. The AEO framework shows its effectiveness on the proposed MM-OSTTA benchmark across various modalities.

### Strengths
- The paper addresses the MM-OSTTA setting for the first time, which is a challenging but practical scenario in real-world applications.
- The paper is well written, making it easy to follow the introduced setting and proposed algorithms.
- The paper provides extensive experiments across two tasks and five modalities, showing the effectiveness and versatility of the proposed method.

### Weaknesses
- The observation in Sec. 3.1 is less impressive in the open-set settings. Previous works [1-2] on the open-set settings have already discovered and leveraged the entropy difference between known and unknown samples. 

- In lines 171-174, the authors argue that some selective entropy minimization methods struggle to increase the entropy difference. But, the evidence supporting this claim is insufficient; Figure 2 compares only simple baselines (source, tent), missing another promising baseline such as EATA [3].

- EATA [3] also takes a sample-wise adaptive weighting scheme based on entropy values and achieves competitive performance. Such methods (e.g, EATA, SAR) seem to be able to increase the entropy difference between known and unknown samples, at least more effectively than TENT. What advantages does the proposed method offer over such selective entropy minimization methods?

- In Sec. 3.3, it is straightforward to enforce consistent predictions across modalities for known samples. However, for unknown samples, what is the benefit of maximizing prediction discrepancy across modalities? The equation (6) seems to penalize (i.g., maximize the prediction discrepancy) samples with consistently high entropy (likely unknown) across modalities, although they are easily classified as unknown. A more in-depth explanation of the adaptive modality prediction discrepancy loss in equation (6) would be valuable.

- One of the key purposes of TTA is to adapt the pre-trained model to make better predictions on unseen test data. Although the proposed AEO significantly improves unknown class detection (AUROC, FPR95), its accuracy gains are limited compared to the baselines. Also, the proposed framework primarily focuses on unknown class detection, showing limited capability in model adaptation itself.


[1] Safaei et al., Entropic open-set active learning. AAAI'24. \
[2] Gao et al., Unified Entropy Optimization for Open-Set Test-Time Adaptation. CVPR'24. \
[3] Niu et al., Efficient test-time model adaptation without forgetting. ICML'22.

### Questions
- Please refer to the weaknesses part.
- In equation (3), (5) and (6), how is the entropy used for the adaptive weight W_ada calculated? Is it based on predictions from each individual modality or from the aggregated output? 
- For the corruption robustness experiments, there are six types of corruption for both videos and audios, resulting in 36 possible combinations (6*6) of corrupted test sets. Why are only six distinct corruption shifts used in the experiments?
- In Table 7, what happens if the diversity loss in equation (8) is excluded?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present Adaptive Entropy-aware Optimization (AEO) to tackle Multimodal Open-set Test-time Adaptation (MM-OSTTA), which consists of Unknown-aware Adaptive Entropy Optimization (UAE) and Adaptive Modality Prediction Discrepancy Optimization (AMP). To thoroughly evaluate the proposed methods in the MMOSTTA setting, the authors establish a new benchmark derived from existing datasets.

### Strengths
1.The proposed method is easy to understand and the source code and benchmarks will be made publicly available.

2.A new benchmark that incorporates five modalities: video, audio, and optical flow for action recognition, as well as LiDAR and camera for 3D semantic segmentation is proposed.

3.The analysis on the entropy difference between known and unknown samples is reasonable.

### Weaknesses
1.It seems that the proposed Unknown-aware Adaptive Entropy Optimization has already been used in some of the existing works of wild TTA.

2.In the experimental settings, the authors say that all experiments are conducted under the most severe corruption level 5. However, it may be unrealistic in real-world applications. What about the performance under more lower corruption level?

3.More recent methods should be included for comparisons in Table 1 and 2, i.e., [1-2]

4.It seems that the performance of the proposed method on Acc is generally inferior to previous methods in Table 1 and 2.


[1]Two-Level Test-Time Adaptation in Multimodal Learning

[2]COME: Test-time adaption by Conservatively Minimizing Entropy

There is one minor issue that will not affect the rating:

1.It would be better for demonstration if the second row in Table 1 fills the entire page

### Questions
What is the underlying reason for the performance gap between the proposed method and previous ones on Acc metric?

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
The paper presents a new problem setting for multimodal open-set test-time adaptation (MM-OSTTA), where the multimodal test data stream contains both known and unknown classes. The paper presents adaptive entropy-aware optimization (AEO) to tackle the MM-OSTTA problem. Intensive evaluations on various multimodal open-set scenarios demonstrate the effectiveness of AEO.

### Strengths
- Introduces a new problem setting of multimodal open-set TTA.
- The proposed method (AEO) performs robustly among various datasets and scenarios by successfully discriminating between known and unknown samples.

### Weaknesses
- The paper needs better motivation/discussion of the new setting (MM-OSTTA) regarding how/why existing open-set TTA approaches fail in multimodal settings. 

- The method seems incremental, combining multiple loss terms of (1) entropy discrimination (similar to OOD detection works [a]), (2) entropy minimization (similar to TTA works), (3) discrepancy minimization across modalities, and (4) negative entropy loss (as cited in the paper).

- The design of AMP with three objectives requires further justification (e.g., deeper ablation study of AMP for each loss function) and an explanation of how they connect to contribute.


- The proposed method performs better with more unknown samples (Table 10), which is counter-intuitive and lacks proper explanation.




----

Citations
> [a] Liu, W., Wang, X., Owens, J. D., & Li, Y. (2020). Energy-based Out-of-distribution Detection. Advances in Neural Information Processing Systems, 2020-December. https://arxiv.org/abs/2010.03759v4

### Questions
- Please discuss how diverse open-set data (e.g., SoTTA [b]) would affect the methods and results.
- How is the method sensitive to loss hyperparameters $\gamma_1, \gamma_2$?
- Why did the authors select hyperparameter $\alpha=0.7$ where 0.8 outperforms in Figure 5?
- The paper used softmax probability as the prediction score, which does not align with the entropy-based adaptation method. Why did the authors decide to use softmax instead of entropy?


----

Citations
> [b] Gong, T., Kim, Y., Lee, T., Chottananurak, S., & Lee, S. J. (2024). SoTTA: Robust Test-Time Adaptation on Noisy Data Streams. Advances in Neural Information Processing Systems, 36.

### Soundness
2

### Presentation
2

### Contribution
2
