# STORM: Spatio-TempOral Reconstruction Model For Large-Scale Outdoor Scenes

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
We present STORM, a spatio-temporal reconstruction model designed to reconstruct in-the-wild dynamic outdoor scenes from sparse observations. Existing dynamic reconstruction methods rely heavily on dense observations across space and time and strong motion supervision, therefore suffering from lengthy optimization time, limited generalizability to novel views or scenes, and degenerated quality caused by noisy pseudo-labels. To bridge the gap, STORM introduces a data-driven Transformer architecture that jointly infers 3D scenes and their dynamics in a single forward pass. A key design of our scene representation is to aggregate 3D Gaussians and their motion predicted from all frames, which are later transformed to the target timestep for a more complete (i.e. “amodal”) reconstruction at any given time from any viewpoint. As an emergent property, STORM can automatically capture dynamic instances and their high-quality masks using just the reconstruction loss. Extensive experiments show that STORM accurately reconstructs dynamic scenes and outperforms other per-scene optimization (+3.7 PSNR) or feed-forward approaches (+1.5 PSNR), it can reconstruct large-scale outdoor scenes within just 200ms and render in real-time. Beyond reconstruction, we qualitatively demonstrate four additional applications of our model, demonstrating the potential of self-supervised learning for advancing dynamic scene understanding. Our code and model will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for dynamic 3D reconstruction (4D reconstruction) of urban scenes from temporally and spatially sparse video input.

The model is based on a per-frame transformer architecture that takes image, ray (from given camera intrinsics and extrinsics), time and motion latent tokens as input as well as some special tokens for handling sky and varying camera exposure. The model takes tokens from an image coming from single camera v and timestamp t, and then processes these tokens jointly with a self-attention transformer, to output feature maps F^v_t for that image. These tokens are then decoded into pixel-aligned 3D Gaussian Splatting parameters G^v_t, which are used to reconstruct the input frame as well as to compute the depth map. In addition, the motion tokens are decoded into a set of motion queries and velocity bases, which are employed to estimate the velocity vector of each 3D Gaussian.

Given a set of training frames coming from one or several cameras, the model is run on each frame independently to obtain independent sets of Gaussians. These independent Gaussians can then be warped to any particular timestamp using the velocity estimates, and assuming velocity constancy.

In addition to the vanilla model, the authors propose a latent variant where instead of predicting the Gaussian parameters directly, the transformer first predicts higher dimensional vectors on a lower-dimensional grid, which are then upsampled to full-resolution using a CNN decoder.

The model is trained and evaluated on clips from the Waymo Open Dataset, using the provided camera intrinsics and extrinsics, and three frontal car cameras.

The authors evaluate their method against both per-scene optimization and feed-forward methods. For each 20 frame test clip, 4 frames are provided as inputs for reconstruction to each baseline, and the rest are used for evaluation. The results in Table 1 show that the proposed method obtains SOTA performance on reconstruction metrics compared to both per-scene optimization and feed-forward methods. In addition, the authors evaluate their method on the scene flow estimation task, also obtaining SOTA results.

Finally, the authors link a website with numerous quantitative results which allow to better assess the performance of the proposed method.

### Strengths
This is an interesting method which applies per-frame feed-forward 3DGS models to a multi-camera scenario for the urban driving setting. While similar methods exist for object-centric scenes (Splatter Image, LatentSplat) and static objects, or even object-centric scenes and dynamic objects (4DGS Guanjun Wu et al.), I believe the extension to outdoor driving scenes is novel and relevant. The authors successfully devised strategies to deal with the complexities of such scenes, by explicitly modeling the sky and the differences in camera exposure.

Furthermore, the authors adopt a similar strategy for modeling dynamics through scene flow as in NSFF, but which results to be more tractable due to the usage of 3DGS as a discrete representation of the scene. This methods seems to be effective in modelling short term dynamics.

Quantitative and qualitative results show that the method achieves good new-view synthesis results from only a few seen views.

The proposed latent-STORM variant shows improved reconstruction of local details, such as for the articulated bodies of walking pedestrians.

### Weaknesses
Some details of the method are not very clear from the paper. For instance, it's not clear how the aggregation and transformation processes are applied on the predictions of the 4 training frames for generating the predicted images \hat{I}. Specifically, the paper lacks a detailed explanation of how the per-frame Gaussian parameters are combined across the multiple input frames to form a coherent representation for rendering novel views at target timesteps. The description of how the predicted Gaussians from each of the four context frames are aggregated and transformed to a target time is missing, making it difficult to understand the temporal modeling aspect of the method.

In addition, it's not clear whether eq. (4) is correct and how exactly the weighs w are computed as the exact shapes of q and k are not specified. Also, it's not clear how the two different estimates v_t^{-} and v_t^{+} from eq (1) are obtained from what is described in eqs. (3,4). Furthermore, not many details are given about how these weights can be used to generate the motion segmentation figures, and the impact of the number of motion basis. It's also not very clear how the background scene is treated during this motion estimation. The paper does not provide sufficient detail on the dimensionality of the motion query and key vectors, and how these are used to compute the assignment weights. The lack of clarity on how the motion basis vectors are used to estimate the final velocity vectors is also a concern. The paper also does not clarify how the motion segmentation is derived from the computed weights, and whether the background is treated differently during the motion estimation process.

Regarding the quantitative results, it's not clear if the baselines for Table 2 have been retrained specifically on the same training set for fairness. Also, it's specified that the baseline models NSFP and NSFP++ require LiDAR input, but it's not clear whether these methods also benefit from having 3 different input views. It is unclear if the baseline methods are trained with the same data and supervision signals as the proposed method. The paper does not specify if the baselines are provided with the same number of input views, which could affect the fairness of the comparison. The fact that NSFP and NSFP++ use LiDAR data while the proposed method does not raises questions about the comparability of the results.

Regarding the qualitative results, having 3D visualizations in addition to depth-maps would help further assessing the temporal consistency and geometric correctness of the predictions. The current qualitative results are limited to depth maps and do not provide a comprehensive view of the 3D reconstruction quality. The lack of 3D visualizations makes it difficult to assess the temporal consistency and geometric accuracy of the reconstructed scenes.

Finally some of the proposed applications or extensions in sec. 4.3 are not explained in sufficient detail. For instance, how the point trajectories are chained for point tracking, given that the local scene-flow estimations are sparse and don't cover the whole space. In addition, it's not clear how latents can be manipulated in the latent-STORM model for achieving the edition, control and inpainting effects. The paper lacks a clear explanation of how the sparse scene flow estimations are used to generate continuous point trajectories. The description of how the latent space is manipulated for editing, control, and inpainting is also insufficient, making it difficult to understand the practical implications of these extensions.

### Questions
- Please clarify how the images \hat{I} are computed for a given training batch and which aggregations and transformations are involved.

- Please clarify the shapes of q and k in eq. (4) and how the weights are used for generating the motion segmentation visualizations, as well as how the number of motion basis is determined.

- Please clarify how the baselines are trained and which inputs they require.

- If possible, having 3D visualizations of the results would be beneficial.

- Please provide additional details about how point-tracking can be obtained, and how the editing, control and inpainting behaviours can be obtained in latent-STORM.

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
3

### Summary
This paper introduces STORM, a spatio-temporal reconstruction model for rendering dynamic outdoor scenes with sparse images. Combining image tokens, ray tokens, and time tokens, STORM uses a Transformer to predict attributes of 3D Gaussians (position, rotation, scale, opacity, color, velocity) at each timestep for real-time rendering. The training requires ground truth images, depth map and predicted sky mask from pretrained segmentation model.

### Strengths
The paper is clearly written.

STORM may be the first method that combines feed-forward 3D Gaussian Splatting and dynamic scenes.

STORM achieves better rendering quality and scene flow accuracy than baselines.

### Weaknesses
STORM only evaluates the quantitative performance in short video clips (about 2 seconds on Waymo open dataset). Applying STORM on 20-second videos requires processing in multiple video clips (L428) because of the heavy computation, which is also discussed in limitations. 

There is no quantitative ablation study.

### Questions
In Fig.3, can authors add ground truth images for comparison? Based on current visualization, Latent-STORM sometimes performs better and sometimes performs worse than STORM.

Could authors provide some reference for handling exposure mismatches with affine transformation?

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
4

### Summary
The paper presents STORM, a spatio-temporal reconstruction model that uses a data-driven Transformer architecture to accurately reconstruct dynamic outdoor scenes from sparse camera images without explicit motion supervision. It employs 3D Gaussian Splatting to aggregate per-frame data into an amodal, cohesive representation, enabling consistent scene reconstruction over time. The model is self-supervised, relying on reconstruction loss and incorporating motion tokens to capture motion primitives efficiently. Extensive testing on the Waymo Open Dataset shows that STORM outperforms traditional methods in photorealism and speed, achieving real-time performance within 0.2 seconds per clip.

### Strengths
1. The paper presents a clear and well-organized approach to addressing the defined problem of dynamic scene reconstruction.
2. The proposed method achieves state-of-the-art performance, showcasing its practical effectiveness and potential.
3. The video results available on the linked website are highly illustrative, providing clear insights into both the strengths and limitations of the proposed method.

### Weaknesses
1. The evaluations are limited to the Waymo dataset, which raises concerns about the comprehensive validation of the method. To strengthen the claims, it would be beneficial to demonstrate the effectiveness of the model across multiple datasets.

2. While the paper targets large-scale outdoor scene reconstruction, existing works such as [1] also address similar challenges. If the primary focus is on dynamic scene reconstruction, the paper’s title should explicitly include the term ‘dynamic,’ and comparative results with dynamic 3D reconstruction methods like [2] should be included to provide context and highlight advancements.

3. One of the main contributions is the introduction of 'motion tokens' in the Transformer’s input sequence, alongside the unique loss function components (reconstruction loss, sky loss, and velocity regularization loss). However, the absence of ablation studies makes it difficult to discern the effectiveness of these specific modules. Adding ablation studies would enhance the paper by showing the impact of each proposed component.

### Questions
1. Could the authors include comparisons across multiple datasets to validate the generalizability of the proposed method?
2. Could the authors provide ablation studies to demonstrate the effectiveness of each proposed module in the method?

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
3

### Summary
This paper introduces a novel pipeline called STORM for dynamic scene reconstruction in real-world environments. 

The core concept involves aggregating reconstructed 3D Gaussians and their motion into a unified representation, enabling the rendering of an amodal representation at any specified time step. 

Additionally, to ensure STORM's effectiveness in diverse scenarios, several significant enhancements have been implemented. 

Experimental results demonstrate the efficacy of the proposed method.

### Strengths
1. The paper is well-written and accessible, making it easy to follow the proposed approach.

2. The core idea is straightforward and well-conceived. By integrating 3D Gaussians into a unified representation, STORM enables rendering at any time step, allowing the entire network to be supervised by the color of the target time step.

3. The experiments are comprehensive and informative, demonstrating the effectiveness of the overall pipeline as well as specific enhancements, such as Latent-STORM.

### Weaknesses
The experiments are conducted solely on the Waymo Open Dataset, which may raise concerns about STORM’s robustness and generalizability to other datasets.

### Questions
The paper highlights that previous reconstruction methods rely on “dense observations across space and time,” whereas STORM “reconstructs dynamic 3D scenes from sparse, multi-timestep, posed camera images.” An insightful ablation study would involve varying the number of camera views and input time steps to assess how effectively STORM performs with different levels of view sparsity. This would provide a clearer understanding of the system's robustness under sparse observation conditions.

### Soundness
3

### Presentation
3

### Contribution
3
