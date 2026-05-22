Now I have sufficient calibration context. Let me finalize my synthesis and write the review.

## Final Review of VIBEFACE

## Summary

VIBEFACE is a multimodal dataset of 2,250 images and 1,550 videos from 50 subjects, designed to support face verification research for electronic Know Your Client (eKYC) scenarios. It is the first publicly available dataset to include eKYC-style video recordings alongside still images, with balanced demographic representation across gender (50:50), four racial groups (~25% each), and three age bands. Data was collected ethically with informed consent and GDPR/AI Act compliance.

## Strengths

- **First publicly available dataset targeting authentic eKYC-style video scenarios.** Table 1 shows that of nine compared datasets, only VIBEFACE includes eKYC-style verification videos. The 18 defined scenarios (circular head rotation, blinking, expression changes, partial occlusions, etc.) directly mirror the actions required in real eKYC workflows, filling a genuine gap that prior datasets (MOBIO, OULU-NPU, SOTERIA, WMCA) do not address.

- **Demographic balance that is rare in existing biometric datasets.** Table 1 confirms VIBEFACE is the only dataset among the nine compared that simultaneously provides gender balance (25M/25F), race balance (13 African, 13 Caucasian, 12 East Asian, 12 South Asian), and age balance (three bands with substantive representation in each). The paper provides per-demographic breakdowns of detection and verification results (Tables 3 and 4), enabling analyses that prior datasets in this niche do not support.

- **Exemplary ethical and legal compliance.** Section 3.4 documents informed consent, anonymization via randomized identifiers, right to withdraw, and compliance with GDPR and the EU AI Act. This stands in sharp contrast to the withdrawn internet-scraped datasets (MS-Celeb-1M, VGGFace2, MegaFace). The controlled-access release agreement is appropriate for sensitive biometric data.

## Weaknesses

### Major

1. **The 50-subject sample size fundamentally limits the dataset's ability to support its stated purposes.** The paper claims VIBEFACE enables evaluation of "fairness" and "generalizability" of face verification systems. With 50 subjects total, the four racial groups contain only 12–13 participants each, and the age–gender cells contain as few as 6–10 subjects. Per-group verification rates computed over such small sets have no statistical grounding — a single subject misclassified can shift a group mean by several percentage points (e.g., MagFace's Caucasian verification at 0.925 in the blinking scenario vs. 1.000 for East Asian and South Asian groups). No confidence intervals, bootstrapping, or statistical tests are reported, so observed demographic differences cannot be distinguished from sampling noise. While comparable datasets in this niche (OULU-NPU: 55, HQ-WMCA: 51) also have small subject counts, those datasets do not claim to benchmark fairness across demographic subgroups. The paper should either (a) substantially expand the subject pool, or (b) recalibrate its claims to acknowledge that demographic comparisons are illustrative rather than statistically reliable.

2. **The evaluation protocol uses a non-standard fixed threshold (0.5) for both ArcFace and MagFace.** The paper reports verification success as the percentage of frames exceeding a cosine similarity of 0.5. ArcFace and MagFace produce different output distributions (MagFace's loss explicitly calibrates feature magnitudes), so the same threshold is not comparable across models. Standard practice in face verification is to report TAR@FAR curves, AUC, or EER. Additionally, no development/validation split is used to calibrate the threshold per model. This makes it impossible to interpret the relative performance of the two models or to compare results against existing benchmarks. The paper should adopt proper evaluation metrics and provide per-model threshold calibration on a held-out set.

3. **No cross-dataset comparison is provided to demonstrate the dataset's unique value.** The paper argues that VIBEFACE addresses limitations of existing datasets (MOBIO, OULU-NPU, SOTERIA) such as lack of eKYC scenarios and demographic imbalance. However, it provides no experiment showing that VIBEFACE reveals different verification patterns or new insights compared to these datasets. A cross-dataset comparison — running the same verification models on comparable samples from existing datasets — would concretely demonstrate whether the eKYC scenarios or demographic balance offer informational value beyond what existing resources already provide. Without this, the benchmarking experiments primarily show that off-the-shelf models perform as expected on clean studio data.

### Minor

4. **Tension between the "realistic eKYC" framing and the controlled studio collection.** The introduction motivates the dataset by describing eKYC as involving "unconstrained conditions — at home, in variable lighting, and across heterogeneous mobile devices." However, Section 3 states data was "conducted in a controlled studio environment... supervised by trained operators." While the lighting conditions are systematically varied (cool white, warm yellow, diffuse softbox), these are laboratory manipulations rather than authentic at-home variability. The dataset is better described as a "controlled, eKYC-mimicking studio dataset" than as capturing "realistic eKYC conditions." This framing mismatch should be corrected.

5. **Detection results show ceiling effects.** RetinaFace achieves 1.000 detection rate for almost all image-based conditions and near-perfect rates for video. This is not a flaw in the dataset — it reflects that modern detectors handle clean, well-framed faces — but it undercuts the claim that VIBEFACE is "challenging" for detection and limits the informativeness of the detection benchmark. The verification results (Tables 4) are more informative and should be the paper's focus.

6. **No analysis of within-subject variation.** The paper does not report intra-subject similarity distributions across sessions (e.g., how much does the same subject's appearance vary between artificial light, flash, natural light, and glasses sessions?). Such analysis would demonstrate whether the dataset actually presents meaningful verification challenges for modern models.

### Trivial

7. Section 3 states "no additional pre- or post-processing was applied" but then describes format conversion (HEIC to JPG, MOV to MP4). This is a minor inconsistency.

## Nice-to-Haves

- Reporting TAR@FAR or AUC metrics alongside or instead of the fixed-threshold approach.
- A cross-dataset experiment comparing VIBEFACE verification patterns with MOBIO or SOTERIA.
- Bootstrapped confidence intervals for all per-demographic results.
- An analysis of whether eKYC video scenarios (scenarios 12–18) elicit different verification difficulty than static images, which would directly support the paper's central claim about eKYC value.

## Removed Points

The following points from the harsh critic review were removed or downgraded:
- **Criticism about the "no post-processing" claim being undercut by format conversion** → Moved to Trivial (it is a minor inconsistency, not a substantive flaw).
- **"No study of dataset's value for training"** → Removed. A dataset paper is not required to demonstrate training utility, especially for a resource this size; evaluating pre-trained models is standard for a benchmark resource paper.
- **Criticism about using flash session photo as reference** → Removed as speculative without evidence of harm; using a consistent, high-quality reference is standard practice.
- **"Race categories omit many populations"** → Weakened. At 50 subjects, four groups already stretch statistical power; adding more categories without more subjects would make the problem worse. The paper acknowledges the limitation.
- **"Scenario exclusion (11, 17, 18) reduces coverage"** → Removed. The paper provides a reasonable justification (scenario 11 has incomplete coverage across sessions; 17 and 18 involve occlusion that makes detection ill-defined).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Expand the dataset to at least 150–200 subjects to make per-demographic analyses statistically meaningful. At current size (12–13 per racial group), the demographic fairness analysis that is the paper's headline feature is not credible.
2. Replace the fixed-threshold percentage metric with TAR@FAR curves or AUC, with per-model threshold calibration on a held-out set.
3. Add a cross-dataset experiment (run the same models on MOBIO or SOTERIA samples) to empirically demonstrate that VIBEFACE reveals patterns these datasets miss.
4. Soften claims from "fair and generalizable verification benchmark" to something like "a novel eKYC-focused resource with balanced demographics, enabling preliminary fairness analyses."

## Score and Decision

**Calibration Report:**

| Round | Anchor ID | Avg Score | Comparison |
|-------|-----------|-----------|------------|
| 1 | NWvsm2VxAM | 3.00 | Rejected; synthetic biometric dataset paper — weaker than VIBEFACE |
| 1 | uW3tNSx7PZ | 2.50 | Rejected; federated learning for biometrics — less relevant, clearly weaker |
| 1 | razAcpFapu | 3.00 | Rejected; face reconstruction attack — weaker contribution |
| 1 | YZ7NWYBd5z | 3.00 | Rejected; deepfake detection — methodology paper, not comparable |
| 1 | 0y3hGn1wOk | 5.40 | Accepted; VLM unlearning benchmark with 400 synthetic faces — similar scale concerns raised, comparable quality |
| 1 | x1Bk51SCL9 | 5.75 | Rejected; face/human benchmark from existing data — stronger evaluation but no new data, comparable tier |
| 1 | C6d9S2lYFN | 3.80 | Rejected; deepfake detector assessment — weaker contribution |
| 1 | TzAJbTClAz | 6.75 | Accepted; fairness benchmark with 45K experiments — substantially stronger evaluation |
| 1 | SctfBCLmWo | 8.00 | Accepted; dataset bias analysis — much stronger and more mature |
| 1 | vaEPihQsAA | 7.60 | Accepted; audio-driven talking body — method paper, not comparable |
| 1 | z8sxoCYgmd | 8.00 | Accepted; synthetic data detection benchmark — much larger scale, stronger |
| 1 | WyEdX2R4er | 8.00 | Accepted; visual data-type understanding — stronger execution |
| 2 | dEGYODD6iU | 3.67 | Rejected; PAD skin tone fairness — weaker methodology, comparable fairness motivation |
| 2 | WjxgruI6A2 | 3.67 | Rejected; cross-modal biometrics — less relevant |
| 2 | CCo8ElCT7v | 4.25 | Rejected; ViT vs CNN comparison — comparable rigor level but no dataset contribution |
| 2 | RoN6NnHjn4 | 6.00 | Accepted; synthetic face generation — stronger technical contribution, larger scale |
| 2 | XhyCPEnlCa | 4.25 | Rejected; deepfake dataset limited by single generation method — most structurally similar to VIBEFACE in profile (dataset with a good idea but limitations) |
| 2 | qnlG3zPQUy | 6.00 | Accepted; large multimodal deepfake dataset — substantially larger scale, stronger evaluation |

**Round 1 bracket:** Initial plausible range 4–6.

**Round 2 narrowing:** Compared against anchors in the 3.67–6.00 range. VIBEFACE is clearly stronger than the 3.67–4.25 rejected papers (which had more fundamental methodological or contribution issues). It is weaker than the accepted 5.40–6.75 papers (which had larger scale, stronger evaluations, or both). Compared to HiDF (4.25, Reject) — the most structurally similar dataset paper — VIBEFACE has a clearer niche gap (first eKYC dataset) and better ethics/demographics. Compared to FIUBench (5.40, Accept) — which was accepted despite similar scale concerns (400 synthetic faces) — VIBEFACE has weaker evaluation methodology (fixed threshold, no cross-dataset comparison) and a smaller subject pool.

**Final position:** Between the 4.25 reject tier and the 5.40 accept tier. Closer to HiDF's profile (genuine niche contribution but execution limitations that prevent acceptance at a top venue) than to FIUBench's.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>