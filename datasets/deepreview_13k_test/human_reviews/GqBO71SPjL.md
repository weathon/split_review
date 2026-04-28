# LUDVIG: Learning-free Uplifting of 2D Visual Features to Gaussian Splatting Scenes

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
We address the problem of extending the capabilities of vision foundation models such as DINO, SAM, and CLIP, to 3D tasks. Specifically, we introduce a novel method to uplift 2D image features into 3D Gaussian Splatting scenes. 
Unlike traditional approaches that rely on minimizing a reconstruction loss, our method employs a simpler and more efficient feature aggregation technique, augmented by a graph diffusion mechanism. 
Graph diffusion enriches features from a given model, such as CLIP, by leveraging 3D geometry and pairwise similarities induced by another strong model such as DINOv2.
Our approach achieves performance comparable to the state of the art on multiple downstream tasks while delivering significant speed-ups.
Notably, we obtain competitive segmentation results using generic DINOv2 features, despite DINOv2 not being trained on millions of annotated segmentation masks like SAM.  When applied to CLIP features, our method demonstrates strong performance in open-vocabulary object detection tasks, highlighting the versatility of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper is primarily concerned with generating 3D feature representations of a scene given multiple images of a stationary scene captured from different viewpoints. The main idea proposed here is that of extracting visual features from the multiple images (using a pretrained general purpose foundational model) and then fusing them with the scene representation computed using the 3D Gaussian splatting optimizer, i.e. fully calibrated camera poses and a set of 3D Gaussians with all the relevant parameters (position, covariance, size, opacity, spherical harmonics coefficients).

Specifically, feature vectors are computed and associated with the 3D centroids for each Gaussian in the 3DGS scene representation. The authors propose to compute these features by an aggregation scheme that is implemented as weighted averaging of the feature vectors extracted in multiple images. First 2D features are computed using existing visual feature extraction models. Features extracted for patches corresponding to the same Gaussian in multiple views are combined using a weighted averaging scheme presented in the paper. The 3D features associated with the 3DGS representation are then used in downstream tasks such as 3D segmentation (or multi-view segmentation) for which certain existing graph diffusion techniques are leveraged. 

The experimental results focus on segmentation performance on the Spin-NeRF and NVOS datasets where the method achieves comparable performance to existing techniques.

### Strengths
The proposed approach to lift 2D features to 3D is efficient and avoids expensive iterative optimization schemes. The approach appears to be simple to implement and could be effective for downstream tasks such as 3D segmentation of stationary scenes where multiple views of the scene are available.

### Weaknesses
My main concerns about this work revolves around:

(1) Low novelty:
- It was unclear to me to what extent the main idea of lifting features from images to 3DGS point couds was novel compared to existing approaches in the literature that have explored scene editing given a 3DGS reconstruction of a scene. The weighted averaging and aggregation scheme described here appears to be very similar to what was proposed in prior work such as Chen et al. 2024.

- The paper mostly focuses on the 3D segmentation application and shows the their proposed ideas work well for that application. They experiment with different features (DINOv2 vs SAM, etc.). However, the authors are not the first to segment or edit 3D Gaussian scenes. This was also explored in the prior work of Chen et al 2024 although they focused on binary segmentation, unlike in this work.

(2) More thorough comparison with existing approaches needed:
The main claimed contribution in the work is towards the technical approach for computing 3D features from 2D features using an efficient approach (referred to as uplifting in the paper). There are other approaches in the literature that have been explored to accomplish the same step. Those optimization based methods are cited and discussed [Kerr et al 2023, Zuo et al 2024] but there is no quantitative comparison between the proposed method and those related works. This makes it difficult to assess the contribution and impact of the novel ideas that are presented here. 

(3) Overall presentation has room for improvement:
The presentation and technical exposition could be improved for better clarity and presentation. I think the core objectives and the problem being tackled in the paper could have been explained better in the abstract and introduction. In the current version of the manuscript, it is difficult to understand what the authors precisely mean by “uplifting visual features to 3D scenes represented by Gaussian Splatting”. The abstract claims that “a simple yet effective aggregation technique yields excellent results.” – but the author have not explained what is being aggregated and for what purpose and what the success criteria is. The authors then talk about competitive segmentation results without clearly explaining the connection between the segmentation task and the 3D reconstruction or 3D scene representation task. Reading Section 1 (Introduction) doesn't give a concrete idea of the main objective, the key motivations and where the novelty lies.

### Questions
Is the graph diffusion framework based on existing work? If so, the appropriate work in the literature should be cited for that. Otherwise, it would be best to clarify that the formulation is novel and developed by the authors themselves for the 3d segmentation task.

"Let I1, . . . , Im be a set of 2D frames from a 3D scene and d1, . . . , dm the corresponding viewing directions." -- the authors should clarify what they mean by viewing directions, and whether they are referring to camera poses, here? The phrase viewing direction is used throughout the paper and makes it difficult to understand the underlying mathematical operations that are being performed. 

The mathematical notation is difficult to follow. The expression \hat{F} = (\hat{F}_d, [) (lines 188) are not well explained. Similarly, the steps to construction the W and D matrices also need to clearly described.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission proposes a simple yet effective scheme of uplifting visual features from 3D scenes represented by Gaussian splitting. In contrast to the previous approaches, the proposed method enables direct 3D segmentation without iterative optimization, while achieves comparable to the SotAs.

### Strengths
+ The proposed scheme of connecting per-pixel 2D features and Gaussians are simple and intuitive. 

+ The segmentation can be directly done without iterative optimization on a trained Gaussian. 

+ The treatment on incorporating with DINOv2 feature into segmentation is nice, as it induces comparable results with the variant using the more tailored-for SAM.

### Weaknesses
- There is neither limitation/failure nor future work discussion in the submission, what is the boarder impact of the work for the community? 

- The submission lacks report on running time.

### Questions
The graph diffusion (Eq.(7)) is similar to power method for computing the dominant eigenvector of a matrix. While it is not guaranteed to converge to the dominant eigenvector, I guess there is a high probability. Is it possible to draw some theoretical connection to, say, spectral clustering methods, and therefore give some insight of the converging point of g_t? 

In figure 2, the rolling stair are separated from the ceiling in the multi-view case while merged to the latter in the single-view case, could the authors provide some explanation on such behavior?

In Sec. 4.2, the DINOv2 features seem to be of coarse scale (predicted in patches), would the recent works on feature super-resolution (e.g., Feature-up in ICLR 2024 by Fu et al.) help?

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
3

### Summary
The paper introduces LUDVIG, a learning-free method designed to uplift 2D visual features or semantic masks to 3D Gaussian Splatting scenes. LUDVIG avoids traditional, iterative optimization processes by using a simple aggregation technique, achieving comparable segmentation quality to state-of-the-art methods. The approach is applied effectively to features from both SAM and DINOv2, demonstrating high segmentation performance and computational efficiency across complex 3D scenarios.

### Strengths
1. The learning-free feature uplifting method is both simple and effective, achieving strong results without training.
2. Experiments with SAM and DINOv2 demonstrate the method’s efficiency, yielding performance comparable to training-based approaches.
3. High Computational Efficiency: LUDVIG bypasses the costly and time-consuming optimization steps typical in 3D reconstruction methods, making it highly efficient.
4. Versatile Input Adaptability: The proposed method adapts seamlessly to various input types, such as features from SAM and DINOv2, showcasing robust performance across diverse feature sources.

### Weaknesses
1. While the method is straightforward, it relies on hand-crafted processes, such as the segmentation score calculation and the graph diffusion process. These manual strategies may raise concerns about robustness, particularly in complex, real-world scenarios.
2. Certain sections, like Sec. 4.2, are challenging to follow. For example, the construction of 2D feature maps from DINOv2 is not clearly outlined. Including diagrams or visual aids could greatly enhance understanding and clarify complex steps.
3. Lack of qualitative comparison results with other baselines. 
4. The proposed method is primarily limited to foreground segmentation, whereas other feature lifting approaches support additional tasks, such as instance segmentation, 3D segmentation, and downstream applications like scene manipulation.

### Questions
1. As in weakness 2, can you explain the process of feature map construction?
2. How is the time efficiency of the proposed method compared to other training-based methods? 
3. As in weakness 4, Can the proposed method performed on other tasks and how well is it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a method that lifts 2D features into the 3D representation space of 3DGS. With the lifted features, the method can perform segmentation of objects, and other applications. The paper tested features of SAM and DINO. For DINO, a graph diffusion step is performed to enhance the results.

### Strengths
1. Previous approaches adopt optimizations, while this method is training-free and maybe fast.
2. The presentation is clear.

### Weaknesses
1. The method needs additional post-processing steps such as graph diffusion.
2. The paper is not fully finished. There is no conclusion section.

### Questions
1. The lifting algorithm is very simple, which is a weighted average of features collected from multiple views. This reviewer had an experience on object segmentation based on NeRF. I feel that the aggregated features may suffer from noises. For example, there may be errors in camera parameters, which can reduce the effectiveness of the aggregation. I suggest the authors to add more analysis on this problem (In fact, I do not know how to evaluate this, and expect the authors to provide more insights). 

2. The method is probably highly affected by the effectiveness of the feature extraction backbone. I am wondering whether the 2D segmentation masks obtained by the backbones applied to the images are similar to those of the lifted 3DGS projected to the 2D. Please provide this additional comparison.

3. I do not see connection between the proposed method and optimization-based approach in lines beginning from 205. Maybe this paragraph discusses the difference between the two kinds of approaches. I think a title of “Difference with optimization-based inverse rendering” may be more appropriate. 

4. The method needs a graph diffusion to further enhance its results. Why do you need this step? Please provide the results w/ and w/o this step. 

5. Please check the paper and make sure all sections are completed.

Overall, I think the accuracy of this method may be limited due to the noises in the features themselves caused by, e.g., misalignment between features of different views. The method is fast, but there is no argument supporting the necessity of this method at the cost of accuracy.

### Soundness
2

### Presentation
3

### Contribution
1
