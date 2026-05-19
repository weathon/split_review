- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 6, 6, 6, 3
Now I have verified all claims against the paper. Let me compose the final review.

## Summary

This paper identifies a realistic but previously unstudied threat model — defending against multiple simultaneous backdoor attacks — and shows that existing single-attack defenses fail in this setting. It then proposes BaDLoss, a defense that detects poisoned examples by comparing their full per-example loss trajectories to those of a small set of guaranteed-clean probe examples. BaDLoss achieves substantially lower attack success rates (7.98% on CIFAR-10, 10.29% on GTSRB) in the multi-attack setting than existing defenses (all above 60%), establishing both a meaningful problem and a functional first defense.

## Strengths

1. **First systematic evaluation of multiple simultaneous backdoor attacks.** The paper demonstrates (Section 3.3, Figure 2) that multiple attacks can be learned simultaneously in a single model without substantially degrading clean accuracy, validating the importance of this previously neglected threat model.

2. **BaDLoss achieves dramatically lower attack success rates than prior defenses in the multi-attack setting.** In the multi-attack setting (Section 5.1, Figure 4), BaDLoss attains average ASR of 7.98% on CIFAR-10 and 10.29% on GTSRB, while the best existing defense (Spectral Signatures) achieves 64.48% and 84.28% respectively. This is concrete evidence that the method delivers on its core claim.

3. **A principled detection method using full loss trajectories.** Section 4 identifies that different backdoor attacks can be learned faster or slower than clean examples (Figure 3). BaDLoss's use of entire loss trajectories avoids the restrictive inductive bias of prior methods (e.g., ABL's assumption that backdoors are always learned faster), which is directly supported by the empirical trajectories shown.

4. **Cross-dataset generalization without retuning.** Hyperparameters are tuned on CIFAR-10 and applied directly to GTSRB without further adjustment (Section 3, line 50). The strong GTSRB results show the method is not overfitted to a single dataset.

5. **Demonstrates interesting attack interactions.** The paper identifies that the single-pixel attack, which fails in isolation on GTSRB, achieves >90% ASR when combined with other attacks (Section 6.2). This finding has practical implications for attack evaluation and is novel.

## Weaknesses

### Fatal

None.

### Major

1. **The 40% removal fraction is not accompanied by detection precision/recall metrics, making it difficult to separate detection ability from data destruction.** The paper rejects 40% of training data (r=0.4, line 246) while the actual poisoning rate is ~8–10% (line 248). This means ~30–32% of the removed examples are clean. The paper does not report what fraction of removed examples are actually poisoned (precision) or what fraction of poisoned examples are caught (recall). Without these metrics, it is unclear whether BaDLoss works because it genuinely detects backdoors or because aggressive filtering cripples the model's ability to learn backdoors (at some cost to clean accuracy). The clean accuracy degradation in the multi-attack setting is modest (~3–4%), which suggests the filtering is somewhat selective — but direct detection metrics are needed to substantiate this. An ablation showing performance at lower removal rates (e.g., r=0.1, 0.2, 0.3) would substantially strengthen the evidence.

2. **Missing ablation of the removal rate.** The paper fixes r=0.4 without any sensitivity analysis. Since the poisoning ratio is 8–10%, a method that removes exactly the poisoned examples (plus a safety margin) would be far more convincing. Showing whether BaDLoss works at r=0.15 or r=0.2 — removal rates closer to those of baselines like Spectral Signatures (15%) — would disentangle the effect of detection from that of aggressive data removal. Without this, the comparison to baselines that remove less data is asymmetric.

### Minor

1. **Single-attack claims are overstated**, particularly for GTSRB. On CIFAR-10, BaDLoss achieves the best ASR (4.02%) but at a clean accuracy of 85.05%, which is ~7 points below the undefended baseline (91.89%) and well below every other defense (all ≥91%). On GTSRB, BaDLoss's average ASR (32.70%) is worse than Neural Cleanse (9.72%). The paper states the method is "effective even in the single-attack setting" (line 254), but the clean accuracy penalty on CIFAR-10 and the weak GTSRB ASR results mean this claim only holds with significant caveats. The paper partially acknowledges this (line 254: "the high removal fraction... degrades our clean accuracy"), but the overall framing remains too optimistic.

2. **No sensitivity analysis on key hyperparameters.** The choices of 30 detection epochs, k=50 nearest neighbors, and the use of mean L2 distance (rather than, e.g., median) are not justified or ablated. A small sensitivity experiment for at least one of these would help establish that results are not brittle to arbitrary choices.

3. **No statistical variance reported.** No error bars, standard deviations, or multiple-seed runs are reported for any result. Given the stochasticity in both training and detection, single-run results weaken confidence in the reported numbers.

4. **The comparison against existing defenses in the multi-attack setting uses their default parameters without exploring whether simple adaptation (e.g., tuning thresholds using the same clean probe set available to BaDLoss) could improve them.** While the paper's justification — that attackers cannot tune for unknown attacks — is reasonable (line 153), testing even one tuned baseline would have made the "existing defenses fail" claim more robust.

5. **Per-attack poisoning ratios are not specified** (line 113: "all attacks are present at their full poisoning ratio"). The overall fraction is given (~8–10%), but individual attack ratios are omitted, making exact replication harder.

### Trivial

- The bar charts (Figures 2, 4) are dense and difficult to read without color; different hatching or separate subplots would help.
- The ASR definition ("evaluated on the full test set excluding the target class, with the backdoor injected into every example") is non-standard; it would benefit from a brief note on how this differs from definitions used in some prior work.

## Nice-to-Haves

- An analysis of false positive rates (or precision/recall) for BaDLoss detection, even for a single multi-attack configuration, would transform the evidence for the method's core mechanism.
- A small ablation on probe set size (e.g., 50, 250, 1000) and detection phase length (e.g., 15, 30, 50 epochs) would improve confidence in the hyperparameter choices.
- The "no image is attacked twice" assumption (line 101) is acknowledged but could be discussed as a simplifying factor — in a more challenging setting, overlapping triggers could interfere with detection.

## Removed Points

- **"MAP-D is referenced but not explained":** The paper cites MAP-D as inspiration (line 176); no further explanation is needed for a cited prior work.
- **"The footnote about rejecting epochs with high loss is a fudge":** This is a reasonable heuristic described transparently in a footnote; calling it a "fudge" is editorializing.
- **"Other defenses could also achieve low ASR if allowed to remove 40% of data":** Speculative — the paper's own Frequency Analysis results show that aggressive removal (its fraction is even higher) crashes clean accuracy to random chance, undermining this speculation.
- **Strongth Finder's strength #6 ("Competitive single-attack performance despite aggressive removal rate"):** Partially retained (modified as weakness #1) where the evidence is mixed; the strength aspect (lowest ASR on CIFAR-10) is acknowledged in the Minor weakness framing.

## Novel Insights

The reviewers collectively surface a tension that the paper does not fully resolve: BaDLoss's striking multi-attack ASR reductions co-exist with an unusually aggressive removal rate (40% vs. 8–10% poisoned). The harsh critic correctly identifies that without detection-level metrics, the reader cannot cleanly attribute the improved ASR to backdoor *detection* versus heavy-handed *data filtering*. However, the paper's own data partly mitigates this concern: aggressive filtering (Frequency Analysis) crashes clean accuracy to near-random, while BaDLoss loses only ~3–4% — suggesting its filtering is non-random. The most novel insight from the reviews is that a single ablation (varying r from 0.1 to 0.4) would likely resolve this ambiguity cleanly, and the absence of this simple experiment is the paper's single largest evaluative gap. Neither reviewer identified flaws in the core problem formulation or the loss-trajectory detection concept, which appear sound.

## Suggestions

1. **Report detection-level metrics.** Add precision, recall, or a precision-recall curve for BaDLoss detection in at least the CIFAR-10 multi-attack setting. This directly addresses the central ambiguity about whether the method detects backdoors or over-filters.

2. **Ablate the removal rate r.** Show BaDLoss performance at r ∈ {0.1, 0.2, 0.3, 0.4}. If r=0.2 achieves similar ASR with higher clean accuracy, this would dramatically strengthen the paper.

3. **Soften the single-attack claims.** Acknowledge explicitly that the aggressive removal rate (tuned for multi-attack) causes a clean accuracy penalty in the single-attack setting, and that on GTSRB, BaDLoss underperforms Neural Cleanse on ASR. The contribution does not depend on strong single-attack performance.

4. **Add error bars.** Report results over at least 3 random seeds to establish stability.

5. **Specify per-attack poisoning ratios** in the multi-attack setting for reproducibility.
