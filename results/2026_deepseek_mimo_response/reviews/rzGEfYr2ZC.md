## Summary
This paper proposes SparseFW, a layerwise LLM pruning method that formulates mask selection as a convex relaxation over the convex hull of binary masks, solved via the Frank-Wolfe algorithm. The method includes a precomputation strategy for efficiency, a theoretical approximation guarantee (Lemma 1), and empirical improvements over Wanda and RIA on multiple modern GPT architectures (Gemma-2, Yi-1.5, DeepSeek-7B, Qwen2.5-7B/14B, LLaMA-3-8B).

## Strengths
- **Novel unification of Wanda and RIA**: Section 2.1 rigorously derives that Wanda's saliency score corresponds to optimal single-weight pruning (Eq. 4–5) and that RIA is equivalent to Wanda on a rescaled weight matrix (Eq. 6–7). This is an insightful theoretical observation that clarifies the relationship between existing methods.
- **Clean convex relaxation with efficient LMO**: The relaxation from binary constraints to the convex hull (Eq. 10) transforms an intractable combinatorial problem into a convex program (Eq. 11). The LMO reduces to a top-k selection (Eq. 12), and the precomputation of G=XX^⊤ and H=WG (Section 2.3) makes per-iteration cost independent of sequence length and sample count — a key scalability insight.
- **Consistent empirical improvements across multiple architectures**: Table 1 shows SparseFW outperforms or matches baselines across five modern GPT architectures. For zero-shot accuracy, SparseFW consistently outperforms at all sparsity levels. Per-layer error reductions of up to 80% (Figure 2) directly validate the optimization improvement. The method delivers particularly strong improvements at high sparsity (60% and 2:4).
- **Theoretical approximation guarantee**: Lemma 1 provides a data-dependent bound decomposing into optimization error (controllable via iterations) and thresholding error, distinguishing SparseFW from heuristic methods. The qualitative explanation connecting theory to Figure 4 is well done.
- **Calibration sample efficiency**: Figure 3 shows SparseFW benefits substantially from more calibration samples (perplexity drops from ~22 to ~19.5 as samples increase from 64 to 512) while Wanda barely improves (25.1 to 24.6), suggesting FW makes better use of calibration data.

## Weaknesses
### Fatal
None.

### Major
- **Framing overstates independence from greedy methods**: The paper's central narrative positions SparseFW as replacing greedy heuristics with principled optimization (abstract, introduction, title). However, Section 2.3 (lines 157–158) reveals that vanilla FW (α=0.0) "consistently yields worse results than the baselines" and that the method requires fixing 90% of the highest-Wanda-saliency weights as unprunable, with FW only optimizing the remaining 10%. The best-performing setting is α=0.9, meaning SparseFW fundamentally depends on Wanda's greedy saliency scores for the overwhelming majority of pruning decisions. The conclusion honestly acknowledges this ("inductive biases still appear necessary"), but this transparency should appear in the abstract and introduction. The contribution is more accurately characterized as "principled local reoptimization atop greedy methods" — still meaningful, but less novel than framed.

### Minor
- **No computational overhead quantification**: The paper runs 2000 FW iterations per layer (each requiring gradient computation and LMO calls) plus precomputation of G and H, but provides no wall-clock timing, FLOP counts, or runtime comparisons with Wanda/RIA. The argument that "one-time pruning cost is worthwhile for deployed LLMs" is reasonable but needs concrete numbers (Section 3, line 240).
- **Inconsistency in claimed error reduction**: The introduction (line 39) states "up to 80%" per-layer pruning error reduction, while Contribution 2 (line 44) states "up to 70%." These should be reconciled.
- **Qwen2.5-14B not listed in experimental setup**: Table 1 includes a Qwen2.5-14B column, but the experimental methodology section (line 182) only lists Qwen2.5-7B.
- **LLaMA-3.1 vs LLaMA-3 naming inconsistency**: Line 182 says "LLaMA-3.1-8B" but Table 1 columns are labeled "LLaMA-3 8B."
- **Mixed perplexity results at 50% sparsity**: At 50% unstructured sparsity on LLaMA-3 8B, SparseFW(Wanda) yields 10.21 perplexity vs. Wanda's 10.09 — a regression. The paper acknowledges improvements are "much more consistent and bigger" at higher sparsity, but the abstract presents broad superiority.

### Trivial
None.

## Nice-to-Haves
- Add SparseGPT to Table 1 as a reference baseline (even with a caveat about the different optimization problem) to clarify where SparseFW stands in the broader pruning landscape.
- Report standard deviations or confidence intervals for Table 1 to establish robustness.
- Ablate the α mechanism more deeply — why does 0.9 work best? Is Wanda correctly identifying the ~10% least important weights?
- Discuss memory overhead concretely (G is d_in × d_in, H is d_out × d_in) rather than just stating "memory-efficient."

## Removed Points
These points are flagged to be removed, treat them with caution.
None — all points were verified against the paper text.

## Novel Insights
The paper's most novel insight is the rigorous derivation showing Wanda and RIA can be understood as greedy approximations to the mask selection problem (Section 2.1), with Wanda corresponding to optimal single-weight pruning and RIA to Wanda on a rescaled matrix. This unification is genuinely useful for understanding the pruning landscape and motivating convex relaxation approaches. The decomposition of approximation error into optimization error and thresholding error (Section 4) also provides qualitative insight into the method's behavior.

## Suggestions
- Reframe the abstract and introduction to explicitly acknowledge that SparseFW builds on top of greedy warmstarts rather than replacing them. The contribution is still strong as "principled reoptimization."
- Add wall-clock timing comparisons for at least one model to quantify the overhead.
- Reconcile the 80% vs 70% error reduction claims.
- Add Qwen2.5-14B to the model list in Section 3.
- Consider a deeper ablation of the α parameter to understand *why* 0.9 works best.

---

### Calibration Report

**Round 1 anchors:**
- 0T8vCKa7yu (3.00) — LLM compression with convex optimization for quantization. SparseFW is clearly stronger: better theory, better empirical scope, better methodology.
- EVZnnhtMNX (3.00) — Convex optimization for LLM preference learning. Not directly comparable.
- 7DY2DFDT0T (2.50) — EfficientSkip: sparse variants of LLMs. Not comparable.
- XTxdDEFR6D (3.40) — Combinatorial optimization solver. Not comparable.
- pOBvr1PxFd (6.00) — OWL: layerwise sparsity for LLM pruning. SparseFW has better theoretical grounding; OWL has circular logic issues per reviewers.
- EjHtQlKEzV (4.50) — Reassessing layer pruning. SparseFW is stronger.
- 9uZGq8P2QM (4.00) — Specialized subnetworks. Less relevant.
- BINwUtUGuq (5.25) — FISTAPruner: very comparable (convex optimization for LLM pruning, rejected). SparseFW has better theory and cleaner methodology.
- OfjIlbelrT (8.00) — FlexPrefill: sparse attention. Not comparable.
- I4e82CIDxv (8.00) — Sparse feature circuits. Not comparable.
- t7P5BUKcYv (8.00) — MoE++. Not comparable.
- f4gF6AIHRy (8.00) — Submodular file selection. Not comparable.

**Round 1 bracket: 5–7**

**Round 2 anchors:**
- D9GoWJJxS5 (5.00) — Optimization-based structural pruning via policy gradient, rejected. SparseFW is cleaner with better theoretical grounding.
- pOBvr1PxFd (6.00) — OWL (same as round 1).
- BINwUtUGuq (5.25) — FISTAPruner (same as round 1).
- B9klVS7Ddk (6.75) — Compressing LLMs benchmarking paper, accepted. Not a method paper, not directly comparable.
- eNQp79A5Oz (6.60) — SNOWS: Hessian-free pruning optimization, accepted (scores 8,5,8,6,6). Very similar in spirit — principled optimization for pruning. SparseFW is slightly below due to α=0.9 framing issue.
- LCrm1FSl26 (5.60) — Adaptive pruning strategy, rejected. SparseFW is stronger.
- TjXjkxhSdE (5.67) — SDS pruning, rejected. SparseFW is stronger.
- 5RZoYIT3u6 (6.00) — PruneNet: calibration-free pruning, accepted (scores 6,6,6,6). Comparable quality level.
- ldJXXxPE0L (6.00) — Cost of scaling down LLMs, accepted. Study paper, not method.
- a0ftEY6puc (6.00) — Multilingual LLM pruning calibration, rejected. Less comparable.
- FT4gAPFsQd (6.00) — How sparse can we prune (theoretical), rejected. Less comparable.
- 88rjm6AXoC (6.25) — OBA: Optimal Brain Apoptosis, accepted. Different approach.
- awHTL3Hpto (6.33) — Convex relaxations for ReLU networks, accepted. Different domain.

**Final score reasoning:** SparseFW is clearly above the rejected 5.0–5.67 anchors (FISTAPruner, policy gradient pruning, SDS), comparable to the 6.0 anchors (OWL, PruneNet), but slightly below SNOWS (6.60) due to the α=0.9 framing issue. The technical contribution is sound, empirical results are consistent across five modern architectures, and the theory is genuine, but the gap between the "replacing greedy heuristics" framing and the actual method (which depends on Wanda for 90% of mask decisions) prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>