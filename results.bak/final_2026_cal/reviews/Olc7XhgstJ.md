Now I have all the information needed. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

---

Here is my final consolidated review:

## Summary

This paper proposes **Steady Thought (ST)**, a three-stage framework that mitigates "under-thinking" (excessive, unproductive thought switching) in large reasoning models. ST first segments model responses into thought-level units using entropy-based detection, then generates committed trajectory completions via logit suppression of switch-indicating tokens, and finally applies a thought-level preference optimization objective (STPO) that teaches the model to favor committed reasoning over wasteful switching. Experiments across DeepSeek-R1-Distill-Qwen (1.5B, 14B) and Qwen3-8B on four math/coding benchmarks show accuracy improvements of up to 5.3% while reducing output length by 19–39%.

## Strengths

1. **Novel and principled formalization of under-thinking as a thought-level preference problem.** The paper formalizes under-thinking by defining commit vs. switch trajectories (Section 2.1, Equation 2) and instantiates this through STPO (Equation 7), a length-normalized objective conditioned on individual thoughts. This is more structured than global suppression methods (NOWAIT, SEAL) and the ablation in Table 4 confirms STPO clearly outperforms both SFT and DPO on the same preference pairs (e.g., MATH500: 84.4%/2809 tokens vs. DPO 82.6%/4273 tokens).

2. **Consistent and practically meaningful empirical gains across model scales and domains.** Table 1 shows ST improves accuracy while reducing length on all three model sizes and all four datasets. Notable results include +5.3% accuracy on LiveCode (Qwen3-8B, 71.8→77.1) while cutting 19% of tokens, and a 39.3% token reduction on GSM8K (Qwen3-8B, 1759→862). The OOD generalization to LiveCode (trained only on math data) is a strong indicator that the method teaches generalizable reasoning patterns rather than dataset-specific memorization.

3. **Direct evidence that ST reduces invalid switching and deepens exploration.** Table 2 shows the percentage of correct intermediate thoughts (an indicator of abandoned promising thoughts) drops after ST training (e.g., DeepSeek-R1-1.5B on MATH500: 54.90% → 40.40%). Figure 2 further shows the final thought proportion increases substantially (e.g., Qwen3-8B on LiveCode: 8.28% → 32.36%), confirming the model commits more deeply to promising reasoning paths.

## Weaknesses

### Fatal
None.

### Major
1. **Missing whole-response SimPO baseline with standard preference pairs.** The paper's central claim is that *thought-level* conditioning is responsible for the gains. However, the ablation in Table 4 only compares variants within the ST pipeline (SFT, DPO, STPO using the same thought-segmented pairs). A natural and informative baseline would be to apply SimPO (or another preference method) on standard correct/incorrect full responses (without thought segmentation or logit suppression). Without this, it is difficult to fully isolate whether the gains come from the thought-level design, from the length normalization in STPO, or simply from having any preference training on the specific data distribution. The DPO baseline partially addresses this, but a SimPO-on-full-responses comparison would cleanly separate the effect of thought-level conditioning from the effect of length normalization.

### Minor

1. **No statistical significance or variance reporting for most results.** Table 1 reports point estimates without confidence intervals, standard deviations, or error bars. The paper states that AIME 2024 is averaged over 8 runs and LiveCode over 2 runs, but for MATH500 and GSM8K it is unclear whether multiple runs were performed. Given that some accuracy gains are modest (e.g., 82.0→84.4 for 1.5B on MATH500, +2.4%), it is difficult to assess whether these improvements are statistically robust. The consistency of the positive results across models and datasets partially mitigates this concern, but adding standard deviations or confidence intervals for at least the main results would meaningfully strengthen the evidence.

2. **The logit-suppression heuristic for generating chosen completions is not fully validated.** The thought-completion stage generates "committed" trajectories by suppressing trigger words ("wait", "alternatively"). This is a reasonable heuristic, but the paper does not analyze what fraction of actual thought switches involve these tokens, nor does it ablate the suppression mechanism (e.g., allowing free generation and retroactively identifying committed completions). The SFT ablation (Table 4) shows that training on these completions alone hurts performance, which rules out simple memorization, but the method's sensitivity to the completeness of the trigger-word set is worth examining.

### Trivial

1. **Entropy thresholds for the 8B and 14B models are deferred to the appendix.** The main text reports threshold tuning only for the 1.5B model (Table 3, optimal threshold 3.0) and states that results for other models are in Appendix D (which is removed by the parser). Readers of the main paper cannot verify whether the same threshold generalizes across model sizes.

## Nice-to-Haves

- A dedicated limitations discussion acknowledging scenarios where ST might impair performance (e.g., problems where multiple thought switches are genuinely necessary because no single initial thought is sufficient).
- An ablation removing the logit-suppression heuristic: allow the model to generate completions freely, then *retroactively* identify which thought prefix leads to the correct answer, and use that as the chosen trajectory.

## Removed Points

These points were raised by the critics but are removed after verification against the paper:

- **"Unfair baseline comparison for training-based methods"** (original framing): The critic claimed the paper only compares against test-time methods. In fact, Table 4 provides a within-pipeline comparison (SFT, DPO, STPO). The DPO baseline *is* a whole-response preference optimization baseline, partially addressing this concern. The valid residual concern (missing whole-response SimPO with standard pairs) is retained as a Major weakness above, but the broader claim of no training baselines is incorrect.
- **"Entropy threshold tuning is opaque across models"** (original framing as a major concern): The paper explicitly states that threshold tuning results for other models are in Appendix D. Since the parser strips appendices, this is not an omission by the authors. The residual concern about main-text transparency is retained as Trivial.
- **All suggestions from "Strengthening the Paper on Its Own Terms"**: These are constructive suggestions for additional experiments, not weaknesses. They are moved to Nice-to-Haves where they are appropriate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add a whole-response SimPO baseline** trained on standard correct/incorrect full responses (without thought-level conditioning or logit suppression). This would directly quantify the value of the thought-level conditioning mechanism vs. simply applying length-normalized preference optimization to the original model outputs.
- **Report standard deviations or confidence intervals** for the main accuracy results (Table 1), even if only for one or two datasets.
- **Include a brief analysis** of how many actual thought switches involve the chosen trigger words ("wait", "alternatively") to validate the completeness of the suppression heuristic.
- **State the entropy thresholds used for the 8B and 14B models** in the main text.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing (three queries):**
- Query A (score < 3.5): Papers on under-thinking / preference optimization for reasoning — avg scores 2.5–3.0. These are weaker, typically rejected papers.
- Query B (score 3.5–7.5): Papers on thought-level preference optimization and reasoning efficiency — avg scores 4.5–6.0. Accepted posters.
- Query C (score > 7.5): Strong papers on diverse LLM topics — avg scores 8.0. Oral/poster papers with very thorough evaluation but different topics.

**Initial bracket:** 5.0–6.5

**Anchors inspected in full (Round 2):**
- *Pruning Long Chain-of-Thought...* (avg 5.0, Poster): Similar preference-based length reduction method. LCPO has stronger baseline comparisons but less novel framing. This paper is somewhat stronger.
- *The First Impression Problem* (avg 5.5, Poster): Analysis of overthinking via internal bias. Stronger causal analysis but no training-based solution. Comparable to this paper.
- *When More is Less* (avg 6.0, Poster): Comprehensive understanding of optimal CoT length with theory and experiments. More thorough evaluation. This paper is slightly weaker.
- *OptimalThinkingBench* (avg 5.33, Poster): Benchmark for over/under-thinking. Less methodological contribution. This paper is stronger.
- *Explore Briefly, Then Decide* (avg 5.0, Reject): Entropy-based overthinking mitigation. Weaker evaluation, rejected. This paper is clearly stronger.

**Final position:** Placing this paper at **5.5**. It offers a more novel methodological contribution than the 5.0 anchors (LCPO, CER) and comparable value to the 5.5 anchor (First Impression), but the missing whole-response SimPO baseline and lack of statistical significance reporting prevent it from matching the 6.0 anchor (When More is Less) in evaluation rigor.

**Score:** 5.5  
**Decision:** Accept (Poster)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>