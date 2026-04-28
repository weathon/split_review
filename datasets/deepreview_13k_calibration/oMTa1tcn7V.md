# 3D Point Cloud Sequences as 2D Videos

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
Dynamic 3D point cloud sequences serve as one of the most common and practical representation modalities of dynamic real-world environments. However, their unstructured nature in both spatial and temporal domains poses significant challenges to effective and efficient processing. Existing deep point cloud sequence modeling approaches imitate the mature 2D video learning mechanisms by developing complex spatio-temporal point neighbor grouping and feature aggregation schemes, often resulting in methods lacking effectiveness, efficiency, and expressive power. In this paper, we propose a novel generic representation called \textit{Structured Point Cloud Videos} (SPCVs). Intuitively, by leveraging the fact that 3D geometric shapes are essentially 2D manifolds, SPCV re-organizes a point cloud sequence as a 2D video with spatial smoothness and temporal consistency, where the pixel values correspond to the 3D coordinates of points. The structured nature of our SPCV representation allows for the seamless adaptation of well-established 2D image/video techniques, enabling efficient and effective processing and analysis of 3D point cloud sequences. To achieve such re-organization, we design a self-supervised learning pipeline that is geometrically regularized and driven by self-reconstructive and deformation field learning objectives. Additionally, we construct SPCV-based frameworks for both low-level and high-level 3D point cloud sequence processing and analysis tasks, including action recognition, temporal interpolation, and compression. Extensive experiments demonstrate the versatility and superiority of the proposed SPCV, which has the potential to offer new possibilities for deep learning on unstructured 3D point cloud sequences.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an approach to convert a 3D point cloud sequence into a 2D video and then utilize 2D convolution blocks to encode. They learn to obtain a grid by deforming a 2D grid to the 3D point cloud while minimizing the EMD loss between the original point cloud and the reconstructed version.

### Strengths
This paper is very novel as it tries something very difficult -- map a 3D point cloud into 2D. This is mathematically impossible for (even) many of the cases they presented in the paper, where the topological difference between the point cloud and the 2D domain precludes a diffeomorphism. The paper indeed made significant efforts to attempt to do this as well as possible.

### Weaknesses
Fundamentally I don't agree with this approach because mathematically it is impossible. Besides, the regular Conv3D is a poor way to handle temporal motion -- we don't use it even in regular 2D videos, e.g. for video object segmentation tasks, due to its incapability to handle motion. This paper has to make a lot of effort to get it to work only somewhat well, with a lot of efficiency limitations.

But putting personal opinions aside, the main problem is that this paper tested only on some fringe problems in 3D point clouds -- it would be more convincing if the evaluations were done on tasks such as semantic segmentation, object detection, instance segmentation, scene flow, point cloud generation etc. rather than the correspondence and upsampling tasks that were examined in this paper. Besides, they should compare with regular point cloud backbones such as PointTransformer, MinkowskiNet, PointConv etc. on both efficiency and speed. For the goal this paper is claiming -- superiority and generality, and "opens up new possibilities for point cloud sequences", I would think the current evaluation is far from enough.

### Questions
I believe this paper needs a major revision and redo their experiments. Hence I cannot support accepting it in its current form.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach to representing point cloud sequences, considering them as colored videos. This representation enables the application of 2D/3D convolution techniques, leading to improved performance in the task. Additionally, the author proposes specific micro-designs for temporal and spatial alignment of different frames within a point cloud sequence.

### Strengths
- Reformulate the task in aspect of input representation, which is remarkable and interesting. 
- it is crucial to acknowledge that when applying convolutional kernels to point cloud data, achieving spatial consistency becomes a pivotal challenge

### Weaknesses
 - The paper is a little hard to read, the method is not clarified clearly. How to optimize the network with EMD loss? How to obtain the point cloud from 'I'.
- How it will perform when deal with unseen data (o.o.d. data), since the author claimed they adopt a over-fitting manner to perform pc2pixel transforms.
- what's pre-defined 2d grids?
- what does "deforms a pre-defined 2D regular grid" mean.

### Questions
See above. I hope the author can provide more clarification in rebuttal, focusing on the detailed pipeline (like, how to represent the point cloud as image.)

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new regular representation modality for 3D point cloud sequences, namely Point Geometry Video (PGV). Specifically, the frame-wise spatial structurization (FWSS) module learns to map a 3D point in the point cloud to a 2D regular grid with 2D convolutions in a coarse-to-fine manner, and the spatio-temporal joint structurization (STJS) module learns to add temporal consistency to the PGV with 3D convolutions. Extensive experiments are conducted on several downstream tasks, namely, dense correspondence prediction, spatial up-sampling, and future point cloud frame synthesis, showing good qualitative and quantitative results.

### Strengths
1. The proposed method is novel and insightful. The intuition is similar to UV mapping in a learnable way.
2. The qualitative and quantitative results are good. The method is promising to facilitate downstream tasks.

### Weaknesses
1. I would recommend the authors put the symbols with their corresponding items on the figures. For instance, in section 3.2 we see the $\mathbf{S}^0$ is the pre-defined 3D grid corresponding to the cube in Fig. 4. But what are $\mathbf{S}_f$, $\mathbf{S}_d$, and $\mathbf{S}'$ referring to? Readers would be happy to see them clearly noted in the figure.
2. For me, the convolutional manner in the STJS module might not be proper. Since the FWSS results are without temporal consistencies, it's surprising that local convolution kernels are able to handle irrelevant information across different timesteps. The concern is that applying 3D convolutions directly on the output of the FWSS module, which lacks explicit temporal alignment, might lead to the network learning spurious correlations or failing to capture meaningful temporal dynamics. The local receptive field of the 3D convolution might not be sufficient to establish the necessary correspondence across frames, especially when objects undergo significant motion or deformation.

### Questions
1. Can the authors explain in detail how the flow maps in the STJS module are learned? 
2. Can the method deal with partial point clouds, incomplete data, or irregular data? Say if we have a point cloud sequence unprojected from a video, we may want to take as inputs partial point clouds due to occlusions, and some parts in one frame might have no correspondence in some other frames.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a new way to represent 3D point clouds called point geometry video (PGV). It is to "flatten" the original 3D point cloud onto a 2D image plane, on which the [R, G, B] channels of each pixel are used to carry the [x, y, z] coordinate of the associated point in 3D space. The author imposes spatial and temporal smoothness in the PGV representation via an overfitting scheme for training the neural network modules. The resulting PGV representation of the 3D point cloud sequence is applied in dense correspondence prediction, spatial up-sampling, and future point cloud frame synthesis, showcasing interesting results.

### Strengths
This proposed PGV representation of point cloud sequence appears to be interesting, it "collapses" the 3D point clouds to regular 2D images so that they can be consumed by a regular processing pipeline (although I have concerns about its novelty, see weakness). The paper is well-written overall and easy to follow.

### Weaknesses
Despite the strength of the work, there are quite a few problems with it:

1. The concept of this "point geometry video" is not entirely new. In fact, it is very similar to two international patents published in 2022:

(a). "Learning-based point cloud compression via tearing transform," with International Publication Number: WO2022232547A1 (available via https://patentimages.storage.googleapis.com/51/19/af/ee3e55ed75618b/WO2022232547A1.pdf),

(b). "Learning-based point cloud compression via unfolding of 3D point clouds" with International Publication Number: WO2022271602A1 (available via https://patentimages.storage.googleapis.com/71/49/ab/6e2ea50f6af4a1/WO2022271602A1.pdf).

Idea-wise, this PGV work is especially similar to (b), the "unfolding" work. Because the "unfolding" work exactly proposes to view the 3D coordinates of the point clouds as pixel values on images, so that they can be processed by downstream 2D pipelines, e.g., see Fig. 3 of the "unfolding" work.
Additionally, the core idea to create such images in the PGV work (Fig. 3 in PGV paper) and that of the "unfolding" work is basically the same (Fig. 3 in "unfolding" work) - both intend to "deform" a predefined regular 2D grid to match with the original point cloud.
I can identify that the detailed designs of the two works are different (e.g., detailed architecture difference, overfitting in PGV v.s. latent codeword for representation in "unfolding" work), and the PGV work as an additional step to promote temporal consistency (Fig. 4 of the PGV paper). However, the idea of the PGV proposal still has many overlaps with that of the "unfolding" work, weakening the novelty of the PGV work.

2. The method used in Fig. 3 (FWSS) is highly related to a thread of point cloud decoders based on deforming a pre-defined pattern like a 2D grid. Representative works in this thread include AtlasNet, FoldingNet, PointCapsuleNet, etc., may be informative to also discuss these works.

3. The overfitting scheme in this work can limit the practical usage of the proposal due to high computational complexity, i.e., the network needs to be retrained for every new point cloud sequence.

4. How does the proposed method behave if the point clouds to be processed contain more complicated topologies? E.g., more holes, or multiple objects. The 8i sequences being used in the experimentation may be somewhat limited due to their simplicity.

### Questions
Please refer to the weaknesses. Please especially address my concern regarding the novelty of the proposal.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
