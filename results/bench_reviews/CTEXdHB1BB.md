Now I have everything I need. Let me synthesize the final review.

## Summary

This paper introduces CANON (Conditional Advantage Estimation), a modification to GRPO for RLVR training of large reasoning models. The key idea is to regroup sampled responses by a training metric (e.g., entropy, response length) into two equal-sized groups, then compute inter-group advantage (which metric trend leads to higher accuracy) and intra-group advantage (which responses within the same trend are better). A coefficient μ interpolates between these two signals. CANON-Inter (μ=1) yields a 1.9-point average gain on math reasoning, CANON-Intra (μ=0) yields a 5.2-point gain on the hardest logic problems, and CANON-Eff (weighting length-based groups) produces a dominant Pareto frontier in the performance–efficiency trade-off.

## Strengths

1. **Clean, principled idea with practical simplicity**: Regrouping by a metric and computing inter/intra advantages is elegantly simple — the paper shows that DR.GRPO is a special case (μ=0.5) of CANON. The change to training code is minimal, and the method operates without hand-crafted directional preferences (higher-is-better or lower-is-better), which prior reward-shaping methods require.

2. **Consistent empirical gains across models and tasks**: CANON-Inter (entropy-based) improves over DR.GRPO by 1.9 points on average across six math benchmarks, with a 5.0-point gain on AIME24. CANON-Intra shows a 5.2-point improvement on the hardest ZebraLogic subset (XLarge). These trends hold across Qwen2.5-Math-7B, 1.5B, and Llama3.1-8B, suggesting the method's benefits are not architecture-specific.

3. **Dominant Pareto frontier for efficient reasoning**: CANON-Eff achieves a 26.3% token reduction with only 0.4-point performance loss, and at low token budgets delivers 2.63× the performance of DR.GRPO. Crucially, CANON-Eff avoids the collapse behavior of Length Reward (+) (which drops from 54.8 to 22.5 when its coefficient moves from 0.004 to 0.005), demonstrating substantially more stable exploration of the performance-efficiency frontier.

4. **Mechanistic analysis of training dynamics**: Figure 2f shows that CANON-Intra's reflection gain curve crosses zero after ~90 training steps, coinciding with rapid improvement on complex logic tasks. This provides an interpretable account of why intra-group advantage helps — it incentivizes models to engage in more rethinking when the metric signal is informative — rather than just reporting aggregate score improvements.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance reporting across all experiments**. The paper reports only point estimates in every table and single curves without error bands in every figure. This is problematic for several reasons: AIME 2024 and AIME 2025 each contain only 30 problems, so a 5-point improvement (~1.5 more correct answers) could be within noise without multiple seeded runs. The 1.9-point gap between CANON-Inter (57.6) and DR.GRPO (55.7) in Table 1 may be meaningful, but the 1.0-point gap between CANON-Intra (54.7) and DR.GRPO in the same table could easily be noise. While the paper does use Avg@10 evaluation for small benchmarks (which reduces evaluation variance), the absence of any multi-seed training runs or confidence intervals means the reader cannot assess whether the reported improvements are statistically reliable. This is the single most critical missing piece for a paper whose central claim rests on empirical superiority.

2. **CANON-Dynamic results are based on post-hoc selection of scheduling strategies**. The paper tries four scheduling strategies and selects the best per-model. The reported CANON-Dynamic results come from this selection (Cosin-First-Inter-Later-Intra for 7B/8B, First-Inter-Later-Intra for 1.5B). The paper acknowledges that alternative schedules (Lambda, Cyclic-triangular2 in Appendix D.2) perform worse. This means the claimed advantage of CANON-Dynamic over DR.GRPO is not guaranteed by the method itself but depends on choosing the right schedule, and no principled a priori rule is provided for this choice. However, this weakness is limited to the CANON-Dynamic variant — the static CANON-Inter, CANON-Intra, and CANON-Eff results are unaffected and provide cleaner evidence.

### Minor

1. **Theoretical framework has limited connection to empirical findings**. Theorem 1 establishes that inter-group advantage is amplified when groups are equally sized, and Theorem 2 shows that CANON does not amplify independent conditions. However, neither theorem is used to generate testable predictions. For example, Theorem 1 predicts that unequal group sizes should reduce effectiveness — this could be ablated but is not. Theorem 2's independence assumption (entropy and length are treated as independent) is questionable in practice since longer responses tend toward different entropy distributions, and this violation is not studied. The theory motivates the equal-split design but doesn't provide falsifiable predictions validated empirically.

2. **Missing ablation on group size**. Since Theorem 1's central claim is that equal-sized groups are optimal for signal amplification, varying the split ratio (e.g., 50/50, 60/40, 70/30) would directly test this prediction and ground the theory. The paper does not include this experiment.

3. **Sensitivity of CANON-Eff's α hyperparameter is under-analyzed**. While Table 11 shows performance and token cost across α = {0.5, 0.7, 0.8, 0.88, 0.96}, the analysis does not examine where the trade-off becomes unstable or how the optimal α depends on task difficulty. The claim that CANON "stably explores the entire frontier" is supported visually (no collapse) but lacks a formal stability metric across seeds or coefficient values.

### Trivial

- The paper states Theorem 1's condition as "only when |C_q^+| = |C_q^-| if |C_q^+| is a constant" which is unnecessarily convoluted — the simpler point is that equal splits ensure amplification when the condition is informative. This could be clarified.

## Nice-to-Haves

- Applying CANON to other metrics (confidence, number of reflection steps) — Appendix D.1 already shows this works for reflection count, confirming the framework's generality.
- Example responses showing behavioral differences (e.g., a math problem solved by CANON-Inter but not DR.GRPO) would illustrate the mechanism concretely.
- Combining multiple metrics simultaneously via multi-condition regrouping (4+ groups) — acknowledged as future work; preliminary results would strengthen the extensibility claim.

## Removed Points

- **Criticism that CANON still uses human prior on which metric to group by**: This is acknowledged transparently in the paper — the point is that CANON does not presuppose the *direction* (higher/lower) of the metric's impact, which is the novel claim vs. prior reward shaping. The framing is precise enough.
- **"Theorem 1's derivation depends on p being constant" — the paper explicitly handles this dependence and notes the ratio varies with p.** The harsh critic's complaint is partially based on a misreading; the theorem states the amplification condition correctly.
- **Missing appendix/proofs content**: The parser strips these; the original submission contains them (Appendix E has full derivations).
- **"Alternative schedules perform worse, weakening CANON-Dynamic claims" — the paper already acknowledges this and reports it transparently.** This is kept as a major weakness (post-hoc selection) but the tone is adjusted: the paper does disclose the selection process, making it a methodological concern rather than a deception.
- **Criticism that the paper doesn't report results with standard deviation (the missing experiments section)** — this is already captured in the Major weakness #1.
- **Generic strengths from the Strength Finder** (e.g., "addressed an important problem") — dropped as they lack specific content.
- **Request for larger dataset / more compute** — the current dataset sizes (45k prompts) are already substantial and standard in the field.
- **"The paper does not adequately explain why First-Inter-Later-Intra is expected to work"** — the paper provides the intuition (exploit fast math gains early, then explore for complex logic later), which is a reasonable explanation for the scheduling's motivation.

## Novel Insights

The reviews collectively highlight an interesting tension: CANON's clean, simple idea (regroup by metric → inter/intra advantages) is the paper's greatest strength, but the evaluation methodology (single-seed point estimates, post-hoc schedule selection) is the paper's greatest weakness. This is a recurring pattern in RLVR papers — a genuinely clever algorithmic insight paired with evaluation practices that lag behind what would be considered rigorous in other ML subfields. The most valuable signal from the paper is the *pattern* of results: CANON-Inter consistently helps math, CANON-Intra consistently helps complex logic, and the relationship between μ and entropy is monotonic (Figure 5). This coherence across models and tasks is more compelling than any single number and suggests the method captures a genuine inductive bias, even if individual point estimates lack error bars.

## Suggestions

1. **Add multi-seed results (≥3 seeds) with standard deviations for all main tables** — this is the most impactful improvement the authors could make, converting the current point estimates into statistically meaningful comparisons. This likely requires the most work but is essential.

2. **Clearly separate static and dynamic claims**: Present CANON-Inter (μ=1) and CANON-Intra (μ=0) as the core empirical contribution, and relegate CANON-Dynamic to a secondary "practical extension" with the caveat that scheduling requires validation-set-based selection. Alternatively, provide a principled rule for schedule selection.

3. **Ablate group size** to directly test Theorem 1's prediction, connecting theory to experiment.

4. **For Figures 2 and 4, add standard error bands** across seeds to strengthen the visual claims about training dynamics and Pareto frontiers.

5. **Add a statistical test** (e.g., paired bootstrap or matched-pairs test) comparing CANON-Inter vs. DR.GRPO on the six math benchmarks to quantify confidence in the 1.9-point gap.

## Score and Decision

**Calibration anchors (all from ICLR 2026 / COLM 2025 review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/.../iRWqcnBlLQ.md` (GRPO-λ) | 4.00 | Similar contribution type (GRPO modification), similar evaluation breadth, similar weakness on statistical significance. CANON has clearer results across two task families vs. one. |
| `/home/.../701tjQXWVk.md` (ExGRPO) | 6.00 | Stronger empirical methodology, broader baselines, more thorough analysis. CANON's core idea is cleaner but the evaluation is weaker. |
| `/home/.../9fwvcl0Jur.md` (Can GRPO Help) | 2.50 | Synthetic experiments, limited scope. CANON is substantially stronger empirically. |
| `/home/.../OHaFgEa0yZ.md` (Uncalibrated Reasoning) | 3.00 | Narrow scope and limited model evaluation. CANON is stronger in breadth and contribution. |
| `/home/.../jGbRWwIidy.md` (RLVR Incentivizes) | 5.33 | Strong theoretical framing combined with empirical validation. CANON is comparable in quality but has more actionable algorithmic contribution. |
| `/home/.../Qr9FAtcpeR.md` (GRPO-MA) | 3.50 | Weaker results on fewer benchmarks. CANON is clearly stronger. |

Relative to these anchors, CANON sits between the 4.00 (GRPO-λ) and 6.00 (ExGRPO) papers. Its core algorithmic insight is cleaner than GRPO-λ's, but its empirical methodology (no variance reporting) is notably weaker than ExGRPO's. The paper is clearly above the rejection-level papers (2.5–3.5) due to the breadth and consistency of its results across models and tasks.

The static CANON-Inter/Intra and CANON-Eff results provide solid evidence for a genuine contribution. The major weaknesses (variance reporting, post-hoc scheduling) are addressable in revision and do not invalidate the core claims.

**Score: 5.0** — Solid contribution with room for methodological improvement.

**Decision: Accept (Poster)**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>