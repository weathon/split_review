Now I have sufficient calibration data. Let me produce the final review.

## Summary

EmoSign introduces a 200-clip ASL video dataset annotated by 3 Deaf native signers with 7-point sentiment scores, 10-category emotion intensity ratings (0–3), and open-ended cue descriptions. It provides baseline evaluations of 4 multimodal LLMs across caption-only, video-only, and video+caption conditions, finding that models perform poorly on visual-only emotion recognition and rely heavily on text captions.

## Strengths

1. **First ASL video dataset with fine-grained emotion and sentiment labels from Deaf native signers.** Table 1 confirms no prior ASL dataset offers this combination. The annotation protocol (Section 3.2) — recruiting Deaf signers with professional interpretation experience who can distinguish grammatical from emotional facial expressions, providing training sessions, pilot testing, and allowing annotators to skip videos — is methodologically sound and represents genuine community engagement.

2. **Three-condition ablation (Tables 3, 4) demonstrates that current MLLMs fail at visual-only emotion recognition for ASL.** GPT-4o achieves only 5.97 wF1 (7-class sentiment) in video-only vs. 26.35 with video+caption; video-only emotion classification accuracy is uniformly below 15% wAcc across all models. This concretely supports the claim that models struggle to extract emotional information from signing video.

3. **Qualitative documentation of emotion cues from native signers (Section 3.4).** The synthesis of non-manual markers (furrowed brows, head thrusts, mouth shapes), sign modifications (speed, size, repetition, finger-spelling for emphasis), and the role of discourse context provides a genuine linguistic contribution that goes beyond what any prior sign language dataset offers.

## Weaknesses

### Fatal
None.

### Major

1. **Krippendorff's alpha numerical error.** Table 2 reports an average α = 0.593, but summing the 11 displayed individual values (0.738, 0.699, 0.552, 0.381, 0.119, 0.555, 0.333, 0.351, 0.166, 0.330, 0.370) gives 4.594, which divided by 11 equals **0.418**, not 0.593. The discrepancy is large (42% relative error) and cannot be explained by rounding. This directly affects the paper's claim that "existing widely-used emotion recognition datasets had lower inter-annotator agreement compared to ours." The authors must clarify whether the table values, the reported average, or the computation method is incorrect.

2. **VADER-based selection confound weakens modality-ablation conclusions.** The dataset was constructed by selecting the 100 most positive and 100 most negative utterances based on VADER scores applied to English captions (line 115). This procedure maximizes text-sentiment signal by construction. The paper's central finding — that models rely heavily on text and fail to integrate visual cues — is partly an artifact of selecting clips where text carries strong emotional signal. While the video-only results are genuinely poor regardless of selection, the claim that models "fail to integrate visual cues" is over-interpreted given that the dataset inflates the informativeness of the text channel. The limitations section (line 330) acknowledges this only briefly and unclearly.

3. **Incomparable inter-annotator agreement metrics.** The paper (line 140) compares its Krippendorff's alpha (reported as 0.593) against MELD's Fleiss' kappa (0.43) and IEMOCAP's Fleiss' kappa (0.48). Krippendorff's alpha and Fleiss' kappa are different statistics that are not directly comparable, even when measuring similar constructs. The framing "lower inter-annotator agreement compared to ours" is misleading irrespective of which average is correct.

4. **Low inter-annotator agreement on several negative emotion categories.** Even taking Table 2 at face value: surprise_neg (α=0.119), disgust (0.166), frustration (0.330), sadness (0.333), fear (0.351), anger (0.370). Krippendorff's α below ~0.3 is generally considered unreliable — the labels contain more disagreement than agreement beyond chance. Benchmarking model performance against these categories means the evaluation partly reflects annotator disagreement rather than model capability.

### Minor

1. **Small dataset size limits statistical power.** 200 clips (16 minutes) from 4 signers from a single corpus (ASLLRP) is acknowledged as a starting point (line 87) and the paper cites similar-sized datasets, but the benchmark comparisons (11-class emotion classification with per-class counts as low as ~25) lack statistical significance testing (no p-values, confidence intervals, or error bars). The reported precision of per-class accuracies to two decimal places is misleading without explicit per-class denominators.

2. **No human ceiling estimate.** Without a human performance baseline on the same task, it is unclear how well the task *can* be done. Leave-one-annotator-out evaluation or a non-signer baseline would contextualize the model results.

3. **Emotion cue grounding analysis (Section 5.3) is purely qualitative.** The analysis is framed as "preliminary" (line 284), which is appropriate, but the paper draws substantive conclusions (e.g., "models were attempting to construct explanations that were consistent with their judgment of the text sentiment") from manual inspection of a few examples without systematic coding or inter-rater reliability. This analysis should be explicitly labeled as illustrative.

4. **Multi-expression subset** (37 clips) is described (line 207) but no results are presented for it in the main paper.

5. **FePh "appears to have hired hearing annotators"** (line 83) is hedged speculation. This should be removed or verified with a citation.

### Trivial
- Line 330 has a grammatical issue ("...VADER results differed from the annotators' results often contained rich non-manual markers...").

## Nice-to-Haves
- Per-signer breakdown of results (only 4 signers used, so individual signer characteristics could drive results).
- Statistical significance tests or bootstrapped confidence intervals on key comparisons.
- Human performance baseline (e.g., leave-one-annotator-out).

## Removed Points

These points were raised but removed after verification against the paper:

1. **"The dataset is too small for any meaningful benchmark"** (Harsh Critic). The paper explicitly acknowledges this is a starting point (line 87) and cites analogous small-scale benchmarks. The contribution is primarily the annotation framework and qualitative findings, which are not invalidated by small size. Demoted from Fatal framing to Minor weakness.

2. **"Neutral-to-positive bias claim is ungrounded due to 5 neutral instances."** The bias claim in the paper (abstract, line 28) primarily concerns *positive* bias. The dataset has 70 positive clips (scores 1–3) supporting this. The neutral aspect of the claim is secondary and the paper does not rest its main case on it. Overstated by the critic.

3. **"VADER selection means the conclusion that models fail to integrate visual cues cannot be supported."** Overstated. The video-only results being uniformly poor (GPT-4o at 5.97 wF1) is independent of how the dataset was selected. The VADER selection primarily affects the *relative* comparison between text and video conditions, not the absolute finding that video-only performance is poor. This is real but not fatal — demoted to Major.

4. **"Per-class accuracy reported to two decimal places with tiny denominators."** Per-class counts can be inferred from Figure 2C. The paper is somewhat imprecise but not misleading.

5. **"No discussion of model variance / single run at fixed temperature."** This is standard practice for LLM API evaluations and API-based benchmarks; singling this out as a weakness would be applying standards not typical for this type of work.

6. **Strength Finder generic strengths** (e.g., "addressing a critical gap"). Removed as generic/superficial.

## Novel Insights

The most interesting observation from synthesizing the reviewer inputs is the tension between the paper's genuine contribution (the qualitative documentation of ASL emotion cues from native signers in Section 3.4) and the paper's self-presentation as a benchmark paper. The qualitative findings — that ASL emotion manifests through specific non-manual markers (pursed lips, head thrusts, furrowed brows), sign modifications (size, speed, repetition), and discourse context — are the most defensible and novel contribution. These findings are not undermined by the dataset's small size, the VADER selection procedure, or the inter-annotator agreement issues. If the paper were reframed to foreground this linguistic/anthropological contribution and present the benchmarks as preliminary, the numerical error and VADER confound would be less damaging. The benchmark framing exposes the paper to methodological scrutiny that the qualitative core largely survives but the quantitative periphery does not.

## Suggestions

1. **Correct the Krippendorff's alpha average** — either explain the discrepancy (if the average uses a different computation) or correct it. Use the corrected value in comparisons with prior datasets.

2. **Reframe the paper's contribution** to foreground the qualitative findings (Section 3.4) and annotation framework as the primary contribution, with the benchmark results presented as preliminary baselines with appropriate caveats about the VADER selection procedure and small sample size.

3. **Remove the incomparable Krippendorff's alpha vs. Fleiss' kappa comparison** or reframe it as a rough contextualization rather than a superiority claim.

4. **Add explicit per-class instance counts to Table 4** and include a note about the small denominators for certain emotion categories.

5. **Add a human performance estimate** (e.g., leave-one-annotator-out agreement as an upper bound on how well the task can be done).

6. **Soften the FePh "appears to have" claim** (line 83) to describe only what is verifiable from the cited work.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FHA-Kitchens (otoggKnn0A) | 4.00 | R1 (low band) | Kitchen hand-action dataset of 2,377 clips, rejected. EmoSign is smaller but addresses a more important gap (ASL emotion) with more rigorous annotation, and is slightly better. |
| TemporalBench (Wto5U7q6I2) | 4.20 | R1 (low band) | Temporal video benchmark (~2K QA pairs), rejected. EmoSign has a smaller dataset but a more unique community contribution. Comparable quality overall. |
| Open-vocab MER (f1uXrAjpOH) | 5.40 | R1 (middle), R2 | Emotion recognition dataset+benchmark, rejected (scores 3–8). EmoSign has more rigorous annotation (Deaf native signers) but is much smaller and has the numerical error. Weaker overall. |
| SignAvatars (L2kbdthX5M) | 6.25 | R1 (middle) | Large-scale 3D SL dataset (70K videos), rejected. Much larger scale and technical sophistication. EmoSign does not compare. |
| Uni-Sign (0Xt7uT04cQ) | 6.40 | R1 (middle) | Large-scale CSL dataset + SOTA methods, accepted. Not directly comparable — EmoSign is much smaller and less technically ambitious. |

**Round 1 bracket:** Based on the initial retrieval, the narrowest plausible range was [4.0, 5.5]. The low-band anchors (FHA-Kitchens 4.0, TemporalBench 4.2) place a floor; the mid-band anchors (Open-vocab MER 5.4, SignAvatars 6.25, Uni-Sign 6.4) set a ceiling.

**Round 2 narrowing:** Additional anchors confirmed the bracket. FHA-Kitchens (4.0) is weaker; Open-vocab MER (5.4) is stronger but still rejected. EmoSign sits between these: it has a more important application domain than FHA-Kitchens and more rigorous annotation than OV-MER, but the Krippendorff's alpha numerical error and VADER confound drag it down relative to OV-MER.

**Final score: 4.5.** The paper addresses a genuine gap with a sound annotation protocol and valuable qualitative findings. However, the Krippendorff's alpha numerical error (a verifiable discrepancy between the reported average and displayed values), the VADER selection confound, the incomparable inter-annotator agreement metrics, and the overall small scale substantially weaken the benchmark-driven claims. The paper's strongest contribution — the qualitative documentation of emotion cues — is real but is not the paper the authors have framed. Major revisions are needed before this work would meet the bar for acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>