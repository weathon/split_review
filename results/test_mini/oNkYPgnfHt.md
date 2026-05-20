Now I have a thorough understanding of the paper and all reviews. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write this now.

Quick check on a few more things I want to verify:

1. The claim about "k is never specified for detection experiments" - Looking at Eq. (1) which uses k for detection, and line 84 which says k=1 for generalization. For detection, k is never explicitly stated. This is a minor oversight.

2. The claim about CBM (ft) finetuning - the paper says "CBM (ft) was finetuned for 10 epochs on CUB and 5 epochs on the Parity MNIST variants" (line 185). So the reviewer's claim that it's not specified is wrong - I need to remove that criticism.

3. The claim about "learning to intervene" - this is a title nitpick. The method does involve the model improving from experience (learning in a broader sense). I'll keep it as a minor point.

4. Detection baseline concern - Let me reconsider. The reviewer says CBMM claims to detect *bottleneck* mistakes. The paper says: "cbmms estimate model errors only based on the bottleneck network" while softmax "uses information from the end of the model." The paper's claim is that bottleneck-specific detection is more suitable for interventions. The softmax baseline is a standard baseline for error detection. This comparison is valid as a practical comparison but doesn't isolate whether the advantage comes from using the bottleneck encoding or from the mistake-memory mechanism specifically. I think this is a valid concern but not a fatal one - the paper provides evidence that CBMM works better than softmax for the practical task of selecting samples for intervention.

Actually, I realize the softmax baseline is detecting *overall* model errors (not just bottleneck errors). CBMM is detecting bottleneck errors specifically. The paper's claim is that CBMM detects errors that are more suitable for intervention correction. The results in Table 3 show CBMM achieves higher NRI on the full set than softmax, which supports this claim. The comparison is practically meaningful even if a bottleneck-encoding baseline would provide additional insight.

Let me finalize my assessment and score.Now I have all the information I need. Let me construct the final review.

## Summary

This paper introduces Concept Bottleneck Memory Models (CBMMs), which augment standard CBMs with a two-fold memory (mistake memory + intervention memory) to enable reuse of past human interventions and detection of future bottleneck errors. The key insight is that once a human corrects a CBM's concept predictions, that correction holds information that can be applied to similar future inputs, overcoming the one-time-use limitation of standard CBM interventions. Experiments across CUB, confounded/unbalanced MNIST variants, and SVHN distribution-shift settings show that CBMMs improve concept and class accuracy by reusing interventions, and outperform softmax-based error detection particularly under confounding.

## Strengths

1. **Well-motivated and practically relevant idea.** The observation that CBM interventions are currently single-use is correct, and reusing them via a memory module is a natural, clean extension. The paper fills a genuine gap: no prior CBM work systematically explored generalizing interventions across inputs.

2. **Strong results on challenging scenarios.** On confounded Parity C-MNIST, CBMM improves identified-instance class accuracy from 20.1% (CBM) to 85.9% (Table 1). On the distribution-shift setting (MNIST→SVHN), class accuracy on identified instances jumps from 39.9% to 60.8% (Table 4). These are substantial gains in realistic failure modes where standard CBMs collapse.

3. **Detection specifically effective under confounding.** On confounded CUB (conf) and Parity C-MNIST, CBMM achieves AUROC of 85.1 and 83.4 respectively vs. softmax's 77.4 and 65.7 (Table 2), with similar advantages in AUPR. This shows CBMM's bottleneck-focused detection provides genuine value when standard uncertainty methods struggle.

4. **Flexible and lightweight.** The memory module requires no model retraining, works with any CBM architecture that exposes bottleneck encodings, and Fig. 3/Appendix show it remains effective even with only 25% of available intervention data.

## Weaknesses

### Major

1. **Missing ablation: what does the two-fold structure add over simpler retrieval?** The intervention generalization experiments (Table 1) compare against a finetuned CBM and vanilla CBM, but not against a simpler baseline that just stores intervened samples and retrieves the nearest-neighbor intervention (without the mistake memory, threshold t_d, or the two-fold structure). This makes it impossible to attribute CBMM's gains to its specific two-fold design rather than to any form of exemplar-based retrieval. Similarly, the detection evaluation lacks a baseline that uses bottleneck encodings directly (e.g., a logistic regression or KNN trained on encodings to predict concept-level correctness). The only non-random detection baseline is softmax on the predictor output, which measures a different quantity (overall model errors vs. bottleneck-specific errors). Adding these ablations is essential to isolate what the mistake-memory mechanism specifically contributes.

2. **Statistical significance is not assessed.** The variances in Table 3 overlap considerably (e.g., CBMM full-set NRI on CUB: 75.5±4.5 vs. Softmax: 70.1±3.1; on C-MNIST: 89.7±6.1 vs. 87.3±0.8). Without confidence intervals or hypothesis tests, the reader cannot determine which differences are real. This is important because the paper's core practical claim is that CBMM better targets interventions.

### Minor

1. **$t_d$ selection on the training set is unusual and potentially problematic.** Line 105 states "The selection of $t_d$ is done on the training set," while the memory is populated from the validation set. Tuning a threshold that controls generalization behavior on the training set risks overfitting. The paper mentions parameters are tuned on training and validation sets (line 156), but the specific statement about $t_d$ contradicts standard practice. A clarification is needed.

2. **CBM (ft) baseline on Parity C-MNIST substantially outperforms CBMM (88.1 vs. 74.9 class accuracy).** The paper acknowledges this gap (lines 190-191) and discusses tradeoffs (cost, interpretability), but the 13-point deficit on the most confounded setting is notable. The claim that CBMM is "on par" with finetuning should be qualified more precisely.

3. **The value of $k$ for detection experiments is unspecified.** Equation (1) defines detection using $k$ nearest neighbors, but the paper never states what $k$ is used for detection tasks. For generalization, $k=1$ is explicitly stated (line 84). This makes the detection procedure underdetermined.

4. **The title "Learning to Intervene on Concept Bottlenecks" slightly overstates the method.** The memory mechanism is retrieval-based, not learnable in the parametric sense. While the paper mentions differentiable memory instantiations as future work (line 292), the current system stores and retrieves rather than learns.

### Trivial

None.

## Nice-to-Haves

- A t-SNE/UMAP visualization of bottleneck encodings showing mistake clusters and whether interventions transfer across semantically similar images would build useful intuition.
- Simulating noisy human feedback (e.g., 90% correct) and measuring degradation in CBMM's detection and generalization would strengthen practical relevance.
- Reporting false positive/negative rates for detection (beyond AUROC/AUPR) and for intervention generalization would provide a clearer operational picture.

## Removed Points

*(These points are flagged to be removed; treat them with caution.)*

- **Detection baselines fundamentally flawed claim (Critical Issue 1 from Harsh Critic):** The reviewer argues there is a "structural" flaw because the only non-random baseline (softmax) measures a different quantity. However, CBMM's detection is designed to detect bottleneck-specific errors, and the comparison against softmax (which detects overall errors) is a practically meaningful comparison: it asks whether bottleneck-focused detection is better for intervention targeting. The paper shows CBMM wins on confounded data where softmax fails. While a bottleneck-encoding baseline would strengthen the analysis, the existing comparison is valid and not "fundamentally flawed." **Moved to Major Weakness #1 (missing ablation) rather than treated as a separate fatal flaw.**

- **"Learning to intervene" criticism (from Section-by-Section):** The reviewer claims "no learning occurs" because the method stores and retrieves. The paper explicitly notes the memory can be differentiable (line 62) and the system improves from experience — a reasonable use of "learn" in a broad sense. This is a terminology nitpick.

- **CBM (ft) finetuning details unspecified claim:** The reviewer says finetuning steps are not specified. In fact, the paper states "CBM (ft) was finetuned for 10 epochs on CUB and 5 epochs on the Parity MNIST variants" (line 185). This claim is factually incorrect.

- **Missing discussion of memory poisoning:** The paper discusses incorrect human feedback and references relevant work (lines 265-266). While it does not run robustness experiments, it does acknowledge the issue.

- **Missing ICBM/ECTP quantitative comparison claim:** The paper's scope is about intervention *reuse*, not concept selection. The paper correctly scopes this out and notes it as complementary (Fig. 2).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the authors themselves do not already acknowledge or discuss.

## Suggestions

1. **Add a simple nearest-neighbor retrieval baseline** for intervention generalization (store all intervened samples, retrieve closest intervention via bottleneck-encoding distance, no mistake memory, no threshold). This directly isolates the value of the two-fold design.

2. **Add a bottleneck-encoding baseline for detection** (e.g., logistic regression trained on bottleneck encodings to predict whether concept prediction is correct). This tests whether the mistake-memory mechanism adds anything beyond standard encoder-based detectors.

3. **Clarify why $t_d$ is selected on the training set** and justify that this does not lead to threshold overfitting, or change the procedure to use held-out validation data.

4. **Report confidence intervals or p-values** for the key comparisons in Tables 2 and 3 where variances overlap substantially.

5. **State the value of $k$ used in detection experiments** explicitly (matching the clarity provided for generalization).

## Score and Decision

I now calibrate against the retrieved anchors.

**Anchor comparison:**

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tcsZt9ZNKD.md` (Sparse Autoencoders) | 8.20 | Much stronger paper — rigorous scaling laws, thorough evaluation. Current paper is not at this level. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/L9U5MJJleF.md` (CB Generative Models) | 6.00 | Similar quality. Both propose clean extensions to CBMs with solid experiments. CB Gen Models has broader coverage (3 model families); current paper has more challenging evaluation scenarios. Comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/R3Tf7LDdX4.md` (MCNN) | 6.00 | Similar quality. Both use memory-augmented architectures. MCNN has theoretical guarantees; current paper has more diverse experiments with confounding/shift. Comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Q9Z0c1Rb5i.md` (SupCBM) | 5.00 | Weaker paper — more incremental idea (hierarchical concept sets) with some clarity issues. Current paper has stronger novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5Aem9XFZ0t.md` (Zero-shot CBMs) | 4.83 | Weaker — limited evaluation scope. Current paper is more thorough. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kTjEPEy96Q.md` (Evaluating Unsupervised CBMs) | 3.00 | Significantly weaker — conceptual fallacy in the evaluation framework. Current paper's contribution is sound. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/a8wjeqTZ9C.md` (CBM Label Noise) | 3.75 | Weaker — very incremental (applying SAM to CBMs under noise). Current paper is more novel. |

The paper's core idea is well-motivated and the experiments cover genuinely challenging scenarios where standard CBMs fail. However, the missing ablations (simple retrieval baseline, bottleneck-encoding detection baseline) and lack of statistical significance assessment leave the precise attribution of gains somewhat unclear. These are fixable in revision but weaken the current submission relative to the strongest 6.0 papers. I place this paper between the mid-5 and low-6 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>