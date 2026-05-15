Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

The paper identifies a fundamental limitation of autoregressive LLMs for text embeddings: due to causal masking, token embeddings cannot encode information from later tokens. The authors propose "echo embeddings" — repeating the input twice and pooling from the second occurrence — enabling early tokens to attend to later tokens via the first occurrence. On MTEB, echo embeddings outperform classical embeddings by 9% zero-shot and 0.7% when fine-tuned, and achieve state-of-the-art among open-source models that do not use synthetic fine-tuning data.

## Strengths

- **Core idea is clean, well-motivated, and practically simple.** The paper identifies a genuine architectural limitation (causal masking preventing early-token embeddings from encoding future context) and proposes an elegant fix: repeat the input and extract from the second occurrence. The method requires no architectural changes and is compatible with any autoregressive LLM. (Sections 1, 3)

- **Synthetic experiment cleanly isolates the failure mode and confirms the mechanism.** The controlled experiment in Section 3.2 (Structures S1/S2) shows that classical embeddings fail when distinguishing information is in the latter part of sentences, while echo embeddings succeed. The bidirectional attention demonstration (Section 3.1) directly confirms that echo embeddings enable early tokens to encode later-token information. This controlled evidence is independent of any prompt-engineering concerns.

- **Large and consistent zero-shot gains across models and tasks.** Echo embeddings outperform classical by ~9% on average (Mistral-7B), with gains across every MTEB category and across model families (LLaMA-2 7B/13B, Mistral-7B). The consistency across architectures and scales strengthens the claim that the benefit is structural, not coincidental. (Section 5.1, Figure 2)

- **Properly controlled fine-tuning comparison.** Both classical and echo embeddings are fine-tuned on the same datasets with the same training pipeline, enabling an apples-to-apples comparison. Echo shows consistent (0.7% average) gains across all MTEB categories. (Section 5.2)

- **Achieves state-of-the-art with an open-source autoregressive model.** Echo embeddings with Mistral-7B match or exceed prior open-source MLM-based models on MTEB, demonstrating that the gap between autoregressive and bidirectional models for embeddings can be substantially closed. (Section 5.2)

- **Qualitative validation with concrete STS examples.** The paper provides specific sentence pairs from STSBenchmark where echo reduces error most, and these examples exhibit exactly the failure mode identified (superficially similar early tokens). (Section 5.1)

## Weaknesses

### Fatal
None.

### Major

1. **Zero-shot prompt templates are not disclosed, undermining reproducibility and isolating the repetition mechanism.** The paper reports 9% zero-shot gains but never specifies the prompt templates used for the classical baseline (or the last-token and summarization baselines). The echo prompt template is given ("Rewrite the sentence: x, rewritten sentence: x"), but readers cannot tell whether the classical baseline uses raw input, a different task instruction, or a controlled template. The paper mentions "prompt randomization" for all strategies, but without knowing the base templates, it is impossible to assess whether the 9% gain comes from the repetition mechanism, from the instruction framing, or from both. This is a significant reproducibility gap for the paper's headline quantitative claim. The authors should provide full prompt templates for every baseline and ideally include a control condition where classical uses the same instruction prompt without repetition (e.g., "Rewrite the sentence: x" → pool from the single occurrence). *(Section 4.1; echo prompt in Section 3)*

2. **Quantitative analysis of the failure mode on real data is claimed but not presented.** The paper asserts (Section 5.1) that "we quantitatively measure the degree to which classical and echo embeddings fail on sentences which are similar for early tokens... We find that classical embeddings systematically fail on examples which exhibit this structure, while echo embeddings do not." No table, figure, or numerical result accompanies this claim. This is a missing piece of evidence that would directly support the paper's central narrative — that the zero-shot MTEB gains are driven by overcoming causal masking. Without it, the link between the synthetic experiments and the real-world improvements remains circumstantial.

3. **Fine-tuning improvement (0.7%) is unexplained and the paper's primary mechanistic argument does not apply to it.** In the fine-tuning setup, both classical and echo use last-token pooling (the trainable end-of-sentence token), which can attend to all tokens. The causal-masking failure mode therefore should not apply. Yet echo still outperforms classical. The paper offers two untested hypotheses and leaves the question to future work. While the paper honestly acknowledges this gap, it weakens the overarching narrative that echo embeddings work by overcoming an architectural limitation — the fine-tuning gains persist even when that limitation is not present. A controlled ablation (e.g., classical with repeated input but pooled from the first occurrence) would help disentangle the source of benefit. *(Section 5.2, Section 7)*

### Minor

- **Last-token pooling brittleness demonstration on synthetic data is informative but the real-world evidence is thin.** Section 3.3 convincingly shows last-token embeddings fail on noisy synthetic data. However, the real-world validation is limited to a one-sentence claim that "last-token embeddings are substantially worse than mean token embeddings in the zero-shot setting" (Section 5.1). Given that the paper uses this brittleness argument to justify why last-token pooling does not resolve the failure mode, a more direct analysis on MTEB data would strengthen the case.

- **GPT-4 synthetic data generation is not analyzed for quality or potential bias.** The synthetic experiment (Section 3) relies on GPT-4 to generate sentence pairs with the required structure. No analysis of generation quality, failure rate, or potential confounds (e.g., GPT-4 may produce sentences where the distinction is trivially detectable via surface patterns) is provided. Given that this experiment is the primary controlled evidence for the mechanism, such analysis would improve confidence.

- **No error bars or statistical significance reported.** MTEB results (especially the 0.7% fine-tuning gain) are reported as single numbers without variance estimates. While single-run evaluation is common practice for large benchmarks, the modest fine-tuning gain would benefit from confidence intervals to assess reliability.

### Trivial
None worth enumerating — the paper is generally well-written.

## Nice-to-Haves
- Reporting zero-shot classical results with the same instruction prompt (without repetition) as a direct control for the prompt-engineering confound.
- A figure showing distribution of classical vs. echo errors on MTEB sentence pairs grouped by early-token similarity, to directly support the claimed mechanism with real data.
- Computational cost/latency analysis, since the method doubles tokens processed.

## Removed Points

These points were raised by reviewers but are removed per the guidelines; treat them with caution:

- **Criticism about missing reproducibility details being "fatal."** The reviewer's claim that the prompt confound "invalidates the paper's most impactful claim" is overstated. The prompt concern is real and significant (kept as Major weakness #1), but the paper has controlled evidence beyond zero-shot (synthetic experiments, properly controlled fine-tuning). Calling it fatal would be inaccurate.
- **Criticism questioning the existence or release status of models/datasets cited.** The hard rule requires removing any such concerns. The paper cites Wang et al. (2023) and the MTEB leaderboard; these exist as cited.
- **Complaints about missing appendix content.** The parser strips these sections from all papers; they exist in the original submission.
- **"Missing related work" points.** Per the hard rule, we cannot confirm the existence of missing references and must not raise this.
- **Strength Finder's claim about "methodological rigor in evaluation."** This conflicts with the verified weakness about undisclosed prompt templates; per the guidelines, when a strength and weakness disagree, the weakness wins. Dropped.
- **Nitpicks about formatting, typos, or presentation artifacts.** These are parser errors.

## Novel Insights

The most interesting insight to emerge from the reviews — beyond the paper's own contributions — is the unresolved tension between the paper's mechanistic claim (echo overcomes causal masking) and the fine-tuning results (echo helps even with last-token pooling, where causal masking is not a factor). This suggests that echo embeddings may have benefits beyond the stated mechanism — possibly providing better training signal via the dual occurrence, or offering a better initialization for the last-token pooling layer. The paper's two hypotheses (intermediate representation bottleneck and initialization quality) are reasonable but untested. A review-crossed analysis might reveal that the echo benefit is partly a *training dynamics* effect rather than purely a *representational* one — an interesting direction for future work that the authors could explore.

## Suggestions

1. **Disclose all zero-shot prompt templates** (for classical, echo, last-token, summarization baselines) in full. Add a controlled condition where the classical baseline uses the same instruction prompt as echo but without repetition — this directly isolates the repetition effect from the prompting effect.

2. **Present the quantitative failure-mode analysis on real data** that is currently claimed but absent. Show concretely (e.g., a figure or table) that echo embeddings disproportionately help on sentence pairs with superficially similar early tokens, measured across MTEB.

3. **Test the fine-tuning hypotheses** with a simple ablation: fine-tune classical embeddings with repeated input but pool from the first occurrence. If this closes the gap to echo, the benefit comes from repeated tokens rather than the echo extraction strategy, which would meaningfully change the interpretation.

## Score and Decision

The paper presents a genuinely simple and well-motivated idea with support from controlled synthetic experiments, consistent zero-shot gains, and a properly controlled fine-tuning comparison. The core contribution is real and potentially impactful. However, the headline zero-shot result suffers from a significant lack of transparency (prompt templates undisclosed) that prevents full assessment, and a claimed quantitative analysis that would bridge the synthetic and real-world evidence is missing. The fine-tuning gains, while credible, are modest and unexplained. These issues are addressable with a major revision but weaken the paper in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>