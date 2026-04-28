# Detecting Backdoor Samples in Contrastive Language Image Pretraining

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Contrastive language-image pretraining (CLIP) has been found to be vulnerable to poisoning backdoor attacks where the adversary can achieve an almost perfect attack success rate on CLIP models by poisoning only 0.01\% of the training dataset. This raises security concerns on the current practice of pretraining large-scale models on unscrutinized web data using CLIP. In this work, we analyze the representations of backdoor-poisoned samples learned by CLIP models and find that they exhibit unique characteristics in their local subspace, i.e., their local neighborhoods are far more sparse than that of clean samples. Based on this finding, we conduct a systematic study on detecting CLIP backdoor attacks and show that these attacks can be easily and efficiently detected by traditional density ratio-based local outlier detectors, whereas existing backdoor sample detection methods fail. Our experiments also reveal that an unintentional backdoor already exists in the original CC3M dataset and has been trained into a popular open-source model released by OpenCLIP. Based on our detector, one can clean up a million-scale web dataset (e.g., CC3M) efficiently within 15 minutes using 4 Nvidia A100 GPUs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Summary: In this paper, the authors analyzed the representations of backdoor-poisoned samples learned by CLIP models and aim to design an efficient detection method for those backdoors. The experiments reveal that an unintentional backdoor already exists in the original CC3M dataset and has been trained into a popular open-source model released by OpenCLIP.

### Strengths
+ Proposed a backdoor data detection method for CLIP models
+ Experimental results show a high detection rate on the tested models.

### Weaknesses
 - The technical novelty is very limited as the main idea of this paper is simply applying existing outlier detection metrics on detecting CLIP backdoor samples. I didn’t see a major technical innovation in this process.

- They only considered the simple and naive attack settings (directly poisoning the data with fixed noise), which seems reasonable to use those common outlier metrics to detect the possible poisoned data. It is not clear whether optimized trigger can be detected, for example  [1]. The authors might want to compare and comment on those more complicated attacker settings.


- It is also concerning especially if we are considering the adaptive attack setting where the attacker knows your defense strategy. It seems not hard to circumvent the current metric and check the detector by having an additional constraint forcing the density/metrics to look normal. 

- The authors claim their method to be efficient, yet I didn’t find detailed comparison/ experimental results suggesting or comparing the runtime with other baselines. Since quite a few detection metrics rely on the k-nearest neighbor, I am confused about how it could be an efficient strategy when the number of data samples is large.

### Questions
see above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This study exploits this feature to detect backdoor samples by analyzing the local spatial representation features of backdoor samples learned by the CLIP model and finding that the local neighborhoods of these samples are sparser than clean samples. Specifically, the paper proposes the use of traditional density-ratio based local anomaly detection methods, such as Simplified Local Anomaly Factor (SLOF) and Dimension-Aware Anomaly Detection (DAO), to efficiently detect CLIP backdoor samples. These methods are able to detect backdoor samples from large-scale network datasets and clean up the dataset.

### Strengths
EFFICIENCY: The method can quickly detect backdoor samples in large-scale datasets. Using 4 Nvidia A100 GPUs, a network dataset of millions (e.g., CC3M) can be cleaned in 15 minutes, which is especially important for processing large-scale datasets.

Accuracy: The proposed methods, especially the density-based local anomaly detection methods (e.g., SLOF and DAO), show high accuracy in detecting CLIP backdoor samples. These methods are able to effectively distinguish backdoor samples from normal samples, even at very low cast rates (e.g., 0.01%).

Robustness: the method shows good stability and robustness at different poisoning rates, especially at low poisoning rates. Even at poisoning rates as high as 10%, the detection performance can still be maintained at a high level by adjusting the localization parameter k.

### Weaknesses
Sensitivity to parameters: local anomaly detection methods (e.g., SLOF and DAO) rely on the choice of the localizability parameter k. Although the paper mentions that these methods are relatively robust to the value of k, improper parameter selection may still affect detection performance. Specifically, the paper does not provide a clear methodology for selecting the optimal k, nor does it explore the sensitivity of the results to different ranges of k values, which could impact the practical applicability of the method.

Dataset dependency: the method performs well on the CC3M dataset, but its validity on other datasets may require further validation, as different datasets may have different characteristics and distributions. The paper lacks a thorough analysis of how the statistical properties of different datasets, such as image resolution, text length, and semantic diversity, may affect the performance of the proposed anomaly detection methods. This limits the generalizability of the findings.

Experiments may be based primarily on specific model architectures (e.g., ResNet-50 and ViT-B-16). Models with different architectures may have different sensitivities to backdoor attacks, so testing on multiple model architectures may provide a more comprehensive evaluation of the approach. The paper does not explore the impact of variations in model architecture, such as different layer depths, attention mechanisms, or embedding dimensions, on the effectiveness of the backdoor detection method.

### Questions
Does this new backdoor defense approach apply to other datasets like Wikipedia-based Image Text (WIT) and RedCaps?

The paper presents advantages over traditional anomaly detection methods but may lack a comparison with the latest or state-of-the-art backdoor detection methods. This may limit the full understanding of method performance.

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
This paper focuses on the backdoor attacks on CLIP models. The researchers identify unique characteristics of poisoned samples and develop an efficient detection method using local outlier detectors. They discover an unintentional backdoor in the CC3M dataset and provide a fast solution to clean large-scale datasets, demonstrating its effectiveness by processing CC3M in just 15 minutes using 4 GPUs. This work highlights the importance of scrutinizing training data for large-scale AI models and offers a practical approach to enhance their security.

### Strengths
1. The paper focuses on a compelling and timely topic in AI security.
2. A key discovery is that backdoor-poisoned samples in CLIP models exhibit distinctive characteristics in their local subspace, notably sparser local neighborhoods compared to clean samples.
3. The research reveals an intriguing and previously unknown unintentional backdoor in the widely-used CC3M dataset.

### Weaknesses
1. The core defense strategy relies on the observation that backdoor examples exhibit sparser local neighborhoods compared to clean samples. This approach is particularly effective when the poisoning ratio is low, as the k-nearest neighbors of a backdoor example are likely to be clean samples. However, if my understanding is correct, as the poisoning ratio increases, the selection of the hyperparameter k becomes crucial. How to choose the hyperparameters of detection algorithms? Specifically, what is the relationship between the choice of k and the poisoning rate, and how does this impact the detection performance? A more detailed analysis of this relationship is needed.
2. As claimed by the authors,  all the backdoor-poisoned samples contain similar features (the trigger) and are likely to be clustered together in a particular region. Intuitively, these backdoor examples will form a denser region. Besides, according to a previous study [1], the backdoor example region is much denser compared to clean examples.  However, in this paper, the authors claim that backdoor examples exhibit sparser local neighborhoods. How to explain such a difference? It is unclear how the local neighborhood is defined and how this definition leads to the observed sparsity of backdoor examples. The authors should clarify the specific context in which the density is being measured, and why their observations differ from existing findings.
3. Lacking discussion of adaptive attacks. It is important to consider how an attacker might adapt their poisoning strategy to evade detection. The paper should explore potential adaptive attacks that could manipulate the feature space to make poisoned samples appear less sparse, and how the proposed method would perform against such attacks.

### Questions
Please see comments.

### Soundness
3

### Presentation
3

### Contribution
3
