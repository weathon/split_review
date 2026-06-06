## Summary

SmartSwitch is a training-free, plug-and-play inference framework for LongCoT LLMs that targets "underthinking" — the tendency of models to prematurely abandon promising reasoning paths. It uses linguistic cue detection to identify thought switches, a Process Reward Model (PRM) to score the abandoned thought's potential, and a "deepen prompt" injection to resume exploration of high-potential thoughts. The framework is evaluated on five models (1.5B–32B) across five math reasoning benchmarks, showing consistent accuracy improvements and inference time reductions.

---

## Strengths

- **Substantial, model-agnostic accuracy gains**: SmartSwitch improves pass@1 across all five tested models and five benchmarks, with notable gains of +16.7 points for 1.5B on AIME25, +23.3 for 7B on AIME25, and +7.2 for QwQ-32B on AIME24 (Table 1). The breadth of coverage across both competition-level and standard benchmarks provides genuine evidence for generalization.

- **Concurrent efficiency improvement**: Despite encouraging deeper exploration, SmartSwitch reduces wall-clock inference time by 14–35% and average total response length across most models on AIME24 (Tables 2 and 3). Critically, the response length reduction is more pronounced for correct answers (e.g., −12.1% for 7B, −16.2% for 32B), suggesting pruning of wasteful reasoning rather than mere truncation.

- **Selective PRM guidance is essential**: Table 4 shows "Always Intervene" (no PRM) degrades the 1.5B model from 20.0% to 18.9% on AIME25, confirming that indiscriminate deepening is harmful. The PRM-guided selectivity is a core design decision with clear empirical justification.

- **Clear advantage over alternative mitigations**: SmartSwitch (40.0%) substantially outperforms TIP (31.3%) and standard prompting (29.0%) on AIME24 for the 1.5B model (Table 5), demonstrating that context-aware, adaptive intervention outperforms heuristic suppression of thought-switching tokens.

- **Rigorous ablation of design choices**: Tables 6 and 7 systematically evaluate process division strategies and score aggregation strategies, with adaptive paragraph division (v4) and last-process scoring consistently dominating, grounding the engineering decisions empirically.

---

## Weaknesses

### Fatal

None verified.

### Major

**1. Threshold sensitivity in Table 8 raises an unresolved selection concern.**

Table 8 shows a striking pattern: τ=0.70 uniformly peaks for all five models on AIME24 (40.0%, 66.7%, 76.7%, 76.7%, 86.7%), while adjacent values τ=0.69 and τ=0.71 drop sharply — with 7B, 32B, and QwQ-32B falling *below* their vanilla baselines (e.g., 7B: vanilla=55.5 → τ=0.69 gives 43.3; QwQ-32B: vanilla=79.5 → τ=0.69 gives 73.3). The discontinuity is 10–14+ percentage points across one tick of threshold, uniformly for five architecturally diverse models.

The paper states simply "we set the promising score threshold to 0.7" (Section 5.1) without describing whether τ was selected from a held-out set, a different benchmark, or directly from AIME24 performance. The threshold ablation (Table 8) is performed only on AIME24 — the same benchmark where SmartSwitch posts its most dramatic headline gains. If τ=0.70 was chosen by evaluating on AIME24, the gains on that benchmark are inflated by construction.

The paper's limitations section acknowledges that "these parameters may require domain-specific or model-specific tuning," which implicitly concedes the sensitivity, but does not resolve whether the reported AIME24 gains are obtained under cold evaluation of a pre-selected threshold or through test-set tuning. The multi-benchmark gains (AIME25, AMC23, MATH-500, GaoKao2023en) in Table 1 provide partial reassurance that the method generalizes, but without an explicit selection protocol, the headline AIME24 numbers cannot be fully trusted.

**Recommendation:** The authors should disclose the threshold selection protocol explicitly — specifically, what dataset was used to arrive at τ=0.70, and whether that dataset overlaps with AIME24. Showing the threshold ablation on AIME25 or MATH-500 would directly test whether τ=0.70 transfers to unseen benchmarks.

**2. Unexplained discrepancy between time reduction and token reduction for small models.**

For the 1.5B model, Table 3 reports a 33.7% wall-clock inference time reduction on AIME24, while Section 5.3 states the actual token-count reduction is 9.93% (from 14,973.97 to 13,486.80 tokens). A 3.4× gap between time savings and token savings is inconsistent with linear decoding costs and deserves explanation. One plausible hypothesis is that under vanilla inference, the 1.5B model frequently hits the 32K maximum token limit (triggering full-budget waits), and SmartSwitch's primary benefit for small models may be avoiding this truncation rather than PRM-guided depth-directed exploration. The paper does not report the fraction of generations that reach the 32K token cap under vanilla vs. SmartSwitch inference, which would directly test this hypothesis. If truncation avoidance is the primary mechanism for small models, this is still a legitimate and useful contribution — but it is a different contribution from PRM-guided exploration and should be framed accordingly.

### Minor

**3. UF metric is partially circular with respect to the intervention.**

Equation (1) defines underthinking frequency as the count of thoughts shorter than token threshold L. SmartSwitch intervenes precisely by lengthening short thoughts (inserting a deepen prompt and extending generation). As a result, SmartSwitch reduces UF almost by construction — presenting the Figure 4(a) reduction in UF as "evidence that underthinking is reduced" partially conflates the intervention effect with the metric it is measured by. Figure 4(b)'s reduction in thought-switch counts is a more independent corroboration. The authors should acknowledge this limitation in the context of UF as a diagnostic tool.

**4. Absence of confidence intervals for small test sets.**

The paper evaluates on AIME24 (30 problems) and AIME25 (15 problems) with 32 sampled responses per query for pass@1 estimation, but reports no confidence intervals or standard deviations anywhere. For AIME25 in particular, a 10-point difference corresponds to 1.5 problems' worth of expected-value difference. Reporting standard errors would substantially strengthen confidence in the reported gains, especially for AIME25 results in Tables 4 and 6.

### Trivial

None beyond parser-induced formatting issues, which are excluded per review policy.

---

## Nice-to-Haves

- A comparison to best-of-N sampling with a verifier would contextualize whether SmartSwitch's gains reflect the architectural mechanism specifically or more generally reflect improved use of token budget. Best-of-N is a natural inference-time baseline for math reasoning.
- Reporting truncation-at-max-length rates under vanilla vs. SmartSwitch inference (especially for 1.5B and 7B) would sharpen understanding of the efficiency mechanism and is highly actionable.
- Extending the threshold ablation (Table 8) to at least one additional benchmark would establish whether τ=0.70 generalizes across domains without benchmark-specific tuning.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Harsh Critic: "UF direction of causality is not addressed"** — Removed. The paper's contribution is an engineering intervention; it does not require establishing a causal arrow between UF and failures. The empirical motivation (Figure 2b: higher UF for wrong answers) is sufficient to motivate the method, regardless of whether UF is a cause or consequence of failure.
- **Harsh Critic: "DeepSeek-V3 thought segmentation noise"** — Removed. The paper uses DeepSeek-V3 only for the offline underthinking investigation in Section 3, not for SmartSwitch itself. Sensitivity of the offline analysis to segmentation is a minor methodological note, not a threat to the main results. No specific error is identified.
- **Harsh Critic: "PRM 72B underperforms 7B — large gap is unexplained"** — Removed. The paper explicitly explains this in Section 5.5: Universal-PRM-7B supports 32,768-token inputs, while Qwen2.5-Math-PRM-72B has a ~4096-token context limit. The long-context LongCoT traces cannot be fully evaluated by the 72B PRM, explaining its underperformance. The paper handles this clearly and designates it a key feature for PRM selection.
- **Harsh Critic: "Comparison to best-of-N is missing"** — Moved to Nice-to-Haves. Best-of-N is not the standard baseline in inference-time reasoning papers of this type; its absence is a limitation but not a flaw.
- **Strength Finder: "Underthinking Frequency reduction validates intervention"** — Partially removed from Strengths. The UF reduction (Figure 4a) has the circularity issue noted above. The thought-switch count reduction (Figure 4b) is a more independent and credible corroboration.
- **Strength Finder: "Clear advantage over alternative methods"** — Kept, but noting that TIP comparison is on only one model (1.5B) on one benchmark (AIME24).

---

## Novel Insights

SmartSwitch contributes one genuinely novel operational finding: PRM-guided selective intervention dramatically outperforms uniform intervention ("Always Intervene" degrades accuracy), which establishes that the *selectivity* of deepening — not mere deepening itself — is the productive mechanism. The striking performance gap between Universal-PRM-7B and all Qwen-PRM variants, attributable to long-context support rather than model scale, reveals that long-context PRM evaluation capability is a bottleneck for this class of inference-time methods — a finding with implications for future PRM development. The joint observation of accuracy gain and inference time reduction (rather than the expected tradeoff) is an empirically interesting result suggesting that underthinking causes genuine token waste rather than simply insufficient exploration.

---

## Suggestions

1. **Disclose the τ selection protocol explicitly**: State whether τ=0.70 was identified from AIME24 data or from a separate held-out set. If from AIME24, conduct the primary evaluation under cold threshold (fixed from a different domain or split).
2. **Report truncation rates**: Add a table showing what fraction of generations hit the 32K token limit for each model under vanilla vs. SmartSwitch on AIME24. This directly tests the truncation-avoidance hypothesis for small model efficiency gains.
3. **Report confidence intervals**: For all AIME24/25 results, add standard errors across the 32-sample pass@1 estimates, particularly for AIME25 with only 15 problems.
4. **Extend threshold ablation**: Report Table 8's τ sensitivity on AIME25 or MATH-500 to demonstrate that τ=0.70 transfers across benchmarks without retuning.
5. **Acknowledge UF circularity**: Add a sentence in Section 5.3 noting that UF reduction partly reflects the mechanical effect of the intervention and that thought-switch count (Figure 4b) provides a more independent validation signal.

---

## Score and Decision

**Originality**: The idea of PRM-guided backtracking and deepening at thought-switch points is novel in this form; the individual components (PRM scoring, prompt injection) are existing techniques but their combination in a monitoring-and-backtracking loop is new. *3/5*

**Importance**: The underthinking problem is practically consequential and well-documented in the paper. A training-free method that improves LongCoT reasoning across model scales has clear community value. *4/5*

**Claims supported**: The multi-benchmark, multi-model empirical evidence is broadly supportive. The threshold selection concern introduces genuine uncertainty around the headline AIME24 figures, partially weakening these claims. *3/5*

**Soundness**: Method design is sound; ablations cover key decisions. The UF metric has circularity issues; the threshold sensitivity and time-vs-token discrepancy lack satisfying mechanistic accounts. *3/5*

**Clarity**: The paper is clearly written with a well-organized pipeline description, motivating examples, and comprehensive ablations. *4/5*

**Community value**: A plug-and-play, model-agnostic, training-free method with strong empirical performance is practically useful for the reasoning LLM community. Code is provided. *4/5*

Overall, SmartSwitch is a practically motivated, empirically well-supported inference-time method with genuine novelty. The primary concern — threshold selection transparency — is addressable in revision and does not invalidate the multi-benchmark gains. The paper sits at the border of accept with minor revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>