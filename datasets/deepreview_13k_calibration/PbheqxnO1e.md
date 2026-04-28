# Lightweight Predictive 3D Gaussian Splats

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
Recent approaches representing 3D objects and scenes using Gaussian splats show increased rendering speed across a variety of platforms and devices. 
While rendering such representations is indeed extremely efficient, storing and transmitting them is often prohibitively expensive. 
To represent large-scale scenes, one often needs to store millions of 3D Gaussians, occupying gigabytes of disk space. 
This poses a very practical limitation, prohibiting widespread adoption.
Several solutions have been proposed to strike a balance between disk size and rendering quality, noticeably reducing the visual quality.
In this work, we propose a new representation that dramatically reduces the hard drive footprint while featuring similar or improved quality when compared to the standard 3D Gaussian splats.} 
Our key observation is that nearby points in the scene can share similar representations. 
Hence, only a small ratio of 3D points needs to be stored. 
We introduce an approach to identify such points—called \emph{parent} points. The discarded points—\emph{children} points—along with attributes can be efficiently predicted by tiny MLPs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a lightweight 3D Gaussian framework that models inherent spatial relationships within a hierarchical tree structure. To optimize the tree structure, the authors suggest adaptive tree manipulation (ATM), an adaptive growth and pruning strategy for parent and children nodes. Consequently, it demonstrates efficient storage size and superior rendering quality compared to compact 3D Gaussian representations, e.g., LightGS, CompactGS, and EAGLES.

### Strengths
- The proposed tree structure enables parent nodes to represent children nodes using an on-the-fly decoding pipeline. This results in the small disk usage of this representation with high rendering quality.

- The optimization schemes, ATM for growth and warm-up for initial training, lead to achieving stable and effective optimization of the proposed representation.

### Weaknesses
 - The main weakness of this paper is the limited technical novelty. The proposed tree structure mainly comes from the anchor-based representation, Scaffold-GS [1]. Also, the adaptive manipulation of children nodes is proposed in HAC [2], with more efficient learnable masks. Moreover, the usage of a hash grid for efficient 3DGS representation is also proposed in HAC and CompactGS [3]. 

- Also, it demonstrates a slower rendering speed compared to 3DGS, as we can see in L458. It indicates that this approach requires more 3D Gaussians splats (both parent splats and children splats) for the rendering phase and only consumes less disk usage in the storage. Therefore, the claim for **"lightweight"** representation seems overclaimed.

- Furthermore, there is limited comparison to existing compact representations. Recently, many papers have been addressing the inefficiency issue of 3DGS. However, there are too less methods in the comparison. Please refer to the question section for the related approaches.

### Questions
- The results of CompactGS in Table 1 seem to be not applying post-processing, such as quantization of the hash grid. As this paper reports the storage size for the quantized hash grid as described in L443, it is fair to report the post-processed results of CompactGS.

- Moreover, it seems that the tree structure and hash grid design require more training time compared to 3DGS. Please provide the training time to optimize this representation.

- Also, the detailed number of 3D Gaussians for 3DGS should be added to prove that this method requires less number of Gaussians as described in the quantitative results section.

- Furthermore, it is recommended to add more comparisons for the compact 3DGS representations as below. According to the reviewer guideline, the authors do not have to compare papers which are recently published in ECCV'24. But, as the idea this paper is significantly related to HAC [1], it could be helpful for comparing with HAC in terms of both performance and methodology.

  - Compressed3D [2] (CVPR 2024)
  - Reduced3DGS [3] (I3D 2024)
  - HAC [1] (ECCV 2024)
  - SOG [4] (ECCV 2024)
  - Compact3D [5] (ECCV 2024)

---
**Reference**
1. Chen et al., HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression, ECCV 2024
2. Niedermayr et al., Compressed 3D Gaussian Splatting for Accelerated Novel View Synthesis, CVPR 2024
3. Papantonakis et al., Reducing the Memory Footprint of 3D Gaussian Splatting, I3D 2024
4. Morgenstern et al., Compact 3D Scene Representation via Self-Organizing Gaussian Grids, ECCV 2024
5. Navaneet et al., Compact3D: Smaller and Faster Gaussian Splatting with Vector Quantization, ECCV 2024

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new representation for 3D Gaussian splats that drastically reduces disk space requirements while providing similar or improved quality compared to previous methods. The method detects inherent common features between splats in close proximity using an attention mechanism (ATM) and exploits these using a hierarchical tree structure in which only the parent splats need to be stored. As a very extensive evaluation on current benchmark data sets shows, the new representation achieves an average reduction in disk footprint of 20x compared to the original 3DGS, with improved PSNR and comparable SSIM and LPIPS, and a 2-5x reduction in storage compared to new works on more efficient representation. In addition, the method is presented to real rendering applications on mobile devices and AR glasses.
In contrast to the competing method CompactGS, it uses a combination of neural fields and self-attention layers to predict not only view-dependent colours but also geometric properties. Secondly, in contrast to competing approaches that store the position of each splat in the point cloud explicitly like ScaffoldGS, the method stores only a small subset of splats, referred to as parents, while the remaining points are predicted on-the-fly during rendering, significantly reducing memory requirements. In contrast to recently presented anchor-based methods, the hierarchical tree representation in combination with the proposed Adaptive Tree Manipulation takes into account the importance of both parent and child splats, which enables a subtree expansion strategy.

### Strengths
The idea of deriving the positions of child splats and associated attributes – position, color, scale, etc. – from the parent using a small neural network and only storing parent splats together with the weights of the neural network is new and should definitely be published.
The paper gives a very nice introduction to the problem and a very good overview of the existing approaches.
The method itself is explained in detail and is easy to follow. Comprehensive ablation studies show the influence of the different components of the algorithm on its performance. The extensive evaluation impressively demonstrates the strength of the method compared to the state of the art. It is interesting to note that, in contrast to the original 3DGS, the quality in some of the benchmark comparisons is better despite the considerable compression of the representation.

### Weaknesses
Unfortunately, there is no code to go with the paper, so that the procedure can be tested independently.

### Questions
In the  text to Figure 2 "patent" should be replaced by "parent".

Maybe you comment already in section 4.1. that in your code you have chosen $K$ to be 2?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a storage-effective 3D gaussian splatting representation. It uses hierarchical tree structure use similarity between nearby 3D gaussians.  The tree structures are manipulated adaptively in the optimization processes. The method not only outperform SOTA methods, but it is also shown to run effectively in mobile devices.

### Strengths
Storage-effective representation for 3D gaussians.  

The proposed method shown to outperform existing SOTA methods. 

The proposed method shown to run on mobile devices. 

Ablation study to show necessities of the proposed components.

### Weaknesses
There is only one figure (i.e., fig.2) for explaining the proposed method. Thus, it may not be easy to follow the process of the method.

### Questions
The format of the sub-section titles is not consistent. Some of them are ended with ":", some with "." and some with " ".

### Soundness
4

### Presentation
3

### Contribution
4
