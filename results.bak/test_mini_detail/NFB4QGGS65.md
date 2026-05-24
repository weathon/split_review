Now I have a solid calibration picture. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper establishes that GPTQ, when executed back-to-front (from last to first dimension), is mathematically equivalent to Babai's nearest plane algorithm for the closest vector problem on a lattice defined by the Hessian matrix. This equivalence yields a tight layer-wise error bound for GPTQ in the no-clipping setting. Leveraging this bound, the paper proposes two no-clipping quantization methods (SSQR and HPTQ) and an efficient GPU inference kernel.

## Strengths

- **Theorem 4 (GPTQ = Babai's nearest plane algorithm) is a genuinely novel theoretical connection.** The paper proves that GPTQ executing back-to-front coincides exactly with Babai's algorithm on the lattice defined by the Hessian factor, without LLL reduction. This is the first such connection and places a widely-used heuristic on principled theoretical footing. The geometric interpretation (Section 4.3) — GPTQ performs an orthogonal walk through nested affine subspaces — is genuinely insightful.

- **Theorem 5 provides a tight layer-wise error bound for GPTQ.** By importing Babai's guarantee, the paper derives $\|X \operatorname{diag}(s_i) z_i - X w_i\|^2 \leq \frac{1}{4} (T^{-1} s_i)^\top D (T^{-1} s_i)$ for the no-clipping setting, with both absolute and relative forms. The bound is proven tight (attained at hyper-cuboid corners). This is a concrete analytical consequence of the core equivalence.

- **Geometric interpretation of OBQ's dimension selection (Corollary 3).** The paper demonstrates that OBQ's greedy rule (Eq. 1) minimizes the distance from the residual target to the nearest hyperplane in the lattice basis, explaining why the greedy heuristic works well — a previously open question.

- **Min-pivot order (Algorithm 3).** The proposed order minimizes the trace of the LDL diagonal matrix, providing a principled alternative to the heuristic act-order with consistent (if modest) improvements.

- **SSQR GPU kernel achieves ~2× speedup over PyTorch BF16 on A6000.** The paper demonstrates that the no-clipping representation can be deployed efficiently, with end-to-end speedups across multiple bitwidth and outlier-rate settings (Figure 4c).

## Weaknesses

### Fatal
None.

### Major

- **The main-paper experimental evaluation is too narrow to substantiate the practical claims.** The main text reports perplexity on WikiText-2 for a single model family (Qwen3) against only RTN, GPTQ, and Huffman-coded variants. No comparisons with contemporary methods (QuIP#, AQLM, QuaRot, etc.) appear in the main paper. Zero-shot task accuracy, Llama-family results, and method comparisons are promised in the appendix (Sections E.3–E.5), which was stripped by the PDF parser. As presented to a reviewer, the practical evidence for SSQR/HPTQ outperforming GPTQ rests on a single figure (Figure 4a) without error bars, variance, or multi-model confirmation. For a paper claiming new quantization schemes that "outperform the original GPTQ" (abstract), this is a significant evidential gap.

- **Theorem 5's practical relevance is unvalidated.** The bound holds only under the no-clipping assumption ($\mathbb{Z}_\dagger = \mathbb{Z}$). The paper explicitly acknowledges this and motivates SSQR/HPTQ as no-clipping methods, but it never empirically measures how close the actual layer-wise error comes to the bound, nor shows that the bound provides useful guidance for hyperparameter selection. Without this validation, the bound remains a formal consequence without demonstrated practical value.

- **The proposed methods (SSQR, HPTQ) are not convincingly derived from the theory.** The paper asserts that SSQR's scale-adjustment mechanism and HPTQ's entropy-guided scale selection are motivated by the no-clipping error bound, but the connection is heuristic and asserted rather than derived. For SSQR, the binary search on a proportional scale over an entire layer is described without justification for why a single multiplicative factor should work across groups with very different weight distributions. For HPTQ, Huffman encoding is a generic compression technique with no specific link to the CVP framework. The paper would benefit from showing how these methods directly control the bound's magnitude or are natural consequences of the lattice perspective.

- **The pseudocode and algorithmic mapping, while correct in essence, is presented opaquely in the main text.** Algorithm 1 gives the standard GPTQ (front-to-back with lower-triangular $L$ from $\text{LDL}(H^{-1})$). The equivalence in Theorem 4 requires running back-to-front with an upper-triangular factor. The paper acknowledges this (Section 4.3: "Second, we run GPTQ in the back-to-front order and replace the lower triangular factor with an upper triangular one"), but the actual equivalent pseudocode (Algorithm 4) is deferred entirely to the appendix. The main text's description ("This is the only (superficial) difference between the two algorithms") is imprecise — the triangular factor must also switch. A reader of the main text alone cannot verify the claimed equivalence without taking the appendix on faith.

### Minor

- **Theorem 1 (Quantization-CVP equivalence) is essentially definitional.** The proof is a single sentence noting that different Hessian factors are related by orthogonal transformations. This is a helpful framing but not a substantive theoretical result. The "dictionary" in Table 1 is useful exposition.

- **The error bound's connection to the proposed methods is not empirically tested.** The bound depends on the LDL diagonal $D$ and the scales $s_i$. The paper does not show how SSQR or HPTQ's choices affect this bound quantitatively, nor does it ablate the bound's tightness on real layers. This weakens the claim that the theory drives the method design.

- **Figure 4 lacks error bars or statistical significance markers.** The perplexity curves and speedup plots in the main text are single-run results. Adding variance information would improve confidence in the practical claims.

- **The discussion of QuIP is surface-level.** The related work section cites QuIP (Chee et al., 2023) and notes it "proves an error guarantee for GPTQ," but does not explain how the present work's bound or analysis goes beyond QuIP's LDLQ analysis. A brief distinguishing comparison would help.

### Trivial

None.

## Nice-to-Haves

- An ablation showing how HPTQ's perplexity varies with Huffman code granularity.
- An ablation separating the contribution of the min-pivot order from the proposed methods.
- Speedup comparison against a standard INT4 GEMV kernel for GPTQ-quantized weights, not just PyTorch BF16.

## Removed Points

Points removed from the harsh critic/strength finder reviews with brief justification:

1. **"GPTQ pseudocode is ambiguous / may not implement standard GPTQ correctly"** (harsh critic #1) — REMOVED. The paper explicitly acknowledges that Algorithm 1 is standard GPTQ (front-to-back) and that the equivalence requires back-to-front ordering with a different triangular factor. The harsh critic's reading conflates the standard algorithm presentation with the equivalence claim. The comment "L[j,:] only updates already-quantized rows when running front-to-back" is factually correct about standard GPTQ but is precisely the issue the paper addresses through the back-to-front reordering. The paper states this clearly. The equivalence pseudocode is deferred to the appendix, which is standard practice.

2. **"Theorem 1 is not novel / essentially definitional"** — REMOVED from weaknesses but noted as Minor. This is a valid observation but it's not a fatal flaw — the paper's main contribution is Theorem 4, not Theorem 1. The table and framing are helpful exposition.

3. **"Figures 2 is overly complicated"** — REMOVED. The figures are detailed but this reflects the complexity of the geometric proof. The harsh critic acknowledges the algebraic proof is in the appendix. This is a style preference, not a validity concern.

4. **"Missing related works"** — REMOVED per instructions (cannot confirm existence of external works).

5. **"Presentation concerns about typos, formatting"** — REMOVED per instructions (parser artifacts).

6. **"No comparison with QuIP#"** — REMOVED as it concerns appendix content that was stripped by the parser. The paper promises comparisons in Section E.5. However, the lack in the main text is noted as a minor weakness.

7. **"The paper lacks variance/error bars"** — KEPT in Minor, as this is a reasonable methodological point.

8. **Strength that SSQR/HPTQ "validate the practical applicability of the theoretical error bound"** — MODIFIED. The connection is asserted but not empirically validated (the bound is never measured), so this strength is overstated. The papers does show perplexity improvement, but this doesn't validate the bound specifically.

9. **Generic Strength Finder claims** — REMOVED. Several claimed strengths ("important problem," "timely topic") are generic and not specific to this paper's evidence.

## Novel Insights

The synthesis of reviews reveals an interesting tension that the paper does not fully address: the theoretical chain (GPTQ = Babai → error bound) is elegant and self-contained, but the practical methods (SSQR, HPTQ) are not derived from the bound in any formal sense — they are heuristics designed to operate in the no-clipping regime. This means the paper's two halves (theory and applications) are weakly coupled. A stronger paper would either: (a) use the bound to directly derive an optimal scale-selection strategy, or (b) clearly separate the theoretical contribution from the empirical one and validate each independently. The observation that the bound could guide basis reduction (mentioned in future work) is a potentially rich direction that the paper does not explore.

## Suggestions

1. Move the equivalence proof (or at least the key algebraic steps of Algorithm 4) into the main text, so the central claim is verifiable without the appendix.
2. Add at least one additional model family (Llama) and one additional task (e.g., MMLU or ARC) to the main paper's Figure 4 to broaden the evidence base.
3. Empirically measure how close the actual layer-wise error comes to Theorem 5's bound on several representative layers — this would validate the bound's practical relevance and strengthen the motivation for SSQR/HPTQ.
4. Provide error bars or variance across multiple calibration data shuffles for the perplexity curves.
5. Clarify the relationship between this work's error bound and QuIP's LDLQ analysis in the main text.

## Score and Decision

**Calibration summary:**

**Round 1 (Bracketing):**
- Weak anchors (score < 3.5): four papers at avg ~3.0 (e.g., PrefixQuant, EfficientQAT). These are rejected PTQ papers with unclear contributions. The current paper is clearly stronger.
- Middle anchors (3.5–7.5): DiscQuant (4.5, Reject), PVQ (5.0, Reject), Low-Rank Correction (5.0, Reject), FPTQ (4.0, Reject), QERA (6.8, Accept).
- Strong anchors (7.5+): CBQ (7.6, Accept Spotlight), Scaling Laws for Precision (8.0, Oral).

*Initial bracket:* 5.0–6.5.

**Round 2 (Narrowing):**
- LRQ (5.25, Reject): Similar structure — novel quantization method with some theory but limited experiments. The current paper has stronger theory but similarly limited main-paper evaluation.
- LLM-Codebook (4.75, Reject): Extreme compression method with limited baselines. The current paper is more theoretically grounded.
- Additional anchors: OSTQuant (6.2, Accept) and QERA (6.8, Accept) — both accepted papers with comprehensive experiments and clear practical improvements. The current paper's experiments are substantially narrower.

*Final positioning:* The paper is stronger than the typical ~5.0 rejected papers (PVQ, Low-Rank Correction, LRQ) because the theoretical contribution (GPTQ = Babai) is genuinely novel, well-grounded, and represents a first-principles understanding of a widely-used algorithm. However, it falls short of accepted papers (~6.2+) because the main-paper experimental evaluation is too narrow to support the practical claims, and the connection between theory and the proposed methods is asserted rather than demonstrated. The paper sits between these bands.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>