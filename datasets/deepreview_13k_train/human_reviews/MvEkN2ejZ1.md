# MamBEV: Enabling State Space Models to Learn Birds-Eye-View Representations

- Decision: Accept
- Scores: 5, 6, 8, 8, 6

## Abstract
3D visual perception tasks, such as 3D detection from multi-camera images, are essential components of autonomous driving and assistance systems. However, designing computationally efficient methods remains a significant challenge. In this paper, we propose a Mamba-based framework called MamBEV, which learns unified Bird's Eye View (BEV) representations using linear spatio-temporal SSM-based attention. This approach supports multiple 3D perception tasks with significantly improved computational and memory efficiency. Furthermore, we introduce SSM based cross-attention, analogous to standard cross attention, where BEV query representations can interact with relevant image features. Extensive experiments demonstrate MamBEV's promising performance across diverse visual perception metrics, highlighting its advantages in input scaling efficiency compared to existing benchmark models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The main content of the paper is focused on enabling state space models (SSMs) to learn birds-eye-view (BEV) representations, specifically in the context of 3D representation learning tasks. 

The authors propose a novel method called MAMBEV, which incorporates SSMs and linear attention to address the challenges of capturing temporal and spatial relationships in multiview video and fusing distinct visual representations. 

They conduct experiments using the nuScenes dataset and achieve results comparable to the state of the art.

### Strengths
1. This paper presents a method for applying Mamba to BEV detection.

### Weaknesses
1. **Writing Issues:**
The paper has several writing issues:
* Many sentences are lengthy, which hinders comprehension. For example, lines 188, 191, and 201.
* Certain sections lack citations, such as on lines 206 and 207.
* Some areas seem to be missing punctuation, possibly in line 225.

2. **Experimental Results:**
The overall improvement in the experimental results is quite limited, and the value of applying SSM to BEV detection is not clear.

3. **Comparison with Related Work:**
Although the authors argue that it is unnecessary to compare with some long-sequence works, I believe it would be best to provide such comparisons, especially given that the authors conducted multi-frame ablation studies. Including comparisons with related work, such as VideoBEV, would strengthen the paper’s claims.

4. **Efficiency Metrics:**
The paper mentions reducing computational load and improving efficiency. The proposed method should provide relevant metrics related to training and testing, such as training time and model latency during testing. While the authors provide some data, these metrics do not demonstrate any significant advantage over more established methods like deformable attention. This lack of practical efficiency undermines the paper’s claims.

5. **Test Dataset Results:**
The authors have not provided results on the test dataset. Their explanation for this omission is unconvincing and raises questions about the generalizability of the proposed method.

6. **Summary:**
Overall, this paper discusses the application of Mamba in BEV detection. However, from the perspective of the detection task, the introduction of Mamba does not demonstrate any practical significance. Combined with the above points, I believe the paper requires more comprehensive experiments to substantiate its contributions.

### Questions
Please refer to section Weaknesses.

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
The paper presents MamBEV, a novel 3D object detection framework designed to improve BEV-based perception systems, particularly for autonomous driving. By introducing state-spatial separation and multi-axis multiview projection, MamBEV addresses the challenges in handling multi-camera BEV representation. The proposed method achieves promising results in complex driving scenarios, showcasing improvements in detection accuracy and computational efficiency.

### Strengths
1. Lower computational cost.
2. Good performance, comparable to VideoBEV.

### Weaknesses
1. The paper could have provided more ablation studies to dissect the contributions of individual components of MamBEV. Specifically, the impact of the state-space model (SSM) within the spatial cross-attention module and the effect of different query insertion strategies are not sufficiently explored. It is unclear how much each component contributes to the overall performance gain.
2. Limited discussion on potential limitations of the framework, such as scalability or adaptability to other domains beyond autonomous driving. The paper does not address the computational cost of the proposed method with respect to increasing input resolution or the number of cameras. Furthermore, the generalizability of the approach to different sensor modalities or tasks is not discussed.
3. limit novelty. The BEVFormer architecture introduces Mamba. The paper needs to better articulate the specific novel contributions beyond the integration of Mamba into a BEV framework.

### Questions
1. An important reason for using Mamba is to achieve lower computational cost; however, the paper only provides theoretical calculations without experimental validation, which is a crucial aspect.
2. In the bottom experiments of Table 1, why do BEVFormerV1-Small and BEVFormerV1-Base use different frames?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new approach to building bird's-eye-view (BEV) maps from multiple cameras. With an aim of mobile deployment, the paper investigates approaches that depart from the existing transformer-based push (from images to 3D) or pull (from 3d to images) methods. In particular, recent work on state space models (SSM) is an inspiration to replace transformers and their quadratic attention computational complexity. Of particular interest here is to leverage ideas from the Mamba-2 and Hydra SSMs and adapt them to the BEV problem. The new SSM-based BEV model is well described and well tested, including several ablation studies.

Two potential caveats noted below are that only one dataset is used (as seems to be the case with other SOTA approaches, so likely not the authors' fault), and the improvements over SOTA are small and sometimes mixed depending on which metric one looks at.

### Strengths
- significant problem domain where much improvement remains possible

- very well explained technical approach

- great to see asymptotic complexity analysis of the various stages of the approach

- convincing evaluation on the nuScenes dataset

- experiments on increasing temporal information, SSM vs deformable attention, feature normalization, scaling, and feature traversal order are interesting and convincing.

### Weaknesses
 - table 1, the proposed model does not outperform SOTA in all metrics. This table needs to be described better. If NDS is the main metric, then what about Focal-DETR? Should explain more clearly which table rows are compared in the main text lines 395-396

- should include a figure with reconstruction samples, for qualitative evaluation by the reader.

- lines 221-222: nonsense sentence

### Questions
- only tested on nuScenes (like some of the other SOTA models, including DETR3D and BEVformerV2). Is there another suitable dataset that this could be tested on to better demonstrate generality?

### Soundness
4

### Presentation
4

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
The paper introduces the Mamba mechanism into 3D visual perception task to learn bird's-eye view (BEV) representations in order to address computational and memory efficiency problems, and designs a Spatial Cross Attention module for the task. The effectiveness of the design is demonstrated through extensive experiments and ablation studies, which would bring benefits to application scenarios such as autonomous driving and driver assistance systems.

### Strengths
1. MamBEV proposes a design based on SSM, which exceeds the performance of existing Transformer-based structures in several metrics.
2. MamBEV provides sufficient experimental results to illustrate the effectiveness of the design.

### Weaknesses
1. Lack of visualization of results. I am quite sorry to say that I am not familiar with the nuScenes dataset, so could the authors provide some visual examples to show the advantages of MamBEV?
2. Lack of more detailed description of the effectiveness of the Spatial Cross Attention module. Since the authors mention in the Introduction that "we further demonstrate that our method can better capture longer dependencies in multiview video", whether this word "better" means the module proposed in the paper comparing to other SSM Attention designs, or Mamba-2 comparing to Mamba-1, or Mamba comparing to Transformer, could it be supported and presented through other ways in addition to the accuracy results on the specific dataset?

### Questions
The main issues have been raised in Weaknesses section.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents MamBEV, a novel framework designed for 3D visual perception tasks like 3D detection from multi-camera images, which are crucial for autonomous driving and assistance systems. The framework leverages a Mamba-based approach to learn unified Bird’s Eye View (BEV) representations using linear spatio-temporal SSM-based attention, which improves computational and memory efficiency across multiple 3D perception tasks. The key is SSM-based cross-attention, which functions similarly to standard cross-attention, enabling BEV query representations to interact effectively with relevant image features. Experiments are conducted to demonstrate the effectiveness of the method. 

Pos:
- Enabling Mamba to BEV representation seems to be interesting.

Cons:
- The authors claim that proposed method supports multiple perceptual tasks but has no proof.
- The article keeps emphasizing computational efficiency, but without proofs.
- The core figures are crude and difficult to understand
- Insufficient experimentation and comparison methods

### Strengths
- Enabling Mamba to BEV representation seems to be interesting.

### Weaknesses
Cons:
- The authors claim that proposed method supports multiple perceptual tasks but has no proof.
- The article keeps emphasizing computational efficiency, but without proofs. The claims of efficiency gains are not substantiated with concrete benchmarks or comparisons against established methods. The paper lacks a detailed analysis of the computational complexity of the proposed Mamba-based approach, especially in relation to the standard cross-attention mechanisms it aims to replace. There is no clear breakdown of FLOPs or memory usage, making it difficult to assess the true efficiency of the method.
- The core figures are crude and difficult to understand
- Insufficient experimentation and comparison methods. The experimental section lacks a thorough evaluation of the proposed method. There is a limited number of experiments and comparisons against state-of-the-art techniques. The ablation studies are not comprehensive enough to fully understand the contribution of each component of the proposed framework. The absence of comparisons with other Mamba-based approaches for 3D perception makes it hard to assess the novelty and effectiveness of the proposed method.

### Questions
Please refer to the above.

### Soundness
2

### Presentation
2

### Contribution
2
