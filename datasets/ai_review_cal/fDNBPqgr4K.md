- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces CogDevelop2K, a benchmark of 2,519 questions (with images and videos) spanning 12 cognitive sub-concepts mapped to Piaget's four developmental stages (sensorimotor through formal operational). The authors evaluate 46 MLLMs and report that advanced models perform better on complex formal operational concepts (e.g., tool using, intention understanding) than on simpler sensorimotor concepts (e.g., object permanence, spatiality) — a pattern they describe as "reversed cognitive development" compared to humans. They also investigate 11 prompting strategies and include a human baseline with 22 participants.

## Strengths

- **Theory-grounded benchmark design**: The 12 sub-concepts are explicitly mapped to Piaget's developmental stages (Fig. 1), providing a principled theoretical framework. This distinguishes CogDevelop2K from prior task-focused benchmarks and enables the investigation of whether MLLMs exhibit a structured developmental trajectory — a novel and worthwhile question.

- **Novel multi-frame interleaved question format**: The paper introduces a format combining images, videos, and text in a single question (842 multi-frame questions in total) that simultaneously tests co-reference, temporal understanding, and reasoning (Section 2.5). This is a genuine methodological contribution beyond standard benchmarks.

- **Broad model coverage**: Evaluating 46 MLLMs with 11 prompt variations (Table 2) provides a comprehensive picture. The finding that concept-explanation prompts boost accuracy by up to 8.1% but do not eliminate the reversal pattern is a useful empirical observation.

## Weaknesses

### Major

- **Insufficient quantitative support for the headline "reversed development" claim**: The paper's central finding — that MLLMs show a reversed developmental trajectory — is supported in the text only by broad accuracy ranges for GPT families (sensorimotor 0.4–0.6, concrete operational 0.2–0.4, formal operational 0.6–0.8, as stated on page 7 lines 187–188). The paper does not provide (a) a per-sub-concept accuracy breakdown for all 46 models, (b) any statistical test (e.g., interaction test between model family and stage complexity), or (c) confidence intervals or variance estimates for any model. The reader must rely entirely on visual inspection of figures whose details are not described in prose. For a paper that stakes its main contribution on this reversal claim, this level of evidence is insufficient.

- **Unaddressed modality confound**: The paper does not report which question formats (single-image, single-video, multi-video, image-video interleaved) are used for each sub-concept or developmental stage. Sensorimotor concepts (object permanence, continuity, spatiality) may naturally require more video-based questions, while formal operational concepts may use more static images or text-heavy scenarios. Since many MLLMs are weaker on video understanding than on image understanding, the observed "reversal" could be an artifact of the modality distribution rather than a genuine dissociation in cognitive capabilities. This confound must be ruled out for the central claim to be credible.

- **Human baseline has significant methodological limitations**: The human baseline (22 college students) counts skipped questions as failures, with no analysis of skip rates or why participants skipped (page 7, line 147). No variance across participants, no inter-annotator agreement, and no per-concept human accuracy breakdown are reported. The 95% correctness threshold (line 104) refers to reviewer screening of questions, not to human participant performance. While the inclusion of any human baseline is commendable, the current one is too weak to serve as a reliable anchor for the "reversed trajectory" claim.

### Minor

- **Construct validity of benchmark is unverified against developmental norms**: The benchmark's 12 sub-concepts are grounded in Piagetian theory and defined with references, but there is no validation that the specific questions actually measure the intended constructs (e.g., that children at the expected developmental stages systematically succeed or fail on these items). No pilot testing, item analysis, or difficulty calibration is described. This weakens confidence in the benchmark's diagnostic power, though it does not invalidate the empirical observations.

- **Results section focuses almost exclusively on GPT models**: Despite evaluating 46 models, the prose discussion of the reversal pattern only covers "GPT families." No comprehensive table showing all 46 models' performance across the 12 sub-concepts is provided. This makes it difficult to assess how widespread the reversal pattern is across model architectures.

### Trivial

- The paper has a minor numerical inconsistency: the abstract and conclusion say "46 MLLMs" while the Results section (line 187) says "48 Multi-modal Large Language Models" — likely a typo.

## Nice-to-Haves

- **Per-concept modality breakdown**: Reporting which question formats are used for each sub-concept would be straightforward from existing data and would help rule out the modality confound.
- **Statistical test for the reversal**: A simple interaction test (model × stage) or a comparison of mean accuracy across stages with confidence intervals would significantly strengthen the main claim.
- **Full results table**: A table showing all 46 models × 12 sub-concepts (even in supplementary) would improve transparency.

## Removed Points

- **"No dataset release URL or license"** (Harsh Critic): Noted the absence of a release URL for a benchmark paper. However, this is an anonymous conference submission; omission at this stage is standard practice. The paper cites its data sources (Wikipedia, Reddit, Physion, etc.) and describes the curation process. Not a genuine weakness.

- **"Human baseline is a strength"** (Strength Finder #5): The inclusion of a human baseline is noted, but given the methodological issues confirmed by the paper text (counting skips as failures, small sample, no variance reporting), this conflicts with a verified weakness. Per the rule, the weakness wins — the baseline exists but is not a strength in its current form.

- **"Reversed developmental trajectory finding as a strength"** (Strength Finder #1): The observation is presented in the paper, but since the evidence for it is insufficiently rigorous (see Major weaknesses), retaining it as an unqualified strength would be misleading. The finding is better characterized as a provocative but insufficiently supported observation.

- **"Recruit children of known developmental stages"** (Harsh Critic's "Strengthening the Paper"): This is a significant scope expansion beyond what a conference paper on MLLM evaluation should be expected to do. A reasonable suggestion for future work, not a weakness of the current paper.

- **Criticisms about missing appendix content**: The PDF parser strips appendices from all papers; any proofs or supplementary material likely exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide a complete results table** showing accuracy for all 46 models across all 12 sub-concepts, with variance estimates (e.g., standard error across questions, or bootstrapped confidence intervals).

2. **Include a modality-by-stage breakdown** to address the confound concern directly. Show that the reversal persists when controlling for question format (comparing only single-image questions across stages, only video questions, etc.).

3. **Add statistical support for the reversal claim** — at minimum, report mean accuracy and standard errors per stage per model family, and run a simple interaction test (Stage × ModelFamily) to quantify whether the pattern differs from the human trajectory in a statistically meaningful way.

4. **Improve the human baseline documentation**: report per-concept human accuracy with variance, analyze skip rates, and consider whether participants who skip many questions should be excluded rather than counting skips as failures.
