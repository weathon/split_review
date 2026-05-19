Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces SCARA, a method for designing semi-open LLMs that hides a small number of bottom (early) decoder layers to balance downstream customizability with resilience against model recovery attacks. The paper provides a theoretical result on the existence of a "transition layer" in infinitely deep transformers, proposes a fine-tuning-free metric (Recovery Difficulty, RD) for selecting the minimal closed-source set, and evaluates the approach across five models (1.3B–70B), three attack strategies, sixteen resilience benchmarks, and six customization tasks. The core empirical finding is that hiding only ~2.5–8.3% of bottom-layer parameters achieves an Average Recovery Ratio (ARR) comparable to fully-closed models and to the SAP-DP baseline, while delivering superior downstream customization performance.

## Strengths

- **SCARA achieves strong resilience with dramatically fewer closed-source parameters than existing approaches.** On Llama2-70B, SCARA hides only 2.5% of parameters yet attains an ARR of 21.9%, nearly matching the fully-closed model (22.8%, 100% hidden) and SAP-DP (21.8%, 92.5% hidden). This pattern holds consistently across all five models (Table 1), with closed-source ratios 8–40× smaller than SAP-DP while ARR differences stay within 1.4 percentage points.

- **The Recovery Difficulty (RD) metric provides a strong, fine-tuning-free predictor of recovery performance.** Figure 6(a) reports Pearson coefficients consistently below −0.80 (and as low as −0.98) between RD and ARR across four models and six capability domains, validating RD as a practical tool for selecting closed-source sets without performing expensive recovery attacks.

- **Error amplification analysis (Figure 4) provides direct empirical evidence for why hiding early layers is more effective.** The paper shows that small perturbations at the first layer grow substantially through subsequent layers, explaining the asymmetric effect of early vs. late layer concealment. This empirical observation is the paper's most direct support for its core design choice.

- **Extensive and systematic evaluation** across five models (1.3B–70B parameters), three attack strategies (FT-all, FT-closed, SEM), sixteen resilience benchmarks spanning six domains, and six downstream customization tasks, plus sensitivity analysis on dataset scale and the ε hyperparameter.

## Weaknesses

### Major

- **Missing control baseline: SAP without DP noise.** The primary baseline SAP-DP confounds two variables — closed-source layer selection (hiding most of the top layers) and Laplace noise injection. Without evaluating SAP *without* DP noise, it is unclear how much of the resilience in the SAP-DP baseline comes from the choice of hidden layers vs. the noise perturbation. The paper claims superiority for hiding bottom layers, but to fully support this attribution it should compare SCARA (hiding a few bottom layers) against a version of SAP that hides a comparable *small* number of top layers without noise. Figure 5a partly addresses this by comparing same-sized bottom vs. top layer sets, but the main numerical comparison (Table 1) still uses SAP-DP.

- **Customizability results are presented only in a figure (Figure 3) without a supporting numerical table.** The paper makes specific quantitative claims (e.g., "30% higher downstream performance score than the baselines in the Financial domain," "improvement of over 40% on Mistral-7B") that cannot be verified from a figure alone. Key customizability numbers should be reported in a table with the same level of detail as the resilience tables.

### Minor

- **Gap between idealized theory and empirical observations is not addressed.** Theorem 1 predicts that under its idealized assumptions (infinite depth, a specific attention normalization, recovered parameters from a continuous distribution), recovery of bottom layers leads to complete output collapse (identical feature vectors for all tokens). Yet in all experiments, recovered models achieve non-trivial performance (e.g., 62.6% recovery ratio on PIQA for Llama2-70B). The paper does not explain why this gap exists — which specific assumptions are violated in practice and how that explains the observed partial recovery. This disconnect weakens the claimed theoretical foundation.

- **Scope condition (failure on small models) not stated up front.** The paper demonstrates that SCARA fails on OPT-350M (a 350M-parameter model), where bottom-layer hiding does not yield the best resilience and the RD metric breaks down. This limitation is discussed only in Section 4.3 but should be clearly stated as a scope condition in the abstract or introduction — SCARA is designed for models above a certain scale (empirically, ~1B+ parameters).

- **Theoretical justification for the RD metric is incomplete.** The paper claims that ‖θ_FT − θ_0‖₂ is of order O(|D|/√N) citing NTK results for single-layer ReLU networks, and asserts this extends to deep transformers with attention without justification or empirical verification (e.g., measuring actual parameter change during recovery fine-tuning). The RD metric works empirically, which is sufficient for a systems contribution, but the claimed theoretical foundation for it is weak.

- **No statistical variance reported.** Tables 1 and 2 report single values per condition with no confidence intervals or standard deviations. Given the variability of fine-tuning outcomes, some measure of spread (e.g., across seeds) is standard practice for this type of experiment.

- **Internal inconsistency in reported closed-source ratio.** The main text (p. 8) states "Llama2-70B, SCARA keeps only 1.25% of parameters hidden," but Table 1 reports the closed-source ratio as 2.50% for Llama2-70B. These figures disagree.

### Trivial

- The threshold mechanism for selecting the closed-source set (RD(I_l) ≥ (1−ε)RD([L])) is not directly validated. The paper shows that RD correlates with ARR, but does not compare the set selected by the threshold rule against the set that would actually achieve the target ARR. This is a minor gap in the evaluation of the methodology.

## Nice-to-Haves

- Recovery attack hyperparameters (training epochs, learning rates, batch size, hardware) are not reported, though these would not invalidate the results — the comparison is still fair across methods since the same attack setup is used for all.
- Evaluation of the RD metric's sensitivity to the size and composition of the 1.5k evaluation sample would strengthen the claim that it is robust.
- The adversarial attack defense analysis (Table 4) is tangential to the paper's core focus on recovery attacks and could be moved to an appendix or supplementary.

## Removed Points

These points were raised by the harsh critic but are excluded from the main weaknesses for the following reasons:

1. **"The evaluation metric for resilience is ambiguous and likely incorrectly reported"** — REMOVED because it is factually wrong. The values in Table 1 *are* recovery ratios as defined by Equation (1) (e.g., PIQA: 62.6 means the recovered model achieves 62.6% of the victim model's performance on PIQA, i.e., 0.626 × victim_accuracy). The reviewer mistook these for raw benchmark scores. The ARR is a meaningful average of these unitless ratios. The victim model's original scores are not needed to interpret the ratios, though including them would be a nice addition.

2. **Formatting/style nitpicks** (Table 1 column spacing, row label splitting, Figure 1 flowchart mismatch) — REMOVED as these are PDF-parser artifacts, not issues in the actual submission.

3. **"Equation (si) non-standard attention"** — REMOVED as a standalone weakness. The theorem explicitly assumes this specific attention form, which is standard practice for theoretical results. The concern about generalizability is subsumed under the theory-practice gap weakness above.

4. **"Transition layer analysis claim is trivial"** — REMOVED. The empirical finding that resilience transitions occur and that bottom layers provide better resilience than top layers of the same size is a nontrivial contribution, even if the general direction is intuitive.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's own findings and do not surface an unexpected interpretation or connection.

## Suggestions

1. **Add the SAP (without DP noise) baseline** to isolate the effect of closed-source layer choice from noise perturbation. Compare SCARA with SAP hiding a similarly small number of top layers to directly test whether bottom-layer concealment is uniquely effective.

2. **Provide a numerical table for customizability** (alongside or replacing Figure 3) so that the claimed improvements can be verified, with concrete numbers for each domain and model.

3. **Reconcile the 1.25% vs. 2.50% closed-source ratio discrepancy** for Llama2-70B in the text versus Table 1.

4. **Explicitly discuss the gap between Theorem 1 and observed results** — acknowledge which assumptions are violated in practice (finite depth, different attention normalization, non-continuous parameter distributions from SGD) and explain why these violations lead to partial rather than complete recovery.

5. **State the scope condition** (ineffectiveness on sub-1B models) in the abstract or introduction.

6. **Add variance estimates** (e.g., standard deviations across seeds) to the main resilience tables.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Weak Accept</decision>