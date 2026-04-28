# RetinaGS: Scalable Training for Dense Scene Rendering with Billion-Scale 3D Gaussians

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
In this work, we explore the possibility of training high-parameter 3D Gaussian splatting (3DGS) models on large-scale, high-resolution datasets. We design a general model parallel training method for 3DGS, named RetinaGS, which uses a proper rendering equation and can be applied to any scene and arbitrary distribution of Gaussian primitives. It enables us to explore the scaling behavior of 3DGS in terms of primitive numbers and training resolutions that were difficult to explore before and surpass previous state-of-the-art reconstruction quality. We observe a clear positive trend of increasing visual quality when increasing primitive numbers with our method. We also demonstrate the first attempt at training a 3DGS model with more than one billion primitives on the full MatrixCity dataset that attains a promising visual quality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper, named RetinaGS, aims to train 3DGS in a distributed way. It first divides the scene space into a set of convex subspaces, each subspace contains a subset of 3DGS and can thus be distributed trained. For each subspace, the proposed method calculates a partial color and partial opacity, and the final color is obtained by a weighted sum of all subspaces. This paper also did exhaustive experiments to show the effectiveness of their method on the MipNeRF360 dataset, Mega-NeRF dataset, and the MatrixCity dataset. The proposed method can achieve comparable rendering quality to existing NeRF/3DGS methods (GP-NeRF, 3DGS, and CityGaussian), while with many more model parameters.

### Strengths
(1) This paper did very exhaustive experiments on publicly available large-scale datasets, such as Mega-NeRF and MatrixCity.

(2) This paper can train 3DGS up to billion-scale 3D Gaussian primitives, which is very impressive.

(3) This paper is a good engineering work, though it is not the only work that can scale up the training of 3D GS to billion-scale data.

### Weaknesses
 (1) This method lacks discussion of more existing distributed methods, such as Hierarchical-GS (Kerbl, *el,al*, SIGRRAPH 2024), DOGS (Chen and Lee, NeurIPS 2024), and City-on-Web (Song *et,al*, ECCV 2024). The absence of a thorough comparison with Hierarchical-GS, which also employs a hierarchical structure for distributed training of 3DGS, is particularly concerning. The paper should clarify how its KD-tree based partitioning compares to the tree structure in Hierarchical-GS, especially in terms of memory overhead and rendering efficiency.

(2) To me, this method is quite similar to 1) **DOGS**, which also adopts a central manager to manage sub-models, and 2) **City-on-Web**, which also adopts a similar partial color and partial opacity rendering strategy (while City-on-Web uses volume rendering instead of point rendering) to compute the final color. Therefore, discussions and comparisons to DOGS and City-on-Web are necessary while missing in the current version. The paper needs to address how the proposed method handles splat boundaries and parameter partitioning, especially since 3DGS splats have volume, unlike the sampling points in NeRF-based methods like City-on-Web. Furthermore, the method should clarify how it avoids boundary artifacts, which are a common issue in methods that divide the scene into sub-models.

(3) The proposed method requires a gradient computation step and a gradient synchronization step on the central manager, which can consume more time than other distributed methods (VastGaussian, DOGS). The time for these steps should be clarified in the paper. It is also unclear how the method handles gradient synchronization for shared splats between workers and the associated overhead.

(4) This method requires running MVS on all training data. However, running MVS on large-scale datasets is time-consuming, and can even require much more time than training 3DGS on the same dataset. The paper should justify the necessity of MVS for initialization, especially since the original 3DGS densification strategy could also be used. The authors should also discuss the computational cost of MVS relative to the overall training time.

(5) This paper cares about the distributed training of 3DGS, and how the method can scale up the training of 3DGS to a billion scale. The improvements in visual quality are only based on the improved number of 3DGS. e.g. in Table 1, the PSNR is 27.70 with 217.30M 3D Gaussians, which has only marginal improvement compared to CityGaussian with 23.7M 3D Gaussians. The paper needs to clarify if the performance gains are solely due to the increased number of Gaussians or if there are other factors contributing to the improved results. The paper should also discuss the diminishing returns of adding more Gaussians.

(6) I appreciate the authors' effort in running exhaustive experiments on many existing large-scale datasets. However, the paper is more like a system work, and the novelty of the paper is limited, especially since the partial color and partial opacity strategy are already proposed in City-on-Web and there is lack of discussion of this paper with related works.

### Questions
(1) In the experiments, RetinaGS uses dense point clouds for initialization. Do the other methods use the same dense point clouds for a fair comparison? If not, the author should provide their results with sparse/dense point clouds.

(2) The author provides training time for their method in Table 2 and Table 3. While the training time of other methods is missing. I wonder would RetinaGS would be slower/faster than CityGaussian/VastGaussian/DOGS?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a distributed training framework, RetinaGS, for training large-scale 3D Gaussian Splatting (3DGS) models to achieve high-definition 3D scene reconstruction. To overcome the limitations of single-GPU training, RetinaGS employs a precise distributed rendering equation, uses KD-tree partitioning for load balancing, and initializes Gaussian splats through multi-view stereo, enabling parallel training of 3DGS across multiple GPUs. Experiments were conducted on datasets including Scannet++, MipNeRF-360, Mega-NeRF, and MatrixCity, demonstrating superior rendering quality and efficiency of RetinaGS on large-scale datasets. Notably, RetinaGS achieved the training of over a billion splats on the MatrixCity dataset, reaching unprecedented visual quality.

### Strengths
1. Clear Writing: The paper is well-organized, with logically structured sections and clear language. It effectively presents the problem background, research motivation, methods, and experimental results, making it easy for readers to understand the design principles and implementation of RetinaGS.
2. Engineering Contributions of Distributed Training: The proposed distributed training framework is technically sound and addresses high-performance computing needs. The framework also makes notable engineering contributions, including the use of KD-tree for load balancing across GPUs and multi-view stereo (MVS) for initializing Gaussian splats, which improve the efficiency and stability of distributed training.
3. Broad Experimentation: The method was tested on multiple datasets, including Scannet++, MipNeRF-360, Mega-NeRF, and MatrixCity, showcasing its applicability and performance across varying scene scales. The MatrixCity dataset especially highlights the scalability and rendering quality of the method.

### Weaknesses
1. Limited Scale of Experimented Scenes: Although the method was tested on four datasets, Scannet++ and MipNeRF-360 have relatively small scene scales, limiting the demonstration of its potential for large-scale scenes. Moreover, while MatrixCity is a large-scale dataset, it is synthetic and lacks validation on real-world scenes. Testing on more large-scale datasets, especially with real-world data, would better illustrate the practical applicability of RetinaGS. The lack of real-world validation is a significant concern, as synthetic data may not accurately reflect the complexities and challenges of real-world scenarios, such as varying lighting conditions, occlusions, and sensor noise. This limits the generalizability of the findings.
2. Lack of Comparison with Other Methods: The paper does not include comparisons with methods like VastGaussian or Hierarchical 3D Gaussians, which are also significant contributions in distributed 3D reconstruction. Comparing RetinaGS with these methods would provide a more comprehensive view of its advantages and limitations. Without such comparisons, it's difficult to ascertain the relative performance and novelty of RetinaGS compared to existing state-of-the-art techniques.
3. Lack of Quantitative Results in Exploration Study: In the first two sections of the EXPLORATION STUDY, the lack of quantitative results weakens support for the effectiveness of the method. Adding quantitative analysis would provide a clearer demonstration of the impact of different settings on model performance. For instance, the impact of different initialization strategies and distributed rendering techniques should be supported by concrete metrics, such as PSNR, SSIM, or LPIPS, to objectively assess their effectiveness.
4. Limited Novelty: The core idea of this paper is relatively straightforward, with the primary contribution being in the engineering implementation rather than in methodological innovation. Consequently, RetinaGS demonstrates moderate novelty in terms of the underlying approach.

### Questions
Insufficient Scenes in Mega-NeRF Experiments: The paper uses only three of the six scenes from the Mega-NeRF dataset for experiments, without explaining the rationale for this choice. This may affect the comprehensiveness of the experimental results. It would be beneficial to include results from all scenes or provide a clear explanation for the selected subset.

Some minor issues:
1. The word “distirbuted” should be corrected to “distributed” in Line 97.
2. In Table 4 on page 9, “Bacth Size” should be corrected to “Batch Size.”

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
The authors aim to achieve exceptional rendering visual fidelity, which requires training GS models with higher spatial resolution, larger datasets, and diverse viewing perspectives. However, current 3DGS training struggles in these settings. A core issue identified is that 3DGS training remains constrained by single-GPU setups, which become infeasible for handling even moderately sized scenes due to time and memory demands. While recent distributed training approaches split the scene data into subspaces processed independently on multiple GPUs, they rely on fixed data layouts like bird's-eye views that minimize ray overlap between subspaces. This partitioning strategy, however, does not generalize well to more complex 3D scenes where ray paths do not align with predefined cells, leading to rendering artifacts or training challenges.
This paper proposed a novel strategy to overcome these limitations, by introducing a more flexible KD-tree partitioning method and optimized multi-GPU training architecture to enhance the applicability of GS models across varied 3D scenes.

### Strengths
+ Significance: this paper is well motivated and tackles a critical gap in existing GS-based methods by addressing the need for higher resolution and the capacity to handle larger datasets and more complex scenes. By moving towards scalable, high-resolution 3D reconstruction, this work could influence a range of fields such as virtual reality, autonomous driving, and simulation. 
+ Quality: the distributed training of 3DGS is well supported by theory and proved efficacy in the experiments. Illustrations are clear and straightforward, with abundant experiments on diverse scenes. Supplemantary material is informative and solid.

### Weaknesses
 - Missing related work: the proposed partitioning and ray segment rendering reminds me of an existing work NeRF-XL. Perhaps these are concurrent works, but authors should at least discuss it in related work.
- Practical usage of KD-tree: it seems that KD-tree partition makes sense when the scene or scene points are evenly distribuuted. Will it still maintain a balanced workload between workers when the scene is not evenly distributed. 
- MVS points for initialization: I suppose that authors need to work from a quite dense and envenly distributed point initialization so they need to do MVS first. This is not necessary a weakness but maybe constraining its application e.g. when views are sparse or inconsistent to get an ideal MVS result, which is quite common in large-scale scene capturing.

### Questions
This work is developed upon 3DGS, can it be compatible with derivatives of 3DGS, e.g. 2DGS or scaffoldgs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents RetinaGS, which utilizes a subspace-based parallelization method as a learning approach for Gaussian Splatting. Each subspace is handled by a single process and rendered using a rendering function with indicators. Instead of the standard splitting algorithm in Gaussian Splatting, MVS primitives are used to control the total number of Gaussians.

### Strengths
1. RetinaGS is a 3DGS model capable of training on large-scale datasets through parallelization.

2. The subspace-level rendering pipeline parallelization using a KD-Tree is intriguing.

3. RetinaGS allows for a controllable number of Gaussians.

### Weaknesses
1. In Table 1, the number of Gaussians is more than five times that of 3DGS. In Figures 5 and 6, reducing the number of Gaussians to 1/10 lowers the PSNR by about 2. Compared to 3DGS, if RetinaGS has the same number of Gaussians, its PSNR would likely be even lower. Therefore, the proposed method does not appear effective relative to the increasing number of Gaussians. The core issue is that while the method scales the number of Gaussians, it does not demonstrate a performance gain commensurate with this increase, suggesting a potential inefficiency in how the additional Gaussians are utilized or optimized. This is further compounded by the fact that the baseline 3DGS method achieves comparable or better results with significantly fewer primitives.

2. It appears that RetinaGS depends on the accuracy of the MVS algorithm. The reliance on MVS for initial Gaussian placement introduces a potential bottleneck. If the MVS point cloud is inaccurate or incomplete, it could negatively impact the subsequent optimization and rendering quality of RetinaGS. Furthermore, the method does not seem to have a robust mechanism to correct or compensate for errors introduced by the MVS stage. This dependence on an external algorithm could limit the overall robustness and generalizability of the approach.

3. I recommend a comparison with Hierarchical3DGS[1], as both methods present chunk-based Gaussian Splatting approaches.

4. Missing a comparison of rendering speeds.

5. Fig. 5 is difficult to understand. First, the resolution/splat, count, and PSNR are not clearly visible. Additionally, the images without labels are ambiguous in meaning. For instance, the images in the bottom row all seem to represent GT.

### Questions
1. Does *k* represent the *k*-th index?

2. During rendering, is it necessary to explore all subspaces along the ray path? On average, how many subspaces does each ray hit?

$~$

Minor comments:

There is an inconsistency in figure references on line 269.

Dots are missing in abbreviations on lines 233, 252, 274, 347, 417, 419, and 879.

A dot is missing in the sentence "Validity of Distribute Rendering" on line 422.

### Soundness
2

### Presentation
1

### Contribution
2
