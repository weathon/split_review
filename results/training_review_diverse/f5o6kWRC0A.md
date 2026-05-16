Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper addresses partial-set Source-Free Unsupervised Domain Adaptation (SFUDA), where the target label set is a subset of the source label set. The authors propose a Machine Unlearning Framework that (1) generates noise samples optimized for source-only classes, (2) fine-tunes the source model to "forget" those classes while retaining target-relevant knowledge via a joint forgetting loss, and (3) adapts the model via pseudo-label self-training. The paper includes a theoretical analysis (Theorems 1–2) suggesting that removing source-only categories reduces distribution discrepancy, and experiments on Office-31 and Office-Home showing accuracy gains when the framework is added to existing SFUDA methods.

## Strengths

- **Novel integration of machine unlearning into partial-set SFUDA.** The core idea — using a forgetting procedure on noise samples to suppress source-only classes — is genuinely novel in this setting. The paper addresses a practical, understudied scenario (class mismatch in SFUDA) with a principled approach that goes beyond standard self-training heuristics.
- **Pluggable architecture yields consistent improvements across multiple backbones.** The framework improves accuracy when added to ResNet-50, TPDS, Sticker, CAiDA, and SHOT across nearly all settings on Office-31 and Office-Home (e.g., TPDS from 70.45% to 76.72% on Cₜ₆; Sticker from 73.95% to 80.55% on Cₜ₂₅). This shows the method is broadly compatible rather than tied to a single base model.
- **Substantial reduction in negative transfer samples.** The paper directly counts predictions assigned to source-only classes, and the reductions are large in several settings — e.g., on Office-31 MSDA (Table 1), negative transfer samples for ResNet-50 on Cₜ₆ drop from 312 to 23. These concrete counts support the claim that the framework alleviates its targeted failure mode.
- **Ablation and sensitivity analysis validate design choices.** The ablation (Table 4) compares only-forget, only-adapt, and the full method at increasing iterations, showing monotonic improvement. The parameter study of K (Figure 3) demonstrates a clear trade-off between pseudo-label quantity and quality, with K=7 as a reasonable operating point.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical analysis does not connect to the proposed method.** Theorems 1–2 show that *if one could retrain on source data filtered to remove source-only classes* (an oracle procedure infeasible in SFUDA), the MDD-based error bound would tighten. The paper acknowledges this gap at line 175 ("However, it is not possible to directly filter the samples from the source domain and retrain") but never bridges it to the actual forgetting procedure. There is no theoretical argument — not even a heuristic one — that training on noise samples optimizes for the same objective, bounds the error of the forgetting model, or meaningfully approximates the oracle retrained model. As a result, the theoretical section motivates a direction but does not support the specific algorithm presented. This overstates the paper's theoretical grounding.

### Minor

- **Partial-set evaluation selects extremes rather than random subsets.** On Office-31, the target classes are chosen as the 6 worst-accuracy classes or 25 best-accuracy classes (line 245). On Office-Home, similarly, 5/15 worst and 50 best. While the paper justifies this as a stress test ("if it works on extremes, it works generally"), it does not test on randomly selected subsets (e.g., 10, 15, 20 classes out of 31 or 65). The Cₜ₂₅ (25/31 classes) setting is nearly closed-set and not a challenging partial-set configuration. Random subset evaluations would strengthen the claim that the method generalizes across arbitrary class ratios.
- **No comparison against simple partial-set baselines.** The paper compares its framework added to existing SFUDA methods against those methods alone, but not against straightforward alternatives designed for class mismatch: (a) masking out source-only classes in the output layer and retraining with pseudo-labels, (b) confidence-threshold-based rejection of source-only class predictions (standard in open-set SFUDA), or (c) pruning the classifier head using a small held-out validation set. Without these, the unique benefit of the forgetting stage over simpler adaptations is unclear, especially given that the one-iteration full method improves over "only adapt" by a modest margin (~1.42% on Office-31 per the ablation study).
- **The forgetting stage's effect is not directly measured.** The paper uses negative transfer counts (predictions assigned to source-only classes) as the primary evidence that forgetting works. However, the pseudo-label filter (Eq. 8) already discards predictions of source-only classes during the adaptation stage, so the reduction could partly come from the filter itself or from adaptation dynamics independent of forgetting. The authors do not directly measure the model's confidence or prediction probability on source-only classes before and after the forgetting stage (e.g., on held-out simulated source-class samples). The "only forget" ablation does show some benefit (63.81% vs. 62.93% baseline for one iteration), but the mechanism is not isolated.
- **The forgetting stage already includes target self-training, blurring the stage distinction.** The forgetting loss (Eq. 10: *L_f = L_ce(y_t, h_s(x_t)) + α L_ce(y_N, h_s(x_N))*) includes a cross-entropy term on target pseudo-labels, which is the same type of objective used in the adaptation stage (Eq. 11). This means the forgetting stage already performs adaptation-like training. The paper does not clarify why a dedicated subsequent adaptation stage is necessary rather than simply training longer with the combined loss.
- **Unclear notation in noise generation objective.** Equation 9 uses the notation *arg min_N E_(θ)[-L(h_s, y) + λ||W_noise||]*. The subscript *(θ)* is never defined or explained — it is unclear whether this denotes expectation over model parameters or something else. This harms reproducibility.
- **Inconsistent iteration counts between datasets without justification.** Office-31 uses 5 iterations with α=5, while Office-Home uses 1 iteration with α=1 (Section 4.1). This difference is not motivated, making it unclear whether the iterative improvement is dataset-dependent or whether Office-Home results could be further improved with more iterations.
- **No statistical significance reported.** Results are reported as single runs without standard deviations, which is a concern given the small class counts in the partial-set settings and the modest margins in some comparisons.

### Trivial

- The adaptation stage loss notation (Eq. 11) writes *L_a = L_ce(x_t, h_f(x_t))* which is missing the pseudo-label argument *y_t* that appears in Eq. 10's definition.

## Nice-to-Haves

- Testing on larger-scale benchmarks (e.g., VisDA, DomainNet) would strengthen claims of practicality, though the current datasets are standard for SFUDA.
- A more thorough analysis of the noise sample generation strategy — e.g., comparing random noise vs. optimized noise, different regularization strengths — would clarify why this specific generation approach was chosen.
- Reporting per-class accuracy would verify that the reduction in negative transfer does not come at the expense of coverage of target classes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *The reviewer faults the paper for not reporting the number of optimization steps, learning rate, and batch size for noise sample generation.* → Removed per hard rule: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details."
- *The reviewer notes that Algorithm pseudocode is referenced (Alg. 1) but not present in the main text.* → Removed per hard rule: parser strips appendix content; the appendix exists in the original submission.
- *The reviewer claims "no evaluation on large-scale datasets" as a core weakness.* → Moved to Nice-to-Haves; the paper evaluates on standard benchmarks for the SFUDA setting.
- *The reviewer criticizes that "the term negative transfer is used narrowly."* → Removed; the paper clearly defines it in context as predictions assigned to source-only classes, which is a reasonable operationalization for this setting.

## Novel Insights

The most insightful observation across the reviews is that the theory–method gap is the paper's most central weakness, not its empirical results. The theorems correctly prove that an *oracle procedure* (retraining on filtered source data) would improve the MDD bound, but the paper's actual method — training on noise samples via a forgetting loss — shares no formal connection to this oracle. This means the theory section, as written, motivates a direction rather than the algorithm, and either needs to be rewritten to directly bound the forgetting model's error (e.g., via influence functions or connectivity to data removal) or repositioned as a high-level motivation rather than a direct theoretical contribution. The fact that the paper *acknowledges* the gap ("However, it is not possible to directly filter...") without bridging it is a structural weakness that limits the claimed contribution regardless of the empirical results.

## Suggestions

1. **Restructure or remove the theoretical section.** Either derive bounds that directly characterize the forgetting model (relating noise-sample training to data removal) or clearly reposition the current theorems as background motivation rather than analysis of the proposed method. The current framing overclaims theoretical support.
2. **Add random subset evaluations.** Test on at least 2–3 randomly selected partial-set configurations (e.g., 10, 15, 20 out of 31 classes) to show the method generalizes beyond extreme class selections.
3. **Include simple baselines for the partial-set scenario.** At minimum, compare against output-layer masking (removing source-only class logits and retraining) and confidence-based rejection of source-only predictions.
4. **Directly measure forgetting.** Report the model's softmax confidence on source-only classes (or on simulated source-only samples) before and after the forgetting stage to isolate the mechanism.
5. **Clarify the stage distinction.** Explain why the forgetting stage's target pseudo-label term is needed alongside the adaptation stage, and whether a single combined loss trained for more epochs would be equivalent.
6. **Report statistical significance.** Run experiments at least 3 times with mean and std, especially for settings with small margins.
7. **Clarify the E_(θ) notation** in Equation 9 and fix the missing argument in Equation 11.

## Score and Decision

**Overall assessment:** The paper introduces a genuinely novel idea (machine unlearning for partial-set SFUDA) and demonstrates empirical improvements across several backbones. However, the theoretical analysis does not support the actual method, the evaluation design uses extreme class subsets instead of random configurations, the forgetting mechanism is not directly validated, and several baseline comparisons are missing. While the core contribution is interesting and the problem is timely, the paper in its current form does not convincingly establish the superiority of the proposed framework over simpler alternatives, and the theoretical framing overclaims what is actually shown. Significant revisions — especially bridging the theory–method gap, adding random subset evaluations, and including direct forgetting measurements — would be needed for a strong paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>