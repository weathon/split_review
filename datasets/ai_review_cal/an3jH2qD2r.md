- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5
Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper studies the *token-level* geometry of internal representations in LLMs (LLaMA 3 8B, Mistral 7B, Pythia 6.9B) using three metrics: cosine similarity, intrinsic dimension (ID), and neighborhood overlap (NO). Unlike prior work that summarizes a prompt as a single point (the last token), the authors treat the full sequence of tokens as a point cloud and track how its geometric properties evolve across layers. Systematic block-shuffling experiments cleanly show that disrupting syntactic/semantic structure raises the ID peak, increases token alignment, and reduces neighborhood overlap. The central finding is a statistically significant Pearson correlation (p<0.01) between token-level ID and next-token prediction cross-entropy loss across 2244 prompts, consistently observed in all three models around the mid-layer ID peak.

---

## Strengths

- **Token-level point-cloud analysis moves beyond prompt-level summarization.** Prior work (Ansuini et al., 2019; Valeriani et al., 2023; Cheng et al., 2023) typically represents each prompt as a single point in representation space. This paper instead studies the full empirical measure — the distribution of all tokens in a prompt across layers — linking directly to the dynamical-systems framework of Geshkovski et al. (2024b). The distinction is explicit in Section 1: "previous studies … summarized as a single point … not from the full sequence of tokens."

- **Systematic shuffling reveals clear geometric signatures of linguistic structure.** A multi-level block-shuffling scheme (Section 4.2, Figure 1) progressively disrupts syntax and semantics while preserving unigram frequencies. The results are clean: increased shuffling raises the ID peak (Figure 3), increases cosine similarity among tokens (Figure 2), and lowers neighborhood overlap (Figure 5). The joint pattern is coherent and well-illustrated.

- **Mechanistic explanation of the ID peak via nearest-neighbor geometry.** Using the TWO-NN estimator relation (Eq. 3), the paper shows that a higher ID implies the first two nearest neighbors are more equidistant. This is confirmed by angle histograms (Figure 4): shuffled prompts produce more equilateral triangles (mean angle ~60°) at the ID peak, providing concrete geometric intuition beyond simply reporting ID values.

- **Cross-model validation confirms patterns and suggests sensitivity to training data.** The same experiments are run on LLaMA, Mistral, and Pythia. Pythia — trained on The Pile (the same source as the test prompts) — consistently shows lower ID peaks and higher NO, consistent with the "structured data" signature (Section 4.3, Figures 6, 7). The authors appropriately caveat that this is suggestive rather than conclusive.

- **Statistically significant ID–loss correlation across three models.** The headline finding — Pearson correlation between ID and cross-entropy loss, computed across 2244 prompts at each layer — is shown in Figure 8 for all three models, with p-values below 0.01 (except Pythia's final layer). The correlation peaks around the middle layers, coinciding with the ID peak, and the pattern is consistent across models.

---

## Weaknesses

### Fatal
None.

### Major

- **The ID–loss correlation analysis lacks sufficient evidential depth for a central claim.** While the reported Pearson coefficients with p-values are a valid starting point, the paper provides no scatter plots, no rank-based (Spearman) correlation, and no analysis of potential confounds (e.g., token frequency, prompt topic, or loss quartile stratification) for the 2244 unshuffled prompts. The Pearson coefficient is sensitive to outliers, and without visual inspection of the data distribution or subgroup analysis, it is difficult to assess whether the correlation is driven by a few extreme prompts or reflects a genuine monotonic relationship throughout the natural range. The paper's main contribution rests on this finding, and the current evidence is thinner than it should be for a claim of this prominence. The authors themselves note that shuffling simultaneously raises both ID and loss, which further motivates the need to show that the correlation is not merely a between-condition effect. *(An analysis restricted to unshuffled data is indeed what was done, but the absence of basic diagnostic plots and robustness checks weakens the result.)*

### Minor

- **The theoretical chain connecting ID to loss is asserted without empirical verification of intermediate steps.** Section 4.4 argues: (i) residual-stream ID → logit ID via linear unembedding, (ii) logit ID → softmax entropy, (iii) softmax entropy → cross-entropy loss. Critically, step (i) assumes that ID is preserved under a non-isometric linear transformation (the unembedding matrix), which is not generally true and is not checked empirically. Step (ii) is discussed only heuristically. The paper treats this chain as explanatory reasoning, but the link from geometry to loss remains phenomenological rather than causally established. This does not invalidate the empirical correlation, but it limits interpretability.

- **No sensitivity analysis for the GRIDE range scaling parameter.** The paper uses range scaling = 2 (the conventional choice for GRIDE) and acknowledges multiscale analysis as future work. For an empirical paper where ID profiles are central, a brief sensitivity check (e.g., showing results for range scaling = 4 or 8) would strengthen confidence that the observed patterns are not artifacts of a single scale.

- **No confidence intervals for the Pearson coefficients.** Only p-values are reported (Figure 8 caption). Bootstrap confidence intervals or reported R² values would better communicate the strength and uncertainty of the correlations.

- **Cross-model comparison is suggestive but inconclusive.** The observation that Pythia shows "structured-data-like" signatures is interesting, but the paper correctly notes that this "would require a more comprehensive analysis" (Section 4.3). Model size and architecture differences between Pythia (6.9B), Mistral (7B), and LLaMA (8B) are not controlled. This is an acknowledged limitation.

### Trivial

- The shading in Figure 8 (and other figures) is labeled "standard deviation from the mean," but it is unclear whether this is the standard deviation across prompts, across bootstrapped samples, or across tokens within a prompt. Clarification would help.

- The multiple p-values across 33 layers × 3 models are not corrected for multiple comparisons. Given the clear pattern this is unlikely to change any conclusions, but it should be noted.

---

## Nice-to-Haves

- Showing a few qualitative examples — e.g., one prompt with high ID/high loss and one with low ID/low loss, with commentary — would help readers build intuition for what the correlation means in practice.
- Extending the analysis to models of substantially different sizes (e.g., 1B and 70B) would strengthen claims of generality.

---

## Removed Points

*These points were flagged in the inputs but are removed from the main review with justification below:*

1. **Harsh critic: "The paper is ambiguous about which data this correlation is computed on."** — The paper explicitly states in Section 4.4: "for the population of 2244 prompts." These are the unshuffled prompts, clearly defined in Section 4.1. No ambiguity exists.

2. **Harsh critic: "The paper does not discuss this" (length-induced bias from filtering to prompts ≥1024 tokens).** — Section 4.1 explicitly states: "We truncate the prompts by keeping the first N = 1024 tokens to eliminate the length-induced bias of our ID estimates if it were to be present." The paper does discuss it.

3. **Harsh critic: Block partitioning scheme is "arbitrary" and "not principled beyond convenience."** — The paper explains (Section 4.2) that N = 1024 = 4⁵, so powers of 4 naturally define the scheme. This is stated directly; it is not arbitrary without justification.

4. **Harsh critic: Range scaling = 2 "not justified."** — The paper states it is "the conventional choice for the GRIDE algorithm" (Section 3). A conventional choice from the cited methodology (Denti et al., 2021) is a perfectly adequate justification for the primary analysis.

5. **Strength Finder: "Three complementary metrics capture distinct aspects of geometry."** — Generic observation about methodology that any paper with multiple metrics could claim. Not a distinctive strength of this paper's contribution.

6. **Strength Finder: "Robustness through large-scale averaging."** — Averaging results across prompts is standard empirical practice. Not a distinctive strength.

---

## Novel Insights

Beyond the paper's own contributions, the only notable pattern emerging from the reviews is the consistent framing of a tension: the paper's central claim (ID–loss correlation) is both its most interesting contribution and its least rigorously supported one. The shuffling experiments, cross-model comparisons, and geometric interpretations are well-executed and internally coherent, but the headline finding that ties geometry to prediction performance rests on a single statistic (Pearson's r) without the diagnostic depth (scatter plots, subgroup checks, rank correlation) that would make it fully convincing. This suggests that the paper's value may shift depending on how much weight a reader places on the ID–loss correlation versus the other empirical observations.

---

## Suggestions

1. **Add scatter plots** of ID (at the peak layer, e.g., layer 10) vs. cross-entropy loss for the 2244 unshuffled prompts, along with Spearman rank correlation. This single addition would substantially strengthen the central claim.

2. **Check for confounds** by computing the ID–loss correlation within subgroups stratified by average token frequency, Pile subset (topic), or loss quartiles. If the correlation holds across subgroups, the claim is more robust.

3. **Empirically verify the unembedding-ID connection** by computing ID on the logits for a subset of prompts and comparing with the residual-stream ID. This would validate (or temper) the theoretical chain in Section 4.4.

4. **Add confidence intervals** for the Pearson coefficients (e.g., via bootstrap) and report R² values alongside p-values for all correlations.

---
