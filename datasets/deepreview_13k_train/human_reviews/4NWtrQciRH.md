# Evidential Learning-based Certainty Estimation for Robust Dense Feature Matching

- Decision: Accept
- Scores: 5, 6, 8, 5

## Abstract
Dense feature matching methods aim to estimate a dense correspondence field between images. Inaccurate correspondence can occur due to the presence of unmatchable region, highlighting the need for certainty measurement. This is typically addressed by training a binary classifier to decide whether each predicted correspondence is reliable. However, deep neural network-based classifiers can be vulnerable to image corruptions or perturbations, making it difficult to obtain reliable matching pairs in corrupted scenario. In this work, we propose an evidential deep learning framework to enhance the robustness of dense matching against corruptions. We modify the certainty prediction branch in dense matching models to generate appropriate belief masses and compute the certainty score by taking expectation over the resulting Dirichlet distribution. We evaluate our method on a wide range of benchmarks and show that our method leads to improved robustness against common corruptions and adversarial attacks, achieving up to 10.1% improvement under severe corruptions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an interesting idea of evidential learning for certainty estimation for the dense pixel-level feature matching task. 
The proposed method is supposedly more OOD and adversarial robust than the current SotA RoMa. 
It is tested against 2D Common Corruptions variants of 2 commonly used datasets for this task i.e. MegaDepth-1500 and ScanNet-1500.
It is also tested against outdated adversarial attacks such as FGSM and PGD.

### Strengths
If the idea of using evidential learning for feature matching is truly novel then that makes the work quite interesting and significant.
Apart from a couple of small typos, the paper is very well written. 
The structure of the paper and the intended story are easy to follow.
The abstract of the paper is well written and to the point.

### Weaknesses
W1- **A lot of implementation details are missing from the paper.**
Simply mentioning that it is built on top of RoMa is insufficient information.
It is understandable to do so for the main paper to save space; however, the supplementary material should be used to provide such information, for example, the exact architecture, the training procedure, details about the datasets, HPC resources used, and other details important for reproducibility.

W2- **Needs a stronger argument for why OOD and Adversarial Robustness is important.**
The argument made in the introduction to explain why OOD and Adversarial robustness are important for this task can be made significantly stronger. Unfortunately, a case has not been made for why this is interesting and important for the community.

W3- **Out-dated evaluations for robustness.**
If the argument for OOD and Adversarial robustness is readiness for the real world, then the evaluations used do not hold up to the argument. Since the 3D Common Corruptions [1] are more real-world common corruptions than the 2D Common Corruptions used in the paper. Additionally, FGSM and PGD attacks were used for evaluating adversarial robustness, however [2] showed in their work that these attacks, originally proposed image classification are inadequate for pixel-wise prediction tasks, such as the one used in this proposed work. This is because FGSM and PGD optimize the attack by increasing the aggregate loss and not the per-pixel loss, this can cause the attack to be highly localized making a non-robust method appear very robust as the mean performance would still be quite well over the rest of the image space. Thus, specialized pixel-wise attacks such as CosPGD are essential for truly evaluating the adversarial robustness of pixel-wise prediction tasks. 

W4- **Using 2D Common Corruptions on other known datasets is not always a novel contribution.**
It is unclear if the contribution of the 2 supposed OOD Robustness evaluation datasets MegaDepth-1500-C and ScanNet-1500-C is merely using 2D Common Corruptions proposed for ImageNet-1k and CIFAR datasets but changing their resolutions and applying them to the respective iid datasets or if there is more to the story, for example, some unforeseen complications that needed to be handled? If not, then simply applying these corruptions to other datasets is not exactly a novel contribution, it is still an interesting study just not a "new contribution" as claimed in the bullet points in the introduction of the paper.

W5- **Almost Redundant Presentation of Results.**
Including both Table 1 and Figure 3 is redundant. I understand that Table 1 contains the mean values over the 5 severity levels while Figure 3 shows the values at each severity, however by using straight dashed lines of respective colors, with y = mean value for all x values the need for Table 1 is eliminated.

### Questions
Following are the questions for which I would highly appreciate an answer, these questions have not impacted my current recommendation for this paper, however, the response might have a significant impact on my final recommendations.

Q1- **Unclear evaluation details for adversarial attacks used.** 
The epsilon values used for attack are starting from 0.1, 0.2 going up to 1., here the attacks l-infinity norm bounded? If yes, then what is the valid image space? Is it [0, 1] or is it [0, 255], meaning when epsilon = 1, does this mean that the epsilon is actually 1/255 (meaning that the valid image space is [0, 255]), or is the value of epsilon actually 1, meaning the entire image is nothing but adversarial noise? In this case, the image would also look semantically different to the human eye meaning that it will no longer be a valid adversarial attack.
And if the epsilon value is in fact 1/255, then the drop in performance is too significant for a very small epsilon value indicating the method is not truly robust to adversarial attacks. Could you also please comment on this?

Q2- **The idea of using Evidential Learning for Pixel-Matching is not entirely novel.** 
While the exact downstream task in [3] is different from the one explored by this proposed work, the core ideas for both seem unusually very similar, the key difference being the distributions used, while [3] used a Normal Inverse-Gamma (NIG) distribution, this work uses a Dirichlet distribution. Would you please further highlight the key differences between the two other than some task-related implementation details?


**References**

[3] Chen Wang, Xiang Wang, Jiawei Zhang, Liang Zhang, Xiao Bai, Xin Ning, Jun Zhou, Edwin Hancock,
Uncertainty estimation for stereo matching based on evidential deep learning,
Pattern Recognition, Volume 124, 2022,108498, ISSN 0031-3203, https://doi.org/10.1016/j.patcog.2021.108498. (https://www.sciencedirect.com/science/article/pii/S0031320321006749)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper applies evidential deep learning to feature matching tasks, introducing an evidential learning framework for certainty estimation in dense feature matching problems. The proposed method enhances robustness in dense matching against corruptions and adversarial attacks, with extensive experiments conducted and visualization presented to demonstrate its performance.

### Strengths
1. The paper is well-motivated, and the main idea is clearly explained.

2. Experiments are conducted across a wide range of benchmarks with various types of corruptions and adversarial attacks. The proposed method outperforms in most cases.

3. The paper includes visualizations to analyze why the proposed method performs better than comparison method, particularly on corrupted data across different datasets.

### Weaknesses
Several questions need to be addressed:

1. This work employs a two-dimensional evidential deep learning (EDL) framework to certainty estimation in both coarse-scale and fine-scale losses. What would happen if EDL were applied to only one of these loss scales? Conducting an ablation study could provide insights into the effectiveness of EDL at each scale. It would be great if the authors could report performance results by applying EDL exclusively to coarse-scale or fine-scale losses, compared to using it on both losses. Specifically, it's unclear if the performance gain is primarily due to the application of EDL at the fine-scale, or if the coarse-scale application is also critical. The interaction between these two scales needs further investigation.

2. Experiments are conducted on two datasets, MegaDepth-1500 and ScanNet-1500. There are other datasets mentioned in RoMa paper such as the street-view IMC 2022 and the challenging WxBS Benchmark. Evaluating the proposed method on those different datasets could further demonstrate its generalizability across diverse scenarios. The current evaluation might not be sufficient to fully assess the robustness of the method across different scene complexities and image characteristics. The lack of evaluation on these datasets limits the conclusions that can be drawn about the method's broad applicability.

3. The proposed framework incorporates evidential deep learning into the training process. Could you provide details on how the proposed framework affects computational time, specifically in terms of training and inference times compared to the baseline RoMa method? It is important to understand the computational overhead introduced by the EDL framework, as this could be a limiting factor for practical applications. A detailed analysis of the time complexity and resource requirements is needed to assess the feasibility of the proposed method.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose modelling certainty of correspondences in dense matchers using an evidential deep learning approach. Instead of just estimating a certainty between 0 and 1, the model outputs the parameters of a Dirichlet distribution over probabilities of the two classes "the predicted correspondence is reliable" and "the predicted correspondence is unreliable". The certainty output is then the expected probability of the first class according to this Dirichlet distribution. The authors show experimentally by retraining the dense matcher RoMa that their approach leads to improved certainty scores, in particular leading to increased robustness to image corruptions.

### Strengths
1. The paper proposes a simple tweak to the RoMa-method, which gives good results experimentally.
2. Within the framework of the RoMa matcher, certainties are updated iteratively in each warp refinement step by a "logit-offset" in the original model. It seems more intuitive to let each refinement step produce positive evidence values for the two classes "correct" and "incorrect" that are summed over the steps, as is done in this paper. Perhaps, the authors could expand on this in the paper.
3. In general, outputting good certainties is an underexplored part of deep learning for 3D vision. The application of evidence based learning to dense matchers is novel.

### Weaknesses
1. The experiments are limited in that only a single model is tested. Hence, it is difficult to say if the improvements generalize to other models.
2. The explanation of evidential deep learning was difficult to understand, and I had to refer back to the original paper by Sensoy et al. I think this section could be improved.
3. Evidential deep learning has a built-in uncertainty measure. In the context of the present paper, we get a Dirichlet distribution over the classes "the predicted correspondence is reliable" and "the predicted correspondence is unreliable", and the associated uncertainty describes how spread out this Dirichlet distribution is. This uncertainty is however not used in the present approach. This makes it a bit difficult to interpret the method. We get a Dirichlet distribution but only use its expected value over the first class. This expected value should signify correspondence reliability, but there is also an uncertainty of this prediction inherent in the Dirichlet distribution, which is not used. Since RoMa uses regression-by-classification in the coarse matching step, a more natural approach may be to reformulate the loss for that classification over $N\times N$ image patches as evidential and use the uncertainty of the predicted Dirichlet distribution as an uncertainty score.

### Questions
1. How much does the threshold used for balanced sampling matter for the robustness under image degradations? Both in the original RoMa and the new model.
2. My reading is that computationally, the new certainty estimation is more or less as heavy as the old in terms of inference and training speed. Is this correct?
3. Is the increased performance due to only better certainties? For example, is the performance the same if certainty scores from the new model are combined with matches from the original RoMa?
4. Is there a way to make use of the built in uncertainty in the Dirichlet distribution as described in Weakness 3?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to unify evidential deep learning (EDL) and dense feature matching, achieving more robust matching results, especially for corrupted image pairs. The authors propose MegaDepth-1500-C and ScanNet-1500-C benchmarks to evaluate the robustness of the proposed method under common image corruptions. The proposed method enjoys superior results in both clean and corrupted data.

### Strengths
1. The incorporation of EDL to dense feature matching is interesting, and has not been investigated before.
2. The proposed method enjoys good performance in corrupted data.

### Weaknesses
1. Although the point of EDL is interesting, the usage of EDL for certainty estimation in dense feature matching is still questionable. From the introduction in Section 2.3, I think EDL's main advance is to detect out-of-distribution samples or mining pseudo-unknown objects. However, the certainty estimation in feature matching is just a binary classification task (matched or not matched). Why is EDL still effective? The authors did not provide a more insightful discussion about this key question. Specifically, the paper lacks a clear explanation of how the evidential framework's uncertainty quantification translates to improved matching performance compared to a standard softmax-based approach, particularly when dealing with in-distribution but corrupted image pairs. The paper should elaborate on the specific mechanisms within EDL that allow it to better distinguish between true matches and mismatches under corruption, rather than simply stating that it provides better uncertainty estimates.

2. The overall contribution is limited. Because of lacking enough in-depth discussion about EDL and certainty estimation in feature matching, makes this work appear more as a mere combination of these two approaches rather than a convincing exploration. The paper does not sufficiently demonstrate a novel insight into the interplay between EDL and feature matching. It feels like a plug-and-play approach, where EDL is incorporated without a deep analysis of its theoretical implications or a thorough investigation into its specific benefits for this task. The lack of ablation studies to isolate the contribution of EDL further reinforces this concern.

3. The introduction of EDL in Section 3.2 is insufficient, missing the necessary background/preliminary in related works. The current introduction does not adequately explain the mathematical foundations of EDL or its connection to Bayesian learning. It lacks a discussion of the Dirichlet distribution and its role in modeling uncertainty, making it difficult for readers unfamiliar with EDL to fully grasp the method's core principles.

4. Experiments are not sufficient, missing discussion of visual localization (InLoc and AachenDay-Night) and homography estimation (HPatches). The proposed method achieves significant improvements in corrupted data, while the improvements based on clean data are limited. As a general certainty estimation, the usage of EDL should consistently improve the matching accuracy in all scenarios. The lack of evaluation on visual localization and homography estimation tasks limits the generalizability of the proposed method. The paper should demonstrate that the improved certainty estimation translates to better performance in downstream tasks beyond just feature matching on corrupted images. The limited improvement on clean data also raises questions about the necessity of EDL for standard feature matching scenarios.

### Questions
If EDL is mainly used for certainty estimation, what are the differences or relationships of the proposed method compared to outlier filtering post-processing in feature matching (RANSAC)?

### Soundness
3

### Presentation
2

### Contribution
2
