- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

ClusComp introduces a compression paradigm that replaces weight quantization with clustering: it partitions weight matrices into groups, represents each group by an FP16 centroid from a learned codebook, stores integer assignments as codes, and optionally refines the codebooks via block-wise error minimization and recovery finetuning. The method naturally supports standard gradient-based finetuning (only the codebooks are updated, <1% of parameters). Experiments on Llama-1/2/3 (7B–70B) show competitive perplexity at 2–4 bits, meaningful 1‑bit results after recovery finetuning, and strong performance on multimodal LLaVA-Next-8B.

## Strengths

1. **Consistent perplexity improvements at low bit-widths.** Table 2 reports that ClusComp achieves the lowest perplexity in 9 of 12 comparisons at 4‑bit and maintains WikiText2 perplexity <13 at 2‑bit across all tested LLMs, where baselines like GPTQ and AWQ degrade far more severely. This is the strongest evidence for the method's core compression claim.

2. **First demonstration of viable 1‑bit compression on 70B-scale LLMs.** Section 4.2 shows that after recovery finetuning, ClusComp attains 51.4% average zero-shot accuracy on Llama-3-70B at ≈1‑bit (against 75.4% for FP16). While the gap is large, no prior method reports non-trivial accuracy at this bit-width for a 70B model.

3. **Well-motivated code-fixed design for block-wise training.** Section 3.2.3 justifies fixing the integer codes (trained only via K-means clustering) and training only the FP16 codebooks during block-wise error minimization. The paper explains (with empirical evidence via the histogram in Figure 3) that this avoids mode collapse and overfitting with as few as 128 calibration samples — a clean design choice.

4. **Strong multimodal compression results.** Table 3 shows that compressing the Llama-3-8B backbone of LLaVA-Next-8B with 2‑bit ClusComp retains 58.7 on MMBench and non-trivial scores on other vision-language tasks, while GPTQ and AWQ at the same nominal bit-width produce no correct outputs.

5. **Parameter-efficient finetuning.** The paper demonstrates that finetuning only the codebooks (<1% of total parameters, requiring only 42 GB for Llama-3-70B) is both parameter- and memory-efficient, and the method's FP16 codebooks support standard backpropagation without STE tricks.

## Weaknesses

### Fatal

None.

### Major

- **Overstatement of recovery finetuning results.** The introduction (line 13) describes the 2‑bit and 1‑bit accuracy after recovery finetuning as "approaches that of the FP16 model." However, the reported numbers — 57.8 vs 68.6 (11‑point gap) for 2‑bit Llama-3-8B and 51.4 vs 75.4 (24‑point gap) for 1‑bit Llama-3-70B — show substantial degradation, especially at 1‑bit. A 24‑point gap on a 70B model undermines the "approaches" characterization. Additionally, the abstract's claim that ClusComp "even rivals full finetuning of the FP16 model" refers to Section 4.3 (downstream finetuning), which is missing from the extracted text and cannot be verified. While the method's compression contributions are solid, the central narrative overstates performance relative to the numbers actually presented.

- **Recovery training data not specified.** Section 3.2.4 states that recovery finetuning involves "predicting the next token" but never specifies the dataset used (e.g., the original pretraining corpus, WikiText2 training set, or a separate corpus). This detail is essential for assessing both the method's data efficiency and the fairness of comparisons to one-shot quantization baselines. The calibration step uses 128 WikiText2 samples (line 145), but it is unclear whether the end-to-end recovery finetuning (ClusComp⁺) uses a much larger dataset.

### Minor

- **Exact average bits per configuration not reported in the main text.** The paper provides the average-bits formula (Equation 3) and a single worked example (g=4, n=2¹⁶−1 → ≈4.25 bits, line 101), but the exact g and n settings — and thus the exact average bits — for each model and bit-width used in Table 2 are delegated to the appendix (Table C.1, C.2). The formula is transparent, but a reader should not have to reconstruct bit budgets from appendix settings to verify the fairness of comparisons. Reporting exact average bits in the main table (or its caption) would resolve this.

- **ClusComp⁻ comparison framing.** The remark in line 103 states that ClusComp⁻ (pure clustering, no calibration data) "already surpasses RTN, GPTQ and AWQ." GPTQ and AWQ use calibration data, while ClusComp⁻ uses none — a comparison that actually favors the baselines (they have more information). The factual claim is correct, but the framing could mislead a casual reader into thinking ClusComp⁻ is strictly superior under equal conditions. The paper should explicitly note the difference in calibration data usage for each baseline.

### Trivial

None.

## Nice-to-Haves

- An ablation study isolating the contribution of each component: ClusComp⁻ (clustering only) → ClusComp (clustering + block-wise) → ClusComp⁺ (clustering + block-wise + recovery), all at the same bit budget, would strengthen the paper and clarify what each stage contributes.
- A sensitivity analysis of the hyperparameters (group size g and number of centroids n) on a smaller model (e.g., Llama-1-7B) would help practitioners understand the trade-off between compression rate, clustering quality, and codebook overhead.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the bit-width comparison is "misleading" and "unverifiable" (Critic Point 1).** The paper provides the exact formula for average bits and explicitly states that settings are in the appendix. The critic's speculation that "the actual average bits could be ~2.2" is not verified against the paper's actual g/n settings. The paper should report exact bits in the main table (kept as a minor weakness above), but calling this "fatal" or "misleading" overstates the issue.

- **Criticism that Section 4.3 (finetuning results) is absent.** Per instructions, the parser strips content from all papers; the missing section is assumed to exist in the original submission. The concern about unverifiable finetuning claims is merged into the Major weakness about overstatement, which covers what *can* be verified from the available text.

- **Criticism about "code availability" and "cannot be independently verified."** The paper's reproducibility statement promises code after decision. Per the hard rules, questioning release status or citing unverifiability of cited entities is removed.

- **Criticism about missing related work comparisons (AQLM, GPTVQ).** GPTVQ is already compared (Table 2 line: it appears as a baseline). AQLM is cited in related work. Per the hard rules, missing related works should not be mentioned.

- **Criticism about missing confidence intervals/variance.** Single-run evaluations are standard practice in the LLM compression literature; demanding statistical significance testing is scope creep.

- **Criticism that the kurtosis analysis is "not novel."** The observation serves as motivation for the method, not as a claimed contribution. The pilot study's value is in motivating the design choice (clustering over quantization), which is reasonable.

- **Criticism about the clustering step being "computationally expensive" and "not data-free."** The paper explicitly frames ClusComp⁻ as using "no calibration data" (line 103), which is factually correct — clustering uses the weight values, not input data. The computational cost (2GB memory, line 91) is reported and claimed to be modest.

- **Criticism that Table 2 only shows "competitive baselines" as a "red flag."** The paper states this is for compact representation and refers to full tables in the appendix — standard practice.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's ambitious framing ("rivals full finetuning") and the actual numbers reported (especially the 24‑point gap at 1‑bit), but this is a presentation issue rather than a novel analytical insight.

## Suggestions

1. Report exact average bits per parameter for every ClusComp configuration used in the main tables (Table 2, Table 3). This can be done in the table caption or a footnote.
2. Specify the dataset used for recovery finetuning (ClusComp⁺). A single sentence clarifying "we use the original pretraining corpus / WikiText2 training set / X" resolves the ambiguity.
3. Tone down the claim that recovery finetuning performance "approaches that of the FP16 model" at 1‑bit — a 24‑point gap on 70B is not well described by "approaches." Replace with a more precise characterization such as "substantially outperforms prior methods at 1‑bit, though a significant gap from FP16 remains."
4. Include an explicit ClusComp⁻ → ClusComp → ClusComp⁺ comparison at 2‑bit on at least one model (e.g., Llama-2-7B) to isolate the contribution of each stage.
