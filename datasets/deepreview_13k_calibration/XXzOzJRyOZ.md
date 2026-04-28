# Incorporating Visual Correspondence into Diffusion Model for Visual Try-On

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Diffusion models have shown preliminary success in virtual try-on (VTON) task. The typical dual-branch architecture comprises two UNets for implicit garment deformation and synthesized image generation respectively, and has emerged as the recipe for VTON task. Nevertheless, the problem remains challenging to preserve the shape and every detail of the given garment due to the intrinsic stochasticity of diffusion model. To alleviate this issue, we novelly propose to explicitly capitalize on visual correspondence as the prior to tame diffusion process instead of simply feeding the whole garment into UNet as the appearance reference. Specifically, we interpret the fine-grained appearance and texture details as a set of structured semantic points, and match the semantic points rooted in garment to the ones over target person through local flow warping. Such 2D points are then augmented into 3D-aware cues with depth/normal map of target person. The correspondence mimics the way of putting clothing on human body and the 3D-aware cues act as semantic point matching to supervise diffusion model training. A point-focused diffusion loss is further devised to fully take the advantage of semantic point matching. Extensive experiments demonstrate strong garment detail preservation of our approach, evidenced by state-of-the-art VTON performances on both VITON-HD and DressCode datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach for virtual try-on tasks, addressing the challenge of preserving garment shape and fine-grained details. Specifically, the authors propose Semantic Point Matching Diffusion (SPM-Diff), a model that leverages structured semantic points as visual correspondence cues between garments and target human models. By mapping 2D semantic points to 3D-aware cues through depth and normal maps, SPM-Diff aligns garment details closely with the target human body. Experimental results on VITON-HD and DressCode datasets demonstrate the effectiveness of SPM-Diff.

### Strengths
- The paper leverages semantic point matching as a prior to enhance garment shape and texture preservation.

- Extensive testing on the VITON-HD and DressCode datasets demonstrates the model's robustness and superior performance.

- The authors have provided the code to ensure reproducibility of their results.

### Weaknesses
 - In line 254, local flow warping is used as a method to associate semantic points with their counterparts on the target person. It would be better to provide more detail on the local flow warping process for better understanding.

- For Figure 5, it’s difficult to assess the accuracy of the matched points. Using different colors (e.g. red and green) to illustrate correct and incorrect mappings would improve clarity.

- Adding a figure to illustrate feature injection would help clarify how point features are incorporated into the Main-UNet.

### Questions
- Could you provide more details on the local flow warping process?

- In Figure 5, are all the points shown the correct correspondences? If not, would it be possible to use different colors to distinguish correct from incorrect point mappings? Additionally, how do you assess the accuracy or correctness of these point mappings?

- It would be better to include a figure to illustrate the feature injection process, specifically showing how point features are integrated into the Main-UNet?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents SPM-Diff, a virtual try-on framework utilizing diffusion models that maintain garment details and shape leveraging visual correspondence. Due to warping variability, traditional VTON methods using diffusion models have difficulty preserving garment features. SPM-Diff addresses this issue by focusing on "semantic points" in garment images that capture detailed textures and shapes. Experiments on the VITON-HD and DressCode benchmarks show that SPM-Diff achieves state-of-the-art results in virtual try-on.

### Strengths
1. By identifying and aligning stable "semantic points" between garment and human images, SPM-Diff effectively reduces randomness in diffusion models, enabling precise and accurate garment reproduction.

2. The incorporation of 3D depth and normal maps enhances realism by accurately controlling garment fit over the body, reflecting considerable thought in modeling garment behavior in 3D space.

### Weaknesses
1. SPM-Diff's dependence on semantic points may lead to instability when many points are used due to interpolation and projection errors, as discussed regarding point count sensitivity. The paper does not explore the impact of different point selection strategies, which could mitigate these issues. For instance, using a more robust point selection method, such as those based on keypoint detectors or learned feature maps, might improve stability and reduce sensitivity to point count.

2. SPM-Diff relies heavily on accurate depth and normal maps, which may limit its generalization to datasets or images without dependable 3D cues. The paper does not discuss the robustness of the method to noisy or inaccurate depth and normal maps, which is a common issue in real-world scenarios. The performance degradation under varying levels of 3D cue quality should be evaluated, and potential solutions, such as incorporating uncertainty estimates, should be considered.

3. Although the model effectively preserves garment details, evaluations primarily concentrate on image quality metrics, neglecting user-centered metrics such as perceived realism in end-user studies. The paper lacks a comprehensive evaluation of the user experience, which is crucial for virtual try-on applications. User studies should assess the perceived realism, fit, and overall satisfaction with the generated try-on results.

4. Introducing "visual correspondence" into diffusion for virtual try-on is not new. Please clarify the "Semantic Point Matching" with "Warping parameters learning". The paper does not clearly articulate the novelty of the semantic point matching approach compared to existing warping-based methods. A more detailed comparison of the technical differences and advantages of the proposed method is needed, especially concerning how it addresses the limitations of traditional warping techniques.

### Questions
The core idea of this paper is to integrate visual correspondence into the diffusion model. However, visual correspondence is not a new thing that is widely used in traditional try-ons. In addition, some people used warping + diffusion, such as : WarpDiffusion: Efficient Diffusion Model for High-Fidelity Virtual Try-on.

Please clarify their differences and provide more details about the novelty, not just replace "warping" with "visual correspondence".

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
This paper presents a new method for virtual try-on by enforcing explicit correspondence through structured semantic points, which are first extracted from the garment image and then warped into the target body pose through local flow warping. The pair of points then serve as priors to guide the overall generation process of the try-on diffusion model, composed of a garment reference net and a main generation net. Experiments demonstrate this method generates high-quality try-on results.

### Strengths
1.	The proposed method is able to generate high-quality virtual try-on results. Experiments show that the proposed method outperforms existing pipelines.
2.	The idea of the paper that adopts pair of semantic points to facilitate the generation process and serve as an extra supervision signal is interesting and reasonable. If robust corresponding points could be found between the garment and the target body, they could be very good priors to boost the diffusion process. 
3.	The paper is well-written and easy to follow.

### Weaknesses
The main weakness of the paper is on semantic point matching.
a)	How to acquire robust and accurate point matching should be the focus of the paper. However, this paper did not address this problem but rely on the local warping method proposed in GP-VTON[1], which is another virtual try-on method. This raises the concern about the contribution. The paper does not sufficiently explore the limitations of the warping method, particularly in cases of significant pose variations or occlusions, which could lead to inaccurate point correspondences and degrade the performance of the proposed method. The reliance on an existing method without a thorough analysis of its failure modes weakens the overall contribution.
b)	The evaluation of the accuracy of the point-matching method is very limited. The point matching should achieve much more accurate results than the base diffusion model thus it could be used as a prior to guide the generation process. However, this is not demonstrated in the paper. The paper lacks a quantitative analysis of the point matching accuracy, such as reporting the average distance between the predicted and ground truth correspondences. Without such metrics, it's difficult to assess the effectiveness of the point matching and its impact on the final try-on results. Furthermore, the paper does not compare the point matching performance with other state-of-the-art methods, which could further highlight the limitations of the chosen approach.

### Questions
There are a few questions apart from the weakness:
1.	As the local flow warping adopted in the paper relies on the coarse human body estimated with SMPL, I doubt if the warping method is capable of dealing with loose clothes like dresses or skirts. If not, will the proposed point prior still work to facilitate the generation process and get a good result?
2.	In lines 262-264, the author claims that pre-trained garment/geometry feature encoders are adopted to extract features for the following generation process, but I could not find any clarification on how these encoders were obtained. The author should clarify this.

### Soundness
3

### Presentation
3

### Contribution
2
