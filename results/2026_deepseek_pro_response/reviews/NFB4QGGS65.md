Now I have a clear comparative picture. Let me finalize.

**Round 1 bracket confirmed: [5.0, 6.5]**

**Round 2 comparisons:**
- **Custom Gradient Estimators = STE (5.25, Reject)**: Proves approximate equivalence between algorithm classes. Current paper's equivalence is exact (not approximate), theory is more rigorous, and it has practical spinoffs. Current paper is **above** this.
- **Pyramid VQ (5.00, Reject)**: Lattice-based LLM quantization with theoretical claims described as "reformulation of known properties." Current paper's theory is more novel and rigorous. Current paper is **above** this.
- **SpinQuant (5.80, Accept)**: Learned rotations, strong empirical validation, limited theory. Current paper has much stronger theory but weaker experiments. Current paper is **below** this.
- **OSTQuant (6.20, Accept)**: New metric + method, SOTA experiments. Current paper is **below** this.

**Final Score: 5.5** — between STE (5.25) and SpinQuant (5.80). The paper's theoretical insight (GPTQ = Babai) is genuinely novel and more rigorous than STE's approximate equivalence. But two Major weaknesses (back-to-front order gap, insufficient QuIP differentiation) and thin empirical evidence in the main body prevent it from reaching the SpinQuant/OSTQuant tier. **Decision: Reject** — the paper would benefit from addressing the Major weaknesses before acceptance.

---

## Summary

This paper proves that GPTQ, when executed back-to-front, is mathematically identical to Babai's nearest plane algorithm for the closest vector problem (CVP) on the lattice defined by a linear layer's Hessian. The key insight is Theorem 2: OBQ's error propagation step is exactly Babai's projection of the residual target onto the nearest hyperplane. This equivalence yields a tight layer-wise error bound (Theorem 5) and motivates two no-clipping quantization methods (SSQR and HPTQ) that outperform standard GPTQ on WikiText-2 perplexity, along with a custom CUDA inference kernel.

## Strengths

- **Theorem 2 provides a genuinely novel geometric interpretation of GPTQ's core mechanism**: The proof constructs the inverse basis N = B^{-T}, projects the error onto the orthogonal projection plane, and derives Δζ_{j_1} = (B^T B)^{-1}[j_1, j_2] / (B^T B)^{-1}[j_2, j_2] · Δζ_{j_2}, matching OBQ's error propagation formula exactly (Eq. 2). This geometric decomposition — illustrated in Figure 2 — transforms what was previously an opaque algebraic update into an intuitive nearest-hyperplane projection. This is the paper's central insight and it is both correct and elegant.

- **Theorem 5 delivers a concrete, computable error bound tied directly to the LDL decomposition**: The bound ‖X diag(s_i) z_i − X w_i‖² ≤ ¼ (T^{-1} s_i)^T D (T^{-1} s_i) is expressed in terms of the diagonal matrix D from the LDL decomposition of the permuted Hessian. The bound is stated with both absolute and relative forms, tightness is properly qualified (worst-case equality at hyper-cuboid corners), and the expected error reduction to ⅓ of worst-case is derived. The bound is directly computable from layer statistics.

- **The CVP dictionary (Table 1) and the invariance result (Theorem 1) systematically bridge two previously separate fields**: The mapping is complete — activations X become basis directions, scales s_i become basis stretches, weights w_i become floating-point coordinates, and quantized integers z_i become lattice coordinates. Theorem 1 shows that any Hessian factor X yields an equivalent CVP up to orthogonal transformation, justifying the use of computationally cheaper square factors.

- **HPTQ achieves the best perplexity-compression tradeoffs among compared methods (Figure 4)**: On Qwen3-8B, HPTQ sustains the lowest WikiText-2 perplexity across bitwidths compared to RTN, GPTQ, HRTN, and SSQR. The method scales cleanly from 0.6B to 14B models, with 3.125-bit identified as Pareto optimal.

- **Corollary 3 gives OBQ's dimension selection a crisp geometric meaning**: The criterion argmin_j (q_i[j] − w_i[j])² / (X^T X)^{-1}[j,j] simplifies to argmin_j |Δζ_j| / ‖n_j‖ — selecting the dimension whose nearest hyperplane is closest to the residual target.

## Weaknesses

### Fatal

None.

### Major

- **The back-to-front order requirement creates a gap between the theory and the practical methods**: The paper's central equivalence (Theorem 4) requires GPTQ to run from the last to first dimension, while standard GPTQ runs front-to-back. The paper acknowledges this (Abstract, Section 4.3) and calls it "superficial," but the gap is substantive: the LDL factor and error propagation direction genuinely depend on the order. The experiments (Section 5) use act-order — "the descending order of the Hessian diagonal, i.e., the ascending order of the Hessian diagonal when applied to Babai's algorithm" (Section 4.5) — but the paper does not empirically verify that act-order in standard GPTQ produces results consistent with the back-to-front Babai equivalence. The practical methods (SSQR, HPTQ) are motivated by the no-clipping insight rather than by the specific ordering guarantee, which weakens the claimed theory-to-practice link. This matters because the abstract and introduction present the equivalence as characterizing GPTQ generally, when it in fact characterizes a specific variant.

- **Insufficient differentiation from QuIP / LDLQ**: The Related Work mentions that "QuIP (Chee et al., 2023) proves an error guarantee for GPTQ and proposes the LDLQ method as an equivalent variant of GPTQ" but provides only this single sentence. The paper does not explain what QuIP's error guarantee covers, how it differs from Theorem 5, whether LDLQ already admits a CVP interpretation, or what is genuinely novel beyond QuIP's prior equivalence. Given that QuIP and its descendants (QuIP#) are the natural lattice-inspired baselines, this omission makes it difficult for the reader to assess the paper's novelty relative to the most relevant prior work. This is a significant gap in situating the contribution within the literature.

### Minor

- **The error bound (Theorem 5) is never empirically validated**: The paper imports Babai's bound and uses it to conceptually motivate no-clipping methods, but never measures actual quantization errors against the bound — e.g., plotting the bound vs. observed error across layers. The theory-to-application connection therefore operates at the level of conceptual motivation rather than operational guidance.

- **The empirical story in the main text is thin**: Figure 4 (WikiText-2 perplexity on Qwen3, scaling behavior, kernel speedup) is the sole empirical figure in the main paper. All zero-shot benchmark results, Llama model comparisons, and method-vs-method tables are relegated to the appendix. For a paper that includes "Applications" as a titled section with two new methods and a CUDA kernel, more empirical support in the body would strengthen the case.

- **The CUDA kernel baseline is weak**: Figure 4c compares the custom SSQR kernel against PyTorch BF16 matrix multiplication. For a custom CUDA kernel targeting Ampere GPUs, the natural baseline would be an optimized FP16/BF16 matmul from cuBLAS, not a PyTorch wrapper. The ~2× speedup claim would be more convincing against a stronger baseline.

- **HPTQ's Huffman decoding overhead is not discussed**: The paper focuses on compression ratio but does not address the latency cost of Huffman decoding during inference, which matters for practical deployment.

### Trivial

- Algorithm 1 line 10 uses L[j,:] ε to propagate error. L from LDL(H^{-1}) is lower triangular, so L[j,:] has nonzeros only in columns 1...j. With front-to-back iteration (j=1 to c), this update pattern should be clarified relative to the comment about affecting "not-yet-quantized rows."

## Nice-to-Haves

- Empirically validate Theorem 5's bound against observed quantization errors on at least one model to transform the bound from a theoretical curiosity into a practical tool.
- Compare the SSQR CUDA kernel against cuBLAS BF16/FP16 rather than only PyTorch BF16.
- Include a comparison against QuIP or QuIP# in the experimental results, or at minimum summarize such results in the main text if they exist in the appendix.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Theorem 1 is overstated as a theorem"** — Mathematical papers routinely label simple observations as theorems. The proof is correct and the result is useful (it justifies using square Hessian factors). This is a pure style nitpick.
- **"The 'tight' claim for the error bound needs qualification"** — The paper already properly qualifies tightness: "Equality is attained when the target y lies at the corner of the hyper-cuboid, so the bound is tight" (Section 3.2). The distinction between worst-case and practical tightness is clear.
- **"No comparison with QuIP/# or other lattice-inspired quantizers in experiments"** — Folded into the Major QuIP differentiation weakness above; the issue is primarily about theoretical positioning, not missing experimental baselines.
- **Pseudocode error claim about L[j,:] affecting already-quantized rows** — Retained as Trivial after verifying: the L from LDL is indeed lower triangular, making the comment about "not-yet-quantized rows" potentially imprecise, but this doesn't affect the theoretical results.

## Novel Insights

The most productive way to understand this paper is as a two-part contribution with a tension at the joint. The theoretical half (Sections 3–4) establishes an airtight equivalence between back-to-front GPTQ and Babai's algorithm, yielding a clean geometric picture and a computable error bound. The applications half (Section 5) proposes practical no-clipping methods motivated by the theory's implications. The tension is that the practical methods (act-order, SSQR, HPTQ) do not directly inherit the theoretical guarantees — the order is different, the bound is unvalidated, and the motivation is conceptual rather than operational. The paper's value lies primarily in the theoretical insight (the geometric interpretation and the Babai connection), with the practical methods serving as evidence that the lattice perspective can inspire useful designs, even if the connection remains looser than the paper suggests.

## Suggestions

- Add a paragraph explicitly comparing Theorem 5 to QuIP's error guarantee: what quantity does each bound, under what assumptions, and what is the relationship to LDLQ.
- Run one experiment measuring actual per-layer quantization error against the bound from Theorem 5, and report whether the bound is loose or tight in practice.
- Clarify in the experiments section whether act-order in the practical methods corresponds to the back-to-front Babai ordering (as Section 4.5 suggests) by explicitly stating the mapping and ideally verifying it empirically.
- Move at least one zero-shot benchmark table (e.g., MMLU results) from the appendix into the main text to strengthen the empirical case for HPTQ/SSQR.

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| orG37FHN4b (Angle-DFQ) | 3.00 | R1 | Below — purely empirical data-free quantization, no theoretical equivalence |
| 0T8vCKa7yu (CVXQ) | 3.00 | R1 | Below — convex optimization framing, limited theoretical novelty |
| mJ8k81O5BF (Improving Low-Bit PTQ) | 3.00 | R1 | Below — data-free PTQ, no deep theory |
| vw0NurJ7UX (PrefixQuant) | 3.00 | R1 | Below — practical outlier handling, no theoretical contribution |
| ZBlfjXubgG (Pyramid VQ) | 5.00 | R1/R2 | Below — also lattice+LLM, but theory described as "reformulation of known properties"; current paper's Babai equivalence is more novel |
| sfTsvy05MX (LL-VQ-VAE) | 4.75 | R2 | Below — lattice VQ for images, not LLMs; less theoretical depth |
| 3j72egd8q1 (Custom Grad Estimators = STE) | 5.25 | R2 | Comparable — both prove algorithm equivalences; current paper's equivalence is exact, STE paper's is approximate; current paper slightly stronger |
| rUx0zQFwD1 (Quantum Speedups LP) | 5.33 | R2 | Not comparable — different domain |
| ogO6DGE6FZ (SpinQuant) | 5.80 | R1/R2 | Above current — stronger empirical validation, weaker theory; current paper below due to order gap and thinner experiments |
| rAcgDBdKnP (OSTQuant) | 6.20 | R1/R2 | Above current — similar theory-to-practice gap but much stronger experiments |
| BifeBRhikU (PB-LLM) | 6.75 | R2 | Above — strong empirical results across many settings |
| bVTM2QKYuA (Representation Geometry) | 6.75 | R2 | Not directly comparable — geometry of LLM representations, different contribution type |

Round 1 bracket: [5.0, 6.5]. Round 2 narrowed to [5.0, 5.8]. Final score set at 5.5 — between STE (5.25) and SpinQuant (5.80), reflecting stronger theory than the former but weaker empirical validation and the back-to-front/QuIP gaps that prevent reaching the latter tier.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>