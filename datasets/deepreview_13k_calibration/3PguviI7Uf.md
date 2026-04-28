# IPDreamer: Appearance-Controllable 3D Object Generation with Complex Image Prompts

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Recent advances in 3D generation have been remarkable, with methods such as DreamFusion leveraging large-scale text-to-image diffusion-based models to guide 3D object generation. These methods enable the synthesis of detailed and photorealistic textured objects. However, the appearance of 3D objects produced by such text-to-3D models is often unpredictable, and it is hard for single-image-to-3D methods to deal with images lacking a clear subject, complicating the generation of appearance-controllable 3D objects from complex images. To address these challenges, we present IPDreamer, a novel method that captures intricate appearance features from complex **I**mage **P**rompts and aligns the synthesized 3D object with these extracted features, enabling high-fidelity, appearance-controllable 3D object generation. Our experiments demonstrate that IPDreamer consistently generates high-quality 3D objects that align with both the textual and complex image prompts, highlighting its promising capability in appearance-controlled, complex 3D object generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces IPDreamer which, by leveraging the complex image prompts for the first time, can generate detailed 3D objects. To achieve this task, IPDreamer first proposes an Image Prompt Score Distillation Sampling (IPSDS) that leverages both RGB features and normal features to help guide the denoising process. The authors further introduce a mask-guided compositional alignment strategy that allows for extracting corresponding features from different images of the same objects, further improving the details of the 3D generation. Extensive qualitative and quantitative experiments have been provided in the paper.

### Strengths
+ The paper is the first time to consider generating 3D objects from complex images. It's quite interesting considering the current progress of the current 2D generative models.

+ The paper is well-written and easy to follow.

### Weaknesses
 - Fig.1 is not clear. It's not able to showcase that existing methods struggle with complex images.

- The results showcased are not quite aligned with the input image.

- The masks in Fig.4 are not quite aligned with the corresponding parts.

- It's hard to see the effectiveness of mask-guided compositional alignment. 

- The results provided in Fig. 5 are not very good.

- What if we apply the best text-to-2D diffusion model to the DreamFusion or other text-to-3D pipeline and carefully design the text prompts? For example, the text-to-2D diffusion model that's capable of generating complex and high-resolution images.

### Questions
Based on my comments on the strengths and weaknesses, I currently still lean a little bit toward the positive rating. I would like to hear from the other reviewers and the authors during the rebuttal.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a text/image-to-3D approach for controlling the appearance of generated 3D objects given complex input images where the subject is not clearly identified.
The proposed approach encompasses multiple components. 
First, IPAdapter image encoder is used to extract image features that are used as texture guidance within the Score Distillation Sampling (SDS).
To be able to handle complex images with multiple components, a mask-guided compositional alignment strategy exploits a Multi-Modal Language Model (MLLM) to provide localization part labels given the image and the provided coarse Nerf model.
Then, cross-attention maps are used to localize those parts by computing attention between the image feature and the textual labels produced by the MLLM.
Finally, the localized parts are optimized jointly to produce a globally consistent 3D object.
Experiments show that the proposed approach produces high-quality results that abide by the guidance image.

### Strengths
- The idea of splitting complex objects into parts that are optimized jointly is interesting and can be potentially employed for more complicated 3D scenes.

- The method section is comprehensive and provides an overview of SDS, making it self-contained.

- The visual quality of the provided results is compelling.

### Weaknesses
 - The paper primarily focuses on controlling the generation of 3D objects from complex input images. As noted in line 537, "IPDreamer addresses the limitations of existing text-to-3D and **single-image-to-3D** methods." However, the paper does not include comparisons with relevant single-image-to-3D methods, such as [1] and [2]. Could the authors clarify why these comparisons were omitted?

- In Figure 7, the qualitative comparison presents different samples for each method. Conventionally, all methods are evaluated on the same samples to ensure consistency in comparisons. Could the authors provide insight into this choice?

- The proposed method incorporates several additional components beyond the standard SDS pipeline, including ChatGPT, SAM, ControlNet, and IPAdapter. Could the authors provide details on the runtime overhead introduced by each component, as well as the overall runtime?

- The method illustration in Figure 2 appears challenging to interpret. It does not effectively aid in understanding the proposed pipeline, and I found it difficult to correlate it with the text. A more intuitive figure might improve readability and clarity.

- As noted by `PRnJ`, the generated 3D objects do not align with the input image (Figure 1, 5 ). This is a fundamental requirement for image-to-3D approaches, which is not fulfilled by your method. For artists, it is crucial that the generated 3D assets align well with their input images.

- I understand that your approach is inspired by IPAdapter in Text-to-Image diffusion models, but I am still wondering how it could be useful in the 3D generation domain! In text-to-3D, the input is text, and the model is free to generate any style, while for image-to-3d, it needs to abide by the input image. Your approach seems to be in the middle between the two cases, making it difficult to position and compare against existing approaches for 3D generation.

- I still have concerns about using different samples for different methods in Figure 7. To be able to position your approach amongst existing approaches, the same samples should be used for all comparisons. "The shinning sun" example that you showed at the bottom of the figure is not sufficient to judge.

- The caption of table 1 and 2 say "text-to-3D", but both Zero123 and SV3D are "image-to-3d".

### Questions
- I do not understand Figure 1b. What is being generated, a 3D shape or an image? both the leaves and the water ripples look like images!

- What is the difference between equations (11-13) and (14-17)? Are both used during optimization?

- What is the impact of employing the super-resolution model, ControlNet tiling, on the final generated quality?

### Soundness
1

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
2

### Summary
The paper introduced a controllable 3D object generation approach using image prompts (similar to style transfer). The proposed IPDreamer approach is a novel method that could capture the intricacies of appearance features from image prompts, and could generate high fidelity and controllable 3D objects. The approach is tested on some public benchmarks with user studies available as well, and was proven to be effective.

### Strengths
- The paper is tackling an important and very challenging 3D genAI problem. Comparing to existing approaches, the IPDreamer could edit the objects using more complex image prompts
- The introduced prompt score distillation sampling approach is a reasonable formulation that builds on existing SDS approaches, and the masked-guided alignment strategy seems to be highly effective 
- Experimental results suggest that the approach is better comparing to other counterparts. User studies is also provided.

### Weaknesses
I think this is a nice paper and a good extension to many of the existing approaches. The final output of the algorithm seems to be good enough. I do have a few clarification questions that I hope the authors could address in future revisions of the papers:
- The paper leverages GPT-4v as MLLM inputs. How accurate should the MLLM be, in case people don't have access to this advanced MLLM algorithm? Would the output become much worse?
- It's very nice to conduct user studies for genAI works in general. Could authors provide more demographics information in the appendix section? (age, gender, background, etc)
- I don't fully understand Fig 1b, especially the right images -- what is the contents in the input and what is the actual real-world application of this particular input/output pair?

### Questions
See the weakness section

### Soundness
3

### Presentation
2

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
This paper present a novel method to capture intricate appearance features from the Image prompts, which is further used to enhance the alignment of the image prompts with the generated objects. Experiments demonstrate the proposed method generate objects which is well-aligned with image prompts, show better ability in complex generation.

### Strengths
* The paper proposes a novel framework for 3D generation by breaking an image prompt into several parts and adopting a multi-guidance optimization process. Experiments demonstrate the effectiveness of the proposed framework.
* The idea of the paper that breaks the complex images into several parts is interesting and good. Breaking a complex thing into parts makes a hard problem much easier.

### Weaknesses
 * The written of the paper is not so clear, some details are lack:
  * The description on how to adopt GPT-4v to generate localization prompts is lack in the paper.
  * In Figure 1 (b), the author gives comparison between VSD and IPSDS on text-based generation. But is the proposed method IPSDS need an image prompt? How to compare IPSDS with VSD on text-based generation? Moreover, for the cases in Fig (a), could the author provide the images parts extracted from the reference image of the castles. It’s hard to understand how could we break such things into parts.
  * For eq.9 and eq.10,the author highlights that “they localize the features of the multiple images onto 3D object” in many places such as Line 321-322, 349-350, which makes me very confused. I think the author is adopting eq.9 and eq.10 to fuse information from different image parts to do SDS loss. Therefore, this description is inaccurate and leads to misunderstanding. 、
  * Some annotation in the equations are missing, like $Z$ in eq.9.
* In line 360, the author declares that a global optimization is further needed, which is achieved by simply concatenating all the features from the multiple images instead of adopting a mask based strategy. Why we need such a global optimization? What if we directly adopt global optimization without the mask-guided one? I think the author should provide such evaluation.
* Finally, I think the evaluation of the paper is not enough. The accuracy of adopting SAM and GPT-4v to break into parts is not evaluated. Moreover, I think the author should provide more visualization examples on the extracted image parts together with the generation results, which will make overall process easier to understand.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2
