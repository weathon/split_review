I now have a thorough understanding of the paper and both sets of reviewer comments. Let me synthesize the final review.

## Summary

This paper introduces Recurrent Context Compression (RCC), an autoencoder-based method for compressing long text sequences into compact vector representations to extend the effective context window of LLMs under memory constraints. RCC extracts compressed vectors from each encoder layer, feeds them into a decoder via residual connections, and employs a two-stage training strategy (full fine-tuning on short sequences, then frozen-encoder training on longer sequences) to scale context length. The paper also proposes an instruction reconstruction method to mitigate instruction-context confusion when both are compressed. RCC achieves BLEU-4 of 0.95 at 32× compression and near-perfect accuracy on a 1M-token passkey retrieval task, with significantly reduced memory growth compared to uncompressed models.

## Strengths

1. **High compression efficiency with strong reconstruction fidelity.** RCC achieves BLEU-4 of 0.95 at 32× compression and ~0.82 at 64×, substantially outperforming ICAE (~0.1 at 64×) as shown in Figures 2a/2b. Using compressed vectors from all encoder layers (rather than just the last layer) is validated as a key design choice, raising BLEU-4 from ~0.6 to ~0.82 at 64×.

2. **Robust length extrapolation to extreme sequence lengths.** On passkey retrieval, RCC achieves near-100% accuracy at 1M tokens after two-stage fine-tuning on only 32k-length data (Table 2). Even with just 8k training, it maintains ~90%+ accuracy up to 1M, demonstrating that the compressed vectors generalize far beyond training lengths.

3. **Dramatic reduction in inference memory growth.** As shown in Figure 8, processing 16k tokens increases RCC's GPU memory by only ~0.5 GB, versus a 2 GB increase for Pythia-1.4b on just 2k tokens. The memory savings grow with sequence length, enabling long-context processing where standard models would be infeasible.

4. **Practical solution to instruction-context confusion.** The instruction reconstruction method demonstrably improves downstream QA (Table 3): RCC-Ins-Reconstruction (avg 22.61) outperforms RCC-Ins-Compress (avg 19.61) and approaches RCC-Ins-Human (avg 23.15) which uses ground-truth instructions. This addresses a problem that prior compression work has overlooked.

5. **Versatility across encoder architectures.** RCC works with both Mamba and Transformer encoders (Table 2 shows strong passkey results for both), allowing practitioners to choose the most efficient encoder for their deployment constraints.

6. **Practical two-stage training strategy.** Freezing the encoder after initial full fine-tuning on shorter sequences enables scaling training to 32k-length contexts without prohibitive memory. The passkey results validate that this strategy is effective despite the encoder being frozen.

## Weaknesses

### Fatal

None. The paper's core contributions (compression efficiency, passkey retrieval, memory savings) are well-supported by evidence, and no weakness identified invalidates them.

### Major

1. **Missing long-context baseline on LongBench undermines the "competitive performance" claim.** The only non-compressed baseline (Pythia-SFT) is evaluated exclusively on sequences under 2k tokens, which is its context limit. For sequences above 2k — where the method's claimed advantage lies — there is no non-compressed baseline whatsoever (Table 3). Without a baseline that can actually process long texts (e.g., via positional interpolation, NTK-aware scaling, or a different LLM with a native long window), the claim that RCC achieves "competitive performance in long-text question-answering tasks compared to non-compressed methods" (abstract) is not properly supported. The reader cannot assess the quality-compression trade-off because the comparison is missing on the very regime that matters.

2. **Unexplained anomaly in Table 3 (RCC-Ins-Reconstruction > RCC-Ins-Human on 0–2k).** On the shortest length bin (0–2k), RCC-Ins-Reconstruction (28.12) outperforms RCC-Ins-Human (25.36), which uses the ground-truth instruction directly. This reversal is theoretically counterintuitive — a learned reconstruction beating the oracle condition — and the paper offers no explanation. Possible causes (different prompt formatting, the reconstruction providing more contextually grounded instructions, etc.) are not discussed. Since the instruction reconstruction claim rests on this comparison, the anomaly must be resolved or explicitly justified for the results to be fully credible.

3. **Architecture description lacks precision needed for reproducibility.** While the overall design is communicated, several critical details are underspecified (Section 3.2, lines 59–64). It is unclear whether the "residual connection" between each decoder block's output and the corresponding layer's compressed vector is addition or concatenation. How the positions of compressed vectors are tracked for selective residual application is not explained. The mechanism by which compressed vectors interact within the decoder (self-attention? cross-attention? additive bias?) is ambiguous. Since the architecture is the paper's primary contribution, these ambiguities limit assessment and adoption.

### Minor

1. **Instruction reconstruction quality is not reported as a separate metric.** The paper attributes performance degradation on longer samples to poor instruction reconstruction (Section 6, Limitations) but never directly measures reconstruction accuracy (e.g., ROUGE-L or BLEU between reconstructed and ground-truth instruction). Separating reconstruction failure from general context compression loss would strengthen the analysis.

2. **Two-stage training benefit from freezing is not fully isolated.** While the paper convincingly shows that two-stage training (stage 1: full FT on 8k, stage 2: frozen encoder on 32k) improves passkey accuracy, there is no ablation comparing against alternatives like training with gradient checkpointing or LoRA on longer sequences during stage 2. The freezing strategy is pragmatically motivated by memory constraints and clearly works, but the paper would be stronger with an explicit documentation of why full fine-tuning on 32k is infeasible with their resources.

3. **No ablation on number of encoder layers used.** The paper shows that using all layers outperforms using only the last layer (Figure 2a), but does not explore intermediate configurations (e.g., every other layer, top k layers). Similarly, the trade-off between compression rate and QA accuracy is not explored — only a single rate (32×) is used on LongBench.

### Trivial

- BLEU-4 for reconstruction conflates fluency with fidelity, though it is a standard metric for the task. Reporting perplexity or token-level accuracy on held-out reconstruction tokens would be more informative but does not invalidate the current results.
- Some notation inconsistencies: Table 2 uses "32K" and Table 3 uses "0-2k" as column headers.

## Nice-to-Haves

- Adding a long-context baseline on LongBench (e.g., Pythia with NTK-aware scaling or YaRN to extend to 16k) would directly test whether RCC's compression trade-off is worthwhile.
- Reporting instruction reconstruction quality (ROUGE-L or BLEU) alongside QA scores on LongBench would help disentangle whether degradation at long lengths stems from instruction recovery failure or broader compression loss.
- Exploring the compression rate vs. QA accuracy trade-off on LongBench (e.g., 16× vs. 32× vs. 64×) would clarify how much degradation is attributable to compression.
- An ablation on the number of encoder layers used for compressed vectors (e.g., top-k, every-other) would strengthen the architectural understanding.

## Removed Points

These points were reviewed and determined to be inaccurate, misdirected, or otherwise not valid weaknesses of this paper:

- **"Different compression rates across tasks without justification"** (Critical Issue 5 from harsh critic): The paper explicitly addresses this — Section 5.2 states "Although this compression rate [512×] might not be effective for reconstruction tasks, experiments show that the fine-tuned RCC model performs well in the passkey retrieval task." The reviewer missed this passage. Different tasks naturally warrant different compression rates given their difficulty.

- **"Memory comparison conflates inference memory with storage"**: The paper clearly states the asymptotic nature of savings ("as text length increases, RCC can save up to nearly 32× in storage space") in context of the memory growth rate shown in Figure 8. The claim is about marginal memory growth, not total storage. The reviewer misreads this.

- **"The benefit of freezing is not isolated" framed as a critical issue**: The paper never claims freezing causes improvement; it claims the two-stage training ENABLES longer-context training under memory constraints. The passkey results validate the method works. An ablation would be nice (moved to Minor) but the paper's claim is accurate as stated.

- **Formatting/style nitpicks and missing appendix concerns**: These are parser artifacts, not author errors.

## Novel Insights

The cross-paper observation that ties these reviews together is that both the harsh critic and strength finder agree on the paper's genuine contributions (compression efficiency, passkey retrieval, memory savings, instruction reconstruction) but diverge sharply on how to weigh the evaluation gaps. The central tension is not about whether the method works — the evidence there is strong — but about whether the paper has adequately benchmarked its claimed regime of advantage (long-context QA). The missing long-context baseline is a consequential oversight because it makes the "competitive performance" claim untestable; however, the passkey retrieval task, while synthetic, provides strong indirect evidence that the compressed representations preserve task-relevant information even at extreme lengths. A fair assessment treats the evaluation as incomplete in one specific dimension (LongBench non-compressed baselines) rather than viewing the paper as fatally flawed.

## Suggestions

1. Add a long-context baseline to the LongBench evaluation. The most direct approach: extend Pythia-1.4b's context window via a lightweight method (e.g., NTK-aware scaling or YaRN to 16k), fine-tune on the same instruction data, and compare per-bin performance. This would directly test whether RCC's trade-off (memory savings for accuracy) is worthwhile.

2. Resolve the RCC-Ins-Reconstruction > RCC-Ins-Human anomaly on the 0–2k bin. If it is a genuine result (e.g., the reconstruction provides more contextually grounded instructions), explain why. If it reflects a confound (different prompt formats, evaluation differences), fix the setup and re-evaluate.

3. Provide a precise algorithmic description of the decoder's forward pass, clarifying: (a) whether residual connections are additive or concatenative, (b) how compressed vector positions are tracked in the sequence, and (c) whether the compressed vectors participate in self-attention or are used as additive biases.

4. Report instruction reconstruction accuracy (e.g., ROUGE-L) as a secondary metric on LongBench to support the paper's own diagnosis that instruction reconstruction degrades at longer lengths.

## Score and Decision

The paper makes genuine contributions — high compression efficiency with strong fidelity, impressive length extrapolation, practical memory savings, and a useful instruction-reconstruction method. However, the evaluation has two substantive gaps: the missing long-context baseline weakens the central comparative claim, and the unexplained anomaly in Table 3 undermines confidence in one key comparison. These are fixable but require attention before the paper is ready. The architecture description, while not as vague as alleged, needs tightening for reproducibility.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>