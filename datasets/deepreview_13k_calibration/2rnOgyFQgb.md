# SynQ: Accurate Zero-shot Quantization by Synthesis-aware Fine-tuning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
How can we accurately quantize a pre-trained model without any data?
Quantization algorithms are widely used for deploying neural networks on resource-constrained edge devices.
Zero-shot Quantization (ZSQ) addresses the crucial and practical scenario where training data are inaccessible for privacy or security reasons.
However, three significant challenges hinder the performance of existing ZSQ methods: 1) noise in the synthetic dataset, 2) predictions based on off-target patterns, and the 3) misguidance by erroneous hard labels.
In this paper, we propose SynQ (Synthesis-aware Fine-tuning for Zero-shot Quantization),
a carefully designed ZSQ framework to overcome the limitations of existing methods.
SynQ minimizes the noise from the generated samples by exploiting a low-pass filter.
Then, SynQ trains the quantized model to improve accuracy by aligning its class activation map with the pre-trained model.
Furthermore, SynQ mitigates misguidance from the pre-trained model's error by leveraging only soft labels for difficult samples.
Extensive experiments show that SynQ provides the state-of-the-art accuracy, over existing ZSQ methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents SYNQ (Synthesis-aware Fine-tuning for Zero-shot Quantization), a novel framework designed to address the challenges associated with zero-shot quantization (ZSQ) of pre-trained models, particularly in scenarios where training data is inaccessible due to privacy or security concerns. SYNQ tackles three main issues: noise in synthetic datasets, off-target pattern predictions, and misguidance from erroneous hard labels. The proposed method employs a low-pass filter to reduce noise, optimizes class activation map (CAM) alignment to ensure correct image region prediction, and uses soft labels for difficult samples to prevent misguidance. The authors show that SYNQ achieves state-of-the-art accuracy in image classification tasks compared to existing ZSQ methods.

### Strengths
1. SYNQ offers a unique solution to the problem of quantizing models without access to training data, which is a significant contribution to deploying neural networks on edge devices.
2. Addressing Key Challenges: The paper clearly identifies and addresses three major challenges in ZSQ, providing a comprehensive approach to improving the accuracy of quantized models.
3. Empirical Validation: Extensive experiments demonstrate SYNQ's effectiveness, showing improvements in classification accuracy over existing methods.

### Weaknesses
1. While the paper focuses on image classification, it's unclear how SYNQ would perform in other tasks such as object detection or segmentation.
2. The paper could provide more details on the computational overhead introduced by SYNQ, especially the impact of the low-pass filter and CAM alignment.
3. The paper could benefit from a deeper analysis of SYNQ's robustness to different types and levels of noise in synthetic datasets.

### Questions
1. How does SYNQ handle different types of noise, and is its performance consistent across various noise levels? Before and after the low-pass filter, what is the changes of generated images?
2. There are more related papers should be included, such as 'Data-Free Learning of Student Networks', ‘Data-free network quantization with adversarial knowledge distillation’ and others.

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
The paper proposed a synthesis-aware fine-tuning method, SYNQ, to improve zero-shot quantization (ZSQ) performance. SYNQ defines the issues of ZSQ as follows: 1) high-frequency noise in the generated synthetic dataset, 2) predictions based on off-target patterns, and 3) misguidance by hard labels. SYNQ effectively addresses these issues to improve ZSQ performance through the use of a low-pass filter, CAM alignment, and hard label filtering.

### Strengths
1. The observations regarding the three limitations of ZSQ are interesting, and the proposed method appears feasible.
2. The performance is validated through a variety of experiments. Specifically, experiments were conducted to verify the performance of SYNQ by comparing it with various ZDQ baselines on not only CNN-based models but also ViT-based models.
3. The detailed analyses of the three components of SYNQ enhance the persuasiveness of the methodology.
4. This paper is well-written and easy to follow.

### Weaknesses
1. Although the observations presented in the paper are interesting, most of the experimental evidence provided was gathered under limited conditions. For instance, in Figure 5, experiments were shown only for TexQ among various baseline models, and the analysis for CIFAR-10 and CIFAR-100 used as benchmarks in Table 1 was omitted.
2. In Figure 2, the heat map is shown only one sample image.

For these reasons, it is difficult to be certain whether the presented observations are phenomena that can be observed only in limited baselines and datasets or are generally seen across ZSQ methods. Therefore, the authors should provide experimental evidence across various baselines and datasets beyond the limited settings.

### Questions
1. While SYNQ has been evaluated on W3 and W4, how does it perform under extremely low-bit (e.g., 2-bit) conditions? For example, GENIE [1], one of the ZSQ methods, demonstrated performance not only on W3 and W4 but also on W2. It would be beneficial to add it as a baseline and show performance in low-bit settings as well.
2. What is the performance variation according to the size of the generated synthetic dataset?

[1] Jeon et al., "GENIE: Show Me the Data for Quantization. ", CVPR 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work points out several problems that prior works of Data-free quantization (DFQ) have.
First, synthesized images are noisy compared to their real counterparts.
Second, models quantized with synthesized images tend to predict based on incorrect image patterns.
In addition, the paper claims that using hard labels on hard samples can cause misguidance.

To resolve these problems, the paper proposes three methods.
- The paper revisits classical signal processing and removes the noise of generated images with a low-pass filter.
- To align activation maps between a full precision model and a quantized model, the paper proposes to use grad CAM as a loss function.
- By considering model outputs as the difficulty of the sample, the paper proposes to omit CE loss if the input is a difficult sample.

### Strengths
- The paper tackles the limitations of previous works well.
- The paper tries to denoise synthesized images with a loss-pass filter. This idea is a good point that highlights the importance of classical techniques and theories in the recent AI era.
- The paper identifies the off-target prediction problem that occurs only in the data-free quantization scenario. It is a good suggestion that analyzes the performance of a quantized model with grad GAM and uses it as a loss function.
- The paper executes various experiments and ablation studies for validating proposals.

### Weaknesses
 - The paper refers to the limitations of previous works too much. The same content is repeated over 3 times.
- The investigation and analysis of prior works is insufficient.
    - The paper notes that using hard labels can be harmful to the performance of quantized models, pointing out that previous works used both hard labels (CE loss) and soft labels (KL divergence loss). It can be a novelty that determines the usage of CE loss according to difficulty. However, there already exist several works that use a soft label instead of a hard label. For instance, Qimera proposed to use the coefficient of superposed latent embedding as soft labels. AIT also pointed out the importance of soft labels and used soft labels only for the loss function.
    - The results of current state-of-the-art works are omitted. In the CNN domain, GENIE shows better performance than this work. Also, in transformer variants, PSAQ-ViT V2 shows better results. Those works should be addressed.
- Generated images with SynQ can help understand the superiority of the proposal.  Please attach generated images with SynQ (before and after applying the low-pass filter)

### Questions
- The reviewer thinks that off-target prediction problems may occur under the DFQ scenario, not general quantization scenarios. Nevertheless, did the authors examine whether the problem occurred with real data?
- What is the experimental setting of the baseline in Table 3 such as the quantization algorithm? (the same result is not in the Table 1)
- In Figure 7,
    - Does this tendency still hold with other models and datasets? For instance, the distribution of model outputs that are used as a measurement of difficulty can be different if the number of classes differs. With various models (e.g., ResNet, MobileNet, etc) and datasets (e.g., CIFAR10, CIFAR100, ImageNet), is the optimal $\tau$ always 0.5 or values close to it?
    - The magnitude of $\lambda_{CAM}$ in (a) are much larger than those of $\lambda_{CE}$. Is the magnitude of CAM loss on average much smaller than that of $\lambda_{CE}$ loss?
- In Table 5 of the appendix,
    - Those experiments are based on 3 works that use a generator. However, SynQ adopts noise optimization for generating images. Why aren’t other works that adopt noise optimization addressed?
    - Those 3 works are improved with SynQ. However, they are worse than SynQ itself. Can the authors’ opinions about this provided?
    - How about applying SynQ to other works based on noise optimization?

### Soundness
3

### Presentation
2

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
They propose SYNQ that targets to overcome the following limitations of current ZSQs:
1. noise in the synthetic dataset; 2. off-target patterns; 3. misguidance by erroneous hard labels.

### Strengths
The manuscript exhibits a coherent structure and is straightforward to navigate. Figures 1 through 3 effectively illustrate the key observations and the rationale behind our approach. Notably, the visualization of the Magnitude spectrum in Figure 1 is particularly engaging. To the best of my knowledge, this method is the first zsq to complete experiments on both cnn and vit, which is appreciated.

### Weaknesses
1.line382:The header method of Table 1 is incorrectly written as CIFAR dataset
2. line237: The Low-pass filter (Section 4.2) directly modifies the image's impact on the model without using artificial visual features to judge whether it is good or bad. Does Low-pass filters have advantages over the existing ZSQ?
3. Is Fig.2 different at different bit widths/networks? Is this a general situation in ZSQ?
4. Lack of computational cost analysis comparison with state of the art methods.

### Questions
The authors could refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
