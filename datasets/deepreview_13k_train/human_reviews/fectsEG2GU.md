# Diffusion$^2$: Dynamic 3D Content Generation via Score Composition of Video and Multi-view Diffusion Models

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Recent advancements in 3D generation are predominantly propelled by improvements in 3D-aware image diffusion models. These models are pretrained on internet-scale image data and fine-tuned on massive 3D data, offering the capability of producing highly consistent multi-view images.
However, due to the scarcity of synchronized multi-view video data, it remains challenging to adapt this paradigm to 4D generation directly.
Despite that, the available video and 3D data are adequate for training video and multi-view diffusion models separately that can provide satisfactory dynamic and geometric priors respectively. 
To take advantage of both, 
this paper presents \textbf{\textit{Diffusion}$^2$}, a novel framework for dynamic 3D content creation that reconciles the knowledge about geometric consistency and temporal smoothness from these models to directly sample dense multi-view multi-frame images which can be employed to optimize continuous 4D representation.
Specifically, we design a simple yet effective denoising strategy via score composition of pretrained video and multi-view diffusion models based on the probability structure of the target image array. 
To alleviate the potential conflicts between two heterogeneous scores, we further introduce variance-reducing sampling via interpolated steps, facilitating smooth and stable generation.
Owing to the high parallelism of the proposed image generation process and the efficiency of the modern 4D reconstruction pipeline, our framework can generate 4D content within few minutes.
Notably, our method circumvents the reliance on expensive and hard-to-scale 4D data, thereby having the potential to benefit from the scaling of the foundation video and multi-view diffusion models. 
Extensive experiments demonstrate the efficacy of our proposed framework in generating highly seamless and consistent 4D assets under various types of conditions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Diffusion^2, an interesting framework that aims to combine video and multi-view diffusion models through score composition for 4D content generation. The method proposes parallel generation of multi-view videos without requiring synchronized 4D training data, offering a novel theoretical perspective on combining different types of diffusion priors.

### Strengths
- Innovative conceptual approach to leveraging video and multi-view diffusion priors
- Well-formulated theoretical framework for score composition
- Thoughtful parallel generation architecture design
- Clear and thorough ablation studies

### Weaknesses
The method has some practicality issues:
- Requires 8-16 A6000 GPUs for basic operation
- Still takes 20 minutes per generation even with massive compute
- Memory-speed tradeoff makes it impractical for most real applications
It would be good to hear the authors discussing about the path to reduce these extreme hardware requirements.

The experimental validation could be more comprehensive:
- Most demonstrations focus on relatively simple motions
- Additional results on more complex scenarios (e.g., rotational movements, articulated motions) would help better understand the method's capabilities
- Further exploration of challenging cases would strengthen the evaluation.

### Questions
- Have the authors considered strategies to reduce the computational requirements?
- Could the authors provide insights on how the method might handle more complex motion patterns?
- What are the main challenges in extending this approach to more diverse scenarios?

### Soundness
2

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
3

### Summary
This paper aims to leverage existing multi-view 3D generation models and video generation models for 4D generation. For this, it designs a score composition strategy to make use of these two kinds of generation models for directly generating multi-frame multi-view image arrays. To alleviate potential conflicts between these two kinds of generation models, a variance-reducing sampling strategy is proposed. With the generated multi-frame multi-view image arrays, the proposed method introduces a dynamic and texture-decoupled
reconstruction strategy to reconstruct 4D videos. Experiments show that the proposed method can make use of these two kinds of generation models for 4D generation.

### Strengths
1. This proposed method takes advantage of existing multi-view 3D generation and video generation for 4D generation and does not require extra 4D training data. 
2. Through the analysis, the score composition for denoising is reasonable to achieve the above goal.
3. Considering the potential conflicts between two kinds of generation models, the proposed method introduces variance-reducing sampling to reconcile the distinct modes at a higher noise level.

### Weaknesses
1. Since the proposed method leverages both multi-view 3D generation models and video generation models, maybe a reasonable baseline is to generate a video first via video generation models, then generate multi-view images based on the frames in this video using the multi-view 3D generation models. Finally, 4D reconstruction methods, such as [1], can be applied to generate 4D contents. It will be better to use this baseline to highlight the effectiveness of the proposed score composition.         
[1] Li, Zhan, et al. "Spacetime gaussian feature splatting for real-time dynamic view synthesis." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.   
2. The experiments are weird. In Figure 4, the qualitative results for the stage-1 and stage-2 are almost the same. As mentioned in L524-525, the images generated in the first stage will show blurring details. Therefore, why are the results in two stage almost the same?
3. For the ablation studies, it is better to show quantitative results like Table 1 and Table 2.

### Questions
1. Can you try the baseline mentioned in W1 to further demonstrate the effectiveness of the proposed method?
2. Can the proposed method generalize to other multi-view 3D generation and video generation methods?
3. Can you show the time consumption for stage-1 and stage-2?
4. Is it possible for the proposed method to generate 4D contents with multiple objects?

### Soundness
2

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
This paper introduces a new algorithm to generate 4D content from a single image or video of a foreground object.
The key idea is to combine a video diffusion model with a multiview diffusion model to generate a set of multiview-consistent videos.
The generation process involves interleaving the denoising of the video diffusion model and the denoising of the multiview diffusion model. To further improve the generation quality, a variance reduction method is proposed to re-denoise some views. Finally, a dynamic Gaussian field is reconstructed from the generated multiview videos. 
Experiments demonstrate that the proposed method is able to produce multiview consistent videos and generate 4D contents.

### Strengths
The main strength of the paper is that the idea of combining two diffusion models to generate 4D content is novel and interesting.
Due to the lack of 4D data, it is difficult to train a 4D diffusion model directly. This method only takes advantage of video diffusion models and multiview diffusion models, which can be trained separately on large-scale 3D object datasets or video datasets. Thus, this method is promising to avoid directly using 4D data but still allow 4D generation. 

The theoretical analysis of the proposed method is reasonable and convincing. The assumptions are provided for a better understanding of the mechanism of the interleaved denoising of two diffusion models.

### Weaknesses
The main weakness is the quality of the 4D generation.
The generation of the proposed method seems to be oversmoothed on unseen viewpoints. As we can see in both figures and the supplementary video, the backside all seems to be oversmoothed without any details, especially when the variance reduction is applied. 
I guess this may be due to the difficulty in making two diffusion models agree with each other. The assumption of independent probability distribution may be a little bit strong. 
The results are even worse than the models with SDS losses or some other models directly trained on limited 4D data.

### Questions
I'm not sure whether a finetuning of SVD on videos containing only foreground objects would be helpful in improving the quality. In my experience, SVD performs poorly in generating videos of only one dynamic foreground object.

### Soundness
3

### Presentation
3

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
This proposal design a framework for combination between temporally aligned VDM(Video Diffusion Model) and spatially aligned multi-view generation model. It utilizes runtime optimization instead of training to build up 4D objects. Among recent SoTA 4D generation methods, this proposal is free of training and achieves competitive performance. Also, it proves that we can use off-the-shell models for 4D content generation without further training.

### Strengths
1、The framework setting needs no further training. 
2、The authors write clear proofs for the denoise process and 4D reconstruction process.
3、Experiments are sufficient to prove the anticipated conclusion.

### Weaknesses
Some conclusions are not that rigorous, see questions.

1、Figure3，If the viewpoints differ by only 30 degrees, can they still be considered independent variables?
2、Variance-reducing sampling，the rollback operation need more specific explanation of why it works? And demonstrate why this would reduce the variance of sampling results? Also, If we set the sampling steps larger, will it achieves similar effect with Variance-reducing sampling?

### Questions
1、Figure3，If the viewpoints differ by only 30 degrees, can they still be considered independent variables?
2、Variance-reducing sampling，the rollback operation need more specific explanation of why it works? And demonstrate why this would reduce the variance of sampling results? Also, If we set the sampling steps larger, will it achieves similar effect with Variance-reducing sampling?

### Soundness
3

### Presentation
3

### Contribution
3
