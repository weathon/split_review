# FreCaS: Efficient Higher-Resolution Image Generation via Frequency-aware Cascaded Sampling

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
While image generation with diffusion models has achieved a great success, generating images of higher resolution than the training size remains a challenging task due to the high computational cost.
Current methods typically perform the entire sampling process at full resolution and process all frequency components simultaneously, contradicting with the inherent coarse-to-fine nature of latent diffusion models and wasting computations on processing premature high-frequency details at early diffusion stages.
To address this issue, we introduce an efficient \textbf{Fre}quency-aware \textbf{Ca}scaded \textbf{S}ampling framework, \textbf{FreCaS} in short, for higher-resolution image generation.
FreCaS decomposes the sampling process into cascaded stages with gradually increased resolutions, progressively expanding frequency bands and refining the corresponding details.
We propose an innovative frequency-aware classifier-free guidance (FA-CFG) strategy to assign different guidance strengths for different frequency components, directing the diffusion model to add new details in the expanded frequency domain of each stage.
Additionally, we fuse the cross-attention maps of previous and current stages to avoid synthesizing unfaithful layouts.
Experiments demonstrate that FreCaS significantly outperforms state-of-the-art methods in image quality and generation speed.
In particular, FreCaS is about 2.86$\times$ and 6.07$\times$ faster than ScaleCrafter and DemoFusion in generating a 2048$\times$2048 image using a pre-trained SDXL model and achieves an $\text{FID}_b$ improvement of 11.6 and 3.7, respectively. FreCaS can be easily extended to more complex models such as SD3.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces FreCaS, a training-free approach for high-resolution image generation based on a diffusion model. FreCaS progressively upscales images using Frequency-Aligned Classifier-Free Guidance, which guides the diffusion model to incorporate new details within the expanded frequency domain. Experimental results show that FreCaS outperforms existing training-free methods in both efficiency and performance. Furthermore, the approach can be seamlessly integrated with advanced models, such as SD3.

### Strengths
1. The proposed method is simple and useful. FreCaS leverages the latent space of lower resolutions, thereby reducing computational costs in the initial stages of higher-resolution generation. By efficiently reusing low-frequency information from lower-resolution outputs, it streamlines the generation process. This simplicity and effectiveness make FreCaS adaptable to other diffusion-based text-to-image models.
2. The ablation study is extensive and thorough, covering critical factors such as inference steps at each resolution stage, adjustments in CFG weights, and reuse of cross-attention maps.

### Weaknesses
1. The coarse-to-fine approach and frequency domain enhancement are commonly applied in training-free high-resolution image generation methods, such as the latest HiPrompt and ResMaster. Although these methods do not use CFG, combining such techniques in this paper does not provide particularly new insights.
2. Generating higher-resolution images can be approached through various methods. This paper focuses primarily on training-free comparisons, but including comparisons with training-based methods, such as Pixart-Sigma or UltraPixel, or super-resolution methods like ESRGAN and SUPIR, would provide a more comprehensive analysis.
3. Training-free methods typically yield low success rates, often requiring tens of attempts to obtain a single satisfactory result. I am not convinced that training-free methods offer a viable solution for high-resolution image generation, especially given that training-based methods are generally faster, more reliable, and stable. Additionally, some training-based methods do not require significant computational resources.

### Questions
1. In Figure 6, the weight of the cross-attention map appears to influence image details and textures (e.g., the blueberry's surface) rather than the layout, which remains stable as the weight varies from 0 to 1. This observation seems to contradict the claim in Section 3.4, which states that cross-attention maps capture the semantic layout by representing attention weights from interactions between spatial features and textual embeddings. Could you clarify whether cross-attention maps primarily control fine-grained details and textures, or if they indeed play a more critical role in determining the semantic layout as suggested earlier?
2. What are the GPU memory requirements for each of the compared methods and for the proposed FreCaS method?

### Soundness
2

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
The paper proposes an efficient frequency-aware cascaded sampling framework designed to tackle the high computational cost of high-resolution image generation. It breaks down the sampling process into progressive stages, expanding frequency bands and refining details step-by-step. Using frequency-aware classifier-free guidance (FA-CFG) and cross-stage attention fusion, FreCaS improves both image quality and generation speed, outperforming state-of-the-art methods like ScaleCrafter and DemoFusion in generating high-resolution images.

### Strengths
1. Assigns different guidance strengths to components of different frequencies to achieve more finegrained control.
2. Good effiency compared with existing works.

### Weaknesses
1. Missing FID which is an important metric and widely adopted by exsiting works. The lacking of FID makes it difficult to comprehensively judge its effectiveness.
2. The cascade framework is widely adopted by the exisitng works. It is also necessary to introduce FID into the ablation study to validate the effectiveness of the main contributions of this work.
3. Some improvements are marginal, e.g., the results on SDXL.

### Questions
See the weekness part.

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
This paper introduces an efficient frequency-aware cascaded sampling framework designed for tuning-free higher-resolution generation. The framework breaks down the sampling process into multiple stages, gradually increasing resolution at each stage. Additionally, it presents a frequency-aware classifier-free guidance approach that applies varying guidance strengths to different frequency components.
Experimental results demonstrate the effectiveness and efficiency of proposed method over various settings.

### Strengths
* This paper proposes a higher-resolution generation method that achieves better performance and faster sampling speeds.
* The paper is well-written, with a clear and straightforward motivation.

### Weaknesses
 * Some evaluation metrics are missing. The authors only provided FID_b and FID_p, but did not include the FID score between the generated and real image sets, which is the most widely used metric for this task.

* Most of the 4K comparison results are in non-realistic styles, such as painting styles. More comparisons in realistic styles need to be provided.

* The cascade pipeline for high-resolution generation has been utilized in several previous works, such as DemoFusion and FouriScale, making the contribution here relatively marginal as it primarily builds on this existing approach. Therefore, a comprehensive evaluation is necessary to demonstrate the improvement brought by the addition of fa-cfg and the F step calculation.

### Questions
Please refer to weakness part.

### Soundness
3

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
4

### Summary
The authors introduce an efficient Frequency-aware Cascaded Sampling (FreCaS) framework for higher resolution image generation. FreCaS decomposes the sampling process into cascaded stages with gradually increased resolutions, progressively expanding frequency bands and refining the corresponding details. Additionally, the authors fuse the cross-attention maps of previous and current stages to
avoid synthesizing unfaithful layouts. Experiments demonstrate that FreCaS outperforms state-of-the-art methods in image quality and generation speed.

### Strengths
1. The  FreCaS is faster than ScaleCrafter and DemoFusion in generating a 2048×2048 image.
2. The  FreCaS introduces a FA-CFG strategy that assigns different guidance strengths to different frequency components.
3. The  FreCaS can be extended to more complex models, validating its broad applicability and versatility.

### Weaknesses
1.  FreCaS relies on several hyperparameters (e.g., w_l, w_h, w_c) that may need careful adjustment to achieve optimal results, which may increase the complexity of experiments.
2. Although FreCaS can be extended to more complex models, its performance may be limited by the pre-trained models.
3. This idea is somewhat similar to FreeU and FreeEnhance.

### Questions
1. In addition to metrics like FID and IS, more comprehensive image quality assessment indicators, such as human subjective evaluation, could be considered to assess the quality of generated images more thoroughly.
2. The experimental part may need to further explore the performance of FreCaS in real-world application scenarios, such as different image contents, styles, and complexities.
3. Although FreCaS improves efficiency, the demand for computational resources remains high when generating high-resolution images.

### Soundness
3

### Presentation
3

### Contribution
3
