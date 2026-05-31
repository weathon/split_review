Now let me run calibration searches to anchor my score.Round 1 bracket: **4.0–6.0**. Now narrowing.Now I have enough calibration material to write the final review.

**Calibration summary:**
- *EyeFairness* (5.50) — dataset paper + fairness method, 30,000 subjects, 6 demographic attributes, stronger methodology
- *HiDF Deepfake Dataset* (4.25) — pure dataset paper, 30K images/4K videos, limited tools diversity
- *CCo8ElCT7v ViT vs CNN* (4.25) — empirical comparison, face recognition, missing key comparisons
- *lAhQCHuANV ROC fairness in FR* (6.33) — theoretical + empirical analysis of FR fairness, stronger methodology

Round-1 bracket: **4–6**. Round-2 anchors cluster at 4.25–5.5. VIBEFACE is weaker than EyeFairness (5.5) in scale and lacks an algorithmic contribution; it is comparable to HiDF (4.25) as a modest-scale pure-dataset paper but has stronger genuine novelty (first eKYC dataset with demographic balance). I place it slightly above the 4.25 cluster given the real gap it fills, but the weak verification benchmark and small scale hold it there.

**Final bracket: 4.0–4.5 → score 4.0**

---

## Summary
VIBEFACE is a multimodal facial biometric dataset of 50 participants, comprising 2,250 still images and 1,550 videos collected under five sessions varying lighting and eyeglasses conditions. Its principal contribution is the first publicly available collection of eKYC-style verification videos (scenarios 12–18), combined with deliberate demographic balance across gender, age brackets, and four racial categories, all collected under GDPR-compliant informed consent. The dataset's utility is demonstrated through face detection and face verification benchmarks across multiple state-of-the-art models.

## Strengths
- **First eKYC-specific dataset with demographic balance**: VIBEFACE introduces seven video scenarios (scenarios 12–18 — circular rotation, head tilt, blinking, expression change, mouth opening, hand occlusion, face touching) that map directly to action-based eKYC workflows. As Table 1 confirms, no prior publicly available dataset provides this combination with photos, videos, and demographic balance.
- **Principled three-axis demographic design**: With 25M/25F subjects, three age brackets (18–30, 31–50, 51–70), and four racial categories at near-equal proportions (13/13/12/12), the dataset is explicitly designed for fairness benchmarking, something absent from most prior work in Table 1.
- **Informative face detection benchmark**: Table 3 presents per-session, per-scenario, per-demographic detection rates across MTCNN, RetinaFace, and MediaPipe. The MTCNN result (0.812 for African vs. 0.984 for East Asian on frontal views) is a concrete, grounded finding demonstrating the dataset's diagnostic value for bias auditing.
- **Sound ethical and legal grounding**: GDPR/AI Act compliance, informed consent, controlled-access licensing, and anonymized identifiers are explicitly described in Section 3.4 — an important differentiator from the Internet-scraped corpora the paper contrasts itself against.

## Weaknesses

### Fatal
None.

### Major
- **Non-standard face verification evaluation metric**: Section 4.2 defines verification success as exceeding a fixed cosine-similarity threshold of 0.5 applied uniformly to both ArcFace and MagFace, reporting "percentage of frames correctly authenticated." This is not a standard biometric protocol; the field uses EER, TAR@FAR, and ROC curves, which characterize the genuine/impostor tradeoff across operating points rather than at a single, uncalibrated threshold. As a consequence, Table 4 is partially uninterpretable: ArcFace OAV values of 0.433–0.519 and MagFace OAV values of 0.274–0.308 are both near-random for off-angle views, yet the paper's text frames ArcFace as "consistently outperforming" MagFace without acknowledging that both models at this threshold are performing poorly on OAV. Without genuine/impostor pair definitions and EER/ROC evaluation, the paper cannot actually demonstrate whether VIBEFACE is suitable for biometric verification benchmarking — which is one of its two stated benchmark tasks. The framework for a proper protocol is already in place (sessions naturally define cross-session genuine pairs), so this is correctable without new data collection.

### Minor
- **Overstated ecological validity**: The introduction describes eKYC as involving "users recording short videos under unconstrained conditions — at home, in variable lighting," yet Section 3 states explicitly that "data acquisition was conducted in a controlled studio environment, each session in a separate room specifically arranged to ensure consistent experimental conditions... participants... continuously supervised by trained operators." The dataset captures lighting variation and device variation but does so in a controlled studio, not in unconstrained in-the-wild conditions. The realism framing should be calibrated accordingly.
- **Demographic conclusions without uncertainty quantification**: Section 4 draws conclusions such as "Both models performed slightly worse on the Caucasian subgroup" and "female participants consistently achieved slightly higher verification rates" based on 12–13 subjects per racial group and 25 per gender. These differences (often 2–5 percentage points) are within a range where individual variation across such small groups could dominate. The paper should present these as preliminary observations requiring confirmation at larger scale, rather than findings.

### Trivial
- The exclusion of Scenarios 17–18 from benchmarks is justified (reduced facial visibility), but the justification is brief. These are the most application-distinctive eKYC scenarios; noting their exclusion more explicitly and pointing to them as open challenges would strengthen the paper.

## Nice-to-Haves
- Implement proper verification protocol: define explicit genuine pairs (same subject, different sessions) and impostor pairs (different subjects), compute EER and TAR@FAR=0.1%/1%, and run the demographic breakdown at those operating points. This is the single highest-leverage improvement and requires no new data collection.
- Include Scenarios 17 and 18 in the face detection evaluation even if verification is difficult. Showing that existing detectors degrade under hand-occlusion conditions directly supports the eKYC research motivation.
- Report per-subject variance in addition to group-level aggregates for demographic analysis, especially given the small group sizes.
- Add a brief explicit statement in the benchmark section (not just the conclusion) that the dataset is bona fide only and lacks presentation attack samples, since the application domain (eKYC, PAD) makes this an important scoping note.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic, Section 3.3 confound (probe-reference camera asymmetry)**: The critic notes that the verification reference (flash, Scenario 3, Session B, rear camera) differs from queries not just in pose but in camera module. While technically accurate, this is a reasonable and commonly used experimental setup in eKYC contexts (verifying against an official document photo taken with a rear camera). This is not a methodological flaw.
- **Harsh Critic, SOTERIA comparison in intro**: The critic suggested the distinction from SOTERIA (which lacks eKYC videos) should be "sharper" in the introduction. This is a presentation preference, not a substantive weakness; the comparison is already present in Table 1 and discussed in Section 2.
- **Strength Finder, "addressing an important problem"**: Generic strength removed per discipline; not included in the final strengths.
- **Harsh Critic, "paper does not address what SOTERIA distinguishing claim is"**: Fully addressed in Table 1 and Section 2 — eKYC scenario coverage is the explicit differentiator.

## Novel Insights
The paper's most genuinely novel insight is infrastructural rather than algorithmic: eKYC verification systems require challenge-response facial video data, but all existing biometric datasets are either photos, generic face videos, or presentation-attack focused. VIBEFACE reveals that standard face recognition models (ArcFace, MagFace) degrade substantially on off-angle and head-rotation sequences even at high cosine-similarity thresholds, while performing near-perfectly on frontal views — suggesting that the transition from static-photo to eKYC-video verification opens a significant, unmeasured performance gap that warrants targeted research. The demographic detection bias finding (MTCNN: 0.812 African vs. 0.984 East Asian on FV) is a concrete, reproducible illustration of how even a controlled benchmark reveals race-contingent disparities in widely deployed biometric tooling.

## Suggestions
1. Replace the fixed-threshold frame authentication rate with a proper genuine/impostor pair protocol reporting EER and TAR@FAR. The session structure already supports this: same-subject cross-session pairs are genuine; different-subject pairs are impostors. This is the most consequential revision.
2. Recalibrate the "unconstrained/at-home" framing in the abstract and introduction to accurately reflect studio-controlled acquisition with device and lighting variation — this improves credibility without weakening the contribution.
3. Frame demographic findings as preliminary observations with a note about small-group statistical power rather than established findings.
4. Include Scenario 17/18 at minimum in the face detection evaluation to measure occlusion impact.

## Score and Decision

**Anchors and comparisons:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| tC1b9DBWww.md | 2.50 | R1 | Weaker: bias analysis without novel contribution |
| 4G6Q4nJBTQ.md | 3.00 | R1 | Weaker: narrow scope, limited empirical rigor |
| NWvsm2VxAM.md | 3.00 | R1 | Weaker: synthetic dataset, identity inconsistency problem |
| lAhQCHuANV.md | 6.33 | R1/R2 | Stronger: theoretical guarantees + empirical fairness in FR, methodologically rigorous |
| x1Bk51SCL9.md | 5.75 | R1 | Stronger: 900+1800 benchmark problems, 25 MLLMs evaluated |
| CCo8ElCT7v.md | 4.25 | R1/R2 | Comparable: empirical face recognition paper, limited novelty |
| Dolm7rrrQd.md | 4.25 | R2 | Comparable: fairness analysis paper in face domain |
| Lv9KZ5qCSG.md | 5.50 | R2 | Slightly stronger: 30,000 subjects + FIS method |
| XhyCPEnlCa.md | 4.25 | R2 | Comparable: dataset paper (deepfake), similar modest scale issues |
| WjxgruI6A2.md | 3.67 | R2 | Weaker: narrow application scope |
| dEGYODD6iU.md | 3.67 | R2 | Slightly weaker: skin tone PAD analysis, no new dataset |

**Round 1 bracket**: 4.0–6.0  
**Round 2 narrowing**: Round-2 anchors cluster at 4.25 (CCo8ElCT7v, Dolm7rrrQd, XhyCPEnlCa) and 5.50 (EyeFairness). VIBEFACE fills a more unique niche than the 4.25-cluster papers (eKYC is a genuine gap; the contribution is not contested). However, VIBEFACE is weaker than EyeFairness at 5.50 because: (a) it is much smaller in scale (50 vs. 30,000 subjects), (b) it proposes no algorithmic contribution (EyeFairness had FIS), and (c) its verification benchmark methodology is notably weaker than standard practice. VIBEFACE is comparable to or slightly above the 4.25-cluster papers: it has stronger novelty than the ViT-vs-CNN comparison paper and the racial-bias compression paper, but those papers also had methodological weaknesses that drove them down. The Major weakness (non-standard verification protocol) is real and reduces the paper's demonstrated utility, though it does not invalidate the dataset itself.

**Final score: 4.0** — sits at the top of the 4.25-anchor cluster but below 5.5, reflecting genuine novelty in dataset design offset by limited scale, weak verification benchmarking, and no algorithmic contribution.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>