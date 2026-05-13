# 3D-GP-LMVIC: Learning-based Multi-View Image Compression with 3D Gaussian Geometric Priors

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Multi-view image compression is vital for 3D-related applications. To effectively model correlations between views, existing methods typically predict disparity between two views on a 2D plane, which works well for small disparities, such as in stereo images, but struggles with larger disparities caused by significant view changes. To address this, we propose a novel approach: learning-based multi-view image coding with 3D Gaussian geometric priors (3D-GP-LMVIC). Our method leverages 3D Gaussian Splatting to derive geometric priors of the 3D scene, enabling more accurate disparity estimation across views within the compression model. Additionally, we introduce a depth map compression model to reduce redundancy in geometric information between views. A multi-view sequence ordering method is also proposed to enhance correlations between adjacent views. Experimental results demonstrate that 3D-GP-LMVIC surpasses both traditional and learning-based methods in performance, while maintaining fast encoding and decoding speed.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel approach to multi-view image compression using 3D Gaussian geometric priors. The authors propose a learning-based framework that uses 3D Gaussian splatting to derive geometric priors for more accurate inter-view disparity estimation. In addition, the paper introduces a depth map compression model to reduce redundancy and a multi-view sequence ordering method to improve correlations between adjacent views. The authors claim that their method outperforms both traditional and learning-based methods in terms of compression efficiency, while maintaining fast encoding and decoding speeds. Not explicitly address the scalabilityto high resolution images, and lacks detailed analysis of the computational complexity.

### Strengths
Strength: 1.The paper introduces a groundbreaking approach by integrating 3D Gaussian geometric priors into the multi-view image compression framework. This innovative method allows for more accurate disparity estimation, which is crucial for complex multi-view scenarios. 2.The proposed depth map compression model is particularly noteworthy as it takes into account the redundancy of geometric information across views. This model not only contributes to improved compression efficiency, but also ensures that depth information, which is essential for 3D applications, is preserved during decoding. 3.The claim of fast encoding and decoding speeds is a strength, especially for applications requiring real-time processing. The paper's approach to balancing model complexity and speed is commendable and well aligned with practical deployment needs. 4.The authors' decision to make the code publicly available is commendable.

### Weaknesses
Weakness: 1.The paper does not explicitly address the scalability of the proposed method to high resolution images, which is an important aspect for many applications. Specifically, the paper lacks experiments demonstrating the performance of the method on images with resolutions significantly higher than those used in the current evaluation. This is crucial because the computational cost and memory requirements of 3D Gaussian splatting and the associated learning models could increase dramatically with higher resolution inputs, potentially limiting the practical applicability of the method. 2.While the paper highlights the fast encoding and decoding speeds, it lacks a detailed analysis of the computational complexity, including parameters such as FLOPs and memory usage. A more thorough analysis should include a breakdown of the computational cost of each component of the proposed framework, such as the 3D Gaussian splatting, the depth map compression model, and the multi-view sequence ordering method. Furthermore, the paper should provide a comparison of the computational complexity of the proposed method with existing state-of-the-art multi-view image compression methods, including a discussion of the trade-offs between compression performance and computational cost.

### Questions
Weakness: 1.The paper does not explicitly address the scalability of the proposed method to high resolution images, which is an important aspect for many applications. 2.While the paper highlights the fast encoding and decoding speeds, it lacks a detailed analysis of the computational complexity, including parameters such as FLOPs and memory usage. Such an analysis is crucial for assessing the practicality of the method, especially on resource-constrained devices.

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
Paper Summary:

This paper proposes a pipeline for multi-view image compression. The core approach involves first estimating depth maps for each image and then compressing the images through view alignment. Gaussian Splatting reconstruction is used to accurately estimate the depth maps. Additionally, a neural network is employed to compress and decompress the image and depth sequences, leveraging image alignments to enhance performance.

Claimed Key Contributions:

- Precise disparity estimation using 3D Gaussian reconstruction
- A depth map compression model
- State-of-the-art performance in multi-view image compression

Overall, I believe this paper is well-structured as an engineering paper or technical report. However, it primarily seems to combine existing methods, which may limit its ability to provide a fresh perspective for readers. I have reservations about the section related to 3DGS. If the authors can clearly highlight their contributions in other techniques they have employed, such as the image compression network, I would be more inclined to reconsider my assessment. That said, I am uncertain about the novelty of the image compression network, as I am not an expert in that area.

### Strengths
- The task is clearly defined: compressing multi-view images with no much quality loss.
- The paper uses the popular Gaussian Splatting method for depth map estimation.

### Weaknesses
 - Firstly, I am not an expert specifically in multi-view image compression, as my research primarily focuses on other areas within multi-view 3D vision. From my perspective, part of this paper lacks novelty in its methodology in its approach to depth map estimation from 3D Gaussian splats. As mentioned in the abstract, the authors suggest that current methods are limited by their difficulties in handling "more complex disparities from wide-baseline setups." Thus, the key motivation here seems to be addressing the challenges in depth map estimation. However, in terms of novelty, I feel that the authors have not introduced new contributions to address these issues of complex disparities in wide-baseline setups; they rely on depth map estimation from 3D Gaussian reconstruction, which is an existing technique.

- From my experience, Gaussian Splatting may not be an ideal choice for depth estimation. Its depth map quality often falls short of state-of-the-art results, particularly in areas with low texture or reflective surfaces. Besides the optical flow methods referenced in the ablation studies, I am curious whether the authors considered alternative depth estimation approaches. I would suggest testing:

  - (1) COLMAP as a representative traditional multi-view depth estimation method. COLMAP is specifically designed for accurate depth estimation, unlike 3DGS, which primarily focuses on novel view synthesis and only produces depth estimation as a secondary outcome.

  - (2) MVSFormer++ as a representative learning-based method. This model is explicitly towards depth estimation, and with a pretrained model, it should perform better in textureless regions with inherent ambiguity.


- The paper lacks qualitative results, particularly visual comparisons. While some results are available in the appendix, there are no visual comparisons in the main text.

- I don’t recommend including such a detailed network architecture figure (Figure 3) in the main paper. Instead, this figure should provide an overview of the compression pipeline. For example, it will be great if the authors remove the layer-specific details (like `Conv` or `Downsample`), as excessive detail may distract readers from grasping the core idea.

### Questions
- How long does it take to compress a set of images as well as decompress a set of images? It seems Table 2’s results excluded 3DGS training time.

- I am curious about the authors' choice to use the mipNeRF360 and TnT datasets in this paper, as these are standard for tasks such as novel view synthesis and 3D reconstruction. However, it seems these datasets have not been evaluated within the context of image compression tasks. Could the authors clarify their rationale for this decision? Additionally, in baseline papers like HESIC (Deng et al., 2021), the authors utilize the KITTI and Stereo 2K datasets for evaluation. Is there a specific reason the authors chose not to use these datasets for a more direct comparison?

### Soundness
2

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
This paper introduces 3D-GP-LMVIC, a novel method for multi-view image compression that uses 3D Gaussian Splatting to improve disparity estimation in complex, wide-baseline scenarios. It includes a depth map compression model to minimize geometric redundancy and a multi-view sequence ordering method to enhance view correlations. Experiments show that 3D-GP-LMVIC outperforms existing methods in compression efficiency while keeping fast processing speeds.

### Strengths
(1) In this paper, the authors carry out a lot of formula derivation to explain 3D Gaussian geometric priors.

(2) 3D-GP-LMVIC achieves SOTA performance on Tanks&Temples, Mip-NeRF 360, Deep Blending dataset compared with other deep learning-based multi-view image compression methods.

### Weaknesses
 (1) Although the author used a large number of formulas to derive 3DGS prior in this paper, I think the interpretation of 3DGS prior is not clear enough. Could you elaborate on how the 3D Gaussian Splatting technique is used to derive geometric priors? How do these priors differ from traditional disparity information, and what unique advantages do they offer for multi-view image compression?

(2) In the selection of datasets in the experimental part, the authors select several datasets commonly used by 3DGS methods. I'm curious why the author didn't add the commonly-used multi-view image compression dataset Cityspace? In addition, since the author emphasizes in the abstract that the application scenarios of the existing methods are mainly stereo images, I strongly suggest that the author include the performance of 3D-GP-LMVIC on stereo image datasets (such as KITTI and Instereo2K).

(3) Are there depth map instances in the 3 datasets used by the authors? If so, why did the authors not show RD performance for depth map compression? If not, I observe that 3D-GP-LMVIC seems to be a dual framework. Did the author include the depth map when calculating Bpp (bits per pixel)? Is this cost-effective relative to the performance improvement, and is there any corresponding experimental proof?

(4) I'm curious why the authors do not show the BiSIC codec time in Table 2. In addition, I suggest that the authors further supplement the number of model parameters for each method to evaluate the spatial complexity of each model.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

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
This work presents a new method for multi-view image compression (MVIC) based on deep neural networks. Considering that accurate disparity estimation is a key factor in MVIC, authors proposed to leverage 3D Gaussian splatting for better disparity estimation. Then, the images and estimated depth maps are compressed in an encoder-decoder framework, by making use of mask maps. The multi-view sequence ordering is also proposed using a simple greedy method to maximize the inter-view correlation. Experiments demonstrate the effectiveness of the proposed codec over existing methods.

### Strengths
1) Experiments demonstrates the effectiveness of the proposed method over existing MVIC approaches.

### Weaknesses
1) Contributions should be clarified. It seems that the depth estimation method itself of Section 3.1 is not new, following existing approaches. To be specific, the original 3D Gaussian splitting method [a] can also extract depth maps from the rendering process, and recently some approaches attempt to enhance the depth quality from the 3D Gaussian splitting framework [b]. If there is nothing new in terms of the depth estimation process, this part can be excluded from Section 3 (Proposed Method).

[a] 3D Gaussian Splatting for Real-Time Radiance Field Rendering, ACM TOG 2023

[b] Self-Evolving Depth-Supervised 3D Gaussian Splatting from Rendered Stereo Pairs, BMVC 2024

2) Section 3.2 about image and depth compression needs significant revisions.
- The compression methodologies of (5) and (6) consist of encoder, quantization, and decoder. It is difficult to grab what the differences from existing learning based MVIC approaches are. More concrete explanations against existing MVIC methods (cited in the paper) should be included.

- What is the purpose of using the mask map in the encoding process?

- Figure 3 is complicate, and it would be better to visualize it with high-level conceptual figure, followed by detailed architectures of separate modules.

- $y_n$ is quantized in (4) and (5), but $z_n$ is quantized in Figure 3.

- Why is 'MaskConv' used in Figure 3?

3) Minor comments
(3) represents the equation of converting a depth into a disparity, and is commonly used in many literatures. So, it would be better to move into appendix instead of main paper.

Overall, this work achieves satisfactory results compared to recent learning-based MVIC, but the technical presentation needs substantial revisions.

### Questions
Refer to the comments in the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
