Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes a fine-tuning method for single-turn long-form text generation: LLMs are trained with auxiliary tasks that involve generating (or conditioning on) intermediate planning steps—document summary, outline, and key information—which are synthetically constructed from existing full articles using a stronger LLM (Gemini Ultra) and a scoring-based selection procedure. Experiments on SciNews and Wikipedia datasets show consistent ROUGE improvements and positive human side-by-side ratings against fine-tuning without intermediate steps, and the trend replicates on Gemini 1.5 Flash.

## Strengths

- **Single-turn integration of planning via auxiliary training tasks, not multi-step prompting.** The paper validates a clean approach: planning steps are used only during training, while at inference the model generates the full article in a single pass. Table 5 shows that single-turn inference (RLsum 46.61) outperforms a multi-turn variant of the same model (RLsum 43.73) on SciNews, supporting the claim that training with planning transfers to a simpler inference procedure.

- **Synthetic construction of intermediate steps overcomes data scarcity.** The pipeline (Algorithm 1) generates multiple candidate plans from full documents using an LLM, then selects the best via a scoring function combining length proportions and bidirectional entailment. This is a practical and scalable solution that does not require human annotation, and it is a clear methodological novelty.

- **Consistent improvements across datasets, metrics, and a second base model.** On SciNews, the best configuration achieves RLsum 46.61 vs. 44.14 for FT w/o I (+2.5 pts); on Wikipedia, RLsum 45.67 vs. 41.28 (+4.4 pts). Human SxS on SciNews shows a strong overall W/L of 3.60. The trend holds on Gemini 1.5 Flash (Table 6), demonstrating generalization beyond a single model generation.

- **Thorough ablation of training mixtures and inference modes.** Table 2 systematically compares different combinations of training tasks ($x_i \rightarrow y_i$, $x_i \rightarrow \bz_i \oplus y_i$, $x_i \oplus \bz_i \rightarrow y_i$) and inference modes, providing clear evidence for which configuration works best and why. This analysis gives the paper useful depth beyond a single headline result.

## Weaknesses

### Fatal
None.

### Major
None that undermine the core claim. The paper's central thesis—that training with synthetic intermediate planning steps improves single-turn long-form generation—is supported by consistent evidence across multiple dimensions.

### Minor

- **No variance reporting for ROUGE scores.** All ROUGE tables report point estimates without confidence intervals, standard deviations, or significance tests. The evaluation sets are modest (200 for SciNews, 98 for Wikipedia), and reported gains are in the range of 2–4 ROUGE points. While the improvements are directionally consistent, the reader cannot assess whether individual differences are statistically reliable. This is the single most important piece of missing rigor.

- **The intermediate step construction is under-specified for reproducibility.** The sinusoidal scoring function g(·) in Algorithm 1 is referred to as "derived from empirical observations" but never explicitly defined. The value of K (number of candidates) is not reported. No example of an actual generated intermediate step (summary, outline, or key information) is shown in the paper. The prompt formats used for the different training tasks are not provided. These omissions make it difficult for other researchers to replicate the method faithfully.

- **It is not explicitly stated which types of intermediate steps (summary, outline, key information) are used in the main experiments and how they are combined** (e.g., concatenated sequentially, or structured as a tree). Section 4.1 defines three types, and the conclusion mentions a "tree structure, where each level corresponds to an intermediate step" (line 422), but the experimental setup does not clarify whether all three are always present or how they are composed in the $\bz_i$ vector.

- **Weak baseline coverage.** The only meaningful baseline isolating the effect of the method is fine-tuning without intermediate steps (FT w/o I). While this is the correct comparison to test the core claim, the paper does not compare against alternatives such as zero-shot chain-of-thought prompting ("first write an outline, then write the article") or prompting with explicit section-heading templates. These would help disentangle whether the gains come from the training recipe specifically or simply from having access to structured planning information.

- **Human evaluation on Wikipedia shows marginal gains.** On Wikipedia, the overall human SxS W/L is 1.56, and Coherence & Organization is essentially at chance (1.10). The auto SxS gives only 1.20. The abstract's claim of "clear wins in organization, relevance, and verifiability" is strongly supported on SciNews but overstated for Wikipedia given these numbers. No inter-rater agreement metrics are reported.

- **An interesting negative result is not discussed.** In Table 2, training on Wikipedia with only $x_i \rightarrow \bz_i \oplus y_i$ and inferring with $x_i \rightarrow y_i$ degrades performance (R1 35.49 vs. 42.61 for vanilla SFT). This suggests that training exclusively on the plan-generation task hurts the model's ability to generate the article directly—a finding worth examining, as it informs the design of the training mixture.

- **The single-turn vs. multi-turn comparison (Table 5) is informative but limited.** Both inference modes use the same model trained on single-turn tasks. While this demonstrates that single-turn inference is more effective for this particular model, it does not compare against genuinely different multi-turn architectures (e.g., STORM-style iterative generation), which the paper itself acknowledges it scopes out. The comparison should be interpreted narrowly.

### Trivial

- The introduction claims the approach "fully leverage[s] the token-level attention mechanism to ensure coherence" — this is a motivational statement rather than an empirically supported claim, and could be softened.
- The paper does not report inference costs (increased output token count when intermediate steps are generated).

## Nice-to-Haves

- An ablation of plan quality: comparing synthetic steps (Gemini Ultra + scoring) against simpler alternatives (e.g., section headings extracted from the target article, plans from a weaker model, or randomized plans). This would directly test whether the *content* of the plan matters or whether any structured training signal suffices.
- A zero-shot chain-of-thought prompting baseline on the base model to separate the effect of training from the effect of inference-time planning.
- A small human evaluation of plan quality (do the generated summaries/outlines faithfully represent the article?).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The 1,900 Wikipedia training articles are a tiny fraction of KILT's 5.9M articles."** The paper describes filtering (removing articles under 1,000 words and those without structured sections) followed by random sampling. 1,900 examples is a reasonable amount for fine-tuning an LLM; the fraction of the full corpus is irrelevant once filtering criteria are applied. This criticism overstates a non-issue.
- **"The paper should compare against domain-specific planning methods like LLM+P, LLM-DP, CO-LLM."** These methods address plan generation for embodied/grounded tasks, not long-form text generation. The paper's related work already correctly scopes the comparison to text generation methods. This is a scope-mismatch criticism.
- **Various formatting/style nitpicks.** Not present in the paper; would be parser artifacts if they appeared.
- **Criticisms about missing appendix content.** The parser strips appendix sections; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations sharpen the paper's weaknesses (lack of statistical rigor, under-specification of the scoring function, marginal Wikipedia gains) but do not introduce new analytical perspectives beyond what the paper already discusses.

## Suggestions

1. **Add confidence intervals or bootstrap resampling** to all ROUGE tables. Even a simple paired bootstrap on the evaluation samples would substantially increase confidence in the reported gains.
2. **Specify the missing details** for reproducibility: define g(·) explicitly, report the value of K, include an example of a generated intermediate step, state which types of steps are used and how they are combined, and show the prompt formats for each training task.
3. **Discuss the Wikipedia degradation case** (training with only $x_i \rightarrow \bz_i \oplus y_i$, inferring with $x_i \rightarrow y_i$ gives R1 35.49 vs. 42.61). This informs the important design principle that the plan-generation task alone is insufficient and must be mixed with the direct generation task.
4. **Ablate plan quality** in a follow-up: even a single comparison against a trivial plan (e.g., section headings) would substantially strengthen the claim that the content of the synthetic plan matters.
5. **Soften the abstract's wording** regarding Wikipedia results, or add a caveat that the improvements on Wikipedia are more modest than on SciNews.

## Score and Decision

This paper makes a clearly motivated and practically useful contribution: a training recipe that injects planning capabilities into an LLM through synthetic intermediate steps, with consistent empirical support across two domains and two model generations. The weaknesses are real but addressable—they concern presentation rigor and depth of analysis rather than fundamental validity of the approach. The central claim is supported by the evidence; the paper would benefit from stronger statistical grounding and fuller disclosure of method details but does not need a structural overhaul.

Score: 6.0

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>