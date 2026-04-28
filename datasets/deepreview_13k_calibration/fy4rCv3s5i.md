# Neural Lighting Priors for Indoor Scenes

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
We introduce Neural Lighting Priors, a learned surface emission model for indoor scenes. Given multi-view observations as well as the geometry of a scene, we decouple spatially varying lighting and material parameters. Existing inverse rendering methods typically use hand-crafted emission models or require a large number of views to better constrain the highly ambiguous appearance decomposition task. We aim to overcome these limitations by introducing an expressive learned parametric emission model and utilizing semantic information to sufficiently constrain the optimization, thus allowing us to infer light sources, even if they are not visible in the observations. We model the emitted radiance with a neural field parameterized by the emitting direction and a local latent code stored in a voxel grid. At test time, we fit the local latent codes to the scene using differentiable path tracing, optimizing the reconstruction loss. Our reconstruction allows us to insert virtual objects in a scene and gives us control over the emitters to change their emission color and intensity. Thanks to the learned 3D prior, our method requires fewer views than state-of-the-art relighting methods, gives more control, and also improves the relighting quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a learned surface emission model for indoor scenes, given sparse observations of the scene and ground truth geometry. The model is conditioned on learned semantic features as well as lighting features learned from a large collection of scenes. A test-time optimization of emission and spatially-varying materials is applied, to finetune the features on sparse scene observations, with view synthesis loss and regularization. The paper is trained on synthetic scenes adapted from 3D-FRONT and tested on both synthetic and real-world scenes.

### Strengths
[1] Novelty in model design. The paper takes inspirations from several previous works to design a model model which leverages learning-based priors for initial prediction, yet allows for test-time optimization (NeRF-like architecture conditional on grid features) for refinement with physics-based rendering formula. Thanks for those considerations, the method enables a wide range of applications including lighting editing & scene relighting, virtual object insertion & relighting, and produces decent results with sparse view inputs.

[2] The paper is generally well written, with details extremely well-documented. The evaluations are extensive, including both qualitative and quantitative results on numerous inverse rendering tasks, and demonstrate noticeable improvement over multiple prior arts.

[3] The paper also proposes a dataset as an extension to 3D-FRONT, with photorealistic physics-based lighting, which will be valuable to the community once released.

### Weaknesses
[1] Experimental setting with GT geometry.

The biggest concern regards the setting of the paper. The paper assumes ground truth geometry, the acquisition of which in indoor setting is a challenging problem by itself, especially in sparse-view setting where the paper claims benefits from its learned priors. Without demonstrating results in cases of **estimated** geometry (especially with sparse views, e.g. with methods like MonoSDF), it is difficult to predict how the method will behave with estimated geometry. Previous works (e.g. FIPT, IRIS) have shown it is entirely possible to estimate mesh-based geometry based on dense view inputs and optimize in a similar paradigm to this paper, and works like MonoSDF have shown the possibility of reconstructing fine geometry with sparse-views. As a result, it is entirely possible and essential for the paper to clarify and evaluate in this setting.

[2] Outdated and incomplete comparison.

Discussion and comparison on some of the most recent works are missing or incomplete, notably FIPT which is a strong baseline (discussion and comprehensive comparison is doable); MILO which is a baseline from FIPT. Code base and datasets (including both synthetic and real-world scenes) are publicly available from early 2023 by FIPT. Why is comparison against FIPT only provided in Fig. 9 and not in other comparison, given the two methods are directly comparable and FIPT is the SOTA baseline (over IPT).

[3] BRDF representation.

The BRDF model is limited to Lambertian diffuse model in this paper, as opposed to account for high-frequency specular lighting as in FIPT, MILO and IRIS. Although the diffuse assumption might work as a good regularization in the presence of strong specular effects VS sparse views (which is a likely explanation for artifacts from FIPT and INR in Fig. 9), without modeling specular component it is not possible to recreate **any** specular effects in downstream applications, and will likely break the view-synthesis objective in scenes with complex lighting. It is crucial for the paper to clarify on the choice, and experiment with additional of specular component to its BRDF representation for a refreshed comparison in Fig. 9.

[4] Insufficient ablation.

(a) With/Without test-time optimization. The method depends on test-time optimization to finetune emission and estimate BRDF for to a specific scene, starting from pre-trained features. It will be interesting to observe how the proposed method behaves with and without test-time optimization, especially considering the sparse/single view setting might cause issues like overfitting in optimization.

(b) Path-tracing in sparse view setting. It is not described how path tracing is implemented with sparse-view/a single view. Do we assume complete geometry with sparse-view observations? If yes how is this a practical assumption. Moreover, with limited view coverage and limited number of paths, it is not clear about how the BRDF and emission look like especially in little/not observed regions.

(c) BRDF estimation quality. As described above, considering the method recovers both BRDF and emission, no BRDF results and comparisons are included. It is of crucial importance to observe the results from a physically based inverse rendering method and conclude how the method behaves in the setting of sparse views, considering IPT heavily relies on dense views to reduce biases and promote spatial consistency.

(d) Emission estimation quality. Similar to mentioned above, no separate results on emission estimation/emission masks are provided. Those results are crucial to understand whether the model is able to correct estimate large emission values for emitters and suppress emission for non-emitters, as is done in the IPT paper.

(e) More results on complex scenes and real-world scenes. In case of scenes with complex lighting, geometry and materials (e.g. cluttered furniture, materials with complex patterns and appearance heavily coupled with shadow/highlights, as well as numerous small lamps, windows), and more importantly real-world scenes, evaluation needs to be done to demonstrate the effectiveness of the proposed in challenging and diverse indoor environments. Real-world scenes are readily available for FIPT and has become a popular benchmark in recent works along this line (e.g. IRIS).

[5] Extra clarification needed.

(a) in Fig. 9: why do three methods use different geometry? What happens if all use the same geometry, and same BRDF representation (by removing specular term from FIPT, or adding specular to this method). Otherwise it is not a fair comparison.

(b) Modifying local lighting features for light editing. Given the method output no notion of emitters, but dense emission, the claim to 'control over the emitters' might be questionable as the method relies on heavily post-processing to mask out the emitters, and re-render image with edited lighting. What happens if for example emission estimation does not perfectly agree with the emitters, or include false positive emitters (non-emitter regions of high emissions). Do types of those failure cases occur, and if yes how they are handled? Overall, section 3.7 is confusing: 'Replacing or modifying local lighting features has only local effects', which presumably is not desired in light editing?

[6] Language issues.

Scene reconstruction -> View synthesis. Table 1: what is geometry prior (it is referring to the learned 3D features?)

### Questions
Please see the above comments for questions to address.

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
4

### Summary
This paper introduces a learned surface emission model to reconstruct 3D lighting fields from sparse multi-view images for indoor scenes.

Leveraging neural fields and voxel-based representations, it enhances relighting and virtual object insertion capabilities. The approach combines explicit inverse rendering with neural priors, enabling complex emission profiles from limited input data by conditioning on 3D spatial and semantic features. This model’s ability to control light sources while requiring fewer views than previous methods suggests advancements in realistic indoor scene applications, such as augmented reality.

### Strengths
This paper presents an original and practical approach by combining neural fields with learned priors for indoor lighting reconstruction, allowing it to infer unobserved light sources. The method demonstrates high-quality lighting reconstruction with substantial quantitative gains over previous methods, proving useful for dynamic lighting applications like AR and VR. The inclusion of a voxel-based emitter sampling technique also improves noise reduction, enhancing the overall quality of relighting and virtual object insertion.

### Weaknesses
The approach is computationally intensive, requiring significant processing time due to path tracing, which may limit its feasibility for real-time applications. Specifically, the reliance on iterative path tracing for each lighting configuration and the high dimensionality of the neural field representation contribute to this bottleneck. Additionally, the method assumes Lambertian materials, which restricts its adaptability to scenes needing complex material representations, such as specular or glossy surfaces, and some of the technical explanations, especially around voxel representation, could benefit from greater clarity. The description of how the voxel grid is used to sample emitters and how this relates to the neural field is not sufficiently detailed, making it difficult to assess the robustness of this sampling strategy.

### Questions
- Could you provide more insights into computational optimizations that could reduce the processing time for practical deployment?
- How well does the model generalize to scenes with mixed lighting types? (naturel or artificial)
- Could the approach be adapted for outdoor scenes, where volumetric light transport might play a significant role?

### Soundness
3

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
3

### Summary
The purpose of this paper is to accurately restore lighting in indoor scenes using a limited number of observed views, enabling realistic lighting effects for applications such as virtual object insertion and lighting editing.

To achieve this, a neural-field-based parametric lighting representation is used. This model predicts the intensity and direction of lighting at each location in 3D space and enhances restoration accuracy by limiting possible light source locations through semantic embeddings. Additionally, differentiable path tracing is used to optimize alignment with observed images, and voxel-based sampling is introduced to reduce noise during path tracing and improve efficiency.

The dataset is an extended version of 3D-Front, incorporating Lambertian materials and texture-based lighting to create synthetic data under diverse indoor lighting conditions, which is used for training and evaluation.

### Strengths
1. Tackling the Challenge of Lighting Reconstruction in Complex Indoor Scenes 

Indoor scenes are particularly challenging for lighting reconstruction due to the variety of light sources, complex geometries, and multiple reflections involved. This paper’s approach appears to address these complexities by enabling accurate lighting reconstruction even with limited observed views, which could potentially broaden the scope for realistic lighting manipulation in intricate indoor environments.

2. Thoughtful Integration of Multiple Techniques 

The paper combines neural field-based lighting representation, semantic embedding, differentiable path tracing, and voxel-based sampling in what seems to be an efficient and well-balanced way. This integration could be a strength as it leverages the individual advantages of each technique, allowing for both high-quality reconstruction and computational efficiency in complex lighting conditions. The combination might help enhance the model’s accuracy and robustness, making it better suited to the intricate lighting variations characteristic of indoor scenes.

### Weaknesses
1. Reliance on Synthetic Datasets

This paper primarily uses synthetic datasets such as 3D-Front to train and evaluate the model. While synthetic data is useful for demonstrating the feasibility of lighting reconstruction in complex indoor scenes, it may not fully capture the variability and complex material characteristics of real-world environments. The textures and material properties in synthetic datasets are often idealized, lacking the imperfections, variations in surface roughness, and complex BRDFs found in real-world scenes. This discrepancy could lead to a model that performs well on synthetic data but struggles with real-world images, where lighting interactions are more nuanced and unpredictable. The lack of real-world validation significantly limits the assessment of the model's practical applicability.

2. Assumption of Complete Geometry Conflicts with Limited View Claims

This paper claims to enable lighting reconstruction with limited views, but it is based on the assumption that precise geometry of the entire scene is already available. In an approach intended to work with limited views, assuming pre-existing complete geometry may be logically inconsistent. The notion of limited views generally implies incomplete scene information; however, by assuming full geometry is already provided, the paper may face limitations in fully evaluating the effectiveness of reconstruction with truly limited views. This assumption undermines the claim of handling limited views because in real-world scenarios, obtaining complete and accurate geometry from sparse views is a significant challenge on its own. The method does not address the uncertainty and errors that would arise from incomplete or noisy geometry, which are common in limited-view settings.

### Questions
1. Obtaining Complete Geometry and Material Information in Realistic Scenarios

In realistic scenarios, obtaining complete geometry and material information for a space requires precise Lidar scanning or highly dense photographic data. Could the authors propose a plausible scenario in which the experiments in this paper could be reproduced in real-world settings with only sparse views to reconstruct the scene’s geometry and material properties?

2. Integration with Modern Radiance Field and Semantic Segmentation Techniques

To achieve a more realistic scene reconstruction, could the authors suggest a scenario in which modern radiance field techniques and compatible semantic segmentation methods (e.g., OpenNeRF) could be integrated with the methodology proposed in this paper?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes Neural Lighting Priors, a method that combines learning and optimization to recover 3D neural surface emission fields from sparse multi-view images and explicit geometry for indoor scenes.

Leveraging explicit geometry, the authors introduce ray tracing to propagate features. They design a learned parametric emission model that decouples spatially varying lighting and material parameters, with a voxel grid storing local latent codes.

During training, both the latent codes and decoder are optimized. In testing, only the latent codes are optimized based on sparse views and geometry. This approach allows the estimation of light sources, supporting accurate shadows and improving photo-realistic relighting and virtual object insertion.

However, the method’s reliance on explicit geometry limits its generalizability.

### Strengths
+ Incorporating path tracing: 

The use of path tracing allows for the accurate estimation of high-order lighting effects, particularly in generating realistic shadows, which enhances the overall relighting and rendering quality.

+ Learning-based decoder regularization: 

The method employs a learned decoder to regularize the latent codes during testing, which effectively reduces overfitting during optimization and leads to more robust lighting reconstructions.

+ Improved performance: 

The proposed approach demonstrates superior performance compared to several baselines, particularly in handling sparse-view settings for relighting and virtual object insertion tasks.

### Weaknesses
I have several concerns regarding the motivation, implementation details, comparison, and baselines.

+ A little overclaiming the problem setting: 

The paper seems to overclaim the difficulty of realistic lighting optimization and relighting from sparse views. While this is undoubtedly a challenging task, the introduction of accurate geometry substantially simplifies the problem. Acquiring geometry is the key aspect of light transport optimization, especially for high-order effects like shadows. However, it is hard to obtain accurate geometry from just 10 sparse views. As a result, this makes the comparison with other methods somewhat unfair, as they don’t have such strong geometry priors. Moreover, how could such a setting be applied to real-world applications? I would encourage the authors to discuss potential use cases, as combining sparse view settings with geometry acquisition seems somewhat unusual.

Additionally, how does the proposed method differ from Nimier-David et al.'s paper on "Material and Lighting Reconstruction for Complex Indoor Scenes with Texture-space Differentiable Rendering," which also uses explicit geometry and path tracing for texture recovery?

+ Writing clarity: 

The writing can be significantly improved. It seems the authors focus more on how the task is conducted rather than explaining why the approach was designed this way. Specifically, there are several concerns regarding the implementation:

a) Material model: On lines 247–248, the paper mentions only Lambertian materials, while in line 269, the dataset is described as using GGX. Why are these different, and how do the authors compensate for the material discrepancy?

b) Ray tracing settings: It appears the method uses only 1 bounce and 1 importance sampling (line 195). How is smooth rendering achieved with just one sample? For instance, in Fig. 11, one sample is typically noisy, yet the renderings shown in the supplementary videos look much smoother. In line 319, it is mentioned that during testing, each pixel shoots 2048 rays. This creates confusion between the training and testing settings. Could you clarify this?

c) Emission model: In Eq. (7), is ​$L_e$  the same as the image color? Emission should typically be evaluated only for light sources. Do you use semantic masks to infer these regions?

d) Methodology clarity: Overall, the methodology lacks sufficient detail, and I couldn’t find these details in the supplementary material. I strongly encourage the authors to revise the method section and ensure consistent terminology throughout.

+ Baselines and fairness: 

Many of the baselines appear outdated. As I mentioned earlier, the use of geometry priors gives the proposed method a significant advantage over others, which is somewhat unfair as the baselines use geometry inferred from a single image (e.g., Wang et al.). I strongly encourage the authors to include a comparison that does not rely on ground-truth geometry but instead infers geometry from the 10 sparse views, to assess the quality of the inference.

Furthermore, the authors should discuss the relationship between their work and the following papers:

Wang et al., Neural Fields meet Explicit Geometric Representations for Inverse Rendering of Urban Scenes, CVPR 2023: This paper also introduces ray tracing to synthesize shadows.
Wang et al., Neural Light Field Estimation for Street Scenes with Differentiable Virtual Object Insertion, ECCV 2022, This work focuses on inserting objects from a single image.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2
