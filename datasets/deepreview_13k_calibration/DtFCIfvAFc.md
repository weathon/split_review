# Gaussian-Det: Learning Closed-Surface Gaussians for 3D Object Detection

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
Skins wrapping around our bodies, leathers covering over the sofa, sheet metal coating the car -- it suggests that objects are enclosed by a series of continuous surfaces, which provides us with informative geometry prior for objectness deduction. 
In this paper, we propose \ours which leverages Gaussian Splatting as surface representation for multi-view based 3D object detection. 
Unlike existing monocular or NeRF-based methods which depict the objects via discrete positional data, 
\ours models the objects in a continuous manner by formulating the input Gaussians as feature descriptors on a mass of partial surfaces. 
Furthermore, to address the numerous outliers inherently introduced by Gaussian splatting, we accordingly devise a Closure Inferring Module (CIM) for the comprehensive surface-based objectness deduction. 
CIM firstly estimates the probabilistic feature residuals for partial surfaces given the underdetermined nature of Gaussian Splatting, which are then coalesced into a holistic representation on the overall surface closure of the object proposal.  
In this way, the surface information \ours exploits serves as the prior on the quality and reliability of objectness and the information basis of proposal refinement. 
Experiments on both synthetic and real-world datasets demonstrate that \ours outperforms various existing approaches, in terms of both average precision and recall.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed a 3D object detection method based on the Gaussian splatting. With the Gaussian splatting as input, the proposed deep model extracts the 3D object bounding boxes. Experiments show the proposed methods give higher recall and precision than the competing methods.

### Strengths
The proposed method takes advantage of the Gaussian splatting representation for 3D object detection. Gaussian splatting is a more compact representation than the point clouds.

### Weaknesses
 - The paper combines several methods: (1) Official implementation of Gaussian splatting and (2) PointNet++. There is no new network structure
developed. The novelty is low.

- The overall network is not explicitly defined in the paper. please add this, otherwise it is impossible to check the details.

- The writing of the paper is quite unclear, especially the section 3.3. Theorem 1 is directly from the existing theorem. No need to include here. It is also confusing where this theorem is used anywhere in the paper. The equations are sloppy. Notations are a mess. The features
used two notations F and f. F^{cand} is not defined. f^{part} is also never defined anywhere in the paper. The equations from (6), (7), (11) need motivation and clarification.

- The experimental setting is not clearly defined. The authors used a dataset originally for 3D object detection in Nerf. It is not clear how the point cloud based methods, which need a point cloud input, are used in the experiment comparison.

- The qualitative examples of the proposed method show the quality of the 3D boxes is sometimes a lot worse than other competing methods. The boxes are often bigger and quite off. The competing methods also show many overlapping bounding boxes. No non-max suppression This may cause the lower numbers from the competing methods.

### Questions
See the questions in the weakness section.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper is presented a novel method for multi-view 3D object detection, exploiting Gaussian splatting to obtain a continuous scene representation. Then, to handle outliers in the previous representation, a closure inferring module is included that learns a probabilistic feature residual for partial surfaces and coalesces them into holistic representation on closure measurement. Experimental evaluation is reported on both synthetic and real datasets, including an ablation study and some comparisons with respect to competing approaches.

### Strengths
The paper is addressing a complex and important problem. 

The authors include most of the details to understand their proposal, being the technical section clear enough and well written. 

Gaussian-Det is simple and effective. To this end, the overall framework is divided into the construction of surfaces based on Gaussian representations, an object proposal initialization, as well as a partial surface feature inference and holistic surface closure coalescence. 

Both synthetic and real experiments are provided in the paper. The results are competitive with respect to several competing approaches.

The ablation study helps the reader.

### Weaknesses
 - Camera poses exploit a type of ground truth (point cloud) to be inferred. In my opinion, this is clearly a strong limitation of the paper. 

- Lack of challenging cases. In my opinion, some qualitative instances could be included in the paper, showing the effectiveness of the method in complex cases, especially, in comparison with other approaches.

### Questions
To be honest, I do not have many issues with the current submission. 

In figure 6, maybe the authors could use a different color per object. 

How could a noisy estimate of the cameras affect overall performance?

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
3

### Summary
This paper introduces a novel 3D object detection method, Gaussian-Det, which uses 3DGS to represent objects as continuous surfaces rather than NeRF discrete points. The method uses Gaussian as a surface descriptor and introduces the Closure Inference Module (CIM), which solves the outlier problem inherent in the 3DGS method by considering surface closure as a prior for objectness. The CIM operates in two phases: firstly, the probabilistic feature residuals are estimated for some of the surfaces, and then they are merged to form a holistic representation that measures the overall surface closure. The method is evaluated on synthetic (3D-FRONT) and real-world (ScanNet) datasets, and the results show a significant improvement over previous SOTA methods. The main innovations of the method are its surface-based representation and the use of surface closure as a geometric prior to improve the quality of detection.

### Strengths
- The proposed method show SOTA performance compared with previous NeRF based methods.
- Use 3DGS is faster than NeRF.
- The CIM module effectively handles outliers in Gaussian Splatting.

### Weaknesses
 - The proposed method show SOTA performance compared with previous NeRF based methods.
- Use 3DGS is faster than NeRF.
- The CIM module effectively handles outliers in Gaussian Splatting.

 - There is a lack of qualitative comparisons between different components, particularly regarding the use of Holistic Surface Coalescence and Residual Estimation. These comparisons are important for readers to better understand the effectiveness of each component. For example, it is unclear how much each contributes to the final performance and if there are scenarios where one is more critical than the other. A detailed ablation study with visual examples would be beneficial.
- It would be interesting to analyze how the underlying Gaussian representation affects the results. For example, what is the impact of using the original 3DGS or a 2DGS representation? The current analysis does not explore the sensitivity of the method to the quality of the initial Gaussian splatting. It is important to understand if the method is robust to variations in the Gaussian representation, or if it relies on a specific type of splatting for optimal performance. Furthermore, the impact of using different Gaussian parameters (e.g., covariance, scale) on the detection results should be investigated.
- The overall writing is unclear and difficult to follow.
	- L.208 should be "From G^{cand}"
	- There is multiple M in FIg. 2, are they the same?
	- Figure 3 is confusing. It is unclear what “open surfaces” and “closed surfaces” refer to. In Figure 3 (a) and (b), the primary visual difference appears to be the incompleteness of the Gaussians in (b). Please clarify the relationship between open and closed surfaces.

### Questions
Improving readability and providing a visual comparison of the ablations would better present this work.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents Gaussian-Det, a method to detect 3D objects via Gaussian Splatting. The proposed method leverages Gaussian Splatting as surface representation for multi-view based 3D object detection. Gaussian-Det proposes Closure Inferring Module (CIM) to deal with the outliers present using Gaussian-Splatting technologies. The paper presents experiments on both synthetic and real 3D-object detection datasets where Gaussian-Det mostly outperforms previous methods.

### Strengths
- Interesting solution using Gaussian-Splatting technologies for 3D object detection.
- Proposing Closure Inferring Module (CIM) to deal with the noisy nature of Gaussian-Splatting representations.

### Weaknesses
 - Clarity of the paper is not good and needs improvement (my most concerning weakness). First, overall the high-level idea is not clearly explained. Although, Fig. 2 tries to do this, it falls short. Figure 2 lacks a clear illustration of the goal using the Backbone, and most importantly, fails to explain clearly how the CIM module (in my opinion the main contribution). Second, given the lack of clarity, it is hard to judge the novelty and quality of the solution. For example, I don't find the description of the Theorem if the high-level idea is not explained clearly. In my opinion it is just using space that could've been used to add Figures to explain CIM in a better way.

- Lack of details in the experiments. First, in line 320-321, the narrative says that the scenes are manually downsized into 159 usable rooms. However, it is not clear if the data was verified to ensure high quality. This is important since this data is used to measure quality.
 
- Insufficient experiments. In my opinion, showing results only on 2 datasets is not that convincing. Given that 3D object detection has been around for some time, it would've been more informative to know the performance of this proposed method on more real-scenes benchmarks/datasets (e.g., Waymo Open datasets, Objectron, etc.). I think that these datasets could've revealed the practical benefit of the proposed approach.

### Questions
See Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3
