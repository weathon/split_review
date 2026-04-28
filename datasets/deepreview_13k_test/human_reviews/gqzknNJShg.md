# FourierAugment: Frequency-Based Image Encoding for Resource-Constrained Vision Tasks

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Resource-constrained vision tasks, such as image classification on low-end devices, put forward significant challenges due to limited computational resources and restricted access to a vast number of training samples. Previous studies have utilized data augmentation that optimizes various image transformations to learn effective lightweight models with few data samples. However, these studies require a calibration step for optimizing data augmentation to specific scenarios or hardly exploit frequency components readily available from Fourier analysis. To address the limitations, we propose a frequency-based image encoding method, namely FourierAugment, which allows lightweight models to learn richer features with a restrained amount of data. Further, we reveal the correlations between the amount of data and frequency components lightweight models learn in the process of designing FourierAugment. Extensive experiments on multiple resource-constrained vision tasks under diverse conditions corroborate the effectiveness of the proposed FourierAugment method compared to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper illuminates the relationship between the learning frequency of lightweight models and the quantity of training data, presenting a clear correlation. It further introduces a novel data augmentation technique that leverages filters within the image frequency domain. The effectiveness of this new augmentation method is then demonstrated through its application in various image classification tasks, showcasing its potential to enhance model performance.

### Strengths
The primary strength of this paper lies in its introduction of a novel data augmentation technique. This new method stands out due to its simplicity and effectiveness, providing a valuable contribution to the field of image classification

### Weaknesses
The paper's weakness lies in its limited scope: the novel data augmentation method is only tested on lightweight models and small datasets. Its efficacy in broader vision tasks such as detection and segmentation remains unexplored, suggesting an area ripe for further research.

### Questions
Could you please clarify the meaning of "I" in formulation (1)? 
Additionally, the operational details of the filter remain unclear to me.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces FourierAugment, a frequency-based image encoding method, to address the challenges faced in resource-constrained vision tasks. By effectively utilizing frequency components from Fourier analysis, FourierAugment enables lightweight models to learn richer features with limited data.

### Strengths
1.  It is meaningful that the authors focus on the scenario where both the training data and computational resources are constrained.

2. The effectiveness of the proposed method on multiple resource-constrained vision tasks is demonstrated.

### Weaknesses
1. Learning both low- and high-frequency information in balance is not novel. There have been many works that promote uniformly learning various frequency domains by randomly masking frequency segments, but the authors did not analyze or compare their work to these related works.

[1] Stochastic Frequency Masking to Improve Super-Resolution and Denoising Networks. ECCV 2020.

[2] FSDR: Frequency Space Domain Randomization for Domain Generalization. CVPR 2021

[3] Spectrum Random Masking for Generalization in Image-based Reinforcement Learning. NeurIPS 2022.

[4] MASKED FREQUENCY MODELING FOR SELF-SUPERVISED VISUAL PRE-TRAINING. ICLR 2023.

2. I am curious if other frequency domain augmentation methods can also enhance performance, such as perturbing amplitudes[5], or randomly masking frequencies in the frequency domain[3].

[5] Proportional Amplitude Spectrum Training Augmentation for Synthetic-to-Real Domain Generalization. ICCV 2023.

3. Can the authors provide evidence that the performance improvement is not solely due to the increased parameters, considering that the number of input channels has been changed to nx3? Could you discuss the computational complexity of your proposed method compared to other methods?

4. Can the authors switch the backbone to demonstrate that there is indeed an increase in learning high-frequency features in the early stages, rather than it being a proprietary feature of ResNet?

5. It would be helpful to understand if there are any limitations to your method. Are there specific scenarios or datasets where your approach may not perform as well as existing methods? If so, what are the reasons for this?

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contributions of the paper include the development of FourierAugment, which leverages frequency-based information to improve feature learning, and the exploration of the relationship between data quantity and frequency components learned by lightweight models. Extensive experiments demonstrate that FourierAugment outperforms baseline methods in various resource-constrained vision tasks.

### Strengths
1. The introduction of FourierAugment as a frequency-based image encoding method represents a novel and innovative approach in addressing resource-constrained vision tasks. FourierAugment's unique utilization of frequency components sets it apart from conventional data augmentation methods.
2. The paper's empirical study is thorough and well-designed, ensuring the validity and reliability of the results. Extensive experiments on multiple datasets and resource-constrained vision tasks provide a strong foundation for the paper's claims.
3. The paper is well-structured, with a clear presentation of the problem statement, method development, empirical study, and results.

### Weaknesses
The paper could benefit from a more comprehensive theoretical background and motivation section. It's important to provide a clear foundation for why FourierAugment was developed and the specific theoretical underpinnings. A deeper exploration of the relationship between frequency components and lightweight model learning could enhance the paper's overall coherence.

### Questions
1. The theoretical underpinnings and motivations for proposing FourierAugment, including the specific theoretical underpinnings that guided its development, would add to the coherence of the paper if they were added in full.
2. The n value is chosen empirically? Is there a definite basis for setting 2 or 3?
3. How does the method proposed in this paper compare to the comparative baseline AugMix, RandAugment and Deep AutoAugment in terms of computational efficiency and generalizability to different visual tasks?
4. Does adding the image enhancement proposed in this paper to the image classification and FSCIL tasks significantly extend the processing time of the tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The presented method works in a specific setting of resource-constrained deep learning. The authors propose to replace the first trainable encoding block of common architectures with a manually crafted frequency-separating module. Namely, a discrete Fourier transform is applied to the input image, and the obtained frequencies are separated into several bands. Afterward, the bands are transformed into the spatial space again with the help of the inverse Fourier transform. The outputs are concatenated channel-wise and serve as an input for the neural network.

The method is evaluated both on a common classification task (with a limited number of data points per class) and on few-show class-incremental learning (FSCIL). As reported, the proposed module works better than recent augmentation strategies developed for full-scale ImageNet training such as AugMix, RandAugment, and Deep AutoAugment.

### Strengths
The problem considered in the paper is quite important for the community since deep learning on edge devices is rather relevant for applications. The authors clearly describe the motivation for their approach, and the description of the method is also easy to understand. 
The proposed approach seems to improve the quality by a significant margin in some cases, e.g. for the ImageNet subset with 100 images per class, the accuracy is twice that of the baseline model (Tab. 1). Taking into account the simplicity of the method, this is an interesting result.

### Weaknesses
1. Separating the frequency bands of the network input is not novel per se: for example, it is used from time to time in generative modeling, see e.g. [1], [2]. However, usually, it is done with the help of wavelets. I recommend adding this baseline to the comparison, namely, decomposing the input image with two or three iterations of discrete wavelet transform before feeding the result to the network.
1. The authors compare their method with a number of other Fourier-based methods (Appendix C.2.3) and conclude that those methods do not perform well in their settings because they were specifically designed for medical image processing. It would be great to evaluate the proposed FourierAugment method on the medical data to demonstrate if it is competitive in that field since medical image processing often suffers from a limited amount of data.
1. Minor remarks:
    1. I find the name of the method, i.e. *FourierAugment*, misleading since it is just a way to present exactly the same information which the image contains, in a different way. In addition, it is deterministic, not random. This contradicts the way the word *augmentation* is typically used by the community nowadays.
    1. Fig. 2 contains too much empty space and does not tell a lot of useful information. For example, the horizontal axis is not very informative since there is nothing unexpected in the training dynamics, and the whole figure may be replaced with a table reporting the final performance.

[1] Hoogeboom et al. simple diffusion: End-to-end diffusion for high-resolution images. In ICML, 2023. 

[2] Barron. A General and Adaptive Robust Loss Function. In CVPR, 2019.

### Questions
Please address the weaknesses listed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
