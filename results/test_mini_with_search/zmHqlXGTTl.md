Now I have a thorough understanding of both the paper and the calibration landscape. Let me write the final review.

## Summary

This paper introduces LayoutSciPG, a new task for layout-aware scientific poster generation from papers. It contributes SciPG, a dataset of 11,302 paper-poster pairs from four ML/AI conferences (CVPR, ICML, NeurIPS, ICLR), and proposes a multimodal extractor-generator framework: a hierarchical RoBERTa+BiLSTM extractor (MDE) for selecting text+image elements, and an interactive BART-based generator with an adaptive memory mechanism that jointly paraphrases content and predicts layout bounding boxes. Experiments compare against baselines (NeuralExt, MSMO, AdaD2P for extraction; AdaD2P for generation) with automatic metrics and human evaluation (50 pairs, 10 annotators).

## Strengths

1. **Large-scale dataset (11,302 paper-poster pairs)** — An order of magnitude larger than prior scientific poster datasets (fewer than 300 pairs each, Table 1), collected from four major conferences. The dataset fills a genuine resource gap and the authors commit to releasing it.

2. **Clear extractor architecture with verified gains** — The hierarchical MDE (RoBERTa + BiLSTM + classification head) is well-described. Table 3 shows it outperforms three baselines (NeuralExt, MSMO, AdaD2P) on both ROUGE and image precision/recall, and the ablation ("w/o LSTM") confirms the BiLSTM's contribution.

3. **Ablation studies that isolate component contributions** — Table 6 systematically removes the memory module, KL-divergence loss, pre-training, and data extension, establishing that each component contributes and that the adaptive memory causes the largest single drop in layout performance. The ablation also compares adaptive vs. vanilla RMT memory, which reveals the adaptive variant's advantage.

4. **Human evaluation with multiple annotators** — Ten annotators rated 50 triplets (ground-truth, baseline, proposed) on text relevance, image accuracy, and layout aesthetics. The proposed method outperforms the baseline on all three axes. The paper honestly notes that layout aesthetics scores remain low overall, acknowledging the difficulty.

5. **Topic-aware evaluation across conferences** — Table 7 tests cross-domain generalization by training on individual conference data vs. all data, showing that training on all topics produces better text and layout metrics and that the model adapts to different publication formats.

## Weaknesses

### Major

1. **Dataset construction is critically underspecified.** Section 3 devotes only two sentences to the pipeline: pairs were "collected from public conference web pages" and elements were "automatically extract[ed]...and perform[ed] matching to create document-to-poster alignment." There is no description of: the crawling procedure or inclusion criteria; the PDF-parsing/OCR pipeline used to extract text blocks and images from either papers or posters; the alignment algorithm that matches paper elements to poster elements, or its accuracy; how text blocks in posters (often raster images) were identified and transcribed; whether alignment was validated on a sample. Because the evaluation relies on ground-truth extraction labels, paraphrase references, and layout targets derived from this alignment, the entire quantitative evaluation rests on an unknown foundation. The dataset is a core contribution — "We create and will release a new dataset" is the first bullet in the contributions — yet the paper provides no basis to assess its quality.

2. **Layout evaluation metrics are too vague to support the quantitative claims.** The definitions in Section 5.1 lack the precision needed to interpret Table 4 and Table 5:
   - *Overlap*: "the intersection over union of various layout elements" — it is unclear whether this computes IoU between predicted and ground-truth bounding boxes, or intra-poster IoU among predicted elements. The ground-truth overlap of 47.12 (Table 4) does not cleanly match either interpretation without a precise definition.
   - *Coverage*: "the percentage of the canvas occupied by the layout elements" — the canvas dimensions are never stated; it is unclear whether coordinates are normalized.
   - *Validity*: "the ratio of valid elements greater than 0.1% of the canvas" — what makes an element "valid" vs. invalid is not defined.
   - *Alignment*: "the extent of spatial non-alignment between elements" — circular and no formula is given.
   
   These metrics are central evidence for the paper's layout claims (e.g., "22.36% improvement in overlap," "25.05% improvement in coverage"). Without clear definitions, the quantitative layout comparisons cannot be independently verified or reproduced.

3. **Only one baseline for the full generation task.** For multimodal generation (paraphrasing + layout), the paper compares only against AdaD2P, adapted from a different domain (document-to-slide). While the paper notes "there are no established baselines," feasible baselines exist — e.g., an extract-then-template pipeline (extractive summarization with a fixed layout template) or a standard abstractive summarizer (T5/BART for text) combined with a simple layout predictor. Without such baselines, it is difficult to tell whether the proposed interactive generator adds value over simpler alternatives.

### Minor

4. **Sequential design of the interactive generator is not empirically justified.** The generator processes extracted elements one at a time in document order, which imposes a linear ordering on a fundamentally 2D layout problem. The paper claims this reduces GPU memory but provides no memory profiling. The ablation (Table 6) does not vary element order (e.g., random vs. document order vs. learned order) to test whether the sequential assumption constrains the model.

5. **"Adaptive" memory distinction from RMT is under-explained.** While Equations 7–8 describe a MultiHeadAttention update between memory segments that goes beyond vanilla RMT (Bulatov et al., 2022), the paper does not provide empirical justification for why this attention-based update is superior. The ablation in Table 6 ("normal memory" vs. "adaptive memory") shows a gap but does not analyze what the attention mechanism captures.

### Trivial

6. The paper states it uses "four [mask] tokens to indicate the layout coordinates in the input, ensuring alignment with the pretraining task" but does not explain how BART's MLM-style pretraining on text helps with layout coordinate regression, which is a fundamentally different prediction type.

## Nice-to-Haves

- Adding confidence intervals or statistical significance tests for Tables 3–7 would strengthen the quantitative claims.
- A brief discussion of poster canvas sizes and aspect ratios would help contextualize the layout metrics.
- Clarifying whether images extracted from the paper are reused directly in the poster or resized/cropped would clarify the layout prediction task.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"No comparison to a modern abstractive summarization system (T5/BART without layout module)"* — The paper's goal is joint content+layout generation, not pure summarization. The generator IS initialized from BART-large; comparing to BART without layout prediction would test a different task. However, the broader point about thin baselines stands in Major #3 above.
- *"The claimed 'adaptive' aspect is not distinguished from the original RMT"* — This is factually incorrect. The paper does distinguish it via the MultiHeadAttention update in Equations 7–8. The critic missed this detail.
- *"Quality of images is not assessable from parser output"* — This is a parser artifact, not an author error.
- *"No statistical significance tests"* — While nice-to-have, not standard for all layout generation papers.
- *"Missing appendix, missing proofs in appendix, or absent references"* — Parser strips these; they exist in the original.
- *"Code and dataset are said to be released but no link or license information"* — The paper states "will release" and it is common to omit links in anonymized submissions.
- *"No discussion of poster canvas sizes"* — Addressed as a nice-to-have.
- Various formatting/style nitpicks from the harsh critic.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension: the paper claims a dataset as a core contribution but provides almost no information about how it was constructed or validated. This is not a novel observation but a straightforward failure to meet documentation expectations.

## Suggestions

1. **Fully document the dataset pipeline.** Describe the crawling procedure, the OCR/PDF-parsing tools used, the element-matching algorithm, and its accuracy on a manually verified sample. Report the distribution of poster sizes and element counts.
2. **Define every layout metric with a precise formula.** Specify exactly what sets of bounding boxes are compared, in what coordinate space, and with what normalization. A worked example in the appendix would be ideal.
3. **Add at least one simple generation baseline** — e.g., extract top-k sentences via MDE (or a standard extractor), place them in a vertical template, and insert extracted images at fixed positions. This would isolate the value of learned layout prediction.
4. **Include an ablation that varies element order** (document order, shuffled, random) to test whether the sequential generation assumption limits the model.
5. **Provide memory usage profiling** to substantiate the GPU memory claim about the interactive generator.

## Score and Decision

**Round 1 bracket:** The most similar topical papers in the human-review corpus — Paper2Slide (avg 3.0, rejected) and AnyLayout (avg 2.5, withdrawn/rejected) — establish a lower anchor. Mid-range papers on multimodal summarization/benchmarking (XFacta 4.0, rejected; UniDoc-Bench 4.5, rejected; TripleSumm 5.5, accepted) form a middle band. Strong anchors (8+) are topically unrelated. **Initial bracket: between 3.5 and 5.0.**

**Round 2 narrowing:** OmniLayout (3.5, withdrawn/rejected) and AutoFigure (3.6, accepted as Poster with highly mixed reviews: 6,2,2,4,4) are the most directly comparable anchors that also contribute a new task+dataset+method. The current paper is stronger than OmniLayout (better ablation coverage, human evaluation) and broadly comparable to AutoFigure (both have dataset documentation gaps and evaluation metric clarity issues, but the current paper has clearer methodology and better ablated experiments). TextAtlas5M (4.5, rejected) is a dataset-heavy paper with automatic annotation concerns.

Comparison to individual round-2 anchors:
- **OmniLayout (3.5, withdrawn/rejected)**: The current paper has stronger empirical validation (human evaluation, parameter sensitivity, topic-aware experiments vs. OmniLayout's limited ablation). **Current paper is stronger.**
- **AutoFigure (3.6, accepted poster)**: Similar profile — both introduce a new task+dataset+method with gaps in pipeline documentation and metric definition. The current paper has more thorough ablations (Table 6: 8 configurations vs. AutoFigure's limited ablations). Comparable human evaluation scope. **Comparable or slightly stronger.**
- **TextAtlas5M (4.5, rejected)**: More mature dataset documentation but limited method contribution. **Different profile, similar quality tier.**

**Final score:** 4.0. The paper has genuine contributions and verifiable strengths, but the two Major weaknesses (underspecified dataset construction, vague layout metrics) substantially limit the confidence a reader can place in the reported results. The work is a solid foundation but needs more documentation before it is publication-ready.

**Decision:** Reject.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>