Now I have all the information I need to produce a thorough, verified review. Let me write it.

## Summary

This paper presents MarineMaid, a large-scale dataset for marine visual understanding containing 14,645 images with 42,217 bounding boxes across 670 categories, paired with 12,873 domain-expert-refined instance captions (avg. 42 words) and 12,431 negative captions. The dataset supports close-set and open-vocabulary object detection, instance captioning, and visual grounding. The paper benchmarks 14 state-of-the-art models across these tasks, revealing significant gaps between current algorithms and the requirements of domain-specific marine understanding.

## Strengths

- **First region-level instance-caption dataset for marine creatures with long, expert-refined captions.** The paper constructs 12,873 instance-caption pairs averaging 42 words (Table 1 comparison), significantly longer than existing datasets like Visual Genome (12 words). This directly addresses the need for detailed biological trait descriptions beyond short image-level captions.

- **Comprehensive multi-task benchmark evaluating 14 models across four tasks.** The paper systematically benchmarks close-set detection, open-vocabulary detection (Table 2), instance captioning (Table 3), and visual grounding (Table 4), revealing concrete limitations of current models on marine data — e.g., region-level VLMs describing the whole image instead of the instance, and GroundVLP mistaking a shark for a cow (Fig. 6).

- **Hierarchical taxonomy with 6 granularity levels automatically queried from the WoRMS database.** Section 3.1 describes this structure (Kingdom–Genus), enabling fine-grained classification and analysis beyond flat category lists.

- **Inclusion of 12,431 negative captions tagged with 11 predefined properties** (classification, background, spatial, action, color, shape, etc.) as hard negatives, going beyond simple noun-replacement strategies in prior work (Section 3.1).

- **Rigorous annotation pipeline with 16 domain experts and 624 human hours.** Section 3.2 details the three-stage process (BBOX labeling, caption generation/refinement, cross-checking), demonstrating substantial annotation effort.

- **Three systematic seen/unseen splits for open-vocabulary detection** (Class-level, Intra-Class, Inter-Class), allowing evaluation of generalization at different taxonomic granularities (Section 4.1).

## Weaknesses

### Fatal
None.

### Major

- **Instance captioning evaluation protocol introduces an unquantified bias.** Image-level VLMs (LLAVA, MiniGPT-4, BLIP2, InstructBLIP) are evaluated on the full image using the prompt "describe the object in this figure," while the ground-truth captions describe a specific cropped instance. The paper acknowledges this limitation in passing (line 103: image-level VLMs "lacked the ability to understand specific object instances") but presents the quantitative comparison in Table 3 as if all models were evaluated under equivalent conditions. The very low CIDEr and BLEU-4 scores for image-level models partly reflect this input-target misalignment rather than pure captioning quality. This conflates two distinct error sources: grounding failure and captioning failure. The authors should either (a) crop the image for all models so visual input matches the target, or (b) explicitly frame the evaluation as measuring a combined task of detection + captioning and avoid ranking image-level vs. region-level models on the same metrics.

### Minor

- **Ambiguity in the "starting sentence" for captioning evaluation.** The paper states (line 103) that a starting sentence "This is a <Category Name>." is constructed, but does not clarify whether this is prepended to the model's output before scoring, appended to the reference, or used as a system prompt. Since this directly affects n-gram metrics (CIDEr, BLEU-4), the procedure must be specified.

- **Caption statistics could be clearer.** The paper reports 12,873 refined captions (abstract, contributions, Section 3.1) and 22,321 total positive captions (Section 3.1). These are consistent (refined vs. refined+generated), but the three-level breakdown requested by the reviewer — total boxes (42,217) → boxes satisfying the 1024-pixel threshold → captions generated → captions refined — is not provided. Additionally, "For each image, we only select one to perform caption refinement" (line 52) implies ≤14,645 refined captions across 14,645 images, but 12,873 < 14,645; the paper should clarify why some images lack a refined caption (e.g., no box ≥1024 pixels).

- **Size thresholds for bounding box categories undefined.** Section 3.1 reports "24,197 large, 10,555 medium, and 7,465 small bounding boxes" without defining what pixel or relative-image thresholds define these categories.

- **Dataset split ratios not specified.** The paper mentions a "train/val data split" (line 86) and a "validation set" (lines 120, 129) but does not report the number of images/instances in each split or whether the same split is used across all three tasks.

- **Inter-annotator agreement not reported.** While the paper mentions cross-checking verification (Section 3.2), no quantitative consistency metrics (e.g., bounding box IoU agreement, caption similarity) are provided, which is a standard expectation for dataset papers.

- **Proportion of excluded captions in grounding evaluation not reported.** Section 4.3 states that "captions that are negatives, empty, and with no noun phrases detected by nltk package are excluded," but the number/percentage affected by each criterion is not given.

- **Negative captions are provided but not used in any benchmark.** The 12,431 negative captions with 11 property annotations are a novel resource (Section 3.1), but the paper does not benchmark them (grounding explicitly excludes them, line 120). While this is acceptable for a dataset paper, stating their intended future use more explicitly would set appropriate expectations.

- **Dataset license not stated.** For a dataset intended for research release, this omission should be addressed.

### Trivial

- **"First marine dataset to support marine monitoring" is slightly overclaimed.** Existing datasets (WildFish, MAS3K, SUIM) already support monitoring via bounding boxes/masks. The unique contribution — and what should be foregrounded — is the combination of monitoring with detailed instance captions (as is done correctly in contribution 1).

## Nice-to-Haves

- **Crop images for all models in the captioning evaluation** to enable a cleaner comparison of pure captioning ability without the grounding confound. Alternatively, explicitly label the current evaluation as "open-world instance captioning" that measures combined detection+description ability.
- **Use negative captions in at least one diagnostic benchmark** (e.g., measuring whether grounding models correctly reject negative prompts) to demonstrate their utility beyond release-as-future-work.

## Removed Points

These points were flagged by reviewers but are removed per policy:

- **Table 1 showing "Yes(9,458)" for instance caption count.** This is a parser artifact from rendering the table image; the number "9,458" does not appear in the paper text. Per hard rules, formatting artifacts from parsing are not author errors.
- **Missing appendix / supplementary material content.** Per policy, appendix content is stripped by the parser; the original submission contains it. Criticisms about missing details referred to supplementary are not valid as weaknesses.
- **Any claim that cited models/tools/datasets do not exist or are not yet released.** All references cited in the paper are assumed to exist.

## Novel Insights

The most interesting insight from the reviews — and one the paper does not fully exploit — is that the evaluation gap between image-level and region-level VLMs reveals something deeper than a simple benchmark deficiency. When a full-image VLM is asked "describe the object in this figure," its failure on marine instances is simultaneously a failure of visual grounding (it does not know which object to attend to) and a failure of domain-specific captioning (even attending correctly, it lacks marine biological vocabulary). Disentangling these two failure modes would be a valuable research contribution in itself, and the MarineMaid dataset (with its paired instance captions and bounding boxes) is well-positioned to enable precisely this diagnosis.

## Suggestions

1. **Clarify the caption evaluation protocol** — specify whether the "starting sentence" is prepended to the model output, appended to the reference, or used as a system prompt. Show one worked example.
2. **Provide a clear statistics table** showing: total images → total boxes → boxes ≥ 1024 px → captions generated (unrefined) → captions refined, resolving the 12,873 vs. 22,321 vs. 42,217 relationship.
3. **Acknowledge the evaluation confound in instance captioning explicitly** — either re-evaluate image-level VLMs on cropped inputs, or clearly state that the scores measure combined grounding+captioning and refrain from direct model-class comparisons.
4. **Report dataset split sizes** (train/val image and instance counts) for all tasks.
5. **Add inter-annotator agreement metrics** and state the dataset license.

## Score and Decision

The paper's core contribution — a carefully constructed marine dataset with expert-refined instance captions — is solid and fills a genuine gap. The benchmarking effort is substantial and revealing. The main structural concern is the evaluation confound in instance captioning, which is addressable through clearer framing or a simple experimental fix (evaluating all models on cropped inputs). No weaknesses undermine the dataset itself or the paper's primary contribution. The paper merits acceptance with minor revisions focused on clarity and transparency.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>