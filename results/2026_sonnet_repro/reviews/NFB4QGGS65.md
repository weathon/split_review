Now let me perform calibration searches.Now I have sufficient information to write the final review. Let me compile it.

---

## Summary

This paper establishes that GPTQ, when executed back-to-front (last-to-first dimension), is mathematically identical to Babai's nearest plane algorithm for the Closest Vector Problem on the lattice defined by the layer's Hessian matrix. From this equivalence (Theorem 4, proved both geometrically in Sections 4.2–4.3 and algebraically in Appendix C), the authors import Babai's approximation guarantee to derive a tight, layer-wise upper bound on quantization error in the no-clipping setting (Theorem 5). They then propose two overflow-tolerant quantization schemes—Scale-adjusted SpQR (SSQR) and Huffman-encoded PTQ (HPTQ)—that respect the no-clipping regime implied by the bound, together with a CUDA inference kernel for SSQR achieving ~2× end-to-end speedup.

---

## Strengths

- **Rigorous equivalence proof (Theorem 4):** The paper proves the GPTQ–Babai correspondence both geometrically (Section 4.2–4.3, Figures 2–3) and algebraically (Appendix C). The geometric proof casts OBQ's error propagation step as an orthogonal projection onto a nearest hyperplane (Theorem 2), and the algebraic proof proceeds in three well-defined steps (rewriting GPTQ to track cumulative error, reversing order, and matching rounding decisions). The "ineffectiveness of composition" result (Section 4.3) also confirms the equivalence is tight.

- **Tight error bound (Theorem 5):** The bound $\|\mathbf{X}\operatorname{diag}(\mathbf{s}_i)\mathbf{z}_i - \mathbf{X}\mathbf{w}_i\|^2 \leq \frac{1}{4}(\mathbf{T}^{-1}\mathbf{s}_i)^\top \mathbf{D}(\mathbf{T}^{-1}\mathbf{s}_i)$ is explicitly tight (attained when the target lies at the corner of the Babai hyper-cuboid), providing the first deterministic, worst-case guarantee directly linked to the LDL decomposition of the Hessian.

- **Theory-motivated practical methods:** SSQR and HPTQ are directly motivated by the no-clipping requirement of Theorem 5, not ad hoc engineering. Figure 4(a) shows HPTQ achieves the lowest perplexity across all compared methods on Qwen3-8B at 3.125 effective bits, with SSQR providing competitive results while achieving ~2× end-to-end latency speedup in Figure 4(c).

- **Principled order heuristic:** The min-pivot order (Algorithm 3) is analytically derived to minimize $\operatorname{tr}(\mathbf{D})$, directly minimizing the absolute error bound. The paper is admirably honest that downstream gains are modest, correctly characterizing act-order as a cheap approximation that already captures most of the benefit.

- **Working inference kernel:** A CUDA/C++ kernel for SSQR handles group-quantized inliers (2–4 bit) and unstructured sparse outliers on Ampere architecture, demonstrating the theoretical representation is deployable in practice.

---

## Weaknesses

### Fatal

None.

### Major

- **Relationship to QuIP's existing error guarantee is underspecified.** Section 2 notes in one sentence that "QuIP (Chee et al., 2023) proves an error guarantee for GPTQ and proposes the LDLQ method as an equivalent variant of GPTQ." Yet the paper claims to be "the first to provide a geometric interpretation for GPTQ, which implies a layer-wise global error bound." Whether Theorem 5 is strictly stronger, qualitatively different (deterministic worst-case vs. QuIP's statistical route), or merely a geometric re-derivation of QuIP's guarantee must be made explicit in the main text. QuIP's guarantee uses incoherence preprocessing and statistical arguments; this paper's bound is a deterministic worst-case via Babai's approximation ratio—that is a meaningful distinction, but it is currently left for the reader to infer. Without this clarification, reviewers cannot assess the novelty of the theoretical contribution relative to prior work.

- **Main-text experimental scope is narrow; comparisons are deferred to appendix.** The main body experiments are limited to Qwen3-8B (Figure 4). Comparison against relevant baselines (e.g., SpQR, which directly inspires SSQR, and methods in Section E.5) is entirely in the appendix. For a paper claiming that HPTQ and SSQR outperform GPTQ, the head-to-head comparison should appear in the main text with at least a summary table—particularly because the paper's conclusions about practical improvements rest on these comparisons.

### Minor

- **The error bound applies to the no-clipping setting only, while standard GPTQ deployment uses clipping.** Theorem 5 requires $\mathbb{Z}_q = \mathbb{Z}$; this is clearly stated. The paper argues (Section 6, Future Work) that MXFP4 and NVFP4 use per-group AbsMax scales effectively eliminating clipping, so the analysis is prospectively relevant. This argument is largely forward-looking. The paper is honest about this limitation; nonetheless, readers should be clearly reminded that the bound does not apply to current INT4/INT8 GPTQ deployments.

- **HPTQ lacks an inference path.** HPTQ uses Huffman coding, which produces variable-length codes. Figure 4(a) shows HPTQ's perplexity curves alongside SSQR (which has a CUDA kernel), creating an implicit impression of parity between the two methods that is not borne out. HPTQ is effectively a compression-ratio analysis tool rather than a deployable method; the paper should acknowledge this explicitly in the main text rather than leaving it implicit.

- **The trace-reduction vs. perplexity link is buried.** Theorem 5 predicts that reducing $\operatorname{tr}(\mathbf{D})$ should reduce quantization error. The min-pivot order consistently reduces $\operatorname{tr}(\mathbf{D})$ relative to act-order (Section D.3 is described as "preliminary"). The relationship between trace reduction and downstream perplexity is the load-bearing link between the theory and the practical results, yet it is not directly visualized in the main text. A scatter plot or table of $\operatorname{tr}(\mathbf{D})$ vs. perplexity across models and orderings would substantially strengthen the claim that the bound is practically predictive.

### Trivial

None worth noting.

---

## Nice-to-Haves

- Even a small-scale pilot applying LLL basis reduction (as suggested in Section 6, Future Work) to a single layer and measuring whether it reduces $\operatorname{tr}(\mathbf{D})$ or downstream perplexity would be extremely valuable—either as positive evidence for the lattice-reduction direction or as an honest early negative result.
- The binary search for the scale-adjustment mechanism in SSQR assumes "the outlier rate is negatively related to the scales in general" (Section 5). A brief monotonicity argument or citation would strengthen the description, since this is the key assumption enabling convergence.
- Section 4.3 describes the direction reversal as a "superficial difference." Since standard GPTQ runs front-to-back and the equivalence holds only back-to-front, the introduction should be somewhat more explicit that the guarantee applies to the reversed variant, not as-deployed GPTQ, to avoid misleading practitioners.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The back-to-front direction is non-trivial for users"** (harsh critic framing that calling it "superficial" is problematic): The paper explicitly states in the abstract that the equivalence holds "when executed back-to-front," and Section 4.3 notes that the two directions "produce the same results if we align the dimensional order." The word "superficial" refers to the mathematical structure being the same, not to implementation consequences. This criticism misreads the paper's intent and is removed.

- **"The bound only applies to a variant of GPTQ"**: This is partially valid but largely addressed by the paper's own framing—SSQR and HPTQ are introduced precisely as no-clipping GPTQ variants motivated by the bound. Retained above as a minor weakness only.

- **"HPTQ experiments compare non-commensurate bitwidths"**: The "average bitwidth" metric is standard for compression-ratio analysis. The issue with HPTQ is the lack of an inference kernel, which is retained above. The non-commensurate bitwidth criticism specifically is noise and is removed.

- **"Min-pivot calling it a principled choice overstates practical contribution"**: The paper says "min-pivot consistently reduces tr(D) relative to act-order, but the downstream accuracy gains are modest." This is accurate and appropriately hedged; the harsh critic's framing that calling it "principled" overstates things ignores that principled and practically impactful are different attributes. Removed.

---

## Novel Insights

The paper's most genuinely novel insight is the "ineffectiveness of composition" result (Section 4.3): once Babai's projection sequence has been executed, any subsequent GPTQ-style error-propagation correction is algebraically redundant (the output $\mathbf{Z}$ is unchanged). This is not merely a corollary of the equivalence—it establishes that the equivalence is tight in a strong sense and rules out a natural class of potential improvements (composing Babai with GPTQ). A second novel consequence is that the min-pivot order has a direct geometric interpretation as always selecting the shortest residual Gram-Schmidt vector, agreeing with Babai's relative error bound—this gives a clean, theory-grounded reason to prefer min-pivot over act-order even when their empirical performance gap is small.

---

## Suggestions

1. Add a paragraph in Section 2 or Section 4.4 explicitly comparing Theorem 5 to QuIP's error guarantee: state whether the two bounds are numerically the same, whether this paper's bound is tighter, or how they relate. This is essential for the novelty claim.
2. Move a summary comparison table against SpQR and other relevant baselines into the main text (currently in Appendix E.5).
3. Add a figure in Section 4.5 or 5 showing the correlation between $\operatorname{tr}(\mathbf{D})$ (under different pivot orders) and downstream WikiText-2 perplexity to close the loop between the theoretical bound and empirical validation.
4. Clearly label HPTQ as a "compression-ratio analysis method" rather than an inference-deployable method in the main text, given the absence of a decoding kernel.

---

## Score and Decision

**Calibration:**

*Round 1 anchors (bracketing):*
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `0T8vCKa7yu.md` (LLM Compression via Convex Opt) | 3.00 | R1-weak | Much weaker — no rigorous theory, rejected for limited novelty |
| `vw0NurJ7UX.md` (PrefixQuant) | 3.00 | R1-weak | Pure empirical method paper, much lower theoretical depth |
| `vJmpg0exYA.md` (DiscQuant) | 4.50 | R1-mid | Similar spirit (theory-inspired quantization), but weaker theoretical proof, limited baselines |
| `ZBlfjXubgG.md` (Pyramid VQ for LLMs) | 5.00 | R1-mid | Lattice-based quantization but methodologically less novel |
| `rAcgDBdKnP.md` (OSTQuant) | 6.20 | R1-mid | Practical PTQ method, no comparable theoretical depth |
| `xw29VvOMmU.md` (LQ-LoRA) | 6.75 | R1-mid | Clean theory + practice but narrower theoretical contribution |
| `wg1PCg3CUP.md` (Scaling Laws for Precision) | 8.00 | R1-strong | Broader empirical + theoretical scope, extensive validation |

**Round 1 bracket: 6.0–8.0** (clearly above the 4.5 anchors; theory rigour and practical contribution place it in the upper half of the range).

*Round 2 anchors (narrowing, 5.5–8.0):*
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `wJv4AIt4sK.md` (Sparsity+Quantization) | 7.50 | R2 | Most comparable: rigorous theorem (optimal ordering), theory-to-practice, extensive multi-model empirical validation across OPT, LLaMA, ViT. This paper matches it in theoretical rigor but has narrower main-text empirical breadth. |
| `Tv36j85SqR.md` (Lattice Transform Coding) | 7.20 | R2 | Also uses lattice geometry for quantization theory+practice; comparable scope. |
| `44cMlQSreK.md` (NeuroQuant) | 7.20 | R2 | PTQ with theoretical framework; weaker theory. |
| `MiPyle6Jef.md` (QP-SNN) | 6.75 | R2 | Practical compression paper, less theoretical depth. |

**Round 2 narrowing:** The paper is most comparable to `wJv4AIt4sK.md` (7.5) and `Tv36j85SqR.md` (7.2). In theoretical depth and novelty it is at least comparable to these: proving that a widely-deployed engineering algorithm is exactly Babai's nearest plane algorithm is a concrete, non-trivial result with clear consequences. The limiting factor relative to the 7.5 anchor is the narrower empirical validation in the main body (single model, comparisons deferred to appendix) and the unresolved QuIP relationship. The paper is clearly better than the 4.5–5.0 anchors; I score it **7.0**, slightly below the 7.5 anchor owing to the experimental presentation gaps and the underspecified theoretical novelty relative to QuIP.

**Axis assessment:**
- **Originality:** High. The GPTQ–Babai equivalence is a genuinely novel observation with broad implications.
- **Importance of research question:** High. GPTQ is one of the most widely used PTQ methods; placing it on rigorous theoretical ground is impactful.
- **Claims well-supported:** Mostly yes. Core theoretical claims are rigorously proved. Practical claims rest somewhat on appendix experiments.
- **Soundness of experiments:** Good but limited in the main body; the appendix carries too much of the evaluation load.
- **Clarity of writing:** Good overall; Section 4 is dense but accompanied by helpful figures.
- **Value to community:** High. Opens a concrete research direction toward LLL/BKZ-based quantization improvements.

**Final score: 7.0 | Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>