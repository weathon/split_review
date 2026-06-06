## Summary

VIBEFACE is a new multimodal facial biometric dataset of 50 demographically balanced subjects (25M/25F, 4 racial groups, 3 age brackets), comprising 2,250 still images and 1,550 videos captured across five sessions varying lighting and eyeglasses on consumer smartphones. Its central claim is that it is the first publicly available dataset to include eKYC-style liveness-challenge videos (Scenarios 12–18: head rotation, blinking, expression changes, hand occlusion, face-touching sequences) alongside standardized photographs, enabling fair benchmarking of biometric systems. The dataset utility is demonstrated through face detection (MTCNN, RetinaFace, MediaPipe) and face verification (ArcFace, MagFace) benchmarks.

---

## Strengths

- **Unique eKYC video coverage**: Scenarios 12–18 explicitly replicate challenge-response sequences used in real electronic Know Your Customer workflows (circular head rotation, blinking, expression change, mouth opening, hand occlusion, sequential face touching). Table 1 confirms no comparable publicly available dataset includes this category, directly supporting the paper's gap claim.

- **Deliberate three-axis demographic balance**: The dataset achieves near-equal representation across gender (25M/25F), three age brackets (18–30: 19, 31–50: 17, 51–70: 14), and four self-identified racial groups (African 26%, Caucasian 26%, East Asian 24%, South Asian 24%), as shown in Figure 1. This is explicitly tied to the fairness use case and is rarer than most datasets in Table 1 (e.g., SOTERIA lacks age balance, MOBIO and OULU-NPU have no demographic metadata at all).

- **Informative detection benchmark exposing demographic disparities**: Table 3 reveals that MTCNN achieves 0.812 on frontal views for African subjects versus 0.984 for East Asian subjects — a 17-point difference for a nominally easy condition — providing a concrete fairness signal. The three-model comparison across sessions, scenarios, and all demographic axes is thorough and practically informative.

- **Systematic session and device variation**: Five sessions with four distinct lighting conditions and eyeglasses variation, combined with randomized assignment of three smartphone models (Xiaomi Redmi Note 13, Apple iPhone 13, Samsung Galaxy A35), introduce genuine and well-controlled covariates relevant to mobile authentication.

- **GDPR and AI Act compliant collection with informed consent**: The ethical and legal framework is explicit and complete, addressing a real deficiency of many prior Internet-scraped datasets that have since been withdrawn.

---

## Weaknesses

### Fatal

None.

### Major

- **The face verification benchmark uses a non-standard fixed-threshold metric that yields largely uninterpretable results.** Section 4.2 states: "Verification was considered successful when the similarity score exceeded a fixed threshold of 0.5." Applied uniformly to ArcFace and MagFace — which have different cosine similarity distributions — without calibration, this produces results that cannot be meaningfully compared between models or conditions. The off-angle view (OAV) rows in Table 4 illustrate the problem starkly: ArcFace achieves 0.509/0.433/0.505/0.481 across sessions, and MagFace achieves 0.274/0.262/0.298/0.296 — both in near-random territory. The paper then states "ArcFace consistently outperformed MagFace," which is nominally true but misleading when both models are performing near chance at this operating point. Biometric verification benchmarks are standardized around EER, TAR@FAR, and ROC curves to characterize the genuine/impostor tradeoff. Without any FAR measurement, the paper cannot answer whether the observed demographic breakdowns reflect real bias or threshold miscalibration artifacts. A properly defined protocol (genuine cross-session pairs, impostor pairs, EER/ROC) requires no new data collection — the sessions and scenarios already support it — but the paper as submitted does not deliver it. This is the most consequential gap: one of the paper's two benchmark tasks is only weakly informative.

- **The verification reference image (Session B, rear camera flash, Scenario 3) differs from all query images not only in lighting but in camera module.** Table 2 explicitly shows that Session B is conducted with the back-facing camera, while all selfie and video scenarios use the front camera. The paper acknowledges the flash/rear camera constraint but does not discuss the probe-reference confound this introduces: any session-level verification performance difference conflates lighting with front-vs-rear camera intrinsics. This is an unacknowledged systematic confound in the experimental design.

### Minor

- **"Unconstrained / at home" framing in the introduction is inconsistent with the controlled studio collection.** The introduction states "eKYC sessions often involve users recording short videos under unconstrained conditions — at home, in variable lighting." Section 3 states: "Data acquisition was conducted in a controlled studio environment, each session in a separate room specifically arranged... participants received standardized instructions and were continuously supervised by trained operators." The lighting variation (four distinct conditions) and device randomization are genuine contributions, but the spatial environment, posture, and behavioral compliance are all controlled. The paper should describe VIBEFACE as capturing device and lighting variation under controlled conditions, not as capturing home/unconstrained behavior. This is a framing issue, not a flaw in the dataset itself.

- **Demographic performance conclusions are drawn without statistical tests from very small per-group samples.** The paper claims "Both models performed slightly worse on the Caucasian subgroup" and "female participants consistently achieved slightly higher verification rates than males" (Section 4.2). With 12–13 subjects per racial group and 25 per gender, reported differences of 2–5 percentage points are within a range where individual variation or outlier subjects could dominate. These observations should be presented as exploratory signals to be confirmed at scale rather than stated as established findings.

- **Scenarios 17 and 18 — the most distinctively eKYC-specific actions — are excluded from both benchmark tasks** (Section 4.1: "scenarios 17 and 18 were omitted because they involve occlusions that significantly reduce facial visibility"). Hand occlusion (Scenario 17) and sequential face touching (Scenario 18) are among the scenarios with no analogue in prior datasets, yet neither detection nor verification is evaluated on them. The paper's core eKYC utility claim rests partly on these scenarios, and excluding them from all benchmarks leaves the claim incompletely demonstrated.

### Trivial

None beyond formatting artifacts from the PDF parser, which are not author errors.

---

## Nice-to-Haves

- Adding a standard verification protocol (defined genuine/impostor pairs, EER, TAR@FAR=0.1%/1%, ROC curves) would immediately transform Table 4 into a result biometrics researchers can use. The dataset already supports this; the incremental implementation cost is minimal.
- Including Scenarios 17 and 18 in at least the face detection evaluation would more forcefully demonstrate the dataset's eKYC relevance by showing that current detectors fail on exactly the conditions that distinguish VIBEFACE from prior resources.
- A brief acknowledgment that 50 subjects limits use for training or large-scale distribution shift studies (the dataset is positioned as a benchmark resource) would be appropriate.
- The conclusion mentions PAD/deepfake detection as future applications; a short forward-looking discussion of what additional collection (e.g., spoofing attacks) would be required to enable those uses would strengthen the paper.

---

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Per-subject variance for group-level detection rates** (harsh critic, Section 4.1): The critic noted that with 12–13 subjects per racial group, a single outlier could drive differences. This is statistically correct in principle, but the MTCNN disparity (0.812 vs. 0.984) is large enough to be noteworthy even under this caveat, and the concern is already captured in the Minor weakness about statistical tests. Removed as a separate standalone point to avoid duplication.

- **Session asymmetry limiting the dataset's verification claim** (harsh critic, Section 3.3): The critic flagged that Session B (flash) contains only standardized photos and creates asymmetry. This is already captured under the Major weakness about the front/rear camera confound. Removed as a duplicate framing.

- **Generic strength about "important research area"**: The Strength Finder's framing that eKYC is a growing and important domain was dropped as a standalone strength because it is generic and not specific to the paper's content. The concrete strengths (unique scenario coverage, demographic balance) replace it.

---

## Novel Insights

The paper's most underappreciated finding sits in Table 3: MTCNN shows a 17-point accuracy gap between African (0.812) and East Asian (0.984) subjects on *frontal* views — the supposedly easy case — while RetinaFace achieves perfect detection for all demographic groups across all scenarios. This suggests that MTCNN's demographic disparity is primarily a training distribution artifact, not an inherent limitation of the modality, since a better-trained model eliminates it entirely. VIBEFACE's demographic balance is precisely what makes this comparison possible; a dataset weighted toward East Asian faces would mask the MTCNN failure mode. This is a concrete research finding, not just a demonstration.

---

## Suggestions

1. Replace the fixed-threshold "frame authentication rate" in Section 4.2 with a proper verification protocol: define genuine pairs (same subject, Session A vs. D or E) and impostor pairs (different subjects, matched scenario), report EER and TAR@FAR=0.1%/1% per demographic group, and include ROC curves. No new data collection is required.
2. Revise abstract and introduction to accurately characterize the acquisition setting as "controlled studio with variation in lighting, device, and eyeglasses" rather than "unconstrained / at-home."
3. Add at least a face detection evaluation for Scenarios 17 and 18, with a note that the occlusion makes detection intentionally challenging. This converts the most distinctive eKYC scenarios from "present in the dataset but unevaluated" to "present and shown to challenge current systems."
4. Add a sentence explicitly framing the demographic comparisons (gender, race, age) in the verification results as preliminary observations, noting the small per-group sample size limits statistical power.
5. In Section 3.3 or 4.2, explicitly discuss the front-vs-rear camera confound in the verification reference setup and note it as a limitation of the chosen protocol.

---

## Evaluation on Key Axes

- **Originality**: Moderate. The dataset format (controlled multimodal collection) is conventional, but the eKYC scenario set and the specific combination of features (GDPR compliance, four racial groups, three age brackets, eKYC-specific videos, eyeglasses sessions) has no direct precedent in the publicly available landscape as shown by Table 1.
- **Importance**: Moderate-to-high. eKYC verification is a real industrial need and the absence of fair, legally compliant benchmarks is genuine. The dataset addresses a practical gap.
- **Claims supported**: Partially. The detection claim (VIBEFACE enables demographic analysis of detectors) is well-supported. The verification claim (VIBEFACE enables fair biometric benchmarking) is only weakly supported by the current fixed-threshold evaluation.
- **Soundness of experiments**: Detection benchmark is sound. Verification benchmark has a significant methodological flaw (no calibration, no EER/ROC).
- **Clarity of writing**: Good overall. Scenario descriptions are precise and Table 2 is an effective overview. The verification results section overstates the informativeness of Table 4.
- **Value to research community**: Solid, assuming the dataset is released as described. A well-balanced, GDPR-compliant, eKYC-specific dataset fills a clear gap regardless of the benchmark methodology.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>