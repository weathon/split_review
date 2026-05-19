- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have everything I need. Here is my consolidated final review.

---

## Summary

This paper proposes using the Bradley-Terry model with ties (BTT) — a generalization of the standard Bradley-Terry (BT) model — to model human preferences in RLHF, arguing that forced-choice annotation masks meaningful tie information. It derives a closed-form bias formula for preference strength when ties are ignored under BTT, proposes a bias-correction algorithm (Algorithm 1) for conventional datasets without tie labels, and presents empirical results on synthetic and LLM-labeled data showing that BTT-based fine-tuning (TDPO) outperforms DPO. The core idea is well-motivated and practically relevant.

## Strengths

- **Well-motivated and timely idea**: The paper identifies a genuine limitation of current preference annotation practices — forced-choice labeling ignores the prevalence of near-tie preferences. The examples in Table 1 (from Wang et al. 2024) concretely demonstrate that a substantial fraction of annotated HH-RLHF pairs have near-zero mean preference strength (e.g., 0.0027, 0.0, 0.00019), making the case for incorporating ties compelling.

- **Explicit bias formula (Theorem 2)**: The paper derives a closed-form expression relating the learned preference strength under BT (Δ\hat{r}) to the true preference strength under BTT (Δr^*). The formula shows that the bias attenuates preference strength (sign opposite to Δr^*) and is bounded by log((1+θ²)/(2θ)). Even if the derivation has a subtle representability gap (see Weaknesses), the formula provides a concrete, testable hypothesis about the structure of the bias.

- **Clear empirical gains**: The bias-correction method improves test accuracy from 0.5333 (DPO baseline) to 0.6042 at θ=5 on HH-RLHF with Pythia-160M (Table 2, >10% relative improvement). Win-rate evaluations against DPO on Pythia-2.8B (Table 3) show 0.5582 (Llama evaluator) and 0.5370 (Qwen evaluator). These results are consistent and directionally clear.

- **Controlled causal evidence in Figure 2**: The synthetic-ties experiment (Section 5.3) varies the fraction of tied samples from 0 to 100%, showing monotonic improvement in TDPO's win rate over DPO as tie ratio increases. This design directly isolates the effect of modeling ties vs. the data itself.

## Weaknesses

### Fatal
None.

### Major

- **Unverified representability assumption in Theorem 2**: The derivation of the bias formula (Equation 6) assumes implicitly that there exists a single global reward function \hat{r}(x, y) such that for all pairs (y₁, y₂), the BT preference probability p_{\hat{r}}(y₁ ≻ y₂ | x) exactly equals the forced-choice distribution q_{r^*}^θ(y₁ ≻ y₂ | x) = p_{r^*}^θ(y₁ ≻ y₂ | x) + ½·p_{r^*}^θ(y₁ = y₂ | x). This is a non-trivial claim: the log-odds of q under BTT is a nonlinear function of Δr^*, and for a single global reward function \hat{r} to exist, this function must be linear (transitive) — which it is not for θ > 1 (it is only linear at θ = 1, where BTT reduces to BT). The paper does not acknowledge this gap, does not prove representability, and does not bound the approximation error. The bias formula is therefore an *approximate* expression rather than an exact one. This undermines the theoretical rigor of the paper's central claim. (Verified by examining the log-odds structure: for θ > 1, the function F(u) = u + log((2θe^u+(θ²+1))/((θ²+1)e^u+2θ)) is nonlinear, violating transitivity required for a global reward function.)

- **Missing critical experimental control — fixed-margin ODPO baseline**: The paper explicitly positions its bias-correction method as a variant of ODPO (DPO with an offset). Yet no experiment compares the BTT-derived *adaptive* margin against ODPO with a simple *fixed* (tuned) margin. The improvements in Tables 2 and 3 could therefore be driven by adding *any* margin (including a constant offset), rather than by the specific BTT-derived functional form. Without this control, the experiments cannot distinguish whether the margin's *shape* matters or just its *presence*. This is the most actionable experimental gap and is essential to validate the paper's core claim that the BTT-theoretic bias formula provides unique benefit.

### Minor

- **No measures of variability**: All experimental results (Tables 1–3) are reported as single point estimates. No confidence intervals, standard errors, standard deviations, or significance tests are provided. The simulation experiment (Table 1) reports three numbers (0.0206, 0.0237, 0.0353) without any indication of variance across random seeds or dataset samples. This makes it impossible to assess the reliability or stability of the reported improvements.

- **Sensitivity to θ is underexplored**: The algorithm requires θ as a hyperparameter. Table 2 tests only three values (θ ∈ {2, 5, 10}), and all subsequent experiments fix θ = 5 based on this single table. The paper does not study sensitivity to θ, nor does it discuss how to estimate or tune θ in practice when the BTT model's ground-truth parameter is unknown. A practitioner would need guidance on selecting θ.

- **Reliance on LLM-simulated (not human) ties**: The synthetic ties experiment (Section 5.3) uses Llama3-70B and Qwen2-72B to annotate ties. The paper acknowledges this limitation. While the results are promising and the bidirectional labeling/evaluation design mitigates some concerns, the evidence that BTT outperforms BT on *real human* tie preferences remains indirect.

### Trivial

- None (no formatting, typo, or presentation issues rise to this level; any such artifacts are parser-originated).

## Nice-to-Haves

- Compare against ODPO with a tuned constant offset (and potentially against a three-class cross-entropy baseline) to isolate the benefit of the BTT-derived margin shape.
- Report results over multiple random seeds with standard deviations/confidence intervals.
- Analyze or bound the approximation error from the representability gap.
- Study θ sensitivity more systematically, or propose a data-driven method to estimate θ (e.g., from the empirical tie proportion).
- Provide training details (architecture, learning rate, batch size, optimizer, compute) to improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The derivation of the bias term itself contains a gap — the 'By subtraction, we can get' step is insufficiently explained."** (from Harsh Critic, point 4) — Removed. The proof is presented as a *sketch* (explicitly labeled). The prose sketches the algebraic backbone clearly enough for a conference paper; filling in the algebra from the stated equations is straightforward.

2. **"The paper would benefit from comparison with other preference models that handle ties (e.g., a simple three-class cross-entropy loss, or the Thurstone model)."** (from Harsh Critic, "Places to Improve") — Removed. The paper's scope is argued from the BT/BTT framework. Requesting comparisons to Thurstone or arbitrary three-class classifiers constitutes scope creep; these are not standard baselines in the RLHF preference-modeling literature the paper targets.

3. **"Reproducibility details are almost entirely absent."** (from Harsh Critic) — Removed. The paper states β = 0.1, follows Rafailov et al.'s setup, and uses standard open models (Pythia). While more detail would help (Nice-to-Have), the claim of "almost entirely absent" is an overstatement; the essential experimental setup is described.

4. **"The bias-correction algorithm solves a nonlinear equation at each step, which could be computationally expensive; the paper does not comment on computational cost or convergence issues."** — Removed. Solving a 1D nonlinear monotonic equation at each step is a trivial O(1) operation (e.g., binary search or Newton's method). This is not a genuine cost concern.

## Novel Insights

The most interesting observation to emerge from cross-referencing the reviews is the **tension between the paper's framing as a theoretically-grounded method and the empirical results' reliance on treating θ as a tunable hyperparameter**. The harsh critic identifies that the bias formula's exactness depends on an unverified representability assumption. Yet the experiments show that the method *works best at θ=5* — a value selected by validation accuracy, not derived from tie-rate estimation. This suggests the method might be better understood as defining a *family of adaptive margin functions* (parameterized by θ) that happen to be inspired by the BTT model, rather than as implementing a theoretically exact correction. The paper's strongest contribution may ultimately be empirical: demonstrating that *some* adaptive margin — and the BTT-derived shape in particular — improves DPO performance. This reframing would resolve the theoretical gap while preserving the paper's practical value.

## Suggestions

1. **Reframe the theoretical contribution**: Acknowledge the representability limitation explicitly. State the bias formula as an *approximation* or as characterizing the bias under the assumption that the BT family can represent q. Alternatively, prove that the log-odds of q is a strictly monotonic transformation of Δr^* and argue that the formula captures the first-order structure of the bias.

2. **Add the fixed-margin ODPO control**: This single addition would transform the experimental section. If the BTT-derived margin consistently outperforms a well-tuned constant offset, the paper's claim that the BTT *structure* (not just any margin) helps would be substantially strengthened.

3. **Provide error bars**: Run the bias-correction experiment (Table 2) with at least 3-5 random seeds and report means and standard deviations. This is standard practice for single-epoch fine-tuning and would significantly increase confidence in the results.

4. **Study θ sensitivity**: Add an ablation varying θ over a finer grid (e.g., θ ∈ {1.5, 2, 3, 5, 7, 10}) to understand the landscape. Discuss how practitioners should select θ.
