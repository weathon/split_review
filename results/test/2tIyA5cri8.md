Now I have a thorough understanding of the paper and all the review claims. Let me draft the final consolidated review.

---

## Summary

This paper investigates whether Llama 3 70B implements temporal difference (TD) learning in-context across three tasks (Two-Step Task, Grid World, graph structure learning). Using sparse autoencoders (SAEs) trained on residual stream activations, the authors identify latent features that correlate with TD errors and Q-values from fitted RL models. Causal intervention experiments (lesioning or clamping these latents) produce predictable behavioral and representational changes, supporting the claim that these features are causally involved in in-context RL computations. The paper combines behavioral modeling, representational correlation analysis, and causal manipulation across multiple task settings.

## Strengths

1. **Multi-method evidence for TD-like representations**: The paper combines behavioral model comparison, representational correlation (SAE latents vs. TD errors, Q-values, SR), and causal intervention across three distinct tasks. This triangulation of evidence is a strength — the correlational findings (r = 0.58–0.60 for TD errors; r ≥ 0.75 in Grid World) are reinforced by lesion experiments showing that deactivating TD-correlated features degrades performance while deactivating low-correlation features does not.

2. **Causal manipulation demonstrates specificity**: In the Grid World task, lesioning four TD latents (r ≥ 0.75) significantly degrades action prediction accuracy, whereas lesioning the lowest-correlation features from the same blocks produces minimal effects (Figure 4D). This control directly addresses the concern that effects could be non-specific artifacts of SAE reconstruction.

3. **Cross-task generality**: The same TD-learning mechanism is identified across three settings — a simple two-step MDP (trial-and-error learning), a 5×5 grid world (action prediction for a Q-learning agent), and a community-graph random walk (successor representation learning). The graph learning task is particularly elegant, showing that the phenomenon extends beyond reward-driven RL to statistical structure learning.

4. **Surprising emergence without RL training objective**: Llama 3 70B was trained only on next-token prediction yet implements a canonical RL algorithm in-context, with the smaller 8B variant failing (Figure 2A), suggesting the ability scales with model size. The controlled experiment showing Llama predicts actions better with correct vs. random rewards (Figure 4A) confirms that the model specifically integrates reward information rather than merely learning action sequences.

## Weaknesses

### Fatal
None.

### Major

- **Behavioral model comparison lacks statistical rigor for the "best captured by Q-learning" claim.** The paper reports raw NLL values (Q-learning: 2729, myopic: 2864, repetition: 5745) without error bars, confidence intervals, or model selection metrics (AIC/BIC) that account for differences in parameter count. The Q-learning model has more free parameters (learning rate, discount factor, temperature) than the myopic model (γ fixed to 0), so raw NLL is insufficient. While the NLL difference of 135 is substantial, without uncertainty quantification or parameter-corrected metrics, the claim that behavior is "best captured by Q-learning" is weaker than stated. Additionally, only three simple models are considered; the paper's own limitations mention that adding a repetition bias could improve fits, but this model is not tested. **Why it matters**: This is the paper's primary behavioral evidence that Llama implements TD learning specifically. Fortunately, the representational and causal evidence is largely independent of this behavioral modeling.

### Minor

- **Missing full-reconstruction baseline in intervention experiments.** The paper's causal claims rest on comparing TD-feature lesions against lowest-correlation-feature lesions (a valid control that shows specificity). However, a standard additional baseline — replacing activations with the full SAE reconstruction *without any lesion* — is not reported. While the existing control (lowest-correlation lesion does not degrade performance) already indicates the reconstruction process is not broadly harmful, including the full-reconstruction baseline would more cleanly separate reconstruction-quality effects from feature-specific effects. This is a standard practice in SAE intervention studies and would strengthen the paper's core causal claim.

- **Correlation magnitudes leave room for alternative interpretations.** Maximum correlations of r = 0.58–0.60 with TD errors mean ~60–65% of variance is unexplained. While this is reasonable for neural/representational data and the causal experiments help establish specificity, the paper could more explicitly acknowledge that these latents may correspond to a broader class of prediction-error or surprise signals that correlate with TD errors without being exclusively tied to value-update computations. The fact that the same latent in the Two-Step task also correlates with myopic values suggests it may be encoding a composite signal.

- **SAE architecture details are underspecified.** The paper does not report the latent dimension of the SAEs or the sparsity level achieved (e.g., average active features per token). These details are relevant for assessing whether the learned features are genuinely sparse and interpretable, and for evaluating how many features were available to capture TD-related signals.

- **SR correlation computation needs clarification.** The successor representation is a state-by-state matrix (vector-valued per state), but SAE latents produce scalar values per token. The paper does not describe how these are matched for correlation analysis — whether the authors correlate with the full SR row, a scalar summary, or the scalar TD error from Eq. 5.

- **Gaussian smoothing (σ = 0.5) applied to block-wise correlations** is mentioned in a figure caption but its motivation is not explained in the main text. Raw (unsmoothed) correlations should be shown or included, as smoothing could obscure fine-grained block-level patterns.

### Trivial

- SAE training epochs differ across tasks (30 epochs for Two-Step, 15 for Grid World) without justification. This is likely due to different dataset sizes but should be noted.
- The paper uses "myopic Q-learning" and "myopic values" terminology which could cause confusion — standard RL terminology would be "reward-only" or "γ=0" model rather than suggesting a Q-value that ignores future rewards.

## Nice-to-Haves

- Fit behavioral models to Llama's choices in the Grid World task (not just Two-Step), to strengthen the parallel between tasks.
- Test whether lesioning TD latents affects performance on a non-RL control task (e.g., simple next-token prediction on unrelated text) to demonstrate that the intervention does not cause general degradation.
- Consider fitting a mixed model combining value-based learning with a repetition bias (as noted in the limitations) to directly test this alternative.
- The paper could strengthen the behavioral model comparison by reporting AIC/BIC values and bootstrapped confidence intervals for the NLL differences.

## Removed Points

- "The paper does not examine attention outputs or MLP activations" — The paper explicitly acknowledges this as a limitation/future work direction (Section 7.1: "Do attention outputs carry important information that is not immediately available in the residual stream?"). Scope limitation already addressed.
- "The behavioral models do not account for the possibility of SARSA, Bayesian RL, Dyna" — These are reasonable but speculative alternatives. The claim is not that Q-learning is the uniquely correct model, but that it best fits among the tested alternatives. The paper's limitations section already acknowledges imperfect alignment. The demand to test every possible RL algorithm is scope creep.
- "The paper should include a comparison with a model that combines value learning with a repetition bias" — The limitations section (Line 179) explicitly mentions this: "adding a preference for repetition to the Q-learning model can be a natural extension." This is already identified as future work.

## Novel Insights

Beyond the paper's own contributions, the most interesting aspect that emerges from the reviews is the parallel tension between the behavioral and representational evidence: the behavioral model comparison is relatively weak (only three models, no statistical rigor), yet the representational and causal evidence is compelling and largely independent. This means the paper's core claim about TD-like representations does not stand or fall on the behavioral modeling alone — a point that could be clarified by the authors. The graph learning task (SR) is a particularly clever experimental design because it separates the TD learning mechanism from reward-driven learning, showing that the same computational primitive appears in a purely statistical learning context.

## Suggestions

1. **Add the full-reconstruction baseline** to the intervention experiments (all tasks). Report whether replacing activations with the full SAE reconstruction preserves the model's original behavior. This is the single most impactful improvement.

2. **Strengthen behavioral model comparison**: Report AIC/BIC values, bootstrapped confidence intervals for NLL differences, and consider adding a model that combines Q-learning with a repetition bias (as noted in limitations).

3. **Report SAE details**: Include the latent dimension size, sparsity level (average active features per token), and justification for differing training epochs across tasks.

4. **Clarify SR correlation computation**: Describe how the vector-valued SR is correlated with scalar SAE latents.

5. **Show raw (unsmoothed) block-wise correlations** alongside or in addition to the Gaussian-smoothed versions.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>