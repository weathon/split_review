Now I have sufficient calibration context. Let me produce the final consolidated review.

## Summary

VIBEFACE introduces a multimodal face dataset (2,250 images, 1,550 videos, N=50 subjects) designed specifically to include eKYC-style video scenarios (head rotation, blinking, face touching, etc.) alongside standardized and selfie photos, captured across three smartphone models under five lighting conditions with and without eyeglasses. The dataset is ethically collected with informed consent and GDPR compliance, and achieves gender balance (50:50) with near-equal representation across four racial groups. The paper reports baseline face detection and verification benchmarks using MTCNN, RetinaFace, MediaPipe, ArcFace, and MagFace.

## Strengths

- **First dataset to include explicitly designed eKYC video scenarios**: VIBEFACE provides seven eKYC verification scenarios (scenarios 12–18) that no prior face dataset (MOBIO, Replay-Mobile, OULU-NPU, SOTERIA, etc.) offers. This is verified in Table 1, where VIBEFACE is the only dataset with the eKYC checkbox filled, and in Section 3.2's detailed scenario descriptions.

- **Stronger demographic balance than comparable mobile-face datasets**: The dataset achieves 50:50 gender balance, near-equal representation across four racial groups (13 African, 13 Caucasian, 12 East Asian, 12 South Asian), and an age distribution spanning 18–69 compliant with ISO standards. In Table 1, VIBEFACE is the only dataset simultaneously checking gender balance, race balance, and age balance among the comparison sets.

- **Full ethical and legal compliance with explicit consent**: Data was collected under GDPR and the EU AI Act, with informed consent, withdrawal rights, and strict de-identification (Section 3.4). This directly addresses the legal and ethical failures that led to the withdrawal of widely-used datasets like VGGFace2 and MS-Celeb-1M.

- **Multi-device, multi-session, multi-condition acquisition**: Data was captured on three consumer smartphones (Xiaomi Redmi Note 13, iPhone 13, Samsung Galaxy A35) across five lighting sessions (artificial, flash, natural, weak natural, and with eyeglasses), enabling systematic studies of device and environmental effects on verification performance.

## Weaknesses

### Major

- **The dataset size (N=50) is structurally insufficient to support the paper's fairness benchmarking claims.** The paper's central narrative — that VIBEFACE enables evaluating demographic fairness in face verification — is undermined by having only 12–13 individuals per racial group. Differences reported in Tables 3 and 4 across demographic categories (e.g., "Caucasian subgroup performed slightly worse," "MTCNN showed reduced detection performance among African descent") are reported without any statistical uncertainty quantification. At these per-group sample sizes, individual subject idiosyncrasies (facial hair, glasses fit, skin reflectance under specific lighting) could dominate observed differences. The dataset is comparable in size to other mobile-face benchmarks (OULU-NPU: 55, HQ-WMCA: 51, SOTERIA: 70), but those do not claim to support demographic fairness evaluation. This is a mismatch between the stated contribution and the resource's capacity. **The paper must either substantially expand the dataset or reframe its contribution away from fairness benchmarking.**

- **The benchmark evaluation does not establish what the dataset uniquely contributes as a benchmark.** Face detection is near-perfect (RetinaFace achieves 1.000 on frontal and off-angle views across all sessions) — the detection task is essentially saturated. For verification, only off-the-shelf pre-trained models are evaluated without fine-tuning, and no cross-dataset comparison is provided (e.g., same ArcFace/MagFace protocol on MOBIO, Replay-Mobile, or SOTERIA). Without such comparisons, the reader cannot determine whether VIBEFACE presents a usefully more challenging or complementary evaluation than existing resources. The verification protocol (one reference from Session B, compared to frames in other sessions) is a reasonable design choice, but omitting cross-session matching means the experiments do not actually simulate the claimed eKYC scenario (matching an ID photo to a live selfie).

### Minor

- **The eKYC scenarios are scripted studio simulations, not naturalistic user behavior.** Data were collected in a controlled studio with operators supervising each step, standardized instructions, and fixed camera positions (Section 3). Scenarios such as "touching various parts of the face with a finger" are scripted actions rather than natural user behavior. The paper frames these as "realistic eKYC sequences" (abstract) and "authentic eKYC-style recordings" (Section 2), but the actual operational realism is low. The dataset has value as a controlled simulation, but the framing over-promises. A more measured description (e.g., "scripted eKYC-mimicking actions under controlled conditions") would better align with the data's characteristics.

- **Key eKYC scenarios (11, 17–18) are excluded from the benchmarks** without sufficient justification. Scenario 11 (selfie video) is excluded due to "incomplete coverage across sessions," and scenarios 17–18 (hand covering face, touching face) because occlusions "significantly reduce facial visibility" (Section 4.1). While the occlusion rationale has merit, excluding the main selfie video scenario weakens the claim that the dataset supports eKYC evaluation.

- **The paper does not define a standard evaluation protocol, data splits, or provide evaluation code.** For a dataset intended as a benchmark, the absence of specified train/validation/test splits, and the lack of released evaluation code, limits reproducibility and adoption.

- **No discussion of the dataset's limitations.** There is no limitations section (or even a sentence) acknowledging the small sample size, the scripted nature of the eKYC actions, the controlled studio setting, or the saturated detection task. This omission is noticeable for a dataset paper.

### Trivial

- Table 1's comparison checkmarks would benefit from explicitly defining what constitutes "balance" for each demographic attribute.
- The fixed threshold of 0.5 for verification (Section 4.2) is used without justification; in practice, thresholds are deployment-dependent.
- Some font/sizing issues in the rendered tables (parser artifacts, not author errors).

## Nice-to-Haves

- Cross-session verification experiments (reference from Session B, probe from other sessions) would better match the eKYC application scenario.
- Cross-dataset difficulty comparison: running the same ArcFace/MagFace protocol on MOBIO, Replay-Mobile, or SOTERIA to contextualize VIBEFACE's difficulty level.
- Within-subject vs. between-subject similarity distributions (genuine/impostor histograms) — a standard visualization for face verification datasets.
- Per-action breakdown for eKYC video scenarios (e.g., is blinking harder than head rotation?) instead of aggregated results.
- t-SNE/PCA visualization of embedding space colored by demographic attributes, sessions, or glasses status.

## Removed Points

- *"No baseline models are trained from scratch"* — This is not standard practice for dataset papers; off-the-shelf model evaluation is the norm.
- *"RetinaFace scores 1.000 — detection is trivial"* — This is an observation, not a flaw. Many modern datasets have saturated detection; the value lies in verification, not detection.
- *"Flash session only includes standardized photos"* — The paper explicitly acknowledges this design constraint in Section 3.3. It is a design choice, not an oversight.
- *"Fixed threshold of 0.5 without justification"* — This is common practice in verification benchmarks; threshold tuning is a deployment detail.
- *"Gender balance, race balance claims are misleading because N=50"* — The *balance* claim (12-13 per group) is factually correct; the issue is whether N=50 supports *fairness evaluation*, which is captured in the major weakness above.
- *Several formatting/style nitpicks and grammar complaints* — These are parser artifacts or below the review bar.
- *"Missing related works"* — Cannot verify without external sources.
- *"Missing appendix content"* — The parser strips appendix sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation that the authors themselves do not already acknowledge (implicitly or explicitly) through the paper's structure and experimental design.

## Suggestions

1. **Reframe the contribution around eKYC scenario evaluation rather than demographic fairness benchmarking.** The dataset's genuine value is as the first resource providing eKYC-style video sequences; this is a solid, specific contribution that does not require N>100 fairness claims. Remove or substantially soften language about "evaluating fairness" and replace with "supporting controlled studies of eKYC verification robustness across varied conditions."

2. **Add cross-dataset difficulty calibration.** Run the same verification models on MOBIO, Replay-Mobile, or SOTERIA under a comparable protocol to show readers where VIBEFACE sits in the difficulty spectrum.

3. **Provide similarity score distributions** (genuine vs. impostor histograms) and defined evaluation splits with released code. These are standard expectations for a dataset-as-benchmark paper.

4. **Add a limitations section** explicitly discussing N=50, the controlled studio setting, the scripted nature of eKYC actions, and the saturated face detection task.

5. **Either expand the dataset** to a size where demographic comparisons become meaningful (minimum ~200 subjects for 4-group comparisons with reasonable statistical power) or remove the fairness evaluation framing entirely.

## Score and Decision

**Calibration anchors** (from vector search, all from ICLR 2026 human-reviewed papers):

| Anchor Path | Avg Score | Comparison to VIBEFACE |
|---|---|---|
| `NYphgYTloq.md` (IRIS Benchmark) | 6.50 | Far more comprehensive fairness benchmark with large-scale evaluation across many models. VIBEFACE is narrower in scope and smaller in scale. |
| `t3ZMiHhqXm.md` (LAION-400M Annotations) | 5.50 | Large-scale dataset contribution with thorough analysis and clear downstream impact. VIBEFACE is much smaller and has thinner analysis. |
| `O4f1NdXtdM.md` (FaceMoE) | 5.00 | Method paper with extensive experiments across 11 datasets. VIBEFACE has fewer experimental controls. |
| `771P34sqnn.md` (FaceCoT Benchmark) | 3.50 | Dataset/benchmark paper with a genuine resource contribution but thin methodological novelty. Comparable to VIBEFACE in having a real contribution but limited experimental depth. |
| `k60jAxVSv7.md` (DenseFace) | 3.33 | Conceptual errors in a bias mitigation paper. VIBEFACE has fewer methodological errors but its core fairness claim is unsupported. |
| `9Xf15SW6mg.md` (LAION-5B Bias) | 2.50 | Descriptive analysis of known biases, low novelty. VIBEFACE has more novelty (first eKYC dataset) but also has the scale issue. |
| `7iwqu82yOC.md` (Adaptive Calibration) | 2.50 | Method paper with evaluation issues. VIBEFACE contributes an actual reusable resource, which is more valuable. |

VIBEFACE sits in the 3.0–4.0 band. It has a genuine, identifiable new contribution (first eKYC video dataset with ethical sourcing and reasonable demographic balance) that distinguishes it from the lowest-scoring papers. However, the fundamental mismatch between the N=50 scale and the fairness-benchmarking claims, combined with thin benchmark evaluation and overframing, prevents it from reaching the acceptance threshold. Like FaceCoT (3.50), it offers a real resource but the paper's current framing and experimental validation do not meet the bar for a top-tier venue.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>