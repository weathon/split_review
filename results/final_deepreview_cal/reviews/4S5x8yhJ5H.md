Now I have all the evidence I need to write the consolidated review. Let me compile everything.

---

## Summary

VIBEFACE presents a face biometric dataset of 2,250 images and 1,550 videos from 50 demographically balanced subjects, collected under five distinct environmental conditions using three consumer-grade smartphones. Its distinguishing contribution is the inclusion of realistic eKYC-style video scenarios (scenarios 12–18: head rotation, blinking, expression changes, facial occlusions) that are absent from all prior datasets listed in Table 1. The dataset is ethically sourced with informed consent under GDPR and EU AI Act compliance. The paper also reports face detection and verification experiments across the dataset's conditions and demographic subgroups.

## Strengths

- **Unique eKYC video scenarios**: Scenarios 12–18 (Figure 3, Table 2) explicitly replicate electronic Know Your Customer workflows — circular head rotation, directional tilts, blinking, facial expression changes, hand-based occlusions, and sequential face touching. Table 1 confirms no existing dataset provides this content, and this directly addresses a real gap in biometrics research.

- **Systematic and well-documented data collection**: Five sessions (A–E) systematically vary lighting (artificial, flash, natural daylight, weak natural light) plus a dedicated eyeglasses condition (Section 3.3, Table 2). Each participant contributed 45 still images and 31 videos across these conditions, using three consumer smartphones (Xiaomi, iPhone, Samsung). The variety of acquisition modalities is a genuine strength for studying environmental and device robustness.

- **Ethical and legally compliant collection**: The dataset was collected under GDPR and EU AI Act compliance with informed consent, anonymized identifiers, and a controlled-access non-commercial license (Section 3.4). This stands in contrast to web-scraped biometric datasets that have been withdrawn.

- **Intentional demographic design**: Subjects are balanced 50:50 male/female, distributed across four self-identified racial groups (26% African, 26% Caucasian, 24% East Asian, 24% South Asian), and stratified into three age groups (18–30, 31–50, 51–70) per ISO standards (Figure 1).

- **Empirical demonstration of condition sensitivity**: The detection and verification experiments (Tables 3 and 4) show that performance degrades substantially across challenging conditions — e.g., MTCNN detection on off-angle views drops from 0.764 (Session A, artificial light) to 0.577 (Session E, weak natural light), and ArcFace verification on off-angle views drops from 0.509 to 0.433 with eyeglasses (Session C). This demonstrates the dataset's ability to expose condition-dependent performance variation.

## Weaknesses

### Fatal

None.

### Major

- **Verification evaluation lacks impostor analysis — the reported numbers are uninterpretable**: The face verification protocol (Section 4.2) computes cosine similarity between a reference image (front-facing flash photo) and probe frames of the *same subject only*, then reports the fraction of these genuine comparisons exceeding a fixed threshold of 0.5. No impostor (different-subject) comparisons are performed. Without an impostor distribution, the 0.5 threshold is arbitrary: the near-100% success rates for frontal queries (Table 4, e.g., ArcFace FV = 1.000 across sessions) likely indicate only that the threshold is low, but we cannot determine the corresponding false accept rate. A usable verification benchmark must, at minimum, compute genuine and impostor score distributions and report a trade-off metric such as TAR at a fixed FAR or an ROC curve. This structural gap means the verification results in Table 4 do not provide meaningful evidence about the dataset's utility for verification benchmarking. The detection evaluation (Table 3) is not affected by this issue and remains informative.

- **Demographic fairness claims are overstated given the sample size**: With 50 subjects and at most 13 per racial category, subgroup sizes are too small to support robust statistical conclusions about differential performance across demographics. The paper reports detection and verification rates broken down by race, gender, and age group (Tables 3–4) but includes no confidence intervals, standard deviations, or significance tests. Observed differences (e.g., MTCNN detection dropping for African subjects vs. East Asian subjects) are suggestive but cannot sustain claims about bias given the sample. The dataset's demographic balance is a good design choice for a resource of this scale, but the paper overstates what can be concluded from it. The abstract's claim that "VIBEFACE establishes a new benchmark for evaluating the robustness and fairness of biometric verification systems" is not supported by the evidence provided.

### Minor

- **Unsubstantiated Fitzpatrick skin-tone claim**: Section 3.1 states "We also ensured that the skin tones of participants reflect the whole spectrum of Fitzpatrick's scale." Only self-identified race is reported; no skin-tone measurement protocol (spectrophotometer, human annotation against the Fitzpatrick chart) is described. This claim should be removed or backed with evidence.

- **No IoU threshold specified for face detection**: The detection evaluation (Section 4.1) reports "the percentage of frames in which a face was successfully detected" but never specifies what constitutes a successful detection (e.g., an IoU threshold against ground-truth bounding boxes). This makes the detection metric ambiguous.

- **No Limitations section**: The paper lacks a dedicated discussion of its constraints: 50 subjects limit statistical power for demographic subgroup analysis; the studio setting limits ecological validity despite varied lighting; the single reference image type (flash) constrains the verification protocol. The paper currently only mentions limitations of *other* datasets.

- **No uncertainty quantification**: All reported numbers in Tables 3 and 4 are point estimates without variance information, which is particularly problematic for the demographic subgroup breakdowns where sample sizes are small.

### Trivial

- The paper's conclusions mention potential applications for presentation attack detection and deepfake detection (Section 5), which are aspirational and unsupported by any experiments in the paper. This forward-looking remark inflates the paper's scope.

## Nice-to-Haves

- An inter-session consistency analysis would be a natural use of the multi-session design — measuring how verification performance for the same subject changes across different lighting and eyeglasses conditions, rather than only reporting aggregated per-session averages.
- Frame-level annotation quality for video scenarios is not discussed. In dynamic head-rotation videos, some frames may have extreme poses where detection is expected to fail; it is unclear whether such frames are included or filtered.
- The reference image for verification is drawn from the flash session to "emulate a typical document-based authentication setup." A flash-illuminated smartphone photo is not identical to a scanned ID document photo, and this modeling choice merits a brief acknowledgment.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No release plan for maintenance or long-term hosting"** — Removed per hard rule: the paper provides a working dataset access link, and we do not question the existence or availability of cited resources.
- **"Table 1 checkmark criteria are too coarse"** — Removed as a formatting/style nitpick. The table is legible and informative for contextualizing the dataset.
- **"The dataset is not suitable for training large models"** — Removed. This is not a weakness of the paper; the paper explicitly positions the dataset for controlled evaluation, not training.
- **Strength Finder claim about "rigorous demographic balance"** — Modified. The demographic design is intentional and balanced for the scale, but "rigorous" overstates what 50 subjects can deliver.
- **"No inter-session consistency analysis" and "no frame-level annotation quality discussion"** — Moved to Nice-to-Haves. These are enrichment analyses, not core requirements.

## Novel Insights

The paper's insight that eKYC-style video sequences (with natural user behaviors like circular head rotation, blinking, and hand occlusion) are missing from all existing public face biometric datasets is well-supported by Table 1 and genuinely novel. However, this insight would be more impactful if paired with an evaluation protocol that can properly measure verification performance under these conditions — specifically, the paper's failure to include impostor analysis means the community cannot yet use this dataset as a benchmark for verification. The concept is strong; the execution of the evaluation is not yet at the level needed to realize it.

## Suggestions

1. **Redesign the verification protocol with genuine/impostor analysis.** At minimum, define gallery–probe splits (e.g., one enrollment image per subject from Session B, all other frames as probes), compute genuine and impostor similarity score distributions, and report an ROC curve or TAR at a fixed, low FAR (e.g., TAR@FAR=1e-3). This is a straightforward fix using the data already collected, and it would transform the verification section from uninterpretable to informative. Even with 50 subjects, a within-dataset ROC is a standard way to demonstrate dataset utility for controlled comparisons.

2. **Add uncertainty quantification.** For Tables 3 and 4, include standard deviations across subjects or bootstrap confidence intervals. For demographic subgroup comparisons, avoid language implying robust fairness conclusions without supporting statistical tests.

3. **Add a Limitations section** that openly discusses trade-offs: 50 subjects enable deep multimodal capture per individual but limit statistical power for subgroup analysis; the studio setting constrains ecological validity; the dataset is intended for controlled evaluation rather than training.

4. **Remove or ground the Fitzpatrick claim.** If skin tone was measured using the Fitzpatrick chart, describe the protocol; if not, delete the sentence.

5. **Rescope the paper as a dataset resource paper** rather than a finished benchmark paper. The dataset's value as a resource for controlled robustness studies is defensible; the claim of establishing a comprehensive benchmark is premature given the current evaluation.

## Score and Decision

**Round 1 bracket**: The paper sits between ~3.5 and ~6.5 based on comparison with anchors covering face biometric datasets and benchmarks (dEGYODD6iU at 3.67, lAhQCHuANV at 6.33, rhaQbS3K3R at 6.25).

**Round 2 narrowing**: Compared against dataset resource papers in the 3.5–7.0 range:
- ScalePerson (3iGponpukH, 4.75): A dataset paper with a clear gap but evaluation concerns — VIBEFACE has a more clearly differentiated contribution (eKYC videos) but similarly flawed evaluation.
- UDC-VIT (DNBwlQYA90, 6.00): A real-world UDC video dataset with sound evaluation and clear utility demonstration — VIBEFACE is weaker due to its structurally incomplete verification protocol.
- ILLUSION (qnlG3zPQUy, 6.00): A large-scale comprehensive dataset accepted at 6.0 — VIBEFACE has a sharper focus (eKYC) but dramatically smaller scale and inferior evaluation.
- Face-Human-Bench (x1Bk51SCL9, 5.75): A benchmark paper with systematic taxonomy — comparable ambition but more developed evaluation framework.

VIBEFACE is clearly better than the weak-band anchors (dEGYODD6iU at 3.67, Dolm7rrrQd at 4.25) that had both novelty and evaluation issues, but notably weaker than the 6.0-level dataset papers that demonstrated sound evaluation. The paper lands between ScalePerson (4.75) and Face-Human-Bench (5.75), closer to the midpoint given its genuine dataset contribution balanced against a major evaluation gap.

**Final score rationale**: The dataset fills a real gap (eKYC videos) and the collection methodology is thorough and ethically sound. However, the verification evaluation — which is the centerpiece benchmark claim — is structurally flawed (no impostor analysis), and the demographic fairness narrative overreaches relative to the 50-subject scale. These are fixable problems that do not invalidate the dataset's value as a resource, but they do prevent the paper from substantiating its primary claim of establishing a benchmark. A score of 5.0 reflects a contribution with real merit held back by significant but addressable evaluation shortcomings.

**Anchor papers referenced**:
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| dEGYODD6iU | Skin tone PAD | 3.67 | R1 | VIBEFACE has a clearer contribution and better collection methodology |
| Dolm7rrrQd | Neural compression bias | 4.25 | R1 | VIBEFACE provides a concrete resource rather than only identifying a problem |
| lAhQCHuANV | Uncertainty in similarity scoring | 6.33 | R1 | Stronger theoretical contribution and more rigorous evaluation than VIBEFACE |
| 3iGponpukH | ScalePerson dataset | 4.75 | R2 | Similar type; VIBEFACE has more unique contribution but comparably flawed evaluation |
| DNBwlQYA90 | UDC-VIT dataset | 6.00 | R2 | Better evaluation methodology; VIBEFACE has more novel content but weaker evaluation |
| qnlG3zPQUy | ILLUSION dataset | 6.00 | R2 | Much larger scale and more comprehensive evaluation than VIBEFACE |
| x1Bk51SCL9 | Face-Human-Bench | 5.75 | R2 | More systematic evaluation framework than VIBEFACE |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>