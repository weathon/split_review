I've now verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces FHA-Kitchens, a dataset for fine-grained hand action recognition in kitchen scenes. The dataset comprises 30,047 frames from 2,377 clips derived from 30 YouTube videos covering 8 dish types. Its core innovation is a 9-dimensional annotation scheme: three sub-interaction regions (left hand–object, right hand–object, object–object) each annotated with a triplet `<subject, action verb, object>`, active–passive object relationships, and contact-area nouns, yielding 878 action triplet classes, 131 verbs, and 384 nouns, plus 198,839 bounding boxes across 9 types. The paper benchmarks detection models (Faster-RCNN, YOLOX, Deformable DETR), action recognition models (TSN, SlowFast, VideoSwin, VideoMAE V2, Hiera), and domain generalization tracks for interaction region detection.

## Strengths

- **Exceptionally fine-grained annotation scheme**: The 9-dimensional action representation — triplets across three sub-interaction regions with active–passive distinctions and contact-area nouns — goes well beyond the verb+noun flat labels of prior datasets (EPIC-KITCHENS, AVA, Kinetics). This yields 878 action categories (52× more than the source Kinetics 700_2020), and the paper provides clear evidence of this granularity leap via Table 1 and Section 3.2.

- **Richer spatial annotations than any comparable dataset**: With 198,839 bounding boxes across 9 types (hand boxes, interaction region boxes, interaction object boxes), including 66,402 interaction region boxes and 82,691 interaction object boxes — averaging 5 additional annotation types per frame over EPIC-KITCHENS — the dataset directly supports region-level hand action analysis that prior datasets do not enable.

- **Multi-track benchmarks establish concrete baselines and reveal real difficulty**: The SL-AR track shows large models (VideoMAE V2, Hiera) achieve far lower accuracy on FHA-Kitchens than on coarse-grained Kinetics 400, and the DG tracks (Tables 5, 6) document ≥15 mAP drops on unseen categories. These results demonstrate that the dataset captures challenges existing benchmarks do not.

- **Long-tail distribution explicitly documented**: Section 3.3 and Figures 3–4 characterize the long-tail property (e.g., the most frequent triplet appearing 9,887× vs. rarer ones), making the dataset directly useful for few-shot and out-of-distribution generalization research.

- **Rigorous annotation pipeline described**: 10 annotators, parallel annotation via Amazon Mechanical Turk and LabelBee, and three rounds of cross-checking and corrections are documented in Section 3.2.

## Weaknesses

### Major

- **No quantitative inter-annotator agreement reported**. This is the most consequential gap for a dataset paper. The annotation scheme is complex: nine bounding-box types across three sub-interaction regions, triplet actions with contact-area nouns, and an active–passive distinction. The paper describes a workflow ("three rounds of cross-checking and corrections," Section 3.2) but provides no metric — Krippendorff's alpha, Cohen's kappa, IoU agreement, or triplet-component agreement — to quantify labeling consistency. Without this, readers cannot assess whether the 878 triplets and 198,839 bounding boxes are reliable or contain systematic noise. Since the dataset is the paper's central contribution, this omission significantly undermines confidence in all downstream experiments. **This is fixable in revision** by computing and reporting agreement statistics on a representative subset, but without them the contribution is incomplete.

- **Dataset derived from only 30 original videos covering 8 dish types**, all sourced from Kinetics 700_2020. This severely limits diversity in backgrounds, viewpoints, lighting, camera motion, and cooking styles. The paper acknowledges this (Section 5, line 176: "Our dataset may be slightly smaller in terms of the number of videos") but the claim of "rich diversity" (line 183) is difficult to sustain. The DG tracks test generalization within this narrow domain, not to broader kitchen scenes. The paper would be stronger if it either scaled up or candidly repositioned the dataset as a diagnostic/probe benchmark for fine-grained annotation rather than a general-purpose benchmark for hand action recognition. This does not invalidate the dataset's contribution but bounds its scope.

### Minor

- **Benchmark insights are shallower than the "compelling empirical evidence" framing suggests.** The key findings are: (1) detecting interaction objects is harder than interaction regions, (2) all models perform worse than on Kinetics 400, (3) pre-training helps, (4) detection models overfit to seen categories in DG. These are largely expected outcomes given the fine-grained and long-tail nature of the data. The paper does not offer deeper analysis — confusion patterns between verbs, impact of long-tail subsampling on head vs. tail recall, failure-case analysis (small objects vs. occlusion), or experiments leveraging the unique triplet structure. The baselines are useful but the verbal framing overstates their insightfulness. This is a common pattern in dataset papers but still worth noting.

- **The SL-AR evaluation protocol could be more complete.** While the paper states that clips represent distinct triplet classes (line 17), uses standard toolkits (MMAction2), and reports Top-1/Top-5 accuracy over 878 classes (line 109), it does not specify how many frames are sampled per clip during training/testing, what the input format is, or how the 878 triplet classes are mapped to model outputs (joint 878-way classification vs. separate verb/noun/subject predictions). These details matter for reproducibility. The subject component ("hand_left"/"hand_right") may also be nearly deterministic given the interaction region, which could inflate accuracy — this is worth discussing.

### Trivial

- **The dataset release page has no URL or license stated.** The paper says "will be released on the FHA-Kitchens project website" (line 4) but gives no URL or terms of use. Since the data derives from Kinetics 700_2020 (which has its own license), stating the license is important for adoption. This is a practical detail easily added.

## Nice-to-Haves

- **Exploit the unique structure of the annotations**: The dataset offers three sub-interaction regions and an active–passive distinction, but the current benchmarks (flat detection, standard action recognition) do not leverage these. An experiment that reasons across the triplet structure — e.g., predicting the O-O action conditioned on L-O and R-O actions, or analyzing whether active–passive labeling helps resolve ambiguous interactions — would demonstrate the value of the annotation scheme rather than treating it as a set of flat classes.

- **Characterize the long-tail with model behavior**: Reporting per-category recall for head vs. tail triplets, or plotting accuracy vs. log frequency, would turn the long-tail property from a statistical observation into diagnostic evidence. A simple class-balancing baseline (weighted loss or oversampling) would make the "avenues for future research" claim concrete.

- **Mask annotations from SAM** (Section 3.2) are mentioned but not used in any experiment. Including them as a future resource is fine, but the claim that they "can be used for action segmentation relevant tasks" would be strengthened by even one illustrative experiment.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"123 new action verbs" ambiguity**: The reviewer questioned whether "new" was ambiguous. However, line 98 explicitly states "Compared to the original coarse-grained annotations in Kinetics 700_2020... introduced 123 new action verbs," making the comparison clear. The verb vocabulary sourcing (line 80) is a separate description of construction methodology. **Removed** — the paper is clear on this point.

- **Tables not visible / numerical values missing**: This is a parser artifact from PDF extraction. The original submission contains the tables. **Removed** per hard rules on parser artifacts.

- **SAM mask annotations not used in experiments**: The reviewer noted this as an unsupported claim, but also acknowledged it is "fine as a resource for future work." This does not constitute a weakness — it is an offered resource, not a claimed experimental result. **Removed**.

- **Critique that the DG track "mismatches the paper's framing"**: The abstract and intro explicitly state the DG track is "for hand interaction region detection" (lines 4, 19). The paper is transparent about what each track evaluates. The title's emphasis on "fine-grained hand action recognition" refers to the dataset's purpose, not to every benchmark track. **Removed** — the paper correctly scopes its tracks.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tension between the paper's ambition (a general benchmark for fine-grained hand action recognition) and its actual scope (a small-video-source, single-domain diagnostic dataset), but this is a framing issue the authors can resolve, not a novel analytical insight.

## Suggestions

1. **Compute and report inter-annotator agreement** — Krippendorff's alpha for triplet components and IoU-based metrics for bounding boxes, on a representative subset. This is the single highest-leverage improvement and should be prioritized before any resubmission.
2. **Acknowledge the 30-video/8-dish limitation more explicitly in the abstract and introduction**, and reframe the dataset as a fine-grained diagnostic/probe benchmark rather than a general-purpose one. Alternatively, scale the dataset to more videos/dish types.
3. **Add clip construction details to the SL-AR track** (frames per clip, sampling strategy, how the 878-class prediction is structured from the triplet components).
4. **Run one analysis that exploits the triplet structure** — e.g., confusion analysis of verbs, head-vs-tail recall, or analysis of how O-O actions relate to L-O/R-O actions.
5. **Include a brief ablation with class-balancing** (weighted loss or oversampling) to give concrete evidence for the long-tail challenge.
6. **State the dataset license and provide a URL** in the paper.

## Score and Decision

The FHA-Kitchens dataset offers a genuinely novel and thoughtful annotation scheme for fine-grained hand actions, with richer spatial and categorical granularity than existing datasets. The benchmarks serve as reasonable starting baselines. However, the paper is not ready for acceptance in its current form. The absence of any inter-annotator reliability metric is a structural gap that undermines trust in the annotation quality — especially given the complexity of the 9-dimensional scheme. The small number of source videos (30) and dish types (8) further limits the dataset's generality, and the framing oversells what is currently demonstrated. These issues are substantively fixable, and a revised version with agreement statistics, sharpened scope, and fuller evaluation details could be a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>