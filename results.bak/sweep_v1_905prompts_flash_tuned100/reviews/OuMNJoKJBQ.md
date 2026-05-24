Now I have sufficient information for calibration. Let me write the final consolidated review.

**Calibration Summary:**

**Round 1 bracket:** The paper is clearly above the rejection-range anchors (1.4–3.0: jailbreak attack papers with minimal experimental substance) and well below the top-tier anchors (8.0–8.67: papers with strong theoretical foundations and polished presentation). Initial bracket: **4.5–7.5**.

**Round 2 narrowing anchors:**
- SafeDPO (6.40, Rejected) — most directly comparable (safety DPO). The paper under review has stronger motivation (causal probing) and more extensive experiments, but similar issues (small absolute improvements, missing efficiency analysis). Slightly stronger than SafeDPO.
- TPO (6.33, Accepted) — tree preference optimization for reasoning. Similar method+experiments structure. Paper under review has broader evaluation (multiple model families, attack categories) vs. TPO's single-family evaluation. Comparable quality.
- TIS-DPO (7.00, Accepted) — token-level importance sampling DPO. More rigorous theoretical derivation. Paper under review has broader scope (causal probing + CoT dataset + AW-DPO) but is less theoretically polished. Slightly weaker than TIS-DPO.
- 3D-Properties (6.25, Accepted) — analysis paper on DPO limitations. Different contribution type, similar quality tier.

**Final score:** 6.0 — the paper is comparable to mid-tier DPO variants. It has genuine contributions (causal analysis, CoT dataset, AW-DPO) and extensive experiments, but the main claim relies on probe-based evidence with behavioral results deferred to the appendix, and there are several presentation gaps (undefined α, no judge reliability analysis, no statistical tests).

---

## Summary

This paper argues that current LLM safety alignment is "superficial" — models learn shallow refusal heuristics rather than deep reasoning about harmfulness. The authors support this with a causal intervention: they use linear probing to identify reasoning-critical attention heads, deactivate them, and show that alignment probe accuracy stays near 100% while reasoning probe accuracy drops to chance. To address the problem, they construct and release a CoT safety fine-tuning dataset, then propose Alignment-Weighted DPO (AW-DPO), which decomposes each response into reasoning trace and final answer, computes separate DPO losses for each, and weights them by component-level harmfulness gaps. Experiments across LLaMA-3.2-3B, LLaMA-3.1-8B, and Mistral-7B-v0.3 show that AW-DPO achieves low ASR across five jailbreak categories while maintaining competitive utility on MMLU.

## Strengths

1. **Causal intervention evidence for the superficial-alignment hypothesis (Section 3, Figure 1).** The probe-then-prune experiment provides a novel empirical lens on why alignment fails: reasoning-critical neurons are causally separable from safety representations. This goes beyond prior speculation about shallow alignment by showing a specific, testable mechanism.

2. **AW-DPO with component-level weighting (Section 4, Equations 3–4, Figure 2).** The idea of decomposing the DPO objective into reasoning-trace and response-segment losses, weighted by their relative harmfulness gaps, is clean and well-motivated by the error analysis. The ablation (Figures 4b–4c) confirms that AW-DPO outperforms standard DPO on the same preference data, validating that the finer-grained signal matters.

3. **Comprehensive evaluation across models and attack categories (Tables 1–3).** The paper evaluates three model families (LLaMA-3.2-3B, LLaMA-3.1-8B, Mistral-7B-v0.3) across five distinct jailbreak categories with standard deviations, and compares against seven baselines including SAFECHAIN, RR, and STAIR. The transferability experiment (Table 3) showing that an AW-DPO dataset built on one model works across others is practically useful.

4. **Controlled comparison with reasoning LLMs (Section 5.3, Figure 3b).** The finding that Phi-4-Reasoning and Phi-4-Reasoning-Plus underperform AW-DPO on safety despite strong general reasoning scores cleanly demonstrates that general reasoning ability does not automatically translate to safety — motivating the need for alignment-specific reasoning training.

## Weaknesses

### Major

- **The causal intervention evidence is primarily about representation separability, not behavioral safety (Section 3).** The paper's central claim — that "current safety alignment is largely superficial and does not depend on deep reasoning" — is a claim about model *behavior* (i.e., actual refusal decisions). But the main experiment only shows that a linear probe for safe/unsafe representations retains near-100% accuracy even after reasoning-critical attention heads are pruned. A probe is a separate classifier trained post-hoc on the pruned representations; its accuracy remaining high does not directly imply that the model's *output-level* alignment behavior is independent of reasoning. The paper mentions behavioral evaluations on safety and reasoning benchmarks in Appendix D (stripped by the parser), and states they "support the same conclusion," but these results do not appear in the main text. The paper would be stronger by presenting the behavioral evidence prominently alongside the probe results, or by directly measuring whether refusal rates change under reasoning impairment.

### Minor

- **The scaling factor α is used in the ablation (Table 4) but never defined in the method section (Section 4).** The paper mentions "the importance scaling factor α" in Section 5.6 and varies it from 0.05 to 0.5 with stable results, but α does not appear in any equation in the method section. Readers cannot determine what α controls or how it relates to the weights in Equation (4). This is a missing detail that should be fixed.

- **No analysis of the judge model's reliability for harmfulness scoring (Section 4).** The entire AW-DPO pipeline depends on a judge LLM assigning harmfulness scores (h_rs, h_rp, h_f) to reasoning traces and response segments. The paper reports no agreement statistics, calibration analysis, or comparison with human judgments. Since the weights and preference pairs are built from these scores, the quality of the judge directly affects the method's validity.

- **No statistical significance tests for the main results (Table 1).** The ASR differences between AW-DPO and standard DPO are often small in absolute terms (e.g., 0.58% vs 1.04% on LLaMA-3.2-3B). While the standard deviations are reported, the paper does not test whether these differences are statistically significant. This matters because the improvements are small enough to fall within noise.

- **The 15% reasoning-misalignment claim is stated but not numerically substantiated (Section 4).** The paper says two failure modes account for "approximately 15% of all failure cases, as shown in Figure 3(a)," but Figure 3(a) is described as a grid-of-circles visualization, not a precise quantitative breakdown. A simple table with counts or percentages would substantiate this central motivation.

- **Utility comparison with STAIR-DPO-3 shows a large gap (Table 2).** STAIR-DPO-3 achieves 73.34% MMLU accuracy vs. 58.27% for AW-DPO (Base). The paper notes the higher training cost of STAIR-DPO-3, but the utility gap is substantial and deserves more discussion — for example, whether a fairer comparison (matching training rounds) would close this gap.

### Trivial

- None.

## Nice-to-Haves

- Evaluate utility on a broader set of benchmarks beyond MMLU (e.g., instruction-following, general QA) to ensure utility is not narrowly preserved.
- Report computational cost comparison between AW-DPO and standard DPO (the pipeline requires k candidate generations per prompt plus judge model scoring).
- Consider a behavioral version of the causal experiment: measure whether actual refusal rates change under neuron pruning, rather than only probe accuracy.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The AW-DPO formulation has an inconsistency between binary masks in Equation (3) and continuous weights in Equation (4)."** — Removed because the paper is clear: the binary masks in Equation (3) separate token types (reasoning vs. response) to compute separate rewards; the continuous weights in Equation (4) weight those two loss terms. These are distinct variables serving different purposes. No inconsistency exists.

2. **"The CoT dataset is not released for review, undermining reproducibility."** — Removed per hard rules: the paper provides an anonymous link. Criticizing the availability of cited datasets/repos is not permitted; the paper states the full dataset will be released upon acceptance.

3. **"The causal experiment 'is uninformative about behavioral safety' and 'does not support the claimed conclusion.'"** — Demoted from the critic's framing of a structural/fatal flaw to a Major weakness (see above). The probe evidence is informative but incomplete without the behavioral results (Appendix D), which the paper asserts exist and support the same conclusion. The criticism that the experiment "does not support the central claim" overstates the problem: the probe experiment provides representation-level evidence, and behavioral corroboration is referenced. The real issue is that the behavioral evidence should be in the main text.

4. **"The paper does not show that AW-DPO actually corrects the 15% reasoning-misalignment cases."** — Partially valid. The ablation (Figures 4b–4c) shows AW-DPO outperforms DPO overall, which is consistent with addressing those cases, but a direct error-type breakdown would strengthen the claim. Moved to Minor (merged with the 15% substantiation point).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Move the behavioral evaluation results (currently Appendix D) into the main text.** The causal intervention is the paper's headline finding; it should be supported by behavioral evidence (actual refusal rates under pruning), not just probe accuracy. If the behavioral results are in Appendix D, bring them forward.

2. **Define α in the method section and show where it enters the loss.** Readers should not have to infer what this hyperparameter controls from an ablation table. Even better, show the complete loss with α explicitly.

3. **Include a brief reliability analysis of the judge model.** Report agreement with human annotators on a held-out sample, or at minimum show that the judge scores are consistent (e.g., test-retest agreement).

4. **Add statistical significance tests or confidence intervals for the key ASR comparisons.** Given the small absolute differences, this would substantially strengthen the paper's claims.

5. **Provide a table with exact counts for the 15% reasoning-misalignment figure.** A simple breakdown of error types with numbers would make the motivation for AW-DPO more concrete.

## Score and Decision

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**