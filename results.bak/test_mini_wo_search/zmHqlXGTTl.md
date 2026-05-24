Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the paper content. Let me produce the consolidated review.

## Summary

This paper introduces LayoutSciPG, a new task for generating scientific posters from papers by jointly handling multimodal content extraction and layout design. The contributions are (1) SciPG, a large-scale dataset of 11,302 paper–poster pairs from four major conferences, and (2) a multimodal extractor-generator framework with an interactive generator that uses an adaptive memory mechanism to paraphrase extracted content and predict layout positions. The method is evaluated against adapted baselines on extraction, generation, and layout metrics, with ablation studies and a human evaluation.

## Strengths

- **Large-scale dataset addresses a genuine data scarcity.** Prior scientific poster datasets contained fewer than 300 pairs; SciPG's 11,302 pairs (Section 3, Table 1 cited in text) are an order-of-magnitude increase that enables data-driven approaches for this task. This is the paper's most concrete and verifiable contribution.

- **Proposed framework with adaptive memory outperforms adapted baselines on layout metrics.** Tables 4 and 5 (results described in the text) show substantial improvements over the adapted AdaD2P baseline: +22.36% in layout overlap and +25.05% in coverage. The ablation study (Table 6) confirms that removing the adaptive memory causes the single largest drop in layout performance, providing evidence for the design choice.

- **Ablation studies and parameter sensitivity analysis provide practical guidance.** Table 6 systematically ablates KL-Divergence optimization, pre-training strategy, data extension, and memory variants (adaptive vs. normal vs. none). Figure 2 varies memory size \(k\) and KL weight \(\beta\), identifying \(k=50, \beta=0.5\) as optimal for layout. This supports reproducibility and gives clear tuning recommendations.

## Weaknesses

### Fatal

None.

### Major

- **The evaluation is heavily reference-based, which only partially supports the paper's aims.** The paper frames the goal as generating "flexible posters" (line 14) that are "informative and visually appealing" (line 12), yet the main quantitative metrics (ROUGE, ImgP/ImgR) and two of three human evaluation criteria (Text Relevance, Image Accuracy) directly measure fidelity to a *single* ground-truth poster. Overlap and Coverage (self-referential layout metrics) and the Layout Aesthetics human criterion (rated on whether placement is "logical and visually appealing" without reference to ground truth, line 303) partially mitigate this, but the core evidence for "effectiveness" is reconstruction quality against one reference. A model that produces an equally valid but different layout or paraphrase would be penalized, making it unclear whether the evaluation measures genuine poster quality or just reproduction of the training examples' specific choices. This does not invalidate the paper — reference-based evaluation is standard in generation tasks — but it substantially narrows what the reported numbers actually demonstrate.

- **Dataset alignment quality is unvalidated.** The paper states that elements are "automatically extracted ... and ... matched to create document-to-poster alignment" (line 69) but provides no accuracy analysis, no human verification on a sample, and no discussion of inevitable errors in multimodal alignment from conference PDFs and poster images. Since the dataset is intended as both training data and a benchmark, corrupted alignment would propagate directly into the training signal and conflate method quality with data quality. This is a significant gap for a claimed benchmark contribution.

- **Claims about GPU memory are asserted without empirical support.** The abstract states the approach "effectively tackles challenges related to GPU memory consumption" (line 6), and the method section motivates the interactive generator and adaptive memory as addressing these constraints (lines 112, 133). Yet no GPU memory usage, peak memory measurements, or runtime comparisons are reported anywhere in the paper. While the interactive approach is plausibly beneficial by construction, the specific claim is unevidenced.

### Minor

- **Layout metrics are imprecisely defined, hurting replicability.** Validity is described as "the ratio of valid elements greater than 0.1% of the canvas" — it is unclear how "valid" is determined beyond the size threshold. Alignment is "the extent of spatial non-alignment between elements" without a formula. FD and DreamSim are mentioned without specifying what they compare (e.g., whether posters are rasterized, at what resolution, and against what reference). Overlap and Coverage are clearer but the descriptions are brief. The paper would benefit from precise mathematical definitions or citations to established layout metrics.

- **Only one adapted baseline for the full generation task.** The generation comparison (Table 4) pits the proposed method against only an adapted AdaD2P. With a single baseline and no simpler reference (e.g., a retrieval-based approach or prompted LLM), it is difficult for a reader to calibrate how challenging the task is or whether the improvements reflect genuine progress or a weak baseline.

- **No inter-annotator agreement reported for human evaluation.** The human evaluation uses 10 annotators rating 50 posters across three conditions (line 299). Reporting agreement (e.g., Krippendorff's alpha or Fleiss' kappa) would strengthen confidence in the ratings' reliability.

- **Pre-training objectives are not individually ablated.** Three pre-training objectives are introduced (Joint Text-Layout Reconstruction, Layout Modeling, Text Construction, Section 4.3.3), but Table 6 only reports a single "w/ PT vs w/o PT" comparison. The individual contribution of each objective is unknown.

- **No analysis of dataset diversity across conferences.** The topic-aware evaluation (Table 7) begins to address this, but the paper does not analyze structural differences between conferences (e.g., are CVPR posters systematically different from ICLR posters?), which would inform generalization claims.

### Trivial

None.

## Nice-to-Haves

- A task-based human evaluation where annotators rate generated posters on clarity and informativeness *without* seeing the ground truth, directly measuring the quality dimension the paper claims to address.
- GPU memory / runtime measurements comparing variants with and without the adaptive memory mechanism.
- Manual verification of alignment accuracy on a random subset of the dataset.
- Additional baselines (e.g., a prompted LLM with layout instructions) to help calibrate task difficulty.
- Individual ablation of the three pre-training objectives.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Every automatic metric... compare the generated poster to a single ground-truth poster" (from Harsh Critic Critical Issue 1):** Factually inaccurate. Overlap (IoU between generated layout elements), Coverage (percentage of canvas occupied), Validity, and Alignment are self-referential layout metrics that do not compare against ground truth. The paper is not as monolithic in its reference-based evaluation as claimed.
- **"Even the human ratings... all operationalize quality as fidelity to one human-authored reference":** Partially inaccurate. Layout Aesthetics (line 303) asks whether placement is "logical and visually appealing" — this is an intrinsic quality judgment, not a reference-based comparison. Text Relevance and Image Accuracy are reference-based, which is a real limitation, but the blanket claim is overstated.
- **"The paper should not be accepted... the reader cannot determine whether the method actually advances the stated goal":** This assessment overstates severity. The evaluation has real limitations but does not render the contribution uninterpretable. The dataset contribution is independently valuable, and the method does show gains on the metrics used. The concern is better framed as a major weakness requiring revision rather than rejection.

(Additional removed: the critic's suggestion about missing related works, which I cannot verify; formatting/style nitpicks that are parser artifacts; and some generic "could be stronger" framing that lacked specific evidence.)

## Novel Insights

The most interesting synthetic observation across the reviews is the tension between the paper's framing of "flexible" poster generation and its reference-locked evaluation. The harsh critic identifies this gap clearly, but the strength finder correctly notes that the paper does include self-referential layout metrics (Overlap, Coverage) and a non-reference-based Layout Aesthetics criterion in the human evaluation. Together, these suggest the paper is *partially aware* of the need for quality evaluation but did not commit fully to it. The adaptive memory mechanism's outsized impact on layout (largest drop in Table 6 ablation) is another genuine insight: it confirms that long-range dependency handling is the bottleneck for this task, which is non-obvious and could guide future work regardless of the evaluation framing concerns.

## Suggestions

1. Reframe the evaluation narrative: explicitly acknowledge that the current metrics measure reference fidelity and that this is only one dimension of poster quality. Add a small-scale task-based human study (e.g., ask annotators to read a paper and rate the generated poster on clarity *without* showing the ground truth) to support the "informative and visually appealing" claim.

2. Validate the dataset alignment on a random sample (e.g., 200 pairs) and report accuracy, including category-specific error types (missing elements, wrong matches). This would substantially strengthen the dataset contribution.

3. Add precise formulas or pseudocode for Validity and Alignment metrics in a supplementary section. Clarify how FD and DreamSim are applied (rasterized poster resolution, reference image).

4. Provide GPU memory and runtime measurements comparing the full model to a version without the adaptive memory mechanism — this would substantiate the computational motivation that currently only appears as a claim.

5. Add a second baseline for the full generation task (e.g., a prompted GPT-4 or a retrieval-based method) to help readers calibrate the difficulty of the benchmark.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>