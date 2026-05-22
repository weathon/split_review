Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper establishes a mathematical equivalence between GPTQ (executed back-to-front) and Babai's nearest plane algorithm for the closest vector problem on a lattice defined by the input Hessian. From this equivalence, the authors derive a tight absolute error bound for no-clipping quantization, propose heuristics for quantization order (min-pivot), and introduce two practical overflow-tolerant quantization schemes (SSQR and HPTQ) together with a CUDA inference kernel. The core theoretical contribution — the GPTQ-Babai equivalence — is genuine, novel, and well-supported.

## Strengths

- **GPTQ-Babai equivalence (Theorem 4):** The paper provides both geometric (Section 4.2/4.3, Figure 2) and algebraic (Appendix B/C) proofs that GPTQ run back-to-front is mathematically identical to Babai's nearest plane algorithm without basis reduction. The proof is rigorous, and the equivalence is shown to be tight — an extra GPTQ-style update after Babai is proven redundant (Section C.4). This places a widely-used practical algorithm on firm theoretical footing.

- **Tight absolute error bound (Theorem 5):** Leveraging the equivalence, the paper imports Babai's absolute guarantee to obtain a tight layer-wise error bound expressed as a quadratic form \(\frac{1}{4}(\mathbf{T}^{-1}\mathbf{s}_i)^\top\mathbf{D}(\mathbf{T}^{-1}\mathbf{s}_i)\), where \(\mathbf{D}\) comes from the LDL decomposition of the permuted Hessian. This bound is correctly derived and practically meaningful.

- **Practical no-clipping methods that outperform GPTQ:** HPTQ achieves lower WikiText-2 perplexity than RTN and original GPTQ on Qwen3-8B across bitwidths (Figure 4a), and 3.125-bit emerges as Pareto-optimal when scaled across model sizes (Figure 4b). SSQR provides a scale-adjustment mechanism to control outlier sparsity. Both methods are motivated by the no-clipping assumption required by the error bound.

- **Geometric interpretation of OBQ's dimension selection (Corollary 3):** The paper provides geometric intuition for why OBQ's greedy index choice works: it selects the dimension whose nearest hyperplane is closest to the target residual. This is an elegant insight.

- **Principled quantization order (min-pivot):** The paper analyzes how quantization order affects the error bound and proposes the min-pivot LDL heuristic, which consistently reduces \(\operatorname{tr}(\mathbf{D})\) relative to act-order. The authors are appropriately modest about the downstream accuracy gains, presenting it as a principled alternative.

- **CUDA kernel demonstration:** The SSQR-compatible kernel achieves approximately 2× speedup over PyTorch BF16 matrix multiplication for Qwen3-8B on an NVIDIA RTX A6000, validating that the no-clipping representation can be run efficiently.

## Weaknesses

### Fatal

None. The core equivalence result and absolute error bound are sound.

### Major

- **Relative error bound claim in Theorem 5 is unjustified.** The paper states a relative bound \(\gamma \leq \sqrt{1 + \max_j \frac{\sum_{i'=1}^{j-1} d_j^2}{d_j^2}} \leq \sqrt{c+1} \cdot \max_{j'\leq j} \frac{d_{j'}}{d_j}\) as a guarantee on the approximation ratio to the optimal CVP solution. This bound is imported from Babai (1986), where it is proven *only* for LLL-reduced bases. The paper explicitly states (in the introduction and Theorem 4) that GPTQ runs *without LLL basis reduction*. Without LLL reduction, Babai's algorithm does not guarantee any constant or subexponential approximation to the optimal CVP solution — indeed, CVP is NP-hard to approximate within constant factors. Presenting this formula as a guaranteed relative error bound against the optimal quantizer is incorrect without further justification. The absolute bound is unaffected and remains valid. **Remedy:** Either remove the relative bound claim, qualify it carefully (e.g., as an algebraic expression of the algorithm's error rather than a guarantee against the optimum), or prove that it holds under weaker conditions.

- **Damping term (\(\lambda\)) is ignored in the theoretical analysis.** GPTQ (Algorithm 1, line 1) computes the Hessian as \(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}\) with typical \(\lambda = \frac{1}{100c}\|\mathbf{X}\|_F^2\). All theoretical results in Section 4 use the undamped Hessian. The paper never discusses whether the equivalence holds (even approximately) with damping, nor does it analyze how damping modifies the error bound. While \(\lambda\) is typically small, the gap between the idealized theory and the actual algorithm should be acknowledged. **Remedy:** Add a discussion of how damping affects the analysis — for instance, bounding the perturbation introduced by \(\lambda\), or arguing that the equivalence holds approximately when \(\lambda\) is small relative to the Hessian spectrum.

### Minor

- **Theory-to-practice link is at the motivational level, not derivational.** The abstract states "Leveraging this bound, we design post-training quantization methods that avoid clipping." The bound does motivate the no-clipping approach, but the specific design choices in SSQR (binary search over per-group scales) and HPTQ (entropy-guided search) are not directly derived from the bound. The framing overstates the tightness of the connection. The paper would be stronger if this claim were softened or if concrete derivational links were provided (e.g., using the bound to guide scale selection).

- **Limited experimental evaluation in the main body.** Only WikiText-2 perplexity appears in the main text (Figure 4). Zero-shot benchmarks are deferred to the appendix (which is standard for theory papers, but this paper also presents practical methods). Comparisons with recent competitive PTQ schemes (e.g., QuIP, AWQ) under comparable bit budgets would help contextualize the practical contribution. The paper's focus is primarily theoretical, so this is not a major concern, but it weakens the practical claims moderately.

- **Theorem 2 exposition is dense.** The geometric proof in Section 4.2 relies heavily on complex 3D/2D figures (Figure 2) with many symbolic definitions (inverse basis vectors, projected lengths, orthogonal projection planes). The in-text sketch is difficult to follow. While the full algebraic derivation is in the appendix, the geometric exposition would benefit from simplification or a more accessible walk-through.

### Trivial

- The CUDA kernel is implemented only for SSQR, which underperforms HPTQ in accuracy (Figure 4a). A kernel for the better HPTQ method would strengthen the practical contribution, though this is a nice-to-have rather than a flaw.

## Nice-to-Haves

- Illustrate the tightness of the absolute error bound with a synthetic or real layer example (e.g., showing that the bound can be approached in practice).
- Provide a more detailed comparison of min-pivot vs. act-order in the main text (the data is in Appendix D.3).
- Discuss computational overhead of Huffman decoding for HPTQ inference to give a more balanced view of the practical methods.
- Extend the CUDA kernel to support HPTQ.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Theorem 2 proof is insufficient."** REMOVED — The paper explicitly states the full proof is in the appendix (which is stripped by the parser). The in-text sketch, while dense, serves its purpose of conveying geometric intuition. The appendix contains the complete algebraic derivation. This is standard practice for theory papers.

- **Harsh critic: "Min-pivot never directly compared with act-order in experiments."** REMOVED — The paper states (Section 4.5): "Across our preliminary runs (Section D.3), min-pivot consistently reduces tr(D) relative to act-order, but the downstream accuracy gains are modest." The comparison exists in the appendix. The paper is appropriately modest about the gains.

- **Harsh critic: "Experimental justification is thin; zero-shot benchmarks deferred to appendix."** PARTIALLY RETAINED as Minor — this is a reasonable observation for a paper with practical claims, but framed as a moderate concern rather than a fatal flaw. It is common for theory-focused papers to place extended experiments in the appendix.

- **Strength Finder: "Efficient CUDA kernel achieving 2× inference speedup."** RETAINED as a strength but noted that it only supports SSQR.

- **Strength Finder: generic strengths about "the problem being important."** REMOVED — these are not specific to the paper.

## Novel Insights

None beyond the paper's own contributions. The equivalence between GPTQ and Babai's algorithm is itself the novel insight, and it is the paper's central contribution.

## Suggestions

- **Address the relative bound issue concretely.** Either (a) prove that the bound holds without LLL reduction for the specific lattice structure arising from Hessian matrices, (b) qualify the claim by stating it holds only when the Hessian is "well-conditioned" in a specific sense, or (c) remove the relative bound and focus on the absolute bound, which is sufficient to motivate the no-clipping methods.
- **Add a paragraph on damping.** Even a short discussion acknowledging that the equivalence holds for the undamped Hessian and that the perturbation from practical damping levels is small (with a brief justification) would close a noticeable gap.
- **Tone down the "leveraging this bound" language** in the abstract and introduction. Replace with phrasing like "Motivated by the no-clipping requirement of this bound, we design..." to accurately reflect the relationship between theory and practice.
- **Bring one representative zero-shot benchmark into the main text** (e.g., a table with a few key tasks) to strengthen the practical claims without bloating the paper.

## Score and Decision

**Anchor comparison:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `orG37FHN4b` (Angle-DFQ) | 3.00 | R1 (weak) | Clearly weaker — limited theoretical depth |
| `0T8vCKa7yu` (CVXQ) | 3.00 | R1 (weak) | Clearly weaker — less novel theory |
| `vJmpg0exYA` (DiscQuant) | 4.50 | R1 (mid) | Weaker — theory relies on strong low-rank assumptions; current paper's equivalence is cleaner |
| `ZBlfjXubgG` (PVQ for LLMs) | 5.00 | R1 (mid) | Weaker — mixed reviews, presentation issues, less rigorous theory |
| `MF7ljU8xcf` (LLMs Generalize Better) | 6.00 | R2 (narrow) | Comparable — both have genuine theoretical contributions with some limitations; this paper's theory is more definitive (proven equivalence vs. bounds) |
| `rAcgDBdKnP` (OSTQuant) | 6.20 | R2 (narrow) | Slightly stronger — more extensive experiments across models/settings, but its theoretical framework has more questionable assumptions |
| `xw29VvOMmU` (LQ-LoRA) | 6.75 | R2 (narrow) | Stronger — more polished with stronger experiments |
| `wg1PCg3CUP` (Scaling Laws for Precision) | 8.00 | R1 (strong) | Clearly stronger — extensive experiments (465+ runs), unified framework |

**Round 1 bracket:** 5.0 – 7.0 (above DiscQuant/PVQ, below Scaling Laws/CBQ).

**Round 2 narrowing:** The paper sits near the 6.0 anchor ("Larger Language Models Provably Generalize Better") — both are theory papers with genuine contributions and acknowledged limitations. The current paper's theoretical result (a proven equivalence) is cleaner than the 6.0 anchor's bounding approach, but it has the specific relative-bound issue that needs correction. It is slightly below OSTQuant (6.20) due to thinner experiments and the relative-bound problem.

**Final score: 5.5.** The relative error bound claim is a genuine error that must be corrected. The core contributions (equivalence proof, absolute bound, practical methods) remain valid and interesting, and the issues are fixable in revision. The paper makes a real contribution to understanding GPTQ through a lattice-theoretic lens.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>