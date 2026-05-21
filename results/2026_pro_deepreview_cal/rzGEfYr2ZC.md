Now I have enough data to calibrate. Let me compile my analysis and write the final review.

Here are my anchor comparisons:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FISTAPruner (BINwUtUGuq) | 5.25 | R1/R2 | Similar topic (convex opt for LLM pruning), SparseFW is stronger — better motivation, more models, more transparent about limitations |
| Bypass Back-propagation (D9GoWJJxS5) | 5.00 | R2 | Optimization-based pruning, SparseFW has broader evaluation and cleaner method |
| Mecon (LCrm1FSl26) | 5.60 | R2 | Evolutionary pruning metric search, less directly comparable |
| Pruning Aggregation (ji6MYm4Htg) | 4.80 | R2 | Different pruning approach, SparseFW clearly stronger |
| PruneNet (5RZoYIT3u6) | 6.00 | R1 | Accepted, calibration-free pruning; SparseFW has broader model coverage and theoretical analysis |
| Double Sparse Factorization (DwiwOcK1B7) | 6.33 | R2 | Accepted, factorization-based; comparable novelty level, similar practical applicability concerns |
| Plug-and-Play/RIA (Tr0lPx9woF) | 6.50 | R2 | Accepted, the RIA paper SparseFW uses as baseline; SparseFW weaker on cleanliness of contribution but has theory |

**Round 1 bracket:** 5.0–6.5

**Round 2 narrowing:** SparseFW is stronger than FISTAPruner (5.25) and comparably situated to PruneNet (6.00) / DSF (6.33), but weaker than Plug-and-Play (6.50). I place it at **6.0**.

---

## Summary

The paper proposes SparseFW, a layerwise LLM pruning method that relaxes the combinatorial mask selection problem to a convex program over the convex hull of binary masks, solved via the Frank-Wolfe algorithm. The key insight is that FW's linear minimization oracle naturally produces sparse updates and accounts for weight interactions that greedy heuristics (Wanda, RIA) ignore. The method reduces per-layer reconstruction error by up to 80% and improves perplexity and zero-shot accuracy across five modern LLM families at higher sparsity levels. A theoretical bound decomposes the error into optimization and thresholding components. The paper is notably transparent: it acknowledges that unconstrained FW underperforms baselines on final model quality and that fixing 90% of high-saliency weights from a warm-start heuristic is necessary for practical gains.

## Strengths

- **Elegant convex relaxation + FW formulation.** The paper derives Wanda and RIA as greedy single-weight approximations to the mask selection problem (Eqs. 4–7), then proposes the convex relaxation over the convex hull of masks (Eq. 10) as a principled alternative that captures weight interactions. The FW algorithm is a natural fit: the LMO selects top-k gradient entries, producing sparse updates without projection. This connection is clean and well-motivated (Section 2.1–2.2).

- **Comprehensive empirical evaluation.** Table 1 covers five modern architectures (LLaMA-3.1-8B, Gemma-2-9B, Yi-1.5-9B, DeepSeek-7B, Qwen2.5-7B/14B) across 50%, 60% unstructured, and 2:4 semi-structured sparsity. At 60% and 2:4 sparsity, SparseFW consistently improves perplexity and zero-shot accuracy over Wanda and RIA warm-starts — for example, LLaMA-3.1-8B perplexity drops from 21.53 (Wanda) to 17.97 at 60% sparsity, and zero-shot accuracy improves by up to 3.8pp across settings.

- **Per-layer error reduction validates the core claim.** Figure 2 shows up to 80% relative reduction in per-layer reconstruction error over Wanda across all layers of LLaMA-3.1-8B at 60% sparsity. The continuous iterate shows ~75% average error reduction over 5000 iterations (Figure 4, left). This directly supports the claim that FW optimization substantially improves the local objective.

- **Theoretical analysis with empirical corroboration.** Lemma 1 provides a data-dependent bound that decomposes error into an optimization term (scaling as O(k/T), vanishing with iterations) and a thresholding term (dimension-dependent, non-vanishing). Figure 4 empirically validates this decomposition: the thresholded mask initially degrades as the iterate moves through the interior (thresholding error grows), then plateaus while the continuous mask keeps improving — exactly as the theory predicts.

- **Honest treatment of limitations.** The paper explicitly states that vanilla FW (α=0.0) yields worse perplexity than baselines, that α=0.9 is required for practical gains (Section 2.3), and that "inductive biases still appear necessary for improved perplexity" (Conclusion). This transparency is commendable and rare in the pruning literature.

## Weaknesses

### Fatal

None.

### Major

- **Gap between theoretical analysis and the method that works.** The theoretical guarantees (Lemma 1) assume optimization over the full convex hull C_k. However, the method that produces the results in Table 1 fixes 90% of weights from the Wanda/RIA warm-start (α=0.9) and applies FW only to the remaining 10%. The paper is transparent about this (Section 2.3, Conclusion), but the abstract and introduction still frame SparseFW as "solving the convex relaxation" without adequately qualifying that the working instantiation is a local refinement of an existing heuristic mask. This theory-practice gap limits the force of the theoretical contribution and means the method is better characterized as mask *refinement* than as a standalone solver for the relaxed problem.

- **SparseGPT omitted as a baseline.** The paper excludes SparseGPT because it "also updates the remaining weights" (Section 3), but SparseGPT is the most prominent layerwise LLM pruning method and addresses the same underlying mask selection problem (combined with weight reconstruction). The stated scope choice is defensible — the paper focuses on pure mask selection — but without this comparison it is difficult to assess whether SparseFW advances the practical state of the art or merely improves upon the weaker Wanda/RIA baselines. This omission weakens the empirical contribution.

### Minor

- **Modest or negative gains at 50% sparsity.** At 50% unstructured sparsity, SparseFW sometimes performs *worse* than baselines (LLaMA-3-8B: Wanda 10.09 vs SparseFW 10.21; DeepSeek-7B: Wanda 7.79 vs SparseFW 7.89). The paper acknowledges that improvements are larger and more consistent at higher sparsity, but the abstract's claim of "consistent gains" should be qualified.

- **No computational cost measurements.** The paper claims memory efficiency from pre-computing G = XX^T and H = WG (Section 2.3), and argues that the extra compute is justified for deployment (Section 3). However, no wall-clock time, peak GPU memory, or FLOP comparisons against Wanda, RIA, or SparseGPT are provided. This makes it hard for practitioners to evaluate the cost-benefit trade-off.

### Trivial

- The abstract states SparseFW "drastically reduces the per-layer pruning error" without distinguishing between continuous and thresholded masks; the dramatic reduction applies to the continuous iterate, not the final thresholded mask (which shows ~40% reduction in Figure 4).

## Nice-to-Haves

- Standard deviations or confidence intervals in Table 1 would help assess whether the small accuracy gains are statistically meaningful. The paper notes they were "omitted for legibility" but could be included in an appendix.
- A more detailed investigation into *why* the unconstrained convex relaxation fails to improve perplexity (overfitting to calibration data? thresholding artifact? limitation of the local objective?) would strengthen the contribution.
- The α=0.9 ablation (currently in appendix) could be promoted to the main text to prevent misinterpretation of SparseFW as a standalone solver.
- The method could be reframed as mask refinement rather than a solver for the convex relaxation, which would align the theoretical analysis with the working algorithm.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The theoretical guarantees do not apply to this setting" (claimed as fatal).** REMOVED as a fatal claim. The paper does not hide the α parameter; it explicitly states the constraint in Section 2.3. The theoretical analysis could be extended to the restricted setting, but the paper's transparency about the gap means this is a limitation to discuss, not a fatal error. Downgraded to Major and reframed as a theory-practice gap.

- **Harsh Critic: "The bound includes a constant thresholding-error term that scales with √(d_in d_out k) and does not vanish" (claimed as overstatement).** WEAKENED. The paper itself discusses this explicitly: "the thresholding error remains nonzero, so the thresholded curve does not fully catch up to the continuous one" (Section 4). The paper claims the *optimization* error can be made arbitrarily small, not the total error. The paper's claims about the bound are appropriately qualified.

- **Harsh Critic: "Exaggerated performance claims" with LLaMA-3-8B 50% example.** PARTIALLY RETAINED as Minor. The paper does state "consistent gains" in the abstract, but at 50% sparsity some results are negative. The paper itself notes bigger improvements at higher sparsity. The criticism is partially valid but the paper's body text is more nuanced than the abstract.

- **Harsh Critic: "Reliance on warm-start questions whether the convex relaxation captures the right objective."** This is a reasonable observation but the paper already discusses this limitation in the Conclusion. Merged into Major weakness 1.

- **Harsh Critic: "The use of a single calibration/validation split and absence of standard deviations."** MOVED to Nice-to-have. Single-split evaluation is standard practice in this literature (Wanda, SparseGPT, RIA all use it). Figure 3 does show min-max ranges over random seeds for the sample/iteration ablation.

- **Harsh Critic: Missing appendix / Table 2 not reproduced.** REMOVED per hard rules — the parser strips appendices; the paper states the α=0.9 result in the main text.

- **Strength Finder: "The warm-start strategy is a simple but effective practical refinement."** RETAINED but reframed — it is simultaneously a practical strength and a limitation (theory-practice gap). The paper's honesty about this is a strength; the necessity of α=0.9 is a limitation.

## Novel Insights

The review process surfaced an interesting tension that the paper itself partially explores: the convex relaxation dramatically improves the *local* per-layer objective (up to 80% reduction in reconstruction error) but this does not reliably translate to better *global* model quality without the warm-start constraint (α=0.9). This local-global mismatch is a genuinely important observation for the pruning community — it suggests that the calibration-based reconstruction error, while computationally convenient, may not be an adequate proxy for downstream performance when optimized aggressively. The paper's finding that constraining the search space to a neighborhood of a saliency heuristic recovers the translation from local to global gains is a useful practical lesson, even if the theoretical underpinnings remain incomplete.

## Suggestions

- Reframe the contribution as mask *refinement*: given a good initial mask from a saliency heuristic, FW efficiently improves it by searching a small continuous neighborhood. This aligns the theory with what actually works and makes the α parameter a feature rather than a caveat.
- Add SparseGPT as a baseline, or provide a more compelling justification for its exclusion (e.g., an experiment showing SparseFW + SparseGPT-style reconstruction).
- Include at least one runtime/memory comparison against Wanda and RIA to substantiate the efficiency claims.
- Move the α-ablation to the main text and prominently show α=0.0 results to prevent misinterpretation.

## Score and Decision

The paper makes a genuine contribution — the convex relaxation + FW formulation for LLM pruning is elegant, the evaluation is broad, and the theoretical analysis is informative. The transparency about limitations is a notable strength. However, the gap between the theory (full relaxation) and the working method (α=0.9 constrained refinement) limits the impact of the theoretical contribution, and the omission of SparseGPT weakens the empirical story. Compared to accepted papers in this space, SparseFW sits above FISTAPruner (5.25, rejected) and PruneNet (6.00, accepted) but below Plug-and-Play/RIA (6.50, accepted).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>