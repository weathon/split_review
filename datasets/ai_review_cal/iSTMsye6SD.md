- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have a thorough understanding of the paper and the reviewer inputs. Let me produce the consolidated review.

## Summary

This paper proposes a fully automated pipeline for generating knowledge-intensive QA benchmarks at scale by sampling subgraphs from open knowledge graphs (Wikidata and T-REx), encoding them as SPARQL queries, and translating those queries to natural language via an LLM (Llama-3-70B-Instruct). Using these benchmarks (100k questions per configuration), the paper evaluates several SOTA LLMs under zero-shot, RAG, and CoT settings, finding that LLMs struggle to recall and leverage world knowledge even when that knowledge was present in pretraining, and that neither RAG nor CoT fully closes the gap. The paper also introduces a "knowledgeability transparency" analysis examining whether LLM answer confidence reflects confidence in the underlying facts.

## Strengths

- **Fully automated, scalable benchmark generation pipeline.** Section 2.2 describes a pipeline involving subgraph sampling via random walks, entity masking, SPARQL encoding, and LLM-based translation that requires zero manual annotation. Table 2 contrasts this approach with existing datasets that rely on human annotation or templates. The manual quality check (Table 3, 1,200 examined questions) provides direct evidence that the pipeline produces high-quality questions at scale. This is the paper's primary contribution and is well-supported.

- **Empirical demonstration that LLMs struggle even with knowledge present in pretraining data.** By generating benchmarks from T-REx (Section 2.3), where all facts are aligned to Wikipedia and guaranteed to be in LLM pretraining corpora, the paper shows that even GPT-4 achieves at most 71.4% on 1-unknown questions (Table 5), with performance dropping sharply for larger patterns. This substantiates Finding 1 with concrete evidence.

- **Comprehensive evaluation across multiple reasoning-supporting techniques.** The paper tests zero-shot (Tables 4–7), RAG with basic and oracle retrieval (Tables 8–9), and CoT prompting including a mismatch analysis (Tables 6–7, 10–11). These experiments produce three concrete findings — showing that neither RAG nor CoT fully closes the performance gap — which is a non-trivial empirical contribution.

- **Careful methodological treatment of knowledgeability metrics.** Section 3 identifies a confounding effect in the basic log-likelihood metric (varying numbers of correct answers can inflate or deflate apparent confidence) and proposes alternative formulations ($\bar{K}_{\text{sum}}, \bar{K}_{\text{min}}$) that are feasible to compute via LLM-generated binary questions. This shows methodological awareness.

- **CoT demonstration–test mismatch analysis.** Tables 10 and 11 systematically vary reasoning patterns between CoT demonstrations and test questions, revealing that mismatches can degrade performance. This adds nuanced insight beyond simply reporting CoT improvements.

## Weaknesses

### Fatal

None.

### Major

- **Knowledgeability transparency analysis lacks quantitative validation.** Finding 4 is a central claim, but its evidence rests entirely on visual inspection of plots (Figure 6). The paper states "the plot suggests" and "These plots indicate very poor correlation between the quantities" but reports no correlation coefficients, no confidence intervals, and no statistical tests. Without quantification, "poor correlation" is an unsubstantiated judgment. Additionally, the method for extracting log-likelihoods (system prompts and few-shot demonstrations to force "Yes"/"No" or entity-name outputs) may alter the model's behavior, making the measured quantities potentially artifact rather than genuine confidence indicators. Since the transparency study is presented as "first-of-its-kind" (abstract), the lack of rigorous quantitative support is a significant gap.

### Minor

- **Impact of SPARQL translation errors on findings is not analyzed.** The manual quality check (Table 3) establishes translation accuracy, but the paper does not analyze whether the ~5–6% (or whatever the exact rate is) of mistranslated questions systematically bias the results in any direction. The paper could bound this concern by re-running key analyses on only high-confidence translations. While the error rate is low, its potential to affect conclusions is unexplored.

- **Exploitable correlations in KGs are acknowledged but not quantified.** The paper (Section 2.4) correctly identifies that KG predicate correlations can let LLMs answer questions via shortcuts rather than genuine knowledge recall, and commits the issue to future work. However, the paper does not estimate what fraction of questions are vulnerable to such shortcuts or how a simple correlation-exploiting baseline would perform. The concern is partially mitigated by the paper's transparent disclosure and the fact that questions still require some reasoning, but the magnitude of the problem is unmeasured.

- **Ground truth incompleteness defense is suggestive but not definitive.** The paper argues (Section 2.4) that comparable performance on T-REx and Wikidata suggests ground truth incompleteness is not foundational. This is a reasonable heuristic but not a rigorous demonstration — similarity in aggregate performance could arise from other factors (overlapping knowledge, model biases). A direct analysis of false-negative rates (model answers that are correct but marked wrong) would substantiate the claim.

### Trivial

- Inconsistent capitalization ("Tabel" instead of "Table" on line 143) and minor grammar issues throughout.
- Figure references (e.g., "Figure 6a" and "Figure 6b" vs. "Figure 6") are somewhat confusing — it is unclear whether these are subfigures or separate figures.

## Nice-to-Haves

- Reporting correlation coefficients (e.g., Spearman's ρ or Pearson's r) for the knowledgeability transparency plots would significantly strengthen Finding 4.
- The RAG and CoT analyses use smaller subsets (5k, 1k questions); reporting confidence intervals or standard errors for these would clarify the precision of the reported accuracies.
- A few concrete examples of mistranslated SPARQL-to-NL questions (from the manual quality check) would help readers understand the nature and severity of the translation noise.

## Removed Points

These points were flagged in the input reviews but are removed for the following reasons:

- **"15–30% of SPARQL-to-natural-language translations are inaccurate"** — This claim from the harsh critic appears to conflate the 95% lower confidence bound with the actual error rate. The Strength Finder reports sample accuracy >94% for all question types. Since Table 3 is only available as an image, the exact numbers cannot be verified from text, but presenting the lower bound as a point estimate of the inaccuracy rate is misleading. The actual error rate is much lower (likely ~5–6%), which changes the severity assessment substantially.

- **Translation errors called "fatal" / "structural"** — Even at the reported 94%+ sample accuracy, translation errors affect a small minority of questions. This is a minor concern that deserves analysis, not a fatal flaw.

- **"Exploitable correlations are a fatal threat"** — The paper transparently discloses this limitation. It does not invalidate the benchmark's core value; the issue is a matter of quantification, not structural invalidity.

- **"No release statement"** — Rule: remove criticisms that question the existence/release status of artifacts.

- **"No error bars or significance tests"** — With 100k questions, standard errors are negligible. For smaller subsets (5k, 1k), the absence is a nice-to-have, not a weakness. Many LLM evaluation papers at this scale do not report error bars.

- **"No analysis of model scale vs. performance"** — This demands the paper pursue a direction (scaling laws) that is outside its stated scope.

- **"Missing related works"** — Rule: do not mention missing related works without external sources to confirm.

- **"Overstated 'first-of-its-kind' claim"** — Without external sources to assess the prior art landscape, this criticism cannot be verified. The paper includes the qualifier "to our best knowledge."

- **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The most interesting observation emerging from the cross-review is the tension between the paper's transparent self-awareness of its limitations (Section 2.4 explicitly identifies exploitable correlations and ground truth incompleteness) and the reviewers' treatment of these same limitations as unaddressed fatal flaws. The paper would benefit from viewing this transparency not as a weakness but as a strength to be leveraged: the acknowledged limitations could be turned into concrete ablation analyses (e.g., filtering questions with correlated predicates and re-running, or manually sampling false negatives to estimate the false-negative rate). Beyond the paper's own contributions, the reviews collectively highlight that benchmark-generation papers carry a higher burden of proof about construct validity — what the benchmark actually measures — which the paper partially addresses but could address more systematically.

## Suggestions

1. **Quantify the transparency analysis.** Report at least one correlation coefficient (Spearman's ρ) with confidence intervals for the plots in Figure 6. This is a low-effort change that would substantially strengthen Finding 4.

2. **Bound the effect of translation errors.** Re-run the main zero-shot results on the subset of questions whose SPARQL translations were manually verified as correct (the 1,200 examined questions, or a larger automated filter). If the qualitative findings hold, this would neutralize the translation-concern critique.

3. **Estimate the exploitable-correlation fraction.** Construct a simple baseline that exploits known predicate correlations (e.g., answering using the most common co-occurring entity) and report what fraction of questions it can answer and how LLMs compare.

4. **Add a small false-negative analysis.** Manually inspect a random sample of supposedly incorrect LLM answers to estimate how often the model produces a correct answer not in the ground truth set.
