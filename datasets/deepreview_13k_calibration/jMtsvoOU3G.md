# SinPoint: A Novel Topological Consistent Augmentation for Point Cloud Understanding

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
Data augmentation is a highly effective method for addressing the issue of data scarcity in machine learning and computer vision tasks. It involves diversifying the original data through a series of transformations to improve the robustness and generalization ability of the model. However, due to the disorder and irregularity of point clouds, existing methods struggle to enrich geometric diversity and maintain topological consistency, leading to imprecise point cloud understanding. In this paper, we propose SinPoint, a novel method designed to preserve the topological structure of the original point cloud through a homeomorphism. Additionally, it utilizes the Sine function to generate smooth displacements. This simulates object deformations, thereby producing a rich diversity of samples. Our extensive experiments demonstrate that SinPoint consistently outperforms existing Mixup and Deformation methods on various benchmark point cloud datasets, improving performance for shape classification and part segmentation tasks. Specifically, when used with PointNet++ and DGCNN, SinPoint achieves a state-of-the-art accuracy of 90.2 on shape classification with the real-world ScanObjectNN dataset. Furthermore, our method is highly versatile and scalable, and it can adapt to different scenarios and requirements for point cloud tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces SinPoint, a novel point cloud data augmentation method that uniquely combines homeomorphism and sine functions. The method addresses two critical challenges: maintaining topological consistency while increasing geometric diversity in point cloud data. SinPoint offers two transformation strategies: Single Sine Function (SinPoint-SSF) and Multiple Sine Function (SinPoint-MSF). The approach demonstrates superior performance on various benchmark datasets, achieving 90.2% accuracy on the ScanObjectNN dataset for shape classification tasks. The method's key innovation lies in its ability to preserve topological structure while simulating natural object deformations, making it versatile and applicable across different point cloud understanding tasks.

### Strengths
The method uniquely preserves topological consistency through homeomorphism while creating diverse geometric variations using sine functions, avoiding the common problem of structure distortion that exists in previous point cloud augmentation methods.

### Weaknesses
1、This method is based on experiments conducted on older methods such as PointNet++ and DGCNN, and the experimental results are not very convincing because it is well known that these methods can also achieve high performance improvements by adjusting some parameters.
2、The paper lacks comparison with some of the latest point cloud enhancement methods in comparative experiments. At the same time, the stability and robustness analysis of the method under different parameter settings is not sufficient.
3、Although sine functions and homeomorphic mappings are used, the theoretical innovation of the method is not prominent enough. This combination of mathematical tools seems to be relatively intuitive, lacking deeper theoretical insights and mathematical derivations.
4、The article lacks detailed ablation experiments to prove the necessity of each component. In particular, there is a lack of in-depth analysis of the selection basis and performance differences between the SSF and MSF strategies.
5、Can the topological structure information of point clouds be learned through persistent homology? What are the advantages of the method proposed in this paper over persistent homology in maintaining the topological structure of point clouds?
6、The expression of Figure 4 needs to be improved.

### Questions
See Weaknesses.

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
5

### Summary
The paper proposes a novel point cloud data augmentation technique called SinPoint. It is based on a homomorphism and maintains topological consistency while increasing the geometric diversity of samples (perturbs the local structure using a Sine function). The approach has 1) a Single Sine Function (SinPoint-SSF) to deform the point cloud with origin as the initial phase and 2) a Multiple Sine Function (SinPoint-MSF) with different anchor points as the initial phase. Richer deformations are achieved from the superimposition of the sine transforms of different parameters. The paper demonstrates the effectiveness of the proposed framework by showing consistent improvements over SOTA augmentation methods on both synthetic and real-world datasets in 3D shape classification and part segmentation tasks. The proposed SinPoint improves the generalization and robustness of several classification models and segmentation (PointNet, PointNet++, and DGCNN) models.

### Strengths
+ Most recent 3D point cloud augmentation methods focus on classification. The proposed approach also focuses on segmentation.
+ Most existing augmentation methods are proposed as an alternative to conventional data augmentation (CDA). The proposed approach is in addition to CDA and allows the simultaneous use of other augmentation techniques.
+ The paper is easy to read and well-written, with ample references to recent works.
+ The experiments sections provide ample proof of the proposed approach's impact on various SOTA point cloud classification methods.

### Weaknesses
 - The impact of the proposed augmentation techniques has been demonstrated on a limited number of segmentation backbones (precisely PointNet, PointNet++, and DGCNN). These backbones are almost five-year-old methods and have ample room to show the impact. The proposed work does not show its effects in recent methods (PointNeXt onwards), making it unclear if the proposed augmentation approach is relevant to the current state-of-the-art segmentation methods. Specifically, the lack of evaluation on more recent architectures leaves a gap in understanding the generalizability of SinPoint's benefits. The performance gains observed on older models might not translate to the same degree on more complex and optimized architectures.
- Figures 8 and 9 in the supplementary pages (page 19) show that the second augmented table generated (using SinPoint SSF) shows that the table top surface has a concave bend so that items placed on it would roll over. Such samples are not realistic or meaningful. This raises concerns about the physical plausibility of the generated augmentations and whether they introduce artifacts that could negatively impact the learning process, especially when dealing with real-world data where such deformations are unlikely to occur.
- Inconsistency in using recent models to demonstrate the improvement in classification accuracy for different datasets. For example, PointNeXt, PointMetaBase, and SpoTr are selected to show the improvement in results for the ScanObjectNN dataset's OBJ_ONLY variant in Table 3; the same models are ignored to show the upgrades for the ModelNet40 dataset in Table 2. And vice versa, when considering models in Table 2 that were used to show improvements for the ModelNet40 dataset, they are ignored when showing improvements on ScanObjectNN dataset variants. This selective reporting makes it difficult to assess the true effectiveness of the proposed method across different architectures and datasets. It also raises questions about potential biases in the experimental design.
- Some of the SOTA models have both classification and segmentation backbones, but there has been a selective approach to showing improvement on one task while ignoring the other. For example, PointMLP was used as the backbone for classification experiments in Table 3 but ignored for segmentation experiments. This inconsistent evaluation strategy limits the scope of the conclusions that can be drawn from the experiments and makes it hard to understand the full potential of the proposed augmentation technique.

### Questions
Although this might sound like a request for more experiments, please include results on a more recent backbone (preferably from 2023 or 2024) to show the relevance/impact on current segmentation methods.

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
4

### Summary
The paper introduces a data augmentation method for point cloud understanding, which utilize Sine function to generate smooth displacements and preserve the topological structure of the original points via a homeomorphism. The authors evaluate the proposed method with different backbones on object classification and part segmentation tasks to demonstrate the effectiveness.

### Strengths
+ The authors propose a simple but effective data augmentation method in some scenarios .
+ The writing and presentation is clear.

### Weaknesses
 - While homeomorphism can theoretically provide a wide range of continuous transformations for data augmentation, in practice, they can distort essential geometric features (can preserve topological properties but not geometric ones like distances, angles, and curvature), introduce unrealistic data (can warp objects into unnatural shapes that do not exist in the real world as shown in Figure 2, 6, 8 and 9), and complicate the learning process for models in part segmentation (can alter these relationships by stretching or compressing certain regions, leading to confusion in part boundaries and potential mislabeling; then providing incorrect training signals and degrading the model's performance as shown in Table 6 and 7).

- Limited Experimental Evaluation:
  + For the synthetic dataset in the classification task, the proposed method is effective when combined with older methods but less so with recent ones, as shown in Table 2.
  + Insufficient Real-World Testing: The authors only tested on the easiest subset (OBJ_ONLY) of the ScanObjectNN dataset (Tables 3 and 4), which does not confirm the method's superior performance with complex and noisy data (PB_T50_RS of ScanObjectNN or other real-world datasets).
  + In the part segmentation task, the proposed method performs on par with other methods. Since segmentation requires point-wise labels rather than whole shape labels, the effectiveness of homeomorphism-based augmentation is limited in this context (as mentioned above).

### Questions
- For the part segmentation, could the authors provide a more detailed analysis of how their method affects part boundaries and label consistency?
- The authors should evaluate their method on more challenging datasets, such as classification on PB_T50_RS of ScanObjectNN, semantic segmentation tasks in S3DIS (real-world, room-scale environments) and SemanticKITTI (outdoor, dynamic, real-world scenarios), to demonstrate its robustness and applicability to complex data.
- The authors should provide the extra model size, parameters, throughput when combining the proposed method with other backbones.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel data augmentation method called SinPoint, which enhances the geometric diversity of point clouds while preserving the topological structure of the original point cloud through a homeomorphism. Experiments conducted on multiple datasets and models demonstrate the effectiveness of this approach.

### Strengths
The SinPoint method proposed in this paper effectively enhances performance across multiple datasets and models, and it is both concise and efficient. Additionally, the article is well-structured, clearly articulated, and includes rigorous mathematical proofs. The experiments are comprehensive, and supported by sufficient visualization results.

### Weaknesses
1. There are some minor errors in the details. In Table 1, the results for SinPoint on PointNet++ and ModelNet40 are calculated incorrectly. Additionally, similar errors are present in Table 2 for PCT and PointMLP. I suggest that the authors carefully review the results in these tables.


### Questions
1. It is recommended that the authors thoroughly review the results in the tables and make corrections in subsequent versions.

2. Figure 3 indicates that random angular velocities may lead to uncontrolled variations. Are there detailed experimental results demonstrating the performance differences between random angular velocities and fixed angular velocities? For instance, it would be helpful to report the accuracy on ModelNet40.

3. The results in Table 5 suggest that SinPoint can be combined with other data augmentation methods. Would it be possible to integrate more advanced mixup techniques to further enhance performance?

### Soundness
3

### Presentation
3

### Contribution
3
