# 3D Object Manipulation in a Single Image Using Generative Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 8, 5, 6

## Abstract
Object manipulation in images aims to not only edit the object presentation but also gift objects with motion. Previous methods encountered challenges in concurrently handling static editing and dynamic motion applications, while also struggling to achieve realism in object appearance and scene lighting. In this work, we introduce OMG3D, a novel framework that integrates the precise geometric control with the generative power of diffusion models, thus achieving significant enhancements in visual performance. Our framework converts 2D objects into 3D, enabling user-directed modifications and lifelike motions at the geometric level. To address texture realism, we propose CustomRefiner, a texture refinement module that pretrain a customized diffusion model to align the style and perspectives of coarse renderings with the original image. Additionally, we introduce IllumiCombiner, an lighting processing module that estimates and adjusts background lighting to match human visual perception, resulting in more realistic illumination. Extensive experiments demonstrate the outstanding visual performance of our approach in both static and dynamic scenarios. Remarkably, all these steps can be done using one NVIDIA 3090. The code and project page will be released upon acceptance of the paper.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces OMG3D, a framework for object manipulation in images that addresses both static editing and dynamic motion generation challenges, while also improving the realism of object appearance and lighting. OMG3D integrates precise geometric control with the generative capabilities of diffusion models, converting 2D objects into 3D for user-directed modifications and lifelike motions. To enhance texture realism, it proposes CustomRefiner, a module that refines textures using a customized diffusion model to match the style and perspective of the original image. Additionally, the authors introduces IllumiCombiner, a module that adjusts background lighting to create more realistic illumination, aligned with human visual perception. The authors conducted extensive experiments show that OMG3D achieves good performance in both static and dynamic applications.

### Strengths
- The proposed method utilizes explicit 3D generation capability to ensure both static and dynamic manipulation. While other 2D-based methods fail to do so.
- The utilization of HDRi for realistic lighting.
- Visual quality is good.

### Weaknesses
 - Lack of technical novelty, most of the presented techniques exist. The proposed method seems to put them together nicely to produce a few good results. E.g., CustomRefiner is a combination of depth-controlnet, dreambooth lora, and differentiable rendering on UV map, IllumiCombiner is a combination of HDRi estimation and virtual-plane rendering.
- The idea of realistic lighting is interesting to me, but I am not convinced by the proposed method. The real light transport is more complex than by linearly modulated two terms. Solving global illumination is a very difficult problem with a single image. The proposed method can only handle simple objects.

Minors:
- L216: IlluminCombiner should be bold.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method for inserting 2D objects into 3D and letting users modify them. The method involves training a customized diffusion model added with a lighting processing module.

### Strengths
They can combine precise geometric control.
They can handle better texture renderings.
They can handle lighting better.

They offer complete comparison to showcase their results with other state-of-the-art methods.

### Weaknesses
They can try comparison with VSD loss. Or provide more visual examples in the supplementary results.

### Questions
Have you tried to insert real humans instead of animation? Want to see that result.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors present a framework named OMG3D for object manipulation from images. Similar to Image Sculpting (Yenphraphai et al. 2024), OMG3D first segments the object and reconstruct a mesh in 3D. The mesh can then be mainuplated by 3D manipulation software. To address the loss of details in the rendered results, the authors propose a texture refinement module, named CustomRefiner, which performs gradient backpropagation directly to the UV texture map through differentiable rasterization. To achieve realistic lighting and shadow effects, the authors propose a lighting processing module, named IllumiCombiner, which estimates lighting from the background images and renders shadows that align with the scene.

### Strengths
+ Compared with Image Sculpting, OMG3D can produce results showing better texture alignment with the original image and achieve realistic light and shadow effects.
+ The idea of gradient backpropagation to the UV texture map through differentiable rasterization sounds novel.
+ The idea of estimating a spherical light from the background image and applying it in the rendering pipeline to achieve realistic shading and shadow sounds logical.
+ The qualitative results look convincing.

### Weaknesses
 - A large part of the proposed pipeline comes from Image Sculpting. For instance, the "precise geometric control" is made possible by object segmentation followed by image-to-3D. The generative enhancement used in driving the UV-texture optimization also appears to be identical to that in Image Scuplting. This makes this work a bit incremental and lowers its novelty. Overall, this work can be regarded as an integration of Image Scultping (for 3D model manuipulation) and DiffusionLight (for introducing light and shadows effects).
- The key difference between this work and Image Sculpting is the replacing of direct rendered image enhancement with UV-texture optimization. However, the authors fail to discuss/analyze in detail why UV-texture optimization can produce better results than direct image enhancement. Specifically, the paper lacks a discussion on the limitations of directly enhancing rendered images, such as potential artifacts or inconsistencies that UV-texture optimization might avoid.
- The light processing and plane creation part is not very clear. The paper does not adequately explain how the estimated spherical lighting is integrated with the scene, nor does it detail the process of creating the transparent plane for shadow capture. The lack of clarity makes it difficult to understand the practical implementation of these components.

### Questions
- In Fig.4, there are two "(ours)". It seems that the one in the 2nd column is a typo.
- How is c_a in (6) used to correct the color of the estimated lighting? 
- What are I_d and I_c in (7)? How to adjust I_d "to maintain the object's saturation while ensuring that shadows remain evenly distributed in all direcionts"?
- How is the normal vector from the depth map being used in rendering shadows?
- Is the motion manually defined for the results of Image Scultping? How come the pumpkin jumping example shows lack of motion?

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
3

### Summary
The paper proposes OMG3D for 3D editing of objects. It takes an image and produce 3D assets with high quality texture and lighting estimation. Then 3D editing including motion and shadow effects can be added in common 3d editing softwares. To get high-quality results, it proposes a texture refinement and a lighting estimation module in the image-to-3d stage. The method is compared against image and video generation models using user study and LLM-based evaluations, under which it works better in realism and consistency axis, and works better or on-par in terms of image/text alignment.

### Strengths
- The paper is well written and the video demo is well made.
- The method produces high-quality results, and those can be plugged into existing graphics pipelines relatively easily due to the explicit modeling of geometry, texture and lighting.
- The authors did a good job in quantitative evaluations and comparisons, including some recent image/video generation methods.
- The method is lightweight and can run on a single 3090 GPU.

### Weaknesses
 - Is the comparison to images/video models fair? For instance, the pipeline introduced in this paper involves human editing (e.g., rigging and animation) while the baselines does not. Although I like the fact that the comparisons reflect the final quality, the different level of human involvement can be made clearer and discussed.
- It would be useful to explicitly state the steps that require manual intervention and differentiate those from the automatic component of the method through a table. For instance, intensity enhancement needs manual adjustment but lighting estimation does not.
- Lack of ablations and comparison to image-to-3D methods. Since this is main technical contribution, it would be useful to ablate the design choices that are different from existing methods, and report quantitative results showing their individual contributions to the overall performance. For instance, how much does DDIM inversion help, how much does dreambooth customization help, how much does depth controlnet help, and how much does feature injection helps. Ideally, by ablating each of the designs one after another, it can reach a known baseline.

### Questions
- How is depth control incorporated? Is it added to SDXL during Dreambooth finetuning? What does the denoising function look like?

- How to deal with multiple planes (e.g., table and ground) in plane creation process? Since depth from Depth Anything is up to scale, how to adjust the plane to be in contact with the object?

- How is the material property specified during rendering in the editing stage?

### Soundness
3

### Presentation
4

### Contribution
2
