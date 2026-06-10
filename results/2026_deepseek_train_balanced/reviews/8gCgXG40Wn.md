Below is the consolidated final review.

---

## Summary
IndianRoad is a large-scale dashcam video dataset from India comprising 1,231 one-minute clips with over 13 million bounding boxes across 16 actor categories and 16 action types. The dataset is designed to benchmark perception methods in dense, VRU-heavy traffic environments underrepresented in existing datasets, with 41.13% of instances being vulnerable road users (vs. 23.71% in Waymo). The paper benchmarks five tasks — tracking, detection, spatiotemporal action localization, video moment retrieval, and multi-label action recognition — and reports performance degradation across all five compared to existing benchmarks.

## Strengths
- **Quantifiably higher VRU representation than comparable datasets**: The paper reports 41.13% VRU instances versus 23.71% in Waymo (abstract, line 4). This is a concrete, measured difference from the most widely used prior dataset, directly supporting the claim that IndianRoad fills a gap in representing VRU-dense, non-Western traffic.
- **Dense manual annotation at unprecedented scale for traffic video**: IndianRoad provides over 13 million bounding boxes for actors and over 1.6 million boxes annotated with both actor identification and action details (Section 1, Table 1, line 30). This is far beyond the annotation density of comparably sized traffic datasets.
- **16 complex action types beyond simple atomic actions**: IndianRoad's action taxonomy includes cut-in, overtaking, U-turn, zigzag movement (Table 1, Figure 3), which are qualitatively more complex than the human-centric actions in prior datasets like AVA (stand, sit, watch, walk). This is explicitly documented and contrasted in Section 1.
- **Multi-task annotation scope**: The dataset supports tracking, detection, STAL, VMR, and M-VAR out of the box (Figure 1), with annotations including GPS trajectories, camera intrinsics, road conditions, and environmental metadata (Sections 2.1–2.2).
- **Privacy protection via face/license plate blurring**: The paper commits to using RetinaFace for face detection and a dedicated license plate blurring method (Section 2.2, line 94), addressing a practical hurdle for releasing traffic video data.

## Weaknesses

### Fatal
None.

### Major
- **Benchmarking experiments are confounded and do not cleanly demonstrate that IndianRoad is "harder"**: All five experimental comparisons compare IndianRoad results against numbers on other datasets where the models were pre-trained or originally developed. The detection comparison (Section 3.2) uses Swin-T pre-trained on ImageNet + COCO, fine-tuned on IndianRoad, then compared to COCO results — the model has seen COCO during pre-training. The tracking comparison (Section 3.1) uses ARTrack pre-trained on GOT-10k and then evaluated zero-shot on IndianRoad. The VMR, STAL, and M-VAR comparisons (Sections 3.3–3.5) all compare IndianRoad results against published numbers on fundamentally different domains (indoor activities, movie clips) where the models were originally developed. These comparisons conflate domain shift, pre-training confounds, and genuine dataset difficulty. The paper's central claim that "IndianRoad is harder" would be better supported by controlled experiments: e.g., training the same detector on IndianRoad and Waymo/BDD100K using identical protocols.

- **No annotation quality metrics reported**: For a dataset with 13M+ bounding boxes and 1.6M action-annotated boxes, the paper provides zero quality control metrics. There is no inter-annotator agreement, no annotation error rate, no description of annotator training or qualification, no discussion of quality assurance workflows (Section 2.2, line 79). For a dataset paper at a top venue, the reliability of labels is foundational. Without quality metrics, readers cannot assess whether the reported performance drops reflect genuine dataset difficulty or annotation noise.

- **No experimental comparison to peer driving-domain datasets**: The paper compares IndianRoad to COCO (general object detection), GOT-10k (generic tracking), AVA (movie actions), and Charades-STA (indoor activities). The only driving dataset mentioned is Waymo (for VRU percentage in the abstract), but no experiment runs the same detector, tracker, or action recognition model on Waymo, BDD100K, or nuScenes data. Since IndianRoad is a driving/road-scene dataset, comparisons to these driving-domain peers would be far more informative than cross-domain comparisons to COCO or Charades. This is a critical omission for establishing the dataset's unique value proposition.

### Minor
- **Overly broad framing that mischaracterizes existing datasets**: The paper repeatedly characterizes existing datasets as having "structured settings with clear foreground-background separation" (line 20) and "human actors performing isolated actions in simplistic and controlled settings" (line 15). These characterizations do not accurately describe Waymo, BDD100K, nuScenes, or Cityscapes, which all feature complex multi-agent urban scenes with occlusions, cluttered environments, and dynamic lighting. The paper also states that "Asian scenarios are far more complex" (line 4) as fact rather than as a testable hypothesis. The contribution would be stronger if framed precisely: IndianRoad fills a gap specifically for Indian traffic patterns with high VRU density, rather than claiming a monopoly on "unstructured environments."

- **"Every visible object is annotated" is unqualified**: Section 1 (line 24) states "every visible object is annotated," but no minimum size threshold, distance cutoff, or visibility criteria are specified. Without these details, the claim is ambiguous.

- **Template-based VMR queries are narrow**: The 26,863 queries follow patterns like "Car is doing lane changing with clear lane markings" and "MotorBike runs in the wrong lane" (Section 3.3, line 126). These are template-generated and lexically narrow, which limits the natural language diversity of the VMR benchmark.

- **STAL results conflate detection and recognition errors**: The ACAR-Net pipeline (Section 3.4) depends on the Swin-T detector from Section 3.2. The 6.3% mAP could reflect detection failures, recognition failures, or both, but these are never disentangled.

### Trivial
None.

## Nice-to-Haves
- A transfer learning experiment (train on IndianRoad, evaluate on Waymo/BDD100K) would directly demonstrate the value of IndianRoad's diversity for improving generalization.
- Per-class instance counts across train/test splits would improve dataset documentation.
- Breakdown of environmental conditions (rain/night/high-density clips) would substantiate the claim of broad coverage.

## Removed Points
These points are flagged to be removed per the filtering rules; treat them with caution:
- Critic's mention that "Dataset availability — no URL, license, or download instructions are mentioned" — per hard rules, removed as questioning release status/availability.
- Critic's suggestion that the paper should add "more annotators, training, disagreement resolution" as a core weakness — the existing criticism (no quality metrics) already captures the issue; the specific pipeline suggestions are scope creep.
- Strength Finder's characterization that all performance drops are "strong, reproducible evidence that the dataset is genuinely harder" — this conflicts with the verified Major weakness about confounded comparisons, so the strength is retained but the "genuinely harder" framing is removed.
- Trivial typos — removed per hard rules about formatting artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a useful meta-point: a dataset paper whose sole experimental strategy is "models perform worse on our dataset" must control for pre-training, domain shift, and evaluation protocol differences, or the results are uninformative. The reviews do not add novel analytical insights beyond this.

## Suggestions
1. **Rewrite the experiments to include at least one controlled comparison against a driving-domain peer dataset** (Waymo detection/tracking benchmarks are the obvious choice). Run the same detector and tracker on IndianRoad and Waymo under identical evaluation protocols.
2. **Add annotation quality metrics**: report inter-annotator agreement (IoU for bounding boxes, Cohen's κ for action labels), annotator counts, training procedures, and any quality assurance pipeline.
3. **Tone down the claim that IndianRoad is "harder"** based on the current confounded comparisons. Frame the experiments as demonstrating domain shift / lack of generalization, which is itself informative but does not require the "harder" conclusion.
4. **Qualify "every visible object is annotated"** with minimum size thresholds and visibility criteria.
5. **Add per-class statistics** across train/test splits for all actor and action categories.

## Score and Decision
Given the dataset's genuine contribution in terms of scale, VRU density, and multi-task annotation scope — but weighed against the major weaknesses (confounded experiments, no annotation quality metrics, missing comparisons to driving-domain peers) that significantly undermine the paper's central claims — the paper does not meet ICLR acceptance standards in its current form. The dataset itself has clear potential value, but the paper's experimental validation and documentation are insufficient.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>