# 3DitScene: Editing Any Scene via Language-guided Disentangled Gaussian Splatting

- Decision: Accept
- Scores: 6, 8, 5, 5, 5

## Abstract
Scene image editing is crucial for entertainment, photography, and advertising design.
Existing methods solely focus on either 2D individual object or 3D global scene editing.
This results in a lack of a unified approach to effectively control and manipulate scenes at the 3D level with different levels of granularity.
In this work, we propose \method, a novel and unified scene editing framework leveraging language-guided disentangled Gaussian Splatting that enables seamless editing from 2D to 3D, allowing precise control over scene composition and individual objects. 
We first incorporate 3D Gaussians that are refined through generative priors and optimization techniques. 
Language features from CLIP then introduce semantics into 3D geometry for object disentanglement.
With the disentangled Gaussians, \method allows for manipulation at both the global and individual levels, revolutionizing creative expression and empowering control over scenes and objects. 
Experimental results demonstrate the effectiveness and versatility of \method in scene image editing.
Code and online demo can be found at our project homepage: \href{https://zqh0253.io/3DitScene/}{\textcolor{blue}{https://zqh0253.io/3DitScene/}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a new image editing pipeline that lift 2D data priors, including CLIP, mono-depth, SAM and Stable Diffusion, into a 3D Gaussian Splatting representation for manipulation. This decomposes the scene into a camera and queryable objects that can be rotated and translated in 3D space. The process introduces discontinuities at novel views, which the authors propose to fill in following an image inpainting procedure and using the SDS loss from Dreamfusion. The resulting scene can be rendered to produce an edited image.

### Strengths
Strengths: 
* The authors leverage a broad variety of methods to extend image features to 3D, all of which are well-justified inclusions.
* Authors ablate the main technical decisions in the paper, specifically the different loss terms, CFG scale and object removal.
* Uses GPT4o LLM-as-critic evaluations from past works to automatically evaluate 3D generation quality.
* Writing is focused and practical, highlighting different elements of the design space and clearly explaining each decision the authors made.
* Method is training-free, so it should improve over time as base models improve.
* Figures are well-presented and understandable.
* The importance of the proposed task is clear and the method seems to be a reasonable improvement over existing works.

### Weaknesses
Weaknesses:
* The main weakness of this paper is that it mostly combines existing techniques in a pipeline to improve an application rather than introducing new technical insights. For instance:
  * LucidDreamer used monocular depth to unproject an image into a Gaussian Splatting scene
  * LERF introduced language-embedded 3D representations
  * Dreamfusion introduced the SDS objective
  * Inpainting techniques are already broadly explored in the image diffusion model literature
* Evaluations are very limited, with the user study not being well-explained and including a small number of participants (25) and generated samples (20). This is a known challenge in this problem space, but it would have been nice to see more discussion or contribution in this direction.

### Questions
* What is the runtime of the proposed method and other alternatives? While the 3D representation seems to improve quality, it seems unlikely that this multi-stage method would be fast enough for real use.
* The teaser figure seems to suggest that this process is "hands-off," taking in a text prompt about manipulating the scene and then generating, but I'm having trouble telling if this is actually true. Could the authors please clarify this?
* To what extent does the method begin to fail if there are large baseline camera movements? SDS at low CFG has very limited generation ability, for instance.
* Are there other downstream tasks where this pipeline could be useful? Maybe other instances of image editing?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a method for highly precise 3d scene editing.
The author starts from a single image input, first using estimated depth to init the 3dgs. Use inpainting for both novel view and its depth map. Authors also introduce a language feature distillation loss, so that we will be able to use text to query the gs during inference

### Strengths
The quality is very well. The proposed methods are solid

Authors also conduct a lot of  experiments to compare with multiple baselines.

### Weaknesses
I am afraid that the SAM mask is not accurate, the distill loss may cause some artifacts. Like some of the gaussians in the edge may not be able to match the image prompt. Is it true?
Current method cannot deal with shadow and lightning, like the Rotate the camera then delete the dog case in the teaser
Need more visual results.

### Questions
How long does it take for training one scene?
How long does it take for rendering one image?
I don't understand why “Remove the headscarf then move the camera” case in the teaser can generate the hair of the woman. cause in inference you just manipulate the gs, is ther anything generative that enables this capability?

I pretty much love the paper, if the author can provide more details, I am happy to raise my score.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a scene editing framework that leverages language-guided disentangled Gaussian Splatting. Initially, the input image is projected into 3D Gaussians, which are subsequently refined and enriched through a 2D generative prior. Language features from CLIP are then embedded into the corresponding 3D Gaussians. This representation enables view changes and text-guided editing of the scene.

### Strengths
The proposed technique is well-founded, and the experimental results are impressive.

### Weaknesses
The novelty appears limited, as the proposed method largely combines existing techniques. Projecting a 2D image into 3D Gaussians based on depth information has been demonstrated in works like LucidDreamer, among others. Additionally, embedding language features into 3D Gaussian Splatting (3DGS) and enabling text-guided editing have been explored in methods such as Grouping Gaussian, LangSplat, and GaussianEditor.

It is unclear how the proposed method outperforms prior techniques, such as LucidDreamer and AdaMPI, in Figure 6. While LucidDreamer and AdaMPI exhibit some out-of-range areas, simple inpainting could potentially address these issues. The comparison lacks a quantitative analysis demonstrating the superiority of the proposed method in terms of editing quality or novel view synthesis compared to these existing methods.

Since the method relies on depth maps to generate 3D Gaussian splats, it appears limited in its ability to handle significant changes in view angle. The reliance on initial depth estimation for 3D Gaussian initialization may introduce inaccuracies and limit the method's ability to extrapolate to significantly different viewpoints. This is particularly concerning when the initial depth map is not accurate or complete.

The method seems to only function with generated images rather than real-world inputs. The paper does not provide sufficient evidence to demonstrate its effectiveness on real-world images with diverse lighting conditions, occlusions, and complex backgrounds. The lack of experiments on real-world data limits the practical applicability of the proposed method.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors introduce 3DitScene, a unified framework that employs language-guided disentangled Gaussian Splatting, allowing seamless transitions from 2D to 3D editing. This approach utilizes refined 3D Gaussians informed by CLIP’s language features, enabling precise control over both individual objects and overall scene composition. Experimental results validate the effectiveness and versatility of 3DitScene, demonstrating its superiority over existing methods.

### Strengths
1. 3DitScene effectively integrates various editing requirements into a single framework, facilitating comprehensive manipulation of both scenes and objects.
2. The framework employs language-guided disentangled Gaussian Splatting to produce a detailed 3D scene representation, which enables novel view synthesis and improves object decomposition.

### Weaknesses
The implementation details are not clearly articulated. Specifically, the training and optimization specifics for 3D Gaussian Splatting (3DGS) are lacking, including the number of iterations during initialization and for novel view optimization. Furthermore, the parameters of the loss function, such as λrecon, are not specified. Additionally, the experimental results do not appear to be satisfactory.

### Questions
See what is written in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed a unified framework, 3DitScene, for 3D-aware 2D image editing with different level of granulairies and diverse editing tasks, such as object level editing and camera adjustments.
By converting a single image into 3D Gaussian splatting (3DGS) representation, 3DitScene generates additional 3D content in previously unseen areas via RGB and depth inpainting from diffussion priors. Additionally, it distills CLIP language semantics into the expanded 3D. With the recontructed 3D scene with disentangled 3D semantics, the framework enables editing of both viewing camera and objects in the the image by camera, bounding box and textual controls.

### Strengths
1. The work proposed a 3D-aware image editing pipeline by establishing semantic 3D representation via 2D-to-3D inpainting for novel view completion and language semantics lifting for semantic disenanglements. Under this language-guided disenangled 3D representation, the editing supports object-level maipulatiion and camera controls.

2. Evaluation experiments are extensive for performance and comparisons with baselines. The method designs are validated through conducting ablation studies, exploring various alternative designs, including layout augmentation, losses, depth inpainting strategies.

### Weaknesses
1. While the paper proposed a practical and accurate image editing system, it does not demonstrate the editing procedure for practical use. Also see Questions 1 for further details.

2. Some details are missing for method reproduction and training, such as trainining parameter configuration. It is also unclear about camera configuration, e.g. whether K and T in Eq.1 are always preset and fixed for given single image? More details are needed to facilitate reproduction and editing controls.

Additional concerns can be found in the Questions.

### Questions
1. The paper lacks clarity on the editing process, despite mentioning text, bounding boxes, and camera controls in Sec.3.4.
The detailed operation steps are still ambiguous, and there is no clear editing procedure outlined in paper or video demo.

    From Sec.3.4, it appears that editing primarily involves "text-guided" editing by querying specific object + object manipulation?

    Is "camera control" achieved always by changing camera instrincs and extrinsics parameters? But in Fig.1, it seems that text prompts are also used for control.

    In addition, there's no examples of bounding box usage in the paper.

    I also suggest more editing details such as text prompts in Fig.5 and 6 and video, similar to what is shown in Fig.1.

2. Since the 3D-aware editing is based on explicit 3DGS, and the disenangled object manipulation does not involve whole image re-generation. Accordingly, lighting inconsistencies arise after editng, e.g., shadows do not change appropriately as object moves. Can the lifted semantics help resolve this problem, or do you have any ideas can handle this obvious artifact?

3. Language-semantics 2D-to-3D lifting is increasingly common nowadays, e.g., LERF, LangSplat, Gaussian Grouping. What are the advantages of proposed semantics lifting schemes over these existing works? Additionally, would other language-embedded 2D-to-3D lifting methods should be compatible with this proposed editing framework?

### Soundness
3

### Presentation
3

### Contribution
2
