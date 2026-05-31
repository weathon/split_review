## Human Reviewer 1

### Summary
(1) Exploits the hypothesis that the number of FN is significantly higher than the number of FP. We attempt to improve the model’s performance by introducing intended FP, conditioned by model performance, into the ground truth masks for enhanced training, thereby penalizing the model for missing out class pixels in smaller regions or some structures entirely. The results validate that this strategy tends to bring an overall improvement in the model performance.
(2) Proved effective across diverse datasets, demonstrating improved performance on both binary and multi-class segmentation tasks. Its versatility makes it applicable to a wide range of imaging scenarios

### Strengths
(1) Authors evaluated their method on difference tasks and datasets.

(2) Quantitative and qualitative results were provided to help readers understand the benefits of the proposed methods.

### Weaknesses
(1) The overall contribution is low. The proposed method did not improve the segmentation performance significantly. In contrast, the proposed method demonstrated a similar performance with U-Net (67.46 vs. 67.09 and 80.64 vs 80.01). Thus, if this method was proposed with other more advanced methods instead of U-Net, it would not outperform them.

(2) The overall novelty is low. Authors only proposed a Miss-aware Mask Modulation which included a simple structure. Based on the segmentation results reported in different tasks, this proposed module did not demonstrate significant improvements over existing methods.

(3) The reproducibility is low. Some implementation details are missing, and authors did not provide these details.

(4) Author did not provide computational complexity of the proposed method. Authors added a new module into the baseline network, such as U-Net, so it is necessary to show the increased parameters and FLOPs due to the incorporation of this module.

(5) The evaluation is insufficient. Authors only evaluated their method on convolutional neural networks, but they did not evaluate it on Vision transformer-based segmentation models.

### Questions
(1) The overall contribution is low. The proposed method did not improve the segmentation performance significantly. In contrast, the proposed method demonstrated a similar performance with U-Net (67.46 vs. 67.09 and 80.64 vs 80.01). Thus, if this method was proposed with other more advanced methods instead of U-Net, it would not outperform them.

(2) The overall novelty is low. Authors only proposed a Miss-aware Mask Modulation which included a simple structure. Based on the segmentation results reported in different tasks, this proposed module did not demonstrate significant improvements over existing methods.

(3) The reproducibility is low. Some implementation details are missing, and authors did not provide these details.

(4) Author did not provide computational complexity of the proposed method. Authors added a new module into the baseline network, such as U-Net, so it is necessary to show the increased parameters and FLOPs due to the incorporation of this module.

(5) The evaluation is insufficient. Authors only evaluated their method on convolutional neural networks, but they did not evaluate it on Vision transformer-based segmentation models.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This work is motivated by the observation that, for medical segmentation tasks, false positives and false negatives are usually not well balanced, resulting in a disproportionate emphasis on one of them.
 The authors proposed a supervised mask modulation (SMM) method to address this issue. The proposed method is architecture-agnostic. SMM improves performance by introducing intentional false positives, under the hypothesis that, for certain tasks, the false negative rate (FNR) is higher than the false positive rate (FPR) due to the small segmentation region (class imbalance).
 The proposed method was tested on four datasets with two variants.

### Strengths
1. The motivation of this work is clearly articulated, and I appreciate the effort to address the observed issues, especially in the medical domain, where further research is certainly needed.
2. The authors run multiple seeds for performance evaluation and conduct proper statistical analyses. This aspect is often overlooked in machine learning research, even though it should not be. I appreciate the authors’ efforts in ensuring the reproducibility of this work.
3. The presentation is clear and easy to follow, with figures that are both intuitive and informative.

### Weaknesses
1. The proposed solution appears to be quite hard-coded. To my understanding, the core idea of the method is to force the model to learn a larger mask through dilation. This raises a concern: what if the class imbalance is reversed, i.e., there are more samples of class = 1 than class = 0? In that case, one would likely need to invert the strategy by shrinking the mask instead. This makes the proposed method heavily hard-coded. It would be more interesting if the authors could propose an adaptive mechanism that automatically accounts for the degree and direction of class imbalance. In this regard, I believe there is substantial room for improvement.

2. The structure of the paper could also be improved. It seems that there are two main components of related work or background information that deserve emphasis. The first concerns evidence from prior work showing that the false negative rate (FNR) tends to exceed the false positive rate (FPR), and the second concerns previous efforts to address this issue and how the proposed method differs from them. Currently, the first part appears in Section 3, and the second is in the first paragraph of Section 2. Both aspects are also briefly mentioned in the introduction but without any citations. I recommend that the authors: (1) cite relevant literature whenever the issue or existing solutions are discussed, and (2) consolidate these contents into a dedicated section with clear subsections.

3. Finally, there is a lack of discussion regarding the results. For example, in Figure 4, it is unclear what the yellow arrow represents and how it should be interpreted. The caption is not sufficiently intuitive. I would suggest saving some space from, for instance, Figure 3 (which could be made smaller or even omitted) and using it to include more paragraphs analyzing and discussing the results in greater depth.

### Questions
1. There’s no weighting inbetween the 2 loss terms in algorithm 2? 
2. Isn’t that the Loss of ESL, is: $L_{ESL} = - \frac{TP+FP}{N+FP+FN}$? I am not sure why this could help the better balance between FP and FN as they have the same weights (weights = 1.0 for both of them). Also do you have any intuition behind this design?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper introduces Supervised Mask Modulation (SMM), a training-time, architecture-agnostic approach for image segmentation that aims to reduce false negatives while controlling false positives. The core idea (MAMM) dilates predicted FN regions and merges them into the ground truth masks during training. Two variants are presented: SMMv1 (with an elevated-sensitivity loss) and SMMv2 (with an adaptive threshold guided by recall trends). Experiments span several datasets (BoMBR, DRIVE, Cracks, Drone) with multiple metrics.

### Strengths
1. Problem motivation is clear and relevant, especially in FN-sensitive domains (e.g., medical, defects). 

2. The method integrates at training time without architectural changes, which is easy to adopt. 

3. Experiments cover multiple datasets and metrics.

4. The paper is generally readable.

### Weaknesses
1. Novelty: The mechanism—dilating FN regions and augmenting labels—resembles label modulation/cost-sensitive training; ESL aligns with recall-weighted objectives. Without a clearer theoretical account or principled links to established losses, the contribution feels incremental for ICLR.

2. Baselines: Key baselines are missing (Tversky, Focal), and evaluations focus on U-Net (and SegNet in the appendix) without modern backbones (e.g., DeepLabv3+, transformer-based segmenters), limiting the architecture-agnostic claim.

3. Dataset: The datasets are small and 2D-only, which limits assessment of scalability and modern applicability. If a 2D focus is intentional, the paper should justify this choice and discuss applicability to volumetric/3D tasks.

4. Result: The main text makes a strong claim that the approach has been "validated on a range of benchmark datasets, consistently outperforming state-of-the-art methods," yet Appendix A shows most improvements are not statistically significant. The authors' own summary acknowledges that "while not all improvements reach statistical significance, there are multiple encouraging trends in favor of our approach."

### Questions
1. Why restrict evaluation to 2D tasks when many target domains use volumetric/3D data? Can SMM be extended to volumetric segmentation, and what limitations would arise?

2. How should readers reconcile the strong claim in the main text with Appendix A showing limited significance (e.g., BoMBR/DRIVE: all p>0.05; Cracks: clDice/JSI; Drone: FPR)? Can you report effect sizes and confidence intervals?

3. How does SMM compare with tuned Tversky and Focal losses? Where does SMM provide unique benefits?

4. How do you ensure modulated masks remain bounded and do not overfit to early noise? How are overlaps handled in multi-class settings in practice?

5. What is the training time and memory overhead relative to the baseline pipeline?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4