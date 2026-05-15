Now I have a thorough understanding of the paper. Let me construct the final review.

---

## Summary

This paper investigates how zero-shot prompt variations affect the latent representations of auto-regressive LLMs. It uses two complementary approaches: (1) measuring the isotropy (effective dimensionality) of EOS-token hidden states via IsoScore across layers, and (2) clustering prompts based on their latent representations to see whether semantically similar prompts are grouped together. Experiments span four model families (Gemma, Phi, Bloomz, Zephyr) and three sentiment-analysis datasets. The paper finds that prompt formulation measurably alters representation geometry, that IsoScore evolves differently across model families, and that clustering reveals "counter-intuitive" groupings where semantically similar prompts are not necessarily grouped together.

## Strengths

- **Novel application of IsoScore to study prompt effects on latent geometry.** Prior work on prompting focused on language-level or performance-level analysis. Applying a principled isotropy metric (IsoScore) to quantify how prompts alter the effective dimensionality of representations at every layer is a genuine methodological contribution. The paper shows that prompt-induced IsoScore variation is non-trivial (e.g., std/mean percentages in Table 3 are 10–20%+ for many models).

- **Multi-model, multi-dataset evaluation reveals model-family-dependent behavior.** The study spans Gemma (2B/7B), Phi (3.8B), Bloomz (1.7B), and StableLM-Zephyr (1.6B/3B) across three datasets (Rotten Tomatoes, IMDB, YELP). This breadth allows the finding that prompt effects are not universal — e.g., Bloomz exhibits smoother IsoScore evolution than Phi/Zephyr — which is a genuinely useful observation for practitioners.

- **Layer-wise analysis of representation evolution.** Rather than only looking at the final layer, the paper tracks IsoScore and clustering quality at every layer, revealing how prompt effects propagate through the transformer stack. This is appropriate for understanding where and how prompt information is encoded.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified prompt set — a core reproducibility and interpretability gap.** The paper never states how many prompts are used, what their exact templates are, or how they relate to each other semantically. Section 4.3 says only: "take the default templates [from Promptsource] and duplicate them with minor modifications to isolate those characteristics." Which characteristics? How many prompts result? Without this information, readers cannot (a) reproduce the study, (b) assess whether the prompt set is sufficiently diverse to support the claims, or (c) interpret Table 4's clustering results (which show only 4 prompts and cannot be contextualized without knowing the full set). This is the single most fixable but also most damaging gap in the paper.

- **Clustering analysis lacks the baselines needed to support the central "counter-intuitive" claim.** The paper's second contribution is that "LLMs do not group prompts in an expected way." But the clustering evidence is evaluated against no baselines whatsoever: no random clustering, no clustering of raw text/SBERT embeddings of prompts, no clustering on prompt semantic similarity. The RIS (Rand Index Score) values are reported as "good," but without a baseline it is impossible to know whether a High RIS reflects meaningful structure or trivial artifacts (e.g., clustering by dataset rather than prompt). Table 4 shows that "Movie Expressed Sentiment 2" and "Text Expressed Sentiment" are grouped ~20% of the time, which the paper calls counter-intuitive — but without defining what the "expected" grouping frequency is (random chance? semantic similarity?), this observation is uninterpretable and could mislead.

- **No quantitative correlation between IsoScore and accuracy.** The paper repeatedly links IsoScore to performance in qualitative terms: "efficient prompts show similar evolution" (visual inspection of Figure 2), "bad performance seems to be correlated with extreme isotropy." Yet no correlation coefficient (Spearman, Pearson) is reported, no statistical test is performed, and the authors themselves acknowledge "we cannot link the IsoScore to the performance of the model and prompt with this Figure." This undermines the claim that bad prompts "destabilize internal representations" — a central component of HP1. The data may well support this, but the evidence as presented is anecdotal.

- **IsoScore operates near floor values with no statistical validation.** The reported IsoScore values range from 0 to 0.006 (max 0.6% of dimensions utilized). The paper acknowledges this is expected for EOS-only analysis, but then interprets tiny absolute differences as meaningful (e.g., Table 3 reports std as a percentage of mean IsoScore — a metric that can be misleading when the denominator is near zero). No confidence intervals, bootstrap estimates, or significance tests are provided to distinguish signal from noise. Given the near-floor values, this is essential.

### Minor

- **Ambiguous hidden state extraction for auto-regressive models.** The paper extracts "the last token representation associated to the EOS (End Of Sentence) token in the language modeling head." For auto-regressive models that generate tokens, it is ambiguous whether this is the last *input* token's representation (before generation begins) or the EOS token from the generated response. Current wording could confuse readers, even if the intended meaning (last input token) is standard practice.

- **Inconsistency about Bloomz's role.** Section 4.1 states Bloomz is "only used for prototyping purposes" due to data contamination, yet Bloomz appears prominently in the main results (Figures 5.1, Figure 2, and the analysis of smooth IsoScore evolution). This contradiction weakens the paper's clarity about what is a main vs. auxiliary result.

- **Limited task diversity.** All three datasets are binary sentiment analysis. The findings may not generalize to other binary classification tasks or to multi-class/generation tasks. The paper acknowledges focusing on binary classification for control, but this remains a limitation.

- **No sensitivity analysis for KMeans $k$.** Setting $k$ to the number of prompts is a natural choice but the paper does not explore how results change with different $k$ values or alternative clustering algorithms.

- **Some writing quality issues.** The Bloomz paragraph is self-contradictory (lists "Phi, Gemma, and Zephyr" as three families, then says "The fourth family is Bloomz"). Table 2's caption ("Mean standard deviation computed over the models and the prompts for each DataSet") does not clarify what quantity the standard deviation is taken over. These hinder readability.

### Trivial
None.

## Nice-to-Haves

- **Correlation analysis between IsoScore and accuracy.** A per-prompt Spearman correlation between IsoScore (per layer or averaged) and classification accuracy would directly test the claimed link between isotropy and performance.
- **Clustering baselines.** Comparing against random clustering, SBERT-embedding clustering, and prompt-length-based clustering would ground the "counter-intuitive" claim.
- **PCA visualizations of hidden states.** Showing 2D PCA of EOS vectors colored by prompt for representative layers would provide intuitive support for or against prompt-based separation.
- **Ablation on prompt length.** Controlling for prompt length as a trivial confound (longer prompts → different representations simply due to sequence length) would strengthen the analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

- Criticism that the paper's novelty claim ("no works have studied...") is too strong. This is a judgment about missing related works, which I cannot verify without external literature search.
- Criticism that PCA analysis is relegated to the appendix. The appendix exists in the original submission (not shown here due to parsing); this is a standard practice.
- Criticism that Figures 3/4 captions lack axis descriptions. The figures are image-placeholders stripped by the parser; the original submission contains the full figures with legends.
- Criticism that the conclusion restates a known fact. The contribution is in the *representation-level demonstration* of prompt sensitivity, not in the claim that prompts matter (which is indeed known at the behavioral level).
- Criticism about clustering methodology being "vague." The paper explains the majority-vote procedure, per-layer application, superclusters, and RIS evaluation (lines 56–66). The description is sufficient for a reader familiar with clustering; some details could be expanded but the methodology is not missing.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments identify methodological gaps (missing baselines, underspecified prompt set, lack of statistical rigor) but do not introduce new scientific insights about the paper's subject matter.

## Suggestions

1. **Disclose the full prompt set.** Provide a table or appendix listing all prompt templates, how they differ, and the "characteristics" each variation is meant to isolate. This is the single most important fix for reproducibility and interpretability.
2. **Add clustering baselines.** At minimum, compare against (a) clustering on SBERT embeddings of the prompts, (b) clustering on random embeddings, and (c) a permutation test to establish whether the observed RIS and superclusters exceed chance.
3. **Report correlation between IsoScore and accuracy.** Compute Spearman's ρ between per-prompt accuracy and per-layer (or averaged) IsoScore across all prompts, for each model and dataset. Report which layers (if any) show significant correlation.
4. **Provide statistical validation for IsoScore differences.** Use bootstrap resampling to estimate confidence intervals for IsoScore values, or report effect sizes with significance tests, especially given the near-floor absolute values.
5. **Clarify the Bloomz status.** Either commit to Bloomz as a full experimental subject (and explain why "data contamination" is not disqualifying) or relegate its results to the appendix.
6. **Resolve the EOS extraction ambiguity.** State explicitly whether the representation is taken from the last *input* token before generation or from the generated EOS token.

## Score and Decision

Originality: The research question (how prompts affect latent geometry) is worthwhile but incremental — IsoScore and similar analyses have been applied to embeddings; the novelty is in the object of study (prompts) rather than the method.

Importance of research question: High. Understanding how prompts influence internal representations has practical implications for prompt engineering and mechanistic interpretability.

Claims support: Weak. The most novel claim (counter-intuitive clustering) lacks baselines and statistical validation. The IsoScore-to-performance link is asserted based on visual inspection.

Soundness: The methodology is reasonable in design but the experimental execution has significant gaps (no baselines, no statistical tests, underspecified prompt set).

Clarity: Adequate but with several confusing passages (Bloomz paragraph, Table 2 caption, EOS extraction).

Value to community: Moderate. The direction is promising and the multi-model analysis is useful, but in its current form the evidence is too incomplete to serve as a reliable reference.

The paper addresses an interesting question and applies a sensible toolkit, but the experimental execution falls short of supporting the core claims. The most critical finding (counter-intuitive clustering) rests on unevaluated clustering results, and the IsoScore analysis lacks the statistical rigor needed to interpret near-floor measurements. These gaps can be fixed, but the paper as submitted does not convincingly demonstrate its contributions.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>