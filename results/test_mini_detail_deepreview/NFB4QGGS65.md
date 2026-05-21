Now I have enough calibration data. Let me write the consolidated review.

## Summary

This paper provides a geometric reinterpretation of GPTQ, showing that when executed back-to-front (from the last to the first dimension), GPTQ is mathematically identical to Babai's nearest plane algorithm for the closest vector problem on a lattice defined by the layer's Hessian. From this equivalence the paper derives a tight layer-wise error bound (Theorem 5) under the no-clipping setting, proposes a min-pivot ordering heuristic based on this bound, and presents no-clipping quantization methods (SSQR, HPTQ) with a CUDA kernel. The theoretical contribution is genuinely novel and significant; the empirical component is suggestive but incomplete in several respects.

## Strengths

- **Theorem 4 (GPTQ ≡ Babai's nearest plane, Section 4.3):** The paper proves that GPTQ, when run back-to-front, coincides exactly with Babai's nearest plane algorithm without basis reduction. This is the first principled geometric explanation for why GPTQ's greedy updates produce globally coherent results. The proof is given both geometrically (Theorem 2 builds the connection via OBQ's error propagation) and algebraically (sketched in Section 4.3, deferred to Appendix C for full detail). This is a genuinely novel insight about a widely-used algorithm.

- **Theorem 5 (Error bound, Section 4.4):** From the Babai equivalence, the paper inherits a tight worst-case error bound for GPTQ in the no-clipping setting. The absolute bound is $\frac{1}{4}(\mathbf{T}^{-1}\mathbf{s}_i)^\top\mathbf{D}(\mathbf{T}^{-1}\mathbf{s}_i)$ and the relative bound is $\gamma \leq \sqrt{c+1}\cdot\max d_{j'}/d_j$. This is the first error guarantee for GPTQ that directly follows from the algorithm's structure rather than being an independent analysis.

- **Geometric interpretation of OBQ/GPTQ (Theorem 2, Corollary 3, Section 4.2):** The paper gives a clean geometric picture: OBQ's error propagation step (Eq. 2) is exactly Babai's nearest-hyperplane projection, and OBQ's dimension selection rule (Eq. 1) chooses the dimension whose nearest hyperplane is closest to the current residual. This reframes previously opaque algebraic updates as natural geometric operations.

- **Practical improvement over GPTQ (Figure 4, Section 5):** HPTQ achieves lower perplexity than original GPTQ across multiple bitwidths on Qwen3-8B, and SSQR with 1–5% outliers also improves over GPTQ. The CUDA kernel delivers approximately 2× end-to-end speedup vs PyTorch BF16, demonstrating that the no-clipping design can be realized in efficient inference hardware.

## Weaknesses

### Major

- **Ordering ambiguity between theory and experiments (Section 5):** The theoretical equivalence (Theorem 4) requires GPTQ to run **back-to-front** (dimension $c \to 1$). The error bound (Theorem 5) also assumes this order. However, the experimental section states only "The quantization order is act-order for all methods" without specifying whether the GPTQ loop runs front-to-back ($j=1\to c$) or back-to-front ($j=c\to 1$). The paper discusses in Section 4.5 that act-order (descending Hessian diagonal in GPTQ's front-to-back convention) corresponds to "the ascending order of the Hessian diagonal when applied to Babai's algorithm," but it never explicitly states loop direction in the experiments. If the experiments run GPTQ in its standard front-to-back mode with act-order, the theoretical equivalence and bound do not directly apply. The authors must clarify this and justify the alignment or restructure the experiments to match the theoretical setting.

- **Missing no-clipping GPTQ baseline (Section 5):** The paper claims that "enforcing no-clipping by simply increasing scales is counterproductive: larger scales enlarge the bound, and the resulting errors can exceed those of a clipped scheme such as MSE." However, **no experimental evidence is provided** for this claim. A direct comparison against GPTQ with enlarged scales (a simple no-clipping variant) is needed to isolate whether HPTQ/SSQR's improvements come from the theoretical insight (avoiding clipping through the bound) or from separate engineering choices (Huffman coding, outlier storage). Without this baseline, the link between the theoretical bound and the practical methods is circumstantial.

### Minor

- **No empirical validation of Theorem 5's bound:** The error bound is a main theoretical result, but the paper provides no empirical check — e.g., computing actual layer-wise L2 error for a small model and comparing it to the bound. Even a single-layer sanity check would significantly strengthen the claim that the bound characterizes GPTQ's behavior.

- **Min-pivot order heuristic (Section 4.5) described but not validated in main text:** The paper states that "across our preliminary runs... min-pivot consistently reduces tr(D) relative to act-order, but the downstream accuracy gains are modest." However, no concrete numbers, figures, or tables appear in the main text. For a paper that emphasizes the importance of ordering, this omission is notable. The claim should be supported (or the heuristic presented as an observation worth future study).

### Trivial

- **Theorem 2's proof (Section 4.2):** The geometric proof in the main text is dense and uses heavy notation (a full page of subscripts, projection operators, and angle variables). An inline algebraic sketch alongside would improve readability without relying on the appendix.

## Nice-to-Haves

- A comparison of the new methods (SSQR, HPTQ) against QuIP's LDLQ (which also operates in a no-clipping regime) would help position the practical contribution within the existing theoretical landscape.
- Direct comparison of SSQR kernel throughput against other quantization kernels (not just PyTorch BF16) would better contextualize the speedup.
- Reporting perplexity over multiple calibration seeds would address variance concerns (though single-run evaluation is standard in this line of work).

## Removed Points

*These points are flagged for removal; treat them with caution:*

- **Missing SOTA comparisons (QuIP#, AQLM):** The paper's primary contribution is theoretical, not empirical SOTA. Requiring exhaustive comparisons to every advanced quantization method is scope creep. The baselines (GPTQ, RTN, HRTN) are appropriate for the claim "outperform original GPTQ."

- **CUDA kernel "only a single number":** Removed as factually inaccurate — Figure 4(c) shows multiple curves across varying outlier rates (0–5%) and bitwidths (2, 3, 4), not a single number.

- **Statistical significance / error bars:** Removed as not standard practice for perplexity evaluation in this setting; single runs are the norm in the PTQ literature.

- **"Dense notation / hard to follow":** Removed as a subjective presentation nitpick that does not threaten any claim.

- **Reproducibility details about MSE method precision:** Removed as a nitpick about implementation details that are standard in the field.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the combined reviews is the structural tension between the paper's two halves. The theoretical analysis cleanly explains GPTQ's behavior under an *infinite integer grid* (no clipping) with a *reversed order*. The practical methods operate on *finite-bitwidth integer grids with outliers* using *standard GPTQ ordering*. The reviews converge on the insight that bridging this gap — empirically demonstrating that the theoretical bound actually predicts real GPTQ behavior under realistic conditions — would transform the paper from a theoretical curiosity into a foundational result. The fact that HPTQ and SSQR improve over GPTQ despite operating outside the theory's exact conditions is interesting but not explanatory; the field needs to know *why*.

## Suggestions

1. **Explicitly state the experimental ordering.** Clarify in Section 5 whether GPTQ runs front-to-back or back-to-front with act-order. If back-to-front, state it directly; if front-to-back, discuss why the Babai equivalence might still inform the behavior.

2. **Add a no-clipping GPTQ baseline.** Run GPTQ with scales multiplied by a factor large enough to prevent any integer overflow, and report the resulting perplexity alongside SSQR/HPTQ. This isolates the effect of the theoretical insight from the engineering choices.

3. **Validate the bound empirically.** For one model and a few layers, compute the actual layer-wise L2 error and compare to the Theorem 5 bound. Even a positive-slope correlation (not necessarily a tight sandwich) would demonstrate that the bound captures meaningful structure.

4. **Move min-pivot results into the main text.** Show a small table or figure comparing tr(D) for act-order vs min-pivot, and the corresponding perplexity impact.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 6Mdvq0bPyG (EfficientQAT) | 3.00 | R1 | A practical QAT method that was rejected as incremental. GPTQ-Babai's theoretical novelty is far higher. |
| vJmpg0exYA (DiscQuant) | 4.50 | R1 | Theory + practice paper using discrepancy theory. Had concerns about algorithm practicality and missing baselines. GPTQ-Babai's theory is cleaner and the equivalence insight is more fundamental. |
| rAcgDBdKnP (OSTQuant) | 6.20 | R1 | Accepted. Strong empirical method with QSUR metric and SOTA results. GPTQ-Babai has weaker experiments but more novel theory. |
| eW4yh6HKz4 (CBQ) | 7.60 | R1 | Accepted. Comprehensive SOTA empirical results with cross-block reconstruction. GPTQ-Babai's experiments are not at this level of completeness. |

**Round 1 bracket:** 5.0–7.0.

**Round 2 — Narrowing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| xw29VvOMmU (LQ-LoRA) | 6.75 | R2 | Accepted. Extension of QLoRA with iterative decomposition. Practical, well-executed, incremental. GPTQ-Babai has stronger theoretical novelty. |
| Tv36j85SqR (Lattice Transform Coding) | 7.20 | R2 | Accepted. Lattice quantization in neural compression. Strong theory + experiments. More complete empirically than GPTQ-Babai. |
| ZBlfjXubgG (Pyramid VQ) | 5.00 | R2 | Rejected. Applied PVQ to LLMs. Mixed reviews with concerns about baselines. GPTQ-Babai's theory is clearly stronger. |
| MF7ljU8xcf (Larger LLMs Provably Generalize Better) | 6.00 | R2 | Accepted. Theoretical generalization bounds for LLMs. Pure theory with some empirical validation. Similar to GPTQ-Babai in being theory-driven. |

**Final assessment:** The paper's core theoretical contribution (GPTQ ≡ Babai's nearest plane) is genuinely novel and significant — it reframes a widely-used algorithm in terms of a classical lattice method, provides the first principled error bound, and opens new research directions. This alone is a strong contribution. The experimental section is weaker than what high-scoring empirical papers (CBQ, Lattice Transform Coding) provide, but the theoretical core is more fundamental than the contributions in LQ-LoRA or OSTQuant. The paper is most comparable to DiscQuant (theory+practice, 4.50) in structure, but exceeds it in theoretical clarity and significance — and to "Larger LLMs Provably Generalize Better" (6.00) in being theory-driven with partial experiments. The ordering ambiguity and missing baseline are real weaknesses that prevent a higher score. 

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>