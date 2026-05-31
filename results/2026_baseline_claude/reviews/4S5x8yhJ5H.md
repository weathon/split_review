## Summary

VIBEFACE is a new biometric dataset for face verification in electronic Know Your Client (eKYC) scenarios. It contains 2,250 still images and 1,550 short videos from 50 demographically balanced subjects (25 male/25 female, 4 racial groups ~25% each, 3 age groups), collected across 5 sessions with varying lighting and eyeglasses conditions. The authors define 18 distinct scenarios, including eKYC-specific sequences (head rotation, blinking, face touching, hand occlusion), and benchmark three face detection algorithms and two verification models, with demographic breakdowns of results.

---

## Strengths

- **Addresses a genuine gap**: To the authors' knowledge (and consistent with the comparison in Table 1), no publicly available dataset combines eKYC-style video sequences with still images, demographic metadata, and consent-based ethical data collection. The 18-scenario design—particularly scenarios 12–18 simulating real eKYC interactions—directly targets an underserved need in practical biometric research.
- **Rigorous ethical compliance**: The dataset was collected with informed consent, GDPR compliance, EU AI Act adherence, and IRCC-style anonymized identifiers. In an era where major datasets (VGGFace2, MS-Celeb-1M, MegaFace) have been retracted for ethical violations, this is a meaningful and increasingly important differentiator.
- **Well-designed demographic balance**: Gender is exactly 50/50; racial groups span four categories at approximately 25% each; age structure follows ISO 19794 guidelines. Fitzpatrick skin tone coverage is explicitly mentioned. This is more methodologically deliberate than most comparable datasets in the comparison table.
- **Multi-session design captures real-world variation**: Five sessions crossing lighting type (artificial, flash, natural, weak natural) with eyeglasses presence/absence, using three different consumer smartphone models, captures realistic operational diversity.

---

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard face verification evaluation methodology.** The paper uses a single fixed threshold of 0.5 to classify frames as "correctly authenticated" and reports only True Positive Rate (TPR) at that threshold. Standard biometrics practice requires metrics such as Equal Error Rate (EER), ROC curves, TAR@FAR (e.g., at FAR=0.1%, 1%), or FNMR@FMR. Without False Match Rate (FMR) reporting, the 0.5 threshold is arbitrary and possibly chosen favorably—ArcFace FV scores of 1.000 in almost all conditions do not characterize a benchmark; they characterize saturation at a lenient threshold. A dataset paper's benchmark value hinges on the quality of its evaluation protocol, and this one does not establish one.

2. **Scale is too small for statistically credible demographic disparity claims.** With 12–13 subjects per racial group and 8–10 per gender/age cell, the demographic breakdown tables (Tables 3 and 4) have insufficient statistical power to support the conclusion that "ArcFace performed slightly worse on Caucasian subgroup" or that MTCNN "showed reduced detection performance among individuals of African descent." No confidence intervals, significance tests, or effect sizes are provided. These numbers reflect noise as much as signal, and treating them as meaningful findings about demographic bias is overreaching.

3. **The verification task conflates detection failures with verification failures.** The percentage of frames "correctly authenticated" collapses face-not-detected and face-detected-but-not-matched into a single number. This makes it impossible to determine whether a low score reflects the detector or the verifier, undermining the usefulness of Table 4 for benchmarking verification algorithms specifically.

### Minor

1. **No liveness detection or PAD experiment is included**, despite being a central stated motivation (eKYC use case). The paper promises PAD applicability as a "potential application" without demonstrating it. A basic experiment, even with a single baseline, would substantially strengthen the paper's claim that VIBEFACE is a useful eKYC benchmark.

2. **Single reference image per subject limits verification depth.** Using only one flash frontal image (Scenario 3, Session B) as the enrollment template does not test cross-session enrollment-to-probe variability, which is central to eKYC operational concerns. A multi-enrollment or leave-one-session-out protocol would better exercise the dataset.

3. **No analysis of video-level vs. frame-level aggregation for verification.** eKYC systems make a single pass/fail decision per session, not per frame. Frame-level TPR is an unusual metric that does not correspond to how eKYC verification is actually scored in practice.

### Trivial

- The paper would benefit from reporting the total number of video frames to give a clearer sense of scale.

---

## Nice-to-Haves

- Reporting standard biometrics metrics (EER, ROC at specified FAR points) would transform this into a genuinely reusable benchmark protocol.
- Adding even a minimal PAD experiment (e.g., replay attack or printed photo test) would directly validate the eKYC use-case framing.
- Confidence intervals on demographic subgroup comparisons would make the bias analysis credible.
- Cross-session verification (enrollment in one session, probe from another) would better reflect eKYC operational conditions.

---

## Novel Insights

The most genuine novel insight in this paper is structural rather than empirical: the observation that existing publicly available biometric datasets have converged on similar failure modes—either they lack eKYC-style video, are ethically compromised (leading to retraction), or fail to jointly satisfy demographic balance across gender, race, and age. VIBEFACE's design attempts to satisfy all three constraints simultaneously, which is novel in combination even if individual components are not. The session design crossing light type with eyeglasses presence is also well-structured for disentangling confounders. However, the empirical results produced by the benchmark experiments do not reveal novel insights about face detection or verification behavior beyond what is already established in the literature.

---

## Suggestions

- Replace the fixed-threshold TPR metric with EER, TAR@FAR=1%, and FMR@FNMR curves as the primary verification evaluation protocol.
- Add statistical significance tests or confidence intervals to demographic subgroup comparisons, and consider pooling subgroups (e.g., age 51–70 across racial groups) to increase power.
- Separate detection failures from verification failures in the pipeline by reporting detection rate and conditional verification rate independently.
- Include a minimal PAD experiment to directly validate the eKYC application claim.
- Provide a multi-enrollment protocol (e.g., one image per non-flash session as enrollment template) to enable cross-session verification evaluation.

---

## Score and Decision

VIBEFACE addresses a genuine need in the biometric research community—a publicly available, ethically collected, eKYC-style face dataset with careful demographic balance. However, the paper's benchmarking protocol has a significant methodological flaw (fixed-threshold TPR rather than standard EER/ROC metrics), the dataset scale (50 subjects, 12–13 per racial group) is too small to support the demographic bias conclusions drawn, and the central eKYC motivation is not validated with any liveness or PAD experiment. The dataset has value, but the paper as currently structured does not establish a reliable or reusable benchmark, which is the core requirement for a dataset paper. These issues are correctable but require substantive work on the evaluation design.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>