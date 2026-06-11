Now I have a comprehensive calibration picture. Let me finalize my review.

## Summary

VIBEFACE is a dataset paper presenting a facial biometric dataset (50 subjects, 2,250 images, 1,550 videos) designed for face verification in eKYC scenarios. It claims to be the first public dataset combining eKYC-style video verification sequences with still images, balanced across gender, race, and age. The paper includes benchmark evaluations on face detection (MTCNN, RetinaFace, MediaPipe) and face verification (ArcFace, MagFace) with demographic breakdowns.

## Strengths

- **Unique eKYC scenario coverage**: Table 1 (line 88–104) confirms VIBEFACE is the only compared dataset with eKYC verification scenarios (head rotation, blinking, expression change, mouth opening, face covering, facial touching — scenarios 12–18, lines 160–168). This fills a clearly identified gap in existing biometric datasets.
- **Best-in-class demographic balance**: Table 1 shows VIBEFACE is the only dataset simultaneously checking all three balance columns (gender, race, age). The actual distributions confirm this: 25/25 gender split (line 137), four race groups each at 24–26% (lines 120–123), and age distribution spanning 18–69 designed to comply with ISO/IEC 19795-1 (line 137).
- **Systematic multi-session design**: Five sessions (Table 2, lines 191–199) systematically vary lighting conditions (artificial, flash, natural, weak natural) and eyeglasses presence, enabling controlled ablation studies. Multi-device collection on three consumer smartphones (Xiaomi Redmi Note 13, Apple iPhone 13, Samsung Galaxy A35 5G — line 77–78) with random device assignment per session (line 187) adds genuine cross-device variability.
- **Rigorous ethical and legal compliance**: GDPR and EU AI Act compliance, informed consent, anonymized storage with randomized identifiers, and controlled-access licensing (Section 3.4–3.5, lines 203–278). This is particularly significant given that several major datasets were withdrawn for ethical concerns (lines 46–48).
- **Granular benchmark with demographic breakdowns**: Tables 3 and 4 provide performance breakdowns across scenarios, sessions, gender, age groups, and racial categories, surfacing fairness-relevant patterns (e.g., MTCNN's detection rate of 0.812 for African vs. 0.984 for East Asian in frontal views — Table 3, line 311).

## Weaknesses

### Fatal
None

### Major

- **Mismatch between "realistic eKYC" framing and controlled studio collection**: The abstract claims the dataset captures "realistic operational settings such as eKYC procedures" (line 8) and the introduction describes users recording "short videos under unconstrained conditions — at home, in variable lighting, and across heterogeneous mobile devices" (line 15). However, Section 3 opens with "Data acquisition was conducted in a controlled studio environment" with "standardized instructions" and "continuous supervision by trained operators" (lines 73–76). A controlled studio with scripted scenarios under supervision is fundamentally different from real eKYC sessions where users interact with an app at home. The paper never acknowledges this gap, yet it is the core value proposition. This is not merely a branding issue — it undermines the paper's central motivation. The eKYC *scenarios* themselves are valuable, but the persistent framing overstates what was collected.

- **Simplistic verification evaluation protocol**: Face verification is evaluated using a single fixed threshold of 0.5 with no justification (line 340: "Verification was considered successful when the similarity score exceeded a fixed threshold of 0.5"), reporting only the percentage of frames "correctly authenticated." Standard biometric evaluation uses ROC curves, equal error rates (EER), or FMR/FNMR trade-offs. A single operating point reveals little about discrimination capability and is sensitive to the arbitrary threshold choice. The paper's closest comparison, SOTERIA, also provides more rigorous evaluation in its own work. This significantly weakens the benchmark contribution.

### Minor

- **Small sample size without statistical caveats for demographic analysis**: With only 50 subjects, demographic subgroups are very small (~12–13 per race, 14–19 per age group). The paper draws conclusions from these breakdowns (e.g., "MTCNN showed reduced detection performance... among individuals of African descent" — line 300) without any confidence intervals, variance estimates, or caveats about statistical power. Observed differences could be driven by a few individual subjects rather than systematic demographic effects.

- **Unsupported Fitzpatrick scale claim**: Line 139 states participants "reflect the whole spectrum of Fitzpatrick's scale" but provides no actual Fitzpatrick classifications, skin tone measurements, or any data substantiating this claim.

## Nice-to-Haves
- Head-to-head evaluation on shared tasks with SOTERIA (the closest comparable dataset, with 70 subjects, photos, videos, and demographic balance — line 102) would demonstrate what VIBEFACE uniquely enables.
- Data quality metrics (video resolution consistency, frame rate stability, inter-rater agreement on scenario execution) would strengthen confidence in the dataset.
- ROC curves, EER, and FMR/FNMR at standard operating points for the verification task — standard practice in the biometrics community.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Criticisms about missing related works: removed per hard rules (no external verification possible).
- Formatting/nitpick issues: removed per hard rules.
- The Fitzpatrick claim is kept as a minor weakness since the paper makes the claim but provides zero supporting data.

## Novel Insights
The paper surfaces a notable finding that MTCNN shows significant performance disparities across racial categories (0.812 detection rate for African subjects vs. 0.984 for East Asian in frontal views, Table 3), while RetinaFace and MediaPipe show minimal demographic variation. The observation that the youngest age group (18–30) yields the lowest verification rates is also somewhat counterintuitive. However, both findings are limited by the small sample sizes and lack of statistical rigor.

## Suggestions
- Reframe the dataset's positioning: describe VIBEFACE as providing *standardized eKYC-style protocols under controlled conditions* (enabling reproducible benchmarking) rather than claiming to capture "realistic" or "unconstrained" eKYC conditions. The controlled setting is a feature for benchmarking reproducibility.
- Replace or supplement the single-threshold verification metric with ROC curves, EER, and FMR/FNMR at standard operating points.
- Add statistical caveats (or bootstrapped confidence intervals) for demographic subgroup analyses given the small sample sizes.

## Calibration Report

**Anchors retrieved across all rounds:**

| Paper | Score | Decision | Round | Comparison |
|-------|-------|----------|-------|------------|
| Clothing-Irrelevant Lifelong Person Re-id | 1.00 | Reject | R1 | Not comparable — off-topic |
| Scaling Illumination Harmonization | 0.50* | Accept | R1 | Not comparable — different domain |
| Humanoid Robots Cross-Lingual | 1.00 | Reject | R1 | Not comparable — off-topic |
| Financial Markets Neural Network | 1.00 | Reject | R1 | Not comparable — off-topic |
| Person Detection Algorithmic Bias | 2.50 | Reject | R1 | Related but weaker — bias analysis without new data |
| Fairness in ML Tensor Data | 3.00 | Reject | R1 | Related but weaker — fairness technique, no new dataset |
| ID-Booth Synthetic Face Data | 3.00 | Reject | R1 | Related — synthetic face data paper, smaller scope |
| Federated Learning Biometric Auth | 2.50 | Reject | R1 | Related but weaker — data augmentation for security |
| Face Recognition ViT vs CNN | 4.25 | Reject | R1 | Related — face recognition comparison, missing baselines |
| VLM Unlearning Benchmark (FIUBench) | 5.40 | Accept | R1 | Similar scope — benchmark paper, more rigorous evaluation |
| Deepfake Detector Assessment (DAP) | 3.80 | Reject | R2 | Similar — assessment framework, but no novel data. VIBEFACE is stronger. |
| Skin Tone PAD (ColorCubeNet) | 3.67 | Reject | R2 | Very related — biometric fairness, skin tone. Narrower contribution. |
| HiDF Deepfake Dataset | 4.25 | Reject | R2 | Similar — dataset paper, larger dataset but less demographic focus |
| ScalePerson | 4.75 | Reject | R2 | Similar — first dataset + benchmark, more experiments but easier dataset |
| Voice-Face Matching Homogeneous Populations | 3.67 | Reject | R2 | Somewhat related — biometric evaluation with demographics |
| ObjectNet Captions | 5.25 | Reject | R2 | New dataset + metric, different domain |
| MarineMaid Dataset | 4.25 | Reject | R2 | Dataset paper, different domain |
| BabyView Dataset | 5.40 | Reject | R2 | Large egocentric video dataset, different domain |
| Balancing VL Datasets Synthetic | 4.67 | Reject | R2 | Debiasing dataset work |
| Fairness Benchmark FFB | 6.75 | Accept | R1 | Benchmark paper, much larger scale (45K experiments) |
| ROC Uncertainty Face Recognition | 6.33 | Accept | R1 | Face recognition evaluation, more theoretical depth |
| Face-Human-Bench | 5.75 | Reject | R1 | Face benchmark for multimodal assistants |
| Object Recognition Generalization | 6.25 | Accept | R1 | Benchmark evaluation, different domain |
| LOKI Synthetic Data Benchmark | 8.00 | Accept | R1 | Comprehensive benchmark, much stronger |
| Dataset Bias Decade | 8.00 | Accept | R1 | Novel insight paper, much stronger |

**Round 1 bracket**: 3.5 – 5.5 (rejected dataset/benchmark papers cluster here)

**Round 2 narrowing**: 3.8 – 4.5 (comparable to DAP at 3.80, HiDF at 4.25, ScalePerson at 4.75 — VIBEFACE is stronger than DAP due to novel real data, comparable to HiDF, slightly below ScalePerson which has more extensive evaluation)

**Final score: 4.0** — VIBEFACE contributes a genuinely novel eKYC-focused dataset with strong demographic balance and well-documented protocols. However, the misleading framing of controlled studio data as "realistic eKYC conditions," the simplistic single-threshold verification evaluation, and the unsubstantiated demographic claims prevent it from reaching the accept threshold. It sits squarely among the rejected dataset papers in the 3.8–4.75 range, above DAP (3.80) due to its novel data contribution, but below ScalePerson (4.75) due to weaker evaluation methodology.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>