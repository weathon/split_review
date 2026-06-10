Now let me write the final consolidated review.

## Summary

This paper proposes YOQO (You Only Query Once), a label-only membership inference attack that reduces the query budget from thousands (required by prior boundary attacks) to exactly one. The core idea is to craft a single query sample \(x'\) whose hard label from the victim model—predicted as the ground-truth class \(l\) or a different class—directly reveals whether the target sample was in the training set. The attack is instantiated in two variants: an online attack (higher accuracy, requires per-sample shadow model training) and an offline attack (lower accuracy, reuses pre-trained models only). Experiments across CIFAR-10, GTSRB, SVHN, Tiny-ImageNet, and tabular datasets show YOQO matching the boundary attack's accuracy while using ~20,000× fewer queries, and remaining robust against the LDL defense specifically designed for label-only attacks.

## Strengths

- **A single-query label-only attack matching the accuracy of a 20,000-query attack.** Fig. 3 and Table 1 show YOQO's online attack achieves nearly identical membership inference accuracy to the boundary attack across training set sizes from 1,500 to 10,000, while the boundary attack requires "over 20,000 queries per sample." This is the paper's headline contribution and is clearly evidenced.

- **Robustness against LDL, the only defense designed specifically for label-only MIAs.** Section 4.3 (Fig. 8) reports that LDL "can significantly reduce the inference accuracy of the boundary and gap attacks in most cases," whereas "the accuracy of our two YOQO attacks remain high and stable." The paper offers a concrete hypothesis (YOQO depends less on concrete distances, so LDL "can hardly influence the improvement area"), backed by empirical comparison across defense parameter settings.

- **Offline variant that removes per-sample training while still outperforming the gap attack.** The offline attack (Section 3.3) avoids retraining in-models per target sample, yet Section 4.1 reports it "still surpasses the gap attack by approximately 10% in terms of inference accuracy." This provides a meaningful accuracy-efficiency trade-off where the gap attack (also 1-query) cannot match.

- **Systematic ablation validating the nearest-class selection strategy.** Section 4.2 (Table 4) explicitly compares nearest-class selection versus random label for the specificity target, showing nearest-class substantially outperforms random. The paper provides a reasoned explanation grounded in softmax score behavior (the "plummet of the second biggest prediction score"), moving beyond a purely empirical claim.

- **Cross-architectural evaluation with diverse victim and shadow architectures.** Fig. 4 and Table 2 evaluate YOQO against CNN7, VGG18, ResNet18, DenseNet121, Inceptionv3, and SeResNet18 victim models using both matched and mismatched shadow architectures, including an ensemble ("Assembly") across architectures. Results show YOQO "tend[s] to have stably higher attack accuracy than the other two attacks," demonstrating robustness to architectural mismatch.

## Weaknesses

### Fatal

None. The core idea is coherent and the main empirical results are reproducible in principle.

### Major

- **The online attack's per-sample training cost is not acknowledged, making the "efficiency" claim incomplete.** Algorithm 1 (lines 1–4 of the pseudocode) requires training 16 in-models *per target sample*. For the 500-sample evaluation, this is ~8,000 model training runs. While the paper correctly claims a query budget of 1 (the API calls to the victim model), it never discusses the computational cost shift from queries to local model training. The boundary attack trains shadow models once and reuses them, paying cost in queries; YOQO's online attack pays cost in per-sample training. This is a real trade-off that the paper presents as an unqualified improvement. The title and abstract frame YOQO as "efficient" without mentioning this dimension, which is misleading in a top-venue submission.

- **The claimed detection-evasion advantage (PRADA motivation) is asserted but never tested.** The introduction (lines 20–21, Fig. 1) motivates YOQO partly by arguing that the boundary attack's high query count makes it detectable by "statistics-based defenses like PRADA," implying YOQO avoids this. However, the defense evaluation in Section 4.3 tests LDL, ADV, PPB, MemGuard, and DP-SGD—none of which are detection-based defenses. PRADA is never tested, and no evidence is provided that YOQO's single query per sample actually evades detection better in practice. If detection-evasion is part of the claimed advantage, it must be empirically supported.

- **The offline attack's MSE constraint is a heuristic without principled justification.** Section 3.3 replaces the sensitivity property (in-model classification) with an MSE proximity constraint, justified by a single sentence: "the generated \(x'\) has a higher chance to be assigned with the same label as \(x\) by any in-model" (line 125). No analysis is provided of (a) the probability of success as a function of distance, (b) whether the improvement area is even connected, or (c) what failure modes exist. The offline attack is consistently weaker (~10% below online), but it is unclear whether this is a fundamental limitation or just an engineering issue. Since the offline attack is presented as a core contribution, its theoretical basis needs to be stronger than a heuristic.

### Minor

- **No error bars, confidence intervals, or statistical significance reported.** The paper states results are "mainly the average accuracy of five repeated experiments" (line 158), but Figures 3–7 and Tables 2–4 report only point estimates without any measure of spread. Given the evaluation size is 500 samples (250 members, 250 non-members), it is impossible to assess whether differences between methods (e.g., online vs. boundary attack in Fig. 3) are statistically meaningful.

- **Improvement area concept lacks formal characterization.** Section 3.1 introduces the improvement area solely via an informal illustration (Fig. 2) and a verbal description. Key questions—under what conditions the area exists, how it depends on architecture or data dimensionality, how stochastic variation in training affects the consistency of boundary shifts across the 16 in-out pairs—are not addressed. While a full theoretical treatment may be scope for an empirical paper, the current level of analysis is thinner than the conceptual weight the improvement area carries in the paper's argument.

- **The data augmentation attack comparison is included despite operating under a different (stronger) threat model.** The paper correctly notes (line 44–45) that this attack "requires the strong assumption that the adversary knows the augmentation strategies for training the victim model, which may not be practical." Yet it is still plotted as a baseline in Fig. 3 and Table 2. While the paper is transparent about the caveat, including it in head-to-head comparisons is uninformative and should be moved to a separate discussion or removed.

### Trivial

- **Pseudocode in Algorithm 1 has ambiguous variable naming.** Line 8 uses `l'` (singular) while line 4 defines `l_i'` (indexed). The condition `l_i ≠ l` on line 4 is also notated unclearly (intended as `k ≠ l`). The intended logic is clear from the main text, but the algorithm is not self-contained.

## Nice-to-Haves

- A formal bound on the size or existence conditions of the improvement area (even for simple classifier families like linear models or nearest neighbors) would substantially ground the core concept.
- Reporting inference accuracy on imbalanced splits (e.g., 95% non-members, 5% members) would clarify whether the reported balanced-split accuracy translates to meaningful privacy risk in realistic settings.
- Evaluating against PRADA or a similar query-statistics-based detection defense would complete the claimed detection-evasion advantage.

## Removed Points

These points were considered but removed after verification against the paper:

- **"Ratio formulation in Eq. 3 is mathematically ill-formed"**: Element-wise division of softmax vectors is a valid vector operation; the formulation is unusual but not ill-formed. Removed as factually incorrect/overstated.
- **"No comparison with recent label-only attacks"**: The harsh critic did not name specific missing attacks. Without concrete missing baselines, this is a knowledge gap in the review, not a paper flaw. Removed.
- **"Accuracy on a balanced split does not support headline claims"**: The paper transparently explains (line 160) why TPR@lowFPR is not applicable to YOQO's binary-output setting. This is an honest methodological choice, not a flaw. Removed.
- **"Boundary attack implementation details insufficient"**: The paper provides reasonable implementation details (16 pairs of shadow models, threshold selection procedure). Standard for a conference paper. Removed.
- **"Evaluation protocol does not support headline claims" (general framing)**: Overly broad; specific sub-points (error bars, imbalanced splits) are retained as minor/nice-to-have above, but the sweeping dismissal is unwarranted. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the method or results that the authors themselves did not present.

## Suggestions

1. Add a paragraph in Section 3.2 or at the end of Section 4 honestly comparing the *total* attack cost: report GPU-hours or approximate training time for the online attack's 16 per-sample model trainings alongside the query budget in Table 1.
2. Either add PRADA evaluation to Section 4.3, or remove the PRADA discussion (Fig. 1, line 20–21) from the introduction to avoid claiming an unevidenced advantage.
3. Add error bars (standard deviation or confidence intervals) to all reported accuracy figures, derived from the five repeated experiments already conducted.
4. Provide at least a heuristic analysis of the offline attack's MSE constraint—e.g., for a given L2 distance δ, what fraction of in-models assign the target label \(l\) to \(x'\)? This can be evaluated empirically on the shadow models the authors already have.
5. Move the data augmentation attack comparison out of the primary results figures to a supplementary discussion, given the acknowledged threat model mismatch.

## Score and Decision

This paper proposes a genuinely novel idea—crafting a single query sample for label-only membership inference—and supports it with reasonably extensive experiments. The core result (matching a 20,000-query attack with exactly 1 query) is compelling, and the LDL robustness finding is a non-obvious empirical contribution. However, the paper has three significant gaps: (1) the per-sample training cost of the online attack is never honestly accounted for, making the "efficiency" framing one-sided; (2) the detection-evasion motivation (PRADA) is asserted but never tested; (3) the offline attack lacks principled justification. These prevent acceptance at a top venue in the current form. The paper would need a major revision addressing the computational cost accounting, completing the PRADA evaluation (or removing the claim), and providing error bars.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>