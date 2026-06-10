## Summary

MuirBench is a benchmark for multi-image understanding by multimodal LLMs, comprising 2,600 multiple-choice questions across 12 tasks and 10 relation categories, with a pairwise design where each answerable instance is paired with an unanswerable variant. Evaluations on 20 models show GPT-4o achieving only 68.0% and open-source models below 44.5%, highlighting the difficulty of multi-image reasoning and the gap between single-image-trained and multi-image-trained models.

## Strengths

- **Comprehensive multi-image coverage far exceeding prior work.** The benchmark spans 12 tasks and 10 multi-image relation categories with 2,600 questions, a substantial advance over Mantis-Eval (207 examples) and BLINK. The breadth is clearly documented in Section 3.1.

- **Pairwise unanswerable design is a thoughtful robustness mechanism.** The paper introduces a genuine methodological contribution by pairing each answerable instance with an unanswerable variant (via image replacement/reordering, question modification, or option modification). The observed accuracy drops (GPT-4o drops 26.8%, Gemini Pro drops 21.5%) provide evidence that the design detects shortcut-based guessing.

- **Empirical demonstration that multi-image training matters.** The comparison showing Mantis-8B (multi-image-trained) outperforming LLaVA-NeXT-34B (single-image-trained) is a concrete, evidence-backed finding that directly supports the paper's motivation (Section 4.2, line 187).

- **Diverse data provenance with quality control.** The benchmark draws from three sources (40.8% existing, 21.7% derived, 37.5% new) and applies both automatic checks and manual expert examination (line 145), which is more rigorous than benchmarks relying solely on automated conversion.

- **Fine-grained diagnostic labels** for image positions and image types beyond task/relation labels enable analyses prior multi-image benchmarks do not support (lines 115-117).

## Weaknesses

### Fatal
None.

### Major

1. **Human performance baseline is stated without any methodological support.** The paper claims GPT-4o and Gemini Pro are "25.1% and 43.8% lower than human performance" (line 49), implying ~93.1% human accuracy, yet provides zero description of how this was measured. No annotator count, qualifications, number of questions each answered, inter-annotator agreement, or whether the protocol matched the model evaluation. For a benchmark paper, the human ceiling is a key calibration reference — leaving its methodology completely unspecified means this central comparison is unverifiable. The paper's core claims about models falling short of human-level understanding rest partly on this figure.

2. **Unanswerable-instance scoring protocol is not specified.** The paper argues that models "should directly indicate when a query is unanswerable" (line 122) and reports accuracy drops on unanswerable variants (line 192). However, it never explains how these instances are scored. For the 40.5% of unanswerable variants created by option modification that produces "no correct answer" (line 142): can models abstain (e.g., output "I don't know") and be scored correct? Is any selected option simply counted as wrong? The paper says it uses "a set of pre-defined rules" to extract choices (line 171), but these rules and how they handle abstention for unanswerable variants are not described. The claim that the pairwise design "improves the reliability of MuirBench" (line 192) cannot be properly evaluated without this information.

### Minor

3. **Image concatenation for single-image models introduces a confound.** The paper concatenates images for models that do not natively support multi-image input (line 171). This creates an input format the model was never trained on — a composite image with different resolution, aspect ratio, and spatial layout. The finding that single-image models "cannot generalize" (line 187) partly conflates genuine inability to reason across images with sensitivity to an unnatural input format. Different concatenation strategies (horizontal vs. vertical stacking, tiling) are not ablated.

4. **No analysis of potential data contamination.** 40.8% of the data comes from existing datasets (GeneCIS, SeedBench, IconQA) and 21.7% from derived datasets (NLVR2, HallusionBench, ISVQA, MMBench). Several evaluated models may have been trained on these source datasets. The paper does not acknowledge or analyze this risk, which is a standard concern for benchmark papers.

5. **Error analysis is too thin to be informative.** The error analysis (Section 4.3, lines 196-198) examines only 100 errors from a single model (GPT-4o), with no breakdown by task, no coding reliability, and no comparison to other models' error patterns. The categories (26% "failure of capturing details," etc.) are intuitive but not rigorously derived.

6. **Unanswerable variant validity is not verified.** The paper describes strategies for creating unanswerable variants but provides no evidence that human annotators actually found them unanswerable. If a human can still infer the intended answer despite the manipulation, the variant is not truly unanswerable and the evaluation is compromised.

### Trivial
None.

## Nice-to-Haves

- Per-task confidence intervals or variance estimates would contextualize results given that task sample sizes vary from 2.5% to 17.8% of the benchmark.
- A dedicated limitations section would improve the paper's credibility by acknowledging the contamination risk, concatenation confound, and multiple-choice format limitations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The main results table is not visible in the parsed text"** — This is a parser artifact, not an author error (per hard rules, formatting artifacts from parsing are not author errors).
- **"The introduction overstates novelty because prior works already include multi-image questions"** — The paper explicitly acknowledges Mantis-Eval and BLINK (lines 37, 70-72) and explains why they are insufficient (207 examples, limited relations). The criticism ignores this discussion.
- **"Missing appendix/proofs"** — The parser strips supplementary sections from all papers; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Describe the human evaluation methodology in full:** annotator count, qualifications, questions per annotator, whether both answerable and unanswerable variants were shown, inter-annotator agreement (Cohen's κ), and the aggregation procedure.
2. **Specify the exact scoring rule for unanswerable instances:** how abstention is detected and scored, and what the pre-defined rules for extracting choices are.
3. **Ablate the concatenation strategy** for single-image models by comparing at least two different arrangements (e.g., side-by-side vs. vertical stacking) to disentangle format sensitivity from multi-image reasoning ability.
4. **Add a contamination analysis:** check which models were trained on which source datasets and report per-task performance differences between potentially contaminated and uncontaminated subsets.
5. **Validate the unanswerable variants with human annotators** to confirm they are indeed unanswerable.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>