Now I have a thorough understanding of both the paper and the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes a typology distinguishing "concept neurons" (sensitive to individual entities) from "relation neurons" (sensitive to relationships between entities) within the Knowledge Neurons (KNs) framework, and extends KN analysis to 10 languages using a new multilingual dataset (Multi-ParaRel). The key empirical findings are that some KNs can be causally linked to specific roles (though with mixed results), and that KNs overlap across languages substantially more than chance would predict, suggesting a partially shared cross-linguistic knowledge representation.

## Strengths

- **Release of Multi-ParaRel, a multilingual benchmark for knowledge attribution.** The paper introduces and releases Multi-ParaRel, an extension of ParaRel with 10 languages and AutoPrompt prompts, enabling reproducible cross-lingual analyses of knowledge neurons. The dataset fills a gap by providing parallel prompts across languages for autoregressive models, and the paper provides a pipeline for further expansion.

- **Principled typology of concept vs. relation neurons with causal validation attempts.** The paper introduces a clear, threshold-based typology (Section 4) that goes beyond prior work treating all KNs as encoding single facts. The boosting experiments (Section 5.3) causally test the typology — showing that for some models under some thresholds, manipulating concept neurons boosts precision at rank 1 while relation neurons affect correct-category proportion — providing partial evidence that the typology captures behavioral differences.

- **Demonstration that KNs overlap across languages far exceeds chance.** The paper shows that KNs overlap significantly across all 10 languages tested, with the number of shared neurons following a power-law decay (exponent α=2.04 for Llama-2-7b) far above the random baseline (Section 6.2). The pairwise overlap is quantified against a random expectation (710 shared vs. ~100 expected by chance for BERT; 189 vs. 2 for Llama-2-7b), providing the strongest evidence to date for a shared cross-lingual knowledge representation at the neuron level.

## Weaknesses

### Fatal
None.

### Major

- **The multilingual overlap analysis shows correlation, not functional equivalence, yet the paper's headline claims imply a stronger mechanistic interpretation.** The paper identifies overlapping neuron *indices* across languages for the same relation but does not verify whether those neurons serve the same *function* in each language. A neuron could be selected as a KN in both English and French for the same relation due to different lexical pattern-matching rather than shared relational knowledge. The paper acknowledges this in Section 7 ("parallel activation does not equate to shared functionality") but does not provide any causal evidence (e.g., cross-lingual editing experiments) to address it. Meanwhile, the abstract claims the data "point[s] to the existence of a partially unified, language-agnostic retrieval system" and the conclusion states "a shared, language-agnostic knowledge base within multilingual models." These causal/mechanistic claims go beyond what the correlational evidence supports. The overlap observation is valuable and interesting, but the interpretive leap is not fully warranted.

- **The AutoPrompt comparison has a known confound that is acknowledged but not addressed.** Section 6.3 reports very high overlap between English KNs and AutoPrompt KNs (≥80% for non-BERT models). The paper notes in passing that "it is possible however that there exists a confound here because both Autoprompt and KNs are gradient based." This is a critical issue: if both the prompt generation method and the attribution method rely on gradients through the same model, the overlap could reflect a shared gradient artifact rather than shared knowledge representation. Since the AutoPrompt result is highlighted as a headline contribution (abstract and introduction), this confound substantially weakens the claim. The paper should at minimum discuss whether alternative attribution methods (e.g., causal mediation) produce similar overlap, or provide experimental controls to rule out the artifact.

### Minor

- **The typology validation is mixed, and the paper's framing oscillates between claiming the typology works and acknowledging its limitations.** The boosting experiments show that only 2 of 6 models exhibit all three expected behavioral patterns, and only under restrictive thresholds (t_r=0.9, t_c=0.1). The paper is honest about this ("classifying KNs into distinct and disentangled roles is not perfect"), but the abstract's claim that "KNs come in different flavors, some indeed encoding entity level concepts" reads as more definitive than the evidence warrants. A clearer separation would be: the typology is a useful heuristic capturing some variance in neuron function for a subset of models/neurons, but it is far from a clean decomposition.

- **"No major variation based on the choice of threshold was found" is contradicted by the paper's own Figure 2b.** Section 4 states thresholds produce "no major variation," but Section 5.2's Figure 2b caption notes that "the proportion of concept neurons decreases with more demanding thresholds." While relational neuron proportions are stable, concept neuron proportions clearly vary with the threshold. This is a minor internal inconsistency.

- **No confidence intervals or formal statistical tests for overlap comparisons.** The multilingual overlap analysis (Section 6.2) provides a useful random baseline calculation but does not report confidence intervals or permutation tests for the observed overlap values. The fitted power-law exponent (α=2.04) is reported without uncertainty bounds. While the observed gap relative to chance is large, formal statistics would strengthen the contribution.

- **Limited dataset quality details for Multi-ParaRel.** The paper does not report human evaluation or automated quality metrics for the translations, average prompt length, answer token consistency, or the proportion of prompts filtered per language. These details would help readers assess dataset quality.

- **The discussion section is very brief (two sentences) and does not deeply engage with limitations.** Key limitations worth discussing: the European-only language sample (10 languages, all Indo-European), the reliance on a single attribution method (KNs via integrated gradients), the small number of prompts per language post-filtering (~10), and the correlational nature of the multilingual overlap. A dedicated limitations section would improve the paper.

### Trivial

- The notation p_kn should be defined before use in Section 3.
- The paper mentions "standrad error" (typo in Figure 3 caption — though note: this may be a parser artifact).
- The text reports boosting effects for "six models" but only shows figures for two; a summary table of all six would improve readability (this straddles Minor/Trivial).

## Nice-to-Haves

- **Cross-lingual editing experiments** to test whether shared KNs are causally involved in the same knowledge across languages (e.g., edit a shared KN in one language and test effects in another). This would directly address the functional equivalence gap.
- **Comparison with an alternative attribution method** (e.g., causal mediation as in ROME) to assess whether the AutoPrompt overlap persists across methods, which would weaken the gradient-artifact explanation.
- **A summary table** showing, for each model and each threshold, whether the boosting experiments supported hypotheses (i), (ii), and (iii). The current prose description is hard to follow across six models.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The conclusion claims the typology is 'agnostic to the specific knowledge attribution technique used' but the paper only tests it on KNs."* — Removed because the claim is about the typology being *method-agnostic by design* (it classifies neurons based on frequency across prompts, not on the attribution method), not about having tested it on other methods. This is a reasonable forward-looking statement, not a flaw.

- *"The definition of Concept Neurons is problematic because it defines a category negatively."* — Removed because the definition is a standard frequency-based thresholding approach, not a "negative" definition. A neuron appearing in very few facts is operationally defined as more likely concept-specific. The threshold sweep mitigates this concern, and the paper does not claim these are "pure" concept neurons but rather neurons that are "more likely" to encode specific entities.

- *"No human evaluation or quality metrics are reported"* for the dataset — Moved from a standalone criticism to Minor (merged with other dataset detail concerns), as the paper provides the pipeline and filtering procedure, which is reasonable for an initial release.

- *Strengths from Strength Finder about "strong evidence for a language-agnostic retrieval mechanism"* — Tempered in the strengths section above to reflect the Major weakness about correlational evidence. The overlap data is real and above chance; the interpretation is what needs tempering.

## Novel Insights

The reviews surface a genuine tension in the paper. The harsh critic correctly identifies that the paper's strongest contribution — the cross-lingual overlap finding — is also where the interpretation outruns the evidence. The paper's own Section 7 acknowledges the functional equivalence problem in two sentences and then moves on, but the abstract and conclusion continue to reference a "language-agnostic retrieval system." This gap between the correlational data and the mechanistic claims is the paper's central unresolved issue. The strength finder correctly identifies the overlap finding as important, but treating it as evidence of a "shared retrieval system" without functional validation is a leap. A genuinely novel angle would be to reframe the paper as: "KNs overlap across languages far beyond chance — but what does this overlap mean? We provide the data and the methods to study this, while explicitly flagging the interpretive limits." This framing would make the paper's caution (Section 7) its central message rather than an afterthought.

## Suggestions

1. **Temper central claims to match the evidence.** Replace "language-agnostic retrieval system" with "substantial neuron overlap across languages, consistent with shared representations, though functional equivalence remains to be demonstrated." This is more accurate and would not diminish the paper's contribution.

2. **Address the AutoPrompt confound explicitly.** Even a brief discussion of why a gradient-based confound is or is not likely (e.g., are other gradient-based methods like integrated gradients on random inputs producing similar overlap patterns?) would substantially strengthen this result.

3. **Add a dedicated limitations section** covering the language coverage (10 European languages), reliance on a single attribution method, limited prompts per language, and the correlational nature of the multilingual analysis.

4. **Include a summary table** for the boosting experiments showing all six models and their support (or lack thereof) for each of the three expected behavioral effects at each threshold tier.

## Score and Decision

The paper makes genuine contributions — the Multi-ParaRel dataset, the systematic cross-lingual overlap analysis across 10 languages, and the concept/relation typology — but the headline claims about a "language-agnostic retrieval system" and the AutoPrompt result are not well-supported by the current evidence. The core empirical finding (KNs overlap across languages far more than chance) is solid, valuable, and worth publishing. However, the paper's framing needs substantial revision to align claims with evidence, and the AutoPrompt confound requires explicit discussion if not additional controls.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>