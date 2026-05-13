# MVDrag3D: Drag-based Creative 3D Editing via Multi-view Generation-Reconstruction Prior

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
Drag-based editing has become popular in 2D content creation, driven by the capabilities of image generative models. However, extending this technique to 3D remains a challenge. 
Existing 3D drag-based editing methods, whether employing explicit spatial transformations or relying on implicit latent optimization within limited-capacity 3D generative models, fall short in handling significant topology changes or generating new textures across diverse object categories.
To overcome these limitations, we introduce \textit{\textbf{MVDrag3D}}, a novel framework for more flexible and creative drag-based 3D editing that leverages multi-view generation and reconstruction priors.
At the core of our approach is the usage of a multi-view diffusion model as a strong generative prior to perform consistent drag editing over multiple rendered views, which is followed by a reconstruction model that reconstructs 3D Gaussians of the edited object.
While the initial 3D Gaussians may suffer from misalignment between different views, we address this via view-specific deformation networks that adjust the position of Gaussians to be well aligned.
In addition, we propose a multi-view score function that distills generative priors from multiple views to further enhance the view consistency and visual quality. Extensive experiments demonstrate that MVDrag3D provides a precise, generative, and flexible solution for 3D drag-based editing, supporting more versatile editing effects across various object categories and 3D representations. Video demos can be found on our project webpage: \href{https://chenhonghua.io/MyProjects/MvDrag3D/}{\textit{https://chenhonghua.io/MyProjects/MvDrag3D/}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors present a framework named MVDrag3D for drag-based 3D editing. It first renders a 3D object and the drag points into 4 orthogonal views, and introduce a multi-view guidance energy to achieve consistent multi-view score-based image editing. Multi-view Gaussian reconstruction is then performed on the edited images, followed by Gaussian position adjustment by view-specific lightweight deformation networks. Finally, an image-conditioned multi-view SDS optimization is applied to further enhance view consistency and visual quality.

### Strengths
+ The idea of casting 3D drag-based editing into multi-view 2D drag-based editing sounds novel and feasible.
+ The use of multi-vew diffusion model to ensure consistent multi-view image editing sounds novel and feasible.
+ The lighweight view-specific deformation networks appear to be effective in improving the geometric alignment of the 3D Gaussians with the image.
+ The use of image-conditioned multi-view SDS optimzation for enhancinmg view consistency and visual quality sounds logical.
+ Both qualitative and quantitative results demonstrate SOTA results.

### Weaknesses
 - There is no disucssions on how to choose the optimal 4 orthogonal views. Theoretically, the 4 orthogonal should be chosen such that the drag directions should be as far away from the view directions as possible. In this paper, the authors simply choose orthogonal azimuths (0 deg, 90 deg, 180 deg, 270 deg) and a fixed elevation (0 deg).
- By rendering only 4 orthogonal views, some details (shape and texture) of the 3D object may be lost. Specifically, the rendering process might not capture high-frequency details or intricate geometric features that are only visible from specific viewpoints not included in the four chosen views. This could lead to a loss of fidelity in the reconstructed 3D model.
- In 3D Gaussian reconstruction step, partial 3D Gaussians are regressed for each view, which are then fused into a unifed representation. It is not clear why the authors do not perform multi-view Gaussian reconstruction instead. This raises concerns about the potential for inconsistencies or artifacts arising from the fusion process, as each view's Gaussian representation might not perfectly align or integrate with others.
- It is also not clear wheather the Gaussian position optimization step is necessary. Why can't the image-conditioned multi-view SDS optimization be carried out directly on the initial 3D Gaussians? The necessity of this intermediate step needs further justification, as it adds complexity to the pipeline and might not be essential if the SDS optimization could directly refine the initial Gaussian positions effectively.

### Questions
- Why do the authors regress a partial 3D Gaussians for each view and fuse them afterwards instead of performing a multi-view reconstruction?
- Referring to Table 1, is there any explanations why SDS optimization produces better results for Gaussians than for meshes in terms of DAI?
- For 3D meshes, are the final outputs still 3D Gaussians? Are the quantitative results all computed on 3D Gaussians?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a 3D editing method based on sparse control point dragging, applicable to both neural implicit representations and explicit mesh representation. The proposed method is based on a multi-view diffusion model and a large model for sparse view reconstruction. Specifically, the method renders the 3D representation into images from four specified viewpoints, then uses DDIM inversion to convert these images into Gaussian noise, which is regenerated using the multi-view diffusion model MVDream. During the generation process, control point movements are incorporated as a constraint to define multi-view guided energy optimization for intermediate denoising features. The generated edited images from the four viewpoints will obtain a 3D GS representation using the large pre-trained model, LGM. However, the 3D Gaussians obtained from the four views exhibit geometric deviations and texture artifacts. The former is addressed by introducing an MLP to shift the positions of Gaussian spheres, while the latter is resolved through multi-view SDS loss optimization. The paper compares the proposed method with other similar drag-based editing methods.

### Strengths
-- The paper has a clear description and is well-structured, providing not only the necessary details for implementing the method but also the motivation for choosing this technical approach.

-- The method proposed in this paper is reasonable and has achieved results superior to other comparative methods.

### Weaknesses
 -- The method proposed in this paper is straightforward but lacks sufficient technical contribution. The first step generates multi-view edited images, with its optimization method and energy terms resembling those of Dragondiffusion. The main difference is merely substituting a single-view diffusion model with a multi-view one, which is a simple and direct change requiring minimal adjustments. In the second step, the LGM is used to regenerate the 3DGS model by directly utilizing an existing pre-trained model. Finally, the adjustments made through the deformation MLP and multi-view SDS loss optimization are common practices in 3D modeling and generation. Therefore, the proposed method primarily combines existing approaches without significant improvements, leaning more towards engineering rather than showcasing technical contributions.

-- Although the proposed method outperforms existing approaches in terms of deformation effects, it is still limited by the 3DGS representation, resulting in some artifacts and blurriness at the model edges in the final output. For instance, this is evident in the green leaves of the flowers, the open mouth of the crocodile, and the open mouth of the lion in the video.

-- The method's reliance on a 3DGS representation, while offering flexibility, introduces limitations in terms of mesh quality. The extraction of a mesh from the 3DGS representation is not ideal, and the resulting mesh might not preserve the original mesh's details and topology. This is a significant drawback, especially when the desired output is a high-quality mesh representation. The deformation MLP and multi-view SDS loss optimization, while helpful, appear to be primarily effective for minor adjustments. Their ability to handle significant geometric inconsistencies and texture artifacts remains questionable, and the lack of ablation studies in the video makes it difficult to assess their individual contributions.

### Questions
-- Does the proposed method ultimately produce a 3DGS representation for editing the input mesh? What if we still want a mesh-based output? While 3DGS can extract the mesh, the quality of the extracted mesh is not very good, and it is necessary to use higher-quality representations like 2DGS for better reconstruction results.

-- While the deformation MLP and multi-view SDS loss optimization do have some effectiveness in fine-tuning the final results, they seem to be suitable primarily for relatively minor issues. For more significant geometric inconsistencies and texture artifacts, it remains unclear whether they can adequately address these challenges. And could the video include results from ablation experiments related to these two aspects?

After rebuttal:
1. Though this work is a good engineering effort, I still believe it lacks sufficient technical contribution and relies heavily on the multi-view reconstruction method. As I mentioned in the previous review, it mainly combines some existing methods with some appropriate improvements, but these improvements are not substantial enough to be considered an independent technical contribution. While this combination can solve certain problems that existing methods struggle with, it does not mean that the approach is technically novel or provides enough insight.

2. Furthermore, the artifacts in the results indicate that the proposed method is too dependent on the robustness of existing methods. The authors mention that more advanced methods can be substituted, but this further suggests that the proposed approach is just a combination of existing methods, and each of these methods needs to have robust results on its own.

3. While the proposed editing method can handle some situations that existing deformation methods cannot, editing methods generally need to preserve the original representation. Although the introduction of 2DGS can further obtain meshes from the editing results, it does not fully preserve the details and topology of the original mesh. Therefore, the proposed method’s applicable editing objects might need to be reconsidered.

Taking these points into consideration along with reviews from other reviewers, I still have concerns about accepting this paper. Hence, I maintain my original score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes MVDrag3D, which utilizes a deformation network and SDS loss from multi-view diffusion models to edit 3D objects. The results show that the proposed method can generate 3D creations with the corresponding drag operation while creating new textures.

### Strengths
* MVDrag3D is capable of user-friendly drag operations. Extending the idea of 2D drag to 3D makes sense and shows good qualitative results.
* MVDrag3D shows the ability to generate new textures, which makes it different from the standard 3D deformation works.

### Weaknesses
 * Low-quality 3D creations: Most of the results are based on simple 3D creations or generated 3D creations, which are pretty low-quality. For example, the shoes and the fox show a blurred texture. Such evaluation dramatically limits the application of the proposed method. In addition, the edited results in the video tend to be blurred compared with the "Drag on meshes" illustration. These observations raise two concerns: (1) will this method blur the original 3D content? (2) will this method work for high-quality 3D creations?
* Failure cases of drag operations: The drag operation does not usually seem successful in the examples. The drag on the owl is not correctly optimized since the cloth doesn't reach the target position. In addition, the texture of the tie is degenerated during this process. Such a result even sees worth than the baselines like APAP. The use of SDS loss probably hurt the results to some extent.

### Questions
* Listed in the wakenesses.

### Soundness
3

### Presentation
2

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
The paper proposed a new algorithm called MVDrag3D, which is a framework for drag-based 3D editing. The method first generates multi-view images, followed by mechanisms introduced to enforce consistencies in the generation process, before reconstructing a 3D model. In the experiments, it looks like the proposed approach provides a more precise 3D reconstructed results comparing to other state of the art approaches

### Strengths
The paper is a system paper but t does has some interesting novel ideas that might be beneficial to the research community. There are several notable strengths
- The proposed approach is sensible in that leverating multi-view to control the dragging behavior is reasonable, and the overall formulation of the algorithm is intuitive.
- The introduced multi-view guidance score and the refinement approach is novel in that it helps reduce artifacts and addressed softspots in the algorithm. There are several mini-ideas in the approach that are interesting, such as adding random noises in the inversion, etc.
- Experimental results looks competitive, especially some of the visual comparisons.

### Weaknesses
I think there are merits in the paper but i've got some questions or confusions while reading the paper
- In figure 3, the differences of the final reconstruction results are very minor to me. I couldn't fully appreciate the need of the random noise unless I zoom into the pictures. Technically none of those results matches the input very well.
- Experimental results are conducted on vey simple 3D objects. Maybe this is a common issue for all state of the art approaches. Similarly, in fig. 6 -- many appraoches perform quite competitively (such as the boots, flower, and the suited animal case), and I struggle to tell if the approach is truly groundbreaking or incremental
- The descriptions of the technical formulations of the approach requires more details. For example, i struggled to understand the "Gaussian appearnace optimization" section -- "Note that all Gaussian properties are optimized during this process, with densification and pruning operations enabled." -- which densification and pruning approach exactly, and how is this done? The "shoe" example in fig.5 is also showing tiny improvements with the optimizations.
- It'd be good if the paper could provide human evaluations. The automatically computed metrics might not tell the full story of the effectiveness of the approach.

### Questions
I have raised questions in the weakness section

### Soundness
3

### Presentation
2

### Contribution
2
