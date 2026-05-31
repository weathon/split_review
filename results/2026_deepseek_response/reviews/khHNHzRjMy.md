Now let me finalize my review with the calibrated score.

## Summary

This paper introduces EmoSign, a dataset of 200 ASL video clips (≈16 minutes) annotated by three Deaf native signers with sentiment ratings (7-point Likert), 10-category emotion intensity labels, and open-ended qualitative descriptions of emotion cues. The authors benchmark four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4-Video) on sentiment analysis and emotion classification under three modality conditions (caption-only, video-only, video+caption), finding that models perform poorly on video-only input and rely heavily on text captions.

## Strengths

- **First dataset with open-ended emotion cue descriptions from Deaf native signers.** Prior work (FePh) used hearing annotators and binary labels only. EmoSign collects rich qualitative descriptions (e.g., "mouth morpheme for 'oooh' conveys a sense of foreboding", "emphasized 'upset' with head shake and head tilt") that go far beyond existing ASL resources. This is documented in Section 3.2 and Figure 3, and the comparison with FePh in Section 2 is explicit.

- **Well-designed three-condition ablation reveals clear modality reliance patterns.** The caption-only / video-only / video+caption setup (Tables 3, 4) cleanly demonstrates that models default to text: AffectGPT outputs 0.04 wF1 on 7-class sentiment in video-only mode, and GPT-4o consistently defaults to "happiness" or "frustration" without text context. The design cleanly isolates the contribution of each modality.

- **Transparent reporting of negative results and specific failure modes.** The paper documents GPT-4o's "relaxed body language" repetition bias, Qwen2.5's "cannot be determined without audio" error (showing misunderstanding of sign language as a concept), MiniGPT4's caption-only performance collapse, and AffectGPT's neutral bias. Section 5.3 provides concrete examples rather than only aggregate metrics.

- **Careful annotation methodology.** Recruiting Deaf native signers with professional interpretation experience is well-motivated (Section 2 explains why hearing annotators are problematic), training sessions were conducted, the interface was pilot-tested, and annotation criteria are clearly documented.

## Weaknesses

### Fatal
None.

### Major

1. **Dataset size and narrow sourcing fundamentally limit the contribution's significance for a dataset paper.** 200 utterances (≈16 minutes) from 4 signers drawn from a single corpus (ASLLRP — news/educational content) cannot plausibly represent the diversity of emotional expression across signers, registers, and interactional contexts. The paper cites similar-sized datasets (CableInspect-AD, etc.) as precedent, but those involve tightly controlled stimuli where the concept generalizes beyond the sample size. Here, "emotional expression in ASL" is a vast, culturally nuanced phenomenon. The paper acknowledges this as a limitation but does not characterize this as a curated, diverse small sample — it is explicitly a convenience sample of the most emotionally salient clips VADER could find in one corpus. This limits the generalizability of both the dataset resource itself and the benchmark conclusions drawn from it.

2. **Low inter-annotator agreement on most emotion categories undermines label reliability for fine-grained classification.** Krippendorff's alpha values for surprise_negative (0.119), disgust (0.166), surprise_positive (0.381), frustration (0.330), sadness (0.333), and anger (0.370) are very low (Table 2). With only 3 annotators, majority-vote ground truth for categories with alpha ≈ 0.1–0.2 may be effectively arbitrary. The comparison with MELD (Fleiss' κ=0.43) and IEMOCAP (Fleiss' κ=0.48) uses different metrics and is not directly informative. Only sentiment (0.738), joy (0.699), and excited (0.552) have acceptable reliability. This means many of the fine-grained emotion classification benchmark results (Table 4) rest on unreliable ground truth labels, and the paper does not sufficiently flag this issue or restrict claims accordingly.

### Minor

1. **VADER-based selection creates a tension with the paper's central narrative, and the paper does not quantify the divergence.** The curation explicitly selects clips where the text caption is emotionally salient (top 100 VADER positive/negative), yet the paper's core argument is that models fail to recognize *visual* emotion in ASL. The paper acknowledges this in Section 6 but provides no analysis of how often text sentiment (VADER) and visual sentiment (annotator) diverge. If they largely agree, the video-only benchmark may be easier than claimed; if they diverge, that would strengthen the narrative — but the paper does not establish either case. This gap weakens the evidential foundation for the paper's central claim about text vs. visual emotion understanding.

2. **No confidence intervals or statistical tests on benchmark results.** With 200 samples and small per-class counts (some emotion categories have 25–30 samples), the reported accuracy and F1 values may have wide variance. Claims about modality comparisons would be strengthened by bootstrap CIs, particularly since some per-class cell counts in Table 4 are very small.

3. **The emotion cue grounding analysis is purely qualitative with very few examples.** Section 5.3 inspects "several randomly selected videos" and draws broad conclusions (e.g., "models attempt to construct explanations consistent with text sentiment") from a small, manually inspected set. No quantitative grounding metric is provided. While this is acceptable as a preliminary analysis, the paper draws stronger conclusions than the evidence supports.

### Trivial

1. Averaging Krippendorff's alpha across 11 categories (Table 2) is non-standard and can be misleading. Reporting the range and flagging the problematic categories explicitly would be more informative.

## Nice-to-Haves

- Quantify text–visual emotion divergence by comparing VADER polarity with annotator sentiment scores to substantiate the paper's central narrative.
- Provide an annotator disagreement analysis (systematic vs. idiosyncratic patterns) to help dataset users decide whether to trust majority-vote labels.
- Report bootstrap confidence intervals for main benchmark metrics, especially per-class results.
- Expand the dataset across additional corpora and signers in future work.

## Removed Points

- **"Dataset is not released"** — Removed per hard rule: criticisms about existence/release status of cited datasets/models are not allowed.
- **"Emotion category set is not well justified"** — Removed. The paper provides justification in Section 3.2 (Ekman's basic emotions + circumplex model, informed by prior work).
- **"VADER-based positive-negative imbalance not discussed"** — Removed. The paper explains this in Section 3.4 ("expected, since we selected clips with captions that had salient positive or negative emotions based on VADER").
- **"Missing appendix / proofs"** — Removed per hard rule (parser artifact).
- **"Pure formatting/style nitpicks"** — Removed per hard rule.
- **"No analysis of annotator disagreement patterns"** — Demoted from Major to Nice-to-Have. This would strengthen the paper but is reasonable future work given the small annotator pool.
- **"Criticism comparing FePh citation"** — Removed. The paper's claim about being "first sign language dataset to include qualitative descriptions" is accurate given the literature surveyed; the reviewer's doubt about plausibility is not a verified weakness.
- Some generic Strengths from Strength Finder removed: generic claims about "addressing important problem" without concrete specificity.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Restrict the strongest benchmark claims to sentiment and the happiness composite (joy+excited) where inter-annotator reliability is acceptable, and explicitly flag unreliable emotion categories in all result discussions.
2. Add a quantitative comparison of VADER text sentiment vs. annotator visual sentiment to clarify the extent of text-visual divergence and strengthen the paper's core narrative.
3. Report bootstrap confidence intervals for benchmark results, especially given small per-class sample sizes.
4. When referencing the dataset's size limitation, characterize whether the 200 clips were curated for diversity or are a pure convenience sample, so readers can calibrate their expectations.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| SignAvatars | L2kbdthX5M.md | 6.25 (Reject) | R1 | Large-scale SL dataset (70K videos) — much larger scale but criticized as derivative data; EmoSign is smaller but has novel original annotations |
| Uni-Sign | 0Xt7uT04cQ.md | 6.40 (Accept) | R1 | Large-scale pretraining + dataset (1,985h) — stronger technical contribution and much larger scale |
| USLNet | eeaKRQIaYd.md | 5.00 (Reject) | R1 | Unsupervised SL translation method — comparable score but different type of contribution |
| VRG-SLT | 7kRFnSFN89.md | 5.00 (Reject) | R1 | SL translation framework — comparable score, moderate reception |
| Sign2GPT | LqaEEs3UxU.md | 5.75 (Accept) | R2 | SLT framework with SOTA results — stronger technical novelty than EmoSign's dataset contribution |
| OV-MER | f1uXrAjpOH.md | 5.40 (Reject) | R2 | MER dataset paper — similar type of contribution (annotations + benchmarks), similar mixed reception (scores 3–8), comparable scale concerns |
| MMToM-QA | sMFqEror1b.md | 4.75 (Reject) | R2 | Multimodal ToM QA dataset with small sample — similar scale concerns |
| One-shot ISLR | flgrH5nK4H.md | 4.00 (Reject) | R2 | SL recognition method — lower score due to limited novelty |
| ILLUSION | qnlG3zPQUy.md | 6.00 (Accept) | R2 | Large-scale multimodal deepfake dataset (1.3M samples) — much larger scale but similar "dataset + benchmarks" structure |

**Round 1 Bracket:** The paper sits between the weak band (scores 1.67–3.33) and the strong band (scores 8.00), in the middle band (3.5–7.5). The most comparable papers are OV-MER (5.40, Reject) as a fellow emotion dataset paper, and Sign2GPT (5.75, Accept) as a sign-language paper.

**Round 2 Narrowing:** The paper is weaker than Sign2GPT (5.75, Accept) because that paper achieved SOTA results on established benchmarks with a technically substantial method. The paper is comparable to OV-MER (5.40, Reject) — both are emotion dataset papers with novel annotation methodologies and mixed reception. EmoSign has the advantage of real Deaf signer annotations (vs. OV-MER's cartoonish style), but both suffer from scale concerns and label reliability questions. The paper is somewhat stronger than the one-shot ISLR paper (4.00, Reject) which had limited technical novelty. Given the small dataset size (200 utterances), low label reliability for most emotion categories, and the VADER selection misalignment, the contribution is best characterized as a well-executed proof-of-concept. The qualitative descriptions are genuinely novel and the benchmark design is clean, but the structural limitations prevent this from being a strong accept at a top venue.

**Final Score: 5.0** — This reflects a paper with genuine, novel contributions (first Deaf-signer emotion cue descriptions, careful benchmark design, transparent reporting) that is ultimately limited by its scale (200 utterances, 4 signers, 1 corpus), label reliability issues on most emotion categories, and a VADER-based selection strategy that somewhat undermines the central narrative. The paper is a solid proof-of-concept that could become a more significant resource with expansion, but in its current form the evidence does not support the stronger generalizations the paper makes about model capabilities and ASL emotion expression.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>