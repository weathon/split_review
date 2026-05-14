Now I have all the information I need. Let me write the comprehensive review.

---

## Summary

VIBEFACE introduces a dataset of 2,250 images and 1,550 videos from 50 subjects, specifically designed to include realistic eKYC (electronic Know Your Client) video scenarios such as head rotations, blinking, expression changes, and facial touching. The dataset is deliberately balanced across gender, four racial groups, and age ranges, collected under five lighting conditions with/without glasses, and ethically compliant with GDPR and AI Act. The paper benchmarks three face detectors and two face verification models across conditions and demographic subgroups. The eKYC video scenarios (scenarios 12–18) are a genuinely novel contribution not present in any prior public dataset.

## Strengths

- **Genuinely novel eKYC video scenarios**: Scenarios 12–18 explicitly capture real-world eKYC interaction dynamics (circular head rotation, directional tilts, blinking, expression changes, mouth opening, hand occlusion, sequential face touching — Section 3.2, Figure 3). Table 1 confirms that no prior public dataset includes such eKYC-style video protocols. This fills a documented gap for research on verification systems deployed in financial and regulatory compliance settings.

- **Deliberate demographic balance and metadata**: The dataset achieves a 50:50 gender split (25F/25M), balances four racial groups (13 African, 13 Caucasian, 12 East Asian, 12 South Asian — Figure 1b), and spans ages 18–69 conforming to ISO biometric testing standards (Section 3.1). Rich metadata (gender, age, race, facial hair, hair color, piercings, glasses) is provided for each subject, enabling covariate analysis.

- **Ethical and legal rigor**: Data collection followed GDPR and EU AI Act compliance with informed consent from all participants, controlled-access licensing, anonymized identifiers, and explicit prohibition of commercial use and re-identification (Sections 3.4, 3.5). This sets a strong example for responsible biometric dataset release.

- **Multi-session environmental diversity**: Five distinct acquisition sessions vary lighting (artificial, flash, natural daylight, weak natural light) and the presence/absence of eyeglasses (Section 3.3, Table 2). These are ecologically relevant factors known to affect verification performance, and the glasses session is particularly underexplored in prior work.

- **Comprehensive model coverage for a dataset paper**: The benchmark evaluates five off-the-shelf models (MTCNN, RetinaFace, MediaPipe for detection; ArcFace, MagFace for verification) across scenarios, sessions, and demographic subgroups (Tables 3–4), providing a broad initial characterization of dataset difficulty.

## Weaknesses

### Fatal

None.

### Major

- **Face verification protocol does not follow biometric evaluation standards**: The verification benchmark (Section 4.2) uses a single fixed similarity threshold of 0.5 with no analysis of the genuine/impostor score distribution, no ROC curve, no Equal Error Rate (EER), and no verification rate at a controlled false accept rate. The origin and justification of the 0.5 threshold are unexplained. The reported metric — "percentage of frames correctly authenticated" — is uncalibrated: without impostor pair testing, the reader cannot determine whether the system is secure or trivial. This substantially weakens the paper's claim that the dataset supports meaningful verification benchmarking. The verification results in Table 4 are, as presented, scientifically uninterpretable.

- **Demographic fairness claims lack statistical support**: The paper draws conclusions about subgroup disparities (e.g., "both models performed slightly worse on the Caucasian subgroup," "female participants consistently achieved slightly higher verification rates than males") from samples of only 12–13 subjects per racial group and 25 per gender, without any confidence intervals, error bars, or significance tests. Given the small per-group N, observed differences could easily be sampling noise. The fairness benchmarking claim requires at minimum an acknowledgment of these statistical limitations, and ideally proper quantification of uncertainty.

- **Overclaiming relative to dataset scale for fairness evaluation**: While 50 subjects is comparable to related specialized benchmarks (Table 1 shows similar datasets at 40–72 IDs), the paper frames VIBEFACE as "establishing a new benchmark for evaluating the robustness and fairness of biometric verification systems." With 12–13 subjects per racial group, the dataset lacks the statistical power to serve as a fairness benchmark. The eKYC contribution is real and valuable, but the fairness-benchmark framing is disproportionate to the dataset's capacity to support such analysis.

### Minor

- **Face detection benchmark partially saturated**: RetinaFace achieves 1.000 detection rates across most conditions (Table 3), and MediaPipe is near-ceiling in many cells. While the dataset does expose meaningful variation for MTCNN and in challenging scenarios (sessions C and E, scenarios 12–13), the detection task provides limited discrimination among strong detectors. This is not a fatal issue — the detection benchmark primarily serves to validate basic dataset usability — but limits its value as a detection challenge.

- **Limited differentiation from existing benchmarks in scale/scope discussion**: The paper's Table 1 provides a useful feature comparison but does not explicitly argue why the 50-subject scale is sufficient for the claimed benchmarking goals, given that related datasets like MOBIO (150 IDs) exist. A brief power analysis or discussion of minimum sample size for fairness testing would strengthen the contribution framing.

### Trivial

- The Related Work section adequately surveys prior datasets but does not discuss how VIBEFACE's scale compares to evaluation standards in biometrics (e.g., how many subjects are needed to detect a given effect size in verification performance).

## Nice-to-Haves

- A proper verification protocol with defined genuine/impostor pairings, ROC curves, and EER reporting would transform the benchmark from illustrative to scientifically useful.
- Bootstrap confidence intervals or standard errors for all subgroup breakdowns would clarify which observed differences are statistically meaningful.
- A cross-dataset evaluation showing that VIBEFACE's eKYC conditions expose failure modes that larger but less realistic datasets miss would help justify the 50-subject scale.
- Score distribution histograms (genuine vs. impostor similarity) per session would immediately convey whether the dataset presents a challenging verification problem.

## Removed Points

*These points were flagged in the input reviews but are removed from the final assessment for the stated reasons.*

- **"Dataset of 50 identities is fundamentally too small to serve as a benchmark" (compared to millions)**: The paper's Table 1 shows comparable specialized benchmarks (Replay-Mobile: 40, OULU-NPU: 55, MobiBits: 53, HQ-WMCA: 51, Soteria: 70 IDs). The criticism conflates training-scale datasets (VGGFace2, WebFace260M) with specialized evaluation benchmarks, which routinely operate at this scale. The size concern is only valid in the specific context of per-group fairness analysis (retained as a major weakness above).

- **"Paper fails to engage with the fact that existing benchmarks operate at scales two to three orders of magnitude larger"**: The paper directly engages with scale through Table 1, which lists datasets at comparable sizes (40–150 IDs). The claim that related evaluation benchmarks are orders of magnitude larger is factually incorrect for the relevant comparison class.

- **Criticism about missing related works**: Per instructions, not included as we cannot verify external references.

- **Formatting/style nitpicks, typos, parser artifacts**: These are parser issues, not paper problems. Removed per instructions.

## Novel Insights

The paper's core insight — that eKYC procedures impose a distinctive set of interaction dynamics (head rotation, blinking, expression change, mouth opening, hand occlusion, sequential face touching) not captured by standard face verification benchmarks — is genuinely novel and practically relevant. Table 1 demonstrates that no prior public dataset includes these protocols. This opens a research direction at the intersection of biometrics and compliance-driven authentication that currently lacks public evaluation resources. The insight that combining these eKYC dynamics with variable lighting and glasses creates a uniquely challenging testbed (evidenced by performance drops in sessions C and E) is valuable even if the current evaluation protocol cannot fully quantify it.

## Suggestions

- **Fix the verification protocol as the highest priority**: Define genuine and impostor pairings, compute and report full ROC curves and EER per condition, and report verification rate at a meaningful fixed false accept rate (e.g., 10⁻² or 10⁻³). Without this, the verification benchmark cannot support any of the paper's claims.
- **Add uncertainty quantification**: Report bootstrap confidence intervals or standard errors for all subgroup breakdowns. If statistical power is insufficient to detect meaningful demographic effects, acknowledge this explicitly and frame the dataset as a resource for studying eKYC conditions rather than as a fairness benchmark.
- **Tone down the fairness benchmark framing**: The eKYC contribution is strong enough to stand on its own. Frame VIBEFACE as "a resource for evaluating face verification under realistic eKYC conditions with demographic metadata" rather than "a new benchmark for fairness." The dataset's demographic balance is valuable as a design feature, not as a statistical claim.
- **Discuss the 0.5 threshold**: Explain its origin. If it was chosen arbitrarily, acknowledge this and demonstrate sensitivity to threshold choice.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Decision | Comparison to VIBEFACE |
|--------|-----------|----------|------------------------|
| BANZ-FS (`GMR9BUsPbq`) | 7.00 | Accept (Poster) | Substantially stronger: 35k+ instances, 116 signers, multi-level annotations, comprehensive benchmarks across tasks and domains. VIBEFACE's scale and evaluation depth are far below this standard. |
| NH-Fair (`GLPmZhhCAE`) | 5.50 | Accept (Poster) | Stronger: 10k+ GPU-hours of systematic hyperparameter optimization, 7 datasets, multiple model families. VIBEFACE's experimental scope is much narrower, though the eKYC novelty is more original than NH-Fair's benchmarking contribution. |
| FaceMoE (`O4f1NdXtdM`) | 5.00 | Reject | Stronger methodologically: 11 datasets, rigorous ablations, state-of-the-art results. VIBEFACE's contribution is more curatorial but fills a clearer gap. Similar level of evaluation incompleteness. |
| FaceID-6M (`yTq81RcKaw`) | 3.50 | Reject | Similar genre (dataset paper). FaceID-6M has larger scale but limited novelty (LAION filtering pipeline), weak evaluation, and no ethical framework. VIBEFACE has a more novel angle (eKYC), stronger ethical grounding, and a comparable level of evaluation gaps. VIBEFACE is moderately stronger. |
| VAD Dimensional Analysis (`I1TBgjF9FU`) | 3.50 | Reject | Weaker: meta-analysis with vague guidelines and limited model coverage. VIBEFACE's concrete dataset contribution with novel eKYC scenarios is more valuable. |
| Adaptive Calibration (`7iwqu82yOC`) | 2.50 | Reject | Significantly weaker: limited novelty, outdated models, improper evaluation metrics. VIBEFACE has a clearer and more original contribution. |

**Calibrated score: 4.0.** VIBEFACE makes a genuinely novel contribution with its eKYC video scenarios and strong ethical practices. However, the verification evaluation protocol is methodologically insufficient to support the paper's benchmarking claims, and the fairness conclusions are drawn without statistical support from samples too small to sustain them. The paper sits above FaceID-6M (3.50) due to stronger originality and ethical compliance, but below FaceMoE (5.00) due to weaker experimental validation. A substantially revised evaluation with proper biometric metrics and uncertainty quantification could raise this to borderline-acceptable territory.

---

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>