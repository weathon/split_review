Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes an evaluation framework for unsupervised concept bottleneck models (CBMs). It introduces **ConceptScore**, a reference-free metric that uses LongCLIP to measure semantic alignment between predicted concepts and images, and **Ref-ConceptScore**, which incorporates ground-truth labels via a harmonic mean between ConceptScore and concept-concept similarity. NLP metrics (BLEU, METEOR, ROUGE) are also adapted for concept evaluation. The framework is validated on LFCBM and PHCBM across CIFAR-10, CIFAR-100, and CUB200, showing moderate correlations (0.29–0.47) with human judgments and GPT-4v scores.

## Strengths

- **Addresses a genuine gap.** Evaluating unsupervised CBMs without ground-truth labels is an open problem, and the paper's framing of this need is well-motivated (Section 2.2, lines 33–35).
- **Reference-free evaluation for unsupervised scenarios.** ConceptScore leverages cross-modal alignment (LongCLIP) to assess concept-image coherence without requiring any annotated concepts, directly targeting the unsupervised setting where existing accuracy-based metrics fail (Section 3.2, lines 39–52; Section 4.4, lines 187–188).
- **Sensitivity to concept degradation.** The sensitivity analysis (Section 4.6, lines 209–210) shows that replacing correct concepts with incorrect ones drops ConceptScore from 0.5625 to 0.3811 and Ref-ConceptScore from 0.6958 to 0.5297, demonstrating that the metrics respond meaningfully to concept quality.
- **Multi-faceted validation with human and GPT judgments.** Correlations with human scores (ConceptScore: 0.4213, Ref-ConceptScore: 0.4704) and GPT scores (Ref-ConceptScore: 0.5913) provide converging evidence that the metrics capture aspects of concept quality aligned with human perception (Section 4.3.1, lines 174–178).

## Weaknesses

### Fatal
None.

### Major

- **No baseline comparisons for correlation magnitudes.** The paper reports correlations of 0.42 (ConceptScore vs. human) and 0.47 (Ref-ConceptScore vs. human) but provides no baseline reference (e.g., random assignment of concepts, constant-score baseline, or a simpler alternative like average embedding similarity without reweighting). The reader cannot judge whether 0.42 is meaningful or merely reflects trivial signal. The implicit comparison against NLP metrics (which score 0.29–0.31) helps partially, but a direct random/trivial baseline is needed to establish the framework's value. (Section 4.3.1, lines 174–178)

- **Key terms left undefined, making results uninterpretable.** The paper repeatedly references "the top 5 combinations for Prompt1" (lines 187, 198) without ever defining what "Prompt1" is or what the "top 5 combinations" are. Since Tables 1 and 2 are presented as evidence for the framework's effectiveness, this omission makes the core experimental results impossible to interpret or reproduce.

- **The sensitivity analysis description is ambiguous.** The paper states it "rearrang[ed] the order of the top 8 concepts and alter[ed] their corresponding weights" (line 209), causing ConceptScore to drop from 0.5625 to 0.5136. It is unclear what exactly was manipulated — whether concept *identities* changed, only their order/weights, or different concept-weight assignments were applied to different images. Since the metric is computed per concept independently, simple reordering should not change the score. The paper needs a precise description of the perturbation and a rationale for why the observed change is expected. (Section 4.6, lines 209–210)

### Minor

- **Undisclosed design parameters hurt reproducibility.** The weight ω in ConceptScore (line 49) is never given a value, the prompt template 𝒫(ĉ) is never specified (line 44: "formulated as 𝒫(ĉ)" is circular), and the choice of LongCLIP over CLIP is asserted but never ablated. While ω as a uniform scaling factor does not affect correlation coefficients (the core validation claim), these omissions prevent exact reproduction of the absolute scores in Tables 1–2 and limit practical adoption of the framework. (Sections 3.2–3.3)

- **Harmonic mean justification is internally contradictory.** The paper claims the harmonic mean "gives more weight to lower values, ensuring that a single low ConceptScore does not dominate" (line 61). In fact, the harmonic mean is *more* sensitive to low values (e.g., H(0.1, 0.9) ≈ 0.18 vs. arithmetic mean 0.5), meaning a low value *does* dominate. The choice of harmonic vs. arithmetic or geometric mean is never justified empirically or mathematically. This does not invalidate the metric (the choice may still be reasonable), but the stated reasoning is incorrect. (Section 3.3, line 61)

- **Correlation type ambiguously reported.** The introduction states that "Kendall τ correlation coefficients" are computed (line 16), but Section 4.3 (lines 172–180) simply refers to "correlation" without specifying the coefficient. The reported values (e.g., 0.4657, 0.4213) could be Pearson's r or Kendall's τ, which have different interpretations. No confidence intervals or bootstrap estimates are provided, which is particularly important given the small human evaluation set (100 points, 5 raters). (Section 4.3)

- **Limited experimental scope.** Validation covers only two methods (LFCBM, PHCBM) and three datasets (CIFAR-10, CIFAR-100, CUB200). While acceptable for a first metrics paper, the claim of filling "a critical gap" (abstract, line 4) would be strengthened by including additional unsupervised CBM variants (e.g., PCBM already described in related work, CEM). (Sections 4.1–4.2)

- **NLP metrics inclusion lacks justification.** BLEU, METEOR, and ROUGE show low correlations with human judgment (0.29–0.31, Section 4.3.1, line 176) and are described only as "complementary." The paper does not discuss what value these metrics add or why they underperform ConceptScore/Ref-ConceptScore. (Sections 3.4, 4.3.1)

### Trivial

- The abstract and introduction emphasize evaluation "without ground-truth labels," yet Ref-ConceptScore and the NLP metrics require ground-truth concepts. A clearer delineation of which metrics apply in unsupervised vs. supervised settings would avoid misleading framing. (Abstract, line 4; Sections 3.3–3.4)

## Nice-to-Haves

- An ablation comparing LongCLIP vs. standard CLIP for ConceptScore would help justify the model choice and show whether the longer context capability matters for concept evaluation.
- A comparison of harmonic vs. arithmetic vs. geometric mean for Ref-ConceptScore would either validate or simplify the design.
- Reporting bootstrap confidence intervals for all correlation estimates, especially given the small human evaluation sample, would increase confidence in the results.

## Removed Points

The following points from the reviewers are removed or downgraded per the verification rules:

- **Critical Issue 4 — "score should remain the same if only order changes"**: The paper states that both order *and weights* were altered (line 209), so the reviewer's specific claim that "the average ConceptScore across images should remain the same" ignores the weight modification. The underlying concern about unclear description is valid and kept above in Major weaknesses; the stronger technical claim is removed as a partial misreading.

- **Strength Finder — "Integration of established NLP metrics with visual grounding"**: This strength conflicts with the verified weakness that NLP metrics show low correlations and lack justification. Per the rule "when a strength and weakness disagree, the weakness wins," this strength is removed.

- **Harsh Critic's "ω doesn't affect correlations" nuance**: While the critic correctly identifies ω as unspecified, the implied severity is reduced because ω is a uniform scaling factor and therefore does not affect correlation coefficients (the paper's main validation evidence). This nuance is noted in the Minor weakness above.

- **Criticism about "no baseline comparisons" framed as fatal**: Downgraded from the critic's implied severity to Major. The paper does provide implicit baselines (NLP metrics score lower), and the lack of a random baseline is a significant gap but does not invalidate the core result.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that goes deeper than what the authors already present (the core idea of using cross-modal similarity for unsupervised CBM evaluation is straightforward, and the reviews' main value is in identifying gaps in validation and presentation).

## Suggestions

1. **Define all experimental parameters.** Specify ω's value, provide at least one example of the prompt template 𝒫(·), and define what "Prompt1" and "top 5 combinations" refer to. Without these, the experimental results in Tables 1–2 are unusable.
2. **Add baseline comparisons.** Compute the correlation of a trivial baseline (e.g., assigning random uniform scores, or average concept embedding similarity without weighting) against human judgments to calibrate whether the reported 0.42–0.47 correlations are meaningful.
3. **Clarify the sensitivity experiment.** Precisely describe what was manipulated (concept identities? weights? both?), and show a cleaner perturbation: replacing one concept with a clearly unrelated one and measuring the score change. Also verify that reordering concept–weight pairs for the *same* image without changing content leaves the score unchanged.
4. **Correct the harmonic mean justification** or replace it with an empirical argument for why harmonic (rather than arithmetic or geometric) mean is the appropriate aggregation for Ref-ConceptScore.
5. **Specify which correlation coefficient** was used in Section 4.3 and report confidence intervals or bootstrap estimates.

## Score and Decision

The paper addresses a genuine problem and proposes a sensible, straightforward approach. ConceptScore is a reasonable use of cross-modal alignment for concept evaluation, and the moderate correlations with human judgment signal that the approach has potential. However, the paper is weakened by several issues that prevent acceptance in its current form: undefined key terms ("Prompt1," ω, prompt template) that make the experimental results uninterpretable, missing baseline comparisons that leave the correlation magnitudes uncalibrated, an ambiguous sensitivity analysis, and a contradictory justification for the harmonic mean. These are fixable, but they collectively undermine the paper's ability to convincingly demonstrate the framework's value and reproducibility.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>