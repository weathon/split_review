Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper revisits the idea of using a prompted off-the-shelf LLM as a guardrail against prompt injection attacks. The authors show that with modern reasoning-capable LLMs (GPT-4o, GPT-4.1), this simple prompting approach achieves remarkably low false positive and false negative rates (both below 1% on AgentDojo), and—uniquely—can *remove* the injected content so the agent continues processing the sanitized input rather than discarding it entirely. The paper is a well-executed empirical study that convincingly demonstrates that prompting-based defenses should now be considered a standard, viable baseline.

## Strengths

1. **Clean central result that directly overturns a prior consensus.** Table 1 shows GPT-4o and GPT-4.1 achieving both FPR and FNR below 1% on AgentDojo and below 5% on Open Prompt Injection and TensorTrust. This directly contradicts prior work (Liu et al., 2024) that found prompting-based detection largely ineffective with older models. The evidence is clear and internally consistent.

2. **Injection *removal* rather than just rejection is a practical differentiator.** Most prior detection-based defenses discard contaminated inputs entirely, which degrades utility. PromptArmor extracts and removes the injected content via fuzzy matching, and Table 2 shows this improves utility over the undefended baseline (UA 72.02% vs. 64.27% for GPT-4.1) while driving ASR to 0.00%. This is a concrete, practically meaningful advance over simply "flag and discard."

3. **Systematic ablation of model size vs. reasoning capability.** The Qwen3 experiments (0.6B to 32B, in reasoning and non-reasoning modes) cleanly separate the effects of model capacity and reasoning. The finding that sufficient capacity is the primary driver, while reasoning helps mid-sized models at the margin (Qwen3-8B FNR drops from 26.50% to 15.78%), gives actionable guidance for practitioners choosing a guardrail model.

4. **Memorization test rules out the most obvious confound.** Section 4.5 applies a standard memorization test: average similarity 0.34, only 3.5% of samples above the 0.6 threshold. This convincingly shows the results are not artifacts of benchmark contamination.

5. **Comprehensive baseline comparison.** Table 2 compares against seven defenses spanning three categories (detection, prompt augmentation, system-level). The comparison is asymmetric in model size, but this is the paper's explicit point: a general-purpose strong LLM beats specialized small detectors. The baselines are properly configured and the comparison is informative on its own terms.

## Weaknesses

### Major
None.

### Minor

1. **Adaptive attack evaluation relies on a single red-teaming method.** The robustness evaluation (Section 4.6) uses only AgentVigil to generate adaptive attacks. While the results show PromptArmor maintains low ASR against these attacks (0.00%–0.16%), the paper would be stronger with either (a) additional automated red-teaming methods, or (b) a small set of hand-crafted attack templates designed to exploit weaknesses in a *guardrail LLM* specifically (e.g., injections disguised as benign tool-call output, split across multiple retrievals, or using encoding the guardrail might not interpret as malicious). The results section appropriately describes this as "fuzzing-based adaptive attacks," but the introduction's claim ("robust against adaptive attacks specifically designed to circumvent it") is broader than what one method can support. The core contribution does not depend on perfect adaptive robustness, so this is a limitation worth noting rather than a fatal flaw.

2. **No discussion of benchmark-inherent randomness.** The paper sets temperature 0, making the guardrail LLM's outputs deterministic, but does not discuss whether the benchmark environments themselves introduce randomness (e.g., sampling procedures in Open Prompt Injection). A brief note on whether any evaluation step involves stochasticity would be helpful for reproducibility assessment. This is a presentation gap, not a validity concern.

3. **No qualitative failure-case analysis.** The paper reports aggregate FPR and FNR but does not examine *which* inputs are misclassified. Even a short qualitative description (e.g., "the missed injections tend to be short commands lacking typical instruction phrasing") would help readers understand the method's boundaries without expanding the paper's scope.

### Trivial
- The memorization test's 0.6 similarity threshold is inherited from prior work (Staab et al., 2023) but is not independently justified. The qualitative conclusion (low memorization) is robust regardless of the exact threshold, so this is a documentation detail rather than a weakness.

## Nice-to-Haves
- A brief quantitative characterization of the latency and token cost added by the guardrail LLM call would help practitioners evaluate the practical trade-off. The paper discusses efficiency qualitatively in §3.2 but does not provide concrete numbers.
- Deepening the adaptive attack evaluation with a few targeted hand-crafted attacks (as described in weakness 1) would strengthen the robustness claim. The paper's core argument does not require this, but it would be a natural extension for the camera-ready version.

## Removed Points
- "Comparison fairness with baselines (model size advantage)": This was raised as a potential concern but the paper's thesis is precisely that general-purpose strong LLMs outperform specialized small detectors. The comparison is appropriate for the claim being made.
- "System prompt details in main text vs. appendix": The parser strips appendices; the original submission has the prompt in the appendix. This is a parser artifact, not a paper flaw.
- "Statistical significance / variance not reported": Temperature 0 eliminates sampling variance from the guardrail LLM. Discussion of benchmark-level stochasticity would be nice (included in minor weaknesses above) but the critic's framing as a significant omission is disproportionate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- Add a brief qualitative analysis of the false negative cases (even 2–3 examples) to help readers understand what kinds of injections the guardrail misses.
- Add a short paragraph quantifying the overhead of the guardrail call in terms of latency and tokens.
- For the adaptive attack evaluation, supplement AgentVigil with at least one additional automated red-teaming approach or a small set of hand-crafted templates targeting guardrail LLMs specifically.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Three queries covering bands (0–3.5), (3.5–7.5), and (7.5+). Weak-band anchors (e.g., Inverse Prompt Engineering at 3.00, Wildflare GuardRail at 3.00) were clearly below this paper. Middle-band anchors included Baseline Defenses (5.25, Reject), RA-LLM (5.33, Reject), SPIN (5.50, Reject), and PFT (4.25, Reject). Strong-band anchors (AgentHarm 6.75, ASB 6.25, Cybench 8.67) were different contribution types (benchmarks) or far above. Initial bracket: **5.5–7.5**.

**Round 2 — Narrowing inside bracket:** Queried (5.5–7.5) for prompt injection and agent security topics. Read GuardAgent (6.00, Reject), ASB (6.25, Accept), AgentHarm (6.75, Accept). PromptArmor is clearly stronger than GuardAgent (which had limited evaluation scope and weak baselines) and comparable to ASB (which had high review variance, 3–8). PromptArmor is slightly below AgentHarm in review consensus but has a different, more practical contribution type.

**Final score: 6.5.** The paper is a clean, thorough empirical study. It has one real limitation (adaptive attack scope) that does not threaten the core claim, and the evidence for the central thesis is strong and internally consistent. This places it above papers around 5–5.5 that had significant methodological or evaluation gaps, and alongside papers around 6.0–6.5 that were accepted with minor reservations.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>