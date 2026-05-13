# UpFusion: Novel View Diffusion from Unposed Sparse View Observations

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
\vspace{-2mm}
We propose UpFusion, a system that can perform novel view synthesis and infer 3D representations for an object given a sparse set of reference images \emph{without} corresponding pose information. Current sparse-view 3D inference methods typically rely on camera poses to geometrically aggregate information from input views, but are not robust in-the-wild when such information is unavailable/inaccurate. 
In contrast, UpFusion sidesteps this requirement by learning to implicitly leverage the available images as context in a conditional generative model for synthesizing novel views. 
We incorporate two complementary forms of conditioning into diffusion models for leveraging the input views: a) via inferring query-view aligned features using a scene-level transformer, b) via intermediate attentional layers that can directly observe the input image tokens. We show that this mechanism allows generating high-fidelity novel views while improving the synthesis quality given additional (unposed) images. 
We evaluate our approach on the Co3Dv2 and Google Scanned Objects datasets and demonstrate the benefits of our method over pose-reliant sparse-view methods as well as single-view methods that cannot leverage additional views. Finally, we also show that our learned model can generalize beyond the training categories and even allow reconstruction from self-captured images of generic objects in-the-wild.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents UpFusion, a system that can generate novel views from a sparse set of uncalibrated multi-view images. Technically, UpFusion consists of two parts: 1) the first part is a modified UpSRT which encodes unposed images into a set representation and renders the feature maps for the target view, 2) while the second part is a diffusion-based ControlNet, which generates the novel view conditioned on the set representation and the decoded feature map.
During training stage, UpSRT and ControlNet are optimized separately.

### Strengths
+ The paper is well-written and well-structured. The problem setting is both innovative and ambitious, as it seeks to address two issues of considerable interest within the research community: 1) reconstruction from sparse views and 2) generation from unposed images, simultaneously.

+ The proposed method is intuitive, and this paper presents specific details and dedicated designs that are well-suited for the challenges inherent to the problem under investigation.

+ The empirical results demonstrate the method's remarkable performance in generating novel views from a few-shot unposed images when compared to the baseline approaches.

### Weaknesses
- The problem formulation lacks clarity. Without specifying poses from images, it becomes ambiguous to define the pose of a target view unless canonical poses are provided. However, canonicalization necessitates per-category calibration, and it has been observed that such methods are specific to certain categories. To further validate the effectiveness of the approach, it is recommended to test the pre-trained UpFusion on additional data domains, such as Blender, LLFF, or Shiny datasets [1].

- Empirical comparisons are insufficient in relevant baseline models. For the task of novel view synthesis, it is advisable to include comparisons with end-to-end pose optimization baselines, such as BARF [2] and NoPe-NeRF [3]. Since this paper asserts novel view generation from sparse views using diffusion, it would also be equitable to compare with state-of-the-art single-image-to-3D baselines such as Zero-123 [4].

- From a technical perspective, despite notable engineering efforts, the proposed method appears to be a combination of existing methods: SRT, ControlNet, and DreamFusion. It also structurally resembles GeNVS [5]. The modifications to UpSRT, specifically the use of a DINOv2 backbone, are not sufficiently justified. The paper does not provide a clear explanation of why DINOv2 features are expected to be more beneficial than the original CNN features for this particular task, especially given that DINOv2 is primarily designed for correspondence tasks, and it's not immediately obvious how this translates to improved view synthesis.

- The paper lacks a discussion and comparison with some relevant prior work, particularly with references [6] and [7].

### Questions
1. The evaluation scheme proposed in Sec. 4.1.2 is designed to mitigate pose ambiguity. However, the enforcement of per-view alignment may introduce more confusion in the evaluation results, making it challenging to assess whether the proposed method can accurately generate views at specified camera poses and maintain smooth views along a camera trajectory. To enhance the evaluation methodology, it is recommended that the authors consider implementing a global alignment across all views collectively, rather than performing alignment on a per-frame basis.

2. Could the authors provide insights into the motivation behind making the specific modifications to UpSRT?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework for 3D-aware novel view synthesis given sparse 2D views without camera poses. Leveraging the features of the 2D views from an UpSRT encoder-decoder, it predicts a view-aligned spatial feature for the target view and a set-invariant feature, and feeds them to Stable Diffusion as conditioning inputs to generate the novel views. Moreover, it also incorporates an underlying 3D representation with NeRF to further enforce view consistency.

### Strengths
- The paper combines view-aligned spatial features and set-invariant features from unposed 2D views and leverages in novel-view diffusions, which sounds natural.
- Both qualitative and quantitative results show that the proposed framework outperforms the prior works not integrating these modules.

### Weaknesses
 - Experimental comparisons with existing works seem limited. The following works are also related and could be discussed in the paper: [1,2,3,4,5]. Several of these works, as well as the single-/few-view NeRF synthesis works mentioned in the related work section, can be compared with the proposed method experimentally. Specifically, the single-view works also don't rely on relative poses, though the setup is not exactly the same as this paper, they can still be compared.
- Quantitatively, the UpFusion 3D model has much better numbers than the 2D model, but visually it loses a lot of geometric details compared to the 2D results. Is it limited by the representation power of the 3D NeRF? Or is it because the learned features are not very view-consistent?


### Questions
- Comparing the 2D and the 3D UpFusion model, I understand that the PSNR and SSIM of the 3D model are better, but why is the LPIPS also better? -- LPIPS is not a pixel-aligned metric, while visually the 2D results look cleaner and have much more details than the 3D ones.
- It seems that the generated views sometimes have inconsistent colors as the input view (e.g. the blue bench and the blue umbrella in Fig. 8, Appendix A). Is there any explanation for this?
- I wonder how the proposed method compares to this baseline: first running COLMAP to estimate the relative poses of the input views, and then running a pose-dependent 3D synthesis method?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on view synthesis from unposed images. Scene Representation Transformer, diffusion model, and controlnet branch are utilized to effectively perform the task on object-level novel view synthesis.

### Strengths
SRT + Diffusion are adopted to study the challenging task of novel view synthesis from unposed images.

### Weaknesses
The experiments are conducted on object-level generation. As the authors also mentioned in the related works section, single view image-to-3d is highly related to the task UpFusion trying to solve. Single view input can also be considered as input image without pose. As a result, I believe the contributions of UpFusion can be better justified when comparing to existing single view novel view synthesis works, for example [1].
Besides, a couple of references are missing [2] (also on Co3D dataset), [3][4] (SDS-based).

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduce UpFusion, a view synthesis method derived from a collection of unposed images. The core design philosophy of UpFusion centers around the use of a Scene Representation Transformer, combined with a Diffusion Model to infuse intricate object details. Subsequently, instance-specific neural representations are introduced to achieve 3D-consistent rendering outcomes.

### Strengths
Scene Representation Transformer (SRT) is renowned as an effective neural renderer that can seamlessly generalize to the rendering of novel scenes and views. However, the SRT represents an image in the latent space, often resulting in blurry rendered outcomes, as evidenced in Fig 2 of this paper. UpFusion examines the constraints in SRT and suggests employing a following diffusion model and an instance-specific 3D representation to enrich the details. Specifically, the denoising diffusion model and a control net branch are employed to master a generative model for novel views of an object, and the instance-specific representation adheres to the paradigm in Score Distillation Sampling to extract a consistent 3D representation.

### Weaknesses
- The reviewer recommends that the authors emphasize the object-level NVS configuration in the title since the methodology chiefly addresses "objects" and the experiments were executed on the "CO3D" dataset.
- Object-level 3D generation (sourced from unposed images or a single image) remains a hot research topic. There exists a plethora of related papers [1,2,3, 4]. However, pivotal experimental comparisons with [1,2,3,5] are missing. Notably, single-view based NVS can ignore the requirment for camera poses: [1,2,3] all necessitate an object-specific representation, while [5] solely requires a forward-pass for view generation.
- What are the specifics regarding the training time for each instance? Considering [4] also employs a 3D representation to tackle a similar scenario, but does not incorporate the SRT and diffusion model, it's useful for the authors to showcase the merits of solely leveraging a 3D representation. Further, comparisons excluding the SRT/Diffusion model or contrasting it against [4] would be insightful.
- The CO3D dataset is characterized by various backgrounds, yet the authors omit the background modeling in the manuscript (possibly using the masks in CO3D). Even though object-level NVS publications typically sidestep background modeling, it's essential to accentuate this specific operations in the experimental framework.
- In terms of the claim 3D consistent generation, it would be useful if the authors could provide diverse rendered video of different objects, as well as producing metrics for your claim.

### Questions
See the recommendated experiments in **Weaknesses** .

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
