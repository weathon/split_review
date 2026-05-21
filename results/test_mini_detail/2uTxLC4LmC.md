## Summary

This paper identifies a critical gap in existing LRM safety alignment: even when final responses are safe, intermediate reasoning often contains harmful content. The authors systematically analyze how safety evolves during reasoning, discovering "safety triggers" (steps that consolidate safe continuation) and "compliance cues" (steps that propagate unsafe reasoning). They propose Intervened Preference Optimization (IPO), which replaces compliance cues with safety triggers at the divergence point and applies DPO on the resulting preference pairs. Experiments across three LRMs (DS-8B, DS-7B, Qwen3-8B) and multiple safety+reasoning benchmarks show substantial safety improvements (e.g., reasoning harmfulness on WildJailbreak drops from ~82% to ~23% for DS-8B) while preserving or improving reasoning performance.

## Strengths

1. **Novel and principled identification of safety dynamics in reasoning.** The CSR metric (Eq. 1) and turning-point detection (Eq. 2) provide a quantitative, interpretable framework for locating safety-critical steps, going beyond prior qualitative observations. The strong correlation (Pearson R=0.85, Figure 5b) between compliance cues and unsafe continuations establishes a solid empirical foundation for intervention. This systematic analysis is a genuine contribution to the under-explored area of reasoning-level safety.

2. **IPO achieves substantial safety gains across multiple models and benchmarks while preserving reasoning ability.** On DS-8B, IPO achieves the lowest reasoning harmful ratios across all three benchmarks (5.7% JailbreakBench, 16.7% StrongReject, 23.4% WildJailbreak) and simultaneously attains the highest average reasoning accuracy (68.5%), surpassing SFT-based methods (e.g., STAR at 64.9%), RL-based GRPO (68.3%), and SafeKey (67.6%). The improvements are consistent across three distinct LRMs, supporting generality.

3. **The core design choice — partial DPO at divergence points — is cleanly validated.** The ablation (Table 3) shows that DPO only on the segments after the compliance cue (10.9% avg harmfulness on StrongReject) dramatically outperforms SFT on full trajectories (42.3%) and DPO on full trajectories (19.0%). The KL divergence analysis (Figure 7) further confirms that IPO's supervision concentrates precisely at the token positions corresponding to compliance cues, while SFT baselines show flat, low KL divergence.

4. **Sample and computational efficiency over RL-based alternatives.** IPO requires ≤14 generations per prompt and ~40 minutes of training, compared to GRPO's ≥40 generations and >2 hours, while achieving better safety. This practical advantage directly addresses the low-rollout-diversity limitation of RL methods identified in Section 2.3 and is convincingly demonstrated.

## Weaknesses

### Fatal
None.

### Major

1. **The auxiliary SFT loss and benign-preference DPO stage are not individually ablated.** IPO uses three components bundled together: (i) the core intervened preference pairs with partial DPO, (ii) an auxiliary SFT loss on preferred CoTs (RPO-style), and (iii) a separate benign-preference DPO stage to reduce over-refusal. The paper ablates the core DPO-vs-SFT-vs-full-DPO design choice (Table 3) but does not disentangle the contributions of the SFT loss and the benign-preference stage. Without this ablation, it is unclear how much each component contributes to the final safety-utility balance, and the method reads as a bundle rather than a precisely characterized intervention. This is the most significant empirical gap.

2. **The method's dependence on an external compliance-cue detector is under-characterized.** The paper acknowledges that replacing GPT-4o with DS-8B degrades average harmfulness on StrongReject from 13.7% to 19.4% (~42% relative increase) but describes this as "only slight degradation" (Section 4.3). The degradation is modest in absolute terms but the characterization is misleading. More importantly, the paper does not analyze how *types* of detection errors (false positives, false negatives, or positional misalignments) affect downstream data quality and training outcomes. A 20% disagreement rate with human annotation (Section 3.2) is nontrivial, and the downstream consequences of these disagreements are unexamined. This dependency is a practical limitation that should be discussed more honestly and studied more thoroughly.

### Minor

1. **No confidence intervals or variability estimates for any safety or reasoning results.** The harmful ratios are estimated from 100–250 prompts, and differences between methods are sometimes small (e.g., IPO vs. GRPO on JailbreakBench reasoning for DS-7B: 11.0% vs. 3.0%). Without any measure of uncertainty, it is impossible for readers to assess whether observed differences are meaningful or within the noise of the evaluation.

2. **The claim that "safe reasoning is often consolidated by a few critical steps" rests on a CSR analysis of only 30 prompts sampled from one benchmark.** While the analysis is insightful and the patterns are plausible, the sample is limited in size and diversity (JailbreakBench only). Demonstrating the same patterns hold across more diverse prompts and longer reasoning traces would strengthen the generality of this core claim.

3. **The preference-pair construction uses the base model's distribution, but during training the model's distribution shifts.** This is a standard concern with offline DPO from a fixed dataset. The paper does not analyze whether the model's post-training reasoning genuinely internalizes the pattern of recognizing and rejecting harmful intent early, or whether it learns to insert trigger-like phrases at early positions. The KL divergence peak in Figure 7 supports the former interpretation but does not conclusively rule out the latter. A qualitative analysis of post-training reasoning traces on held-out prompts — examining whether safety triggers appear without external insertion — would strengthen the claim.

### Trivial
None.

## Nice-to-Haves

- A per-prompt breakdown of safety gains (e.g., "IPO makes safe 40 of the 50 prompts that were unsafe under STAR") would clarify whether improvements are broad-based or concentrated on a subset of easy prompts.
- Extending evaluation to a small set of multiturn or agentic scenarios, given that these are mentioned as motivation in Section 1, would strengthen practical relevance. The paper explicitly scopes this to future work, so this is not a weakness, but a demonstration would move the paper from "promising method" to "deployed solution territory."

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Criticism about CSR estimate using only 32 samples**: This is a standard sample size for Monte Carlo estimation in language model analysis. The paper's analysis identifies clear patterns with this sample size; larger samples would add marginal precision but are not required for the qualitative conclusions drawn.
- **Threshold choices (μ=0.9, K=15) not ablated**: The paper reports that with these values, "over 90% of sampled safe trajectories contain such turning points," which serves as implicit validation. Full ablation would be nice but is not necessary for the paper's validity.
- **"20% GPT-4o disagreement rate" as a standalone weakness**: The paper explicitly acknowledges this rate. KEEP the downstream-analysis concern (merged into Major weakness #2) but the raw rate alone is not a weakness.
- **GRPO experiment "only one model shown"**: Table 2 shows GRPO results for all three models. The Table 1 analysis uses only DS-8B, but that is a diagnostic experiment, not the main evaluation.
- **Training budget asymmetry concern (SFT methods vs. IPO's DPO+SFT)**: The paper clearly distinguishes the training approaches of baselines and does not claim a control-for-every-variable comparison. The comparison is fair and standard for this type of work.
- **Missing evaluation on multiturn/agent settings**: Explicitly scoped as future work. Scope creep.
- **Formatting, typo, and appendix-missing criticisms**: Parser artifacts or prohibited by review policy.

## Novel Insights

The harsh critic's observation about the detector dependency being underplayed is well-taken and forms a genuine actionable gap. However, the most novel angle that emerges from cross-referencing the reviews is the tension between the paper's claim of "genuine reasoning reform" and the available evidence: the KL divergence peak at compliance-cue positions (Figure 7) could equally indicate surface-level trigger memorization or deeper internalization. This is not a fatal flaw — the paper's behavioral results stand on their own — but it points to a specific, addressable gap: showing that safety triggers persist in post-training generations *without explicit insertion* would transform a strong empirical paper into one with mechanistic insight. The review synthesis also highlights that the bundle of auxiliary losses (SFT loss, benign-preference stage) is the most straightforward ablation to run and would significantly improve the paper's scientific precision.

## Suggestions

1. **Ablate the auxiliary SFT loss and benign-preference DPO stage individually.** Run IPO (a) with only the core intervened DPO, (b) core + SFT loss, (c) core + benign stage, (d) full pipeline. This is the single highest-value experiment for the camera-ready.
2. **Report confidence intervals** (e.g., bootstrap or Wilson intervals) for all safety ratios. The differences between methods on some sub-metrics are small enough that uncertainty is relevant.
3. **Add a qualitative analysis of post-training reasoning traces** on held-out adversarial prompts, showing whether safety triggers appear without external insertion. This would distinguish genuine internalization from surface-level imitation.
4. **Provide a more honest characterization of detector sensitivity** — explicitly state the DS-8B degradation as a limitation — and analyze what types of detection errors most affect downstream data quality.

## Score and Decision

**Calibration anchors:**
- **Round 1 (bracketing):** Weak band — KjxZ4BdUdN (3.0, guardrail pipeline), 6QBHdrt8nX (3.33, safety moderation), jOuHjFw71C (3.0, LRM planning). Middle band — z7usV2BlEE (5.5, reasoning alignment, REJECT), EEWpE9cR27 (4.5, VLM safety). Strong band — 6Mxhg9PtDE (9.5, safety alignment depth, ORAL), Iyrtb9EJBp (8.0, trust align RAG, ORAL), N8N0hgNDRt (8.0, MetaMath, spotlight).
- **Round 1 bracket:** Narrowest plausible range = [6.5, 8.5].
- **Round 2 (narrowing):** TyFrPOKYXw (7.5, Safe RLHF, spotlight) — Safe RLHF uses a standard CMDP formulation with Lagrangian methods; its contribution is primarily the decoupling framework. IPO has stronger methodological novelty (discovery of compliance cues/safety triggers, intervention-based preference construction) and more thorough experiments (3 LRMs, multiple safety+reasoning benchmarks, ablation studies). IPO is at least comparable and arguably stronger. ERce2rgMQC (7.0, CoSA, poster) — CoSA focuses on inference-time safety configurability. IPO has a cleaner evaluation, stronger behavioral gains, and a more fundamental contribution (targeting reasoning-level safety itself). IPO is clearly stronger. A6Y7AqlzLW (7.3 avg, Rewarding Progress, spotlight) — process rewards for math reasoning; strong theory but narrower scope. IPO is comparable in empirical thoroughness and arguably broader in significance. 6Mxhg9PtDE (9.5, safety alignment depth, oral) — a tier above IPO due to a more fundamental, unified insight about shallow alignment across attack types and cleaner mitigation strategies. IPO does not reach this tier.
- **Final score after narrowing:** The paper is clearly above the 7.0–7.5 anchors (CoSA, Safe RLHF) due to stronger novelty, broader evaluation, and cleaner results. It is clearly below the 9.5 oral (safety alignment depth). It sits comfortably with the 8.0 oral anchors (Trust-Align RAG). Score: **8.0**.

The paper is a strong accept. It identifies a genuinely overlooked and important problem (reasoning-level safety), provides a principled analysis of safety dynamics in reasoning, proposes an effective and practical method (IPO), and supports it with thorough experiments across multiple models and benchmarks. The weaknesses are real but bounded — they do not threaten the core contribution. The methodological novelty (compliance cue detection + intervention-based preference construction) is significant relative to existing SFT-based and RL-based approaches. The paper is well-written, the claims are mostly well-supported, and the value to the community is clear.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>