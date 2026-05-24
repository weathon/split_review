Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper revisits the simple idea of prompting an off-the-shelf LLM to detect and remove prompt injections. Prior work (circa 2023) dismissed this approach as ineffective because it was tested on weaker models. PromptArmor shows that with modern LLMs (GPT-4o, GPT-4.1, Qwen3-32B), the same idea achieves FPR and FNR below 1% on AgentDojo and below 5% on two other benchmarks, reduces attack success rate from 54.53% to 0.00%, and remains robust against adaptive attacks. The paper provides a comprehensive empirical evaluation against 7 baseline defenses across 3 benchmarks, along with ablations on model size, reasoning mode, and prompting strategies.

## Strengths

- **Near-perfect detection across multiple benchmarks (Table 1).** GPT-4o achieves 0.07% FPR and 0.23% FNR on AgentDojo, and both GPT-4o and GPT-4.1 maintain FPR and FNR below 5% on Open Prompt Injection and TensorTrust. This directly refutes prior claims that prompting-based defenses are ineffective and is the paper's central empirical contribution.

- **Attack success rate reduced to near zero with high utility preservation (Table 2).** PromptArmor-GPT-4.1 reduces combined ASR from 54.53% (no defense) to 0.00% while achieving 72.02% UA — higher than the undefended baseline (64.27%). The comparison against 7 baselines (Deberta, Llama Prompt Guard 2, DataSentinel, Repeat Prompt, Delimiter, Tool Filter, MELON) shows PromptArmor dominates on all security metrics while maintaining competitive utility.

- **Robustness against adaptive red-teaming (Table 4).** When AgentVigil generates attack templates specifically optimized to evade PromptArmor, the defense maintains 0.16% ASR (AgentVigil-Adaptive) with 0.70% FPR and 2.26% FNR — showing the approach is not trivially circumvented by attacks designed after seeing the defense.

- **Systematic ablation of model size and reasoning (Figure 3, Qwen3 family).** Varying model scale (0.6B → 8B → 32B) and reasoning mode in a controlled family provides clean evidence that model capacity is the primary driver of effectiveness, with reasoning providing additional benefit at intermediate scales. This analysis cleanly disentangles two factors that prior work conflated.

- **Memorization test (Section 4.5).** Using the Carlini et al. (2021) method, the paper shows GPT-4.1 is unlikely to have memorized AgentDojo data (average similarity 0.34, only 3.5% above 0.6 threshold), ruling out the concern that reported performance stems from benchmark contamination.

## Weaknesses

### Major

- **No naive-prompt baseline on the strong LLMs that actually work.** Section 4.3 states that "newer models like GPT-4o and GPT-4.1 perform equally well across different prompting strategies" — but provides no data for this claim. The prompting-strategy ablation (Table 3) is run only on GPT-3.5, which is the one model that underperforms. If a trivial prompt ("Does this contain a prompt injection? Answer Yes or No.") on GPT-4.1 already achieves the same near-perfect results, then PromptArmor's specific design (definition of prompt injection, output formatting, fuzzy matching) is not what drives its performance — the model alone is. The paper's framing emphasizes a "carefully designed system prompt" (abstract) as essential, yet doesn't present evidence isolating this contribution from model capability. This gap can be fixed by adding the naive-prompt baseline for GPT-4o/4.1.

### Minor

- **Exclusion of SecAlign lacks direct evidence.** The paper dismisses SecAlign by stating it "exhibit[s] poor utility on AgentDojo even in the absence of attacks" (Section 4.2) without presenting supporting data. A related-work citation to Jia et al. (2025) is provided, but the specific claim about AgentDojo utility is unsupported. If the authors have this data, they should include it; if not, the exclusion should be more carefully hedged.

- **Adaptive attack evaluation lacks qualitative characterization.** Section 4.6 reports aggregate metrics but provides no examples of the generated attacks, no analysis of attack diversity, and no discussion of whether the generated templates specifically target the guardrail LLM's detection heuristics. The setup is reasonable but thin — the claim of robustness would be stronger with at least a few illustrative examples.

- **No utility metric reported on clean (unattacked) inputs.** UA measures utility under attack, but there is no separate measurement of utility degradation when no attack is present. Even a 0.56% FPR can accumulate over many tool calls. Reporting the agent's task success rate on clean inputs with and without PromptArmor would clarify the practical cost of false positives.

- **Fuzzy matching removal is described but not evaluated.** The removal step uses a regex-based fuzzy match that "allows arbitrary characters between words." There is no analysis of how often this correctly extracts the injected string, whether it ever removes benign content, or whether it leaves injection artifacts. An evaluation of removal precision/recall would strengthen the claim about utility preservation.

### Trivial

- None that survive filtering — the paper is clearly written and the empirical sections are well-structured.

## Nice-to-Haves

- Testing on more obfuscated or context-blended attacks (e.g., injections that mimic legitimate system messages or are embedded in natural language instructions) would strengthen generalizability claims.
- Including the Sandwich Defense as a prompt-augmentation baseline, since it is cited in the references.

## Removed Points

The following points from the inputs were removed after verification:

- *"Abstract implies PromptArmor's specific design makes it work, not just the model"* — Partially kept above as the central Major weakness. The claim of overselling is softened because the paper's core thesis ("prompting a strong LLM should be a standard baseline") does not hinge on the specific prompt design being superior.
- *"The design rationale advantages are generic"* — This is a presentation observation, not a substantive weakness about the paper's claims or evidence. Removed.
- *"Memorization of attack patterns not tested"* — The paper tests benchmark data memorization (the standard concern). Testing memorization of attack patterns is a different, nonstandard question. Removed.
- *"Sandwich defense not included as baseline"* — A reasonable suggestion but a nice-to-have, not a weakness. Moved.
- *"The paper does not test on more obfuscated attacks"* — The paper evaluates on established benchmarks with standard attacks; asking for additional attacks is scope expansion. Moved to nice-to-have.
- *"Execution of fuzzy matching is described but not evaluated"* — Kept the evaluation gap but noted as Minor since the removal step is auxiliary to the core detection results.

## Novel Insights

None beyond the paper's own contributions. The most interesting finding not previously documented is the clean separation of model capacity vs. reasoning effects via the Qwen3 family (Section 4.4): model size is the primary driver of defense effectiveness, with reasoning mode providing meaningful gains only at intermediate scales (8B) and little benefit at either very small (0.6B, capacity bottleneck) or very large (32B, saturation) scales. This has practical implications for deployment decisions.

## Suggestions

1. **Add the naive-prompt baseline (most important).** Run GPT-4o and GPT-4.1 with a minimal prompt — e.g., "Does the following text contain a prompt injection? Answer Yes or No." without any definition, removal instruction, or output formatting. If results are equal to PromptArmor, reframe the contribution as an empirical demonstration that *model capability, not prompt design,* makes the approach viable. If results are worse, the paper gains a genuine design contribution.

2. **Provide quantitative support or remove the SecAlign exclusion.** Either include SecAlign numbers on AgentDojo, cite a specific source with data, or replace the hand-wavy dismissal with a more measured justification.

3. **Add qualitative examples from the adaptive attack evaluation.** Show 2–3 attack templates generated by AgentVigil, and discuss whether they target the guardrail's behavior or the backend agent.

4. **Report utility on clean inputs.** Add a row or column showing agent task success rate without any attack, both with and without PromptArmor, to make the FPR cost concrete.

---

## Calibration Report

**Round 1 — Bracketing.** Three queries over increasingly strict score bands:
- Low band (avg < 3.5): prompt injection defense papers averaged 2.33–3.00 (jailbreak detection, safety probing). These are empirically weak or narrow-scope papers. PromptArmor is clearly above this band.
- Middle band (3.5–7.5): promp injection / guardrail defense papers averaged 4.25–5.50 (PFT at 4.25, VLMGuard at 5.00, RA-LLM at 5.33, SPIN at 5.50).
- High band (7.5+): papers at 7.75–9.50 (safety alignment, benchmark cheating). These are top-venue papers on different topics.

**Round 1 bracket:** This paper sits above the rejected mid-band papers (4–5.5) but below the high-band (7.5+) papers. Narrowed range: **5.5–7.0**.

**Round 2 — Narrowing.** Two queries inside (3.5, 7.0):
- "Prompt injection defense benchmark evaluation guardrail" → 4.75–5.25 (Prompt Injection Benchmark at 5.25, Baseline Defenses at 5.25).
- "LLM security defense empirical evaluation strong results" → 5.75–6.75 (Rapid Response at 5.75, Probe before You Talk at 6.00, Durability of Safeguards at 6.50, Robustness Over Time at 6.75).

**Anchor comparisons read in full:**
- **SPIN (5.50):** Rejected. Similar topical area (prompt injection defense) but evaluated on only two small 7B models, no guardrail comparison, threshold calibration issues, limited attack evaluation. PromptArmor is empirically much stronger: 7 baselines, 3 benchmarks, multiple model scales, memorization test, adaptive attacks. **PromptArmor is clearly stronger.**
- **PFT (4.25):** Rejected. Narrow attack evaluation, missing important baselines, limited real-world applicability. **PromptArmor is substantially stronger.**
- **RA-LLM (5.33):** Rejected. Lack of baseline comparisons, small dataset, no adaptive attacks, no proprietary model experiments. **PromptArmor is stronger.**
- **Durability of Safeguards (6.50):** Accepted. This is a critique/re-evaluation paper with a different contribution type. Not directly comparable on empirical density but marks a reasonable upper bound for careful empirical work with clear limitations.
- **Rapid Response (5.75):** Rejected. Comparable empirical breadth but concerns about adaptive attacks and novelty. **PromptArmor is somewhat stronger** in empirical rigor and clear positive result.

**Final score:** The paper is clearly above SPIN (5.50) and comparable anchors in the 4–5.5 range — it has broader, more rigorous evaluation and a cleaner result. It is below the 6.5+ range because of the one structural weakness (missing naive-prompt baseline) and several minor evidence gaps. Within the 5.5–7.0 bracket, it sits closer to the upper end when considering the strength of its empirical evidence, but the framing issue pulls it back. **Score: 6.0.**

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>