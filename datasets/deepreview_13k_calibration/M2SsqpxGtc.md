# CubeDiff: Repurposing Diffusion-Based Image Models for Panorama Generation

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
We introduce a novel method for generating 360° panoramas from text prompts or images. Our approach leverages recent advances in 3D generation by employing multi-view diffusion models to jointly synthesize the six faces of a cubemap. Unlike previous methods that rely on processing equirectangular projections or autoregressive generation, our method treats each face as a standard perspective image, simplifying the generation process and enabling the use of existing multi-view diffusion models. We demonstrate that these models can be adapted to produce high-quality cubemaps without requiring correspondence-aware attention layers. Our model allows for fine-grained text control, generates high resolution panorama images and generalizes well beyond its training set, whilst achieving state-of-the-art results, both qualitatively and quantitatively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces CubeDiff, which is a simple and efficient method for generating 360 panorama from image and text conditions. CubeDiff builds on pretrained a multi-view diffusion model and fine-tunes it to output cubemap representations that is later stitched together into a single panorama. Compared to previous approaches that employ complex cross-view attention mechanisms, CubeDiff simply inflates existing attention layers and adds positional embeddings to adapt to cubemap representation. Thanks to this simple change to multi-view diffusion model, CubeDiff achieves high-quality panorama generation while retaining the generalizability of the base diffusion model. The qualitative and quantitative comparisons with baselines demonstrate the CubeDiff achieves better quality panoramas, and also enabling fine-grained text control which was challenging in previous methods.

### Strengths
* The proposed method is simple yet effective, according to the provided qualitative examples. Using cubemaps as a representation for panorama generation seems to be a valid choice, and building on a pretrained multi-view diffusion model is an adequate approach as it is proven to be effective at handling similar tasks requiring multi-view consistent generation.
* The method shows notable training efficiency, as only 48k panoramas were used for training. It is convincing that it adapts well to out-of-distribution conditions, as shown by the outdoor generations in Fig. 1.
* The fine-grainded text control of CubeDiff seems to be a clear advantage compared to previous approaches that use other types of panorama representatiions. From a user perspective, being able to provide certain controls for each of view would be more convenient with cubemaps, as it removes the need to consider the overlapping regions between neighboring views.

### Weaknesses
While the provided qualitative results of CubeDiff are convincing, several key aspects regarding the methodology and baseline comparisons are missing:

* In Sec. 4.1, it is remains unclear how the "inflated" attention layer in CubeDiff is different from previous appoaches, such as the Correspondence-Aware Attention from MVDiffusion [1]. Specifically, it's unclear why this method reduces the risk of overfitting and results in greater generalization compared to approaches like MVDiffusion. This is particularly confusing since MVDream [2], from which CubeDiff adapts its layers, also incorporates an additional "3D Self-Attention" layer on top of a 2D diffusion model. Further clarification would be helpful to understand why one approach may lead to overfitting (as in MVDiffusion), while the other leads to generalization (as in CubeDiff).

* Missing baseline: PanFusion [3] is an imporant baseline to consider for 360 panorama generation from text prompts. As it was published in CVPR 2024, it serves as a valid baseline for this work. To claim state-of-the-art performance on panorama generation, comparisons with PanFusion (e.g. in terms of image quality, generalization) would be required. Alternatively, it would be helpful to provide explanations on how CubeDiff differs from PanFusion and why a direct comparison may not be necessary.

* I am curious about the details of the quantative evaluation procedure for the FID and KID metrics. Were the generated 360 panoramas directly used for measuring FID, or were projected perspective views used instead? Additionally, there exists a variant of FID, called FAED [4], specifically designed to assess the quality and realism of panoramas. Evaluating with such metrics could provide a more accurate reflection of the actual quality of the panorama generations.

* I could not find ablation studies for the key components of the method, specifically regarding the effectiveness of synchronized group normalization and overlapped predictions. These are critical design choices for CubeDiff, yet it is difficult to assess their validity without quantative or qualitative comparisons showing the impact of these components.

Overall, I agree that the cubemap representation could be an effective choice for panorama generation, and CubeDiff introduces a new approach of incorporating the cubemap representation. However, without the concerns about the key contribution addressed - particularly a clear explanation on why this approach should lead to enhanced generalization to out-of-distribution cases - it is difficult to assign a higher rating.

### Questions
The main questions on the method are in the Weaknesses section.

* While fine-grained text control appears useful, I'm curious whether the conditioning can truly be applied on a "per-face" basis. Interactions between the pixels in different views may influence the content generated in each other. Could there be failure cases where changing the text condition for one view can lead to unintended changes in another view?

* As described in Sec. 4.5, CubeDiff is trained with both dropped text and image conditions. In this case, is CubeDiff also capable of performing text-conditioned generation without an image input?

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
4

### Summary
This paper proposes CubeDiff, a method that generates panoramas from text or single-image condition. The core of CubeDiff is to represent a panorama with cubemaps, 6 images representing the 6 faces of a cube that seamlessly capture the scene in an inside-out way. With this representation, CubeDiff adapts a pre-trained text-to-image diffusion model to generate the 6 cube-face images simultaneously. Similar to previous works like MVDream and Wonder3D, the proposed method extends the self-attention layer in the pre-trained denoising network to operate on multiple images for learning holistic multi-view consistency. Experiments on Laval Indoor and Sun360 datasets show that CubeDiff outperforms previous panorama generation methods (MVDiffusion, Diffusion360, etc,) across various generation settings (text-conditioned, image-condition, or both).

### Strengths
1. CubeDiff's design choices are reasonable and backed up with a detailed discussion and comparison of different panorama representations. Extending the original self-attention over image patches of a single image to handle multiple views is a common strategy in the literature of multi-view diffusion models and is a natural choice here, considering the cube map representation. 

2. The paper provides a detailed discussion on different representations for the panorama in Sec.3. Together with the related works (Sec.2), choosing cube maps as the generation targets of the multi-view diffusion model is well-motivated. 

3. The experiments cover a rich set of conditioning settings, and CubeDiff demonstrates supreme performance both qualitatively and quantitatively. The anonymous website provides an interactive qualitative comparison, which helps better understand the quality of different approaches.

### Weaknesses
1. The experiment section of the paper lacks some critical ablation studies and is not complete: 1) Sec4.2 states the importance of the Synchronized GroupNorm, but there is no quantitative analysis for this design; 2) Sec4.4 claims the design of overlapping predictions between the nearby faces can reduce the generation artifacts, but again lack a corresponding ablation study.

2. The overall technical contribution is relatively limited - there are no new designs from the modeling perspective. However, given the good empirical performance and the simplicity of the approach, this is not necessarily a vital weakness. Therefore, I hope the authors can address the first point above to complete the ablation studies for the core modeling components described in Sec.3 and Sec.4.

3. It is unclear to me if the training data of the baselines (e.g., MVDiffusion and DIffusion360) is the same as the proposed CubeDiff. If they use different training data, would the comparisons be unfair? Ideally, the authors should re-train those diffusion-based baselines with the same training data.

### Questions
Please refer to the Weaknesses section for the questions.

In general, the proposed CudeDiff is simple and obtains good experimental results. However, the paper does not provide necessary ablation studies for some detailed design choices, and it's also unclear if the comparisons against baselines are conducted in a fair setting. These two points are especially important given CudeDiff's limited technical novelty. I will consider updating the rating if these concerns can be properly addressed.


-----

**After rebuttal**: I increased the score to 6 as the authors provided a thorough study with different amounts of training panoramas, which helps demonstrate the method's effectiveness and generalization capability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a new method for generating panoramic images. The key idea of the method is to utilize cubemap projections, instead of equirectangular projection. The method is relatively straightforward, but demonstrates good results.

### Strengths
- It is a simple to understand and implement method.
- Paper is well written and easy to follow.
- Results seem to be better than competitive methods.
- New application of generating panorama based on multiple text-prompts.

### Weaknesses
 - The claim of "fully recycle pretrained text-to-image model, enabling generalization far beyond the limited training data" is not well supported by results. The convincing results here would be, if the paper shows that the method can generate panoramas that are clearly outside of the panoramic dataset distribution. For example, stylistic panoramas, e.g. cartoons, oil painting or some fantasy concepts, such as "Alice in wonderland", etc.

- Table. 1 is confusing. First of all there is no column $Ours_{text}$, while in Sec 4.5. It is said that models can operate in this mode. Second coloring in this Table is confusing. My suggestion would be to provide green/light green coloring within each modality: "Text-only", "Image-only", etc.

### Questions
--

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
This paper presents a thoughtful approach to cubemap generation. The authors’ methodology is straightforward yet effective, addressing important challenges in cubemap generation, and achieves outstanding results compared to state-of-the-art.

### Strengths
This is a solid, simple yet effective work.  

First, desipte the idea of using cubemap generation for panorama is not new,  the authors' solution through cubemap mv diffusion is simple but effective. This work offers an effective solution through overlapping predictions to address the wellknown issue of cubemap discontinuity.

Second, since each frame is generated individually (even with shared attention), tone shifts can occur across views. The authors address this by incorporating GroupNorm in VAE, which is a great application of existing techniques to solve this specific issue.

Lastly, their solution, while simple, performs significantly better than other alternatives, demonstrating that careful adjustments can yield meaningful improvements.

### Weaknesses
1. Lack of deeper analysis on how discontinuity is addressed: The proposed approach of overlapping predictions to handle discontinuity is interesting, but its effectiveness is not entirely clear. Overlapping predictions will bring new issues:  discontinuities within each view due to the six-view projection.  I recommend a more in-depth exploration:
- Visualization of the overlapping predictions: How does each view appear before panorama merging?
- Techniques for managing discontinuity within each view. Now each view might have severe boundary inside due to the discontinuity. Does the model handle this fine?  Is the achieved primarily due to VAE finetuning? How is shared attention helping here? Maybe attention visualization will benefit analysis.
 
2. No ablation study on component effectiveness: An ablation study would strengthen the paper, particularly with results on:
- The impact of GroupNorm
- The impact of overlapping prediction

### Questions
- Section 4.5 could be removed by briefly mentioning these details in the implementation section.
- The implementation details could benefit from more specifics, such as the base model used.
- Additional information on the VAE and UNet architectures would be helpful, particularly regarding the base models and the placement of GroupNorm in the VAE.
- Why did the authors choose to concatenate positional encodings as additional channels? It’s more common to add positional embeddings directly to the latent representation along with timestep embeddings.
- Is this work the first one to address panorama generation through cubemap diffusion?

### Soundness
3

### Presentation
4

### Contribution
3
