# CSI: Enhancing the Robustness of 3D Point Cloud Recognition against Corruption

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 8, 3

## Abstract
Despite recent advancements in deep neural networks for point cloud recognition, real-world safety-critical applications present challenges due to unavoidable data corruption. 
Current models often fall short in generalizing to unforeseen distribution shifts.
In this study, we harness the inherent set property of point cloud data to introduce a novel critical subset identification (CSI) method, aiming to bolster recognition robustness in the face of data corruption. Our CSI framework integrates two pivotal components: density-aware sampling (DAS) and self-entropy minimization (SEM), which cater to static and dynamic CSI, respectively. DAS ensures efficient robust anchor point sampling by factoring in local density, while SEM is employed during training to accentuate the most salient point-to-point attention. Evaluations reveal that our CSI approach yields error rates of 18.4\% and 16.3\% on ModelNet40-C and PointCloud-C, respectively, marking a notable improvement over state-of-the-art methods by margins of 5.2\% and 4.2\% on the respective benchmarks

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a "critical subset identification (CSI)" framework for robust point cloud perception, which comprises 1) a new point sampling strategy "density-aware sampling (DAS)" that locates high-density point areas for anchors, and 2) a new optimization objective "self-entropy minimization (SEM)" that encourage high-confidence predictions.

### Strengths
1. The two proposed techniques are clear and reasonable to me and design choices are backed up by concrete examples. Figure 3. shows a concrete example where Farthest Point Sampling and Random Sampling fail and the new Density-Aware sampling succeeds. Both techniques should be easy to implement in practice.

2. The ablation studies are thorough in the paper. It helps to understand the effect of the neighbor number k in DAS and the layer position of the SEM loss. 

3. A significant all-around robustness improvement is achieved. As shown in the supplementary table, the model gains better robustness to not only global noise injection but also various other types of corruption.

### Weaknesses
1. SEM is mostly based on previous knowledge that entropy minimization helps classification robustness, which slightly undermines the significance of the proposed techniques. Nonetheless, the paper provides a detailed discussion of how entropy minimization should be applied to transformer-based point classifiers in both attention layers and the classification head, accompanied by sufficient ablation studies.

2. It is not clear how general DAS is and how it affects the classifier's robustness to more types of corruptions other than global noise addition shown in Figure 3. Table 1 and Table 2 in the supplementary material ablate CSI as a whole so they can not show the effect of DAS. It would be better if DAS could be individually studied on different types of corruption.

### Questions
Please address the questions in the weakness section.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article proposes a critical subset identification (CSI) method for bolstering recognition robustness in the face of data corruption, which consists of two parts: density-aware sampling (DAS) and self-entropy minimization (SEM). DAS uses local density weighting to better sample point cloud data. During the training process, SEM introduces an optimization strategy of entropy minimization to the significance value calculated by self-attention, which improves the model's attention to points with higher significance values . The authors subsequently conducted experiments on two corruption benchmarks: ModelNet40-c and PointCloud-c, proving that their method can effectively improve the robustness of the point cloud transformer (PCT) model while ensuring performance on clean data sets.

### Strengths
- This paper is well-written, especially Section 3 providing clear and easily understandable explanations of the CSI framework.
- The idea of introducing Entropy minimization in Self-Attention Modules is simple and effective, and it integrates the significance values of different points into the model training process.
- The experiments are extensive in terms of implemented models. Especially the exploration of the impact of hyperparameters in the ablation study demonstrates the key parameters that affect the method.

### Weaknesses
 - The proposed method is somehow ad-hoc, with the authors needing to specify that DAS is only suitable for models including sampling&aggregation module. Also the justification for the proposed method is not well established, with the motivations being weak.
- The experiments on CSI are not persuasive enough, from the method comparison to the diversity of datasets. The authors should consider comparing with other train-time point cloud robust methods. The selected datasets are all derived from ModelNet40, indicating a lack of experimental diversity.
- The experiments show that CSI cannot effectively handle point dropping (e.g., occlusion) and transformations (e.g., rotation), and may even be harmful. This raises concerns about the generalizability of CSI and suggests that the results derived from the ModelNet40-C may be misleading. The method's limitations in handling occlusions and rotations are significant, and the authors should acknowledge this more explicitly.

### Questions
1. Please explain the statement “local density of a point positively correlated with its significance”? Previous work has indicated that significant points are usually outward points in the point cloud, which are generally sparse[1]. Also, traditional sampling methods like FPS tend to find points with low density as representations.
2. The authors should compare with other SOTA train-time methods under the same settings in the main experiment, such as data augmentation or modules addition to the model.
3. The authors present the SEM method for Global Feature in Table 5. Given that the authors are making a critical point selection, what is the purpose of this?
4. The experiments should consider including datasets not based on ModelNet40.
5. Tables 1 and 2 in Supplementary show that CSI cannot effectively handle point dropping (e.g., occlusion) and transformations (e.g., rotation), and may even be harmful. Does this indicate the limitations of CSI in terms of generalizability? Therefore, the reviewer points out that the results derived from the ModelNet40-C can be misleading.

[1] Zheng, Tianhang, et al. "Pointcloud saliency maps." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an important contribution addressing the challenge of robustness in 3D point cloud recognition. The proposed CSI method shows promising results and demonstrates improvements over existing methods. The authors propose a novel critical subset identification (CSI) method that utilizes the set property of point cloud data to enhance recognition robustness. The CSI framework consists of two components: density-aware sampling (DAS) and self-entropy minimization (SEM), which cater to static and dynamic CSI, respectively. Experimental results show that the CSI approach outperforms state-of-the-art methods on corruption robustness benchmarks.

### Strengths
(1). The paper introduces a novel method, CSI, to enhance the robustness of 3D point cloud recognition against data corruption. This is an innovative and practical contribution that addresses an important challenge in the field.


(2). The CSI framework incorporates two components, DAS and SEM, which provide a comprehensive approach to critical subset identification. The combination of these two techniques allows for both static and dynamic CSI, improving the robustness of recognition models in different scenarios.


(3). The paper presents thorough evaluations of the proposed CSI method on two corruption robustness benchmarks. The experimental results demonstrate significant improvements over state-of-the-art methods, validating the effectiveness of the approach.

### Weaknesses
(1). The paper could improve the clarity of exposition. Some parts of the paper, particularly in the methodology section, are not explained in a clear and concise manner, which may impede the reader's understanding. For instance, the specific implementation details of the density-aware sampling (DAS) and self-entropy minimization (SEM) components are not sufficiently elaborated. The reader would benefit from a more detailed explanation of how these components are mathematically formulated and how they interact within the CSI framework. The transition between static and dynamic CSI also lacks a clear explanation, making it difficult to understand the exact conditions under which each approach is applied.

(2). The paper could benefit from more detailed evaluation and ablation studies. While the experimental results show the superiority of the CSI method, it would be valuable to have a more in-depth analysis of its performance and a comparison with widely-known baselines in the field. For example, the paper does not provide a detailed analysis of the computational cost associated with the CSI method, which is a crucial factor for practical applications. Additionally, the ablation studies should include a more granular analysis of the individual contributions of DAS and SEM, perhaps by evaluating the performance of the CSI framework with only one of these components active.

### Questions
I think the method proposed in ModelNet40-C and PointCloud-C should also be compared and analyzed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduce the CSI, which incorporates DAS and SEM to find the essential subset of the point cloud for representation learning. This improves the model's robustness against data corruption.

### Strengths
- The focused topic is crucial for real-world applications of point clouds.
- The introduced SEM demonstrates its effectiveness.

### Weaknesses
 - The novelty of the proposed density-aware sampling may be limited as similar ideas have already been explored by previous methods [1,2], but the authors do not provide any comparisons with them.
- The writing is hard to read and follow. For example,
    - Too many sentences that are too long.
    > Similarly, in medical imaging, where point cloud data aids in 3D reconstructions from MRI or CT scans, the presence of artifacts, noise, and incomplete data — arising from limited resolution, patient movement, or implants — poses substantial challenges.
    >
    > By studying the robustness among various 3D architectures including PointNet (Charles et al., 2017), PointNet++ (Qi et al., 2017), DGCNN (Wang et al., 2019), etc., they revealed that Transformers, specifically PCT (Guo et al., 2021), can significantly enhance the robustness of point cloud recognition.
    - Inconsistent usage of section references. For instance, Section 3.2 (SELF -ENTROPY MINIMIZATION) uses different references like $\S 3.1$, $\S 1$, and *Section 2*; $d_a$ and $d_e$ in equation 4.
- The performance is not satisfactory. It over claims to "significantly outperform state-of-the-art methods by 5.2% and 4.2% on the respective benchmarks." This also weakens the motivation, as the authors believe that the data augmentation is inadequate in countering data corruption, leading to the proposal of CSI. However, it turns out that CSI performs worse than certain data augmentation techniques.
    - In Table 1, `PCT+CSI` achieves an ER of 18.4 in ModelNet40-C, which is clearly inferior to `PCT+PointCutMix-R` (16.3) and `PCT+PointCutMix-K` (16.5). These two configurations are from the method [3] that originally introduces the ModelNet40-C dataset. I observe that the authors perform the experiment with `PCT+PointCutMix-R+CSI` in Table 2, but the comparison is unfair because it involves comparing `A+B+C` against `A+B`, and the overall improvement is minimal (0.4%).
    - Similar observations can be found in Table 2 of the Appendix, where `PCT+PointCutMix-R+CSI` fails to outperform `PCT+WOLFMix`.
- The proposed method `PCT+CSI` is clearly inferior to `PCT+data_aug` in both ModelNet40-C and PointCloud-C. In ModelNet40-C, `PCT+CSI` achieves an ER of 18.4, while `PCT+RSMix`, `PCT+PointCutMix-K`, and `PCT+PointCutMix-R` achieve 17.3, 16.5, and 16.3, respectively. In PointCloud-C, `PCT+CSI` achieves an mCE of 0.757, whereas `PCT+WOLFMix` achieves 0.574. Furthermore, the authors claim that data augmentation techniques have varying degrees of effectiveness against different types of corruption. However, `PCT+WOLFMix` consistently enhances the original `PCT` across all types of corruption except for Scale, while `PCT+CSI` fails to improve performance in both Scale and Drop-G. This further weakens the authors' motivation.

### Questions
1. Did the authors try using `PCT+DAS` in Table 1? It would be more illustrative to include this result.
2. I am still confused about how SEM works. The authors mention that "Applying SEM to the row-wise embeddings in S amplifies the importance of the most crucial point-level feature corresponding to feature row i." Can the authors provide visualizations of attention maps to show which areas of the point cloud are salient?
3. Why did the authors suddenly switch to using mOA as a metric in Table 2 of the Appendix instead of ER?
4. Have the authors tried using the mCE metric from PointCloud-C [4] to directly compare the results of this paper with those in [4]?

---
References:

[4]: Benchmarking and Analyzing Point Cloud Classification under Corruptions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
