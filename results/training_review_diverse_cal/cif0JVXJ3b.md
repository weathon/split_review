I now have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a typology for distinguishing "Concept Neurons" (activated for few facts within a relation) from "Relation Neurons" (activated across many facts within a relation) within the Knowledge Neurons framework. It applies this typology across multiple PLMs, extends the analysis to 10 natural languages plus AutoPrompt, and releases the mParaRel dataset. The key claims are that (1) KNs exhibit a spectrum from fact-specific to relation-general roles rather than monosemanticity, and (2) KNs overlap substantially across languages, suggesting a partially shared, language-agnostic retrieval mechanism.

## Strengths

1. **Finer-grained typology that challenges KN monosemanticity.** The paper moves beyond treating KNs as monolithic and demonstrates that neurons occupy a continuum from concept-specific to relation-general (Figure 2a). The distributional analysis reveals polysemantic behavior that prior KN work (Dai et al., 2022) largely glossed over, providing a useful corrective.

2. **Large-scale multilingual KN overlap analysis across 10 languages.** The paper extends prior bilingual work (Chen et al., 2024) to 10 languages and provides a scaling analysis (Figure 4c) showing that shared KNs decay as a power law (~L^{-2.04}) rather than exponentially, making the random-overlap explanation extremely unlikely. This is the cleanest single result in the paper.

3. **Release of the mParaRel dataset.** A multilingual extension of ParaRel covering 10 languages with autoregressive-compatible prompts, along with a pipeline for further expansion. This is a concrete resource that enables reproducible cross-lingual KN research and is a clear community contribution.

4. **Honest self-assessment of limitations.** The paper transparently reports mixed boosting results ("classifying KNs into distinct and disentangled roles is not perfect"), acknowledges the AutoPrompt confound, and presents threshold-exhaustive analyses. This candor strengthens the credibility of the claims that survive scrutiny.

## Weaknesses

### Fatal
None.

### Major

1. **The "concept neuron" label conflates entity-specific with fact-specific encoding.** The typology defines Concept Neurons as KNs appearing in few instantiations within a single relation (Section 4). A neuron that activates for only one fact (e.g., *capital of France*) could encode the entity Paris, the entity France, the specific pair (France, Paris), or a relational subtype ("capital of a European country"). The paper never checks whether these neurons are invariant across *different relations* involving the same entity (e.g., does a "Paris" concept neuron also fire for *population of France*?). Without cross-relation evidence, the claim that the typology disentangles "conceptual" from "relational" knowledge is overstated — these are better described as "fact-specific" vs. "relation-general" within a single relation. The boosting experiments (Section 5.3) inherit this ambiguity.

2. **Mixed boosting evidence undermines the typology's claimed diagnostic utility.** Of six models tested, only two satisfy all three predicted effects (and only under restrictive thresholds: t_r=0.9, t_c=0.1). Only two models exhibit prediction (ii), and four exhibit prediction (iii). The paper's conclusion that "classifying KNs into distinct and disentangled roles is not perfect" is accurate but undersells the severity: the typology fails to reliably separate functional roles for most models. Attributing the failure to "noise" or "polysemanticity" raises the question of what the typology contributes beyond restating that KNs are not monosemantic (already established by Hase et al., 2023; Niu et al., 2023). The paper would be stronger if it demonstrated that even a noisy typology predicts editing outcomes better than a uniform baseline, or if it deeply characterized the one model where it works cleanly.

3. **Multilingual overlap is consistent with a simpler explanation: shared factual content, not a language-agnostic retrieval system.** The paper interprets KN overlap across languages as evidence of "a partially unified, language-agnostic retrieval system" (Abstract) and "a shared cross-linguistic mechanism for knowledge retrieval" (Introduction). However, the same relation and same entity pairs are probed in each language. The overlap could simply mean that the same fact (e.g., "Paris is the capital of France") recruits the same computational path regardless of language prompt — this is fact-driven overlap, not necessarily evidence of a language-agnostic *retrieval system*. To disentangle these, the paper would need controls such as testing facts present in English but absent from another language's training data, or showing that overlapping KNs correlate with the *relation* rather than the specific entity pair. Figure 5 attempts this via Concept vs. Relation Neuron analysis, but the results are inconclusive and model-dependent.

4. **The AutoPrompt experiment is fundamentally confounded by the shared gradient-based nature of both methods.** Section 6.3 reports >80% KN overlap between AutoPrompt triggers and natural-language prompts. The paper parenthetically notes that "it is possible that there exists a confound here because both Autoprompt and KNs are gradient based." This is not a minor caveat — it is a critical confound. AutoPrompt optimizes triggers via gradient descent over the same objective function used by the integrated gradient attribution that defines KNs. The high overlap may reflect shared sensitivity to the same gradient signal rather than shared knowledge representation. A non-gradient-based attribution method (e.g., ROME's causal tracing) would be needed as a control before any strong claim can be drawn. As it stands, this experiment cannot support its intended conclusion.

### Minor

1. **"Method-agnostic" claim not demonstrated.** The paper claims the typology is "agnostic to the specific knowledge attribution technique used" (Section 8, also Section 4), but all experiments use only KNs. Demonstrating the typology with even one other method (e.g., ROME or MEMIT) would substantiate this claim. As it stands, the contribution is KN-specific.

2. **Threshold statement contradicted by data.** The paper states "no major variation based on the choice of threshold was found" (Section 4), yet Figure 2b shows the proportion of Concept Neurons varies monotonically with threshold (decreasing from ~0.8 at t_c=0.05 to ~0.1 at t_c=0.3). The qualitative finding is robust, but the claim as written is misleading and should be qualified.

3. **Multi-ParaRel dataset documentation is insufficient.** The construction is described in only two sentences (Section 6.1): no details on the translation pipeline, quality assurance process, or how the "curation pipeline" works. For a released dataset meant to support reproducible research, this is inadequate.

4. **No robustness testing w.r.t. KN parameters (t_kn, p_kn).** The KN method itself has two parameters; the paper varies t_r and t_c exhaustively but does not test whether the typology results or the multilingual overlap findings are stable under different KN extraction thresholds. Since the entire analysis depends on what counts as a KN, this is an omission worth addressing.

### Trivial
- None that survive filtering (parser artifacts are not author errors).

## Nice-to-Haves

- Statistical significance testing for overlap coefficients using permutation tests (rather than a simple random baseline) would strengthen the multilingual analysis.
- An operational rule for selecting t_r and t_c thresholds (e.g., maximize predictive power in boosting) would make the method more replicable and reduce the appearance of arbitrariness.
- A deeper causal analysis on one well-behaved model (e.g., Gemma-2-9b under restrictive thresholds) showing how gradient attribution scores correlate with boosting outcomes, and whether the same neuron behaves as concept-like for one relation and relation-like for another.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper lacks method validation with ROME/MEMIT as a fatal flaw** — moved from Fatal to Minor because the typology is framed as "applicable to" other methods, and the paper explicitly positions it as "illustrated with KNs." The criticism is valid but not fatal.
- **Generic strength from Strength Finder about "addressing an important problem"** — dropped as superficial/unsubstantiated.
- **The reviewer's suggestion that the paper "should provide a baseline comparison using a non-gradient-based attribution method"** for the AutoPrompt experiment — kept in spirit as a Major weakness (the confound is real), but the specific ask for ROME causal tracing is noted as one possible approach, not the only one.

## Novel Insights

The most genuinely novel insight from the reviews is that the multilingual overlap finding may be *too* consistent with the simplest explanation (shared facts drive shared activations) to support the strong interpretation the paper gives it. The scaling analysis (power law decay of shared KNs across languages) is indeed the best evidence against randomness, but it does not distinguish between "language-agnostic retrieval system" and "fact-driven overlap with language as a shallow surface form." This distinction — whether KN overlap reflects shared content or shared mechanism — is the central unresolved question the paper leaves open and is more interesting than the paper's own interpretation suggests. A follow-up controlling for fact presence in training data across languages would cleanly adjudicate.

## Suggestions

1. **Rename the typology categories** from "Concept Neuron" and "Relation Neuron" to "Fact-Specific" and "Relation-General" (or similar) to accurately reflect what is actually measured — specificity within a single relation — unless cross-relation validation is added.

2. **Add a control for factual content in the multilingual experiments.** Identify facts that are present in English but absent from another language's training data (via corpus analysis) and test whether KNs for those facts still overlap across languages. If they do, the "language-agnostic" claim is strongly supported; if not, the overlap is driven by shared factual content.

3. **Either redesign or substantially de-emphasize the AutoPrompt experiment.** The gradient-based confound is too severe for the current result to be interpretable. At minimum, acknowledge it as a first-order limitation in the abstract and conclusion, not a parenthetical remark.

4. **Provide a deeper analysis of the one model where the typology works cleanly** (Gemma-2-9b or Llama-2-7b under restrictive thresholds), showing concrete examples of neurons that behave as concept-like for one relation and relation-like for another. This would give a tangible demonstration of the typology's value even in the face of mixed results.

5. **Clarify the threshold statement** in Section 4 to say that the *existence* of both concept-like and relation-like neurons is robust to threshold choice, not that proportions are invariant.

## Score and Decision

This paper tackles a genuinely important question with a conceptually useful distinction and a valuable new dataset. However, the empirical validation consistently falls short of the claims: the "concept neuron" label is ambiguous, the boosting evidence is mixed across models, the multilingual overlap has an uncontrolled alternative explanation, and the AutoPrompt experiment is confounded. The core contributions (the distributional analysis showing a spectrum of KN behavior, the power-law scaling of cross-lingual overlap, and the mParaRel dataset) are real, but they are presented within an interpretive frame that overstates what has been established.

The paper is best characterized as a *descriptive exploratory analysis* that generates interesting hypotheses rather than a *confirmatory study* that validates them. This kind of work has value for the community, but the claims need to be calibrated to the evidence. With the suggested revisions — particularly renaming/reframing the typology, adding a factual-content control for the multilingual analysis, and tempering the AutoPrompt interpretation — the paper could make a solid contribution. In its current form, the gap between claims and evidence is too wide.

**Originality:** 7/10 — typology and multilingual scaling are novel
**Quality:** 5/10 — sound but overclaimed; confounds weaken central results
**Clarity:** 7/10 — well-structured and honest about limitations
**Significance:** 6/10 — useful dataset and interesting preliminary findings

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>