Now I have all the information I need. Let me write the consolidated review.

## Summary
This paper investigates why naive output alignment fails in 1-bit post-training quantization (PTQ) for LLMs, identifying three specific problems: (i) layer-wise alignment doesn't guarantee block-level improvement, (ii) activation errors accumulate across layers, and (iii) output matching can disrupt token similarity matrices. To address these, the authors propose a method with three components: selective output alignment at the block level (restricted to the last layer of each block), a reformulated objective that uses the true full-precision output error instead of the activation-conditioned approximation, and an Attention Matrix Preservation (AMP) mechanism that preserves token-similarity structure. Experiments on OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) show consistent perplexity reductions over existing 1-bit PTQ methods.

## Strengths
- **Novel and well-motivated diagnosis of output-alignment failures (Section 3)**: The paper identifies three concrete failure modes of naive output matching in 1-bit PTQ — (a) layer-wise optimization doesn't reduce block-level loss, (b) the activation-conditioned error diverges from the true output error as quantization errors accumulate, and (c) output matching degrades token-similarity matrices. Figure 1 and Figure 2 provide clear empirical evidence for each point. This analysis is the paper's strongest contribution and genuinely advances understanding of why output-alignment approaches underperform in the 1-bit regime.

- **AMP mechanism with clean ablation evidence**: Table 3 shows that removing AMP from LLaMA-2-7B increases perplexity from 19.25 to 29.12 on C4 (a 52% increase) and from 15.42 to 26.24 on WikiText2. This clean ablation confirms that the attention-preservation component is critical, particularly for architectures using RMSNorm. The effect is notably smaller for OPT (16.22→16.35 on C4), which is consistent with the paper's architectural-sensitivity hypothesis.

- **Reformulated objective validated by ablation**: Table 4 shows that replacing the activation-conditioned error with the true output error yields consistent improvements (e.g., 19.97→19.25 on C4 for LLaMA-2-7B). This directly supports the claim that accounting for accumulated quantization error matters.

- **Broad evaluation across model families and scales**: Experiments cover OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B), with evaluation on three perplexity benchmarks plus seven zero-shot QA datasets. This scope exceeds most prior 1-bit PTQ papers.

## Weaknesses

### Fatal
None.

### Major
- **PTB outlier on LLaMA-2-7B is not adequately explained (Table 2)**: The method produces a perplexity of 3166 on PTB for LLaMA-2-7B, compared to 681.24 (ARB-X) and 763.19 (ARB-RC). The paper acknowledges this only in a single sentence: "with the exception of Llama-2-7B model evaluated on PTB dataset," followed by "the large perplexity indicates that the metric cannot provide a meaningful evaluation" (lines 237). This dismissal is unsatisfactory — the metric is clearly providing a comparative signal (ARB-X is 681 vs. Ours is 3166). While all methods degrade severely on this setting (ARB-X: 681 vs. FP: 37.91), a 4–5× gap relative to competitors requires analysis (e.g., does AMP cause instability on certain architectures/data? Is it a calibration randomness issue?). The paper's claim of "consistently outperforms" in the abstract is contradicted by this result as reported. Additionally, for LLaMA-2-13B on PTB, Ours (196.64) appears bolded as "best" but ARB-X (182.10) is actually lower (better), which is either a bolding error or a misleading presentation.

- **Selective layer assignment is not ablated (Section 4.2)**: The method restricts output alignment to only the last fully-connected layer of each block, with the justification "since it has the most direct impact on the block loss." No ablation compares this strategy against alternatives (e.g., full output alignment across all layers, alignment on a different layer, or data-driven selection). Given that Section 3.1 demonstrates layer-dependent effectiveness, this choice needs empirical support. Without it, one cannot distinguish whether the improvement comes from the selective strategy or simply from the reformulated objective + AMP.

### Minor
- **AMP objective contains a mathematical inconsistency (Eq. 9)**: The paper writes
  `max L_AMP = || (hat{X} hat{W} hat{W}^T hat{X}^T) ⊙ (X W W^T X^T) ||`
  and then claims this equals `Tr[ hat{X} hat{W} hat{W}^T hat{X}^T X W W^T X^T ]`. The Frobenius norm of an element-wise product is `sqrt(Σ_ij (A_ij·B_ij)²)`, while the trace gives `Σ_ij A_ij·B_ij` (the Frobenius inner product). These are not equal. The intended objective (maximizing the trace/Frobenius inner product) is sound, but the derivation line with ⊙ and ||·|| is incorrect and should be fixed. This does not invalidate the method (the actual computation uses the trace), but it is a clear mathematical error that must be corrected.

- **Calibration dataset details are underspecified (Section 5.1)**: The paper does not state the number of calibration samples, sequence length, or random seed used for the main experiments. It references "C4 calibration sets" only in the preliminary analysis (Section 3.1, 3.2) but not in the main experimental setup. This hinders reproducibility.

- **Average bitwidths are reported without explanation**: Tables report bitwidths like 1.06, 1.11, 1.7 without defining how these are computed. Since different methods achieve slightly different bitwidths (e.g., 1.06 vs 1.11), direct perplexity comparisons across columns are not strictly fair to the higher-bitwidth methods. The effective compression ratio should be clarified.

### Trivial
None beyond those already listed.

## Nice-to-Haves
- An ablation comparing selective vs. full output alignment would substantially strengthen the paper.
- Reporting statistical variance (e.g., across calibration subsets) would increase confidence, though single-run perplexity evaluation is the field standard.
- A direct measurement of attention-map preservation (e.g., KL divergence between FP and quantized attention maps with/without AMP) would strengthen the claim that AMP "preserves attention behavior," which is currently supported only by the token similarity proxy and the perplexity improvement.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"Mathematical error invalidates the paper's core claims"** (Harsh Critic): The critic claims the AMP notation error is fatal. It is not — the trace expression that follows is the correct Frobenius inner product, and the computation uses this expression. The error is in the intermediate derivation step (first line of Eq. 9) and should be corrected, but it does not invalidate the method.
- **"No statistical significance or error bars"**: Single-run perplexity evaluation without error bars is the standard practice in the PTQ literature for LLMs at this scale. Demanding confidence intervals would go beyond community norms.
- **"AMP hard-swap update is unjustified"**: The binary mask is a design choice. The ablation (Table 3) empirically validates that AMP works, which is sufficient.
- **Strengths that are generic/superficial** (from Strength Finder): Generic statements about the problem being important or the method being novel without specific evidence are removed.
- **"Missing related works"**: Cannot be independently verified.
- **Any criticism about the appendix, missing proofs, or formatting/typos**: The parser strips appendices and introduces formatting artifacts.

## Novel Insights
The most interesting observation from the reviews is the potential tension between the PTB outlier and the AMP mechanism's sensitivity. The paper hypothesizes that LLaMA's RMSNorm makes token-similarity preservation critical — yet the catastrophic failure on PTB (where the method is 4–5× worse than baselines) occurs precisely on a LLaMA model. This may not be a contradiction (AMP might be working correctly but some other interaction causes the failure), but the paper does not investigate it. A systematic analysis of which components break on the PTB dataset could reveal deeper architectural interactions between 1-bit quantization, normalization schemes, and sequence length. None beyond the paper's own contributions.

## Suggestions
1. Fix the AMP objective derivation (Eq. 9) by replacing the first line with the correct Frobenius inner product formulation or removing the ⊙/||·|| notation entirely.
2. Investigate the PTB failure on LLaMA-2-7B: Is it a calibration outlier, a stability issue with AMP, or a sequence-length sensitivity? Provide analysis or at minimum a more substantive discussion.
3. Add an ablation comparing selective vs. full output alignment to validate the design choice in Section 4.2.
4. Clarify the calibration dataset specifications (number of samples, sequence length, seed) and explain how average bitwidths are computed.
5. Correct the bolding in Table 2 for LLaMA-2-13B PTB (196.64) if ARB-X (182.10) is indeed better.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>