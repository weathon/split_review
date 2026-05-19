- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the consolidated review.

## Summary

This paper proposes RainbowPO, a framework that decomposes existing DPO extensions into seven mathematically orthogonal components (length normalization, link function, home advantage/margin, reference policy, contextual scaling, rejection sampling, and SFT loss), identifies four that are empirically effective, and combines three (length normalization, mixing reference policy, contextual scaling) into a single objective. The key technical insight is the mixing reference policy, which linearly interpolates between the SFT policy and a constant-margin policy, bridging DPO and SimPO. The method achieves 51.66% LC WR on AlpacaEval2 with Llama3-8B-Instruct.

## Strengths

- **Systematic decomposition of DPO variants into orthogonal components (Table 1, Section 3):** The paper provides a structured categorization of seven mathematically orthogonal directions in which existing DPO methods modify the loss. This goes beyond prior work that treats methods in isolation and enables researchers to understand what each variant actually contributes. The mapping in Table 1 is a genuinely useful reference for the community.

- **Theoretically motivated mixing reference policy (Section 3.1, Eq. 3.2):** The derivation showing that SimPO's margin term can be understood as a reference policy (π_γ), and that interpolating between π_ref and π_γ via π_α ∝ π_ref^α · π_γ^{1-α} yields a concrete improvement over both endpoints, is a genuine contribution. Figure 2c and Table 2 empirically validate that an intermediate α outperforms pure DPO-LN (α=1) and pure SimPO (α=0).

- **Rigorous component-wise ablation (Tables 2–5):** The paper evaluates each component individually, in combination with length normalization, and via removal tests on the full RainbowPO. Tables 2 and 5 provide clear evidence of which components contribute and by how much. The use of two judges (GPT4 and Llama3-70B) across all experiments strengthens reliability.

- **Identification of non-independence among orthogonal components (Section 4.1, lines 314, 412):** The paper explicitly documents that mathematically orthogonal components are not empirically independent (e.g., RSO improves DPO alone but hurts with length normalization), and that some combinations yield "1+1>2" effects. This is a useful caution for future method design.

## Weaknesses

### Fatal
None.

### Major

- **Discrepancy in the reported baseline win rate (abstract/intro vs. tables):** The abstract and introduction state: "RainbowPO improves Llama3-8B-Instruct from 22.92% to 51.66% for Length Controlled Win Rate." However, every table in the paper (Tables 2, 3, 5) reports the base model's LC WR as 41.88%. The 22.92% appears to come from an external leaderboard, while 41.88% is the paper's own evaluation of the same model. These should be the same quantity, and using the lower (external) number to claim improvement inflates the apparent contribution from ~10 points to ~29 points. The paper must either reconcile these numbers or use a single, consistent baseline throughout.

- **Claims of "state-of-the-art" and "best among all open-sourced algorithms" are not supported by the evidence.** The conclusion claims "state-of-the-art performance" (line 419) and the introduction claims the method "perform[s] the best among all open-sourced algorithms when tuning Llama3-8B-Instruct" (line 38). The comparison set includes only 6 methods at 1 epoch (DPO, IPO, KTO, CPO, ORPO, SimPO) and 2 methods at 3 epochs (DPO, SimPO). Many other preference optimization recipes exist for this model (iterative DPO variants, online methods, etc.). The claim is unsubstantiated and should be removed or heavily qualified to match the comparison scope.

- **Evaluation limited to a single configuration (one model, one dataset pipeline, one benchmark):** The experiments use only Llama3-8B-Instruct, UltraFeedback prompts ranked by ArmoRM, and AlpacaEval2. While the paper acknowledges this limitation (Section 4.3), it does not adjust its title ("A Unified Framework") or central claims accordingly. Without at least one additional base model (e.g., Mistral-7B) or evaluation benchmark (e.g., Arena-Hard), the paper's claim of providing a generally applicable "framework" is premature. The decomposition insight is valuable on its own, but the empirical validation does not match the scope implied by the paper's framing.

### Minor

- **One-epoch results are essentially tied with SimPO (Table 4):** RainbowPO achieves 48.08% LC WR vs. SimPO's 47.96% at one epoch — a 0.12% gap well within noise. The paper's advantage only appears at three epochs (51.66% vs. SimPO's 48.40%). This should be more prominently highlighted, as it means RainbowPO's benefit is in long-horizon training, not in one-shot superiority. The paper does mention this (line 386) but positions the one-epoch comparison as "RainbowPO performs the best" without noting the margin is negligible.

- **Length normalization dominates the ablation, while mixing policy contributes modestly (Table 5):** The removal ablation shows that dropping length normalization costs 5.98 points (51.66% → 45.68%), dropping contextual scaling costs 3.26 points (→ 48.40%), and dropping mixing costs only 1.14 points (→ 50.52%). The paper's emphasis on mixing as a key insight is somewhat at odds with its marginal contribution in the final ablation. The paper acknowledges LN is "of the most critical importance" (line 336), but the presentation does not reflect this asymmetry.

- **Individual component gains on top of DPO are very small (Table 2):** Adding individual components to DPO yields: LN +1.76%, Mixing +0.04%, Contextual Scaling +0.16%, Rejection Sampling +0.09%. The paper does not discuss why individual gains are so modest or whether the combination effect is robust across hyperparameter choices.

- **ORPO analysis is mathematically opaque (Section 1, Eq. bounding ORPO loss):** The derivation depends on the assumption Δ_θ > 0, which is not guaranteed during training. The connection between ORPO and "CPO with length normalization and contextual β" is stated without sufficient derivation. This analysis would benefit from simplification or deferral to an appendix.

- **Limitations not reflected in the abstract or conclusion:** The conclusion claims "state-of-the-art performance" (line 419) without the qualifications present in the limitations section (Section 4.3). The abstract does not mention the single-model scope.

### Trivial
None.

## Nice-to-Haves

- **Why exponential mixing rather than arithmetic mixing?** The paper presents π_α ∝ π_ref^α · π_γ^{1-α} as natural. A brief justification (or a comparison with arithmetic mixing in an ablation) would strengthen the theoretical framing.

- **Learning curves across training steps** would more directly support the claim that RainbowPO benefits from longer training than the current two-data-point comparison (epoch 1 vs. 3).

- **Statistical significance testing** (e.g., bootstrap confidence intervals from AlpacaEval) would help assess whether the reported differences (often 1–3%) are likely real.

## Removed Points

- **"Component independence claim is contradictory" (Harsh Critic Point 4):** The paper explicitly states that components are "mathematically orthogonal" but "not empirically independent" (line 314), and documents that RSO helps alone but hurts with LN. This is a finding, not a contradiction. The paper never claims additive gains or empirical independence. Removed because it misreads the paper.

- **Reproducibility nitpicks about hyperparameter details / missing appendix content:** The reviewer's concerns about undisclosed hyperparameters and missing appendix details are partially addressed by the paper's mention of the greedy search methodology and planned code release. These are standard practices; removing per the hard rule about trivial reproducibility concerns. Some specific hyperparameter questions (e.g., learning rate, batch size) are reasonable but fall under minor reproducibility concerns already addressed by the paper's commitment to release code.

- **"Why not learned α per prompt":** This is a speculation, not a weakness. The paper uses a global α which works. A learned per-prompt α is a future extension, not a flaw.

- **"Not comparing to other labs' results on AlpacaEval2 leaderboard":** Removed per the hard rule that questions about cited entities' existence/release status should not be raised. However, the related weakness about overclaimed "best among all open-sourced algorithms" is retained based on the paper's own comparison scope.

## Novel Insights

The harsh critic's observation that RainbowPO's benefit is concentrated in long-horizon training (epoch 3 vs. epoch 1) is a genuinely insightful nuance that the paper itself underplays. The paper frames the one-epoch comparison as a win ("RainbowPO performs the best") when the 0.12% gap over SimPO is negligible; the real story is that RainbowPO continues to improve with more epochs while SimPO plateaus. The reviewer's correct identification of this asymmetry adds more precision to the paper's own narrative than the paper provides.

## Suggestions

1. **Fix the baseline discrepancy.** Choose one consistent baseline (ideally the paper's own evaluated base model at 41.88%) and use it throughout — abstract, introduction, and all claims about improvement magnitude. Or, if using the external 22.92% figure, explain why it differs from the paper's 41.88% and use it consistently.

2. **Temper the claims.** Replace "state-of-the-art" / "best among all open-sourced algorithms" with claims that precisely match the comparison scope (e.g., "best among the methods we evaluated under this specific setup"). The phrase "to the best of our knowledge" does not excuse a claim that cannot be verified.

3. **Add at least one additional evaluation configuration** (e.g., Mistral-7B base model, or Arena-Hard benchmark) to support the generality implied by the "unified framework" framing. If this is not feasible, explicitly scope the paper's claims to the single instantiation studied.

4. **Re-balance the narrative** to reflect that length normalization is the dominant contributor and mixing policy is a smaller (but still positive) contributor, consistent with the ablation data.

5. **Highlight the long-training advantage** more prominently. The paper's most distinctive empirical result is that RainbowPO keeps improving at 3 epochs while SimPO does not.
