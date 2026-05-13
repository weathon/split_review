# Anchors Aweigh! Sail for Optimal Unified Multi-Modal Representations

- Decision: Reject
- Scores: 5, 8, 3, 6, 8, 5

## Abstract
Multimodal learning plays a crucial role in enabling machine learning models to fuse and utilize diverse data sources, such as text, images, and audio, to support a variety of downstream tasks. A unified representation across various modalities is particularly important for improving efficiency and performance. Recent binding methods, such as ImageBind~\citep{girdhar2023imagebind}, typically use a fixed anchor modality to align multimodal data in the anchor modal embedding space. In this paper, we mathematically analyze the \textit{fixed anchor binding methods} and uncover notable limitations: (1) over-reliance on the choice of the anchor modality, (2) failure to capture intra-modal information, and (3) failure to account for inter-modal correlation among non-anchored modalities. To address these limitations, we propose CentroBind, a simple yet powerful approach that eliminates the need for a fixed anchor; instead, it employs dynamically adjustable centroid-based anchors generated from all available modalities, resulting in a balanced and rich representation space.
We theoretically demonstrate that our method captures three crucial properties of multimodal learning: intra-modal learning, inter-modal learning, and multimodal alignment, while also constructing a robust unified representation across all modalities. Our experiments on both synthetic and real-world datasets demonstrate the superiority of the proposed method, showing that dynamic anchor methods outperform all fixed anchor binding methods as the former captures more nuanced multimodal interactions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores limitations in current Fixed-Anchor-Bind (FABIND) methods used for multi-modal learning, which commonly align various modalities using a fixed anchor like images or text.  These methods struggle to capture essential intra-modal and shared information among non-anchored modalities.  To address these shortcomings, the authors propose a novel approach, CentroBind, which dynamically computes centroid-based anchors from all modalities, enhancing representation alignment.  Their experimental results demonstrate that CentroBind outperforms traditional FABIND methods on synthetic and real-world datasets.

### Strengths
1、Innovative Approach: The introduction of CentroBind addresses key limitations in existing multi-modal learning methods by using dynamic anchors, offering a fresh perspective and improving multi-modal alignment.


2、Theoretical Rigor: The paper provides a comprehensive mathematical analysis to support the efficacy of CentroBind, ensuring a solid foundation for the proposed approach.

### Weaknesses
1、Robustness of anchor generation: CentroBind takes the centroids of all modalities to generate anchors, how does this approach perform in the face of modalities with significantly different information densities? For example, if some modalities contain more or less useful information than others, does the centroid bias towards these modalities, resulting in an imbalance in the representation space? Specifically, if one modality is dominated by noise, will the centroid be unduly influenced, leading to a suboptimal anchor? Furthermore, how does the method handle scenarios where some modalities are sparse or have missing data, which could skew the centroid calculation?

2、Effect of different modal weights: All modes are treated as equally weighted when calculating the centroid anchor. Have methods been investigated for assigning different weights to each modality to better capture inter-modality differences? Does this weight assignment improve or optimize the overall performance of the model? For instance, could a learned weighting scheme, perhaps based on modality-specific variances or mutual information with other modalities, lead to better performance than a uniform weighting? The paper should explore how sensitive the method is to different weighting strategies.

3、CentroBind aims to maximize both intra-and inter-modality information, but is there an information bottleneck effect (e.g. information may be compressed in high-dimensional embedding Spaces)? How does this bottleneck effect affect the representation power of the model, especially in tasks where multimodal interactions are very complex? Have experiments been conducted to verify the balance between information maximization and representation compactness? It would be beneficial to analyze the dimensionality of the embedding space and its impact on performance, particularly in scenarios with high modality complexity.

4、Does CentroBind suffer from potential optimization pitfalls when multiple modalities are strongly correlated or there is obvious synergy information between modalities? For example, when two modes are highly dependent, is the centroid overly pulled towards a particular mode? In this case, how can the optimization process be adjusted or improved to capture real multimodal relationships? The paper should investigate whether the method can effectively disentangle redundant information from highly correlated modalities.

5、Boundary conditions for theoretical analysis: The theoretical analysis in the paper explores the advantages of CentroBind, but are there certain boundary conditions or assumptions under which CentroBind might lose its advantage? For example, does this approach still work when the data is unevenly distributed or the amount of data is severely imbalanced? It is important to understand the limitations of the theoretical analysis and whether the derived bounds hold under various real-world conditions.

6、Loss function Optimization: CentroBind's loss function combines multiple InfoNCE loss terms, but does this design affect the convergence speed or stability of the model? Has the effect of different temperature parameters or weight of the loss term been explored to optimize the convergence of the model? The paper should provide more details on the optimization process and the sensitivity of the method to different hyperparameter settings.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel method to eliminate the need for an anchor in multimodal representation. Such method is based on centroid anchors computed from the modalities. The method faces a real problem in the largest part of current multimodal models that mainly rely on text anchors. The proposed method is novel and of interest to the community.

### Strengths
1) The paper faces the problem of misalignment among non-anchor modalities, which is a real problem in multimodal alignment.
2) The mathematical solutions and proofs to the problem, as well as the mutual information perspective, make the paper valuable.
3) Although simple, the experiments confirm the theoretical intuitions.
4) The paper is well-written and well-presented.

### Weaknesses
1) A tSNE visualization of the learned space could be strengthen the claims.
2) Maybe more detailed experiments with existing embedding models could be conducted to generalize the results. But the paper is fine also as it is now. :)


Minor comments:

1) Supplementary materials should have been submitted together with the paper.
2) The Saxon genitive should be avoided in scientific writing, although I know that both ChatGPT and Grammarly suggest to use it. However, I suggest the authors to remove all the Saxon genitives from the paper.

### Questions
1) Could the authors better explain how they dynamically adjust the centroids? I mean, after an iteration, or step by step also inside the iteration?
2) How would this model scale up to multiple (more than three) modalities?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper removes the need for selecting a fixed anchor modality in Fixed-Anchor-Bind (FABIND) and uses the centroid of all modality representations as an anchor representation. The paper study their method theoretically, showing that it captures intra- and inter information and shows empirical improvements over various synthetic and real-world datasets.

### Strengths
The paper addresses challenges with Fixed-Anchor Binding (FABIND) and introduces a centroid-based anchor approach as an effective alternative. This method, Centro BIND, demonstrates superior performance over FABIND across both synthetic and real-world datasets in retrieval and classification tasks, which is likely to capture the interest of the community. Additionally, the paper is concise, well-written, and easy to follow.

### Weaknesses
The paper addresses challenges with Fixed-Anchor Binding (FABIND) and introduces a centroid-based anchor approach as an effective alternative. This method, Centro BIND, demonstrates superior performance over FABIND across both synthetic and real-world datasets in retrieval and classification tasks, which is likely to capture the interest of the community. Additionally, the paper is concise, well-written, and easy to follow.

*   **Limited Baseline Comparison**: While the limitations of fixed anchors are well-articulated, additional baselines would help to further justify the centroid-based approach. For example, sampling a modality as an anchor randomly or choosing an anchor based on the minimum or maximum similarity score could provide useful comparisons to strengthen the motivation for centroid-based anchoring.

*   **Positioning Among Related Works**: Although the paper’s primary focus is to demonstrate improvement over FABIND, it would benefit from a broader positioning among recent multimodal works [1, 2, 3]. Several studies have explored inter- and intra-modality information; a comparative discussion here would contextualize the contributions more effectively. Including a simple baseline of early or late fusion across modalities for both synthetic and real-world datasets would be insightful. Additionally, it’s unclear why Centro BIND does not utilize all modalities in Table 2 for a more comprehensive comparison.

*   **Comparison with Individual Modalities**: Since the work emphasizes intra-modality information, a comparison with individual modality baselines and an ensemble of modalities, especially in Table 2 for evaluation, is essential. This would underscore how effectively Centro BIND leverages intra-modality information compared to single-modality models.

*   **Clarification on FABIND Setup**: Could the authors clarify if FABIND uses pre-trained encoders in the experiments, or are the encoders randomly initialized? This detail would help to understand the experimental setup more clearly.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
**Summary of this paper:**

This work introduces a new task: CentroBind, a novel approach in multimodal learning that addresses limitations found in fixed-anchor binding methods(FABIND). FABIND typically uses a single anchor modality to align representations across various modalities. However, this method has critical drawbacks, such as dependence on the anchor choice and lack of intra- and inter-modal information sharing. CentroBind proposes to replace fixed anchors with dynamic centroid-based anchors derived from all available modalities, creating a more balanced representation space. Theoretical analysis and experiments on synthetic and real-world datasets demonstrate that CentroBind enhances multimodal alignment and performs better in tasks requiring nuanced multimodal interactions.

**Strengths:** 

The paper is well-organized and written. The paper proposes an innovative solution to the limitations inherent in fixed-anchor binding methods by introducing CentroBind, which leverages centroid-based dynamic anchors. CentroBind's design is rooted in solid theoretical analysis, addressing crucial aspects of multimodal learning, including intra-modal, inter-modal, and multimodal alignment. The paper conducted extensive experiments on both synthetic and real-world datasets, and the results confirmed that CentroBind outperformed FABIND. The research content is innovative and holds potential application value.

**Weakness:**

As for method. The theoretical advantages of dynamic centroid-based anchors are well-articulated, the practical implementation details are somewhat limited.As for the experimental results. (1) I believe that the comparative experiments and ablation studies are not sufficiently. The paper only compares CentroBind and FABIND methods, lacking additional comparisons with other recent multi-modal alignment frameworks, which leads me to question the validity of this comparison. (2) There could be more exploration into how CentroBind performs under different data distributions and noise levels, which could provide further insights into its robustness.

**Weakness Summary.** 

CentroBind's scalability and practicality for large datasets require further consideration. In addition, broadening experimental comparisons and analysis would help address potential limitations and position the method within the broader multimodal research.

### Strengths
Refer to the summary

### Weaknesses
As for method. The theoretical advantages of dynamic centroid-based anchors are well-articulated, the practical implementation details are somewhat limited.As for the experimental results. (1) I believe that the comparative experiments and ablation studies are not sufficiently. The paper only compares CentroBind and FABIND methods, lacking additional comparisons with other recent multi-modal alignment frameworks, which leads me to question the validity of this comparison. (2) There could be more exploration into how CentroBind performs under different data distributions and noise levels, which could provide further insights into its robustness.

**Weakness Summary.**

CentroBind's scalability and practicality for large datasets require further consideration. In addition, broadening experimental comparisons and analysis would help address potential limitations and position the method within the broader multimodal research.

### Questions
Refer to the summary

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addressed the issues related to fixing a particular modality as an anchor in multi-modal representations. They argue that the anchor should not be fixed since the semantic relationships among the non-anchors may be lost and also since intra-modality information  may not be captured if the anchor is fixed. Instead, they propose choosing centroids of positive augmentation pairs among multiple modalities. The paper presents theoretical analyses demonstrating the drawbacks of fixed anchors and the advantages of dynamic anchors. Experimental results show the superiority of the proposed strategy on a synthetic dataset and a multimodal dataset for cross-modal retrieval and, sarcasm and speaker classification.

### Strengths
1. A strong theoretical paper that shows that fixing an image or text as an anchor for multimodal representation loses information contained in other modalities that are not selected as anchors.
2. The proposed strategy of using dynamic anchors is also supported theoretically by deriving a lower bound on CentroBind's objective function and minimizing the objective function.
3. Very good interpretations based on theoretical analysis of why FABind is insufficient and how CentroBind overcomes the former's limitations.

### Weaknesses
There are no major weaknesses to speak of.
1. To me, the claim of a closer representation to Huh et al's "Platonic representation" is not  quite evident. I tend to believe the authors are also not very positive about this aspect from their statement in line 361 that the representation is "likely closer" to the Platonic representation.
2. This is not a weakness of the paper per se. Audio, video and text are the usual modalities that are discussed in multimodal representation. It would be interesting to study datasets with additional modalities such as VIDIMU: Multimodal video and IMU kinematic dataset on daily life activities using affordable devices (https://zenodo.org/record/8210563), which has inertial sensors.

### Questions
1. Line 220: The authors may clarify why equation (4) shows that FABind does not guarantee shared information fbetwen non-anchor modalities.
2. Are there any constraints on the batch B from which the anchor embeddings are derived?
3. It is not clear which part of the analysis specifically shows that using a fixed anchor affects the representativeness of all modalities (P4).
4. How would acc(All) perform in Fig 2 (a)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes CentroBind, which employs a dynamically adjustable centroid-based anchors generated from all available modalities. The experiments are conducted on synthetic and real-world datasets.

### Strengths
1. The paper is easy-to-follow.
2. The paper provides sufficient analysis of the proposed method.

### Weaknesses
1. CentroBind computes the average of the inputs in the batch as the anchors. However, means are sensitive to outliers. When there are outliers in a batch, the performance will be influenced. Particularly, when the batch size is small, it will also influence the performance.
2. The experiments are not sufficient. There are many unified multimodal representation methods. Why do the authors only compare FABind? More recent baselines should be included.
3. I consider this paper to be incremental work, as it makes only very minor changes to FABind.
4. There are no visualizations in the experiments. Features before and after CentroBind should be visualized to better demonstrate its effectiveness.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
