Here is the consolidated final review.

---

## Summary

This paper identifies and analyzes three interrelated optimization problems with Direct Preference Optimization (DPO), termed the **3D-properties**: (1) Drastic drop in the likelihood of rejected responses, (2) Degradation into response suppression (where the gradient for chosen responses vanishes), and (3) Dispersion of probability mass to unseen responses. The authors derive the gradient ratio ∂ℓ/∂π⁻ / ∂ℓ/∂π⁺ = −π⁺/π⁻ to explain why the rejected-response gradient dominates asymptotically, validate the predicted dynamics with a toy model, conduct controlled on-policy vs. off-policy experiments on Baichuan2 LLMs (confirming on-policy DPO mitigates the effects), contrast DPO's instability with the balanced gradients of RM training, and propose Flex-DPO and SFT-augmented regularization as partial remedies. The contribution is primarily analytical/explanatory rather than a new state-of-the-art algorithm.

---

## Strengths

- **Closed-form gradient ratio derivation**: Section 3.1 (Corollary 1) derives ∂ℓ/∂π⁻ / ∂ℓ/∂π⁺ = −π⁺/π⁻, the first explicit mathematical explanation for why the rejected-response likelihood drops faster than the chosen-response likelihood. This goes beyond the qualitative observations in prior work (Feng et al., 2024).

- **Toy model isolates the causal dynamics**: Figure 2 tracks chosen/rejected/unseen likelihoods alongside gradient magnitudes over training, directly visualizing the degradation phase where ∂ℓ/∂π⁺ vanishes while ∂ℓ/∂π⁻ diverges, then unseen likelihood rises. This synthetic isolation provides stronger causal evidence than the correlational analyses in earlier work.

- **Controlled on-policy vs. off-policy ablation on real LLMs**: Table 1 reproduces the toy model's four scenarios on Baichuan2-13B with MATH* and SuperCLUE-Math. Scenario 1 (both chosen and rejected on-policy) outperforms others by clear margins (e.g., 3.85 vs. 3.60 on MATH*). This factorial experiment directly validates that distribution gap modulates 3D-properties.

- **Formal contrast showing RM training avoids 3D-properties**: Section 3.4 (Equation 10) derives symmetric gradients for RM's chosen and rejected logits (−σ(r⁻−r⁺) and σ(r⁻−r⁺)), which never diverge as DPO's do. This mathematical contrast explains RM-based methods' inherent stability and is corroborated by the accuracy curves in Figure 5.

- **Quantitative regularization sweep with trade-off finding**: Figure 4 varies β⁻ in Flex-DPO and finds a non-monotonic performance curve peaking around 0.08. This reveals that over-suppressing the rejected gradient harms generalization — a nuanced, non-obvious empirical finding that guides practical application.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical gap: probability-level gradients do not directly translate to parameter-level updates (undermines the theoretical claim but not the empirical evidence)**
   The core theoretical apparatus (Corollaries 1–3, Section 3.1) computes partial derivatives of the DPO loss with respect to the *probability outputs* π⁺ and π⁻. However, the actual parameter gradient is ∇_θ ℓ = (∂ℓ/∂π⁺)·∇_θ π⁺ + (∂ℓ/∂π⁻)·∇_θ π⁻. The claimed dominance of the π⁻ gradient during optimization follows only if ‖∇_θ π⁺‖ and ‖∇_θ π⁻‖ are comparable in magnitude and direction. For a neural network with shared parameters (especially when chosen and rejected responses share tokens), this may be approximately true, but the paper neither argues for nor empirically verifies this assumption. Additionally, Corollary 2's limit analysis (∂ℓ/∂π⁻ → ∞ as π⁻ → 0) does not account for the fact that ∇_θ π⁻ itself contains a factor π⁻(1−π⁻) in softmax-parameterized models, which could partially counteract the blow-up. The paper's empirical evidence (toy model, real LLM experiments) independently confirms the predicted phenomena, so this weakness does not invalidate the overall argument — but the theoretical derivation as presented is less rigorous than claimed, and this gap should be acknowledged and addressed.

2. **Flex-DPO is critically underspecified (not reproducible as written)**
   Section 3.3 introduces Flex-DPO as using "adaptive values of β" to moderate the decline of rejected-response likelihood. Section 4.3 then describes: "we fixed β⁺ and systematically decreased β⁻." Figure 4 shows a sweep of *static* β⁻ values. It is entirely unclear whether β⁻ is (a) a static per-training-run hyperparameter chosen from a sweep, (b) a dynamically scheduled value that changes during training, or (c) a per-sample adaptive quantity. The term "adaptive" is misleading given the experimental description, and the method cannot be reproduced from the paper alone. The authors must specify the exact mechanism.

3. **PPO comparison (Section 4.5, Table 2) lacks essential implementation details, making the comparison uninformative**
   The paper states that DPO underperforms "RLHF-PPO" on poem and slogan generation but provides zero details about the PPO implementation: reward model architecture and training procedure, KL penalty coefficient, number of PPO iterations/epochs, learning rate, batch size, how the reward model was trained on the preference data, or any hyperparameters. Without these, the comparison cannot be assessed for fairness or statistical validity, and the strong claim that "its superiority stem largely from avoiding the 3D-properties" (abstract) is not adequately supported by this experiment.

### Minor

4. **No statistical significance or variance reporting**
   Tables 1, 2, and Figure 4 present results without measures of variance (standard deviation, confidence intervals) or multiple seeds. Given the on-policy/off-policy comparison is a central experiment, single-run results weaken the conclusions.

5. **GPT-4-as-judge evaluation confound (Section 4.2)**
   The paper uses GPT-4 to score responses on a 1–5 scale with "standard solutions given as the reference context." GPT-4-based evaluation has known biases (style preferences, verbosity bias), and the use of standard solutions as reference could systematically favor off-policy chosen responses that lexically match those solutions. While MATH problems have objectively correct answers, this confound is not discussed.

6. **In-house poem and slogan datasets are not characterized**
   Section 4.1 mentions "two in-house datasets" for poem and slogan generation but gives no information about dataset size, source, annotation procedure, how preferences were collected, or inter-annotator agreement. This makes it impossible to assess task difficulty or result reliability.

7. **Token-overlap mechanism for Property 3 asserted, not directly demonstrated**
   Corollary 3 attributes the decline in chosen response likelihood to shared tokens between chosen and rejected responses. This mechanism is plausible but not empirically tested — e.g., by partitioning chosen-response tokens into those overlapping vs. not overlapping with the rejected response and measuring their likelihood trajectories separately.

### Trivial
None.

---

## Nice-to-Haves

- **Direct gradient measurements during real LLM training**: Tracking ‖∂ℓ/∂π⁺ · ∇_θ π⁺‖ and ‖∂ℓ/∂π⁻ · ∇_θ π⁻‖ across training steps would connect the theoretical prediction to empirical observation and bypass the probability-to-parameter gap.
- **Causal mediation analysis**: Showing that regularization improves performance *because* it corrects the gradient imbalance (rather than through some other mechanism) would strengthen the causal chain.
- **Token-overlap partitioning experiment**: Separately tracking likelihood trajectories for overlapping vs. non-overlapping tokens in chosen responses, as described above.

---

## Removed Points

These points were flagged by reviewers but are removed from the main assessment for the following reasons:

- **"Few models using DPO have achieved performance comparable to closed-source LLMs"** — The harsh critic faults this motivation statement for not being directly tested. This is scope creep: the paper is an analysis paper, not a benchmark; the statement serves as motivation and is a widely acknowledged observation in the community. **Removed** (scope creep).
- **"Accuracy metric measures preference prediction accuracy, not generation quality"** — The paper explicitly states this metric is used to compare training *dynamics* and *stability* (Section 4.4). The metric choice is appropriate for the stated purpose. **Removed** (misreading of the paper's intent).
- **Pure formatting nitpicks and missing-appendix complaints** — Removed per hard rules.
- **Strength "this paper addresses an important problem"** — Generic/superficial. **Removed** per filtering rules.

---

## Novel Insights

The gradient-ratio derivation (π⁺/π⁻) connecting DPO's loss structure to asymmetric gradient dynamics is the paper's most novel analytical contribution. The on-policy/off-policy factorial experiment (four scenarios, Table 1) cleanly demonstrates that distribution gap is not just a correlate but modulates severity of the identified problems, and the non-monotonic β⁻ performance curve (Figure 4) provides a subtle insight: suppressing the rejected gradient too aggressively hurts generalization by pushing the method back toward SFT-like behavior. These contributions are useful and original.

---

## Suggestions

1. **Acknowledge the probability-to-parameter gradient gap explicitly** in Section 3.1 as a simplification, and either (a) provide an argument for when ∇_θ π⁺ and ∇_θ π⁻ are comparable, or (b) present the theoretical analysis as a diagnostic heuristic that the empirical evidence independently supports.
2. **Fully specify Flex-DPO**: clarify whether β⁻ is a static hyperparameter (chosen per run), dynamically scheduled, or per-sample adaptive. Provide the exact procedure and any scheduling formula.
3. **Add PPO implementation details** to Section 4.5 (or the appendix): reward model architecture, training data and procedure, KL coefficient, learning rate, batch size, number of steps/epochs.
4. **Report results from multiple seeds** for the key comparisons (at least Table 1 and Figure 4).
5. **Characterize the in-house datasets** (size, annotation protocol).
6. **Consider adding a footnote acknowledging the GPT-4 evaluation limitation.**

---

## Score and Decision

This paper makes a genuine analytical contribution by identifying and systematically validating the 3D-properties in DPO training. The strengths (gradient-ratio derivation, toy model, controlled on-policy/off-policy ablation, RM contrast, non-monotonic regularization trade-off) are concrete and well-supported. The weaknesses are significant but not fatal: the theoretical derivation has a gap at the probability-to-parameter level (though empirical evidence independently supports the predicted dynamics), Flex-DPO is underspecified, and the PPO comparison lacks essential detail. All weaknesses are addressable in revision. The paper's explanatory contribution is valuable and likely to influence future work on preference optimization.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>