Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper proposes DICE (Bootstrapping with **D**PO **I**mpli**C**it r**E**wards), an iterative alignment method that uses the implicit reward model from a DPO-trained LLM to construct new preference data, which is then used for further DPO training rounds. The authors augment this core idea with length-regularized reward shaping (to counteract length exploitation) and experience replay (to mix high-quality offline data with on-policy generated data). On AlpacaEval 2, DICE improves the length-controlled win rate of Llama-3-8B-DPO from 18.20% to 27.55%, outperforming Gemini Pro (24.38%) with only 8B parameters and without external feedback.

## Strengths

1. **Novel and well-motivated use of DPO implicit rewards for bootstrapping.** The observation that the DPO implicit reward (Equation 3) can itself serve as a preference signal for iterative self-alignment is non-obvious and elegantly extends the DPO framework. The paper clearly articulates why this is possible (Section 4) and illustrates the pipeline in Figure 1.

2. **Length-regularized reward shaping is empirically effective.** The paper diagnoses the length bias issue directly (Figure 2 shows a mean length difference of +1031 tokens under vanilla implicit rewards) and proposes a simple reward shaping term that reduces this to −21 tokens. The ablation study (Table 3, lines 236-238) confirms that this component is critical for LC win rate gains and that the α-search procedure (Equation 5) finds a good operating point.

3. **Experience replay provides clear, quantifiable benefit.** The γ sweep (Figure 3) shows that mixing offline data (γ=0.5) outperforms both pure generated data (γ=0) and pure offline data (γ=1), providing direct evidence that the method balances on-policy freshness with retention of initial knowledge. This is a clean experimental result.

4. **Strong empirical gains on AlpacaEval 2 with thorough ablations.** DICE improves LC win rate by 9.35% (Llama3) and 8.02% (Zephyr) over base models, and the ablation study validates each component (LR shaping, experience replay) individually. The demonstration that DICE-generated data works with KTO, IPO, and Hinge loss (Section 5.2) shows the generated preference data has value beyond DPO itself.

5. **Transparency about limitations.** The paper openly acknowledges the plateau after 2–3 iterations (line 245) and the reliance on a well-trained initial DPO model (lines 245-246), which gives readers a realistic picture of the method's scope.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (DICE improves DPO-trained models; its components each contribute to the gain) are supported by the evidence presented. The weaknesses below are substantive but do not invalidate the results.

### Minor

1. **Evaluation on a single benchmark.** The paper evaluates only on AlpacaEval 2.0 (line 185). While this is a standard alignment benchmark, the method is presented as a general alignment technique, and many papers in this space report results on MT-Bench, TruthfulQA, or other held-out evaluations to demonstrate generalization. Without broader evaluation, it is unclear whether the observed gains reflect genuine alignment improvement or exploit characteristics of the GPT-4-based judge / AlpacaEval prompt distribution. The length-controlled win rate mitigates length exploitation concerns but does not address other forms of overfitting.

2. **No direct validation of implicit reward accuracy as a preference judge.** The entire bootstrapping pipeline depends on the implicit reward model (Equation 3) to label which on-policy responses are winning and losing. The paper acknowledges this reward is an "approximate proxy" (line 21, line 159) but never measures how accurate it is — e.g., by checking agreement with human judgments on a held-out set or comparing against a trained external reward model. The ablation study shows length regularization helps, but it does not validate whether the *direction* of preference is correct. If the implicit reward is systematically biased beyond length, the constructed dataset may contain incorrect labels that get reinforced across iterations.

3. **Hyperparameter γ appears to be tuned on the test metric.** The paper reports a sweep of γ ∈ {0.0, 0.25, 0.5, 0.75, 1.0} and selects γ=0.5 based on AlpacaEval 2 LC win rate (Figure 3). No separate validation set is described (line 174 does not mention one). This means the hyperparameter is effectively optimized on the evaluation benchmark, which weakens the claim of generalizability. The sweep is informative, but reporting the result on a held-out set or using a tuning procedure not tied to the test metric would be more rigorous.

4. **Limited evidence for sustained improvement and no analysis of the plateau.** The paper observes that improvements plateau after two iterations (line 245: "we did not observe continuous improvement in our model beyond three iterations"). For a bootstrapping method, understanding *why* the implicit reward ceases to provide useful signal is important. The paper does not analyze round-by-round dataset quality (e.g., label consistency, margin distributions, or overlap with human preferences), leaving an open question about whether the method is a genuinely iterative procedure or a one-to-two-step trick.

5. **Theoretical analysis (Section 4.1) is simplified intuition, not a formal justification.** The analysis considers a single losing response and argues that minimizing its probability suffices. In practice, DPO operates over many pairs with a softmax ratio affecting all responses simultaneously. The argument that on-policy sampling alleviates the "never-sampled" issue assumes that a suboptimal response with high probability will be sampled and used as a losing example in the *same* round — but sampling is stochastic and the probability shifts during optimization. The analysis provides useful intuition but the paper presents it as formal justification (lines 109-130). This does not invalidate the empirical results, but the theoretical framing oversells what is actually shown.

### Trivial
None.

## Nice-to-Haves

- **Validate the implicit reward model.** Computing agreement between the implicit reward's pair choices and human preferences on a small held-out set (e.g., a subset of UltraFeedback or Anthropic-HH) would directly test the core assumption of the method.
- **Evaluate on at least one additional benchmark** (e.g., MT-Bench, or a small-scale human evaluation). This would address concerns about benchmark-specific overfitting.
- **Analyze constructed dataset quality across rounds.** E.g., measure proportion of pairs where the implicit reward agrees with an external reward model, or track reward margin distributions over iterations. This would shed light on why the method plateaus.
- **Decouple hyperparameter tuning from the test metric** by using a separate validation split.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- *"Missing comparison with iterative DPO using an external reward model"* — Removed because the paper explicitly scopes out external models (line 28: "Our experiment excludes approaches requiring external models... as they are beyond this work's scope"). This is a deliberate scope choice, not an omission.
- *"Length regularization is not principled; other biases are not addressed"* — Removed because the paper addresses the known problem of length exploitation specifically and transparently. No method addresses all possible biases at once.
- *"A direct controlled comparison with Gemini Pro is not performed"* — Removed because fine-tuning a closed-source API model is practically infeasible for academic authors. The leaderboard comparison is standard practice.
- *"Various formatting and reproducibility nitpicks"* — Removed per instructions (parser artifacts; standard academic resource constraints).

## Novel Insights

The reviews surface an interesting tension: the paper's core success depends on the quality of the DPO implicit reward as a preference judge, yet this quality is never directly measured. The method works empirically (as shown by the AlpacaEval 2 gains), but the absence of validation creates ambiguity about *why* it works — is the implicit reward genuinely good at distinguishing quality, or does the combination of length regularization and experience replay compensate for its deficiencies? The plateau after 2–3 iterations further suggests that whatever signal the implicit reward captures is depleted quickly, hinting that the reward's utility may be limited to correcting a specific set of errors in the initial DPO policy rather than enabling open-ended improvement. A deeper analysis of the constructed dataset's properties (label flip rates, margin distributions, agreement with held-out judgments) would significantly strengthen the contribution and is the most actionable recommendation across both reviews.

## Suggestions

1. **Validate the implicit reward's preference accuracy.** Compute agreement between the implicit reward's pairwise choices and human preferences on a subset of a held-out preference dataset (e.g., 500-1000 examples from Anthropic-HH or UltraFeedback). Report agreement rates and analyze failure cases. This would directly address the most significant structural concern.
2. **Add evaluation on MT-Bench or another standard LLM benchmark** to demonstrate that gains on AlpacaEval 2 are not due to benchmark-specific overfitting. Even reporting results on a few held-out instruction-following or safety benchmarks would substantially strengthen the paper.
3. **Analyze why improvement plateaus.** For rounds 1, 2, and 3, compute (a) the agreement between the implicit reward and the offline dataset's original labels, (b) the reward margin between winning and losing responses, and (c) the rate at which pairs are re-labeled across rounds. This would illuminate whether the implicit reward becomes less discriminating or noisier as the policy improves.
4. **Use a validation set for hyperparameter tuning** (e.g., hold out 10% of the training prompts) and report test-set results only for the best configuration found on validation, or clarify if the sweep in Figure 3 is on a separate evaluation set.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>