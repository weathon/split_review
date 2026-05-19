- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This survey paper addresses uncertainty in Large Language Models (LLMs). It proposes a taxonomy distinguishing *operational uncertainty* (arising from data, model, alignment, and inference processes) from *output uncertainty* (pertaining to the quality and evidential grounding of generated text), provides standardized definitions for uncertainty/confidence/reliability, reviews four families of estimation methods (logit-based, consistency-based, self-evaluation, internal-based) with a comparative table, and outlines future research directions.

## Strengths

1. **Clear, well-motivated definitions of uncertainty, confidence, and reliability (Section 2).** The paper distinguishes these often-conflated terms with concrete examples (lines 56–58: "How many planets are in the universe?" as a known unknown, speculative historical counterfactuals). This provides a useful conceptual foundation for the field.

2. **Lifecycle-based framework (Section 3) that organizes uncertainty sources differently from the traditional aleatoric/epistemic/distributional tripartition.** The framework traces uncertainty through pre-training/training (data uncertainty, model uncertainty), instruction tuning/alignment (annotation inconsistency, guideline interpretation), and inference (distributional uncertainty, sampling/decoding strategy), then separately addresses output uncertainty about generated content quality. This organization is genuinely distinct from existing taxonomies in the literature and offers stakeholder-specific insight (developers, users, administrators).

3. **Systematic identification of limitations across four method families (Section 4).** The paper clearly articulates why each family fails to identify uncertainty sources: logit-based methods confound linguistic form with correctness, self-evaluation suffers from circular reasoning, internal-based methods lack transferability, etc. Table 1's explicit "Identifying Sources: No" for all four methods drives home a key gap.

## Weaknesses

### Major

1. **The claimed novelty and superiority of the operational/output framework is asserted but not demonstrated.** Section 3.1 states that traditional categories "fail to fully address the unique challenges of LLMs" (line 77) and "cannot be adequately addressed by simply categorizing uncertainty into three traditional types" (lines 77–78). However, the paper never provides a concrete case where applying the traditional aleatoric/epistemic/distributional taxonomy would lead to a wrong understanding or wrong decision that the new framework fixes. For instance, it does not show a side-by-side analysis of the same LLM output classified under both taxonomies, nor does it explain why the output uncertainty category (lack of supporting evidence, contradictory knowledge) cannot be accommodated within an extended notion of epistemic or distributional uncertainty. Without such grounding, the framework reads as a useful reorganization rather than the "first comprehensive" advance claimed in Contribution 2 (line 29). This weakens the paper's central thesis.

2. **Table 1 makes subjective comparative claims without empirical support.** The table assigns ordinal ratings ("High"/"Low"/"Very Low"/"Mid") for properties including "Accuracy," "Transferability," and "Explainability" across four method families, but provides no experimental data, meta-analytic evidence, or even a worked example justifying these ratings. The caption states the labels are "relative to the other approaches and based on the general idea behind them" (line 204), which is an admission of subjectivity. Presenting these as a structured comparison table gives a false veneer of quantitative rigor. A survey can compare methods qualitatively without ordinal labels, or it can cite published results; this table does neither, and its inclusion undermines the credibility of the review.

### Minor

1. **Method descriptions in Section 4 are accurate but shallow.** Each family receives roughly one paragraph. The discussion of logit-based methods correctly identifies the vocabulary-space vs. truth-content mismatch but does not discuss how severe this mismatch is in practice (the cited works are named but no experimental comparisons or error analyses are reproduced). Consistency-based methods are discussed without depth on how the consistency measurement challenge has been addressed in recent work (e.g., semantic equivalence clustering). Internal-based methods are covered with only one primary reference (Beigi et al., 2024) and a few related approaches. For a paper aiming to be a "comprehensive survey," the method review lacks the depth needed for practitioners to make informed choices.

2. **Future directions (Section 5) are generic.** The five identified gaps—going beyond confidence, explainability, ground truth, transferability, standardized evaluation—are widely acknowledged deficiencies in the field. The paper does not propose concrete next steps such as specific new metrics, benchmark designs, or validation strategies that would distinguish this survey's agenda from others'.

3. **Reliability is defined narrowly as calibration (Section 2).** The paper equates reliability with aligning confidence scores to actual correctness probabilities (line 54: "a process known as calibration"). Reliability in the context of LLMs is broader, encompassing factual correctness, consistency with evidence, robustness to input variation, and safety. While the paper is free to adopt a working definition, the narrowing is not justified.

### Trivial

None.

## Nice-to-Haves

- A systematic description of how papers were located, the time span covered, and any selection criteria would strengthen the survey's comprehensiveness claim.
- The relationship between "output uncertainty" and hallucination detection merits explicit discussion, as the two concepts (lack of supporting evidence, contradictory knowledge) overlap substantially.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Missing related works" (Bayesian inference for LLMs, conformal prediction, ensemble methods).** This criticism cannot be independently verified without full knowledge of the literature, and the paper covers four major method families. Per guidelines, this is removed.

2. **"No systematic search strategy / lack of methodological rigor as a survey."** The paper frames itself as a "critical review and analysis" (line 29), not a PRISMA-style systematic review. This is a style choice rather than a flaw, and many survey papers in this field do not report a formal search protocol.

3. **Criticism that the logit-based section "cited no experiments" for the vocabulary-space mismatch.** The paper does cite Lin2022, si2022, and tian2023 (line 169) in support of this claim. While it does not reproduce their quantitative results, the criticism as originally phrased was factually incorrect about the absence of citations.

## Novel Insights

None beyond the paper's own contributions. The two reviews present no observations that fundamentally reshape understanding of the paper beyond what is evident from reading it.

## Suggestions

1. **Provide a concrete failure case** — take a specific LLM query, show how the aleatoric/epistemic/distributional taxonomy would classify the uncertainty, show why that classification is insufficient or misleading, and then show how the operational/output taxonomy yields better insight. This would transform the framework from a restatement into a demonstrated advance.

2. **Replace or substantially revise Table 1.** Either remove the ordinal ratings and keep only categorical/comparative information that is directly supported by cited evidence, or ground each rating in published experimental results (e.g., "Logit-based methods achieve an AUC of X on correctness prediction tasks [ref], which is lower than internal-based methods achieving Y [ref]"). If the available literature does not support such comparison, the table should not imply quantitative ranking.

3. **Expand the method review** to at least ~2 pages per family, including representative algorithms, strengths illustrated by published results, and specific failure modes with examples. Consider adding a subsection on evaluation metrics (Brier score, AUC for correctness prediction, semantic entropy) with critical comparison.

4. **Make one future direction concrete** (e.g., propose a specific benchmark design or metric) to distinguish the paper's agenda from generic calls for more research.
