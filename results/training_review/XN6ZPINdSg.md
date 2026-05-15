Now I have all the information I need. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Points that were removed with justification

## Novel Insights
One paragraph

## Suggestions
- specific actionable suggestion

## Score and Decision

Here is my final consolidated review:

---

## Summary

COLEP proposes the first certifiably robust conformal prediction framework that integrates external domain knowledge and logical reasoning via probabilistic circuits (PCs). The paper provides end-to-end robustness certification for prediction coverage under ℓ₂ bounded perturbations (Theorems 1–3), proves that the framework achieves higher certified coverage and accuracy than a single model when knowledge utilities are non-trivial (Theorems 4–5), and demonstrates empirical improvements over RSCP and standard CP on GTSRB, CIFAR-10, and AwA2.

## Strengths

- **Novel integration of knowledge-enabled reasoning with certifiably robust conformal prediction.** Combining probabilistic circuits with conformal prediction for certified robustness is new. The paper correctly motivates the choice of PCs over Markov Logic Networks (exponential inference complexity) and variational inference (approximation error) for exact and efficient reasoning (Section 3.2). The illustrative stop-sign example (lines 190–195) concretely shows how the reasoning component corrects adversarially inflated probabilities.

- **Complete end-to-end certification pipeline.** The paper provides a closed-form bound connecting input perturbation bounds (via randomized smoothing) through the PC reasoning component (Theorem 1) to the final prediction set coverage (Theorems 2–3), including finite-sample corrections. This gives a principled certification chain from the learning component to the conformal prediction output.

- **Consistent empirical improvement over SOTA baseline.** On all three datasets and under all perturbation radii tested, COLEP achieves higher certified coverage than RSCP (Figure 1), with the gap widening under larger perturbations (δ=0.5). Under PGD attacks (Figure 2), COLEP maintains nominal coverage with smaller prediction sets than RSCP. These results are consistent with the theoretical claims.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of the reasoning component is not isolated from the effect of additional model capacity.** The experiments compare COLEP (main model + 2–4 knowledge models + PC reasoning) against RSCP and CP, both using only a single main model. No ablation compares COLEP against a simple ensemble that uses the same set of models (main + knowledge models) without PC-based logical reasoning (e.g., averaging their probability outputs). Without this control, the observed improvement cannot be cleanly attributed to the knowledge-enabled reasoning—it may partially or entirely come from the additional model capacity or better uncertainty quantification from multiple models. The theoretical analysis (Theorems 4–5) compares COLEP to a single model, not to an ensemble without reasoning, so this gap is not addressed by the theory either. The paper states "For fair comparisons, we use the same model architecture and parameters in COLEP and baselines CP and RSCP" (line 499), but this refers only to the main model architecture, not to total system capacity.

### Minor

- **Mixture weight estimation for combining multiple PCs is underspecified.** The paper states that the coefficients β_r for combining PC outputs can be estimated "using the data by examining how frequently each PC correctly predicts the outcome across the given examples" (lines 187–188), but does not specify which data split (training, calibration, or separate validation) is used for this estimation. This matters because using the calibration set would affect the exchangeability assumption underlying conformal prediction. The description is too vague for reproduction.

- **Theoretical utility parameters are not validated experimentally.** Theorems 4–5 depend on utility parameters t_{cid,D}, z_{cid,D}, U_j^{(r)} and require ε_{j,c} > 0 to guarantee superiority. The paper does not estimate these parameters on any dataset nor verify that the required inequalities hold in the experimental setting. While the empirical results indirectly suggest the conditions are met, the theoretical claims remain conditional statements without empirical grounding. This weakens the connection between theory and experiments.

- **Sensitivity to the knowledge rule weight w is unexplored.** The paper fixes w = 1.5 for all experiments (line 504) but does not study how certified coverage, empirical coverage, or set size vary with w. Since w controls how much the reasoning component penalizes rule-violating assignments (Eq. 2, line 158), the results may be sensitive to this choice.

- **Accuracy comparison from Theorem 5 is not reported in the main experiments.** Theorem 5 (Thm. comp_1) proves that COLEP achieves higher prediction accuracy than a single model, and the paper cites \Cref{app:add} for further analysis. However, the main experiments (Figures 1–2) focus on coverage and set size without reporting accuracy numbers. Accuracy is a core promised benefit; its absence from the main empirical section weakens the validation of Theorem 5.

### Trivial

- None.

## Nice-to-Haves

- Reporting variance or confidence intervals for the certified coverage values (Figure 1) would strengthen the reliability of the comparisons, though we note that single-split evaluation is common in this setting.
- A concrete case study (similar to the illustrative stop-sign example in Section 3) showing where the main model is wrong under attack and the PC reasoning corrects it, with actual probability values from the experiments, would make the mechanism more tangible.
- A comparison of the certified coverage bound τ^{cer} alongside empirical coverage under attack would help readers assess how conservative the certification is.

## Removed Points

- **Criticism about CIFAR-10 knowledge rules not being specified in the main text.** The paper states "detailed steps of PC construction in \Cref{app:exp_detail}" (line 509). The appendix is stripped by the parser; the details exist in the original submission.
- **Criticism about knowledge model training details and architectures.** The paper references the appendix for construction details (\Cref{app:exp_detail}). The reviewer's concern may be addressed there.
- **Criticism about "no accuracy numbers reported anywhere."** The paper references \Cref{app:add} and \Cref{app:exp_res} for additional evaluations including accuracy. Accuracy may be reported in the appendix.
- **Complaint about missing proofs or appendix content.** The reviewer notes derivations are "relegated to the appendix." This is standard practice and the appendix exists in the original submission.
- **Claim that the comparison is "unfair" because COLEP uses extra knowledge models.** The baselines CP and RSCP use a single main model by design—they do not have a mechanism to incorporate additional knowledge models. Comparing complete systems is standard; the missing ablation (noted in Major weaknesses) is the proper way to address this concern, not calling the comparison unfair.

## Novel Insights

The most interesting observation across the reviews is a structural tension between the theoretical framing and the experimental design. The theory (Theorems 4–5) carefully proves superiority over a *single model* under quantified utility assumptions—a well-posed comparison. The experiments, however, compare COLEP as a full system against single-model baselines, which conflates the effect of the reasoning component with the effect of having more models. This means the theoretical framework could be more directly leveraged than it currently is: rather than claiming "COLEP is better," which the experiments support but don't fully isolate, the paper could design an experiment that tests the specific parameterized predictions of Lemma 1 (e.g., how the correction magnitude ε varies with model quality parameters t,z and rule utility U). Such an experiment would simultaneously validate the theory and isolate the reasoning mechanism. That said, the paper's current experiments still demonstrate a practically meaningful improvement over the SOTA baseline RSCP, even if the attribution to reasoning per se is not fully resolved.

## Suggestions

1. **Add an ensemble ablation.** Compare COLEP against a baseline that uses the same main model and knowledge models but replaces the PC reasoning with simple averaging (or a learned linear combination) of their probability outputs. This is the single most informative experiment for isolating the effect of logical reasoning.
2. **Clarify the mixture weight estimation procedure.** Specify which dataset split is used to estimate β_r, and confirm that exchangeability for the calibration set is preserved.
3. **Report accuracy in the main paper.** Since Theorem 5 promises accuracy improvement, show accuracy numbers alongside coverage in Figure 2 or a new table.
4. **Add a sensitivity analysis for w.** Show how certified coverage and set size vary over a range of w values (e.g., 0.5, 1.0, 1.5, 2.0) for at least one dataset.

## Score and Decision

**Originality**: High — first to combine knowledge-enabled reasoning via PCs with certified conformal prediction.  
**Importance of research question**: High — bridging robustness certification and uncertainty quantification is practically important for safety-critical applications.  
**Claims supported**: Partially — the core empirical claim (COLEP outperforms RSCP) is supported, but the attribution to reasoning is not fully isolated.  
**Soundness of experiments**: Adequate — experiments are on three datasets with SOTA baselines, but missing a critical ablation.  
**Clarity of writing**: Good — the paper is dense but well-structured; the cited appendices likely fill remaining gaps.  
**Value to community**: High — the framework and certification approach open a new direction for robust conformal prediction.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>