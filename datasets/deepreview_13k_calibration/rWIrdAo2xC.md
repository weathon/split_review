# Generalizable Monocular 3D Human Rendering via Direct Gaussian Attribute Diffusion

- Decision: Reject
- Avg Score: 5.20
- Scores: 3, 10, 5, 5, 3

## Abstract
This paper leverages 3D Gaussian Splatting to tackle the challenging task of generating novel views of humans from given single-view images. Existing methods typically adopt an indirect supervision manner, i.e., splat-based rasterization for differentiable rendering. However, the intricate coupling of various 3D Gaussian attributes complicates precise error backpropagation during optimization, often
resulting in convergence to local optima. In contrast, we propose a novel direct paradigm to train a conditional diffusion model directly supervised by proxy-ground-truth 3D Gaussian attributes. Specifically, we propose a two-stage construction process to derive consistent and smoothly distributed proxy-ground-truth 3D Gaussian attributes. Subsequently, we train a point-based conditional diffusion model customized to learn the data distribution of these proxy attributes. The resulting diffusion model can generate the 3D Gaussian attributes for the input
single-view image, which are further rendered into novel views. Extensive experimental results showcase the significant performance advancement of our method over state-of-the-art approaches. Source code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces a method that renders novel views of human avatars, given only a single image. The authors propose a pipeline of multiple stages, where they first learn a prior and then they can render a human under novel views. They highlight their paradigm as "direct", using extracted attributes for supervision, in contrast with other approaches (indirect) that use differentiable rasterization and pixel-level supervision during training.

### Strengths
+ Learning a generalizable approach for human avatars is an interesting topic. Most approaches in this area are identity-specific. Rendering a novel human, given only a single image, is useful. This method seems to work in this case.

+ The authors show better performance than other methods.

### Weaknesses
 - The claim of "direct" paradigm is not clear. The method essentially consists of multiple stages. It is then supervised by extracted features, that can also propagate the error to later stages.

- The writing of the paper is not clear.

- It was not directly obvious what the ablation studies show with respect to the contributions of various components as they present single cases of failure as opposed to complete numerical results, so it is hard to understand where the significant improvements in the overall results come from.

- There are no animation results. Most of similar methods show both novel views (reconstruction), but also animation (e.g. SHERF). It will be good that the authors include animation results as well, to be able to validate the consistency of their solutions.

- Even though the authors show good results, the overall contribution and novelty of the paper is not well supported. Components like transformers, stable diffusion, etc have been used by other papers as well. Learning pixel-aligned features from different views have been proposed by previous works, like the generalizable NeRF ActorsNeRF (ICCV 2023) and MonoHuman (CVPR 2023). Stable diffusion has been used by works for humans, like DreamHuman (NeurIPS 2024), DreamAvatar (CVPR 2024), AvatarPopUp (ECCV 2024), and other works for 3D objects (e.g. DreamFusion). It is not clear to this reviewer what the additional challenges of monocular reconstruction are in the particular set up of this paper and how the particular method addresses them.

Missing citations of generalizable models for humans, including GM-NeRF (CVPR 2023), Neural Human Performer (NeurIPS 2021), ActorsNeRF (ICCV 2023).

### Questions
Please see the above weaknesses.

What is causing the large numerical improvement?

Can the authors provide animation results? Would their method work?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes a new method, Human-DAD, and shows it outperforms previous SOTAs on the task of novel view synthesis of humans from a single-view image. The authors showed that *directly* predicting 3D Gaussian attributes enhances the effectiveness of the training process, compared to the traditional *indirect* supervision through photometric losses. To enable the *direct* paradigm training, a two-stage data construction method is proposed to obtain proxy ground truth 3D Gaussian attributes. Using the proxy ground truth as training data, a conditional Diffusion Model, GSDIFF, is trained to output 3D Gaussian attributes of a scene given a single-view image of human.

The paper contains extensive experiments, ablation studies and user studies, proving its superiority over other baselines and previous SOTAs.

### Strengths
1. The writing of the paper is in general very clear and detailed. The presentation of the flowchart is very useful for better understanding the multi-stage method. 
2. The method is innovative and non-trivial. For example, in stage1 of the Gaussian attribute dataset construction, instead of doing a vanilla 3DGS per scene optimization, the authors trained a point cloud transformer to directly output the other attributes given Gaussian positions. As shown later in the Experiment section, the inherent smoothness tendency of the learned network is essential for achieving high quality NVS later on.
3. The design of the diffusion model is very careful and smart. Instead of naively taking the single-view image as input, the diffusion model is conditioned on the Gaussian positions, pixel-aligned features and SMPL semantic features. Off-the-shelf mono-depth prediciton model and instruction based image2image model are used in the process to obtain high quality condition signals. 
4. As shown in Table2, Human-DAD outperforms all the previous SOTAs that it has been compared to on all the metrics reported by the authors. The qualitative results also show the impressive visual quality of the output.

### Weaknesses
1. Wrong index to the referenced figure in the paper. I believe it should be Fig8, not Fig3 at line 503.
2. Same issue as above at line 507-508
3. The paper will be stronger if an ablation study of naively conditioning the diffusion model on input RGB image is provided in the paper. The current design uses a complex combination of Gaussian positions, pixel-aligned features and SMPL semantic features. It is not clear how much each of these components contributes to the final performance, and whether a simpler approach could achieve comparable results.
4. Reference should be given for the claim at line 41-43.
5. The 2-stage Gaussian attribute data construction process, though effective, might have limited generality over heterogeneous data. The paper uses a single dataset, Thuman2, for proxy GT construction. If given additional human data with diverse backgrounds, different scales or shifted domains etc., whether this carefully designed and calibrated pipeline can be as effective remains unclear. The reliance on a single, potentially homogeneous dataset for proxy ground truth generation raises concerns about the robustness of the method when applied to more varied and challenging datasets. The method's performance on datasets with significant variations in pose, clothing, and background is not explored.
6. What auxiliary constraints are imposed should be elaborated at line 248 in the main paper. The current description lacks the necessary detail for a complete understanding of the training process. Specifically, the mathematical formulation of these constraints and their impact on the optimization process should be explicitly stated.

### Questions
1. At line 291, the authors mention the semantic lables are embedded in the latent space through MLPs. Could you elaborate on this? Are the MLPs pre-trained or trained separately by the authors?
2. Zooming in on the results in the last column of Figure6, I saw artifacts of thin dark lines, which almost look like countour lines. Can you explain what might be the cause of such artifacts?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper uses the 3D GS representation to generate novel views of humans from single-view images. Different from existing methods that train with supervision from 2D image space, it proposes to learn a diffusion model that directly models the GS attributes in the 3D GS space. To prepare a proxy-ground-truth GS dataset for training, the position of GS is obtained by downsampling from GT point cloud, and the other attributes are optimized using multi-view supervision and a network-based regularization. A GS attribute diffusion model is then trained with the condition of point cloud position, pixel-align feature and semantic feature. Experiments demonstrated the superior performance of the proposed approach.

### Strengths
1. This paper designs a pipeline to prepare the ground truth GS dataset regularized by network overfitting is new for me.
2. The proposed GS attribute diffusion model condition on image feature maps and SMPL semantic maps makes sense.
3. The proposed method shows better performance compared with the state of the arts.

### Weaknesses
1. For GS dataset preparation, stage 1: per-scene overfitting seems to be ineffective in regulating the distribution only relying on the inherent smoothness of a neural network. So, it further needs a network for additional distribution unification. However, if I'm not wrong, it still mainly depends on the smoothness of the neural network without other regularization. I wonder if the use of a neural network in the first stage is necessary, which makes the pipeline over complicated.
2. I'm suspicious of the core argument that GS space supervision leads to better performance than image space supervision. Empirically, we are finally evaluating the NVS results in image space. It's not straightforward that a small error in GS space could indicate a small error or better quality in the image space. For the ablation study in Table 3, the performance difference using direct/indirect supervision is not that significant, the image-supervision method even gets better scores in SSIM and LPIPS, which reflect the perceptual quality.
3. Similarly, for the ambiguity problem the author mentioned when using 2D space supervision, I don't think it's related to supervision space but to deterministic/stochastic paradigm or loss design. 
4. The diffusion model design is very confusing, especially for the extra steps for alpha, scale, and quaternion attributes.
5. It seems that using stable diffusion model to generate the back view and using position generator (HaP) [1] to generate point cloud are of great importance to better performance. But these two components are existing works, not the technical contribution of this paper.

### Questions
1. It seems that this work mainly focuses on the texture of humans while using an existing work for shape generation. I wonder about the importance of shape during evaluation. Is it possible to extract the texture of other comparable method and re-map it to your point could or ground truth point cloud to exclude the influence of different shapes?
2. I also wonder if the diffusion network just maps the front and back view to the point cloud. Could you show some results that use front view and back view to perform 3DGS optimization to map the texture?
4. I wonder how the extra step of the diffusion model is performed. Is it not the diffuse-denoise process modeling anymore but a straightforward one-step regression? If so, I think the description is confusing and misleading.

### Soundness
2

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
4

### Summary
This paper proposes to train a conditional diffusion model for generating novel views of humans from given single-view images, directly supervised by proxyground truth 3D Gaussian attributes. The authors first create a dataset of proxy ground-truth Gaussian attributes with addtional neural network to smooth the dataset distrbution. A point-based conditional diffusion model is then employed to learn the data distribution of these attributes. Experimental results showcase the performance advancement of their method over current approaches.

### Strengths
The method is well-written, with clear motivation behind each module design. The final results demonstrate improvement compared to previous methods like LGM. The idea of using a neural network to constrain the distribution of target 3D Gaussian attributes makes sense and is effective.

### Weaknesses
 - The main claim of the paper is that the direct supervision approach (using 3D regression loss) is superior to the indirect supervision method (using rendering loss). However, direct supervision approach also has limitations with memory consumption and the time-intensive nature of direct supervision. Moreover, with more iterations or larger batch size, will it be possible that the indirect supervision method could achieve similar performance? The **supervision gap** suggested by the paper isn’t clearly demonstrated to be an intrinsic limitation. The core issue is that the single-image to human avatar task is inherently ill-posed, as a single image can correspond to many possible 3D avatar solutions due to the invisible parts in the single images. The paper's focus on the many-to-one problem during Gaussian Splatting regression, while relevant, does not fully address this fundamental ambiguity.
- Although the method outperforms other generalizable novel view synthesis techniques like LGM, the image quality remains limited since only one single input image are used. Another potential direction in this field is incorporating a 2D diffusion prior to enhance information, as demonstrated in Human 3Diffusion [1]. A comparison to these baselines is needed.
- The figures are a bit too small to clearly distinguish all the differences in results.

### Questions
- How does the model perform on in-the-wild and out-of-distribution evaluations?
- Is it feasible to extend this approach to support multi-view input and obtain much better novel view synthesis results? Several works focusing on this can be considered like [2], [3].
  [2]: Kwon Y, Kim D, Ceylan D, et al. Neural human performer: Learning generalizable radiance fields for human performance rendering[J]. Advances in Neural Information Processing Systems, 2021, 34: 24741-24752.
  [3]: Gao Q, Wang Y, Liu L, et al. Neural novel actor: Learning a generalized animatable neural representation for human actors[J]. IEEE Transactions on Visualization and Computer Graphics, 2023.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Human-DAD, which adapts a new paradigm for training a generalizable 3DGS, to reconstruct the 3D human body from a single-view image. Unlike a common strategy in optimizing 3DGS from multi-view images, the authors proposed to train the model with direct supervision (applying loss function directly into Gaussian attributes). To apply good supervision, this paper uses two-stage workflow to construct 3D pseudo-GTs of 3D Gaussians: optimizing 3D Gaussian per scene and then unifying the distribution of Gaussian attributes along the camera views. Furthermore, to reconstruct 3D human Gaussians from the single-view image, the authors device a diffusion model conditioned from SMPL-semantic features and pixel-aligned features. The proposed Human-DAD outperforms existing state-of-the-art 3D human reconstruction methods.

### Strengths
In recent years, 3D Gaussian splatting (3DGS) has shown impressive results in 3D vision fields. Despite the promising results of 3DGS, the exploration of adapting 3DGS for single-view 3D human reconstruction is still lacking. This paper can provide several good intuitions about the 3DGS for 3D human reconstruction, especially in the proposed 'distribution unification' of 3D Gaussian pseudo-GTs.

### Weaknesses
I have several concern points as below.


1) Discussion about direct vs indirect supervision

a. This paper strongly suggests the inefficacy of the traditional 'indirect paradigm' in reconstructing 3D humans with 3DGS. 
In 3DGS for 3D objects, I agree that recent works apply image loss to train their model instead of direct supervision [4]. However, to the best of my knowledge, I haven't heard about employing 3DGS for single-view 3D human reconstruction (also in the submitted paper). If there is a reference algorithm, it would be good to refer to it and conduct the experiment based on it. If not, the proposals in this paper may be a hasty conclusion.

b. This paper validates the effectiveness of the direct paradigm in their constructed algorithm (Tab. 1). However, their experiment setting in Tab. 1 cannot be representative of covering recent 3D human reconstruction approaches. So, it is difficult to suggest that a direct paradigm is better by only referring Tab. 1. I recommend that experiment Tab. 1 should be conducted in more general settings, such as [1].

c. Direct supervision is not always better than indirect supervision. In the two-stage workflow (Fig. 2), the algorithm reduces the randomness of fitted 3DGS, but it does not completely solve it. In generating 3D pseudo-GTs, enormous 3DGS can be mapped into multi-view images, similar to many-to-one mapping (L44) in indirect supervision. This discussion needs to be taken into consideration


2) Distribution unification

As shown in Fig. 4 and Tab. 1, the distribution unification (L250-257) is effective. However, it is difficult to understand why the training approach of Fig. 2 (right) helps the Gaussian distribution. The approach is very simple, batch-wise training. For example, if the network learns identity (A -> A), it would be a good local minima to minimize the photometric loss. What is the main component that to leads unifying the Gaussian distribution? A detailed discussion of this should be included in the manuscript.


3) Evaluation of 3D geometry

This paper only produces evaluation in rendered images (PSNR, SSIM, ...) and does not report 3D metrics (P2S, Chamfer Distance, ...), although the used datasets have 3D GT scans.


4) Paper writing

a. In L32-38, it does not clarify the categorization: Reconstruction-based vs NerF-based. The reconstruction-based approaches also use neural fields. I think that more suitable words are image-based vs video/multi-view-based. I recommend that this paper needs more clarification about it.

b. In L128, the paper mentioned Zou et al. follow PIFu. It's not clear which part of PIFu they followed (PIFu does not use triplane representation).

c. It is unclear what the authors used datasets for Tab. 1 and Tab. 3.


[1] Zou et al., Triplane meets gaussian splatting: Fast and generalizable single-view 3d reconstruction with transformers, CVPR, 2024.


In conclusion, I'm concerned about accepting this paper, for two main reasons.
a. It is hasty to suggest direct supervision is beneficial, given the content of this paper.
b. Distribution unification of 3DGS is difficult to agree on, without extensive explanation of its design reason.

### Questions
1) Diffusion model
It is unclear why the diffusion model was chosen. I conjecture the main strength of the diffusion model is generative power.
Does the algorithm produce diverse reconstruction candidates corresponding to the single-view image?

2) Reconstruction quality
In Fig. 8, why the reconstructed human face is blurred, unlike Fig. 6?
In Fig. 7, why the SHERF's results are more darker than others, unlike Fig. 6?

### Soundness
2

### Presentation
3

### Contribution
2
