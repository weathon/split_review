Here is my consolidated final review after verifying all claims against the actual paper.

---

## Summary

This paper proposes Recurrent Context Compression (RCC), an autoencoder-based method that compresses long contexts into compact vector representations to extend the effective context window of Transformer LLMs. The encoder cyclically segments and compresses long sequences into compressed vectors, which the decoder reads via cross-attention. The paper also introduces a two-stage training strategy (full fine-tuning on short sequences, then frozen encoder + decoder fine-tuning on longer sequences) to manage memory during long-sequence training, and an instruction reconstruction method to mitigate performance degradation when both instructions and context are compressed. Experiments include text reconstruction (BLEU-4), passkey retrieval up to 1M tokens, and LongBench document QA.

---

## Strengths

1. **High compression efficiency with strong reconstruction quality.** At 32× compression, RCC achieves a BLEU-4 score of 0.95 on text reconstruction (Figure 2b, line 103), substantially outperforming ICAE at 64× (~0.1 BLEU-4). This directly supports the paper's central claim of improved compression efficiency.

2. **Effective long-context retrieval at 1M tokens.** On the passkey retrieval task, RCC-Transformer-FT-32k achieves consistently near-100% accuracy across sequence lengths from 32K to 1M (Table 2, line 113). This demonstrates that the recurrent compression mechanism enables the model to handle sequences far beyond the encoder's 8K training window.

3. **Demonstrated memory savings.** RCC increases GPU memory by only ~0.5 GB when processing 16K tokens, whereas uncompressed Pythia-1.4b uses 2 GB more for just 2K tokens (Figure 1, line 161). The paper notes up to 32× storage savings for very long inputs — a concrete resource advantage.

4. **Instruction reconstruction alleviates context-instruction confusion.** RCC-Ins-Reconstruction achieves an average LongBench document QA score of 22.61, notably higher than RCC-Ins-Compress (19.61) and close to RCC-Ins-Human (23.15) (Table 3, lines 135–137). This validates that the proposed instruction reconstruction method meaningfully recovers performance when both context and instructions are compressed.

5. **Empirically validated architectural choices.** Using compressed vectors from all encoder layers yields BLEU-4 of 0.82 at 64× compression vs. 0.6 when using only the last layer (Figure 2a, line 101). The ablation demonstrates that the multi-layer design choice is justified.

---

## Weaknesses

### Major

1. **Insufficient baselines for long-context evaluation undermine the "competitive performance" claim.** On LongBench document QA, the only external baseline is Pythia-SFT, which has a 2K context window and cannot process samples beyond that length. For the 4–8K and 8K+ buckets, there are literally **no** non-RCC baselines — no position-interpolation-extended LLMs, no sliding-window attention models, no other compression methods (AutoCompressor, Selective Context, etc.). The paper asserts "competitive performance compared to non-compressed methods," yet a reader cannot assess whether RCC's scores on longer sequences (e.g., 17.72 on 8K+) are good, bad, or middling relative to any alternative that actually handles those lengths. This gap weakens the paper's central experimental narrative. *(Lines 133–143, 153–158)*

2. **Two-stage training validated only on a simple retrieval task.** The two-stage training strategy (freeze encoder, fine-tune decoder on longer sequences) is presented as a key contribution for resource-efficient long-context training, but it is validated only on the passkey retrieval task — a synthetic digit-location task that does not test complex reasoning over compressed representations. No ablation is provided for the LongBench setting: the paper does not compare two-stage training to any alternative (e.g., full-parameter training with gradient checkpointing at 16K, or a single-stage approach), nor does it analyze how much the frozen encoder degrades performance relative to an unfrozen counterpart. The claim that the method "further improved the efficiency of the model in handling long-text training" is plausible but lacks controlled evidence. *(Lines 69–70, 121–122, 150)*

### Minor

1. **Unexplained multi-value entries in the passkey table.** Table 2 reports three slash-separated numbers per cell (e.g., "98/100/97") without any specification of what these represent — whether they are three random seeds, three test sets, accuracy/recall/precision, or something else. The caption only says "performance... on the passkey retrieval tasks." This omission makes the central validation of the two-stage method harder to interpret than it should be. *(Lines 108–117)*

2. **Underspecified instruction reconstruction inference protocol.** The paper describes the *training* procedure for instruction reconstruction (decoder trained to output instruction first, then answer) but does not specify the *inference-time* decoding protocol. At test time, is the decoder given a fixed prompt prefix (e.g., "Reconstruct the instruction:") or trained to autonomously begin with the instruction? The exact prompt structure and decoding setup are not reported. Additionally, the paper does not quantify the success rate of instruction reconstruction itself (how often does the reconstructed instruction match the ground truth?), which would help explain the performance drop at longer lengths that the authors themselves attribute to reconstruction failures. *(Lines 71–72, 150, 154, 175)*

3. **Narrow evaluation of reconstruction quality.** Reconstruction performance is evaluated only with BLEU-4. No semantic/embedding-based metrics (e.g., BERTScore, NLI coherence) are reported, making it unclear whether the high BLEU scores reflect genuinely faithful semantic preservation or surface-level n-gram overlap. This is particularly relevant given that the reconstruction task uses prompts sampled from the same document as the reconstruction target, which may inflate BLEU scores. *(Lines 98–103)*

4. **Infini-Transformer comparison is the sole external passkey baseline.** The passkey retrieval comparison includes only Infini-Transformer as a non-RCC baseline. While the paper shows competitive or better results, the evaluation would benefit from additional comparisons to other long-context methods (e.g., position-interpolation-extended models) to contextualize the results more thoroughly.

### Trivial

None.

---

## Nice-to-Haves

- Add a comparison to at least one position-interpolation or sliding-window attention model on LongBench for sequences >2K, even if the comparison favors RCC only in memory usage.
- Provide an ablation in the LongBench setting comparing two-stage training (frozen encoder) to a single-stage full-parameter counterpart (possibly with gradient checkpointing to fit in memory).
- Report the instruction reconstruction success rate and its correlation with downstream QA score.
- Include semantic similarity metrics (e.g., BERTScore) for reconstruction quality.
- Provide explicit quantitative memory/FLOPs comparison at specific sequence lengths (2K, 8K, 16K, 32K) rather than only a qualitative figure.

---

## Removed Points

These points were raised by reviewers but are factually incorrect, reflect misreading of the paper, or are invalid on other grounds:

- **"Does not report reconstruction performance at 32×"** — REMOVED (factually wrong). The paper explicitly states: "At a 32× compression rate, the BLEU-4 score reached 0.95" (line 103).
- **"ICAE was not designed for such high compression, so the comparison is weak"** — REMOVED (invalid reasoning). The paper's claim is precisely that RCC achieves higher compression efficiency than existing methods. Comparing at a challenging rate where the baseline struggles is standard practice and strengthens the claim, not weakens it. The comparison is asymmetric in favor of the baseline's intended lower-rate regime, making RCC's outperformance more telling.
- **"The language overstates the case with 'competitive performance'"** — REMOVED. RCC-Ins-Reconstruction scores 28.12 vs. Pythia-SFT 30.54 on 0–2K (92% of the uncompressed baseline at 32× compression). "Competitive" is an accurate descriptor; this is not an overstatement.
- **"No comparison to single-stage full-parameter training on 16K"** — REMOVED (physically infeasible ask, acknowledged by the reviewer). The paper's motivation for two-stage training is that single-stage full-parameter training on long sequences is prohibitively memory-intensive. Asking for this comparison is asking for something outside the paper's technical motivation.
- Generic or unsubstantiated strengths from the Strength Finder — all listed strengths in my review are concretely cited and verified against the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method or results that is not already present in the paper.

---

## Suggestions

1. **Explain the three values in the passkey table.** Specify whether they represent separate runs, random seeds, test folds, or metrics. This is the single most actionable fix and requires no additional experiments.
2. **Add at least one long-context baseline to LongBench.** Position-interpolation-extended LLaMA, YaRN, or a sliding-window model would give readers a meaningful reference point for the 4K+ buckets.
3. **Specify the inference-time decoding protocol for instruction reconstruction** — what prompt, if any, is fed to the decoder at the start of generation.
4. **Consider a more challenging validation of two-stage training** — e.g., a long-document summarization task where reasoning beyond retrieval is required.
5. **Add a semantic evaluation metric (BERTScore) for reconstruction** to verify that BLEU-4 gains reflect genuine semantic preservation.

---

## Score and Decision

**Originality:** Moderate — combines autoencoding with recurrent segmentation and two-stage training in a practical way, but the individual components are not fundamentally new.
**Importance of research question:** High — efficient long-context inference is a critical problem.
**Claims support:** Moderate — the core claims about compression efficiency and passkey retrieval are well-supported, but the competitive performance claim on LongBench is under-supported by missing baselines.
**Soundness of experiments:** Adequate but with notable gaps (missing long-context baselines, unexplained table entries, narrow reconstruction metrics).
**Clarity of writing:** Generally clear but with important omissions (inference protocol, table explanation).
**Value to community:** Moderate — the method is practical and could be useful for resource-constrained long-context inference, but the evaluation gaps limit immediate confidence.

The paper has real contributions — high compression efficiency with strong reconstruction, effective 1M-token retrieval, and a workable instruction reconstruction method — but the evaluation has structural gaps that prevent full assessment. The missing long-context baselines on LongBench and the unexplained passkey table entries are the most serious issues. These are addressable in revision but non-trivial to fix in a rebuttal window. The paper is a credible *work-in-progress* that would be strengthened substantially by deeper evaluation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>