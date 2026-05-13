# Consistent Flow Distillation for Text-to-3D Generation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Score Distillation Sampling (SDS) has made significant strides in distilling image-generative models for 3D generation. However, its maximum-likelihood-seeking behavior often leads to degraded visual quality and diversity, limiting its effectiveness in 3D applications. In this work, we propose Consistent Flow Distillation (CFD), which addresses these limitations. We begin by leveraging the gradient of the diffusion ODE or SDE sampling process to guide the 3D generation. From the gradient-based sampling perspective, we find that the consistency of 2D image flows across different viewpoints is important for high-quality 3D generation. To achieve this, we introduce multi-view consistent Gaussian noise on the 3D object, which can be rendered from various viewpoints to compute the flow gradient. Our experiments demonstrate that CFD, through consistent flows, significantly outperforms previous methods in text-to-3D generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the 'Consistent Flow Distillation (CFD)' for text-to-3D generation. It extends the success of SDE into 3D domain, and with its novel multi-view consistent Gaussian noise sampling, it demonstrates a simple yet effective ways to enhance the visual quality and diversity in 3D generation. Extensive quantitative and qualitative comparisons demonstrates its effectiveness compared to previous methods.

### Strengths
[**Novelty**] 
- The adaptation of probability flow ODE (PF-ODE) with clean flow gradient from 2D images to guide 3D generation is innovative
- The adaptation of multi-view consistent Gaussian noise ensures a unified appearance from all angles, which is the key to high-fidelity texture generation

[**Significance**]
- The propose design of multi-view consistent noise is useful for the whole community, its performance boost in 3D-FID and 3D-CLIP scores compared to SDS, ISM, and VSD baselines, and exhibits richer details and more photorealistic textures, providing a considerable improvement to text-to-3D generation.

[**Completeness & Clarity**]
- I like its various qualitative comparisons with different baselines and ablations, also its examples of diverse generation for the same prompt. 
- It is well-organized, and effectively explains advanced technical concepts, including clean flow gradients, PF-ODE, and the SDE-based sampling process.

### Weaknesses
- On significance and novelty, I think based on the current progress in the field of 3DGen AI, although CFD introduces innovative noise techniques, it doesn’t propose entirely new model architectures or evaluation metrics beyond standard score distillation approaches. This is more fundamental concern when existing 3D-generative models can generate high-quality 3D assets within minutes, which this approach can still take hours. 
- Limited Qualitative Examples for long and complex Prompts: although the paper includes various qualitative comparisons, additional examples, especially for complex prompts, could further enhance understanding of CFD’s limitations
- I also feel that some example results are not sharp enough, like around line 820

### Questions
NA

### Soundness
4

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
This work proposes Consistent Flow Distillation (CFD) to enhance generation diversity and quality in SDS-based text-to-3D generation task. By treating the SDS as a trajectory of SDE, the authors propose guiding the optimization process via consistent 2D clean flow gradients. A key insight is maintaining consistent 2D image flows across different viewpoints for generating high-quality 3D outputs. To achieve this, they present an algorithm for computing multi-view consistent Gaussian noise, aligning noise textures precisely on the 3D object's surface. Extensive experiments showcase the effectiveness of CFD over related methods like VSD, ISM.

### Strengths
- The paper stands out for its robust presentation of results, thorough experimental analysis, and compelling evidence.
- Introducing Consistent Flow Distillation, the paper leverages 2D clean flow gradients and multi-view consistent noise to elevate the diversity and quality of 3D generation.
- Through empirical results, it is evident that the proposed CFD effectively enhances the diversity of generated outputs, showcasing its potency in improving the quality and variety of 3D-generated content.

### Weaknesses
- The stated contributions appear to overlap with existing methodologies.
    - The utilization of SDE formulations mirrors the approach outlined in "Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior." While Consistent3D emphasizes addressing the unpredictability inherent in SDE sampling by introducing a deterministic sampling prior, the rationale behind employing image PF-ODE to steer 3D generation remains ambiguous.
    - The concept of multi-view consistent Gaussian noise is the same in "Geometry-Aware Score Distillation via 3D Consistent Noising and Gradient Consistency Modeling." Despite the advancements in quality seen in this work, a detailed comparative analysis is warranted. These approaches all seem to draw inspiration from Integral Noise.

- Introducing CFD could potentially inject more diversity into the 3D generation process. However, in SDS-based 3D generation, each iteration of inconsistent content distillation may exhibit the Janus problem. It remains uncertain whether CFD might improve multi-Janus issues, prompting the incorporation of MVDream for distillation. It could be beneficial to present results distilled from SDV2 or DeepFloy-IF to strengthen their argument.

### Questions
- The primary questions are raised in the Weaknesses part, which related to raising score.
- Could the paper provide a detailed comparison regarding memory usage and training time costs to existing methods?
- While MVDream is introduced to mitigate the Janus problem, there is a concern that it might overfit to the 3D training set, potentially resulting in object omission issues. Is there potential for CFD to address this drawback effectively? Typical prompts such as "A squirrel playing the guitar," "A pig wearing a backpack," and "a bear playing an electric bass" could shed light on this aspect.
- An open question: amidst various efforts to enhance SDS optimization for improved quality, can the authors assert that their formulation stands out as the best in Table 1? 
- The significance of Figure 10 in the appendix, which likely demonstrates the effectiveness of CFD, suggests that its inclusion in the main body could boost the paper's impact and clarity.

### Soundness
3

### Presentation
2

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
This paper proposes Consistent Flow Distillation (CFD), which leverages gradients from 2D image flows to achieve better consistency across views, thereby improving 3D generation quality and diversity.

### Strengths
1. The generation quality of this proposed method is very high. The textures are realistic and detailed, providing a high level of visual fidelity that closely resembles real-world materials.
2. This paper is well-written, with well-organized sections that guide the reader through theory and methodology.

### Weaknesses
1. Concurrent work. I believe it is necessary for the authors to clarify the distinction between their approach and “Consistent Flow Distillation for Test-to-3D Generation” within the main body of this paper. The ODF-based optimization and multi-view consistent Gaussian noise used here are quite similar to those in FSD, which warrants a more explicit comparison.
2. Experimental Setup. (a) It’s unclear whether CFD utilizes MVDream in the comparison experiments, and if so, this may introduce an unfair advantage. (b) Only ten prompts are used in the comparative experiments. A broader evaluation set would improve the robustness of the evaluation. (c) FSD also should be included in the comparison for a more comprehensive evaluation. (d) The generation diversity hasn't been well evaluated. I also suggest that aesthetic evaluation metrics, e.g., LAION Aesthetics Predictor [1] and PickScore [2], can provide a more holistic assessment of the generated textures. (e) The ablation study lacks visualizations, which would help in understanding the impact of different components of the proposed method.

[1] https://laion.ai/blog/laion-aesthetics. [2] Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation.

### Questions
See the weaknesses section. I would consider raising my socre if the author can address my concerns above.

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
The authors propose consistent flow distillation (CFD) strategy which can replace existing score distillation sampling (SDS) which leverages pre-trained 2D diffusion models for 3D generative models. The authors propose to guide 3D generation with 2D clean flow gradients operating jointly on a 3D object. They identify that a key in this process is to make the flow guidance consistent across different camera views.

### Strengths
1. The authors well compare other proposed SDS variants including VSD and ISM.
2. The author demonstrates the qualitative results of the proposed method compared to other variants.

### Weaknesses
1. The concern is that the proposed method leverages both MVDream and StableDiffusion2 as text-to-2D diffusion model, but other competitive methods, DreamFusion, ProlificDreamer, and LucidDreamer only StableDiffusion2. It means that the superiority of the proposed method might be from not the proposed CFD but from MVDream.

2. The proposed method only do experiments on text-to-3D tasks where the proposed CFD can be applied to any X-to-3D models.

### Questions
1. What happen if the proposed CFD is applied on DreamFusion pipeline which only replaces SDS to CFD while keeping all the other components the same?

2. What happen if the proposed CFD is applied to image-to-3D models like Wonder3D? Please show some results more than text-to-3D task.

3. Please give some results on user study for text-to-3D generative models where most of the recent text-to-3D generative models also show this results (or show SSIM or LPIPS results on image-to-3D tasks where there exist GT images on other camera views).

### Soundness
3

### Presentation
2

### Contribution
2
