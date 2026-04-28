# UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Recent advancements in multi-modal 3D pre-training methods have shown promising efficacy in learning joint representations of text, images, and point clouds. However, adopting point clouds as 3D representation fails to fully capture the intricacies of the 3D world and exhibits a noticeable gap between the discrete points and the dense 2D pixels of images. To tackle this issue, we propose UniGS, integrating 3D Gaussian Splatting (3DGS) into multi-modal pre-training to enhance the 3D representation. We first rely on the 3DGS representation to model the 3D world as a collection of 3D Gaussians with color and opacity, incorporating all the information of the 3D scene while establishing a strong connection with 2D images. Then, to achieve Language-Image-3D pertaining, UniGS starts with a pretrained vision-language model to establish a shared visual and textual space through extensive real-world image-text pairs. Subsequently, UniGS employs a 3D encoder to align the optimized 3DGS with the Language-Image representations to learn unified multi-modal representations. To facilitate the extraction of global explicit 3D features by the 3D encoder and achieve better cross-modal alignment, we additionally introduce a novel Gaussian-Aware Guidance module that guides the learning of fine-grained representations of the 3D domain. Through extensive experiments across the Objaverse, ABO, MVImgNet and SUN RGBD datasets with zero-shot classification, text-driven retrieval and open-world understanding tasks, we demonstrate the effectiveness of UniGS in learning a more general and stronger aligned multi-modal representation. Specifically, UniGS achieves leading results across different 3D tasks with remarkable improvements over previous SOTA, Uni3D, including on zero-shot classification (+9.36%), text-driven retrieval (+4.3%) and open-world understanding (+7.92%).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel multi-modal pre-training method, UniGS, designed to achieve more general and efficient joint representations of text, images, and point clouds. The innovative introduction of 3D Gaussian Splatting (3DGS) and the proposed Gaussian-Aware Guidance module achieve leading results in different 3D tasks. The experiments are solid and can confirm the effectiveness of the proposed method.

### Strengths
The proposed approach can achieve state-of-the-art performance on various challenging datasets, which demonstrates the effectiveness in learning strong cross-model representations.

### Weaknesses
1）No detailed explanation was given on how negative samples were selected. Do different tasks need to adjust the negative sample strategy?
2）There are significant differences in the structural and spatial characterization of 3DGS and traditional point cloud data. Does it affect the final performance？

### Questions
See weakness.

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
4

### Summary
This paper presents a text-image-3D pre-training framework that leverages 3DGS as the 3D representation for multi-modal representation. Experiments on various datasets are conducted.

### Strengths
- The proposed method has good performance on various multi-modal datasets.
- The experimental results are given on two different datasets COCO and VisDrone.

### Weaknesses
 - Uni3D has used one model to unify the 3D representations from different models, which can be used to align with image and text. What is the main advantage of proposed method using 3DGS.
- The proposed method introduces 3DGS for feature experimentation. Does it increase computational cost.
- It seems that most experiment are not inconsistent with the results in Uni3D. In this paper, the performance are relatively poor. What is the difference.
- I think that it is better to use the similar settings as Uni3D for experiments.

### Questions
I suggest that the authors provide more experiments and illustrations for the questions in weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
UniGS introduces 3D Gaussian Splatting (3DGS) into multi-modal pre-training to address the limitations of point clouds in capturing the full complexity of 3D scenes. By representing the 3D world as collections of colored, opaque Gaussians, UniGS bridges the gap between discrete 3D points and dense 2D images. Starting from a pre-trained vision-language model, UniGS aligns 3DGS with text and image representations, creating a unified multi-modal representation. A Gaussian-Aware Guidance module further enhances fine-grained 3D feature learning and cross-modal alignment. Tested on Objaverse, ABO, MVImgNet, and SUN RGBD datasets, UniGS shows substantial improvements over the previous state-of-the-art Uni3D.

### Strengths
1. The improvement gain is significant compared with previous methods, which shows the effectiveness of using 3DGS as the unified 3D representation.

2. The paper introduces an innovative Gaussian-Aware Guidance module that utilizes priors from pre-trained point cloud encoders as an initialization to enhance the learning of 3DGS features. This design is effective since it doesn't require training from scratch but can make use of existing models from a different 3D representation.

3. The intuition to use 3DGS as the unified 3D representation is novel and reasonable. To the best of my knowledge, it seems to be the first paper to use 3DGS as the unified 3D representation to bridge multimodal.

### Weaknesses
1. Figure 2 could provide an overall description of the information flow (like how this pipeline works in general) in the caption. Also, the figure could be improved by adding some diagrams to represent downstream tasks instead of using text only.

2. I think one significant weakness of using 3DGS as a unified 3D representation is that, usually raw data doesn't use this representation, like point cloud from a Lidar sensor. In this way, this method needs to optimize or process a 3DGS using those raw data (let me know if I understand incorrectly), then leverage this unified 3D representation to conduct downstream tasks. It could be computationally expensive. It seems that this paper does not provide the computation cost for inference, I would appreciate it if authors could include this and discuss this potential weakness.

3. L56-L60, the paper discusses the weakness of using point clouds as a 3D presentation due to the discrete representation. How about other potential 3D representations? Like depth maps or NeRF, which do not suffer from the discrete representation. I think some discussion among all potential 3D representations will help to justify the choice of using 3DGS as the unified 3D representation.

### Questions
1. L56-L60, the paper discusses the weakness of using point clouds as a 3D presentation due to the discrete representation. How about other potential 3D representations? Like depth maps or NeRF, which do not suffer from the discrete representation. I think some discussion among all potential 3D representations will help to justify the choice of using 3DGS as the unified 3D representation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a system for computing a joint embedding of images, text and 3D models (similar to an extension to CLIP). The paper proposes to use gaussian splats as the 3D representation instead of using point clouds to represent 3D shapes.

### Strengths
Building joint representations across different modalities is an interesting direction of work. Including 3D shapes can have lots of applications (which would be good to discuss in the paper).

### Weaknesses
I miss clear experiments that help understand the benefit of using 3D gaussian splats as the representation of 3D shapes instead of using point clouds. For instance, what numbers do you get in table 3 if you use the architecture used in UniGS but replacing the GS with point clouds?

Can you provide some scenarios in which it is useful to have the representation you propose?

The paper has no visual results. There are only tables with numbers. But it is hard to get an intuition of what the numbers mean and what the results look like just by reading those tables. It would be helpful to show some visual illustrations. You could show examples if 3D retrieval when the query is a 2D image.

Caption in figure 2 could provide some details to help interpret the system sketch. Figure 1, figure 2 and figure 3 seem redundant. It would be clearer if they were integrated into a more comprehensive system description.

Section 3.1 is not very helpful, presents standard material and it is not particularly clear. Section 3.2, which introduce the architecture proposed in the paper, is short.

Some typos:
Line 32: “to achieve Language-Image-3D pertaining,” -> pretraining?
Line 239: “for understanding the relationships between global position and feature.” What feature?
Line 253: “We donate the process”, -> denote. 

Section 3.4 is not very clear.  It will be helpful if figure 3 had the same notation than the one used in section 3.4. For instance, where is f_{fun}, f_{adv}? Then, in line 257 the notation changes again introducing f’_{fun} and f’_{adv}.  Why do you add the single quote ‘?

It would be helpful to add figures with some visual examples and comparisons across different methods. How helpful is to use GS versus point clouds?

The experimental results section has a lot of tables, but they are not clearly described. For instance, section 4.3 only briefly describes table 5, but it is not clear what the table shows. If this is not central to the paper, this table and section could be moved to the supplementary material section and the extra space can be used to better describe the other experiment and add a figure with visual results.

### Questions
1. Caption in figure 2 could provide some details to help interpret the system sketch. Figure 1, figure 2 and figure 3 seem redundant. It would be clearer if they were integrated into a more comprehensive system description.

2. Section 3.1 is not very helpful, presents standard material and it is not particularly clear. Section 3.2, which introduce the architecture proposed in the paper, is short.

3. Some typos:
Line 32: “to achieve Language-Image-3D pertaining,” -> pretraining?
Line 239: “for understanding the relationships between global position and feature.” What feature?
Line 253: “We donate the process”, -> denote. 

4. Section 3.4 is not very clear.  It will be helpful if figure 3 had the same notation than the one used in section 3.4. For instance, where is f_{fun}, f_{adv}? Then, in line 257 the notation changes again introducing f’_{fun} and f’_{adv}.  Why do you add the single quote ‘?

5. It would be helpful to add figures with some visual examples and comparisons across different methods. How helpful is to use GS versus point clouds?

6. The experimental results section has a lot of tables, but they are not clearly described. For instance, section 4.3 only briefly describes table 5, but it is not clear what the table shows. If this is not central to the paper, this table and section could be moved to the supplementary material section and the extra space can be used to better describe the other experiment and add a figure with visual results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that point clouds, as 3D representations, cannot fully capture the intricacies of the 3D world. To address this, it proposes the use of 3D Gaussian primitives instead of point clouds. The authors introduce a pretraining strategy to align the 3D Gaussian features with those of a pretrained vision-language model, establishing a shared visual and textual space through extensive real-world image-text pairs. Additionally, they propose a Gaussian-Aware Guidance module that leverages priors from pretrained point cloud encoders to guide the learning of Gaussian features, enhancing 3D understanding. The proposed approach achieves state-of-the-art performance across various challenging datasets.

### Strengths
1. Introduction of 3D Gaussian Primitives: It proposes a novel representation using 3D Gaussian primitives, offering a potential alternative to point clouds for improved 3D modeling.
2. Alignment with Vision-Language Models via Pretraining: The pretraining strategy aligns 3D Gaussian features with a pretrained vision-language model, enabling a shared visual-textual space through large-scale real-world image-text pairs.
3. Gaussian-Aware Guidance Module: The proposed module leverages pretrained point cloud encoders to guide the learning process, helping the 3D Gaussian features improve their understanding and representation capabilities.
4. State-of-the-Art Performance: The method demonstrates superior results, achieving state-of-the-art performance across some of the datasets against point cloud-based counterparts.

### Weaknesses
This paper has several weaknesses that should be addressed:

1. Lack of Comparison with Related Works: While the authors contend that 3D Gaussian primitives (3DGS) offer a superior 3D representation, the paper does not provide comparisons with other relevant works, such as [1], [2], [3], and [4]. These works utilize Neural Radiance Fields (NeRF), which offer similar advantages for 3D perception tasks, as mentioned in Lines 63-70. Specifically, the paper should include quantitative comparisons with NeRF-based methods on tasks such as zero-shot classification and object retrieval, which would provide a more comprehensive evaluation of the proposed approach. The absence of such comparisons makes it difficult to assess the true novelty and effectiveness of 3DGS compared to existing state-of-the-art techniques.

2. Insufficient Clarity in the Implementation Details: The paper lacks clear explanations regarding the methodology, leaving certain aspects ambiguous. For example, the exact process of initializing the 3D Gaussian primitives is not well-defined. It is unclear whether the initial Gaussian parameters are randomly generated or derived from the input data, such as point clouds or meshes. This lack of clarity makes it challenging to reproduce the results and understand the contribution of each component. Additionally, the paper does not specify the optimization algorithm used for training the 3D Gaussian features, which is a critical detail for ensuring reproducibility.

3. Unsubstantiated Hypothesis: Without addressing the aforementioned issues, the core hypothesis that 3D Gaussian primitives are a better representation than point clouds remains unconvincing. A thorough comparison and clearer implementation details are necessary to support this claim effectively. The paper needs to provide more evidence to demonstrate the advantages of 3DGS over point clouds, especially in terms of computational efficiency and representation power. The current results do not sufficiently justify the claim that 3DGS is a superior alternative, particularly given the additional optimization required for 3DGS compared to directly using raw point cloud data.

4. Improving these weaknesses could strengthen the paper’s claims, which may lead me to consider raising its rating.

### Questions
1. Clarification on NeRF-based Methods: Could you clarify why NeRF-based methods were not discussed in this work? Are there any specific disadvantages that prevented you from considering them as alternatives to 3DGS?

2. Evaluation of Computational Time: Have you evaluated the runtime of your method? While 3D Gaussian primitives may offer several advantages, they require an additional optimization process that point clouds do not, as point clouds represent raw data directly from 3D sensors. This suggests that 3DGS involves additional time for optimization, which is not discussed in the paper. Could you provide more details on this aspect?

3. Initialization with Point Clouds: For clarification, did you use sample raw point clouds from meshes to initialize the Gaussian primitives for the experiments (for ABO and Objaverse) presented in your main results? If so, could you explain why, in some datasets (such as ABO in Table 2), the performance of 3DGS falls short compared to point cloud methods?

4. Clarification on Baseline Performance and Experimental Settings: Could you elaborate on how the performance of the baseline models was obtained? Additionally, how does the experimental setting of the results reported in your paper (Table 2, Lines 328-329, showing 38.17% top-1 accuracy) differ from the Objaverse-LVIS zero-shot classification performance reported in Uni3D[5] (Table 1)? A detailed comparison would clarify any discrepancies.

**References:**

[1] Jeong, et al. (2022). Perfception: Perception using radiance fields. Advances in Neural Information Processing Systems, 35, 26105-26121.

[2] Hu, et al. (2023). Nerf-rpn: A general framework for object detection in nerfs. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,* (pp. 23528-23538)

[3] Li, et al. (2024). GP-NeRF: Generalized Perception NeRF for Context-Aware 3D Scene Understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 21708-21718).

[4] Ballerini, et al. (2024). Connecting NeRFs Images and Text. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshop (pp. 866-876).

[5] Zhou, et al. (2024). Uni3D: Exploring Unified 3D Representation at Scale. In The Twelfth International Conference on Learning Representations.

### Soundness
3

### Presentation
3

### Contribution
3
