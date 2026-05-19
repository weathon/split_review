- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes LoQA, a method that integrates LoRA with weight quantization for LLMs by using two separate LoRA modules to fine-tune both the scale and zero-point parameters of a uniformly quantized model, enabling a merged quantized representation after training. A bit-aware scaling factor (QBAS, defined as $s = \alpha/(r \cdot 2^{N-1})$) is introduced to normalize LoRA updates across different bit-widths. The method is evaluated on MMLU and commonsense reasoning tasks across LLaMA-7B/13B/30B, showing gains over QA-LoRA and competitiveness with higher-precision mixed-precision approaches.

## Strengths

- **HQ-LoRA enables joint learning of scale and zero-point in a format-preserving way.** Section 3.2 introduces a forward pass (Equation 6) that decouples updates to scale ($\mathbf{S}$) and zero-point ($\mathbf{Z}$) via two separate low-rank terms ($\mathbf{BA}$ and $\mathbf{B'A'}$), and Equations 8–9 show they can be merged back after fine-tuning without breaking the quantized format. This is a clear advance over QA-LoRA, which only learns zero-points.

- **Consistent gains across model sizes, datasets, and bit-widths.** Tables 1 and 3 show LoQA outperforms QA-LoRA across LLaMA-7B/13B/30B on both Flan v2 and Alpaca (e.g., LLaMA-7B/Flan v2: 47.4% vs 45.2%; LLaMA-30B/Alpaca: 54.6% vs 53.7%). Table 2 shows 2-bit LoQA surpasses the 2+16-bit state-of-the-art IR-QLoRA by 4.7% (31.5% vs 26.8%).

- **Better parameter efficiency than QA-LoRA.** Table 7 compares LoQA (rank=16) vs QA-LoRA (rank=32) — LoQA uses half the parameters yet achieves 47.1% vs 45.2% on LLaMA-7B/Flan v2, demonstrating that HQ-LoRA's structure, not just parameter count, drives improvement.

- **Ablation study confirms individual contributions of HQ-LoRA and QBAS.** Table 6 shows that adding HQ-LoRA alone improves 4-bit accuracy from 45.2% to 46.3%, and QBAS alone yields gains of +0.9%, +1.2%, and +1.3% for 4-bit, 3-bit, and 2-bit respectively, with the combination achieving the best results.

## Weaknesses

### Fatal
None.

### Major

- **Reproduced QA-LoRA baseline may differ from the original paper's reported numbers, with no explanation provided.** The paper states baselines were "reproduced under the same environment" (Section 4.1), but the reviewer flags discrepancies between these reproduced numbers and those in the original QA-LoRA paper (e.g., LLaMA-7B 4-bit Flan v2: 45.2% reported here vs 46.1% in QA-LoRA Table 2). If true, this would inflate the apparent gains. The paper does not discuss or acknowledge this gap, nor does it report the original QA-LoRA numbers alongside its reproduction for transparency. This undermines confidence in the claimed improvements over the key baseline. *(Note: This criticism depends on external numbers from the QA-LoRA paper that cannot be independently verified here, but the paper would benefit from addressing this proactively.)*

### Minor

- **Ultra-low-bit claims (2-bit) are not fully contextualized.** The paper reports that 2-bit LoQA "surpasses the original 16-bit model by 3.8%" (Section 4.1, Text after Table 2). However, the "original 16-bit model" is presumably not fine-tuned, so this comparison conflates the benefit of fine-tuning with the benefit of the quantized representation. A more informative comparison would be against a fine-tuned full-precision model. The primary comparison against 2+16-bit IR-QLoRA (+4.7%) is valid and interesting, but the claim about beating the 16-bit model needs qualification.

- **No statistical significance or variance reporting.** All main results (Tables 1–3, 5, 8) report single-run accuracy without confidence intervals, standard deviations, or multiple seeds. While single-run MMLU evaluation is the norm in the quantization+PEFT literature, the 1–2% gains over QA-LoRA could plausibly originate from random variation. At minimum, the paper should acknowledge this and ideally provide multiple-run statistics for the core comparisons.

- **QBAS contribution lacks sensitivity analysis.** The critic's claim that QBAS "can be absorbed into α" is partially incorrect — the paper's Section 3.3 correctly notes that QBAS specifically normalizes the *asymmetric* effect where $\mathbf{W}^{\text{Int}}$ modulates the scale-related LoRA update ($\mathbf{B'A'}$) but not the zero-point update ($\mathbf{BA}$), which simple α-tuning cannot replicate. However, the paper does not provide a sweep over α with and without QBAS, nor does it show gradient magnitude dynamics across bit-widths to demonstrate the claimed stabilization effect. The ablation (Table 6) shows QBAS helps, but the mechanism could be more rigorously validated.

- **Evaluation scope is reasonable but incomplete.** The paper focuses on MMLU and commonsense reasoning, which are standard for downstream task evaluation. However, for a quantization paper, the absence of perplexity measurements on a language modeling benchmark (e.g., WikiText-2) and the absence of any inference throughput or latency measurements is a gap. The paper claims compatibility with acceleration toolboxes (MLC-LLM, AWQ, BitBLAS, Marlin) in Section 4.3 but provides no empirical demonstration. Adding even a single table showing tokens/sec or peak memory would significantly strengthen the paper.

- **LLaMA3 finding is reported but not investigated.** The paper notes (Section 4.1) that LoQA achieves lower loss on LLaMA3 but not better MMLU, attributing this to dataset insufficiency and citing prior work. This is an interesting negative result that the paper mentions only briefly; a systematic investigation (e.g., analysis of overfitting, comparison of training dynamics) would turn this into a strength rather than an unresolved observation.

### Trivial
None — the paper is reasonably well-written and the technical content is clear.

## Nice-to-Haves

- **Perplexity evaluation on a standard LM benchmark** (WikiText-2, C4) would align with conventions in the quantization literature and help demonstrate that the method does not degrade generation quality.
- **Inference speed/memory benchmark** even for a single model size (7B) would substantiate the claimed deployment compatibility.
- **A sensitivity analysis of α with and without QBAS** across bit-widths, showing gradient dynamics or effective update norms, would clarify QBAS's role.
- **Analysis of why HQ-LoRA uses parameters more efficiently** than QA-LoRA (hinted at by Table 7) — e.g., effective rank of learned updates, gradient norm analysis — could be a genuinely insightful finding if unpacked.

## Removed Points

These points were removed or demoted from the harsh critic's review for the reasons stated:

1. **"Grouping operator description is vague"** — The paper states "one-dimensional average pooling with the corresponding group size to x" (p. 5, text after Equation 6). This level of description is standard for this field and sufficient for reproducibility given the group-quantization context.

2. **"Tables are poorly formatted with missing/garbled numbers"** — The tables appear as embedded images in the PDF; the garbled text is a parser artifact, not a paper issue.

3. **"QBAS can be absorbed into α"** — This is factually incorrect given the paper's argument. QBAS specifically normalizes the asymmetric modulation effect where $\mathbf{W}^{\text{Int}}$ scales the $\mathbf{B'A'}$ update but not the $\mathbf{BA}$ update (Section 3.3). Simply tuning α would affect both branches equally and cannot replicate this normalization. The criticism about insufficient ablation is valid (moved to Minor), but the absorption claim is removed.

4. **"Comparison with QLoRA training time cited without direct measurement"** — The paper shows its own 1.3× overhead over QA-LoRA and references the QA-LoRA paper's 2× figure for QLoRA. This is standard practice for contextualization.

5. **"Strengthening the Paper on Its Own Terms: focus comparison on format-preserving baselines"** — This is a suggestion for restructuring, not a weakness. The paper already makes this distinction clear in Related Work and the reader can evaluate accordingly.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an analysis angle the paper itself missed. The observation about parameter efficiency (HQ-LoRA achieving better results with half the parameters of QA-LoRA, Table 7) is noted by the paper and is its strongest finding, but neither reviewer unpacks *why* this occurs.

## Suggestions

1. **Address the baseline reproduction concern**: Report both the original QA-LoRA paper's published numbers and your reproduced numbers in the same table, with a brief discussion of any differences (e.g., data processing, random seeds, evaluation pipeline). This will preempt the concern.

2. **Add multiple-seed results**: Run the core comparison (LLaMA-7B 4-bit, Flan v2) for 3 seeds and report mean ± std. If resources permit, extend to the 13B and 30B comparisons.

3. **Strengthen QBAS validation**: Add a figure showing gradient magnitudes of the scale-LoRA vs zero-point-LoRA updates with and without QBAS, or a sweep over α with both QBAS on/off.

4. **Add perplexity**: Evaluate on WikiText-2 or C4 for one configuration to demonstrate language modeling quality is preserved.

5. **Clarify the 2-bit vs 16-bit comparison**: Explicitly state that the 16-bit baseline is not fine-tuned, and add a comparison against a fine-tuned 16-bit model or at least acknowledge the confound.

**Score and Decision**
