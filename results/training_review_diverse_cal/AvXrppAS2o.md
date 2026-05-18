Now I have a complete picture. Let me produce the consolidated review.

---

## Summary

This paper proposes a framework that jointly learns causal structure (as an auxiliary task) and outcome prediction by sharing a latent representation from a graph autoencoder (building on CausalGAE, Ng et al., 2019), then using separate decoder heads for data reconstruction (g₂) and outcome prediction (g₃). The core idea — that outcome prediction can benefit from both causal parents and non-causal predictive signals — is well motivated, and the paper correctly identifies two limitations of the prior CASTLE method (scalability of its feed-forward architecture and its use of the reconstructed target as the final output). However, the experimental section contains a fatal inconsistency regarding the key training hyperparameter κ that renders the empirical results uninterpretable.

---

## Strengths

- **Clear identification of limitations in prior work.** The paper correctly identifies two concrete unsolved challenges in CASTLE (Kyono et al., 2020): (1) its feed-forward architecture does not scale with the number of features, and (2) using the reconstructed target variable as the final output hinders both causal learning and prediction. The proposed remedies — adopting a graph autoencoder (CausalGAE) that builds a single graph for all variables, and adding a dedicated outcome prediction head g₃ — are architecturally reasonable responses to these limitations.

- **Scalability analysis demonstrates a real architectural advantage.** Figure 1 and Table 4 show that the GAE-based approach scales far better than CASTLE's feed-forward architecture as the number of variables increases (CASTLE's training time grows from ~20s at d=10 to >4000s at d=200, while the proposed model stays under ~50s). This advantage is architectural and does not depend on the κ issue.

---

## Weaknesses

### Fatal

- **The stated hyperparameter κ=0 is incompatible with the claimed training procedure and reported results.** The paper states (line 103): "The loss hyperparameter κ is set to 0." In the objective function (Eq. 6), the supervised loss term for outcome prediction is weighted by κ:
  
  min_{w,Θ₁,Θ₂,Θ₃} (1-κ)/(2n) Σ‖X−X̂‖²_F + λ‖W‖₁ + κ/n Σ‖Y−Ŷ‖²_F

  If κ = 0, the supervised loss term vanishes. The parameters Θ₃ of the outcome prediction head g₃ appear **only** in this term, meaning g₃ receives **no gradient from the outcome labels** during joint training. The paper therefore provides no mechanism by which g₃ learns to predict the target variable, yet reports that the proposed model substantially outperforms CausalGAE and CASTLE on outcome prediction (Tables 1, 3, 5, 6).

  Moreover, the ablation study (Table 3) reports different MSE values for "Our model" and the "w/o outcome prediction" variant. With κ=0, both variants lack a supervised signal for outcome prediction, yet their reported results differ — a logical inconsistency that the paper does not explain.

  Three possibilities exist: (a) κ was intended to be non-zero but a typographical error appears in the paper, (b) κ was set to 0 only for the CausalGAE baseline and a different value was used for the proposed model, or (c) the supervised loss is applied through some mechanism not described in the objective. None of these are supported by the text as written. **Whatever the truth, the paper as presented does not allow a reader to determine how the outcome prediction head was actually trained, and the reported results cannot be trusted.** This is not a minor oversight — it undermines every empirical claim in the paper.

  Because this single issue invalidates the evidentiary basis for the paper's core claim (that shared representation between causal structure learning and outcome prediction improves generalization), the paper cannot be accepted in its current form.

### Major

- **Missing standard survival analysis baselines in the case study.** The Worcester heart attack study (Table 6) compares the proposed model only to MLP variants and CASTLE. Standard survival models such as Cox Proportional Hazards or random survival forests are absent. If the goal is to demonstrate translational value for clinical survival analysis, the comparison set needs to include methods a practitioner would plausibly use.

- **No discussion of limitations.** The paper ends abruptly with the conclusion. Given the ambitious framing (addressing unmeasured confounders, evolving conditions, etc.), a frank assessment of where the method might fail (e.g., high-dimensional data, strong violations of causal assumptions, non-stationarity beyond temporal splits) is essential.

### Minor

- **Causal interpretability claim is not validated.** Figure 2 shows causal graphs recovered from the survival case study, with a brief textual description of which variables appear. However, no systematic validation of these edges against domain knowledge or prior medical literature is provided. Without such validation, the interpretability benefit remains anecdotal.

- **The "robust causal discovery for the outcome variable" claim is evaluated on full-graph metrics, not specifically on edges incident to the outcome.** Table 2 reports FDR, TPR, FPR, and SHD for the full graph. While these metrics are standard, the paper states its focus on "robust causal discovery for the outcome variable" but provides no targeted evaluation of how well edges involving the outcome are recovered.

### Trivial

None.

---

## Nice-to-Haves

- Provide a failure analysis on synthetic data that isolates when joint learning helps (e.g., vary the strength of the non-causal term in the data-generating process).
- Compare against NOTEARS and DAG-GNN on causal discovery metrics (the paper justifies focusing on CausalGAE, but including them would strengthen the evaluation).
- Validate the learned causal graph on real data by comparing to known risk factors from medical literature.

---

## Removed Points

These points were raised by reviewers but are removed or downgraded for the following reasons:

- **"Missing comparison to CASTLE's reconstructed-target approach"** — The ablation study ("w/o outcome prediction") is intended to address this, but the ablation results are themselves undermined by the κ issue. This is subsumed by the fatal weakness.
- **"Causal discovery evaluation compares only to CausalGAE"** — The paper provides a justification (lines 127–128): CausalGAE has already demonstrated superior performance over NOTEARS and DAG-GNN on the same synthetic data. This is a reasonable scoping choice.
- **"CASTLE comparison on scalability"** — This is already provided in Figure 1 and Table 4. The reviewer may have missed it.
- **"Weakness about LAS Vegas dataset performance being too good"** — Not raised by the harsh critic, but the Strength Finder's claim of AUC "0.724 vs baselines below 0.55" is a strength, not a weakness.
- **Generic strengths from Strength Finder** — Several claimed strengths ("novel architecture improves generalization," "joint learning enhances causal discovery," "ablation studies confirm necessity") all depend on the κ issue being resolved. They are mentioned here for completeness but cannot be relied upon until the experimental protocol is clarified.

---

## Novel Insights

None beyond the paper's own contributions. The fatal κ inconsistency prevents any meaningful assessment of whether the proposed framework works as claimed.

---

## Suggestions

1. **Resolve the κ uncertainty.** Clarify and correctly report the value of κ used in all experiments. If κ was non-zero, correct the statement in the paper and include a sensitivity analysis showing how performance varies with κ. If κ was truly zero, explain the mechanism by which g₃ learns (or acknowledge that g₃ is not jointly trained, which would fundamentally change the contribution).

2. **Re-run and correctly report all experiments** once the κ setting is clarified.

3. **Add standard survival analysis baselines** (Cox PH, random survival forests) to the case study.

4. **Add a limitations section** discussing scenarios where the method would be expected to fail.

5. **Validate the learned causal graphs** against domain knowledge or prior literature.

---

## Score and Decision

**Originality:** The idea of separating the prediction head from the reconstruction decoder while sharing representations is a reasonable extension of CausalGAE, but the core approach (jointly learning causal structure for prediction) is already explored in CASTLE.

**Importance of research question:** The question of how to combine causal structure learning with outcome prediction for improved generalization is practically important, especially in medical domains.

**Whether claims are well supported:** The claims are not well supported due to the fatal κ inconsistency.

**Soundness of experiments:** The experiments cannot be evaluated in their current form due to the κ issue.

**Clarity of writing:** Generally clear, though the κ issue represents a critical omission.

**Value to the research community:** The conceptual framing is interesting, but without trustworthy empirical validation, the paper's value is limited.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>