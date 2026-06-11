Now let me finalize the review with the complete output.

## Summary

This paper establishes a novel theoretical connection between GPTQ (an LLM weight quantization method) and Babai's nearest plane algorithm from lattice theory. The core result (Theorem 4) is that GPTQ, when executed back-to-front, is mathematically identical to Babai's algorithm applied to the lattice defined by the Hessian of a layer's inputs, without LLL basis reduction. This yields a geometric interpretation of GPTQ's error propagation as hyperplane projection and a tight layer-wise error bound under the no-clipping assumption. The paper also proposes practical no-clipping quantization methods (SSQR, HPTQ) and a CUDA kernel, with perplexity comparisons on Qwen3-8B.

## Strengths

- **Novel theoretical connection (Theorem 4).** The paper provides both a geometric proof and an algebraic proof showing that back-to-front GPTQ coincides exactly with Babai's nearest plane algorithm. The additional result that composing Babai and GPTQ yields no improvement (Section 4.3) confirms the equivalence is algebraically tight — neither algorithm can be strengthened by running the other on top. This is a genuinely non-obvious insight that reframes our understanding of a widely-used algorithm.

- **Clean geometric interpretation (Theorem 2, Corollary 3).** The paper shows OBQ's error propagation step is precisely Babai's hyperplane projection, and OBQ's dimension-selection rule (Eq. 1) minimizes the distance to the nearest hyperplane. This reframes GPTQ from an opaque algebraic procedure into an intuitive geometric "orthogonal walk" through nested subspaces — a genuine explanatory contribution that answers the open question of why the greedy per-weight rule works globally.

- **Tight error bound for the no-clipping regime (Theorem 5).** The bound relates the layer-wise quantization error to the diagonal **D** of the LDL decomposition of the permuted Hessian, and is tight (attained at hyper-cuboid corners). This gives GPTQ a worst-case guarantee in the no-clipping setting that prior work lacked.

- **Principled connection between quantization order and error (Section 4.5).** The paper shows quantization order directly controls the error bound through the **D** matrix, motivating the min-pivot heuristic (Algorithm 3) as a principled alternative to the heuristic act-order. The paper is honestly transparent that downstream gains are modest (line 219), which strengthens credibility.

## Weaknesses

### Major

- **Experimental evaluation for the practical methods is insufficient to support the claimed improvements.** The abstract states the new methods "outperform the original GPTQ," but the main text contains only one figure (Figure 4) with WikiText-2 perplexity. Three specific issues undermine the evaluation:

  (i) **Compositional inequality in bitwidth comparisons.** SSQR stores outliers separately in full precision (CSR format, line 251). The x-axis "Average Bitwidth" averages over variable-bitwidth representations, making the comparison against fixed-bitwidth GPTQ potentially unfair since SSQR uses additional storage for outliers that is not directly comparable to GPTQ's fixed-bitwidth format.

  (ii) **Speedup baseline choice.** The speedup comparison in Figure 4(c) is against PyTorch's BF16 matmul kernel, not against an optimized quantized inference kernel (e.g., GPTQ's grouped kernel or bitsandbytes). A ~2× speedup over BF16 is expected for any 4-bit kernel; this does not demonstrate that the SSQR representation provides advantages over existing quantized inference.

  (iii) **No variance reporting.** Perplexity numbers are reported without error bars, confidence intervals, or multiple seeds. For comparisons where differences may be small relative to the BF16 baseline, this is a significant omission.

  These issues collectively weaken the claim of having produced practically superior methods. The paper would be stronger if it either substantially expanded the experimental section or scoped back its practical claims.

### Minor

- **The equivalence requires back-to-front execution, while standard GPTQ runs front-to-back.** The paper is transparent about this condition (the abstract, lines 187-189, and Theorem 4 all state it explicitly). However, calling the direction difference "the only (superficial) difference" (line 187) understates the structural change: the LDL decomposition produces a lower triangular factor in one direction and an upper triangular factor in the other, meaning the algorithm that practitioners actually run (Algorithm 1 with **P** = **I**, iterating *j* ← 1 to *c*) is not the one whose theoretical guarantees are analyzed. The paper does not empirically characterize how much the front-to-back and back-to-front variants differ in practice — a simple experiment that would either validate the framing (if results are similar) or reveal a genuine gap.

- **The error bound (Theorem 5) applies only in the no-clipping regime (ℤ† = ℤ), excluding GPTQ's primary use case of clipped INT4 quantization.** The paper is honest about this limitation and discusses it in Section 5. However, this means the theoretical guarantee does not directly cover the regime where GPTQ is most commonly applied, and the bound offers no characterization of how quickly errors degrade under clipping. The future work discussion (line 275) partially mitigates this by noting that modern 4-bit floating-point formats (MXFP4, NVFP4) are essentially no-clipping.

- **The practical methods (SSQR, HPTQ) and the CUDA kernel are underdescribed in the main text.** SSQR discards SpQR's second-level scale quantization "for simplicity" (line 251), making it unclear whether improvements stem from the scale-adjustment mechanism or from using more bits for scale storage. The CUDA kernel receives only two sentences of description (line 269) — absent are details on tiling strategy, shared memory usage, or how sparse outliers interact with group-quantized inlier matmuls. This makes the kernel contribution hard to assess or reproduce.

### Trivial

None.

## Nice-to-Haves

- A direct empirical comparison between front-to-back GPTQ (standard) and back-to-front GPTQ on perplexity across several models/layers. If they produce similar results, the theory explains the actual algorithm de facto; if they diverge, characterizing the gap would itself be a useful analysis.
- A controlled experiment isolating the value of no-clipping (e.g., GPTQ with a wider INT8 grid that avoids clipping, compared against GPTQ with INT4 clipping, matched for total bit budget).
- Replacing the BF16 speedup baseline with an optimized quantized kernel baseline to demonstrate whether the SSQR representation offers specific advantages over existing quantized inference.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- "Equation 2 has a formatting error (missing bracket)": This is a parser artifact from PDF extraction, not an author error.
- "Babai error bound distinction assumes LLL reduction": The paper's Theorem 5 bound is self-contained via LDL decomposition and does not depend on LLL reduction. The standard Babai bound is cited purely for context.
- "Theorem 1 is nearly trivial": Formally establishing the quantization-CVP correspondence is necessary for the paper's logical flow. This is a framing choice, not a weakness.
- "Proof is too compressed for full verification": The full proof is in the appendix (stripped by parser). The main text proof sketch is appropriately compressed for a conference paper.
- "Expected error bound not justified in main text": The proof is deferred to Section D.2 in the appendix (stripped by parser).
- "Missing comparison with QuIP#, AQLM in main text": The paper references "comparison with other methods (Section E.5)" which the parser stripped. Whether these comparisons exist cannot be determined from the available text.
- "No downstream task evaluation in main text": The paper explicitly states Section E.3-4 contains benchmark results (stripped by parser). This is standard practice.
- "min-pivot results relegated to appendix": Relegating preliminary results to the appendix is standard practice for conference papers.
- Criticisms about the paper not addressing problems outside its stated scope (e.g., detailed analysis of clipping degradation beyond the scope of the current theory) are scope-creep.

## Novel Insights

The most substantive insight from the critical review is the tension between the paper's theoretical framing and its practical relevance. The direction-reversal issue (back-to-front vs. front-to-back) is structurally nontrivial because it changes the LDL factor from upper to lower triangular, corresponding to a different pivot sequence. The paper characterizes this as "superficial" but does not provide empirical evidence either way. This is the one point where a simple experiment — compare front-to-back GPTQ against back-to-front GPTQ on perplexity — would either validate the framing (if results are similar) or reveal a genuine gap between the theory and the algorithm practitioners use. The no-clipping limitation is similarly a real constraint that the paper acknowledges, but the future work discussion about MXFP4/NVFP4 being no-clipping regimes partially mitigates this concern. Overall, the paper's core theoretical contribution is sound and valuable; the main weakness is that the experimental section overreaches relative to the evidence it provides.

## Suggestions

1. Empirically compare front-to-back GPTQ against back-to-front GPTQ across several model sizes and layers to determine whether the direction difference matters in practice. This single experiment would clarify how much the theory explains the actual algorithm.
2. Add at least one downstream task accuracy result (e.g., MMLU, ARC) to the main text for HPTQ and SSQR.
3. Replace the BF16 speedup baseline in Figure 4(c) with an optimized quantized kernel baseline (e.g., GPTQ's grouped kernel or bitsandbytes).
4. Add error bars or multi-seed variance for perplexity results.
5. Provide a controlled ablation where GPTQ with a wide no-clipping grid is compared against GPTQ with INT4 clipping at matched total bits, to directly test the theory's prediction about the no-clipping regime.
6. Expand the CUDA kernel description (tiling strategy, shared memory usage, how sparse outliers interact with group-quantized inlier matmuls) to make it reproducible.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Low band (<3.5): Unrelated quantization/clustering papers (3.0-3.25) — our paper is clearly stronger.
- Middle band (3.5-7.5): DiscQuant (4.50), SPFQ (4.25), Pyramid VQ (5.00), LQ-LoRA (6.75)
- High band (>7.5): Unrelated generative compression papers (8.0) — not comparable.

**Round 2 — Narrowing (4.5-7.5):**
- *DiscQuant* (4.50): Quantization with discrepancy theory. Stronger experiments but its theory relies on low-rank gradient assumptions. **Our paper is stronger.**
- *Pyramid VQ* (5.00): Geometric quantization via spherical codes. Mixed reviews (8,6,1,5) with serious presentation issues. **Our paper is stronger.**
- *SpinQuant* (5.80): Learned rotation matrices. Strong experiments but incremental novelty. **Comparable; our paper has deeper theory but weaker experiments.**
- *LQ-LoRA* (6.75): Quantization + finetuning. Very strong experiments. **Our paper is below this anchor.**
- *OmniQuant* (6.40): Learnable quantization parameters. Extensive experiments. **Our paper is below this anchor.**
- *OSTQuant* (6.20): Orthogonal/scaling transforms. Strong experiments. **Our paper is below this anchor.**

The paper's genuine theoretical contribution places it above DiscQuant (4.50) and Pyramid VQ (5.00), and comparable to SpinQuant (5.80). However, the weak experimental evaluation for the practical claims prevents it from reaching the 6.2-6.75 range of empirically strong papers.

**Final score:** 5.5 — borderline accept. The theoretical contribution is genuine and well-argued, but the experimental evaluation issues (compositional inequality in bitwidth comparisons, speedup baseline choice, no variance reporting) are real and prevent a higher score. The paper would benefit from narrowing its practical claims or substantially strengthening the evaluation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>