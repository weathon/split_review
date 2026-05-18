Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes integrating a Process Reward Model (PRM) into reinforcement learning from unit-test feedback for code generation. The PRM provides dense, line-level correctness signals to overcome the sparsity of binary pass/fail unit-test rewards. The authors introduce an automated binary-search labeling procedure to generate PRM training data (without human annotation) and explore three strategies for using the PRM in RL: as dense rewards only, as value initialization only, and their combination. On LiveCodeBench, the combined approach improves Pass@1 from 28.2% (RL baseline) to 29.8%; on an internal benchmark, from 31.8% to 35.8%. The paper also finds that PRM benefits are concentrated in long-horizon responses (>100 tokens) and that selecting only "Revised" responses for PRM training (where prefixes are recoverable) works best.

## Strengths

- **First systematic demonstration of PRMs in RL for code generation.** The paper is the first to show, through controlled experiments, that a learned process reward model can improve RL-based code generation beyond what sparse unit-test rewards alone achieve. The combination of DenseReward + ValueInit yields a 5.7% relative improvement on LiveCodeBench and 12.6% on InHouseBench over the RL baseline (Table 1).

- **Automated binary-search labeling for process supervision data (Algorithm 1).** The method efficiently labels partial code prefixes by completing them with K=20 rollouts and checking unit tests, avoiding costly human annotation. This is a practical contribution that makes PRM training scalable.

- **Systematic ablation of integration strategies.** Table 1 compares three strategies (DenseReward only, ValueInit only, both) and shows that the combination is necessary for the best results — ValueInit alone is ineffective (28.2% vs. baseline 28.2%), while DenseReward alone gives a smaller gain (28.9%). This provides clear practical guidance.

- **Identification of data quality over quantity for PRM training.** Table 2 shows that selecting only "Revised" responses (where a prefix was fixable by the policy) substantially outperforms using all data (29.8% vs. 26.9% on LiveCodeBench). The result that more data hurts is counter-intuitive and valuable for practitioners.

- **Analysis of PRM's benefit for long-horizon code generation.** Figure 4 shows that PRM-trained models consistently outperform the baseline for responses longer than 100 tokens, while short responses see negligible improvement. This aligns with the intuition that dense rewards help most on complex tasks.

## Weaknesses

### Fatal

None.

### Major

1. **Missing statistical significance and variance reporting.** The paper states results are averaged over 10 independent runs (Table 1 caption) but reports no variance, confidence intervals, or significance tests. For a 1.6-point absolute gain on LiveCodeBench (28.2% → 29.8%), the reader cannot assess whether this improvement is statistically robust or within noise. This is a critical omission for an empirical paper whose central claim rests on comparative performance numbers.

2. **Insufficient comparison baselines.** The only RL baseline is the authors' own method *without* the PRM. No simpler intermediate-feedback alternatives are compared — for example, rewarding lines that compile, using execution-trace error location (as in RLTF, Liu+ 2023), or giving partial credit for passing some unit tests. Without these baselines, the paper cannot establish that the *PRM specifically* drives the improvement rather than *any* form of non-zero intermediate reward. This weakens the central claim that the PRM's process-level signal is the cause of the gains.

3. **No validation of PRM quality on out-of-distribution prefixes.** The PRM is trained on prefixes from four checkpoints of the baseline RL, then used to guide *new* RL runs where the policy distribution shifts. The paper does not report the PRM's accuracy, calibration, or correlation with actual recoverability on prefixes from the new policy. Without this, it is unclear whether the reward signal remains aligned during training — the PRM could degrade or be exploited in unmeasured ways. The mitigations (length normalization, neutral label) are described but not ablated individually to verify their necessity.

### Minor

4. **Binary search labeling conflates recoverability with prefix correctness.** A prefix is labeled +1 if it can be *completed* to pass unit tests (via K=20 rollouts). This means a prefix containing an actual error can still receive a positive label if the follow-on completion overrides or ignores that error. The paper labels these as "potentially correct" but does not analyze how frequently this mismatch occurs or whether it weakens the training signal. While recoverability is a reasonable proxy, the paper should characterize this gap.

5. **"Full" data hurting performance receives insufficient analysis.** Table 2 shows that using all collected PRM data achieves *worse* results on LiveCodeBench (26.9%) than the RL baseline without any PRM (28.2%), while the "Revised Only" subset works best (29.8%). This is a striking result that receives only a brief high-level explanation (Section 4.2.1). Deeper analysis of *why* adding more data hurts — e.g., what the PRM learns from Correct or Wrong responses that degrades its signal — would strengthen the paper.

6. **Key implementation details omitted.** The paper does not report the PRM's architecture or parameter count, nor quantify the computational cost of the binary-search data collection (number of forward passes, wall-clock time relative to the baseline RL run). These are practical concerns for replication and adoption.

7. **Scalability evidence is limited.** Figure 5 shows Pass@1 improving with more PRM training data, but the curve has no error bars, spans only up to 8 responses per prompt on average, and is shown for a single benchmark. The claim that performance "improves consistently" would be stronger with more data points, error bounds, and evidence that the trend continues beyond 8 responses per prompt.

### Trivial

- The long-horizon analysis uses a single threshold of 100 tokens. While reasonable, a continuous curve or multiple thresholds would be more informative and remove the sense of an arbitrary cutoff. (This is a minor presentational point.)

## Nice-to-Haves

- **Evaluate the PRM's direct predictive quality** on a held-out set: compute correlation between PRM scores and actual prefix recoverability. This would directly demonstrate the PRM is learning useful signal.
- **Compare against a simpler dense-reward baseline** that does not require training a PRM (e.g., rewarding lines if the partial program compiles). If PRM outperforms this, the contribution is clearer.
- **Ablate the two PRM hacking mitigations individually** (length normalization and neutral label) to verify both are necessary and understand their relative importance.
- **Compute Pass@k** with higher temperatures or process-level metrics (e.g., lines until first error) to give a fuller picture of the PRM's effect.

## Removed Points

These points from the reviewer inputs were identified as problematic and removed or downgraded:

1. **"First to demonstrate" vs. RLTF novelty dispute.** The paper claims to be the first to show *PRMs* (learned process reward models) benefit RL for code generation. RLTF (Liu+ 2023) provides intermediate feedback via execution-trace error location but does not train a learned PRM — the distinction is real and clearly stated. The critic acknowledges the distinction but calls it insufficient. This is a subjective novelty-calibration issue, not a factual weakness. *(Removed)*

2. **"Only Pass@1 with fixed decoding" criticism.** Pass@1 with temperature 0.2 and 10 samples is the standard evaluation protocol for code generation benchmarks (Chen+ 2021, Jain+ 2024). The paper follows established practice. *(Removed — evaluates against wrong class of expectations.)*

3. **"Would it improve GPT-4o-mini at 40.7%?"** Asking whether the method improves a much stronger baseline is scope creep; the paper is evaluated on its own model and claims. *(Removed — scope creep.)*

4. **"InHouseBench described only vaguely."** The paper provides: 245 Chinese coding problems, 2 categories (Contest: 169, NL2Alg: 76), Python and C++, no data contamination risk. This is sufficient description for an in-house benchmark. *(Removed.)*

5. **Generic strength: "this paper addressed an important problem."** The Strength Finder's claim #1 (generic "first demonstration" phrasing) is kept because it is backed by specific evidence (Table 1 numbers). Other generic formulations were dropped. *(Filtered from strengths.)*

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the binary-search labeling procedure defines prefix correctness as *recoverability* (the prefix can be completed to pass tests) rather than *intrinsic correctness* (the prefix itself is free of errors). This means the PRM is trained to predict whether the policy can fix the prefix, not whether the prefix itself is correct. Whether this distinction matters in practice is an open question that the paper neither analyzes nor defends. If recoverability is actually the right signal for RL (since the policy can always complete its own prefixes), then the labeling is well-motivated; if not, the PRM may reward sloppy intermediate code. Empirical investigation of this question would be a valuable contribution beyond what the paper currently provides.

## Suggestions

1. **Report variances (standard deviations or bootstrap CIs) for all main results.** Even adding error bars to Table 1 and Figure 5 would substantially increase reader confidence in the results.
2. **Add at least one simpler intermediate-reward baseline** — e.g., reward each line if the partial program compiles, or reward partial test passing. This directly tests the claim that the *PRM's learned signal* is what matters.
3. **Report the PRM's accuracy or correlation with prefix recoverability on held-out data**, ideally on prefixes sampled from the new RL policy to quantify distribution-shift effects.
4. **Quantify the computational cost** of the data collection procedure (total forward passes, approximate wall-clock time) so practitioners can assess the trade-off.
5. **Analyze why "Full" data hurts performance on LiveCodeBench.** Table 2 is the paper's most surprising result and deserves a dedicated analysis figure or discussion.

## Score and Decision

The paper tackles a real problem (sparse rewards in code-generation RL) with a reasonable method and systematic experiments. However, the empirical evidence has critical gaps: no variance reporting for the central result, insufficient baselines to attribute gains to the PRM specifically, and no validation of PRM quality under distribution shift. These are major but addressable weaknesses. The paper's contributions — automated labeling, systematic integration strategies, data quality insights — are genuine and practically useful. On balance, the paper has enough substance to merit publication if the authors can address the statistical rigor and baseline concerns in revision, but in its current form the evidence is weaker than it should be for the claims made.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>