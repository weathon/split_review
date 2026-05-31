Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

UNComp proposes using matrix entropy (effective rank) to measure uncertainty across layers and heads in LLMs, enabling adaptive, non-uniform compression of both hidden states (for prefilling speedup) and KV cache (for memory reduction). Layers and heads are grouped by their truncated effective rank, and different token budgets are assigned accordingly — deeper layers receive more compression, while higher-rank heads retain more tokens. The method is training-free and uses a small calibration set (Wikitext2) to determine groupings. Experiments on LongBench and needle-in-a-haystack across Llama2, Llama3, and Mistral show competitive results at aggressive compression (4.74%–9.38% of original KV size), including a 1.6× prefilling speedup and 6.4× throughput improvement.

## Strengths

- **Prefilling-stage speedup via hidden-state compression before KV generation.** Unlike existing eviction methods (H2O, SnapKV, PyramidKV) that compress only the KV cache after it is built, UNComp compresses hidden states during prefilling, yielding a verified 1.58× speedup (Table 5: 48.78s vs 77.34s on A100). This is a clear and well-supported concrete advantage.

- **Effective extreme compression via non-uniform head allocation.** Table 2 shows that at very small token budgets (e.g., 12 tokens per head in the low-rank group), UNComp achieves an average score of 26.08 vs 22.06 for the best baseline (PyramidKV at KV size=64). Additionally, removing up to 4 heads (Ours-delete-4-heads: 27.05) still substantially outperforms baselines at the same total budget. This provides strong evidence that the effective-rank-based grouping identifies genuinely expendable heads.

- **Training-free and calibration-light.** The entire grouping procedure uses a single pass on Wikitext2 without gradient updates or fine-tuning. This is a practical advantage over GQA, MLA, and LoRA-based approaches that require retraining.

## Weaknesses

### Fatal
None.

### Major

1. **Missing uniform-head ablation — the core claim is not causally isolated.** The paper's central contribution is that effective-rank-guided non-uniform head allocation improves over uniform compression. Yet no experiment compares UNComp against a version that distributes the *same total KV budget uniformly across all heads*. Without this ablation, the observed gains could stem from other components (the specific eviction policy, the recent-token ratio tuning, or simply using a larger budget for some heads regardless of how they are selected). This is the single most important missing experiment.

2. **No statistical significance or variance reporting.** Every table reports single numbers. Given the small performance margins (often 1–2 points) and the inherent randomness in LLM generation, the ranking could flip with multiple runs. For example, in Table 1, Ours-group (32.57) vs SnapKV (31.94) and PyramidKV (31.81) on Llama2-7B is a ~0.6–0.8 point gap — well within the range that variance could affect. The paper states "confirmed by averaging multiple repeated experiments" (line 326) but never reports the actual variance or number of runs.

3. **Method hyperparameters are under-specified, harming reproducibility.**  
   - The threshold ε in Eq. 4 (how much effective rank must decrease to trigger a new compression stage) is never stated or ablated.  
   - The "elbow point" for selecting top-k eigenvalues (Eq. 7–8) is referenced without operational definition (knee-of-curve heuristic? fixed variance threshold?).  
   - The number of layer groups C and head groups m (reported as 5 and 2 in experiments) is stated as determined by the effective rank distribution, but no procedure is given for setting them automatically.  
   - The H/R ratio selection (Section 4, paragraph "The Ratio of Recent Tokens…") introduces an additional tuning step using Pearson correlation on calibration data — its sensitivity is not evaluated.

### Minor

1. **Needle-in-a-haystack claim is overstated.** The headline result (98.80 vs 98.70 on Llama2-4k, Table 6) is a 0.1-point difference with no variance reported, and on Llama3-8k UNComp is *below* FullKV (83.73 vs 84.99). The abstract and conclusion state that UNComp "surpasses the performance of the full-size KV cache," but this is supported by only one model and one tiny margin that could be noise.

2. **Indexing error in the head context size formula.** The formula for head-level context sizes (§3.3, Eq. 13) reads: \(S_{i,h} = S_{i,h-1} - (h-1) \cdot \Delta s_h\). This produces a quadratic (accelerating) decrease — steps of Δs_h, 2·Δs_h, 3·Δs_h — rather than the "fixed step size applied between consecutive groups" stated in the text (line 200). It should be either \(S_{i,h} = S_{i,1} - (h-1) \cdot \Delta s_h\) or \(S_{i,h} = S_{i,h-1} - \Delta s_h\). Since the actual implementation cannot be verified, this is at minimum a presentation error.

3. **"Sustain a high level of accuracy" is an overstatement for extreme compression.** The paper claims (line 396) that "our methodology can sustain a high level of accuracy relative to the full KV cache size when only 12 tokens are preserved." FullKV average is 30.54 vs Ours-remain-tokens-12 at 26.08 — a 14.6% loss. While 26.08 is better than baselines at larger budgets, "sustain a high level" is not accurate for a 15% drop.

4. **No sensitivity analysis for any hyperparameter.** The method introduces ε, Δs_h, number of groups (C, m), the elbow criterion threshold, and the H/R ratio — none are ablated. Even a brief analysis on one dataset would improve confidence.

### Trivial
- The naming "Ours-group-stage" vs "Ours-group" is ambiguous; clearer names (e.g., "UNComp (KV+HS)" vs "UNComp (KV)") would help.
- The throughput comparison (Table 5 caption vs text) uses a prompt+generation length of 2048+8096 stated only in prose (line 430), not in the table.

## Nice-to-Haves
- **Disentangle contributions**: An ablation removing individual components (effective-rank grouping, per-group budgets, attention-score eviction, H/R ratio tuning) would clarify what drives performance and would strengthen the paper significantly.
- **Calibration overhead**: The paper uses Wikitext2 for calibration but does not report how many tokens/sequences are needed or how long the preparation stage takes. This is a one-time cost but should be quantified.
- **Show effective-rank groupings are not a proxy for simpler statistics**: Compare UNComp's groupings against groupings based on cumulative attention entropy or other simple metrics to demonstrate that matrix entropy provides non-redundant information.

## Removed Points
These points were removed from the main review with justification:
1. **"Inconsistent compression direction for layers vs heads"** (Harsh Critic, Critical Issue 1) — The paper explicitly defines "compression rate" as "compressed size over original size" (line 26). Under this definition, "lower compression rate for layer" = smaller ratio = more compression (consistent with deeper layers getting smaller contexts) and "higher compression rate for head" = larger ratio = less compression (consistent with higher-rank heads keeping more tokens). The paper is internally consistent; the criticism stems from a different interpretation of the term.
2. **"CHAI comparison is unfair"** (Harsh Critic, Critical Issue 2) — The asymmetry favors CHAI (77.54% ratio, i.e., much less compression) over UNComp (9.38% ratio). Per the rules, when a comparison asymmetry favors the baseline, the criticism is removed. The paper also explicitly acknowledges the different compression ratios in the table header and caption.
3. **"Overclaimed needle-in-a-haystack"** — Retained in weakened form as a Minor weakness (point 1 above) rather than a Critical Issue, since the paper's claim is limited ("specific needle-in-a-haystack tasks") and the difference is factual, just not statistically supported.
4. **Generic reproducibility nitpicks** about trivial implementation details (e.g., calibration dataset dependence, complete training logs) — removed as insubstantial.
5. **Strength about "outperforms full KV cache on needle-in-a-haystack"** — removed because it conflicts with the verified weakness (marginal/no variance). The strength is weak evidence at best.

## Novel Insights
None beyond the paper's own contributions. The two novel observations — that deeper layers (higher effective rank) can tolerate more compression while higher-rank heads need less compression, and that effective rank can be measured without data dependence — are the paper's own contributions and are well articulated.

## Suggestions
1. **Add a uniform-head ablation**: Use the same total KV budget as UNComp but distribute it uniformly across all heads. Compare to UNComp's non-uniform allocation. This directly tests whether effective-rank-guided allocation is the source of improvement.
2. **Report variance**: Run key experiments (especially needle-in-a-haystack and LongBench average) with 3–5 seeds or calibration splits. Report standard deviations to establish that the margins are meaningful.
3. **Specify all hyperparameters**: State ε, the elbow criterion (operationally defined), and how C and m are determined from the effective rank distribution. Add a brief sensitivity analysis.
4. **Fix the indexing error**: Correct Eq. 13 to \(S_{i,h} = S_{i,1} - (h-1) \cdot \Delta s_h\) (or \(S_{i,h} = S_{i,h-1} - \Delta s_h\)) to match the stated linear decrease.

## Score and Decision

The paper presents a well-motivated, training-free compression method with a principled information-theoretic basis. The prefilling speedup and extreme-compression results are genuine contributions. However, the absence of a uniform-head ablation leaves the core claim incompletely supported, and the lack of variance reporting makes the small-margin comparisons uncertain. These are fixable but non-trivial gaps. The paper should be considered for acceptance contingent on addressing the major weaknesses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>