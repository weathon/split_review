## Summary

EmoSign introduces a dataset of 200 ASL video clips annotated with sentiment ratings, emotion intensity scores for 10 categories, and open-ended descriptions of emotion cues — all annotated by 3 Deaf native ASL signers with professional interpretation experience. The paper also provides benchmark evaluations of four multimodal LLMs across sentiment analysis, emotion classification, and a qualitative emotion cue grounding analysis. The dataset addresses an underexplored gap in sign language research.

## Strengths

- **Deaf native signer annotation pipeline**: The paper recruits 3 Deaf ASL signers with professional interpretation experience (Section 3.2), a clear methodological improvement over the closest prior work FePh (Alaghband et al., 2020), which used hearing annotators. The paper cites evidence (Lim et al., 2024) that hearing individuals frequently misinterpret signers' facial expressions, making this distinction directly relevant to annotation quality.

- **Ablation study reveals video-only failure**: The three-condition benchmark (caption-only, video-only, video+caption) in Tables 3 and 4 shows that video-only performance across all models is near-chance (11–14% wAcc), while caption-only matches or exceeds video+caption. This provides quantitative evidence that current MLLMs fail to extract emotional information from visual sign language, supporting the paper's central claim.

- **Open-ended emotion cue descriptions**: Beyond categorical labels, the paper collects free-text descriptions of why annotators assigned each emotion (Section 3.2) and extracts thematic findings about non-manual markers (furrowed brows, pursed lips, head thrusts), sign modifications (size, speed, repetition), and the role of sentence context (Section 3.4). No prior ASL dataset provides this qualitative layer.

- **Documented model reasoning failures**: Section 5.3 provides specific, verifiable failure modes grounded in model outputs (Figure 3) — e.g., Qwen2.5 claiming "the exact content of the sign language cannot be determined without audio" (demonstrating misunderstanding of sign language as a visual language), AffectGPT defaulting to "neutral expression" on every video, and GPT-4o parroting "relaxed body language" regardless of content content.

## Weaknesses

### Major

- **Numerical error in reported inter-annotator agreement**: Table 2 reports the average Krippendorff's alpha as 0.593. Computing the mean of the 11 values shown (0.738, 0.699, 0.552, 0.381, 0.119, 0.555, 0.333, 0.351, 0.166, 0.330, 0.370) yields approximately **0.418**, not 0.593. This is a substantial discrepancy — a 42% overstatement. The paper then uses this 0.593 value to claim that annotation quality exceeds that of MELD and IEMOCAP. The error directly affects a comparative claim the paper makes about its own quality.

### Minor

- **Inappropriate comparison of agreement metrics**: The paper states: "To contextualize, existing widely-used emotion recognition datasets had lower inter-annotator agreement compared to ours: MELD (Fleiss' kappa = 0.43), IEMOCAP (Fleiss' kappa = 0.48)." Krippendorff's alpha (used for EmoSign) and Fleiss' kappa are different statistics with different computational bases and ranges. They are not directly comparable without careful methodological disclaimers. Combined with the numerical error above, this inflates the apparent annotation quality relative to established benchmarks.

- **VADER-based selection partially confounds benchmark interpretation**: The dataset curated the 100 most positive and 100 most negative utterances based on VADER text-sentiment analysis of captions (Section 3.1). This means clips where text sentiment and visual emotion diverge — the most informative cases for testing whether models genuinely integrate visual cues independently of text — are systematically excluded. The paper acknowledges this in passing (Section 6) but does not discuss how this shapes the headline conclusion that "models rely on text." (Note: the video-only near-chance result remains robust and is not affected by this issue.)

- **Limited dataset size for benchmark statistical power**: 200 clips (16 min) from 4 signers, drawn from a single lab-recorded corpus (ASLLRP). Per-class sample sizes in the single-expression emotion benchmark (140 clips across 11 classes) are very small, with some categories having single-digit evaluation counts after splitting. No confidence intervals or uncertainty quantification are reported for benchmark results. The paper cites precedent for similarly sized datasets, but the statistical implications for the reported metrics are not discussed.

### Trivial

- **Table 1 inconsistency**: Table 1 reports "3" signers for EmoSign in the "Signers" column, while the text (line 144) states the dataset "includes 4 different signers." The table appears to conflate video-subject signers with annotators. Other datasets in the table report video performers, so EmoSign's entry should be "4" for consistency.

## Nice-to-Haves

- A quantitative grounding metric (e.g., overlap between model-attended regions and annotator-identified cues) would strengthen the emotion cue grounding analysis beyond the current qualitative inspection of a few examples.
- Per-class F1 scores alongside the per-class accuracy in Table 4 would enable more standard comparison.
- Expanding the limitations section to directly discuss the small signer count and the sample size implications for benchmark generalizability would improve the paper.

## Removed Points

- **VADER circularity called "fatal/structural" by harsh critic**: The critic claimed this "undercuts the paper's main experimental claim." This is an overstatement. The video-only near-chance result (11-14% wAcc) is robust regardless of VADER selection — it demonstrates that models cannot extract emotion from visual ASL cues at all. The VADER selection primarily affects the comparison between caption-only and video+caption conditions. Demoted from fatal to minor.
- **Criticism about "first sign video dataset" claim**: Removed — the paper properly acknowledges FePh as prior work and specifies the novelty lies in fine-grained annotations and qualitative descriptions from Deaf signers.
- **Missing related works**: Removed per hard rules (no external verification possible).
- **Formatting/style nitpicks and grammar concerns**: Removed per hard rules (parser artifacts, not author errors).
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem"): Removed as superficial and applicable to almost any paper.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies the tension between the VADER-based curation and the benchmark claim about text reliance, though overstates its severity. The strength finder correctly identifies the Deaf native signer annotation pipeline and the qualitative cue descriptions as the most distinctive and durable contributions — these are stronger than the benchmark findings.

## Suggestions

1. **Fix the Krippendorff's alpha calculation** in Table 2 and the corresponding text. Report the correct average (~0.418) and discuss its implications honestly, including the low agreement for several negative-emotion categories.
2. **Recompute or remove the comparison** between EmoSign's Krippendorff's alpha and the Fleiss' kappa values for MELD/IEMOCAP. Either compute the same metric across all datasets, or acknowledge the methodological incomparability and refrain from claiming superiority.
3. **Reframe the VADER selection issue**: Acknowledge directly in the main text (not just the limitations section) that the dataset construction via text-sentiment filtering limits conclusions about text reliance. Consider adding a held-out set where VADER and annotators disagree.
4. **Add confidence intervals** for the main benchmark results given the small per-class sample sizes.
5. **Correct Table 1** to show "4" video signers (matching the text) or clarify the column definition.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Strong-reject band (<2.5): lMW9d1AqC9 (1.67, sign-language-to-SQL framework), 3ZdGSTxKuy (2.00, atypical video dataset), gNoqEdT2wO (2.33, multimodal continual learning). EmoSign is clearly above these.
- Weak band (2.5-4.5): 9DDJuab67K (3.80, multimodal emotion recognition), Wto5U7q6I2 (4.20, TemporalBench), Pa6SiS66p0 (4.33, multimodal continual learning). EmoSign is comparable to or slightly above the upper end.
- Middle band (4.5-6.1): 7kRFnSFN89 (5.00, sign language translation), f1uXrAjpOH (5.40, OV-MER emotion dataset, Reject), LqaEEs3UxU (5.75, Sign2GPT, Accept), eeaKRQIaYd (5.00, unsupervised SLT). EmoSign is comparable to the lower end of this band.
- Good band (6.0-7.5): nY9nITZQjc (6.50, MIntRec2.0, large multimodal intent dataset), Fb0q2uI4Ha (6.50, TAU-106K, traffic accident dataset). EmoSign is below these — they have much larger datasets and more rigorous evaluation.
- Strong band (7.5+): All at 8.00. EmoSign is far below these.

Initial bracket: **4.0 – 5.5**

**Round 2 (Narrowing):**
- flgrH5nK4H (4.00, one-shot ISLR, Reject) — Less novel methodologically than EmoSign's dataset contribution, but no comparable errors.
- f1uXrAjpOH (5.40, OV-MER emotion dataset, Reject) — Larger scale, novel paradigm, but rejected due to methodological concerns about LLM-based annotation circularity. EmoSign has cleaner annotation methodology but smaller scale and a verifiable numerical error.
- F6h0v1CTpC (6.00, EmpathyRobot, Reject) — Larger dataset (10K samples), mixed reviews (5, 3, 8, 8). EmoSign is below this in scale and rigor.

**Final calibration**: EmoSign sits below the OV-MER paper (5.40, Reject) and the EmpathyRobot paper (6.00, Reject) due to the verified numerical error in a key table, the inappropriate metric comparison, and the small dataset size. It sits above the 4.00 anchors because the dataset genuinely fills a gap that no prior work addresses. The core dataset contribution (Deaf signer annotations, qualitative cue descriptions) is salvageable, but the paper in its current form has concrete issues that undermine specific claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>