Now I have a thorough understanding of the paper and can produce a consolidated review.

---

## Summary

This paper establishes a formal equivalence between GPTQ (executed back-to-front) and Babai's nearest plane algorithm for the closest vector problem on the lattice defined by the Hessian matrix of a linear layer's inputs. Building on this geometric interpretation, the authors derive a tight worst-case error bound for the no-clipping setting, propose two no-clipping quantization methods (SSQR and HPTQ), and provide a CUDA inference kernel for SSQR. The main text reports WikiText-2 perplexity results on Qwen3-8B showing HPTQ outperforming original GPTQ at matching average bitwidths.

## Strengths

1. **Formal theoretical connection between GPTQ and Babai's nearest plane algorithm (Theorem 4).** The paper rigorously shows that GPTQ run back-to-front coincides exactly with Babai's nearest plane algorithm without basis reduction. This is the first formal proof of this equivalence and provides a principled bridge between LLM quantization and lattice theory. The algebraic proof in Section C (referenced in the main text) substantiates this claim.

2. **Tight worst-case error bound for GPTQ under no-clipping (Theorem 5).** By inheriting Babai's approximation guarantee, the paper derives an absolute upper bound on the layer-wise quantization error (and a relative bound) that is proven tight. This gives the first formal global error certificate for GPTQ in the no-clipping regime.

3. **Empirical validation that no-clipping methods can outperform original GPTQ.** Figure 4a shows that HPTQ achieves lower WikiText-2 perplexity than GPTQ at the same average bitwidth on Qwen3-8B, and the 3.125-bit variant is identified as Pareto-optimal across multiple model sizes (Figure 4b). The SSQR kernel achieves ~2× end-to-end speedup over PyTorch BF16 on an RTX A6000 (Figure 4c).

4. **Geometric interpretation of OBQ/GPTQ error propagation (Theorem 2, Figures 2–3).** The visual and algebraic explanation of OBQ's local update rule as a Babai projection onto the nearest hyperplane provides useful intuition and clarifies why the greedy procedure works.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evaluation in the main text is too narrow to fully support the practical claims.** The main text reports perplexity on only one model (Qwen3-8B) and one dataset (WikiText-2). While the appendix apparently contains additional results (zero-shot evaluations, Llama models, further baselines), the key claim that the proposed methods "outperform the original GPTQ" would be better supported by including at least a summary of these additional evaluations in the main text. Moreover, comparisons with state-of-the-art methods that are directly related (SpQR, which motivates SSQR, and QuIP#, which also uses LDL-based quantization) are absent from the main figures. The paper's practical contribution would be significantly strengthened by showing how SSQR and HPTQ compare against these established approaches.

2. **HPTQ's practical utility is unclear without an inference kernel.** HPTQ uses variable-length Huffman coding to avoid clipping, but no inference kernel is provided for it. The paper compares average bitwidths, which is meaningful for memory footprint, but the practical advantage for end-to-end latency is unsubstantiated. A throughput discussion or comparison with existing quantization kernels (e.g., bitsandbytes, GPTQ's own kernel) would help contextualize the practical value.

### Minor

3. **The geometric proof sketch in Section 4.2 contains a simplification error.** The derivation of the error propagation coefficient ends with the expression `Δζ_{j₁} = (B^T B)^{-1}[j₁, j₂] Δζ_{j₂}`, but the correct simplification from the intermediate expression `⟨n_{j₁}, n_{j₂}⟩/⟨n_{j₂}, n_{j₂}⟩` should yield `(B^T B)^{-1}[j₁, j₂] / (B^T B)^{-1}[j₂, j₂] · Δζ_{j₂}` — the denominator in the OBQ update formula (Eq. 2) is dropped in the final simplified expression. The geometric argument's internal logic is preserved (the intermediate expression has the correct denominator), but the presentation error makes the sketch harder to follow. The full algebraic proof in the appendix likely resolves this, but the main text should be self-consistent.

4. **No comparison with QuIP's existing error bound.** The related work section notes that "QuIP (Chee et al., 2023) proves an error guarantee for GPTQ and proposes the LDLQ method as an equivalent variant of GPTQ," but the paper never states whether Theorem 5 is equivalent to, tighter than, or different from QuIP's bound. Since QuIP's analysis is the most closely related theoretical work, explicitly positioning the new bound relative to it would clarify the novelty of the analytical contribution.

5. **The connection between the error bound and the proposed methods is high-level.** The bound motivates avoiding clipping, and the methods are designed to avoid clipping, but the bound itself is never verified empirically (e.g., by computing the LHS and RHS for actual layers), nor is it used to guide any design decision beyond the "avoid clipping" principle. The min-pivot ordering is explicitly derived from the bound but yields "modest" accuracy gains, as the paper honestly acknowledges. The claimed "principled" improvement over GPTQ therefore rests more on the specific no-clipping engineering than on tight coupling with the theoretical analysis.

6. **The notation `N = B^{-T}` for a non-square matrix is a conventional abuse** but may confuse readers unfamiliar with dual-basis notation. A brief remark clarifying that this denotes the left-inverse transpose would improve accessibility. (The underlying geometric argument is sound.)

### Trivial
None.

## Nice-to-Haves
- **Empirically verify the error bound:** computing the LHS (actual quantization error) and the RHS of Theorem 5 for several layers would directly demonstrate the bound's tightness and illustrate the practical value of the theoretical analysis.
- **Compare the min-pivot ordering more thoroughly:** reporting how often min-pivot reduces tr(D) and whether certain layers see significant improvement would help assess its practical relevance.
- **Provide a throughput comparison for the SSQR kernel against existing quantized kernels** (e.g., GPTQ's own kernel, AWQ's kernel) rather than only against PyTorch BF16, which is a weaker baseline.

## Removed Points
- Criticisms about the corrupted LaTeX in Eq. (2) (missing bracket): parser artifact, not an author error.  
- Criticisms about the abstract "overstating complexity": subjective judgment, not a concrete weakness.  
- Criticisms about missing reproducibility details (batch size, calibration data, etc.): these are standard for papers that defer to appendix for setup; the appendix presumably contains them and the parser strips appendices.  
- Claim that the geometric interpretation is "not new" because Table 1 is a simple dictionary: the contribution is the full equivalence proof, not just Table 1.  
- Complaints that concurrent work (Birnick, 2025) exists: the paper acknowledges this in a footnote and still provides its own independent derivation.

## Novel Insights
The reviews do not surface any genuinely novel insight beyond the paper's own contributions. The observation that GPTQ run back-to-front is identical to Babai's nearest plane algorithm is the paper's central contribution and is correctly identified by both the harsh critic and strength finder. The missing-denominator observation in the proof sketch is a useful correction but not a novel insight in itself.

## Suggestions
1. Fix the simplification error in Theorem 2's proof (Section 4.2): the final expression should read `(B^T B)^{-1}[j₁, j₂] / (B^T B)^{-1}[j₂, j₂] · Δζ_{j₂}` to match Eq. (2).
2. Add a brief comparison with QuIP's error bound in Section 4.4, stating whether Theorem 5 is equivalent, tighter, or different.
3. Include a summary of the additional experimental results (zero-shot accuracy, Llama models, comparisons with SpQR/AWQ/QuIP#) in the main text rather than deferring entirely to the appendix.
4. Add a note clarifying that `B^{-T}` for a non-square matrix denotes the transpose of the left inverse (dual basis).
5. Discuss the practical implications of HPTQ's variable-length encoding for inference throughput, or acknowledge the limitation.

## Score and Decision

The paper makes a genuine theoretical contribution by establishing a formal equivalence between a widely-used LLM quantization method (GPTQ) and a classical lattice algorithm (Babai's nearest plane). The error bound, geometric interpretation, and proof of algorithmic redundancy add value beyond what was previously known. The practical methods show promising results within their evaluated scope.

However, the experimental validation in the main text is limited in breadth (one model, one dataset, no comparisons with several relevant SOTA methods), the proof sketch in Section 4.2 contains a presentation error that should be corrected, and the relationship to QuIP's existing bound is not clarified. These are addressable issues that do not undermine the core theoretical contribution but do temper the strength of the practical claims.

**Score:** 6.5 — a solid paper with a real theoretical contribution and reasonable practical validation, held back by narrow experiments and a presentation error in the main proof sketch.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>