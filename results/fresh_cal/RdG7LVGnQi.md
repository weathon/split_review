Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes LLM-QFA, a once-for-all (OFA) quantization-aware training framework for LLMs that enables a single training run to produce deployable subnets across multiple bit-width constraints. The key technical contributions are: (1) decoupling shared weights across quantization configurations via per-configuration LoRA adapters to avoid interference, and (2) a non-parametric scheduler that balances training resources across subnets with different average bit-widths. Experiments on LLaMA2-7B and LLaMA2-13B show that LLM-QFA matches or slightly exceeds baselines (GPTQ, QA-LoRA) across bit-widths while requiring constant training time regardless of the number of deployment scenarios.

## Strengths

- **First OFA framework for quantized LLMs with sound architectural mitigation of interference**: The paper identifies that weight-sharing in traditional OFA causes interference across quantization configurations (different bit-widths have different noise magnitudes). The solution — freezing quantized weights and maintaining separate LoRA adapters per bit-width (Eq. 3) — is clean and validated by the ablation in Figure 6, where the shared-LoRA variant degrades across all bit-widths.

- **Non-parametric scheduler addresses a genuine, formally characterized imbalance**: The paper analytically shows (Eq. 4) that uniform sampling of configurations concentrates subnets near the mean bit-width, starving extreme subnets. The proposed scheduler (Eq. 5) dynamically shifts the sampling distribution to approximate uniform coverage. The ablation (Figure 6, uniform vs. proposed) confirms the scheduler helps even in the median region.

- **Constant training cost w.r.t. number of deployment scenarios**: Figure 2 empirically demonstrates that QA-LoRA's cost grows linearly with N, while LLM-QFA's is flat. This is the paper's central value proposition and is cleanly supported.

- **Additional analysis separates the OFA benefit from mixed-precision benefit**: Figure 5 compares LLM-QFA subnets against mixed-precision subnets constructed from individually trained QA-LoRA models at (2,3,4) bits. The LLM-QFA subnets show higher and more stable accuracy, confirming the supernet optimization itself contributes beyond mixed-precision capability.

## Weaknesses

### Major

- **Search on MMLU evaluation data conflates selection and reporting**: The paper states (line 163): "For the MMLU Benchmark, we search the optimal subnets on the MMLU evaluation dataset." The methodology section (line 146) describes using a *validation set* for search, but for MMLU no held-out test split is mentioned — the same "evaluation dataset" is used for both subnet selection and final accuracy reporting. This violates standard evaluation protocol and makes the MMLU results potentially optimistically biased. (Note: the Common Sense QA setup is cleaner — search on ARC-C, test on separate datasets — but the MMLU numbers are the headline results.)

### Minor

- **Primary comparison conflates OFA training with mixed-precision capability**: Tables 1–2 compare uniform-precision baselines (GPTQ, QA-LoRA at exactly 2/3/4 bits) against mixed-precision subnets from LLM-QFA meeting the same average-bit-width constraints. This combines two factors: the OFA training scheme and the flexibility of mixed-precision. The paper does include a separate analysis (Figure 5) that isolates the OFA benefit, but this is not in the primary tables, so readers could over-attribute gains to the OFA training alone.

- **MMLU average computation is not transparent**: The reported "Avg." values in Table 1 are clearly not simple averages of the four category scores shown (e.g., for GPTQ 4-bit on LLaMA2-13B, 61.3+43.3+62.5+57.2 averages to 56.1 but the reported value is 54.9; the direction of discrepancy varies across rows). These are presumably standard MMLU macro-averages across all 57 subjects, but the paper does not state this, making it impossible for readers to verify the arithmetic.

### Trivial

- "We apply quantize" → grammar issue (line 78).

## Nice-to-Haves

- A brief analysis of how many MMLU subjects the 150 searched subnets actually "see" during search would clarify the risk of overfitting on MMLU.
- Reporting results for the uniform-precision variant of LLM-QFA (forcing each subnet to use uniform bit-width) in the main tables would cleanly separate the OFA training benefit from mixed-precision.
- The schedule epoch length (8k steps) seems somewhat arbitrary; a more systematic sensitivity analysis would be helpful.

## Removed Points

- **Arithmetic inconsistency claim (harsh critic)**: The critic claims QA-LoRA 3-bit on LLaMA2-13B (5-shot) should be 52.8 not 51.7 based on summing the four category scores. However, MMLU overall accuracy is the average across all 57 subjects — not a simple average of four category-level macro-averages. Every row in Table 1 exhibits this discrepancy (e.g., GPTQ 4-bit 13B: 61.3+43.3+62.5+57.2 → simple avg 56.1 vs. reported 54.9), confirming the averages are computed via standard MMLU methodology. The criticism is factually wrong.

- **Claim that the paper misses mixed-precision vs. uniform-precision disentanglement**: The critic asserts this is missing from the paper, but Section 4 ("Impact of Mixed Precision and Quality of Optimization") and Figure 5 directly address it with mixed-precision QA-LoRA constructed from individually trained models. The criticism ignores existing content.

- **Speculative fatal flaw about evaluation validity**: The critic's framing implies the evaluation is "impossible to interpret," but the CSQA setup (search on ARC-C, test on others) is methodologically sound, and the MMLU concern, while valid, is a specific and bounded issue rather than a wholesale invalidation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors missed.

## Suggestions

1. **Clarify the MMLU evaluation protocol**: Explicitly state whether MMLU test data was used for subnet selection and, if so, either (a) hold out a portion of MMLU subjects for final reporting, or (b) justify why the risk of overfitting from ~150 subnet evaluations on a 14k-example benchmark is negligible. At minimum, acknowledge this limitation.
2. **State the MMLU averaging methodology**: Add a footnote explaining that the reported "Avg." is the macro-average across all 57 MMLU subjects (not the average of the four category columns), so readers can verify the numbers.
3. **Add uniform-precision LLM-QFA results to a main table**: This would make the disentanglement of OFA-training vs. mixed-precision benefits immediately visible to readers, preempting the concern entirely.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>