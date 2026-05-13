# Gaga: Group Any Gaussians via 3D-aware Memory Bank

- Decision: Reject
- Scores: 8, 5, 3, 5

## Abstract
We introduce {\ourmethod}, a framework that reconstructs and segments open-world 3D scenes by leveraging inconsistent 2D masks predicted by zero-shot segmentation models.
    Contrasted to prior 3D scene segmentation approaches that heavily rely on video object tracking, {\ourmethod} utilizes spatial information and effectively associates object masks across diverse camera poses.
    By eliminating the assumption of continuous view changes in training images, {\ourmethod} demonstrates robustness to variations in camera poses, particularly beneficial for sparsely sampled images, ensuring precise mask label consistency.
    Furthermore, {\ourmethod} accommodates 2D segmentation masks from diverse sources and demonstrates robust performance with different open-world zero-shot segmentation models, enhancing its versatility. 
    Extensive qualitative and quantitative evaluations demonstrate that {\ourmethod} performs favorably against state-of-the-art methods, emphasizing its potential for real-world applications such as scene understanding and manipulation.
  \keywords{3D Open-world Segmentation \and Gaussian Splatting \and Scene Understanding}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new framework called Gaga to segment 3D Gaussians in the open world. The key idea is to assign a multi-view consistent universal mask ID before lifting the 2D result to 3D, which is achieved by searching a memory back for the category ID based on the overlap area with the unprotected mask. Extensive qualitative and quantitative results show the effectiveness of the proposed method.

### Strengths
1. Clear motivation and insightful key idea.
2. Simple but effective, supported by extensive experiments on various datasets.
3. A demo video, more extensive details and limitations are provided in the supplementary material.
4. The paper is well-written.

### Weaknesses
1. The whole framework is heavily based on the Identity Encoding proposed in Gaussian Grouping by utilizing 3D Gaussian representations. However, in the abstract, it does not mention the use of 3D GS. This should be addressed in the final version.  
2. Some important works [1, 2, 3, 4] should be discussed in the final version. Especially for both [1, 2, 4], they all propose to merge 3D results in 3D space, [4] also assign universal mask ID derived from prompt ID for better consistency.

### Questions
Can the proposed 3D-aware memory bank be used in other 3D representations such as NeRF, 3D point clouds? Some discussions are expected to be provided. 
In the final version, the author may include a brief discussion in their Future Work or Discussion section about potential adaptations or challenges in applying their 3D-aware memory bank to other 3D representations like NeRF or point clouds.

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
3

### Summary
The paper introduces Gaga, a framework for reconstructing and segmenting open-world 3D scenes using 2D masks from zero-shot segmentation models. Gaga focuses on achieving consistent label assignments across multiple views, crucial for accurate 3D segmentation. Using a 3D-aware memory bank, it proposes a mask association strategy to unify multi-view masks. Evaluations on datasets like LERF-Mask, Replica, ScanNet, and MipNeRF 360 for tasks such as open-vocabulary 3D queries and 3D segmentation demonstrate promising results, highlighting its potential for downstream scene manipulation applications.

### Strengths
1. The introduction of a 3D-aware memory bank reduces dependence on continuous view changes in training images, enhancing
adaptability in segmentation.
2. Comprehensive experimental comparisons demonstrate the proposed method's effectiveness across multiple tasks, validating its versatility.
3. Gaga shows strong robustness to variations in the amount of training data. maintaining high performance even when training images are significantly reduced.

### Weaknesses
1. The proposed approach, which uses Gaussian overlap and ID assignment by overlap ratio, is straightforward but highly hand-crafted, relying on manually chosen hyperparameters. While results are promising, the method offers limited innovation to the research community.
2. Although effective on indoor datasets, testing on outdoor or mixed environments would better showcase generalizability.
3. Hyperparameter Sensitivity. Key hyperparameters like percentage $x$, patch size, and overlap ratio are crucial, potentially impacting robustness, especially with distribution shifts.
4. Some sections, such as the Gaussian selection process and Fig.4(b), could be more concise and easier to follow, the figure is not clear to show the problem with pixel-wise startegy.

### Questions
1. I am interested in how the performance of Gaga will hold on outdoor datasets and how different hyperparameter settings might impact the results in these scenarios.
2. From the qualitative results in Figures 6 and 7, it appears that Gaga, especially in combination with SAM, consistently produces a black boundary around objects—a phenomenon not seen with other methods. What might be the cause of this effect?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new Gaussian splatting segmentation method by designing a mask association algorithm and lifting the created view-consistent mask to the reconstructed Gaussians.

* Technique-wise, to address the inconsistency of 2D masks across different views, this paper designs a 3D-aware memory bank that gathers Gaussians belonging to the same group. This memory bank is utilized to align 2D masks across various views.

* The paper conducts extensive experiments to demonstrate the effectiveness of the proposed method compared to the previous method, i.e., Gaussian grouping using video tracking strategies for mask association.

### Strengths
* The proposed method is simple yet effective. It introduces a new mask association algorithm that leverages the intrinsic 3D information of reconstructed Gaussians.
* The paper is well-written and easy to follow.
* The experiments have covered datasets with various settings (e.g., different 2D models, and sparse views).

### Weaknesses
 * The paper lacks sufficient comparisons with state-of-the-art methods. For example, existing methods have proposed solutions such as the linear assignment [1] or contrastive learning methods [2,3] combined with clustering algorithms to bypass the need for complex mask association preprocessing. These methods should be included as main baselines to verify the effectiveness of the proposed approach. Specifically, the paper should include a comparison with OmniSeg3D [3], given its 3D-GS implementation, which would allow for a more direct comparison. The current comparison with OmniSeg3D is insufficient, lacking detailed experimental settings and a clear explanation of how the method was adapted for the comparison.

 * Although the mask association is designed to group Gaussians from 2D pose images, the algorithm closely resembles SAM3D[4], which groups point clouds from 2D pose images. The paper does not adequately address the similarities and differences between the proposed algorithm and SAM3D. A more comprehensive discussion is needed, including a quantitative comparison to demonstrate the novelty of the proposed approach. The paper should also consider including a baseline that uses SAM3D's pre-processing results to further evaluate the contribution of the proposed method.

 * Although this paper introduces a new variant of mask association pre-processing with improved performance, there are no significant differences as it still suffers from similar limitations. Similar to video tracking, the proposed pre-processing involves many hyperparameter tuning and is sensitive to its hyperparameters, such as the percentage for finding corresponding Gaussians, overlap threshold, and image partition, as demonstrated in Tables 1, 2, and 3 in Supp. The paper should provide more analysis on how these hyperparameters affect the performance and generalization ability of the method.

 * In the proposed algorithm, using a fixed percentage to find corresponding Gaussians is too straightforward, while the optimal percentage should be dependent on the opacity properties. Hence, the preset parameter is likely to be unsuitable for new scenes and may potentially limit the generalization of the proposed method.

### Questions
Besides the following question, please refer to the weaknesses section above for my concerns.
* In Supp Figure 1, it is good that the author provides a qualitative comparison with a method using contrastive learning. However, it lacks quantitative comparisons. Besides, the comparison does not make much sense as the GARField model seems not to have converged, and the rendered RGB from GARField is much worse than that from the proposed method. Furthermore, the clustering is sensitive to parameters, but there is no detailed information provided about these settings.
* I strongly encourage the authors to compare their approach with the additional baselines mentioned above and update them in the main experiments, particularly with OmniSeg3D [3], as it provides a 3D-GS implementation, enabling fairer comparisons. To compare with OmniSeg3D, the authors may consider using the same SAM input to train OmniSeg3D, followed by a clustering algorithm for the final results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Gaga, a framework that segments open-world 3D scenes by addressing label inconsistencies in 2D masks. Using a 3D-aware memory bank, Gaga achieves multi-view consistent segmentation by associating 2D masks across views with a universal ID.

### Strengths
1. Gaga proposes a novel 3D-aware memory bank that improves multi-view consistency in 3D segmentation by leveraging spatial information from 3D Gaussians, providing an innovative alternative to video-based mask association methods.
2. Extensive experiments validate Gaga's robustness across challenging scenarios, datasets, and limited data.

### Weaknesses
1. As noted in Fig. 4a (View 2), the author selects the nearest 20% of Gaussians, considering that the background may contribute to foreground segmentation. However, in cases like Fig. 4 (View 1), where the background does not influence the foreground, this approach may lead to Gaussians from the target partition being omitted.  Please provide visual analysis on how different percentages of nearest Gaussians affect performance across various scenarios.  Specifically, the method's reliance on a fixed percentage of nearest Gaussians may not be universally optimal, potentially excluding relevant Gaussians in scenarios where the target object occupies a smaller portion of the view or is more sparsely represented by Gaussians. This could lead to incomplete or inaccurate segmentation, particularly when the density of Gaussians varies significantly across different regions of the scene or when objects exhibit complex shapes.
2.The comparison with existing methods is limited. Including additional comparisons with state-of-the-art approaches, such as Panoptic-Lifting [1] and Contrastive-Lift [2]. The lack of comparison with methods that also attempt to lift 2D segmentations to 3D limits the assessment of the proposed method's relative performance and novelty. It is crucial to demonstrate how Gaga's approach compares to other techniques that address similar challenges in 3D scene understanding.

### Questions
1. Could you provide visual examples to demonstrate that selecting the nearest 20% of Gaussians is robust across different scenarios? Additionally, is there any evidence that some Gaussians relevant to the segmentation may be excluded?
2. How your method handles cases where the ground truth segmentation is more fine-grained than their mask partitioning approach allows. For example, in the replica ground truth segmentation, the left and right panels in Figure 4b belong to different masks.  However, the mask partition merges them into a single object, which can reduce segmentation accuracy.

### Soundness
2

### Presentation
3

### Contribution
2
