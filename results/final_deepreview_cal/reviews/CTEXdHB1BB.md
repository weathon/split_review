Now I have sufficient calibration. Let me write the consolidated review.

**Final bracket determination:** Round 1 bracketing placed this paper between the weak-anchor band (2.3–3.0) and the strong-anchor band (8.0). Round 2 anchors showed it sits above clearly rejected papers at 5.0–5.25 (VerifierQ, APA, On Designing Effective RL Reward) but below the accepted TPO at 6.33, which had comparably comprehensive evaluation without the radar chart issue. The paper is closest to the 5.5 anchor ("Learning to Reason at Pre-Training Scale"), which was also rejected despite a solid core idea. I place it at 5.5 — the core contribution is meaningful, but the radar chart inconsistency is a genuine presentation error that undermines trust, and the post-hoc scheduling selection weakens the dynamic method's claimed generality.

---

## Summary

This paper introduces CANON (Conditional Advantage Estimation), a method for reinforcement learning with verifiable rewards (RLVR) that regroups sampled responses by a metric (entropy or length) and computes inter-group and intra-group advantages. The key insight is that this amplifies the metric's influence on the advantage signal without presupposing its directional preference (higher-is-better or lower-is-better). The authors show that CANON-Inter (favoring inter-group comparison) improves math reasoning accuracy (e.g., +1.9 points on Qwen-7B math, +5.0 on AIME24), while CANON-Intra (favoring intra-group comparison) helps on complex logic reasoning (e.g., +5.2 points on XLarge ZebraLogic). By scheduling between the two, CANON-Dynamic achieves balanced gains across both task types, and CANON-Eff (length-based grouping with weighted conditions) produces a superior Pareto frontier for token efficiency.

## Strengths

- **Novel and well-motivated idea.** The core concept — regrouping responses by a metric to compute inter/intra-group advantages that amplify the metric's influence without imposing a fixed directional prior — is clean, intuitive, and clearly differentiated from prior advantage-shaping approaches that rely on hand-crafted penalties. The theoretical framing (Theorems 1 and 2) supports the claim that CANON selectively amplifies the grouping metric's influence without amplifying independent factors.

- **Comprehensive evaluation across models and tasks.** Experiments span three models (Qwen2.5-Math-7B/1.5B, Llama3.1-8B), six math benchmarks (AIME24/25, OlympiadBench, AMC, MATH-500, GSM8K), and three difficulty levels of a logic reasoning task (ZebraLogic). This is more extensive than many comparable RLVR papers. The 5.2-point improvement on the hardest ZebraLogic subset (XLarge) and the 5.0-point gain on AIME24 are concrete, non-trivial improvements.

- **Efficiency Pareto frontier is a genuinely useful finding.** CANON-Eff's ability to reduce tokens by 26.3% with only 0.4-point accuracy drop (α=0.96), and to achieve 2.63× the performance of DR.GRPO at low token budgets (α=0.88), provides a practical contribution. The stability of CANON-Eff across α values versus the collapse of Length Reward (+) at coefficient 0.005 is a meaningful robustness advantage.

- **Theoretical grounding.** Theorem 1 provides a formal condition under which the inter-group advantage yields a stronger signal than DR.GRPO. Theorem 2 shows selective amplification — CANON amplifies the grouping metric's influence without amplifying independent factors. While these are not deep theoretical breakthroughs, they are adequate formal support for the proposed method.

## Weaknesses

### Major

- **Radar chart (Figure 3) numbers are inconsistent with the reported tables.** The embedded table in Figure 3 gives values that do not match any results in Tables 1 or 2. For example: (a) DR.GRPO for Qwen-7B is listed as Math 57.6 / Logic 39.2, but Table 2 reports 55.7 / 26.2 — the logic number differs by 13 points. The Math 57.6 actually matches CANON-Inter (Entropy) from Table 1. (b) DR.GRPO for Llama-8B in the radar chart (Math 22.6 / Logic 18.9) matches the CANON-Dynamic (Cosin) values from Table 2, not DR.GRPO's actual numbers (22.0 / 14.9). (c) CANON-Dynamic for Llama-8B shows Math 35.2 / Logic 35.2, but Table 2 reports 22.6 / 18.9 (Cosin) and 22.1 / 17.7 (First-Inter) — these values do not appear in any table. (d) CANON-Inter and CANON-Intra values for Llama-8B (35.2, 15.0 and vice versa) are not reported in any table. The paper provides no explanation for these discrepancies. This is a significant presentation error that undermines trust in the paper's central visualization and must be corrected.

- **Post-hoc scheduling strategy selection weakens the dynamic method's claimed generality.** The paper tries four scheduling strategies and then selects a model-specific strategy for each model (Cosin-First-Inter-Later-Intra for Qwen-7B and Llama-8B, First-Inter-Later-Intra for Qwen-1.5B) based on which yields the best per-model results. This is explicitly acknowledged ("A specifically designed strategy is acceptable for better performance in practice"), but it makes CANON-Dynamic less of a principled method and more of a recipe of "pick what works best per model." A fairer demonstration would pre-specify one scheduling rule (e.g., μ = 1 − training_accuracy) and evaluate it consistently across all models, even if it underperforms on some.

### Minor

- **Single-run results without uncertainty quantification.** All main tables report single runs with no standard deviations, confidence intervals, or error bars. While multi-seed RL training at 7B scale is expensive, some of the reported gains are small enough (e.g., 1.9 points on math, 1.5 points on logic) that variance across seeds could affect conclusions. A sensitivity analysis with even 2–3 seeds would substantially strengthen the claims.

- **The Pareto frontier comparison for efficient reasoning relies on a sparse set of hyperparameters for baselines.** The paper tests 4 values for Length Reward (+), 3 for Length Reward (×), and 2 for Clip Length. While CANON does show better stability (the Length Reward collapse at 0.005 is instructive), the claim of "Pareto dominance" would be more convincing with a denser grid or evidence that the chosen values span each method's effective range.

- **Theorem 1's condition is narrow.** The theorem assumes |C_q^+| is a constant and requires equal-sized groups. In practice, the paper always splits groups equally, so the condition is satisfied, but the theoretical framing is less general than the method itself, which could in principle work with unequal splits.

### Trivial

- None beyond the issues already listed above.

## Nice-to-Haves

- Adding standard deviations from 2–3 seeds would increase confidence in the reported gains.
- A pre-specified (non-per-model) scheduling rule for CANON-Dynamic would better demonstrate generality.
- Including the scaling methodology for the radar chart explicitly in the caption or text would prevent confusion.
- A brief limitations paragraph acknowledging that CANON requires choosing a metric and that grouping size is fixed to equal splits would improve the paper's completeness.

## Removed Points

- **Criticism that Theorem 1's proof is relegated to an appendix (not verifiable).** The appendix exists in the original submission; the parser stripped it. Removed per hard rules.
- **Criticism that Section 5.3 baseline training conditions may differ (max length, dataset).** The paper states "We follow the training setups described in Section 5.1" and that all baselines are "conducted with DR.GRPO," indicating shared conditions. Removed as factually not supported by the paper.
- **Criticism that CANON needs comparison with other metric-based methods not tested.** This is a generic request that could apply to any paper; no specific missing method is identified. Removed.
- **Criticism about missing reproducibility details (exact training script, cosine schedule parameters).** The paper provides key hyperparameters (batch size, learning rate, ε_high, grouping strategy) sufficient for replication. Exact scripts are not expected in a main paper. Removed.
- **Several strength-finder items about "quantifiable performance gains" and "substantial improvement" — kept where concrete, removed generic restatements of results.**
- **Strength about "consistent improvement across multiple model scales" — kept as it is specific and verified.**
- **Strength about "hierarchical metric control validated empirically" — kept as it cites a specific figure (Figure 5) with clear trends.**
- **Strength about "selective amplification outperforms naïve scaling" — kept as it cites Table 4.**
- **Criticism about "no discussion of limitations" — this is a generic suggestion, moved to Nice-to-Haves.**

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis surfaced one genuinely novel observation: the radar chart is not simply a different normalization but appears to systematically mislabel method identities (DR.GRPO's plotted values are actually CANON-Dynamic's numbers for Llama-8B, and CANON-Inter's numbers for Qwen-7B), which no single reviewer identified clearly. This suggests either a plotting error where data series labels were swapped, or a deliberate scaling that the paper fails to document.

## Suggestions

1. **Fix the radar chart (Figure 3).** Either (a) correct the numbers to match Tables 1 and 2, clearly state the normalization if one was applied, or (b) remove the embedded table and simply present the radar chart as a qualitative visualization with a note that axes are normalized.
2. **Pre-specify a single scheduling rule for CANON-Dynamic** (e.g., μ = 1 − training_accuracy) and evaluate it consistently across all models, treating the per-model strategy search as a separate analysis.
3. **Add 2–3 seeds** for at least the main comparison (CANON-Dynamic vs. DR.GRPO on Qwen-7B) to provide error bars on the headline numbers.
4. **Test additional values for the Length Reward baselines** (e.g., coeff=0.002, 0.003, 0.006) to strengthen the Pareto dominance claim, or soften the claim to "a more favorable frontier over the range tested."

## Score and Decision

**Calibration report:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| 28TLorTMnP | 2.50 | R1 (weak) | Much weaker — had fundamental methodological flaws; CANON is clearly stronger |
| ZK1NnjpjEs | 3.00 | R1 (weak) | Much weaker — basic NLU fine-tuning; CANON is more novel and comprehensive |
| mMPMHWOdOy | 8.00 | R1 (strong) | Stronger — WizardMath was a major empirical contribution; CANON is less impactful |
| rfdblE10qm | 8.00 | R1 (strong) | Stronger — provided convergence theory for BT reward models; CANON's theory is shallower |
| OD9pwKQzXl | 5.25 | R1/R2 | Slightly weaker — VerifierQ had unclear presentation and weaker experiments; CANON has cleaner motivation and broader eval |
| F0GNv13ojF | 5.17 | R1/R2 | Similar quality — both have solid core ideas with meaningful evaluation gaps; CANON's radar issue is analogous to this paper's incremental-novelty criticism |
| MwU2SGLKpS | 4.50 | R1 | Slightly weaker — GenRM had limited novelty claims; CANON's regrouping idea is more distinctive |
| BGnm7Lo8oW | 5.50 | R1/R2 | Most comparable — both have interesting core ideas with experimental limitations that prevent strong acceptance; CANON's evaluation is broader but has the radar chart issue |
| O0sQ9CPzai | 6.33 | R2 | Slightly stronger — TPO had similarly comprehensive experiments without a presentational error like the radar chart |
| RtOTTdWbZd | 5.25 | R2 | Slightly weaker — APA had narrower evaluation scope; CANON's multi-model multi-task eval is more convincing |

**Round 1 bracket:** [5, 7]  
**Round 2 narrowing:** Paper is stronger than the 4.50–5.25 cluster (VerifierQ, GenRM, APA, On Designing Effective RL Reward) due to a more novel core idea and broader evaluation, but weaker than TPO (6.33) due to the radar chart presentation error and post-hoc scheduling. Most comparable to "Learning to Reason at Pre-Training Scale" (5.50), which was rejected despite a solid core idea due to experimental limitations.

Based on this calibration, the paper merits a score of **5.5**. The core contribution (conditional regrouping for advantage estimation) is genuinely novel and well-motivated, with reasonably comprehensive experiments. However, the radar chart inconsistency is a significant presentational error that undermines the paper's credibility and must be addressed before acceptance. The post-hoc scheduling selection and single-run results are additional concerns. The paper sits in the borderline range where the core idea is solid enough to warrant revisions, but the current submission is not ready for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>