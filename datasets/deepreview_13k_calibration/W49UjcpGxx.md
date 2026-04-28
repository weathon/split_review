# FasterCache: Training-Free Video Diffusion Model Acceleration with High Quality

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
In this paper, we present \textbf{\textit{FasterCache}}, a novel training-free strategy designed to accelerate the inference of video diffusion models with high-quality generation. By analyzing existing cache-based methods, we observe that \textit{directly reusing adjacent-step features degrades video quality due to the loss of subtle variations}. We further perform a pioneering investigation of the acceleration potential of classifier-free guidance (CFG) and reveal significant redundancy between conditional and unconditional features within the same timestep. Capitalizing on these observations, we introduce FasterCache to substantially accelerate diffusion-based video generation. Our key contributions include a dynamic feature reuse strategy that preserves both feature distinction and temporal continuity, and CFG-Cache which optimizes the reuse of conditional and unconditional outputs to further enhance inference speed without compromising video quality. We empirically evaluate FasterCache on recent video diffusion models. Experimental results show that FasterCache can significantly accelerate video generation (\eg 1.67$\times$ speedup on Vchitect-2.0) while keeping video quality comparable to the baseline, and consistently outperform existing methods in both inference speed and video quality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a training-free feature caching strategy for video diffusion models, named FasterCache, that improves how features are reused for accelerating inference. Instead of directly reusing the adjacent-step features as in previous works, FasterCache interpolates the neighboring features to efficiently synthesize features for the missing steps. In addition, the paper introduces CFG-Cache, which aims to effectively reuse the conditional outputs for computing the unconditional outputs. Experimental results demonstrate notable visual quality and efficiency improvements compared with the existing methods.

### Strengths
1. The paper clearly demonstrates the motivation and the problem of existing works with illustrative examples (Fig. 3-7). Overall, the limitations of vanilla cache-based acceleration methods with CFG is analyzed very thoroughly.

2. Qualitative results demonstrate notable improvements in visual details and the spatio-temporal consistency of the generated frames.

### Weaknesses
1. Slightly missing justifications for the design choices of the proposed method. For instance, is the linear interpolation strategy sufficient for dynamically building the missing features? Are there any other options that the authors have considered? Using the proposed Dynamic Feature Reuse, how similar are the computed features compared to the existing caching methods? (Please guide me if I missed the descriptions)

2. Limited video-specific contributions. The proposed methodologies seem to applicable to any image diffusion model, of which comparison to previous works is missing, and I could not find any video-related novelties proposed. The notation $t = \{1 ... T\}$ in Equations seem to denote the diffusion sampling steps, and I think there is no notation for the temporal axis? Please correct me if I misunderstood any equations.

3. (Minor) Figure captions are not very descriptive. I would suggest to include the main points (Fig. 2, 8) or where to focus on (qualitative figures).



### Questions
1. For CFG-Cache, should we interpret the feature differences in the frequency domain in a similar way as MSE? 

2. In Figure 7b, it seems to me that low-frequency components do not gradually shift into high-freq as the authors mention in L300-301, since the high-freq components differ both at the beginning and near the end. What kind of insights can we gain from this analysis?

3. In the experiments, PAB seems to significantly outperform $\Delta-DiT$, but there are no PAB results for CogVideoX and Vchitect. Also, why is the performance of $\Delta-DiT$ so low? Is it because of the inherent randomness of image diffusion models?

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
This paper presents an innovative approach to accelerate video diffusion models without sacrificing quality. By analyzing existing cache - based methods and classifier - free guidance (CFG), the authors identify limitations and redundancies. They introduce FasterCache, which includes a dynamic feature reuse strategy for attention modules and CFG-Cache. The dynamic feature reuse strategy adjusts features across timesteps, maintaining distinction and continuity. CFG-Cache optimizes the reuse of conditional and unconditional outputs. Experimental results on multiple video diffusion models demonstrate significant acceleration while keeping video quality comparable to the baseline, outperforming existing methods.

### Strengths
In terms of originality, the proposed FasterCache method is highly innovative. It combines a dynamic feature reuse strategy that considers subtle differences between adjacent timesteps and a CFG - Cache component for handling conditional and unconditional outputs in a novel way. This is a departure from existing methods and reveals new acceleration opportunities through a pioneering investigation of classifier - free guidance (CFG). 

Regarding quality, a thorough analysis of existing cache - based methods and CFG is provided. This includes identifying problems and limitations, and conducting in - depth investigations into feature reuse and CFG outputs, which forms a solid foundation for the method. The experimental design is robust, with testing on multiple video diffusion models and the use of various evaluation metrics. Ablation studies further demonstrate the effectiveness of each component. 

For clarity, the paper has a clear structure, starting with an introduction to the problem and existing solutions, followed by a detailed description of the method in the methodology section. The experimental results are presented clearly, and the discussion and conclusions are well - organized. Complex concepts are explained accessibly, such as through diagrams and detailed descriptions of the key components. 

In terms of significance, the research has practical implications as it can reduce the time and computational resources required for video generation, which is important for applications like video content creation, virtual reality, and augmented reality. It also advances the field by filling gaps in existing research on video diffusion models, addressing limitations of current acceleration methods, and inspiring further studies on improving efficiency and performance.

### Weaknesses
Hyperparameter Explanation. Some of the hyperparameters used in the method, such as the weighting function are not explained in sufficient detail. Although default values are provided and it is mentioned that they work well for most models, a more in-depth discussion on how these hyperparameters are chosen and their impact on the performance for different datasets and models would make the method more reproducible and understandable. Specifically, the weighting function $w(t)$ in the dynamic feature reuse strategy is not justified with sufficient detail. The paper mentions a linear interpolation but does not explain why this choice is optimal or how it interacts with different video characteristics. Furthermore, the caching intervals for both the dynamic feature reuse and CFG-Cache are not thoroughly explored. The paper lacks a systematic analysis of how these intervals affect the trade-off between acceleration and video quality. The selection of $\alpha$ values in CFG-Cache also lacks a detailed explanation, making it difficult to understand their impact on the final results.

Uncertainty in complex scenes. The paper mentions that in complex scenes with substantial video motion, the method may occasionally produce degraded results. This may limit the practical applicability of the method once video generation model baselines are imporved and complex video content is common. More discussions refer to the Question 1.

Weak theoretical underpinning: The paper focuses more on the empirical evaluation and practical implementation of the FasterCache method. Although the experimental results are strong, the theoretical foundation behind some of the proposed techniques could be strengthened. For example, a more in-depth analysis of why the dynamic feature reuse strategy and CFG-Cache work as expected in different scenarios from a theoretical perspective would add more credibility to the method. Specifically, the paper provides a Taylor expansion to justify the dynamic feature reuse, but it does not discuss the limitations of this approximation, such as the assumption of smoothness and differentiability of the feature function $F(t)$. The theoretical justification for CFG-Cache also needs further elaboration. While the paper mentions the similarity between conditional and unconditional outputs, it does not provide a rigorous analysis of the conditions under which this similarity holds and how it affects the performance of the method.

### Questions
Questions:
1. Is the effectiveness of the Dynamic Feature Reuse Strategy because the videos generated by existing video generation methods are relatively smooth, with little difference between adjacent frames, e.g. fixed backgrounds? If so, once the motion of the video is large and the adjacent frames change greatly, then is the proposed method still effective?

2. Negative prompt will affect the quality of video generation, which generally improves it. So will CFG-Cache and the separation of high and low frequencies have an impact on negative prompt setting?

3. For Open-Sora-Plan, although FasterCache achieved an acceleration of 1.68x, the generated video has significant varying in pixel domain compared to the original one (PSNR 23.72). What is the reason for this bias? Blurriness, noise, or changes in semantic level?

4. Will the setting of g value in CFG formula 4 (Line 167) affect the performance of FasterCache?

### Soundness
2

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
This paper propose a training-free method for efficient video generation. Their method is based on the attention feature map and output redundancy observed in the forward pass of the denoising process. To this end, they propose to (1) use the feature map dynamics to restore the missing details in the previous naive feature map reuse method. (2) use the frequency difference to compensate the cached conditional output in CFG. The proposed method has been validated with several models and showed promising results.

### Strengths
- The paper is well-written and easy to read.
- The proposed attention feature map dynamics could be a generic method and applied into all other cache based efficient generation methods.
- the proposed frequency residual method for CFG is novel and seems also a generic method that can be applied into CFG for all diffusion based image/video generation models.

### Weaknesses
 - Distillation based efficient generation methods are less discussed and not added into the comparison. I can understand that this work mainly focused on the cache based method. But:
  - What's the delta of this method compared to distillation based method?
  - Are they compatible to each other? If not, in real world applications, which method we need to use?

- the overall method seems to perform better than all other methods. What's the contribution of each individual method? What the cost of additional computation in each individual method?

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method to accelerate the computation for video diffusion models. Based on the observation that adjacent-time features exhibit subtle differences,  the authors propose a dynamic feature reuse scheme. Based on the observation that the conditional and unconditional generation features have strong similarity in CFG, the authors propose a CFG-Cache scheme to save computations of unconditional stage.

### Strengths
this paper is relatively well organized and written.

### Weaknesses
this paper lacks novelty and insight. the proposed method is not solid in terms of logical and theoretical justification. the speedup of computation could be achieved using other methods.

On Motivation for Dynamic Feature Reuse: In Appendix A.3.2, there is a strong assumption "When ∆t is sufficiently small, the second-order term becomes negligible", which is quite strong. Basically you are assuming that the signal change between adjacent time steps is linear, which lacks evidence in theory and statistics.

On Motivation for CFG-Cache: In Appendix A.3.2, the same strong assumption "we find that when ∆t is sufficiently small, the ϵ can be considered negligible" should be justified. In Figure 14, that specific example indicates that the conditional and unconditional outputs themselves are high-frequency signals at later stages of diffusion. So I wonder does it necessary to add a time-varying weighting mechanism? I have not seem a ablation study on this issue.

In Fig. 13 (c), the second-order component is of range around 0.01, while the first-order component is of range around 0.03, so that the second-order term is not a term that can be considered negligible. Moreover, in Fig. 13 (d), the authors only compared the approximation error but not the ultimate generation quality. After all, a smaller term in approximation could have a large impact on the performance of generation.

In Table 3, does the performance of "CFG-Cache w/o Enhancement" include FR? Is it unfair to compare "Vanilla FR" and "Full (w/ Dynamic FR) " as the later include CFG-Cache?

"there are still noticeable differences between them, which remain relatively stable (Fig. 5, right).": this is just one specific example (moreover, without numerical measurement of similary), which cannot lead to a solid justification.  

"This bias term essentially estimates the error between the cached feature from the previous timestep and the current feature, as discussed in Appendix A.3.1." : similar to my previous comment, the key assumption that quadratic and higher-order terms can be omitted is strong, and there is no analysis on the error bound and optimality of this estimator.

My concerns remain unresolved.

### Questions
1. what is the reason of using equation (5) for feature reuse? it seems to be quite heuristic.
2. why in cfg, the similarity of two stages has such a wired characteristics (time-varing low and high frequency similarity)? there should be more analysis and insight.
3. in terms of saving the computation of unconditional stage, how about existing and well-adopted methods such as "On Distillation of Guided Diffusion Models"? 
4. how does your method work with video generation models using flow matching?

### Soundness
3

### Presentation
3

### Contribution
2
