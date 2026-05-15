Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a typology to disentangle "knowledge neurons" (KNs) into concept neurons (entity-specific) and relation neurons (relation-sensitive), applies this across six PLMs, and analyzes KN overlap across 10 natural languages plus AutoPrompt. The authors release the Multi-ParaRel dataset to enable this cross-lingual analysis. The main findings are that (a) KNs exhibit a continuous rather than cleanly dichotomous distribution between concept-like and relation-like roles, and (b) KNs overlap across languages far above chance, suggesting a partially shared knowledge retrieval mechanism.

## Strengths

1. **Well-motivated conceptual framework.** The paper correctly identifies that "knowledge" in a cloze task is not monolithic — distinguishing entity-level from relation-level encoding is a genuinely useful analytical lens, and the critique of monosemantic assumptions in the KN literature is timely and important.

2. **Cross-lingual KN overlap is quantified and shown to be far above random expectation.** For bert-base-multilingual-uncased, 710 shared KNs are observed between English and French versus ~100 expected by chance; for Llama-2-7b the gap is 189 vs. 2 (Section 6.2). The power-law decay (α=2.04 for Llama-2) further demonstrates non-random structure. This is the most compelling empirical result in the paper.

3. **KN overlap extends to unnatural languages (AutoPrompt).** Table 1 shows overlap coefficients up to ~80% for Llama-2 and Gemma-2, extending the multilingual finding to gradient-based machine-generated prompts — a novel result that strengthens the language-agnostic hypothesis.

4. **Honest characterization of limitations.** The paper transparently reports that only 2 of 6 models satisfy all three predicted boosting effects, that many neurons fall into an intermediate category, and that "classifying KNs into distinct and disentangled roles is not perfect" (line 98). This candor is a genuine strength, not a weakness.

5. **Release of Multi-ParaRel dataset.** A multilingual (10 languages) extension of ParaRel with an average of 17 prompts per relation and language, plus a pipeline for extensibility, is a practical contribution that enables future cross-lingual interpretability research.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent causal validation of the concept/relation neuron typology.** The boosting experiments (Section 5.3) test three predicted effects, but only 2 of 6 models (bert-large-uncased and gemma-2-9b) exhibit all three, and only under restrictive thresholds (t<sub>r</sub>=0.9, t<sub>c</sub>=0.1). The remaining four models fail to match at least one predicted pattern. While the paper is transparent about this, it means the central claim — that concept and relation neurons are functionally distinct and causally manipulable — is not consistently supported. The typology is defined purely by frequency within the KN attribution framework, without an independent behavioral assay to confirm the functional distinction. The mixed results do not rule out that the frequency-based separation reflects noise, token-level artifacts, or other confounds rather than genuine functional specialization.

2. **Multilingual KN overlap results do not adequately control for surface-level confounds.** The observed overlap across languages is quantitatively striking, but the paper does not test whether shared KNs are driven by shared subword tokens, cognates, or gradient-based attribution artifacts rather than genuinely shared semantic knowledge. The authors identify a similar concern for AutoPrompt ("may be confounded because both Autoprompt and KNs are gradient based," line 135) but do not extend this caution to the natural-language results. Without analyses that control for token overlap (e.g., testing with languages that share minimal subword vocabulary, or ablating shared surface forms), the conclusion of a "language-agnostic retrieval system" (line 129) is premature. The overlap is real; its interpretation as semantic (vs. surface-level) sharing is less secure.

### Minor

1. **No random-neuron control in boosting experiments.** The boosting experiments (Section 5.3) double or nullify concept/relation neurons but never compare effects to those from manipulating an equal number of randomly selected neurons from the same layers. Without this baseline, it is impossible to fully attribute the observed P@k changes to the *content* of selected neurons rather than to the general effect of perturbing any set of activations. (Dai et al. likewise lacked this control, but the omission limits the specificity claim here.)

2. **No formal statistical significance tests.** The boosting results are presented with standard error bars but no significance tests (e.g., permutation tests or confidence intervals) for whether the observed ΔP@k and ΔCCP@k reliably differ from zero. Similarly, the power-law fit (α=2.04) is reported without a goodness-of-fit measure or significance test.

3. **The symmetric threshold choice (t<sub>r</sub> = 1 − t<sub>c</sub>) is stated "for simplicity" (line 77) without justification.** The interaction between the upstream KN thresholds (t<sub>kn</sub>, p<sub>kn</sub>) and the new typology thresholds (t<sub>r</sub>, t<sub>c</sub>) is not explored, so the sensitivity of results to these coupled choices is unclear despite the claim of "no major variation" (line 48).

4. **Multi-ParaRel construction is described at a high level only.** The paper mentions a "translation and curation pipeline" (line 118) but does not specify how translations were obtained (automatic vs. human), whether quality checks were performed, or how prompts were validated for each language. This affects the ability to assess data quality, especially for lower-resource languages in the set.

### Trivial
- Minor typographical issues (e.g., "standrad error" on line 86).

## Nice-to-Haves

- **Permutation test for the typology distribution.** The continuous distribution in Figure 2a could be tested against a null distribution (shuffling instantiation labels) to quantify whether the tail of highly-frequent neurons is improbable under random assignment.
- **Token-level confound analysis for multilingual overlap.** Adding a non-Indo-European language (e.g., Chinese, Arabic) or testing facts with disjoint vocabularies would help disentangle semantic sharing from surface-form sharing.
- **Concrete case studies of proposed relational neurons.** Showing activation patterns for a putative relational neuron across different instantiations of the same relation (e.g., capital-of for different country pairs) would make the typology more tangible.
- **Apply the typology to other attribution methods (ROME, MEMIT).** The paper claims the method is "knowledge-attribution method-agnostic" but demonstrates it only on KNs.

## Removed Points

These points were flagged for removal from the main review; they are listed here with brief justifications in case they are useful.

- **Criticism that the boosting experiments are "inconsistent" and that "four models fail to match the predicted pattern" →** This was retained in the Major weaknesses section above (it is substantive and verified against the paper). However, the critic's framing that this "undermines the central contribution" is too strong — the paper's contribution includes *revealing* this inconsistency, not just establishing a clean typology.
- **Criticism about missing appendix/proofs →** Not present in the original reviewer comments.
- **Complaint that the paper does not explore different t_kn/p_kn values →** This is partially addressed in Minor weakness #3 above; the critic's demand for a "systematic sweep" is disproportionately heavy for an already empirically dense paper and is more of a nice-to-have.
- **"Missing related works" →** Hard rule: do not mention missing related works.

## Novel Insights

None beyond the paper's own contributions. The cross-referencing of the two reviewer perspectives does not surface any genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Add a random-neuron control** to the boosting experiments. This directly addresses the specificity claim and is a relatively small addition.
2. **Include a token-overlap analysis** for the multilingual results. Test whether KNs shared across languages are disproportionately those whose subword tokens overlap (e.g., "cap" in "capital," "Par" in "Paris" across Romance languages). Alternatively, add at least one non-Indo-European language to the analysis.
3. **Tone down the abstract and introduction** to better match the mixed results. Phrases like "unprecedented overlap... pointing to the existence of a partially unified, language-agnostic retrieval system" overstate the conclusiveness of the evidence given the uncontrolled confounds.
4. **Provide a significance test** for the power-law fit and for the boosting experiment deltas to clarify which effects are reliably nonzero.

## Score and Decision

The paper addresses an important question and makes concrete contributions (Multi-ParaRel dataset, cross-lingual overlap quantification, a critical conceptual lens on KNs). However, the central empirical claims are incompletely supported: the concept/relation neuron typology is validated inconsistently across models, and the multilingual overlap evidence does not adequately rule out surface-level confounds. The paper's honesty about limitations is commendable but does not fully compensate for the evidentiary gaps in its strongest claims.

**Originality:** 6/10 — The typology is a useful refinement, not a radical departure.  
**Importance of research question:** 8/10 — Disentangling knowledge representations is important for interpretability.  
**Claims well-supported:** 4/10 — The strongest claims outrun the evidence.  
**Soundness of experiments:** 5/10 — Reasonable methodology but missing key controls and significance tests.  
**Clarity of writing:** 7/10 — Clear, well-organized, honest about limitations.  
**Value to the community:** 6/10 — The dataset and conceptual framing are useful, but the empirical conclusions need strengthening.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>