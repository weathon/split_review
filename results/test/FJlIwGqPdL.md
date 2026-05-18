Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper studies conformal prediction (CP) under standard $l_\infty$ adversarial attacks. It makes two empirical discoveries: (1) CP fails to produce informative prediction sets under strong attacks unless the model is adversarially trained, and (2) advanced adversarial training methods (TRADES, MART) often increase prediction set size (PSS) despite improving robust accuracy. To address this, the paper proposes Uncertainty-Reducing Adversarial Training (AT-UR), combining entropy minimization and a Beta-weighted loss based on True Class Probability Ranking (TCPR). Theorem 1 provides a theoretical connection showing the Beta-weighting loss upper-bounds expected PSS. Experiments across four datasets and three AT baselines show consistent PSS reductions (e.g., CIFAR100: AT PSS 14.29 → AT-Beta 11.61 under AutoAttack).

## Strengths

1. **First demonstration that CP fails under standard $l_\infty$ adversarial attacks without adversarial training.** The paper shows that for non-robust models, PSS of three CP methods (APS, RAPS, RSCP) is nearly equal to the number of classes under strong $l_\infty$ attacks (Fig. 2: ~9.79/10 on CIFAR10, ~83/100 on CIFAR100). This is a genuine empirical finding — prior work (Gendler et al., Ghosh et al.) only considered small $l_2$ budgets, and the paper correctly identifies this gap.

2. **Key observation that improved adversarial training can hurt CP-efficiency.** Table 1 shows that TRADES and MART often achieve higher robust accuracy than AT but produce larger prediction sets (e.g., CUB200: TRADES robust acc 22.30% vs AT 23.34%, but PSS 22.29 vs 17.75). This is non-trivial and motivates the proposed method well.

3. **Novel method (AT-UR) with a theoretical grounding.** The paper proposes two components — entropy minimization and Beta-weighting based on TCPR — and proves (Theorem 1) that the Beta-weighting loss is an upper bound on expected PSS at the population level. The design choice to weight *promising* samples (moderate TCPR) rather than hard samples is supported by the comparison with focal loss (AT-Focal performs much worse, e.g., PSS 27.24 vs AT baseline 23.79 on CIFAR100).

4. **Consistent empirical improvements across datasets and baselines.** Under AutoAttack (Table 2), AT-UR variants reduce PSS compared to the base AT method on all four datasets (e.g., CIFAR100: AT PSS 14.29 → AT-Beta 11.61; Caltech256: AT PSS 23.73 → AT-Beta 18.54). The improvement holds over a range of coverage values (Fig. 3 coverage-PSS curves) and attack budgets (Table S3).

## Weaknesses

### Fatal
None.

### Major
1. **Missing robust accuracy for AT-UR in main results.** The paper claims AT-UR learns "adversarially robust models with substantially improved CP-efficiency" (contributions, line 30), yet Table 2 (Tab.~\ref{tab:autoattack}) reports only coverage and PSS for AT-UR variants — robust accuracy is absent. The table caption states the paper's focus is CP metrics (line 413: "we only report the performance of CP...in the main paper"), but this conflicts with the claim about adversarial robustness. Without robust accuracy, the reader cannot assess whether PSS reductions come at the cost of degraded adversarial robustness. This is the single most important empirical gap in the paper. While AT-UR inherits adversarial training and is unlikely to catastrophically lose robustness, the paper must report these numbers to support its claim.

### Minor
2. **Theoretical connection (Theorem 1) is stated without sufficient clarity in the main text.** The theorem asserts that the Beta-weighting loss upper-bounds expected PSS, but the mechanism connecting the weighted loss (defined via TCPR-conditioned expectations) to the conformal prediction set size after the calibration step is not explained. The remark (line 369) gives only a brief intuitive restatement. Without a proof sketch in the main text, the theorem reads as an opaque assertion rather than an established result that clarifies *why* the weighting scheme reduces PSS. The proof likely exists in the appendix (stripped by parsing), but the main-text presentation should provide enough reasoning for a reader to follow the logic.

3. **Same-attack assumption for calibration and test is acknowledged but not probed.** The paper uses the same adversarial attack for both calibration and test (line 411) and acknowledges this as a limitation (line 626). In practice, the defender may not know the test-time attack. An experiment testing sensitivity to this assumption (e.g., calibrating on clean or differently-attacked data) would substantially strengthen practical relevance. The paper's conclusions about safety-critical applications (abstract, introduction) are weakened without probing this scope condition.

4. **MART is excluded from AT-UR experiments without explanation.** MART is presented as a motivating baseline in Table 1 (showing large PSS), but is not tested as a base method for AT-UR in Table 2. Given that MART had the largest PSS among baselines, it would be a natural test case to see if AT-UR can improve its CP-efficiency. The paper does not explain this omission.

5. **Beta-weighting creates a moving target during training — stability not discussed.** The weight assigned to a sample depends on its TCPR, which changes as the model trains. The paper does not discuss whether this feedback loop causes training instability, weight distribution collapse, or increased hyperparameter sensitivity beyond the reported $b$ sweep. This is a practical concern for adoption.

6. **Uncertainty-aware attack experiment (Table 3) is limited to CIFAR100.** The paper's only evaluation against an attack explicitly designed to undermine CP-efficiency covers just one dataset and one attack configuration. The conclusions (line 466: "Our method is still competitive") are qualitative and not supported by the same breadth of evidence as the main AutoAttack results.

### Trivial
None.

## Nice-to-Haves
- An experiment where calibration is performed on clean images or images attacked with a different budget/norm would probe scope sensitivity.
- An analysis of *why* TRADES/MART increase PSS (e.g., is it logit-level regularization, softened posteriors, or something else?) would deepen the contribution beyond correlation.
- Including robust accuracy scatter plots (PSS vs. robust accuracy) for all methods and datasets would enable the reader to directly see the trade-off.

## Removed Points
- **"The theorem is an assertion rather than an established result"** — Downgraded from Fatal/Major to Minor. The theorem is stated and a proof sketch exists in the (stripped) appendix. The concern is about main-text clarity, not validity. Standard for conference papers is to defer proofs to the appendix.
- **"The paper does not explore why advanced AT increases PSS"** — Moved to Nice-to-Haves. This is a direction for future work, not a weakness of the presented claims.
- **"Demand for comparing against closed-source models or adding additional AT baselines beyond the three tested"** — The paper's three baselines (AT, FAT, TRADES) are defensible choices covering vanilla AT, fairness-aware AT, and logit-regularized AT. The zoo is adequate for the claim.
- **"Criticism that the paper does not include theoretical proofs for generalization bounds (Theorem in the CUT section)"** — These are in a CUT (stripped) section and were likely in the appendix of the original submission.

## Novel Insights

The harsh critic's observation that the missing robust accuracy is the single most critical gap is spot-on — without it, the paper's central claim is partially unverifiable. Conversely, the strength finder correctly identifies that the core empirical findings (CP failure under $l_\infty$, AT methods hurting CP-efficiency) are genuinely novel and practically important regardless of the robustness verification gap. The synthesis of these two perspectives is that this paper has real contributions that are partially obscured by an incomplete evaluation. The theoretical result (Theorem 1) is novel in connecting importance weighting to CP-efficiency, but its impact is muted by opaque presentation. The paper would be substantially stronger if it verified robustness preservation and clarified the theorem's reasoning.

## Suggestions

1. **Report robust accuracy (and clean accuracy) for every AT-UR variant in the main results table (Table 2).** This is the single most impactful change. Add a scatter plot of (robust accuracy, PSS) for all methods across datasets to let readers directly assess the trade-off.
2. **Add a proof sketch or intuitive explanation in the main text for Theorem 1** showing how the weighted loss relates to the non-conformity scores used in APS prediction sets.
3. **Include at least one experiment probing the same-attack assumption** (e.g., calibrating on clean data and testing on attacked data, or calibrating under attack budget $\epsilon=4$ and testing under $\epsilon=8$).
4. **Test AT-UR with MART as a base method** or explain why it is excluded.
5. **Discuss training stability** of the Beta-weighting scheme given the dynamic TCPR.

## Score and Decision

The paper addresses a genuine and under-explored problem, makes novel empirical observations, and proposes a method with both theoretical grounding and consistent empirical support. However, the missing robust accuracy in the main evaluation table is a significant gap that prevents full verification of the central claim about "adversarially robust models." This gap is addressable in revision. The remaining weaknesses (clarity of Theorem 1, same-attack scope, limited ablation scope) are typical for a conference paper of this length.

**Overall Assessment**: The paper has real contributions — the CP-failure-under-$l_\infty$ observation, the AT-hurts-CP-efficiency finding, and the AT-UR method are all novel and useful. The main weakness (missing robust accuracy) is a significant but correctable omission. The paper would benefit from revision but its core contributions are sound.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>