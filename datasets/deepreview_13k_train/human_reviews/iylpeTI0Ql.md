# Noisy Test-Time Adaptation in Vision-Language Models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Test-time adaptation (TTA) aims to address distribution shifts between source and target data by relying solely on target data during testing. In open-world scenarios, models often encounter noisy samples, i.e., samples outside the in-distribution (ID) label space. Leveraging the zero-shot capability of pre-trained vision-language models (VLMs), this paper introduces Zero-Shot Noisy TTA (ZS-NTTA), focusing on adapting the model to target data with noisy samples during test-time in a zero-shot manner. In the preliminary study, we reveal that existing TTA methods suffer from a severe performance decline under ZS-NTTA, often lagging behind even the frozen model.  We conduct comprehensive experiments to analyze this phenomenon, revealing that the negative impact of unfiltered noisy data outweighs the benefits of clean data during model updating. In addition, as these methods adopt the adapting classifier to implement ID classification and noise detection sub-tasks, the ability of the model in both sub-tasks is largely hampered. Based on this analysis, we propose a novel framework that decouples the classifier and detector, focusing on developing an individual detector while keeping the classifier (including the backbone) frozen. Technically, we introduce the Adaptive Noise Detector (AdaND), which utilizes the frozen model’s outputs as pseudo-labels to train a noise detector for detecting noisy samples effectively. To address clean data streams, we further inject Gaussian noise during adaptation, preventing the detector from misclassifying clean samples as noisy.
Beyond the ZS-NTTA, AdaND can also improve the zero-shot out-of-distribution (ZS-OOD) detection ability of VLMs. Extensive experiments show that our method outperforms in both ZS-NTTA and ZS-OOD detection. On ImageNet, AdaND achieves a notable improvement of $8.32\%$ in harmonic mean accuracy ($\text{Acc}_\text{H}$) for ZS-NTTA and $9.40\%$ in FPR95 for ZS-OOD detection, compared to state-of-the-art methods. Importantly, AdaND is computationally efficient and comparable to the model-frozen method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper deals with the test-time adaptation (TTA) task and extends it to a challenging scenario, i.e., zero-shot noisy test-time adaptation (ZS-NTTA). The ZS-NTTA  adapts the source model to deal with the noisy target data during test-time and allow the target data to be noisy. This work first studies which factors can decline the performance in the ZS-NTTA task, then proposes a new method to overcome these problems.

### Strengths
1. This work studies a challenging task of zero-shot noisy test-time adaptation, which is practical and applicable to in real-world applications.
2. The three observations are interesting and novel. They reveals the reasons why the NS-TTA is difficult and contribute to the community.
3. The proposed method is reasonable and achieve good results in the experiment.

### Weaknesses
1. The proposed method studies the ranking distribution of different methods in Fig. 2. Can these ranking really tell the superiority of these methods? It is possible that one method is good at dealing with challenging datasets, and the other is good at easier datasets. Why not evaluate them using the absolute accuracy (instead of the ranks in this work)?
2. How to inject the noise to the data is an important factor of the proposed method. Is there any theoretical analysis?
3. It is better to study how the portion of the noisy labels influence the performance.

### Questions
1. Please discuss the reason to evaluate the methods using rank in Fig. 2. 
2. It is better to analyze the theoretical foundation of injecting the noise to the data using the proposed method.
3. It is better to study how the portion of the noisy labels influence the performance.

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
5

### Summary
This paper introduces a novel task setting termed zero-shot noisy Test-Time Adaptation (ZS-NTTA), focusing on adapting models to target data containing noisy samples during test-time in a zero-shot manner. To address this challenge, the authors propose the AdaND method, which trains a noise detector online using detected noisy samples. The results of the experiments are reported in terms of classification accuracy and Out-of-Distribution (OOD) detection metrics.

### Strengths
1. The proposed task addresses issues commonly encountered in real-world applications of classification models, which are often overlooked in current research. For instance, existing OOD detection methods assume a clean stream when reporting accuracy, and clip models are applied in noisy TTA tasks for zero-shot usage.
2. Although the method of training an additional noise detector is simple, it proves to be quite effective according to the experimental results.
3. There is improved performance in both classification and OOD detection metrics.

### Weaknesses
1. I have concerns regarding the definition of the task name. The ultimate goal of the proposed ZS-NTTA task is to detect OOD samples and correctly classify In-Distribution (ID) samples. I understand the definitions of noisy TTA and OOD detection, where both aim to handle test sets containing both ID and OOD cases. In my view, TTA leans more towards a methodological strategy focusing on enhancing model performance and adaptability during testing, while OOD detection leans towards a task definition, primarily studying how to handle test datasets with noise/OOD samples. Thus, from this perspective, the task might be more appropriately named something like "test-time OOD detection," as there are similar task definitions in academia, such as [1,2], which require discussion and comparison.

[1] Test-Time Linear Out-of-Distribution Detection, CVPR2024

[2] Atta: Anomaly-aware test-time adaptation for out-of-distribution detection in segmentation. NIPS2023

2. Assuming there are no issues with the paper's title or task definition, and considering that TTA focuses more on classification accuracy while OOD detection focuses on the capability of detecting OOD/noise, there appears to be a mismatch between the methodology and the title of the paper. Specifically, the method emphasizes training an OOD detector with a fixed classifier, focusing on OOD detection capability rather than improving classification accuracy. I suspect the improvement in classification accuracy reported in the paper's tables is due to successful OOD detection rather than enhancements to the classifier, correct?

3. TTA methods are generally sensitive to the ratio of clean to noise in samples, ranging from 1:1000 to 1000:1. Is the performance of this method stable across such variations?

4. Line 376 is ambiguous and could lead readers to misunderstand that the clean and noisy streams are known. If I understand correctly, the paper suggests that the test stream is unknown, and that inserting Gaussian noise can handle various unknown test stream scenarios, including both clean and noisy streams.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel setting called Zero-Shot Noisy TTA and builds benchmarks. It provides a theoretical analysis of why existing TTA methods struggle in noisy scenarios. The paper proposes AdaND, which decouples the classifier and detector to identify noisy data. Experiments show that AdaND works well in ZS-NTTA and achieves computational efficiency.

### Strengths
The paper is well-organized, and the idea of the Zero-Shot Noisy TTA setting is novel. It offers a comprehensive analysis of existing methods that suffer from Zero-Shot Noisy TTA, and this analysis is easy to follow. The results demonstrate a notable improvement across many benchmarks, and the proposed method AdaND is computationally efficient.

### Weaknesses
Though Zero-shot Noisy TTA is a new task, the method of utilizing two stages and pseudo labels to train a noisy detector is not novel; the idea of using unlabel test data to train a more robust OOD classifier has been explored in other scenarios, such as [1] for zero-shot OOD detection.

It would be better to provide more experiments with more complex datasets, such as near ID/OOD datasets, for example, Imagenet and NINCO[2].

Some recent test-time adaptation works are not compared in the experiments, such as [4], which adopts a training-free adapter to achieve efficiency. I am concerned whether the noise detector can be replaced by another training-free module to be more efficient for test time and get better performance, such as cache memory.

### Questions
As the authors analyze in Section 3.3, some inaccuracies during the early stages of TTA can gradually lead the model to overfit. I wonder whether the pseudo-labels in the early stages are accurate and the inaccuracies in the Noise Detector will accumulate.

### Soundness
3

### Presentation
3

### Contribution
2
