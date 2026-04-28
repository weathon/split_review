# Robust-PIFu: Robust Pixel-aligned Implicit Function for 3D Human Digitalization from a Single Image

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Existing methods for 3D clothed human digitalization perform well when the input image is captured in ideal conditions that assume the lack of any occlusion. However, in reality, images may often have occlusion problems such as incomplete observation of the human subject's full body, self-occlusion by the human subject, and non-frontal body pose. When given such input images, these existing methods fail to perform adequately. Thus, we propose Robust-PIFu, a pixel-aligned implicit model that capitalized on large-scale, pretrained latent diffusion models to address the challenge of digitalizing human subjects from non-ideal images that suffer from occlusions.

Robust-PIfu offers four new contributions. Firstly, we propose a 'disentangling' latent diffusion model. This diffusion model, pretrained on billions of images, takes in any input image and removes external occlusions, such as inter-person occlusions, from that image. Secondly, Robust-PIFu addresses internal occlusions like self-occlusion by introducing a `penetrating' latent diffusion model. This diffusion model outputs multi-layered normal maps that by-pass occlusions caused by the human subject's own limbs or other body parts (i.e. self-occlusion). Thirdly, in order to incorporate such multi-layered normal maps into a pixel-aligned implicit model, we introduce our Layered-Normals Pixel-aligned Implicit Model, which improves the structural accuracy of predicted clothed human meshes. Lastly, Robust-PIFu proposes an optional super-resolution mechanism for the multi-layered normal maps. This addresses scenarios where the input image is of low or inadequate resolution. Though not strictly related to occlusion, this is still an important subproblem. Our experiments show that Robust-PIFu outperforms current SOTA methods both qualitatively and quantitatively. Our code will be released to the public.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a robust method for single-image human reconstruction by building upon the PIFu framework and addressing its limitations. The improvements focus on four main aspects. First, a diffusion model is employed to remove external occlusions from the image, ensuring a clearer view of the target human. Second, another diffusion model is used to predict multi-layer normal maps to mitigate the impact of self-occlusion. Third, the pixel-aligned implicit model is modified to use both the original image and the multi-layer normal maps as inputs for predicting 3D occupancy labels. Finally, an optional refinement diffusion model is introduced to enhance the resolution of the normal maps if finer details are required.

### Strengths
1. The proposed approach significantly improves the robustness of PIFu by addressing specific limitations, such as handling occlusions and introducing normal maps. The modifications are logical and well-justified, leading to more accurate reconstructions.
2. The method demonstrates better performance on the BUFF and MultiHuman datasets compared to existing approaches, underscoring its effectiveness in general human reconstruction tasks.

### Weaknesses
1. The necessity of eight distinct normal maps (both outer and inner maps for each direction) in the Penetrating Diffuser is not fully intuitive. It is unclear why both outer and inner maps are required for each direction, as they may simply represent flipped orientations. Further explanation on the additional information provided by the inner normal maps would enhance understanding. Specifically, it's not clear how the inner normal maps capture information that is not already present in the outer normal maps, given that they are derived from the same underlying geometry. A more detailed justification, perhaps with a visual example demonstrating the differences, would be beneficial.

2. The need to run the Penetrating Diffuser separately for the front-back and left-right orientations introduces significant computational overhead. The left-right normal map prediction is conditioned on the front-back prediction; however, simultaneous prediction of all eight maps could potentially enhance the conditioning across all pairs. This two-stage execution doubles the computational load, requiring two diffusion models and multiple sampling runs, which could be optimized. The sequential nature of this process also raises questions about potential error propagation from the first stage to the second.

3. Clarification on MLP in Pixel-Aligned Implicit Model (Section 3.3): Additional clarification on the structure of the MLP in the Pixel-Aligned Implicit Model would be beneficial. Specifically, it is unclear if this MLP follows the structure of the original PIFu model, and whether all normal maps and features are concatenated directly as inputs to the network. The specific dimensions of the input and output layers, and the number of hidden layers, should be explicitly stated to allow for a better understanding of the model architecture.

### Questions
Please justify the design of the Penetrating Diffuser (see Weakness 1 and 2). Please justify why inner and outer normal maps are needed, and why separate models for front-back and left-right are needed.

Please also add more explanations to the architecture of the Pixel-Aligned Implicit Model (see Weakness 3).

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
This paper propose Robust-PIFu, a novel approach designed to reconstruct 3D human models from a single image, especially under the occlusion setting. By harnessing the power of large-scale pre-trained latent diffusion models： a disentangling latent diffusion model and a penetrating latent diffusion model, Robust-PIFu effectively separates each human and inpaints the occluded areas of the human. Subsequently, a layered-normals pixel-aligned implicit model, coupled with an optional super-resolution mechanism, is employed to reconstruct the 3D clothed human model. Experimental results demonstrate that Robust-PIFu outperforms current state-of-the-art methods in both qualitative and quantitative evaluation.

### Strengths
1. Robust-PIFu provides a novel solution to the problem of external and internal occlusions in 3D human reconstruction from single image by means of pretrained diffusion models.
2. Extensive experiments prove the effectiveness of the proposed methods.

### Weaknesses
1. The writing and the presentation of the paper need improving.
2. Robust-PIFu seems to be primarily effective in reconstructing 3D humans from laboratory datasets. Its generalizable experiment in real image reconstruction scenarios is simple, as it lacks more complex real image reconstruction results.
3. Lack of the training details of Disentangling Diffuser.

### Questions
1. I am curious about the reconstruction performance of Disentangling Diffuser on real images when there are significant areas of missing. Specifically, how well can it reconstruct the head portion if it is occluded?
2. In the images presented in the paper, the characters are arranged side by side. If the characters were arranged vertically, such as one person standing and another crouching in front of them, would the disentangling strategy of Disentangling Diffuser still be effective?

### Soundness
4

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
4

### Summary
The authors propose a method to reconstruct 3D human(s) from a single image by leveraging pretrained latent diffusion models and implicit function representation. The models are utilized for disentangling external occlusions (overlapping people), recovering from internal occlusions (viewpoint specific missing details) and an optional normal map super-resolution module to improve fidelity. The diffusion models+implicit models are trained using Thuman2.0. The method is evaluated on MultiHuman and BUFF datasets and show superior quality and performance compared to prior works.

### Strengths
The method is simple and the writing is easy to follow. To highlight specific positives:
- Leveraging open-source diffusion models: This method highlights the ability of large open-source pretrained diffusion models to tackle 2D human inpainting (disentangling diffuser) and cross-domain conditional image generation (penetrating diffuser). The pipeline chains the outputs in a straightforward manner and obtains good quality results.
- Superior result quality: From the evaluations, it is quite clear that prior work cannot address the problem of inter-penetrating and self-occluding human reconstruction. This method achieves much higher quality reconstructions that reflects in the qualitative and quantitative experiments.
- Experimental results and observations: The authors have provided extensive results and ablations between the paper and the appendix which is quite appreciated.

### Weaknesses
The approach overall is quite straightforward. However, I have a few concerns regarding the details of the method. Specifically:
- Need for SMPL-X mesh: The paper mentions that prior work ECON and Wang et al. require accurate SMPL-X meshes for good predictions which Robust-PIFu does not need (L51-53). In fact, not using the SMPL-X model causes the model to have errors as shown in Fig. 14. Please clarify this point and show results when the SMPL-X input has some error.
- Method's robustness to diverse data: The results in the main paper are quite impressive. But, I would urge the authors to add more qualitative results on a larger diversity of data to get a more holistic view of the method's robustness (to live upto its name :) ).:
  * Ex. real-world images under multiple settings (single/multi-humans with **varying degrees of occlusion**).
- Predicted normal maps N_s: What is the reason behind choosing an arbitrary number 8? There are numerous set of human poses that do not get covered by just 8 maps. How does the method handle such scenarios?

### Questions
- Fig. 3: consider adding a caption.
- Fig. 4 caption has incorrect layout for the titles.
- Disentangling Diffuser: 
  * How well does the disentangling diffuser work for overlapping humans at different depths? I presume the training data had humans at similar depths. 
  * Were any augmentations applied to add external occlusions to human images? L306 is not clear about this.
- Penetrating Diffuser: 
  * What is the reason behind generating the normal maps in two parts? Is it mostly due to memory and compute or due to bad predictions?
- Layered Normals PIFu model:
  * What is the need for adding SMPL-X normal maps N_s here? Since all the required information to reconstruct the human is present in N_c. An ablation on this would be useful.
- Refining Diffuser:
  * Why is R run 8 separate times to obtain the super-resolved normal maps? Would it be possible to super-resolve all 8 at once or 4 at a time (similar to P's output format)?
- Fig. 7 (Row 4) - Show results for both humans.
- For ablations on P (L481) and the implicit model (L492), what are the inputs to the implicit model in each setting?
- For ablation on P (Fig. 8), The hidden arms of the person in each image should have been reconstructed correctly if P outputs the correct normal maps. Does P fail when there are multiple people in the input image since its OOD?
- Fig. 22: It would be interesting to show results on these examples. This would show that even though the GT mesh has holes, the method can reconstruct plausible surfaces.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method to address the common challenges in single-image to 3D human reconstruction, specifically the performance degradation caused by self-occlusion and inter-person occlusion. The authors introduce the Disentangling Diffuser, a diffusion model used for inpainting occluded regions to resolve inter-person occlusion, and the Penetrating Diffuser, which generates multi-layer normal maps to handle self-occlusion. Using these outputs, the paper proposes a PIFu-based structure for 3D human shape reconstruction.

### Strengths
This work takes an approach to resolving self-occlusion and inter-person occlusion without significantly altering the foundational PIFu method. 

By using the divide-and-conquer strategy with the Disentangling Diffuser and Penetrating Diffuser diffusion models.

### Weaknesses
1. The method novelty is limited. The proposed Disentangling Diffuser is identical to the Stable Diffusion [1] inpainting model in both its structure and functionality, making it difficult to consider this as a unique contribution of the paper. Similarly, the Penetrating Diffuser is analogous to ICON [2], which utilizes the SMPL model for normal prediction. It is also challenging to find novelty in the Pixel-aligned Implicit Model.
2. The paper’s structure is difficult to follow, and the notations lack clarity. In particular, section 3 lacks a formal formulation of the inputs and outputs for each model, and there is excessive repetition regarding input and output dimensions that could be streamlined. Significant revisions are needed for paper quality.
3. The figure 3,4 and 5 are excessively large and occupy too much space.
4. Figure 4, figure 8, 10 placement is inconvenient. It reduces readability.
5. The paper does not reference any methods from 2024, and all comparison methods are from 2023 or earlier. Additional experiments with newer methods are needed.
6. The experimentation and result analysis are insufficient. In particular, a quantitative evaluation of the inter-occlusion claimed in this paper is necessary.
7. There is no explanation or reference for the evaluation metrics. A reader who doesn't know the abbreviation for 'evaluation metric' would find it difficult to understand.
8. The requirement to manually define occlusion regions (mask) limits practical applicability.
9. There is an insufficient ablation study regarding layer depth of outer and inner normal map, particularly concerning variations in limb length and pose.
10. There is a lack of detail on which diffusion and PIFu models were used and the training and optimization procedure, making reproduction challenging.

### Questions
1. Why are there no references and comparisons to methods published after 2023?
2. Is there a specific rationale for defining the Penetrating Diffuser views as front, back, right, and left? Could additional views be used?
3. How does the inference runtime or computational complexity compare to other methods?
4. When using the Disentangling Diffuser and Penetrating Diffuser for inference, how many denoising steps were performed, which scheduler was used, and was classifier-free guidance (CFG) applied?
5. Is there an additional study on the reliability and performance of images generated by the diffusion model (particularly normal maps), given that diffusion model results can vary with different seed values?
6. How does the viewpoint of a single-view image affect performance, and to what extent does it impact reconstruction quality?

### Soundness
2

### Presentation
1

### Contribution
2
