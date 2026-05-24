Now I have a clear picture of the calibration landscape. Let me synthesize everything into the final review.

## Summary

This paper presents an empirical study demonstrating that activation steering — a technique often framed as precise, interpretable, and safe — systematically undermines LLM safety alignment. Through experiments on 8 models across 3 families (Llama3, Qwen2.5, Falcon3/FalconH1, 3B–70B parameters) with ~300,000 responses, the authors find that (1) even random steering vectors produce non-zero harmful compliance (2–27%), (2) SAE-derived steering vectors (from Goodfire's SAE on Llama3.1-8B) show comparable or slightly higher danger, with the most effective features corresponding to benign concepts like "brand identity", and (3) averaging 20 random vectors that jailbreak a single prompt creates a universal attack vector that increases compliance by ~4× on unseen JailbreakBench prompts. A practical case study confirms exploitability via a public production API.

## Strengths

1. **Core finding is robust and well-supported across diverse models.** The demonstration that even *random* steering systematically breaks refusal mechanisms is tested across Llama3 (8B, 70B), Qwen2.5 (3B, 7B, 32B), and Falcon3/FalconH1 (3B, 7B, 34B), with baseline compliance of 0% rising to 2–27% under steering (Figures 2a, 2b, 3). This is the paper's strongest and most reproducible claim.

2. **Practical significance is grounded through a real API case study.** Section 4.3 demonstrates jailbreaking Llama3.1-8B via the Goodfire production API using a benign "brand identity" SAE feature, producing two distinct failure modes (disclaimer-then-compliance, fictional framing). This moves the threat from abstract to concrete.

3. **Universal attack construction is clever and minimally demanding.** Averaging 20 prompt-specific random vectors (obtained through 100–500 trials) produces a vector that increases compliance by 4× on average across unseen JailbreakBench prompts — requiring only black-box access to the steering interface, no model weights or gradients. The effect for Falcon3-7B (5.7% → 63.4%) is particularly striking.

4. **Systematic experimental sweep across layers and coefficients.** The paper varies both the intervention layer (first third, middle, last third) and steering coefficient, identifying that middle layers are most vulnerable and that the effect is non-monotonic with strength (Figures 2a, 2b). This methodological care strengthens the reliability of findings.

5. **Cross-category analysis supports the monitoring-infeasibility argument.** Figure 4b shows that dangerous SAE features generalize poorly across categories (conditional probabilities near baseline), providing evidence that systematic safety screening is practically impossible.

## Weaknesses

### Fatal
None.

### Major

1. **SAE experiments are limited to a single SAE at a single layer of one model (Llama3.1-8B, layer 19).** The paper's second main claim — that SAE feature steering has "comparable potential" to random noise and that benign features are the most dangerous — rests entirely on Goodfire's SAE. The paper acknowledges this in §3.3 ("We therefore limited our investigation...") but frames the finding as challenging "the paradigm of safety through interpretability" (Abstract) — a broader claim than the evidence supports. Without testing at least one additional SAE family (e.g., Gemma Scope, a different training run, or a different layer), this remains a suggestive but narrow observation. The SAE finding is the paper's weakest evidential link, and the scope of conclusions should be tempered accordingly.

### Minor

2. **The "universal" attack framing is weakened by model-dependent failures.** In Figure 6, averaging 20 unsafe directions for Qwen2.5-32B yields 9% compliance — identical to random steering and *lower* than individual unsafe directions (16%). The paper acknowledges this ("as evidenced by the reduction in performance observed for Qwen2.5-32B") but does not analyze *why* averaging fails on certain models. Without a diagnostic (e.g., cosine similarity to refusal directions, correlation with model capacity), the claim is not truly "universal" and the boundary conditions are unknown.

3. **LLM-as-judge evaluation could share family bias with tested models.** The judge is Qwen3-8B, and tested models include Qwen2.5-3B/7B/32B. If the judge and tested model share family-specific calibration biases (both under- or over-classifying certain categories), reported compliance rates could shift relative to human judgment. The paper mentions human annotation quality assessment in Appendix B (stripped by parser), which partially mitigates the concern, but the potential interaction is not discussed. A small human annotation subset (e.g., 200 responses) would substantially increase confidence.

4. **No analysis of why averaging works for the universal attack.** The paper constructs the universal attack by averaging vectors but does not investigate the mechanism (e.g., does the average align with a refusal-suppression direction, or simply improve signal-to-noise?). An ablation varying the number of averaged vectors (1, 5, 10, 50) would strengthen the contribution and help characterize the method's boundaries.

### Trivial

None.

## Nice-to-Haves

- A quantitative comparison of the reported compliance rates (10–27%) against established adversarial jailbreak methods (which often achieve >90%) would help readers assess practical severity, though the paper's key contribution — that *benign* vectors suffice — is independent of this comparison.
- The inconsistent depth selection across experiments (Fig. 2b shows middle layers are most vulnerable, but Fig. 3 uses 1/3 depth for random steering) should be explained: since 1/3 depth is plausibly *less* vulnerable, the reported rates are conservative, which the paper should state explicitly.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Threshold of 5 prompts is arbitrary"** — Using a threshold of "at least 5 prompts out of 100" to classify features as dangerous is standard practice for defining a meaningful baseline; this is not an arbitrary or problematic choice.
2. **"No analysis of steering direction relative to refusal direction"** — The paper explicitly references Appendix E for this analysis ("Preliminary analysis of potential mechanisms (App. E) suggests this safety compromise is not due to simple alignment with known refusal directions"); the appendix is only absent because of parser stripping.
3. **"Inconsistent depth selection"** — The paper states it uses the first-third layer as its "primary baseline for comparative analysis." Using a less vulnerable layer makes the reported compliance rates conservative, which *strengthens* rather than weakens the paper's conclusions.
4. **"Missing comparison to established jailbreak methods"** — The paper's scope is specifically about *benign* vectors compromising safety; comparing to adversarial attacks is outside this scope. The paper correctly notes its finding is distinct from adversarial jailbreak vectors.

## Novel Insights

None beyond the paper's own contributions. The reviewers' inputs do not surface any observation about the paper that is not already present in or directly derivable from the paper's own discussion.

## Suggestions

1. **Expand SAE validation to at least one additional SAE source** (e.g., Gemma Scope's SAEs or a different layer/run of the Goodfire SAE) to support the broad claim about "the paradigm of safety through interpretability." Even a single additional data point would substantially strengthen this finding.
2. **Diagnose the universal attack failure on Qwen2.5-32B.** Measure cosine similarity between the average vector and known refusal directions, or check if the attack correlates with model size/alignment method, to characterize when averaging helps and when it doesn't.
3. **Validate judge calibration with a human annotation subset** (e.g., 200 samples) to rule out family-specific bias from the Qwen3-8B judge.
4. **Acknowledge the potential judge-model interaction explicitly** in the limitations or evaluation section, even if only to explain why the shared family is not expected to bias results.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (score < 3.5): three papers on steering-related topics scoring 2.0–3.33 (Rejected/Withdrawn). The current paper is clearly stronger than all of these.
- Middle anchors (score 3.5–7.5): SteeringSafety (6.0, Reject), AlphaSteer (7.0, Accept Poster), Context-Specific Steering (4.0, Reject), COLD-Steer (6.0, Accept Poster), Refuse without Refusal (5.5, Reject). The current paper is stronger than Context-Specific Steering (4.0) and roughly comparable to SteeringSafety (6.0) and COLD-Steer (6.0).
- Strong anchors (score > 7.5): Narrow Finetuning (7.5, Accept Poster), Persona Features (7.5, Accept Poster). These papers are stronger than the current paper due to broader experimental scope and/or deeper mechanistic analysis.

**Round 1 bracket: [5.5, 7.5].**

**Round 2 — Narrowing:**
- Anchors in (5.5, 7.0): SteeringSafety (6.0, Reject), COLD-Steer (6.0, Accept Poster), Activation Steering with Feedback Controller (6.0, Accept Poster), Discern Truth from Falsehood (6.0, Accept Poster).
- Anchors in (6.0, 8.0): AlphaSteer (7.0, Accept Poster), Narrow Finetuning (7.5, Accept Poster), Watch Your Steps (6.5, Accept Oral), Persona Features (7.5, Accept Poster).

**Comparison to key anchors:**
- **SteeringSafety (6.0, Reject):** Has a mixed review profile (scores 8,6,8,2). The current paper has a clearer contribution, broader model coverage, and a more striking empirical finding. **Current paper is stronger.**
- **Watch Your Steps (6.5, Accept Oral):** Similar type of empirical safety study with a novel attack. Current paper is of comparable quality — both have clear findings and broad experiments, with some limitations. **Comparable.**
- **AlphaSteer (7.0, Accept Poster):** Proposes a method with theoretical grounding; was well-received (scores 8,4,8,8). The current paper is an empirical study rather than a method paper, but its finding is important and well-supported. **Current paper is slightly weaker due to the SAE limitation and lack of mechanistic depth.**
- **Narrow Finetuning (7.5, Accept Poster):** Broader experimental scope (33 organisms), very well-received (scores 8,8,6,8). **Current paper is weaker — less experimental breadth and a more significant evidential gap in the SAE findings.**

**Final score: 6.5.** The paper sits above SteeringSafety (6.0) and at parity with Watch Your Steps (6.5), but below AlphaSteer (7.0) and Narrow Finetuning (7.5). The core finding is important and well-supported, but the single-SAE limitation and unanalyzed model-dependence of the universal attack prevent a higher score.

### Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>