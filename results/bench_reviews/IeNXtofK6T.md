Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper revisits an old idea—prompting an off-the-shelf LLM to detect and remove prompt injections—and shows that it works extremely well when modern LLMs (GPT-4o, GPT-4.1, Qwen3-32B) are used. Across three benchmarks (AgentDojo, Open Prompt Injection, TensorTrust), the proposed PromptArmor achieves near-zero false positive/negative rates and 0.00% attack success rate on AgentDojo, decisively outperforming specialized fine-tuned detectors. The paper includes ablations on prompting strategies, model size vs. reasoning (using Qwen3's dual-mode capability), a data contamination check, and adaptive attack evaluation.

## Strengths

- **Comprehensive empirical demonstration that the approach now works.** PromptArmor with GPT-4.1 achieves 0.56% FPR, 0.13% FNR, and **0.00% ASR** on AgentDojo (Table 2), while maintaining the highest utility (UA 72.02%) among all tested defenses. This concretely overturns prior negative results (Liu et al., 2024) that were based on weaker models.

- **Systematic evaluation across three diverse benchmarks and multiple model families.** Performance generalizes beyond agent settings: FPR and FNR are below 5% on Open Prompt Injection and TensorTrust for GPT-4o and GPT-4.1 (Table 1). The paper tests proprietary (GPT-3.5, GPT-4o, GPT-4.1) and open-source (Qwen3 0.6B/8B/32B) models, providing broad coverage.

- **Controlled isolation of the model-size vs. reasoning effect.** Using Qwen3 in reasoning and non-reasoning modes (Figure 3), the paper shows that sufficient model capacity is the primary driver of performance, with reasoning helping primarily at mid-range sizes (8B). This offers actionable guidance for practitioners choosing a model.

- **Data contamination check.** The paper tests whether GPT-4.1 memorized AgentDojo data (average similarity 0.34, only 3.5% above the 0.6 threshold), ruling out a common confound that is often ignored in benchmark evaluations.

- **Honest framing.** The paper is transparent that it is "revisiting" a known approach, not claiming a fundamentally new method. This clarity helps the reader assess what is and is not contributed.

## Weaknesses

### Fatal
None.

### Major
- **Novelty is limited to an empirical scaling observation.** The paper's core contribution is that a known approach (prompting an LLM to detect injections) now works because models are stronger. There is no new method, no mechanistic analysis of *how* the guardrail detects injections, and no design principle beyond "use a strong model with a good prompt." The paper is a competent empirical replication study, but at a top venue this level of novelty is thin. The comparison to prior work (Liu et al., 2024) is valuable, but the incremental insight is primarily a function of model release dates, not of a new research idea.

- **Adaptive attack evaluation is too narrow to support the broad claim of robustness.** The abstract and introduction state that PromptArmor "is robust against adaptive attacks," but Section 4.6 tests only *one* adaptive method (AgentVigil, a fuzzing-based red-teaming pipeline). The paper itself qualifies the result as "fuzzing-based adaptive attacks" in Section 4.6, yet the broader-scope claim in the introduction is unsupported. An adaptive attacker who targets the guardrail LLM directly—e.g., crafting injections that appear benign to the guardrail's reasoning, or exploiting the guardrail's own vulnerability to prompt injection—is not considered. This gap means the robustness claim is significantly weaker than the paper's framing suggests.

### Minor
- **No breakdown of detection vs. removal failures.** The paper reports end-to-end ASR, which aggregates detection success *and* removal success. However, the removal step (fuzzy matching via regex from extracted words) is never evaluated in isolation. If the guardrail rephrases the injection (e.g., "disregard earlier commands" instead of "ignore previous instructions"), the fuzzy matching may fail or produce a partial/incomplete removal, yet this would be invisible in the combined ASR metric. Reporting removal quality (e.g., exact-match rate, edit distance to ground-truth injection) would strengthen the analysis.

- **Missing ablation: PromptArmor's crafted prompt vs. a generic prompt on the same strong LLM.** The paper compares PromptArmor against smaller specialized models but does not compare against GPT-4.1 or GPT-4o prompted with a simple, non-crafted instruction (e.g., "reject unsafe content"). Section 4.3 tests different prompting strategies only on GPT-3.5, and the claim that "newer models like GPT-4o and GPT-4.1 perform equally well across different prompting strategies" (line 270) is stated without shown results. Without this control, it is unclear how much of the performance comes from the specific prompt design vs. the raw capability of the model.

- **No confidence intervals or variance estimates.** Although temperature=0 removes model stochasticity, there remains sampling variance from the finite test sets (e.g., 629 adversarial scenarios in AgentDojo). Reporting CIs or variance across runs would improve the empirical rigor.

- **The paper does not discuss the utility improvement under attack.** PromptArmor's UA (72.02%) is higher than the no-defense baseline (64.27%)—suggesting that removing injections not only prevents attacks but actually improves task completion. This is an interesting phenomenon (perhaps injected text distracts the agent even when not executed) that goes unremarked.

### Trivial
- Figure 3's bar charts include a trimmed data table at the bottom, making the visual a bit redundant and busy. A standalone table or cleaner figure would suffice.

## Nice-to-Haves
- **Analysis of which attack types are easier/harder for reasoning vs. non-reasoning models.** The Qwen3 experiment (Figure 3) shows that reasoning helps at 8B but the paper does not break down by attack type (e.g., "Ignore Previous Instructions" vs. "System Message" vs. "Tool Knowledge"). Such an analysis could provide genuine insight into why reasoning helps.
- **Human- or LLM-designed attacks that target the guardrail rather than the backend.** At minimum, testing whether the guardrail can be tricked by injections designed to look benign to a safety classifier (e.g., embedding instructions in seemingly innocuous text).
- **Concrete examples of successful and failed detection/removal.** A few case studies from AgentDojo would help reviewers develop intuition for how and why the method works.

## Removed Points
These points are flagged as removed; treat them with caution.

- **Criticism that the exact system prompt is in the appendix (stripped).** The appendix exists in the original submission; parser artifacts are not author errors.
- **"The paper is a technical report rather than a research paper."** This is a subjective judgment about novelty that is already captured in the major weakness above, but the phrasing is not constructive and is removed as editorializing. The substantive novelty concern is retained.
- **"The method description is too brief."** The method, as described in Section 3.1 and Figure 2, is sufficient for a simple prompting approach; the system prompt and code are in the appendix.
- **"The design rationale reads like a position piece."** The design rationale section is standard for papers of this type and does not claim to be an empirical comparison.
- **Criticism about "unfair comparison" with baselines using smaller models.** The paper's point is to show that a strong off-the-shelf LLM with prompting beats specialized fine-tuned models; comparing against the best available SOTA defenses is standard and appropriate.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface any observation about the paper's findings that the paper itself does not articulate.

## Suggestions

1. **Qualify the adaptive-attack robustness claim** throughout the paper to match what is actually tested: robustness against a fuzzing-based adaptive method (AgentVigil). Add an explicit "Limitations" paragraph acknowledging that attacks targeting the guardrail LLM directly are not evaluated.
2. **Report removal quality metrics** (e.g., exact match between extracted and ground-truth injection, edit distance, or a human evaluation of removal completeness) to complement the end-to-end ASR.
3. **Add the missing control experiment**: compare PromptArmor's crafted prompt against a generic "reject unsafe content" prompt on GPT-4.1. If the results are similar, the paper should acknowledge that the specific prompt engineering matters less than the model capability. The claim on line 270 should be backed by data or removed.
4. **Add confidence intervals** or note the sample sizes for each metric to allow readers to assess result stability.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/MqLJRCUBYG.md` (Firewall defense) | 3.50 | Similar type of contribution (simple LLM-based defense for prompt injection). The current paper has more thorough evaluation but similar novelty limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/3cK8gUZWBD.md` (CommandSans) | 3.50 | Similar topic and evaluation scope. Interestingly, this paper was criticized *for not comparing against PromptArmor*, suggesting PromptArmor is seen as relevant prior art. |
| `/home/wg25r/review_agent/human_reviews_2026/fF9alVesJ0.md` (IntentGuard) | 3.50 | Had a more novel approach (intent analysis) than the current paper but still scored low due to evaluation gaps. The current paper has stronger benchmarks but less novelty. |
| `/home/wg25r/review_agent/human_reviews_2026/yPgbdOdOPG.md` (AlignSentinel) | 4.50 | A detection paper for prompt injection with a novel three-class framing. Better novelty story but also had weaknesses about synthetic benchmarks. Comparable execution quality. |
| `/home/wg25r/review_agent/human_reviews_2026/CaUHFOa4X1.md` (Scam2Prompt) | 5.20 | A well-executed empirical security paper with a new framework. More novel in methodology (scam detection pipeline) and discovered new scam sites. Scored higher but still rejected. |
| `/home/wg25r/review_agent/human_reviews_2026/7B9mTg7z25.md` (The Attacker Moves Second) | 6.00 | A paper about stronger adaptive attack methodology. Different contribution type but demonstrates what a mid-to-high-scoring security paper looks like — novel methodology, comprehensive evaluation, and actionable insights. |
| `/home/wg25r/review_agent/human_reviews_2026/9gw03JpKK4.md` (Gaia2) | 8.00 | A benchmark paper of the highest quality. Illustrates the gap between the current paper (empirical replication) and what constitutes a top-venue contribution. |

**Score assessment:** The current paper is cleanly executed and the results are practically useful, but the contribution is an empirical scaling demonstration rather than a novel method or deep insight. Compared to the anchor papers in the 3.5–5.0 range, it is on par with or slightly better than the 3.5 papers (more comprehensive evaluation) but lacks the methodological novelty of the 4.5–5.0 papers. The major weakness—limited novelty paired with an overstated robustness claim—prevents it from reaching the 5+ range.

**Score relative to anchors:** Positioned between the 3.50 anchors (MqLJRCUBYG, 3cK8gUZWBD) and the 4.50 anchor (yPgbdOdOPG). The paper's evaluation is more thorough than the 3.50 papers, but its novelty deficit relative to the 4.50 papers keeps it below that tier.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>