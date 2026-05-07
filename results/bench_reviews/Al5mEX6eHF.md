Now I have a thorough understanding of the paper. Let me verify the harsh critic's key claims:

1. **"Cannot advance" overclaiming**: The title says "Explainable AI Cannot Advance Without Better User Studies." The paper does acknowledge XAI has produced useful tools for ML practitioners (Section 5, line 304), and that functional evaluation has a role in prototyping (line 312). However, the paper also addresses this in its "Alternative Views" section (line 302-310), explicitly considering the "XAI is still progressing" counterargument and responding that progress for ML practitioners doesn't equal progress toward societal desiderata for end-users. This is a genuine position paper rhetorical move — provocative but internally consistent. Per my rules, I should REMOVE the "overclaim" criticism about the title.

2. **Missing transition plan**: The paper acknowledges expertise is low (line 328) and proposes a dedicated venue (line 330) as part of the solution. But it doesn't lay out a clear transition path. This is a real gap, though it's somewhat outside the paper's stated scope (which is about establishing the position, not implementing it).

3. **Output-type incompatibility underdeveloped**: Confirmed — it's one paragraph (line 300). This is a genuine structural observation, and it IS underdeveloped.

4. **Reproducibility vs. validity**: The paper treats reproducibility as a proxy for quality, but conflates "enough detail to reproduce" with "well-conducted study." This is a valid concern.

5. **Practitioner-developer niche**: The paper does address this (line 304, line 310), acknowledging ML practitioners are often the target user, but argues we still have "little to no understanding" of why/when XAI is useful for non-practitioners. This is partially addressed.

6. **Better functional evaluation**: Not addressed explicitly. Could reduce urgency of user studies.

7. **Regulatory compliance**: Not addressed. The paper mentions "legislative oversight" in passing but doesn't engage with compliance-driven evaluation.

Now let me finalize my review.

## Summary

This position paper argues that XAI cannot advance without substantially better user studies, supported by two premises: (1) user studies are essential because XAI's end goal is satisfying societal desiderata that require human subjects to evaluate, and (2) the current state of user studies is remarkably poor, as demonstrated by an empirical analysis of 607 XAI papers showing low reproducibility, minimal fidelity, and methodological shortcomings—especially at top ML venues.

## Strengths

- **Large-scale empirical evidence backing the position.** The analysis of 607 XAI papers provides concrete, quantitative support. The finding that top-4 venue user studies have ~15% reproducibility versus 50-90% for other venues (Figure 4) is a striking, counterintuitive result that directly supports the claim that prestigious ML venues tolerate low methodological standards for user studies.

- **Novel structural argument about functional evaluation's comparability limitation.** Section 5 identifies that functional evaluation cannot compare XAI methods with different output types (e.g., feature importance vs. counterfactuals vs. heatmaps), because the presentation is an integral part of the method. This is a non-obvious structural argument that goes beyond the standard "subjective vs. objective" framing and explains *why* there is no adequate substitute for user studies when comparing across explanation paradigms.

- **Compelling placebo effect argument.** Section 3.4 synthesizes evidence that placebo explanations invoke similar perceived trust as real explanations (Eiband et al., 2019; Kosch et al., 2023; Villa et al., 2023), while noting that no XAI user study presenting a novel explanation has used a placebo-control group. This directly challenges the validity of the existing evidence base.

- **Synthesis of proxy-to-real-world disconnect.** Section 3.3 compiles multiple studies (Hase & Bansal, 2020; Buçinca et al., 2020; Amarasinghe et al., 2024) showing that proxy tasks and subjective measures do not predict actual downstream performance, undermining the rationale for relying on functional evaluation as a substitute.

- **Honest engagement with counterpositions.** Section 5 directly addresses the strongest counterarguments—functional evaluation's supposed objectivity, and the view that XAI is advancing anyway—rather than straw-manning them. The acknowledgment that functional evaluation has a legitimate prototyping role (line 312) prevents the position from being dismissed as absolutist.

## Weaknesses

### Fatal
None.

### Major

- **The output-type incompatibility argument—arguably the paper's strongest structural contribution—is underdeveloped.** This insight (line 300) receives only a single paragraph, yet it provides a principled reason why functional evaluation alone is insufficient: it cannot compare across explanation paradigms. This could have been a centerpiece of the paper, systematically demonstrating how Nauta et al.'s ~100 functional metrics are each tied to a specific output type and therefore cannot serve as a common yardstick. As presented, readers may not appreciate its significance, and the argument lacks the depth its importance warrants.

- **Reproducibility is conflated with study quality in the empirical analysis.** The paper treats low reproducibility as evidence that user studies are poor (e.g., line 202-203, line 326), but reproducibility measures whether sufficient methodological detail is provided for replication, not whether a study's conclusions are valid. A well-conducted study can be poorly documented (low reproducibility) while a trivially designed study can be easily reproduced. This distinction matters because the remedy for "studies lack detail" (better reporting) is different from the remedy for "studies are poorly designed" (better methodology). The paper treats both as requiring "higher methodological standards," but these are different problems that may require different solutions. The paper does not clearly distinguish them.

### Minor

- **The transition from "raise standards" to "better studies exist" is underspecified.** The paper acknowledges low community expertise in user studies (line 328) and proposes a dedicated venue to build that expertise (line 330), which is constructive. However, if standards are raised immediately and most studies fail to meet them—as the paper documents—there will be a gap period with very few publishable user studies. The paper does not discuss this transition challenge explicitly, though it's partially implied by the venue proposal.

- **Insufficient engagement with the practitioner-as-user niche.** The paper acknowledges ML practitioners are often the target users of their own tools (line 304), and responds that we still lack understanding of XAI's value for non-practitioner users (line 310). But if a substantial portion of XAI's real-world value comes from practitioners using tools they develop for themselves—a niche where functional evaluation may be more directly informative—the urgency of end-user studies for general XAI advancement is somewhat diminished. The paper could have more thoroughly analyzed how large this niche is and its implications for the position's strength.

### Trivial
None.

## Nice-to-Haves

- It would strengthen the paper to systematically develop the output-type incompatibility argument with examples showing which comparisons are rendered impossible across explanation paradigms, rather than stating the limitation in one paragraph.

- The paper could briefly engage with regulatory-driven evaluation (e.g., EU AI Act compliance requirements) as a possible future driver that might push the field toward compliance-oriented evaluation rather than user studies, regardless of the authors' preference.

- The paper could briefly discuss whether improved functional evaluation metrics (better correlations with downstream performance) could reduce the urgency of user studies for some purposes, even if they cannot fully replace them for societal desiderata evaluation.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Cannot advance" overclaiming criticism.** The harsh critic argues the title's "cannot advance" framing is stronger than the argument supports, because the paper acknowledges XAI has produced useful tools for ML practitioners and that functional evaluation has a role. However, for a position paper, provocative framing is a feature, not a flaw. The paper explicitly addresses this counterargument in Section 5 (lines 302-310), responding that progress measured by adoption doesn't equal progress toward the societal goals that define XAI's purpose. The remaining gap—the paper grants ML practitioners are sometimes the target user—is handled in the paper's own terms. The "overclaim" criticism treats a strong rhetorical frame as a factual error, but the argument is internally consistent.

- **Criticisms demanding empirical validation, baselines, or ablations.** Position papers argue from reasoning and evidence; they do not need to empirically prove every claim.

- **Missing appendix / missing proofs criticism.** Per rules, the parser strips appendices.

- **Missing related works.** Per rules, I cannot verify external references.

## Novel Insights

The paper's most novel contribution is the structural argument that functional evaluation has a fundamental comparability limitation—it cannot serve as a common yardstick across XAI methods with different output types (heatmaps vs. feature importance vs. counterfactuals vs. text). This reframes the user-studies-vs-functional-evaluation debate from the tired "subjective vs. objective" framing to a more precise argument about what functional evaluation structurally cannot do. This insight, if developed more fully, could reshape how the community thinks about evaluation design in XAI.

## Suggestions

- Expand the output-type incompatibility argument (Section 5, line 300) into a standalone subsection with concrete examples: show which pairs of XAI methods cannot be compared via any existing functional metric, and explain why user studies are the only evaluation that can provide cross-paradigm comparisons (because users can judge which explanation helps them more regardless of modality).

- Clearly distinguish reproducibility (reporting detail) from study quality (methodological rigor) in the empirical analysis and recommendations. Different failures need different remedies: better reporting standards vs. better study design standards.

- Add a brief paragraph in Section 6 discussing the transition challenge: if standards are raised as recommended, how should the community handle the near-term reduction in publishable user studies while expertise is being built?

## Score and Decision

**Calibration anchors:**

- **High-scoring anchors (≥6):** `yqKfMr0yvY` (avg 7.67, LLM-as-judge validity critique using measurement theory, Accept), `R5uuqCAPf8` (avg 6.33, AI-generated survey DDoS with empirical evidence, Accept Oral), `vFae5rRman` (avg 6.0, benchmarking is broken with PEERBENCH proposal, Accept), `dl5pvd5IgW` (avg 8.0, AI-for-social-impact evaluation reform, Accept), `5X4GDSUumr` (avg 7.0, time series benchmark reform with 3500+ networks, Reject). This paper is comparable to these in having a clear position + large-scale empirical evidence + structural argument. It's weaker than the measurement-theory paper (yqKfMr0yvY) which has a more sophisticated theoretical framework, but comparable to the survey-DDoS paper (R5uuqCAPf8) which also combines empirical analysis with a call for reform. It's stronger than the benchmarking paper (vFae5rRman) in the quality of its empirical evidence (607 coded papers vs. no systematic coding).

- **Medium-scoring anchors (~5):** `0TRVB5ghCR` (avg 5.0, XAI plausibility critique, Reject), `8ZH52QHIZV` (avg 5.33, XAI paradigm critique, Reject), `iOSHFKHQNP` (avg 5.67, evaluation methodology, Reject). This paper is clearly stronger than these—it has far more empirical support, clearer argumentation, and avoids the "framework without implementation" problem that plagued these medium-scorers.

- **Low-scoring anchors (≤4):** `FJF1sa6elQ` (avg 3.33, evaluation crisis with five-tier framework, Reject). This paper is far above this level—it has real empirical evidence, not just a conceptual framework, and its position is clearly stated and well-argued rather than vague.

This paper sits clearly above the medium-scoring XAI evaluation papers (~5-5.5) and somewhat below the top-scoring evaluation reform papers (~7-8). Its empirical analysis of 607 papers is a substantial contribution that most position papers lack, and its structural argument about functional evaluation is genuinely novel. Its main weakness is the underdevelopment of its strongest structural argument and some conflation of reproducibility with quality. Compared to the 6.33 scoring survey-DDoS paper (which also had empirical trend analysis + reform call + concrete proposal), this paper has similarly strong empirical backing and similarly important structural insights, but is somewhat less polished in argumentation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>