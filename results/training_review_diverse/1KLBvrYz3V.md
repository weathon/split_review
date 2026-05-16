Here is my consolidated review.

---

## Summary

Century is a dataset and benchmark paper that presents (1) a scalable methodology combining knowledge graphs and LLMs to mine Wikipedia for 1,500 sensitive historical images, (2) the Century dataset itself, and (3) a reference-free evaluation protocol measuring historical contextualisation along accuracy, thoroughness, and objectivity. The paper demonstrates the approach by evaluating four foundation models, finding that none exceed ~57% on any dimension, indicating the task remains challenging for current systems.

## Strengths

- **Scalable, reproducible dataset construction methodology.** The pipeline combining knowledge graph queries (7,385 search terms) with LLM-generated candidate page titles (1,297 unique titles) to mine 37.8M WIT records is novel and reproducible. The low overlap between two foundation models' outputs (15.1%) validates the value of combining automated sources. This method goes beyond manual curation and offers a template for future dataset construction in other sensitive domains.

- **Empirical evidence that historical contextualisation is challenging for current models.** Both automated and human evaluation (n=378 ratings) show that four state-of-the-art models (GPT-4 Omni, Claude Opus, Gemini 1.5 Pro, Gemini 1.5 Flash) achieve at most ~57% "agree or higher" on accuracy/thoroughness/objectivity (Table 3). This concrete finding validates Century's utility as a challenging benchmark and motivates further work on socio-cultural understanding in vision-language models.

- **Convergent quality validation from both human and automated raters.** The paper reports quality labels from 151 crowd-workers and six labeller models. The finding that 90.9% of images are rated "somewhat sensitive" or higher by at least one human rater, with broadly similar aggregate patterns from automated labellers, provides convergent evidence that the dataset captures sensitive content. Releasing all quality and diversity labels enables disaggregated analysis and future work on measurement in this domain.

- **Transparency about limitations and strong ethics practices.** The paper openly discusses over-representation of North America/Western Europe, lack of targeted community inclusion, risks of generative labelling for non-majoritarian perspectives, and the context-free nature of the evaluation. The ethics statement is well-considered (linking to images rather than hosting, providing blurring/skip mechanisms for annotators).

## Weaknesses

### Fatal

None.

### Major

- **The evaluation protocol for historical contextualisation lacks validation against expert human judgement.** The paper proposes accuracy, thoroughness, and objectivity as evaluation dimensions, and uses LLM-as-judge with ensembling. However, the protocol is never shown to produce ratings that correspond to human expert (e.g., historian or curator) assessment of description quality. The human evaluation (63 images, 3 crowd-worker ratings per response) is small and uses non-expert raters, making it insufficient as validation. No inter-rater agreement statistics are reported for either human or automated evaluations (CrowdTruth metrics are mentioned but results are not shown). Without evidence that the automated ratings measure what they claim, the model results in Table 3 are difficult to interpret as meaningful assessments of historical contextualisation quality.

- **No baseline or "chance-level" comparison for model evaluation.** The paper reports absolute percentages (e.g., GPT-4 Omni scoring 56.5% on accuracy) but provides no baseline — not even a simple heuristic like a model instructed to provide only a visual description without historical context, or a random baseline. This makes it impossible to calibrate whether 56.5% represents poor, adequate, or good performance relative to a reasonable floor. The claimed difficulty of the benchmark would be substantially strengthened by showing that even trivial approaches perform worse than the weakest tested model.

- **Construct definition of "sensitive historical image" is underspecified.** The paper identifies four root themes (conflict, oppression, discrimination, reform) and four image types (events, organizations, people, locations) through an interdisciplinary review, but never provides a tight operational definition of what makes an image "sensitive" versus merely "historical." The rating task asks annotators to judge sensitivity without a shared definition or calibration examples. The fact that 90.9% are rated "somewhat sensitive or higher" by at least one rater — while 55.8% have a *mean* rating at that level — suggests the construct boundaries are porous and rater-dependent. For a dataset that aims to carve out a specific evaluation space, clearer construct boundaries are needed.

### Minor

- **The "completeness" set of 128 images (8.5%) is not explained.** The paper states that these are included "for completeness" but gives no description of what they are, how they were selected, or why they are not covered by the KG or LM methods. This is a small but notable gap in the dataset documentation.

- **Downsampling criteria from 7,385 search terms to 1,500 images are not fully specified.** The paper states that images from the KG method were "downsampled" to reach the 1,500 target, but does not describe the sampling strategy (random? stratified by theme/region? representative?). This matters for understanding potential biases in the final dataset.

- **No confidence intervals or uncertainty estimates for model comparisons.** The paper reports point estimates in Table 3 without confidence intervals, bootstrapped estimates, or significance tests. Given the small human evaluation sample (63 images) and variance across automated labellers (differences up to 30 percentage points), uncertainty quantification would substantially strengthen the reliability of findings.

- **The context-free evaluation protocol is tested in only one prompt format.** The paper acknowledges that context-free evaluation is a limitation and recommends comparing context-free and context-driven protocols, but all reported results use a single prompt format. LLM responses are known to be sensitive to prompt wording, so this narrow operationalization limits generalizability.

### Trivial

- The sentence about CrowdTruth metrics (line 63) appears truncated with a dangling citation. This is likely a parser artifact, but the authors should ensure the full text is present in the original submission.

## Nice-to-Haves

- **Expert validation of a held-out subset.** Recruiting historians or museum curators to rate a subset of images for historical sensitivity and to evaluate model responses would dramatically strengthen both the dataset's construct validity and the evaluation protocol's credibility. This is the single highest-leverage improvement.

- **Baseline comparisons.** Adding even a simple baseline (e.g., instructing a model to describe visible content only, or a rule-based keyword extraction method) would help calibrate the difficulty of the benchmark and make the evaluation results more interpretable.

- **Decomposition of "sensitivity" into sub-constructs.** Breaking sensitivity into dimensions such as graphicness, controversiality, and representational harm potential would provide richer characterization of the dataset and enable more targeted evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that the paper does not provide exact prompting/rubrics for LLM judges.* The paper references Appendices B–G for details on reproducibility; the exact prompts are likely in the stripped appendix.
- *Criticism that Section 2 (Related Work) does not ground historical contextualisation in broader literature.* The parser stripped this section; the original submission contains it.
- *Criticism that mean ratings per image are not reported.* The paper states "3 ratings for each image" (line 62), so this is factually incorrect.
- *Criticism about "self-enhancement bias" discussion being cut off.* This is a parser artifact; the original submission contains the full sentence.

## Novel Insights

The most interesting observation to emerge from reading the reviews against the paper is that the reviewers converge on a tension the paper itself partially acknowledges but does not fully resolve: the paper's greatest strength — its fully automated, scalable pipeline for sourcing sensitive historical images — is also the source of its greatest vulnerability. Because the pipeline is entirely automated (KG + LLM queries matched against WIT), the construct of "sensitive historical image" is defined by *what the pipeline retrieves* rather than by an independently validated criterion. The human and automated sensitivity ratings then become circular to varying degrees: they confirm that the retrieved images are indeed sensitive, but they cannot confirm that the pipeline didn't miss important categories or include borderline ones. This tension is not unique to this paper — it is a structural challenge for any large-scale automated dataset construction — but the paper would benefit from explicitly addressing this circularity and proposing a strategy (e.g., a targeted expert review of pipeline failures and edge cases) to break it.

## Suggestions

- Conduct a small expert validation study (50–100 images rated by 2–3 historians or museum curators) to establish that the automated pipeline's construct of "sensitive historical image" aligns with expert judgement. Even a modest study would substantially strengthen the validity argument.
- Add a simple baseline to the model evaluation — e.g., a "literal description only" prompt that instructs the model to describe visual content without historical context — and show that it scores lower than the evaluated models on accuracy, thoroughness, and objectivity.
- Report inter-rater agreement metrics (e.g., Fleiss' kappa for human raters, pairwise agreement for automated labellers) to characterize the reliability of all reported quality and evaluation labels.
- Clarify the "completeness" set of 128 images and the downsampling procedure for the 7,385 KG-derived search terms.

## Score and Decision

This paper tackles an important and underserved evaluation need. The scalable methodology for dataset construction is a genuine contribution, and the empirical finding that all tested models struggle on this task provides useful evidence for the community. However, the paper currently suffers from two interrelated weaknesses that undermine confidence in its central claims: the evaluation protocol is not validated against any external (especially expert) standard of description quality, and there is no baseline to calibrate the reported model scores. Additionally, the construct of "sensitive historical image" is operationalized but not rigorously bounded. These issues are fixable, but they require non-trivial additional work (expert validation, baseline experiments) that cannot be fully resolved in a rebuttal. The paper also has several smaller documentation gaps (completeness set, downsampling procedure, inter-rater agreement).

On balance, the dataset and methodology are valuable enough that the paper merits revision and resubmission rather than outright rejection, but in its current form the evidence does not fully support the claims of what the evaluation protocol measures.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>