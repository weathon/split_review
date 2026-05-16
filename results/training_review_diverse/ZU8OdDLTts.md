Now I have verified all the key claims against the paper. Let me produce the final consolidated review.

## Summary

The paper proposes ARB-LLM, a family of 1-bit post-training quantization (PTQ) methods for LLMs. The core idea is an alternating refinement algorithm (ARB) that iteratively updates the binarization parameters (mean μ, scaling factor α, and binary matrix B) to progressively reduce the distribution shift between binarized and full-precision weights. Two extensions are developed: ARB-X, which incorporates calibration data into the parameter updates, and ARB-RC, which introduces column-wise scaling to handle column deviations in LLM weight distributions while removing the mean parameter. A refined Column-Group Bitmap (CGB) strategy is also introduced for better weight partitioning. The final models, ARB-LLM_X and ARB-LLM_RC, consistently and substantially outperform the SOTA binary PTQ method BiLLM across OPT, LLaMA 1/2/3, and Vicuna families, and ARB-LLM_RC is reported as the first binary PTQ method to surpass same-size FP16 models on zero-shot QA tasks.

## Strengths

1. **Alternating refinement with theoretical error reduction guarantee**: The ARB algorithm provides a principled iterative procedure (Theorem 1) that monotonically reduces the quantization error L₁. The ablation in Table 4 confirms this empirically: vanilla ARB drops perplexity from 49.79 (BiLLM) to 22.67 on LLaMA-7B WikiText2, a dramatic improvement that directly validates the core idea.

2. **Novel extensions address real structural issues in LLM weights**: ARB-RC's introduction of column-wise scaling factors is well-motivated by the observed column deviation in LLM weights (Fig. 3), and ARB-X's incorporation of calibration data into binarization parameter updates (with a theoretical speedup via reformulation, Theorem 2) is a genuinely new capability for binary PTQ. The ablation (Table 4) shows both extensions contribute meaningfully beyond the basic ARB.

3. **Consistent and substantial SOTA improvements across multiple model families**: ARB-LLM_RC achieves 14.03 perplexity on LLaMA-7B WikiText2 vs. BiLLM's 49.79 (Table 2), with similar large margins across OPT (Table 1), LLaMA-2/3 (Table 2), and Vicuna (Table 3). Memory is simultaneously reduced (e.g., 2.83 GB vs. BiLLM's 2.93 GB on LLaMA-7B with CGB, Table 6). The improvements are systematic and large enough to be practically meaningful.

4. **Well-designed ablation and convergence studies**: The paper ablates the contribution of each component (ARB baseline → ARB-X/ARB-RC → +CGB), shows iteration count effects, calibration set size sensitivity, and the necessity of the joint column-group bitmap. These give confidence that each design choice is grounded in empirical evidence.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The headline claim about "surpassing FP16" would benefit from more granular reporting.** The abstract states that ARB-LLM_RC "is the first to surpass FP16 models of the same size" on zero-shot QA. The paper provides two pieces of supporting evidence: the teaser figure (Fig. 1) showing OPT average accuracy, and Fig. 6 showing LLaMA family average accuracy. However, per-task breakdowns across all 7 individual datasets are not reported in the main paper (deferred to supplementary), and no confidence intervals or significance tests are provided. The claim itself is supported by the figures, but the presentation could be more transparent. The paper states "More results are provided in the supplementary file" (line 402), so this is largely a presentation/accessibility issue rather than an evidential gap.

2. **The ARB-X algorithm does not update B, and the implications are underexplored.** The paper correctly states (line 221) that B cannot be updated via gradient of L₂ because B is discrete, so it remains frozen from the initial sign computation. This is acknowledged transparently, but the paper does not discuss whether alternative strategies were considered (e.g., updating B via sign after the μ,α updates from L₂, or treating B as a latent variable). Since ARB-RC (which uses L₁ and updates B via sign) consistently outperforms ARB-X (which uses L₂ but does not update B), a brief discussion of this design trade-off would help readers understand the limits of the calibration-aware approach.

3. **The ablation for ARB-RC conflates two changes.** The comparison between ARB (with μ) and ARB-RC (without μ, with α^c) changes both the removal of μ and the addition of column-wise scaling α^c simultaneously. An ablation that isolates the effect of removing μ from the effect of adding α^c would strengthen the design justification. The paper's argument that "weight distribution shows a mean close to zero" (line 224) is reasonable but could be empirically validated.

4. **The theoretical speedup ratio (389×) for ARB-X is not empirically verified.** Theorem 2 derives a speedup ratio proportional to 389 under typical settings, but no actual runtime comparison is provided to confirm this. The paper does provide end-to-end runtime comparisons (Table 5) showing the total quantization time, but the specific claim about the reformulation's efficiency is left as a theoretical value.

5. **Theorem 1's presentation omits the conditions that guarantee the inequality.** The theorem states L₁^τ ≤ L₁^0 with an expression involving (α^τ)² − (α^0)² − (μ^τ−μ^0)², but the main text does not explain why the RHS is always non-negative or what assumptions about the update order are needed. The proof is in the supplementary, but the main paper should at least state the key lemma or monotonicity condition.

### Trivial

- Fig. 2 (distribution_shift) and its caption are somewhat difficult to parse; a statistical summary (e.g., standard deviation per column) would be more informative than the current visualization.
- The group number ablation (Table 4f) shows ARB-LLM_X with 4 groups yielding perplexity 6.55 on WikiText2 — a striking number that is not discussed or contextualized in the text. While the paper focuses on 2-group as the practical choice, this result deserves at least a brief comment.

## Nice-to-Haves

- Per-task zero-shot QA accuracy tables (rather than just average figures) would make the "surpassing FP16" claim easier for readers to verify independently.
- Reporting QA results with estimation variability (e.g., confidence intervals) would strengthen the evidential weight of the comparisons.
- Extending the ARB-X analysis to test out-of-distribution generalization (e.g., on a dataset from a different domain than C4) would address potential concerns about calibration set overfitting.
- A discussion of limitations (currently absent from the Conclusion, as noted by the critic) would improve the paper's completeness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The only direct evidence [for surpassing FP16] is the teaser figure (Fig. 1) showing OPT"** — Factually incorrect. Fig. 6 (llama-acc) shows average accuracy on 7 zero-shot QA datasets for LLaMA 1/2/3 families, directly supporting the claim for the LLaMA family as well. The critic's concern about missing per-task breakdowns is reasonable (moved to Minor), but the claim that evidence is entirely absent for LLaMA is not correct.

- **"RTN 3-bit on OPT-66B is missing"** — Factually incorrect. RTN 3-bit for OPT-66B is reported as 6,126.09 in Table 1 (line 251).

- **"The 3-bit baselines... should include AWQ, QuIP"** — Scope creep. The paper is a binary PTQ method. The comparison to 3-bit methods is secondary context, not a core claim. Demanding specific 3-bit methods goes beyond what is reasonable for this paper's scope.

- **"No error bars or variance on perplexity"** — Not standard practice for perplexity evaluation in LLM PTQ papers. The existing literature (BiLLM, GPTQ, etc.) uniformly reports single-run perplexity.

- **"ARB-X lacks a full alternating update... methodological gap"** — The paper explicitly acknowledges and justifies this (line 221): B is not updated because it is discrete and cannot be updated via gradient. This is a design constraint, not a gap. The critic's question about whether alternative B-update strategies were considered is reasonable but belongs in Discussion/Nice-to-Have territory.

- **"Missing appendix, proofs in appendix"** — Parser artifact. The supplementary exists in the original submission.

## Novel Insights

The main insight from the reviews that goes beyond the paper's own contributions is the observation that the ARB-X method's inability to update B via the L₂ gradient creates an inherent limitation: the calibration-aware updates (μ, α) operate on a frozen binary structure, which may explain why ARB-RC (which does update B via sign under L₁) consistently outperforms ARB-X despite the latter using more information-rich calibration data. This suggests an interesting open problem: how to incorporate calibration data into the B update step for binary PTQ without sacrificing the discrete nature of B. The paper's design split (L₁-based B updates vs. L₂-based μ,α updates) highlights this tension.

## Suggestions

1. Provide a supplementary table with per-task zero-shot QA accuracy for all model families, making the "surpassing FP16" claim fully transparent.
2. Add a brief ablation isolating the effect of removing μ from the effect of adding α^c in ARB-RC, to strengthen the design justification.
3. Add a sentence or two in Section 5 (Conclusion) explicitly discussing limitations, e.g., the difficulty of coupling calibration data with row-column binarization parameters, and the discrete B update constraint in ARB-X.

## Score and Decision

The paper makes a solid contribution to binary PTQ for LLMs. The alternating refinement idea is clean, well-motivated, and consistently delivers large improvements over SOTA. The three minor weaknesses identified do not undermine the core claims. The paper should be accepted with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>