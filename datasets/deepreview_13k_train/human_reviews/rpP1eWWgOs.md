# Surface Representation in LiDAR Scenes

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Learning from point clouds entails knowledge of local shape geometry. Recent efforts have succeeded in representing synthetic point clouds as surfels. However, these methods struggle to deal with LiDAR point clouds captured from real scans, which are sparse, uneven, and larger-scale. In this paper, we introduce \textbf{RealSurf}, a general framework that processes point clouds under extreme conditions like autonomous driving scenarios. We identify several key challenges in applying surface representations to real scans and propose solutions to these challenges: Point Sliding Module that jitters point coordinates within the reconstructed surfels for geometric feature computation, and LiDAR-based surfel reconstruction process that enables models to directly construct surfels from LiDAR point clouds by attenuating unevenness. We evaluate our approach on a diverse set of benchmarks, including nuScenes, SemanticKITTI, and Waymo. RealSurf, with a simple PointNet++ backbone, outperforms its counterparts by a significant margin while remaining efficient. By achieving state-of-the-art results on three benchmarks through a fair and unbiased comparison, RealSurf brings renewed attention to the effectiveness of point-based methods in LiDAR segmentation. Code will be publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a surface representation approach for the lidar point cloud semantic segmentation.
Based on the RepSurf, the authors proposed RealSurf by mainly introducing a point sliding module and FPS sampling to address challenges by sparsity, density variation, and large scale as analyzed. Evaluation results on three benchmarks show the advantages of the proposed method.

### Strengths
- The paper is well-written and easy to follow.
- The motivation of the method is practical and reasonable for processing LiDAR point cloud.
- The experiments on there datasets show the advatanges of RealRep.

### Weaknesses
 - The paper misses comparison with recent point cloud works such as [1].
- In my understanding, the main purpose of the introduced strategies seems to make the real data uniform for Repsurf and make the model more robust to real noisy data by jitter augmentation. The technical contributions are somewhat limited considering the RepSurf.


### Questions
- The efforts of proposed strategies such as downsampling seem to trim the data more suitable for Repsurf.  How about the effects if applying the same strategies to synthetic data?
- It is a little confusing why the number of points doesn't increase after the densification process as illustrated in Fig. 2.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to generate surface elements (surfels) from LiDAR point clouds. Different from the previous approach that only works on synthetic data, the proposed method, RealSurf, is able to process the point clouds in real data. To solve this problem, the proposed method includes a Point Sliding Module that jitters points within the reconstructed surfels, and a LiDAR-based surfel reconstruction process leveraging attenuating unevenness. The proposed method is evaluated on three popular outdoor benchmarks, such as nuScenes, SemanticKITTI, and Waymo, and archives state-of-the-art results even compared to voxel-based and RGB+point methods.

### Strengths
1. The method is evaluated extensively on three popular outdoor benchmarks and achieves state-of-the-art performance.
2. Thorough ablation studies are conducted to show the effectiveness of each proposed module.

### Weaknesses
1. Naive baseline: Occupancy Network + Marching Cubes?
2. How many points are left after a different number of downsampling?
3. Outdoor lidar point cloud is more sparse, I am wondering how the proposed method works on indoor dense point cloud with more occlusions in real scans?
4. Point Sliding is a data augmentation method that jitters the points so as to make the proposed method more robust to noises. In the ablation study (Figure 7), the authors show 0.5 performs best with Guassian noise on SemanticKITTI. I am wondering, is this hyper parameter consistent across different benchmarks?
5. Is the method limited to pointnet++?
6. I am not sure jitter points count as a novel contribution for dealing with noisy real scans. It is common to apply this technique when training networks on noisy point clouds, e.g, see MinkovskiEngine dataloader.

### Questions
The voxel-based method also shows some advantages, do you consider a hybrid network that consumes both points and voxels? such as Point-Voxel CNN for Efficient 3D Deep Learning.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents RealSurf, a framework designed to process point clouds in challenging environments like autonomous driving. The paper identifies challenges in applying surface representations to real scans and offers solutions, including the Point Sliding Module for geometric feature computation and a LiDAR-based surfel reconstruction process that reduces unevenness. When evaluated on benchmarks like nuScenes, SemanticKITTI, and Waymo, RealSurf outperforms its competitors and establishes its efficiency. This success highlights the potential of point-based methods in LiDAR segmentation.

### Strengths
1. The presented work offers a new framework designed for processing LiDAR point clouds. 
2. Using a basic PointNet++ structure, this method has demonstrated top-tier performance across multiple demanding datasets, such as SemanticKITTI, nuScenes, and Waymo. 
3. Their innovative solutions are versatile and can be integrated into any point-based network.

### Weaknesses
1. The paper would benefit from further refinement in its writing. Some sections might appear a bit complex and could be clarified for easier comprehension. 
2. Many parts of the writing are not professional, such as many lines in the text that have only one word, which should be avoided as much as possible.
3. It might be beneficial for readers if the motivation behind the paper were more prominently emphasized. Upon careful reading, I found it a bit subtle to identify the core motivation. Was it primarily about the 'point sliding module'? If so, the contribution of the article appears to be somewhat incremental. I hope the authors can highlight their contributions. 
4. The experimental results are good, but the comparison might not seem very fair. If I'm not mistaken, the entire framework is just PointNet++ with the addition of tangent plane information to its input. Why is there such a significant improvement compared to PointNet++ as shown in Table 1 or Table 2? Does the comparison in Table 1 or 2 involve an unfair comparison? How would it fare against other methods if various tricks were also applied? In Table 2, compared to the previous PointNet++, there's an improvement of 50 points. It seems that some of the latest tricks were used. It's hard to believe that there would be such a significant improvement by just adding some extra information. If there are any unfair comparisons, it would be better to unify some settings for a fair comparison and demonstrate it on top-performing (SOTA) methods. After all, the method introduced in the paper is framework-agnostic and is a general method for point clouds.

### Questions
All the questions I want to ask are in the 'weakness' section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose a representation dedication for LiDAR point clouds. It particularly extends the work RepSurf for synthetic point clouds to the case of LiDAR point clouds. To tackle the challenge of sparse, uneven, and large-scale LiDAR point clouds, the authors use a point sliding module to jitter the centroid of the triangle. An additional strategy is to gradually downsample the point clouds and extract the features for aggregation. This work demonstrates its performance in point cloud segmentation and shows some advantages.

### Strengths
This paper is well-written and easy to follow. The idea to extend RepSurf to the LiDAR point cloud case is also interesting. Experimentation seems to support the capability of the proposal for the application of segmentation.

### Weaknesses
There are quite a few concerns about this work:

1. This work only applies the proposed method for feature extraction to segmentation. Can it be generalized to other types of point cloud problems, for instance, low-level point cloud processing problems, e.g., denoising, upsampling, etc.? Specifically, the method's reliance on surface normals and triangle mesh construction might limit its applicability to tasks where these geometric features are not directly relevant or reliable, such as in highly noisy or incomplete point clouds.

2. A follow-up question is, since this method works well for sparse LiDAR point clouds, can it be applied back to the simpler case which is the dense point clouds or synthetic point clouds? Will the performance also be improved? It's unclear if the computational overhead of the proposed method would justify its use in scenarios where simpler methods already perform well. The paper should explore this trade-off.

3. The Point Sliding Module generates some jittering to the centroid for augmentation. This process has certain randomness because the coefficients are drawn from uniform or Gaussian distribution. I wonder how stable this method would be in the end, because there is a certain randomness in the process. The paper lacks a thorough analysis of the impact of these random augmentations on the final performance, including variance in results across multiple runs.

4. The authors use downsampling with FPS to obtain the RealSurf feature. However, this is also performed in PointNet++. Thus it would be better if the authors could further clarify the way they do the downsampling differs from that is proposed in PointNet++. The paper needs to clarify if the FPS is used in the same way as in PointNet++, or if there are any modifications or specific parameter settings that make it different. Without this, it's difficult to assess the novelty of the approach.

5. How this this work compare to other types of advanced feature extractors? For example, those based on transformer modules, e.g., Point transformer and Voxel transformer. A more comprehensive comparison with state-of-the-art methods, including those based on attention mechanisms, is needed to fully understand the advantages and limitations of the proposed approach.

6. How is the computational complexity of this proposal compared to PointNet++ and other competing methods? The paper should provide a detailed analysis of the computational cost, including both time and memory requirements, and compare it with existing methods to evaluate its practical feasibility.

### Questions
Please refer to the concerns/questions/comments mentioned in the weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
