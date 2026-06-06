---

## Summary

VeriFree proposes a verifier-free approach to DeepSeek-R1-Zero-style RL for general reasoning tasks. The central insight is that, under a unique correct answer, the RLVR objective (expected binary reward) equals the model's probability of generating the reference answer given a reasoning trace, derived by marginalizing out the sampled answer. This yields a gradient estimator that is theoretically equivalent in expectation to the verifier-based objective but has lower variance by Rao-Blackwellization. Empirically, VeriFree matches or surpasses verifier-based training across MMLU-Pro, SuperGPQA, and math benchmarks at 1.7B–8B model scale, while eliminating the computational burden of maintaining a verifier model.

---

## Strengths

- **Clean theoretical derivation of objective equivalence.** Under the unique correct answer assumption, Eq. (4) shows $J_\text{VeriFree} = J_\text{Verifier}$ by analytically marginalizing out $y$ via the indicator reward, yielding $R_\text{VeriFree}(z; x, y^*) = \pi_\theta(y^*|x,z)$ as the reward. This is mathematically clean and provides a principled rather than heuristic motivation for the method.

- **Formal variance reduction grounding.** Theorem 1 invokes Rao-Blackwellization (Casella & Robert, 1996), arguing that marginalizing out $y$ removes one source of stochasticity from the gradient estimator. Despite the labeling error in Eq. (6) discussed below, the underlying theoretical logic is sound and well-established.

- **Strong empirical results across scales.** Tables 1 and 2 show VeriFree consistently matches or surpasses the verifier-based baseline at 1.7B, 4B, and 8B scales (e.g., Qwen3-8B-Base-VeriFree achieves 67.2% vs. 65.9% for Verifier on MMLU-Pro; 38.0% vs. 37.1% on SuperGPQA). VeriFree also matches or exceeds the Qwen3 Instruct thinking-mode models despite training from base weights.

- **Ablation studies validate key design choices.** Figure 6 (Left) shows removing RLOO reduces final MMLU-Pro accuracy by over 3%, and the text-based (non-tokenization-aware) split causes optimization instability. Section 2.4 provides a concrete, actionable solution (ending $z$ at `<answer` rather than `<answer>`) that is validated by these ablations.

- **Transferable reasoning skills demonstrated.** Figure 5 shows that training on WebData with all math removed still improves math benchmark performance (Base ≈55% → VeriFree-NoMath ≈60% on Math-Eval-Suite), providing evidence that VeriFree elicits domain-general reasoning rather than domain-specific pattern matching.

- **Practical advantage over existing verifier-free methods.** The comparison in Section 2.3 clearly differentiates VeriFree from JEPO and LaTRO: JEPO uses $\log \pi_\theta(y^*|x,z)$ as reward and always weights the reference answer term by 1, potentially reinforcing low-quality traces. VeriFree weights the reference answer term by $\pi_\theta(y^*|x,z)$, down-weighting poor traces. This qualitative argument is coherent and is corroborated by the experimental comparison in Appendix E.2.

---

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1, Eq. (6) states the inequality backwards.** The theorem defines $\hat{G}_\text{Verifier}(x, y^*, z, y)$ as the estimator requiring both $z$ and $y$, and $\hat{G}_\text{VeriFree}(x, y^*, z)$ as the estimator that marginalizes out $y$. But Eq. (6) as written reads:
$$\text{Var}_{z \sim \pi_\theta}[\hat{G}_{\text{Verifier}}(x, y^*, z)] \leq \text{Var}_{z \sim \pi_\theta, y \sim \pi_\theta}[\hat{G}_{\text{VeriFree}}(x, y^*, z, y)]$$
The LHS places $\hat{G}_\text{Verifier}$ under a subscript marginalizing only over $z$ (i.e., with $y$ already marginalized), which by the theorem's own definitions corresponds to the VeriFree estimator. The RHS places $\hat{G}_\text{VeriFree}$ under a subscript marginalizing over both $z$ and $y$, which corresponds to the Verifier estimator. The function names and subscripts are thus swapped, and the inequality as written asserts that the Verifier estimator has *lower* variance — the opposite of the paper's claim and of what Rao-Blackwellization implies. The surrounding prose (line 114: "for estimating $\nabla_\theta J_\text{VeriFree}$ we analytically marginalize out $y$, thereby removing this source of randomness") is correct. This is therefore a transcription error in the theorem statement itself, not a theoretical flaw; the intended direction is clear from context. However, Eq. (6) is the paper's central formal claim and must be corrected before publication — as written, it contradicts the paper's thesis.

### Minor

- **Scope of theoretical equivalence not clearly delineated.** Section 2.2 derives $J_\text{VeriFree} = J_\text{Verifier}$ under the assumption of exact match ($\mathbb{1}_{y = y^*}$ strict equality). The Verifier baseline (Section 3.1) uses a Qwen2.5-Math-1.5B model fine-tuned to assess semantic equivalence — a strictly larger equivalence class. The paper acknowledges this briefly in footnote 1 and in the phrasing "i.e., exact match rather than semantic equivalence" in Sec. 2.2, and the equivalence class ablation (Fig. 6 Right) shows the practical gap is small. However, the framing in Sections 2.2 and 3.2 of VeriFree as "optimizing exactly the same objective" as the Verifier baseline is overstated; the theorem holds for exact match, while the empirical superiority in the semantic equivalence regime is an additional empirical finding rather than a consequence of the theory. This gap between theory and empirical setup should be stated explicitly in the main text, not absorbed into a footnote.

- **Reward signal asymmetry between VeriFree and Verifier baseline.** Section 3.1 specifies that the Verifier baseline applies a format penalty of −0.5 (for missing `\boxed{}`) and a length penalty. VeriFree's reward is solely $\pi_\theta(y^*|x,z)$; the paper does not state whether VeriFree also uses these auxiliary penalties. If VeriFree achieves superior results with a strictly simpler reward signal, this is a strong additional practical argument that deserves explicit acknowledgment.

- **GPQA-Diamond comparisons lack statistical hedging.** The GPQA-Diamond evaluation set contains approximately 198 items. Differences of 2–3 percentage points in this regime are within noise range at single-run evaluation, yet the paper treats these results on par with MMLU-Pro (which has ~12,000 items). The paper should hedge GPQA conclusions or report confidence intervals for this small-sample benchmark.

### Trivial

- The comparison with JEPO and LaTRO is the primary differentiator from prior verifier-free methods, yet the experimental results are deferred entirely to Appendix E.2 due to space constraints. A brief summary of the Appendix E.2 findings would strengthen Section 2.3.

---

## Nice-to-Haves

- **Direct gradient variance measurement.** Figure 4 (Left) shows VeriFree converges faster, which is attributed to reduced gradient variance. Directly measuring and plotting gradient variance (e.g., variance of the norm of $\nabla_\theta J$) during training for VeriFree vs. Verifier would close the loop between Theorem 1 and the empirical convergence result.

- **Sensitivity to the 7-token answer length cutoff.** The data filtering step retaining samples with fewer than 7 answer tokens (Sec. 3.1) ties the practical method primarily to MCQ/short-answer settings. A brief experiment on slightly longer open-ended answers would give readers more confidence about the method's generalizability beyond short label tokens.

- **Explicit numerical summary of JEPO and LaTRO comparison in the main paper.** Even a two-column table in Section 2.3 summarizing the Appendix E.2 results would help readers assess VeriFree's standing among verifier-free alternatives without flipping to the appendix.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"R1-Zero-style training limited to math and code" is overstated (Introduction).** The harsh critic notes this framing is slightly overstated since the paper itself cites Ma et al. and Su et al. as existing general-domain approaches. However, the paper's claim is specifically about verifier *dependency*, not a complete absence of general-domain methods, and this distinction is made clear in the same paragraph. This is a framing precision issue too minor to retain as a weakness; removed.

- **Correlation ρ=0.82 is "circular."** The harsh critic observes that $\pi_\theta(y^*|x,z)$ is both the training signal and the metric being correlated with accuracy, suggesting circularity. However, the paper presents this as an empirical characterization of how well model confidence tracks held-out accuracy during training (Fig. 4 Right), not as an independent causal claim. The observation is interpretively useful and the framing is appropriately hedged. Removed as a weakness.

- **"Strengthening" suggestions about gradient variance and open-ended answer experiments.** These are reasonable but clearly outside the paper's stated scope (MCQ-format general reasoning). Moved to Nice-to-Haves.

- **Missing related works demands.** Per the hard rules, no criticism about missing related works is included, as external sources cannot be confirmed.

---

## Novel Insights

The paper's most novel observation is the Rao-Blackwellization view of RLVR: by recognizing that the verifier reward is just an indicator function over the answer space, one can analytically marginalize out the answer token and replace binary reward feedback with a continuous, lower-variance signal — the model's own probability of the reference answer. This reframing unifies what previously looked like separate methods (RL with verifier, SFT on reference answers) into a single gradient term with two interpretable components: a policy gradient term for the reasoning trace weighted by answer-probability, and a reward-weighted SFT term for the reference answer. The insight that JEPO/LaTRO's failure case is the constant-weight-1 reference answer term — which reinforces mismatched traces — is a clear and useful diagnostic for the design space of verifier-free methods.

---

## Suggestions

1. **Fix Theorem 1, Eq. (6):** Swap the function names so that $\hat{G}_\text{VeriFree}(x, y^*, z)$ appears on the LHS (lower variance, marginalized over $z$ only) and $\hat{G}_\text{Verifier}(x, y^*, z, y)$ appears on the RHS (higher variance, marginalized over $z$ and $y$). Ensure the subscripts match the function arguments throughout the theorem statement.

2. **Clarify the theory-to-practice gap:** Add one sentence in Section 2.2 or 3.2 explicitly stating that the theoretical equivalence holds under exact match, and that empirical superiority in the semantic equivalence regime (the actual experimental condition) is an additional empirical result, not a corollary of the theorem.

3. **Explicitly state whether VeriFree uses the format/length penalties** from the Verifier baseline (or not), and discuss the implications for the comparison.

4. **Hedge GPQA-Diamond results** by noting the small evaluation set size (~198 items) and treating differences < 3 points as within noise.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>