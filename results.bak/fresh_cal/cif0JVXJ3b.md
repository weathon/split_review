Now I have all the information needed. Let me construct the final review.

## Summary

This paper proposes a typology of "knowledge neurons" (KNs) distinguishing concept neurons (sensitive to individual entities) from relation neurons (sensitive to relationships between entities), applies this typology across multiple PLMs, and investigates cross-lingual sharing of KNs across 10 languages using a new Multi-ParaRel dataset. The core contributions are: (i) evidence that KNs exhibit a continuous spectrum from concept-specific to relation-specific behavior, challenging strict monosemanticity assumptions, and (ii) demonstration of substantial KN overlap across languages that far exceeds random chance, suggesting partially language-agnostic knowledge retrieval mechanisms.

## Strengths

1. **Concrete, large-scale evidence of cross-lingual KN overlap.** The paper reports specific numbers: for Llama-2-7b, 189 shared neurons observed vs. 2 expected by chance across a language pair; for mBERT, 710 shared vs. ~100 expected. The power-law decay in shared neurons as languages are added (fitted α=2.04) is a non-trivial pattern inconsistent with random sharing and strengthens the claim of a structured, partially language-agnostic retrieval mechanism (Section 6.2, Figure 4c).

2. **Release of Multi-ParaRel, a multilingual benchmark.** The paper introduces and will release a dataset spanning 10 languages with prompts for cloze-style knowledge retrieval, including a translation/curation pipeline for extension. This is a concrete resource contribution enabling the cross-linguistic analysis in the paper and future work (Section 6.1).

3. **Honest characterization of the typology's limitations.** Unlike what a less careful paper might do, the authors explicitly acknowledge that KNs fall on a continuum (Section 5.2, line 73: "a continuous range"), that many neurons fall into an "intermediate category" (line 77), and that the boosting experiments yield "mixed results" (line 98). The paper states "classifying KNs into distinct and disentangled roles is not perfect" (line 98) — this is a strength of scientific candor even as it limits the strength of the claims.

4. **Evaluation breadth.** Experiments cover BERT, OPT, Llama-2, and Gemma-2 for monolingual analysis, and mBERT and Llama-2-7b for multilingual analysis, showing the main findings generalize beyond a single architecture (Sections 5.1, 6.1).

## Weaknesses

### Fatal

None.

### Major

1. **Cross-lingual overlap results have an unaddressed attribution-method confound.** The paper acknowledges a potential confound for the AutoPrompt experiment ("both Autoprompt and KNs are gradient based," line 135) but does not adequately address it for the core cross-lingual overlap result (Section 6.2). The random-neuron baseline used throughout does not control for the possibility that the integrated gradient attribution method systematically selects the same high-gradient neurons regardless of the input language or prompt. If the attribution method itself acts as a shared filter, the overlap may partially reflect methodological consistency rather than shared knowledge. The paper even notes that "shared activation does not equate to shared functionality" (Section 7) but does not apply the same scrutiny to the attribution method itself. **Why it matters:** This confound could undermine the paper's strongest claim — "the presence of a shared, language-agnostic knowledge base" (line 153). The power-law decay pattern (Figure 4c) is harder to explain by confound alone, but a proper control (e.g., comparing overlap across languages to overlap across different tasks in the same language, or using a non-gradient-based attribution method) is needed to disentangle genuine knowledge sharing from attribution artifacts.

2. **The concept/relation neuron typology is validated only partially and inconsistently across models.** The paper's causal tests (boosting experiments) show that all six models support the concept-neuron effect (effect i), but the relation-neuron effects are observed in a subset of models: effect (ii) in only 2/6 models (Llama-2 and Gemma-2), and effect (iii) in 4/6 models. The two models adhering to *all three* expected behaviors (bert-large-uncased and gemma-2-9b) do so only "under restrictive thresholds (t_r=0.9, t_c=0.1)." The paper is candid about these mixed results (line 98), yet the conclusion states "we were able to identify a subset of more specialized neurons, which we categorized as either conceptual or relational" (line 153) without sufficient qualification about how model-dependent and threshold-dependent this categorization is. **Why it matters:** A core claimed contribution is the typology itself. If relational neurons are only distinguishable from concept neurons at extreme thresholds and only in some models, the typology's practical utility and empirical grounding are substantially weaker than the presentation suggests.

### Minor

1. **Per-language performance on Multi-ParaRel is not reported.** The paper applies a 10% top-1 accuracy filter across all languages (line 66) but does not report accuracy per language or per relation-language pair. If model performance is poor in certain languages (e.g., Danish, Swedish — which may be underrepresented in training), the KNs identified for those languages may not correspond to genuine knowledge retrieval, weakening the cross-lingual overlap analysis. Reporting per-language accuracy would allow readers to assess whether the overlap finding is driven primarily by high-performing language pairs.

2. **The definition of concept neurons conflates concept-specificity with rarity.** A concept neuron is defined as one appearing in fewer than t_c×N instantiations of a relation. This means a neuron that genuinely encodes "Paris" but appears across multiple relations involving Paris (e.g., capital of, located in, population of) would be captured differently across relations, not as a unified concept. The paper does not acknowledge this limitation explicitly.

### Trivial

- None.

## Nice-to-Haves

- Provide a tabular summary of the boosting experiment results (ΔP@1, ΔCCP@1) across models and thresholds, supplementing the visual presentation in Figure 3.
- Compare cross-lingual KN overlap to overlap across *shuffled prompt sets* within the same language, as a control for the gradient-based attribution confound.
- Embrace the continuous-spectrum finding more explicitly by providing a "concept-ness" or "relation-ness" score per neuron rather than applying hard binary thresholds — some of this is already implicit in Figure 2, but making it explicit would strengthen the contributions.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not discuss sensitivity of integrated gradients to baseline choice":** True but this is a general limitation of the attribution method, not specific to this paper's analysis. The paper uses an existing method (Dai et al., 2022) without modifying it. This is scope creep.

- **"'No major variation based on choice of threshold was found' contradicts later restrictive-threshold result":** Misreading. The "no major variation" statement (line 48) refers to the distribution of concept/relation neuron *counts* across thresholds (Figure 2b), not to the causal boosting effects. These are distinct analyses; there is no contradiction.

- **"No quantitative summary of boosting results — purely text descriptions":** Incorrect. Figure 3 provides full quantitative curves with ΔP@k and ΔCCP@k values with error bars across k=1 to 100, and for multiple threshold pairs and models. The critic appears to have missed the figure. A tabular summary would be nice-to-have, but not absent.

- **"No discussion of computational constraints / total compute hours":** The paper reports "less than an hour per relation" (line 64) and "about one hour per relation and per language" (line 116), which is sufficient for reproducibility. Requesting more detail is a minor presentation preference, not a weakness.

- **"If the paper cites it, it exists" rule applies:** Any criticism questioning whether the models or datasets cited exist is removed by policy.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the power-law decay of shared KNs as a function of number of languages (Figure 4c) is a more striking and specific result than the paper fully capitalizes on. While the paper notes this fits α=2.04, it does not discuss what this specific exponent might imply about the underlying sharing structure (e.g., whether it suggests hierarchical clustering by language families, or a latent dimensionality of the shared knowledge subspace). The reviews do not surface any other insight that the paper itself has not already articulated.

## Suggestions

1. **Address the gradient confound directly.** The most actionable suggestion is to perform a control experiment: compare KN overlap across languages to KN overlap across two *different relations* within the same language. If the cross-lingual overlap is genuinely about shared knowledge retrieval, it should be substantially higher than cross-relation overlap (where different knowledge is accessed). Alternatively, use a non-gradient attribution method (e.g., causal mediation as in ROME) to verify the overlap patterns persist.

2. **Quantify the typology on a continuous scale.** Rather than binary classification at arbitrary thresholds, define a "relational score" per neuron (e.g., the proportion of instantiations in which it appears), and show that this score correlates with the expected causal signatures (ΔP@1 vs. ΔCCP@1) in the boosting experiments. This would transform the typology from a threshold-dependent categorization into a graded, empirically validated measure.

3. **Report per-language accuracy** on the Multi-ParaRel dataset in a supplementary table. This simple addition would substantially strengthen confidence in the cross-lingual overlap analysis.

4. **Rephrase the conclusion** to more precisely reflect the mixed evidence: e.g., "for some models (particularly bert-large and gemma-2), at restrictive thresholds, we observed the predicted causal signatures for both concept and relation neurons, while for other models only the concept-neuron signature was consistent."

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>