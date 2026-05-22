Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper proposes CANON (Conditional Advantage Estimation), a modification to GRPO-style advantage estimation for RLVR in LLMs. Instead of computing advantages over all sampled responses, CANON regroups responses into two equal-sized groups based on an auxiliary metric (entropy or length), then computes inter-group and intra-group advantages. This allows the model to leverage the metric's trend (e.g., lower-entropy responses are more accurate) without imposing a hard directional prior (higher-is-better or lower-is-better). Experiments on three LLMs (1.5B–8B) across six math benchmarks and three complex logic subsets show that CANON-Inter (favoring inter-group comparison) improves math accuracy, CANON-Intra improves complex logic accuracy, and CANON-Dynamic (scheduling between the two) achieves balanced gains. CANON also shows favorable token efficiency when applied to response length.

## Strengths

- **Novel, principled approach to incorporating auxiliary metrics without directional priors.** The core idea—splitting sampled responses into two groups by a metric and computing separate inter/intra advantages—is clean and well-motivated. Unlike prior methods that add handcrafted penalty/reward terms (e.g., Length Reward +/*, Entropy Adv) with brittle assumptions about higher/lower being better, CANON naturally lets the reward signal determine which metric trend is beneficial. The theoretical analysis (Theorems 1–2) formalizes that this provides selective amplification of the grouping metric without amplifying independent factors, supported empirically by the Numerical Scaling ablation in Table 4.

- **Consistent empirical gains across models and task types.** Table 1 shows CANON-Inter (entropy) improving average math accuracy by +1.9 points over DR.GRPO (57.6 vs 55.7) on Qwen2.5-Math-7B, with a notable +5.0-point gain on AIME24. CANON-Intra (entropy) achieves a +5.2-point improvement on the most complex logic subset (XLarge). Table 2 demonstrates that CANON-Dynamic outperforms DR.GRPO across all three tested models (Qwen2.5-Math-7B/1.5B, Llama3.1-8B) on both math and logic simultaneously—e.g., Llama3.1-8B logic accuracy improves from 14.9% to 18.9%.

- **Training dynamics analysis validates the mechanism.** Figures 2 and 5 show a clear, hierarchical relationship between μ (the inter/intra balance) and entropy trends, confirming that CANON controls metric trends as intended. Figure 6 provides a concrete behavioral explanation: CANON-Dynamic simultaneously achieves positive "gain from rethinking" (like CANON-Intra) and high training reward (like CANON-Inter), linking the scheduling strategy to the observed performance.

- **Strong token efficiency results.** CANON-Eff achieves a Pareto frontier that dominates all baselines (Clip Length, Length Reward +/*) in the performance–cost trade-off (Figure 4c). At α=0.96, it reduces token consumption by 26.3% over DR.GRPO with only 0.4-point accuracy drop. At α=0.88, it achieves 2.63× higher performance at low token budgets compared to Length Reward (*), at 45.5% fewer tokens—a practically meaningful result.

## Weaknesses

### Major

- **Single-run evaluations with no variance estimates.** All results in Tables 1–3 are reported as single points with no standard deviations, confidence intervals, or multiple seeds. For 7B-parameter model training, run-to-run variance is non-negligible. The headline improvements are modest in some cases (+1.9 points on math, +3.0 points on logic scheduling), and without variance estimates the reader cannot assess whether these are genuine effects or within noise. This is the single most important experimental omission—it weakens confidence in every empirical claim.

- **Scheduling strategy selection leaks test information.** Section 5.2 states: "We try four scheduling strategies… The shown results of CANON-Dynamic are derived from one of the tried scheduling strategies that achieve strong performance in both scenarios." Different strategies are selected for different models (Cosine for Qwen-7B and Llama-8B, First-Inter-Later-Intra for Qwen-1.5B). This constitutes hyperparameter selection using the full evaluation results, without a held-out validation set. The CANON-Dynamic results in Table 2 and Figure 3 are therefore compromised—one cannot distinguish genuine improvement from selection bias. The paper frames this as "a specifically designed strategy is acceptable for better performance in practice," but this is not a substitute for proper held-out evaluation.

- **Radar chart values are inconsistent with Table 2.** A side-by-side comparison reveals discrepancies between the radar chart's numerical table (Figure 3 embedded table) and Table 2. For example, Table 2 reports Qwen-7B DR.GRPO math=55.7, logic=26.2; the radar chart table reports math=57.6, logic=39.2. For CANON-Dynamic, Table 2 reports math=56.7, logic=29.2; the radar chart reports math=45.0, logic=45.0. The radar chart uses an unexplained different scale or normalization. This is confusing and undermines the credibility of the visual comparison. The paper must explain what the radar chart numbers represent or correct them.

### Minor

- **Figure 5 caption mislabels μ values.** The caption states "mu=0.5 (CANON-Intra)" and "mu=0.3 (DR.GRPO)." From the paper's own definitions: μ=0.0 = CANON-Intra, μ=0.5 = DR.GRPO, μ=1.0 = CANON-Inter. The caption is therefore wrong on both counts. This appears to be more than a formatting artifact—it reflects a genuine labeling error that could confuse readers about which setting produces which behavior.

- **Theoretical support is narrower than claimed.** Theorem 1 shows that CANON-Inter has larger magnitude than DR.GRPO under equal-sized groups, but as the reviewer correctly notes, magnitude amplification alone could be achieved by scaling the advantage (which the paper acknowledges and addresses in Table 4). Theorem 2 (selective amplification) is more substantive but relies on an independence assumption unlikely to hold between real metrics (e.g., length and entropy are correlated in practice). The theoretical contribution would benefit from acknowledging these limitations.

- **Notation inconsistencies and missing details.** (a) Eq. (1) defines $\text{clip}_1^b(x) = \max(\min(x, a), b)$ with mismatched parameters a/b vs the literal call $\text{clip}_1^{1+\varepsilon}$. (b) Eq. (3) uses $G_q^+$/$G_q^-$ while Section 4.1 defines $C_q^+$/$C_q^-$. (c) Tie-breaking for discrete metrics (e.g., when many responses have equal length) is not specified—since groups must be equal-sized for Theorem 1's guarantee, ties can affect the split and thus the advantages. (d) The "gain of rethinking" metric in Figure 6 is mentioned but not formally defined.

- **Efficiency comparison omits the simplest baseline.** The paper does not compare against a baseline that trains with DR.GRPO and then truncates responses at test time to match token budgets. This zero-cost baseline would help isolate whether CANON's efficiency gains come from the training procedure or simply from producing shorter responses that could be obtained through post-hoc truncation.

### Trivial

- The abstract's mention of "DeepSeek-R1 and OpenAI-o1" is gratuitous—the paper evaluates on 7B-scale models, not frontier systems.

## Nice-to-Haves

- Reporting results with at least 3 random seeds (or at minimum acknowledging single-run limitations) would substantially strengthen the paper.
- A held-out validation set for scheduling strategy selection, or cross-validation, would resolve the overfitting concern.
- A formal definition of the "gain of rethinking" metric used in Figure 6 would aid reproducibility.
- The rope theta modification for context extension (10000 → 40000) is a change from the base model—its independent impact on reasoning quality could be briefly discussed or ablated.

## Removed Points

- *"Proof cannot be verified (appendix removed)"* — Removed per policy: the parser strips appendices from all papers; they exist in the original submission.
- *"The dramatic improvement for Llama-8B from 22.6 to 35.2 on math (Table 2) is especially suspicious; it likely stems from a lucky configuration"* — Removed because the 35.2 value comes from the radar chart (which uses an unexplained scale), not from Table 2. Table 2 shows Llama-8B math improving from 22.0 to 22.6. The specific numerical claim is factually inaccurate.
- *"No rationale for 45k dataset size"* — Removed as a generic nitpick; 45k is a standard subset size and the paper explicitly cites its source.
- *"The paper should not be accepted in its current form"* — This is an overall assessment, not a specific weakness.
- Several speculative criticisms from the harsh critic about confounders and potential hidden assumptions were removed because they lacked concrete textual anchors in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an angle or implication that the paper itself fails to address.

## Suggestions

1. **Add multi-seed results** to Tables 1–3 (or clearly state the compute constraints and discuss potential variance). Even 2-3 seeds with mean ± range would significantly strengthen the empirical claims.
2. **Use a held-out validation set** for scheduling strategy selection in Section 5.2, or reframe CANON-Dynamic as an exploratory result requiring further validation.
3. **Reconcile the radar chart numbers** with Table 2. If the radar chart uses a different normalization/scale, explain it explicitly.
4. **Fix the Figure 5 caption** (mu=0.5 should be DR.GRPO, mu=0.0 should be CANON-Intra, mu=1.0 should be CANON-Inter) and correct the notation inconsistencies in Eq. (1) and (3).
5. **Specify tie-breaking** for the regrouping step when responses have equal metric values (particularly for discrete metrics like length).
6. **Define the "gain of rethinking" metric** formally.

## Score and Decision

The paper presents a novel, well-motivated method with strong empirical evidence across multiple models and tasks. The core idea is clean and the supporting analysis (dynamics, reflection gains, ablation vs. numerical scaling) provides reasonable evidence for the claimed mechanism. The weaknesses are real but addressable: the scheduling overfitting concern primarily affects the CANON-Dynamic results (Table 2, Figure 3), while the main CANON contribution (Table 1 with fixed μ) and the efficiency results (Table 3) are less impacted. The single-run limitation is the most significant across-the-board weakness and should be addressed in a revision. On balance, the contribution is solid and the paper provides sufficient evidence of effectiveness to warrant acceptance with revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>