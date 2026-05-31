## Human Reviewer 1

### Summary
This manuscript addresses a long-standing issue in semi-supervised LiDAR semantic segmentation: the error propagation and confirmation bias from noisy pseudo-labels. The authors propose REPL, a pseudo-label refinement framework that integrates a teacher-student model with a novel refiner module. 

The refiner detects unreliable pseudo-labels using confidence-based teacher–student agreement, then corrects them via masked reconstruction inspired by masked autoencoders. The framework is complemented by theoretical analysis showing conditions under which refinement improves pseudo-label quality, as well as a training strategy with random masking, negative learning, and mixed labeled/unlabeled scenes to strengthen supervision. 

Empirical results on nuScenes-lidarseg and SemanticKITTI benchmarks demonstrate consistent improvements over state-of-the-art semi-supervised methods across various label ratios.

### Strengths
(+) Tackling noisy pseudo-labels is highly relevant, as confirmation bias remains a fundamental bottleneck in semi-supervised LiDAR semantic segmentation. This manuscript articulates this motivation clearly and positions REPL against existing post-hoc strategies. The idea of refining pseudo-labels before training (rather than adjusting them afterward via weighting or filtering) provides a clean, conceptually different direction. The masked reconstruction approach is well-aligned with recent advances in self-supervised learning.

(+) Theoretical justification: The inclusion of theoretical results (Propositions 1 and 2) formalizes why refinement is easier than generating labels from scratch and under what conditions it yields improvements. This adds depth beyond empirical validation.

(+) REPL achieves SOTA on both nuScenes-lidarseg and SemanticKITTI, with notable gains especially at low label ratios (e.g., +2.0 mIoU over IT2 on average). The ablation studies and sensitivity analyses further support the design choices.

### Weaknesses
(-) While the refinement-based perspective is novel, many components (teacher-student EMA, confidence thresholds, masked reconstruction) are individually adapted from prior works. The contribution lies more in integration than in fundamentally new architectures.

(-) The reliability detection relies on simple agreement-based thresholds. Although results show effectiveness, this component may be brittle in challenging cases (e.g., rare classes, long-range sparse points). More adaptive or learned error-detection strategies could strengthen the approach.

(-) Evaluation comprehensiveness: Please consider comparing FRNet [Xu, et al.], LarseMix++ [Kong, et al.], and Lim3D [Li, et al.] for a more comprehensive evaluation on the semi-supervised LiDAR segmentation benchmark. Additionally, there are several self-supervised LiDAR segmentation methods that are evaluated on the same benchmark; please consider including those as well, such as SLidR [Sautier, et al.], Seal [Liu, et al.], and SuperFlow [Xu, et al.].

References:
- FRNet [Xu, et al.] FRNet: Frustum-Range Networks for Scalable LiDAR Segmentation. TIP, 2025.
- LarseMix++ [Kong, et al.] Multi-Modal Data-Efficient 3D Scene Understanding for Autonomous Driving. TPAMI, 2025.
- Lim3D [Li, et al.] Less is More: Reducing Task and Model Complexity for 3D Point Cloud Semantic Segmentation. CVPR, 2023.
- SLidR [Sautier, et al.] Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. CVPR, 2022.
- Seal [Liu, et al.] Segment Any Point Cloud Sequences by Distilling Vision Foundation Models. NeurIPS, 2023.
- SuperFlow [Xu, et al.] 4D Contrastive Superflows are Dense 3D Representation Learners. ECCV, 2024.

---

**Minor Suggestions**

(-) Clarify computational overhead: The refiner introduces an additional network and losses—reporting training/inference cost overhead would be valuable for practitioners.

(-) Proposition 2 is well-explained, but its assumptions (e.g., independence of correction/error rates) could be elaborated for readers less familiar with information-theoretic analysis.

(-) While some qualitative comparisons are shown, additional side-by-side visualizations across challenging categories could better demonstrate where refinement helps most.

(-) Some sections could be slightly condensed for readability, especially in the theoretical analysis.

### Questions
The manuscript tackles a critical challenge in semi-supervised LiDAR semantic segmentation and offers a conceptually fresh perspective—refining pseudo-labels instead of merely reweighting or filtering them. The integration with masked reconstruction and theoretical grounding strengthens its contributions, and empirical results are solid.

That said, the core novelty is more in formulation and integration rather than new architectural design, and the evaluation scope is somewhat narrow. Nevertheless, the work is well-motivated, cleanly executed, and empirically convincing, making it a meaningful step forward for the community. With additional efforts in addressing the main weaknesses and minor suggestions (as detailed above), the manuscript could have a strong impact.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper proposes REPL, a framework for semi-supervised LiDAR semantic segmentation. The main idea is to directly refine pseudo-labels rather than simply discarding low-confidence ones or reweighting them. 

A teacher-student setup produces pseudo-labels, and a refiner detects unreliable voxels (via teacher–student confidence agreement) and reconstructs them using a masked autoencoder-inspired method. The authors also provide a theoretical analysis, showing when refinement improves label quality. 

Experiments on nuScenes and SemanticKITTI benchmarks demonstrate strong performance, setting a new state of the art across different label ratios.

### Strengths
- Instead of post-hoc filtering or reweighting, REPL improves pseudo-labels at their source, directly tackling confirmation bias. The entropy-based task difficulty and the ζ condition provide a principled reason why refinement is beneficial. This is relatively rare in semi-supervised segmentation papers.

- New SOTA on nuScenes and SemanticKITTI, with robust gains especially in the low-label regime (e.g., +4.7 mIoU over supervised-only baseline at 1% labeled data). Ablation studies show the importance of each loss (Lrsup, Lrunl, Lrmix), and sensitivity experiments (error mask quality, random masking) demonstrate the design choices matter.

- The paper is overall well-written. The figures (especially Fig. 1 and qualitative results in Fig. 3–9) make the method understandable, showing how refinement corrects pseudo-label noise.

### Weaknesses
- Teacher–student EMA, agreement-based confidence, and masked reconstruction are all known individually. The contribution is more in how they are combined and applied to LiDAR pseudo-label refinement.

- The confidence percentile rule is simple but might not be optimal in cases of class imbalance or rare categories (e.g., pedestrians, bicycles). Results could be brittle under distribution shifts.

- Evaluation is limited to nuScenes and SemanticKITTI. More diverse benchmarks (Waymo, SynLiDAR, Robo3D, or other datasets) would strengthen claims of generality.

- While qualitative improvements are shown, the paper doesn’t deeply discuss where REPL still fails—e.g., does it help small-object categories or long-range sparse regions?

### Questions
1. What is the additional training and inference cost of running the refiner? Is REPL practical for large-scale deployment?

2. How does REPL perform on rare classes or long-tail categories in SemanticKITTI (e.g., “motorcyclist,” “other-ground”)? Does the refinement help there or mostly on dominant classes?

3. Would a learned error detector (instead of heuristic agreement) further improve the error mask? Or is the current approach already close to optimal?

4. Can the refinement process be extended to sequential settings (e.g., 4D spatio-temporal LiDAR), where temporal consistency might aid error correction?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper presents REPL, a new framework for semi-supervised learning in LiDAR semantic segmentation. The core contribution is a shift from adjusting pseudo-label usage to actively improving their quality. The method identifies unreliable pseudo-labels using a heuristic and then corrects them using a masked reconstruction mechanism. The authors demonstrate state-of-the-art performance on the nuScenes-lidarseg and SemanticKITTI benchmarks.

### Strengths
1. The paper is well-written, logically structured, and easy to follow.

2. The analysis of the trade-off between error correction ($q_j$) and error introduction demonstrates the refiner's effectiveness .

3. The paper provides a rich set of ablation studies (e.g., Table 2-5) that thoroughly validate the contributions of the individual components, such as the refiner losses and the masking strategies.

### Weaknesses
1. The paper claims that pseudo-label quality improves during training due to the refiner. However, in teacher–student frameworks, the teacher naturally improves over time thanks to EMA updates. It is thus hard to isolate how much of the improvement is due to the refiner versus the inherent dynamics of self-training. A comparison between EMA-only and EMA+refiner over time would strengthen the claim.

2. The refiner is based on masked reconstruction, which is generative by nature. It is unclear whether the gains stem from genuine pseudo-label correction or simply from the introduction of stronger feature representations via MAE. Ablations that replace MAE with another feature extractor (e.g., contrastive learning backbone) or apply MAE without pseudo-label refinement would help clarify this distinction.

3. The 'unreliable voxel identification' heuristic relies on several parameters (e.g., confidence percentile $\kappa$). This raises a question about potential hyperparameter sensitivity. The paper would be strengthened by an analysis of how performance varies with these parameters, as it is currently challenging to gauge the tuning effort that might be required for new datasets.

4. The framework introduces a third network (the refiner), which presumably adds computational and memory overhead. The paper does not currently include an analysis of training time or memory usage relative to baseline methods. Including this would help readers better evaluate the practical performance-vs-efficiency trade-off.

5. The evaluation could be further strengthened by including additional benchmarks. For instance, key prior work like LaserMix also reported results on the ScribbleKITTI dataset. An evaluation on this would provide a more comprehensive picture of the method's robustness.

### Questions
na

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4