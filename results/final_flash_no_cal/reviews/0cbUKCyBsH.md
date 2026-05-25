Now I'll synthesize the final review.

## Summary

This paper argues that a fundamental "self-stimulation" assumption — predicting the future using only historical time series values — imposes a mathematical error bound that cannot be broken by scaling models alone. Through a control-theoretic analysis, it proposes Influence-Aware Time Series Forecasting (IATSF), a paradigm that incorporates textual external influences to break this barrier. The paper contributes a formal theoretical framework (Propositions 2.1 and 3.1), a leak-free benchmark with temporally-synced textual influences, and FIATS, a lightweight LLM-free model whose CASM and CAPS mechanisms operationalize the theory. Controlled synthetic experiments show FIATS approaching the theoretical error bound while foundation models fail catastrophically, and real-world experiments on traffic, game user activity, and atmospheric physics show consistent gains over strong baselines.

## Strengths

- **Clean controlled validation of the core theoretical claim.** The FM Toy experiment (Table 1, Section 6.1) provides direct empirical evidence for Proposition 2.1: FIATS achieves near-zero MSE (0.003) while foundation models like Chronos-L (0.012) and Moirai-L (0.013) produce collapsed, averaged-out forecasts. This cleanly isolates the "self-stimulation barrier" from model-capacity confounds, making the theoretical point concretely.

- **Architecture explicitly derived from theory, with ablations confirming the derivation.** The CASM mechanism is designed as a learnable implementation of the `CB` sensitivity matrix from the paper's linear system formulation `X_f = CAZ_h + CB U_f`. The ablation study (Table 3) verifies this: removing channel descriptions ("Zero Desc.") degrades MSE from 0.182 to 0.209 at horizon 96, confirming that CASM's channel-specific sensitivity modeling — not just the presence of text — drives the gains.

- **Well-motivated benchmark design principles.** The leak-free, temporally-synced benchmark (Section 4.1) explicitly addresses contamination issues in prior multimodal TSF datasets (e.g., future state information leakage). The requirement that influences be independently evolving and not directly describe the time series trajectory is a principled contribution that provides a template for future work.

- **Empirical validation of the partial-influence efficacy theory.** Figure 6 directly tests Proposition 3.1 by injecting noise into influence inputs. The graceful degradation in performance (rather than a cliff) provides a concrete empirical link between the theoretical claim that imperfect influence reduces uncertainty and practical robustness.

- **Interpretability through CASM attention maps.** Figure 5 reveals the learned sensitivity weights between specific textual sentences (e.g., "Pressure," "Weather") and individual time series channels, providing transparency that is genuinely useful for understanding which influences drive which channels.

## Weaknesses

### Fatal
None.

### Major

- **The Atmospheric Physics dataset creates a tension with the paper's own leak-free definition.** The leak-free principle (Section 4.1) requires that influences be "independently evolving" and not "directly describe or summarize the time series trajectory." The Atmospheric Physics dataset (Section 4.2) uses weather forecasts as the "influence" while forecasting atmospheric variables (solar radiation, pressure, dew point) — i.e., the same physical system that the weather forecast describes. A forecast of "clear skies" is not an independent external control input for solar radiation; it is a prediction of the future state of the target system. While the paper anticipates this by allowing "predictions of U_f from expert sources" (line 113), the conceptual tension remains: if the influence modality describes the same physical quantities as the target, the experiment cannot cleanly support the paradigm's claim that external *influence-awareness* — rather than multi-modal information access — breaks the barrier. The NYC Traffic dataset (weather → traffic) and GAUD (developer logs → game activity) are clean on this dimension, but Atmospheric Physics is the headline complex-system result and its results are therefore ambiguous as evidence for the core theoretical narrative.

### Minor

- **The theoretical contribution is presented with inflated novelty.** Proposition 2.1 (the self-stimulation error bound) is essentially the law of total variance / omitted-variable bias expressed in control-theoretic notation. While the framing for deep learning TSF is novel and valuable, the claim that this is a "hard, mathematical barrier" that the community has "universally overlooked" overstates the case given decades of work on ARIMAX, VARX, state-space models with inputs, and econometric treatments of omitted variables. The paper's genuine novelty lies in the *application* of these ideas to textual influence modeling in deep TSF, not in the discovery of the barrier itself. Recalibrating this narrative would strengthen credibility.

- **Missing variance or uncertainty estimates throughout the experiments.** All results in Tables 1 and 3 report point estimates to three decimal places with no standard deviations, confidence intervals, or multi-run statistics. Since the paper argues its gains are structural and decisive (e.g., FIATS 0.003 vs. PatchTST 0.006 on FM Toy, or FIATS 0.182 vs. FIITS 0.248 on Atmospheric Physics), the absence of any replication-based uncertainty measure makes it impossible to assess statistical reliability. This is standard practice in much of the TSF literature but is especially conspicuous given the strength of the claims.

### Trivial

- **FIITS is not defined in the main body.** The acronym "FIITS" appears in Table 1 but is never explained in the visible main text. Context suggests it is "FIATS without influence input," but this should be stated explicitly.

## Nice-to-Haves

- A discussion of how temporally correlated influences (e.g., persistent weather patterns) interact with the assumption that influences are independently evolving stochastic variables would strengthen the theoretical framing.
- Adding at least one clean real-world dataset where the textual influence is a genuinely *independent external variable* (e.g., policy announcements for economic data, news events for industrial systems) would fully resolve the Atmospheric Physics tension and make the empirical case airtight.
- A brief explicit note on what FIITS stands for and how it is constructed.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The paper largely ignores the substantial existing literature on exogenous variable handling (ARIMAX, VARX, SSMs)."* — The paper does mention ARIMAX (line 37) and explicitly scopes its contribution to textual influences, not traditional exogenous variables. The criticism expects engagement with literature outside the paper's stated scope. Removed per scope-creep filter.

2. *"The writing has formatting artifacts"* — These are parser issues from PDF extraction, not author errors. Removed per hard rule.

3. *"Missing related work citations"* — The merger cannot independently verify the existence of missing citations. Removed per hard rule.

4. *Strength Finder's claim that the paper "provides a clean, rigorous experimental testbed that isolates the effect of genuine influence-awareness"* — This conflicts with the verified weakness about the Atmospheric Physics dataset's leak tension. Per the rule "when a strength and weakness disagree, the weakness wins," this strength is removed.

5. *Strength Finder's generic framing strengths such as "this paper addressed an important problem"* — Such generic statements are dropped per the filtering instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the Atmospheric Physics tension directly.** Either (a) replace this dataset with one where the textual influence is unequivocally an external factor (e.g., policy documents for economic indicators, news events for supply-chain metrics), or (b) provide a substantive defense showing that weather forecasts constitute a genuinely independent influence modality (e.g., because the forecast is generated by a different physical model with different inputs, and does not directly encode the specific measurement-station values). If (b) is chosen, explicitly reconcile the dataset with the paper's own leak-free definition.

2. **Add uncertainty estimates.** Report means and standard deviations over multiple random seeds (3–5 runs) for the main tables. If computational cost is prohibitive, disclose this and report at least one multi-run experiment as a proxy.

3. **Recalibrate the theoretical narrative.** Acknowledge the connection to classical omitted-variable results and reframe the contribution as the application of control-theoretic modeling to *textual* influence integration in deep TSF, rather than the discovery of a previously unknown barrier. The FIATS architecture and the leak-free benchmark are the paper's strongest contributions; they do not need the maximal novelty framing to be impressive.

4. **Define FIITS explicitly** in the experimental setup or baseline description.

## Score and Decision

The paper makes an interesting and well-motivated contribution. The theoretical framing, while rooted in standard ideas, provides a useful lens for the TSF community, and the FIATS model is cleanly designed and convincingly ablated. The FM Toy experiment is a particularly strong and clean demonstration. However, the Atmospheric Physics dataset creates a genuine tension with the paper's own leak-free principle that undermines the flagship complex-system result. This is addressable and does not invalidate the paper's other contributions, but it prevents the empirical case from being fully conclusive. I recommend acceptance contingent on the authors addressing this concern and recalibrating the novelty claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>