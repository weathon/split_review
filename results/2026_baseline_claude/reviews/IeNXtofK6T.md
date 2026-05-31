## Summary

PromptArmor revisits the idea of using an off-the-shelf LLM as a guardrail to detect and remove prompt injection attacks against LLM agents. The core claim is that the previous consensus—that prompting-based defenses are ineffective—was based on evaluations of older, weaker models; modern reasoning-capable LLMs (GPT-4o, GPT-4.1) can achieve both FPR and FNR below 1% on AgentDojo and below 5% on Open Prompt Injection and TensorTrust. Additionally, PromptArmor extends prior detection-only approaches by also removing identified injections via fuzzy matching, allowing the backend agent to continue executing the legitimate task.

---

## Strengths

- **Clear, timely empirical contribution.** The paper squarely demonstrates that a strong LLM (GPT-4o, GPT-4.1) with a carefully designed system prompt can achieve near-zero FPR/FNR on standard benchmarks. This directly updates a previously incorrect community understanding and has immediate practical value. The claim is credibly backed by three separate benchmarks.

- **Comprehensive comparison against baselines.** Table 2 compares PromptArmor against seven diverse baselines spanning fine-tuned detectors (Deberta, Llama Prompt Guard 2, DataSentinel), prompt augmentation (Delimiter, Repeat Prompt), system-level defenses (MELON), and Tool Filter. PromptArmor-GPT-4.1 achieves 0% ASR with 72% Utility under Attack, dominating on the security-utility frontier.

- **Instructive ablations on model capability.** The Qwen3 family experiments (0.6B, 8B, 32B with/without reasoning mode) provide a principled analysis showing that model scale is the primary driver of effectiveness, with reasoning providing secondary gains. This offers actionable guidance for practitioners constrained by compute budget.

- **Detect-and-remove rather than detect-and-discard.** The practical innovation of extracting and removing the injected portion via fuzzy matching, instead of discarding the whole data sample, is a meaningful improvement that preserves agent utility. UA for PromptArmor-GPT-4.1 (72%) exceeds the no-defense baseline (64.27%) on AgentDojo, which is a notable result.

- **Data contamination check.** Running the Carlini-style memorization test on GPT-4.1 across all AgentDojo samples (average similarity 0.34, 3.5% exceed threshold) meaningfully addresses the worry that good performance is due to benchmark memorization.

---

## Weaknesses

### Fatal
None.

### Major

**1. Adaptive attack evaluation is limited to fuzzing-based attacks, not attacks specifically designed to fool the guardrail.**
The paper evaluates AgentVigil-Adaptive, which optimizes attack templates by black-box feedback on end-to-end success rates. However, a white-box or targeted adaptive attacker who knows PromptArmor uses an LLM guardrail would directly craft injections designed to look like benign data to that guardrail—e.g., embedding instructions in natural prose, using indirection ("the following is a reminder from the system administrator"), or weaving the injected goal into what appears to be legitimate document content. The paper explicitly excludes white-box attacks, but the exclusion rationale ("most models in agents are black-box") does not cover adaptive prompt-level evasion, which requires only knowledge of the defense strategy, not model weights. This is the central vulnerability of prompting-based detection, and its omission is the paper's most significant gap.

**2. No cost or latency analysis.**
PromptArmor requires an additional API call to a strong LLM (GPT-4o or GPT-4.1) per tool-call result. In multi-step agentic workflows this can at least double the API cost and add meaningful latency. The paper claims "computational efficiency" as an advantage but provides no cost figures, API call counts, or latency measurements. This gap undermines the practical deployment argument, especially compared to fine-tuned small-model detectors.

### Minor

**3. Benchmark attack diversity may be limited.**
AgentDojo's four attack types (Ignore Previous Instructions, System Message, Important Messages, Tool Knowledge) are relatively simple, template-based patterns. It is not surprising that a state-of-the-art LLM detects them well. Real-world injections may be more subtle, context-dependent, or interleaved with legitimate content. The paper would benefit from evaluating at least one dataset with more naturalistic or human-adversarial injections.

**4. Context dependency of benign vs. malicious classification.**
The system prompt shown in Figure 2 asks the guardrail LLM to detect injection without access to the user's original task intent. The paper mentions that the guardrail can "leverage the context of the intended user task to detect inconsistencies," but the actual prompt does not consistently include user task context. The evaluation across datasets uses adjusted prompts ("we adjusted the detection prompt for each dataset"), which suggests non-trivial prompt engineering is required per deployment context—somewhat at odds with the "easy-to-deploy" framing.

**5. Fuzzy matching removal correctness is unanalyzed.**
When the LLM extracts the injection and fuzzy matching is applied for removal, it is possible that the matched region overlaps with legitimate data (especially for injections that semantically blend with content). The paper does not report how often removal over-strips content or corrupts the sanitized data sample.

### Trivial

None beyond the above.

---

## Nice-to-Haves

- A token/dollar cost comparison per defended agent task would meaningfully support the "computational efficiency" claim.
- An evaluation against attacks crafted to evade text-based LLM detection (e.g., instruction embedding in natural prose, multi-step indirect injections) would significantly strengthen the robustness narrative.
- Reporting the actual system prompts used per benchmark (not just in an appendix) or at minimum confirming they differ substantially would clarify the generalization claims.

---

## Novel Insights

The paper's most novel insight is not the prompting technique itself (which has existed since 2022) but the rigorous demonstration that the transition from GPT-3.5-era to GPT-4o/4.1-era models constitutes a qualitative phase shift in detection capability—turning an essentially useless defense (16%+ FNR with GPT-3.5) into one that dominates all trained specialized detectors tested. The additional finding that Qwen3-32B (a fully open model) matches GPT-4.1 performance suggests this capability is not proprietary, making PromptArmor accessible for self-hosted deployments. The result that enabling reasoning in 0.6B models actually worsens the FNR (from 37% to 76%) while improving FPR suggests that small models may be "over-reasoning" themselves into overcautiousness—a non-obvious interaction between scale and reasoning mode.

---

## Suggestions

- Add a targeted adaptive attack where the adversary crafts injections specifically to appear as benign user data to the guardrail LLM (e.g., injections embedded as quoted user feedback, system reminders, or structured data fields), and report whether PromptArmor maintains low FNR.
- Include a table of approximate API costs per task (input/output tokens for guardrail call × number of tool calls × model pricing) to substantiate the efficiency claim.
- For the fuzzy-matching removal step, report the rate of accidental over-removal on clean samples and whether this affects any agent task utility metrics.

---

## Score and Decision

PromptArmor delivers a well-executed, timely empirical update to a community belief, shows strong results on multiple benchmarks with diverse comparisons, and introduces the useful detect-and-remove paradigm. The contribution is somewhat incremental (same strategy, better model), and the adaptive attack evaluation has a meaningful gap. However, the practical value, completeness of ablations, and the corrective impact on community baselines outweigh these limitations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>