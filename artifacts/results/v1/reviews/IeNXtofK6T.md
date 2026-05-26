Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper revisits the idea of using a prompted off-the-shelf LLM as a guardrail against prompt injection attacks, overturning prior negative results (from 2023) by using modern LLMs with strong reasoning capabilities. The proposed PromptArmor prompts a guardrail LLM to both detect and *remove* injected prompts (rather than discarding the entire input), achieving near-perfect detection (FPR/FNR < 1% on AgentDojo) and reducing attack success from ~55% to ≤1% across three benchmarks. The paper further ablates the effect of model size and reasoning using Qwen3 models (0.6B–32B) and tests against fuzzing-based adaptive attacks.

## Strengths

1. **Clear, evidence-based overturning of a widely-held belief.** Prior work (Liu et al., 2024) had concluded that prompting an off-the-shelf LLM for injection detection was ineffective. PromptArmor directly contradicts this with comprehensive evidence: FPR 0.07% and FNR 0.23% with GPT-4o on AgentDojo (Table 1), and ASR reduction from 54.53% to 0.00% with GPT-4.1 (Table 2). This is a practically significant finding that will influence how future defenses are evaluated.

2. **Strong ablation isolating model capacity and reasoning.** The Qwen3 experiments (Section 4.4, Figure 3) cleanly separate the effects of model size and reasoning mode across 0.6B→8B→32B scales. The 0.6B model fails regardless of reasoning, 8B benefits from reasoning, and 32B matches GPT-4.1. This provides concrete guidance for practitioners and demonstrates the finding generalizes beyond proprietary APIs.

3. **Multi-benchmark evaluation with end-to-end metrics.** Unlike many detection papers that stop at FPR/FNR, PromptArmor measures Utility under Attack (UA) and Attack Success Rate (ASR) on AgentDojo — capturing the full defense impact. Evaluation covers agent (AgentDojo) and non-agent (Open Prompt Injection, TensorTrust) settings.

4. **Data contamination check.** The Carlini et al. memorization test on GPT-4.1 (average similarity 0.34, only 3.5% > 0.6 threshold) rules out the concern that high detection rates stem from benchmark memorization (Section 4.5).

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison conflates model capacity with method quality.** Table 2 compares PromptArmor (GPT-4o/4.1) against Deberta (BERT-scale), Llama Prompt Guard 2 (small model), and DataSentinel (Mistral-7B). The dramatic gap in FNR/ASR could be driven largely by the underlying model's capacity rather than any superiority of *prompting* over *fine-tuning* as a detection approach. The paper acknowledges DataSentinel uses a weaker model but does not control for this. The Qwen3 experiments (Section 4.4) partially alleviate this by showing Qwen3-32B (a model smaller than GPT-4.1) matches GPT-4.1's performance, but this still compares prompting to prompting, not prompting to fine-tuning on the same base model. A controlled comparison — e.g., fine-tuning GPT-4o/4.1 on the same detection task — would be needed to substantiate that the *method* (prompting) is what drives the advantage rather than the *model scale*.

### Minor

2. **Adaptive attack scope is limited to fuzzing-based variants.** The paper tests adaptive attacks via AgentVigil, which generates attack templates through fuzzing and recombination. To the paper's credit, it explicitly acknowledges these as "fuzzing-based adaptive attacks" (line 290). However, the framing
("robust against adaptive attacks specifically designed to circumvent it") implies a stronger claim. A truly adaptive adversary aware of the guardrail LLM could try character-level obfuscation, benign-mimicry, prompt splitting across samples, or attacks targeting the fuzzy-matching removal logic. The present evaluation does not address these.

3. **Per-dataset prompt adjustment is not justified.** The paper states "we adjusted the detection prompt for each dataset" (Section 4.1). While the prompts are included in Appendix C of the original submission, the paper does not explain what the adjustments were, what motivated them, or whether the method works without such tuning. If the prompts differ in substantive ways (not just formatting), any claim of generalization across benchmarks is weakened.

4. **Utility trade-off with Repeat Prompt is undiscussed.** PromptArmor-GPT-4.1 achieves UA=72.02% while Repeat Prompt — a simpler method — achieves UA=76.39% (Table 2). The paper never mentions this. For practitioners, the choice between a defense with perfect security but slightly lower task completion versus one with higher utility but 30% ASR is a real design decision that deserves discussion.

5. **No error bars or confidence intervals.** All tables report point estimates without variance. Given that AgentDojo has 629 test cases, a reported FNR of 0.13% corresponds to roughly 1 missed injection; binomial confidence intervals would clarify the reliability of these headline numbers.

6. **Computational efficiency claim is unsubstantiated.** Section 3.2 claims PromptArmor provides "computational efficiency" but provides no latency, throughput, or cost measurements. Calling a large LLM on every tool-call result is *prima facie* expensive — the paper should either provide measurements or drop the efficiency framing.

### Trivial

7. **Memorization test only on GPT-4.1.** The Qwen3-32B model also achieves strong performance (FNR 0.33%), so testing it for benchmark memorization would strengthen the data-contamination argument.

## Nice-to-Haves

- A same-model controlled experiment (prompting GPT-4.1 vs. fine-tuning a GPT-4.1-class model on the same detection task) would cleanly separate method from model capacity.
- Failure-case analysis: with FNR and FPR near zero, examining the handful of missed/false alarms would strengthen diagnostic value.
- Latency/cost analysis for the guardrail LLM call (tokens consumed, API cost, wall-clock time).
- Adaptive attacks designed to directly evade the guardrail LLM's detection (e.g., Unicode tricks, benign-mimicry, prompt splitting).

## Removed Points

- **"Adaptive attacks are not meaningfully adaptive because AgentVigil's optimization signal is attack success against an undefended agent."** — Removed as factually incorrect. The paper explicitly states AgentVigil-Adaptive runs against agents *with* PromptArmor (Section 4.6). The paper also qualifies the scope as "fuzzing-based adaptive attacks."
- **"Prompts relegated to Appendix C (unavailable to the reviewer)."** — Removed per policy: the parser strips appendices, and the paper states the prompts are present in the original submission. The substantive concern about per-dataset adjustment is preserved in Minor Weakness 3.
- **"Comparison with existing defenses is unfair because it favors the author's method"** — Actually, this criticism about asymmetry applies. Let me re-read: "REMOVE criticisms that are factually wrong or misunderstand the paper." The critic says the comparison is unfair because PromptArmor uses bigger models. This IS a valid concern. But checking the second rule: "REMOVE 'weaknesses' about unfair comparison with other methods if the asymmetry favors the baseline and not the author's method." Here the asymmetry favors the author's method (bigger model), so this does NOT get auto-removed by this rule. The rule says if asymmetry favors the *baseline*, remove it. Since it favors the *author's method*, it stays. So I keep the Major weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between two valid perspectives: the paper makes a simple, well-supported empirical finding that is practically important, but the evaluation design could more cleanly separate the contribution of "method" from "model scale." This is a tension the paper itself partially addresses (via Qwen3 experiments) but does not fully resolve.

## Suggestions

1. Add a controlled experiment: fine-tune a GPT-4o/4.1 on the same detection data and compare against the prompted version. This would directly test whether prompting itself has inherent advantages over fine-tuning at the same model scale.
2. Disclose and justify the per-dataset prompt adjustments in the main paper, ideally with ablation showing whether a single prompt works across all benchmarks.
3. Add binomial confidence intervals to all main results given the modest sample sizes.
4. Include at least one adaptive attack that explicitly targets the guardrail LLM's detection (e.g., obfuscation tricks, benign-mimicry injections) rather than relying solely on fuzzing.
5. Add a brief discussion of the UA trade-off between PromptArmor and Repeat Prompt.

## Score and Decision

Let me now calibrate against the retrieved anchors:

**Anchor list:**
- **GuardAgent** (avg 6.00, topic-high): Guardrail for LLM agents via knowledge-enabled reasoning. Rejected despite high avg. Complex design but limited baseline comparison. PromptArmor has more comprehensive evaluation but simpler method.
- **ASB** (avg 6.25, topic-high): Comprehensive agent security benchmark. Accepted. Much larger scope (10 scenarios, 400 tools, 90k test cases) but less focused contribution.
- **Prompt Infection** (avg 5.20, topic-mid): LLM-to-LLM prompt injection attack. Novel threat model but evaluation limited to GPT models and some presentation issues.
- **PFT** (avg 4.25, topic-mid): Position-enhanced fine-tuning for prompt injection robustness. Narrower contribution, weaker attack/defense baselines, questionable real-world applicability.
- **Your Agent Can Defend Itself** (avg 3.50, topic-low): Backdoor attack defense for agents. Much weaker evaluation.
- **Inverse Prompt Engineering** (avg 3.00, topic-low): Task-specific safety. Generic approach with limited evidence.
- **Specialized Foundation Models struggle** (avg 6.50, weakness-baseline): Shows that simple baselines beat specialized models. Similar high-level theme (simple baselines are strong), but this is a methodological contribution across domains rather than a specific security finding.
- **Blind Baselines Beat MIA** (avg 4.50, weakness-baseline): Shows evaluation flaws in membership inference. Shares the weakness that baseline comparisons can be misleading.
- **Quantifying Variance** (avg 4.17, weakness-error-bars): On the value of uncertainty quantification in benchmarks. Supports the need for confidence intervals.

The low-band topic anchors (3.00–3.50) fail on evaluation quality — they have limited experiments, unclear contributions, or weak baselines. PromptArmor is clearly stronger than these. The mid-band anchors (4.25–5.20) share some weaknesses with PromptArmor (limited attack scope, presentation issues) but have comparable evaluation scope. The high-band anchors (6.00–6.50) either have more novelty in framing (GuardAgent) or substantially broader scope (ASB), or are in different subfields. PromptArmor sits between the mid and high bands — its empirical contribution is stronger than the mid-band papers, but its 2 Major weaknesses and bounded contribution prevent it from reaching the 6+ level.

MY FINAL SCORE: 5.5
MY FINAL DECISION: Accept

The paper makes a clear, well-supported empirical contribution that overturns a widely-held negative result. The evaluation is comprehensive across three benchmarks with multiple models, good ablation analysis, and a memorization test. The major weaknesses (uncontrolled baseline comparison, undisclosed prompt adjustments) are significant but do not invalidate the core finding, and the suggestions are addressable in revision. The paper will serve as an important baseline for future prompt injection defense work.