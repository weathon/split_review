# Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
3D Gaussian Splatting (3DGS) has achieved excellent rendering quality with fast training and rendering speed. However, its optimization process lacks explicit geometric constraints, leading to suboptimal geometric reconstruction in regions with sparse or no observational input views. In this work, we try to mitigate the issue by incorporating a pre-trained matching prior to the 3DGS optimization process. We introduce Flow Distillation Sampling (FDS), a technique that leverages pre-trained geometric knowledge to bolster the accuracy of the Gaussian radiance field. Our method employs a strategic sampling technique to target unobserved views adjacent to the input views, utilizing the optical flow calculated from the matching model (Prior Flow) to guide the flow analytically calculated from the 3DGS geometry (Radiance Flow). Comprehensive experiments in depth rendering, mesh reconstruction, and novel view synthesis showcase the significant advantages of FDS over state-of-the-art methods. Additionally, our interpretive experiments and analysis aim to shed light on the effects of FDS on geometric accuracy and rendering quality, potentially providing readers with insights into its performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
the geometric under-constrain problem of 3D Gaussian Splatting (3DGS) in sparse view setups. By incorporating pre-trained matching priors into the optimization process of 3DGS, this method significantly improves both the geometric accuracy and rendering quality of 3DGS.

### Strengths
The method proposed in this paper integrates matching priors derived from a pretrained optical flow model to guide the optimization of 3DGS. This approach effectively enhances both the reconstruction quality and rendering quality of existing 3DGS-based methods.

The methodology is well-structured, providing clear and detailed explanations of the proposed FDS technique, the adaptive camera sampling scheme, and the associated loss functions.

Comprehensive experimental evaluations are conducted across multiple datasets, demonstrating the method's effectiveness and robustness.

Additionally, the paper includes interpretive experiments to illustrate the mutual refinement process of the flows, thereby enhancing the understanding of the method's capabilities.

### Weaknesses
The results of the proposed method are constrained by the initial quality of the prior flow, however, the reliability of the prior flow cannot be assured under certain sparse viewpoint configurations. Specifically, the method does not explicitly address scenarios where the optical flow estimation might be inaccurate due to large occlusions or significant changes in viewpoint between the input and sampled views. This could lead to suboptimal performance in challenging cases where the prior flow is not a reliable guide for the 3DGS optimization.

As noted in the limitations section, the method's reliance on the performance of a pretrained optical flow model restricts its generalizability. The paper does not explore the sensitivity of the proposed approach to different optical flow models or the potential impact of domain mismatch between the training data of the optical flow model and the target scenes. This reliance on a specific pre-trained model limits the applicability of the method in scenarios where such models may not be readily available or perform well.

While the authors have conducted experiments across multiple datasets, it is important to point out that these datasets are primarily limited to indoor scenes. It is recommended that the authors evaluate their method on a more diverse range of datasets to assess its applicability in various scenarios. The lack of evaluation on outdoor scenes or datasets with more complex geometry and lighting conditions raises concerns about the robustness and generalizability of the method.

The paper lacks a discussion on the computational complexity of the method. It is recommended that the authors include a detailed report on the training and inference times of the model in the experimental section, along with comparative metrics against other existing methods. Without a clear understanding of the computational cost, it is difficult to assess the practical applicability of the proposed approach, especially in resource-constrained environments.

### Questions
In the related work section, the review of existing prior art aimed at improving 3DGS performance should be more comprehensive and clearer, particularly concerning the relevant work on optical flow priors. Additionally, in the subsection on Prior Regulation for Rendering, there are sentences with grammatical errors that require careful review and correction.

In Algorithm 1, there are notation errors that need careful checking and correction.

The comparison of depth reconstruction experiments needs to be supplemented with results from other methods to validate the superiority of the proposed approach in geometric reconstruction.

In the dataset section, the paper mentions that the authors have evaluated their method on the Replica dataset, but the experimental results are not presented.

The authors provide limited comparisons with existing methods; it is recommended that they include more baseline methods for a more robust evaluation.

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
The paper proposes a optical flow based regularization for 3D and 2D Gaussian Splatting. It compares the optical flow output between an input view and a sampled unobserved view to a so-called radiance flow determined from the camera motion and the reconstructed scene. The authors claim that a loss on the difference between the radiance flow an the optical flow results in improved geometry and view synthesis quality. Experiments show improved performance of 3DGS and 2DGS with flow distillation on the SceneNet, Mushroom and Replica dataset.

### Strengths
- The paper describes an interesting idea on incorporating a flow prior for 3D reconstruction with Gaussian Splatting.
- The related works contains all relevant geometry reconstruction-based 3DGS works and set them in context to the proposed method.
- The approach is simple and easy to understand, as Figure 1 and 2 are well done and intuitive.

### Weaknesses
 - The experimental evaluation only considered indoor room datasets, MuSHRoom, ScanNet and Replica. Baseline methods usually use more diverse datasets such as DTU [Jensen et al. 2014], Tanks and Tem-
ples [Knapitsch et al . 2017] and Mip-NeRF360 [Barron et al. 2022].
- The authors found that the depth distortion loss in 2DGS degrades the results. However they do not provide evidence or explanations for that and it is unclear how this influenced the quantitative comparison to 2DGS.
- The paper solely focus on 3DGS-based methods in the related work and also in the experimental evaluation. Comparisons to neural field based methods such as Geo-NeUS or NeuralAngelo would significantly strengthen the claim of state-of-the-art performance.
- The overall quality and the presentation should be improved, e.g. the conclusion is unspecific and contains general claims,  inconsistent capitalization of 'Gaussian', no explanation of \hat{\alpha} in equation 2.

### Questions
- The Radiance Flow maps pixels from the source view  to the target view. Considering pixels in the target view containing splatted Gaussians that are occlude in the source view, how is the Radiance Flow computed for these regions?
- In line 267, how does detaching the optical flow influence the overall performance?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to improve the 3D Gaussian Splatting reconstruction quality in regions with sparse or no observational input views, by integrating a pre-trained matching prior into the 3DGS optimization process. The matching prior is incorporated through optical flow from a pre-trained model, which supervises the Radiance Flow calculated using 3DGS-rendered depth. Additionally, the authors introduce a Flow Distillation Sampling scheme to efficiently sample unobserved camera views around the input views. The proposed Flow Distillation Loss effectively avoids the scale ambiguity existing in monocular priors. The authors present clear ablation studies and quanlitative improvements to support their claims.

### Strengths
- The idea is simple but makes intuitive sense. Matching priors can provide absolute scale information in constrast to monocular priors. This paper offers a promising direction of using pair-wise information prior to advance sparse view reconstruction.
- This ablation study clearly demonstrates the improvement benefited from using this pair-wise matching prior without scale ambiguity. The quanlitative results shown in Table 3. validate the advatange compared to monocular depth prior, even to multi-view depth prior. A clear visualization of the mutual refinement of two flows is also provided.

### Weaknesses
 - This paper lacks evaluation on widely used geometry reconstruction and novel view synthesis benchmarks such as DTU, Tanks and Temples, and MipNeRF 360. The advantages of the proposed method would be more convincing if the authors could present results on one or more of these benchmarks.
- As mentioned in line 252, both the Prior Flow and Radiance Flow suffer from inaccuracies, raising concerns about the stability of the benefits provided by the proposed Flow Distillation Loss. It is possible that this loss could introduce artifacts or incorrect guidance due to bias. While the metrics in Table 3 appear strong, it’s unclear why the loss significantly outperforms multi-view depth supervision, which does not suffer from inaccurate prior flow. More explanation and analysis are needed to clarify this point.

### Questions
- Given that RAFT is computed at every time step, how does the training time for 2DGS + FDS compare to 2DGS?
- Why do both monodepth and multi-view depth seem to only worsen the results, as shown in Table 3.?
- it's said in line 316 that, the normal prior is introduced for evaluation on the ScanNet dataset. But the metrics in Table 2. and Table 3. seem inconsistenct regarding the results of 2DGS + FDS. Does this mean the ScanNet result in Table 2. doesn't use the normal prior?
- Can 2DGS + FDS outperform 2DGS + Normal in Table 3.?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, Flow Distillation Sampling (FDS) is proposed to improve the geometric accuracy and rendering quality of  3D Gaussians Splatting.
FDS first adopts a camera sampling scheme to sample unobserved views near the training views, and then uses the flow predicted by the pre-trained model to guide the flow calculated from the 3DGS geometry.

### Strengths
1. The ideas are intuitive, the paper is well written and easy to understand.
2. FDS leverages the matching prior mitigate the overfitting problem and enhance the geometry.

### Weaknesses
1. More ablation studies are needed.
- The depth-adaptive radius is calculated by Eq. (8). How to determine the value of the hyperparameter $\sigma$? Is FDS robust to different $\sigma$?
- Is  FDS must require the normal consistency loss $\mathcal{L}_{n}$? In Table 3, how is the performance of “2D-GS+FDS”?
- How to determine the weight for FDS $\lambda_{fds}$?
- How to determine the start iteration (e.g., 15,000) of applying FDS?

2. Lack of visual comparison on the ScanNet dataset.

### Questions
See `Weakness`.

### Soundness
3

### Presentation
3

### Contribution
3
