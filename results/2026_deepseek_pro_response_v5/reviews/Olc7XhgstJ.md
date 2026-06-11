Now I have a thorough calibration. Let me write the final review.

## Calibration Summary

**Round 1 — Bracketing:** Initial bracket identified as roughly 5.0–7.0 based on comparison against anchors across all score bands.

**Round 2 — Narrowing:** Retrieved 6 anchors inside the bracket:

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| SCDPO (ZRDa2IT1sQ) | 6.00 | Reject | ST is stronger — OOD eval, 3 model scales, clearer motivation |
| Evo-Step (aapUBU9U0D) | 5.50 | Reject | ST is stronger — more general method, better empirical coverage |
| TypedThinker (VIUisLx8lQ) | 6.00 | Accept | Comparable — ST has broader experiments, TypedThinker more creative angle |
| 3D-Properties (9Hxdixed7p) | 6.25 | Accept | Different category (analysis paper), hard to compare |
| TPO (O0sQ9CPzai) | 6.33 | Accept | ST has better empirical coverage; TPO has more method complexity |
| D2PO (OspqtLVUN5) | 6.25 | Accept | D2PO has major novelty concerns; ST has genuine novelty but missing key baseline |

ST is clearly stronger than SCDPO (6.00) and comparable to or slightly below TPO (6.33). The missing SimPO baseline is the key limiting factor. Final score: **6.0**.

---

## Summary
This paper identifies "under-thinking" in Large Reasoning Models — the tendency to switch reasoning trajectories too frequently, abandoning promising thoughts before reaching a correct answer. The proposed Steady Thought (ST) framework operates in three stages: entropy-based thought segmentation, forced completion of each thought via logit suppression of switch-trigger tokens, and thought-level preference optimization (STPO) that treats the completed thought as "chosen" and the wasteful continuation as "rejected." Experiments across three model scales (1.5B, 8B, 14B) and four datasets show accuracy gains up to 5.3% with token reductions of 19–39%, including out-of-distribution generalization to code generation.

## Strengths
- **Principled problem formulation**: The paper casts under-thinking in a Bradley-Terry preference framework (Section 2.1, Eq. 2), providing a clean theoretical foundation that connects an empirically observed failure mode to a well-understood optimization paradigm.
- **Thought-level granularity is the key insight**: Rather than treating entire reasoning chains as monolithic preference pairs, ST constructs preference pairs at the precise divergence point — the committed completion of thought T_i (chosen) vs. the wasteful switch thoughts (rejected) — providing targeted supervision at the critical juncture where under-thinking occurs (Section 3.3, Eq. 7).
- **Consistent accuracy gains with token reduction across diverse models**: Table 1 shows ST simultaneously improves accuracy (by 1.9%, 3.12%, and 2.52% on average for 1.5B, 8B, and 14B models respectively) while cutting output length by 24.9%, 25.5%, and 17.3%. These results hold across MATH-500, AIME 2024, GSM8K, and LiveCode.
- **Out-of-distribution generalization to code**: Despite training exclusively on math data (omni-math), ST improves LiveCode accuracy by 5.3% (Qwen3-8B) and 4.2% (14B) with token reductions, suggesting transferable reasoning discipline rather than dataset-specific shortcuts.
- **Multi-angle behavioral analysis triangulates the effect**: Reduced response length, fewer thoughts per response, larger proportion of final thought (Figure 2), and decreased proportion of correct intermediate thoughts (Table 2) collectively support the claimed mechanism.
- **Entropy-based segmentation is principled and tunable**: Using token-level entropy spikes to detect thought switches is computationally lightweight and theoretically grounded, with hyperparameter sensitivity analysis provided (Table 3).

## Weaknesses

### Fatal
None.

### Major
- **Missing response-level SimPO baseline leaves the core contribution unisolated**: The central novelty claimed for ST is thought-level granularity in preference optimization. Yet the training-method ablation (Table 4) compares STPO only against SFT and DPO. The paper itself explains (Section 5.2) that DPO struggles with large length disparities between chosen and rejected responses — and in ST's data, rejected responses are systematically much longer than chosen ones. STPO's loss (Eq. 7) is structurally identical to SimPO (Eq. 3) with the prompt extended to include the thought prefix. A response-level SimPO baseline (same preference pairs, same data, applied to the full response rather than at thought boundaries) would directly isolate whether thought-level conditioning drives the observed gains, or whether length normalization alone accounts for the DPO→STPO improvement. Without this comparison, the paper's headline contribution — that thought-level granularity specifically mitigates under-thinking — is asserted but not conclusively demonstrated.

### Minor
- **PCT metric conflates genuine reduction in wasteful switching with mechanical effect of fewer total thoughts**: The paper argues that lower Proportion of Correct intermediate Thoughts (PCT) after ST training indicates fewer "invalid switches" (Section 4.4.2). However, ST demonstrably reduces total thought count per response (Figure 2). When the total thought count shrinks, thoughts previously classified as "intermediate" can become "final" under ST, mechanically reducing PCT without necessarily reflecting fewer abandoned correct thoughts. For example, if the vanilla model produces correct thought A, switches to incorrect B, then correct final C — A counts toward PCT. Under ST, the model might commit to A and finish, making A the final thought and contributing zero to PCT. The analysis should control for changes in total thought count.
- **Unresolved tension between NOWAIT failure and ST's Thought Completion stage on Qwen3-8B**: ST's Stage 2 uses logit suppression on the same switch-trigger tokens ("wait," "alternatively") that NOWAIT suppresses. On Qwen3-8B, NOWAIT causes a 21-point accuracy collapse and 85% token explosion (Table 1). While ST applies this suppression only during training data generation (not at inference time), the paper never discusses whether the completions generated via this suppressed decoding are of acceptable quality for this model, or acknowledges this tension.
- **Training details are sparse**: The number of training problems sampled from omni-math, hyperparameters (β, γ, learning rate, number of epochs), and the yield of valid preference pairs are not specified in the main text, affecting reproducibility.
- **No error bars or variance estimates**: Accuracy numbers in Table 1 are reported without standard deviations or confidence intervals. For AIME 2024 (only 30 problems), even with 8-run averaging, the confidence intervals on differences of ~3 percentage points would be wide.
- **Entropy threshold tuning shown only for 1.5B model**: Section 4.4.3 reports tuning for DeepSeek-R1-Distill-Qwen-1.5B only, with results for 8B and 14B deferred to Appendix D (stripped). Given the sensitivity observed (threshold 3.2 drops AIME accuracy from 31.2% to 28.3%), per-model tuning is a relevant detail.

### Trivial
- **"Overall" column in Table 1 is a simple unweighted average** across datasets of vastly different sizes (30 to 1319 problems). A micro-average or weighted average would be more informative.

## Nice-to-Haves
- A breakdown by problem difficulty or by whether the first thought was correct would strengthen the claim that ST is selective rather than globally converging to shorter responses.
- Discussion of the computational cost of Stage 2 (Thought Completion), which requires n separate forward passes per training problem for n thoughts.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic claimed the Table 4 ablation is "confounded"**: This overstates the issue. The comparison against DPO and SFT is valid and informative; the gap is the missing SimPO baseline, not that the existing comparisons are invalid.
- **Harsh Critic criticized the Bradley-Terry formalism as "more ornate than functional"**: This is a stylistic preference, not a substantive weakness. The formalism provides clear notation for the subsequent method and connects the problem to a known optimization framework.
- **Harsh Critic claimed behavioral metrics (Section 4.4.1) are "merely downstream consequences of the training objective"**: While partially true, these metrics serve as sanity checks that the training had the intended behavioral effect, which is a standard and valid use of such metrics. The paper uses multiple metrics to triangulate.
- **Harsh Critic's criticism about the anomalous AIME case (1.5B thought count increase) receiving a "post-hoc explanation"**: The paper acknowledges this anomaly and provides a plausible explanation (Section 4.4.1, line 219: "when smaller models tackle high-difficulty problems, they tend to increase the frequency of thought transitions to find the optimal solution"). This is a reasonable observation, not an evidential flaw.
- **Strength Finder's claim about Table 4 ablation being "compelling evidence that STPO is necessary and not trivially replaceable"**: Softened because the missing SimPO baseline limits how conclusive the ablation is.
- **Criticism about the "Acc[%]↓" column header using a down arrow**: This is a formatting artifact/nitpick removed per hard rules.
- **Harsh Critic's concern about computational cost of Stage 2**: Moved to Nice-to-Haves since the paper acknowledges this in Appendix E (stripped).
- **Request for error bars / confidence intervals**: Kept as Minor since this is a reasonable concern for small test sets like AIME (30 problems), but noted that single-run evaluation is common in this area.

## Novel Insights
The paper's formulation of under-thinking through the lens of preference optimization at thought boundaries is genuinely novel. Rather than globally suppressing switching behavior (as prior work does), ST localizes the preference signal to the exact point where the model faces the commit-vs-switch decision, conditioned on the specific intermediate thought. This framing — that under-thinking can be addressed not by eliminating switching but by teaching the model when to commit — represents a conceptual advance over prior suppression-based approaches. The OOD generalization to code generation despite math-only training further suggests ST teaches a transferable meta-skill rather than dataset-specific heuristics.

## Suggestions
- Add a response-level SimPO baseline to Table 4. This is the single highest-impact experiment: it would directly test whether thought-level granularity (the paper's core claimed contribution) matters beyond length normalization.
- Restructure the PCT analysis to control for total thought count, e.g., report the proportion of correct thoughts that were subsequently abandoned normalized by total correct thoughts, or directly count "invalid switches."
- Discuss the NOWAIT/Thought Completion tension for Qwen3-8B, or report the quality of completions generated during Stage 2 for that model.
- Report training hyperparameters (β, γ, learning rate, epochs, number of training problems) in the main text or a clearly referenced appendix section.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>