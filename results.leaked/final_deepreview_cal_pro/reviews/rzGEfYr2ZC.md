Now I have a solid set of calibration anchors. Let me synthesize the final review.

**Round 1 Bracket:** Based on the comparison, this paper sits between the weak band (CVXQ at 3.00) and the strong band (8.00 papers), likely in the 5–6 range. The most comparable anchor is FISTAPruner at 5.25.

**Round 2 Narrowing:** Reading FISTAPruner (5.25), RotPruner (5.33), OWL (6.00), and PruneNet (6.00):

- SparseFW is clearly stronger than CVXQ (3.00), which had fundamental formulation issues.
- SparseFW is comparable to FISTAPruner (5.25) — both propose convex-optimization-based LLM pruning with theoretical guarantees, but SparseFW has a cleaner theoretical framing (convex relaxation + FW rather than just LASSO/FISTA) and better empirical evaluation across more models.
- SparseFW is somewhat weaker than OWL (6.00) and PruneNet (6.00), which had more clearly scoped contributions and fewer framing issues. OWL's and PruneNet's weaknesses were more about missing experiments; SparseFW's framing issue (advertising a standalone method that relies on a 90% frozen heuristic mask) is more structural.
- This places SparseFW around **5.5**.

---

## Summary

This paper proposes SparseFW, a layerwise LLM pruning method that relaxes the combinatorial mask-selection problem to a convex program and solves it via the Frank-Wolfe algorithm. The method is memory-efficient, scales to billion-parameter models, and is shown to improve over Wanda and RIA baselines in perplexity and zero-shot accuracy at higher sparsity levels, with supporting theoretical guarantees.

## Strengths

- **Insightful unification of greedy methods.** The analysis showing that Wanda and RIA can be understood as greedy single-weight approximations to the mask-selection objective (Equations 4–7) is well-executed and provides a clear conceptual motivation for why accounting for weight interactions should help.

- **Strong per-layer error reductions and good empirical gains at high sparsity.** Figure 2 demonstrates up to 80% per-layer reconstruction error reduction over Wanda. Table 1 shows consistent improvements in perplexity and zero-shot accuracy at 60% and 2:4 sparsity across five modern LLM architectures (Gemma-2, Yi-1.5, DeepSeek, Qwen2.5, LLaMA-3).

- **Memory-efficient, practical design.** Precomputing the Gram matrix $G = XX^\top$ and $H = WG$ makes the gradient computation independent of sequence length and sample count, enabling the method to scale to large models (Section 2.3).

- **Effective use of calibration data.** Figure 3 shows SparseFW's perplexity continues to improve as calibration samples increase from 64 to 512, whereas Wanda plateaus — demonstrating that the FW optimization better exploits additional data.

- **Theoretical grounding.** Lemma 1 provides a decomposition of the approximation error into optimization error (from FW convergence) and thresholding error, offering a formal justification absent from prior heuristic methods.

## Weaknesses

### Major

- **The method that produces results is not the method advertised in the abstract and introduction.** Vanilla FW (α = 0.0, full search space) *underperforms* the baselines. The results in Table 1 all use α = 0.9 — i.e., 90% of the mask is frozen to the warmstart's (Wanda's or RIA's) highest-saliency weights, and FW optimizes only the remaining 10%. The abstract and introduction frame SparseFW as a principled alternative to greedy heuristics, but the actual working method is more accurately described as a lightweight post-processing refinement of those same heuristics. The paper is transparent about this in Section 2.3 and the conclusion, but the framing in the front matter overclaims what has been demonstrated. This narrows the significance of the contribution.

- **The theoretical bound (Lemma 1) describes the full FW algorithm, not the α = 0.9 version actually evaluated.** The bound uses the full mask dimension $d_{in} d_{out}$ and assumes FW runs on the entire search space. Since the working method restricts optimization to only 10% of weights preselected by a heuristic, the bound does not directly characterize the empirical algorithm, nor does it explain why the fixed-fraction trick is necessary.

### Minor

- **Improvements at 50% sparsity are weak and occasionally reversed.** In Table 1, SparseFW (Wanda) on LLaMA-3.1-8B at 50% sparsity yields perplexity 10.21 versus Wanda's 10.09 — a regression. The gains are concentrated at 60% and 2:4 sparsity, and the paper does not discuss when SparseFW is or is not worth the additional compute.

- **SparseGPT is excluded without empirical justification.** The paper argues SparseGPT is a different problem class (mask selection + weight reconstruction) and excludes it. While the scope argument is reasonable, a single comparison point would help readers situate SparseFW within the broader pruning landscape. Without it, the claim of "outperforming strong baselines on state-of-the-art GPT architectures" is incomplete relative to what practitioners actually use.

- **Algorithm 1 does not reflect the actual method.** The pseudocode shows a generic FW procedure with no mention of frozen weights or the α parameter. The crucial constrained variant is only described in prose and deferred to the appendix, making reproduction unnecessarily difficult.

### Trivial

- The caption of Table 1 does not specify the fixed-fraction setting α, requiring the reader to recall from Section 2.3 that α = 0.9 was used.

## Nice-to-Haves

- Reporting inference speedup or memory reduction of pruned models, and the wall-clock runtime of SparseFW relative to Wanda, would ground the perplexity/accuracy numbers in practical terms.
- Investigating *why* vanilla FW prunes "crucial" weights and whether a different initialization, constraint, or rounding scheme could reduce the α dependency would substantially strengthen the core contribution.
- Discussing how to choose between Wanda and RIA warmstarts when both are available.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claim that the method is "not a standalone pruning criterion" and that the dependency on warmstart is "fatal."** While the dependency is real and limits the contribution, the paper *is transparent about it* in Section 2.3 and the conclusion. The method does produce genuine improvements over the warmstart baselines even if it cannot stand alone. This is a framing issue (moved to Major), not a fatal flaw invalidating all results.

- **Harsh critic claim that "the convex optimization operates on a search space that has been massively restricted by the very greedy saliency scores the paper sets out to improve upon."** This is factually correct but the paper openly acknowledges it. Demoted from "fatal" to "major framing issue."

- **Strength Finder claim of "consistent downstream improvements across models and sparsity levels."** Not fully accurate — at 50% sparsity there are regressions. The strength has been qualified.

- **Strength Finder generic claim about the problem being important.** Removed as superficial.

- **Harsh critic nitpick about "which saliency scores are used to determine the fixed fraction when the warmstart is RIA."** This is a minor reproducibility detail already addressed by the paper's statement that Wanda scores are used for both warmstarts. Removed as speculative noise.

- **Harsh critic request for confidence intervals and standard deviations.** Removed — single-run evaluation is standard in LLM pruning benchmarks and the paper explicitly omits standard deviations for legibility.

## Novel Insights

The paper provides a crisp lens for understanding Wanda and RIA not as ad-hoc heuristics but as single-step greedy approximations to the mask-selection problem (Equations 4–7). This unification is genuinely clarifying and could influence how future work frames saliency-based pruning methods.

## Suggestions

- Reframe the contribution honestly in the abstract and introduction: SparseFW is a lightweight post-processing step that refines a mask initially produced by greedy heuristics, not a standalone replacement. The empirical story (10% optimization yields meaningful gains at high sparsity) is interesting on its own terms and does not need overclaiming.
- Include the constrained (α-parameterized) version in Algorithm 1 or a separate algorithm box, with precise pseudocode for the freezing procedure.
- Add a single SparseGPT comparison point (e.g., one model at 50% and 60%) to contextualize results, or provide a clear argument for why mask-selection-only methods should be evaluated separately.
- Discuss when SparseFW regresses (e.g., 50% sparsity on LLaMA-3) and provide guidance on when the additional compute is worthwhile.

---

**Calibration anchor comparison:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| CVXQ (0T8vCKa7yu) | 3.00 | R1 | Clearly weaker — fundamental formulation issues, poor comparisons |
| FISTAPruner (BINwUtUGuq) | 5.25 | R1/R2 | Most similar concept. SparseFW has cleaner framing and better evaluation but shares the "convex optimization for pruning" space. SparseFW is slightly stronger. |
| RotPruner (wV9iMiyQcc) | 5.33 | R2 | Different approach (rotated space pruning). SparseFW has stronger theoretical grounding; comparable empirical results. |
| OWL (pOBvr1PxFd) | 6.00 | R2 | Stronger empirical story, but had logical/circular-reasoning critiques. SparseFW's framing issue is more structural. OWL slightly edges ahead. |
| PruneNet (5RZoYIT3u6) | 6.00 | R1 | Good novelty, evaluation gaps. SparseFW's framing issue is more central to its claims. SparseFW is slightly below PruneNet. |

**Round 1 bracket:** 5.0–6.0. **Round 2 narrowing:** Comparing against FISTAPruner (5.25, slightly below SparseFW) and OWL/PruneNet (6.00, slightly above), the paper lands at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>