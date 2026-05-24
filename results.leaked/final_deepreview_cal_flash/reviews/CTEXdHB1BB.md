Now let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me compose the final review.

---

Actually, I need to include the calibration comparison. Let me organize the anchors.

**Round 1 — Bracketing anchors:**
- Weak band (< 3.5): ZK1NnjpjEs (3.0), 28TLorTMnP (2.5), 9LAqIWi3QG (3.0), RiDtvlNiqp (3.0)
- Middle band (3.5-7.5): BGnm7Lo8oW (5.50), F0GNv13ojF (5.17), MwU2SGLKpS (4.50), gdzpnRBP4F (4.50)
- Strong band (> 7.5): OOxotBmGol (8.0), mMPMHWOdOy (8.0), rfdblE10qm (8.0), WJaUkwci9o (8.0)

**Round 2 — Narrowing anchors (4.5-8.0):**
- 0er6aOyXUD (5.40), O0sQ9CPzai (6.33), Ze4aPP0tIn (6.60), womU9cEwcO (6.67), IEduRUO55F (6.25), IcVNBR7qZi (6.25)

My bracket from round 1: The paper is clearly above the 3.0 level papers (which had trivial contributions). It's also above the 4.5-5.5 level papers (which had limited experiments or weak novelty). It's comparable to the 6.25-6.67 papers which were accepted and had solid contributions with some notable weaknesses.

Initial bracket: between 5.5 and 7.0.

After round 2: The paper is stronger than the 5.40 paper (benchmark paper with limited novelty) and the 5.17-5.50 papers. It's in the same range as the 6.25-6.67 papers. The 6.33 TPO paper had limitations (only one model type, limited tasks) — CANON has broader experiments. The 6.25 vanishing gradients paper had strong theoretical contribution but limited solution.

I'd place CANON at 6.5.## Summary

This paper proposes **CANON** (Conditional Advantage Estimation), a method for RLVR (Reinforcement Learning with Verifiable Rewards) that regroups sampled responses by a metric (entropy or response length) into two equal-sized groups and computes inter-group and intra-group advantages. The inter-group advantage amplifies the influence of the grouping metric without presupposing its direction, while the intra-group advantage identifies better responses within the same metric trend. Experiments across three LLMs (Qwen2.5-Math-7B/1.5B, Llama3.1-8B) on six math benchmarks and three complex logic reasoning benchmarks show consistent improvements over GRPO and DR.GRPO, and CANON applied to response length achieves a better Pareto frontier for token efficiency.

## Strengths

1. **Novel and principled advantage estimation method.** The core idea—regrouping responses by a metric and computing separate inter/intra-group advantages to amplify metric signals without directional bias—is original and well-motivated. Theorem 1 proves that inter-group advantage amplifies the grouping metric's influence when groups are equal-sized, and Eq. 7 elegantly shows DR.GRPO is the special case μ=0.5 of the unified CANON formulation.

2. **Consistent empirical gains across models and tasks.** CANON-Inter (entropy) improves math accuracy by +1.9 points over DR.GRPO on average (57.6 vs. 55.7, Table 1); CANON-Intra (entropy) improves complex logic reasoning by +2.9 points (29.1 vs. 26.2), with the gap widening on harder subsets. CANON-Dynamic outperforms DR.GRPO on *both* task types across all three LLMs (Table 2, Figure 3), demonstrating robustness.

3. **New Pareto frontier for token efficiency.** Figure 4c shows CANON-Eff's cost-performance frontier dominates all compared baselines (Clip Length, Length Reward +/ *). CANON-Eff (α=0.96) reduces token consumption by 26.3 % with only a 0.4‑point accuracy drop (Table 3), and at α=0.88 it achieves 2.63× higher performance at low token budgets while cutting tokens by 45.5 % at matched performance.

4. **Empirical verification of selective amplification vs. naive scaling.** Table 4 shows that direct numerical amplification of the advantage (multiplying by 2) degrades logic reasoning (25.1 % vs. DR.GRPO's 26.2 %), whereas CANON-Inter improves math (57.6 %) while maintaining logic performance (25.7 %), confirming Theorem 2's claim that CANON selectively amplifies the grouping metric without amplifying unrelated factors.

5. **Insightful training dynamics analysis.** Figures 2, 5, and 6 reveal how CANON-Inter drives rapid math improvement with decreasing entropy, CANON-Intra fosters exploration and positive rethinking gains on logic tasks, and CANON-Dynamic simultaneously maintains positive rethinking gain *and* high training reward—explaining why scheduling achieves comprehensive performance.

## Weaknesses

### Major

1. **No statistical uncertainty quantification.** All experiments appear to be single-run, with no standard errors, confidence intervals, or multi-seed results reported. For the AIME 24/25 benchmarks (30 problems each), the reported differences of a few percentage points could fall within the noise of a single run. While the consistency of improvements across 3 models and 9 benchmarks partly mitigates this concern, the absence of any variance estimate makes it impossible to assess the statistical reliability of the claimed gains. Adding at least 3 seeds with mean and standard deviation for the main comparisons (Tables 1 and 2) is the single highest-leverage improvement.

### Minor

2. **Entropy Adv and Clip-Cov baselines are cited but not described.** These methods appear in the tables (Table 1, Table 4) and are referenced only by citation (Cheng et al., 2025; Cui et al., 2025) without any description of what they do. A reader cannot gauge how strong these baselines are or how they relate to CANON without looking up external papers.

3. **Post-hoc selection of scheduling strategy per model.** The paper reports trying several scheduling strategies and selecting the best one per model to produce the final results in Figure 3 (Cosin-First-Inter-Later-Intra for Qwen-7B and Llama-8B, First-Inter-Later-Intra for Qwen-1.5B). This constitutes tuning on the test benchmarks to some degree. The claim is weakened because the paper does not hold out a validation set for schedule selection. (The paper does show that First-Inter-Later-Intra works consistently across all three models in Table 2, which partially addresses this.)

4. **Theorem 2's independence assumption is strong.** Theorem 2 assumes that the conditions used for grouping are independent. For metrics like entropy and response length, which are correlated in practice, the independence assumption does not hold. While the theorem provides useful intuition about selective amplification under ideal conditions, its direct applicability to realistic settings is limited.

5. **DAPO is not compared as a full baseline despite sharing design elements.** The paper follows DAPO's training setup (clip-higher strategy, response-level length bias correction) but does not include DAPO as a comparison method. Since DAPO is a competitive recent RLVR system, including it would better isolate whether CANON's gains come from the grouping mechanism rather than other shared design choices.

### Trivial

6. **"Gain of Rethinking" / "reflection gain" (Figures 2f, 6) could be more explicitly defined.** The text describes it as "the gap in average reward between the group with more and fewer reflections," but the exact procedure for counting reflection patterns is not specified.

## Nice-to-Haves

- An ablation on group split ratios other than equal-sized groups would test whether Theorem 1's equal-size condition is strictly necessary in practice.
- Testing a third grouping metric (e.g., token-level confidence or number of reasoning steps) would strengthen the claim that the mechanism generalizes across metrics.
- Including a held-out validation set for schedule selection would address the post-hoc selection concern more cleanly.
- A comparison with DAPO as a full system would help situate CANON in the current best-practice landscape.

## Removed Points

- **"Abstract oversimplifies"**: The abstract's claim that CANON (which includes CANON-Dynamic) consistently outperforms is supported by Table 2 across all three models. The abstraction to "CANON" is appropriate for a framework-level claim.
- **"Theorems are informal / unclear"**: Theorem 1's statement and the equal-size condition are stated clearly. The informal presentation level is standard for conference papers.
- **"Gain of Rethinking not precisely defined"**: It is defined (gap in average reward between groups with more vs. fewer reflections), sufficiently for a training dynamics visualization.
- **"Baselines may not be thoroughly tuned"**: Speculative—the paper reports tuning grids for each baseline.
- **"45.5% token reduction is ambiguous"**: Grammar-level concern on a clearly scoped comparison.
- **"2.63× claim against DR.GRPO which is not length-optimized"**: The comparison is valid in context—the claim is about low-token-budget efficiency, where even non-length-optimized methods are relevant.
- **"Length Reward (+) collapse from 54.8 to 22.5"**: This is the paper's own observation demonstrating CANON-Eff's stability, not a weakness.
- **All appendix-related comments**: The appendix is stripped by the parser; these points cannot be verified from the on-page content.
- **"Missing related work / PRIME"**: As per policy, missing-related-work criticisms are removed.
- **"Tie-breaking when sorting by metric values not discussed", "Entropy computation should be explicitly defined"**: Trivial implementation details.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective not already present in the paper's own analysis.

## Suggestions

1. Report results with at least 3 random seeds (mean ± std) for the core comparisons in Tables 1 and 2. If compute is prohibitive, at minimum run multiple seeds for the most critical comparisons (CANON-Inter vs. DR.GRPO on math, CANON-Intra vs. DR.GRPO on logic).
2. Briefly describe what Entropy Adv and Clip-Cov do in the main text (1–2 sentences each) so readers can assess the baselines without external lookups.
3. Explicitly state the schedule-selection procedure and, ideally, validate the chosen schedule on a held-out subset.
4. Add a discussion of Theorem 2's independence limitation and note when it might or might not hold for real metrics.
5. Include DAPO as a full baseline if compute allows, or explain more clearly why it is excluded (e.g., DAPO is a full training framework, not purely an advantage estimation method).

## Score and Decision

**Score calibration summary.**

*Round 1 (bracketing):*
- Weak band (< 3.5): ZK1NnjpjEs (3.0) — PPO+LoRA for NLU, no novelty → CANON is much stronger.
- Middle band (3.5–7.5): BGnm7Lo8oW (5.50), F0GNv13ojF (5.17) — each has a solid motivation but limited experiments or marginal solutions → CANON has broader experiments and more thorough analysis.
- Strong band (> 7.5): OOxotBmGol (8.0), mMPMHWOdOy (8.0) — accepted papers with very strong empirical/theoretical contributions → CANON is not at this level due to the variance-reporting gap.

→ **Initial bracket: 5.5 – 7.0**

*Round 2 (narrowing):*
- O0sQ9CPzai (6.33, accepted) — TPO: multi-branch preference optimization for reasoning, tested on only one model family → CANON tests 3 model families and has broader evaluation.
- IcVNBR7qZi (6.25, accepted) — Vanishing gradients in RFT: strong theoretical contribution but limited practical solution → CANON has comparable theoretical grounding and stronger empirical scope.
- 0er6aOyXUD (5.40, rejected) — Reward model benchmark with limited novelty → CANON is clearly stronger.
- Ze4aPP0tIn (6.60, accepted) — Twisted SMC for math reasoning verification → comparable evaluation breadth.

The paper is stronger than the 5.0–5.5 range papers (which have weaker empirical scope) and comparable to accepted papers in the 6.25–6.60 range. The main gap to the 7.0+ range is the single-run evaluations. The strongest of the retrieved 6.x anchors (6.60) is slightly ahead on polish but CANON matches it on breadth. Score is placed at the upper end of the plausible range given the consistent cross-model results.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>