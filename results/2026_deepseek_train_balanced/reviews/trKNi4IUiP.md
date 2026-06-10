Now I'll produce the final review.

## Summary

This paper proposes RIGBD, a defense against graph backdoor attacks. The core idea is: (1) train a backdoored model on the poisoned graph, (2) perform random edge dropping and measure prediction variance to detect poisoned nodes (which exhibit large variance when trigger edges are dropped), and (3) train a robust classifier with a loss that minimizes confidence in the detected target class for identified poisoned nodes, keeping clean accuracy intact. The method is evaluated against three attacks (GTA, UGBA, DPGBA) on several benchmark datasets.

## Strengths

1. **Robust training loss with strong ablation evidence (Eq. 6, Section 5.4).** The ablation convincingly demonstrates the design's effectiveness: when recall is only ~17.4% (at β=0.1, K=2), full RIGBD achieves 1.86% ASR versus ~80% ASR when identified triggers are simply removed (RIGBD\R variant). This shows the loss actively counteracts undetected triggers, not just identified ones — a non-obvious property.

2. **Effective against in-distribution triggers (DPGBA) where prior defenses fail.** Prior work (Prune, OD) was specifically shown to fail on DPGBA's in-distribution triggers. RIGBD consistently achieves ASR close to 0% across datasets against DPGBA, representing a genuine advance over the state of the art.

3. **Addresses the multi-edge subgraph trigger scenario explicitly.** The paper identifies that exhaustive per-edge dropping fails when triggers connect via multiple edges (Fig. 1b) and provides a clean complexity analysis: random edge dropping scales as O(K) versus O(L N d^L M(d+M)) for the exhaustive approach. The ablation confirms random edge dropping outperforms per-edge dropping by ~40% ASR reduction in the multi-edge setting.

## Weaknesses

### Major

1. **Missing undefended ASR baseline — results cannot be properly calibrated.** The paper never reports the ASR of a vanilla GCN trained on poisoned data without any defense. While the defense baselines (Prune, OD) provide some calibration (they fail on DPGBA), the undefended ASR is the standard reference point in backdoor defense papers. Without it, the reader cannot assess whether DPGBA achieves 30% or 99% ASR on an undefended model — a critical difference for evaluating whether ASR ≈ 0% is impressive or marginal. This is a concrete gap, not a scope issue.

2. **Overclaimed theoretical guarantee (Contribution ii).** The paper claims: "Theoretical analysis guarantees that our specially designed graph convolution operations can precisely distinguish poisoned nodes from clean nodes through random edge dropping." What the theory actually delivers: Theorems 1–2 prove that clean node embeddings remain stable under random edge dropping (providing a bound against false positives). Theorem 3 bounds expected trigger-edge removals (Kβ). The theory does **not** prove that poisoned nodes will exhibit large prediction variance, nor does it establish a bound on the separation between classes. The poisoned-side distinguishability relies entirely on the empirical observation in Section 3.2 (one dataset, one attack). The paper later acknowledges this framing (line 122: "the last-layer classifier's sensitivity... leads to a significant variance. This is verified in Sec. 3.2"), but the contribution statement and abstract remain overstated. This is a framing error, not a methodological flaw, but it misrepresents what is proven vs. observed.

### Minor

1. **No variance/confidence measures across 5 runs.** The paper states "Each experiment is conducted 5 times and the average results are reported" but provides no standard deviations, confidence intervals, or run-to-run ranges. Without these, the reader cannot assess whether the reported differences between RIGBD and baselines are meaningful or within noise.

2. **Dataset coverage mismatch.** Section 5.1 lists 6 datasets (Cora, Citeseer, PubMed, Physics, Flickr, OGB-arxiv) and the evaluation protocol specifies trigger counts for all 6. Yet Section 5.2 states defense results are reported "across three datasets." The detection evaluation (Table 3), hyperparameter analysis, and ablation are all conducted only on OGB-arxiv. The actual evaluation breadth does not match the claimed scope. At minimum, detection precision/recall on a second dataset would strengthen claims of generality.

3. **Threshold selection heuristic is ad-hoc (Eq. 5).** The threshold τ is determined by finding two consecutive non-target-class nodes in the sorted prediction variance list. No analysis is given for cases where this structure breaks (e.g., a clean non-target node with anomalously high variance appearing early in the list, or the list never yielding two consecutive non-target entries). The paper does not ablate this choice or compare it against simpler alternatives (e.g., top-k selection, percentile-based thresholding).

4. **Core empirical observation (Section 3.2) demonstrated on only one setting.** Figure 1 shows results for OGB-arxiv with DPGBA only. The claim that "dropping adversarial edge connecting backdoor trigger will result in a much larger prediction variance" is presented as general, but its generality across datasets and attack methods is not established.

### Trivial

None.

## Nice-to-Haves

- Report wall-clock runtime or training cost comparison with baselines.
- Extend the hyperparameter and ablation analysis to at least one additional dataset and one additional attack method.

## Removed Points

These were raised by reviewers but removed after verification against the paper; they are listed here for reference only:

- *"Robust training loss does not provide an alternative label for poisoned nodes"* — The loss intentionally minimizes confidence on the target class (unlearning the backdoor association), which is a standard design choice explained in Section 4.2. This is not a flaw. **Removed**.
- *"Missing section content for 'Impact of Various Numbers of Triggers and Trigger Sizes'"* — Likely a parser artifact truncating content that exists in figures or the original PDF. **Removed** per hard rule about parser artifacts.
- *"Dataset split protocol (inductive vs transductive) is a concern"* — The paper explicitly states it uses the inductive setting, matching the evaluation protocol of the attack papers it builds on. This is transparent and intentional. **Removed**.
- *"No discussion of computational cost"* — The paper provides time complexity analysis (Section 3.2, line 57) comparing exponential per-edge dropping with linear random edge dropping. This is present. Downgraded to Nice-to-Have for wall-clock numbers. **Removed** as a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface an overclaiming issue in the theoretical framing and a missing evaluation baseline, but these are correction points rather than novel readings.

## Suggestions

1. Add a "Vanilla GCN (No Defense)" row to all tables reporting ASR — this single addition dramatically improves interpretability.
2. Temper Contribution (ii) to reflect what the theory actually proves (clean node stability guarantees low false positives) and clarify that the poisoned-node distinguishability is empirically supported and theoretically motivated, not theoretically guaranteed.
3. Report standard deviations or error bars for the 5-run averages throughout.
4. Extend detection precision/recall evaluation to at least one additional dataset beyond OGB-arxiv.
5. Clarify the dataset coverage: resolve the "three vs. six" inconsistency by stating explicitly which datasets appear in which tables.
6. Analyze the threshold heuristic's failure modes, or ablate against a simpler alternative (e.g., top-k), to establish robustness.

## Score and Decision

The paper proposes a well-motivated defense with a sound core idea and one genuinely impressive result (the ablation showing the robust loss works even at 17.4% recall). However, two major issues prevent acceptance: the missing undefended ASR baseline, which leaves the headline results uncalibrated, and the overstated theoretical guarantee. These are fixable, and with revision the paper could be a solid contribution, but as submitted it does not meet the bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>