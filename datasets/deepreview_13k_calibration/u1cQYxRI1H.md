# Scaling In-the-Wild Training for Diffusion-based Illumination Harmonization and Editing by Imposing Consistent Light Transport

- Decision: Accept
- Avg Score: 10.00
- Scores: 10, 10, 10, 10

## Abstract
Diffusion-based image generators are becoming unique methods for illumination harmonization and editing. The current bottleneck in scaling up the training of diffusion-based illumination editing models is mainly in the difficulty of preserving the underlying image details and maintaining intrinsic properties, such as albedos, unchanged. Without appropriate constraints, directly training the latest large image models with complex, varied, or in-the-wild data is likely to produce a structure-guided random image generator, rather than achieving the intended goal of precise illumination manipulation. We propose Imposing Consistent Light (IC-Light) transport during training, rooted in the physical principle that the linear blending of an object's appearances under different illumination conditions is consistent with its appearance under mixed illumination. This consistency allows for stable and scalable illumination learning, uniform handling of various data sources, and facilitates a physically grounded model behavior that modifies only the illumination of images while keeping other intrinsic properties unchanged. Based on this method, we can scale up the training of diffusion-based illumination editing models to large data quantities (> 10 million), across all available data types (real light stages, rendered samples, in-the-wild synthetic augmentations, etc), and using strong backbones (SDXL, Flux, etc). We also demonstrate that this approach reduces uncertainties and mitigates artifacts such as mismatched materials or altered albedos.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper introduces an extremely well-generalized illumination control model for recent diffusion models. Illumination control is essential for numerous artistic effects and is key to driving the mode of generated imagery. Recent methods struggle to capture this control due to the lack of large-scale real-world datasets. The key idea of the paper is to use the linearity of lighting as a constraint, i.e., the blending of two images of the same scene under two different illuminations is the same as blending the two illuminations and applying them to the scene. The authors collect a high-quality dataset from various sources using numerous recent pre-trained models to generate a large-scale paired dataset. The effectiveness of the idea is extremely well-demonstrated both qualitatively and quantitatively. The resulting images have extremely consistent materials, even so consistent that high-quality normal maps can be extracted using multi-light generation.

### Strengths
This is an extremely well-written and well-motivated paper; I believe this is a really good example of a highlight paper. Key points I have considered during reviewing the paper:
* The paper proposes a well-working solution to an extremely challenging task. Lighting and material are only observed in a highly intertwined manner, making it difficult to control only one without changing the other. Previous methods tried to solve this problem with paired synthetic datasets, albeit falling into a domain gap. 
* The proposed dataset provides a really important insight, which can be important for the community: using pre-trained models and synthetic degradations can still provide helpful signals. 
 * The light transport consistency is a simple but very effective way to enforce consistency. However, the idea is not new, earlier methods required multi-light datasets to utilize a similar constraint. This paper shows a way how to realize it with in-the-wild samples. 
* The approach is extremely well-documented together with practical insights and considerations.

### Weaknesses
This is an extremely good paper overall; I just have minor comments, which might help improve the writing quality.
* It would be great to highlight more which datasets are used for which parts of the training. Potential cause for confusion: the pipeline figure shows that the training required I_d, although I_d is used only for in-the-wild samples, but then it is not clear where the other components of the dataset are used. 
* Some additional related works, which could be discussed:
  * [Shape-form-shading](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2013/EECS-2013-117.pdf) - how it relates to the current normal extraction
  *  [LightIt](https://peter-kocsis.github.io/LightIt/) - illumination control with a generated paired dataset, where similarly an automatically relit image is used as input during training to avoid domain gap. 
* It would be good to highlight the best metrics with bold in Tab. 1.

### Questions
It would be helpful for easier understanding to better describe the followings:
* More details would be helpful on the synthesis of L1 and L2 (L.319), probably even some visuals in the supplementary. 
* More qualitative samples from the dataset with all the methods used to generate the synthetic components.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes a physically inspired relighting scheme for training a lighting-aware generative model. The idea of imposing consistent light (IC-Light) is based on the observation of the real world; i.e., an object’s appearance under different illumination conditions is consistent with its appearance under mixed illumination. To this end, the authors train a generative model conditioned by lighting environment maps and an additional light consistency loss. In order to train the model effectively, the authors introduce several strategies for data collection, including rendering intrinsic components from a synthetic dataset, augmenting the existing dataset with random shadows, and separating the foreground and background. They manage to collect more than 10 million images for final training. The results of the proposed method appear to be astonishing. The authors also demonstrate side applications such as image harmonization and surface normal estimation, both of which are object-centered.

### Strengths
- The results are very strong. The performance of the proposed IC-Light is astonishing, and it can be further improved with a stronger generative model as the backbone.

- The method is sound. Although the fundamental observation (the intrinsic component is always invariant to lighting) is not new, the authors are able to effectively leverage this observation in the training of generative models. They thoroughly explain all the details and intuition behind their method.

- The contribution is significant, impacting not only the vision and graphics communities but also holding great commercial potential for the photography and movie industries.

### Weaknesses
 - The fundamental observation of this paper is common knowledge in the computational photography and low-level vision communities. Unfortunately, I found that the authors overlooked a large portion of the literature in these fields, especially in terms of intrinsic image decomposition. I noticed that the authors use several IID methods to generate the intrinsic components and mention them in the supplemental materials; I think the authors should also list them in the main paper. Specifically, the paper would benefit from a more thorough discussion of how their approach relates to classical intrinsic image decomposition techniques, such as those based on Retinex theory or optimization-based methods, and how the generative approach offers advantages or addresses limitations of these traditional methods. The current discussion is too brief and does not adequately contextualize the work within the broader field.

- The quantitative experiments are somewhat limited (including details on the rendering data, e.g., how distinct they are from those in training dataset). Additionally, the numerical and visual comparisons could be improved by including methods like Neural Gaffer. The paper lacks a detailed analysis of the generalization capabilities of the model. It is unclear how the model performs on datasets with different characteristics than the training data, and the paper should include experiments that explicitly test this. Furthermore, the quantitative metrics used should be more diverse and include metrics that specifically evaluate the quality of the relighting, such as perceptual metrics or metrics that compare the consistency of shading and shadows.

- Some figures in the paper should be better explained:  For Figure 4 and 5-(c), what is the prompt/condition for the background/lighting? The lack of clarity in the figure captions makes it difficult to understand the specific conditions under which the results were generated. This makes it hard to assess the robustness and reliability of the method. The prompts and conditions for the background and lighting should be explicitly stated in the captions or in the main text.

- L. 427 and L. 431: " shadow maps" should be shading maps.

### Questions
- Although the IC-Light scheme works very well for foreground relighting, would it perform equally well for general scene-level relighting? For instance, could the proposed method achieve effects similar to turning on or off a visible light source within a scene, as shown in the paper "Physically-Based Editing of Indoor Scene Lighting from a Single Image" by Li et al., ECCV 2022?

- In Figure 1, the authors demonstrate impressive lighting effects. I am curious whether the method consistently provides such high-quality, precise lighting effects, or if it requires careful tuning of the prompt and seed to achieve this result.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper proposes a method to generate illumination and background from given foreground reference images and text prompts. The paper's key contribution is to use a new consistency loss, which makes the foreground appearance consistent under different lighting conditions. The paper argues that thanks to the new loss functions, the fine-tuning of diffusion models can be scaled up to over 10 million samples. Experimental results show both qualitatively and quantitatively superior image editing results compared to existing methods.

### Strengths
### Loss design
The design of the new loss function is reasonable. Adding the appearance consistency under a mixed lighting environment is somewhat inspired by the mixing strategies in augmentation and regularization in neural network training, while using that regularization for image illumination editing would be new to me.

### Large-scale training
The paper fine-tunes major image generation models with over 10 million samples, resulting in an immediately useful tool for image editing.

### Weaknesses
### Unclearness of the releases of the data and implementation
From the paper, it is unclear whether the authors will release the data and implementations or intend to provide a black box web tool for users. This lack of clarity hinders reproducibility and further research. The absence of details regarding the dataset's composition, including the diversity of foreground objects, lighting conditions, and background scenes, makes it difficult to assess the generalizability of the proposed method. Furthermore, without access to the implementation details, it is challenging to verify the claims made about the effectiveness of the proposed consistency loss and the large-scale training process. The community would greatly benefit from a clear plan regarding the release of the model weights, training code, and the dataset used for fine-tuning.

### Questions
I consider that the proposed method and the resulting tool will be immidiately useful for many users. I would like to ask the authors how it will be released.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper presents a diffusion-based method for image illumination control. Compared to vanilla T2I diffusion models, the proposed model additionally inputs a degraded or altered lighting image as a reference and an HDR environment map as lighting condition, and outputs the image under the target lighting. The key of the method is the incorporation of lighting consistency loss and the use of a variety of data, including 3d renderings, processed in-the-wild data, and OLAT light-stage data. The proposed method scales well on both large-scale data and different base models and advances other methods both qualitatively and quantitatively. The authors also provided additional applications, like background-conditioned illumination control and normal estimation.

### Strengths
The paper is in general very good, with many strengths:
1. The data preparation pipeline is very solid
    1. The authors assembled data from diverse sources for training, significantly enhancing the model's generalizability.
    2. For in-the-wild data, the authors utilized various intrinsic estimation methods, making the pipeline robust and avoiding inductive bias from any single method.
2. The proposed lighting consistency loss is novel and effectively prevents training degradation.
3. The training strategy demonstrates excellent scalability, is applicable to various diffusion base models and is capable of handling large-scale in-the-wild images.
4. The method achieves state-of-the-art image quality among diffusion-based lighting control methods.
5. The method also supports alternative lighting control interfaces, such as background condition.
6. The lighting consistency can be validated through the normal estimation application.

### Weaknesses
Some small weaknesses exist in the paper:

Formulation:
1. Only linear HDR images have light transport additivity, but natural images and images generated by diffusion models are usually tone-mapped LDR images, which do not have additivity. How is this misalignment handled?
2. There is material ambiguity in the single input image as different material-lighting combinations can yield a similar appearance. Hence I wonder how much the prompt and seed affect the model’s material estimation / final lighting result.

Implementation details:
1. Lighting consistency loss:
    1. To add the lighting consistency regularization during the training of latent diffusion models, the authors replaced the sum of two RGB-space images with an MLP that operates in latent space. The MLP works as a soft proxy, but does this MLP really work as intended without any other regularization?
    2. Also, the loss is derived using x_0 prediction, which is not very stable and can have low SNR when t is large, is there any special design regarding this issue?
2. Normal estimation:
    1. The formulas for normal estimation are not correct. Equation 8 should be minus rather than average. It is also not proper to call these two directions N_green and N_red. They should be defined in the world space with range [-1, 1] and visualized as (N + 1) / 2.
    2. It is better to use a consistent coordinate for the normal maps. In Fig (6), the man in the middle row has a different normal map specification from the examples on the last row, with R and G representing opposite directions in these two examples.

I would raise my score if the above problems were explained.

Besides, in the image results:
1. Some specular highlight seems to be baked in or show a strong correlation to the input image. E.g. the specular highlight on that car in Fig. 1, and on the helmet in Fig. 4
2. Some images have wrong global illumination (GI) effects, e.g. the ice-cream example on supp material page 6, has two shadows in opposite directions.

### Questions
I also have some small and less important questions:

Implementation details:
1. The reliability of DiffusionLight depends on the FOV of the image, is there any special handling on small FOV images?
2. To estimate environment maps from in-the-wild images, the original image is divided by albedo to obtain a shading map, and then projected to form the environment map: how to handle visibility/occlusion? e.g. on a concave object. Also, if the original image itself is already over-exposed, it will produce a wrong environment map even with HDR.
3. L242, the authors use CLIP for lighting filtering. However, as the text prompt is not enough for the lighting description, I wonder if the CLIP really has a good embedding for these lighting-related keywords. How effective does this filter work? Will something like an aesthetic score help here?
4. L246, do you mean “image-space” rendering? Does this image-based rendering pipeline consider GI? E.g. self-occlusion and inter-reflection. If not, is this the cause of some wrong GI effects?
5. For background conditioned inference, when only providing background, is env map L set to 0? Or is an environment map estimated from the background condition?
6. For normal estimation, when generating a shadow map, is 3 channels averaged? I can see some color in Fig 5 (c)’s shadow maps (which should be monocular), but it’s understandable for diffusion models. Besides, will specular highlights degrade this estimation? I'm also a little confused about the division by two in equation 8 and the way of ambient computation (using the average of four images instead of using the minimum value of all images). Can you clarify this?

Extra results:
1. Normal quantitative results: how well does the normal align with a real 3D normal map? Or what does the shape look like after running a normal integration on the estimated normal map?
2. How well is the temporal consistency when continuously changing the environment map L during inference?

Extra question:
1. Do you try to also impose lighting consistency on foreground and background?

I would also be happy to raise my scores if the authors provide answers or results regarding these questions.

### Soundness
3

### Presentation
4

### Contribution
4
