Now I have enough calibration data to finalize my score. Let me write the consolidated review.

**Round 1 bracket:** The paper falls between the weak band (<3.5 — papers like "Playing Language Game with LLMs" at 2.50) and the strong band (>7.5 — papers like "Safety Alignment Should be Made More Than Just a Few Tokens Deep" at 9.50). Initial narrowest plausible range: 6–8.5.

**Round 2 narrowing:** Compared against "Backtracking Improves Generation Safety" (8.00, similar recovery-from-unsafe-states concept), "Catastrophic Jailbreak of Open-source LLMs" (7.00), "Cross-Modal Safety Mechanism Transfer" (6.50), and "Breach By A Thousand Leaks" (5.80), the current paper is clearly stronger than 5.80–7.00 anchors and comparable to the 8.00 anchor.

**Final score:** 8.0 — comparable to "Backtracking Improves Generation Safety" (8.00) and slightly below "Safety Alignment Should be Made More Than Just a Few Tokens Deep" (9.50), which had a more fundamental unifying insight and targeted the more widely-used ARM domain.

---

## Summary

This paper identifies a *priming vulnerability* in masked diffusion language models (MDLMs): affirmative tokens injected at intermediate denoising steps can steer subsequent generation toward harmful responses, even in safety-aligned models. The authors quantify the vulnerability via an anchoring attack (intervention-based) and a First-Step GCG attack (optimization-based, no intervention needed) backed by a theoretical lower bound. They then propose Recovery Alignment (RA), which trains MDLMs to generate safe responses from contaminated intermediate states. Experiments across three MDLMs, six attack methods, three baselines, and eleven general capability benchmarks show RA substantially reduces attack success rates (e.g., from 17.3% to 0.0% at step 1 on LLaDA Instruct) while maintaining utility within ±0.4 points of the original.

## Strengths

1. **Clear quantification of a previously unanalyzed vulnerability.** Figure 2 shows the anchoring attack raises ASR from 2% to 21% at step 1 on LLaDA Instruct, and exceeds 80% by step 16 across all models. This directly demonstrates the vulnerability's existence and severity in a controlled setting.

2. **Effective, principled defense (RA).** Table 2 shows RA reduces ASR to 0.0% (LLaDA Instruct) and 1.0% (LLaDA 1.5) at intervention step 1, while all baselines (SFT, DPO, MOSA) leave ASR above 5%. At step 4, RA achieves 1.3% versus 24.0% for the best baseline (MOSA). The RA w/o inter ablation confirms that training on contaminated intermediate states is the critical ingredient.

3. **Theoretical lower bound enabling efficient optimization.** Theorem 4.1 provides a tractable surrogate for the intractable GCG objective. Table 1 shows First-Step GCG achieves 4× higher ASR than Monte Carlo GCG on LLaDA-1.5 (49.5% vs 12.5%) while being 20× faster (0.2 h vs 4.1 h per prompt).

4. **Robustness generalizes to non-intervention jailbreaks.** Table 3 shows RA reduces ASR on PAIR from 44.3% to 10.0% on LLaDA Instruct, outperforming MOSA (27.3%) and DPO (31.3%). This suggests learning to recover from contaminated states transfers beyond the anchoring attack.

5. **General capability maintained across 11 benchmarks.** Table 4 shows RA changes average accuracy by less than 1% on LLaDA (52.2% → 52.6%) and LLaDA 1.5 (52.7% → 52.8%), with improvements on TruthfulQA (e.g., +5.8%). The negligible degradation on ARC-C, MMLU, and HellaSwag shows the method does not sacrifice capability for safety.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Limited mechanistic analysis of how RA achieves its effect.** The paper hypothesizes that RA teaches the model to "re-detect harmfulness at later steps" (Section 6.2, line 252: "A plausible mechanism is..."), but provides no direct evidence — e.g., output distribution comparisons at different denoising steps, attention pattern analysis, or case studies showing a model recovering from a partially harmful response. While this does not undermine RA's empirical effectiveness, it weakens the claim about *how* RA works versus merely that it works.

2. **The monotonicity assumption underlying Theorem 4.1 is validated only in the appendix.** Since First-Step GCG depends critically on this assumption, showing empirical validation for all three models in the main text would increase confidence in the attack results and, by extension, in the severity of the vulnerability.

3. **Distributional alignment between training and attack contamination remains unanalyzed.** RA trains on contaminated states from dataset responses with a specific injection procedure. While RA generalizes to PAD, DiJA, and PAIR (Table 3), the paper does not analyze *why* this transfer occurs or characterize the distribution of contamination states. A more sophisticated attack crafting partial harmful responses that deviate from the dataset responses could potentially evade RA. The paper acknowledges this implicitly (RA remains imperfect against ReNeLLM), but a deeper analysis would strengthen the claims.

### Trivial

- The paper reports MMaDA's "No Attack" ASR as 79.7% (Table 2), indicating it is already not safety-aligned. This makes MMaDA a useful testbed for RA performing alignment from scratch rather than patching an aligned model. The paper could be more explicit about this interpretation, though it is a strength, not a weakness.

## Nice-to-Haves

- **Training cost summary in main text:** The paper mentions training cost details in Appendix C.4 but does not summarize wall-clock time or computational overhead relative to standard RLHF in the main body. A brief note would help practitioners assess practicality.
- **Reward model ablation:** Using DeBERTaV3 as a fixed reward model is reasonable, but an ablation with a different reward model (e.g., an LLM-as-judge) would strengthen the claim that RA is robust to reward model choice.
- **Hyperparameter sensitivity of the linear schedule:** The paper ablates t_max but not the schedule length or duration. A brief note on sensitivity would be useful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Vulnerability framing vs inherent conditional generation behavior"** — The harsh critic raised this as a discussion point but explicitly states the paper "does not overclaim" and "the framing is valid." It is a framing observation, not a weakness.
- **"Missing related works"** — Per instructions, I cannot mention missing related works as I lack external sources to confirm their existence.
- **"Re-masking behavior clarity"** — The paper already states clearly in Section 3: "Unmasked tokens in r_t are unchanged and never re-masked in subsequent steps." This concern is addressed in the paper.
- **"Appendix/references stripped" complaints** — The parser strips these; they exist in the original submission.
- **"Typos/formatting issues"** — Parser artifacts, not author errors.
- **"Strength Finder strengths about problem importance"** — Generic strengths ("this paper addresses an important problem") are removed as they lack specific evidence.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that RA on MMaDA constitutes alignment from scratch (rather than patching) is worth highlighting but not a novel insight.

## Suggestions

1. Add a case study in the main text showing a model successfully recovering from a partially harmful intermediate state (e.g., starting with "Sure, here is how to..." and ending with "I'm sorry, I cannot"). This would directly illustrate the recovery mechanism RA instills.
2. Move the monotonicity validation (Appendix C.2) into the main text, or at least summarize it concretely (e.g., "the assumption held for >95% of prompts across all three models").
3. Include a brief note on training cost (wall-clock time, GPU-hours) in Section 6.1 to help practitioners assess practicality.
4. Add a short discussion of the distributional gap between training and attack contamination — even a qualitative description of why transfer occurs (or its limits) would strengthen the paper's characterization of RA's generalization properties.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

**Calibration details:**

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Safety Alignment Should be Made More Than Just a Few Tokens Deep | 6Mxhg9PtDE.md | 9.50 | 1 | Stronger paper with a more fundamental unifying insight (shallow alignment connects multiple attack types) and targets the more mainstream ARM domain. The current paper is more narrowly scoped (MDLMs only) and slightly less polished. |
| Backtracking Improves Generation Safety | Bo62NeU6VF.md | 8.00 | 1 | Comparable quality: both propose teaching models to recover from unsafe intermediate states, both have thorough experiments, both maintain utility. The current paper has more models/attacks/baselines and a theoretical contribution, while Backtracking has a simpler mechanism. Score parity is appropriate. |
| Interpolating Autoregressive and Discrete Denoising Diffusion Language Models | tyEyYT267x.md | 8.00 | 1 | A methods paper about diffusion LMs rather than safety. Less directly comparable; the current paper is a different type of contribution (safety discovery + defense) within the same model family. |
| Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation | r42tSSCHPh.md | 7.00 | 2 | Good paper about a simpler attack (decoding manipulation) with weaker novelty. The current paper's discovery of the priming vulnerability is deeper and more fundamental. Current paper is clearly stronger. |
| Cross-Modal Safety Mechanism Transfer in Large VLMs | 45rvZkJbuX.md | 6.50 | 2 | Safety paper with some weaknesses (limited robustness analysis, no adversarial testing). The current paper has more thorough evaluation and no structural flaws. Current paper is clearly stronger. |
| Breach By A Thousand Leaks | 8Rov0fjpOL.md | 5.80 | 2 | More niche threat model (information leakage via decomposition); weaker empirical evaluation. Current paper is clearly stronger. |
| Diffusion Attacker (LLM Jailbreak) | u08UxVNdIo.md | 4.75 | 1 | Rejected paper with inadequate baselines and questionable metrics. Current paper is significantly stronger. |
| Diffusion LMs Can Perform Many Tasks | Qn4HEhezKW.md | 5.00 | 1 | Rejected due to limited methodological contribution. Current paper is significantly stronger. |