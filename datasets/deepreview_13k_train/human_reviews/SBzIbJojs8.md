# HiSplat: Hierarchical 3D Gaussian Splatting for Generalizable Sparse-View Reconstruction

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Reconstructing 3D scenes from multiple viewpoints is a fundamental task in stereo vision. Recently, advances in generalizable 3D Gaussian Splatting have enabled high-quality novel view synthesis for unseen scenes from sparse input views by feed-forward predicting per-pixel Gaussian parameters without extra optimization. However, existing methods typically generate single-scale 3D Gaussians, which lack representation of both large-scale structure and texture details, resulting in mislocation and artefacts. In this paper, we propose a novel framework, HiSplat, which introduces a hierarchical manner in generalizable 3D Gaussian Splatting to construct hierarchical 3D Gaussians via a coarse-to-fine strategy. Specifically, HiSplat generates large coarse-grained Gaussians to capture large-scale structures, followed by fine-grained Gaussians to enhance delicate texture details. To promote inter-scale interactions, we propose an Error Aware Module for Gaussian compensation and a Modulating Fusion Module for Gaussian repair. Our method achieves joint optimization of hierarchical representations, allowing for novel view synthesis using only two-view reference images. Comprehensive experiments on various datasets demonstrate that HiSplat significantly enhances reconstruction quality and cross-dataset generalization compared to prior single-scale methods. The corresponding ablation study and analysis of different-scale 3D Gaussians reveal the mechanism behind the effectiveness. Project website: \url{https://open3dvlab.io/HiSplat/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
HiSplat introduces a coarse-to-fine strategy to construct hierarchical 3D Gaussians for generalizable 3D Gaussian Splatting. Additionally, HiSplat proposes an Error-Aware Module and a Modulating Fusion Module to enhance inter-scale interactions. Comprehensive experiments demonstrate that HiSplat achieves better results than single-scale methods.

### Strengths
1. HiSplat first introduces the hierarchical 3D Gaussian representation in the task of generalizable 3D Gaussian Splatting.
2. The experiment effectively demonstrated the effectiveness of its hierarchical representation through Fig 4, which shows the primitives of Gaussians obtained from different stages.
3. This paper show the effective ablation study, comparing the impact of different modules on the performance of Generalizable Sparse-View Reconstruction.

### Weaknesses
1. Several spelling errors have been identified in the document, specifically on lines 73, 106, and 508.
2. The hierarchical representations appear to be memory-intensive and computationally inefficient. It is recommended that the paper discusses the implications for memory, FLOPs, and inference time.
3. The rationale for incorporating the DINO feature seems underwhelming, and the provided experiments do not convincingly demonstrate the necessity of including the DINO feature. The performance gain attributed to the DINO feature is marginal, and it is not clear if this gain justifies the added complexity and potential computational overhead.
4. I hope to see additional experiments conducted to explore the impact of increasing the number of perspectives on the quality of reconstruction. It appears that the majority of the experiments presented in the article are limited to just two perspectives, which may not fully capture the potential benefits of a multi-perspective approach.

### Questions
1. Discuss more about the importance of incorporating the DINO feature.
2. Discuss more about the complexity analysis of the method.

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
This paper claims that previous generalizable 3D Gaussian Splatting methods utilize uniform 3D Gaussians, making it challenging to simultaneously capture large-scale structures and intricate texture details. The authors propose a hierarchical approach to generalizable 3D Gaussian Splatting, constructing hierarchical 3D Gaussians through a coarse-to-fine strategy. Additionally, they design an Error Aware Module and a Modulating Fusion Module to manage interactions among different hierarchical Gaussians.

### Strengths
1. The idea of using different hierarchical Gaussians to simultaneously capture large-scale structures and delicate textures in scene generation sounds reasonable.
2. The ablative study seems complete. 
3. The motivation is clear since not all points in a single image are equally important.

### Weaknesses
1. The paper introduces many modules, which slows down the process compared to MVSplat, which is also revealed in Tab.4, after adding all the stages together. 
2. The improvement in metrics compared with baseline method does not seem very significant from the reviewer's perspective. But the generalization capability to unseen datasets like DTU seems interesting. The authors can show more cases that demonstrates generalization capability. 
3. Some of the visualized cases does not seem to possess a very significant improvement compared with MVSplat. For example, the last line of Fig.6; the left red bounding box in the first example in Fig. 1.
4. The number of Gaussian primitives is a concern. It is unclear how the hierarchical structure affects the total number of primitives compared to baseline methods. A comparison of primitive numbers would be beneficial.
5. The claim that HiSplat generates fewer artifacts in occluded areas needs more rigorous justification. The provided example in Fig. 6, while suggestive, could be coincidental and requires more evidence to support the claim.

### Questions
Apart from the weakness part, I also have the following questions.
1. Will the number of Gaussian primitives change significantly after applying this hierarchical structure? A comparison with baseline methods on the primitive numbers will be nice.
2. It seems that the first example in Fig.6. shows that HiSplat can generate less artifacts in the occluded area, as highlighted by the red bounding box. Does this just happen in coincidence or is it a prevalent phenomenon?

I still have the aforementioned concerns and I would be glad to raise my rating if they can be addressed.

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
This work presents a new 3DGS-based generalizable sparse-view scene reconstruction method, HiSplat, which effectively integrates multi-scale hierarchical MVS features with proposed EAM and MFM modules to enhance the quality of feed-forward 3DGS models, especially in fine-grained details. Experimental results demonstrate the superior reconstruction quality compared to prior SoTA methods.

### Strengths
1. The paper is well-motivated from the prior works on multi-scale hierarchical visual knowledge. It is well-written.
2. The way the authors integrate the multi-scale features is clever and interesting. I love the Error Aware part, HiSplat wisely incorporates the reconstruction error refinement, usually through gradient optimizations, into this feed-forward reconstruction model.  The error maps are used to guide the refinement on the higher levels. I believe this idea can also be beneficial for other related tasks.
3. The analysis in 4.4 is very informative and useful. The figures effectively demonstrate how multi-scale features can help improve the reconstruction quality.

### Weaknesses
1. The current model is pretty complex. It contains a lot of different neural models (MVSformer++, DINOv2, and a bundle of UNets and MLPs). I am not very clear which modules are trainable and which are not. The authors should clarify and summarize this in 3.6. Also, it would be even better, this is not required for rebuttal, if HiSplat could be a relatively simpler unified foundation model (e.g., like LRM).  
2. Although the writing is generally good, the citation format of this paper is a bit disturbing. Please properly use `\cite` and `\citep` provided in the ICLR template.
3. Minor typos:
    * MVSpalt → MVSplat
    * L298: fellow → follow

### Questions
1. Since it is unlikely we can always get accurate camera poses from sparse views in real life, can this work be extended to handle the pose-free sparse-view reconstruction for the captures from real life? If it is easy to implement, it would be great to see some examples.
2. The depth coefficient $\eta$ is a bit tricky. I assume it is a fixed value for each stage after the training, is this correct? If so, how do you choose the proper $\eta$ values?

### Soundness
3

### Presentation
4

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
This paper proposes HiSplat to estimate the 3D Gaussian Splatting structure of two given images with known camera poses in a feedforward process. It aims to use multi-scale information to improve the quality and for which two novel modules are proposed. Extensive experiments on various datasets can show its SOTA performance and good generalizability, and validate the effects of each proposed component.

### Strengths
- The proposed Error Aware Module and Modulating Fusion Module are interesting, which can effectively filter the errors from photometric loss in a simple way.

- Experiments are extensive. Both qualitative and quantitative results show that HiSplat achieves SOTA performance compared to the compared baselines. The results are convincing.

- The paper is easy to follow.

### Weaknesses
 - Some related methods are missed in the discussion, e.g., FreeSplat [1] and Splatt3R [2]. Especially, FreeSplat also uses a cost-volume-based structure to estimate the depth and then Gaussians with multi-scale strategy. A step further, the architecture of this work is also somehow similar to CasMVS [3] that uses a cascade structure to solve the MVS depth estimation task. The main differences lie in how the multi-scale features are used. Need more deeper discussions about these related works to show the technical differences and more valuable analysis.

- The setting of this paper seems to be fixed at using only two images. Would like to see some discussion about if it's possible to extend the method to more input views, just like what FreeSplat does. Even if it is a part of limitation, it would still be much valuable.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3
