Now I have a solid calibration. Let me write the final consolidated review.

## Summary

This paper identifies a *priming vulnerability* in Masked Diffusion Language Models (MDLMs): an affirmative token appearing at an intermediate denoising step can steer the remainder of generation toward a harmful response, even in safety-aligned models. The authors quantify this vulnerability through a controlled anchoring attack (ASR rises from 2% to 21% with a single-token intervention at step 1) and derive a tractable lower bound (Theorem 4.1) that enables First-Step GCG — an optimization-based attack that is 20× faster and up to 4× more effective than Monte Carlo GCG. To mitigate the vulnerability, they propose *Recovery Alignment* (RA), which trains models to generate safe responses from intentionally contaminated intermediate states using an RLHF-style objective. Experiments across three MDLMs, multiple attack families, and eleven general capability benchmarks show RA reduces ASR to near zero at early intervention steps with negligible utility degradation.

## Strengths

- **Systematic quantification of a new vulnerability.** The anchoring attack (Figure 2) cleanly isolates the priming vulnerability: injecting a single affirmative token at step 1 raises ASR from 2% to 21% for aligned LLaDA Instruct. This is direct, controlled evidence that the iterative denoising process is exploitable in a way fundamentally different from ARM prefilling attacks.

- **Tractable surrogate for optimization-based attacks.** Theorem 4.1 derives a lower bound that avoids costly Monte Carlo estimation over stochastic denoising paths. The resulting First-Step GCG (Table 1) achieves 58.0% ASR on LLaDA Instruct at 0.2 hours per prompt, outperforming Monte Carlo GCG (20.0% ASR, 4.3 hours) — a 20× speedup and ~3× ASR improvement. This shows the vulnerability is exploitable without direct intervention in the denoising process.

- **Recovery Alignment nearly eliminates the vulnerability at early steps.** Table 2 is the strongest evidence: RA brings ASR to 0.0% at intervention step 1 for LLaDA Instruct and LLaDA 1.5, and to 1.3% at step 4 for LLaDA Instruct. No baseline (SFT, DPO, MOSA) achieves comparable suppression — MOSA, the previous DLM-specific alignment, still has ≥5.0% ASR at step 1.

- **Robustness generalizes beyond the anchoring attack.** Table 3 shows RA reduces PAIR ASR from 44.3% to 10.0% on LLaDA Instruct and improves robustness against Crescendo and ReNeLLM, indicating that recovery training teaches a general re-detection and recovery capability rather than overfitting to the specific intervention pattern.

- **Negligible utility degradation across 11 benchmarks.** Table 4 shows average accuracy within 0.4 points of the original model for LLaDA (52.2 vs. 52.6), with improvements on TruthfulQA (+5.8 points). This demonstrates the safety gains do not come at substantial capability cost.

- **Ablations cleanly support the causal story.** RA *without* intervention (RA w/o inter) fails to reduce ASR below 20% at step 4 (Table 2), and Figure 3b shows linear scheduling of the intervention step outperforms constant or uniform scheduling. These results directly support the paper's claim about why existing alignments fail and why RA works.

## Weaknesses

### Major
None.

### Minor

- **The reward model is used without validation in an otherwise careful pipeline.** RA training uses DeBERTaV³ as the reward model without reporting its accuracy on the safety/helpfulness judgments that drive the RLHF objective. While this is a common practice in the alignment literature, the paper would be strengthened by a correlation analysis between the reward model's scores and the GPT-4o/LLaMA Guard evaluators on a held-out set of RA outputs. The final evaluation uses external judges, so this does not threaten the paper's core claims, but it makes the training signal an unmeasured confound.

- **The monotonicity assumption in Theorem 4.1 is empirically supported but not theoretically established.** The paper states the assumption holds across a broad range of models (Appendix C.2) and provides an intuitive justification. However, the theoretical guarantee that First-Step GCG is always a valid surrogate depends on this assumption. The paper is transparent about this, and the empirical results are strong, but readers should be aware the theoretical claim has a gap.

- **Residual vulnerability remains at late intervention steps (t_inter ≥ 32).** Table 2 shows RA reduces ASR from 96.7% to 50.7% at t_inter=32 for LLaDA Instruct, and from 99.0% to 79.3% for MMaDA. The paper acknowledges this is because "it is practically impossible to generate a contextually safe response due to many anchors," but does not discuss whether this is a fundamental limitation or whether training adjustments could push further. This is a real boundary on the method's practical effectiveness.

- **Improvement on ReNeLLM is modest.** In Table 3, RA reduces ReNeLLM ASR from 92.7% to 72.3% for LLaDA (and actually worsens MMaDA from 79.3% to 81.7%). The paper notes ReNeLLM is a "harder" attack type but does not analyze why RA handles PAIR and Crescendo well but struggles with ReNeLLM. This limits the scope of the generalization claim.

- **Choice of GRPO over simpler RL methods is not motivated.** The paper instantiates RA with GRPO but does not discuss whether alternative RL objectives (e.g., PPO, basic policy gradient) would yield different results, or whether GRPO was chosen for practical convenience. An ablation comparing RL objectives would strengthen the methodological contribution.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of the computational cost of RA training (reward model inference per step, training wall-clock time) relative to baselines would help practitioners assess adoption cost.
- The discussion of reward hacking at large t_max (Section 6.4) could be expanded: how was degradation detected, and can the schedule be adjusted to avoid it?

## Removed Points

The following points from the inputs are removed with justification:

- *"Table 2 erroneously uses 'LLaMA' as the model name header"* — This is a PDF parsing artifact (the font rendering of "LLaDA" was parsed as "LLaMA"). The original paper consistently uses LLaDA. Per hard rules, formatting/parser artifacts are removed.

- *"Algorithm 1 is redundant with the main text and could be moved to the appendix"* — A formatting/style preference, not a substantive weakness. Per hard rules, removed.

- *"The paper does not compare RA against RLHF without intervention"* — The paper includes RA w/o inter as an ablation, which directly serves this purpose. The criticism is factually inaccurate.

- *"Missing related works"* — Per hard rules, this cannot be verified without external sources. Removed.

- *"Monte Carlo objective not explained in full detail"* — The paper adequately describes the intractability of the MC objective; details are standard in the diffusion LM literature.

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: RA works very well when the contamination is early (t_inter ≤ 16) and degrades sharply for late contamination (t_inter ≥ 32). The harsh critic asks whether this residual ASR at late steps is a training instability issue, reward model imperfection, or a fundamental limit. Reading across the reviews, the most plausible reading is that this is partly a fundamental constraint (once too many harmful anchors are fixed, there is no safe continuation consistent with them) and partly a training limitation (the linear curriculum may not expose the model to enough late-step recovery practice). The paper's ablation on t_max scheduling (Figure 3b) hints at this — at very large t_max, training becomes unstable — but does not disentangle the two factors. Future work could design a curriculum that spends more steps at the high end of the intervention range to probe whether the residual ASR is compressible.

## Suggestions

1. Add a validation analysis showing that the DeBERTaV³ reward model's scores correlate with the GPT-4o/LLaMA Guard safety judgments used in evaluation, or replace it with a reward model whose safety accuracy is documented.
2. Include a brief discussion of why ReNeLLM resists RA more than PAIR and Crescendo — is it because ReNeLLM's prompt obfuscation bypasses the model's ability to detect harmfulness at intermediate steps?
3. Motivate the choice of GRPO over simpler alternatives, or ablate across RL objectives.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Queried "diffusion language model safety alignment vulnerability" across three score bands.
- Weak anchors (score < 3.5): Papers about simple jailbreaking attacks (1.4–3.0). Current paper is clearly stronger.
- Middle anchors (3.5–7.5): Diffusion Attacker (4.75, Reject), Fine-tuning Aligned LMs (4.75, Accept), Diffusion LMs Can Perform Many Tasks (5.0, Reject). Current paper is stronger than these.
- Strong anchors (7.5+): Safety Alignment Should be Made More Than Just a Few Tokens Deep (9.5, Accept) — a truly exceptional paper. Current paper is not at that level.
- **Initial bracket: 5.5–7.5**

**Round 2 (Narrowing within bracket):**
- Catastrophic Jailbreak (7.0, Accept): A very clean, simple attack paper. The current paper is comparable in quality but slightly less polished in its core finding. Current paper is slightly below this anchor.
- Adaptive Attacks (6.14, Accept): Strong empirical work but missing baselines and organizational issues. Current paper is cleaner and more complete.
- Breach By A Thousand Leaks (5.80, Accept): Mixed reviews, narrower scope. Current paper is stronger.
- Jailbreak in Pieces (6.25, Accept): Compositional VLMs attacks. Current paper is comparable but addresses a different model class with both attack and defense.
- Baseline Defenses (5.25, Reject): More of a survey/evaluation. Current paper is substantially stronger.

**Final score: 6.5** — The paper's novel vulnerability discovery, combined attack + defense contribution, and thorough evaluation place it above the ~6.0–6.25 accepted papers but slightly below the 7.0 Catastrophic Jailbreak paper due to the bounded but real methodological gaps (unvalidated reward model, residual late-step vulnerability, modest ReNeLLM improvement).

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>