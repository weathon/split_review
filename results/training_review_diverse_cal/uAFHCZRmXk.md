Now I have all the paper content I need. Let me synthesize the final review.

---

## Summary

This analysis paper investigates two phenomena in contrastive vision-language models—the modality gap (a geometric separation of image and text embeddings) and object bias (poorer performance on non-object tasks). The central contribution is identifying **information imbalance** between modalities (images contain more information than their captions) as the common trigger for both phenomena. The paper introduces a new metric (MOAD) to measure object bias, shows the modality gap is driven by few embedding dimensions, presents controlled synthetic experiments validating the causal role of information imbalance, provides supporting evidence from real data, and explores a connection between the modality gap and logit entropy control.

## Strengths

- **Controlled causal evidence via synthetic data (MAD dataset).** The paper directly manipulates the number of attributes in captions while keeping images fixed (Section 5.1, Figure 4). This clean intervention shows that reducing information imbalance simultaneously decreases both the modality gap and object bias, and improves accuracy. This is the strongest evidence for the paper's central causal claim and is well-designed.

- **Introduces a formal, generalizable metric for object bias (MOAD).** The Matching Object Attribute Distance (Section 5) provides a principled way to quantify bias that goes beyond simple performance gaps. The metric is general—applicable to any pair of factors, not just objects vs. attributes—and enables the paper to show that bias arises from per-sample caption presence (the conditional probability of a word appearing in a caption given the image), not from global word frequency (Figure 3(c) vs. 3(d)).

- **Systematic large-scale evaluation across 98 models with confounder analysis.** Section 4.1 evaluates a broad zoo of off-the-shelf VLMs and uses Kendall's τ rank correlation (Table 1) to show that the naive positive correlation between gap size and performance is driven by confounders like model size and embedding size. This clarifies a previously contradictory result in the literature and supports the practical claim that closing the gap is "worth fighting."

- **Reveals the low-dimensional structure of the modality gap.** Section 4.2 demonstrates that the mean difference between image and text embeddings is concentrated in a handful of dimensions (Figure 2(a)), and that two dimensions suffice to perfectly separate the modalities (Figure 2(b)). This structural insight goes beyond prior work that treated the gap as a uniform phenomenon and has implications for post-hoc mitigation strategies.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The entropy-gap connection is interesting but remains suggestive rather than conclusive.** The frozen-vs-learnable temperature experiment (Section 5.2, Figure 5) shows that a model with frozen temperature compensates by increasing the modality gap more, achieving similar logit entropy to the learnable-temperature model. The paper interprets this as the gap being a "feature, not a bug." However, an alternative explanation is not ruled out: freezing the temperature simply makes optimization harder, and the larger gap is a side effect of constrained optimization rather than a deliberate mechanism for entropy control. The paper partially acknowledges this via a footnote ("we do not claim a causal relationship; the changes can also just be measurable by the modality gap"), but the main text's "feature, not a bug" framing overstates the certainty. The evidence is consistent with the interpretation but does not uniquely support it.

2. **The real-data manipulation (CC12M caption truncation) is a coarser intervention than ideal for supporting the causal claim.** Dropping contiguous halves or quarters of captions (Section 5.1) changes caption length, syntactic structure, and semantic coherence simultaneously—not just information imbalance. While the synthetic experiment provides clean causal evidence, the real-data experiment does not isolate information imbalance from these covariates. The paper notes that "full" captions can be viewed as enriched versions of truncated ones, which partially addresses this, but a more controlled real-data manipulation (e.g., selectively removing objects vs. attributes while controlling length) would strengthen the external validity claim.

3. **The confounder-controlled analysis showing that smaller gap correlates with better performance is deferred to the appendix.** The main text (Section 4.1, line 188) states "when we control for these factors, we observe the expected negative correlation" with a reference to \cref{sub:fixed_dataset} in the appendix. Given that this claim contradicts the naive correlation shown in the main figures and is central to the paper's practical recommendation, showing at least one controlled condition (e.g., a partial correlation table or a plot for models of the same architecture family) in the main text would make the argument more self-contained and convincing.

### Trivial

- The MOAD formula is given for the image modality in the main text (Eq. 3), with the text modality version referenced to the appendix (line 334). Stating that the same logic applies symmetrically would improve readability.
- The neighborhood analysis (Kendall-τ distance, Table 2) uses class-mean embeddings, which discard within-class variance. The paper notes this implicitly but could state upfront that per-sample distances might differ and justify the choice more explicitly.
- The object/attribute frequency analysis (Figure 3(c)) uses token matching on the specific vocabulary from Bravo et al. The paper could note whether the finding is robust to plural/synonym handling.

## Nice-to-Haves

- A continuous measure of information imbalance (e.g., ratio of caption entropy to image entropy, or mutual information) would allow stronger quantification of "how much" imbalance causes "how much" gap/bias, and would bridge the synthetic and real-data experiments onto a common scale.
- A complementary intervention that **increases** shared information (e.g., enriching CC12M captions with additional attribute descriptions from an image captioner, as the paper itself suggests) would provide a stronger test of the causal claim than truncation alone and directly support the caption-enrichment recommendation.
- For the entropy-gap experiment, training from scratch with frozen temperature at different information imbalance levels (not just fine-tuning on "quarter" captions) and checking that the gap increases monotonically with imbalance would strengthen the mechanistic interpretation.
- The conclusion could list 2–3 concrete mitigation strategies beyond caption enrichment (e.g., balanced attribute sampling, training with an alignment-focused auxiliary loss) and note which are supported by evidence vs. speculative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder point #4 ("Reveals that the modality gap acts as a mechanism to control logit entropy"):** Moved here because the verified weakness (Minor point #1 above) shows that the evidence for this interpretation is suggestive but not conclusive. The experiment exists and is interesting, but calling it a "revealed mechanism" overstates what the evidence strictly supports. The finding is better characterized as an intriguing correlation consistent with the interpretation, rather than a confirmed functional role.

- **Harsh Critic's suggestion that "the paper should discuss how simplifications could affect generalizability" of the synthetic experiment:** The paper already discusses the MAD dataset design and the rationale for controlling attributes independently. The critic's suggestion is reasonable but amounts to asking the paper to add a caveat that is already implicit in the paper's own framing of the synthetic experiment as a "fully-controllable" simplification. This is not a weakness of the current paper.

- **Harsh Critic's "deepen information imbalance quantification" suggestion:** A continuous measure would be nice but is not necessary for the paper's ordinal claims. The paper's ordinal manipulations (number of attributes, dropped fraction) are adequate to support its central claims.

## Novel Insights

None beyond the paper's own contributions. The reviews largely agree on the paper's strengths and identify similar areas for improvement, rather than offering novel observations the paper missed.

## Suggestions

1. **Moderate the certainty on the entropy-gap "feature" claim.** Reframe Section 5.2 to present the finding as an observed correlation consistent with the interpretation, rather than as a demonstrated functional mechanism. The footnote already does this partially; the main text should follow suit.
2. **Show at least one controlled-condition plot in the main text for the confounder analysis** (Section 4.1), such as a partial correlation or a scatter plot color-coded by model family, so the reader can see the reversed correlation without consulting the appendix.
3. **Add a caption-enrichment experiment** (or acknowledge it as future work more explicitly) to strengthen the real-data causal evidence and directly support the practical recommendation.
4. **State explicitly in the main text that the MOAD formula applies symmetrically to both modalities** to avoid any ambiguity.

## Score and Decision

This is a solid analysis paper that makes a genuine contribution to understanding contrastive VLMs. The central claim (information imbalance as the common trigger) is well-supported by a clean synthetic experiment and corroborated by real-data evidence. The MOAD metric is a useful new tool. The structural analysis of the gap (few dimensions) is a genuine insight. The main weaknesses are (1) the entropy-gap connection is interesting but oversold relative to the evidence, and (2) the real-data manipulation is coarser than ideal. These do not undermine the paper's core contributions. The paper is well above the acceptance threshold.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>