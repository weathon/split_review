- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 1, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

MarineMaid is a dataset and benchmark for marine visual understanding, comprising 14,645 images, 42,217 bounding boxes across 670 categories, and 12,873 expert-refined instance captions averaging 42 words—significantly longer and more domain-specific than existing alternatives. The paper benchmarks 14 state-of-the-art models across close-set detection, open-vocabulary detection, instance captioning, and visual grounding, revealing consistent performance gaps that demonstrate the dataset's value as a challenging domain-specific testbed.

## Strengths

- **First instance-level caption dataset for marine creatures with biological-traits detail**: MarineMaid's captions average 42 words vs. ~12 for general-purpose datasets (Table 1, §3.3), and are refined by domain experts from four aspects (features, spatial info, background, activity). No prior marine dataset provides this combination of dense BBOX annotations and detailed per-instance captions.

- **Comprehensive multi-task benchmarking reveals clear domain gaps**: Tables 2–4 quantitatively show that state-of-the-art detectors (YOLOX, DECOLA), VLMs (LLaVA, InstructBLIP), and grounding models (GroundingDINO, GroundVLP) all perform poorly on marine creatures, with qualitative evidence such as GroundVLP misclassifying a shark as a cow (Fig. 6). This demonstrates MarineMaid exposes limitations that general-purpose evaluation suites miss.

- **Wide taxonomic coverage with hierarchical structure**: 670 categories spanning Cephalopods, Crustaceans, Sharks, Rays, Mammals, Corals, and Invertebrates, organized under a 6-level coarse-to-fine taxonomy (Kingdom → Genus) queried from the official WoRMS database (§3.1). Goes well beyond existing marine datasets that focus primarily on fish.

- **Structured negative captions with 11 fine-grained error properties**: The dataset introduces negative captions annotated with properties such as classification, background, spatial, action, color, shape, etc. (§3.1). This is more informative than the random-noun-substitution negatives in prior work (Zhao et al., 2022; Yuksekgonul et al., 2022).

- **Substantial human annotation effort**: 16 domain experts contributed 624 person-hours with a five-stage pipeline (SAM-assisted BBOX, MarineGPT caption candidates, expert refinement from four aspects, two-annotator cross-checking, final expert inspection) (§3.2).

## Weaknesses

### Fatal
None.

### Major

- **No inter-annotator agreement metrics reported**. For a dataset paper that claims "superior level of quality," the absence of any quantitative reliability measure—neither for bounding boxes (e.g., IoU consistency across annotators) nor for captions (e.g., semantic similarity or property-label agreement)—is a significant evidential gap. The paper mentions cross-checking by two annotators (§3.2) but provides no statistics. This undermines confidence in annotation consistency and is the most impactful weakness to address.

### Minor

- **BBOX annotation pipeline is underspecified**. The description in §3.2 says "first manually label bounding boxes" then "employ SAM model to label all marine objects…by receiving the human prompts to iteratively obtain high-quality BBOX annotations." It is unclear whether SAM is used for initial labeling, refinement of manual boxes, or both. The exact human-in-the-loop workflow, prompting strategy, and quality thresholds are not described, making the pipeline hard to replicate or assess.

- **1024-pixel threshold for caption generation is not justified**. The paper (§3.2) states it only generates captions for image regions larger than 1024 pixels, but provides no rationale or analysis of how many instances this excludes or whether it systematically biases the caption set toward larger organisms. For a monitoring-oriented benchmark, juvenile or small specimens may be equally important.

- **Negative captions are introduced but never evaluated**. The 11-type negative caption scheme (§3.1) is described as a contribution, yet none of the benchmarks (detection, captioning, grounding) use these negatives in any evaluation. Even a simple experiment showing that models fail to reject negative captions would integrate this feature into the paper's contribution.

- **Prompt-mismatch confound for image-level VLMs is not acknowledged as a limitation**. Image-level VLMs (LLaVA, BLIP-2, InstructBLIP) are prompted with "describe the object in this figure" and evaluated on instance-level captions. Since these models are designed for holistic image understanding, low CIDEr/BLEU scores may partly reflect prompt misalignment rather than a true inability to describe marine instances. The paper does not discuss this.

- **Category prepending to reference captions may affect metric interpretation**. The paper prepends "This is a \<Category Name\>." to reference captions (§4.2) to penalize generic responses, but does not clarify whether the same prepending is applied to model outputs during evaluation. If not, CIDEr/BLEU/ROUGE scores could be artificially affected.

- **Limitations section is too brief**. A single sentence acknowledging that not all marine creatures are covered (§5) omits important discussion topics: annotation bias, class imbalance (Fig. 3 shows long-tailed distribution), the 1024-pixel threshold, and the prompt confound mentioned above.

### Trivial

- **Abstract vs. body data statistics could be clearer**. The abstract states "12,873 fine-grained instance-captioning pairs" while §3.1 gives 22,321 total positive captions. The body does explain that 12,873 are expert-refined and 22,321 includes generated ones, but the relationship is not immediately obvious on first read; a brief clarification in the abstract or a footnote would help.

## Nice-to-Haves

- Confidence intervals on main results (Tables 2–4) would strengthen model comparisons.
- Class imbalance analysis showing how detector performance varies with category frequency would be valuable for a monitoring-oriented benchmark.
- The negative caption evaluation could be a natural extension: e.g., testing whether VLMs can distinguish positive from negative captions.
- Discussion of how class names are phrased for open-vocabulary detectors (e.g., "Coral" vs. "Scleractinia") would improve reproducibility since naming choices can significantly affect results.

## Removed Points

These points from the input reviews are flagged for removal; treat them with caution:

- **"Confusing object detection evaluation (close-set detectors on all three splits)"**: REMOVED. The paper explicitly states at line 84: "report the mAP50 of 24 seen categories under three settings" and "Please note that we do not evaluate these close-set object detection algorithms on the unseen categories." Close-set detectors are evaluated on the 24 Class-level consolidated categories across all three settings. The critic's claim that evaluating on 555/482 seen categories is "structurally impossible" reflects a misreading of the paper.

- **"Data statistics relationship never explained"**: REMOVED. The paper at line 45 clearly states: "There are 12,873 captions that have been refined by domain experts… Totally we have 22,321 refined and generated positive captions, and 12,431 generated negative captions." The relationship is explained.

- **"SAM contradicts manual labeling"**: PARTIALLY REMOVED. The description is vague (kept as a Minor weakness above), but the critic's framing as a contradiction is too strong—the stages can be sequential (manual then SAM refinement).

- **"Missing related works"**: REMOVED per protocol (no external source to confirm omissions).

- **Formatting/style nitpicks, reproducibility nitpicks about undisclosed hyperparameters**: REMOVED per protocol.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): REMOVED. Only concrete, specific strengths are retained.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that the paper's demonstrated value (exposing failure modes of general-purpose models on marine data) actually partially conflicts with its own evaluation design choices. The low performance of image-level VLMs is presented as a failing of those models, but it may equally reflect a task misalignment (whole-image vs. instance-level) that could mask progress. Similarly, the negative captions are carefully constructed but absent from all benchmarks, making them a structural contribution without empirical validation. These tensions suggest the paper would be strengthened not by adding more models, but by tightening the alignment between what the dataset enables and what the benchmarks actually evaluate.

## Suggestions

1. **Add inter-annotator agreement statistics** (IoU consistency for BBOX, semantic similarity or classification agreement for captions) on a representative subset. This directly supports the claim of annotation quality and is standard for dataset papers.
2. **Clarify the SAM-in-the-loop BBOX pipeline**: provide a short algorithmic description or diagram showing the exact human-SAM interaction, prompting strategy, and quality thresholds used.
3. **Justify or remove the 1024-pixel threshold**: report how many instances are excluded and whether this biases the caption set toward larger organisms.
4. **Expand the limitations section** to address class imbalance, the prompt confound for image-level VLMs, and annotation biases.
5. **Clarify the category prepending** in the captioning evaluation: state whether the same "This is a \<Category Name\>." prefix is added to model outputs or only to references.
