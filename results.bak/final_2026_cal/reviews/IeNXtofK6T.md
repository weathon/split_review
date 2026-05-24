Now I have a solid calibration picture. Let me compile my final analysis.

**Round 1 Bracket: 5.0–7.0** — PromptArmor is clearly above the 3.2–5.2 band (SAID, SelfGrader, AlignSentinel, DiffuGuard) and below the 8.0 band (LLMs Get Lost, Gaia2, which are large-scale benchmark/topical papers of a different nature).

**Round 2 Narrowing:** Comparing against papers in the 5.0–6.5 range on related topics:
- ChatInject (5.00, Poster), VPI-Bench (5.33, Poster), A2ASecBench (5.50, Poster): PromptArmor has cleaner results and a more clearly scoped contribution.
- Foundational Guardrail (6.50, Poster): More engineering scope, but PromptArmor has more striking results (0.00% ASR) and a cleaner empirical story. PromptArmor sits slightly below this but comfortably above the 5.0–5.5 band.

**Final score: 6.0.**

Now let me write the consolidated review.

First, let me verify which weaknesses from the harsh critic and strength finder are real, and which I should remove.

**Verifying each claimed weakness:**

1. **DataSentinel comparison unfair** — The paper explicitly acknowledges (line 266-268) that DataSentinel uses Mistral-7B and wasn't adapted to the agent setting. The comparison is against the *published* version, which is standard. The critic's suggestion to "adapt DataSentinel's method to use GPT-4o" would mean retraining someone else's model — beyond reasonable scope. **Keep as minor weakness** with softened framing: the comparison is against published versions, but the gap may be partially explained by backbone model differences.

2. **Narrow adaptive attack evaluation** — The paper uses only AgentVigil (fuzzing-based). The claim in Section 4.6 is "robustness against fuzzing-based adaptive attacks" which is appropriately scoped. However, the broader title "Adaptive Attacks" could imply more generality. **Keep as minor weakness** — the evaluation scope is stated but limited.

3. **Lack of latency/cost analysis** — The paper claims "computational efficiency" in Section 3.2 but provides no measurements. This is a genuine gap. **Keep as minor weakness.**

4. **No error bars** — The paper uses temperature=0, but Open Prompt Injection involves random sampling. **Keep as minor weakness.**

5. **Missing limitations section** — Valid, but very minor. **Keep as trivial weakness.**

6. **Ablation on fuzzy matching** — The paper doesn't analyze how often exact matching fails. **Keep as nice-to-have.**

**Verifying Strengths (from Strength Finder):**

1. Near-zero FPR/FNR on AgentDojo with modern LLMs — confirmed in Table 1. **KEEP.**
2. Injection removal reduces ASR to near zero — confirmed in Table 2. **KEEP.**
3. Robustness against automated adaptive attacks — confirmed in Table 4. **KEEP.**
4. Controlled ablation of reasoning and model size — confirmed in Section 4.4, Figure 3. **KEEP.**
5. Memorization test rules out data contamination — confirmed in Section 4.5. **KEEP.**

All strengths check out.

Now let me write the review.Now I'll produce the final consolidated review.

## Summary

This paper revisits the idea of using an off-the-shelf LLM with a carefully designed system prompt as a guardrail against prompt injection attacks. While prior work (Liu et al., 2024) found such prompting-based defenses ineffective with older models, PromptArmor shows that modern LLMs with strong reasoning capabilities (GPT-4o, GPT-4.1) achieve remarkably low false positive and false negative rates across three benchmarks (AgentDojo, Open Prompt Injection, TensorTrust) and reduce attack success rates to near zero (0.00% on AgentDojo). The paper's core contribution is the empirical demonstration that a previously dismissed baseline now works very well and should be treated as a standard comparison point for future work.

## Strengths

- **Compelling central empirical finding (Tables 1, 2):** PromptArmor with GPT-4.1 achieves 0.56% FPR and 0.13% FNR on AgentDojo, cutting ASR from 54.53% (no defense) to 0.00% after sanitization. These results directly overturn the prior negative result from Liu et al. (2024) and provide clear evidence that the approach has become viable with modern LLMs.

- **Thorough, multi-faceted evaluation:** The paper evaluates across three distinct benchmarks (AgentDojo for agents, Open Prompt Injection and TensorTrust for non-agent settings), compares against seven existing defenses from four categories (detection-based, prompt augmentation, system-level, tool filtering), and reports FPR, FNR, UA, and ASR — providing a comprehensive picture of both security and utility.

- **Controlled isolation of key factors (Section 4.4, Figure 3):** Using Qwen3 models spanning 0.6B to 32B in both reasoning and non-reasoning modes, the paper cleanly demonstrates that model capacity (not just reasoning capability) is the primary driver of detection performance. The finding that Qwen3-32B matches GPT-4.1 regardless of reasoning mode, while Qwen3-0.6B cannot balance security and utility even with reasoning, is informative and well-supported.

- **Memorization test rules out data contamination (Section 4.5):** Using the prefix-suffix similarity test (Carlini et al., 2021; Staab et al., 2023), the paper shows average similarity of 0.34 on AgentDojo samples, with only 3.5% exceeding the 0.6 threshold, supporting the claim that performance reflects genuine detection ability rather than benchmark memorization.

- **Honest framing and appropriate scope:** The paper is transparent about what it is — a simple baseline that now works well — and does not overclaim novelty. It acknowledges limitations of older models (GPT-3.5) and contextualizes why DataSentinel's published version underperforms.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Latency and cost are unmeasured despite claimed "computational efficiency."** Section 3.2 lists "computational efficiency" as a core advantage, but the paper provides no measurements of inference latency or API cost per query. Using GPT-4o/4.1 as a guardrail for every tool-call result could introduce significant delay and expense in real agent deployments. This is a concrete gap between the paper's deployability claims and the evidence provided.

2. **Adaptive attack evaluation is limited to one automated fuzzing method.** Section 4.6 tests only AgentVigil (template-based fuzzing). While the paper appropriately scopes its robustness claim to "fuzzing-based adaptive attacks" in the results paragraph, the section title "Adaptive Attacks" and the broader claim that "PromptArmor is robust against adaptive attacks" (stated in the abstract/introduction context) could imply broader coverage. Human-crafted attacks, semantic obfuscation, homoglyph-based attacks, or attacks designed to exploit the fuzzy matching component are not tested.

3. **No variance or confidence intervals reported for sampled benchmarks.** For Open Prompt Injection, the paper samples 100 random tasks to construct the dataset, which introduces randomness, yet only single point estimates are reported. While temperature=0 makes AgentDojo results deterministic, the sampling procedure for Open Prompt Injection would benefit from reporting means and variances across multiple random seeds.

4. **Ablation on the fuzzy matching component is absent.** The paper relies on a fuzzy matching step to remove injected prompts (Section 3.1), but never analyzes how often exact matching fails, how often fuzzy matching introduces errors, or how removal accuracy affects the reported ASR numbers.

### Trivial

- The paper has no explicit limitations section; a brief paragraph discussing cost/scope/sensitivity to prompt design would improve completeness.

## Nice-to-Haves

- A single experiment measuring latency and API cost for PromptArmor-GPT-4.1 on a representative agent workload (e.g., 1000 tool-call results) would ground the "computational efficiency" advantage and help practitioners assess deployability.
- Testing adaptive attacks that specifically target the fuzzy matching removal mechanism (e.g., injections that are hard to extract cleanly) would strengthen the robustness analysis.
- An ablation comparing PromptArmor to DataSentinel's method *re-implemented* with a GPT-4o backbone (rather than Mistral-7B) would clarify how much of the performance gap is due to the approach itself vs. the backbone model.

## Removed Points

These points were raised by reviewers but are removed for the reasons given:

- **"DataSentinel comparison is unfair"** — The paper uses DataSentinel's *published* version (Mistral-7B, not agent-adapted). Comparing against published baselines is standard practice. The authors explicitly acknowledge these limitations. The suggestion to retrain DataSentinel with GPT-4o is beyond reasonable scope.
- **"Memorization test may not detect all forms of memorization"** — This is speculative. The prefix-suffix test is a standard, accepted method (Carlini et al., 2021; Staab et al., 2023).
- **"Paper does not discuss related works on X"** — The related works section is well-organized by defense category. Missing-related-works claims cannot be verified without external sources.
- **"Error bars missing for AgentDojo"** — AgentDojo uses temperature=0 and deterministic execution, so variance from model stochasticity is not expected.
- **"Reproducibility details relegated to appendix"** — The appendix is standard for supplementary materials. The paper provides the system prompt description and fuzzy matching approach in the main text.
- **Formatting, grammar, typo complaints** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a brief paragraph on latency/cost implications for practitioners who may want to deploy this approach.
- Report confidence intervals or variance across random seeds for the Open Prompt Injection and TensorTrust benchmarks where sampling is used.
- Add a small ablation study quantifying how often the fuzzy matching step is needed (vs. exact matching) to provide insight into the removal pipeline's reliability.

## Score and Decision

**Calibration Report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SAID (PKrYc2nyO4) | 3.20 | R1-low | Much weaker method and writing quality |
| Bypassing Prompt Guards (d1fVTnq3c8) | 2.50 | R1-low | Attack paper, different contribution |
| SelfGrader (qRSlhvA38I) | 4.00 | R1-mid | Rejected for limited novelty; PromptArmor's empirical framing is cleaner |
| AlignSentinel (yPgbdOdOPG) | 4.50 | R1-mid | Rejected for synthetic benchmark concerns; PromptArmor uses established benchmarks |
| DiffuGuard (zBPzxhso8M) | 5.20 | R1-mid | Accepted poster; PromptArmor has fewer methodological weaknesses |
| ChatInject (WVhgFSKniL) | 5.00 | R2 | Accepted poster; PromptArmor's defense contribution is stronger empirically |
| VPI-Bench (UMauKu2azg) | 5.33 | R2 | Accepted poster; different contribution type (benchmark) |
| A2ASecBench (LfdFnakqGJ) | 5.50 | R2 | Accepted poster; PromptArmor is stronger on evaluation quality |
| Foundational Guardrail (M47SWYubR5) | 6.50 | R2 | Accepted poster; more engineering scope, but PromptArmor has cleaner, more striking results |

**Round 1 Bracket:** 5.0–7.0 (between the weak papers at 2.5–5.2 and the strong topical benchmarks at 8.0). **Round 2 Narrowing:** PromptArmor sits above the 5.0–5.5 posters (ChatInject, VPI-Bench, A2ASecBench) due to cleaner results and clearer contribution framing, and slightly below the comprehensive Foundational Guardrail paper at 6.50 due to the latter's larger engineering scope. Final score: **6.0**.

This paper makes a well-supported, clearly communicated empirical contribution. It demonstrates that a previously dismissed baseline defense against prompt injection has become highly effective with modern LLMs — a finding that meaningfully changes how the community should evaluate future defenses. The weaknesses are minor and do not undermine the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>