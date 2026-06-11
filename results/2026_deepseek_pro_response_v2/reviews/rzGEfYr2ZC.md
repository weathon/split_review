Now I have a clear calibration picture. Let me finalize the review.

**Calibration summary across all rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| CVXQ (convex quantization) | 3.00 | R1 | Much weaker — different problem, incomplete method |
| FISTAPruner (convex pruning, LASSO+FISTA) | 5.25 | R1 | Most similar anchor. Our paper has stronger theory, cleaner method, better analysis of baselines |
| PruneNet (calibration-free pruning) | 6.00 | R1/R2 | Our paper has stronger theoretical grounding, broader model set |
| OWL (non-uniform sparsity) | 6.00 | R2 | Different angle; our theory is stronger |
| Double Sparse Factorization | 6.33 | R2 | Different paradigm; our theory is stronger |
| Unreasonable Ineffectiveness (layer pruning) | 6.50 | R2 | Empirical study; our paper has more technical depth and theory |
| Probe Pruning (dynamic pruning) | 7.00 | R2 | Stronger practical novelty and experiments; our theory is stronger but framing issue holds us back |

**Bracket (R1):** 6.0–7.5 → **Narrowed (R2):** Our paper is above Unreasonable Ineffectiveness (6.50) in technical depth but below Probe Pruning (7.00) in practical comprehensiveness. **Final score: 6.5**.

---

## Summary
This paper proposes SparseFW, a layerwise LLM pruning method that relaxes the combinatorial mask-selection problem into a convex program over the convex hull of binary masks, then solves it with the Frank-Wolfe algorithm. The method outperforms Wanda and RIA baselines on WikiText perplexity and zero-shot accuracy across five GPT model families, particularly at higher sparsity levels (60%, 2:4). The paper also provides theoretical approximation guarantees (Lemma 1) and a useful analysis connecting Wanda/RIA to single-weight greedy optimization.

## Strengths
- **Clean convex relaxation of mask selection**: Reformulating the combinatorial binary-mask problem as optimization over the convex hull C_k (Equation 10, Figure 1) is principled and makes the problem amenable to first-order convex optimization via FW. This is a genuinely novel approach in the LLM pruning space.
- **Theoretical approximation guarantees**: Lemma 1 provides a formal error bound decomposing into optimization error (vanishes as ~k/T) and thresholding error. The theory successfully explains empirical dynamics in Figure 4, where thresholded mask error initially degrades before improving, matching the predicted threshold-residual behavior.
- **Elegant analysis of prior methods**: Section 2.1 derives Wanda's saliency score directly from a single-weight greedy pruning objective (Equation 5), showing Wanda is equivalent to iteratively selecting the weight that minimizes per-weight error without modifying remaining weights. RIA is similarly shown to be Wanda applied to a rescaled weight matrix. This reframes heuristically-motivated methods as principled (if myopic) optimization steps and is a genuine contribution independent of the FW method.
- **Consistent zero-shot accuracy gains**: SparseFW improves zero-shot accuracy over Wanda and RIA in nearly every (model, sparsity, warmstart) configuration tested, including at 50% sparsity where perplexity gains are mixed.
- **Memory-efficient design**: Precomputing G = XX^T and H = WG reduces the relevant matrix dimension from d_in × (N·L) to d_in × d_in, making per-iteration FW cost independent of sequence length and sample count (Section 2.3). This enables using larger calibration sets, which Figure 3 shows continues to improve perplexity.
- **Honest treatment of limitations**: The paper explicitly acknowledges that pure FW (α=0.0) yields worse perplexity than baselines despite better local reconstruction (Section 2.3), and the conclusion is appropriately cautious about the local-global objective mismatch.

## Weaknesses

### Fatal
None.

### Major
- **Framing mismatch between narrative and deployed method**: The abstract and introduction present SparseFW as an alternative to greedy heuristics that accounts for weight interactions. However, the deployed method (α=0.9) fixes 90% of the mask using Wanda saliency scores and applies FW only to the remaining 10% (Section 2.3). Pure FW (α=0.0) consistently underperforms baselines. While the paper is honest about this in Section 2.3 and the conclusion, the framing in the abstract and introduction does not reconcile with the fact that the method as deployed is a post-hoc refinement on top of Wanda. The contribution would be stronger and more credible if reframed as "Wanda + FW refinement." This does not invalidate the paper's results but weakens the central narrative.

### Minor
- **Duplicate Wanda/RIA accuracy rows in Table 1**: The 60% sparsity zero-shot accuracy rows for Wanda and RIA are identical across all six models (63.19 / 53.7 / 50.51 / 59.44 / 63.58 / 48.08). This is almost certainly a copy-paste error and should be corrected.
- **SparseGPT excluded from experiments**: The paper compares only to Wanda and RIA, arguing (line 192) that SparseGPT combines mask selection with weight reconstruction while SparseFW focuses on mask selection only. This scope decision is defensible, but SparseGPT is the field's standard baseline and including it would substantially strengthen the empirical contribution.
- **Theory-practice gap in Lemma 1**: The bound applies to the pure FW method (α=0.0), which the paper shows performs worse than baselines. The α=0.9 hybrid that produces the paper's results has no theoretical characterization. The paper would benefit from explicitly discussing this mismatch when presenting the theory.
- **Mixed perplexity at 50% sparsity**: At 50% unstructured sparsity, SparseFW loses to Wanda on DeepSeek-7B (Wanda 7.79 vs. SparseFW 7.89/7.93) and LLaMA-3.1-8B (Wanda 10.09 vs. SparseFW 10.21) in perplexity. The paper acknowledges that gains are larger at higher sparsity, but the "consistent gains" phrasing in the introduction slightly overstates the 50% results.

### Trivial
- Algorithm 1 omits the α mechanism, making it an incomplete specification of the method; noted as "for simplicity" but a reader implementing from Algorithm 1 would not reproduce results.
- Minor inconsistency: abstract reports "up to 80%" error reduction (line 39) while the contributions list reports "up to 70%" (line 44).
- The thresholding error floor in Lemma 1 (~k + sqrt(2·d_in·d_out·k)) may be large for LLM layers; the paper does not compute this for any concrete layer.

## Nice-to-Haves
- Include SparseGPT as a baseline, or at minimum discuss expected comparison outcomes.
- Provide wall-clock time or FLOP analysis to contextualize additional compute cost of FW iterations vs. one-shot Wanda/RIA.
- Analyze which specific weights FW changes relative to the Wanda warmstart to illuminate systematic patterns.
- Compute the theoretical bound from Lemma 1 for a concrete layer to assess tightness.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh critic: method "contradicts core premise" as fatal flaw** → Removed as fatal. The paper honestly reports pure FW underperforms (Section 2.3). The issue is a framing/narrative mismatch, not deception or contradiction. Retained as major weakness about framing.
- **Harsh critic: identical Wanda/RIA rows "undermine confidence in all reported numbers"** → Demoted. The duplicate rows are a table error but do not affect SparseFW comparisons; extrapolating to all results is speculative overreach.
- **Harsh critic: SparseGPT exclusion as "methodological gap" weakening contribution significantly** → Weakened to minor. The paper provides a clear scope justification. An ideal paper would include SparseGPT but its absence does not invalidate the mask-selection comparison to Wanda/RIA.
- **Harsh critic: missing appendix content (α ablation, proofs)** → Removed per hard rules. The appendix is stripped from the review copy; its absence is a parser artifact, not an author error.
- **Harsh critic: compute cost analysis missing** → Moved to nice-to-haves.
- **Harsh critic: "80% vs 70%" inconsistency is "overstated"** → The paper shows both continuous (80%) and thresholded (~40%) error reduction in Figure 4. The abstract reports continuous mask reduction which is accurate but could be clearer. Retained as trivial.
- **Strength Finder: generic strength about "important problem"** → Removed as generic.

## Novel Insights
The most insightful observation from the review synthesis is that the paper's strongest contribution may not be the FW method itself but the reframing of Wanda and RIA as special cases of single-weight greedy optimization (Section 2.1). This analysis makes explicit what was implicit in prior work — that Wanda and RIA are optimal for a myopic, one-weight-at-a-time objective — and provides a clear conceptual foundation for why accounting for weight interactions should theoretically help. The tension between this theoretical insight and the practical necessity of fixing 90% of weights via Wanda saliencies (α=0.9) is the most interesting open question the paper surfaces: why does local optimization of weight interactions harm global performance, and what does this reveal about LLM loss landscape structure?

## Suggestions
- Reframe the paper as "Wanda + FW refinement" rather than as a standalone alternative to greedy methods. Move the α parameter from a caveat (Section 2.3 paragraph) to a central design choice with dedicated analysis.
- Correct the duplicate Wanda/RIA accuracy rows in Table 1 and reconcile the "up to 80%" vs. "up to 70%" discrepancy.
- Add the α mechanism to Algorithm 1 or clearly explain its omission.
- Include SparseGPT in at least one comparison table for context, even if outside the main mask-selection scope.
- Discuss the theory-practice gap explicitly: what Lemma 1 implies for the 10% of weights FW actually optimizes, given α=0.9.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>