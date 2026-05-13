# ControlMM: Controllable Masked Motion Generation

- Decision: Reject
- Scores: 6, 6, 6, 6, 5

## Abstract
Recent advances in motion diffusion models have enabled spatially controllable text-to-motion generation. However, despite achieving acceptable control precision, these models suffer from generation speed and fidelity limitations. To address these challenges, we propose ControlMM, a novel approach incorporating spatial control signals into the generative masked motion model. ControlMM achieves real-time, high-fidelity, and high-precision controllable motion generation simultaneously. Our approach introduces two key innovations. First, we propose masked consistency modeling, which ensures high-fidelity motion generation via random masking and reconstruction, while minimizing the inconsistency between the input control signals and the extracted control signals from the generated motion. To further enhance control precision, we introduce inference-time logit editing, which manipulates the predicted conditional motion distribution so that the generated motion, sampled from the adjusted distribution, closely adheres to the input control signals. During inference, ControlMM enables parallel and iterative decoding of multiple motion tokens, allowing for high-speed motion generation. Extensive experiments show that, compared to the state of the art, ControlMM delivers superior results in motion quality, with better FID scores (0.061 vs 0.271), and higher control precision (average error 0.0091 vs 0.0108). ControlMM generates motions 20 times faster than diffusion-based methods. Additionally, ControlMM unlocks diverse applications such as any joint any frame control, body part timeline control, and obstacle avoidance. Video visualization can be found at \url{https://exitudio.io/ControlMM-page/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors of this work introduce ControlMM, an approach to text-to-motion generation that incorporates spatial control signals. ControlMM uses a pretrained motion tokenizer and a conditioned masked transformeras the first stage of generation. Next, it uses inference-time logit editing to refine control precision, enhancing the control precision.

### Strengths
* The problem of spatially controllable text-to-motion generation is an important and difficult problem. 
* Results look impressive.
* Proposed methods supports a wide range of downstream applications.

### Weaknesses
 * I found the write-up challenging to follow due to inconsistent notation in some sections and unexplained terms. The figures are also quite small with small fonts that are hard to read. They also don’t provide much additional insight. Additionally, certain details about the method are deferred to later sections, which disrupts readability. As someone less familiar with discrete latent motion representations, I needed to revisit the original MMM paper (Pinyoanuntapong et al., 2024) to understand the paper, but I still have questions about the approach. I believe the write up will benefit from further refinement in eloborating on the details of the approach and clear referencing to previous works if need be (e.g. following X, we represent Y as Z).
* In addition, one of my concerns is that authors seem to be down-playing the importance and influence of previous works which are the building blocks of the current proposed paper. After digging deeper into the paper, it looks to me as this work is using the Masked Motion Models while adding support for spatial constraints via the ControlNet mechansim. Then some additional components and tricks are applied to make the model even more effective. Despite all this, the write up seems to avoid clearly mentioning the source of the building blocks and that the works is incremental. This is one of main contributors of the lack of readability as important details are missing, but not referenced.

### Questions
1. There are minor typos in the text; e.g. "inference-timelogits" in line 145.
2. Figure 3 and Figure 4 are too small with very small font for the text, making it very difficult to read. If the figure doesn't fit the width of the text, maybe you should try to break it down into multiple components. I personally found the figures in the Masked Motion Models paper [Pinyoanuntapong et al., 2024] more helpful.
3. In Equation 1, what is $\mathbf{e}$? After reading the VQ-VAE paper, I understand that it's the tokenized embedding but this must be clarified for the general audience for improved readability.
4. In Equation 2, what is $L$? Also, from the description provided in the paragraph above Equation 2, it seems like $x_i$ is the $i$-th component of the quantized motion. But $x_i$ was previously used to represent the original motion frames in line 167. This choice of notation is confusing and I suggest either changing it, or emphesizing that these are different.
5. In lines 184-188, inference time iterations are discussed for the very first time. But it is very confusing as what these "iterations" really are after reading these lines. I would recommend either moving these lines to Section 3.3 entirely, or adding an overview of what the inference algorithm looks like in high level, and then adding lines 184-188 as follow-up detail.
6. To enhance understanding, I recommend adding the inference algorithm in the supplementary material.
7. The description of the motion representation (root positions or rotations) and whether and how it affects the proposed approach is also valuable. This needs to be added to the supplementary material.
8. I appreciate the quantitative and qualitative comparisons with recent diffusion-based methods of OmniControl and GMD. CondMDI (Cohan et al., 2024) is a more recent work that has improved performance over these two baselines. I am curious to where this work stands in the comparisons, and I believe it should be mentioned in the related work section.
9. In page.4, it says " We design a masked transformer
architecture to learn the conditional motion token distribution. This is the first attempt to incorporate
the ControlNet design principle (Zhang et al., 2023b) from diffusion models into generative masked
models, such as BERT-like models for image, video, language, and motion generation (Devlin et al.,
2019; Chang et al., 2022; 2023; Villegas et al., 2022)". I believe I've seen the same technique used in OmniControl, where they call the approach realism guidance. Particularly, similar to your suggested approach, they create a trainable copy of all the attention layers and connect them to the original corresponding layers using zero-initialized linear layers. Can you please alaborate on if and how the explained realism guidance is different from your suggested approach?

### Soundness
4

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
4

### Summary
Text-driven human motion generation has received attention but faces challenges in precise spatial control. Existing controllable motion generation models have difficulties in generating high-fidelity motion with real-time inference and handling both sparse and dense spatial control signals. This paper presents an interesting and innovative approach to controllable text-to-motion generation. The proposed ControlMM method shows promising results in terms of motion quality, control precision, and generation speed, outperforming existing state-of-the-art methods in many aspects.

### Strengths
1. This paper achieves real-time, high-fidelity, and high-precision controllable motion generation. Besides, it outperforms state-of-the-art methods in motion quality (better FID scores) and control precision (lower average error).
2. This paper ntroduces masked consistency modeling and inference-time logit editing. Masked consistency modeling ensures high-fidelity motion generation and reduces inconsistency between input and extracted control signals. Inference-time logit editing allows for better control precision and enables new control tasks.
3. This framework generates motions 20 times faster than diffusion-based methods.
4. Based on this design choice, it enables a wide range of applications such as any joint any frame control, body part timeline control, and obstacle avoidance.

### Weaknesses
1. The model's architecture and training process appear to be relatively complex. The use of multiple components and techniques may make it difficult for other researchers to understand and implement the model. A more detailed and intuitive explanation of the model's inner workings could be beneficial for reviewers.

2. While the paper mentions some handling of out-of-distribution situations in the context of body part timeline control, it is not clear how well the model would perform in more extreme or unforeseen out-of-distribution cases. This could be a potential limitation in real-world applications where the input data may deviate significantly from the training data.

3. The reliance on pretrained models (e.g., MoMask) may limit the model's adaptability and performance in some cases. If the pretrained models have biases or limitations, these could be carried over to the ControlMM model. It would be interesting to see if the model can be trained from scratch or with different pretrained models and still achieve similar performance.

### Questions
1. Provide a more detailed and intuitive explanation of the model's architecture and training process. This could include visualizations or step-by-step breakdowns of how the different components interact to generate motions.
2. Conduct more experiments to test the model's robustness in handling a wider range of out-of-distribution data. This could involve creating synthetic datasets with more extreme variations or using real-world datasets from different domains to evaluate the model's performance.

### Soundness
2

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an approach, namely ControlMM, for controllable motion generation. ControlMM is based on a generative masked motion model. A ControlNet-like controlling module is introduced to inject spatial guidance. Additionally, inference-time logits and embedding optimization are proposed to reinforce the spatial control signal as post-processing. Extensive experiments are performed to show the sota performance on motion generation and control ability.

### Strengths
+ The ControlNet-like design is first used in the masked generation model, which is interesting and inspiring.
+ The inference-time optimization has reasonable performance on control joint error. More impressively, the generation quality during optimization does not drop.
+ The overall performance is good compared with baseline methods.

### Weaknesses
 - My biggest concern is that from the ablation study, the motion control module along does not seem to perform well. In fact, from table 3, the fifth variation has the second worst trajectory error. Only using inference-time optimization on a vanilla motion generation model achieves better trajectory error. This undermines the contribution of the controlnet-like motion control module.
- Correct me if I am wrong, but OmniControl does not seem to use any inference-time optimization for better control accuracy. Therefore, the comparison seems not fair. 
- Minor Writing Issues:
1. Line93: i.e. => \textit{i.e.},
2. Line94: Control => control
3. Line101: use \citep

### Questions
See my comments in the weaknesses section. If my concern towards the effectiveness of the motion control module can be addressed, I would consider raise the rating.

### Soundness
3

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
4

### Summary
This paper presents ControlMM, a framework for integrating spatial control signals into a masked motion model. The main innovations focus on two aspects: (1) Masked Consistency Modeling to ensure high-fidelity motion by minimizing inconsistencies between input control signals and generated motion, and (2) Inference-time Logit Editing to enhance control precision and facilitate tasks like obstacle avoidance without retraining. The experimental results show that ControlMM delivers strong performance in motion quality, control accuracy, and generation speed, while supporting diverse applications, such as arbitrary joint and frame control and body part timeline control.

### Strengths
1. This paper extends the ControlNet concept from a diffusion-based framework to a mask generation framework. In addition, the Inference-time Logit Editing feature is presented as an innovative contribution.

2. The paper presents the methodology in a well-organized and accessible way, making both the theoretical framework and implementation details easy to understand.

3. The paper provides extensive experiments to validate the performance of ControlMM. These include comparisons with other models and ablation studies that highlight the contributions of specific components (e.g., masked consistency modeling, logit editing).

### Weaknesses
1. While the paper conducts extensive experimentation on large datasets like HumanML3D, it does not explore how the model performs under data-constrained scenarios. Many other studies in the field validate their models on smaller datasets, such as KIT, which provide insights into the robustness of models in resource-limited settings.

2. Although the paper compares ControlMM with several state-of-the-art models, such as OmniControl and GMD, it lacks comparisons with MoMask—an earlier exploration of the motion mask generation framework. Including this comparison in Table 1 is essential, as MoMask forms the baseline upon which ControlMM’s controllability innovations build. Clarifying the specific contribution of ControlMM to the improvement of the masked generation framework would provide a more complete evaluation.

3. While the paper provides strong quantitative results, it lacks qualitative user studies similar to those conducted in other works, such as MLD [2]. Furthermore, the paper relies heavily on specific joint control during both training and testing. It is unclear how the system would determine which joint information to use for control in practical applications, where such data may not be known in advance. This reliance on ground truth joint data during testing raises concerns about the practical applicability of the method.

### Questions
1. We noticed that the paper relies heavily on specific joint control during both training and testing. Could you clarify whether this joint control data is also used during test set validation? If so, would this constitute a data leakage issue? Additionally, how would the system determine which joint information to use for control in practical applications, where such data may not be known in advance?

2. As a generative model, ControlMM’s performance should not only be assessed on quality and controllability but also on diversity. Can the authors provide additional qualitative or quantitative examples that showcase the diversity of generated motions under the same control constraints (e.g., identical control signals and prompts)? This would help demonstrate that the model can generate varied outputs without overfitting to specific patterns.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a controllable motion generation model, which supports joint, obstacle, and timeline controls. The key technical contributions claimed in this paper are the mask consistency training and the latent optimization during inference. The experiments verify the effectiveness of the method.

### Strengths
The experiments verify the effectiveness of the method. 

The videos are provided on the website.

### Weaknesses
The writing quality of this work should be significantly improved. For example, the citation format in L112 should be revised. The writing of the method is very hard to read, especially the notation system. For example, the notations $l$ in Eqn. 6 is not well specified. 

Despite these, my main concern lies in the technical contribution. The method part seems to show something like "a bag of tricks". The key components are logit editing, codebook editing, and controlnet. The controlnet of controllable motion generation is first introduced by MotionLCM, which is not very novel to me. The ablation in Table 3 (L1 vs. L5) shows the control module performs not very well. This might be the reason for introducing the other two tricks. From the alation, it seems that embedding editing is the main component for editing precision (L1 vs L3). Therefore, the separate sub-components are not all effective enough. 

I also have some concerns about the evaluation. The authors miss two latest baselines, TLControl and MotionLCM. The method requires inference optimization, which introduces more time. The efficiency is not well discussed in the main text. Besides, the generation quality is not reported in the main text, which is a simple baseline for comparison. Besides, whether the optimization in the latent space has some issues about the over-fitting or not is not well discussed. How are the parameters determined? 

As shown in the demo website, some of the motions jitter a lot. Some of motions are not continuous. (e.g., "A figure walks forward in a zig zag pattern", "person is walking as if injured", "a person walks forward carrying something", "A person walks forward, casually greeting others with a wave or hello") Is this owing to the latent optimization of the method?

### Questions
see weakness

### Soundness
2

### Presentation
1

### Contribution
2
