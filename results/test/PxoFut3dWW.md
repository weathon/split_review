Now I have a thorough understanding of the paper and can verify all claims against the source text. Let me write the final consolidated review.

---

## Summary

This paper introduces Wanda, a pruning method for large language models that uses a simple metric—weight magnitude multiplied by the input activation norm—applied on a per-output basis. The key contribution is that Wanda matches or competes with the state-of-the-art SparseGPT method across LLaMA and LLaMA-2 model families (7B–70B) on both perplexity and zero-shot accuracy, while requiring no weight update and being orders of magnitude faster to compute (e.g., 0.54s vs. 203.1s on LLaMA-7B). The paper also provides a theoretical connection to Optimal Brain Damage and extensive ablations showing the importance of the per-output comparison group and robustness to few calibration samples.

## Strengths

- **Simple metric that rivals Hessian-based methods without weight update**: Wanda's metric (|W_ij| · ||X_j||_2) matches SparseGPT across model sizes and sparsity levels, despite SparseGPT requiring expensive second-order inverse computation and a weight update procedure. For example, on LLaMA-13B at 50% sparsity, Wanda achieves 59.33% zero-shot accuracy vs. SparseGPT's 58.61% (Table 1), and perplexity 6.15 vs. 6.21 (Table 2)—all without modifying any retained weights.

- **Orders-of-magnitude faster pruning**: Computing Wanda's pruning metric takes 0.54 seconds on LLaMA-7B vs. 203.1 seconds for SparseGPT (Table 3), a ~375× speedup. This gap holds across all model sizes (e.g., 5.6s vs. 1353.4s on LLaMA-65B). The paper transparently states this measures only the metric computation time, excluding the forward pass common to both methods (Section 4.3).

- **Per-output pruning insight is novel and empirically validated**: The paper identifies that comparing weights per output neuron (rather than per-layer or per-input) is consistently better for LLMs. The ablation (Table 4) shows this holds for both Wanda's metric (7.26 perplexity for per-output vs. 7.95 for per-layer) and the SparseGPT metric (7.41 vs. 7.91). The paper also verifies this does not generalize to image classifiers, suggesting the finding is LLM-specific.

- **Robustness with very few calibration samples**: Figure 2 shows Wanda achieves perplexity of 7.66 on LLaMA-7B at 50% sparsity with just a single calibration sample, whereas SparseGPT's performance degrades more sharply with few samples. This is practically important for data-constrained deployment scenarios.

- **Clean theoretical connection to classical pruning theory**: The paper explicitly derives Wanda's metric as a diagonal approximation of SparseGPT's Hessian-based score (Eq. 3), situating Wanda as a "renaissance of Optimal Brain Damage" (OBD) adapted to the local reconstruction objective used by SparseGPT/OBS.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the experiments, and no structural flaw undermines the contribution.

### Minor
- **"Single forward pass" claim is slightly imprecise**: The paper states Wanda "can be done with a single forward pass of the LLM" (Abstract, Section 3 bullet 2, line 154). However, the procedure is sequential: pruning earlier layers affects the activations fed into later layers (lines 97–98, acknowledged by the authors). In practice, this is still one inference pass with layer-by-layer pruning applied during it, and the computational cost is far below SparseGPT's. The phrasing could mislead readers into thinking all layers can be pruned in parallel without the sequential dependency. This does not affect the correctness of the results but is a precision issue worth clarifying.

- **Zero-shot results reported only as means across 7 tasks without per-task breakdowns or variance**: Table 1 reports mean accuracy without showing individual task scores or standard errors. This is conventional in this literature, but it limits the reader's ability to assess whether small differences between Wanda and SparseGPT (e.g., 54.21 vs. 54.94 on LLaMA-7B at 50% sparsity) are systematic or task-specific. The paper does not overclaim—it correctly states Wanda is "competitive"—so this is a minor completeness concern, not a threat to the conclusions.

- **Fine-tuning analysis limited to LLaMA-7B with LoRA only on Q/V projections**: The fine-tuning experiments (Table 5) are conducted only on LLaMA-7B, and LoRA adapters are applied only to query/value projections in attention layers, not to MLP layers or other projections affected by pruning. Given the stated compute budget constraints (1 GPU/12h for LoRA), this is understandable but limits the generalizability of the fine-tuning findings.

### Trivial
None.

## Nice-to-Haves

- An analysis quantifying the overlap between weights preserved by Wanda and the large-magnitude input features that motivate the method (e.g., how often does Wanda preserve weights on channels with outlier activations vs. magnitude pruning?) would further substantiate the mechanism.
- Extending the fine-tuning analysis to larger models (e.g., LLaMA-13B or 30B) would strengthen the practical relevance of the recovery results.
- Reporting per-task zero-shot results in an appendix would allow deeper comparison with SparseGPT.

## Removed Points

- The harsh critic's observation about the speed comparison (Table 3 measuring only pruning metric computation, excluding forward passes) is kept as context but not listed as a weakness, since the paper explicitly states this (line 263: "excluding the forward pass process shared by both methods"). The critic correctly notes this is not a flaw.
- The harsh critic's suggestion to add a table for the image classifier experiment: this would be a nice addition but the paper's one-sentence statement (line 72) is sufficient for the scope. The paper is about LLM pruning, not image classifiers.

## Novel Insights

None beyond the paper's own contributions. The paper is transparent about what it does and the reviews do not surface an original insight not already present in the paper's own analysis.

## Suggestions

- Clarify the "single forward pass" phrasing in Section 3 to explicitly note the sequential dependency (pruning earlier layers affects later activations), distinguishing "one inference pass" from "fully parallelizable across layers."
- Add per-task zero-shot results in an appendix or supplementary material to enable more granular comparison.
- Consider extending the fine-tuning analysis to MLP-layer LoRA adapters or larger model sizes in future work.

## Score and Decision

This is a clean, well-executed paper. The core contribution—a simple, theoretically grounded pruning metric that matches SparseGPT without weight update and at a fraction of the computational cost—is novel, well-motivated, and thoroughly validated across multiple model families, sizes, sparsity types, and evaluation metrics. The experiments are extensive (LLaMA and LLaMA-2 from 7B to 70B, three sparsity types, both perplexity and zero-shot evaluation, plus ablations on comparison groups, calibration sample size, and weight update effects). The paper is clearly written and appropriately frames its claims. The weaknesses are minor and do not affect the central contribution.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>