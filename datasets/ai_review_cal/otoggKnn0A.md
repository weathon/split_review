- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have all the information needed. Let me synthesize the final consolidated review.

## Summary

FHA-Kitchens is a dataset for fine-grained hand action recognition in kitchen scenes, comprising 30 videos (84 minutes) sourced from Kinetics 700_2020, yielding 2,377 clips, 30,047 frames, and 878 action triplets across 8 dish types. The dataset's core innovation is a 9-dimensional annotation scheme that divides hand interactions into three sub-regions (left hand-object, right hand-object, object-object), represents each action as a triplet ⟨subject, verb, object⟩, and captures active-passive relationships and contact areas. The paper benchmarks representative detection and recognition models across supervised learning and domain generalization tracks, showing that even large VideoMAE V2 models achieve only 22.3% Top-1 accuracy, demonstrating genuine difficulty.

## Strengths

- **Novel 9-dimensional annotation scheme for hand actions.** The paper introduces a structured representation of hand interactions by decomposing them into three sub-interaction regions (L-O, R-O, O-O), each annotated with ⟨subject, verb, object⟩ triplets plus active-passive roles and contact areas. Table 1 (referenced in text) shows FHA-Kitchens has action dimension 9 while all prior datasets have 0–2 dimensions. This is a genuine conceptual contribution that could influence future dataset design.

- **First benchmarking of domain generalization for hand interaction region detection.** The intra- and inter-class DG tracks (Section 4.4, Tables 5–6) are novel evaluations not present in prior action detection datasets. The results show a minimum 15 mAP drop on unseen sub-categories (Table 5), providing the first empirical evidence of this specific challenge.

- **High annotation throughput yields substantial fine-grained categories despite modest video count.** The dataset contains 878 action triplets, 131 verbs, 384 nouns, and 198,839 bounding boxes (49,746 hand boxes, 66,402 interaction region boxes, 82,691 interaction object boxes). This is a materially larger and more fine-grained label space than existing hand-action datasets (e.g., EPIC-KITCHENS, MPII Cooking), even if the source video count is limited.

- **Empirical evidence that the task is genuinely hard for SOTA models.** Table 4 shows VideoMAE V2-huge with pre-training achieves only 22.3% Top-1 accuracy. Models consistently perform worse than on coarse-grained benchmarks, validating that fine-grained hand action recognition remains an open challenge.

## Weaknesses

### Major

- **No inter-annotator agreement statistics reported.** The paper describes "three rounds of cross-checking and corrections" (Section 3.2) but provides no quantitative measure of annotation reliability (e.g., Cohen's κ or Krippendorff's α) for any of the nine annotation dimensions. Given the complexity of the scheme—distinguishing contact areas (e.g., "carrot_end" vs. "carrot"), assigning active/passive roles, and labeling three sub-region bounding boxes per frame—it is essential to demonstrate that different annotators produce consistent labels. Without this, the "high-quality annotations" claim is unsupported, and the dataset's trustworthiness for benchmarking is uncertain.

- **Data split methodology creates risk of temporal leakage.** The paper states the dataset was "randomly divided into disjoint train, validation, and test sets, with a video clip-based ratio of 7:1:2" (Section 3.3). Since clips are derived from only 30 source videos and defined by action triplet classes (Section 3.1), multiple clips likely originate from the same video. If clips from the same video appear in different splits, frames will be highly correlated (same background, lighting, object states), artificially inflating performance and compromising benchmark validity. The paper does not clarify whether splits were performed at the video level or the clip level, nor whether any measures were taken to prevent leakage.

- **Limited dataset scale constrains its utility as a general benchmark.** The dataset derives from 30 YouTube videos (84 minutes) covering 8 dish types, all from Kinetics 700_2020's kitchen subset. This narrow source pool means the visual diversity (backgrounds, camera viewpoints, lighting, cuisine types, kitchen layouts) is inherently limited. With ~34 frames per action triplet on average and a long-tail distribution, many categories have very few instances. While the paper acknowledges being "slightly smaller in terms of the number of videos" (Section 5), the scale limitation is structural: the dataset currently cannot support robust evaluation of fine-grained hand action recognition across diverse cooking scenarios. The claim that it "paves the way for future research" is premature at this scale.

### Minor

- **The "52 times" claim is misleading.** The paper states the dataset "increased the number of action categories by 52 times" compared to Kinetics 700_2020 (Section 3.3). However, this compares FHA-Kitchens' 878 fine-grained triplets (subject-verb-object combinations) against what must be a small number of kitchen-relevant coarse categories in Kinetics. These are fundamentally different kinds of labels (fine-grained compositional triplets vs. coarse action classes), so the 52× figure is an apples-to-oranges comparison. The claim inflates perceived progress.

- **No dataset release details provided.** The abstract states the "dataset will be released on the FHA-Kitchens project website" but provides no URL, license, or release timeline. For a dataset paper, concrete release information is a minimum requirement for the community to evaluate and use the resource.

- **Contact area annotation guidelines not reported.** The annotation scheme includes fine-grained contact areas (e.g., "carrot_end" vs. "carrot", "utility-knife_handle" vs. "utility-knife"), but the paper does not report how many unique contact-area labels exist, how annotators were instructed to determine boundaries, or whether contact-area labeling was reliable. This dimension of the annotation is the least explained.

### Trivial

- **Per-category instance counts not provided.** The paper shows aggregate distributions (Figures 3–4) and mentions the long-tail property qualitatively, but does not report the number of instances per action triplet category (e.g., Gini coefficient, head-vs-tail frequency breakdown). This information is needed for users planning to work with the dataset.

## Nice-to-Haves

- The paper could strengthen the positioning by including a brief quantitative estimate of diversity coverage (e.g., how many distinct kitchen backgrounds, camera angles, or cuisines are present) rather than only reporting resolution and FPS statistics.
- The experiments could be augmented with oracle oracle analyses (e.g., how much performance drops when removing the triplet structure or contact-area information) to directly validate the value of the annotation scheme.

## Removed Points

*These points were raised by reviewers but are removed with brief justification:*

- *"The 87% resolution statistic is misleading—it's a property of the subset, not an intentional curation."* → REMOVED. The paper simply reports this as a descriptive statistic of what was collected; it does not claim this was intentional curation.
- *"The connection to Kinetics 700_2020 is ambiguous."* → REMOVED. The paper is clear: raw videos from Kinetics were used, and all original annotations were discarded. No ambiguity.
- *"More results are in the appendix but cannot be evaluated."* → REMOVED per instructions: appendix content is stripped by the parser and existed in the original submission.
- *"The introduction sets expectations of a 'large-scale benchmark' that the dataset does not deliver."* → REMOVED. The phrase "it is desirable to establish a large-scale benchmark" (line 10) is a general aspiration, not a claim about FHA-Kitchens. The paper never calls FHA itself "large-scale."
- *"The experiments do not reveal anything that was not already obvious."* → REMOVED. The DG tracks (intra- and inter-class) are novel evaluations that have not been previously studied for hand interaction region detection. The results showing a minimum 15 mAP drop on unseen sub-categories are not obvious prior to this work.
- *"The human finder finds similar weaknesses from other papers"* → Not applicable; no such content was in this review.
- *"The 'Strengthening the Paper on Its Own Terms' suggestions"* → These are absorbed into weaknesses/nice-to-haves where relevant.

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the annotation scheme is the paper's primary contribution and is genuinely novel, but dataset papers are evaluated on the resource's utility and reliability. The harsh critic's concerns about scale and IAA reflect this genre mismatch—the paper presents the annotation methodology and preliminary benchmarks as if the contribution is a finished resource, but the evidence only supports a contribution at the methodology/proof-of-concept level. The strength finder correctly identifies the 9-dimensional representation and DG benchmarking as concrete advances, but these strengths do not compensate for the lack of annotation reliability metrics and the unresolved data-split ambiguity. The core unresolved question is whether the annotation scheme itself is robust enough to serve as a template for future dataset construction, and that cannot be assessed without IAA. The paper would be stronger if it repositioned itself as introducing an annotation methodology with a preliminary dataset, rather than as a benchmark dataset ready for community use.

## Suggestions

1. **Compute and report inter-annotator agreement** on a held-out subset (e.g., 200–500 frames annotated by at least 3 annotators) for all nine annotation dimensions. This is the single most important missing piece.
2. **Clarify and fix the data split procedure.** Confirm whether splits are at the video level (preferred, to avoid leakage) or clip level. If clip-level splits were used with multiple clips from the same video, re-split at the video level and re-run all benchmarks.
3. **Include a limitations paragraph** that honestly discusses the dataset's narrow source (30 videos from a single dataset, 8 dishes, all from YouTube cooking tutorials) and the implications for generalization.
4. **Provide concrete release plans** (URL, license, expected release date).
5. **Either substantially expand the dataset** (to at least 100+ source videos with more dish diversity) **or reposition the paper** as primarily contributing the annotation methodology and protocol, with the current data as a preliminary instantiation. The current framing as a benchmark dataset overpromises.
