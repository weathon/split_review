Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes an evaluation framework for unsupervised concept bottleneck models (CBMs), introducing ConceptScore and Ref-ConceptScore — metrics that use LongCLIP to measure alignment between images and predicted concepts. The framework also adapts NLP metrics (BLEU, METEOR, ROUGE) and validates against human judgments (n=100) and GPT-4v ratings. The core idea — applying CLIP-based alignment to CBM evaluation in a systematic way — addresses a genuine need in the field.

## Strengths

- **Addresses an under-explored evaluation gap**: Unsupervised CBMs lack standardized evaluation, and the paper targets this gap directly. The framework integrates multiple perspectives (cross-modal alignment, lexical overlap, human/LLM ratings) into a single assessment pipeline, which is practically useful for benchmarking future unsupervised CBM methods.

- **Empirical validation against human and LLM judgments**: The paper reports Kendall τ correlations between automatic metrics and human/GPT-4v scores (e.g., Ref-ConceptScore vs. Human: 0.4704; Ref-ConceptScore vs. GPT-4v: 0.5913) with Krippendorff's α=0.7405 among human raters. These provide initial evidence that the metrics capture something aligned with human perception.

- **Sensitivity analysis demonstrates basic responsiveness**: Replacing concepts with incorrect ones causes a measurable drop in ConceptScore (0.5625→0.3811) and Ref-ConceptScore (0.6958→0.5297), showing the metrics are not inert.

## Weaknesses

### Fatal
None. The paper's core agenda is sensible and the framework, while imperfect, is not fundamentally invalid.

### Major

- **Overclaimed novelty: ConceptScore is functionally identical to CLIPScore (Hessel et al., 2021).** The formula `ω·max(cos(image_embedding, text_embedding), 0)` is the same as CLIPScore's standard definition. The paper cites Hessel et al. (2021) in passing (Section 2.2) but presents ConceptScore as a novel metric without acknowledging this direct lineage or explaining what differentiates it. The novelty of this paper lies in the *application* of CLIP-based alignment to CBM evaluation and the *framework integration*, not in the metric formula itself. The current framing inflates the contribution and needs to be corrected.

- **Claimed evaluation dimensions (relevance, consistency, informativeness) are never operationalized.** The abstract and introduction state the framework assesses concepts along these three dimensions, but no metric is explicitly mapped to any of them. ConceptScore measures image–text alignment, Ref-ConceptScore adds concept–concept similarity, and the NLP metrics measure lexical overlap — none of these are labeled as "relevance," "consistency," or "informativeness." This creates a significant gap between the advertised scope and what is actually measured.

- **"Strong correlations" overstates the evidence.** The abstract and conclusion claim "strong correlations" / "strong certain alignments," but the actual Kendall τ values range from 0.29 to 0.59 — moderate at best. The paper's own discussion (Section 4.3.1) describes these as "moderate" (line 174, 176, 180), which contradicts the conclusion's "strong" characterization. This is a claim–evidence mismatch that inflates the contribution.

### Minor

- **The weight ω is introduced but never specified or varied.** ω appears in the ConceptScore formula (Section 3.2) and is described as "adjust[ing] the significance of the similarity score," but its value is never stated, nor is there any ablation showing its effect. If ω=1 always, it is redundant and should be removed.

- **"Top 5 combinations for Prompt1" is undefined.** Tables 1 and 2 are described as "the top 5 combinations for Prompt1," but neither "Prompt1" (what are the different prompts?) nor "combinations" (combinations of what? models, templates, concept sets?) is ever defined in the paper. This makes the experimental results difficult to interpret.

- **Sensitivity analysis is a single anecdotal example.** Section 4.6 reports score changes for one specific case (0.5625→0.3811). A single data point cannot demonstrate systematic sensitivity. Aggregate statistics across many examples, or at least several diverse case studies, are needed to validate that the metrics are generally responsive to concept quality.

- **Correlations reported without uncertainty quantification.** The Kendall τ values are reported as point estimates on only 100 samples (Section 3.5). No confidence intervals, p-values, or bootstrap estimates are provided. Given the modest sample size and moderate correlation magnitudes, it is unclear whether these would replicate.

- **No comparison against existing evaluation proxies.** For CUB200, where ground-truth concepts exist, the paper could compare ConceptScore/Ref-ConceptScore against concept accuracy (the standard metric in prior CBM work) to show how the proposed metrics relate to established ones. This would help contextualize the contribution.

- **No discussion of limitations.** The conclusion (Section 5) reiterates contributions but does not acknowledge limitations such as: CLIP/LongCLIP biases, the moderate correlation magnitudes, the small human evaluation sample, or the limited scope of the sensitivity analysis.

- **Redundant operation in Ref-ConceptScore formula.** Equation (66) contains `max(max(cos(...), 0), 0)` where the outer max is unnecessary after the first `max(..., 0)` clips to non-negative values. This suggests editorial sloppiness.

- **Baseline descriptions lack implementation specifics.** Section 4.1 describes CBMs, CEMs, LFCBMs, and PCBMs in generic terms but does not specify which exact implementations/checkpoints were used or how they were obtained/reproduced, making it difficult to replicate the evaluation.

### Trivial
None beyond what was already captured above.

## Nice-to-Haves

- Compare ConceptScore against standard CLIPScore (using vanilla CLIP vs. LongCLIP) to justify the design choice of LongCLIP.
- Provide bootstrap confidence intervals for all reported correlations.
- Release code, prompt templates, and exact concept sets used.
- Justify why lexical overlap metrics (BLEU, METEOR, ROUGE) are appropriate for concept evaluation when concepts can be semantically equivalent but lexically different.

## Removed Points

These points are flagged to be removed — treat them with caution.

- *"Tables 1 and 2 are embedded as images and unreadable"*: This is a PDF-extraction artifact. The original submission has these as proper images/tables; the parser cannot render them. The paper does provide some numerical results in text (e.g., LFCBM scores of 0.4767 and 0.4911). The substantive remaining concern — "top 5 combinations" being undefined — is kept in Minor.

- *"Missing related works"*: Removed per meta-instructions — I lack external sources to confirm whether additional related works exist or are missing. The paper does cite relevant CBM literature (Koh et al., Oikarinen et al., Yuksekgonul et al., Espinosa Zarlenga et al.) and Hessel et al.

- *"Missing appendix / proofs"*: Removed per meta-instructions — the parser strips appendix content; it exists in the original submission.

- *Strength: "Novel evaluation metrics"*: Moderated to reflect that ConceptScore is functionally CLIPScore. The strength of the paper is in the framework application, not metric novelty per se.

- *Strength: "Sensitivity analysis validates metric responsiveness"*: Kept in strengths but noted as based on a single example; the weakness section captures the limited scope.

## Novel Insights

None beyond the paper's own contributions. The key insight — that CLIP-based alignment can be systematically applied to evaluate concept quality in unsupervised CBMs — is useful but straightforward. The reviews do not surface any additional analytical or cross-community perspective that the paper itself does not already contain.

## Suggestions

1. **Reframe the contribution honestly.** Acknowledge that ConceptScore is an adaptation of CLIPScore applied to CBM evaluation, and explain what (if anything) is novel about the formulation. Drop the overblown "relevance, consistency, informativeness" framing unless you can explicitly map each metric to a dimension.

2. **Define all experimental variables.** Specify the value of ω, explain what Prompt1 and "combinations" refer to, and describe what prompt templates were used. Without these, the results are not interpretable.

3. **Add uncertainty quantification to the correlation analysis.** Report 95% confidence intervals (via bootstrap) for all Kendall τ values. Consider collecting more human judgments or justifying the power of n=100.

4. **Expand the sensitivity analysis.** Show aggregate statistics across many concept-replacement trials rather than a single case study. This would provide much stronger evidence that the metrics are systematically responsive to concept quality.

5. **Align the conclusion with the evidence.** The text currently claims "strong correlations" while the data shows moderate ones (0.42–0.59). Adjust the language to match what the results actually support.

## Score and Decision

This paper identifies a real problem and proposes a framework that is sensible in direction. However, the execution has multiple significant issues: the primary metric is an unacknowledged adaptation of CLIPScore, the framing claims dimensions that are never operationalized, the empirical validation is preliminary (moderate correlations on 100 samples, no confidence intervals, single-example sensitivity analysis), and key experimental details are undefined. These are not fatal — the framework could be useful after revisions — but the current version does not meet the threshold for acceptance at a competitive venue.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**