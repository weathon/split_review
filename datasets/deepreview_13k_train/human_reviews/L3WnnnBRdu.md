# Hi-Gaussian: Hierarchical Gaussians under Normalized Spherical Projection for Single-View 3D Reconstruction

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Single-view 3D reconstruction is a fundamental problem in computer vision, having a significant impact on downstream tasks such as Autonomous Driving, Virtual Reality and Augment Reality. However, existing single-view reconstruction methods are unable to reconstruct the regions outside the input field-of-view or the areas occluded by visible parts. In this paper, we propose Hi-Gaussian, which employs feed-forward 3D Gaussians for efficient and generalizable single-view 3D reconstruction. A Normalized Spherical Projection module is introduced following an Encoder-Decoder network in our model, assigning a larger range to the transformed spherical coordinates, which can enlarge the field of view during scene reconstruction. Besides, to reconstruct occluded regions behind the visible part, we introduce a novel Hierarchical Gaussian Sampling strategy, utilizing two layers of Gaussians to hierarchically represent 3D scenes. We first use a pre-trained monocular depth estimation model to provide depth initialization for $leader$ Gaussians, and then leverage the $leader$ Gaussians to estimate the distribution followed by $follower$ Gaussians. Extensive experiments show that our method outperforms other methods for scene reconstruction and novel view synthesis, on both outdoor and indoor datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims at the single-view 3D reconstruction which follows the Splatter Image [Stanislaw et al] and proposes two techniques to solve the limited FOV and occlusions. To give a broader view range, the paper converts the pixel coordinates to a normalized  Spherical Projection and then enlarges the FOV during the projection. For occlusion, the paper splats more gaussians biased from the leader gaussians that come from the per-pixel splat. The experiments show good performances in outdoor datasets.

### Strengths
1. Quantitatively, the paper outperforms all other methods in semantic KITTI dataset and BundleFusion dataset.
2. The method gives a clear rendering in unbounded street views.

### Weaknesses
1. The differences between the paper and the splatter image are using a pre-trained monocular depth network, changing the pixel coordinate representation as spherical coordinate and splatting more gaussians using a leader and follower way. These contributions are a little incremental and do not show good insights into this field.
2. I argue the performances may highly depend on the pre-trained monocular depth. Please show more experiments that the paper’s ability to tolerate the bad depth prediction in some cases where UniDepth does not work. Or show more results for the zero-show generalization ability on other images like tank and temple, LLFF dataset.
3.  The qualitative results are not enough. For example, only the zoom-in effect is shown and the view range in indoor room is also limited. Moreover, no videos are present to see the 3D consistency of reconstruction.

### Questions
I mainly care about how much the paper depends on monocular depth estimation and generalization ability. Moreover, more qualitative results with arbitrary camera trajectory are also expected

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
They propose a generalizable single-view 3D reconstruction method with Normalized Spherical Projection module for larger FOV reconstrcution. Some validation results show the effectiveness.

### Strengths
The paper proposes to use normalized spherical projection for single view acne reconstruction and have some better results compared with baseline methods even though with blurry effects.

### Weaknesses
Although the paper has presented better experimental results against existing methods, some major concerns remain:

1. Among all the competitors, SceneRF is the most relevant, which is also dedicated to single-view reconstruction at scene level. However, by comparison, this work is much more restricted as it requires a pretrained depth estimation model while SceneRF is self-supervised. This  also renders the comparison between SceneRF and this work unfair in Table 1, due to the use of pretrained model. The reliance on a pre-trained depth model introduces a significant dependency and limits the method's applicability in scenarios where such models are unavailable or perform poorly. Furthermore, the performance gains observed might be attributed to the pre-trained model's capabilities rather than the proposed architecture itself, making the comparison with self-supervised methods like SceneRF less convincing.

2. The Normalized Spherical Projection module seems to be heavily influenced by the Spherical U-Net module in SceneRF, which again weakens the contribution of this paper. The similarity in concept and implementation raises questions about the novelty of this module. The paper should provide a more detailed analysis of the differences and justify the specific design choices made in the Normalized Spherical Projection module compared to the Spherical U-Net, and also provide ablation studies to show the effectiveness of the proposed module.

3. The significance of single-view Gaussian Splatting does not entirely convince me. The occluded areas are unseen in a single view, and yet not hallucinated by any learned priors in the method as well. In a practical view, what is the significance of single-view Gaussian Splatting when occluded areas are visually blurry or even nonsense? The method's inability to generate meaningful content in occluded regions severely limits its practical utility. Without a mechanism to infer or hallucinate plausible structures in these areas, the reconstruction is incomplete and potentially misleading, especially in complex scenes with significant occlusions.

### Questions
1.Do you retrain the compared methods with your evalution cameras for a fair comparison? 

2.How you select the training and testing cameras?

### Soundness
2

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
5

### Summary
The paper proposes a single-view 3D Gaussian Splatting (3DGS)-based 3D reconstruction method trained on a collection of posed images. This approach eliminates the need for expensive 3D ground-truth data for training and leverages the fast rendering capabilities of 3DGS. The method introduces two key contributions: a normalized spherical projection, which models information outside the field of view (FOV) while reducing the information compression typical of this projection, and hierarchical Gaussian sampling to effectively model occluded areas. The approach achieves SOTA performance in novel view synthesis in both outdoor and indoor datasets.

### Strengths
- The paper is well-written and clearly presented.
- The technical contributions are solid: Hierarchical Gaussian Sampling effectively models occluded areas—a critical challenge in single-view 3D reconstruction -- while the normalized spherical projection captures outside-FOV information, addressing limitations of the spherical projection used in existing techniques. Note that this Gaussian refers to the one used in 3DGS for rendering, not the Gaussian in SceneRF, which is only used to improve point sampling for NeRF.
- The experiments, including both the main results and ablation studies on novel view synthesis, are comprehensive and demonstrate the advantages of the proposed approach.
- Figures 8 and 9 are particularly helpful to understand the impact of the proposed components.

### Weaknesses
- The paper claims to address 3D reconstruction from a single image; however, it lacks any evaluation of 3D reconstruction. The paper should incorporate evaluations of 3D reconstruction and novel depth synthesis, similar to approaches like SceneRF, or include qualitative visualizations of 3D Gaussian distributions alongside depth maps, as demonstrated in pixelSplat, CVPR'24.

- The normalized spherical projection appears similar to the spherical projection technique proposed in SceneRF, with the primary difference being the normalization of x and y before projection. However, it's unclear how this normalization reduces spatial compression, as the paper suggests. What is the intuition behind this normalization?

- Figure 8 should be placed or at least referenced in Section 3.2 to illustrate the effect of normalization in spherical projection. Adding an explanation of the observed impact, specifically how normalization reduces black areas in the image, would help the readers understand more about the effect of the normalized spherical projection.

- Regarding Hierarchical Gaussian Sampling, since "leader" Gaussians are initialized using depth estimation, they are positioned on visible surfaces, with their distribution predominantly around these areas. It's unclear how "follower" Gaussians diverge from the "leader" Gaussian to cover occluded regions, given that they are sampled using the leader's distribution.

- Figure 7 would benefit from an additional column to highlight occluded scenery and areas outside the field of view in the novel view.

- The authors should clarify that the paper addresses single-view 3D reconstruction within a self-supervised setting, distinguishing it from monocular 3D reconstruction methods that often require 3D ground truth for supervision. I also think this is another selling point of the method and should be highlighted.

- On line 116, the authors mention choosing 3DGS over NeRF to achieve faster rendering speeds. Demonstrating the method's rendering speed relative to NeRF-based counterparts would provide valuable reference.

### Questions
Please refer to the Weaknesses section. I combined Weaknesses and Questions since they are linked and need to be together for better clarity.

### Soundness
4

### Presentation
4

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
The paper studies the problem of single-view 3D reconstruction in computer vision. Specifically,  a pre-trained monocular depth estimation model is used to provide initializations for the Gaussians, and an Encoder-Decoder network is employed to predict 3D Gaussian attributes from single-image inputs. A Normalized Spherical Projection module is proposed to expand the input FOV and enable reconstruction beyond the FOV, also a Hierarchical Gaussian Sampling strategy is proposed to reconstruct the occluded areas in the image. Experiments show that the proposed method performs favorably against the other competitors on scene-level single-view reconstruction.

### Strengths
The presentation is in general clear and easy to follow. The investigated problem of single-view reconstruction is of general interest to a broad audience.

### Weaknesses
Although the paper has presented better experimental results against existing methods, some major concerns remain:

1. Among all the competitors, SceneRF is the most relevant, which is also dedicated to single-view reconstruction at scene level. However, by comparison, this work is much more restricted as it requires a pretrained depth estimation model while SceneRF is self-supervised. This  also renders the comparison between SceneRF and this work unfair in Table 1, due to the use of pretrained model.

2. The Normalized Spherical Projection module seems to be heavily influenced by the Spherical U-Net module in SceneRF, which again weakens the contribution of this paper. 

3. The significance of single-view Gaussian Splatting does not entirely convince me. The occluded areas are unseen in a single view, and yet not hallucinated by any learned priors in the method as well. In a practical view, what is the significance of single-view Gaussian Splatting when occluded areas are visually blurry or even nonsense?

### Questions
Please respond to the three points made in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
1
