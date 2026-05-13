# CAR: Controllable Autoregressive Modeling for Visual Generation

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Controllable generation, which enables fine-grained control over generated outputs, has emerged as a critical focus in visual generative models. 
    Currently, there are two primary technical approaches in visual generation: diffusion models and autoregressive models. Diffusion models, as exemplified by ControlNet and T2I-Adapter, offer advanced control mechanisms, whereas autoregressive models, despite showcasing impressive generative quality and scalability, remain underexplored in terms of controllability and flexibility.
    In this study, we introduce \textbf{C}ontrollable \textbf{A}uto\textbf{R}egressive Modeling (\textbf{CAR}), a novel, plug-and-play framework that integrates conditional control into multi-scale latent variable modeling, enabling efficient control generation within a pre-trained visual autoregressive model.
    CAR progressively refines and captures control representations, which are injected into each autoregressive step of the pre-trained model to guide the generation process.
    Our approach demonstrates excellent controllability across various types of conditions and delivers higher image quality compared to previous methods. 
    Additionally, CAR achieves robust generalization with significantly fewer training resources compared to those required for pre-training the model. 
    To the best of our knowledge, we are the first to propose a control framework for pre-trained autoregressive visual generation models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes controllable autoregressive modeling (CAR), a conditional control module for VAR image generation. Following VAR, CAR adds control to pretrained model with multi-scale latents in a progressive manner. Experiments on multiple conditional generation task show competitive performance of CAR over baselines include T2I-Adapter and ControlNet.

### Strengths
1. The motivation and formulation of the work is clear, namely investigating conditional control of AR image generation model. 
2. The model show competitive performance on various conditional generation tasks. 
3. The paper is clearly written and easy to follow.

### Weaknesses
Two major concerns of this work:
1. The model follows VAR which leverages multi-scale latents in generation. This greatly limits the application to broader autoregressive image generation models, where no multi-scale latent is used. 
2. The other concern is the computational overhead has not been properly reported. The Transformer module in CAR is built with half of the parameters of original VAR, which can be expensive in training/inference.

### Questions
1. Can you authors provide more implementation details of baseline ControlNet and T2I-Adapter?
2. How does the training cost and convergence speed of CAR compared with baseline models?
3. How can CAR be applied to other AR generative models that don't use multi-scale tokens?
4. Also, how does it work if use small-sized CAR for large pretrained VAR model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the first control framework for autoregressive generation models, achieving controllability validated under various conditions like Canny, depth, and HED annotations. The results indicate effectiveness, but as I am not an expert in this specific domain, I am inclined to give **borderline acceptance** and look forward to other reviewers' feedback to ensure nothing has been overlooked.

### Strengths
1. The paper presents a novel contribution, as CAR is the first framework for controllable autoregressive image generation.
2. The analysis in Section 4.3 clearly shows that controllable autoregressive modeling functions effectively.
3. The presentation of the paper is well done, with clear equations, figures, and tables.

### Weaknesses
1. In Section 4.2 (line 643), the authors mention retraining T2I-Adapter and ControlNet but do not provide sufficient details about whether these models were trained with the same parameters and training time as CAR. Additionally, it is worth noting that both methods are based on diffusion models, which seems slightly unconventional. While there may not be directly comparable models, having a stronger baseline would be beneficial.
2. The supplementary material lacks extensive visualizations, with only source code provided. Additional visual results would enhance the paper's comprehensiveness.

### Questions
1. A minor question: In Figure 2, when using Canny as a condition (assuming $c$ represents Canny), is $c_1$  obtained by resizing? If so, does the Canny information retain its integrity after downsampling?

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
4

### Summary
This paper proposes CAR designed to adapt pre-trained AR-based image generation models with additional pixel-level controls. A fusion function and a transformer-based adapter are leveraged to inject control information into the original model. The proposed approach demonstrates superior performance compared to retrained ControlNet and T2I-Adapter.

### Strengths
- AR-based visual generation is popular.
- The proposed approach was tested with different control types.

### Weaknesses
- The "control token", "control map", and "control information" are mixed to describe $c_k$ which is very confusing.
- The model architecture (such as $\mathcal{F}$ and $\mathcal{T}$) is described in the experiment section making it hard to understand the workflow of the proposed approach.
- The proposed approach introduces $\mathcal{T}$ which has 0.5 #param of the original model + several fusion modules $\mathcal{F}$ making the model much larger compared to VAR.
- The author claimed that CAR is the first framework to adapt pre-trained AR-based image generation approaches to additional conditions. However, there exist previous approaches designed for AR models, such as Lumina-MGPT.
- The proposed approach is motivated by improving data and model efficiency. However, it costs 100 epochs on 10% of the ImageNet with a larger model with additional $\mathcal{F}+\mathcal{T}+\mathcal{G}$. The original VAR is just trained with 200-350 epochs.
- Only a few baseline methods (ControlNet and T2I-adapter) are compared. What about the performance compared to ControlVAR?
- The performance of the proposed approach is fair.

### Questions
- Only $r_k$ is discussed in Sec 3.1. How to obtain the control map $c_k$? Is it a quantized feature or a resized raw input?
- A comparison of the speed and model size against VAR is missing.
- I am curious about why is the model trained with an adapter-based approach instead of LORA.
- More qualitative results will be helpful in understanding the performance.

I initialed the rating as 3 and will increase it if my concerns can be well addressed.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a plug and play method for scale-based autoregressive conditional image generation.
The authors trains a side network to fuse and inject the conditional information into a pre-trained VAR.
The proposed method was trained on 100 categories and shows generalizable controllability on other classes.
The results shows superiority over T2I-Adapter and ControlNet.

### Strengths
* The paper is easy to follow. 
* The proposed method maintains the pre-trained VAR network unchanged, and is trainable with only 8 V100.
* Detailed ablation study over the network design is provided.

### Weaknesses
* Some important information is missing from the paper and there is no appendix to explain those points. See questions.
* The problem solved in this paper is same as in ControlVAR, yet it has not compared with this baseline method. In fact, the results from ControlVAR is better than this paper. 
* Derivation of eq 3 is not obvious and not detailed information.

### Questions
1. What are the number of parameters of the proposed fusion function, transformer, and injection function?

2. What are the flops of the proposed method compared to ControlVAR. From current results, there is no demonstration of efficiency as claimed in the paper. While the authors showed in Table 1 that the inference time is faster than T2I-Adapter and ControlNet, I believe this mainly comes from the benefits of VAR over diffusion models.

3. What is the scalability of the proposed method over the number of data. Why 100 categorizes are chosen? Does the method work for less classes? Does the method work for more classes?

### Soundness
3

### Presentation
2

### Contribution
2
