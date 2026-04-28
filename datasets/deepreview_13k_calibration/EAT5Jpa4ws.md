# SHARE: Bridging Shape and Ray Estimation for Pose-Free Generalizable Gaussian Splatting

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
While generalizable 3D Gaussian Splatting enables efficient, high-quality rendering of unseen scenes, it heavily depends on precise camera poses for accurate geometry. In real-world scenarios, obtaining accurate poses is challenging, leading to noisy pose estimates and geometric misalignments. To address this, we introduce SHARE, a novel pose-free generalizable Gaussian Splatting framework that overcomes these ambiguities. Our ray-guided multi-view fusion network consolidates multi-view features into a unified pose-aware canonical volume, bridging 3D reconstruction and ray-based pose estimation. In addition, we propose an anchor-aligned Gaussian prediction strategy for fine-grained geometry estimation within a canonical view.
Extensive experiments on diverse real-world datasets show that SHARE achieves state-of-the-art performance in pose-free generalizable Gaussian splatting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SHARE, a framework for pose-free generalizable 3D Gaussian Splatting that addresses the challenge of multi-view 3D reconstruction from unposed images. SHARE's key innovation is a ray-guided multi-view fusion network that consolidates multi-view features into a unified pose-aware canonical volume, bridging 3D reconstruction and ray-based pose estimation. It also proposes an anchor-aligned Gaussian prediction strategy for fine-grained geometry estimation within a canonical view. The paper reports that SHARE achieves state-of-the-art performance in pose-free generalizable Gaussian splatting through experiments on diverse real-world datasets, including DTU and RealEstate10K.

### Strengths
- The paper presents a novel framework that addresses the challenge of pose-free generalizable 3D Gaussian Splatting, which is an under-explored field in 3D scene reconstruction and novel view synthesis.
- The approach of using a ray-guided multi-view fusion network to consolidate features into a canonical volume for Gaussian prediction is creative.
- The language is clear and technical terms are well-defined, making the paper accessible to readers familiar with the field.

### Weaknesses
 - Insufficient baselines and experiments.  
I think the paper lacks the comparison with the state-of-the-art pose-free multi-view reconstruction framework, i.e., DUST3R [1] (or its subsequent work MAST3R [2]), in terms of pose estimation accuracy and reconstruction quality. Also, several recent works built upon DUSt3R also explored pose-free generalizable Gaussian Splatting, e.g., Splatt3R [3] and InstantSplat [4], I believe that including experimental results and discussions on these methods (at least Splatt3R since it is feed-forward) would make the paper's claim stronger.

- Potentially unfair comparison with pixelSplat and MVSplat.  
The authors report the view synthesis results of pixelSplat and MVSplat using "poses predicted by our method" in Table 1 and Table 2. However, we are not clear about the quality of the pose prediction results of SHARE due to the lack of evaluations on pose estimation accuracy. What if we feed (potentially) more robust predicted poses to them, such as the outputs of MAST3R?   
Besides, I notice that the results on DTU in Figure 5 are from 3 input views, while the original pixelSplat and MVSplat models were trained on paired images. How did the authors adapt them to 3 input views?

- Small camera baselines and scalability.  
The proposed framework utilizes plane-sweep volumes and predicts all Gaussians from a canonical feature volume, raising concerns on its reconstruction capability on more challenging input views, such as large camera baselines and occusions. The qualitative results shown in the paper demonstrate small camera movements compared to the input view, I hope the authors can include some discussions on the upper limit and scalability to more diverse datasets of the proposed method.

### Questions
My main questions have been listed in the weakness part, I will adjust my final rating accoding to the author's response. I suggest the authors to visualize all the input images in Figure 5 and Figure 2 of the supplementary, intead of labeling "Input view (1/3)" on the top. It is hard for readers to measure the view synthesis quality from only one input view.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on generalizable Gaussian splatting from sparse unposed images. To this end, it employs the Pl$\ddot{u}$cker ray representation for relative pose estimation. Based on the ray representation, it builds cost volumes from extracted image features. Moreover, it embeds the ray representation into the cost volumes using patch-wise cross attention. After aggregating these cost volumes, a geometry volume and feature volume are obtained to construct Gaussians. This works employs anchor points to distribute local Gaussians. By optimizing both the Gaussians and ray representation, it can recover the pose and 3D scene at the same time. Experiments on DTU and RealEstate10K verify the effectiveness of the proposed method.

### Strengths
1. This paper introduces the Pl$\ddot{u}$cker ray representation for relative pose estimation instead of directly predicting camera rotation and translation. 
2. Based on the pose representation, the proposed method embeds learned pose information into the cost volume to improve the Gaussian learning. 
3. For Gaussian learning, this work leverage anchor points to distribute local Gaussian, which can hierarchically learn intricate textures or complex geometries.

### Weaknesses
1. The proposed method relies on cost volume construction, which requires depth range priors. Moreover, can you discuss the limitation of the proposed unable on tackling unbounded $360^{\circ}$ scenes?
2. In fact, the anchor point idea used in this work is proposed by Scaffold-GS [1].  Can you clarify the difference between your use and Scaffold-GS? Maybe it is better to present a preliminary to introduce it as the scene representation.     
[1]  Lu, Tao, et al. Scaffold-gs: Structured 3d gaussians for view-adaptive rendering. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
3. The proposed method are trained on DTU and RealEstate10K, respectively. Then, the trained models are used to test the corresponding datasets. This cannot verify the generalizable ability of the proposed method. Can you test the proposed method on RealEstate10K with the model trained on DTU, and test the proposed method on DTU with the model trained on RealEstate10K?

### Questions
1. For the generalizable ability, can the model trained on one dataset generalize to different datasets? For example, can the model trained on RealEstate10K be used to test Tanks and Temples datasets [2]?   
[2] Knapitsch, Arno, et al. "Tanks and temples: Benchmarking large-scale scene reconstruction." ACM Transactions on Graphics (ToG) 36.4 (2017): 1-13.  
2. This work uses the ray representation from RayDiffusion. Can you compare the pose estimation performance with RayDiffusion?
3. For the pose-required methods, such as MVSplat, I am wondering if their rendering performance will improve if they are trained with the pose information estimated by  the proposed method or RayDiffusion.
4. In fact, the weighted cost volume in Eq. (3) can reflect the complex visibility information better. Why the mean and variance-based volume is added? Can you have an experiment on this?  
5. Can you show the efficiency of the proposed method in terms of inference time and GPU memory usage? Can the proposed method tackle higher-resolution input images, such as the original-resolution images in DTU and Tanks and Temples?

### Soundness
2

### Presentation
2

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
In this work, the authors predict a framework for pose-free generaliable 3DGS primitives prediction. By jointly predicting camera poses described with Plucker rays and injecting them into the Canonical Volume Construction, the framework can integrate multi-view features into geometry volume and feature volume under a single canonical view, which would be used for subsequent Gaussian primitive prediction through MLPs.

### Strengths
1. The idea of introducing  Plucker ray for pose representations and multi-view fusion guidance is useful;
 2. The Anchor-aligned Gaussian prediction by integrating cost volumes from multiple views into a single canonical view is a interesting idea;
 3. The evaluations on DTU and RealEstate10K datasets confirm that the proposed method can predict higher quality 3DGS primitives under the pose-free setting;

### Weaknesses
The main weaknesses of this work may include the lack of some critical details and discussions about related works. Please check the questions section for my problems about the details.
As for the lack of discussions, the idea of introducing Plucker ray maps to represent camera poses has been introduced in CAT3D[1]. The authors should discuss about their differences, at least.
As for the pose-free generalizable prediction of 3DGS primitives, Splat3R[2] also proposes another effective solution by estimating the camera poses through DUST3R[3]. Some related discussions and comparisons should be necessary to validate the effectiveness of this work.

### Questions
1. How is the cost volume $C_i$ transformed into pose-aware cost-volume $C_i'$? Cost volumes directly calculated from different views should not be directly added. Is there any operation, such as alignment, to make them additive? I would also appreciate it if the authors can provide more details about the $V_f$ and Fig.4.
 2. The necessity of using Plucker rays for camera poses should be further confirmed through some ablation experiments. For example, can we directly regress the camera poses with GT poses?
 3. How is the ground truth  Plucker rays acquired? Are they acquired with the original camera poses?
 4. How is the performances on more challenging dataset, e.g., Scannet? Besides, I am also curious about the number of Gaussian primitives acquired by this framework. As only one canonical view is used for prediction, would the number of predicted primitives less than other methods?

### Soundness
3

### Presentation
2

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
This paper introduces a pose-free generalizable Gaussian Splatting framework that leverages a feed-forward network to directly regress camera poses and Gaussians from unposed sparse RGB images. The authors propose two key modules to enhance the performance: Ray-Guided Multi-View Fusion, which consolidates multi-view features into a canonical volume using Plücker rays for pose estimation and scene geometry estimation, and Anchor-Aligned Gaussian Prediction, which predicts anchor points and offsets to generate refined Gaussian Splatting for detailed reconstruction. These modules enable the proposed framework outperform previous methods on benchmarks like DTU and RealEstate10K.

### Strengths
- The paper is clearly written with informative illustrations. The proposed framework is intuitive and the motivation behind each module is well-explained. The evaluation and ablation results validate the impact of the proposed components.
- The idea of coarse-to-fine Gaussian splatting generation using anchor-aligned Gaussian prediction is innovative and effective.

### Weaknesses
 - The main concern is the lack of comparison with state-of-the-art (SOTA) pose estimation methods like COLMAP, DUSt3R[1], and MASt3R[2]. The proposed method should compare baselines like camera poses from COLMAP or DUSt3R plus MVSplat/PixelSplat. While I expect COLMAP may not perform very well given the sparse image input,  DUSt3R/MASt3R is promising to give relatively accurate pose estimiation, as the paper InstantSplat[3] shows.
- The paper lacks evaluation in cross-dataset or in-the-wild settings, which raises concerns about the generalizability of the proposed methods, particularly in terms of pose estimation.
  [1]: Wang S, Leroy V, Cabon Y, et al. Dust3r: Geometric 3d vision made easy[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 20697-20709.
  [2]: Leroy V, Cabon Y, Revaud J. Grounding Image Matching in 3D with MASt3R[J]. arXiv preprint arXiv:2406.09756, 2024.
  [3]: Fan Z, Cong W, Wen K, et al. Instantsplat: Unbounded sparse-view pose-free gaussian splatting in 40 seconds[J]. arXiv preprint arXiv:2403.20309, 2024.

### Questions
- It's acceptable that the method is unable to outperforms pixelsplat/ MVSplat with GT pose assumption, since it's imfeasible to obtain such accurate poses using sparse image input. But as mentioned in the weekness, we need to see whether it can outperform other methods using SOTA camera pose estimation.
- Are the baselines shown in table trained with GT cmaera poses or noisy camera poses?
- The implementation details of other baselines seem to be missing in the Appendix/Supplementary, which is cliamed in line 405. The detailed implementation of all the network structure is also missing, as cliamed in line 419. 
- The equation related to \delta p is missing in equation 5. Based on Figure 4, it appears to be derived using network f_p. However, f_p in Equation 5 is used to generate Gaussian attributes, which creates some misalignment between the figure and the equation.

### Soundness
3

### Presentation
4

### Contribution
3
