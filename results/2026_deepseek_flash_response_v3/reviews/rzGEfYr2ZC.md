## Summary

The paper proposes SparseFW, a layerwise LLM pruning method that relaxes the binary mask-selection problem to a convex program over the convex hull of binary masks and solves it via the Frank-Wolfe (FW) algorithm. The method is warm-started from a Wanda or RIA mask, fixes 90% of the highest-saliency weights (α=0.9), and applies FW to optimize the remaining 10%. Results show consistent per-layer reconstruction error reduction (20–80%) and consistent zero-shot accuracy gains across several modern GPT families, alongside a theoretical bound relating the relaxed-and-thresholded solution to the optimal binary mask.

## Strengths

1. **Convex relaxation + Frank-Wolfe is a principled departure from greedy heuristics that ignore weight interactions.** The paper shows (Section 2.1) that SparseGPT, Wanda, and RIA all solve per-weight subproblems that bypass weight interactions. SparseFW instead relaxes the binary mask constraint to its convex hull (Eq. 10, Figure 1), yielding a convex program that accounts for all weight interactions. Figure 2 verifies this translates to up to 80% per-layer reconstruction error reduction over Wanda, with average reductions of 20–40% across models — a concrete, measurable improvement in the local objective that greedy methods cannot achieve.

2. **Consistent zero-shot accuracy improvements across five model families and multiple sparsity regimes.** At 60% sparsity, SparseFW variants outperform their baselines on all 6 models (e.g., LLaMA-3-8B: 51.92% vs Wanda's 48.08%; Qwen2.5-7B: 61.13% vs 59.44%). At 2:4 sparsity, improvements are similarly consistent, spanning LLaMA 3, Gemma 2, Yi 1.5, DeepSeek, and Qwen 2.5.

3. **Transparent acknowledgment of the method's core limitation.** The paper explicitly states (Section 2.3) that α=0.0 (pure FW) "consistently yields worse results than the baselines" and that α=0.9 is required. It acknowledges the "local–global objective mismatch" in the conclusion (Section 5). This candor is a strength that contrasts with many papers that hide their method's limitations.

## Weaknesses

### Major

1. **The method cannot stand alone; it depends on the very baseline it frames itself as replacing.** Pure FW (α=0.0) produces *worse* perplexity than Wanda. The method only recovers when 90% of the mask is fixed to Wanda's decisions (α=0.9) and FW optimizes only the remaining 10%. This means SparseFW (Wanda) is structurally Wanda's mask on 90% of entries plus FW refinement on 10% — not an independent pruning method. The fact that pure FW degrades perplexity despite improving the local pruning objective reveals a fundamental local–global mismatch that the paper documents but does not resolve. The paper's framing (abstract: "drastically reduces the per-layer pruning error, outperforms strong baselines") oversells this; the primary contribution is a refinement step grafted onto existing heuristics, not a replacement for them.

2. **The theoretical guarantee (Lemma 1) bounds the gap in the *local* pruning objective, not the evaluation metrics.** The paper's own results show that improving the local objective does not reliably translate to better perplexity (α=0.0 yields the smallest local error but the worst perplexity). The theory therefore guarantees proximity to a quantity the paper itself demonstrates is misaligned with final performance. Moreover, the bound's thresholding error term depends on λ_max(Q) (not empirically evaluated) and large dimension products, leaving its practical tightness unclear.

### Minor

1. **Exclusion of SparseGPT limits the empirical claims.** The paper justifies this (line 192: SparseGPT "involves a reconstruction step"), but SparseGPT is the most widely-used LLM pruning method, and the abstract/intro reference it repeatedly. Without this comparison, readers cannot assess SparseFW's practical value relative to the dominant approach. Even a comparison restricted to mask quality (without SparseGPT's weight reconstruction) would strengthen the evaluation.

2. **Empirical perplexity gains are modest and inconsistent.** At 50% sparsity, SparseFW (Wanda) outperforms Wanda on 3 of 6 models, ties on 1, and underperforms on 2. At 60% sparsity on DeepSeek-7B, SparseFW (Wanda) has worse perplexity (11.99 vs 11.44). The strongest gains appear at higher sparsity and for zero-shot accuracy, but the compute cost is substantial (2000 FW iterations per layer), and no cost-benefit analysis is provided.

3. **No wall-clock time or FLOPs comparison.** The paper acknowledges SparseFW is "more compute-intensive" (line 240) but provides no quantitative comparison. For a 7B model with ~60 linear layers at 2000 iterations each, the overhead is non-trivial and should be contextualized.

4. **Standard deviations omitted** (line 208). Given the small gaps in many configurations, this makes it impossible to assess statistical significance.

### Trivial

None.

## Nice-to-Haves

- An ablation isolating FW's marginal contribution: compare SparseFW (α=0.9, Wanda warmstart) against a control that also fixes 90% of Wanda's weights but resolves the remaining 10% via a simpler method (e.g., remaining Wanda scores or random selection). This would disentangle the effect of FW optimization from the effect of the pre-fix.
- Analysis of where the local–global mismatch occurs: at which layers and for which weight types does improving the local objective hurt perplexity?

## Removed Points

- **Factual error about LLaMA-3.1-14B at 60%:** The harsh critic claimed SparseFW (Wanda) "underperforms" Wanda on this configuration (10.28 vs 10.87). The table shows SparseFW achieves 10.28 vs Wanda's 10.87 — lower perplexity is better, so SparseFW outperforms. Removed as factually wrong.
- **Missing appendix content:** The harsh critic complained the appendix (α ablation) is not in the review copy. This is a parser artifact; the appendix exists in the original submission. Removed per hard rule.
- **Speculative bound vacuity:** The harsh critic's calculation that the bound is "vacuous" depends on unknown λ_max(Q) values and is somewhat speculative. The milder version (bound's practical tightness is unclear) is retained in Major weakness 2.
- **Uniform sparsity allocation disadvantaging SparseGPT:** Speculative, as SparseGPT was not included. Removed.
- **Strength Finder's generic strengths** about "addressing an important problem" etc. were already filtered out of the draft.

## Novel Insights

The most interesting observation emerging across the reviews is the asymmetry between the local pruning objective and global perplexity: SparseFW's pure form (α=0.0) demonstrably *improves* the local reconstruction error but *worsens* perplexity. This is a clean empirical demonstration that the layerwise pruning objective is misaligned with the actual metric of interest — a finding that is arguably more significant than the incremental gains of the α=0.9 variant. The paper's own Figure 4 reinforces this by showing the thresholded mask's error reduction plateaus well below the continuous mask's. This suggests that the core challenge in LLM pruning is not solving the local combinatorial problem more accurately, but rather bridging the gap between local and global objectives — a direction the paper identifies but does not pursue.

## Suggestions

1. **Add a SparseGPT comparison.** Even without SparseGPT's reconstruction step, compare mask quality and final perplexity. This is the single most impactful addition for the empirical evaluation.
2. **Analyze the local–global mismatch directly.** Identify layers/weight types where improving the local objective hurts perplexity. This could yield insights more valuable than additional benchmarks.
3. **Ablate the marginal contribution of FW.** Compare α=0.9 with FW against α=0.9 with a simpler resolver (e.g., greedy on remaining weights) to isolate what FW specifically contributes.
4. **Report wall-clock time.** Even a rough comparison (e.g., "SparseFW takes X hours for a 7B model vs Y minutes for Wanda") would help readers assess the cost-benefit tradeoff.

## Score and Decision

**Calibration anchor comparison:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| FASP (f4b0YVwKUO) - structured pruning | 4.00 | R1 | SparseFW has more algorithmic novelty but a more severe structural flaw |
| SparsitySolver (zZU69H8tcr) - RL pruning | 3.75 | R1 | SparseFW is better written and more clearly motivated |
| FISTAPruner (BINwUtUGuq) - convex opt pruning | 5.25 | R2 | FISTAPruner has stronger empirical results (5% gains on 70B, SparseGPT comparison) and works standalone |
| PGZ (IU4L7wiwxw) - gradient pruning | 4.50 | R2 | Comparable; PGZ has better empirical scope but writing issues; SparseFW has a more fundamental dependency |
| RIA (Tr0lPx9woF) - pruning metric | 6.50 | R1 | RIA is a standalone method with no dependency issue; SparseFW is clearly weaker |

**Round 1 bracket:** 4.0–5.5
**Round 2 narrowing:** SparseFW sits near the lower end of the bracket, comparable to PGZ (4.50) but somewhat weaker due to the structural α=0.9 dependency. It is clearly below FISTAPruner (5.25), which has stronger empirical results, compares against SparseGPT, and does not require grafting onto baselines. It is above FASP (4.00) and SparsitySolver (3.75) due to its more principled approach, stronger theory, and clearer writing. The paper has a genuinely novel core idea (convex relaxation + FW for mask selection), well-articulated methodology, and honest limitation disclosure, but the α=0.9 dependency is a significant weakness that limits the contribution's practical value.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>