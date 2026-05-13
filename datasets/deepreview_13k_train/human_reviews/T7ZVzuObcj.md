# Interpretable point cloud classification using multiple instance learning

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
3D image analysis is crucial in fields such as autonomous driving and biomedical research. However, existing 3D point cloud classification models lack interpretability, limiting trust and usability in safety-critical applications. To address this, we propose PointMIL, an inherently locally interpretable point cloud classifier using Multiple Instance Learning (MIL). PointMIL offers local interpretability, providing fine-grained point-specific explanations to point-based models without the need for \textit{post-hoc} methods, addressing the limitations of global or imprecise interpretability approaches. We applied PointMIL to four popular point cloud classifiers, PointNet, DGCNN, CurveNet, PointMLP, and PointNeXt, and proposed a transformer-based backbone to extract high-quality point-specific features. PointMIL made these models inherently interpretable while increasing predictive performance on standard benchmarks (ModelNet40, ShapeNetPart) and achieving state-of-the-art mACC ($97.3\%$) and F1 ($97.5\%$) on the IntrA biomedical data set, and another dataset of biological cells. To our knowledge, this is the first work to apply MIL to interpretable point cloud classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces PointMIL, an inherently locally interpretable point cloud classifier using Multiple Instance Learning (MIL). It addresses a gap in existing classification methods, which either employ post-hoc interpretability techniques or focus on global interpretability. PointMIL comprises a feature encoder, implemented using either 3D transformers, DGCNN, or PointNet, to capture per-point features. A MIL pooling layer provides interpretability, with several types of MIL pooling methods explored, including Instance, Attention, Additive, and Conjunctive pooling.  A contextual prior is also injected into attention mechanism to learn local information. Experiments are conducted on medical dataset IntrA and general 3D object dataset ModelNet40.

### Strengths
1. The paper is well-written and easy to follow.
2. It claims to be the first work to achieve locally interpretable point cloud classification on a per-point basis.
3. The visual results are compelling, highlighting important regions for classification. Quantitative results on multiple classification benchmarks, such as IntrA and ModelNet40, and part segmentation benchmarks, including IntrA and ShapeNetPart, demonstrate performance improvements over baselines.

### Weaknesses
The technical contribution appears somewhat limited, as it primarily involves combining various typical point cloud encoders with existing MIL pooling methods for point cloud classification. I would have expected a deeper exploration of this combination. For example, were any modifications made to the MIL pooling methods to better adapt them to point cloud data? What specific challenges were encountered and addressed when applying MIL to this domain? Providing more insights into these aspects could help strengthen the contribution and highlight the distinctiveness of the approach.

Furthermore, in Tables 4, 5, and 6 in Appendix A.1, the paper presents varying performance across different MIL pooling methods. However, there is a lack of analysis explaining why certain methods perform better than others, and how these insights could guide the selection or adaptation of pooling methods in future work. Simply presenting the empirical results without such analysis misses an opportunity to make the work more insightful and inspiring.

The backbones used for evaluation are somewhat limited, as more recent and widely adopted models, such as Point Transformer (ICCV 2021) and sparse convolutional architectures, are not included. Evaluating PointMIL with these modern architectures would provide a more comprehensive comparison. I would appreciate it if the authors could discuss how PointMIL might be adapted to work with these newer backbones.  Additionally, a side-by-side comparison of the interpretability outputs for the same representative examples using different backbones would be valuable to determine if they highlight the same local regions of interest.

### Questions
1. In Lines 195-197, the paper claims to use five MIL pooling methods, but only four are listed: Instance, Attention, Additive, and Conjunctive. Could the authors please clarify whether a fifth pooling method was intended and omitted, or if this is a typo that should be corrected?
2.  In Table 2,  PointNet is reported to achieve 86.0 mACC, whereas the original paper cites 86.2 mACC. Could the authors please verify this discrepancy and explain? I wonder if this difference is due to variations in the implementation, experimental setup, or evaluation criteria.
3. Could the authors provide visual results for segmentation similar to Figures 2-5? Specifically, it would be interesting to include side-by-side comparisons of classification and segmentation interpretability outputs for a the same representative examples.

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
This paper introduces PointMIL, the first framework to apply MIL to point cloud classification. PointMIL provides fine-grained point-specific interpretability without post-hoc techniques.

### Strengths
1.	This paper is well-written, and the organization is great.
2.	The motivation is clear enough.

### Weaknesses
1.  The backbones and compared methods are limited. There are lots of methods that have been proposed for point cloud classification and segmentation. It is recommended to compare with them, including Point-MAE and PointTransformer V3.
2.  “Group features through k-nearest neighbours”, “Learned relative positional encoding”, and “Attention on the augmented features” are also widely used in point cloud processing, including PoinTr, Point-BERT, or DGCNN. It is recommended to move these parts into appendix and focus on your interpretation. 
3.  The logic in L90-L94 is puzzling. “Post-hoc or inherently interpretable” and “local or global approaches” could be organized better.
4.  The citation in L100 should be (Tan & Kotthaus, 2022). The remaining part should also be carefully checked.
5.  It is claimed that “most local interpretability methods for point cloud classification are post-hoc” and “no one has yet offered an inherently locally interpretable model for point cloud classification” seems conflict.
6.  Local and global features are widely studied in point cloud classification. Why your local approach is effective than others?
7.  MIL pooling has been widely used in 2D images. Please clarify the main difference between these methods. And it is also recommend to exploit the specific design for point cloud.
8.  The main contribution of this paper is the interpretation. However, the discussion about the interpretation is limited and the discussion about the network design has a great portion.
9.  The performance gain on ModelNet40 and ShapeNetPart is marginal. Moreover, more newly proposed backbones should be included as your backbone.

### Questions
1.	It is claimed that “most local interpretability methods for point cloud classification are post-hoc” and “no one has yet offered an inherently locally interpretable model for point cloud classification” seems conflict.
2.	Local and global features are widely studied in point cloud classification. Why your local approach is effective than others?
3.	MIL pooling has been widely used in 2D images. Please clarify the main difference between these methods. And it is also recommend to exploit the specific design for point cloud.
4.	The main contribution of this paper is the interpretation. However, the discussion about the interpretation is limited and the discussion about the network design has a great portion.
5.	The performance gain on ModelNet40 and ShapeNetPart is marginal. Moreover, more newly proposed backbones should be included as your backbone.

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
5

### Summary
This paper proposes a method for generating point-level importance in point cloud classification, aiming to interpret the contribution of each point to the classification outcome. A modified Transformer is introduced to extract point-level features, with MIL pooling applied to determine each point's importance. The paper presents a strong motivation and is well-organized.

### Strengths
The motivation is innovative, focusing on the interpretability of point cloud models and aiming to address the issue of poor interpretability in existing models.

### Weaknesses
1. The authors aim to propose a general interpretability method; however, they add a Transformer-based feature extractor to existing models as an additional modification to the backbone network. This modification can be seen as an alteration to the backbone, which may impact the original performance of the point cloud network. Consequently, conducting interpretability analysis on this modified version may not align with the original motivation.

2. The novelty is limited: the authors' contributions primarily include (1) the feature extractor and (2) MIL pooling. However, the core iead of the feature extractor is merely a straightforward combination of existing Transformer and DGCNN approaches, lacking significant originality. In the MIL pooling, existing ideas are directly applied without any improvements tailored to the inherent characteristics of point cloud data. These factors restrict the paper's novelty, as it largely reflects a simple combination and adaptation of existing methods.

3. The performance improvements are likely attributed mainly to the additional feature extraction network.

### Questions
Although the authors provide visualizations of points deemed important for classification in the figures, these points are derived from the final pooling output. Why are these highlighted red points considered more important—just because they have higher importance scores? The current conclusions remain insufficiently convincing. Are there alternative methods that could offer supplementary validation? One possible approach could involve removing the red points and observing a significant accuracy drop, while removing the gray points leads to no substantial accuracy decrease. However, this is an intuitive idea and may not hold in actual experiments.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces multiple instance learning to provide local interpretability for point cloud classification models. Experiments are conducted on several popular point cloud classification models and classification benchmarks, demonstrating the effectiveness of the proposed method.

### Strengths
This paper is the first to introduce multiple instance learning for interpretable learning in the 3D domain. It can be integrated as a simple module into existing point cloud classification models, effectively enhancing classification performance while also improving interpretability.

### Weaknesses
1.The point cloud classification models applied in PointMIL appear to be relatively outdated, as more advanced models such as PointNeXt and PointMLP, as well as more classic models like PointNet++, have not been included in the experiments. The absence of these models limits the assessment of PointMIL's generalizability and performance against state-of-the-art techniques. Specifically, the paper does not explore how PointMIL would perform with architectures that utilize more sophisticated feature extraction methods or attention mechanisms, which are common in modern point cloud models.

2.The practicality of PointMIL in real-world applications remains questionable, as it lacks experiments on real datasets such as ScanObjectNN, or robustness tests against noise, rotation, and other transformations. The current experiments are limited to relatively clean datasets, which do not fully represent the challenges of real-world scenarios where point clouds are often noisy, incomplete, or subject to various transformations. This limits the conclusions that can be drawn about the method's practical utility.

3.There are some minor errors in the details: $\textbf{(a)}$. it seems that $\hat{y}$ in Equation 8 is not defined. $\textbf{(b)}$. there is an error in Table 4 of the appendix

### Questions
1.Is the performance comparison on classification tasks fair? If I understand correctly, PointMIL eliminates downsampling to achieve point-level predictions, whereas the other methods compared, such as PointNet++, still employ downsampling. The authors should consider the impact of downsampling on performance.

2.I recommend that the authors include experimental results for PointMIL on ScanObjectNN and test the interpretability on more advanced point cloud models such as PointNeXt and PointMLP.

3.Is PointMIL also applicable to scene-level tasks, such as scene segmentation that requires generating point-level predictions? This could effectively demonstrate the applicability of PointMIL.


4. I hope the authors can provide a detailed explanation of the results, for example, why $\textbf{Additive}$ and $\textbf{Conjunctive}$ achieve better results compared to other MIL pooling methods in Figure 2. Such an exploration would be beneficial for understanding how to choose MIL pooling methods under different circumstances.

### Soundness
2

### Presentation
3

### Contribution
2
