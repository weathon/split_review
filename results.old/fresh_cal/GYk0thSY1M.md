Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes Recurrent Context Compression (RCC), an autoencoder architecture for extending LLM context windows by compressing long texts segment-by-segment into multi-layer compressed vectors, which are fed into a decoder via cross-layer residual connections. The key contributions are: (1) an architecture using per-layer encoder outputs as compressed representations, (2) a two-stage training strategy (full-parameter on short sequences → freeze encoder, train decoder on longer sequences), and (3) an instruction reconstruction method to mitigate context-instruction confusion. The paper reports a 32× compression rate with BLEU-4 ≈ 0.95 on text reconstruction, near-perfect accuracy on 1M-length passkey retrieval, and competitive results on LongBench document QA.

## Strengths

1. **High compression efficiency at 32× rate**: RCC achieves BLEU-4 ≈ 0.95 at 32× compression and ≈ 0.82 at 64× (Section 4.1, Figures 3a/3b). The per-layer vector approach (ablated against last-layer-only which scores ~0.6) clearly improves reconstruction quality over traditional autoencoder designs.

2. **Near-perfect long-range retrieval on 1M-length sequences**: On the passkey retrieval task at 512× compression, RCC-Transformer-FT-32k achieves 100/100/100 accuracy at 1M sequence length (Table 2), matching or exceeding Infini-Transformer. This provides concrete evidence that the recurrent compression scheme generalizes to extremely long contexts.

3. **Instruction reconstruction method provides measurable gains**: RCC-Ins-Reconstruction (22.61 average on LongBench document QA) substantially outperforms RCC-Ins-Compress (19.61) and approaches RCC-Ins-Human (23.15, Table 3). The paper directly compares these conditions, isolating the benefit of reconstructing instructions from compressed vectors.

4. **Memory savings experimentally demonstrated**: Figure 1 shows RCC's GPU memory grows by only ~0.5 GB from 2k to 16k tokens, while Pythia-1.4b's grows by ~2 GB over just 2k tokens. This provides quantitative backing for the storage-efficiency claims.

5. **Two-stage training is practical and effective**: Freezing the encoder in stage 2 (Section 3.3.1) allows training on 32k-length sequences under limited GPU memory, validated by perfect accuracy at 1M retrieval after this training (Table 2).

## Weaknesses

### Fatal
None.

### Major

1. **LongBench evaluation lacks external baselines, undermining the "competitive performance" claim.** The paper compares RCC only with its own ablations (RCC-Ins-Reconstruction, RCC-Ins-Human, RCC-Ins-Compress) and a Pythia-SFT baseline limited to 2k context (Table 3). There are no comparisons with other context compression methods (AutoCompressor, ICAE on realistic tasks), extended-context models (LongChat, Mistral with RoPE extension), or even simple baselines like truncation. The abstract claims "competitive performance in long-text question-answering tasks compared to non-compressed methods," but the reader cannot verify this because no other method's scores on the same LongBench subsets are reported. This is the most significant evidential gap.

2. **The ICAE comparison is not well-controlled and presented without caveats.** ICAE (14B parameters) is evaluated at 64× compression, where it scores ~0.1 BLEU-4, while RCC (2.8B total parameters) scores ~0.82 (Section 4.1, Figure 3a). The paper itself notes that ICAE "experiences a significant performance drop beyond an 8x compression rate" (Introduction). Testing ICAE at 64× — far outside its designed operating range — and presenting this as evidence of RCC's superiority is misleading. A controlled comparison at rates where both methods are designed to work (e.g., 8× or 16×) is needed, along with discussion of the model size discrepancy.

### Minor

3. **True memory efficiency is unclear due to per-layer vector extraction.** The paper claims a "compression rate of 32" and says RCC "can save up to nearly 32x in storage space" (Section 4.3). However, the encoder extracts vectors from *every* layer at each selected position (Section 3.2.1). For Pythia-1.4b (24 layers) with segment length 2048 and compression rate 32: 64 positions × 24 layers = 1,536 vectors per segment. The paper says "each segment will generate a compressed vector of length 64" (Figure 1 caption) without clarifying this is per layer, making it difficult to assess the true vector count and actual memory savings relative to a full KV cache. The reported GPU memory savings (Figure 1) show the practical benefit, but the relationship between the stated "32× compression rate" and the actual vector count needs clarification.

4. **Instruction reconstruction quality degrades with context length.** RCC-Ins-Reconstruction scores drop from 28.12 (0–2k) to 17.72 (8k+) on LongBench (Table 3), while RCC-Ins-Human (gold instructions) stays more stable (25.36 → 20.48). The paper acknowledges this (Section 4.3, Limitations) but this degradation means the instruction reconstruction technique is least effective precisely where compression matters most. The method is currently most beneficial for shorter contexts, where compression is less needed.

5. **Passkey retrieval results lack variance information.** Table 2 reports accuracy triples (e.g., "94/96/96A") without explaining whether these are three independent runs, three samples, or three seeds. No standard deviations or confidence intervals are provided for any experiment. The "A" in "96A" appears to be a parsing artifact but the ambiguity about what the triples represent should be clarified.

6. **LongBench evaluation scope is limited.** Only single-document QA and multi-document QA subsets (4 subtasks) are evaluated, not the full LongBench benchmark (which includes summarization, few-shot learning, and code completion). The paper states this is due to fine-tuning dataset limitations, which is reasonable, but the scope should be clearer when making broad claims about "competitive performance."

### Trivial

7. **Some training hyperparameters are unspecified.** Learning rate is given (1e-4) but batch size, gradient accumulation steps, optimizer, and learning rate schedule are not reported. The convergence criterion ("training was stopped if the model failed to converge after one epoch or converged prematurely within an epoch") is qualitative.

## Nice-to-Haves

- A truncation baseline (Pythia-SFT on first 2k tokens of long samples) on LongBench would directly demonstrate that extending the context via RCC is beneficial.
- A direct comparison with AutoCompressor or similar compression methods on the same long-document QA tasks would strengthen the evaluation.
- A systematic analysis of what the decoder reconstructs incorrectly during instruction reconstruction (e.g., missing key instructions vs. hallucinating content) would increase confidence in the claimed problem and solution.
- A memory/quality trade-off curve showing RCC's performance at different compression rates vs. the memory cost of unconstrained inference (and alternative strategies like sparse attention or RAG).

## Removed Points

These points from the input reviews are removed or demoted with justification:

- **"Transformer can be viewed as a state space model is hand-wavy/not substantiated"**: The paper cites feng2024attention, which substantiates this claim. Removed.
- **"Abstract claim not referenced to figure"**: Formatting nitpick. Removed per hard rules.
- **"Related work doesn't differentiate from IC-LM/AutoCompressor"**: Vague; also, we cannot verify missing related-work criticisms per rules. Removed.
- **"Statement about instructional confusion not being studied is arguable"**: Reviewer opinion, not a concrete weakness. Removed.
- **"Catastrophic forgetting of frozen encoder"**: Pure speculation — no evidence presented. Removed.
- **"Pythia-No-SFT (4.41) is not a reasonable baseline"**: It is clearly used as a lower bound, not a serious comparison. Removed.
- **"94/96/96A has OCR artifact"**: Parser issue, not a paper problem. Removed per formatting rules.
- **Strength Finder dropped strengths**: "importance of the problem addressed" and other generic praises are removed as lacking specific evidence.
- **"The 'average' in LongBench table unspecified"**: The paper explicitly states "single-document QA and multi-document QA tasks." The critic missed this. Removed.

## Novel Insights

None beyond the paper's own contributions. The two-stage training strategy (freeze encoder for long-sequence fine-tuning) is a practical insight that could benefit other compression methods, but it is already present in the paper.

## Suggestions

1. **Add external baselines on LongBench.** Report scores from at least 2–3 comparable methods (AutoCompressor, ICAE at reasonable compression rates, a truncation baseline) on the same document QA subsets. This single addition would significantly strengthen the paper's core claims.

2. **Clarify the relationship between "compression rate" and actual vector count.** Provide a worked example: for an input of length N with compression rate R, state how many vectors (per layer and total) the decoder receives, and translate this into a comparison with the KV cache size of standard decoding.

3. **Explain what the passkey triples in Table 2 represent** (e.g., three random seeds, three runs, or three samples per condition).

4. **Report variance** (standard deviations or bootstrapped intervals) for at least the main results (reconstruction, LongBench).

5. **Either report ICAE at a rate within its design range (e.g., 8×) or add a caveat** that the comparison at 64× is beyond ICAE's intended operating range.

## Score and Decision

The paper presents a sound architecture and training recipe with impressive results on synthetic tasks (text reconstruction at 32×, 1M-length passkey retrieval). The method is genuinely novel in its use of multi-layer compressed vectors and two-stage training. However, the evaluation on realistic long-context tasks is significantly incomplete: the LongBench results lack any external baselines, and the ICAE comparison is not well-controlled. These gaps prevent the paper from fully supporting its claims of being "competitive" on real-world tasks. The core technical contributions are solid but the evidence for practical usefulness needs substantial expansion.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>