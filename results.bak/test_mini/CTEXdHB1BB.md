## Summary

The paper introduces CANON (Conditional Advantage Estimation), a reinforcement learning framework for large reasoning models that regroups sampled responses based on a target metric (e.g., entropy or response length) and computes inter-group and intra-group advantages to amplify the metric's influence without presupposing its beneficial direction. The core idea is that by separating responses into two groups based on a metric (e.g., high vs. low entropy) and comparing across groups, the method can identify which metric trend yields higher accuracy without imposing a directional bias. Experiments on Qwen2.5-Math (1.5B, 7B) and Llama3.1-8B across six math benchmarks and a high-complexity logic reasoning benchmark (ZebraLogic) show consistent improvements over DR.GRPO. CANON-Eff, the efficiency variant applied to response length, establishes a new Pareto frontier in the performance–token cost trade-off.

## Strengths

- **Novel and principled advantage estimation method**: CANON's regrouping idea is well-motivated and clean. By splitting responses into equal-sized groups based on a metric and computing inter-group vs. intra-group advantages, the method naturally distinguishes which metric trend correlates with higher reward — without requiring handcrafted directional penalties. The fact that DR.GRPO emerges as the special case μ=0.5 (Eq. 7) is a nice theoretical connection.
- **Theoretical support for selective amplification**: Theorem 1 shows that inter-group advantage amplifies metric-specific signal when groups are equal-sized, and Theorem 2 proves that CANON does not amplify independent metrics — only the grouping metric. These results provide genuine analytical backing for why regrouping works differently from simple numerical scaling. Table 4 empirically confirms this: direct numerical scaling of advantage (56.1% math, 25.1% logic) underperforms CANON-Inter (57.6%, 25.7%) and CANON-Intra (54.7%, 29.1%).
- **Comprehensive empirical evaluation across models and tasks**: The paper tests three LLMs (Qwen2.5-Math-1.5B/7B, Llama3.1-8B) on six math benchmarks and three difficulty levels of ZebraLogic. The efficiency experiments (Table 3, Figure 4) are a standout contribution: CANON-Eff (α=0.96) reduces token consumption by 26.3% vs. DR.GRPO while losing only 0.4 accuracy points, and the Pareto frontier in Figure 4c dominates all baselines across a hyperparameter sweep. The analysis in Table 4 cleanly validates that regrouping — not mere advantage scaling — drives the gains.
- **Clear analysis of complementary benefits**: Figure 2 and Section 6 convincingly show that CANON-Inter (μ=1.0) favors lower-entropy, more certain responses suitable for in-distribution math tasks, while CANON-Intra (μ=0.0) encourages exploration and reflection beneficial for out-of-distribution logic tasks. The "gain of rethinking" analysis (Figure 2f, Figure 6) provides mechanistic insight into why scheduling between the two variants works.

## Weaknesses

### Major

- **No confidence intervals, standard deviations, or error bars for any result**: Tables 1, 2, and 3 report only point estimates. Given that evaluations use temperature 0.6, Avg@10 on smaller subsets (AIME 24/25: 30 problems each), and the headline improvement on math is 1.9 points (57.6 vs. 55.7), the reader cannot assess whether this difference exceeds sampling noise. On the largest gains — +5.0 points on AIME24 (32.7 vs. 27.7) — the result is more plausibly significant, but even here variance matters because AIME24 has only 30 problems and results are averaged over 10 samples. The same concern applies to smaller gaps like the 0.4-point loss on CANON-Eff (56.2 vs. 56.6 in Table 3). Without variance reporting, the paper's central empirical claim that CANON "consistently outperforms prior methods" (abstract) is weaker than it should be.

### Minor

- **Scheduling evaluation mixes model-specific selection with fixed-strategy results**: Section 5.2 tries four scheduling strategies and selects the best per model for the headline CANON-Dynamic results: cosine annealing for Qwen-7B and Llama-8B, accuracy-based *First-Inter-Later-Intra* for Qwen-1.5B. The paper is transparent about this choice. However, the paper also shows that the fixed *First-Inter-Later-Intra* strategy (same schedule for all models) yields performance that consistently exceeds DR.GRPO across all three models (Table 2). The fixed-strategy results are buried in the per-model discussion rather than foregrounded. Since the fixed strategy already makes the core point, the per-model tuning creates unnecessary ambiguity about whether the method requires problem-specific schedule selection.
- **Improvement on standard math benchmarks is modest and concentrated on specific subsets**: The average gain over DR.GRPO on six math benchmarks is 1.9 points (57.6 vs. 55.7). On MATH-500, CANON-Inter (87.0) is actually below Entropy Adv (87.6). The largest math gain is +5.0 on AIME24 (32.7 vs. 27.7). The bigger and more consistent gains appear on ZebraLogic (+5.2 on XLarge subset). The paper's claim of "consistently outperforming" would benefit from a more calibrated tone that distinguishes between the modest math improvement and the stronger logic-reasoning gains.
- **Efficiency variant's α<1 reintroduces the directional prior the method claims to avoid**: Section 4.3 introduces an α < 1 weighting that explicitly penalizes longer responses: "by slightly reducing the weight of longer responses, CANON can accomplish reasoning of high token efficiency." This is a useful practical extension, but it *presupposes that shorter is better*, which is the same type of directional prior the paper's main motivation (Section 1) argues against ("amplifying the impact of specific metric changes without presupposing preferences"). The paper acknowledges this tension, but framing the efficiency variant as a separate knob that *reintroduces* a directional preference — rather than as a natural extension of the "direction-free" principle — would strengthen narrative coherence.

### Trivial

- None.

## Nice-to-Haves

- **Hyperparameter sensitivity analysis for μ**: The paper varies μ across seven values (0.0–1.0 in Figure 5) but only for entropy on Qwen-7B. A brief exploration on a second model or for the length metric would strengthen claims about robustness.
- **Ablation with random grouping**: The paper does not compare CANON to a version that groups responses randomly (i.e., splits responses into two arbitrary groups without using the metric). Such an ablation would directly test whether the metric-based regrouping is essential or whether any split suffices.
- **Formal definition of "gain of rethinking"**: The metric is described in the text (counting reflection patterns, computing the gap in average reward), but a concise formula in the main paper would help reproducibility. The current description in Section 5.1 is adequate but informal.

## Removed Points

- **"Entropy Adv outperforms CANON on MATH-500"** — The paper already acknowledges CANON-Inter is "highly competitive" and the claim is about average performance across 6 benchmarks, not any individual benchmark. Not a real weakness.
- **"Best/second-best formatting confusing"** — The bold/underline notation is standard and clear. Formatting nitpick.
- **"Theorem 2 independence assumption unrealistic"** — The paper explicitly states the independence assumption as a condition of the theorem. Theoretical results require assumptions; this is standard practice.
- **"Arora & Zanette typo"** — Trivial formatting/typographical issue; parser artifacts.
- **"Missing related works"** — Not verifiable without external sources.
- **"Missing appendix/supplementary details"** — Parser strips these from all submissions.

## Novel Insights

None beyond the paper's own contributions. The key insight — that regrouping responses by a metric and computing inter- vs. intra-group advantages can amplify metric influence without imposing a directional prior — is well-articulated in the paper itself.

## Suggestions

1. **Add variance reporting.** Report standard deviations or bootstrapped 95% confidence intervals for all key results (Tables 1, 2, 3). Even a note on the number of seeds used would increase confidence. Given small benchmark sizes (AIME 24/25: 30 problems), bootstrapping over evaluation samples or reporting Pass@1 variance across seeds would be particularly informative.
2. **Foreground the fixed-schedule results.** In Section 5.2 and Table 2, present the model-agnostic *First-Inter-Later-Intra* strategy results as the primary evidence, then report the per-model tuned schedules as a supplementary sensitivity study. This would eliminate any appearance of cherry-picking without losing any information.
3. **Calibrate the language in the abstract and conclusion.** Replace "consistently outperforms" with a more precise statement such as "achieves a 1.9-point average gain on math reasoning and a 2.9-point gain on high-complexity logic reasoning, with larger gains (up to 5.2 points) on the most challenging logic subsets."
4. **Reframe the efficiency variant's relationship to the core motivation.** In Section 4.3, explicitly state that CANON-Eff reintroduces a directional preference (shorter-is-better) as a deliberate design choice orthogonal to the direction-free principle of the main method. This resolves the narrative tension cleanly.

## Score and Decision

**Bracketing (Round 1):** The weak anchors (avg ~3.0–3.2, e.g., EDGE-GRPO, ZAPO, RENT) are papers that were withdrawn or rejected for significant methodological flaws or unclear contributions. The paper under review is clearly stronger — it has a well-defined novel method, theoretical analysis, and broad experiments. The middle anchors (avg ~4.0–5.0, e.g., RankGRPO at 4.00, Off-Policy GRPO at 5.00, Group-Relative REINFORCE at 4.50) are GRPO-adjacent papers with mixed reception; the paper under review is stronger than these in both clarity and empirical scope. The strong anchors (avg 8.00) are on unrelated topics (world models, multimodal verifiers, benchmarks) and are not directly comparable. **Initial bracket: 4.5–6.5.**

**Narrowing (Round 2):** Three topically close anchors were read in full:
- **ExGRPO (avg 6.00, Poster)**: Experience replay for RLVR with larger reported gains (+3.5/+7.6 points). CANON's gains are smaller but the method is more principled (theoretical grounding, no heuristic replay selection). Comparable quality.
- **RL-ZVP (avg 6.00, Poster)**: Entropy-guided advantage shaping for zero-variance prompts. Similar domain and approach; RL-ZVP shows larger gains (up to +8.61) but has hyperparameter sensitivity concerns. CANON has broader evaluation (3 models vs. 2) and a more novel regrouping mechanism. Roughly comparable.
- **On Entropy Control (avg 6.50, Poster)**: Strong theoretical analysis of entropy regularization but evaluated only on 1.5B models. CANON tests on 1.5B, 7B, and 8B models, giving broader empirical support. Slightly below this anchor overall due to the variance-reporting gap.

The paper's strengths — novel method, theoretical validation, broad evaluation, strong efficiency results — place it solidly in the 5.5–6.5 range. Its main weakness (lack of variance reporting) prevents it from being placed higher, as reviewers on similar papers (e.g., RankGRPO, Off-Policy GRPO) explicitly flagged the same issue. **Final score: 6.0.**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| EDGE-GRPO | VZermIifAQ.md | 3.00 | 1 | Much weaker — method is less principled, contributions unclear |
| Useless or Untapped (ZAPO) | FPVB4qSXCZ.md | 3.20 | 1 | Much weaker — narrower scope, less convincing empirical results |
| Maximizing Confidence Alone (RENT) | Qhg479eBmo.md | 3.20 | 1 | Much weaker — fully unsupervised, different problem setting |
| Honesty Alignment | ZjidJlTOxd.md | 3.00 | 1 | Much weaker — different problem, smaller experimental scope |
| Off-Policy GRPO | XXfOf22o3K.md | 5.00 | 1 | Weaker — mixed reviews, some found presentation confusing |
| On Computation of GRPO | hm8b9CQQQY.md | 4.00 | 1 | Weaker — theoretical focus with limited empirical validation |
| RankGRPO | 9664No4ulo.md | 4.00 | 1 | Weaker — unclear methodology, no confidence intervals |
| Group-Relative REINFORCE | 7CFlXvCoN6.md | 4.50 | 1 | Weaker — primarily theoretical reinterpretation, limited experiments |
| Info-GRPO | d5qElNtXS5.md | 4.67 | 2 | Weaker — narrower evaluation, different approach |
| Entropy-Guided Generation | NCLjpR2MDq.md | 4.67 | 2 | Different domain (text-to-image), not directly comparable |
| Entropy Dynamics in RFT | 4XIfmxhTaX.md | 5.50 | 2 | Comparable — theoretical analysis but limited experimental validation |
| ExGRPO | 701tjQXWVk.md | 6.00 | 2 | Comparable — stronger empirical gains, but CANON has more principled method |
| RL-ZVP | kiXFIESZKv.md | 6.00 | 2 | Comparable — similar domain and approach, CANON has broader model evaluation |
| On Entropy Control (AEnt) | LqazVN5epT.md | 6.50 | 2 | Slightly stronger — deeper theoretical analysis, but CANON evaluates on more model sizes |
| Diff. Smoothing | 2RWf359T0p.md | 6.00 | 2 | Different approach (diversity collapse), comparable quality |
| ResT | gNZlaKRWki.md | 6.00 | 2 | Different domain (tool-use), comparable quality |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>