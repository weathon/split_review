I've thoroughly verified claims against the paper. Let now produce the consolidated review.

---

## Summary

This paper introduces a new setting called Realistic Open-world Long-tailed Semi-supervised Learning (ROLSSL), which removes the assumption that known and novel class distributions are consistent and assumes labeled known-class data is much scarcer than unlabeled data. The authors propose Dual-stage Post-hoc Logit Adjustment (DPLA), which applies logit adjustments in two stages: first using a scaling factor that accounts for class count and dataset size beyond sample frequency, and second using predicted class frequencies to reweight unlabeled data logits. Experiments across six datasets show DPLA substantially outperforms the OpenLDN baseline under the ROLSSL setting.

## Strengths

- **Realistic and timely problem formulation.** The ROLSSL setting relaxes two unrealistic assumptions in existing OLSSL benchmarks: (1) that labeled and unlabeled data have similar distributions, and (2) that labeled data is abundant relative to unlabeled data. Table 1 clearly situates ROLSSL relative to prior settings. This is a meaningful direction that better reflects real-world annotation constraints.

- **Consistent and often large accuracy gains over the sole adapted baseline.** DPLA outperforms OpenLDN across nearly all datasets and distribution conditions (Consistent, Reversed, Uniform). The gains are particularly striking on novel class accuracy — e.g., CIFAR-10 Uniform novel: 3.8% → 53.9%; SVHN Consistent novel: 0.5% → 35.4%; SVHN Reversed novel: 15.3% → 20.2% (Tables 1–2). These margins directly support the claim that DPLA mitigates the novel-class recognition collapse that plagues OpenLDN under ROLSSL.

- **Ablation confirms the contribution of each design stage.** On SVHN, the first-stage logit adjustment alone raises novel accuracy from 0.5% to 32.5%, and the second stage further improves it to 35.4% (ablation table, Section 4.4). This clean decomposition validates the dual-stage design.

- **Scaling factor adaptation addresses a known PLA limitation.** The paper identifies that the original PLA fails on datasets with many classes (CIFAR-100, ImageNet-100) and proposes a scaling factor incorporating $\mathcal{C}$ and $\mathcal{S}$. Figures 5–6 (described in text) show the scaling factor has a sweet spot where performance exceeds baseline, demonstrating a principled fix.

## Weaknesses

### Fatal
None.

### Major

- **Only one baseline (OpenLDN) is evaluated under the long-tailed ROLSSL setting.** Tables 1 and 2 list several OSSL methods (ORCA, UNO, RankStats, etc.) but only in the non-long-tailed "Semi-supervised & Open-world" sections, not under the three long-tailed conditions. Other OSSL methods (ORCA, OpenCon) or LTSSL methods (DASO, ACR, CReST) are not re-instantiated in the ROLSSL framework. Without such comparisons, the claim that DPLA is "superior" to existing approaches is only supported relative to a single baseline. Since OpenLDN often achieves near-chance novel accuracy in ROLSSL (e.g., 0.5% on SVHN Consistent), beating it is necessary but not sufficient to establish that DPLA is a strong solution.

- **Key hyperparameters are not disclosed, hindering reproducibility.** The method specification omits values for several critical parameters:
  - $\mathcal{C}_{base}$ and $\mathcal{S}_{base}$ in the first-stage scaling factor (Eq. 3) are described conceptually but their numerical values are never reported.
  - $\alpha$ and $\beta$ in the second-stage weighting (Eq. 4) are introduced without any values or selection procedure.
  - The pseudo-label masking threshold $\rho$ (Eq. 11 / Eq. 12 discussion) is not specified.
  - Mixmatch hyperparameters are not given; the number of epochs for the second training stage is absent.
  No code release is mentioned, making the method difficult to reproduce or build upon.

- **No statistical reporting over multiple runs.** All results appear to be single-run. Given that Section 4.3 explicitly notes that OpenLDN has "random seed variations" and the paper selects its "best performance," the lack of mean ± std over multiple seeds for both OpenLDN and DPLA makes it impossible to assess the significance of the reported improvements.

### Minor

- **Ablation for the stage-wise contribution is limited to SVHN.** The core ablation table (Section 4.4) showing the incremental benefit of each DPLA stage is conducted only on SVHN. While the first-stage scaling factor is also ablated on CIFAR-100 and ImageNet-100 (Figures 5–6), the second-stage and pseudo-label refinement contributions are not validated on additional datasets. Similarly, the $\lambda_1, \lambda_2$ trade-off parameter sweep is only performed on CIFAR-10, and the paper merely asserts the pattern is "consistent across most other datasets" without evidence.

- **"S/N Consistency" in Table 1 is not defined.** This column header appears in the table comparing ROLSSL to other settings but is never explained in the text.

- **The claim about logit margins is stated without formal justification.** The paper claims the first-stage adjustment "encourages a larger relative margin between the logits of rare and dominant labels" (Section 3.3) but provides no analysis or proof. While empirical results support the method's effectiveness, the mechanistic claim is asserted rather than demonstrated.

- **The motivation for the specific sigmoid-based second-stage weighting form (Eq. 4) is not explained.** The paper describes what the weighting does (suppress frequent classes, encourage rare classes) but not why this particular functional form was chosen over alternatives (e.g., log-proportional weighting, temperature scaling).

### Trivial

- Minor notation inconsistency in the imbalance ratio definition for novel classes: $\gamma_n^u = \frac{max_c M_1}{min_c M_{c_k}}$ (line 76) mixes sorted indices ($M_1$) with class-count subscripts ($M_{c_k}$), which is confusing.

- The "up to 50.1%" improvement figure in the abstract comes from CIFAR-10 Uniform novel accuracy (3.8% → 53.9%), which is a 50.1 percentage-point absolute gain. This is an impressive improvement but could be clarified as absolute percentage points to avoid confusion with relative improvement.

## Nice-to-Haves

- Adapting at least one additional OSSL method (e.g., ORCA, OpenCon) or LTSSL method (e.g., DASO, ACR) to the ROLSSL setting and reporting its performance would substantially strengthen the empirical case.
- Adding per-class accuracy breakdowns (head vs. medium vs. tail) for both known and novel classes would directly test whether DPLA reduces category bias as claimed.
- Plotting pseudo-label quality (accuracy and coverage) over training epochs for both OpenLDN and DPLA would provide mechanistic insight into why DPLA avoids novel-class collapse.

## Removed Points

*These points are flagged to be removed; treat them with caution:*

- **Cherry-picked baseline criticism (from Harsh Critic #1).** The reviewer claims this "invalidates all comparative claims." However, the paper states it selected the *best* OpenLDN run (i.e., most favorable to the baseline). Comparing against the best-case baseline makes the comparison *harder*, not easier, for the proposed method — this is a conservative design choice, not a flaw. The real issue (kept above) is the lack of mean±std reporting, not that the comparison is invalid.

- **Hungarian algorithm for known classes (from Harsh Critic's Section 4 notes).** The paper clearly states: "We assess accuracy for known classes using standard measures. For novel classes, we evaluate clustering accuracy and employ the Hungarian algorithm" (line 134). The reviewer's concern that it's unclear whether Hungarian is used for known classes reflects a misreading.

- **Notation ambiguity of $\stackrel{\sim}{=}$ (from Harsh Critic's Section 3 notes).** The symbol is slightly unconventional but its meaning (approximately equal) is clear from context; this is a formatting nitpick.

- **Typos/grammar/formatting complaints.** The hard rules require removing these.

## Novel Insights

The reviews surface an interesting tension: the paper's framing simultaneously claims to establish "a strong baseline" for a new task (which implies first-mover status where exhaustive comparisons are not expected) and claims "superiority" over existing methods (which invites demands for broader baselines). The core tension is between introducing a new challenging setting and evaluating it thoroughly. The paper convincingly shows that existing OLSSL methods collapse under ROLSSL and that DPLA provides a meaningful fix, but it does not yet show that DPLA is the *best* possible approach — only that it is substantially better than one alternative. A deeper insight is that the failure of OpenLDN under ROLSSL is specifically a *novel-class collapse* phenomenon (Section 4.3, Fig. 4), which DPLA addresses through its logit adjustment strategy. This suggests that logit-margin interventions may be particularly well-suited to settings where novel class discovery interacts with distribution mismatch — a hypothesis worth testing in future work.

## Suggestions

1. **Release code and specify all hyperparameters.** Provide values for $\mathcal{C}_{base}$, $\mathcal{S}_{base}$, $\alpha$, $\beta$, $\rho$, Mixmatch settings, second-stage training epochs, and learning rate schedules. Without these, the paper is not reproducible.

2. **Report mean ± std over at least 3–5 random seeds** for both OpenLDN and DPLA, and clarify whether the reported DPLA numbers are also the best over seeds or averaged.

3. **Adapt at least one additional OSSL or LTSSL method** (ORCA would be the most natural choice given its availability) to the ROLSSL setting and report its performance in the long-tailed tables.

4. **Add per-class accuracy** (head/medium/tail) to demonstrate that DPLA specifically benefits tail classes, supporting the claimed bias-mitigation mechanism.

5. **Label the x-axes in the scaling factor ablation figures** (Figs. 5–6) and specify what values of the scaling factor are being swept.

## Score and Decision

The paper identifies a genuine gap and proposes a reasonable method with strong initial results. However, the evaluation relies on a single baseline (OpenLDN) under the long-tailed setting, key hyperparameters are undisclosed, and no variance statistics are reported. These issues are significant but not fatal — the core contribution (ROLSSL setting + DPLA method) remains valid and the results are promising. The paper would benefit from additional comparisons and full specification before it can be considered a thoroughly validated baseline.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>