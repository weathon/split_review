Now I have a good calibration. Let me synthesize my final review.

## Summary
This paper revisits the idea of using an off-the-shelf LLM as a prompt-injection guardrail — an approach previously deemed ineffective when tested on weaker models. With modern reasoning-capable LLMs (GPT-4o, GPT-4.1), the authors' PromptArmor achieves near-zero false positive and false negative rates on AgentDojo and strong results on two other benchmarks, reducing attack success rate to 0% while preserving reasonable utility. The paper also explores model size and reasoning effects through Qwen3 family experiments and includes a preliminary adaptive-attack evaluation.

## Strengths
- **Clear, timely contribution with strong empirical support.** The core claim — that modern LLMs can serve as an effective off-the-shelf baseline for prompt injection defense — is well-supported by experiments across three benchmarks (AgentDojo, Open Prompt Injection, TensorTrust). Table 1 shows GPT-4o and GPT-4.1 achieving FPR/FNR below 1% on AgentDojo, and Table 2 shows PromptArmor-GPT-4.1 reducing ASR from 54.53% to 0.00% while maintaining 72.02% utility under attack, substantially outperforming seven baselines.

- **Thorough ablation studies.** The paper investigates prompting strategies (Section 4.3), showing that including a definition of "prompt injection" dramatically improves GPT-3.5's performance. The Qwen3 scaling experiments (Section 4.4) demonstrate that while reasoning helps mid-sized models (Qwen3-8B FNR drops from 26.50% to 15.78% with reasoning), sufficient model capacity (32B) is the primary driver of near-perfect performance, and a 0.6B model fundamentally cannot balance security and utility regardless of reasoning mode. The memorization test (Section 4.5) rules out data contamination as a confound.

- **Practical detect-and-remove design.** Unlike prior work that simply discards flagged inputs, PromptArmor identifies and removes injected content via fuzzy matching, allowing the backend LLM to continue processing sanitized data — a genuine practical improvement demonstrated end-to-end through the UA and ASR metrics.

## Weaknesses

### Fatal
None.

### Major
- **Model-scale confound in baseline comparisons (Section 4.2, Table 2).** PromptArmor-GPT-4.1/4o is compared against detection-based defenses (Deberta, Llama Prompt Guard 2, DataSentinel) that use models orders of magnitude smaller (e.g., Mistral-7B for DataSentinel). The paper therefore shows that a very large prompted model beats smaller fine-tuned models, but does not disentangle the effect of model scale from the prompting approach. The Qwen3 experiments partially address this by showing a 32B open-source model can approximate GPT-4.1 performance, but a direct comparison against a fine-tuned model of comparable scale (e.g., fine-tuning Qwen3-32B on the same detection task) is absent. This limits the strength of the claim that _prompting_ specifically — rather than simply using a larger model — is the key.

### Minor
- **Prompt adjustments per dataset weaken the "single baseline" framing.** Section 4.1 states that "given the varying settings of the benchmarks, we adjusted the detection prompt for each dataset." While some adjustment for different input formats is reasonable, the paper does not report how much these adjustments affect performance or whether a single unified prompt would suffice. This makes it unclear whether the method generalizes to new attack surfaces without similar per-dataset tuning.

- **Limited adaptive-attack evaluation scope (Section 4.6).** The adaptive evaluation uses only one tool (AgentVigil) with five attack templates selected per run. While results are positive (0.16% ASR), the paper's claim that PromptArmor is "robust against adaptive attacks" overstates what this single-tool, five-template experiment can support. The attack space explored is narrow, and the attacks were not explicitly designed to evade the guardrail LLM's detection prompt itself.

- **AgentDojo negative set construction not fully specified (Section 4.1).** The paper describes the 629 adversarial scenarios but does not explicitly state how many clean samples were used or how they were constructed for FPR computation. For Open Prompt Injection and TensorTrust, the negative sets are described, but for AgentDojo — the primary benchmark where the strongest results are reported — this information is missing from the main text.

### Trivial
- The "computational efficiency" claim in Section 3.2 is misleading when the method requires querying large proprietary LLMs; the intended meaning (no training cost) should be clarified.
- The Repeat Prompt baseline achieves higher Utility under Attack (76.39%) than PromptArmor-GPT-4.1 (72.02%) in Table 2; this trade-off (utility vs. security) is noted but not discussed.

## Nice-to-Haves
- Unify the detection prompt across benchmarks to strengthen the "single baseline" claim, or systematically analyze the effect of per-dataset adjustments.
- Add a fine-tuned baseline of comparable model scale (e.g., fine-tuned Qwen3-32B) to isolate the prompting approach from model scale effects.
- Broaden the adaptive attack evaluation with additional tools or methods that explicitly target the guardrail LLM's detection prompt.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The full prompts are not reported in the main text"** — REMOVED. The paper states prompts are provided in Appendix C; the appendix was stripped by the parser. This is not an author error.
- **Harsh Critic: "The described prompt seems simple, which is promising" / "design rationale is partly aspirational"** — REMOVED. These are subjective assessments, not verifiable weaknesses.
- **Harsh Critic: "Cost and baselines — should note the use of same model as both backend and guardrail LLM"** — DEMOTED to trivial. The paper already acknowledges this in Section 3.1: "though in practice, both of them may use the same underlying model." It's a minor clarification point.
- **Harsh Critic: "Scope of conclusions — should delimit what 'essential baseline' means"** — REMOVED. The paper's scope is clear enough; this is a stylistic preference, not a substantive flaw.
- **Strength Finder: "Robustness to adaptive attacks" framed as a core strength** — RETAINED but tempered. The adaptive evaluation exists and shows positive results (0.16% ASR), but the scope is narrow. Listed under Minor weakness instead.
- **Harsh Critic: "For AgentDojo, the construction of the negative (clean) set is not explained"** — RETAINED as a minor weakness since the main text indeed lacks this detail for the primary benchmark.

## Novel Insights
The paper's most interesting finding is that the effectiveness of a prompted guardrail LLM depends not just on model scale but on whether the model _understands the concept of "prompt injection"_ — GPT-3.5, which did not recognize the term, achieved dramatically better performance once a definition was added to the prompt (FNR dropping from 60.24% to 15.74%). This suggests that the guardrail's success is partly a function of the model's security-related pretraining exposure rather than pure reasoning capability, which is a non-obvious insight that could inform future work on both attacks and defenses.

## Suggestions
- Clarify AgentDojo negative set size and construction method explicitly in the main text.
- Move a concise version of the prompts into a table in the main text showing how they differ across benchmarks, even if full prompts remain in the appendix.
- Temper the "robust against adaptive attacks" claim to reflect the limited scope of the current evaluation (e.g., "preliminary evidence of robustness against fuzzing-based adaptive attacks").

Now evaluating on the key axes:
- **Originality**: Moderate. The idea of prompting an LLM for detection is not new, but the systematic demonstration that modern LLMs reverse prior negative results is a valuable contribution.
- **Importance**: High. Prompt injection is a critical security concern for LLM agents, and establishing a strong, simple baseline is important for the field.
- **Well-supported claims**: The core claim is well-supported. Some auxiliary claims (adaptive robustness, computational efficiency) are overbroad.
- **Soundness**: Good. Comprehensive experiments with multiple benchmarks, models, and ablations. Some methodological gaps (model-scale confound, per-dataset prompt tuning) but they do not invalidate the central finding.
- **Clarity**: Good. Well-structured and clearly written, though some experimental details (negative set construction for AgentDojo) could be more explicit.
- **Value to community**: High. The paper provides a practical, easy-to-deploy baseline that future defenses should compare against, and demonstrates that previous negative results on this approach are outdated.

Final score anchored against: AC5n7xHuR1 (AgentHarm, 6.75, accept — benchmark paper with some evaluation concerns), fsW7wJGLBd (TensorTrust, 7.00, accept — dataset paper), syThiTmWWm (Null Models, 7.75, accept — stronger, more surprising finding). PromptArmor is comparable to AgentHarm in quality and contribution level, with somewhat more comprehensive empirical validation but lacking the benchmark-infrastructure contribution. Score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>