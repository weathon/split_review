Now I have a thorough understanding of the paper. Let me synthesize the final review by cross-checking every claim against the paper text.

---

## Summary

This paper investigates how zero-shot prompts alter the geometric structure of latent representations in auto-regressive LLMs. It evaluates four model families (Phi, Gemma, Zephyr, Bloomz) on three sentiment classification datasets, measuring layer-wise IsoScore (isotropy) and applying KMeans clustering to prompt representations. The claimed contributions are: (1) prompts modify latent vector distributions in a non-negligible way; (2) LLMs do not group prompts by semantic similarity, but rather by geometric features.

## Strengths

1. **Multi-family, multi-dataset systematic investigation.** The paper evaluates four distinct model families (Phi, Gemma, Zephyr, Bloomz) across three sentiment datasets (Rotten Tomatoes, IMDB, YELP) using a consistent protocol (Sections 4.1–4.2, Figures 1–2). This breadth reveals that prompt effects on IsoScore evolution are "highly dependent on the model family" (Section 5.1, Figure 1), a finding that goes beyond single-model studies.

2. **Layer-wise analysis of prompt effects on representation geometry.** The paper tracks IsoScore through all layers and shows that different prompts produce distinct distributions at each layer, with mean standard deviations reaching 5–30% of the mean IsoScore per model (Table 3). This provides genuine evidence that "prompts modify the vector distribution on the latent space in a non-negligible way" (Section 1) and that the effect persists through model depth.

3. **Counterintuitive clustering observation.** Table 4 documents that semantically related prompts (e.g., "Movie Expressed Sentiment 2" and "Text Expressed Sentiment") are grouped ~20% of the time, while intuitively similar pairs ("Movie Expressed Sentiment" and "Movie Expressed Sentiment 2") are not consistently grouped. This provides some support for the claim that LLMs "focus on more geometrical features than only semantic characteristics of prompts" (Section 1).

4. **Clustering stability across layers.** Figures 3–4 show that after majority voting, the number of prompt clusters and the Rand Index Score remain relatively stable through consecutive layers, indicating that the geometric features driving grouping are robust across depth (Section 5.2).

## Weaknesses

### Fatal

None.

### Major

1. **Prompt templates are underspecified, limiting reproducibility.** The paper states prompts are taken from Promptsource and "duplicated with minor modifications to isolate those characteristics" (Section 4.3), but neither the original templates nor the full set of modifications are enumerated. Only four prompts are named by their descriptive labels (M0, M1, S0, S1 in Table 4). Without knowing exactly what prompts were compared, how many there were, or what specific variations they encoded, the reader cannot fully interpret the results or replicate the study. While some prompt information may reside in the stripped appendix, the core method section should characterize the prompt set sufficiently for the reader to understand what was varied.

2. **Statistical significance testing is absent for IsoScore comparisons.** The reported IsoScore values range from 0 to 0.006 (at most 0.6% of dimensions effectively used). The paper acknowledges these low values, but it never provides confidence intervals, permutation tests, or any other statistical procedure to establish that the observed differences between prompts are significant relative to within-prompt variability or numerical noise. Error bars in Figure 1 are standard deviations *across prompts* rather than estimates of measurement uncertainty. Without such tests, the claim that "prompts do influence the way representations are distributed" (Section 5.1) is not adequately supported against the possibility that the tiny absolute differences arise from noise.

3. **The isotropy–performance link is handled inconsistently.** The paper initially motivates studying isotropy because prior work links it to model performance (Section 1, line 20; Section 2). It then finds "no apparent monotonic correlation or relation between isotropy and model performances" (Section 5.1). Rather than treating this as a null result that partially undermines the motivation, the paper pivots to "bad performance seems to be correlated with extreme isotropy" as a post-hoc observation on a subset of models (Figure 2) without any quantification or statistical support. This unmeasured, post-hoc claim should either be removed or backed with evidence.

4. **Accuracy evaluation pipeline is not described.** The paper references accuracy scores and uses them to color data points in Figure 2 (Section 5.1) but never explains how the model's generative output is mapped to a binary classification prediction. It does not specify whether log-probabilities of label tokens are compared, greedy decoding is used, or how ties or malformed outputs are handled. Without this, claims linking representation geometry to "bad performance" are unverifiable.

### Minor

1. **The clustering interpretation is overclaimed relative to the evidence.** The finding that prompts "Movie Expressed Sentiment 2" and "Text Expressed Sentiment" are grouped ~20% of the time (Table 4) is presented as "counter-intuitive," but no baseline or chance-level comparison is provided. Without knowing the expected grouping frequency under a null model (e.g., random labels), 20% may or may not be significant. The broader claim that clusters "weakly correspond to the semantic attributes of the prompts" (Section 5.2) is a reasonable interpretation but would be strengthened by contrasting against a formal baseline.

2. **EOS-only representation extraction is justified but not deeply examined.** The paper uses only the last (EOS) token representation (Section 3), arguing it "captures all contextual information." However, it does not consider whether other token positions (e.g., the last token of the input text) might be more informative for classification or more sensitive to prompt variations. This is a standard but not-trivial design choice that limits the scope of conclusions about "latent representations" writ large.

3. **Causal attribution of "bad prompts destabilizing representations" is not established.** The paper states that "bad prompts tend to destabilize internal representations" (Section 5.1), but accuracy is itself correlated with prompt properties (length, label wording, etc.) that could independently affect representation dispersion. The paper provides no causal analysis or controlled ablation to isolate prompt quality from prompt form.

### Trivial

- The text in Section 4.1 contains a duplicated sentence ("It is also noteworthy that other models provide minimal information regarding their pre-training data..." appears twice). This should be cleaned up.
- Bloomz is flagged for data contamination (Section 4.1) and said to be "only used for prototyping purposes," yet it still appears in main results figures. Clarify whether it is included or excluded from specific analyses.

## Nice-to-Haves

- A controlled ablation that varies prompts along known axes (label wording, instruction length, phrasing variations preserving semantic equivalence) and tests whether IsoScore differences replicate across multiple random seeds.
- Including permutation tests or bootstrapped confidence intervals for the IsoScore differences between prompts.
- Reporting variance within a single prompt across repeated runs (different random seeds for example ordering) to estimate noise levels.
- Using silhouette scores or gap statistics to determine the natural number of clusters rather than fixing k = number of prompts.

## Removed Points

These points from the reviews were removed with justification:

1. **"The clustering analysis is circular."** — Removed as a strawman. Setting k = number of prompts and running KMeans is a standard approach to test if prompts produce distinguishable representations; the majority-vote procedure then checks whether prompts collapse into shared clusters. This is methodologically sound, not circular.

2. **"RIS is not clearly defined."** — Removed as factually incorrect. The paper explicitly states: "The RIS assesses the extent to which a pair of examples, presumed to belong to the same cluster, are correctly labelled" (Section 3), which is the standard definition of the Rand Index.

3. **"The paper should acknowledge existing work on how input phrasing affects hidden states."** — Removed per the rule against demanding missing related works, as external verification is not possible.

4. **"Duplicated text and editorial errors in Sections 4.1/4.2."** — Kept as Trivial (the duplicated sentence is real) but the reviewer's characterization as a major editorial failure is disproportionate.

5. **Criticism of garbled prompt format.** — Removed as a parser artifact. The original submission likely contained a table of prompt templates that was lost during text extraction.

6. **"This claim is audacious given extensive literature."** — Removed per the rule against criticizing novelty claims about missing related works.

## Novel Insights

The harsh critic's claim that the clustering analysis is "circular" misunderstands the methodology: the paper sets k = number of prompts, runs KMeans, then uses majority voting to check whether prompts collapse into fewer clusters. The resulting k' < k is a genuine finding about prompts sharing geometric properties, not an artifact. However, neither reviewer identifies that the real weakness is not circularity but lack of a baseline comparison — without knowing chance-level grouping frequency, the claim of "counter-intuitive" clustering is weakly supported. The most novel insight from synthesizing the reviews is that the paper's actual contribution (prompts produce statistically distinguishable but weak geometric signatures) is more modest than claimed but still meaningful, and that the paper would be much stronger if it leaned into this measured finding rather than overclaiming.

## Suggestions

1. **Provide the full prompt set** in the main paper or appendix, including the exact templates and the modifications made to isolate specific characteristics. This is essential for reproducibility.

2. **Add statistical testing** (e.g., bootstrapped confidence intervals or permutation tests) for all IsoScore comparisons between prompts, and for the "~20% clustering" claim in Table 4.

3. **Describe the accuracy evaluation pipeline** — how model outputs map to binary predictions, how ties are resolved, and what decoding strategy is used.

4. **Remove or substantiate the post-hoc "bad performance correlates with extreme isotropy" claim.** If kept, provide quantification (e.g., correlation coefficient with p-value).

5. **Add a limitations section** discussing: (a) the very low absolute IsoScore values and whether findings are robust to other representation extraction methods (e.g., mean pooling); (b) the lack of causal isolation between prompt form and prompt quality.

6. **Frame the negative finding** (no monotonic correlation between isotropy and performance) as a contribution rather than an afterthought — it is an honest null result that challenges prior assumptions in the isotropy literature.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>