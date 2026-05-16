Here is my final consolidated review.

## Summary

This paper proposes Mamba-CDSP, a Mamba-based (state-space model) framework for time-varying counterfactual prediction (TCP). The key ideas are (a) using Mamba as the backbone to address the quadratic complexity of Transformer-based TCP methods, and (b) introducing a Covariate-based Decorrelation towards Selective Parameters (CDSP) regularization term that penalizes the covariance between the current treatment and the learned hidden state, intended to mitigate sequential confounding bias while avoiding the over-balancing problem of adversarial approaches. The paper also adopts a dropout layer in place of Mamba's 1-d convolution to reduce overfitting on temporal data.

## Strengths

- **Novel integration of Mamba with a lightweight de-correlation regularizer for TCP.** To my knowledge, this is the first paper to adapt Mamba's selective state-space model for counterfactual prediction over time series. The motivation is clear: existing Transformer-based TCP methods (e.g., Causal Transformer) suffer from quadratic complexity that limits scalability, and Mamba's linear-time selective SSM is a natural alternative. The CDSP regularizer is designed to be parameter-efficient by updating only the selective parameters \(\overline{C}, \overline{B}\) rather than the full model, which is a practical consideration.

- **The CDSP mechanism targets the over-balancing problem with a step-wise bias control approach.** The paper correctly identifies that prior TCP methods (CRN, CT) control confounding bias primarily at the final time step or via group-level adversarial balancing, which can distort covariate representations (the over-balancing problem, per Huang et al. 2024). CDSP's design — penalizing \(\|Cov(h_{t-1}, a_t)\|_2^2\) at each time step rather than globally — represents a genuinely different strategy that could preserve more covariate information.

- **Architectural adaptation (dropout replacing 1-d convolution) is motivated by the TCP setting.** The replacement is justified by the observation (citing Wang et al. 2024b) that Mamba's 1-d convolution, originally designed for token mixing in language, can cause overfitting on temporal data where neighboring time steps have strong sequential dependencies. This is a reasonable domain-specific adaptation.

## Weaknesses

### Fatal

None.

### Major

- **Missing experiments section (Section 5) in the provided manuscript.** The provided text jumps directly from Section 4.4 (Theoretical Analysis) to Section 6 (Conclusion), with no experimental results, dataset descriptions, baseline descriptions, ablation studies, hyperparameter settings, or evaluation metrics. The only empirical evidence is Figure 1 in the Introduction, which compares Mamba-CDSP against Causal Transformer on a single synthetic dataset (Tumor simulator). While this may be a parsing/extraction artifact, the paper's central claim — that "Mamba-CDSP not only outperforms baselines by a large margin, but also exhibits prominent running efficiency" — cannot be assessed from the available content. A new-method paper's evaluation is the core evidence for its contribution, and its absence here is the most significant weakness.

- **The derivation of the CDSP regularization term (Equation 3) contains a mathematically unjustified step.** The paper expands \(Cov(h_{t-1}, a_t)\) and then replaces \(Cov(K_i \tilde{X}_i^h, a_t)\) with \(K_i Cov(\tilde{X}_i^h, a_t)\), claiming this follows from "the property of cross-covariance." However, \(K_i = \overline{B}_i \prod_{j=i}^{t-1} \overline{C}_j\) depends on the learned selective parameters, which are functions of the input data. Because \(K_i\) is correlated with both \(\tilde{X}_i^h\) and \(a_t\), it cannot be treated as a constant and pulled out of the covariance operator in this way. This is not a minor notation issue — the entire CDSP regularizer \(\mathcal{L}_{\mathrm{CSDP}}\) is built on this step. Without a correction, it is unclear whether the proposed objective actually achieves the intended de-correlation, or whether it is simply penalizing something else. The paper would benefit from either (a) a corrected derivation that accounts for the data-dependence of \(K_i\), or (b) explicitly presenting CDSP as a heuristic regularization with an empirical rationale rather than as a mathematically derived objective.

- **The theoretical analysis (Theorem 1) is too sketchy to be informative.** The risk bounds involve multiple undefined or underspecified constants (\(r_1, r_2, r_3, C, \kappa_j, \overline{\sigma}\)), and the meaning of \(\eta\) (despite the "with probability \(1-2\eta\)" phrasing) is not explained. The three bounds differ only in the coefficient multiplying \(\|\mu_1 - \mu_2\|_2^2\), yet the paper does not discuss whether the CDSP bound is always tighter than the ADB bound — in fact, the ADB bound has a term involving \(\sigma_0 + \sigma_1\) that could be smaller or larger depending on the data. The assumptions (Gaussian covariates, linear outcome structure, omission of time indices) are restrictive and do not match the non-linear Mamba model used in the method. The analysis as presented adds little confidence in the method's theoretical properties.

### Minor

- **The C-MAMBA architecture description is vague on several implementation details.** The text says "input signals are embedded into the representation space with linear embedding" but does not specify how categorical treatments are encoded, how static features \(V\) are merged with time-varying features, or what the hidden state dimension is. These details matter for reproducibility.

- **The replacement of the 1-d convolution with dropout is motivated only by an empirical observation** ("we observe that the original Mamba model tends to overfit") without supporting evidence in the available text. No quantitative comparison (e.g., training vs. validation loss) is provided to demonstrate that overfitting occurs with the convolution and is resolved by dropout.

- **The paper acknowledges that CDSP is designed for linear SSMs (Section 6) but applies it to a non-linear Mamba model** (with silu activation in one branch). This inconsistency between the method's theoretical grounding and its practical implementation is noted in the limitations but not addressed — no analysis is provided to justify why the linear derivation should remain valid in the non-linear setting.

- **The claim that existing TCP methods "suffer from both the efficiency and the effectiveness" is supported only by a single comparison** (Causal Transformer on the Tumor simulator in Figure 1). No evidence is provided against other baselines (RMSNs, CRN, G-net, etc.) to demonstrate the generality of this claim.

- **The computational complexity remark in §4.3 is incomplete** — it begins comparing CDSP with adversarial balancing in terms of discriminator layers but is cut off ("4.3)") without a conclusion.

- **No discussion of the regularization hyperparameter \(\alpha\).** The combined loss is \(\mathcal{L}_{\mathrm{MSE}} + \alpha\mathcal{L}_{\mathrm{CSDP}}\), but the paper does not discuss how \(\alpha\) is set, whether it is tuned per dataset, or how sensitive results are to its value.

### Trivial

None (formatting/parser artifacts removed per guidelines).

## Nice-to-Haves

- A full ablation study separating the contributions of (a) the Mamba backbone itself vs. standard RNNs/Transformers, (b) the dropout replacement vs. original convolution, and (c) the CDSP regularizer vs. no regularizer vs. adversarial balancing.
- Specification of training details (batch size, optimizer, learning rate schedule, number of epochs, early stopping) and evaluation metrics (one-step vs. multi-step RMSE, factual vs. counterfactual metrics).
- Empirical quantification of the "over-balancing" problem (e.g., comparing covariate representation quality before and after balancing) to directly validate the motivation for CDSP.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No baseline that isolates the effect of the Mamba backbone from the effect of the CDSP mechanism"** — This claim assumes the absence of ablations in Section 5, which is missing from the provided text. Since the experiments section may exist in the original submission, this criticism is speculative. It is instead noted as a Nice-to-Have.
- **"The review of related work is broad but uncritical"** — This is a subjective stylistic judgment about literature review depth, not a substantive weakness about the paper's contribution.
- **"No mention of recent Mamba-based time series forecasting work"** — This demands the paper cover a different body of literature outside its stated scope (counterfactual prediction, not general time series forecasting).
- **"The expansion of the hidden state assumes no activation functions in the state transition"** — The Mamba SSM recurrence itself is linear (\(h_t = \overline{C} h_{t-1} + \overline{B} x_t\)); the silu activation is applied in a parallel branch before the SSM. The linear expansion of \(h_{t-1}\) in terms of historical inputs is valid for the SSM recurrence itself. The real issue (kept above) is about pulling data-dependent \(K_i\) out of the covariance, not about the linearity of the recurrence.
- **Strengths from Strength Finder removed:** The claim of "extensive empirical validation demonstrating substantial gains" is unsupported in the provided text (only Figure 1 is available). This is reframed as a potential strength conditional on the missing experiments section.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the mathematical flaw in the CDSP derivation and the incompleteness of the theoretical analysis, but these are critiques, not novel insights that reframe the paper's contribution in a new light.

## Suggestions

1. **Fix the CDSP derivation.** Either provide a corrected mathematical derivation that accounts for the data-dependence of the selective parameters, or explicitly reframe CDSP as an empirically motivated heuristic regularizer. The current "due to the property of cross-covariance" explanation is incorrect as written.
2. **Complete the theoretical analysis** by defining all constants, discussing the comparison between the three risk bounds (when is CDSP tighter than ADB? when is it not?), and connecting the restrictive assumptions to the actual non-linear model.
3. **Include a full experiments section** with multiple datasets, multiple baselines (RMSN, CRN, G-net, CT), ablations separating the three modifications (Mamba backbone, dropout replacement, CDSP), and runtime measurements. Report how \(\alpha\) is set and its sensitivity.
4. **Clarify the architecture details**: how categorical treatments are embedded, how static features are handled, hidden state dimensions.

## Score and Decision

This paper proposes a timely and novel combination of Mamba with a covariance-based regularizer for TCP, and the core research direction is worthwhile. However, the provided manuscript has two severe structural problems: (a) the mathematical derivation of the main proposed mechanism (CDSP) contains a step that is not generally valid, and (b) the experiments section — the central evidence for a new-method paper — is absent from the provided text. The theoretical analysis is too sketchy to convincingly support the claimed advantages. The ideas are promising, but the paper in its current form does not provide a sound, complete, or verifiable argument for acceptance.

**Score:** 4.0/10  
**Decision:** Reject

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>