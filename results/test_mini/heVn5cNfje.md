Now I have enough context. Let me construct the final review.

**Round 1 bracket**: Based on the band-1 (avg 1.6–3.33), band-2 (avg 4.0–6.0), and band-3 (avg 8.0) anchors, this paper clearly sits in band 2 — it has substantive experiments and a novel idea, but not the theoretical depth or extreme rigor of the 8.0 papers.

**Round 2 narrowing**: Reading the band-2 anchors in full:
- "Not All Code Helps" (5.00, Reject) — rigorous large-scale ablations but rejected partly for narrow architecture scope and no error bars.
- "MathFimer" (6.00, Accept) — novel FIM-based step expansion, extensive experiments, but scope limited to math.
- "EntropyLong" (5.50, Accept) — entropy-based data construction for long-context, controversial (scores 6,4,10,2) but accepted.
- "How to train data-efficient LLMs" (6.80, Accept) — massive 220 pre-training runs, very strong empirical basis.

The HES paper is closest to EntropyLong (5.50) in terms of novelty-level, experimental breadth, and the nature of its weaknesses. It is stronger than "Rethinking Data Selection" (4.00) and "Knowledge-Centric Data Selection" (4.40) — both of which had methods that barely beat random or had very narrow scope. It is somewhat weaker than "MathFimer" (6.00) in experimental rigor due to missing error bars. **Final score: 5.5**.

---

## Summary

This paper proposes HES (High-Entropy Sum), a metric that sums the entropy of only the top 0.5% highest-entropy tokens in reasoning trajectories, and uses it for data selection across SFT, RFT, and RL training paradigms. The core idea — that the cumulative intensity of critical "forking" tokens captures reasoning complexity better than average-based measures — is well-motivated by the observation that average entropy dilutes signal from the few truly uncertain tokens in long CoTs. Experiments span math, code, and STEM domains across multiple model sizes (0.6B–8B), showing that training on the top 20% of HES-ranked data matches full-dataset performance, and the top 80% consistently surpasses it.

## Strengths

1. **HES separates correct from incorrect samples far more cleanly than existing metrics.** Figure 1 shows HES achieves a normalized mean gap of 0.39 (correct: 0.29, incorrect: 0.68), versus Avg Entropy's 0.01 gap. This is a concrete, empirical grounding for the metric's design.

2. **HES-based selection enables matching or surpassing full-dataset SFT performance across models and domains with less data.** The top-20% HES subset achieves 31.14% vs Full-Dataset 32.61% on Qwen3-8B (Table 1), and actually *exceeds* full-dataset on DeepSeek-R1-Distilled-7B (34.61% vs 30.22%, Table 2). This pattern replicates on Code (Table 3: 39.54% vs 36.28%) and STEM (Table 4: 49.56% vs 44.42%) domains, demonstrating consistent transferability.

3. **Small-to-large model transfer works with negligible performance loss.** Using Qwen3-0.6B to select data for Qwen3-8B achieves 32.12% average, nearly matching the 8B self-selection baseline (31.14%), while reducing inference costs by an order of magnitude (Table 1). This supports the claim that HES captures intrinsic dataset-level properties rather than model-specific artifacts.

4. **Unified framework across three training paradigms.** The paper validates HES in SFT, RFT, and RL — a scope that few data-selection papers attempt. The consistent pattern that high-HES samples are informative across all three paradigms is a genuine contribution.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or multiple-run reporting.** Every result in the paper is a single point estimate with no confidence intervals, standard deviations, or indication of how many seeds were used. This is especially problematic for the headline result that HES-80% beats Full-Dataset (35.36% vs 32.61% in Table 1) — a 2.75-point gain that could fall within the noise of a single random draw. Subsampling 20% or 80% of a dataset is a stochastic process, and the paper provides no evidence that the observed advantages are significant. This weakness cuts across all three experimental sections and limits the strength of the evidence. *[Verified: grep for "seed", "variance", "standard deviation", "multiple" returns no matches in the paper.]*

### Minor

2. **Unexplained performance heterogeneity on GPQA.** In RFT Global Pool (k=2, Table 5), Random achieves 58.35% on GPQA while Highest-HES gets 42.30% — a 16-point gap. This 58.35 value is anomalous compared to all other GPQA values in the table (typically 30–42), and the paper never discusses it. Similarly in RL (Table 6), HES underperforms Full-Batch on GPQA (35.54 vs 36.71). These heterogeneities suggest HES may not be universally beneficial across all benchmark types, and the paper would be stronger by acknowledging and discussing these patterns.

3. **The "reward signal" framing overreaches relative to the evidence.** The paper states "[HES] can serve as an effective, training-free reward signal" and claims to "obviate the need for costly external reward models." In RFT and RL, HES is used to *rank correct trajectories* after correctness filtering — it is a secondary ranking heuristic, not a replacement for a learned reward model. The paper does not compare against using an ORM or PRM for positive-sample selection, so this claim is unsupported. The contribution is still meaningful as a training-free selection heuristic, but the framing should be toned down.

4. **The logical chain from "HES separates correct from incorrect" to "among correct, highest HES is best" is not explicitly justified.** Figure 1 shows correct samples have *lower* HES than incorrect ones (0.29 vs 0.68), yet the method selects the *highest* HES among correct samples. The paper's rationale is that high-HES correct samples navigated more complex forks, but this reversal could be explained more clearly. An analysis showing that within correct solutions, HES correlates with some ground-truth measure of reasoning complexity would strengthen the argument.

### Trivial
None.

## Nice-to-Haves

- Report wall-clock time or token-level FLOPs for computing HES on a dataset of ~100k samples. The paper calls the metric "training-free" and "efficient" but provides no compute cost analysis.
- Extend RL experiments to a non-math domain (code or STEM) to support the claim of a "unified" metric across all training paradigms.
- Compare against a trained ORM/PRM for positive-sample selection in RFT or RL on at least one benchmark to ground the claim about replacing reward models.

## Removed Points

*These points were raised by reviewers but removed during merging for the reasons stated.*

1. **"Circularity between the metric and the model"** — The paper explicitly tests this through small-to-large model transfer (Table 1: 0.6B, 1.7B proxy models produce comparable results to 8B self-selection). The base-model sensitivity is already examined. *Removed because the paper addresses this concern.*

2. **"Forking-Only baseline comparison is not apples-to-apples"** — The critic notes Forking-Only uses 100% of data while HES-80% prunes 20% of samples. The paper itself acknowledges these are different approaches (one is a training method, the other a selection method), so this is not a weakness of the paper. *Removed.*

3. **Strength Finder strength #3 ("In RL, pairing highest-HES positive with random negatives outperforms full-batch")** — While factually correct (21.30% vs 20.63%), the gain is small and unaccompanied by error bars. This strength is kept but its significance is caveated in the evaluation.

## Novel Insights

The strongest insight from these reviews is that the paper's experimental breadth (SFT + RFT + RL, three domains, multiple model sizes) serves as a partial mitigant for the missing error bars — the same qualitative pattern (high-HES > random > low-HES) replicates across so many independent settings that it is unlikely to be purely noise. However, this does not excuse the absence of explicit variance reporting, and the paper's most impressive claim (HES-80% beats full-dataset) would significantly benefit from multiple-seed verification.

## Suggestions

1. **Add multiple seeds (3–5) with standard deviations** for the key comparisons: HES-20% vs Random-20%, HES-80% vs Full-Dataset, and the RL Pos-High Neg-Rand vs Full-Batch. This single change would address the most substantive weakness.
2. **Discuss the GPQA performance degradation** in RFT and RL with a hypothesis (e.g., GPQA is knowledge-heavy rather than reasoning-heavy, so high-entropy tokens may not correspond to reasoning forks).
3. **Tone down the "reward signal" framing** to "training-free selection heuristic" unless a comparison against a trained reward model is added.
4. **Add a brief justification or small analysis** for why, among correct samples, those with higher HES are more informative for training.

## Score and Decision

**Calibration anchors across all rounds:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 9qA5cpZmJh (Entropy Proxy for Memorization) | 2.00 | R1 | Clearly weaker — narrower scope, no actionable training method |
| C8yjlrx4Wo (SemanticDPP) | 3.33 | R1 | Weaker — uncertainty quantification for hallucination, not data selection |
| Q6OIA4KIGT (TRUST scores) | 2.00 | R1 | Weaker — position paper/uncertainty, no training results |
| QI9fRzGs6b (Tokens to Meaning) | 1.60 | R1 | Weaker — position paper only |
| g1DiK2Yi4j (Rethinking Data Selection) | 4.00 | R1 | Weaker — method doesn't beat random, narrow scope (MCQA only) |
| 7ZRF2ZkJpt (Knowledge-Centric Data Selection) | 4.40 | R1 | Weaker — requires external LLM for concept extraction, limited experiments |
| SFXX5Pjl5K (EntropyLong) | 5.50 | R1/R2 | Comparable — similar novelty level and weakness profile (accepted) |
| 11kPIEkj75 (Quantum Tensor UQ) | 6.00 | R1 | Different topic (hallucination detection) |
| fVz0UaZcrE (Not All Code Helps) | 5.00 | R2 | Slightly stronger empirical rigor but rejected for narrow scope |
| 14i2wzPPfn (MathFimer) | 6.00 | R2 | Stronger — more thorough experiments with no error-bar concerns |
| LIv0bfJZIi (On Code-Induced Reasoning) | 5.50 | R2 | Comparable — similar score and evaluation profile |
| yKUbw7q1IA (How to train data-efficient LLMs) | 6.80 | R2 | Stronger — 220 pre-training runs, very robust evidence |
| uYK6GPVg1O (Estimating Semantic Alphabet Size) | 5.50 | R2 | Different topic (UQ) but similar score tier |
| zPvdG1Va5Q (MathNet) | 5.00 | R2 | Different topic (benchmark creation) |

**Round 1 bracket**: 4.0–6.5 (clearly above band-1, clearly below band-3). **Round 2 narrowing**: The paper is closest in character and quality to EntropyLong (5.50) and stronger than the rejected papers at 4.0–5.0. Positioned relative to these anchors, 5.5 is the best fit — the core idea is novel and validated across an unusually broad scope, but the lack of variance reporting prevents it from being a stronger paper in the 6+ range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>