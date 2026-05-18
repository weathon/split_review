I now have a thorough understanding of the paper, the critic's claims, and the strength finder's output. Let me produce the final consolidated review.

## Summary

This paper introduces LoQA, a method that integrates LoRA with quantization by jointly fine-tuning both quantization scale (S) and zero-point (Z) parameters via two technical contributions: HQ-LoRA (a reformulation of the quantization operator to enable low-rank updates to both S and Z) and QBAS (bit-width-aware scaling of the LoRA update magnitude). The key motivation is overcoming QA-LoRA's limitation of only fine-tuning zero-points. Experiments on LLaMA-1/2/3 models show consistent accuracy gains over QA-LoRA, with particularly strong results in ultra-low-bit (2-bit) regimes where LoQA outperforms the prior state-of-the-art by 4.7% on MMLU.

## Strengths

- **Expanding the optimization space to both scale and zero-point yields measurable gains.** The core idea — using two LoRA branches to update both S and Z — is well-motivated and validated by ablation (Table 7), where HQ-LoRA at rank 32 outperforms QA-LoRA at rank 64, showing the improvement comes from optimization space, not just parameter count.

- **Consistent accuracy improvements across model scales and datasets.** On MMLU after Flan v2 fine-tuning (Table 1), LoQA-4bit outperforms QA-LoRA by +2.2 pts (7B), +1.4 pts (13B), and +1.7 pts (30B). The same trend holds on Alpaca (Table 3). These gains are systematic and scale with model size.

- **Impressive ultra-low-bit performance.** LoQA-2bit achieves 47.4% on MMLU, surpassing IR-QLoRA (42.7%) by 4.7 pts and even the full-precision 16-bit model (43.6%) by 3.8 pts (Table 2). This is a striking result — accuracy improvement despite 2-bit compression — and is the paper's strongest empirical contribution.

- **QBAS ablation supports its effectiveness.** Table 6 shows removing QBAS degrades performance across 4/3/2-bit settings, confirming that the bit-width-aware scaling addresses real instabilities in training quantized LoRA.

## Weaknesses

### Fatal
None.

### Major

1. **Unresolved mathematical gap in the forward pass and merging procedure for group size > 1.** Equation (6) defines the forward pass using pooled input \(x'\) (dimension \(D_{\text{in}}/g\)) for both LoRA terms. However, the third term \((W^{\text{Int}} \odot f((B'A'), g)) \cdot x'\) has a dimensional mismatch: the matrix is \(D_{\text{out}} \times D_{\text{in}}\) while \(x'\) is \((D_{\text{in}}/g) \times 1\). Furthermore, the merging of BA into Z (Eq. 8–9) introduces a factor-of-\(g\) discrepancy between training behavior (where BA operates on pooled \(x'\)) and inference behavior (where the merged Z is applied to the original full-dimensional input \(x\) via the column-duplication operator \(f\)). The paper only provides a rigorous derivation for the \(g=1\) case and hand-waves \(g>1\) as "maintaining consistency" without proof. While the method clearly works empirically, this gap in the theoretical foundation undermines the claimed "mathematical equivalence." The authors should either prove the equivalence for general \(g\), correct the dimensional issue in Eq. 6, or clearly state the approximation and its impact.

2. **No efficiency measurements despite inference efficiency being a core selling point.** The paper repeatedly emphasizes that LoQA "maintains the quantized format" and preserves inference efficiency. Section 4.3 ("Inference Efficiency") only lists compatible acceleration toolboxes (MLC-LLM, AWQ, etc.) without reporting any latency, throughput, or memory measurements. Since one of the paper's central claims is preserving quantized inference structure (unlike QLoRA which reverts to FP16), the complete absence of efficiency benchmarks is a substantive gap that prevents assessing the method's practical value.

### Minor

1. **Baseline comparisons to QLoRA and IR-QLoRA may not be controlled.** The paper states that QA-LoRA was reproduced "under the same environment and on the same machines." However, it does not explicitly confirm that IR-QLoRA and QLoRA results were obtained under identical training conditions (learning rate, batch size, steps, optimizer settings). While QA-LoRA is the most directly comparable baseline (same quantized-format-preserving setting), the strong claim of outperforming IR-QLoRA by 4.7% at 2-bit would benefit from verification under controlled conditions.

2. **Missing implementation details needed for reproducibility.** The paper does not specify (a) whether the two LoRA branches (BA for zero-point, B'A' for scale) share the same rank or are set independently; (b) the exact pooling operation (applied across which dimension); (c) training hyperparameters such as learning rate, optimizer, batch size, and number of training steps. The LoRA rank is stated as 64 for "all adaptation methods" but the scale branch rank is not separately discussed.

3. **QBAS applies the same scaling factor to both LoRA branches without discussion.** The scaling factor \(s = \alpha / (r \cdot \text{maxq})\) is applied to both the zero-point LoRA (BA) and the scale LoRA (B'A'). The paper only motivates this for the scale branch (which interacts with \(W^{\text{Int}}\)). It does not discuss whether the same scaling is optimal for the zero-point branch, which does not interact with \(W^{\text{Int}}\).

### Trivial

- The claim that HQ-LoRA has an "intrinsic ability to more efficiently utilize the parameter space" (from the parameter ablation) is speculative without analysis of what the learned scale/zero-point updates actually do (e.g., per-layer breakdowns or visualizations of changes).

## Nice-to-Haves

- Latency/throughput benchmarks comparing merged LoQA to the original quantized model and to an unmergeable LoRA baseline (QLoRA).
- Ablation exploring different scaling factors for the two LoRA branches, or a principled justification for sharing the same scaling.
- Per-layer performance breakdown to understand where the scale vs. zero-point updates contribute most.
- Explicit statement of training hyperparameters (learning rate, batch size, optimizer, steps, hardware) in a dedicated experimental settings subsection.

## Removed Points

These points from the original reviews were removed with justification:

1. **"LLaMA3 results contradict the paper's main claims."** — Removed. The paper handles this transparently: it cites (Huang et al., 2024) showing that ALL fine-tuning methods on Alpaca degrade LLaMA3's MMLU (NF4 zero-shot 62.5 → QLoRA fine-tuned 56.7). LoQA achieves lower loss than QA-LoRA on LLaMA3, so it is actually better than the comparable baseline. The MMLU degradation is a dataset issue, not specific to LoQA.

2. **"The claim of mathematical equivalence to the original operator is misleading."** — Removed. This misreads the paper. The claim is that the reformulated quantization operator (the rewriting of the dequantization formula to separate S and Z) is mathematically equivalent to the standard dequantization formula — not that adding LoRA terms is equivalent to not adding them. This is a standard and reasonable claim.

3. **"The paper does not specify the LoRA rank used for the scale branch."** — Partially addressed. The paper states "rank =64 for all adaptation methods" (Table 1 caption) but doesn't separately discuss whether both branches use this rank. This is already covered in Minor weaknesses.

4. **"LLaMA-30B results are not clearly presented."** — Removed. The text explicitly mentions LLaMA-30B results (line 218), and the tables (as images) include them. The parser likely stripped the table content but the paper does present these results.

5. **"The paper does not disclose training hyperparameters."** — Partially addressed in Minor weaknesses as a missing implementation detail, but reformulated more precisely (the original critic's complaint was about the LLaMA-30B table).

6. **Strength Finder claim #5 about "maintains inference efficiency"** — Weakened. The claim is about the design principle (merging preserves format) rather than measured efficiency. The verified weakness about missing efficiency measurements means this should not be claimed as a demonstrated strength, only as a design claim.

## Novel Insights

The most interesting observation from the reviews is the unresolved factor-of-\(g\) discrepancy between the training forward pass (using pooled inputs) and the merged inference (operating on full-dimensional inputs). This gap is genuinely novel: it suggests that either (a) the method implicitly relies on the scaling factor or learning rate to absorb this constant factor during training, or (b) the \(g>1\) case actually implements a subtly different function than claimed. Since the empirical results are strong, this likely manifests as a harmless constant rescaling rather than a broken method, but making this explicit would strengthen the paper. The 2-bit results (outperforming the FP16 baseline) are the paper's most novel empirical finding and warrant deeper analysis.

## Suggestions

1. **Fix the mathematical gap.** Provide a clean derivation showing either that the forward pass with pooling and the merged inference are equivalent (accounting for the factor of \(g\)), or clearly state the approximation. Fix the dimensional mismatch in Equation (6) for \(g>1\).

2. **Add efficiency measurements.** Report tokens/second or wall-clock time for merged LoQA vs. the baseline quantized model, even if on a single GPU. This directly supports the inference efficiency claim.

3. **Reproduce all baselines** under identical conditions for the main comparisons (especially the 2-bit LoQA vs. IR-QLoRA claim), or clearly mark which numbers are from original papers.

4. **Add a dedicated experimental settings subsection** specifying learning rate, batch size, optimizer, gradient steps, hardware, and the rank configuration for both LoRA branches.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>

**Rationale**: The paper tackles an important problem and shows compelling empirical results, particularly the 2-bit results that surpass the FP16 baseline. However, the unresolved mathematical gap in the forward pass/merging procedure for \(g>1\) represents a real theoretical weakness in the paper's core formulation that goes beyond presentation issues. Combined with the absence of any efficiency measurements (undermining a key claimed advantage) and insufficient experimental details for reproducibility, the paper is not yet ready for acceptance. The core contribution is promising and the empirical trends are clear, but the theoretical grounding and experimental completeness need substantial revision. The paper should be encouraged to resubmit after addressing these issues.