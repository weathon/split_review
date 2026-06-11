Now I have a clear picture. Let me write the final review with the calibrated score.

## Summary

VIBEFACE is a facial biometric dataset comprising 2,250 images and 1,550 videos from 50 subjects, designed for eKYC (electronic Know Your Client) verification scenarios. It includes 18 scenarios across five sessions varying lighting and eyeglasses, captured on three consumer smartphones. The dataset balances gender (25M/25F), four racial categories, and three age bands. The paper benchmarks three face detectors and two face verification models on the dataset.

## Strengths

- **Genuinely novel eKYC video scenarios**: The dataset includes 7 distinct verification video scenarios (scenarios 12–18: circular head rotation, head tilting, blinking, expression changes, mouth opening, face covering, sequential face touching) that mimic real-world eKYC workflows. Table 1 confirms no prior public dataset (MOBIO, Replay-Mobile, OULU-NPU, MobiBits, WMCA, HQ-WMCA, SOTERIA) includes eKYC-style videos.

- **Tri-axis demographic balance**: The dataset simultaneously balances gender (25M/25F), race (13 African, 13 Caucasian, 12 East Asian, 12 South Asian), and age (18–30: 19, 31–50: 17, 51–70: 14). Table 1 shows no prior dataset achieves all three balances simultaneously — SOTERIA, for instance, has gender and race balance but lacks age balance.

- **Systematic five-session environmental design**: Sessions A–E systematically vary lighting (artificial, flash, natural daylight, weak natural light) and eyeglasses presence (Table 2), enabling isolation of individual environmental factors on algorithm performance.

- **Multi-device capture on consumer smartphones**: Three devices (Xiaomi Redmi Note 13, Apple iPhone 13, Samsung Galaxy A35 5G) with random assignment per session introduce cross-sensor variability reflecting real-world deployment heterogeneity.

- **Thorough ethical framework**: Section 3.4 specifies GDPR and EU AI Act compliance, controlled-access licensing, informed consent with explicit permission for biometrics/AI research, and randomized-identifier anonymization — addressing the ethical deficiencies that caused the withdrawal of datasets like MS-Celeb-1M and VGGFace2.

- **Diagnostic detection results**: The face detection benchmarks (Table 3) surface a concrete disparity: MTCNN achieves only 0.812 detection rate on frontal views for African subjects versus 0.984 for East Asian subjects, while RetinaFace and MediaPipe show no such gap — demonstrating the dataset's ability to expose algorithm-specific demographic failure modes.

## Weaknesses

### Fatal

None.

### Major

- **Verification benchmark uses a single arbitrary threshold without standard biometric metrics**: The face verification evaluation (Section 4.2, line 337–340) declares verification successful when cosine similarity exceeds a fixed threshold of 0.5 for both ArcFace and MagFace. No ROC curves, Equal Error Rate (EER), or True Accept Rate at a fixed False Accept Rate (TAR@FAR) are reported. ArcFace and MagFace produce cosine similarity scores on different scales, so a threshold of 0.5 does not correspond to comparable operating points across models. The claim that "ArcFace consistently outperformed MagFace" (line 342) could be an artifact of where this arbitrary threshold falls on each model's score distribution. Standard biometric evaluation practice requires threshold-independent metrics.

- **Verification metric conflates detection failure with recognition failure**: Performance is reported as "percentage of frames in which the face was correctly authenticated" (line 340). A frame where no face is detected cannot be authenticated, so the numbers blend detection errors and recognition errors. For the challenging conditions central to the dataset's value (off-angle views, weak light, eyeglasses), the reader cannot determine whether failures stem from the detector or the recognizer. For example, Scenario 12 under session C with ArcFace scores 0.604 — it is unclear whether this reflects faces going undetected during head rotation or genuine embedding mismatches.

- **No evaluation protocol defined for future benchmark use**: A dataset paper intended as a community resource must specify how identities should be partitioned for enrollment vs. query, whether and how the 50 identities should be split for training/validation/testing, and which reference samples constitute the enrollment set. The paper evaluates off-the-shelf models against a single flash photo (Session B, Scenario 3) as reference, but never articulates a standardized protocol for other researchers. Without one, results across labs will not be comparable, undermining the dataset's function as a benchmark.

### Minor

- **Detection benchmark saturated for modern detectors**: RetinaFace achieves 1.000 on most cells in Table 3 and MediaPipe is near-perfect on frontal views, meaning the detection task provides little discrimination among strong detectors. MTCNN provides more informative variation but is an older model.

- **No statistical tests for demographic subgroup analyses**: The paper makes claims about demographic performance differences (e.g., "both models performed slightly worse on the Caucasian subgroup," line 344) based on point estimates with as few as 12–13 subjects per racial group and 14–19 per age band. No confidence intervals or significance tests accompany these comparisons, making the demographic claims statistically unsupported at N=50.

- **Unsubstantiated Fitzpatrick scale claim**: The paper states skin tones "reflect the whole spectrum of Fitzpatrick's scale" (line 139) but never provides a Fitzpatrick distribution or explains how skin tone was assessed. Only self-identified racial categories are reported.

- **Only two verification models evaluated, both margin-based cosine classifiers**: ArcFace and MagFace share similar operating principles (angular margin losses). Including a broader range of verification approaches would better demonstrate the dataset's utility, though two models is acceptable for an initial demonstration.

- **No explicit acknowledgment of small sample size**: At N=50, the dataset is modest by modern standards. The paper would benefit from discussing what claims can and cannot be supported at this scale, rather than implying comprehensiveness.

- **PAD and deepfake claims unsupported by dataset content**: The conclusion (lines 373–374) mentions presentation attack detection and deepfake detection as potential applications, but the dataset contains only bona fide samples with no attack/presentation-attack data. These claims are purely aspirational.

### Trivial

- **Table 1's checkmark format** flattens some distinctions (e.g., "Age Balance" for VIBEFACE with 14-17-19 across three bands is a reasonable effort but not perfectly balanced), though the table remains a useful high-level comparison.

## Nice-to-Haves

- Provide intra-class vs. inter-class similarity distributions to ground the difficulty of the dataset and quantify inter-session variability.
- Report confidence intervals or apply statistical tests to all demographic subgroup analyses.
- Include a broader set of verification models (e.g., non-margin-based) in the benchmark.
- Clarify the Fitzpatrick skin-tone assessment methodology and distribution.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Resolution details: no distribution given for image sizes"** — This is a pure nitpick; the paper gives a minimum resolution (2316×3088) which is sufficient for a dataset paper.
- **"Session B only includes scenarios 1-5, limiting cross-session comparisons"** — The paper explicitly acknowledges this (lines 183–184): the flash session required the back camera and thus includes only standardized photographs. It is an acknowledged design choice, not a hidden flaw.
- **"The abstract overclaims slightly with 'establishes a new benchmark'"** — This is a framing judgment without a concrete anchor; the paper does set up benchmark tasks, even if the protocol is underspecified.
- **"The introduction's claim about eKYC benefit is asserted rather than demonstrated"** — The paper provides benchmark evidence (Tables 3–4); the claim that the dataset *can* benefit research is forward-looking, not a claim requiring proof.
- **"The face verification model choice is unfair or under-tested"** — Only two models were used, but both are standard off-the-shelf models, which is acceptable for an initial dataset demonstration. This is already captured in the Minor weakness about limited model diversity.
- **"Could the demographic percentages be inaccurate or noisy?"** — The demographic distributions are clearly reported in Figure 1 and lines 135–139; the paper is transparent about the sizes. This is the reviewer manufacturing doubt without evidence.

## Novel Insights

The MTCNN demographic disparity finding (0.812 for African vs. 0.984 for East Asian subjects on frontal views, Table 3) is a concrete demonstration of how a demographically balanced dataset can expose failure modes invisible in less diverse collections. The fact that RetinaFace and MediaPipe do not exhibit this gap suggests the disparity is algorithm-specific rather than an inherent property of the data — an observation with implications for fairness-aware model selection in biometric systems.

## Suggestions

- Replace the single-threshold verification evaluation with standard biometric metrics: ROC curves, EER, and TAR@FAR (e.g., TAR@FAR=10⁻³). Report these per session, per demographic group, and per scenario.
- Report verification accuracy only on frames where a face was successfully detected, and report detection rates separately, so recognition quality can be assessed independently of detection robustness.
- Define a clear evaluation protocol: specify enrollment/query partitions, a recommended train/validation/test split of the 50 identities, and which reference images constitute the enrollment set.
- Add confidence intervals or statistical tests to all demographic subgroup comparisons.
- Acknowledge the N=50 limitation explicitly and discuss what evaluation questions the dataset can and cannot support.
- Either remove the PAD/deepfake claims from the conclusion or clarify they are purely aspirational and not supported by the current dataset content.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KidSat | 2.00 | R1 (strong reject) | Unrelated (satellite imagery); much weaker than VIBEFACE |
| EgoQR | 2.20 | R1 (strong reject) | Unrelated (QR code reading); much weaker |
| MCIL Benchmark | 2.33 | R1 (strong reject) | Unrelated (continual learning); much weaker |
| FMBench | 3.50 | R1 (weak reject) | Fairness benchmark repurposing existing data; VIBEFACE is stronger due to original data collection and better design |
| VideoEval | 4.00 | R2 (lower) | Video evaluation benchmark; comparable quality but different domain |
| Gone With the Bits | 4.25 | R1/R2 | Racial bias in neural compression; interesting but narrower scope; VIBEFACE has broader contribution |
| HiDF | 4.25 | R2 (lower) | Deepfake dataset; larger scale but single-generation method and weak evaluation; VIBEFACE has better design but similar evaluation weaknesses |
| FIUBench | 5.40 | R2 (upper) | VLM unlearning benchmark; clearer protocol and more comprehensive evaluation; VIBEFACE is weaker |
| Few-Class Arena | 5.50 | R2 (upper) | Classification benchmark; well-structured protocol; VIBEFACE is weaker |
| Face-Human-Bench | 5.75 | R1/R2 | Face benchmark with 25 models; more comprehensive evaluation; VIBEFACE is weaker |
| Alice Benchmarks | 6.50 | R1 (strong) | Re-ID benchmark with clear protocols and online server; clearly stronger |
| Assessing Uncertainty | 6.33 | R1 (strong) | Technical contribution on ROC analysis; clearly stronger |

Round 1 bracket: ~4.0–6.0. Round 2 narrowed to ~4.0–5.5. VIBEFACE sits above HiDF (4.25) due to more original dataset design, thoughtful scenarios, and better ethical framework, but below FIUBench (5.40) and Face-Human-Bench (5.75) due to the flawed verification evaluation (arbitrary threshold, no standard biometric metrics) and the absence of a defined evaluation protocol. The paper's core contribution — a demographically balanced eKYC video dataset — is genuine, but the evaluation that should demonstrate its utility is undermined by these issues. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>