## Summary
BadDet+ is a principled backdoor attack framework for object detection that unifies Region Misclassification Attack (RMA) and Object Disappearance Attack (ODA) under a single log-barrier penalty mechanism. The paper first diagnoses evaluation blind spots in existing work—specifically ASR inflation from duplicate detections and mAP misuse in ODA—then proposes a corrected evaluation protocol (including a new True Detection Rate metric), and demonstrates that its penalty-augmented training objective substantially outperforms data-poisoning-only baselines across four architectures, two datasets, and physical-world trigger transfer.

## Strengths

- **Well-motivated evaluation critique with concrete evidence.** The paper identifies genuine and previously overlooked failure modes in existing OD backdoor evaluations (e.g., BadDet RMA producing dual detections that inflate ASR, UBA producing phantom boxes that deflate mAP). Figure 1 and the preliminary investigation in Section 3 make this case convincingly with concrete examples.
- **Genuinely useful new metric.** True Detection Rate (TDR) fills a real gap: it distinguishes attacks that *replace* the original class prediction from those that merely *add* a target class alongside it. This is analogous to recovery accuracy in classification backdoor literature, but had not been applied to OD. The empirical contrast in Tables 2 and 4 (BadDet TDR@50 up to 85% vs. BadDet+ TDR@50 of ~3%) clearly validates the metric's discriminative power.
- **Unified formulation with clean technical motivation.** The log-barrier penalty (Eq. 1/2) is technically clean, architecture-agnostic across sigmoid-based (FCOS, YOLO, DINO) and softmax-based (Faster RCNN) detectors, and its behavior is intuitively interpretable. Treating background as a special target class to make ODA a special case of RMA is an elegant observation.
- **Comprehensive empirical scope.** Experiments span COCO and MTSD, four architectures (FCOS, Faster RCNN, DINO, YOLOv5), multiple trigger placements (fixed, random, physical), and a physical-world validation dataset (PTSD). The poisoning ratio sweep in Figure 3 directly addresses the "can you just increase poisoning?" question and provides a clear negative answer for baselines.
- **Honest reporting of failure cases.** The paper transparently reports that BadDet+ underperforms BadDet on YOLOv5 for RMA and in certain defense scenarios, and that synthetic-to-physical transfer, while improved, remains imperfect.

## Weaknesses

### Fatal
None.

### Major
- **Asymmetric threat model in comparisons.** BadDet+ assumes adversarial control of the *training procedure* (loss manipulation), while all compared baselines are data-poisoning-only attacks. This is not a trivial distinction: training-time loss control is meaningfully stronger than data poisoning. While the paper justifies this by demonstrating that data poisoning alone is insufficient (Figure 3, Section 5.3), the comparison framing can be misleading. The win against data-poisoning baselines is partly a consequence of having access to a stronger attack primitive. A more careful framing—or a comparison to another training-time attack from the classification backdoor literature adapted to detection—would strengthen the argument.
- **YOLOv5 anomaly is insufficiently explained.** For RMA on MTSD/PTSD (Table 4), BadDet+ underperforms BadDet on YOLOv5 in both ASR@50 and TDR@50, and the paper's explanation that "λ=0 is optimal for this architecture" essentially means the method degrades to the baseline. The paper defers full explanation to Appendix A.8 (not available), but the core question—why the penalty is counterproductive for YOLO—is left scientifically open. If this failure mode reflects a fundamental architectural incompatibility, it limits the generality claim of the unified framework.

### Minor
- **Physical-world ASR gap is underemphasized.** PTSD ODA results (Table 3) show ASR@50 for BadDet+ ranging from 59–85%, compared to the near-perfect (93–98%) MTSD results. While this is better than baselines, the ~30–40 percentage point drop for some architectures represents a substantial and practically significant synthetic-to-physical gap. The paper could be more precise about when and why this gap is large.
- **Defense evaluation scope is narrow.** Only FT and FT-SAM defenses are evaluated, with the paper explicitly deferring pruning-based, test-time, and image-space defenses to future work. This is methodologically honest but limits the completeness of the robustness claim.
- **Theoretical analysis is lean in the main body.** The main paper promises that the penalty "acts selectively within a trigger-specific feature subspace" but provides only informal intuition; the formal analysis is entirely in the appendix. The in-paper theoretical contribution reduces to a design rationale rather than a theorem.

### Trivial
- Minor figure duplication artifacts from PDF parsing.

## Nice-to-Haves
- An ablation isolating the contribution of data poisoning vs. the penalty term separately (i.e., what does BadDet+ achieve with only the penalty and no poisoning, or only poisoning with λ=0) would clarify the relative importance of each component.
- A brief investigation of the YOLOv5 failure mode in the main text would strengthen the generality claim.
- Reporting confidence intervals or standard deviation for Table 1–4 results (not just Figure 2) would aid reproducibility.

## Novel Insights
The paper's most genuinely novel observation is that the dominant failure mode in existing OD backdoors is not insufficient trigger association but rather *insufficient original-class suppression*: models learn to predict the target class while retaining a parallel prediction for the true class. This insight—that the bottleneck is a soft decision boundary rather than an encoding capacity problem—motivates the log-barrier formulation. The further insight that ODA can be reduced to RMA with background as the target class is a clean theoretical unification that had not been explicitly stated in prior work and simplifies future study of both threat models.

## Suggestions
- Explicitly report the computational overhead of the log-barrier penalty in the main paper (not only in the appendix) to help practitioners assess adoption costs.
- Include a comparison to a training-time attack from the classification backdoor literature (e.g., gradient-based loss manipulation from BadNets variants) adapted to detection, to contextualize the advantage of the proposed penalty design independent of the threat model gap.
- For PTSD, consider reporting confidence intervals across physical trigger collection conditions to better characterize the distributional gap between synthetic and physical triggers.

## Score and Decision
BadDet+ addresses a real and underexplored problem, proposes a technically clean and practically validated solution, and makes a meaningful methodological contribution by exposing evaluation blind spots in prior work. The empirical coverage is thorough and the presentation is honest. The primary concern—the threat model asymmetry in comparisons—is mitigated by the paper's own analysis, but is not fully resolved. The YOLOv5 failure case limits the universality claim. Overall, the paper meets the bar for acceptance: it brings new, relevant knowledge to the community and establishes a principled benchmark for a class of security risks with direct safety implications.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>