- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3
Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

The paper introduces SEEKER, a multimodal LLM that encodes text from document images as visual (image) tokens rather than OCR-extracted text, achieving a fixed 576 tokens per image regardless of text density. The goal is more compact representations that fit within context-length budgets. The method is evaluated on six self-created long-context multimodal tasks and compared against several proprietary and open-source MLLMs.

## Strengths

1. **Clear compactness advantage of image tokens.** Section 6.1 and Figure 4 show that representing document pages as images yields a fixed 576 tokens per page, whereas OCR-extracted text tokens vary widely and exceed an 8,192-token budget 33.75% of the time. This directly supports the paper's practical motivation.

2. **Competitive empirical results.** Table 2 reports that SEEKER achieves the highest average scores across all six long-context tasks among the evaluated models (GPT-4V, LLaVA-Next-13B, DeepSeek-VL, etc.). This demonstrates that the overall approach — combining visual-token encoding with instruction tuning on long-context data — yields a working system.

3. **Inference efficiency improvement.** Section 6.2 and Figure 5 show that SEEKER is approximately 3× faster than a pipeline that first runs OCR and then feeds extracted text into the same model. This is a practical advantage for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim not directly tested with a controlled ablation on SEEKER.** The paper's core thesis is that representing text as image tokens is more compact and enables better long-context handling than OCR text tokens. However, the evaluation never tests this within the same model architecture. Table 2 compares SEEKER (which inherently uses image tokens) against other MLLMs — different models with different training data, architectures, and capacity. The only comparison of image-token vs. text-token input (Figure 1) uses GPT-4V, not SEEKER. Without an ablation that feeds OCR-extracted text into the same SEEKER architecture and measures accuracy, we cannot determine whether the claimed advantages come from the tokenization strategy or from other design choices (rendered-text training data, image-separator tokens, LoRA fine-tuning, choice of DeepSeek-VL as base model). This is the single most important gap in the paper.

2. **Evaluation on small, self-created datasets with no error bars.** Each of the six long-context tasks contains only 80 samples (line 117). The paper makes strong claims — "outperforming all existing proprietary and open-source MLLMs by large margins" — on this basis. With n=80, a handful of examples can shift results by several percentage points. No confidence intervals, variance estimates, or statistical tests are reported. The datasets are not standard benchmarks (they are rendered Wikipedia text and constructed arxiv QA), making it difficult to compare against or reproduce the evaluation. Realistic long-context multimodal benchmarks (e.g., subsets of DocVQA, InfoVQA) are absent.

### Minor

3. **Missing ablations of key design choices.** Several components could explain SEEKER's performance: (a) the rendered-text Wikipedia training data, (b) the image-separator tokens (`<|startofimgi|>`, `<|endofimgi|>`), (c) the LoRA fine-tuning, (d) the choice of DeepSeek-VL as base. No ablation isolates which of these is responsible for the gains. The only ablation-like analysis is the token-count density plot (Figure 4) and the inference-time comparison (Figure 5), neither of which measures task accuracy.

4. **Novelty framing slightly overclaimed.** The paper states it is "the first to address this in the long-context MLLMs by employing a compact tokenization strategy that leverages visual tokens for textual information" (line 24). Prior work (Rust et al. 2023, Gao et al. 2024, cited by the paper itself) explores processing text within pixels. The contribution is better scoped as a specific instantiation for long-context *multi-image* MLLMs with instruction tuning, rather than as the first work to use pixel-level text encoding.

### Trivial
None.

## Nice-to-Haves

- A controlled study of task performance under varying token budgets (e.g., comparing image-token SEEKER vs. text-token SEEKER as context window shrinks from 8192 to 2048) would directly demonstrate the compactness-accuracy tradeoff.
- Analysis of failure cases or error types (e.g., character-level errors in dense text) would strengthen the evaluation.
- Standard, larger-scale long-context multimodal benchmarks would improve generalizability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Missing instruction dataset description (Section 3.2).** The reviewer notes Section 3.2 appears absent from the extracted text. Per the rules, this is a parser artifact — the section exists in the original submission. Removed.

2. **No comparison to Pix2Struct, Donut, or similar document MLLMs.** Per guidelines, missing related-work comparisons should not be mentioned as weaknesses, as the reviewer cannot verify appropriate coverage. Additionally, the paper already cites Rust et al. (2023) and Gao et al. (2024) as pixel-level processing work. Removed.

3. **"Tables referred to (Table 3, Table 4) are absent."** Parser artifact — tables in images may not survive text extraction. Removed per parser-artifact rule.

4. **Inference time comparison is "meaningless" / "trivial".** The comparison (SEEKER with vs. without an explicit OCR preprocessing step) is valid — it demonstrates a real practical speed advantage. The criticism is overstated. Removed.

5. **Criticism that Section 6.3 uses GPT-4V rather than SEEKER.** The section is transparently labeled as analyzing GPT-4V's tradeoff behavior; it does not claim to show SEEKER's behavior. Removed.

6. **"Qualitative examples are cherry-picked."** Generic criticism without specific evidence. Removed.

7. **Formating/style nitpicks and reproducibility concerns about trivial implementation details.** These do not constitute substantive weaknesses. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tension between a practically motivated approach and insufficiently rigorous evaluation of its core mechanism. The insight that emerges is that the paper's most compelling evidence (the compactness plot) is disconnected from its strongest claims (state-of-the-art accuracy), and bridging this gap with a within-model ablation would substantially strengthen the paper.

## Suggestions

1. **Run a controlled ablation:** Feed OCR-extracted text (from Nougat or similar) into the SEEKER architecture, and compare accuracy against the default image-token input on the same six tasks. This directly tests whether image tokens are the source of improvement.

2. **Increase evaluation规模和 statistical rigor:** Either expand to standard long-context benchmarks or report confidence intervals (e.g., bootstrap) for the current 80-sample tasks. Hedge the strong claims ("by large margins") given the small n.

3. **Add component ablations:** At minimum, ablate the rendered-text Wikipedia training data (train without it) and the image-separator tokens to show their individual contributions.

4. **Tone down the novelty claim** to accurately reflect prior pixel-level text processing work (Rust et al., Gao et al.) and position SEEKER's contribution as targeting the long-context multi-image setting specifically.
