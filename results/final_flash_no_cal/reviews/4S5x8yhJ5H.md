Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

VIBEFACE is a multimodal facial dataset designed specifically for eKYC (electronic Know Your Client) verification scenarios. It contains 2,250 images and 1,550 videos from 50 participants, balanced across gender (50:50), race (~25% each of African, Caucasian, East Asian, South Asian), and age (18–30, 31–50, 51–70). Data were collected under five lighting sessions using multiple consumer smartphones, with full GDPR and AI Act compliance. The paper reports baseline face detection (MTCNN, RetinaFace, MediaPipe) and verification (ArcFace, MagFace) results on the dataset, broken down by demographics and acquisition conditions.

## Strengths

**1. First public dataset with eKYC-specific video scenarios.** Table 1 shows VIBEFACE is the only compared dataset with an eKYC checkmark. The verification videos include actions directly relevant to eKYC workflows (circular head rotation, blinking, mouth opening, hand-over-face, touching face parts) that are absent from existing mobile-face datasets. This fills a concrete gap.

**2. Simultaneous demographic balance across gender, race, and age — unique among public face datasets.** VIBEFACE achieves 50:50 gender split, ~25% per racial category (African, Caucasian, East Asian, South Asian), and three age bands (18–30, 31–50, 51–70). Table 1 confirms it is the only dataset with checkmarks for GB, RB, and AB together; comparators like SOTERIA have GB+RB but not AB, and MobiBits has only DD+GB. This balance is valuable for exploratory bias analysis even within the size constraints.

**3. Thorough ethical and legal compliance.** Section 3.4 documents informed consent, GDPR compliance, AI Act alignment, anonymization via randomized identifiers, controlled-access licensing, and the right to withdraw. This provides a clean legal foundation that contrasts sharply with the withdrawn web-scraped datasets (MS-Celeb-1M, VGGFace2, MegaFace) discussed in Section 2.

**4. Realistic multi-session, multi-device capture protocol.** Five acquisition sessions (artificial light, flash, natural daylight, weak natural light, dedicated glasses session) and three consumer devices (Xiaomi Redmi Note 13, iPhone 13, Samsung Galaxy A35 5G) produce meaningful variation in illumination and image quality that is directly relevant to operational eKYC deployment.

## Weaknesses

### Fatal
None.

### Major

**1. The fairness and demographic-robustness claims are stronger than the sample size supports.** The abstract and introduction position VIBEFACE as "a new benchmark for evaluating the robustness and fairness of biometric verification systems" and "a comprehensive and demographically rich resource." However, with only 50 subjects (12–13 per racial group), the power to draw conclusions about group-level performance differences is very limited. The paper makes specific claims such as "MTCNN showed reduced detection performance… particularly among individuals of African descent" (Section 4.1) based on raw detection percentages without any statistical testing (confidence intervals, bootstrap, tests of proportions). With 13 African subjects, observed differences could easily reflect individual variation rather than systematic bias. The paper does not acknowledge this limitation or qualify its demographic conclusions accordingly. **This is not a flaw in the dataset itself — the balanced design is genuinely valuable — but the framing needs substantial recalibration.** The authors should either (a) add appropriate statistical rigor (confidence intervals, effect sizes) and caveats about the exploratory nature of the demographic analysis, or (b) explicitly reposition the fairness claims as "preliminary observations from a small but balanced sample."

### Minor

**2. Evaluation protocol lacks standard biometric metrics.** Verification is assessed only as the percentage of frames exceeding a fixed threshold of 0.5, without ROC curves, AUC, EER, or FAR/FRR. The threshold choice is arbitrary and not justified — a different threshold would shift all comparisons. Face detection reports only detection rate (binary success/failure) without IoU-based localization accuracy, making it impossible to assess whether detections are properly localized. While basic demonstrations can illustrate dataset usability, the absence of standard metrics weakens the paper's demonstration that VIBEFACE can support rigorous benchmarking.

**3. No comparative experiments on existing datasets.** The paper asserts VIBEFACE's advantages over MOBIO, SOTERIA, etc., but never evaluates the same models on any other dataset to empirically show what different patterns or disparities VIBEFACE reveals. A direct comparison (e.g., running the same ArcFace/MagFace pipeline on MOBIO or SOTERIA video frames) would substantially strengthen the case that VIBEFACE offers unique value. Without it, the claimed advantages remain asserted rather than demonstrated.

**4. No explicit discussion of the sample size limitation.** The paper provides demographic breakdowns and draws conclusions from them without ever acknowledging that 12–13 subjects per racial group limits the reliability of group comparisons. Adding a limitations paragraph and exploratory caveats would substantially improve scientific honesty and prevent readers from overinterpreting the reported numbers.

**5. Occluded scenarios (11, 17, 18) excluded without justification for future use.** The paper reasonably excludes these from the main evaluation due to occlusion and incomplete coverage, but given that hand-over-face (scenario 17) and face-touching (scenario 18) are core eKYC actions, the paper should at minimum note that evaluating on these scenarios is important future work. Currently the exclusion is stated without comment on the gap this leaves.

### Trivial
- The "first publicly available database to include diverse video-based eKYC verification scenarios" claim (Section 5) could be sharpened to clarify what distinguishes these scenarios from generic liveness-detection videos already in Replay-Mobile or OULU-NPU. (The dataset's specific action sequences are genuinely different, but the framing invites a skeptical reader to blur the distinction.)

## Nice-to-Haves
- Provide recommended train/validation/test splits respecting the session and scenario structure, so researchers can train or fine-tune verification models on VIBEFACE.
- Release benchmarking code (beyond the dataset itself) with exact preprocessing steps and model hyperparameters to support reproducibility.
- Evaluate at least one occluded scenario (e.g., scenario 17, hand over face) to demonstrate the dataset's value for occlusion robustness analysis.
- Add a third recent verification model (e.g., AdaFace) to broaden the baseline comparison.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism that the "first eKYC dataset" claim is overstated because Replay-Mobile/OULU-NPU contain short videos.** Those datasets contain generic liveness-detection videos (head movements, blinking), not the specific eKYC workflows that VIBEFACE targets (e.g., covering face with hand, sequential face-touching). Table 1 confirms VIBEFACE is the only dataset with an eKYC checkmark. The claim is accurate.

2. **Criticism that the conclusion's mention of PAD/deepfake detection is "premature."** The paper uses hedging language ("holds potential for," "well-suited for advancing research in") and explicitly notes this is "beyond the scope of the experiments presented here." This is an appropriate forward-looking statement, not an overclaim.

3. **Criticism about the reference image choice (flash session frontal).** The paper justifies this as "emulating a typical document-based authentication setup," which is a reasonable design choice. A different reference could be used in future work but the current choice is defensible.

4. **Complaints about missing appendix, proofs, or supplementary material.** The parser strips these sections; they may exist in the original submission.

5. **Formatting, typo, and style nitpicks.** These reflect parser artifacts (PDF extraction), not author errors.

6. **Criticism that Table 1's checkmarks do not convey sample size.** Table 1 has an explicit "IDs" column (50 for VIBEFACE). The checkmarks indicate balance (roughly equal per bin), which is what they are designed to convey.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a clear tension: the dataset's balanced design and ethical foundations are genuinely novel, but at N=50 its utility for rigorous fairness benchmarking is necessarily limited. Neither the harsh critic nor the strength finder identified a hidden flaw or unexpected strength that the paper's authors themselves overlooked — the core tradeoff between demographic coverage and sample size is apparent from the stated numbers.

## Suggestions

1. **Recalibrate the framing.** Replace "a new benchmark for evaluating fairness" with language like "a demographically balanced dataset designed to support exploratory fairness analysis and system development for eKYC scenarios." Add a one-paragraph limitations section acknowledging that N=50 means demographic comparisons should be treated as preliminary.

2. **Add statistical grounding to demographic comparisons.** Report bootstrap 95% confidence intervals for each cell in Tables 3 and 4, or at minimum note that no statistical tests were performed and readers should interpret group differences cautiously.

3. **Replace or augment the fixed-threshold verification metric with ROC analysis (AUC or EER).** This is standard practice in biometric evaluation and would make the results threshold-independent.

4. **Run the same verification models on at least one existing dataset (MOBIO or SOTERIA) using the same codebase and metrics.** This directly addresses the most common question a reader will have: "What does VIBEFACE tell me that existing data does not?"

5. **Add IoU-based evaluation for face detection.** Detection rate alone conflates correct detections with poor localizations.

## Score and Decision

**Score:** 6.0

**Decision:** Accept

**Rationale:** The VIBEFACE dataset fills a genuine gap — no other public dataset combines eKYC-specific video scenarios with demographic balance across gender, race, and age while maintaining ethical/legal compliance. The dataset itself is a solid, citable resource that will be useful to the biometrics community. The main issues (overclaimed fairness framing, basic evaluation metrics, no comparative experiments) are all addressable in a revision and do not undermine the core dataset contribution. The paper is an acceptable contribution pending a good-faith revision that tempers the fairness claims, adds statistical caveats, and ideally strengthens the evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>