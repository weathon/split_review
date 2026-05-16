Now I have all the information needed. Let me synthesize the final review.

## Summary

STBLLM introduces a structured binarization framework that compresses LLM weights below 1-bit precision (as low as 0.55 bits) by combining N:M structured sparsity with binarization. The method contributes a gradient-free Standardized Importance (SI) metric for pruning, an adaptive layer-wise N:M assignment, a trisection-based non-salient aware quantization scheme, and a specialized CUDA kernel leveraging NVIDIA sparse tensor cores. Experiments across LLaMA-1/2/3, OPT, and Mistral show large perplexity and zero-shot accuracy improvements over the sub-1-bit BiLLM baseline, with up to 17.85× kernel speedup.

## Strengths

- **First sub-1-bit LLM compression with compelling performance gains**: STBLLM achieves extreme compression while maintaining far better performance than prior 1-bit methods. At 0.55 bits on LLaMA-1-7B, perplexity is 31.72 versus 688.73 for the BiLLM-based baseline (Figure 2). At 65B scale, 0.55-bit STBLLM surpasses BiLLM's 0.7-bit version (11.07 vs. 11.57, Table 2). On LLaMA-1-30B zero-shot tasks, STBLLM(4:8) averages 51.78% accuracy vs. 43.72% for BiLLM(4:8) (Table 4).

- **Novel SI metric that outperforms alternatives in the binary pipeline**: The Standardized Importance metric is gradient-free and computationally efficient, yet achieves lower perplexity than magnitude, Wanda, and SparseGPT when used in the same STBLLM pipeline (Table 5). This is shown on both LLaMA-1-7B and LLaMA-2-7B under 4:8 configuration.

- **Effective adaptive layer-wise assignment**: The L2-norm-based per-layer N:M allocation consistently outperforms uniform and sin-shaped strategies across model families (Table 6), demonstrating that non-uniform sparsity ratios help balance compression and accuracy.

- **Non-salient aware quantization substantially reduces degradation**: The trisection-based grouping of non-salient weights into sparse/intermediate/dense regions (Table 8) drops perplexity from 57.78 to 10.06 on LLaMA-2-7B (4:8) compared to BiLLM's bell-shaped splitting, isolating a clear source of gain.

- **Hardware-validated speedup**: The CUDA kernel reaches 263.45 TFLOPS (79.74% of RTX4090 sparse tensor core peak) and delivers up to 17.85× speedup over ABQ-LLM's 2-bit implementation at sequence length 8192 (Figure 4).

## Weaknesses

### Fatal
None.

### Major

1. **The sub-1-bit BiLLM baseline conflates pruning metric with binarization innovation**. As stated in Section 4.1: "We conduct the N:M sparsity using Wanda (Sun et al., 2024) as the baseline." So the baseline = Wanda pruning + BiLLM's binarization, while STBLLM = SI pruning + its own binarization/quantization. The ablation in Table 5 already shows SI outperforms Wanda for the *same* STBLLM pipeline, confirming that a significant fraction of the reported gains (e.g., 688.73 → 31.72 at 0.55 bits) could originate from the better pruning metric rather than from the binarization or non-salient quantization innovations. A controlled comparison — e.g., applying SI pruning + BiLLM's binarization — is needed to isolate the contribution of STBLLM's novel quantization scheme. This does not invalidate the full pipeline as a practical contribution, but it weakens claims about the superiority of the binarization components per se.

### Minor

2. **Unclear separation between Hessian-based and SI-based importance**. Section 3 states: "We leverage the Hessian matrix to distinguish between salient and non-salient weights for the binarization process." Section 3.2 then motivates SI as avoiding "the second-order information of the weights, which can be computationally expensive for LLMs." Since the Hessian is still used for the salient/non-salient split, the characterization of the method as "gradient-free" or avoiding second-order information applies only to the pruning step, not the full pipeline. This should be explicitly clarified to avoid misleading readers about the total computational overhead.

3. **Adaptive layer-wise assignment formula may not ensure the claimed overall compression ratio**. The formula $N_i/M_i = \alpha_i + (1-\alpha_i)\cdot R_{\text{target}}$ is stated to "ensure the overall compression ratio meets $R_{\text{target}}$" (Section 3.3). For non-uniform layer sizes, the weighted average of $N_i/M_i$ across layers will not generally equal $R_{\text{target}}$ under this definition. The constraint equation and a proof (or at minimum an empirical verification that the actual ratio is close to target) are missing.

4. **Connection between the random-flip observation (Figure 1) and N:M pruning is not explicitly argued**. The paper motivates compression by showing that flipping binary weight signs has little effect, but then applies N:M *pruning* (zeroing out weights). Flipping preserves the parameter count and distribution, while pruning removes parameters entirely — these operations have different effects on the retained weights and the subsequent binarization. A brief argument connecting the two would strengthen the motivation.

5. **Unexplained SparseGPT underperformance in Table 5**. SparseGPT — typically a strong pruning method — performs worse than both Wanda and SI under the N:M binary setting. The paper notes only that SparseGPT "requires second-order information" and has "massive computation burden" (Section 4.4), but does not discuss why it produces worse *perplexity* than simpler methods. Since this is a somewhat surprising result, a brief explanation (e.g., interaction between SparseGPT's reconstruction and binarization) would be helpful.

6. **Per-configuration breakdown of $r_{\text{salient}}$ and resulting bit components is not provided**. Table 1 shows the average bits, but the paper does not report explicit $r_{\text{salient}}$ values or $b_{\text{size}}$ per configuration. While $b_{\text{size}} = 128$ is mentioned for the main results (Section 4.2), readers cannot verify the bit-width derivations in Table 1 without reverse-engineering.

7. **The specific form of $\mu(|\mathbf{W}_{i,j}|)$ in the SI metric (Equation 2) — the sum of L1-normalized magnitudes along both input and output dimensions — is introduced heuristically without intuitive motivation**. Why this particular combination, rather than, say, the product or the max of the two normalizations? A brief justification would improve the reader's understanding.

### Trivial
None.

## Nice-to-Haves

- **Compare against a 1-bit dense kernel** to isolate the speedup attributable to N:M structure itself versus the lower bit-width. The current comparison against ABQ-LLM (2-bit) mixes both differences.
- **Report the trisection thresholds $p_1^*, p_2^*$** that emerge across layers, to strengthen the claim that the Gaussian non-salient distribution is meaningfully split into three regions.
- **Add a simple baseline**: apply magnitude-based N:M pruning to the full-precision model *without* binarization, to contextualize how much degradation comes from sparsity vs. binarization.
- **Run a small-scale variance analysis** (e.g., LLaMA-7B with different calibration subsets) to show result stability.

## Removed Points

These points were raised by reviewers but are removed or downgraded for the following reasons:

- **"Sin-shaped baseline is arbitrary"** — The paper defines it as a sine-wave pattern from low to high sparsity across layers. Whether it is "arbitrary" is a matter of design choice; it serves as a concrete alternative allocation strategy. This is not a meaningful weakness.
- **"No statistical significance or variance reported"** — Single-run perplexity evaluation is standard practice in the LLM quantization literature. Moved to Nice-to-Haves.
- **Missing comparison: SI + BiLLM binarization as a baseline** — This is the core of Weakness #1 (Major) already captured above; the critic's further elaboration on this point is redundant.
- **"CUDA kernel comparison lacks details about ABQ-LLM's kernel"** — The paper reports TFLOPS and % of peak utilization, which is the standard way to characterize kernel performance. Further architectural details about the baseline kernel are not required for the speedup claim to be valid. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core narrative — that combining N:M sparsity with binarization via a careful pipeline can break the 1-bit barrier — but do not surface a fundamentally different interpretation of the results beyond the baseline-fairness concern.

## Suggestions

1. **Construct a controlled baseline**: Apply SI (the paper's own pruning metric) for the N:M pruning step, then use BiLLM's binarization (residual approximation + bell-shaped splitting) for the retained weights. Compare this against the full STBLLM pipeline. This directly isolates the gain from the non-salient aware quantization, adaptive assignment, and any other binarization-side innovations.

2. **Clarify Hessian usage**: State explicitly that SI replaces Hessian-based importance only for the N:M pruning step, while Hessian information is still used for the salient/non-salient split in binarization. Report the total overhead including both steps.

3. **Verify or correct the adaptive assignment formula**: Either prove that the formula satisfies the global $R_{\text{target}}$ constraint (accounting for non-uniform layer sizes), or empirically report the actual achieved compression ratio alongside the target for each configuration.

4. **Comment on SparseGPT's worse perplexity** in the binary N:M setting — this is a non-obvious result that deserves a short hypothesis (e.g., second-order reconstruction may overfit to the calibration set when combined with binarization).

## Score and Decision

**Originality**: Good — the combination of N:M sparsity with binarization for sub-1-bit LLM compression is new.  
**Importance of question**: High — extreme LLM compression has clear practical relevance.  
**Claims supported**: Partially — the central comparison is weakened by the metric confound, though ablations partially disentangle contributions.  
**Soundness of experiments**: Solid breadth (many model families, sizes, and zero-shot tasks), but the baseline fairness gap is a real concern.  
**Clarity**: Generally clear, though the Hessian/SI duality and the adaptive formula need better exposition.  
**Value to community**: Positive — the method and kernel could be useful for deployment of LLMs on resource-constrained hardware.

The paper has a genuine contribution and the core results are striking, but the main evaluation is weakened by a confounded baseline that prevents clean attribution of gains. The issue is addressable with additional controlled experiments. I recommend acceptance contingent on the authors addressing the baseline fairness concern.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>