Now I have all the information I need. Let me compile the final review.

**Bracket from Round 1:** I initially bracketed this between the weak anchors (~3.0 range for methodologically limited papers) and the strong dataset anchors (~6.0+). My initial bracket was **3.5–5.0**.

**Narrowing from Round 2:** I compared against ScalePerson (4.75), HiDF (4.25), UDC-VIT (6.00), and EyeFairness (5.50). VIBEFACE is weaker than UDC-VIT (which has a novel capture setup and cross-dataset comparison) and EyeFairness (much larger scale). It is comparable to ScalePerson (both have good motivation but insufficient experiments) and somewhat weaker than HiDF (larger dataset). The range narrows to **3.5–4.5**, and within that, the paper sits closer to 4.0 given that the core gap (eKYC scenarios) is real but the validation is too weak.

---

## Summary

VIBEFACE introduces a multimodal dataset (2,250 images and 1,550 videos from 50 subjects) designed to support face verification in electronic Know Your Client (eKYC) workflows. The dataset is collected with strong ethical and legal compliance (GDPR, AI Act, informed consent), includes balanced demographic metadata across gender, race, and age, and covers eKYC-specific video scenarios (head rotation, blinking, expression changes, etc.) that are absent from existing public datasets. The paper also provides baseline face detection and verification benchmarks using standard models.

## Strengths

- **First public dataset to include authentic eKYC-style video scenarios.** Table 1 shows VIBEFACE is the only dataset among the nine compared that marks ✓ for "eKYC." Section 3.2 describes seven eKYC verification video scenarios (scenarios 12–18) — circular head rotation, tilting, blinking, expression change, mouth opening, hand covering, and face touching — that directly mimic real-world eKYC workflows. This fills a gap clearly identified in Section 2.

- **Demographic balance with explicit metadata.** The dataset achieves a 50:50 gender split (25M/25F), near-equal representation across four self-identified ethnic groups (African 26%, Caucasian 26%, East Asian 24%, South Asian 24%), and three age bands (18–30, 31–50, 51–70) each with at least 14 subjects. Figure 1 and Section 3.1 document this. Per Table 1, VIBEFACE is the only dataset with ✓ marks for all three of gender balance, race balance, and age balance among the compared datasets.

- **Exemplary ethical and legal compliance.** Section 3.4 details informed consent, anonymization with randomized identifiers, GDPR (EU 2016/679) and AI Act (EU 2024/1689) compliance, and a controlled-access license for non-commercial academic use (Section 3.5). Section 2 notes that widely used datasets such as MS-Celeb-1M, VGGFace2, and MegaFace were collected without explicit consent and have been withdrawn — making VIBEFACE a legally reusable resource.

- **Multi-device and multi-condition acquisition.** Data were captured with three consumer smartphones (Xiaomi Redmi Note 13, Apple iPhone 13, Samsung Galaxy A35 5G) across five sessions that vary lighting (artificial, flash, natural daylight, weak natural light) and include an eyeglasses condition. Images are high resolution (min. 2316×3088 pixels) and videos are Full HD (1920×1080). The controlled, supervised acquisition protocol (standardized instructions, neutral expression, 30–60% face-to-frame width) ensures reproducibility.

- **Baseline evaluations with demographic/scenario breakdowns.** Tables 3 and 4 report detection and verification rates broken down by scenario, session, gender, age group, and racial category for multiple models, providing initial reference points.

## Weaknesses

### Fatal
None.

### Major

- **N=50 fundamentally limits the stated fairness and robustness evaluation goals.** The paper frames VIBEFACE as a benchmark for "evaluating the robustness and fairness of biometric verification systems" (Abstract) and reports demographic breakdowns. With 50 subjects split into four racial groups (~12–13 each) and three age groups (~14–19 each), subgroup analyses have very limited statistical power. Observed disparities (e.g., MTCNN's lower detection for African subjects in Table 3; "Caucasian subgroup underperformance" in Table 4) are reported without confidence intervals, standard deviations, or significance tests, so the reader cannot distinguish genuine demographic patterns from sampling noise. The paper does not acknowledge this limitation. This does not invalidate the dataset's value as a carefully collected resource, but it means the fairness and robustness claims are not supported by the evidence as presented.

- **The benchmark evaluation does not demonstrate the dataset's value over existing resources.** The paper runs face detection and verification on VIBEFACE but never compares performance on existing datasets (e.g., MOBIO, SOTERIA, Replay-Mobile). Without such a comparison, the reader cannot assess whether VIBEFACE's eKYC scenarios actually reveal different failure modes or pose novel challenges. The core claim — that existing datasets "fail to capture the natural dynamics of eKYC interactions" — is plausible but not empirically substantiated.

- **Non-standard evaluation metrics undermine the benchmarks.** Verification is reported as the percentage of frames exceeding a fixed similarity threshold of 0.5 (Section 4.2), rather than standard biometric metrics such as EER, AUC, or FNMR at a given FMR. A single fixed threshold applied uniformly to both ArcFace and MagFace (which have different score distributions) is arbitrary and untuned — no validation set was used to select it. Frame-level rates also inflate the effective sample with correlated frames from the same video. The results are difficult to compare with any existing or future work as a result.

### Minor

- **Verification protocol conflates detection and verification failures.** The paper reports verification success as the percentage of frames where similarity exceeds the threshold, but does not clarify what happens when no face is detected (MTCNN achieves as low as 57.7% detection in some conditions). Frames with no detection would produce no verification score and would be counted as verification failures. Since RetinaFace and MediaPipe have near-perfect detection while MTCNN does not, the verification comparison partially reflects detection gaps rather than verification model quality. The paper should disentangle these.

- **Missing details hamper reproducibility.** The paper does not specify video lengths or frame counts per video (only "short videos" and a 6 fps sampling rate in the benchmark section), the exact frame rate of recordings, the number of frames per video at the 6 fps sampling rate, or the total number of frames in the benchmark. The reference image for verification (a single frontal from the flash session, Scenario 3 Session B) is used without analysis of sensitivity to this choice.

- **Minor overclaim about PAD.** The conclusion (Section 5) states the dataset is "well-suited for advancing research in presentation attack detection (PAD)," but the dataset contains no attack samples — only bona fide samples. This is a speculative forward-looking statement rather than a false claim (bona fide samples are necessary for PAD research), but it goes beyond what the paper demonstrates.

### Trivial
None.

## Nice-to-Haves

- A comparison with at least one existing dataset (e.g., MOBIO or SOTERIA) to demonstrate that VIBEFACE's eKYC scenarios produce meaningfully different verification patterns.
- Replace the fixed-threshold frame-level verification rate with subject-level metrics (EER, FNMR@FMR) with bootstrapped confidence intervals, using a held-out threshold selection protocol.
- Acknowledge the N=50 limitation explicitly and position the dataset as a carefully collected, ethically compliant resource suitable for controlled experiments, protocol design, and as a supplement to larger benchmarks rather than as a standalone fairness benchmark.

## Removed Points

- *Criticism about the temporary link not persisting:* The paper states the dataset is available through the official project website with a license agreement. The temporary link is a review artifact; removed per Hard Rules on reproducibility concerns rooted in process rather than content.
- *Criticism that the claim about being "first" is not formally verified against all possible datasets:* Scope creep — Table 1 supports the claim relative to the listed comparable datasets, which is standard for dataset papers.
- *Criticism about the demographic pyramid visual "showing gaps":* The reviewer acknowledged this was mistaken (the table confirms 9 males in 18–30). Removed as factually wrong.
- *Criticism about format/grammar/punctuation:* Removed per Hard Rules — parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the paper's contribution explicitly: present VIBEFACE as a high-quality, ethically compliant, small-scale dataset focused on eKYC scenario coverage, with open acknowledgment of the N=50 limitation and what analyses it does and does not support.
2. Add a cross-dataset comparison experiment to demonstrate that eKYC scenarios yield different verification outcomes than standard protocols.
3. Replace the frame-level verification rate with standard biometric metrics (EER, FNMR@FMR) using proper threshold selection and bootstrapped confidence intervals.
4. Add a brief limitations paragraph in the conclusion that discusses sample size constraints and their implications for subgroup analysis.
5. Provide video duration statistics (mean, min, max, total frames) in the dataset description section.

## Score and Decision

**Anchor Papers Used for Calibration:**

| Paper | Score | Round | Comparison to VIBEFACE |
|---|---|---|---|
| ScalePerson (3iGponpukH) | 4.75 | R1/R2 | Dataset paper filling a gap, rejected. VIBEFACE has comparable dataset design quality but weaker experimental validation (231 experiments in ScalePerson vs. simple baselines in VIBEFACE). VIBEFACE has stronger ethical compliance. Slightly weaker overall. |
| HiDF (XhyCPEnlCa) | 4.25 | R2 | Deepfake dataset (30K images, 4K videos), rejected. HiDF is larger in scale but VIBEFACE fills a different gap. Similar level of methodological rigor in experiments. Comparable quality. |
| UDC-VIT (DNBwlQYA90) | 6.00 | R2 | Real-world UDC video dataset, rejected despite score. Has a novel capture setup and cross-dataset validation that VIBEFACE lacks. VIBEFACE's contribution (eKYC gap) is comparable in importance but less well-validated. VIBEFACE is weaker. |
| EyeFairness (Lv9KZ5qCSG) | 5.50 | R1 | Large-scale medical dataset (30K subjects), rejected. Much larger scale and more extensive fairness experiments. VIBEFACE is substantially weaker in scale and validation depth. |
| "Does Your Mobile Suit Your Skin" (dEGYODD6iU) | 3.67 | R1 | PAD application paper, rejected. VIBEFACE has a more concrete dataset contribution and better ethical compliance. VIBEFACE is stronger. |

**Round 1 bracket:** 3.5–5.0  
**Round 2 narrowing:** Comparing against ScalePerson (4.75, stronger validation but no ethical edge), HiDF (4.25, comparable), and UDC-VIT (6.00, clearly stronger), the paper lands below 4.75 and above 3.67.  
**Final position:** Closer to HiDF (4.25) but slightly weaker due to the N=50 limitation for the stated fairness claims. Final score: **4.0**.

The paper has a genuine contribution (first eKYC-focused public dataset with strong ethical compliance), but the N=50 sample size and weak benchmark evaluation (no cross-dataset comparison, non-standard metrics, no error bars) mean the contribution is not adequately validated and the fairness/robustness framing overreaches what the data can support.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>