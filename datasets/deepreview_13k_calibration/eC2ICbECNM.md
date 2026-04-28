# Ctrl-U: Robust Conditional Image Generation via Uncertainty-aware Reward Modeling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we focus on the task of conditional image generation, where an image is synthesized according to user instructions.
The critical challenge underpinning this task is ensuring both the fidelity of the generated images and their semantic alignment with the provided conditions.
To tackle this issue, previous studies have employed supervised perceptual losses derived from pre-trained models, \ie, reward models, to enforce alignment between the condition and the generated result.
However, we observe one inherent shortcoming: considering the diversity of synthesized images, the reward model usually provides inaccurate feedback when encountering newly generated data, which can undermine the training process.
To address this limitation, we propose an uncertainty-aware reward modeling, called \textbf{Ctrl-U}, including uncertainty estimation and uncertainty-aware regularization, designed to reduce the adverse effects of imprecise feedback from the reward model. 
Given the inherent cognitive uncertainty within reward models, even images generated under identical conditions often result in a relatively large discrepancy in reward loss. Inspired by the observation, we explicitly leverage such prediction variance as an uncertainty indicator.
Based on the uncertainty estimation, we regularize the model training by adaptively rectifying the reward. 
In particular, rewards with lower uncertainty receive higher loss weights, while those with higher uncertainty are given reduced weights to allow for larger variability.
The proposed uncertainty regularization facilitates reward fine-tuning through consistency construction.
Extensive experiments validate the effectiveness of our methodology in improving the controllability and generation quality, as well as its scalability across diverse conditional scenarios, including segmentation mask, edge, and depth conditions. Code, models, and demo will soon be available at \href{https://grenoble-zhang.io/Ctrl-U-Page/}{\textcolor{purple}{ this https URL}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors investigate the reward model used in conditional generation diffusion models and find that it tends to output wrong conditions (e.g., segmentation masks) on the de-noised images. They propose leveraging the output uncertainty on two different generated results from different denoising timestamps. They reduce the loss weight of pixels with high uncertainty while increasing ones with low uncertainty.

### Strengths
1. The proposed method is intuitive and easy to incorporate.
2. The quantitative results outperform the baselines by a large margin (although some metrics used seem to be questionable, e.g., mIoU from another segmentation model; see Weaknesses)

### Weaknesses
1. If I understand correctly, the authors leverage another more powerful segmentation model to evaluate mIoU. However, this seems strange to me. For instance, in Fig. 3, while the authors circled out the additional green masks by ControlNet++, I think this shouldn't be regarded as an error. Because the green boxes seem to be windows, and the powerful segmentation model predicts these masks, it could be that ControlNet++ did a great job generating the windows based on the concept of the pinkish building mask.
2. Please see Questions.

### Questions
1. The annotation in Fig. 2 and Eq. 2 needs to be clarified. Specifically, is the KL divergence computed between the input control (c) and c1, c2 separately? Or is it computed only between c1 and c2? While Fig. 2 denotes the former, Eq. 2 denotes the latter.
2. What is the range of t1 and t2? Also, do the optimal t1 and t2 vary on different datasets/tasks?
3. Visualization of inaccurate prediction from the reward model and the corresponding uncertainty prediction. Are they aligned? In other words, does the uncertainty reduce the weight loss of positions where the predicted condition matches the input but somehow has a significant loss (the reward model predicts the wrong segmentation mask)?
4. Line 360, can the authors elaborate more on "After communicating with the authors, we re-implemented the CLIP-Score for ControlNet++ (Li et al., 2024b) and marked it with ∗ in Table 3"?
5. Does the reward model impact the performance if a different one is used? Also, does the consistency prediction generalize well to different distributions? (e.g., different segmentation datasets)

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
2

### Summary
This paper addresses the issue of conditional image generation. The authors identify a significant flaw in the perceptual loss used for conditional image generation, where it may provide incorrect supervisory signals for some newly generated images, thereby affecting the results. To address this, the authors propose a simple yet effective approach to assess the reliability of supervisory loss by estimating the uncertainty in the generated images. Specifically,  during the training process they measure the variability between two different images generated under the same condition as an indicator of the uncertainty in the supervisory loss, suggesting that a high variability implies an unreliable signal. This method automatically corrects the supervisory signals, thereby enhancing the quality of the generated models. The conclusions are supported by detailed experimental evidence.

### Strengths
The method is straightforward and effective, and the paper is well-organized and easy to understand.

### Weaknesses
1. There is a lack of important comparisons, particularly the absence of direct comparison with methods that use auxiliary networks to measure uncertainty (e.g.  Learning model uncertainty as
variance-minimizing instance weights(ICLR 24), It can be used to conduct an ablation experiment to compare who is the better way to measure uncertainty for Conditional Image Generation), discussed on line 214, which is a significant oversight.

2. The motivation section in the introduction is somewhat abrupt and some statements, such as those mentioned on line 74 regarding "the denoised image at t = 0 aligns well with the input condition," are not intuitive and require clearer explanation.

### Questions
see Weaknesses

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
3

### Summary
Targeting  conditional image generation, the authors proposed an uncertainty-aware reward modeling method, named Ctrl-U. This method includes uncertainty estimation and uncertainty-aware regularization, aimed at mitigating the negative effects of inaccurate feedback from the reward model. The authors use the prediction variance as an uncertainty indicator, and based on this, they adaptively adjust the reward during model training. Rewards with lower uncertainty are given higher loss weights, while those with higher uncertainty are given reduced weights, allowing for more variability.

### Strengths
1. This paper targets the uncertainty problem existing in training with reward models, which is critical and meaningful.

2. Despite increasing training time for each training step, the proposed method avoids incorporating additional modules to assess reward uncertainty.

### Weaknesses
1. Lack of novelty. The major contribution of this work is the methodology that generates two images, calculates their uncertainty, and reweights the reward loss. Such a solution seems to be trivial, double the time of each training step, and bring neglective quantitative improvement.
Maybe the author can report the computational cost required before and after using the proposed method. 
In addition, why do not the authors collect a dataset composed of paired generated images and their uncertainty scores and then train a simple predictor to predict uncertainty for each image to remove the necessity to generate two images in one step? In my opinion, such an uncertainty predictor can also be adaptive to different generative models and can significantly improve the training efficiency compared to the proposed method. Since the predictor can be more lightweight than generative models and can be trained on image latents.

2. Unfair comparison. The method proposed in this paper is mainly used for post-training. In other words, authors need to pretrain a conditional model such as ControlNet before employing the proposed training losses (Line 292-295). However, during quantitative comparison, authors compare their methods with pretrained models. Such a comparison seems to be inappropriate. It may be better to report the performance improvement when applying the proposed method to different base models, showing the generalization ability of the proposed method.

### Questions
1. As specified in L215-217, authors stated that directly regressing uncertainty can incur indistinguishable predictions over samples. However, In L239-240, the proposed methods also require additional terms to prevent indistinguishable predictions. Considering that the proposed method can introduce double training time, what’s the major advantage of the proposed method?
2. I'm confused by the value of t in equ. 7. Specifically, how does t in equ.7 relate to t1 and t2 introduced in equ.5?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper made improvements to the controllability of diffusion-based conditional generative models by introducing the concept of uncertainty.
The authors designed loss functions for probabilistic and non-probabilistic conditions by assessing the differences between images in two inference processes.
The authors claim that they have achieved SOTA performance on both objective and subjective metrics.

### Strengths
I appreciate the motivation behind this paper, and I believe the method presented is quite sound.

### Weaknesses
1. We found that the loss function proposed in this paper can lead to artifacts, such as the linerart in Fig 3. The proposed method can achieve alignment between the outputs and the conditions, but the authors do not discuss how to maintain the visual plausibility of the generated results while ensuring this alignment. Specifically, the method seems to prioritize condition alignment over image quality, leading to noticeable distortions when the condition itself is not of high quality. This raises concerns about the robustness of the method when dealing with imperfect or noisy conditions.

2. In Tab.5a, there seems to be no clear evidence of what the optimal value of delta t is. We hope the authors can further discuss the choice of delta t. I am curious about why a relatively small delta t (1% of total 1000 timesteps) can encourage the diversity of generated samples. The lack of a clear explanation for this parameter's behavior makes it difficult to understand the underlying mechanism of the proposed method. A more rigorous analysis of how different delta t values affect the generated samples is needed.

3. From Fig.2, it can be seen that the gradient obtained from 2 different timesteps is back-propagated, and the parameters of the UNet will be also optimized. We hope the authors can provide some discussion on the training computational cost. Have the authors tried to only optimize the parameters of the control net?

4. This point does not affect our rating, but we want to know why the ControlNet method on SDXL in Tab.1 performs significantly worse than on SD1.5.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
