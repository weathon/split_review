# T2V-Turbo-v2: Enhancing Video Model Post-Training through Data, Reward, and Conditional Guidance Design

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
In this paper, we focus on enhancing a diffusion-based text-to-video (T2V) model during the post-training phase by distilling a highly capable consistency model from a pretrained T2V model. Our proposed method, \modelname, introduces a significant advancement by integrating various supervision signals, including high-quality training data, reward model feedback, and conditional guidance, into the consistency distillation process. Through comprehensive ablation studies, we highlight the crucial importance of tailoring datasets to specific learning objectives and the effectiveness of learning from diverse reward models for enhancing both the visual quality and text-video alignment. Additionally, we highlight the vast design space of conditional guidance strategies, which centers on designing an effective energy function to augment the teacher ODE solver. We demonstrate the potential of this approach by extracting motion guidance from the training datasets and incorporating it into the ODE solver, showcasing its effectiveness in improving the motion quality of the generated videos with the improved motion-related metrics from VBench and T2V-CompBench. Empirically, our \modelname establishes a new state-of-the-art result on VBench, \textbf{with a Total score of 85.13}, surpassing proprietary systems such as Gen-3 and Kling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents T2V-Turbo-v2, a method that enhances a diffusion-based text-to-video model by distilling a consistency model using high-quality training data, reward model feedback, and conditional guidance. The approach achieves state-of-the-art performance on VBench, demonstrating improved text-video alignment and motion quality through tailored datasets, diverse reward models, and optimized guidance strategies

### Strengths
The results appear promising and solid.

The experiments are thorough.

The writing is easy to follow.

### Weaknesses
The method combines existing techniques such as consistency distillation and motion guidance, so its novelty is somewhat limited.

VideoCrafter uses a 2D+1D decoupled spatial-temporal approach, whereas most recent advanced methods employ full 3D attention. How would motion guidance be applied when using 3D attention? Specifically, the method relies on a decoupled approach to apply motion guidance, but it's unclear how this would translate to models that use a full 3D attention mechanism where spatial and temporal information are processed jointly. The paper does not provide sufficient detail on how the motion guidance would be adapted to these architectures, which is a significant limitation.

What is the peak training cost, such as peak GPU memory, compared to training a single model? How does it perform on less powerful video diffusion models like Zeroscope—can it still achieve results comparable to VideoCrafter?

### Questions
Please see the weakness part.

### Soundness
3

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
4

### Summary
This paper introduces T2V-Turbo-v2, an improved text-to-video model that enhances video generation by distilling a consistency model from a pretrained T2V model during the post-training phase. The method integrates multiple supervision signals—including high-quality training data, reward model feedback, and conditional guidance—into the consistency distillation process. Experiments show a new state-of-the-art result on VBench.

### Strengths
1. The paper is well-organized and easy to follow. 
2. The method employing motion guidance is logically sound, and the experimental results showing improved semantic scores effectively validate its effectiveness.

### Weaknesses
1. The early work Energy-guided stochastic differential equations[1] first present a framework that utilize an energy function to guide the generaion process for diffusion model. Please cite this paper.
2.	In Figure 2, does the DDIM inversion require k forward passes for each training step? If so, does this introduce excessive computational cost?
3.	Please provide .mp4 files for visual comparisons, as Vbench cannot fully substitute for a user study. Including video files will allow reviewers and readers to better assess the performance and quality of the proposed method.

### Questions
See weakness.

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
3

### Summary
This paper introduces T2V-Turbo-V2, aiming at improving the video quality and alignment with prompts by focusing the post-training phase. It distills a pre-trained T2V model using various supervision signals, including, 1. the reward models feedback from pre-trained vision language models (CLIP and InternV2) for both image and video levels. 2. the self-consistency loss used in many other distillation models, and injecting the classifier-free guidance and energy function into the self-consistency loss. 
This paper also optimize the data preprocessing and the reward feedback, allowing the T2V-Turbo-V2 to achieve the state-of-the-art results on the Bench and outperform previous models like VideoCrafter2, Gen-3, and Kling.

### Strengths
1. The model achieves high scores across multiple metrics and outperforms proprietary systems, demonstrating the effectiveness of proposed modules.
2. T2V-Turbo-V2 introduce an effective post-training process to enhance video quality and prompt alignment, and this process if architecture agnostic, potentially can be used on other pre-trained video generation models.
3. This paper provide detailed ablation studies on various factors like the dataset selection, reward model configurations, the effectiveness of motion guidance, and so on.

### Weaknesses
1. The model appears optimized for single-caption, short-context prompts, its ability to generate longer or more complex video context may be limited.
2. When generating the dataset for the motion guidance, it may require considerable computation resources.

### Questions
1. What are the evaluation datasets when comparing the T2V-Turbo-V2 with the SOTA methods (Table 1)?
2. Since both the OV and VG dataset contain the high visual quality data, and the Quality Score is high when only using OV, it seems that OV is a good dataset to improve the visual quality, I want to know  the metrics of using OV + VG and OV + VG + WV (in Table 2 setting) and why the author does not use the OV dataset?
3. For the motion guidance, how the values of  λ, τ were chosen?
4. Can the author give more details on the dataset processing, like the needed computation resource?
5. If replace the base pre-trained video generation model with other models, can the T2V-Turbo-V2 method still achieve good results?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper present motionclone-based consistency distillation, using motion guidance to improve temporal and spatial coherence.

### Strengths
1. This method demonstrates strong performance, achieving state-of-the-art (SOTA) results on VBench. Visualized video outputs appear smooth and high-quality, reflecting its effective design.

2. The paper is clearly written, allowing reviewers to easily understand the authors' intent.

3. This method is simple and effective, making it generally more practical.

### Weaknesses
This method is overly engineering-focused and lacks novelty, as the motion guidance and consistency distillation techniques involved are already established, making it appear less innovative.

Additionally, while it conducts extensive ablation experiments on motion guidance and reward models, this does not constitute a significant contribution of the paper. I am unclear about the paper's contributions; is it providing more interesting insights? It would be helpful if the authors could briefly summarize this in their response.

Regarding the contribution summary of the paper (L117), it seems to emphasize the advantages of existing work and the potential of extracting motion priors. And, I do not see any strong insights that stand out; motionclone has already demonstrated this fairly clearly. If the authors mean that motion priors are particularly useful during T2V training, they should provide more experiments. For example, training SVD and VideoCrafter2 shows that the insights presented in T2V-Turbo are quite limited.

### Questions
1. I’m curious why this method, although based on distilling VideoCrafter2, outperforms VideoCrafter2 across multiple tasks, such as in the three metrics shown in Table 1.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In the paper, the authors present T2V-Turbo-v2, a method to enhance diffusion-based text-to-video models by distilling a consistency model from a pre-trained T2V model. This approach integrates high-quality training data, feedback from multiple reward models, and motion guidance into the distillation process. Through ablation studies, it emphasizes the importance of high-quality datasets and diverse reward models to improve visual quality and text-video alignment. The method also verifies the effectiveness of incorporating motion guidance to enhance video motion quality. T2V-Turbo-v2 achieves a state-of-the-art total score of 85.13 on VBench, outperforming advanced text-to-video models like Gen-3 and Kling.

### Strengths
1. The experiments are comprehensive and thorough, with detailed analysis.
2. The analysis of minimizing CD loss using entire datasets while restricting reward optimization to short-captioned datasets is interesting and meaningful, which may encourage future work.
3. This paper establishes a new SOTA total score on VBench, leveraging open-source models to outperform some advanced text-to-video models.
4. The paper is well-written and easy to understand.

### Weaknesses
1. The integration of MotionClone into T2V-Turbo is an interesting direction. However, while the contribution highlights the potential for diverse forms of energy functions, this study primarily utilizes the motion representation from the MotionClone work without substantial modifications to the energy function's format. The other enhancements are relatively minor, such as the reward model used, which only adds a CLIP compared to T2V-Turbo, and the removal of the EMA model. It might be beneficial to explore further variations to strengthen the contribution.
2. It would be beneficial to include a discussion on the performance differences between VCM and the proposed method across various datasets. For instance:
    - Could you explore why VCM achieves the best performance using only OV, while the proposed method does not attain similar results? It appears that different methods may lead to varying conclusions regarding dataset choices. Additionally, how would the results differ if T2V-Turbo (not v2) was used?
    - Considering OV and VG are both high-quality video datasets, it would be insightful to analyze why OV+WV exhibits poorer performance compared to VG+WV, which performs quite well.
3. In the section on data preprocessing, the approach involves using DDIM Inversion on all videos to obtain the necessary motion guidance for training, which is effective in reducing training time. Nevertheless, this approach does not significantly simplify the overall complexity. It would be better to explore improvements to the motion guidance strategy itself to enhance training efficiency.
4. It would be valuable to include theoretical or experimental results to analyze why the EMA model in consistency distillation is unnecessary.
5. It would be better to conduct a user study to further verify the performance from a human perspective.

### Questions
1. The pseudo-code in Algorithm 2 for training includes theta-, but the method states that EMA is not needed. Please update either the text or the algorithm to ensure consistency.

### Soundness
4

### Presentation
3

### Contribution
3
