## Summary

This paper investigates whether activation steering — an inference-time technique that injects vectors into a model's hidden states to control behavior — can inadvertently compromise LLM safety. Through experiments across multiple model families (Llama-3, Qwen2.5, Falcon-3) and a standard 100-prompt harmfulness benchmark, the authors find that even steering in a *random direction* reliably produces harmful compliance (2–27% depending on the model), and that SAE feature vectors (the standard interpretable steering source) are comparably dangerous. They further construct a "universal attack" by averaging 20 vectors that individually jailbreak a single prompt, achieving up to 4× the compliance rate of random steering on unseen prompts.

## Strengths

- **Demonstrates that random (non-adversarial) steering systematically undermines safety across multiple model families.** Figure 2a shows that merely injecting a random unit-normal vector raises harmful compliance from 0% to non-zero rates for Llama3-8B, Qwen2.5-7B, and Falcon3-7B, and Figure 3 confirms this at scale (17% overall CR for Llama3-8B on JailbreakBench). This is a genuinely surprising finding that challenges the prevailing assumption that benign steering is harmless.

- **Proves that SAE features — intentionally benign and interpretable directions — are comparably dangerous to random noise.** Figure 2c directly compares random vs. SAE steering on the same model (Llama3.1-8B), showing SAE features yield 2–4% higher compliance. Crucially, the most dangerous features correspond to semantically benign concepts like "brand identity" (Figure 4a), making them indistinguishable from legitimate control vectors. The case study (Section 4.3) grounds this in a real API deployment with concrete harmful outputs.

- **Constructs a universal attack requiring minimal resources.** Section 4.4 shows that averaging 20 vectors that jailbreak a single prompt produces a universal vector that generalizes to most unseen JailbreakBench prompts, achieving up to 63.4% compliance on Falcon3-7B (vs. 5.7% for random steering). The attack is zero-shot, requires no model weights, gradients, or logits, and works across eight models of varying sizes.

- **Systematic layer and coefficient analysis.** The single-prompt sweep (Figure 2a,b) provides actionable findings: middle layers are most vulnerable, the effect is non-monotonic, and optimal coefficients vary across models — all of which inform both attack construction and potential defense design.

## Weaknesses

### Major

None. The issues raised by reviewers do not threaten the paper's core claims.

### Minor

- **The universal attack experiment lacks a control for averaging random vectors not filtered for jailbreak success.** The paper averages 20 vectors individually verified to jailbreak the bomb prompt, then compares against a *single* random vector. The missing control is averaging 20 random vectors drawn from the same distribution *without* verifying jailbreak effectiveness. If the unfiltered average also produces high compliance, then the mechanism is averaging per se rather than selective aggregation of effective vectors. This does not undermine the practical finding — the attack works — but it weakens the mechanistic claim that "localized vulnerabilities can be scaled into universal attacks" via targeted selection. The authors should add this control.

- **The full-dataset evaluation (Figure 3) does not include a direct random-vs-SAE comparison on the same model at scale.** SAE features are tested on Llama3.1-8B, while random steering is tested on Llama3-8B and Qwen2.5-7B — different model families with different baseline refusal strengths. The single-prompt comparison (Figure 2c) does directly compare random vs. SAE on Llama3.1-8B, mitigating this concern, but the cross-model comparison in the main evaluation makes the headline claim ("SAE features demonstrate comparable potential to random noise") rely partly on cross-model inference. Including a random-on-Llama3.1-8B condition in the full evaluation would strengthen this claim.

- **The full-dataset evaluation uses fixed steering coefficients per model without ablation.** The single-prompt sweep shows optimal coefficients vary by model and layer (Figure 2a,b), yet the full evaluation uses fixed coefficients (2.0 for Llama3-8B, 1.5 for Qwen2.5-7B, 2.0 for Llama3.1-8B SAE). Showing that the qualitative pattern (non-zero compliance across categories) holds across a range of coefficients would increase confidence.

### Trivial

- The paper asserts "for all models and prompts, the baseline compliance rate without any steering is 0%" (Section 3.4) without a dedicated summary table. While Figure 2 implicitly confirms this at coefficient 0.0, a brief explicit verification table would be cleaner.

## Nice-to-Haves

- The universal attack is tested only on JailbreakBench. Testing on a separate harmful-prompt dataset (e.g., AdvBench subset) would strengthen the generality claim.
- The SAE analysis is limited to one model (Llama3.1-8B) and one layer (layer 19). The authors acknowledge this, but the limitation is worth emphasizing: the claim that "SAE features are dangerous" may not generalize to other SAEs (e.g., Gemma Scope) or other layers.
- A brief discussion of *why* steering breaks safety (beyond the deferred Appendix E) would deepen the paper. Speculative mechanisms mentioned elsewhere (interference with refusal direction, stochastic degradation of refusal circuitry) could be discussed in the main text.

## Removed Points

These points were raised by reviewers but are excluded for the following reasons:

- *"0% baseline is asserted without evidence"* — **Removed.** The paper's Figure 2 shows 0% compliance at coefficient 0.0 for all models, which is an implicit demonstration of the baseline. The claim is also standard for aligned models on harmful prompts.
- *"LLM-as-judge is unvalidated"* — **Removed per instructions.** The paper references Appendix B for human annotation validation, which was stripped by the parser. The original submission contains this evidence.
- Various formatting and style nitpicks — **Removed per instructions** as they reflect parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the missing control to the universal attack experiment (Section 4.4):** Compare the average of 20 random vectors (unfiltered) against the average of 20 jailbreak-verified vectors. This distinguishes between averaging as a general phenomenon and selection as the active mechanism.
2. **Add random-on-Llama3.1-8B to Figure 3** to enable a same-model comparison between random and SAE steering at scale.
3. **Include a coefficient-ablation panel for the full-dataset evaluation** showing whether the qualitative findings hold at weaker/stronger steering strengths.

## Score and Decision

### Calibration report

**Round 1 (bracketing):** Searched three bands on activation steering, safety alignment, and jailbreak topics.
- Weak band (<3.5): 4 anchors, avg scores 2.5–3.0 (all Reject) — papers with limited scope or flawed execution. This paper is clearly above them.
- Middle band (3.5–7.5): 4 anchors including "Understanding Jailbreak Success" (4.75, Reject), "Steering Language Models with Activation Engineering" (5.00, Reject), "Improving Instruction-Following through Activation Steering" (7.00, Accept), and "Programming Refusal with CAST" (7.33, Accept).
- Strong band (>7.5): 4 anchors including "Safety Alignment Should Be More Than Just a Few Tokens Deep" (9.50, Accept), "Backtracking Improves Generation Safety" (8.00, Accept) — very strong accepted papers with clean novel methods.

**Initial bracket:** 4.5–7.5.

**Round 2 (narrowing):** Searched within (5.5, 7.5) on activation steering safety and universal jailbreak topics.
- "Safety-Tuned LLaMAs" (6.00, Accept) — less novel (known safety-helpfulness tradeoff); current paper has more surprising findings.
- "Programming Refusal with CAST" (7.33, Accept) — proposes a new method; current paper is comparably well-executed but documents a vulnerability rather than proposing a method.
- "Injecting Universal Jailbreak Backdoors" (6.67, Accept) — similar threat model.
- "Scaling Laws for Adversarial Attacks on LM Activations" (6.50, Accept) — strong empirical study; comparable in execution quality.
- "Failures to Find Transferable Image Jailbreaks" (6.25, Accept) — solid empirical work.

**Final score determination:** This paper is stronger than Safety-Tuned LLaMAs (6.00) due to greater novelty and surprise value. It is comparable to the scaling laws and jailbreak backdoor papers (6.50–6.67) in execution and significance. It is slightly below CAST (7.33), which benefits from proposing a practical new method. The paper's main weaknesses (missing control for universal attack, cross-model comparison in Figure 3) are bounded and addressable. **Score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>