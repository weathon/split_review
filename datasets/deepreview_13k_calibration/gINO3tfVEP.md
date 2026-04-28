# Beyond 2D Representation: Learning 3D Scene Field for Robust Monocular Depth Estimation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Monocular depth estimation has been extensively studied over the past few decades, yet achieving robust depth estimation in real-world scenes remains a challenge, particularly in the presence of reflections, shadow occlusions, and low-texture regions. Existing methods typically rely on extracting front-view 2D features for depth estimation, which often fail to capture those complex physical factors present in real-world scenes, leading to discontinuous, incomplete, or inconsistent depth maps. To address these issues, we turn to learning a more powerful 3D representation for robust monocular depth estimation, and propose a novel self-supervised monocular depth estimation framework based on the Three-dimensional Scene Field  representation, or TSF-Depth for short. Specifically, we build our TSF-Depth framework upon an encoder-decoder architecture. The encoder extracts scene features from the input 2D image, and subsequently reshapes it as a tri-plane feature field by incorporating scene prior encoding. This tri-plane feature field is designed to implicitly model the structure and appearance of the continuous 3D scene. We then estimate a high-quality depth map from the tri-plane feature field by simulating the camera imaging process. To do this, we construct a 2D feature map with 3D geometry by sampling from the tri-plane feature field using the coordinates of points where the line of sight intersects with the scene. The aggregated multi-view geometric features are subsequently fed into the decoder for depth estimation. Extensive experiments on KITTI and NYUv2 datasets show that TSF-Depth achieves state-of-the-art performance. We also validate the generalization capability of our model on Make3D and ScanNet datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper argues that existing monocular depth estimation methods primarily focus on extracting front-view 2D features while neglecting 3D representations, which hinders their performance in various challenging real-world scenarios, including reflections, shadow occlusions, and low-texture regions. To address these limitations, the authors propose a 3D scene field representation within a self-supervised monocular depth estimation pipeline. They have conducted several ablation studies to validate the effectiveness of the proposed modules. Overall, the manuscript is well-structured and easy to follow.

### Strengths
The paper proposes multi-scale scene feature and tri-plane feature fields to model a multi-view representation. Based on the ablation study, the proposed method can improve depth accuracy. Although this idea is firstly applied in monocular depth estimation, it has been widely applied in single-image 3D generation.

### Weaknesses
1) The paper posits that the incorporation of 3D features enhances robustness and addresses complex real-world scenarios effectively. However, it primarily relies on an ablation study to assess accuracy improvements. While various techniques exist for optimizing model training to enhance performance, mere improvements in accuracy do not necessarily validate the robustness of the proposed features, particularly regarding their argued low-texture regions and reflective surfaces. It is advisable for the authors to include more relevant evaluations that present greater challenges.


2) In Ln267-Ln269, the paper asserts that the predicted multi-scale depths are affine-invariant, leading to the proposal of reconstructing multi-scale point clouds to address distortions induced by affine transformations. However, it is important to note that while an unknown scale does not result in geometric distortions, a shift does. Given that this shift is unrecoverable, the projection process cannot yield a geometrically coherent point cloud. Consequently, I question the validity of the proposed 3D scene field. If the proposed method can mitigates the shift issues, the paper should provide a mathematical analysis of how their method handles this.

3) Because of the shift issues, I suggest that the authors include visualizations of their reconstructed point clouds at different scales to demonstrate their geometric coherence.

4) Where the performance advantage comes from is a bit confusing. The baseline accuracy in Table 5 is already very high, and is almost achieved SOTA compared with methods in Table 1. The question arises as to whether the SOTA performance of TF-DEPTH on benchmarks will come from baseline? In order to make the results more convincing, I suggest to compare the baseline in Table 2,3 and 4.

### Questions
1. The paper lacks more convincing experiments to support the method. Although the accuracy is improved, it cannot support the method can solve more complicated real-world scenarios, such as reflections, shadow occlusions, and low-texture regions. Therefore, I suggest the paper design a test set, which includes a higher proportion of challenging cases  (reflections, low-texture regions, etc.). In presentation, the paper could illustrate more qualitative comparisons. 

2. As pointed in W2, i.e. affine-invariant distortions caused by the shift, the paper should consider how to model the shift in the unprojection process or provide a mathmatical analysis about how to mitigate the shift issues.

### Soundness
2

### Presentation
3

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
The paper proposes a self-supervised monocular depth estimation method that incorporates additional tri-plane features to establish a 3D representation, enhancing robustness in depth estimation which previous self-supervised methods struggle with. Key contributions of this work include:

- Introducing the first 3D scene field for monocular depth estimation using tri-plane features.
- Utilizing 3D-to-2D mapping techniques to project the 3D representation onto 2D image space.
- Conducting diverse experiments across various datasets to validate the approach.

### Strengths
S1. Clear Contribution with Tri-plane Features: The paper presents a contribution by incorporating tri-plane features to create 3D representation for self-supervised monocular depth estimation. 

S2. Diverse Experiments: The paper shows diverse experiments with multiple datasets and cross validations.

S3. Writing and Presentation: The paper is well-written and easy to understand.

### Weaknesses
W1. Clarity of Figure: The paper includes many parameter variables (e.g. Fs, Es, ˜Fs). However, Figure 2 does not contain notations that indicate where each parameter is represented, making it difficult to understand the overall method.

W2.  Limited Qualitative Results: The qualitative results are only provided for KITTI. While the quantitative results show improvements across various datasets, it is unclear whether these improvements are due to the 3D representation or merely a result of an increase in the number of network parameters.

### Questions
I would like to start by thanking the authors for their contribution to this field with their submission. Here are some questions:

Q1: This relates to W1. Adding notations to Figure 2 could make it easier to understand and interpret.

Q2: This relates to W2. If there are visualization results for other datasets, it would help in assessing whether the proposed design truly preserves completeness and consistency, as claimed in the paper.

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
The authors propose to use the 3d scene field for self-supervised monocular depth estimation. To this end, a tri-plane feature field and a 3D-to-2D mapping strategy are further developed. The proposed method is validated on multiple datasets including KITTI, Make3D, NYU, and ScanNet and outperforms previous methods.

### Strengths
The paper is well-written and structured;

The proposed method is novel to the best of my knowledge;

The experiments are thorough and the proposed method outperforms previous state-of-the-art methods.

### Weaknesses
No obvious weakness is observed.

### Questions
What level of improvement does the proposed method achieve compared to Lite-Mono when using the same encoder? For instance, both use Lite-Mono-8M as the encoder, along with the corresponding computational efficiency, such as the number of parameters and inference time.

### Soundness
3

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
This paper proposes a self-supervised depth estimation network, it designs a 3D intermediate point cloud representation to improve the performance of the network.  And the experiment part is sufficient, the proposed TSF-Depth achieves state-of-the-art performance.

However, I have some slight confusion about this paper in terms of the method design.

### Strengths
1. This paper is easy to follow.
2. This paper designs a 3D intermediate point cloud representation for self-supervised depth estimation to improve the performance of the network.
3. The experiment part is sufficient, the proposed TSF-Depth achieves state-of-the-art performance.

### Weaknesses
1. The title of this paper should include the keyword "self-supervised".
2. I am certain of the motivation of the paper, but I think there are some unreasonable aspects in the design of the method. I will elaborate on it in detail in the Questions part, and I hope the author can give me the answers.



### Questions
I have several questions, If the author can solve my confusion, I will increase the rate.
1. The paper proposes an implicit three-plane representation method, achieving this by decoupling the image coordinates and feature channels of the three dimensions. But, during this "Tri-plane Feature Field" building process, there are no constraints between different plane features. In other words, we can get the 3D representation capability simply by only using different image coordinate encodings?
2. As mentioned in the line 211 "the pixel depth in an image is closely related to its relative spatial position", line 803 "As for the outdoor scene such as driving scene, the road and sky appear in the lower and upper parts respectively, and other objects such as people, vehicles, houses, etc. are connected and located above the road. Besides, objects in the middle area of the image often have greater depth than objects in other areas." 
I don't think these priori are always right. In the KITTI dataset, images are taken along the forward direction of the car. However, in many cases, the image may be a side view. Also, to save memory, some scholars may use the top cropping to cut the sky part of image. In this case, is TSF-Depth still applicable for these cropped cases?
3. The paper supervises the generation process of intermediate depth maps through photometric loss.  From another perspective, TSF-Depth is similar to a Coarse-to-Fine network. So, I have a simple question. Can I achieve comparable or even better performance with TSF-Depth by adding a simple refine module on the existing network?
4. I want to know how the network handles sky areas, and I want to see the visualization results about the intermediate depth maps and point cloud projection process.
5. Please state the experimental setting of the ablation experiment more clearly (**Effects of 3D Scene Field on 3D Geometric Representation**). And, as mentioned in line 525, why replace the learnable encoder $\theta_E$ with a pre-trained encoder $\theta_E^{PT}$ without retraining?

### Soundness
3

### Presentation
3

### Contribution
2
