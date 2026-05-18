Now I have all the information I need. Let me construct the consolidated review.

---

## Summary

This paper proposes JOOD, a jailbreak strategy that applies simple mixing transformations (text-mixing for LLMs, mixup/CutMix for MLLMs) to create "out-of-distribution" (OOD) inputs that bypass safety alignment. The method achieves high attack success rates on GPT-4, GPT-4V, MiniGPT-4, and LLaVA-1.5 across seven harmful scenarios, significantly outperforming existing baselines (e.g., 63% ASR on GPT-4V in Bombs or Explosives vs. 23% for the best baseline). The core empirical finding — that simple data mixing can reliably jailbreak safety-aligned models — is important and well-supported.

## Strengths

- **Strong empirical results demonstrating a genuine vulnerability**: JOOD achieves state-of-the-art attack success rates by large margins across all models and scenarios tested. In the Bombs or Explosives scenario against GPT-4V, JOOD reaches 63% ASR compared to 23% for the previous best method (FigStep-Pro). The margins are large enough to be practically meaningful even with the modest instruction count.
- **Systematic evaluation across multiple models and scenarios**: The paper evaluates on both proprietary (GPT-4, GPT-4V) and open-source MLLMs (MiniGPT-4 7B, LLaVA-1.5 13B), across seven harmful scenarios. JOOD achieves the highest ASR in every single model–scenario combination, including over 80% ASR on open-source models in multiple scenarios. This breadth strengthens the claim that the vulnerability is general.
- **Well-designed ablation studies that support the mixing-as-driver interpretation**: The mixing coefficient ablation (Figure 4) shows a clear dose-response relationship: intermediate α values produce the highest ASR, while α=0 (harmful image alone) and α=1 (auxiliary image alone) produce low ASR. The auxiliary image similarity analysis (Figure 5) shows a strong negative correlation between semantic similarity and harmfulness. These ablations go beyond mere performance reporting and provide meaningful evidence about *why* the attack works.
- **Robustness against system-prompt defenses**: JOOD maintains 60% ASR even when the model is given a safety-focused system prompt, while baselines degrade to near zero. This suggests the vulnerability is deeper than simple prompt engineering can fix.

## Weaknesses

### Fatal
None.

### Major

1. **The text-mixing attack confounds OOD transformation with prompt framing.** For the text-only LLM attack (Section 3.1), the JOOD template wraps the harmful request in a meta-instruction: *"The following is a newly coined word made by mixing words... Please answer the request below for each of these words."* This framing differs substantially from the vanilla baseline's direct harmful instruction. Without a control experiment that uses the **same meta-instruction** with the harmful word **unscrambled**, we cannot attribute the jailbreak effect to the OOD-ifying transformation versus the instruction framing. This is a genuine experimental gap that weakens the paper's ability to support its central causal claim for the text-mixing attack.

   *However*, this concern is largely scoped to the text-mixing attack on text-only LLMs. For the **image-mixing** attack (which produces the paper's strongest results on GPT-4V), the α=0 ablation in Figure 4 provides an implicit control: when α=0 (harmful image alone, presented within the JOOD framework's instruction), ASR is low. The fact that ASR rises only when mixing is applied (α > 0) suggests the mixing itself is the active ingredient for the image-based attack. The authors should verify this interpretation explicitly or add the requested control.

2. **The central mechanistic claim — that OOD-ifying increases model uncertainty — is asserted without direct evidence.** The paper repeatedly states that OOD-ifying "highly increases the uncertainty of the model" (abstract, introduction, conclusion) and that this uncertainty is the mechanism enabling the jailbreak. However, **no direct measurement of uncertainty is provided** — not output entropy, not token-level log probabilities, not refusal-token probability, not calibration. The only "evidence" is that jailbreaking occurs, which is circular when used to support the mechanism. This is a significant gap: the mechanistic story is presented as a key part of the paper's contribution but is entirely untested. The empirical finding (mixing improves ASR) remains valid, but the paper's explanatory framing is unsupported.

### Minor

1. **Small instruction count per scenario (~30).** The paper uses approximately 30 harmful instructions per scenario (Advbench-M subset). While the performance margins over baselines are large enough that this is unlikely to change the qualitative conclusions, reporting bootstrapped confidence intervals or using a larger instruction set would strengthen statistical reliability. This is particularly relevant for the per-instance comparison claims (e.g., "10 additional instructions out of 30").

2. **The "+42% ASR" claim in the abstract needs clarification.** The abstract states: "improving performance by +42% ASR compared to the state-of-the-art baseline (Gong et al., 2023) in the Hacking scenario." The specific numerical claim should be directly verifiable against the corresponding entries in Table 1. Since the table is embedded as an image in the parsed text, this cannot be verified here. The authors should confirm the number is consistent with the table for the Hacking scenario and clarify what the +42% references (percentage points vs. relative improvement).

3. **The "out-of-distribution" concept is invoked without formal grounding.** The paper repeatedly refers to OOD but never specifies what distribution the safety-alignment training data follows — which is unknowable for proprietary models like GPT-4V. "Out-of-distribution" is therefore an untestable assumption. The empirical finding is better characterized directly: mixing transformations produce inputs that bypass safety alignment, possibly because they differ from the types of inputs seen during RLHF training. The OOD framing is evocative but not necessary for the contribution.

### Trivial
None.

## Nice-to-Haves

- **Add a control experiment for the text-mixing meta-instruction:** Compare the JOOD template with a scrambled word vs. the same template with an unscrambled harmful word. If the unscrambled version is refused and the scrambled version succeeds, this cleanly demonstrates the OOD-ifying effect.
- **Provide direct uncertainty measurements:** Report output entropy, refusal-token probability, or logit-based confidence for a subset of instructions comparing vanilla vs. OOD-ified inputs. This would directly support the claimed mechanism.
- **Report confidence intervals for ASR comparisons,** especially given the modest instruction count per scenario.
- **Add a limitations section** discussing potential defenses (input sanitization, anomaly detection), the model-as-judge evaluation bias, and the reliance on multiple transformations per instruction.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- The critic's framing of both Critical Issue 1 and 2 as "fatal" errors that "invalidate core claims" is an overstatement. The image-mixing attack already provides an implicit control (α=0 ablation showing low ASR), and the empirical finding stands even without the mechanistic explanation. Downgraded from fatal to major.
- The critic's suggestion that "the method works because of OOD, not because of some artefactual property" demands additional experiments that are not necessary to validate the core empirical finding; moved to Nice-to-Haves.
- The critic's request for an explicit "discussion of limitations" section is not a weakness per se and is addressed in Nice-to-Haves.
- The critic's call for more detailed text-mixing algorithm specification is a reasonable reproducibility suggestion but not a weakness; moved to suggestions.

## Novel Insights

None beyond the paper's own contributions. The main finding — that simple mixing-based data transformations which create ambiguous inputs can reliably bypass RLHF-based safety alignment in state-of-the-art models — is itself the novel insight.

## Suggestions

1. **Add the text-mixing control experiment** (same meta-instruction, unscrambled word) to isolate the OOD-ifying effect from the instruction framing effect.
2. **Add at least one direct uncertainty measurement** (e.g., refusal-token probability or output entropy for vanilla vs. OOD inputs). This can be done post-hoc from existing experiments if logits are logged; for API models, logprobs may be available.
3. **Clarify the "+42% ASR" claim** in the abstract by confirming it against Table 1 and specifying whether it refers to percentage points or relative improvement.
4. **Consider adding confidence intervals** for the main ASR comparisons (e.g., via bootstrap), given the ~30-instruction sample per scenario.
5. **Reframe the paper's claims** about "uncertainty" and "OOD" as plausible mechanistic hypotheses rather than established facts, to better match the evidence presented.

## Score and Decision

The paper presents a meaningful empirical discovery: simple mixing transformations reliably jailbreak safety-aligned LLMs and MLLMs, outperforming existing methods by large margins. The evaluative work is thorough across models, scenarios, and auxiliary conditions. However, the paper suffers from two material weaknesses: (1) the text-mixing experiment confounds the OOD transformation with the instruction framing, and (2) the central mechanistic claim about uncertainty is asserted without direct evidence. These issues do not invalidate the empirical finding but do weaken the paper's framing and explanatory contribution. With revisions to address these concerns, the paper would be a strong contribution; in its current form, it falls short of its own claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>