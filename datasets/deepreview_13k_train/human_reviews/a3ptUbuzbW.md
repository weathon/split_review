# CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, manifesting efficient and high-fidelity novel view synthesis. However, accurately representing surfaces, especially in large and complex scenarios, remains a significant challenge due to the unstructured nature of 3DGS. In this paper, we present CityGaussianV2, a novel approach for large-scale scene reconstruction that addresses critical challenges related to geometric accuracy and efficiency. Building on the favorable generalization capabilities of 2D Gaussian Splatting (2DGS), we address its convergence and scalability issues. Specifically, we implement a decomposed-gradient-based densification and depth regression technique to eliminate blurry artifacts and accelerate convergence. To scale up, we introduce an elongation filter that mitigates Gaussian count explosion caused by 2DGS degeneration. Furthermore, we optimize the CityGaussian pipeline for parallel training, achieving up to 10$\times$ compression, at least 25\% savings in training time, and a 50\% decrease in memory usage. We also established standard geometry benchmarks under large-scale scenes. Experimental results demonstrate that our method strikes a promising balance between visual quality, geometric accuracy, as well as storage and training costs. The project page is available at \url{https://dekuliutesla.io/CityGaussianV2/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents CityGaussianV2, a new method for large-scale 3D scene reconstruction that builds on a variant of Gaussian Splatting, 2D Gaussian Splatting.
CityGaussianV2 introduces 3 contributions to resolve scaling problem in large scale scene reconstruction. 1) Depth supervision which uses pre-trained depth estimator to supervise inverse depth, 2) decomposed-gradient-based densification (DGD) which adaptively densifies based on SSIM, and 3) elongation filter to accelerate convergence and mitigate the Gaussian count explosion problem. 
In addition to the core technical contributions, the paper presents an optimized parallel training pipeline and new evaluation protocol for large-scale scenes that addresses the limitations of existing benchmarks by accounting for boundary effects.

### Strengths
The paper solves one of the tougher remaining challenges in 3D reconstruction with Gaussian Splatting: large scale scene reconstruction. The qualitative and quantitative results of the paper are outstanding. Compared to existing baselines, the paper demonstrates faster convergence, more accurate photo-realistic reconstruction and lower memory usage. 
Moreover, the reviewer appreciates additional contributions such as new evaluation criteria that better captures geometric details of larger scenes. The paper spends a lot of effort on being fair on evaluation. The method compares with all SotA methods that the reviewer is aware of.

### Weaknesses
The technical novelty of the paper seems rather weak. The paper is built on top of existing works: 2D GS, Depth anything. While the paper has demonstrated a good way to fuse these existing works in a nice scalable manner, the provided contributions seem like multiple ad-hoc solutions to circumvent an underlying core problem: solving densification in a scalable way. 

In other words, the reviewer expects solid theoretical reasoning on why their optimization techniques are justified, instead of relying on empirical demonstration of good qualitative results. Otherwise, it is hard to justify whether the contributions of the work provided by authors are coming from meta-fine tuning of the existing 3D reconstruction dataset, or whether they are actual improvements.

### Questions
How were the baseline hyper-parameters tuned? It seems to me that the OOM and convergence may be overcome by the best set of hyperparameters in few of the existing models. 

How did the authors design the new techniques? I’m curious as to what led to the decisions of such new optimization techniques that are helpful, instead of other potential choices that may be similar in results.

### Soundness
2

### Presentation
3

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
This paper presents CityGaussianV2, a novel methodology for 3D scene reconstruction tailored for large-scale urban environments. It builds on the 2D Gaussian Splatting technique by incorporating advanced features such as Decomposed-Gradient-based Densification, depth supervision, and an Elongation Filter. These enhancements collectively aim to improve geometric accuracy and reduce computational demands.

### Strengths
The manuscript is well-constructed, with a logical flow that enhances readability. 

The use of technical terminology is appropriate, and complex concepts are elucidated with commendable clarity. The integration of innovative techniques like DGD and the Elongation Filter is particularly noteworthy, as these elements not only speed up training convergence but also refine rendering quality, effectively mitigating the Gaussian number explosion issue often seen in 3D Gaussian Splatting of large-scale scenes.

### Weaknesses
1. The manuscript explores outdoor reconstruction, yet it does not fully address the incorporation of techniques for improving robustness against variable lighting conditions and viewing angles. Techniques similar to the decoupled appearance models used in GOF could potentially bolster the system's adaptability. Specifically, the method does not account for shadows, specular reflections, or changes in ambient illumination that are common in real-world urban environments. The lack of explicit modeling of these effects could lead to artifacts and inconsistencies in the reconstructed 3D model, particularly when the input images are captured under diverse lighting conditions.

2. The proposed method employs an Elongation Filter to prevent excessive Gaussian numbers, but it lacks a mechanism for handling cases where splitting is necessary. Will directly limiting the Gaussian split result in some areas being under reconstruction? At the same time, why does the number of Gaussians in the method plus an Elongation Filter in Table 2 exceed the baseline? Shouldn't the filters be limited to the number of Gaussian functions? The concern is that by aggressively filtering elongated Gaussians, the method might prematurely discard Gaussians that are essential for capturing fine details or complex geometries. This could lead to a loss of fidelity in the reconstructed scene, especially in areas with intricate structures.

3. There appears to be a discrepancy between the Gaussian count reported in Figure 3 and the data presented in Table 2. The number of CityGaussian is less than that of the author's method (w Elongation Filter), it is inconsistent with the results shown in Table 2. This inconsistency raises questions about the reliability of the reported results and the experimental setup. It is crucial to have a clear and consistent reporting of the Gaussian counts across different experiments and figures to ensure the reproducibility and validity of the findings.

4. The limitations are only briefly touched upon in the appendix. A detailed examination within the main body of the paper would provide a more balanced perspective and foster a clearer understanding of the method's scope and potential constraints. The current brief mention in the appendix does not provide sufficient context or analysis of the limitations, which makes it difficult to assess the practical applicability of the method in real-world scenarios.

5. The metrics presented in Table 2 (e.g., number of Gaussians, processing time, memory usage) should specify the units of measurement to aid in interpretation. For example, the processing time should indicate whether it is measured in seconds, minutes, or hours, and the memory usage should specify whether it is in megabytes or gigabytes. Without clear units, it is difficult to compare the performance of the proposed method with other existing techniques.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose an optimization framework for Gaussian splitting, to address scalability issues when reconstructing large-scale scenes. The proposed framework builds on top of CityGaussian and is named CityGaussianV2 but addresses convergence and scalability issues. They propose the use of DGB densification and depth regression to improve blurry artifacts and accelerate convergence, an elongation filter to mitigate the Gaussian count explosion in 2DGS and a parallel training technique to improve training times and memory consumption.

### Strengths
The authors address critical issues in adapting Gaussian splitting techniques in large-scale 3D reconstructions. The proposed framework addressed issues related to scalability as well as reducing the costs associated with training large-scale Gaussian splitting models. The results of the proposed model show that the method is able to scale up CityGaussian without degrading visual quality and geometric accuracy. The paper is well-written and the ideas are well explained. The experimental evaluation is complete and supports the claims in the paper. The authors also provide ablation studies to support their design choices.

### Weaknesses
Minor weaknesses overall 
1) The novelty of the paper is limited but addresses a very important aspect of large-scale 3D reconstruction using gaussian splitting.

2) Lines 189-190 It looks like R and S symbols are flipped assuming that R is rotation and S is scaling then the decomposition of the covariance matrix makes sense. 

3) Line 352-352 How do you estimate the ground plane? Could you provide some more details about the number of points, the scale of the scene, and the hardware used so that this process can be completed in 1 minute?

### Questions
See above

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
The paper proposes a large-scale scene geometry reconstruction method based on Gaussian splatting. Specifically, it implements parallel training and compression for 2D Gaussian splatting, incorporates regression based on Depth Anything V2, and designs an Elongation Filter along with a Decomposed-Gradient-based Densification. Additionally, the paper establishes a benchmark for large-scale scene geometry reconstruction for evaluation purposes. The paper demonstrates through comparison experiments that its method achieves superior reconstruction quality on large-scale scenes.

### Strengths
1. The paper is clearly written.
2. It implements a comprehensive process for large-scale surface reconstruction, addressing issues in previous methods with thoughtful design, offering a substantial engineering contribution.
3. The paper conducts thorough ablation studies, analyzing the impact of each module on rendering, reconstruction quality, training time, storage requirements, and other factors.
4. The establishment of a large-scale geometry reconstruction benchmark is also a significant and meaningful contribution.

### Weaknesses
1. The method comprises multiple combined modules, some of which are known techniques or modified versions of known techniques, so overall, the novelty is somewhat limited. Moreover, the ablation results suggest that some modules have only minor impacts.
2. In the comparison experiments, the authors should also include metrics such as the number of Gaussians, training time, and memory usage for each method, in addition to rendering and reconstruction quality. For certain baseline methods like 2DGS, adjusting hyperparameters can increase the number of Gaussians to enhance the results. The authors should demonstrate that their method has advantages in rendering and reconstruction quality compared to baselines under similar training times and storage usage; otherwise, the results are not fully convincing.

### Questions
Apart from the weaknesses mentioned, there are some additional questions:
1. When running the baseline models, was the same hardware used (8 A100 GPUs)? This information should be included in the paper.
2. While the reconstruction quality surpasses CityGS, the rendering quality is slightly inferior across all datasets. What could be the potential reason for this?

### Soundness
3

### Presentation
3

### Contribution
3
