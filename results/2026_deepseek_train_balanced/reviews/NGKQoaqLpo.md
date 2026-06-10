## Summary

This paper studies how learning a single new text via gradient updates can cause an LLM to "prime" (hallucinate) the text's keyword in unrelated thematic contexts. The central empirical finding is that the keyword's token probability *before* learning predicts the degree of priming *after* learning — a relationship validated across PALM-2-xs/s, Gemma-2b, and Llama-2-7b, across model sizes, training stages, spacing conditions, and interference from multiple texts. The paper introduces the Outlandish dataset (1320 samples, 12 keywords, 4 themes, 11 textual categories) to enable this study, and proposes two mitigation strategies: "ignore-topk" gradient pruning and "stepping-stone" text augmentation. The core finding is interesting, the cross-model validation is a genuine strength, and the mitigation techniques are novel and counterintuitive.

## Strengths

- **Robust cross-model, cross-condition validation of the probability–priming relationship.** The paper demonstrates that keyword probability pre-learning correlates with priming post-learning across PALM-2-xs/s, Gemma-2b, and Llama-2-7b (Figs. 2, 13–15), across model sizes (Fig. 16), across training stages (pretrained vs. FLAN, Fig. 15), under spaced training (Fig. 3a), with as few as 3 presentations (Fig. 3b), and under simultaneous learning of two interfering texts (Fig. 17). This breadth of validation is unusual and substantially strengthens the claim.

- **The "ignore-topk" gradient pruning strategy is genuinely novel and surprising.** Conventionally, gradient sparsification keeps the top-k% of updates. This paper discovers that *ignoring* the top 8% and keeping the rest reduces priming by 50–95% across models while preserving memorization and generic Wikipedia next-word prediction (Section 5.1, Fig. 5, Figs. 23, 25). The connection to differential privacy clipping (Andrew et al., 2019) provides a principled anchor for future mechanistic work.

- **The stepping-stone intervention provides converging evidence beyond pure correlation.** Rather than only reporting a correlation, the paper manipulates keyword probability through text augmentation (increasing probability by adding intermediate explanatory clauses) and shows that priming attenuates accordingly (a median 50–75% reduction across models, Fig. 6, Figs. 26–27). The comparison against simple rewrites and adding logical consequences (Fig. 28) strengthens the specificity of this result.

- **In-context vs. in-weights comparison reveals a meaningful dissociation.** Section 4.3 shows that in-context learning of the same texts produces a much attenuated probability–priming relationship compared to in-weight learning (Fig. 22), providing an interesting empirical distinction between implicit and explicit optimizers that prior work had not directly compared.

## Weaknesses

### Major

- **The priming metric ($S_{\text{prime}}$) has a denominator stability concern that is not analyzed or discussed.** The metric is defined as $\mathbb{E}[P_{\text{after}}(x_{\text{key}}|X_{T,j}) / P_{\text{before}}(x_{\text{key}}|X_{T,j})]$. For rare keywords (e.g., "mauve", "haggis") evaluated on thematic prefixes about colors/foods, $P_{\text{before}}$ can be extremely small, making the ratio numerically fragile. A tiny absolute increase (e.g., $10^{-12} \to 10^{-9}$) produces a large ratio that may be dominated by noise rather than meaningful signal. The paper uses log-transformed priming scores ($\log S_{\text{prime}}$) and Spearman correlations, which partially mitigate this, but there is no analysis of floor effects, numerical precision, or whether the observed correlation is driven by samples where the denominator is near the noise floor. Since the entire main finding rests on this metric, this gap needs to be addressed — at minimum with a diagnostic showing that the relationship is not an artifact of denominator instability.

- **The limitations section is functionally absent.** Section 6 reads in its entirety: "Limitations of this study include the growing size of the dataset, and the puzzling mechanism behind both priming and Ignore-topk mitigation." This omits discussion of: (a) the narrow lexical scope (12 keywords, 4 themes), (b) the single-sample insertion paradigm versus realistic multi-example training, (c) whether priming as measured here corresponds to practically significant hallucination, (d) the limited generic evaluation of ignore-topk (Wikipedia next-word prediction only), and (e) the lack of a mechanistic account for the main finding. A paper that makes broad claims should acknowledge its boundaries.

### Minor

- **The stepping-stone intervention is presented with somewhat overstated causal language.** The paper claims "direct evidence" (Discussion) and "strongly tested the hypothesis that keyword probability before learning causes priming after learning" (Contributions). However, the stepping-stone elaboration changes text length, syntactic structure, the distribution of gradient updates, and overall loss landscape — not just keyword probability. The paper does compare against simple rewrites and logical-consequence baselines (Fig. 28), which is helpful, but the causal claim would be more convincing if the paper also attempted the reverse manipulation (decreasing probability through a minimal perturbation to see if priming *increases*), or acknowledged the confounds more explicitly. The evidence is suggestive and convergent, not "direct" in a strict causal sense.

- **The practical significance of the core finding is asserted rather than demonstrated.** The abstract states "it is through these accumulated changes that the LLM was initially pre-trained," framing priming as fundamental to pre-training dynamics. But the experimental setup — inserting a single text 20–40 times into a fully trained model — is far from the simultaneous billion-exposure regime of pre-training. The interference experiment uses only two simultaneous texts (Fig. 17). The connection to real training dynamics is conjectural, and the paper would benefit from situating its contribution more modestly within knowledge-editing/continual-learning paradigms rather than pre-training.

- **The generic evaluation for ignore-topk is too narrow.** The claim that language performance "was not degraded" (Fig. 5c) is supported only by Wikipedia next-word prediction. Standard benchmarks (MMLU, HellaSwag, ARC, etc.) would be needed to substantiate this claim, especially given that the procedure removes the top 8% of parameter updates.

- **The $10^{-3}$ threshold for keyword probability is presented without statistical justification.** The paper observes a separation at this value (Fig. 2b) but provides no formal test, confidence interval, or analysis of how sharp or stable this threshold is across conditions.

### Trivial

- The limitations sentence includes "growing size of the dataset" — but the dataset has a fixed 1320 samples; this phrasing appears garbled (likely a parser artifact). (No action needed in light of the parser note.)

- Several sentences are incomplete or broken (e.g., line 157 starts with "5)"), which are parser artifacts from PDF extraction.

## Nice-to-Haves

- An analysis of *which* parameters/ layers are differentially affected by ignore-topk pruning would greatly deepen the contribution. The paper acknowledges the mechanism is puzzling, but even a speculative account (connection to gradient norms, learning dynamics, or the geometry of the loss landscape) would make the finding more informative.

- Variance or confidence intervals on the key correlations (Fig. 2a) would help assess whether differences between adjacent measurements are meaningful.

- Expanding the interference experiments beyond two simultaneous facts would strengthen claims about real-world relevance.

## Removed Points

The following points were considered but filtered out per review-merging guidelines:

1. **"Causal claim in Section 5.2 is not established" (in strong form)** — The stepping-stone intervention is a legitimate causal manipulation (manipulate keyword probability → observe priming change), and the paper provides baseline comparisons. The concern about confounds is real but does not invalidate the experiment; it only means the causal claim should be moderated. Kept as a Minor weakness above.

2. **"No confidence intervals on correlations"** — The paper shows scatter plots (Fig. 2b) that inherently display variance, and reports Pearson and Spearman coefficients across 1320 samples. While error bars would be nice, their absence is not a structural weakness.

3. **"No analysis of which parameters are affected by ignore-topk"** — This is a good suggestion for future work, not a flaw in the current paper. Moved to Nice-to-Haves.

4. **"Dataset comprehensiveness overstated"** — The paper claims "comprehensive" for a dataset of 12 keywords; the harsh critic labels this overstatement. The dataset is clearly scoped in Section 3.1 as serving a specific controlled-study purpose, and the diversity is in textual categories (11 categories) rather than lexical breadth. The criticism is somewhat overwrought.

5. **"Title broader than evidence"** — Partially valid but merges with the practical-significance concern above. The title "How new data pollutes LLM knowledge" is broad, but the paper's findings are still about new data's impact on LLM knowledge. This is a framing preference rather than a concrete weakness.

## Novel Insights

The synthesis of reviewer perspectives yields one observation beyond the paper's own contributions: the paper's pattern of results — cross-model robustness of the probability-priming correlation, coupled with the model-specific dissociation in whether memorization and priming are coupled (PALM-2: yes; Llama/Gemma: no) — suggests that the probability-priming relationship is a *property of the learning dynamics of auto-regressive transformers in general*, while the coupling with memorization is an architecture-specific feature. This framing (a universal data-property effect vs. an architecture-specific implementation detail) could guide follow-up work on mechanistic interpretability of gradient-based learning.

## Suggestions

1. **Address the denominator stability of $S_{\text{prime}}$ head-on.** Show that the probability–priming correlation holds when excluding samples with very low $P_{\text{before}}$ (e.g., below $10^{-10}$), report bootstrapped confidence intervals, and consider reporting an alternative metric (e.g., absolute probability change $\Delta P$) alongside the ratio to demonstrate robustness.

2. **Expand the limitations section substantially** to cover the scoping issues noted above (narrow lexical palette, single-sample paradigm, limited generic evaluation, lack of mechanistic account).

3. **Moderate the causal language** around the stepping-stone experiment: replace "direct evidence" and "strongly tested" with "converging evidence consistent with a causal relationship."

4. **Add standard benchmarks (MMLU, HellaSwag, or similar) to the ignore-topk evaluation** to substantiate the claim that generic language performance is not degraded.

5. **Either temper the title/framing** to reflect the controlled paradigm (e.g., "How individual training examples prime LLM knowledge") or provide evidence that the findings scale to more realistic training regimes.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>