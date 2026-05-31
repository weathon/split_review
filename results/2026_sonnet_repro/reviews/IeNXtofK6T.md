Now let me run the calibration search to anchor the score.**Round 1 bracket: 5.5 – 7.0** — The paper is clearly above the weak-reject band (the rejected 3.0 papers) and clearly below the score-8 papers which have genuinely novel methodological contributions. The most topically relevant anchors land at 5.25–6.25. Let me narrow within this range.Now I have enough to write the full review. Let me compile all findings.

---

## Summary

PromptArmor revisits the idea of using an off-the-shelf LLM as a guardrail for detecting and removing prompt injection attacks, arguing that the prior finding of ineffectiveness was an artifact of older, weaker models. With modern LLMs (GPT-4o, GPT-4.1), the approach achieves near-zero FPR and FNR on AgentDojo (<1% each), 0.00% combined ASR, and outperforms a broad set of detection-based, training-based, and prompt-augmentation baselines. The paper also includes an ablation on model size and reasoning mode using the Qwen3 family, a data contamination check, and an adaptive attack evaluation using AgentVigil.

---

## Strengths

- **Near-perfect detection performance on a challenging agent benchmark.** Table 1 shows GPT-4o achieves FPR 0.07% / FNR 0.23% on AgentDojo; GPT-4.1 achieves FPR 0.56% / FNR 0.13%. Table 2 shows 0.00% combined ASR with GPT-4.1, vs. 54.53% for the undefended baseline. This is a compelling empirical demonstration that the prior consensus ("prompting is ineffective") is no longer accurate.

- **Comprehensive baseline comparison across defense categories.** Table 2 compares against seven defenses spanning detection-based (DeBERTa, Llama Prompt Guard 2, DataSentinel), training-based (SecAlign excluded for stated reasons), prompt augmentation (Delimiter, Repeat Prompt), system-level (MELON), and tool-filtering (Tool Filter). PromptArmor-GPT-4.1 dominates on both FNR and ASR while maintaining competitive utility (UA 72.02% vs. best baseline Repeat Prompt at 76.39%).

- **Systematic ablation on model size and reasoning mode.** The Qwen3 experiments (Figure 3) show that model capacity is the primary driver of detection quality (0.6B fails regardless of reasoning mode; 32B approaches GPT-4.1 parity at FNR 0.96%/0.33%), while reasoning provides moderate benefit at intermediate scales. This directly supports the paper's central claim about reasoning capability.

- **Methodologically sound data contamination check.** Section 4.5 adapts the Carlini et al. (2021) memorization test to verify that GPT-4.1 has not memorized AgentDojo inputs (average prefix-suffix similarity 0.34; only 3.5% of samples above the 0.6 threshold), providing important support for the generalization claim.

- **Careful ablation of prompting strategy.** Table 3 shows that GPT-3.5 without a definition of "prompt injection" achieves FNR 60.24%, dropping to 15.74% with the definition. This validates the paper's emphasis on prompt engineering and explains why naïve prompting fails — a useful finding for practitioners.

---

## Weaknesses

### Fatal
None.

### Major

- **Adaptive attack evaluation scope is overstated.** Section 4.6 evaluates robustness against AgentVigil-Adaptive, described explicitly as "an automated, adaptive red-teaming method that generates new attack templates optimized based on feedback from success rates." This is a black-box template-fuzzing adversary. The paper's system prompt is published in Appendix C, meaning a principled white-box adversary can craft injections that semantically argue against their own classification (e.g., authority framing, context impersonation, legitimate-workflow mimicry). The paper's description of the result as demonstrating "robustness of PromptArmor against fuzzing-based adaptive attacks" is accurate in the text, but the section title and conclusion framing ("we demonstrate that PromptArmor is robust against adaptive attacks") is broader than the evidence supports. A white-box semantic adversary who knows the system prompt was not tested. This should be acknowledged more clearly as a known limitation, and the abstract/conclusion framing should be scoped to fuzzing-based adversaries.

### Minor

- **Compounding FPR over multi-step agent trajectories is not analyzed.** Table 2 reports per-call FPR of 0.56% for GPT-4.1 on AgentDojo. However, some task suites in AgentDojo involve multiple tool-call retrievals per trajectory. A per-call FPR of 0.56% compounds to a non-trivial trajectory-level probability of at least one spurious false positive. The UA metric partially captures this effect but conflates it with other failure modes. The paper never acknowledges this compounding behavior, which is directly relevant to the agent scenario it emphasizes. A sentence or brief analysis of trajectory-level false positive rates would sharpen the evaluation.

- **TensorTrust negative samples do not reflect realistic agent data.** The paper notes that TensorTrust negative samples are "correct access codes" — short, structured strings. The near-zero FPR on TensorTrust (GPT-3.5: 0.59%; GPT-4o: 0.67%) is therefore unsurprising and adds limited evidence about PromptArmor's false positive behavior on realistic, semantically richer agent data. The paper should acknowledge this as an artifact of the benchmark's construction.

- **Computational efficiency claim is about training costs only, but the deployment inference overhead is not discussed.** Section 3.2 claims "Computational efficiency" as a key advantage, arguing PromptArmor "avoids the significant costs associated with developing and training custom security models." This is accurate for training costs. However, in deployment, PromptArmor-GPT-4.1 requires an additional full GPT-4.1 API call for every tool-call result, roughly doubling inference cost and latency per retrieval step. No latency or token-cost measurements are reported. For a paper arguing this should be a practical "standard baseline," this is a notable gap — the efficiency claim is only partially supported.

### Trivial

- **Qwen3-32B reasoning mode underperformance deserves a sentence of explanation.** Figure 3 data shows Qwen3-32B non-reasoning achieves 0.00% ASR while reasoning mode gives 0.15%, with FNR of 0.96% vs. 0.33%. The reasoning mode yields better FNR but slightly higher ASR; this small but counterintuitive pattern is unexplained. A plausible hypothesis (output format variability from reasoning tokens disrupting structured output parsing) is worth one sentence.

---

## Nice-to-Haves

- A rough estimate of average tokens and API calls per AgentDojo task trajectory would make the cost efficiency argument concrete for practitioners and is not a methodological requirement.
- A white-box red-team experiment — constructing injections specifically designed to semantically convince the guardrail LLM they are benign content — would make Section 4.6 genuinely persuasive rather than suggestive. This would either validate or appropriately scope the robustness claim.
- Computing trajectory-level false positive probability (from per-call FPR and average tool calls per task suite) and verifying it aligns with observed UA drop would sharpen the agent evaluation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **DataSentinel comparison asymmetry as a fatal/major flaw (Harsh Critic).** The critic argues the model capacity gap (Mistral-7B vs. GPT-4.1) makes the comparison unfair. However, the paper explicitly acknowledges in the text: "DataSentinel uses Mistral-7B as the guardrail LLM, which has limited reasoning ability; and the fine-tuned guardrail LLM provided by the authors was not specifically adapted to the agent setting." The comparison is therefore not hidden. Per the hard rules, unfair comparisons that favor the baseline and not the author's method are not valid criticisms — the point was to show that even specialized fine-tuned detectors underperform. **Removed**: appropriately disclosed and directionally conservative.

- **Strength: "practical and reproducible workflow."** This is a generic description of the modular design. Removed per the filtering rules against generic strengths not backed by specific content.

- **Strength Finder's framing of AgentVigil-Adaptive FNR 2.26% as validating general adaptive robustness.** The 2.26% FNR is real (Table 4) but the claim that it supports robustness against "targeted exploitation" or principled adversaries is overstated. The strength as stated is partially correct — the defense does hold against this class of attack — but should not be claimed as general adaptive robustness. Demoted and merged into the major weakness above.

---

## Novel Insights

The most genuinely novel observation in this work is not the defense itself — which was known — but the *calibration* finding: that the reasoning capabilities required for effective prompt injection detection appear around the 32B parameter scale for open-source models (Qwen3-32B non-reasoning: FNR 0.96%, ASR 0.00%), and that reasoning mode provides disproportionate benefit at mid-sizes (Qwen3-8B FNR drops from 26.5% to 15.78%) but is not needed at large scales. This model-capability characterization is practically useful for deployments where using GPT-4-class models as guardrails is cost-prohibitive.

---

## Suggestions

1. Retitle or re-scope Section 4.6 to "Robustness Against Fuzzing-Based Adaptive Attacks" and add a brief paragraph on the open question of semantic white-box adversaries who know the published system prompt.
2. Add one sentence to the conclusion acknowledging that the per-call FPR compounds over multi-step trajectories, and note that the UA metric in Table 2 reflects this aggregate effect.
3. Add a table in Section 3 or Appendix estimating average API calls and tokens per AgentDojo trajectory to ground the efficiency claims.
4. Address the Qwen3-32B reasoning-mode FNR/ASR discrepancy with one explanatory sentence.

---

## Score and Decision — Calibration

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| MV5j4Qpq7N.md (Jailbreak via system-prompt attention) | 2.33 | R1-weak | Clearly weaker; narrow, preliminary work |
| 3MDmM0rMPQ.md (Inverse Prompt Engineering) | 3.00 | R1-weak | Weaker; limited evaluation, generic defense |
| lUyYX9VFgA.md (Code-of-thought prompting) | 3.00 | R1-weak | Unrelated; attack paper |
| 5kMwiMnUip.md (NEMESIS jailbreaking) | 1.40 | R1-weak | Much weaker |
| 0VZP2Dr9KX.md (Baseline Defenses for Adversarial LLM Attacks) | 5.25 | R1-mid / R2 | Weaker than PromptArmor — inconsistent setups, single attack, incomplete methodology |
| V01FPV3SNY.md (Robustly Aligned LLM) | 5.33 | R1-mid | Slightly weaker — single-defense paper with broader claims |
| MsRdq0ePTR.md (Prompt Injection Benchmark) | 5.25 | R1-mid / R2 | Benchmark paper with narrower insights; PromptArmor more actionable |
| V4y0CpX4hK.md (Agent Security Bench) | 6.25 | R1-mid / R2 | Accepted; most topically relevant. Broader scope but weaker rigor; PromptArmor comparable or slightly below |
| leSbzBtofH.md (AutoAdvExBench) | 6.17 | R2 | Similar range; benchmark paper, different topic |
| YauQYh2k1g.md (Dissecting Adversarial Robustness of Multimodal Agents) | 6.25 | R2 | Accepted; more novel methodology; PromptArmor slightly below |
| S1Bv3068Xt.md (Backdoor Attacks against Embodied LLM) | 6.25 | R2 | Accepted; proposes novel attack framework; higher originality |
| tTPHgb0EtV.md (Booster: Harmful Fine-tuning) | 8.00 | R1-strong | Clearly stronger; novel method with robust theoretical and empirical support |
| Bo62NeU6VF.md (Backtracking for Generation Safety) | 8.00 | R1-strong | Clearly stronger; novel mechanism |
| oZtt0pRnOl.md (DP In-Context Learning) | 8.00 | R1-strong | Unrelated topic; stronger theoretical contribution |
| 4KqkizXgXU.md (Curiosity-driven Red-teaming) | 8.00 | R1-strong | Different topic; novel RL methodology |

**Round 1 bracket:** 5.5–7.0

**Round 2 narrowing:** The three accepted anchors at 6.25 (ASB, Dissecting Adversarial Robustness, Backdoor Attacks on Embodied LLM) all have broader scope or higher methodological novelty than PromptArmor. PromptArmor is fundamentally a revisitation paper with a clearly stated incremental contribution (modern LLMs make a known approach effective). However, its empirical execution is tighter than ASB, its claims are more precisely bounded, and its practical impact as a field-level baseline-setter is genuine.

PromptArmor sits *at or just below* the 6.25 accepted anchors. The major weakness (overstated adaptive robustness claim) and the inherently incremental nature of the contribution pull it slightly below ASB. The tight empirical execution, systematic ablation, and field-level relevance hold it above the 5.25 rejected papers.

**Final score: 6.0 — Accept**

The paper corrects a field-wide misunderstanding with solid evidence, provides a reproducible and practical defense baseline, and includes a systematic characterization of the relationship between model capability and injection detection effectiveness. The main weaknesses (adaptive attack scope, compounding FPR analysis, inference cost) do not undermine the core contribution and are addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>