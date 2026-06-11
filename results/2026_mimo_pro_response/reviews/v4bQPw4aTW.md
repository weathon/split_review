Now I have all the calibration data I need. Let me write the final review.

## Summary
This paper proposes AdaBoN, a two-stage adaptive Best-of-N allocation strategy that distributes inference-time compute across a batch of prompts. The method uses KDE-based reward distribution estimation in an exploration phase, then greedily allocates remaining samples based on estimated marginal gains (grounded by Proposition 3.1's optimality guarantee). It is evaluated across 12 LM-RM pairs, 3 datasets, and 50 batches per pair using two novel metrics (BWR and EST).

## Strengths
- **Entirely test-time with no auxiliary model training**, making it far more practical than the closest prior work (Damani et al., 2024), which requires training a separate MLP per LM-RM pair per budget value — 216,000 MLPs for the paper's setup (line 188). AdaBoN works out-of-the-box for any LM-RM combination (lines 52, 100–101).
- **Proposition 3.1 provides a theoretical guarantee** that the greedy allocation is optimal for the estimated marginal gains (line 108), connecting the practical algorithm to well-known resource allocation theory (Federgruen and Groenevelt, 1986).
- **Broad empirical evaluation**: 12 LM-RM pairs, 3 datasets, 50 batches per pair, and ablations over K ∈ {3,5,10,15,20} and B ∈ {80,100,120,140,160} — substantially more comprehensive than Damani et al. (2024) who tested a single LM, single RM, and single batch (line 56).
- **Consistent outperformance**: AdaBoN beats uniform allocation on >75% of batches across all 12 LM-RM pairs (Table 2b), with median BWRs of 0.54–0.62 (Table 1) and median ESTs of ~150, competitive with 20% larger uniform budgets (Table 2a). Some batches reach BWRs as high as 0.70 and ESTs ≥ 160.
- **Well-motivated novel evaluation metrics**: BWR uses win-rate comparison because RM scalar values are only meaningful comparatively (Bradley-Terry training, lines 170–172), and EST quantifies computational savings by measuring how large a uniform budget AdaBoN can match.
- **Minimal hyperparameter tuning**: single hyperparameter d=0.75B works well across all experiments (line 242), with Table 3 (Appendix G.1) showing minimal drop vs. per-pair optimal d.
- **Latency-aware two-stage design**: only two calls to the base LM needed, fully parallelizable (lines 136–146), directly addressing a practical engineering concern.

## Weaknesses

### Fatal
None.

### Major
- **Only comparison baseline is uniform allocation** — The entire evaluation (Tables 1–2, Figures 2–3) compares AdaBoN against uniform allocation only. While uniform is the standard practice and the minimax-optimal non-adaptive baseline, it is the weakest possible comparison for any adaptive method. The paper's core contribution is its specific design (KDE estimation + greedy marginal gain allocation), but without simple adaptive heuristics — e.g., allocating remaining budget proportionally to estimated variance, or based on observed exploration maximums — readers cannot determine whether AdaBoN's specific design choices matter or whether *any* reasonable adaptive strategy would beat uniform. Given the modest margins (median BWRs of 0.54–0.63), this distinction is especially consequential: with stronger baselines, these margins might shrink or disappear. The paper acknowledges not comparing with Damani et al. (2024) due to implementation difficulty (line 188), which is understandable, but trivially simple adaptive baselines should be included to establish the value of AdaBoN's specific design.

### Minor
- **Exploration budget ablation range is narrow** — The default d=0.75B means 75% of per-prompt compute is spent identically to uniform allocation, with only 25% adaptively allocated. The ablation in Appendix G.1 tests only d ∈ {0.60B, 0.70B, 0.75B, 0.80B} (line 242). Testing a wider range (e.g., 0.3B–0.9B) would illuminate the tradeoff between estimation quality and adaptive capacity, which is central to understanding the method. Notably, the motivating example in Section 2.3 uses d/B = 40% (d=10, B=25), a much lower exploration ratio than the 75% used in experiments, creating a disconnect between the theoretical motivation and the practical configuration.
- **HH-RLHF and PKU-SafeRLHF results entirely deferred to appendix** — The paper claims "similar performance across all of them" (line 158) but all main-text results are for AlpacaEval only. Including even one summary table from an additional dataset would substantiate the cross-dataset claim without requiring readers to consult the appendix.
- **No formal statistical significance tests** — Results report medians and IQRs across 50 batches but no significance tests. For weaker LM-RM pairs where median BWRs approach 0.50 (e.g., Qwen-Armo at 0.54), knowing whether the win rate is significantly above chance would strengthen the evidence.

### Trivial
None.

## Nice-to-Haves
- Wall-clock timing comparison between AdaBoN and uniform to quantify practical overhead of the estimation and allocation step.
- Sensitivity analysis for the Monte Carlo sample size m=1024 used to estimate V_{i,j}.
- More explicit analysis of when AdaBoN provides the most benefit — Figure 3 shows improving performance with K, suggesting the method benefits from diversity in prompt difficulty, but this isn't analyzed directly.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Reward distribution smoothness based on visual inspection** — The critic flagged this as "informal," but the paper also validates KDE empirically against Gaussian and Skew-Normal MLE in Appendix K.3 (Table 16), which shows KDE performs best. Visual inspection is a reasonable motivating observation.
- **EST sensitivity to 2B cap** — The paper is transparent about this cap (line 215) and it's a standard practical choice.
- **Qwen-Armo failure mode in appendix** — The paper mentions this in the main text (line 217) and explains the cause (left-skewed distributions).
- **Formatting/style nitpicks** — parser artifacts, not author errors.

## Novel Insights
The paper's key novel insight is that reward distributions in Best-of-N alignment are smooth and easy to estimate via simple KDE, enabling a practical two-stage adaptive allocation that requires no auxiliary model training. This observation — combined with the theoretical guarantee from Proposition 3.1 that greedy allocation is optimal for the estimated marginal gains — provides a clean, principled foundation for adaptive Best-of-N that significantly lowers the barrier to adoption compared to prior work requiring auxiliary model training (Damani et al., 2024). The breadth of the empirical evaluation (12 LM-RM pairs, 3 datasets) also provides a substantial contribution to understanding how adaptive Best-of-N behaves across diverse configurations.

## Suggestions
- **Add 2–3 simple adaptive baselines** (e.g., variance-proportional allocation, max-reward-based allocation, random reallocation of remaining budget) to demonstrate that AdaBoN's specific design matters beyond just "any adaptivity helps." This is the single most impactful improvement.
- **Expand the exploration budget ablation** to a wider range (e.g., d ∈ {0.3B, 0.4B, 0.5B, 0.6B, 0.7B, 0.75B, 0.8B, 0.9B}) and include it in the main text.
- **Include at least one summary result** from HH-RLHF or PKU-SafeRLHF in the main text.
- **Add a simple statistical significance test** (e.g., Wilcoxon signed-rank) for the BWR results, especially for weaker LM-RM pairs.

## Reporting — Calibration Anchors

| Anchor Paper | Avg Human Score | Round | Comparison |
|---|---|---|---|
| Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | 5.00 | 1 | Empirical scaling analysis; Reject. AdaBroader evaluation and cleaner method. |
| Rational Metareasoning for Large Language Models | 5.00 | 1 | Test-time compute efficiency; Reject. AdaBoN has broader evaluation and cleaner contribution. |
| Test-Time Alignment via Hypothesis Reweighting | 5.33 | 1 | Test-time alignment; Reject. AdaBoN has much broader evaluation. |
| LASeR: Learning to Adaptively Select Reward Models | 5.25 | 1 | Adaptive RM selection; Reject. Both have weak baseline concerns, but AdaBoN has cleaner method. |
| Inferring from Logits: Best Practices for Decoding-Free Selection | 3.00 | 1 | Decoding efficiency; Reject. AdaBoN is clearly more substantial. |
| Polybasic Speculative Decoding | 3.00 | 1 | Inference efficiency; Reject. AdaBoN is clearly better. |
| Inference-Aware Fine-Tuning for Best-of-N | 5.67 | 1, 2 | Best-of-N improvement; Accept. AdaBoN has broader eval but is more incremental. |
| Inference Scaling Laws | 5.75 | 1, 2 | Compute-optimal inference; Accept. Comparable breadth of evaluation. |
| CARDS: Cascade Reward Sampling | 5.75 | 2 | Decoding-time alignment; Reject. AdaBoN has much broader evaluation (3 datasets vs 1). |
| Learning How Hard to Think (Damani et al.) | 6.50 | 1, 2 | Closest prior work; Accept. More novel approach (learned difficulty model) but narrower evaluation. AdaBoN is simpler/more practical. |

**Round 1 bracket:** 5.0–6.5 (above 5.0–5.33 rejects, below 6.5 Damani et al.)

**Round 2 narrowing:** 5.0–6.0 (below Damani et al. which is more novel, above 5.0–5.33 rejects given AdaBoN's broader evaluation and cleaner method, comparable to 5.67–5.75 range but with a different weakness profile — broader eval but weaker baselines)

**Final score: 5.5** — AdaBoN is a solid, well-executed practical contribution with the broadest evaluation in its subfield. The single-baseline comparison is a genuine weakness that prevents the paper from establishing the specific value of its design choices, and the improvements are consistent but modest. Adding simple adaptive baselines would likely elevate this to a clear accept. The paper sits at the borderline — strong practical merit with a key evaluative gap.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>