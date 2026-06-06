## Summary
PromptArmor revisits the idea of using an off-the-shelf LLM as a guardrail detector for prompt injection attacks, arguing that prior negative results were based on weaker 2023-era LLMs. With modern models (GPT-4o, GPT-4.1), the approach now achieves sub-1% FPR and FNR on AgentDojo while reducing attack success rate from ~55% to 0.00%, positioning it as a strong and practical baseline. The paper includes ablations on model size and reasoning mode, comparisons against seven existing defenses, and a memorization test to rule out data leakage as a confound.

---

## Strengths

- **Near-perfect detection with modern LLMs on AgentDojo**: GPT-4o achieves FPR 0.07% and FNR 0.23% (Table 1), and GPT-4.1 achieves 0.56%/0.13% with a combined ASR of 0.00% (Table 2). This directly demonstrates the core claim and provides a dramatic quantitative baseline relative to the undefended 54.53% ASR.

- **Comprehensive comparison against a wide defense landscape**: Table 2 shows PromptArmor-GPT-4.1 outperforming all seven baselines on ASR, including detection-based (DeBERTa: 18.92%, Llama Prompt Guard 2: 34.66%, DataSentinel: 38.63%), prompt augmentation, and system-level methods (MELON: 3.18%), while maintaining competitive or superior utility.

- **Systematic ablation on model size and reasoning (Section 4.4)**: The Qwen3 family sweep (0.6B, 8B, 32B; reasoning vs. non-reasoning) produces clean, interpretable findings — 32B non-reasoning mode nearly matches GPT-4.1 (FNR 0.96%) — substantiating the central hypothesis that model capacity drives effectiveness.

- **Prompt engineering ablation (Table 3)**: Adding an explicit definition of "prompt injection" to GPT-3.5 reduces FNR from 60.24% to 15.74%, empirically validating that naive prompting fails and deliberate prompt design is necessary.

- **Memorization test (Section 4.5)**: Applying the Carlini et al. (2021) / Staab et al. (2023) prefix-suffix similarity test to GPT-4.1 yields an average similarity of 0.34 (3.5% above the 0.6 threshold), providing meaningful evidence that the strong detection performance reflects genuine reasoning rather than benchmark memorization.

---

## Weaknesses

### Fatal
None.

### Major

- **Adaptive attack evaluation tests only fuzzing, not semantic adversaries.** Section 4.6 uses AgentVigil, described by the paper as "an automated, adaptive red-teaming method… that generates new attack templates optimized based on feedback from success rates." Table 4 shows AgentVigil-Adaptive achieves FNR 2.26% and ASR 0.16%. However, AgentVigil operates as a black-box template search — it does not use knowledge of the published system prompt (Appendix C) to craft injections that impersonate benign data or argue against their own classification to the guardrail LLM. The paper explicitly publishes its defense mechanism, making semantic adversarial exploitation a realistic threat model for a deployed baseline. The introduction states "we demonstrate that PromptArmor is robust against adaptive attacks" without this qualifier, while the results section more carefully says "fuzzing-based adaptive attacks." The conclusion drawn is overstated: the evidence supports robustness against template-search adversaries but leaves the question of principled semantic evasion open. The paper would be strengthened by either bounding this claim explicitly or including a targeted white-box evaluation.

### Minor

- **Compounding FPR over multi-step agent trajectories is unanalyzed.** AgentDojo task suites involve multiple tool calls per trajectory (banking, workspace, etc. may require 5–10+ retrievals). The per-call FPR of 0.56% compounds non-trivially across trajectories, yielding a measurable probability of at least one false positive per task. The UA metric partially captures end-to-end effects but conflates multiple failure modes. The paper never acknowledges or quantifies this trajectory-level compounding, which would help practitioners correctly interpret Table 1's per-call figures. (Note: empirically the UA results are positive, so this does not undermine the conclusions, but the analysis is incomplete.)

- **Computational efficiency advantage is asserted without quantitative support.** Section 3.2 lists "Computational efficiency" as a core rationale, stating PromptArmor "avoids the significant costs associated with developing and training custom security models." This is accurate relative to training-based baselines, but PromptArmor-GPT-4.1 adds one full GPT-4.1 API call per tool-call result, roughly doubling inference cost in a GPT-4.1-backend agent. No latency or token-cost figures are reported per trajectory. The efficiency claim, as written, is a qualitative assertion; a rough quantitative estimate (average tool calls per AgentDojo task × inference overhead) would make it concrete.

- **TensorTrust negative samples are structurally unlike realistic agent data.** Section 4.1 specifies that TensorTrust negative samples are "correct access codes" — short, structured alphanumeric strings from a human-written access-control competition. These bear little resemblance to the instruction-rich tool-call outputs an agent would actually encounter. Near-zero FPR on TensorTrust therefore adds limited evidence about PromptArmor's behavior on realistic benign data and should be interpreted cautiously.

### Trivial

- Qwen3-32B non-reasoning mode achieves 0.00% ASR while reasoning mode gives 0.15%; this small inversion is not discussed. A sentence acknowledging this (e.g., possible output-format variability with reasoning tokens) would be informative.

---

## Nice-to-Haves

- A per-trajectory false-positive analysis: for each AgentDojo suite, compute the expected probability of ≥1 false positive given the observed per-call FPR and average number of tool calls, then compare against the observed UA delta. This would tighten the practical interpretation for agent deployments.
- An explicit scope statement in Section 4.6 that identifies "semantic adversaries targeting the guardrail's classification logic" as out-of-scope but important future work, and describes what such an attack would look like.
- Even a rough token-count or latency estimate per AgentDojo task trajectory (e.g., "an average of X tool calls, each adding ~Y input tokens to the guardrail call") would ground the efficiency claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **DataSentinel comparison is buried in a footnote** (Harsh Critic, Section 4.2): The paper addresses the model-capacity asymmetry directly in the main text of Section 4.2 ("the released version uses Mistral-7B as the guardrail LLM, which has limited reasoning ability; and (2) the fine-tuned guardrail LLM provided by the authors was not specifically adapted to the agent setting"), not in a footnote. The concern is already foregrounded and this criticism misreads the paper structure. REMOVED.

- **SecAlign exclusion needs more justification** (Harsh Critic): The paper explicitly states the rationale — "poor utility even without attacks" — and cites Jia et al. (2025) for evidence that training-based defenses degrade instruction-following. This is a reasonable and specific justification. REMOVED.

- **Sanitization precision failure mode** (Harsh Critic, Section 3.1): The critic hypothesizes that fuzzy matching may corrupt benign content or leave injection residue. This is a speculative failure mode not supported by any observed evidence in the paper. The UA results (72.02% with GPT-4.1 vs. 64.27% without) show the sanitized outputs are usable. Absent any empirical signal, this reads as speculation rather than an identified problem. REMOVED.

- **Open Prompt Injection sample construction needs clarification** (Harsh Critic, missing parts): The paper describes the construction clearly: "We randomly sample 100 target tasks from each target task set and 100 injected tasks from each injected task set, following the setting in Liu et al. (2024), to construct the positive set. We use the target tasks only, without injection, to construct the negative set." This is sufficiently detailed. REMOVED.

---

## Novel Insights

The most genuinely novel insight is the *model-capacity threshold hypothesis* demonstrated empirically in Section 4.4: there appears to be a qualitative capability transition between 8B and 32B parameters for this detection task, with Qwen3-32B achieving GPT-4.1-comparable performance without reasoning. This suggests that prompt injection detection is a cognitively bounded task — once a model crosses a sufficient capacity threshold, it can reliably perform the task without specialized training. The finding that Qwen3-32B non-reasoning mode achieves 0.00% ASR without incurring reasoning overhead has direct practical implications for cost-efficient deployment, and the trade-off profile (small models forced to choose between FPR and FNR extremes, with reasoning causing the pathological swing in Qwen3-0.6B) is an insightful characterization of the capacity requirement.

---

## Suggestions

1. Narrow the adaptive robustness claim in the abstract and introduction to "fuzzing-based adaptive attacks," matching the language used in Section 4.6, and add a brief sentence acknowledging that semantic evasion attacks remain an open evaluation gap.
2. Add a paragraph or figure computing expected false-positive-per-trajectory rates from the per-call FPRs, with comparison to the observed UA change — this closes the gap between detection and agent-level evaluation.
3. Include a rough cost estimate table (average tool calls per suite, tokens per guardrail call, estimated dollar cost per task vs. base agent) to ground the efficiency advantage concretely.
4. Add one sentence discussing the Qwen3-32B reasoning/non-reasoning ASR inversion (0.00% vs. 0.15%) and the possible mechanism (output format instability under reasoning).

---

## Evaluation on Key Axes

**Originality**: Moderate. The method itself — prompt an LLM to detect injections — is not new; the contribution is empirically demonstrating this is now highly effective with modern models and establishing it as a standard baseline. This is a legitimate and important revisionist contribution, not a methodological novelty.

**Importance of research question**: High. Prompt injection is a critical and underdefended threat to LLM agents in production, and establishing a reliable, easy-to-deploy baseline has clear practical value.

**Claims well supported**: Largely yes. The core detection and ASR claims are solid across three benchmarks and an ablation suite. The adaptive robustness claim is the one area where the evidence supports a narrower claim than stated.

**Soundness of experiments**: Good. Multi-benchmark evaluation, seven baselines, model size sweep, memorization testing, and an adaptive attack evaluation are all present. The main gap is the scope of the adaptive attack evaluation.

**Clarity of writing**: Good. The paper is well-organized, and the qualifications in the results sections (e.g., "fuzzing-based adaptive attacks") are appropriate, even if the introduction overstates the scope.

**Value to the research community**: High. Establishing a strong, reproducible baseline with published system prompt and code (Appendix C) and a clear model-size guideline is directly actionable for future work in this area.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>