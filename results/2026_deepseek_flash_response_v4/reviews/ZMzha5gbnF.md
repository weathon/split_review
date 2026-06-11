## Summary

This paper identifies and characterizes the "priming vulnerability" in Masked Diffusion Language Models (MDLMs): if an affirmative token appears at an intermediate denoising step, it can steer the model toward a harmful response even in safety-aligned models. The authors propose Recovery Alignment (RA), which trains models to generate safe responses from intentionally contaminated intermediate states. Experiments across three MDLMs, multiple attack types (anchoring, First-Step GCG, PAD, DiJA, conversational jailbreaks), and three evaluators show that RA substantially reduces attack success rates while preserving general capability across 11 benchmarks.

## Strengths

1. **Theoretically grounded surrogate objective for optimization-based attacks (Theorem 4.1).** The paper derives a lower bound on the full-generation log-likelihood using only the first-step predictor, making GCG-style attacks tractable on MDLMs without Monte Carlo sampling. Table 1 shows First-Step GCG is ~20× faster (0.2h vs 4.3h per prompt) and achieves up to 4× higher ASR than Monte Carlo GCG. This is a concrete advance over both ARM-based GCG and prior MDLM attack work that relied on heuristic interventions.

2. **RA achieves substantially lower ASR than all baselines across all three MDLMs and multiple intervention steps.** At t_inter=4, RA achieves ASR of 1.3% on LLaDA Instruct while the original model scores 44.0%, SFT 42.7%, DPO 20.0%, and MOSA 24.0%. The ablation RA w/o inter (same RLHF but trained only from fully masked sequences) yields 22.0% ASR at the same setting, directly confirming that training on contaminated intermediate states — not RLHF alone — drives the improvement. No prior MDLM alignment method shows comparable results.

3. **General capability is preserved across 11 diverse benchmarks (Table 4).** Average scores for LLaDA move from 52.2% (original) to 52.6% (RA), and for LLaDA 1.5 from 52.7% to 52.8%. This is more extensive utility evaluation than comparable MDLM safety work provides. The fact that RA *improves* TruthfulQA (+5.8 points on LLaDA) while holding other tasks essentially flat is a meaningful result.

4. **Broad evaluation scope.** The paper evaluates across 3 models spanning different MDLM families (LLaDA, LLaDA 1.5, MMaDA), 4 priming-specific attacks, 3 conversational jailbreak attacks, and 3 evaluators (GPT-4o, LLaMA Guard 3, keyword matching). This breadth substantially exceeds concurrent MDLM safety work (PAD, DiJA, MOSA). The inclusion of both intervention-based and optimization-based threat models strengthens the central claim.

5. **Ablation study (Figure 3b) isolates why RA works.** Linear scheduling of t_inter outperforms both constant and uniform scheduling, confirming that a curriculum from easy to hard contaminated states is critical. Constant scheduling fails because it either never exposes the model to hard states or makes learning impossible. This gives mechanistic insight beyond "ours is better."

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The monotonicity assumption in Theorem 4.1 receives only a plausibility argument in the main text, with full justification deferred to the appendix.** The assumption (log π_θ(r̂_{t+1}=r | q, r_t) ≥ log π_θ(r̂_1=r | q, r_0) for all t) underpins the First-Step GCG lower bound and thus the entire non-intervention threat model. While the paper sketches a rationale ("unmasked tokens are unchanged... probability mass concentrates") and claims empirical support in Appendix C.2, the main text should at least summarize what the empirical validation showed — e.g., what fraction of steps satisfied the assumption, across which models. Currently the main-text reader cannot assess how well-grounded the lynchpin result is.

2. **The reward model (DeBERTaV3) is used without analysis of its accuracy or blind spots.** RA's effectiveness is bounded by the reward model's ability to correctly judge safety and usefulness across diverse responses, including those arising from contaminated intermediate states. The paper does not analyze the reward model's calibration, coverage, or failure modes. While using an off-the-shelf reward model is standard practice, discussing its known limitations would help practitioners anticipate where RA might break down.

3. **The choice of GRPO over alternatives (PPO, REINFORCE) is not motivated.** The paper states that GRPO is used for optimization but provides no rationale. A brief justification would help readers assess the design choices and understand whether a specific property of GRPO (e.g., no value function) is important for RA.

4. **General capability results (Table 4) are reported without error bars or significance tests.** Some fluctuations are notable (PIQA dropping from 74.4 to 71.6 for LLaDA, HumanEval dropping from 22.0 to 17.1). Without confidence intervals, it is difficult to assess whether these changes represent meaningful degradation or noise. Given that the paper reports standard deviations for ASR, the same practice should extend to utility benchmarks.

5. **The regime where RA's protection degrades could be characterized more precisely.** At t_inter=32, RA's ASR reaches 50.7% (LLaDA), 43.0% (LLaDA 1.5), and 79.3% (MMaDA). The paper honestly acknowledges this limitation but does not quantify the contamination level (e.g., number of affirmative tokens or proportion of unmasked tokens from the harmful response) at which protection meaningfully collapses. A more precise characterization would give practitioners a concrete sense of when RA is sufficient and when additional measures are needed.

### Trivial

1. **Algorithm 1 contains a likely typo:** line 5 uses `r_{t_min}` (a constant) where it should use `r_{t_inter}` (the scheduled intervention step computed on line 2). The comment on line 6 also says "Denoise from t_inter" but uses `r_{t_min}`.

## Nice-to-Haves

- Error bars or confidence intervals for the general capability benchmarks in Table 4.
- A brief analysis of the reward model's known capabilities and limitations in the context of RA.
- Wall-clock training time or GPU hours for RA, which is practically relevant for adoption.
- A short summary in the main text of the empirical validation of the monotonicity assumption (what the appendix shows).

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses after verification against the paper:

- **"No Attack ASR tells an ambiguous story for MMaDA"** — Removed. The paper is transparent about MMaDA being an unaligned model (labeled as such in Figure 2). It does not claim MMaDA was safety-aligned; including it alongside aligned models is standard practice for showing generalizability. The paper reports the numbers clearly.

- **"First-Step GCG may be doing more than just exploiting the priming vulnerability"** — Removed. The paper does not claim that First-Step GCG *only* exploits the priming vulnerability. The lower bound is derived by leveraging the vulnerability property, and the resulting optimization-based attack naturally involves additional prompt-optimization effects beyond the vulnerability. This is an insightful observation but not a paper weakness.

- **"Method fails under heavy contamination"** — Removed as already addressed. The paper explicitly acknowledges this limitation: "when the intervention step is very late, such as t_min = 32, generating a fully safe response becomes challenging. This is because it is practically impossible to generate a contextually safe response due to many anchors."

## Novel Insights

The harsh critic's observation about the gap between First-Step GCG's ASR (58%) and the anchoring attack at step 1 (21%) is genuinely interesting and not fully explained by the paper. First-Step GCG appears to do more than exploit the priming vulnerability as isolated by the anchoring attack — the prompt optimization likely also makes the harmful response generally more likely through mechanisms beyond affirmative-token implantation. Disentangling these effects (e.g., by checking whether First-Step GCG suffixes actually produce affirmative tokens at intermediate steps) would sharpen the causal claim. This is a concrete direction the authors could explore in future work.

## Suggestions

1. Add a brief summary of the empirical validation of the monotonicity assumption (Theorem 4.1) to the main text — e.g., what fraction of steps satisfied it across which models.
2. Include a brief discussion of the reward model's known capabilities and limitations.
3. Add error bars to Table 4 or explicitly note that results are single-run without variance.
4. Fix the pseudocode typo in Algorithm 1 (line 5: t_min → t_inter).
5. Provide a brief rationale for choosing GRPO over alternatives.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| BeOEmnmyFu.md (language game jailbreaking) | 2.50 | R1 | Much weaker — pure attack paper with thin evaluation |
| 5kMwiMnUip.md (CoT jailbreaking) | 1.40 | R1 | Much weaker — simple attack catalog |
| KyKTjRtyNG.md (multi-round jailbreaking) | 3.00 | R1 | Much weaker — attack paper |
| lUyYX9VFgA.md (code-of-thought) | 3.00 | R1 | Much weaker — pure attack |
| u08UxVNdIo.md (DiffusionAttacker) | 4.75 | R1 | Weaker — attack-only, questionable design |
| plmBsXHxgR.md (Jailbreak in Pieces) | 6.25 | R1 | Weaker — attack-only, mixed reviews |
| 8Rov0fjpOL.md (Breach By A Thousand Leaks) | 5.80 | R2 | Weaker — narrower evaluation framework |
| hXA8wqRdyV.md (Simple Adaptive Attacks) | 6.14 | R2 | Weaker — attack-only, less principled method |
| r42tSSCHPh.md (Catastrophic Jailbreak via Exploiting Generation) | 7.00 | R2 | Comparable — identifies vulnerability + proposes defense, but our paper has stronger theoretical grounding and broader utility evaluation |
| xP1radUi32.md (Endless Jailbreaks with Bijection Learning) | 6.25 | R2 | Weaker — pure attack paper |
| vESNKdEMGp.md (Multilingual Jailbreak) | 6.40 | R2 | Weaker — narrower contribution |
| Bo62NeU6VF.md (Backtracking Improves Generation Safety) | 8.00 | R1/R2 | Slightly stronger — cleaner execution, simpler story, fewer deferred details. Our paper is broader (vulnerability discovery + attack + defense) but has more minor weaknesses |
| tTPHgb0EtV.md (Booster) | 8.00 | R1/R2 | Similar tier — strong safety paper with principled method, but our evaluation is more thorough across models and benchmarks |

**Round-1 bracket:** The paper sits between the weak band (<3.5) and the strong band (>7.5). The initial bracket is (5.5, 8.0).

**Round-2 narrowing:** The paper is clearly stronger than the 5.5-7.0 anchors (Catastrophic Jailbreak at 7.00, Simple Adaptive Attacks at 6.14) — those are primarily attack papers with thinner contributions. The closest comparator is Backtracking (8.00), which is similarly structured (vulnerability + mitigation) but cleaner in execution. Our paper has more minor weaknesses (deferred justification, reward model not analyzed, no utility error bars) that pull it slightly below 8.0, but its broader scope (vulnerability discovery + theoretical attack + defense + 11-benchmark utility eval) keeps it well above the 6-7 range. 

**Final score: 7.5**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>