Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

## Summary

VIBEFACE is a facial image/video dataset targeting the eKYC (electronic Know Your Client) domain, containing 2,250 images and 1,550 videos from 50 subjects balanced across gender (25F/25M), race (4 categories, ~25% each), and age (3 groups). Data was collected across 5 sessions varying lighting and eyeglass occlusion using 3 consumer smartphones. The paper includes benchmark evaluations for face detection (MTCNN, RetinaFace, MediaPipe) and face verification (ArcFace, MagFace) with demographic breakdowns.

## Strengths

1. **First public dataset with eKYC-specific video scenarios** — Table 1 shows VIBEFACE is the only dataset among eight compared that includes an eKYC column. Section 3.2 describes seven verification video scenarios (12–18) explicitly mimicking real eKYC workflows (circular head rotation, blinking, expression changes, mouth opening, occlusion sequences). This is a genuine gap-filling contribution.

2. **Demographic balance across gender, race, and age** — Section 3.1 reports exactly 25 female and 25 male participants (50:50). Figure 1B shows a near-equal split across four racial categories (African 26%, Caucasian 26%, East Asian 24%, South Asian 24%). Table 1 marks VIBEFACE as the only dataset with checks for all three demographic-balance criteria among compared resources. This is rare in the existing facial biometrics landscape.

3. **Ethical and legal compliance** — Section 3.4 documents informed consent, GDPR and AI Act compliance, anonymization via randomized identifiers, and a controlled-access license (Section 3.5). This directly addresses the withdrawal of earlier datasets (MS-Celeb-1M, VGGFace2) due to privacy failures noted in Section 2, and sets a responsible standard for future face dataset releases.

4. **Systematic session variability** — Section 3.3/Table 2 defines five acquisition sessions varying lighting (artificial, flash, natural daylight, weak natural light) and including an eyeglass-occlusion session. The benchmark results in Tables 3 and 4 show that sessions C (glasses) and E (weak light) produce consistent performance drops across detectors and verifiers, confirming that the controlled variability is meaningful for robustness evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **Sample size (50 subjects) fundamentally limits the fairness claims the paper invites.** With only 50 subjects and 12–13 per racial category, the reported demographic breakdowns in Tables 3 and 4 (e.g., MTCNN on African vs. East Asian subjects) can be driven by a few individuals rather than population-level disparities. The paper claims to "ensure coverage and balance of demographic attributes" and to support fairness evaluation, but without confidence intervals, statistical tests, or per-subject variance, the benchmark tables give a false impression of statistical reliability. This is not a fixable issue at the current scale — it is an inherent constraint. A 50-subject dataset can be a useful controlled resource (analogous to Multi-PIE's role), but the paper needs to explicitly reframe its claims from "fairness benchmarking" to "small-scale controlled evaluation."

2. **Benchmark methodology lacks statistical rigor.** Tables 3 and 4 report only aggregate percentages without any measure of variance (standard deviation, confidence intervals, or per-subject distributions). With tiny demographic subgroups, this is potentially misleading. The detection results show ceiling performance for RetinaFace and MediaPipe (1.000 across almost all conditions in Table 3), rendering the detection task uninformative for differentiating detector robustness. The verification task uses a single fixed threshold (0.5) rather than reporting at a fixed FAR or providing ROC/DET curves, which is non-standard for biometric evaluation and can unfairly penalize models with different optimal thresholds.

3. **Disconnect between the "unconstrained" motivation and the controlled studio collection.** The introduction motivates the dataset by stating that "eKYC sessions often involve users recording short videos under unconstrained conditions — at home, in variable lighting, and across heterogeneous mobile devices," but Section 3 states that "Data acquisition was conducted in a controlled studio environment" with trained operators, standardized instructions, and supervised sessions. Participants did not act naturally in their own environments; they followed a scripted protocol. While the paper is transparent about the studio setting, the central framing overclaims the "realism" of the data. The dataset occupies an awkward middle ground: it is more controlled than genuine in-the-wild data, but not as clean as a pure laboratory dataset.

### Minor

4. **No cross-device experiments despite having three phone models.** The dataset was collected with Xiaomi Redmi Note 13, Apple iPhone 13, and Samsung Galaxy A35 5G, but the benchmarks do not evaluate whether cross-device matching (e.g., reference from one phone, query from another) affects performance. This is a natural experiment the dataset structure supports but the paper does not run.

5. **Unsupported Fitzpatrick scale claim.** Section 3.1 states "we also ensured that the skin tones of participants reflect the whole spectrum of Fitzpatrick's scale," but no Fitzpatrick type distribution is provided in the paper or used in the benchmark analysis. This reads as an unsupported assertion.

6. **No video-level analysis.** The benchmarks extract frames at 6 fps and report frame-level rates, but do not analyze verification rates across the duration of an action (e.g., blink sequence), whether some actions are harder than others, or how temporal dynamics affect verification. This underutilizes the video modality that is the paper's distinguishing feature.

### Trivial

7. The related work comparison table (Table 1) uses checkmarks but several entries are empty for most columns (e.g., MOBIO has checkmarks only in "Videos"), making column headers like "DD," "GB," "RB," "AB" appear as empty checks rather than absences. A clearer visual convention (e.g., ✓ vs. ✗ vs. —) would improve readability.

## Nice-to-Haves

- Cross-session verification was already done (reference from Session B flash, queries from Sessions A/C/D/E), but the paper could explicitly frame this as a cross-session experiment and add cross-device experiments.
- Running detection on occluded scenarios (17–18) even if expected to fail, to demonstrate detector failure modes.
- Per-subject variability plots or bootstrapped confidence intervals for the benchmark results.
- A simple liveness detection or PAD baseline to showcase additional value beyond detection and verification.

## Removed Points

These points were raised by the reviewers but are removed with justification:

- **"No cross-session verification"** — REMOVED (factually incorrect). The paper evaluates verification using a reference from Session B (flash, standardized) with queries from Sessions A, C, D, E — this is cross-session verification. The reviewer misread the experimental setup.

- **"Missing datasets like LFW, IJB-C in related work"** — REMOVED. The paper is scoped to mobile/eKYC datasets; the comparison is appropriate for its stated focus. The selection criteria are implicit in Table 1's column headers.

- **"Scenarios 17-18 exclusion is a missed opportunity"** — DEMOTED to Nice-to-have. Excluding heavily occluded scenarios from detection is a reasonable experimental design choice; including them would be additional evidence but not a flaw to omit them.

- **"Dataset should be expanded in future versions"** — REMOVED. This is speculation about future plans, not a weakness of the presented work.

- **"No discussion of comparison in terms of subjects per demographic cell"** — REMOVED. The paper provides this information in Figure 1 and Section 3.1 (exact counts: 13 African, 13 Caucasian, 12 East Asian, 12 South Asian).

- **"Weakness about unfair comparison with other methods"** — Not applicable; no such claim was made by reviewers.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension that is already implicit in the paper: the dataset fills a genuine gap (eKYC-specific video data with demographic balance and ethical sourcing) but at a scale (N=50) that cannot support the fairness-benchmarking claims the paper makes. This tension is recognized in the weakness about sample size, but neither the paper nor the reviews offer a resolution — the dataset either needs to grow substantially or the claims need to be explicitly scaled back.

## Suggestions

1. **Reduce the scope of claims** — Reframe the paper from "fairness and robustness evaluation" to "small-scale, controlled evaluation resource with per-subject depth." Explicitly acknowledge the sample size limitation and its implications for statistical inference. The Multi-PIE / Color FERET analogy suggested by one reviewer is a good framing.

2. **Add variance measures to all benchmark results** — At minimum, report per-subject means with standard deviations, or use bootstrapped confidence intervals. This is essential when demographic subgroups have N≈12.

3. **Run the natural cross-session and cross-device experiments the dataset supports** — The verification benchmark already uses cross-session matching (reference from Session B, queries from A/C/D/E), which should be highlighted. Adding device-stratified results would leverage the multi-device collection.

4. **Replace or supplement the single-threshold verification with FAR-based reporting** — Report verification rates at a fixed false acceptance rate (e.g., FAR=0.001 or 0.01) using the similarity score distribution, which is standard in biometric evaluation.

## Score and Decision

Let me now run the final calibration analysis.

**Round 1 bracket (from initial searches):** I placed the paper between 3.5 and 5.5. The low-end anchors (2–3) had major ethical issues or minimal novelty (CrossFaceID, FFHQ-Makeup). The mid-range anchors (4–5) had genuine contributions but significant limitations (IDSPACE, OVid, FaceID-6M). The high-end anchors (7+) were substantially larger-scale, more comprehensive dataset efforts (InclusiveVidPose: 398 subjects, 327k frames, new metric; BANZ-FS: 35k instances, 116 signers, multi-domain).

**Round 2 narrowing:** Comparing VIBEFACE against specific anchors:
- **IDSPACE (avg 4.00):** Both are niche datasets with clear application gaps. IDSPACE generates synthetic ID documents with BO tuning; VIBEFACE collects real eKYC facial data. VIBEFACE has stronger ethical foundations and fills a clearer gap, but has smaller subject count. Slightly above IDSPACE.
- **FaceID-6M (avg 3.50):** 6M images but inherited LAION's ethical problems and had limited curation novelty. VIBEFACE has better novelty (first eKYC) and ethics. Clearly above FaceID-6M.
- **OVid (avg 4.50):** Massive scale (10M hours video) but caption quality issues limited its demonstrated value. VIBEFACE is more focused and useful for its specific domain. Comparable tier, with VIBEFACE slightly weaker on scale but stronger on focus.

VIBEFACE's core contribution is genuine (first public eKYC dataset with demographic balance), and the ethical compliance is thorough. However, the 50-subject scale fundamentally limits what the dataset can support, and the disconnect between "unconstrained" framing and controlled studio collection weakens the motivational claims. The benchmarks are functional but thin and lack statistical rigor. This paper lands at the lower end of the borderline range — it has a real contribution but the evidence does not convincingly demonstrate sufficient utility to warrant acceptance at a top venue in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>