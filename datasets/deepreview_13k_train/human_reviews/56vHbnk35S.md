# Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
This paper investigates an open research challenge of reconstructing high-quality, large-scale 3D open scenes from images. It is observed existing methods have various limitations, such as requiring precise camera poses for input and dense viewpoints for supervision. 
To perform effective and efficient 3D scene reconstruction, we propose a novel graph-guided 3D scene reconstruction framework, GraphGS. Specifically, given a set of images captured by RGB cameras on a scene, we first design a spatial prior-based scene structure estimation method. This is then used to create a camera graph that includes information about the camera topology. Further, we propose to apply the graph-guided multi-view consistency constraint and adaptive sampling strategy to the 3D Gaussian Splatting optimization process. This greatly alleviates the issue of Gaussian points overfitting to specific sparse viewpoints and expedites the 3D reconstruction process. We demonstrate GraphGS achieves high-fidelity 3D reconstruction from images, which presents state-of-the-art performance through quantitative and qualitative evaluation across multiple datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a collection of practical optimizations to improve quality and efficiency of Gaussian Splatting reconstructions from image collections without poses. The optimizations relate to 
1. Efficient View-Pair Finding for Match-graph Construction for Structure from Motion
2. Octree initialization of 3D points and Level-of-details based pruning
3. Multi-view Consistency Loss in 3DGS optimization
4. Match-graph / Camera-graph Importance based View Sampling for 3DGS optimization

The author show results indicating, 
Optimization 1 leads to faster SfM (Table 3) and quality improvements in GS (Table 4)
Optimizations 2, 4 leads to faster GS optimization (Table 5, Table 7)
Optimizations 3, 4 leads to quality improvements in GS (Table 4, Table 7)

The results are evaluated on scenes from Waymo, Kitti, and Mill-19 datasets with images in the range of ~600, ~100, and ~2000.

### Strengths
Overall, I like that the authors propose very practical optimizations that bring both quality and run-time improvements. 

* Originality: The key original contribution of the paper is: Concentric Nearest Neighbor Pairing (CNNP) and Quadrant Filter (QF) organizing/pruning view-pairs in camera-graph. Other contributions are good practical applications of previously known ideas. 
* Clarity: The paper is written in a clear language, structured well, and shows experimental validation of the proposed ideas. 
* Significance: The paper introduces practical ideas for 3DGS from no-pose image collections.

### Weaknesses
 The method proposed in the paper is forming camera-graph using Dust3r to find relative poses between image pairs and pruning pairs using the proposed CNNP and QF steps. The efficiency of structure estimation is estimated w.r.t default COLMAP pipeline (assuming incremental Structure from Motion). This is not a fair comparison and sufficient details are not provided, making it harder to assess the true benefit of the proposed improvements. 

- Paper mentions that Dust3r is used to estimate pairwise relative poses in 0.01 seconds. Can you provide a more detailed breakdown of the Dust3r usage, including whether the 0.01 seconds is per pair or total, what specific hardware was used, and how many total pairs were evaluated across the different datasets

- COLMAP exhaustive and COLMAP vocab-tree matching time are provided. However, sufficient details on the experimental setup and compute resources are not provided. For example, for vocab-tree matching, which dataset is used to compute the vocab-tree, how many nearest neighbors are retrieved per image, in total how many pairs are evaluated? What compute resources are used for this matching? 

Without these details, it is difficult to draw conclusions. 

At a more basic level, Dust3r + CNNP + QF contributions are mainly to improve match-graph construction and BA runtime. A fair comparison of the improvements in these runtimes should be with other SoTA efficient SfM methods, not default COLMAP. 

Default incremental SfM implemented with COLMAP is commonly used by radiance field papers to compute poses but by no means this is the most efficient pipeline. There is a vast literature on how to approximate match-graph construction going back a decade. There are well-established alternatives to incremental Structure from Motion with implementations in Open source SfM libraries such as OpenMVG, OpenSfM, Theia, and most recently GLOMAP that offer much better run-time behavior. 

Given the authors use prior poses estimated from Dust3r, the comparison of CNNP and QF steps should be done with match-graph pruning methods that already use prior poses. A naive baseline to compare against would be to construct a camera-graph only from view pairs with overlapping frusta. Can you add this comparison to your evaluation, evaluating both quality and run-time?

I like the practicality of proposed ideas but I don't think that they are contextualized and compared correctly. The other ideas such as LOD-based point pruning and view-importance based sampling are nice practical improvements which provide qualitative and runtime gains w.r.t. original 3DGS paper, however 3DGS provides a baseline not SoTA comparison. A number of methods have been proposed since the original paper to improve both, the quality and efficiency of 3DGS (2DGS, RadSplats, . A few relevant to the paper: Hierarchical 3D Gaussian Representation (Kerbl et al SIGGRAPH Asia 2024), Scaffold-GS (Lu et al CVPR 2024), Octree-GS (Ren et al).  

The authors can also provide results on MipNeRF360 dataset which is used more commonly in radiance field literature, this will make it easier to compare their results against contemporary 3DGS methods.

As is, the paper is an assortment of good practical improvements for a sparse recon + 3DGS reconstruction system, and I am positive that these insights can be valuable for practitioners in the field. However, these small contributions are scattered across the pipeline and none are evaluated as thoroughly as they should be with SoTA methods and good baselines respectively for each, making it difficult to place the value/significance of contributions in context of SoTA.

### Questions
- See questions in Weaknesses sections. 
- What does "w/o structure estimation" mean in Table 4. 
- Which datasets are used for results in Table 4, Table 5, Table 7. 
- Is Dust3r used for only pairwise pose estimation or is the step that yields globally aligned point maps and poses also used?
- Definition of S_3^i in Eqn 1. is ambiguous, can you clarify what does this set include?

Minor : 
- Abstract mentions that : "This paper investigates ...  reconstructing high-quality, large-scale 3D open scenes from images." but the paper deals with scenes with 100 images, 600 images, and two scenes with 1500-2000 images. Typically large-scale in context of SfM and 3DGS refers to city-scale scenes with tens of thousands of images. 
- It should be clarified if I(p) in Eqn 8 means "intensity or color at pixel p in the image" refers to GT image or rendered image.

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
Focus on the large-scale Gaussian-based reconstruction pipeline, the authors propose a graph-guided framework, GraphGS, which leverages spatial priors for scene structure estimation to create a camera graph encoding camera topology. Using graph-guided multi-view consistency and an adaptive sampling strategy, GraphGS enhances the 3D Gaussian Splatting optimization, mitigating overfitting to sparse viewpoints and accelerating reconstruction. Quantitative and qualitative evaluations across multiple datasets demonstrate that GraphGS achieves state-of-the-art performance in 3D reconstruction.

### Strengths
1. the paper is easy to understand.
2. the results show the effectiveness of proposed pipeline.

### Weaknesses
1. The manuscript lacks a detailed explanation for each term in Equation (1), which would enhance clarity and understanding. Specifically, the roles of 'r', 'w', and 'h' in determining the camera matching pairs are not sufficiently elaborated, making it difficult to grasp the underlying logic of the graph construction. The lack of explanation makes it hard to understand how these parameters affect the graph topology and subsequent optimization.
2. Many of the authors' methods are designed to improve upon COLMAP. It would be beneficial to include experiments comparing the accuracy of initial values in GS, such as pose accuracy, to illustrate the improvements. The absence of a direct comparison of initial pose quality makes it challenging to isolate the contribution of the proposed graph-guided approach from improvements in the initial pose estimation. This makes it difficult to assess whether the gains are due to the graph structure or simply better initial pose estimates.

### Questions
1. If the spatial prior-based structure relies on the initial pose estimation, wouldn’t inaccurate initial results lead to a poorly constructed graph?
2. In Table 1, why doesn’t the FPS of the proposed method exceed that of the original 3D Gaussian Splatting (3DGS)? Intuitively, the pose estimation should contribute positively. Where is the additional computation time being spent?

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
5

### Summary
The authors propose a framework for large-scale 3D reconstruction using Gaussian splatting.  The authors suggest the construction of a prior graph-guided scene structure. This results in estimating a camera graph that encodes the camera topology. Then based on graph weights the employ an adaptive sampling strategy to the 3D Gaussian splatting optimization.

### Strengths
The authors present an elaborate pre-processing framework to effectively scale Gaussian splitting to large scenes. The ideas presented in the paper are exciting and well-presented for the most part. The concept of exploiting low-cost prior heuristics to allow the network to focus on the underlying task is interesting and the experimental evaluation demonstrates the effectiveness of the method.

### Weaknesses
1) minor: There are some spelling errors, please proofread the manuscript e.g ( line 135 formed -> form, line 138 initializaition -> initialization )

2) Line 147 - 149: Please specify here which models you use to obtain camera poses. How approximate are these poses? What is the error tolerance? Could you please provide quantitative metrics on the initial pose quality compared to ground truth if available?

3) For the concentric nn pairing the authors use the symbol S multiple times. It would make sense to use CNNR as a symbol of the overall process output and use more meaningful names than S1 S2 and S3 for the various heuristics. Maybe names related to their role in CNNR computation.

4) In the quadrant filer could you please specify whether the orientation is provided as a normal or any other form (euler angles)?

5) The adaptive sampling section is not clear.
    - line 322 primarily considers two criteria -> Are there more criteria than these two?
    - Line 344 We design node weight wn(i) based on betweenness centrality -> So the node weight does not take into account the degree centrality? 
    - How is the view selection probability integrated into the 3DGS optimization?

6) Lines 457-458: Could you please provide more information on how you obtained your initial poses and what is the size of the dataset, the hardware used, or any preprocessing stats that the relative pose estimation is done in 10ms?

### Questions
What is the minimum quality of poses required by the proposed framework? 
Does any of the proposed steps account for large errors in the pose estimation? 
Why do the authors attempt to compete strongly with COLMAP? COLMAP was used as a method to obtain initial poses and the authors used wang et al. 2024 to obtain initial poses. The framework the authors propose can be used with poses computed by either method.

### Soundness
3

### Presentation
3

### Contribution
3
