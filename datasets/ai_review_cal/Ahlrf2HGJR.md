- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper identifies a fundamental failure mode of autoregressive language models used for text embeddings: due to causal attention, early-token embeddings cannot encode information from later tokens. The authors propose "echo embeddings"—a simple method that repeats the input twice in context and pools embeddings from the second occurrence—allowing early tokens to attend to later information via the first occurrence. The paper evaluates this approach on MTEB, showing zero-shot gains over 9% and finetuned gains of ~0.7%, and demonstrates the mechanism through controlled synthetic experiments.

## Strengths

- **Well-motivated and precisely identified failure mode.** The paper pinpoints a concrete architectural limitation of autoregressive models for embeddings (causal masking prevents early tokens from encoding later information) and demonstrates it with a clean synthetic setup (Section 3.3, Figure 3) where classical mean-token embeddings cannot distinguish sentences differing only in later tokens, while echo embeddings can.

- **Simple, effective method with direct causal evidence.** Echo embeddings (Section 3.1) are described clearly, and the paper provides direct evidence that the mechanism works: in a controlled synthetic setting where only early-token embeddings are pooled, echo embeddings from Mistral-7B assign higher similarity to semantically matching later content than to dissimilar later content (Section 3.2, Figure 2), confirming that repetition actually recovers bidirectional information.

- **Large and consistent zero-shot gains across architectures and scales.** Echo embeddings outperform classical embeddings by over 9% on average in zero-shot evaluation (Table 1 / Figure 8, Section 5.1), with gains holding across Mistral-7B, LLaMA-2-7B, and LLaMA-2-13B, and across all MTEB task categories. This is a substantial empirical win for a zero-shot method with essentially no training cost.

- **State-of-the-art open-source results without synthetic data after fine-tuning.** When finetuned on identical data, echo embeddings improve over classical by ~0.7% on MTEB (Table 2 / Figure 9, Section 5.2). Mistral-7B with echo embeddings surpasses prior open-source models that use bidirectional masked language models (MLMs), demonstrating that autoregressive models with this simple modification can match or exceed MLM-based approaches—a result that was not previously achieved.

- **Thorough ablations rule out trivial alternatives.** The paper systematically compares against last-token pooling (shown to be brittle in Section 3.3), summarization-based embeddings (Section 5.1), and bidirectional-attention fine-tuning (Section 5.2). Even removing the causal mask during fine-tuning does not match echo performance, ruling out the possibility that the gain simply comes from enabling bidirectional context.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot evaluation is conducted on an unspecified subset of MTEB.** Section 4 (line 160) states: "In the zero-shot setting, for convenience, we only evaluate on a subset of MTEB." No details are given about which tasks or datasets constitute this subset, how large it is, or whether it balances across the seven MTEB categories. The paper's headline quantitative claim ("over 9% improvement zero-shot") rests entirely on this subset, and the claim of "consistent gains across every MTEB category" cannot be verified from an unspecified subset without knowing which categories were included. While the finetuning results on the full MTEB partially corroborate the trend, this remains a significant evidential gap for the paper's strongest result.

- **Finetuning improvement lacks statistical characterization.** The paper reports that echo embeddings outperform classical by 0.7% on average after finetuning and states gains are "consistent across each category" (Section 5.2), but provides no confidence intervals, standard errors, or per-task breakdowns in the text. At margins below 1%, sampling variability, random seeds, or minor hyperparameter choices could plausibly flip the direction of results on individual tasks. Without measures of uncertainty or per-task detail, the reliability of this finding is difficult to assess.

### Minor

- **"Quantitative" failure mode analysis on real data is not actually quantified.** Section 5.1 (lines 198-199) contains a paragraph titled "Quantitative evaluation of the failure mode" that claims "We quantitatively measure the degree to which classical and echo embeddings fail on sentences which are similar for early tokens" but then provides only the qualitative statement "We find that classical embeddings systematically fail on examples which exhibit this structure, while echo embeddings do not." No numerical breakdown, correlation statistic, or error analysis is given. This is a missing piece of evidence that would have cleanly connected the synthetic analysis to real-world performance.

- **Prompt randomization details are underspecified.** The paper mentions sampling prompts with randomized wording, punctuation, and capitalization (Section 4.1) but does not report how many prompt variants were sampled, how variance across prompts was handled, or whether the echo template itself was included in the randomization. This affects exact reproducibility of the zero-shot results.

- **Bidirectional attention ablation is described too briefly.** The ablation removing the causal mask during fine-tuning (Section 5.2) yields a noteworthy result—bidirectional attention underperforms echo embeddings—but is described in only two sentences. Details about whether the same training data, hyperparameters, and pooling strategy were used are implied ("same setup") but not explicitly stated, and the architecture modification needed to use pretrained weights with bidirectional attention is not explained.

### Trivial
None.

## Nice-to-Haves

- Extend the zero-shot evaluation to the full English MTEB set (or explicitly specify and justify the subset) to remove the main evidential gap.
- Provide per-task finetuning results with error bars (multiple seeds or standard deviations) so readers can assess whether the 0.7% average improvement is a uniform shift or driven by large wins on specific tasks.
- Include a direct, quantitative test of the failure mode on real MTEB data—e.g., for each task, compute the correlation between early-token overlap of sentence pairs and the error difference between classical and echo embeddings.
- Include a brief computational cost analysis: doubled inference is acknowledged, but a discussion of whether improved retrieval quality offsets this cost (e.g., through smaller candidate sets) would contextualize the trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Instruction-tuned variant only may not generalize to base model"** (Harsh Critic): The paper evaluates consistently across all strategies using the instruction-tuned variant, which is standard practice. This is a reasonable methodological choice, not a weakness. **Removed as scope creep.**

- **"Noise distribution in last-token pooling experiment is artificial"** (Harsh Critic): The paper explicitly acknowledges this ("While this particular distribution of noise is artificial...") and then validates the finding on real MTEB data in Section 5.1. The criticism is already addressed by the paper. **Removed as strawman (paper already addressed).**

- **"Summarization comparison 'more robust' claim lacks evidence"** (Harsh Critic): The paper says "We suspect that echo embeddings are more robust" (Section 5.1)—this is a speculation, not an asserted claim. The critic's framing overstates the paper's commitment. **Removed as misunderstanding of hedging language.**

- **Pure formatting and presentation nitpicks** (various): Any criticism about typos, spacing, figure placement, or other parser artifacts. **Removed per hard rule on formatting.**

- **Strength Finder claim about "quantitative" failure mode analysis**: The strength finder claimed the paper "quantifies that classical embeddings systematically fail more on such examples," but the paper does not actually provide numbers. This strength conflicts with verified weaknesses and is removed. **Removed as factually inaccurate (no numbers given).**

## Novel Insights

The harsh critic correctly notes that the zero-shot subset issue is the paper's primary evidential gap, while the strength finder correctly identifies the synthetic experiments as strong mechanistic evidence. The key tension in the reviews is between appreciation for the method's conceptual clarity (both reviewers agree it is simple, well-motivated, and sound) and concern that the most impressive quantitative result (the 9% zero-shot gain) rests on an underspecified evaluation. Neither reviewer identifies a flaw in the core mechanism itself—the criticism is about the completeness of the evidence, not its direction. The insight that emerges from reading both reviews together is that the paper would be substantially strengthened by reporting the missing evaluation details (full zero-shot MTEB, per-task finetuning numbers) rather than by adding new experiments, since the existing synthetic and ablation evidence already convincingly supports the mechanism.

## Suggestions

1. **Report the composition of the zero-shot subset** and, ideally, extend evaluation to the full English MTEB zero-shot set. This is the single most impactful revision for credibility.
2. **Provide per-task finetuning results** with multiple seeds or statistical uncertainty measures to support the "consistent gains" claim.
3. **Add actual numbers to the "quantitative evaluation of the failure mode"** paragraph in Section 5.1—e.g., the mean/median error for classical vs. echo embeddings on early-token-similar vs. early-token-dissimilar pairs.
4. **Expand the bidirectional attention ablation** with explicit training details to strengthen this control experiment.
5. **Specify the number of prompt templates sampled** and how variance across templates was handled.
