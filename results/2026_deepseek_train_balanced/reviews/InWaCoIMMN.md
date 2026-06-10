## Summary

This paper introduces CALM (Competence-based Analysis of Language Models), a framework for measuring LLM "linguistic competence" via causal probing, along with Gradient-Based Interventions (GBIs), a new causal probing methodology that uses adversarial attacks against differentiable probes to manipulate internal representations. A case study applies CALM+GBI to BERT and RoBERTa on 14 LAMA ConceptNet lexical inference tasks.

## Strengths

1. **Formal quantitative competence metric (Eqn. 2, lines 147–150).** The paper operationalizes the previously informal notion of "linguistic competence" for LLMs as an expectation over interventions against a ground-truth causal model, bounded in [0,1]. This is the first quantitative measure of LLM competence that goes beyond prior causal probing work.

2. **GBIs address a known limitation of prior causal probing methods.** The paper correctly identifies that INLP and kernel INLP suffer from "recoverability" because they assume linear representations (lines 158–160). The GBI approach works with any differentiable probe (lines 168–169), expanding the scope of causal probing to nonlinearly-encoded properties.

3. **Constrained adversarial attack formulation improves over prior unconstrained GBI work.** The paper identifies (lines 330–333) that prior work used unconstrained gradient descent without limiting perturbation magnitude, and introduces a constrained formulation (FGSM, ε=0.1) to better control collateral damage to representations.

## Weaknesses

### Major

- **The paper's central claim that CALM can "explain and predict" LLM behaviors is not supported by the evidence.** The headline quantitative finding (Section 5.2, line 287) is a Spearman correlation ρ=0.508 with p=0.064 between accuracy differences and competence differences across tasks. This is not statistically significant at conventional thresholds (p<0.05). Moreover, the paper never defines a prediction task, never holds out data to test predictive power, and never compares predicted to actual behavior. The "explanation" offered (lines 294–297) is a post-hoc reinterpretation of scores, not a finding independently validated against an alternative account. The abstract (line 13), contributions (line 50), and conclusion (line 350) all claim that CALM "explain[s] and predict[s]" behavior — this is substantially overstated relative to the evidence.

- **The GBI methodology is not validated to confirm it actually intervenes on the intended property.** The paper acknowledges this circularity in principle (lines 362–364) but provides no experimental validation. The most basic sanity check — measuring whether the probe's prediction on the intervened representation matches the target counterfactual value — is not reported. Without this, the competence scores rest on an untested assumption that GBIs manipulate what they claim to manipulate. This is especially important given the paper explicitly notes that GBIs cannot provide the strong theoretical constraints on collateral damage that methods like INLP offer (lines 362–363).

- **There is a potential layer mismatch between probe training and intervention application.** Probes are trained on each model's *final hidden layer* (line 236), but the GBI methodology extracts embeddings from some layer *l*, applies the gradient-based attack there, and feeds the modified representation into subsequent layers *L = l+1,...,|L|* (lines 181–183, 188–191). The paper does not specify which layer *l* is used for interventions, nor whether the probe is retrained on representations from that layer. If *l* is not the final layer, the probe's decision boundary at layer *l* may not correspond to the decision boundary at the layer it was trained on, potentially compromising the intervention target.

### Minor

- **Probe accuracy is not reported.** The probe (2-layer MLP) is central to the GBI methodology, yet its ability to reliably predict the target property from model representations is never presented. If the probe performs poorly, GBIs are attacking a straw target, and the resulting competence scores become unreliable.

- **No comparison to alternative causal probing methods.** The paper does not compare CALM/GBI results to what would be obtained with INLP-based interventions (the most directly comparable prior approach). Without this, it is unclear whether GBI provides different or better information than existing methods — especially given the paper's own note (lines 365–367) that INLP can be used when strong constraints on collateral damage are needed.

- **Within-task variance across random probe seeds is non-negligible but not discussed.** The error bars in Figure 3 (showing min/max across 10 random probe initializations) span 0.2 competence points or more for several tasks, which is large relative to the 0.3–0.5 mean values and the ~0.05 BERT-vs-RoBERTa difference. This suggests the competence measure is sensitive to probe initialization; the paper does not analyze or discuss this.

- **The independence assumption across tasks, while acknowledged, limits interpretability.** The paper notes (footnote, line 221; Limitations, line 374) that treating all non-causal relations as equally non-causal is a simplification. However, when properties like "CapableOf" and "HasProperty" share substantial mutual information, a competent model *should* change its predictions when one is intervened upon — and the current metric would incorrectly penalize this as incompetence. The aggregate scoring approach cannot separate genuine incompetence from this structural confound.

### Trivial

- The competence scores for the 14 tasks are only shown in a bar chart (Figure 3); numerical values would aid comparison and reproducibility.
- The correlation description (line 287) appears to contain a reporting error: it states "between the average difference in accuracy and average difference in performance" — given the context (discussing competence differences, line 286) the second term should likely be "competence."

## Nice-to-Haves

- Reporting component scores separately (impact of intervening on causal vs. environmental properties) rather than only the aggregate competence metric would make results more interpretable.
- A sensitivity analysis on the perturbation bound ε and inclusion of PGD results in the main paper (currently deferred to appendix) would strengthen the methodological validation.
- Using competence scores from a subset of tasks to predict held-out performance differences under distribution shift would turn the current correlational finding into a genuine predictive test.

## Removed Points

The following points from the inputs were removed with justification:
- **"Competence metric's experimental operationalization deferred to appendix"** — The main paper describes the experimental setup (one-hot encoding, top-k overlap scoring) adequately. Deferring the exact formula to the appendix is standard practice. The paper states at line 375 that impacts are "summed across 14 widely-varying lexical relation types," providing the key aggregation detail.
- **"No sensitivity analysis on ε"** — Partially addressed: PGD results are deferred to the appendix, and the main paper reports one ε value. This is common for main paper / appendix splits.
- **Strength: "Case study provides direct empirical evidence that CALM can decompose model behavior"** — The evidence is too weak (p=0.064 correlation) to constitute a genuine strength; removed as overclaimed.
- **Strength: "Competence metric exhibits a moderately strong positive correlation"** — Same issue; a non-significant correlation does not warrant listing as a strength.
- **"The raw intervention effect sizes broken down by causal vs. environmental properties are never reported"** — Downgraded from the harsh critic's framing to the Nice-to-Haves section; it is a useful addition but not a core weakness.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder recognized the same core trade-off: a well-motivated framework with insufficient empirical validation. No synthetic insight emerged beyond what the authors and reviewers each identified independently.

## Suggestions

1. **Validate the GBI intervention.** Report the intervention success rate: after a GBI attack targeting property Z, what fraction of the time does the probe's prediction on the intervened representation match the intended counterfactual value? This is the single most important missing piece.

2. **Clarify or resolve the layer mismatch.** Specify which layer l is used for interventions. If l is not the final layer, retrain probes on representations from that layer, or justify why the final-layer probe generalizes.

3. **Temper the "explain and predict" claim.** The current evidence supports a correlation (with marginal significance), not prediction. Reframe claims to match what was actually demonstrated, or add a genuine prediction experiment (e.g., using competence scores to forecast behavior under distribution shift).

4. **Report probe accuracy** for each property and model to establish that the intervention target is meaningful.

5. **Report separate causal and environmental intervention effects** rather than only the aggregate competence score, making the results more interpretable.

## Score and Decision

This paper makes a genuine conceptual contribution: formalizing LLM competence and developing GBIs as a causal probing tool. The framework is well-motivated and clearly presented. However, the empirical case study does not deliver on the paper's central claims. The evidence is limited to a non-significant correlation with no prediction task, the GBI methodology is not validated, and there is an unresolved methodological concern about probe layer mismatch. For a top-tier venue like ICLR, the empirical validation must match the ambition of the claims. The paper needs substantial strengthening before it is ready.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>