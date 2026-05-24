Now let me write the consolidated review.

## Summary

This paper revisits the idea of using an off-the-shelf LLM to detect and remove prompt injections (PromptArmor), overturning prior findings (Liu et al., 2024) that this approach is ineffective. The key insight is that modern LLMs with strong reasoning capabilities (GPT-4o, GPT-4.1, Qwen3-32B) make the approach highly effective — achieving <1% FPR and FNR on AgentDojo, reducing ASR from 54.53% to 0.00% with GPT-4.1, and outperforming seven specialized baselines. The paper also includes ablations on model size, reasoning mode, prompting strategy, a memorization test, and an adaptive attack evaluation.

## Strengths

1. **Reversal of a prior negative finding with clear evidence.** Earlier work (Liu et al., 2024) concluded that prompting an off-the-shelf LLM as a guardrail is largely ineffective. PromptArmor provides concrete evidence to the contrary: with GPT-4o/4.1, both FPR and FNR are below 1% on AgentDojo (Table 1), directly demonstrating that the approach is now viable. This is a clean, well-motivated contribution that the community can build on.

2. **Near-complete attack mitigation while preserving utility.** On AgentDojo, PromptArmor-GPT-4.1 reduces ASR from 54.53% (undefended) to 0.00% while maintaining 72.02% utility under attack (Table 2). This substantially outperforms all seven baselines, including DataSentinel (ASR 38.63%, UA 46.38%), Llama Prompt Guard 2 (ASR 34.66%), and Tool Filter (UA 18.80%). The security–utility trade-off is clearly favorable.

3. **Memorization test rules out data contamination.** Section 4.5 conducts a rigorous memorization test (Carlini et al., 2021; Staab et al., 2023) on GPT-4.1, finding average similarity of 0.34 and only 3.5% of samples exceeding the 0.6 threshold. This rules out the common concern that benchmark performance is inflated by training data leakage.

4. **Systematic analysis of model size and reasoning across the Qwen3 family.** Using Qwen3 models from 0.6B to 32B parameters in both reasoning and non-reasoning modes (Figure 3), the paper provides quantitative evidence that sufficient model capacity is the primary factor for robust detection, with reasoning further improving the trade-off. This level of structured analysis is absent from prior prompting-based defense evaluations.

5. **Comprehensive comparison with diverse baselines.** PromptArmor is evaluated against seven existing defenses spanning three categories (detection-based, prompt augmentation, system-level) on the same benchmark (Table 2). This controlled comparison supports the claim that PromptArmor should serve as a strong baseline.

## Weaknesses

### Fatal

None.

### Major

1. **Adaptive attack evaluation is too narrow to fully support the robustness claim.** The paper tests only AgentVigil, a fuzzing-based method that generates new attack templates. Notably, even in the *undefended* setting, AgentVigil produces attacks with lower ASR (21.46%) than the original benchmark attacks (52.73%), indicating the generated attacks are not particularly strong. A proper adaptive evaluation for a detection-based defense should consider attacks directly optimized to bypass the guardrail LLM — for example, obfuscating injected instructions to appear benign to the detector, or exploiting prompt-level vulnerabilities in the guardrail's own instructions. The paper claims robustness "against adaptive attacks specifically designed to circumvent it" (Section 4.6) and "robust against adaptive attacks" (conclusion), but the evidence rests on a single attack generation method that may not approximate a determined adversary aware of the defense. This does not invalidate the core finding, but the robustness claim is overextended relative to the evidence.

### Minor

2. **Guardrail LLM coverage is limited to two model families.** The paper tests only OpenAI GPT models (GPT-3.5, GPT-4o, GPT-4.1) and the Qwen3 family. While these results are convincing for these families, the general recommendation that "prompting an off-the-shelf LLM with strong reasoning capabilities should be reconsidered as a powerful and important baseline" would be significantly strengthened by testing models from other providers (e.g., Claude 3.5/Opus, Gemini, Llama-3 70B/405B). Detection performance could vary due to differences in training data, alignment procedures, or instruction-following characteristics.

3. **Claim about prompt sensitivity for strong models is stated without evidence.** Section 4.3 states that "newer models like GPT-4o and GPT-4.1 perform equally well across different prompting strategies" but provides no empirical results to support this. Prompt sensitivity was tested only for GPT-3.5 (Table 3), where adding a definition helped substantially. Without assessing whether GPT-4o/4.1 are truly robust to prompt design variations, it is unclear whether the reported results depend on the specific wording used. The paper's own results show GPT-3.5 is highly sensitive to prompt phrasing, making it reasonable to expect some sensitivity in stronger models too.

4. **Computational efficiency claim is overstated.** Section 3.2 states that "even smaller LLMs can achieve effective detection performance," but the Qwen3 experiments (Section 4.4) show that the smallest model (0.6B) fails dramatically on at least one dimension (FPR 62.57% without reasoning, FNR 75.71% with reasoning), and the 8B model has moderate FNR (15–26%). The smallest model that achieves robust performance is 32B parameters, which is not "small" in any practical sense. This point should be qualified to models of sufficient capacity.

5. **Adaptive attack evaluation lacks key operational details.** The paper does not report the number of attack iterations attempted by AgentVigil, the success rate of generating effective templates, or the diversity of the generated attacks. These details would help the reader assess the practical difficulty an adversary would face in circumventing PromptArmor.

### Trivial

None that survive filtering.

## Nice-to-Haves

- **Cost/latency analysis**: Running a large LLM to screen every data sample adds overhead. A brief discussion of token cost, latency, and potential caching strategies would help practitioners assess real-world suitability.
- **Failure case analysis**: Showing a few representative false positives and false negatives would give insight into the defense's boundaries (e.g., what kind of inputs the guardrail mistakes as injections, or clever injections that bypass detection).
- **Confidence intervals**: While temperature=0 reduces variance, LLMs exhibit some nondeterminism. Reporting binomial confidence intervals for the main FPR/FNR results would strengthen credibility.
- **Integration with other defenses**: The paper notes in Related Work that system-level defenses (e.g., MELON, IsolateGPT) can be integrated with PromptArmor but does not evaluate this combination. Showing that a layered defense further reduces ASR would increase practical value.

## Removed Points

*These points were flagged for removal but preserved for reference.*

- **"Prompt is omitted from main text"** (Harsh Critic): The paper states the prompt is in Appendix C, which is stripped by the parser. This is a parser artifact, not an author omission.
- **"Missing confidence intervals for TensorTrust results"**: Not a standard requirement for this type of evaluation, particularly with temperature=0.
- **"TensorTrust negative set may not reflect realistic false positive scenarios"**: This is a property of the benchmark, not a flaw in the paper's methodology. The paper describes the setup transparently.
- **"Exclusion of SecAlign and StruQ"**: The paper provides a citation-based justification (Jia et al., 2025) for excluding them due to poor utility. This is a reasonable editorial choice, though testing them would have been stronger.
- **"DataSentinel comparison may exaggerate advantage"**: The paper explicitly notes the caveats about DataSentinel (Mistral-7B, not adapted to agent setting), so the comparison is transparent.

## Novel Insights

None beyond the paper's own contributions. The core finding — that the prior conclusion about prompting-based injection defenses being ineffective no longer holds with modern LLMs — is itself the novel insight.

## Suggestions

1. **Deepen the adaptive attack evaluation** by constructing attacks that specifically target the guardrail LLM (e.g., embedding injection text that exploits the guardrail's own system prompt, using encoding tricks like Unicode homoglyphs, or optimizing injection text against the guardrail's output distribution). This would demonstrate whether the defense holds against adversaries aware of the defense mechanism.

2. **Expand the guardrail LLM set** to include at least one model from a different commercial provider (e.g., Claude 3.5 Sonnet) and one larger open-source model from a different family (e.g., Llama-3 70B). This would directly test whether the conclusion generalizes across significantly different training recipes and architectures.

3. **Empirically verify the prompt sensitivity claim** for GPT-4o or GPT-4.1 by testing a handful of alternative phrasings of the detection instruction. A small ablation would confirm whether the reported low error rates are robust or fragile.

## Score and Decision

### Calibration details

**Round 1 — Bracketing.** Three queries on *prompt injection defense, LLM guardrail detection* across three score bands: (0, 3.5), (3.5, 7.5), and (7.5, 10). 

- Weak anchors (avg 2.33–3.00): papers with fundamental flaws, limited evaluation. *Inverse Prompt Engineering* (3.00), *Wildflare GuardRail* (3.00), *Jailbreak Leveraging Attention* (2.33). PromptArmor is clearly stronger than these.
- Middle anchors (avg 4.25–5.50): *SPIN* (5.50), *RA-LLM* (5.33), *VLMGuard* (5.00), *LLM Jailbreak Detection* (4.25). These have solid ideas but notable limitations (limited models, threshold generalization issues, narrow evaluation). PromptArmor is stronger — more benchmarks, more baselines, better ablations.
- Strong anchors (avg 7.75–9.50): papers with fundamental theoretical contributions. PromptArmor is clearly weaker than these.

**Initial bracket:** 5.5 – 7.5

**Round 2 — Narrowing.** Single query filter (5.0, 7.5) on *guardrail LLM prompt injection detection evaluation AgentDojo*. 

- *GuardAgent* (6.00, Reject): Similar guardrail agent topic, but evaluates on only 2 custom benchmarks with less comprehensive baseline comparison. PromptArmor is stronger.
- *Agent Security Bench* (6.25, Accept): Comprehensive benchmark paper with mixed reviews (3,6,8,8). PromptArmor is comparable in quality but makes a different type of contribution (defense method vs. benchmark).
- *AgentHarm* (6.75, Accept): Well-executed benchmark with broad model coverage and clear findings. PromptArmor is slightly weaker due to narrower model coverage.
- *Prompt Injection Benchmark* (5.25, Reject): Benchmark proposal with limited differentiation from prior work.
- *JudgeRail* (5.75, Reject): Open-source LLM guardrail with limited novelty.
- *Baseline Defenses for Adversarial Attacks* (5.25, Reject): Evaluates basic defenses (perplexity, paraphrasing) against adversarial attacks.

**Final position:** PromptArmor sits above SPIN (5.50), GuardAgent (6.00), and most middle anchors, and is comparable to ASB (6.25). It is weaker than AgentHarm (6.75) due to narrower model coverage and less thorough adaptive evaluation. The limitations identified (adaptive eval scope, model coverage, prompt sensitivity) prevent it from reaching the 7+ range but do not undermine its solid core contribution.

### Score

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>