Now let me compose the final consolidated review.

## Summary

This paper proposes **VeriFree**, a verifier-free reinforcement learning method for training LLMs on general reasoning tasks. The key insight is that under a unique-correct-answer assumption, the expected verifier reward for a reasoning trace equals the model's own probability of generating the correct answer given that trace, i.e., $\pi_\theta(y^*|x,z)$. This enables directly optimizing the RLVR objective without any external verifier, with the additional benefit of lower gradient variance via Rao-Blackwellization. Experiments on Qwen3 models (1.7B–8B) across MMLU-Pro, GPQA, SuperGPQA, and math benchmarks show that VeriFree matches or slightly exceeds verifier-based alternatives while being simpler, faster, and more memory-efficient.

## Strengths

1. **Principled theoretical grounding.** The derivation from the verifier-based RLVR objective (Eq. 2) to the verifier-free objective (Eq. 4) is mathematically sound under the stated unique-answer assumption. The variance reduction argument via Rao-Blackwellization (Theorem 1) is clean and well-motivated. This provides a firmer theoretical foundation than related verifier-free approaches (JEPO, LaTRO) that optimize variational lower bounds rather than recovering the exact RLVR objective.

2. **VeriFree matches or surpasses verifier-based methods on general reasoning benchmarks.** Table 1 shows Qwen3-8B-Base-VeriFree achieves 67.2% on MMLU-Pro vs. 65.9% for the verifier baseline; Table 2 shows 38.0% vs. 37.1% on SuperGPQA. These results hold across three model scales and are accompanied by consistent improvements on GPQA (Appendix E). The transfer experiment (Figure 5), where VeriFree trained without any math data still improves math performance, provides particularly compelling evidence that the method learns general reasoning.

3. **Better learning efficiency.** Figure 4 (Left) shows VeriFree consistently outperforms the verifier baseline from early training steps onward, suggesting that the continuous probability-based reward signal provides more informative gradients than the binary verifier reward.

4. **Comprehensive ablations confirm key design choices.** The tokenization-aware splitting strategy (Section 2.4) and RLOO variance reduction are each ablated in Figure 6, showing clear performance degradation when removed. The equivalence-class ablation (Figure 6 Right) provides empirical support that a single reference answer suffices.

5. **Practical benefits are well-demonstrated.** VeriFree eliminates the need to maintain and query a separate verifier model during training, reducing memory footprint and computational overhead. The method works from base models without any SFT warmup, following the "Zero" setting.

## Weaknesses

### Fatal
None.

### Major

1. **The verifier baseline comparison is confounded by fundamentally different reward formulations.** The Verifier baseline (Section 3.1) uses a composite reward: binary verifier correctness + format penalty (−0.5 for missing `\boxed{}`) + length penalty (−0.05 × min(10, |len_diff|)). VeriFree uses only the continuous probability $\pi_\theta(y^*|x,z)$ as reward, with no penalties. The paper states "all other settings are consistent" but the reward signal itself is different. Since the margins are small (1–2%), it is unclear whether VeriFree's advantage stems from the algorithm or simply from not penalizing the model for format or length violations. An ablation that runs the Verifier baseline *without* the format/length penalties (or runs VeriFree *with* matching penalties) is needed to disentangle these effects.

2. **No uncertainty estimates for main results.** Tables 1 and 2 report single numbers without standard errors, confidence intervals, or multiple seeds. Given the modest margins (47.0 vs. 46.9 for 1.7B on MMLU-Pro; 25.3 vs. 24.8 for 1.7B on SuperGPQA), it is impossible to judge whether these differences are meaningful or statistical noise. The paper should report mean±std over at least 3 seeds, or provide bootstrap confidence intervals.

### Minor

3. **Missing ablation of the reference answer term weighting.** Section 2.3 hypothesizes that weighting the reference answer term $\nabla_\theta \log \pi_\theta(y^*|x,z)$ by $\pi_\theta(y^*|x,z)$ (VeriFree) is superior to the fixed weight of 1 used by JEPO/LaTRO. However, no ablation within VeriFree's own framework tests this claim — the comparison to JEPO/LaTRO (Appendix E.2) involves additional differences (log reward, KL regularization). A simple ablation comparing "VeriFree with weight=$\pi_\theta(y^*|x,z)$" vs. "VeriFree with weight=1" (keeping everything else identical) would directly validate this stated advantage.

4. **Training hyperparameters not reported.** The paper does not specify the learning rate, optimizer, learning rate schedule, or warmup steps. These are standard reporting requirements for reproducibility in RL training.

5. **The unique-correct-answer gap between theory and practice is not characterized.** The theoretical equivalence (Eq. 4) assumes a single correct answer string. The paper acknowledges this limitation and provides an equivalence-class ablation (Figure 6 Right), but does not analyze how the objective deviates from the verifier-based one when multiple valid answers exist. A bound or characterization of this bias would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- Break down the Math-Eval-Suite in Figure 5 by individual benchmark (GSM8K, MATH-500, etc.) to show which math skills transfer.
- Report training dynamics on GPQA and SuperGPQA (similar to Figure 4 Left for MMLU-Pro) to demonstrate the efficiency advantage is not benchmark-specific.
- Briefly discuss whether the model's self-computed probability could be vulnerable to reward hacking (e.g., whether confidence grows faster than accuracy), since this is a known concern for self-referential rewards in RL.

## Removed Points

The following points were raised by reviewers but are removed or demoted per the filtering guidelines:

- *"The paper does not discuss potential reward hacking when the model optimizes a self-computed probability."* → Demoted to Nice-to-Have. The paper's empirical results (correlation between confidence and accuracy in Figure 4 Right, ρ=0.82) already partially address this concern, and a deep analysis would strengthen but is not required.
- *"The paper does not include an exact-match verifier baseline for multiple-choice questions."* → Removed. The paper's primary value is replacing verifiers entirely; the comparison to a model-based verifier is the standard setup from prior work (Ma et al., 2025). An exact-match verifier would be a toy baseline with no practical value for general reasoning.
- *"Reward hacking" concerns* → Based on the empirical evidence (stable training curves, positive accuracy-confidence correlation), this is a speculative concern not substantiated by evidence in the paper.
- *"Format penalty confound is not discussed"* → This IS retained as Major weakness #1 (the confound is real whether discussed or not).

## Novel Insights

The review process surfaces an important tension: the paper claims "all other settings are consistent" when comparing VeriFree to the verifier baseline, but the reward functions are fundamentally different in kind (continuous probability vs. binary correctness + penalties). This is not a small implementation detail — it is arguably the independent variable in the comparison. The community would benefit from a controlled study that isolates the effect of the reward *type* from the effect of the *algorithm* (VeriFree vs. RLVR). Additionally, while the Rao-Blackwellization argument is theoretically correct, its practical benefit depends on whether the variance from answer sampling ($y \sim \pi_\theta(\cdot|x,z)$) is actually a significant contributor to total gradient variance compared to reasoning trace sampling ($z \sim \pi_\theta(\cdot|x)$). An empirical variance decomposition would be a valuable follow-up.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): aONZZA0oIQ (2.00), Fuhmh86Ckv (2.50), K7DCGOzSVW (2.50) — papers about RL without verifiers that were withdrawn/rejected with significant flaws.
- Middle band (3.5–7.5): abAMONjBwb (4.50, NRT), 3jrWUqoItt (4.00, RLPIR), OU9nFEYR2M (5.50, Intuitor), jGbRWwIidy (5.33, RLVR analysis).
- Strong band (avg > 7.5): DM0Y0oL33T (8.00), 9gw03JpKK4 (8.00) — multimodal verifiers and agent benchmarks, not directly comparable.

**Round 2 — Narrowing:**
- abAMONjBwb (avg 4.50) — NRT: similar verifier-free method but with serious confounds (data regime differences, baseline reimplementation). VeriFree is clearly stronger — cleaner comparisons, wider model scales, better theoretical grounding.
- DZjbL9BuHs (avg 4.67) — RLVR generalization study: different type of paper.
- jGbRWwIidy (avg 5.33) — RLVR analysis paper: different contribution type.
- ZumVIktGbt (avg 6.50) — RLVRR: extends RLVR to open-ended generation with reference-based rewards; still uses verifiers. Stronger evaluation rigor.
- OU9nFEYR2M (avg 5.50) — Intuitor: uses self-certainty as reward, less principled theory, evaluated on math/code where verifiers exist. VeriFree is comparable in quality.

**Round 1 bracket:** [4.5, 6.5]

**Final score determination:** VeriFree is clearly stronger than NRT (4.50) and RLPIR (4.00). It is comparable to Intuitor (5.50) but with stronger theoretical grounding and evaluation in genuinely non-verifiable domains. It falls below RLVRR (6.50) due to the latter's cleaner experimental setup and absence of the confound/uncertainty issues. The paper's core contribution is solid and the weaknesses are fixable — this is a clear accept-level paper but the confounded baseline comparison and missing uncertainty estimates prevent it from being a top-tier submission.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>