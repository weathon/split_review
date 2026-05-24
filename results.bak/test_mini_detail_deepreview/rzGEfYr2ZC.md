Now I have enough calibration data. Let me finalize my review.

**Round-1 bracket**: Based on comparison with FISTAPruner (5.25), MoreauPruner (4.80), and Bypass Back-Propagation (5.00), the paper sits in the **4.0–6.0** range. The α=0.9 dependency and lack of SparseGPT comparison place it below FISTAPruner.

**Round-2 narrowing**: Closest comps are FISTAPruner (5.25), MoreauPruner (4.80), and Bypass Back-Propagation (5.00). The current paper has a more principled optimization approach than FISTAPruner but weaker evaluation (no SparseGPT, models only up to 9B). The α=0.9 dependency is a more significant structural concern than any single weakness in those anchors. **Final score: 4.5.**

---

## Summary

This paper proposes SparseFW, a post-training LLM pruning method that relaxes the combinatorial mask-selection problem into a convex program over the convex hull of binary masks and solves it via the Frank-Wolfe (FW) algorithm. The method precomputes activation Gram matrices to make each FW iteration independent of calibration set size, supports both unstructured and 2:4 semi-structured sparsity, and warm-starts from existing masks (Wanda or RIA). Experiments on five models up to 9B parameters show per-layer error reductions of up to 80% and modest gains in final perplexity and zero-shot accuracy, especially at higher sparsity levels.

## Strengths

1. **Principled optimization formulation.** The convex relaxation of the binary mask constraint over the polytope C_k (Section 2.2) is technically sound and naturally lends itself to FW, which yields sparse iterates via an efficient LMO (select top-k negative gradient entries, O(d_out·d_in·log(k))). This is a genuinely different approach from the greedy heuristics (Wanda, RIA) and provides a formal connection — via the LMO structure — between the relaxed and combinatorial problems.

2. **Consistent improvements over Wanda/RIA at higher sparsity regimes.** Table 1 shows real gains at 60% unstructured sparsity and 2:4 semi-structured sparsity. For example, LLaMA-3-8B at 60%: SparseFW(Wanda) perplexity 17.97 vs Wanda 21.53; at 2:4: 20.45 vs 24.82. Zero-shot accuracy gains of 2–4 percentage points at these levels are substantive. The per-layer error reduction (up to 80% per Figure 2, 20–40% average) validates that the FW optimization is meaningfully improving the local objective.

3. **Memory-efficient implementation.** Precomputing G = XX^T (dimensions d_in×d_in) and H = WG makes per-iteration cost independent of calibration set size and sequence length (Section 2.3). For a 4096-dimensional layer, G is ~128 MB in float32. This is a practical engineering contribution that enables the method to scale.

4. **Benefits from additional calibration data, unlike Wanda.** Figure 3 (right) shows SparseFW perplexity dropping from ~22 to ~19.5 as calibration samples increase from 64 to 512, while Wanda plateaus (25.1→24.6). This is a genuine practical advantage when more calibration data is available.

5. **Honest reporting of limitations.** The paper transparently discloses that vanilla FW (α=0.0) fails, that fixing 90% of weights from the warmstart is necessary, and that the local-global objective mismatch persists (Sections 2.3 and 5). This candor is commendable.

## Weaknesses

### Major

1. **The core method only works as a refinement, not as a standalone solver.** The paper states (Section 2.3) that "setting α = 0.0 (full FW without any fixed weights) consistently yields worse results than the baselines." The successful variant fixes 90% of weights from the same greedy baseline (Wanda/RIA) that SparseFW claims to outperform. This is a structural gap between the paper's framing ("Don't Be Greedy, Just Relax!") and what actually works. The contribution is better characterized as *local FW-based refinement* of an existing mask on 10% of weights, rather than a new pruning paradigm that "accounts for weight interactions." The main algorithm (Algorithm 1) does not include the α-fixing step, making it inconsistent with the method that produces the reported results.

2. **No comparison against SparseGPT, the most widely used post-training LLM pruning method.** The paper excludes SparseGPT (Frantar & Alistarh, 2023) with the justification that it involves weight reconstruction and therefore does not directly solve (MASK SELECTION). While this scoping is explicitly stated (Section 3, line 196), the paper's headline claims ("outperforming strong baselines," "consistent gains in final WikiText perplexity and zero-shot accuracy") are about *final model quality after pruning*. Practitioners choosing a pruning method care about final perplexity and accuracy, not about which subproblem is being solved. SparseGPT achieves substantially better perplexity than Wanda at these sparsity levels, and its absence from the comparison tables makes it impossible to assess the practical significance of SparseFW's gains.

3. **No variance or confidence intervals reported for perplexity/accuracy.** Table 1 omits standard deviations (the paper states "We omit standard deviations for legibility"). At 50% sparsity, several comparisons show margins of 0.1–0.2 perplexity points (e.g., DeepSeek-7B at 50%: Wanda 7.79 vs SparseFW(Wanda) 7.89 — the baseline actually *wins*). Without variance estimates, the reader cannot determine whether the claimed improvements are statistically reliable or within the noise of calibration set sampling. This is particularly concerning because Figure 3 (left) reports min-max ranges over random seeds for the ablation curves but those are absent from the main comparison table.

4. **Theoretical guarantee (Lemma 1) is unlikely to provide practically meaningful assurance.** The bound contains a term 2(k + sqrt(2 d_in·d_out·k)), where d_in·d_out can be on the order of 10^7 for layers in 8B-parameter models. The sqrt term alone is several thousand. Combined with λ_max(Q) (the spectral radius of the Hessian w.r.t. the mask — itself an ill-defined quantity without additional structure), the bound does not constrain the suboptimality gap in any useful way for LLM-scale problems. The informal lemma is stated without a clear definition of Q (the paper says "Q represents the Hessian of the objective function and λ_max(Q) its largest eigenvalue" but the Hessian w.r.t. a matrix is a fourth-order tensor whose spectral properties require clarification deferred to the appendix). This weakens the paper's claim of providing "strong theoretical justification."

### Minor

5. **Model scale limited to 7B–9B parameters.** The largest model evaluated is Gemma-2-9B and Yi-1.5-9B. Scalability to 13B, 30B, or 70B models is not demonstrated. The paper claims the method "scales to large models" but provides no evidence beyond 9B. Given that 2000 FW iterations per layer for a 32-layer 8B model implies 64,000 iterations total, the wall-clock time and memory requirements at larger scales are not reported.

6. **Wall-clock runtime not reported.** The paper discusses memory efficiency but provides no runtime comparison against Wanda or RIA. The claim "spending more resources once to improve the performance of pruned models is worthwhile" (Section 3) is not backed by concrete timing numbers. A practitioner needs to know whether a 2000-iteration-per-layer method takes minutes, hours, or days.

7. **Only one calibration dataset (C4) and one evaluation perplexity (WikiText).** Generalization to other domains (e.g., downstream tasks, out-of-distribution settings) is not validated.

### Trivial

8. Algorithm 1's thresholding step (Line 7) selects top-k entries of M_T, but M_T's entries lie in [0,1]; ties in the thresholding are not discussed.

9. The paper states "we will make our code publicly available" but does not include a reproducibility statement with specific details.

## Nice-to-Haves

- An ablation showing SparseFW's sensitivity to the choice of which 10% of weights are optimized (random subset vs. lowest-saliency subset vs. gradient-guided selection) would clarify whether the gains come specifically from FW optimization or from any local search on a small fraction of weights.
- Comparing SparseFW's *mask selection* alone (without reconstruction) against SparseGPT's mask selection (decoupled from its weight update step) would address the scope gap while maintaining fairness.
- Runtime vs. perplexity Pareto plots showing where SparseFW sits relative to Wanda and RIA under matched compute budgets.
- Moving the α ablation (currently only in the appendix, referenced in text) into the main paper.

## Removed Points

- **Criticism about the paper not addressing weight interactions for 90% of fixed weights**: The paper acknowledges this (Section 2.3: "This suggests that Wanda reliably identifies weights that should be preserved, even if a more thorough local optimization would prune them"). The critic frames this as the core idea failing, but the paper honestly discloses the issue. Retained in weakened form as Weakness #1 (major).
- **Claim that Q being a fourth-order tensor makes λ_max(Q) undefined**: This is incorrect — the Hessian operator's operator norm is well-defined for linear operators on matrix spaces. The criticism about lack of clear definition is valid and retained as part of Weakness #4.
- **"Perplexity improvements are inconsistent and often small"**: At 60% and 2:4 sparsity, improvements are substantial (e.g., 3.5+ perplexity points on LLaMA-3). The inconsistency is mainly at 50% sparsity. The critic overstates this; retained in weakened form as part of Weakness #3 (no variance reported).
- **Generic strengths about "addressing an important problem"** or "well-written" from the Strength Finder: Removed as too generic.
- **Strength about theoretical guarantees**: Weakened significantly since the bound is likely vacuous at scale.
- **Strength about "drastically reduces pruning error"**: Retained as Strength #2 but caveated — the local error reduction does not always translate to perplexity gains, which the paper acknowledges.

## Novel Insights

The most interesting observation to emerge from the reviews is that the gap between the continuous mask (which FW optimizes well, achieving 80% error reduction) and the thresholded mask (which shows only ~40% error reduction) creates a persistent "thresholding residual" that does not vanish with more iterations (Figure 4, right panel). This suggests that the convex relaxation + rounding pipeline has a fundamental limitation for the mask selection problem: the extreme points of C_k that FW approaches are not necessarily well-aligned with the binary solutions to (MASK SELECTION), because the relaxed problem's optimum may lie strictly in the interior of C_k. This structural insight — that the relaxation gap at LLM scale is not closure-guaranteed to favor the original problem — is not fully discussed in the paper and may point to why α=0.0 fails. The paper would benefit from analyzing whether the thresholded mask converges to a better solution as T→∞ or whether there is an irreducible gap.

## Suggestions

1. **Reframe the contribution.** Present SparseFW as a *local mask refinement* method for LLM pruning, rather than a standalone alternative to greedy pruning. The paper's own evidence (α=0.0 fails, α=0.9 works) supports this framing, and it would honestly communicate what the method does.

2. **Include SparseGPT as a baseline for final perplexity/accuracy**, even if this requires noting that SparseGPT benefits from weight reconstruction. A fair comparison would show what each method achieves on the same models at the same sparsity levels.

3. **Report standard deviations or confidence intervals** for the main results in Table 1, especially where margins are small (≤0.5 perplexity points). Provide the number of random seeds and the sampling procedure for calibration data.

4. **Move the α-ablation to the main paper** as a sensitivity analysis. Show the perplexity at α = 0.0, 0.1, 0.5, 0.9, 1.0 to demonstrate where the gains come from.

5. **Report wall-clock pruning time** for a representative model (e.g., LLaMA-3-8B) alongside Wanda and RIA, with GPU/CPU details. Show Pareto curves of perplexity vs. runtime at different iteration counts.

6. **Clarify the theoretical bound.** Define Q precisely, state the formal lemma (not just informal), and discuss how loose the bound is in practice. Acknowledge if the thresholding error term dominates at LLM scale.

## Score and Decision

**Calibration Anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| FISTAPruner (BINwUtUGuq) | 5.25 (Reject) | R1, R2 | Most similar paper: convex optimization for LLM pruning, better evaluation (SparseGPT included, scales to 70B), but less principled optimization (LASSO+FISTA vs FW on convex relaxation). Current paper has a cleaner formulation but weaker evaluation and the α=0.9 dependency issue. Slightly weaker overall. |
| MoreauPruner (Y0qmwm6tgy) | 4.80 (Reject) | R1, R2 | Another optimization-based LLM pruning paper with provable guarantees. Marginal improvements, limited model scale. Comparable quality and impact. |
| Bypass Back-Propagation (D9GoWJJxS5) | 5.00 (Reject) | R2 | Policy-gradient LLM pruning. Stronger evaluation (more models, more baselines). Current paper is slightly weaker due to evaluation gaps. |
| LLM Compression Convex Opt (0T8vCKa7yu) | 3.00 (Reject) | R1 | Quantization not pruning, poorly executed. Clear reject. Current paper is substantially stronger. |
| PruneNet (5RZoYIT3u6) | 6.00 (Accept) | R2 | Calibration-free pruning via policy learning. More novel framing, broader experiments. Current paper is weaker. |

**Round-1 bracket**: 4.0–6.0. **Round-2 narrowing**: The paper sits below FISTAPruner (5.25) due to the α=0.9 structural issue and lack of SparseGPT comparison, but above the 3.0-level papers. Comparable to MoreauPruner (4.80) and Bypass Back-Propagation (5.00), with slightly more fundamental flaws (the method-as-described doesn't work without the warmstart crutch) but a more principled optimization foundation.

**Overall**: SparseFW introduces a novel, principled optimization framework for LLM mask selection. The method yields real improvements over Wanda/RIA at higher sparsity levels. However, the requirement to fix 90% of the mask from a greedy baseline (because pure FW fails) fundamentally undermines the paper's narrative. Combined with the absence of comparisons against SparseGPT, the lack of statistical rigor, a theoretical guarantee that is likely vacuous at scale, and evaluation limited to ≤9B models, the evidence falls short of supporting the paper's stronger claims. The paper has solid components but needs substantial revision before it can be accepted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>