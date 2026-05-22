Now I have a good picture. Let me write the final consolidated review.

**Round-1 bracket:** The paper sits above the weak band (1-3, clearly reject) but below the strong band (8+). The middle band anchors (5.0-6.4) are the relevant comparison. Initial bracket: **4.5–6.5**.

**Round-2 narrowing:** The most comparable anchor is CulturalBench (5.0, rejected) — both are benchmark datasets with careful human annotation but limited size. CulturalBench had 1,227 items across 45 regions and was criticized for insufficient per-region samples. EmoSign has 200 items total. OV-MER (5.4, rejected) is another emotion dataset with scale concerns. Sign2GPT (5.75, accepted) is a methods paper in a different contribution class. EmoSign is comparable to or weaker than these on the benchmark-quality dimension but stronger on the annotation-uniqueness dimension.

**Final score: 5.0** — the paper has a real contribution (first native-signer-annotated ASL emotion dataset with rich qualitative cues) but the dataset is too small to support the "benchmark" framing as written. The paper lands just below the acceptance threshold and would need major revisions to its framing or dataset scale to be acceptable.

---

## Summary

This paper introduces EmoSign, a dataset of 200 ASL video utterances (≈16 minutes, 4 signers) with sentiment labels (7-point scale), 10 emotion categories (4-point intensity), and open-ended emotion cue descriptions — all annotated by 3 Deaf native ASL signers with professional interpreting experience. The paper also reports baseline results for four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) across sentiment and emotion classification tasks with video-only, caption-only, and video+caption ablations, plus a qualitative analysis of model reasoning. The key finding — that models rely heavily on text captions and largely fail to extract emotion from sign video alone — is clearly demonstrated.

## Strengths

1. **First dedicated ASL emotion dataset with native-signer annotations.** EmoSign fills a genuine gap. Table 1 shows no existing ASL dataset provides emotion labels, and the annotation team (Deaf native signers) is uniquely qualified to distinguish grammatical from affective facial expressions. This is a first-of-its-kind resource.

2. **The qualitative emotion cue descriptions are a distinctive and valuable contribution.** The annotation protocol collected open-ended descriptions of *how* emotions manifest visually (Section 3.4). The analysis covers non-manual markers (furrowed brows, head thrusts, mouth shapes), signing modifications (speed, size, repetition), and role/context cues. This documentation provides grounded knowledge not available in any other dataset.

3. **Benchmark results convincingly show text reliance in current MLLMs.** Table 3 shows stark gaps: video-only GPT-4o achieves wF1 of 5.97 on 7-class sentiment, while video+caption reaches 26.35. AffectGPT output is essentially constant (wF1 = 0.04) on video-only. This directly supports the paper's central claim and aligns with known issues in multimodal LLMs.

4. **Careful annotation methodology.** The annotation pipeline is well-designed: training sessions, pilot tests, three independent annotators, confidence ratings, majority-vote with tie-breaking by confidence, and explicit ethical safeguards (option to skip videos). The effort to engage the Deaf community is commendable and scientifically essential for this task.

## Weaknesses

### Major

1. **Dataset size (200 utterances, 4 signers) fundamentally limits the benchmark contribution.** The paper is framed as establishing a "new benchmark for understanding model capabilities in multimodal emotion recognition for sign languages," but 200 utterances across 7–11 classes yields roughly 18–28 samples per class. This is too small for stable evaluation; metrics could shift substantially with a different train/test split or a few additional samples. The paper acknowledges the cost constraint ("start with 200") but this does not resolve the structural limitation for the *benchmark* portion of the contribution. The qualitative annotation work remains valuable at this scale, but the claim of establishing a reliable benchmark is overstated.

2. **VADER-based selection introduces selection bias that is not adequately addressed.** The dataset was constructed by taking the top 100 positive and 100 negative utterances by VADER text sentiment. This means (a) the dataset deliberately excludes the mid-range and most of the neutral zone where cross-modal divergence would be most interesting, and (b) the finding "models rely on captions" is partially confounded — if captions are all strongly valenced, using them is an easy shortcut. The paper's Limitations section notes that VADER results differed from annotator judgments but does not systematically analyze this discrepancy. The dataset's construction makes it harder to study the phenomenon the paper itself highlights (visual vs. textual emotion divergence).

### Minor

3. **Comparison of inter-annotator agreement to MELD/IEMOCAP is misleading.** The paper reports Krippendorff's alpha (0.593) and compares it to Fleiss' kappa for MELD (0.43) and IEMOCAP (0.48). These are different metrics with different ranges and interpretations, making the "higher agreement" claim unsupported. The raw agreement values are reasonable for emotion annotation, but the comparison should either use the same metric or acknowledge the incomparability.

4. **Several emotion categories have near-chance inter-annotator agreement.** Krippendorff's alpha for surprise_neg (0.119), disgust (0.166), and frustration (0.330) indicate very weak agreement. These categories are retained in the benchmark with majority-vote labels from only 3 annotators. The paper does not analyze whether model errors on these categories are partially driven by label noise. This does not invalidate the dataset but should be reflected in the benchmark conclusions.

5. **The emotion cue grounding task is not quantitatively evaluated.** Despite being presented as a third benchmark task alongside sentiment and emotion classification, it receives only qualitative analysis (manual inspection of a few samples). No metric, human baseline, or systematic evaluation is provided. This should either be operationalized with a quantitative evaluation or renamed to "qualitative reasoning analysis."

6. **No confidence intervals or significance testing on benchmark results.** With only 200 samples, the reported wF1 and accuracy values likely have wide variability. Bootstrap confidence intervals would substantially strengthen the reliability claims.

### Trivial

- Table 3 metrics for MiniGPT4 caption-only (wAcc 1.92, wF1 5.92 on 3-class) appear to indicate near-floor performance, but the paper does not comment on this outlier.
- Confidence scores (0–100) are collected from annotators but only used for tie-breaking; no analysis of whether confidence correlates with agreement or label reliability.

## Nice-to-Haves

- Analyze the VADER vs. annotator sentiment discrepancy systematically (e.g., scatter plot, confusion analysis). This could identify a "hard subset" where text and visual emotion diverge, which would be the most useful test cases for model evaluation.
- Report per-signer performance breakdown to diagnose whether model failures are signer-specific or general.
- Expand the emotion cue description analysis with category-level quantification (e.g., how often each cue type is mentioned per emotion).

## Removed Points

- *"Weakness about the existence/release status of models or datasets"* — The reviewer questioned whether cited papers' datasets are comparable; this is removed per hard rules.
- *"Fatal claim that dataset size makes the contribution unsalvageable"* — This is too strong. The qualitative contributions are valuable at this size. The dataset *can* serve its purpose as a diagnostic tool and starting point; it is the "benchmark" framing that overreaches, not the dataset itself. Downgraded from fatal to major.
- *Strength: "Inter-annotator agreement is higher than widely used spoken-language emotion datasets"* — Removed because the comparison uses different metrics (Krippendorff's alpha vs. Fleiss' kappa), making the claim misleading. The paper's agreement is still reasonable, but the comparison as stated is not valid.

## Novel Insights

The most interesting observation that emerges from the reviews is a mismatch between the paper's framing and its strongest contribution. The reviews converge on the view that the qualitative annotation layer (emotion cue descriptions from Deaf native signers) is the paper's most novel and durable asset, while the quantitative benchmark contribution is undercut by small sample size. This suggests the paper would be better served by restructuring its narrative around the annotation resource and cue analysis, treating the benchmark results as a secondary diagnostic exercise rather than the headline contribution. No further novel insight emerges beyond the paper's own findings.

## Suggestions

1. **Reframe the contribution.** Either expand the dataset substantially (3–5×) to support the benchmark framing, or reposition the paper as primarily an annotation resource with detailed cue analysis, demoting the benchmark to a supporting role. The second path is more realistic and would still be a strong contribution given the uniqueness of the annotations.

2. **Provide confidence intervals** for all benchmark metrics, given the small sample size.

3. **Analyze the VADER–annotator sentiment discrepancy systematically.** This would strengthen the paper's own motivation and identify the most informative examples for future work.

4. **Address the Krippendorff's alpha vs. Fleiss' kappa comparison** by either computing the same metric for the comparison datasets or clearly acknowledging the incomparability.

5. **Either operationalize the emotion cue grounding task** with a quantitative metric (frame-level localization, human baseline) or remove it from the task list.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>