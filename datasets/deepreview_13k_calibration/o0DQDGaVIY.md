# Noise-Augmented Deep Neural Networks for Image Classification: Insights from Information Theory

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 5, 1

## Abstract
In this study, we explore the impact of proactively injecting noise into deep learning models, focusing particularly on classification problems, such as image classification and domain adaptation. While noise is typically seen as harmful, our findings reveal that, under certain conditions, noise can beneficially influence the entropy of the system, enhancing the learning outcomes. We employ information entropy to characterize the complexity of the learning tasks and categorize noise into two types, positive noise (PN) and harmful noise (HN), based on whether it helps reduce task complexity. We theoretically prove that positive noise reduces task complexity and demonstrate the presence of positive noise through extensive experiments on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs). We further propose NoisyNN, an innovative approach to leverage positive noise. NoisyNN achieves state-of-the-art performance on various image classification and domain adaptation tasks. Extensive experiments conducted on {15 datasets}, including popular image datasets and out-of-distribution datasets, demonstrate the efficacy of our method. Our study provides the community with a new paradigm for improving model performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores how adding noise to deep neural networks can improve image classification and domain adaptation. It differentiates between positive noise, which helps, and harmful noise, which hurts model performance. The authors introduce NoisyNN, a method that uses positive noise to enhance model outcomes. Theoretical and empirical evidence supports the effectiveness of NoisyNN, showing it can achieve better results than traditional approaches. This study offers a new view on noise in machine learning.

### Strengths
- introduces a novel perspective on noise in deep learning by categorizing it into positive noise (PN) and harmful noise (HN) based on its impact on task complexity
- offers a fresh approach to understanding noise in the context of deep learning
- presents impressive experimental results

### Weaknesses
The results presented in the paper are excellent, and the authors have already provided the code. However, it is inconvenient to reproduce the experimental results without the pretrained models. Could you please provide models or APIs that would make it easier to replicate the results?

### Questions
Could you please provide models or APIs that would make it easier to replicate the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new type of noise for injecting in the latent dimension space to regularize the network. It shows that the popular Gaussian and Salt-Pepper noises are harmful and degrade performance. The paper shows the requirement for noise to have a positive effect. Based on this, a linear transformation noise is proposed, which is created by a circular shift Q matrix.

### Strengths
1. The proposed method is effective and well explained. 
2. It works with popular architectures. CNN and Transformers show in the paper. 
3. The method is helpful in domain adaptation as well.

### Weaknesses
1. Paper compares the proposed approach only with 2 basic latent dimension noise. Approaches similar to Manifold mixup should be compared: Noisy Feature Mixup
2. Why does the performance drop when combined with input augmentations (Table 17)? Input augmentations are staple of training neural networks. Incompatibility with it can be a big problem.
3. How does it compares against advanced input augmentation (like mixup, cutmix, randaug etc). Is better or worse? Is it compatible with them?
4. The paper's claim can be strengthened by showing results with another linear transformation noise.

### Questions
1. When compared to other noise for injection, the proposed approach shows beneficial. How does it fit with other regularization methods should be explored in more detail.
2. The paper comapres results when no input augmentation is present. How does the baseline methods compare with input augmentations?
3. Were the baseline noise arguments optimized? like the mean and variance of gaussian noise.
4. Domain adaptation results are compared with ViT and CNN based approaches but results are shown only with ViT based approach. Since, it is compared with CNN based approaches, it would be interesting to see how the approach performs with it.
5. How does it impact the training loss/accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper analyzes the proactive noise injection into deep learning models from both theoretical and empirical perspectives. This paper theoretically characterizes the positive noise that reduces task complexity based on information entropy, and demonstrates the presence of positive noise through experiments. The approach ‘NoisyNN’ leveraging positive noise is proposed, and its efficacy is shown through empirical experiments.

### Strengths
1. Theoretical analysis is provided to characterize the idea of 'positive noise' proposed in this paper.

2. Empirical experiments are given in this paper to support the advantage of leveraging positive noise.

3. The approach 'NoisyNN' that utilizes the positive noise is proposed in this paper, and its efficacy is demonstrated through empirical experiments.

### Weaknesses
1. This paper introduced the‘NoisyNN’ method based on a specific type of positive noise, namely the positive linear transformation noise, and the following empirical experiments are also for the 'NoisyNN' method. How does the idea of this paper work with other types of positive noise?

2. This paper aims to analyze the influence of injecting noise both theoretically and empirically. The empirical experiments focus on image classification and domain adaptation, alongside several other related tasks. However, the current theoretical analysis is primarily for classification tasks. How might the current theoretical analysis be extended to cover other related tasks mentioned in this paper, for example, those mentioned in Section 4?

### Questions
1. Apart from the specific types of noise analyzed in this paper (Section 3), how do other types of positive noise work under the idea of this paper? 

2. The novelty of this paper seems mainly lies in proposing the concept of 'positive noise' and its application. How does this paper compare with existing papers with similar ideas of adding noise? And the novelty of this paper compared to those papers?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper introduces NoisyNN, a novel approach that leverages positive noise to improve deep neural networks' performance on tasks like image classification and domain adaptation. The authors categorize noise into positive noise (PN) and harmful noise (HN) based on their effect on task complexity, using information-theoretic metrics. The analysis is conducted on various noise type including Linear transformation noise, Gaussian and salt-and-pepper noise. Extensive experiments validate NoisyNN's effectiveness using CNNs and Vision Transformers (ViTs) across multiple datasets.

However, a major red flag is the suspicious ImageNet-1K accuracy. No model (22K pretrained + 1K finetuned) has ever achieved 95% top-1 accuracy on the ImageNet-1K validation set. Even with extensive web-scale pre-training, the best state-of-the-art performance remains below 92.5% (https://paperswithcode.com/sota/image-classification-on-imagenet). I intend to reproduce the reported performance. However, the README in the anonymous submission is completely missing, raising concerns about the completeness of the codebase. This lack of professionalism further reflects the questionable nature of your reported performance. I am willing to proceed, but please provide detailed instructions first. Given the unusually high performance you reported, you should be thoroughly familiar with the codebase, so there should be no reason for not providing this.

### Strengths
- (1) The analysis of noise choices is thorough including Linear transformation noise, Gaussian and salt-and-pepper noise.
    
- (2) The method can be generalized to various architecture includes ResNet and ViT.

### Weaknesses
- (1) Poor writing organization. The authors study three types of noise but the linear transformation noise is the one with positive effect. Thus, the authors are suggest to emphasize that the proposed NoisyNN is built upon linear  linear Transformation noise to avoid confusion.
    
- (2) Experimental details are not explained clearly.
    
    - (a) The author report the results of Vanilla ViT-B with accuracy of 84.33%. It would be great if the author could reference the codebase/implementation of the baseline.
        
    - (b) Are the noises applied to the imageNet-1k fine-tuning or {imageNet21K pretraining + imageNet1K fine-tuning} ?
        
- (3) The specifics of injecting noise at the feature or feature-grid level are unclear. Is the noise applied to each feature grid individually?
    
- (4) The comparison with state-of-the-art data augmentation models is missing. NoisyNN is essentially a data augmentation technique, but the related work in Section 2 only covers research up to 2020—prior to the introduction of vision Transformers. As a result, the references are outdated. Additionally, the approaches compared in Table 18 are overly simplistic, relying on basic techniques such as “RandomFlip + Gaussian Blur + RandAugment.”
    
- (4) Suspicious Claim of Accuracy in ImageNet-1K. The reasons are explained in (a) (b) (c) below. The suggestion is provided in (d) below.

    
    - (a) One of the major red flags is the suspiciously high ImageNet-1K top-1 accuracy reported in this paper. In Table 3, the proposed approach claims to achieve 94.8% top-1 accuracy. However, no model has ever reached such a performance on the ImageNet-1K validation set. Even with extensive web-scale pre-training, the best state-of-the-art performance remains below 92.5% ([https://paperswithcode.com/sota/image-classification-on-imagenet](https://paperswithcode.com/sota/image-classification-on-imagenet)). This discrepancy is a critical concern for the computer vision community.
        
    - (b) Under the same imageNet21K pretraing and imageNet1K fine-tuning setting, the state-of-the-art computer vision model is CoAtNet-4 (Table 4 in ) achieving 88.56%.
        
    - (c) Even with stronger web-scale image-text pre-training, PaLi [2] and CoCa [3] can only reach 90.9% and 91.0% respectively on imageNet-1K.

    - (d) The authors are suggested to provide more constructive guideline on the reproduction of the codebase as raise in the Question section.
        
- (5) I am going to reproduce the performance. But the README in the anonymous is entirely MISSING, and thus I have concerns about the completeness of the codebase. I am willing to reproduce the code, but first, please provide clear instructions. There should be no excuse, as you are presumably very familiar with the codebase, given the unusually high performance you achieved.

[1] Dai Z, Liu H, Le Q V, et al. Coatnet: Marrying convolution and attention for all data sizes[J]. Advances in neural information processing systems, 2021, 34: 3965-3977 (1283 citations till Oct 2024).

[2] Chen X, Wang X, Changpinyo S, et al. Pali: A jointly-scaled multilingual language-image model[J]. ICLR, 2023 (567 citations till Oct 2024).

[3] Yu J, Wang Z, Vasudevan V, et al. Coca: Contrastive captioners are image-text foundation models[J]. TMLR, 2022 (1225 citations till Oct 2024).

[4] Tu Z, Talebi H, Zhang H, et al. Maxvit: Multi-axis vision transformer[C]//European conference on computer vision. Cham: Springer Nature Switzerland, 2022: 459-479 (620 citations till Oct 2024).

[5] Liu Z, Mao H, Wu C Y, et al. A convnet for the 2020s[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 11976-11986 (5765 citations till Oct 2024).

### Questions
- Can the authors assess the transferability of their model to downstream object detection and segmentation tasks. In practice, models trained on ImageNet [4, 5] often utilize ImageNet1K-pretrained weights as the pretrained backbone for these downstream applications.
    
- I plan to reproduce the performance, but the README (reproduction instructions) in the anonymous submission is completely missing. This raises concerns about the codebase's completeness. The author should include detailed instructions, covering installation, training, and entry scripts. Without these, reproducibility is impossible. Even if the codebase of this work may be built upon timm and opensource codebase, the authors should still provide the reproducing instruction. Here’s a step-by-step guide to help you.
    
    - Installation instruction, please refer to the template([https://github.com/facebookresearch/ConvNeXt/blob/main/INSTALL.md](https://github.com/facebookresearch/ConvNeXt/blob/main/INSTALL.md))
        
    - Training instruction, and command with all necessary arguments, please refer to the template ([https://github.com/facebookresearch/ConvNeXt/blob/main/INSTALL.md](https://github.com/facebookresearch/ConvNeXt/blob/main/INSTALL.md)).  More systematical version can be seen in timm.
        
    - Evaluation procedure

    - Data preparation steps. Was the validation data separated from the training data?

    - Release of the model weights

    - Details for the packages and the version.

### Soundness
1

### Presentation
2

### Contribution
2
