# TexTailor: Customized Text-aligned Texturing via Effective Resampling

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We present TexTailor, a novel method for generating consistent object textures from textual descriptions. Existing text-to-texture synthesis approaches utilize depth-aware diffusion models to progressively generate images and synthesize textures across predefined multiple viewpoints. However, these approaches lead to a gradual shift in texture properties across viewpoints due to (1) insufficient integration of previously synthesized textures at each viewpoint during the diffusion process and (2) the autoregressive nature of the texture synthesis process. Moreover, the predefined selection of camera positions, which does not account for the object's geometry, limits the effective use of texture information synthesized from different viewpoints, ultimately degrading overall texture consistency. In TexTailor, we address these issues by (1) applying a resampling scheme that repeatedly integrates information from previously synthesized textures within the diffusion process, and (2) fine-tuning a depth-aware diffusion model on these resampled textures. During this process, we observed that using only a few training images restricts the model's original ability to generate high-fidelity images aligned with the conditioning, and therefore propose an performance preservation loss to mitigate this issue. Additionally, we improve the synthesis of view-consistent textures by adaptively adjusting camera positions based on the object's geometry. Experiments on a subset of the Objaverse dataset and the ShapeNet car dataset demonstrate that TexTailor outperforms state-of-the-art methods in synthesizing view-consistent textures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes TexTailor, a method for text-to-texture synthesis utilizing an inpainting approach to achieve view-consistent textures. To address common challenges in texture generation, TexTailor introduces a resampling scheme and fine-tuning to maintain texture consistency across viewpoints. Furthermore, it employs adaptive viewpoint refinement for efficient viewpoint sampling.

### Strengths
1. The paper proposes TexTailor to address view-consistent texture synthesis by combining inpainting with resampling and fine-tuning.
2. Method and results are presented clearly and logically, making the paper easy to follow.

### Weaknesses
1. While effective, the approach primarily combines existing techniques, with limited emphasis on novel contributions. The paper could be strengthened by enhancing the resampling scheme or accelerating the fine-tuning phase.

2. While the paper discusses performance preservation loss qualitatively, a quantitative analysis of its impact on quality would clarify its specific role. Including an ablation study of the performance preservation loss in Table 2 could better highlight its contribution to TexTailor’s performance.

3. Since the viewpoint refinement uses a fixed threshold, how sensitive is the model’s performance to changes in this parameter?

### Questions
1. Could the authors clarify the novel aspects of TexTailor? The current version of TexTailor appears to be a combination of existing methods. It would be helpful if they could elaborate on any unique modifications within the resampling scheme or improvements made to accelerate the fine-tuning process.
2. While the paper discusses performance preservation loss qualitatively, a quantitative analysis of its impact on quality would clarify its specific role. Including an ablation study of the performance preservation loss in Table 2 could better highlight its contribution to TexTailor’s performance.
3. Since the viewpoint refinement uses a fixed threshold, how sensitive is the model’s performance to changes in this parameter?

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
4

### Summary
This paper introduces a method for text-driven 3D object texturing. Previous work on this important topic fail in some areas, according to the paper, including: Consistency and the gradual change in textures assigned to the object. The paper aims to solve these issues, by introducing 2 ideas: First, the model leverages a resampling scheme for better integration of previously generated texture during the diffusion process, and second, the model fine-tunes a depth-aware diffusion model with these resampling textures. With these contributions, the method is said to achieve higher quality and consistency than previous work, measured on a set of datasets and perceptual metrics.

### Strengths
- This paper adequately identifies problems in previous methods for text-driven object texturing, including lack of texture consistency and graduality in texture changes. The origin of this problems are identified as being caused by insufficient integration, predefinition of camera positions, and autorregresion. The paper introduces changes to these methods, to enhance their quality and consistency. This is an important line of research, as these works are becoming more prevalent in the literature and industrial applications. 
- This paper tackles an important and salient problem in the literature. 
- The results shown in the paper indeed suggest that the proposed method provides less gradual changes in texture properties. In objects with different parts, TexTailor shows superior performance in assigning different texture to different parts, than previous work do. 
- The proposed method is sound, and the ideas proposed here are very well suited for the task the paper is aiming to solve. In this sense, the paper is correct as far as I am familiar with the literature and the problems in 3D content generation.
- This paper is well written and easy to follow. The problems identified in previous work are clearly stated, and the ideas to solve them are easy to understand and very well explained. 
- Code is provided as a supplementary material, which should greatly enhance reproducibility.

### Weaknesses
 - While sound, the ideas introduced in this work are somewhat limited in scope and the paper fails to be compelling that they are particularly effective. In this sense, I am not convinced about the extent upon which these contributions will be impactful in the literature. Furthermore, the resampling scheme introduced in this paper is not new, as it is borrowed from previous work. Therefore, the ideas introduced here are not particularly novel nor signficant.
- Insufficient results are shown on the paper. It is hard to understand the capabilities of the model with the amount of results shown here. In particular, only four results are shown in the comparisons on Objaverse, and these results are not particularly compelling (for example, in the hammer, the method assigns a metal texture to the handle and a wooden texture to the head, which is not correct and arguably a worse result than TEXTure). Only two results are shown in ShapeNet car, and the ablation study is shown exclusively on a single object. Significant more results should be provided to convince the reader that the method is more effective than previous work.
- I am unconvinced about the metrics used in this paper. While standard for 3D object texturing work, LPIPS and FID do not adequately measure text-to-image alignment. CLIP-based metrics should be used in conjunction to the ones shown in this paper, to be more informative about how well this model is generating results aligned with the prompts. While visually more consistent than previous work, this model seems to struggle more than previous methods (particularly TEXTure and Text2Text) in asigning the correct texture to each part of the object. This is not something that LPIPS and FID can measure correctly. 
- A user study should be provided for better comparisons between methods, across a bunch of dimensions, including alignment, realism, quality, consistency, etc. 
- The quantitative results are not particularly convincing. The ablation study does not show significant improvements across the metrics used, particularly LPIPS, and without standard deviations of the errors it is hard to understand whether the improvements are actually statistically significant. Therefore, the ablation fails to convince that the proposed contributions are actually valuable and effective. 
- No results are shown on 3D human avatar texturing, which is a very closely related and relevant line of work. 
- Related to the previous point, the analysis of the related work is lacking on a set of areas. The most relevant is the work on 3D human texturing. Relevant work include: SMPLitex: A Generative Model and Dataset for 3D Human Texture Estimation from Single Image (BMVC 2023), UVMap-ID: A Controllable and Personalized UV Map Generative Model (ACMMM 2024), TexDreamer: Towards Zero-Shot High-Fidelity 3D Human Texture Generation (ECCV 2024), etc. Besides, 2D texturing methods with generative models should also be included as part of the related work. 
- Limitations are not adequately addressed or discussed. From the paper, it seems like the only limitation of the proposed method is its computational cost. However, the results shown in the paper indicate that the method is by no means perfect and it struggles with consistently assigning the appropriate texture to different parts of the object, among other limitations. These should be mentioned more explicitly. 
- Contributions are very overstated. Sentences like "... demonstrate the superior performance of TexTailor in .... " or " ... surpases SOTA texture synthesis methods driven by language cues" should be empirically demonstrated or removed altogether.
- The paper suggests some reasons why previous methods fail (autorregressive inference, integration of previous information, fixed camera positions, etc), but it fails to provide adequate evidence that these actually limiting factors.

### Questions
- Can the authors provide a user study that measures consistency, alignment, quality, and realism? This should provide a better idea on the quality of the results on the actual goals that the paper aims to achieve. 
- I believe that computational costs should be compared more explictly with previous work, so as to better understand the quality/cost pareto frontier in this line of work.  
- I suggest the paper should provide a CLIP-guided text-image alignment metric. 
- I suggest the paper should provide a more upfront discussion of its limitations.
- The paper should include a detailed analysis of 2D texturing models.
- The paper should include a detailed analysis of text-to-avatar models, as well as quantitative and qualitative comparisons. 
- How does the model behave with non-diffuse objects? Very few glossy, metallic, or translucent objects are shown. 
- The paper should include many more results, at least in the supplementary material.
- Results should include standard deviations to better understand the differences between methods in terms of LPIPS, FLIP, etc.

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
4

### Summary
The paper focuses on **consistent texture synthesis**. The authors analyze the artifacts in the current approaches and propose a new approach, **TexTailor**, to keep synthesized textures consistent across different viewpoints. TexTailor equips with a resampling scheme for integrating previous textures, a finetuned depth-aware T2I model trained with performance preservation loss, and an adaptive viewpoint refinement strategy for inpainting. 

The authors evaluate the performance of TexTailor on a subset of Objaverse dataset, and showcases that TexTailor outperforms state-of-the-art methods.

### Strengths
## Motivation
The paper starts with an analysis of the limitations of previous methods. It hypothesizes those inconsistent results from previous methods are mainly coming from an inappropriate way of integrating information from previously synthesized textures. Given this agile insight, it tries to addresses the inconsistency issue by proposing a new approach to better use information across different viewpoints and previously synthesized textures. 

The motivation of the paper is more about a technical aspect. The analysis of previous approaches makes sense. 

## Method
- In Section 3.2, the problem of ControlNet for incorporating multi-views is interesting. 
- In Section 3.3, the analysis of setting viewpoints sounds interesting (Line 303-310). Using a proportion (Eqn. (12)) is an intuitive way. 

## Experiments
- TexTailor outperforms the previous methods in terms of view consistency and quality, as shown in Table 1. 
- The ablation study shows a progressive improvement of each component. 

The authors also show the limitation of TexTailor - the processing time could be further improved.

### Weaknesses
What concerns me the most in this paper is the motivation behind some technical parts and its unclear writing.

## Motivation
- In Line 93, it is not clear to me why finetuning a depth-aware T2I model matters. Maybe including a brief explanation could be helpful. 

## Method
- In Section 3.1, the authors propose a non-Markov process to reduce the sampling steps. However, the benefits of it is confusing to me. Would it involve a faster sampling speed? If it would, there is not result to support it. On the other hand, the authors mainly show the effects of resampling is to "preserve the texture properties" (Line 480). This makes me confused about the motivation of newly proposed resampling trick. 

## Experiments
- It does not make sense to me the authors choose to not compare with text-driven methods (Line 373-374) just because they have "difficulties" when optimizing textures for "cars". Wouldn't it be a good chance to showcase the superiority of TexTailor?  
- The authors do not show any viewpoint-varying results in video format, making it less convincing that TexTailor achieves a good view consistency. 
- It is hard to see obvious improvement from TexTailor in Figure 5, especially comparing with Text2Tex. Perhaps including some bounding boxes and zoom-in patches would help. 

## Writing/Delivery
The writing of the papers can be further improved. For example,
- Most of the figures in the paper are compressed, resulting in blurriness and sometimes hard to read. 
- In Fig.1, citing previous methods (i.e., Text2tex and Texture) might make readers easier to check the idea of them. 
- It is challenging for readers to digest Eqn. (6) - (8). A good strategy to improve it might be similar to what Repaint shows in their paper: demonstrating all the terms in a figure with pictures for a vivid demonstration. Current delivery of newly proposed resampling way in Section 3.1 is hard for readers to understand, especially about the main difference between it and Repaint. 
- Fig.3 does not deliver a clear message for each component. For example, simply giving readers two equations does not help them to understand what is going on. It might be helpful if the authors can name these two equations in high level.

### Questions
1. What are the difficulties for the text-driven methods mentioned in Lines 373 and 374? 
2. Is LPIPS (Section 4.1, Evaluation metrics) a good metric to evaluate view consistency, as LPIPS is sensitive to spatial information? Given that the view angles are known, would it make more sense to reproject one of the views to another and then compute LPIPS between the projected view and the other one?
3. What does the performance preservation loss do in Eqn. (10)? Why would it be effective at a high level? 

Some of the questions may have been entangled with the Weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed a novel architecture that can generate more consistent 3D texture than TEXTure and Text2Tex.

### Strengths
1. Proposed a better approach for viewpoint sampling.
2. The performance of the proposed method is better than listed SOTAs.

### Weaknesses
1. The resampling strategy is similar to the [TexFusion:Synthesizing 3D Textures with Text-Guided Image Diffusion Models] and [TexGen: Text-Guided 3D Texture Generation with Multi-view Sampling and Resampling]. Please explain the difference. Specifically, the method's iterative refinement process, which involves resampling and merging texture information from multiple viewpoints, needs a more detailed explanation of how it differs from existing approaches. The novelty of the resampling strategy is not sufficiently clear.
2. In Fig. 1b, it seems that the proposed method is over-smoothed. Please explain the reason. The smoothing effect observed in the results needs a more thorough analysis. It is not clear if this is an inherent limitation of the method or a result of specific parameter choices. The paper should discuss the trade-off between texture consistency and detail preservation.
3. I do not get the correlation of the third paragraph in Section I with the main content. I think the geometry conversion is not a problem to be solved in this paper. And the SDS can be directly applied on the mesh (DMTET) which does not need conversion.
4. The authors mentioned that " we can achieve high-quality texture with only 30 steps, significantly fewer than the 250 steps required by the original resampling method for a single view." Other methods like texture and text2tex only sampled no more than 50 steps for each view. Where is this "250" from.
5. What is the meaning of resampling steps? Does it mean you have to sample R steps for each view at each timestep?
6. The authors used "resampled images near the first viewpoint to extract images of the same object from different angles in the output domain of the diffusion model" . How to make sure that the viewpoints near the first viewpoint maintain the same style as the first view.
7. In the loss function of Eqn. 10, the target is constraining the new noise estimation to be the same as the original noise estimation. The what is the meaning of training? The optimal case is keeping the original model unchanged.
8. Any 3D results of the method? I prefer to see the rendered 360-degree videos of results.
9. The attention feature injection as in [Text-Guided Texturing by Synchronized Multi-View Diffusion] can help to reduce the problem of the autoregressive inpainting. Have you tried this?

### Questions
1. I do not get the correlation of the third paragraph in Section I with the main content. I think the geometry conversion is not a problem to be solved in this paper. And the SDS can be directly applied on the mesh (DMTET) which does not need conversion.
2. The authors mentioned that " we can achieve high-quality texture with only 30 steps, significantly fewer than the 250 steps required by the original resampling method for a single view." Other methods like texture and text2tex only sampled no more than 50 steps for each view. Where is this "250" from.
3. What is the meaning of resampling steps? Does it mean you have to sample R steps for each view at each timestep?
4. The authors used "resampled images near the first viewpoint to extract images of the same object from different angles in the output domain of the diffusion model" . How to make sure that the viewpoints near the first viewpoint maintain the same style as the first view.
5. In the loss function of Eqn. 10, the target is constraining the new noise estimation to be the same as the original noise estimation. The what is the meaning of training? The optimal case is keeping the original model unchanged.
6. Any 3D results of the method? I prefer to see the rendered 360-degree videos of results.
7. The attention feature injection as in [Text-Guided Texturing by Synchronized Multi-View Diffusion] can help to reduce the problem of the autoregressive inpainting. Have you tried this?

### Soundness
3

### Presentation
3

### Contribution
2
