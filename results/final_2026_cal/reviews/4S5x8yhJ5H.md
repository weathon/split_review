Now I have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

VIBEFACE introduces a multimodal facial biometric dataset of 2,250 images and 1,550 short videos from 50 subjects, specifically designed to simulate eKYC (electronic Know Your Client) verification workflows. The dataset is notable for its simultaneous demographic balance across gender (50:50), race (≈25% each of four categories), and age (three tiers from 18–69), and for its full GDPR/AI Act ethical compliance with informed consent. Benchmark experiments on face detection (MTCNN, RetinaFace, MediaPipe) and face verification (ArcFace, MagFace) are presented to demonstrate the dataset's utility for studying robustness and demographic bias.

## Strengths

- **Unique eKYC-focused design filling a genuine gap.** Table 1 provides direct comparative evidence: VIBEFACE is the only dataset among eight listed (MOBIO, Replay-Mobile, OULU-NPU, MobiBits, WMCA, HQ-WMCA, SOTERIA) that includes structured eKYC verification scenarios. Scenarios 12–18 (circular head rotation, blinking, expression changes, partial occlusions, facial touches) are concretely designed to mimic real eKYC identity verification workflows, not just general liveness detection.

- **Simultaneous demographic balance across three axes unmatched by prior datasets.** VIBEFACE achieves a 50:50 gender split, near-equal representation across four racial categories (13 African, 13 Caucasian, 12 East Asian, 12 South Asian), and a three-tier age distribution (18–30: 19, 31–50: 17, 51–70: 14). Table 1 shows every other dataset fails at least one of the gender/race/age balance columns; SOTERIA (the closest competitor) underrepresents middle-aged and older individuals. This makes VIBEFACE a uniquely useful resource for fairness research.

- **Exemplary ethical and legal compliance.** Section 3.4 documents informed consent, GDPR compliance (EU 2016/679), AI Act compliance (EU 2024/1689), anonymized identifiers, withdrawal rights, and controlled-access licensing. This directly contrasts with the withdrawn internet-scraped datasets (MS-Celeb-1M, VGGFace2, MegaFace) discussed in Section 2, providing a legally usable alternative for the research community.

- **Systematic multi-condition acquisition.** Five distinct sessions (artificial light, flash, artificial light+glasses, natural daylight, weak natural light) across three consumer smartphones (Xiaomi Redmi Note 13, iPhone 13, Samsung Galaxy A35) with random device assignment provide controlled-but-varied variability beyond most prior datasets.

## Weaknesses

### Major

- **Face verification evaluation protocol is not a valid benchmark.** The paper reports "percentage of frames in which the face was correctly authenticated" using a fixed similarity threshold of 0.5. This metric suffers from two problems. First, per-frame predictions from the same video are highly correlated, inflating effective sample size. Second, a single absolute threshold is meaningless for cross-model comparison—the same threshold may be too strict for MagFace and too lenient for ArcFace depending on model calibration. No ROC curves, equal error rates (EER), verification rates at controlled false accept rates (FAR), or any standard biometric evaluation metric (ISO/IEC 19795) is reported. The paper claims to "establish a new benchmark," but the evaluation as designed is not reproducible or comparable to future work. This is the paper's most consequential weakness: the dataset itself remains valuable, but the benchmark task is not methodologically sound.

- **Demographic findings are based on very small subgroups but reported with false precision.** With 50 subjects split across 4 racial categories (12–13 per group) and 3 age groups (14–19 per group), Tables 3 and 4 report per-group percentages to three decimal places without any uncertainty estimates (no confidence intervals, standard deviations, or per-subject distributions). For example, the claim that "MTCNN showed reduced detection performance among individuals of African descent" relies on 13 subjects. Differences of a few percentage points among such small groups are likely dominated by individual-level variance. The paper should present per-subject distributions and explicitly acknowledge this limitation rather than presenting aggregate percentages as statistically reliable findings.

### Minor

- **The "first eKYC" claim would benefit from clearer differentiation from liveness detection datasets.** The paper states it is "the first publicly available database to include diverse video-based eKYC verification scenarios." While Table 1 supports this claim by showing that no other dataset has the eKYC column checked, the actions described (head rotation, blinking, expression changes) are also present in some liveness detection datasets (e.g., Replay-Mobile, OULU-NPU). A more precise articulation of what makes a scenario distinctively "eKYC" (beyond the list of actions—e.g., the structured workflow, the combination with still image references, the specific regulatory context) would strengthen the novelty argument.

- **Exclusion of scenarios 11, 17, and 18 from evaluation is not fully justified.** Scenario 11 (selfie video) is excluded "due to incomplete coverage across sessions," and scenarios 17–18 (occlusion scenarios) are excluded "because they involve occlusions." While these exclusions are not unreasonable, they remove exactly the scenarios that would test the dataset's ability to surface robustness failures. Including them as a separate analysis, rather than dropping them, would better demonstrate the dataset's value.

## Nice-to-Haves

- Report verification rates using a proper protocol: verification rates at 0.1% and 1% FAR using ROC analysis, with per-subject score distributions rather than per-frame aggregated percentages.
- Provide confidence intervals or bootstrap estimates for all demographic breakdowns, and frame the demographic analysis as illustrative rather than as statistically robust findings.
- Strengthen the comparison to existing datasets by quantifying action overlap—e.g., a table showing which specific actions appear in Replay-Mobile, WMCA, or SOTERIA, and whether they are embedded in an eKYC-like workflow.
- Include scenario 11 and the occlusion scenarios (17, 18) as a separate challenging evaluation track rather than excluding them.

## Removed Points

The following points from the inputs were removed:

- **Table 1 blank cells instead of "No" markers** — This is a formatting/presentation nitpick. The comparison intent is clear. REMOVED per formatting nitpick rule.
- **Reproducibility concern about undisclosed hyperparameters and threshold being manually set** — The threshold of 0.5 is a design choice, not a reproducibility gap. The paper describes the evaluation procedure clearly. REMOVED per soft rule on reproducibility nitpicks.
- **Criticism about MOBIO entry in Table 1** — The parsing of the table is ambiguous due to PDF extraction artifacts; the paper's intent is clear. REMOVED per formatting artifact rule.
- **"Broader applications (PAD, deepfake detection) are speculative"** — This is a standard feature of dataset papers discussing potential future uses. REMOVED as it criticizes a non-essential part of the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise the verification evaluation protocol.** Adopt standard biometric metrics: report verification rates at 0.1% and 1% FAR with full ROC curves, and include EER. Present per-subject score distributions rather than per-frame aggregated percentages.

2. **Add uncertainty quantification for all demographic analyses.** Report standard deviations, confidence intervals, or per-subject distributions. Explicitly discuss the small-N limitation (12–13 per racial group) and reframe demographic findings as illustrative rather than conclusive.

3. **Tone down the "benchmark" framing.** The dataset is a valuable resource, but the current experimental evaluation does not constitute a technically sound benchmark. Either fix the evaluation protocol or reframe the paper as a dataset description with illustrative analyses.

4. **Include the currently excluded scenarios.** Adding scenario 11 (selfie video) and scenarios 17–18 (occlusions) as a separate challenging track would better demonstrate the dataset's ability to stress-test models under difficult conditions.

5. **Sharpen the eKYC novelty claim.** Provide a precise definition of what makes a scenario "eKYC" vs. general liveness detection, and show quantitatively that prior liveness datasets do not cover the same structured workflow.

## Score and Decision

**Round 1 bracket:** I queried three bands. The low band (<3.5) returned papers with avg scores 2.5–3.33 (fundamentally flawed or highly incremental). The middle band (3.5–7.5) returned papers with avg scores 4.0–5.0, including DeepfakeBench-MM (4.0, Withdrawn) and FaceMoE (5.0, Reject). The high band (>7.5) returned papers at 8.0 (top-tier accept). I placed VIBEFACE in the (4.0, 6.5) bracket after reading these anchors.

**Round 2 narrowing:** I queried two sub-bands: (4.0, 5.5) and (5.5, 7.0). The lower sub-band returned anchors at 4.5–5.33 (Latent Feature Alignment 4.5, AbdCTBench 4.5, Weakly Supervised Forgery 5.33, FaceMoE 5.0). The upper sub-band returned anchors at 6.0–6.67 (Phantom-Data 6.0, VTBench 6.0, So-Fake 6.0, SpeakerVid-5M 6.67, IRIS Benchmark 6.5).

**Comparison to anchors:** VIBEFACE is notably weaker than the 6.0+ anchors (Phantom-Data, So-Fake, SpeakerVid-5M), which have datasets orders of magnitude larger and more rigorous evaluation protocols. VIBEFACE is comparable to FaceMoE (5.0) in overall quality but for different reasons: FaceMoE had stronger experiments but less novel contribution, while VIBEFACE has a more novel dataset contribution but substantially weaker experimental validation. VIBEFACE is clearly above the 4.0-level papers (DeepfakeBench-MM, MAVOS-DD) which had more serious structural problems.

**Final score: 5.0.** The dataset fills a genuine gap and the ethical/demographic design is exemplary. However, the benchmark evaluation protocol is not methodologically sound, and the demographic claims are not supported by the sample size. These are fixable issues, but in their current form the experiments do not adequately validate the paper's claims about establishing a benchmark.

**Decision: Reject.** The core dataset is a useful contribution, but the paper as presented overstates its experimental claims. A substantially revised version with proper biometric evaluation metrics (ROC, EER, FAR-controlled rates), uncertainty estimates for demographic analyses, and toned-down claims could merit acceptance at a future venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>