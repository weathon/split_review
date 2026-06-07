Now I have enough information for calibration. Let me write the final review.

## Summary

This paper proposes SparseFW, a method that relaxes the binary mask selection problem in layer-wise LLM pruning to a convex program (L1-constrained continuous mask) and solves it with the Frank-Wolfe (FW) algorithm. The core idea is principled: instead of greedy heuristics that prune one weight at a time and ignore interactions, SparseFW optimizes over the convex hull of all feasible masks. The authors provide a theoretical error bound, a memory-efficient implementation, and empirical results on five LLM families at multiple sparsity levels.

## Strengths

1. **Convex relaxation framework for LLM mask selection is well-motivated and novel.** Unlike Wanda, RIA, and the mask-selection component of SparseGPT—which all make greedy decisions per weight—SparseFW solves a convex program that accounts for weight interactions in the local pruning objective. Figure 2 confirms that this yields per-layer reconstruction error reductions of up to 80% relative to the Wanda warm-start.

2. **Clean derivation linking Wanda and RIA to greedy single-weight optimization (Section 2.1).** The paper shows that Wanda's saliency score \( |W_{ij}| \|X_{j,:}\|_2 \) arises naturally from a greedy one-step pruning of the quadratic objective (Equation 5), and that RIA applies the same logic to a rescaled weight matrix. This is a genuine conceptual contribution to understanding why these heuristics work.

3. **First theoretical guarantee for the LLM mask selection problem.** Lemma 1 provides an explicit error bound decomposing the gap to the optimal combinatorial mask into an optimization term (vanishing as \(k/T\)) and a thresholding term. No competing mask-selection method (Wanda, RIA) offers any such guarantee.

4. **Memory-efficient gradient computation.** By precomputing \( G = XX^\top \) (a \( d_{in} \times d_{in} \) matrix), the per-iteration cost is independent of the number of calibration samples and sequence length, which is critical at LLM scale.

5. **Consistent zero-shot accuracy improvements across most model/sparsity combinations.** In Table 1, SparseFW (with either Wanda or RIA warm-start) improves or matches zero-shot accuracy on nearly every tested model and sparsity level (e.g., at 60% sparsity on LLaMA-3.1-8B: 51.92% vs. Wanda's 48.08%).

## Weaknesses

### Major

1. **The pure FW optimization (α=0.0) is consistently worse than the greedy heuristic; the working method (α=0.9) fixes 90% of the mask using that heuristic.** Lines 156–157 state this plainly: "setting α = 0.0 (full FW without any fixed weights) consistently yields worse results than the baselines." The best results require fixing the top 90% of Wanda-identified high-saliency weights and only applying FW to the remaining 10%. This means SparseFW's output is, for the vast majority of entries, determined by the greedy heuristic it claims to improve upon. The paper's framing (title: "Don't Be Greedy, Just Relax!", abstract, contributions) presents SparseFW as a standalone principled alternative, but the empirical realization is a refinement of Wanda's mask on its least-confident decisions. This mismatch between framing and substance is significant.

2. **SparseGPT, the de facto standard one-shot LLM pruning method, is excluded from comparison with a questionable justification.** The paper states (line 192) that it does "not compare directly to methods that involve a reconstruction step, such as SparseGPT." While SparseGPT combines mask selection with weight reconstruction and SparseFW is a mask-only method, SparseGPT is discussed at length in Sections 2.1 and the related work, and is the obvious baseline against which any new LLM pruning method should be evaluated. Without this comparison, the practical significance of SparseFW's improvements cannot be properly assessed.

3. **No error bars or significance measures for the main results (Table 1).** The table caption says "We omit standard deviations for legibility" but provides no indication of multiple runs or variance. Many improvements are small (e.g., perplexity 6.58 vs. 6.58 on Yi-1.5 at 50%), and several entries show SparseFW underperforming the baseline it warm-starts from (e.g., DeepSeek at 50% and 60%). Without uncertainty quantification, it is impossible to assess whether the reported improvements are statistically meaningful.

### Minor

1. **The local–global objective mismatch is acknowledged but not analyzed.** The paper notes (Section 5) that reducing per-layer pruning error does not reliably translate to lower perplexity, which is why α=0.9 is needed. However, there is no diagnosis of when or why this mismatch occurs (e.g., correlation with layer type, sparsity level, or model family). Understanding this is central to the method's credibility.

2. **The theoretical bound is for the local objective and involves unquantified constants.** Lemma 1's bound depends on λ_max(Q) (not reported for any model) and a √(d_in·d_out·k) term that is large at LLM scale. The paper acknowledges the bound is for the local pruning objective, not for perplexity, so its practical relevance is unclear.

3. **No wall-clock time or compute cost comparison.** The paper states SparseFW is "more compute-intensive" (line 240) but does not report runtimes or GPU-hours. For practitioners, the cost–benefit trade-off relative to Wanda is opaque.

### Trivial

1. Table 1 could report variance in a supplementary table even if omitted from the main table for legibility.

## Nice-to-Haves

- Adding SparseGPT as a baseline (even with a note about the mask-only vs. mask+reconstruction distinction) would substantially strengthen the evaluation.
- Characterizing the local–global mismatch (which layers benefit most from FW, which do not) would deepen the contribution beyond reporting the workaround.
- Reporting λ_max(Q) for the tested models would help readers assess the theoretical bound's relevance.

## Removed Points

- **Criticism about missing related works (AQA, SpQR, SliceGPT):** These are not standard baselines for this specific mask-selection setting; the paper's comparison scope is defensible.
- **Claim that the theory bound is "unlikely to be tight":** Generic criticism; theoretical bounds in ML are rarely tight. The bound's existence is a strength, and its limitations are acknowledged.
- **Oversimplification that "SparseFW's mask is exactly Wanda's mask for 90% of entries":** α=0.9 fixes the top 90% of high-saliency weights from being altered by FW, but the remaining 10% includes both weights Wanda pruned and weights Wanda kept. The fixed subset is not identical to the full Wanda mask.
- **Strength about "consistent improvements across all five model families and all sparsity regimes":** Slightly overstated — at 50% sparsity on Gemma-2, SparseFW accuracy (68.42) is marginally below Wanda (68.44). The broad trend is positive but not perfectly universal. Qualifying the strength rather than removing it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Reframe the contribution precisely: SparseFW is a method for refining existing pruning masks (e.g., from Wanda) via local convex optimization, not a standalone replacement for greedy heuristics. The title and abstract should reflect this.
- Add SparseGPT as a comparison point, even with a note about the differing problem setup.
- Report multiple-seed results or confidence intervals for the main table.
- Report wall-clock runtimes to help practitioners assess the cost-benefit trade-off.
- Investigate the local–global mismatch systematically: which layers, sparsity levels, or model families exhibit the largest gap?

## Score and Decision

**Calibration methodology:**

Round 1 (bracketing, 3 queries):
- Weak band (avg ≤ 3.5): CVXQ quantization (3.00), CVX-DPO (3.00), MOEfication (3.40), EfficientSkip (2.50), ConvexDistillation (3.00), LLM4Solver (3.40). These are clearly below the paper under review.
- Middle band (avg 3.5–7.5): **FISTAPruner (5.25, Reject)** — most comparable (convex optimization for LLM pruning); MoreauPruner (4.80, Reject); OWL (6.00, Reject); SparsitySolver (3.75); YOPO/PruneNet (6.00, Accept).
- Strong band (avg ≥ 7.5): All ~8.00 — these are substantially stronger papers (dimensional collapse, long-context attention, scaling laws, etc.) and not comparable.

Round 1 bracket: **3.5–7.5**, narrowed to the 4–6 range given the competitors in the middle band.

Round 2 (narrowing, 2 queries):
- **FISTAPruner (5.25, Reject)**: Most similar paper — convex optimization for LLM pruning. Our paper has a cleaner conceptual framework (convex relaxation of mask selection, not just LASSO) and the first theoretical guarantee. However, our α=0.9 issue is a significant weakness that FISTAPruner does not share. Our paper is slightly weaker → below 5.25.
- **MoreauPruner (4.80, Reject)**: Another optimization-based LLM pruning paper. Our paper's contributions (relaxation framework, Wanda derivation, theory) are stronger, but the α=0.9 framing mismatch is more damaging than MoreauPruner's weaknesses. Comparable or slightly below → ~4.5.
- **"Bypass Back-propagation" (5.00, Reject)**: Optimization-based structural pruning. Similar trade-off: novel approach but significant gaps. Comparable → ~4.5–5.0.
- **"The Unreasonable Ineffectiveness of the Deeper Layers" (6.50, Accept)**: Clean, well-executed empirical study on layer pruning. Not directly comparable but illustrates what an accept-level pruning paper looks like. Our paper is substantially weaker.

The paper has genuine contributions (convex relaxation framework, theoretical guarantee, memory-efficient implementation, clean Wanda derivation, consistent accuracy gains) but suffers from a significant framing-vs-reality problem: the pure optimization method is strictly worse than the heuristic, and the working method fixes 90% of the mask with that heuristic. Combined with the absence of SparseGPT as a baseline and the lack of statistical uncertainty measures for the main results, the paper in its current form does not meet the ICLR bar. A major revision with honest reframing, complete baselines, and statistical rigor would be needed.

**Final score: 4.5** — borderline paper with genuine contributions but a significant gap between claims and evidence that prevents acceptance in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>