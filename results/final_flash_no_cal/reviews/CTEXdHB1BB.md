Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes Conditional Advantage Estimation (CANON), a method for RLVR that regroups sampled responses by a target metric (entropy or length) and computes inter-group and intra-group advantages, amplifying the metric's influence without presupposing a preferred direction. The approach is evaluated across three LLMs (Qwen2.5-Math-7B/1.5B, Llama3.1-8B) on six math benchmarks and three ZebraLogic subsets. CANON-Inter (entropy) achieves up to 1.9-point gains on math, CANON-Intra (entropy) yields up to 5.2-point gains on complex logic, and the dynamic scheduling variant (CANON-Dynamic) maintains competitive performance across both task types. When applied to response length (CANON-Eff), the method establishes a favorable Pareto frontier in the performance–token-efficiency trade-off, with reductions of up to 45.5% in tokens at equal performance.

## Strengths

- **Consistent empirical advantage over DR.GRPO across models and tasks.** CANON-Inter (Entropy) achieves 57.6% average math accuracy vs. DR.GRPO’s 55.7% on Qwen-7B (Table 1), and CANON-Dynamic outperforms DR.GRPO on both math and complex logic across all three models (Table 2). The improvement is not isolated to one configuration.

- **Demonstration of a superior efficiency Pareto frontier.** CANON-Eff with α=0.96 reduces token consumption by 26.3% while losing only 0.4 accuracy points, and with α=0.88 achieves substantially higher performance at low token budgets than all baselines (Table 3, Figure 4). The Pareto frontier of CANON-Eff clearly dominates that of Clip Length, Length Reward (+), and Length Reward (*).

- **Selective amplification empirically validated.** Table 4 shows that directly scaling the advantage numerically (A = A×2) yields 56.1 math / 25.1 logic, while CANON-Inter achieves 57.6 / 25.7 and CANON-Intra achieves 54.7 / 29.1—supporting the claim that the regrouping operation, not mere amplification magnitude, drives the benefit.

- **Flexible scheduling that balances opposing behavioral trends.** Section 5.2 and Figure 6 show that CANON-Dynamic simultaneously maintains positive reflection gains and high training reward—a combination neither pure CANON-Inter nor pure CANON-Intra achieves alone—and generalizes this balance across three model scales (1.5B, 7B, 8B).

- **Systematic control over the target metric's trend confirmed.** Figure 5 demonstrates that varying μ from 0.0 to 1.0 produces a monotonic, hierarchical change in generation entropy (increasing to decreasing), validating that CANON-Inter and CANON-Intra can steer the metric in opposite directions without hand-crafted preferences.

## Weaknesses

### Fatal
None.

### Major

- **Radar chart (Figure 3) values are inconsistent with the main tables and unexplained.** The accompanying table in Figure 3 reports numbers that do not match the accuracy scores in Tables 1 and 2. For Qwen-7B, the radar lists DR.GRPO math=57.6 and logic=39.2, but Table 1 gives DR.GRPO math=55.7 and logic=26.2. For Llama-8B, DR.GRPO math is listed as 22.6 (vs. 22.0 in Table 2) and logic as 18.9 (vs. 14.9). CANON-Inter and CANON-Intra values in the radar table also deviate substantially from the main tables. The paper says the chart visualizes "average performance of the two scenarios" and uses a "scale from 0 to 100," but no normalization or transformation is described. This makes the figure misleading and undermines trust in the presentation of results. The authors should clarify what the radar values represent or correct them to match the reported accuracy.

- **No measure of variance or statistical significance.** All results are reported as point estimates without standard deviations, confidence intervals, or number of seeds. RL training is inherently noisy, and several evaluation sets (AIME24, AIME25, AMC with 30–40 problems each) are small. A 5-point gain on AIME24 (30 problems) could be 1–2 problems. Without multiple trials or bootstrap estimates, the reader cannot assess whether the observed improvements are stable or within run-to-run variation. While single-seed reporting is common in this field, the paper's central claims would be substantially strengthened by at least a two-seed study or variance estimates.

### Minor

- **Scheduling strategy selection lacks a clean validation protocol.** The paper tries four scheduling strategies and reports the one that works best per model (Cosin-First-Inter-Later-Intra for Qwen-7B/Llama-8B, First-Inter-Later-Intra for Qwen-1.5B). This selection is informed by test-set performance, which constitutes a form of implicit overfitting. The absence of a held-out validation split or a pre-specified selection rule makes the reported gains for CANON-Dynamic difficult to interpret as unbiased. The authors should either fix a single schedule for all models or document a validation-based selection.

- **Only two of four scheduling strategies are shown.** The paper lists four strategies (*First-Inter-Later-Intra*, *First-Intra-Later-Inter*, *Cosin-First-Inter-Later-Intra*, *Cosin-First-Intra-Later-Inter*) but reports results only for the first and third in Table 2. The other two are never shown, even as negative results. Full transparency would require presenting all four or explaining why they were excluded.

- **Theoretical framing is limited.** Theorem 1 shows that the inter-group advantage can have larger magnitude than DR.GRPO when groups are equal-sized, but larger magnitude does not guarantee better credit assignment—it could equally amplify noise. Theorem 2 assumes independent conditions, which is unrealistic for real training dynamics. The theorems are algebraic identities rather than learning guarantees, and the paper's central premise ("amplify the impact of the target metric without presuming its direction") is not established by these results. A clearer presentation would move the theory to the appendix and focus the main text on intuition.

- **Different training data for Llama vs. Qwen models.** Qwen models use 45k prompts from OpenR1-Math-220k, while Llama3.1-8B uses a simpler 35k-sample mixture due to weaker capability. This means the cross-model generalization claim ("works across three models") does not control for data. Within-model comparisons (CANON vs. DR.GRPO for the same model on the same data) are valid, but the claim of architecture-agnostic effectiveness would be stronger if a common data condition could be established.

### Trivial

- **"Per-token generation entropy" is not formally defined.** The paper uses this metric for regrouping but never specifies how it is computed (e.g., average token log-probability, actual entropy of the next-token distribution). A brief formula would aid reproducibility.

- **Token-level advantage mapping is implicit.** Equations 3–5 include a token index \(t\) on the left-hand side, but the right-hand side depends only on response-level rewards and group means. The paper follows DR.GRPO where the advantage is constant across all tokens in a response, but this is never stated explicitly.

- **Typo in reference: "Aroca & Zanette" vs. "Arora & Zanette".** The paper correctly cites "Arora & Zanette" in the main text (lines 15, 36) but writes "Aroca & Zanette" in the baseline description (line 263). This should be harmonized.

## Nice-to-Haves

- An ablation varying group size (not just equal split) would validate the design choice motivated by Theorem 1.
- A "random grouping" control (grouping by a random metric) would help demonstrate that CANON's benefit comes from meaningful metric-based regrouping, not the regrouping operation itself.
- Code release (the paper states code is available; the repository could not be verified during review, but it was not a source of criticism in the reviews).
- The max-length reduction setup for Table 3 (max_length=3072 vs. 8192 in the main experiments) should be explicitly stated when reporting DR.GRPO baselines in that table.

## Removed Points

These points are flagged for removal from the original reviews. They should be treated with caution and not counted toward the paper's assessment:

- **"Inconsistent baseline numbers across tables"** (Harsh Critic). The critic claimed DR.GRPO numbers differ between Table 1 (53.8/17.2) and Table 2 (55.7/26.2). This is factually wrong: the critic confused **GRPO** (which has Acc=53.8, logic Acc=17.2 in Table 1) with **DR.GRPO** (which has Acc=55.7, logic Acc=26.2 in **both** tables). The DR.GRPO baseline is consistent. REMOVED — factual error.

- **"Different datasets for Llama" as a weakness for within-model claims.** The critic argued this makes cross-model comparisons uncontrolled. However, Table 2 compares each model's CANON-Dynamic against its own DR.GRPO baseline trained on the same data, not across models. The claim "works across three models" means the method benefits each model individually. The data difference is justified by Llama's weaker capability and does not invalidate within-model improvements. REMOVED — scope creep; does not harm the core claim.

- **"Aroca typo" as a weakness of substance.** This is a minor typographical inconsistency, not a scientific weakness. MOVED to Trivial above.

- **"The paper does not state whether baselines were retrained under reduced max length"** for Table 3. The paper states "We follow the training setups described in Section 5.1 and reduce the maximum response length to 3072" and "All these baselines are conducted with DR.GRPO," which implies retraining. The critic's uncertainty is addressed by context. MOVED to Nice-to-Haves as a clarificatory note.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two useful observations:
1. The hierarchical control over metric direction (Figure 5 showing monotonic entropy change with μ) is a clean empirical validation of the method's core design—this is stronger evidence for the method's mechanism than the theoretical theorems.
2. The efficiency results (Table 3, Figure 4) are arguably CANON's most practically significant contribution, yet the paper presents them as a secondary application. The reviews collectively missed the opportunity to highlight this as potentially more impactful than the accuracy gains.

## Suggestions

- Clarify or correct the radar chart (Figure 3) values. If they are normalized or computed differently from accuracy, state the transformation explicitly. If they are errors, align them with the main tables.
- Add at least one additional seed for the main comparisons (Tables 1–2) or provide bootstrap confidence intervals for the small evaluation sets (AIME24/25, AMC).
- Report results for all four scheduling strategies or explain why two were excluded.
- Fix the "Aroca" → "Arora" typo and add a brief definition for per-token generation entropy.
- Consider fixing the scheduling strategy across all models and reporting the test performance of that single strategy, rather than selecting per-model strategies, to avoid implicit overfitting concerns.

## Score and Decision

The paper proposes a conceptually clean and empirically effective method for incorporating training metrics into RLVR without directional bias. The main experimental results are convincing (consistent improvement across models, strong efficiency Pareto frontier), and the weaknesses are primarily in presentation and rigor (radar chart inconsistency, missing variance, scheduling selection). The radar chart issue is the most significant concern but does not invalidate the core claims, which are supported by the main tables. With clarifications and corrections to the visualization, the paper would be a solid contribution.

Score: 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>