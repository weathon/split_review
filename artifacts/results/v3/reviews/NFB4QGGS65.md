Now I have a thorough understanding of the paper and the appropriate calibration context. Let me synthesize the final review.

## Summary of calibration anchors

**Round 1 anchors:**
- Low band (0T8vCKa7yu, 3.00, LLM quantization theory): Rejected, fundamental flaws
- Low band (orG37FHN4b, 3.00, data-free quantization): Rejected
- Mid band (vJmpg0exYA/DiscQuant, 4.50, quantization theory): Rejected — similar structure to current paper: theoretical quantization insight + practical algorithm, but experiments limited to GPTQ/RTN baselines, reviewers cited limited comparisons
- Mid band (ZBlfjXubgG/PVQ, 5.00, vector quantization): Rejected — interesting idea, poor writing, missing baselines
- Mid band (vmiV4Z99lK/SPFQ, 4.25): Rejected
- Weakness-anchored (sMwYn2lZjO, 4.60, MoE PTQ benchmark): Rejected
- Weakness-anchored (LnKDcqOfgy, 5.00, rate-distortion quantization): Rejected — limited models, incremental
- High band (wg1PCg3CUP, 8.00, scaling laws): Accepted, very strong

**Round 2 anchors:**
- (sfTsvy05MX, 4.75, lattice VQ): Rejected
- (ClkfwM3STw, 4.75, quantized LLM benchmark): Rejected
- (5bdcDl6mC7, 5.50, diffusion quantization): Rejected

**Round-1 bracket:** 3.5 – 5.5

**What low-band anchors failed at:** Insufficient experimental validation, missing baselines, unclear contributions. The current paper shares these issues but has a clearer theoretical insight. **The paper under review shares the experimental shortcomings of the low-band and mid-band anchors** — in fact, its main experimental comparison is on fewer models and with a more significant confound (variable-rate vs fixed-rate) than DiscQuant (4.50). This is the binding constraint.

**Final score: 4.5 — Reject**

---

## Summary

This paper establishes a theoretical connection between GPTQ (a popular post-training quantization method for LLMs) and Babai's nearest plane algorithm for the closest vector problem (CVP) on lattices. The authors prove that GPTQ, when executed back-to-front, is mathematically identical to Babai's algorithm. Leveraging this equivalence, they derive a tight layer-wise error bound and propose two no-clipping quantization schemes (SSQR and HPTQ) that avoid the clipping errors that would violate the bound. They also provide a GPU inference kernel for the SSQR representation. The paper presents experimental results on Qwen3-8B showing that HPTQ achieves lower WikiText-2 perplexity than GPTQ at comparable average bitwidths.

## Strengths

1. **Novel geometric connection between GPTQ and a classical lattice algorithm.** Theorem 4 (GPTQ back-to-front ≡ Babai's nearest plane) provides a genuinely new perspective on why GPTQ works, grounding its greedy error propagation in the geometry of the closest vector problem. This is a conceptual contribution that could influence future quantization research. The algebraic derivation in the main text (Theorem 2) maps the OBQ error propagation formula to Babai's projection via inverse basis vectors — the essential algebraic equivalence is present in the main text, not just the appendix.

2. **Tight error bound under no-clipping (Theorem 5).** By importing Babai's guarantee, the paper derives a worst-case bound expressed in terms of the LDL decomposition of the Hessian. This bound is tight and gives a theoretical target for quantization design: avoid clipping to satisfy the bound's precondition.

3. **The no-clipping methods show clear improvement over baseline GPTQ.** In Figure 4(a), HPTQ consistently achieves lower perplexity than GPTQ across a range of bitwidths on Qwen3-8B, with the gap widening at lower bitwidths. The inclusion of HRTN (Huffman + RTN) as a baseline helps separate the benefit of GPTQ's error propagation from the benefit of variable-rate coding.

4. **Efficient GPU inference kernel.** The SSQR CUDA kernel achieves ~2× end-to-end speedup over PyTorch BF16 inference (Figure 4c), demonstrating that the proposed representation is practically deployable.

## Weaknesses

### Major

1. **The HPTQ vs. GPTQ comparison confounds the effect of no-clipping with variable-rate encoding.** HPTQ uses Huffman coding (variable-rate) while GPTQ uses fixed-rate integers with group size 128. This means HPTQ can allocate more bits to outlier weights — the observed perplexity improvement could be largely due to this variable-rate flexibility rather than the no-clipping principle derived from the theory. The paper includes HRTN (Huffman + RTN) as a baseline but is missing the crucial ablation: **GPTQ without clipping + Huffman vs. GPTQ with clipping + Huffman**, which would isolate the effect of clipping vs. no-clipping while keeping the compression scheme fixed. Without this, the connection between the theoretical insight (no-clipping satisfies the error bound) and the practical improvement (HPTQ beats GPTQ) remains circumstantial.

2. **Limited experimental scope in the main text.** The headline results (Figure 4a) are on a single model (Qwen3-8B) with a single metric (WikiText-2 perplexity). While the paper references appendix results on additional models and zero-shot benchmarks, the main text should present at least a summary table showing perplexity and downstream accuracy across multiple model families (e.g., Llama-3, Qwen3, Mistral) to support the claimed practical outperformance. DiscQuant (a 2025 paper with similar theoretical+applied structure) included results on 2 model families with multiple downstream tasks in its main body.

3. **Kernel speedup compared only against PyTorch BF16, not against competitive quantized kernels.** The ~2× speedup over BF16 is expected from moving to 2–4 bit weights. To demonstrate that the SSQR kernel itself is efficient, the paper should compare against an optimized quantized matmul kernel at the same effective bitwidth (e.g., bitsandbytes, the GPTQ repository's kernel, or Marlin). Without this, it is unclear whether the kernel adds overhead or is competitive.

4. **The theoretical error bound (Theorem 5) is not empirically validated.** The paper derives a worst-case bound under the no-clipping assumption and uses it to motivate the no-clipping designs, but never measures per-layer quantization error or checks whether the bound is predictive. An experiment comparing actual layer-wise error against the bound would ground the theory in practice and strengthen the motivation.

### Minor

5. **Theorem 4 proof in the main text is a sketch; the rigorous algebraic proof is deferred entirely to the appendix.** The main text says "Theorem 2 shows that each intermediate weight vector produced by OBQ, equivalently GPTQ, can be viewed as Babai's residual vector" and then refers to Sections B–C for the full proof. Given that this equivalence is the paper's central theoretical contribution, a more self-contained main-text proof — or at least a clear outline of the algebraic mapping — would significantly strengthen the paper. The geometric proof of Theorem 2 (OBQ ↔ Babai projection) is present but dense, relying on figures that are difficult to parse.

6. **Relationship to QuIP/LDLQ is underdeveloped.** The related work notes that QuIP "proves an error guarantee for GPTQ and proposes the LDLQ method as an equivalent variant of GPTQ" but does not clearly differentiate the present paper's contribution from that prior work. Since LDLQ is already described as algebraically equivalent to GPTQ, the paper should explicitly state what the geometric perspective adds that the algebraic LDL view does not.

7. **Min-pivot ordering shows only "modest" accuracy gains, as the paper acknowledges.** Including this as a contribution without demonstrating clear practical benefit makes the section feel like filler. A comparison table showing perplexity under act-order vs. min-pivot would help.

### Trivial

8. Figures 2 and 3 are extremely dense, with legend entries longer than the surrounding text. The geometric intuition they intend to convey is hard to extract.

## Nice-to-Haves

- Controlled ablation: GPTQ without clipping + Huffman (to isolate no-clipping benefit from variable-rate benefit)
- Comparison against AQLM, QuIP#, or AWQ for context on where the proposed methods sit relative to the broader SOTA
- Error bars or variance estimates (though single-run evaluation is field-normative for perplexity)
- A table with exact perplexity and bitwidth numbers alongside Figure 4(a) for precision

## Removed Points

These points were raised by the reviewers but are removed or demoted after verification against the paper:

- **"GPTQ perplexity values seem far higher than typical results"** — Removed. This is a factual claim about typical GPTQ performance that cannot be verified without running the specific model. Qwen3-8B at 3-bit may legitimately exhibit ~30 WikiText-2 perplexity; the BF16 baseline of ~11 and the spike at very low bitwidths are consistent with known behavior of 3-bit quantization on modern LLMs.
- **"The paper's claim of being first to provide a geometric interpretation should be qualified given QuIP"** — Removed. The paper does cite QuIP and states QuIP "proves an error guarantee and proposes the LDLQ method as an equivalent variant of GPTQ." The geometric interpretation (GPTQ as Babai's nearest plane, connection to CVP geometry) is genuinely distinct from QuIP's algebraic LDL equivalence. The paper also acknowledges concurrent work (Birnick, 2025) via footnote.
- **"No error bars"** — Moved to Nice-to-Haves. Single-run perplexity evaluation is standard in the LLM quantization literature.
- **"Theorem 1 is straightforward"** — Removed. This is a judgment about depth, not a weakness. Many foundational lemmas are simple observations.
- **"Closing remarks note MXFP4 is no-clipping, undermining novelty"** — Removed. The paper mentions this as future work context, not as a limitation of its own contribution.
- **"Missing comparison with AQLM/AWQ/bitsandbytes"** — Partially removed. The kernel comparison against bitsandbytes is a valid point (kept in Major #3). The missing method comparisons are noted in Nice-to-Haves but aren't fatal omissions since the paper claims to outperform "the original GPTQ," not to be SOTA.

## Novel Insights

The most genuinely novel observation across the reviews is not in the critiques but latent in the paper itself: the GPTQ back-to-front equivalence implies that the GPTQ quantization order (act-order, min-pivot) directly corresponds to the Gram-Schmidt orthogonalization order in Babai's algorithm. This means the quantization order controls the error bound through the diagonal entries of the LDL factor, providing a principled optimization target that was previously opaque. The reviewers did not surface any deeper insight beyond what the paper already states.

## Suggestions

1. **Add a controlled ablation experiment** comparing GPTQ (no Huffman, with clipping) → GPTQ (no Huffman, no clipping) → HPTQ (Huffman, no clipping) to separate the benefits of no-clipping from variable-rate coding. If GPTQ without clipping (using extended integer range or per-group scale adjustment) already closes most of the gap to HPTQ, the theoretical insight is validated directly.

2. **Present a compact results table in the main text** with perplexity and average accuracy across 2–3 model families (e.g., Llama-3-8B, Qwen3-8B, Mistral-7B) at 3–4 bitwidths, similar to how DiscQuant and other quantization papers structure their main empirical contribution.

3. **Validate the error bound empirically** for at least one layer: compute the LHS of Theorem 5's inequality and compare against the RHS across several layers and scales. Show that the bound is reasonably tight and that clipping violations indeed cause bound violations.

4. **Restructure the main-text proof of Theorem 4** to include the core algebraic mapping (the equivalence of the rounding decisions), even if the full technical details remain in the appendix. The current sketch ("Theorem 2 shows that...") is insufficient for a central claim.

5. **Benchmark the kernel against an optimized quantized kernel** (e.g., bitsandbytes 4-bit, GPTQ's own CUDA kernel, or Marlin) at the same effective bitwidth to demonstrate that the sparse-outlier handling does not introduce significant overhead.

## Score and Decision

**Round-1 bracket:** 3.5 – 5.5 (based on topic-band and weakness-anchored searches)

**Narrowing:** The weakness-anchored queries for papers with limited experiments, theoretical proofs deferred to appendix, and insufficient baseline comparisons returned anchors scoring 4.25–5.00, all rejected. DiscQuant (4.50) is the most structurally similar anchor — it also presents a theoretically grounded quantization method with experiments limited to GPTQ/RTN baselines — and was rejected. The current paper has a cleaner theoretical result (exact equivalence rather than a bound under assumptions) but weaker experimental controls (confounded comparison, single-model main result). The round-2 anchors in the 4.75–5.50 band are either benchmarks or methods papers with broader experimental validation, reinforcing that the experimental scope here falls below the acceptance threshold.

**What the low-band anchors failed at** — and the current paper shares these failures: insufficiently controlled experiments (confounding variable-rate with no-clipping), main results limited to one model and one metric, missing empirical validation of the stated theoretical bound, and lack of comparison against competitive quantized kernels. These are structural rather than cosmetic issues.

**Score: 4.5 — Reject**

The theoretical contribution (GPTQ ↔ Babai equivalence) is genuine and interesting, but the experimental evaluation does not meet the standard required for acceptance. The confounded comparison between HPTQ and GPTQ weakens the claimed practical outperformance, and the limited experimental scope leaves the practical significance unclear. The core insight deserves a stronger empirical backing.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>