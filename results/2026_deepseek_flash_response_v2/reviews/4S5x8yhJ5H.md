## Summary

VIBEFACE is a multimodal face dataset (2,250 images, 1,550 videos, 50 subjects) designed for evaluating biometric verification in electronic Know Your Client (eKYC) scenarios. It features eKYC-style video actions (head rotation, blinking, expression changes, etc.), balance across gender (50:50), race (four groups), and age (three brackets), with full GDPR/EU AI Act compliance and informed consent — distinguishing it from web-scraped, now-withdrawn datasets. The paper also presents face detection and verification benchmarks using standard models.

## Strengths

1. **First publicly available dataset with structured eKYC-style video scenarios.** Table 1 shows VIBEFACE is the only dataset among eight compared (MOBIO, Replay-Mobile, OULU-NPU, MobiBits, WMCA, HQ-WMCA, Soteria) that includes eKYC scenarios. Section 3.2 describes seven specific eKYC actions (scenarios 12–18: circular head rotation, tilting, blinking, expression changes, mouth opening, hand covering, face touching) that directly mimic real identity verification workflows. This claim is verified in Section 5 and Table 1.

2. **Simultaneous demographic balance across gender, race, and age — unmatched by prior datasets.** Table 1 shows VIBEFACE is the only dataset with checkmarks in all three balance columns (GB, RB, AB). Section 3.1 provides the supporting statistics: exactly 50:50 gender split (25F, 25M), near-equal racial distribution (13 African, 13 Caucasian, 12 East Asian, 12 South Asian), and age distribution across 18–69 in three brackets. This triple-axis balance is a measurable improvement over prior datasets like Soteria (which lacks age balance).

3. **Full legal/ethical compliance with GDPR and EU AI Act.** Section 3.4 details informed consent, right to withdraw, anonymization, and controlled-access licensing. This is a substantive differentiator from web-crawled datasets (MS-Celeb-1M, VGGFace2, MegaFace) that were collected without explicit consent and have since been withdrawn.

4. **Systematic multi-factor session design.** Section 3.3 designs five acquisition sessions (A–E) with varied lighting (artificial light with three color temperatures, flash, natural daylight, weak natural light), eyeglasses presence/absence, and three different consumer smartphones (Xiaomi Redmi Note 13, iPhone 13, Samsung Galaxy A35). Table 2 maps all 18 scenarios across these sessions with the acquisition device randomly chosen per session.

5. **Demographically disaggregated benchmark results.** Tables 3 and 4 break down face detection and verification performance by scenario, session, gender, age group, and racial category — enabling fairness auditing of the evaluated models.

## Weaknesses

### Major

1. **Non-standard verification evaluation protocol.** The verification experiment (Section 4.2) uses a single fixed threshold of 0.5 and reports "the percentage of frames in which the face was correctly authenticated." This conflates genuine accept rate (correctly accepting a legitimate user) and false reject rate (incorrectly rejecting a legitimate user) into one number. Standard biometric evaluation requires at minimum reporting both False Accept Rate (FAR) and False Reject Rate (FRR) separately, or reporting True Accept Rate (TAR) at a fixed FAR (e.g., TAR@FAR=1e-3), or providing ROC curves. The paper provides none of these. Furthermore, since ArcFace and MagFace operate in different embedding spaces, a shared threshold of 0.5 is not meaningful across models. The paper also does not clarify whether impostor comparisons were conducted alongside genuine comparisons. As a result, the absolute numerical results in Table 4 are substantially less informative than they should be for a dataset that aims to serve as a verification benchmark. The within-table relative comparisons (e.g., ArcFace > MagFace, off-angle < frontal) are still interpretable, but the core verification analysis that is supposed to demonstrate the dataset's utility is incomplete.

2. **No defined evaluation protocol for future researchers.** The paper does not specify a standard evaluation protocol: no defined enrollment/gallery set, no probe set, no protocol splits, no closed-set vs. open-set specification. The verification experiment uses a single frontal flash image as reference (an ad hoc choice), but without a fixed protocol, future researchers cannot compare results on this dataset. For video-based verification, the paper does not clarify whether decisions are per-frame or per-video, or how frames are aggregated into a video-level decision.

3. **Limited sample size undermines fairness claims.** The dataset has 50 subjects divided into 4 racial categories (~12–13 per group) and 3 age groups (~16–17 per group). The paper frames VIBEFACE as supporting fairness evaluation (abstract, Sections 1, 5), but per-group sample sizes are far too small for meaningful demographic bias analysis — a single outlier subject can shift group means substantially. No confidence intervals or statistical tests are reported for the demographic breakdowns in Tables 3 and 4. The observed spread in OAV verification rates across racial categories (0.460–0.509 for ArcFace) could easily be sampling noise with ~12 subjects per group. These analyses should be explicitly framed as descriptive/pilot-level rather than as definitive fairness benchmarking.

### Minor

4. **Face detection benchmark is not informative for modern detectors.** RetinaFace achieves 1.000 detection rate on almost all conditions and MediaPipe is near-perfect (≥0.924). This tells us the dataset is not challenging for current face detectors, which somewhat undermines the paper's motivation about detection difficulty in eKYC conditions. The one detector showing meaningful variation (MTCNN) is older. The detection benchmark does not strongly validate the dataset's utility as a challenging evaluation set.

5. **Controlled studio environment vs. real eKYC framing.** The paper frames the dataset as capturing "realistic eKYC conditions" (abstract) while acknowledging data was collected in a "controlled studio environment" with "trained operators" (Section 3). Real eKYC occurs in unconstrained home environments with variable lighting, backgrounds, and user behavior. This tension should be explicitly acknowledged as a limitation.

6. **No intra-class vs. inter-class similarity distribution analysis.** Standard for a face verification dataset paper would be to show that the dataset has sufficient separation between genuine and impostor similarity distributions, demonstrating that the dataset is not trivially easy or impossibly hard for verification. This analysis is absent.

### Trivial

None.

## Nice-to-Haves

- Replace the face detection benchmark with a more relevant downstream task (e.g., presentation attack detection or liveness detection, which the paper mentions as future applications).
- Add confidence intervals or bootstrap-based uncertainty estimates for the demographic breakdowns.
- Include analysis of Fitzpatrick skin tone distribution beyond the four racial categories.

## Removed Points

*These points were flagged as invalid or noise during filtering. Treat with caution if referenced elsewhere.*

- **"No discussion of existing dataset sizes"** (Harsh Critic): Table 1 includes an "IDs" column showing the number of unique identities for each dataset. Removed as factually incorrect.
- **"No discussion of how video frames were selected"** (Harsh Critic): Section 4.1 explicitly states "frames were extracted at a sampling rate of 6 frames per second." Removed as factually incorrect.
- **"Ambiguous whether the same images were used as queries and reference"** (Harsh Critic): Section 4.2 clearly states "a frontal image from the flash session (Scenario 3, Session B) was used as the reference sample." Removed as misunderstanding of the paper.
- **"Scenario 11 exclusion unexplained"** (Harsh Critic): Section 4.1 states it was "excluded due to incomplete coverage across sessions." Removed as factually incorrect.
- **Generic/superficial strengths** (Strength Finder): Claims like "addressed an important problem" without specific paper-grounded evidence. Removed as insufficiently specific.
- **"Missing related works"**: Removed per policy (cannot verify existence of external sources not cited in the paper).
- **"Missing appendix/proofs"**: Removed per policy (parser strips these from all papers).

## Novel Insights

Beyond the paper's own contributions, the reviews surface a core tension: VIBEFACE fills a genuine dataset niche (first eKYC-style video dataset with ethical provenance and demographic balance), yet its primary evaluation experiment — the verification benchmark intended to demonstrate the dataset's utility — uses a non-standard protocol that makes the reported numbers difficult to interpret as biometric verification performance. This means the paper's evidence for its own utility claim is weaker than it should be. The dataset's value as a resource is plausible but not convincingly demonstrated through the current experiments. Several calibration anchors (HiDF, ScalePerson) show similar patterns where dataset contributions were acknowledged but evaluation limitations led to rejection — suggesting a consistent standard that dataset papers must have sound evaluation protocols even if the dataset itself is useful.

## Suggestions

1. **Fix the verification evaluation.** Replace the fixed-threshold accuracy with standard biometric metrics: report ROC curves, AUC, and TAR@FAR (e.g., TAR@FAR=1e-2 or 1e-3). Report FAR and FRR separately. If using a threshold-based metric, justify the threshold via calibration on a held-out set and apply model-specific thresholds rather than a shared 0.5.
2. **Define a fixed evaluation protocol.** Specify which images serve as enrollment templates, which are probes, whether the task is closed-set or open-set verification, and how video-level decisions are made (e.g., majority vote, embedding averaging).
3. **Calibrate the fairness claims.** Acknowledge the small per-group sample sizes explicitly and present the demographic analyses as descriptive/pilot-level rather than as definitive fairness benchmarking.
4. **Add intra-class/inter-class similarity distribution analysis** to demonstrate that the dataset has meaningful verification difficulty.
5. **Acknowledge the controlled-environment limitation** relative to truly unconstrained eKYC.

## Score and Decision

**Calibration anchors used:**

*Round 1 (bracketing):*
| Anchor | Score | Query Band |
|--------|-------|------------|
| Face-Human-Bench (face benchmark) | 5.75 | Middle (3.5–7.5) |
| HiDF (deepfake dataset) | 4.25 | Middle (3.5–7.5) |
| EyeFairness (medical fairness dataset) | 5.50 | Middle (3.5–7.5) |
| Assessing Uncertainty (face ROC fairness) | 6.33 | Middle (3.5–7.5) |

*Round 2 (narrowing within 3.5–6.0):*
| Anchor | Score | Comparison |
|--------|-------|------------|
| HiDF (deepfake dataset) | 4.25 | Most comparable dataset paper. VIBEFACE's verification evaluation flaw is more fundamental than HiDF's "single generation tool" limitation. VIBEFACE slightly weaker. |
| ScalePerson (adversarial attack dataset) | 4.75 | Better evaluation design with standardized metrics. VIBEFACE weaker due to verification protocol issues. |
| FIUBench (facial unlearning benchmark) | 5.40 | Accepted. Stronger evaluation despite similar small dataset concerns. VIBEFACE clearly below. |
| Gone With the Bits (bias framework) | 4.25 | Different paper type but comparable quality. |
| DAP (deepfake assessment platform) | 3.80 | VIBEFACE is above — more unique dataset contribution. |

**Round 1 bracket:** 3.5–5.5

**Final score determination:** VIBEFACE sits between HiDF (4.25) and DAP (3.80), slightly below HiDF because the verification evaluation flaw (non-standard biometric metrics) is more fundamental than HiDF's single-tool limitation. The dataset's unique eKYC niche and ethical provenance are genuine strengths, but the evaluation methodology prevents the paper from convincingly demonstrating its utility. Combined with the small sample size for fairness claims, absence of a defined protocol, and uninformative detection benchmark, the paper requires major revision.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>