## Human Reviewer 1

### Summary
The paper claims to be the first to apply a pruning-based approach to knowledge distillation that removes the use of a regressor to overcome the parameter mismatch between the teacher and student networks. To support this, the paper claims that they theoretically demonstrate the limitations of using a regressor. Furthermore, the paper claims that the proposed method outperforms existing limited approaches through experiments conducted on small yet basic datasets such as CIFAR-100 and TinyImageNet.

### Strengths
- The paper adopts a pruning method to eliminate the need for a regressor in knowledge distillation between homogeneous networks with different dimensions or layers.

- The authors use mutual information to convincingly address the limitations of conventional approaches.

- The paper is simple to read and get the contribution of the paper.

### Weaknesses
- The proposed regressor-free method using pruning only when the number of layers is the same and only the number of channels differs. It does not provide a solution for cases where the layer counts differ, and it results in limiting its applicability. Furthermore, it cannot address knowledge distillation between heterogeneous networks. 

- Although knowledge distillation is a relatively young field, there already exist numerous studies. The related work section in this paper is insufficiently comprehensive, and the contributions are not clearly distinguished from similar prior works, such as:\
[1] O’Neill et al., Deep Neural Compression via Concurrent Pruning and Self-Distillation, arXiv:2109.15014, 2021\
[2] Aghli et al., Combining Weight Pruning and Knowledge Distillation for CNN Compression, CVPR Workshop 2021\
[3] Muralidharan et al., Compact Language Models via Pruning and Knowledge Distillation, arXiv:2407.14679, 2024

- The performance comparison with previous methods is quite poor. Comparing only with LD, FitNet, and conventional KD does not ensure fairness. The paper should provide the SOTA comparison tables because the main claim of this paper is the traditional regressor-based KD has the limitation and the proposed regressor-free method does not. 

- Although the paper claims to demonstrate its superiority through extensive experiments, the evaluation is limited to small-scale toy datasets such as CIFAR-100 and TinyImageNet. These datasets are too small, and CIFAR-100, in particular, is known to produce high variation across runs, making it difficult to ensure objective results. Therefore, more comprehensive experiments using larger datasets such as ImageNet are generally required to validate the proposed method.

### Questions
Now I have no question on this paper.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper proposes a regressor-free intermediate layer distillation method that uses teacher pruning to address dimensional mismatches between teacher and student models. The authors argue that traditional regressor-based approaches lead to indirect and suboptimal knowledge transfer. Through probing experiments, they demonstrate the limitations of regressors and propose pruning the teacher's intermediate layers to align dimensions directly. Extensive experiments on ResNet, VGG, and ShuffleNetV2 across CIFAR-100 and TinyImageNet show that their method often outperforms conventional intermediate layer distillation, sometimes even exceeding the teacher's performance.

### Strengths
- The method is simple and applicable across multiple architectures.
- Experimental results show consistent improvements over regressor-based ILD.
- The paper includes ablation studies on loss functions and alpha values.

### Weaknesses
**Novelty and Positioning**: The core idea of pruning the teacher for distillation has been explored in Park & No (ECCV 2022). The authors do not clearly distinguish their method beyond the use of intermediate (rather than logit) distillation.

**Theoretical Justification**: The mutual information argument in Section 3.3 is superficial and does not convincingly explain why pruning helps or why mutual information is the right measure for knowledge transfer.

**Experimental Gaps**:
1. No analysis of why VGG on TinyImageNet suffers a significant performance drop after pruning.
2. No explanation for why ShuffleNetV2 is "difficult" for distillation.
3. The retraining cost of the pruned teacher is not accounted for in comparisons.

**Overstated Claims**: The authors claim "comprehensive theoretical analysis" but provide only a brief and non-rigorous inequality. They also claim to "consistently outperform" but simultaneously state they are not targeting SOTA, which is contradictory.

### Questions
**Theoretical and Conceptual Concerns**
1. The mutual information-based justification is superficial and lacks rigor in connecting to the actual knowledge transfer process.
2. Mutual information is not adequately justified as a meaningful measure for distillation quality.
3. Theoretical analysis is generally weak and fails to provide a solid foundation for the proposed method.

**Novelty and Positioning**
1. The distinction from prior work, especially Park & No (ECCV 2022), is unclear. Both use teacher pruning before distillation.
2. It is ambiguous whether the core contribution lies only in applying pruning to intermediate layers rather than logits.
3. The related work section does not sufficiently differentiate the method from existing pruning-for-distillation approaches.

**Experimental Analysis and Unexplained Observations**
1. Key experimental phenomena are left unanalyzed: (1) Significant performance drop in VGG on TinyImageNet after pruning. (2) Difficulty in distilling ShuffleNetV2 effectively.
2. The computational cost of pruning and retraining the teacher is not evaluated or compared to baselines (e.g., training time, FLOPs).
3. Experimental gains, while consistent, are not always substantial or thoroughly interpreted.

**Clarity and Consistency of Claims**
1. Some claims are overstated or inconsistent, such as: (1) Stating the goal is not to surpass SOTA, while claiming to “consistently outperform” conventional methods. (2) Describing the theoretical analysis as “comprehensive” when it is minimal.
2. The scope of contributions is not clearly defined relative to the experimental results.

**Methodological and Evaluation Gaps**
1. No analysis is provided on why certain architectures (e.g., VGG, ShuffleNetV2) behave differently under the proposed method.
2. Broader applicability is not tested on modern architectures such as Vision Transformers (ViTs).
3. The impact of architectural elements like skip connections or channel shuffling in ShuffleNetV2 is not discussed.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
The authors proposed a regressor-free intermediate layer distillation method. They prune the teacher's target layer (L1 channels) to match the student's, with a retaining process. The experiments show that it is effective on small CNN benchmarks. However, the core idea overlaps with “prune-then-distill” [1] and pruning teacher width to enable ILD as in InDistill [2]. Thus, the novelty is incremental.

[1] Park, J., No, A. “Prune Your Model Before Distill It.” ECCV 2022 / arXiv:2109.14960.  
[2] Sarridis, I. et al. “InDistill: Information Flow-Preserving Knowledge Distillation for Model Compression.” WACV 2025 / arXiv:2205.10003.

### Strengths
1. The core idea of pruning for feature distillation shall work. The process is straightforward and appears to be easily reproducible.
2. The motivation is well-supported by various tests and visualizations.
3. The experiments are consistent with the motivation, and the implementation details are clearly presented.

### Weaknesses
1. The core idea overlaps with “prune-then-distill” [1] and pruning teacher width to enable ILD as in InDistill [2].
2. The current pruning scheme lacks thorough development, and conducting an ablation study on this aspect would be beneficial.
3. As a distillation method, the proposed approach requires retraining the pruned teacher model on the same dataset. This results in high computational costs, potentially rendering it impractical in many scenarios. Additionally, this contradicts the authors' assertion that "the performance gap between the pruned teacher and the original teacher remains negligible."
4. The assumption that "γ can be regarded as negligibly small" does not hold. Consequently, Eq. 6 cannot support the conclusion that the performance of the proposed method is lower-bounded by that of traditional regressor-based ILD methods. Meanwhile, should it be I(f_t, f_s) instead in Eq. 5?
5. All experiments are limited to CIFAR-100 and TinyImageNet datasets, with no results provided for ImageNet-1K or CIFAR-10. This limitation hinders the ability to evaluate practical impact and robustness at realistic resolutions effectively. Furthermore, many state-of-the-art methods have not been included in the comparisons.

[1] Park, J., No, A. “Prune Your Model Before Distill It.” ECCV 2022 / arXiv:2109.14960.  
[2] Sarridis, I. et al. “InDistill: Information Flow-Preserving Knowledge Distillation for Model Compression.” WACV 2025 / arXiv:2205.10003.

### Questions
1. Please discuss the differences between "prune-then-distill" [1] and InDistill [2].
2. The motivation and assumptions require further investigation.

[1] Park, J., No, A. “Prune Your Model Before Distill It.” ECCV 2022 / arXiv:2109.14960.  
[2] Sarridis, I. et al. “InDistill: Information Flow-Preserving Knowledge Distillation for Model Compression.” WACV 2025 / arXiv:2205.10003.

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