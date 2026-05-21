## Summary

This paper introduces CANON (Conditional Advantage Estimation), a method for RLVR (Reinforcement Learning with Verifiable Rewards) in LLMs. The core idea is to regroup sampled responses into two groups based on a target metric (e.g., entropy or response length) and compute separate inter-group and intra-group advantages. Inter-group advantage identifies which metric trend correlates with higher rewards, while intra-group advantage selects better responses within the same trend. This avoids imposing hand-crafted directional priors (higher-is-better or lower-is-better). The method is evaluated on six math benchmarks and three logic reasoning subsets across three model families, with additional experiments on token-efficiency trade-offs.

## Strengths

- **Clean and well-motivated methodological contribution.** The idea of regrouping responses by a metric and computing inter/intra-group advantages to *learn* the metric's beneficial direction from data (rather than imposing it) is sensible and addresses a real limitation of prior reward/advantage shaping approaches. The connection to DR.GRPO as a special case (μ=0.5) when groups are equal-sized (Eq. 7) is clearly established.

- **Consistent empirical gains across diverse settings.** CANON-Inter (Entropy) achieves 57.6% average math accuracy vs. DR.GRPO's 55.7% (Table 1), and CANON-Intra achieves 29.1% on ZebraLogic vs. DR.GRPO's 26.2%, with the margin growing on the hardest subsets (5.2 points on XLarge). These gains hold across three different model scales (Qwen-7B, Qwen-1.5B, Llama-8B) and two distinct task families (math and logic reasoning) in Table 2.

- **Strong efficient-reasoning results.** Section 5.3 is the paper's strongest part. CANON-Eff achieves a clearly superior Pareto frontier over length-penalty baselines (Clip Length, Length Reward, Length Reward*), reducing token consumption by 26.3% with minimal performance loss (Table 3, Figure 4). The budget-performance curves show CANON outperforming baselines at both low and high token budgets. The stability advantage—where Length Reward(+) collapses from 54.8 to 22.5 with a 0.001 coefficient change while CANON remains stable—is well-demonstrated.

- **Insightful ablation and analysis.** Figure 5 shows smooth hierarchical control over entropy across μ values, validating the method's directional selectivity. Figure 6 provides an interpretable explanation for why CANON-Dynamic works: it combines the reflection gains of CANON-Intra with the reward stability of CANON-Inter. Table 4's comparison with direct numerical scaling is a useful control that supports the selective-amplification claim.

## Weaknesses

### Fatal
None.

### Major

1. **Discrepancy between Figure 3's table and Table 2/Table 1.** The reported values in Figure 3's accompanying table do not match the corresponding entries in Tables 1 and 2. For example, Figure 3 lists DR.GRPO on Llama-8B as 22.6% math and 18.9% logic, while Table 2 reports 22.0% and 14.9%. More concerningly, Figure 3 lists CANON-Dynamic (called "Cosin-First-Inter-Later-Intra" in Table 2) for Llama-8B at 35.2/35.2, while Table 2 reports 22.6/18.9 for the same setting. For Qwen-7B, Figure 3 reports DR.GRPO at 57.6/39.2, while Table 2 reports 55.7/26.2. The Figure 3 values appear to be on a different scale or computed differently—the paper must clarify whether these are normalized/scores, the result of a different averaging scheme, or a data-entry error. As presented, the radar chart cannot be verified against the underlying data.

2. **No variance or significance reporting anywhere.** All results are reported as single numbers with no mention of multiple seeds, confidence intervals, or significance tests. This is particularly problematic because the headline gains are modest (1–3 points on math tasks) and RLVR training is known to be noisy. Without at least mean and standard deviation over 2–3 seeds, it is impossible to assess whether the reported improvements are meaningful or attributable to training noise. This is the single highest-priority fix.

### Minor

3. **Baseline hyperparameter tuning is unclear.** The paper states evaluations are "under a unified setting" but does not clarify whether each baseline method (ReMax, R++, RLOO, GRPO, DR.GRPO, Entropy Adv, Clip-Cov) had its hyperparameters (learning rate, clipping range, etc.) tuned separately, or whether all used the default DR.GRPO settings. If the latter, some baselines may be under-tuned, making the comparison less fair. This should be clarified.

4. **Theoretical contribution is supporting, not foundational.** Theorems 1 and 2 establish that inter-group advantage amplifies the grouping metric's signal under equal-group and independence assumptions. These are clean supporting results but do not constitute a theoretical explanation for why the method works in practice; they confirm what the design intends. The paper's framing ("theoretical guarantee") slightly overstates what is provided. This does not detract from the empirical contribution but should be scoped accurately.

5. **Dataset filtering for the 45k subset of OpenR1-Math-220k is not described.** The paper mentions using a "subset with 45k prompts" that is "filtered and constructed" without specifying the filtering criteria (difficulty, answer length, etc.). If filtering correlates with the grouping metric, it could affect the relative improvement of CANON over baselines.

### Trivial

6. **No explicit statement of ZebraLogic evaluation metric** (Pass@1 vs. exact match vs. other) in the main text.

## Nice-to-Haves

- Demonstrating CANON with a third grouping metric (e.g., confidence, number of self-corrections) would strengthen the generality claim.
- A control experiment that scales advantage only for responses in a particular metric group (rather than global scaling) would more directly test Theorem 2's selectivity.
- Providing guidance on how to choose the scheduling strategy for CANON-Dynamic without access to a validation set.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **The harsh critic's claim that Figure 3 shows CANON-Dynamic "at 35.2 on both axes" for Llama-8B contradicts Table 2 "by a large margin" but this is presented as a larger discrepancy than what Table 2 actually shows.** The actual claim (CANON-Dynamic for Llama-8B at 35.2 vs. Table 2's 22.6) is already captured above—no need for the redundant framing about the radar chart being "suspicious" or "fabricated." The core issue (unexplained different numbers) is merged into the major weakness above. The "fabricated" speculation is removed as it cannot be verified; the values may come from a different normalization.

- **The critic's claim that the efficient reasoning stability comparison is "based on a single example" and that "other intervals of α would also cause collapse."** This is speculative. The paper shows CANON's frontier with five α values, which is a reasonable demonstration. The stability claim is supported by the data shown. This criticism is weakened/removed.

- **The critic's claim about "different group sizes" being a conceptual issue.** The paper always uses equal groups (Theorem 1's recommendation), so this is a non-issue. Removed.

- **The critic's concern that "direct scaling is a very crude baseline" and that a better control would "scale the advantage only for responses belonging to a particular metric group."** This is a reasonable suggestion but moved to Nice-to-Haves, as the current ablation (Table 4) already shows that CANON's regrouping mechanism achieves effects that global scaling cannot.

- **Strength Finder's strengths about the problem being "important" or "well-framed" without specific evidence.** These generic strengths are removed.

## Novel Insights

The two-reviewer synthesis surfaces a useful observation not explicitly made by the paper: the efficient-reasoning experiments (Section 5.3) are substantially stronger evidence for CANON's benefits than the accuracy-gain experiments (Tables 1-2). In the efficiency setting, CANON produces a clean Pareto improvement with demonstrated stability (no collapse across a range of α values). In contrast, the accuracy gains of 1–3 points over DR.GRPO lack variance estimates, making their significance uncertain. The paper would benefit from emphasizing this asymmetry and treating the efficiency results as its primary empirical contribution.

## Suggestions

1. **Clarify Figure 3's values.** State whether the radar chart uses normalized/min-max-scaled values, a different averaging scheme, or raw percentages. If the values in the table are correct, explain how they relate to Tables 1-2. If they are incorrect, correct them.

2. **Add multiple-seed results** for at least the main comparisons (Tables 1 and 2). Report mean and standard deviation across 2-3 seeds.

3. **Clarify baseline tuning.** State whether each baseline was individually hyperparameter-tuned, or whether all used the DR.GRPO defaults under the "unified setting."

4. **Describe the 45k dataset filtering criteria** briefly in the main text or appendix.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all on RL/LLM reasoning topics):**
- Weak band (avg < 3.5): Papers on LLM understanding via RL (avg 3.0), RL in-context learning (avg 3.75), RAG with reward (avg 3.0) — all withdrawn/rejected. The CANON paper is clearly stronger than all of these.
- Middle band (3.5–7.5): "Rewarding Progress: Scaling Automated Process Verifiers" (avg 7.14, Spotlight) — much stronger theoretical framing and clearer narrative than CANON. EURUS (avg 6.5, Poster) — broader in scope with strong results. These set the upper bound.
- Strong band (avg > 7.5): WizardMath (8.0, Oral), MetaMath (8.0, Spotlight), SCoRe (8.0, Oral) — papers with very strong empirical results or novel methodology. CANON does not reach this tier.

**Initial bracket: 5.0 – 7.0**

**Round 2 — Narrowing inside the bracket:**
- TPO (avg 6.33, Poster): Preference optimization for reasoning. Similar to CANON in being a focused methodological improvement. CANON has broader evaluation (3 models, 2 tasks, efficiency) but has the Figure 3 discrepancy and no variance reporting. Comparable papers, CANON slightly weaker due to presentation issues.
- PQM (avg 6.4, Poster): Process Q-value model. Strong empirical results with clear baselines. CANON is comparable in evaluation breadth but PQM has cleaner presentation.
- GPO (avg 5.67, Poster): Group preference optimization. CANON has stronger empirical evaluation.
- Q-Shaping (avg 5.67, Reject): CANON is clearly better — better written, more thorough experiments.

**Final position:** CANON is comparable to TPO (6.33) and PQM (6.4) but held back by the Figure 3 discrepancy and missing variance estimates. It is stronger than the 5.67 papers. Score of 6.0 reflects a solid paper with real contributions that needs clarification on key presentation issues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>