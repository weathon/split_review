# DMV3D: Denoising Multi-view Diffusion Using 3D Large Reconstruction Model

- Decision: Accept
- Scores: 8, 6, 8, 1

## Abstract
We propose \ourmethod{}, a novel 3D generation approach that uses a transformer-based 3D large reconstruction model to denoise multi-view diffusion.
Our reconstruction model incorporates a triplane NeRF representation and can denoise noisy multi-view images via NeRF reconstruction and rendering, achieving single-stage 3D generation in $\sim$30s on single A100 GPU.
We train \ourmethod{} on large-scale multi-view image datasets of highly diverse objects using only image reconstruction losses, without accessing 3D assets. We demonstrate state-of-the-art results for the single-image reconstruction problem where probabilistic modeling of unseen object parts is required for generating diverse reconstructions with sharp textures. We also show high-quality text-to-3D generation results outperforming previous 3D diffusion models.  
Our project website is at: \url{https://justimyhxu.io/projects/dmv3d/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a 3D generation method that uses a transformer-based 3D large reconstruction model to denoise multi-view diffusion. The proposed method supports both text- and image-conditioned 3D generation. Experimental results seem promising.

### Strengths
The idea of directly denoising a triplane-based NeRF is interesting. The result of multi-view diffusion is promising.

### Weaknesses
1. Does the method use a pre-trained stable diffusion model or train the DDPM from scratch? If from scratch, how is the generalization ability guaranteed?

2. For multi-view diffusion, what is the number of views for training and inference?

### Questions
Please see the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an approach to 3D generation via a single-stage diffusion model. By denoising multi-view image diffusion, the authors aim to generate realistic 3D assets. Central to this methodology is a large transformer model that processes multi-view noisy images to reconstruct a clean triplane NeRF, subsequently yielding denoised images through neural rendering. The proposed method showcases flexibility, supporting both text- and image-conditioning inputs, and claims rapid 3D generation without requiring per-asset optimization. The approach is evaluated and shown to be superior to previous 3D diffusion models in certain domains.

### Strengths
(+) The paper showcases impressive results in 3D generation compared to prior methods. 

(+) The method's ability to accommodate text- and image-conditioning inputs augments its versatility, making it potentially suitable for diverse applications.

(+) The paper is well-structured and clearly explains both the methodology and foundational design choices.

### Weaknesses
Although the paper showcases promising results and a solid methodology; however, its level of novelty is unclear:

- It appears that the proposition combines techniques that have been used before. The 3D diffusion part of the proposal seems to have been influenced by "Viewset Diffusion (ICCV 2023)", while the design and training approach of the large-scale transformer model is similar to "LRM: LARGE RECONSTRUCTION MODEL FOR SINGLE IMAGE TO 3D", which was also submitted to ICLR 2024.
- Concerns have been raised about potential overlap with the LRM manuscript, questioning submission singularity.

Besides, a balanced perspective is lacking due to the absence of discussion on the paper's limitations, which could provide valuable insights for potential areas of improvement.

### Questions
- Given the inherent training characteristics of diffusion models, how does DMV3D achieve a training timeframe analogous to LRM? It would be helpful if the authors could provide an explanation.
- It is important to clarify the extent of overlap between this work and the LRM submission in order to understand the distinctiveness of the contributions in this manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method to generate novel 3D objects based on a diffusion model that encloses a large reconstruction model. To leverage the strong generative power of 2D models while improving the 3D consistency of the generated objects, the diffusion model operates on the domain of multi-view images and internally learns a transformer-based reconstruction model to build a 3D representation, which is later rendered into denoised output images. In order for the model to generalize across different categories, the reconstruction model uses the DINO features to bootstrap the features used for deriving tokens. Results show that by training jointly on the Objaverse dataset and MVImageNet dataset, the model is able to generate diverse shapes, conditioned either on images or texts. The usage of the transformer-based large reconstruction model improves the 3D consistency while maintaining a good generation quality.

### Strengths
- The paper is clearly written and well presented. The notations are clear and the illustrations are informative. It's easy to read and understand most of the technical details and design choices.
- Though conceptually similar to, e.g., MVDiffusion and RenderDiffusion (or diffusion with forward models), the method elegantly combines the advantages of both works with the help of a generalizable large reconstruction model using transformers, hence lifting the previous constraints within only one single category.
- The method naturally enables conditioning over images by fixing the diffusion variables, leading to a new scheme for bridging 2D and 3D domains.
- The generated shapes are of high quality and surpass the baselines by a considerable margin.

### Weaknesses
- In contrast to Image-based diffusion models, the runtime efficiency might be compromised since the reconstruction model operates during every iteration of sampling. Investigating whether the reconstruction can be repurposed or distributed over the intermediate denoising phases could be insightful, especially since the current intermediate reconstructed model is discarded (would be great if they could be visualized), leading to potential wastage.

- The textures produced lack sharpness. Exploring the proposed framework's performance on higher-resolution images and 3D triplanes would be intriguing. Additionally, employing a hybrid representation that decouples geometry and textures could yield enhanced results.

### Questions
- How the camera viewpoints are sampled during the training process? Would the reconstruction model easily fall into a local minima where the 3D results become trivial by generating planes that are parallel to the image planes?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes DMV3D, a 3D generation approach that uses a transformer-based 3D large reconstruction model to denoise multi-view diffusion. The reconstruction model incorporates a triplane NeRF representation and, functioning as a denoiser, can denoise noisy multi-view images via 3D NeRF reconstruction and rendering, achieving single-stage 3D generation in the 2D diffusion denoising process. The model is trained on large-scale multi-view image datasets of extremely diverse objects using only image reconstruction losses, without accessing 3D assets.

### Strengths
1. The first contribution of this paper is to scale 3D diffusion generative models to very diverse categories and objects. Previous models such as DiffRF, etc. can only generalize within some shapenet like datasets with no more than 13 categories.

2. The model demonstrates a novel method to conduct multiview diffusion. Instead of build attentions across views like mvdreamer or syncdreamer, they use attention to attend with learnable triplane tokens and with each other, therefore incorporating the 3D spatial prior in the process.

3. The model shows good results of 3d generation, especially high quality geometry, which alwyas fail in SDS or nerf2nerf lines of works.

### Weaknesses
1.It seems the model learns from the objaverse and mvimagnet, which contain mostly single objects or separated objects. even the examples in out of domain results, in figure 6, the objects are not complicated as people use in SD-based models.

### Questions
1. As mentioned in weakness 1,  I would like to see some results of "bunny seating on pancake", this kind of generation. Even it is hard to do text to 3d, since the training set doesn't have compound objects, is it possible to do 2d conditioned 3d generation with this kind of prompt?

2. The author mentioned in the 2d conditioned 3d generation task, they do not add noise to the reference view, however, some of other diffusion models usually also add noise to the reference view and each step, use the gt x0 of the that view and add new noise in ancestral sampling. The logic behind is the model is trained with noise images paired with the corresponding time step embedding, the clean image strategy will shock the model in inference. I wonder, in inference, if this clean ref image strategy can bring benefit over adding noise from x0.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
