- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 5, 6
I have all the information needed from the paper. Let me now synthesize the final review.

## Summary

This paper presents the first domain adaptation benchmark for indoor 3D object detection. It introduces two large-scale synthetic datasets (SimRoom with 7,202 scenes/176k boxes, SimHouse with 7,306 scenes/686k boxes) generated via the ProcTHOR framework, and combines them with ScanNet and SUN RGB-D to define four adaptation scenarios (high-to-low quality, low-to-high quality, synthetic-to-real, single-to-multiroom). Through controlled experiments — including a data-scale ablation (Table 5) that equalizes scene counts — the paper demonstrates that the synthetic-to-real gap is the most challenging domain adaptation hurdle. It also provides baselines using mean teacher and several existing UDA methods adapted to the detection task.

## Strengths

1. **First domain adaptation benchmark for indoor 3D object detection.** Section 3.3.3 defines four well-motivated adaptation scenarios (high-to-low, low-to-high quality; synthetic-to-real; single-to-multiroom), and Table 2 quantifies large cross-domain performance drops (e.g., SimRoom→ScanNet: 11.20 mAP vs. target-only 44.09), establishing an evaluation protocol that did not previously exist in this subfield.

2. **Large-scale synthetic datasets enabling controlled analysis.** SimRoom and SimHouse provide an order of magnitude more annotations than existing real datasets (e.g., 686k boxes in SimHouse vs. ~37k in ScanNet and SUN RGB-D, Table 1), enabling the controlled study of domain gaps at a scale prior indoor detection datasets do not offer.

3. **Controlled data-scale ablation isolating the synthetic-to-real gap from data quantity.** Table 5 equalizes training scene counts (230, 400, 3,000) across datasets and shows SimRoom→ScanNet (5.25 mAP) remains far below SUN→ScanNet (14.10) and ScanNet++→ScanNet (22.54), directly attributing the performance loss to the synthetic-to-real style gap rather than data scarcity. This is the paper's strongest piece of evidence for its central claim.

4. **Causal decomposition of semantic vs. layout domain gaps.** Table 4 compares "SimRoom + Real objects" against fully simulated and oracle conditions, showing that real objects improve mAP from 11.20 to 21.99 but still trail the full real layout (44.09), empirically separating object semantics from room layout as distinct gap factors.

5. **First UDA baselines adapted to indoor 3D object detection.** Table 3 evaluates mean teacher, VSS, PPFA, RV, and OHDA across all four benchmarks, providing the community with reproducible starting points for future work.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance reporting.** Every mAP value in Tables 2–5 is a single number with no standard deviation, confidence intervals, or mention of multiple seeds. Given that many adaptation gains are modest (e.g., MT improving from 11.20 to 14.78 in rm2scn; VSS improving from 28.23 to 28.35 in sun2scn), it is impossible to assess whether these improvements are stable or noise. For a benchmark that aims to ground future research, this is a significant evidential gap. The paper does not mention running experiments with multiple seeds anywhere (Section 4.1).

2. **Main domain gap analysis relies on a single detector (VoteNet).** Section 4.1 mentions experiments on Pointformer and V-DETR are in the supplementary, but the core analysis of domain gaps (Tables 2, 4, 5), data scale, and adaptation methods uses only VoteNet. The observed difficulty rankings (e.g., synthetic-to-real being hardest) may be detector-dependent — transformer-based detectors with attention mechanisms could handle layout or style differences differently. For a benchmark paper whose conclusions aim to guide the community, the generality of the claims is uncertain without multi-detector results integrated into the main analysis.

3. **Adjustments to UDA baselines are unspecified.** Section 4.3.2 states "we re-implement all the methods and make some adjustments to achieve better results on object detection task" but provides no detail on what these adjustments are. Since VSS, PPFA, and RV were originally designed for segmentation/classification tasks, the specific changes made for object detection are critical for reproducibility. Without these details, the baseline results in Table 3 cannot be reliably compared against by future work.

### Minor

1. **Label space alignment mapping is not provided in the paper.** Section 3.3.2 describes merging fine-grained categories into 15 broad ones (e.g., "dining table" and "office table" → "table"), but the actual mapping table across all four datasets is not shown. While the methodology is described, the absence of the full mapping makes it difficult to assess potential misalignment issues (e.g., whether "nightstand" consistently maps to the same broad category across datasets). The mapping may exist in the supplementary (stripped by parser), but the main paper should at least summarize the merging rules by dataset.

### Trivial
- None beyond typical formatting artifacts from PDF extraction (irrelevant to evaluation).

## Nice-to-Haves
- **Limitations discussion:** The paper would benefit from explicitly acknowledging limitations such as: synthetic point clouds are uniformly sampled from clean meshes (differing from real sensor noise), the benchmark covers only 15 categories, and the analysis is VoteNet-centric.
- **Per-category AP results:** Reporting AP for a few representative categories would help understand whether adaptation benefits are uniform or category-dependent, especially given the size differences noted in Figure 3(b).
- **Original category counts in Table 1:** Including the number of original categories in each dataset (not just the merged 15) would give a clearer picture of the label merging scope.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"Object placement layout conclusion is under-supported (conflates placement and geometry)"** — Removed. Table 4 shows SimRoom+RealObj at 21.99 vs. oracle at 44.09, and the gap between these two conditions is indeed attributable to layout (since both use real objects). The conclusion is reasonably supported by the controlled experiment.
- **"Paper does not discuss diversity of object shapes in synthetic datasets"** — Removed. The ProcTHOR framework is a cited, established system; the meshes are detailed enough to provide valid 3D structure. This is a curiosity, not a weakness.
- **"Exact scene IDs should be provided"** — Removed. The paper states datasets will be released with the paper, and for generated data, providing the generation code/parameters is standard practice.
- **"Object size prior analysis should have tested estimation from unlabeled target data"** — Removed. This is scope creep — requesting an additional contribution the paper never claimed to make.
- **"Category-wise results missing"** — Removed. This is a useful extension but not a weakness; moved to Nice-to-Haves.
- **"Missing related works"** — Removed per instructions: the reviewer cannot confirm missing citations without external sources.

## Novel Insights

None beyond the paper's own contributions. The key insight — that synthetic-to-real is the hardest domain gap for indoor 3D detection, and that this is not merely a data-scale issue — is already clearly articulated in the paper. The cross-validation from the data ablation (Table 5) and the semantic-vs-layout decomposition (Table 4) are the paper's own analytical contributions, and no reviewer observation supersedes or deepens them.

## Suggestions

1. **Report variance.** Run all experiments with at least 3 random seeds and report mean ± std in Tables 2, 3, and 5. If computational cost is prohibitive, at minimum run the key synthetic-to-real and data-scale experiments (Tables 2 "rm2scn" and Table 5) with multiple seeds.

2. **Integrate second-detector results into the main paper.** The main analysis (at minimum, the domain gap rankings in Table 2 and the data-scale ablation in Table 5) should include results from Pointformer or V-DETR. If results are consistent, this strongly strengthens the claims; if different, that is itself a valuable finding.

3. **Document the UDA baseline adjustments.** Provide a paragraph or table specifying how each method (VSS, PPFA, RV, OHDA) was adapted from its original task (classification/segmentation) to object detection — e.g., what architectural changes were made, what loss functions were modified, what hyperparameters were tuned.

4. **Include the label mapping table** in the main paper or appendices, along with a brief verification note (e.g., "a random sample of 50 category mappings was manually cross-checked across all four datasets").
