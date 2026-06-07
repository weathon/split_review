Now I have enough calibration data to finalize my score. Let me write the final review.

## Summary
EmoSign introduces a dataset of 200 ASL video clips annotated for sentiment (7-point scale), 10 emotion categories (0–3 intensity), and open-ended descriptions of emotion cues by 3 Deaf native ASL signers with professional interpretation experience. The paper also presents zero-shot benchmarks of 4 multimodal LLMs under caption-only, video-only, and video+caption conditions, finding that current MLLMs struggle to extract emotion from video alone and rely heavily on text captions.

## Strengths
- **Annotation by Deaf native ASL signers** — The paper explicitly contrasts with FePh (lines 82–83), which used hearing annotators, noting that "hearing individuals frequently misinterpret signers' facial expressions." EmoSign's annotators are Deaf native signers with professional interpretation experience who can distinguish grammatical from emotional facial expressions. This is a genuine methodological improvement over prior work and directly supports the paper's core claim about understanding emotions in ASL.

- **First ASL dataset with qualitative emotion cue descriptions** — As stated in line 83, EmoSign is "the first sign language dataset to include qualitative descriptions of how emotions manifest in signing, from the perspective of native signers." These descriptions document specific non-manual markers (furrowed brows, pursed lips, head thrusts), sign modifications (speed, size, repetition), and contextual disambiguation cues (lines 193–194), going beyond binary presence/absence labels.

- **Systematic three-condition ablation design** — The paper tests all four MLLMs on caption-only, video-only, and video+caption conditions for both sentiment and emotion tasks (Section 4.2, line 215; Tables 3–4). This design reveals diagnostic patterns (e.g., AffectGPT outputs "Neutral" for essentially all video-only inputs with wF1 of 0.04; GPT-4o exhibits a positive bias) that a single-condition evaluation would miss.

## Weaknesses

### Fatal
None.

### Major
1. **Invalid inter-annotator reliability comparison** — Table 2 reports Krippendorff's alpha for EmoSign (sentiment = 0.738, average across emotions = 0.593) and compares these to MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48). Krippendorff's alpha and Fleiss' kappa are different chance-corrected agreement coefficients with different mathematical formulations. Directly comparing their raw values as if on the same scale is not methodologically valid. Several individual emotion categories have very low alpha values (surprise_neg = 0.119, disgust = 0.166, frustration = 0.330), indicating near-random agreement. The paper's claim that "existing widely-used emotion recognition datasets had lower inter-annotator agreement compared to ours" (line 140) is not supported by this comparison. To be clear: the annotations themselves may well be high-quality — the issue is with how this is argued in the paper.

2. **VADER-based selection limits benchmark interpretation** — The dataset selects the 100 most positive and 100 most negative utterances by text-caption VADER score (line 115). This enriches for videos where text sentiment is strong and unambiguous. The paper's main benchmark finding is that models rely heavily on text captions and struggle with video alone — but the dataset construction maximizes text-sentiment signal. This design makes it difficult to distinguish "models cannot extract emotion from ASL video" from "the dataset's selection procedure has created a benchmark where text is an unusually informative shortcut and the mapping from video to emotion may be artificially hard because the filter selected clips where visual and textual sentiment diverge." The paper mentions this briefly (line 330: "VADER results differed from the annotators' results often contained rich non-manual markers that conveyed emotions differently than the text") but does not grapple with how the selection protocol affects the interpretation of every benchmark result. The ablation study design is good, but the selection bias weakens the core claim about modality reliance.

### Minor
1. **Small dataset without uncertainty estimates** — 200 utterances, 4 signers, 16 minutes. Several emotion categories have only 25–30 clips (surprise_neg, anger, fear, disgust). Per-class accuracies in Table 4 are based on very small denominators, yet no confidence intervals, error bars, or variance estimates are reported anywhere. For a 200-sample zero-shot evaluation set, aggregate metrics like wF1 have wide confidence intervals (roughly ±5–10 points at 95% confidence). Fine-grained claims about model behavior patterns (e.g., "GPT-4o almost always classified videos as displaying either happiness or frustration," line 253) would benefit from some indication of statistical stability.

2. **Emotion cue grounding analysis is not a benchmark task** — Section 5.3 describes a manual inspection of "several randomly selected videos" with qualitative observations. The paper frames this as the third of "three benchmark tasks" (Section 4.1, line 199), but there is no systematic coding scheme, quantitative metric, or clear sampling methodology. The findings are anecdotal. The paper would be stronger if this section were explicitly reframed as a qualitative error analysis rather than a benchmark task.

3. **No per-signer breakdown** — The dataset contains 4 signers (line 144), but the paper provides no information about how label distributions or model accuracy vary across signers. Signer identity could confound results if certain signers are over-represented in positive vs. negative clips or if model performance varies systematically by signer. This is important for a 200-utterance dataset with only 4 signers.

4. **No systematic analysis of open-ended cue descriptions** — The qualitative themes (non-manual markers, sign modification, context dependence, lines 193–194) are interesting but derived from informal inspection with no systematic content analysis. A simple frequency analysis of cue types would substantially strengthen this section.

### Trivial
None.

## Nice-to-Haves
- Including a small set of neutral-text but emotionally signed videos as contrastive examples would substantially strengthen the benchmark's ability to test video-only emotion recognition.
- Fine-tuned baselines on sign-language-specific models (e.g., LLaVA-SLT) would complement the zero-shot results and better serve the paper's goal of "establishing baseline model performance."

## Removed Points
These points were flagged by reviewers but are removed or demoted for the following reasons:

- **VADER "circularity" as a fatal flaw (Harsh Critic)** — Removed as a fatal classification. The dataset's primary contribution is as an annotation resource, not the benchmark finding. The VADER selection limits benchmark interpretation (kept as Major) but does not invalidate the core dataset contribution or make the paper unsalvageable.
- **No train/test split (Harsh Critic)** — Removed. Zero-shot evaluation on the full set is standard practice; no train/test split is needed.
- **Inter-annotator comparison as a strength (Strength Finder)** — Removed because it conflicts with the verified weakness that different metrics are being compared.
- **Generic strengths from Strength Finder** (e.g., "addresses an important problem," "provides a meaningful quality benchmark") — Removed as superficial or conflicting with verified weaknesses.
- **Missing related works** — Removed per policy (cannot verify external works).
- **Mismatch between motivation and data (Harsh Critic)** — The abstract's mention of "distinguishing syntactic versus affective functions" is aspirational about future work, not a delivered capability. Not a genuine weakness for a dataset paper.

## Novel Insights
None beyond the paper's own contributions. The reviewers' main observations align with well-understood trade-offs in dataset construction: filtering for emotional salience via text creates a benchmark where text has disproportionate influence, and the resulting findings about modality reliance must be interpreted cautiously. This is a standard concern for multimodal datasets, not a novel insight specific to this paper.

## Suggestions
- Replace the Krippendorff's alpha vs. Fleiss' kappa comparison with a proper same-metric comparison, or remove the direct comparison and instead contextualize EmoSign's alpha values against established interpretation guidelines (e.g., conventional thresholds for "moderate" / "substantial" agreement).
- Add bootstrapped confidence intervals to all benchmark metrics.
- Provide per-signer label distributions and model accuracy breakdowns.
- Reframe Section 5.3 as a qualitative error analysis, not a "benchmark task."
- Add a simple frequency analysis of the open-ended cue descriptions.

---

### Calibration Anchors

**Round 1 (Bracketing):** Queried for high-scoring (>7.5), mid-scoring (3.5–7.5), and low-scoring (<3.5) papers. High-scoring papers were 8.0 on unrelated topics (data scaling laws, VLMs); low-scoring papers were 1.67–3.0 with fatal flaws. The plausible bracket was [4, 7].

**Round 2 (Narrowing):** Queried within [4, 7] for emotion recognition dataset papers and sign-language dataset papers.

| Anchor | Avg Score | Round | Comparison to EmoSign |
|--------|-----------|-------|----------------------|
| Open-vocabulary MER (f1uXrAjpOH) | 5.40 | 1,2 | Slightly better scale (1,615 samples), similar methodological concerns (LLM dependency). EmoSign has stronger annotation methodology but smaller scale. |
| MIntRec2.0 (nY9nITZQjc) | 6.50 | 1,2 | Much larger scale (15K samples), more rigorous evaluation. EmoSign is clearly weaker. |
| ViML (Tgsc0KEkN6) | 4.50 | 1 | Large scale (3M clips) but pipeline concerns. EmoSign has stronger methodological novelty. EmoSign is slightly better. |
| SignAvatars (L2kbdthX5M) | 6.25 | 3 | Much larger scale (70K videos), rejected for being derivative data. EmoSign has genuinely new data but much smaller scale. |
| Hybrid Model for SLT (7kRFnSFN89) | 5.00 | 3 | Method paper, not a dataset paper. Comparable score level. |
| Uni-Sign (0Xt7uT04cQ) | 6.40 | 3 | Large-scale SLU pre-training. Much more comprehensive but different contribution type. |
| Babel-ImageNet (uLOFyiruin) | 6.50 | 2 | Clean benchmark extension, rejected for simplicity. Different domain. |

EmoSign is strongest compared to Open-vocabulary MER (5.40) and ViML (4.50), and clearly weaker than MIntRec2.0 (6.50) and SignAvatars (6.25). The paper has a genuine dataset contribution with a well-motivated annotation methodology, but the two Major weaknesses (metric comparison, VADER selection affecting benchmark interpretation) and the small scale without uncertainty estimates place it below the stronger anchors. The final score of 5.0 reflects a paper with real but limited contributions that needs substantive revision before it would be competitive at a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>