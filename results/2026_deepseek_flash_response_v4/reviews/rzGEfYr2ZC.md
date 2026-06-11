**Round 1 bracket explicit statement:** Based on the calibration search, the paper sits between the weak-anchor band (scores 2.5–3.4, papers significantly weaker) and the strong-anchor band (scores 8.0, papers on different topics and clearly stronger). Comparing to the middle-band anchors: the paper is clearly stronger than Compresso (5.25), comparable to OWL (6.00) and PruneNet (6.00), and slightly weaker than Double Sparse Factorization (6.33). This places the paper in the **4.5–6.0 range**.

**Round 2 narrowing:** Within this bracket, reading full reviews of DSF (6.33), OWL (6.00), PruneNet (6.00), and Compresso (5.25) confirms placement. SparseFW's contributions (broad model coverage, theoretical framework) are comparable to the ~6.0 papers, but the warmstart caveat (pure relaxation fails) is a more significant limitation than any single weakness in those papers. This pushes the score to the lower end of the range.

**All anchors:**
- DSF `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DwiwOcK1B7.md` (6.33, Round 2) — Cleaner formulation without warmstart hack; SparseFW slightly weaker.
- OWL `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/pOBvr1PxFd.md` (6.00, Round 2) — Strong empirical results but questionable logic; SparseFW comparable.
- PruneNet `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5RZoYIT3u6.md` (6.00, Round 2) — Calibration-free approach but limited model scope; SparseFW comparable.
- Compresso `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ktiikNTgK5.md` (5.25, Round 2) — Limited baselines, no theory; SparseFW stronger.
- Cost of Scaling Down `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ldJXXxPE0L.md` (6.00, Round 2) — Analysis paper, different genre.
- Rethinking Sparse Scaling `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ud8FtE1N4N.md` (6.67, Round 2) — More comprehensive study; SparseFW weaker.

---

## Summary

The paper proposes SparseFW, a method for LLM pruning that relaxes the combinatorial mask selection problem to a convex program over the convex hull of binary masks and solves it with the Frank-Wolfe (FW) algorithm, aiming to account for weight interactions that greedy heuristics ignore. The method warm-starts from Wanda or RIA masks and further optimizes the mask via FW iterations, achieving per-layer pruning error reductions of up to 80% and perplexity/accuracy gains, particularly at higher sparsity levels (60%, 2:4).

## Strengths

1. **Principled departure from greedy heuristics.** The convex relaxation formulation (Equation 10: $\mathcal{C}_k = \{M \in [0,1]^{d_{\text{out}} \times d_{\text{in}}} : \|M\|_1 \leq k\}$) explicitly accounts for weight interactions in mask selection, addressing a known limitation of methods like Wanda and RIA that prune weights independently. The LMO derivation (Equation 12) is clean and yields sparse updates naturally.

2. **Substantial per-layer reconstruction error reductions.** Figure 2 shows reductions of up to 80% (average 20–40% across models and sparsity regimes) relative to Wanda warmstarts. This provides direct evidence that the FW optimization improves the local objective over baselines.

3. **Meaningful perplexity/accuracy gains at higher sparsity levels.** At 60% and 2:4 sparsity, SparseFW consistently achieves best perplexity and accuracy across most models (e.g., LLaMA-3.1-8B at 2:4: perplexity 20.45 vs. Wanda's 24.82; accuracy 48.54% vs. Wanda's 47.13%). The method shows its value where pruning is hardest.

4. **Theoretical approximation guarantee.** Lemma 1 provides a data-dependent bound connecting the relaxed solution to the original combinatorial problem, with a clean decomposition into optimization error ($k\lambda_{\max}(Q)/T$, vanishing with iterations) and thresholding error. This is validated empirically in Figure 4.

5. **Memory-efficient implementation.** Precomputation of $G=XX^\top$ and $H=WG$ makes per-iteration cost independent of calibration dataset size (line 153), a practical advantage.

6. **Transparent disclosure of limitations.** The paper candidly reports that vanilla FW ($\alpha=0.0$) "consistently yields worse results than the baselines" (line 157), discusses the local-global objective mismatch, and acknowledges the warmstart heuristic in the conclusion (lines 278-283).

## Weaknesses

### Fatal
None.

### Major

1. **The pure convex relaxation fails; the working method is a fundamentally different hybrid.** The paper reports that setting $\alpha=0.0$ (full FW without any fixed weights) "consistently yields worse results than the baselines" (line 157). The best results come from $\alpha=0.9$, which fixes 90% of weights using the baseline saliency scores (Wanda or RIA) and optimizes only the remaining 10%. This means the method that actually works is not the pure convex-relaxation approach described in the methodology and theory, but a hybrid where most pruning decisions come from the baseline heuristic. The theoretical guarantees (Lemma 1) apply to the full relaxation over $\mathcal{C}_k$, not directly to the $\alpha=0.9$ variant, and no argument connects the two. The paper's framing throughout (abstract, introduction) emphasizes the convex relaxation approach without adequately foregrounding this dependence. While the paper is transparent about this issue in Section 2.3, the narrative framing overstates the scope of the contribution relative to what actually works.

2. **Empirical improvements are inconsistent at lower sparsity.** At 50% sparsity, Table 1 shows SparseFW is worse than the best baseline in 3 of 6 models for perplexity (e.g., DeepSeek-7B: Wanda 7.79 best, SparseFW(Wanda) 7.89 worse; LLaMA-3-8B: RIA 9.88 best, SparseFW(Wanda) 10.21 substantially worse). The headline claim of "outperforms strong baselines" requires qualification by sparsity regime. Gains are more consistent at 60% and 2:4 sparsity, which partially mitigates this concern.

3. **The theoretical bound is loose at LLM scale.** The thresholding error term $O(k + \sqrt{d_{\text{in}} d_{\text{out}} k})$ dominates the bound (roughly $4.4 \times 10^7$ for a $4096 \times 4096$ layer at 60% unstructured sparsity), while the optimization error ($k/T \approx 3350$ at $T=2000$) is negligible by comparison. The bound therefore does not provide a meaningful quantitative guarantee in the practical regime where the method is applied. The paper does not discuss its tightness.

### Minor

1. **No comparison to SparseGPT.** The paper justifies this by noting SparseGPT involves a weight reconstruction step (line 192), which is a reasonable methodological distinction. However, SparseGPT is the most widely used one-shot LLM pruning method; the paper's broader claim of outperforming "state-of-the-art" approaches is harder to evaluate without this comparison. Many practitioners care about end-to-end performance.

2. **Standard deviations omitted.** Table 1 notes "We omit standard deviations for legibility" (line 208). Given the modest and sometimes inconsistent gains (especially at 50% sparsity), it is difficult to assess which improvements are statistically significant.

3. **$\alpha$ hyperparameter analysis in appendix.** The $\alpha$ sensitivity sweep (arguably the most important hyperparameter, since it defines which version of the method is viable) is cited as Table 2 in the appendix. This analysis warrants main-paper placement.

4. **No computational cost comparison.** SparseFW uses 2000 FW iterations per layer, a significant cost. The paper argues this is worthwhile for one-shot pruning (line 240), but provides no wall-clock time or FLOPs comparison with baselines.

### Trivial
None.

## Nice-to-Haves

- Analysis of which specific weights the pure FW ($\alpha=0.0$) prunes incorrectly vs. what Wanda correctly preserves, to better understand the local-global mismatch.
- Ablation of $\alpha$ values (0.0 to 1.0) in the main paper.
- Standard deviations for a representative subset of results.
- Wall-clock time or FLOPs comparison with Wanda, RIA, and SparseGPT.

## Removed Points

These points were raised by the reviewers but are removed for the reasons below. Treat them with caution if referenced.

- **"The claim that Wanda does not increase with additional data is stated without evidence"** (Harsh Critic) — Factually incorrect; the paper provides specific numbers (line 240: perplexity decrease from 25.1 to 24.6 for Wanda when increasing samples from 64 to 512).
- **"The warmstart issue is a fatal structural issue that invalidates the paper"** (Harsh Critic framing) — Demoted from Fatal to Major. The paper is transparent about this issue, and the hybrid approach still contributes value even if the pure relaxation fails. The contribution is narrower than claimed but not invalidated.
- **"The theoretical bound is uninformative"** (Harsh Critic framing as fatal) — Retained as Major weakness 3 but softened. The bound's decomposition into optimization vs. thresholding error is conceptually useful even if absolute numbers are loose.
- **Generic strengths about "important problem," "timely topic"** (Strength Finder) — Removed as generic/superficial lacking specific evidence.

## Novel Insights

The reviews surface a central tension: the paper's clean theoretical framing (convex relaxation + FW) is belied by the empirical necessity of the warmstart heuristic. The pure relaxation fails because optimizing the local reconstruction objective aggressively produces masks that harm the global (perplexity) objective. This local-global mismatch, which the paper transparently identifies but does not resolve, is a genuinely interesting finding — it suggests that interaction-aware mask optimization on the local objective alone may not suffice, and that the heuristics in greedy methods implicitly encode useful inductive biases for the global objective. The paper itself notes this but does not deeply analyze it.

## Suggestions

1. **Reframe the contribution.** Position SparseFW as "improving Wanda/RIA masks via local convex optimization on a subset of uncertain weights" rather than as a pure convex-relaxation approach. The warmstart should be presented as a core component, not a caveat.
2. **Include SparseGPT results** (with appropriate caveats about different problem formulations) to help practitioners gauge practical competitiveness.
3. **Show the $\alpha$ sensitivity sweep in the main paper** — it is the most critical hyperparameter and defines what the method actually does.
4. **Provide standard deviations** for at least a representative subset of results, especially at 50% sparsity where gains are inconsistent.
5. **Include a computational cost comparison** (wall-clock time or relative FLOPs) to help readers assess the practical trade-off.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>