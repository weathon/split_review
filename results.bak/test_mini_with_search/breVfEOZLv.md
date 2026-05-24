Now I have sufficient calibration data. Let me compose the final review.

## Summary

This paper applies the weak-to-strong distillation idea (Burns et al., 2023) to vision models, replacing the fixed hyperparameter α in AugConf with a data-dependent weighting function β(x) = exp(CE(f(x), f̂(x))) / (exp(CE(f(x), f̂(x))) + exp(CE(f(x), f̂_w(x)))). The proposed AdaptConf loss dynamically balances the weak teacher's soft labels against the strong student's own hard labels. Experiments span image classification, few-shot learning, transfer learning, and noisy-label learning across architectures (ResNet, WRN, VGG, ShuffleNet, MobileNet, ViT).

## Strengths

1. **Broad empirical scope across tasks and architectures.** The paper evaluates on four distinct settings (classification, few-shot, transfer, noisy labels) with multiple teacher–student pairs (same-architecture, cross-architecture, and ViT-based). This breadth supports the claim that weak-to-strong distillation can be applied broadly in vision.

2. **Non-trivial gains in the no-ground-truth setting.** Table 4b and Table 7 show that when only weak teacher soft labels are available (a practically important scenario), AdaptConf yields meaningful improvements — e.g., +2.15% on ImageNet transfer without ground truth, where the margin over AugConf is also clear (AugConf +1.47% vs. AdaptConf +2.15%).

3. **Empirical validation of the adaptive weighting mechanism.** Figure 3 tracks β(x) over training and shows that as training progresses, β converges toward 0.5 for more samples, indicating that the student increasingly aligns with the teacher's correct predictions. This provides interpretable evidence that the mechanism behaves as designed.

4. **Lower sensitivity to hyperparameter tuning.** Figure 2 shows that AdaptConf's performance fluctuates less across temperature values than AugConf's performance fluctuates across α values, and its average outcome is higher. This practical robustness advantage is clearly documented.

## Weaknesses

### Fatal
None.

### Major
1. **Incremental contribution relative to AugConf (Burns et al., 2023).** The core innovation — replacing a fixed scalar α with a data-dependent β(x) defined as a softmax over two cross-entropy values — is a straightforward modification. The paper offers no theoretical motivation for why this specific functional form should be superior, and the reported improvements over a well-tuned AugConf are modest (typically 0.5–2%, and often at the lower end of this range). This limits the significance of the contribution.

2. **No error bars or statistical significance tests.** All results are reported as averages of 3 trials without standard deviations or confidence intervals. Given that the claimed advantages over AugConf are often small (e.g., 0.3–0.5% in several settings), it is impossible to determine whether these are reliable signals or statistical noise. This undermines the paper's central claim of "consistently superior performance."

3. **Conflation of weak-to-strong with self-distillation in few-shot experiments.** In Section 4.2.2 (line 141), the paper states: "In the meta-learning stage, we employ weights from different training stages of the same model as the teacher." This is self-distillation / temporal ensembling, not weak-to-strong in the paper's own definition (a weaker-capacity model supervising a stronger one). This weakens the conceptual coherence of the evaluation.

4. **Ad-hoc formulation of β(x) without clear justification.** The function β(x) uses CE(f(x), f̂_w(x)) where f̂_w(x) is the weak model's *hard* label. Using hard labels discards distributional information that soft labels carry. The paper does not explain why this specific form is chosen over simpler alternatives (e.g., softmax confidence of the weak teacher, or a learned gating network), nor why hard labels from the weak model are used in one term while soft labels from the weak model are used in the other loss term.

### Minor
1. **Missing comparison to straightforward self-training baselines.** In settings without ground truth (Table 4b, 7), the paper compares only against AugConf and strong-to-weak KD methods. Simpler alternatives such as confidence-thresholded self-training (Lee et al., 2013) are not included, even though they would be natural competitors in the no-ground-truth scenario.

2. **Abstract overclaims scope.** The abstract states the approach "exceeds the performance of fine-tuning strong models on full datasets," but this claim is only directly tested in the transfer learning setting (Table 7), not across all tasks. The statement is too broad.

3. **Limited analysis of failure cases or negative results.** The paper does not discuss settings where AdaptConf might underperform relative to AugConf or simple baselines. For example, on CIFAR-10 noisy labels (Table 8), "all methods except ours negatively impact the model" — this is presented as a success but the margin is tiny and deserves more nuanced discussion.

4. **Weak teacher is always from the same domain.** All experiments use teachers and students trained on the same downstream dataset. Using a teacher from a different dataset or a zero-shot model would test the method's generality more rigorously.

### Trivial
None.

## Nice-to-Haves
- Comparing β(x) against alternative adaptive weighting schemes (learned gating, confidence-thresholded weighting) to isolate whether the specific functional form matters.
- Reporting confidence intervals over more runs (5–10) to establish statistical significance.
- Testing on more realistic weak-to-strong pairs (e.g., small ResNet-18 teacher → large ViT student).

## Removed Points
- *"Tables presented as images"* — This is a PDF parser artifact; the original submission would have proper tables.
- *"Weak-to-strong definition using ImageNet-pretrained models not relevant to modern foundation models"* — This is a scope choice the paper is entitled to make.
- *"No code at submission"* — The paper states code will be released; this is standard practice for a submission.
- *"Strong-to-weak KD baselines are straw men"* — Including these baselines provides useful context about the paradigm shift; the paper correctly identifies the main competitor as AugConf.
- *"Generic strengths about addressing important problems"* — Removed per filtering rules as they lack concrete specificity to this paper.

## Novel Insights
The reviews surface a tension that the paper does not fully confront: the adaptive weighting mechanism's advantage over a fixed-weight baseline is systematically positive but too small to be convincing without statistical validation. The SAAD anchor (4.50) had a similar structure (sample-wise adaptive weighting) and was rejected for comparable reasons (limited novelty, missing baselines). A genuinely novel insight would require either (a) a clear theoretical argument for why the specific β(x) form is optimal, (b) much larger empirical margins that render significance tests unnecessary, or (c) enabling a capability that fixed-weight approaches categorically cannot achieve. None of these are present.

## Suggestions
1. Provide error bars or confidence intervals over at least 5 runs for the main comparison (AdaptConf vs. AugConf) to establish that the improvement is statistically significant.
2. Add a comparison to simple self-training with confidence thresholding (Lee et al., 2013) in the no-ground-truth setting — this is a natural and strong baseline the paper currently omits.
3. Clarify the scope: either remove the weak-to-strong framing from the few-shot self-distillation experiments or reposition them as a separate (but related) setting.
4. Include a sensitivity analysis comparing β(x) against alternative adaptive weighting functions (e.g., softmax confidence of the weak teacher, or a simple learned scalar) to justify the specific functional choice.

## Score and Decision

**Calibration anchors:**

*Round 1 bracket (3–10):*
- TAND (3.00, R1): Theoretical KD fix with similar incremental-novelty issue. Current paper has broader experiments but similar magnitude of contribution.
- SAAD (4.50, R1): Sample-wise adaptive weighting for adversarial distillation. Rejected. Comparable incremental novelty, but SAAD had a diagnostic analysis the current paper lacks.
- DTO-KD (6.67, R1): Principled multi-objective KD optimization. Accepted (Oral). Stronger theory and more convincing gains. Current paper is clearly below this.
- K-Gen (4.40, R1): Data-free KD for high-resolution. Rejected. Similar level of contribution breadth.

*Round 2 narrowing (3.5–6.0):*
- Intra-Class Contrastive KD (3.50, R2): Incremental modification to teacher training. Withdrawn. Current paper has broader evaluation and is slightly stronger.
- CUD (4.50, R2): Calibrated uncertainty for KD. Rejected. Similar incremental-novelty pattern.
- Dataset Distillation Memorization (5.33, R2): Accepted (Poster). Had a more novel finding and rigorous controlled experiments. Current paper is weaker.
- Early Layer Readouts KD (3.50, R2): Similar incremental contribution. Current paper is somewhat stronger empirically.

*Round 1 bracket:* Paper plausibly sits between 3.5 and 5.5, based on comparison to TAND (3.00) below and DTO-KD (6.67) above.

*Narrowing:* Comparing to SAAD (4.50, rejected) — the current paper is slightly weaker due to the lack of diagnostic analysis and the conflated few-shot setting. Comparing to CUD (4.50, rejected) — similar. Comparing to Intra-Class Contrastive KD (3.50) — the current paper is stronger due to broader evaluation and more relevant baselines.

*Final placement:* The paper is closest to the SAAD/CUD cluster (4.0–4.5). Among these, SAAD had clearer diagnostic motivation for its weighting; CUD had a theoretical framing (even if incomplete). The current paper has less analytical depth but broader task coverage. A score of **4.0** reflects that this is a solid but incremental empirical contribution with genuine breadth, held back by the lack of statistical rigor, the conceptual inconsistency in the few-shot setting, and the ad-hoc nature of the core formulation.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>