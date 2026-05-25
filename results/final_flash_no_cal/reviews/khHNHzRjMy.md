Now I have a comprehensive understanding of the paper. Let me synthesize the review.

---

## Summary

This paper presents EmoSign, a dataset of 200 ASL video clips annotated by three Deaf native signers with sentiment ratings (7-point scale), ten emotion categories (intensity 0–3), and open-ended descriptions of emotion cues. The dataset is the first to include fine-grained emotion and sentiment labels for continuous ASL signing. The paper also provides zero-shot benchmarks on four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) across three input conditions (caption-only, video-only, video+caption), finding that models heavily rely on text captions and struggle to recognize emotions from visual signals alone.

## Strengths

1. **First dedicated emotion-annotated ASL dataset with Deaf native signer annotations.**  
   Table 1 confirms that among seven major ASL datasets, EmoSign is the only one containing emotion labels, sentiment labels, and open-ended emotion cue descriptions. The annotations were performed by three Deaf ASL signers with professional interpretation experience (Section 3.2), which is a critical design choice given that hearing individuals frequently misinterpret signers' facial expressions (Section 2, citing Lim et al., 2024).

2. **Unique open-ended descriptions of emotion cues from native signers.**  
   Beyond discrete labels, annotators provided free-text explanations of specific visual indicators — mouth shapes, head movements, signing speed, sign size — that led to each emotion judgment (Section 3.2). Section 3.4 synthesizes these into reusable themes (non-manual markers, modified signing parameters, role of context), offering qualitative insights no prior sign-language dataset provides.

3. **Well-designed annotation pipeline.**  
   The annotation process includes training sessions, pilot tests with Deaf individuals, confidence ratings, skip options for problematic clips, and majority-vote post-processing with confidence-based tie-breaking (Sections 3.2–3.3). This is methodologically stronger than many emotion annotation efforts and shows respect for the annotators' expertise.

4. **Systematic ablation benchmark revealing consistent text reliance.**  
   The three-condition design (caption-only, video-only, video+caption) across four models consistently shows that video-only performance is poor, and video+caption roughly matches caption-only (Tables 3–4). This internal ablation is the strongest evidence in the paper and supports the core claim about text reliance more robustly than the absolute accuracy numbers do.

5. **Transparent reporting of inter-annotator agreement with category-level breakdowns.**  
   Table 2 provides Krippendorff's alpha for each of the 11 labels, allowing readers to see which emotions have high vs. low agreement. This candor is a strength and enables informed use of the data.

## Weaknesses

### Fatal
None.

### Major

1. **No baselines (majority-class, random, human ceiling) for benchmark interpretation.**  
   The paper reports absolute wAcc and wF1 scores without any comparator. This makes it nearly impossible to interpret whether a wF1 of 0.55 (GPT-4o, 7-class sentiment) is meaningful or close to chance. Given the small sample (140 clips for single-expression classification, 11 classes plus neutral), a majority-class baseline would likely be non-trivial. Without such anchors, absolute numbers create an illusion of precision that the sample does not support. Adding bootstrapped confidence intervals and simple baselines would dramatically strengthen the benchmark section without requiring new experiments.

2. **Low inter-annotator agreement for several emotion categories is not adequately addressed.**  
   Krippendorff's alpha for `surprise_neg` is 0.119, `disgust` 0.166, and `sadness` 0.333 (Table 2). These are well below the conventional 0.67 threshold for acceptable agreement. The paper compares its average alpha (0.593) to Fleiss' kappa on MELD (0.43) and IEMOCAP (0.48) for context, but this comparison is limited: Krippendorff's alpha and Fleiss' kappa are different coefficients with different scales, so the numbers are not directly comparable. More importantly, the paper never discusses what it means to have near-chance agreement on `surprise_neg` or `disgust` — these emotions appear in the evaluation benchmark, meaning some ground-truth labels may be unreliable. The paper should explicitly address how this affects conclusions about model performance on those categories.

3. **No confidence intervals or significance tests for benchmark metrics.**  
   With only 140 clips in the single-expression set and many classes having single-digit instances, the reported point estimates are likely unstable. Per-class accuracies in Table 4 (e.g., MiniGPT4's 0% for worry, fear, disgust in the video-only condition) are based on very few examples. The paper draws conclusions about model bias from these numbers without any indication of uncertainty. Bootstrapped 95% confidence intervals for the aggregate metrics (wAcc, wF1) would be straightforward and essential given the sample size.

### Minor

1. **VADER-based selection bias is acknowledged but its interaction with benchmark results is not explored.**  
   The dataset was built by selecting the 100 most positive and 100 most negative utterances by VADER on English captions (Section 3.1). The paper notes this as a limitation (Section 6) but does not discuss how it affects the benchmark interpretation — in particular, the video+caption condition may look better simply because the captions were pre-selected for strong text sentiment, which could inflate the apparent benefit of adding video to text. The paper's claim that "visual information can contribute meaningfully" should be tempered by this selection effect.

2. **The claim that "visual information can contribute meaningfully" is not uniformly supported.**  
   In Table 3, MiniGPT4 shows *worse* performance in the video+caption condition than in the video-only condition on both 3-class and 7-class sentiment (e.g., 3-class wF1 drops from 40.00 to 36.89). The paper acknowledges this indirectly with "nearly all models" but does not discuss this counterexample or what it implies about the robustness of the finding. If adding text hurts performance for one model, the conclusion that visual and textual information are being "meaningfully integrated" is less general than claimed.

3. **Grounding analysis is qualitative and anecdotal.**  
   Section 5.3 manually inspects "several randomly selected videos" and draws conclusions about model behavior (e.g., "models were attempting to construct explanations that were consistent with their judgment of the text sentiment"). While this is labeled as preliminary exploration, the paper uses it to support the headline claim that "current multimodal models fail to integrate visual cues into emotional reasoning." A few cherry-picked examples do not constitute evidence for a general failure mode, and the language should be consistently caveated.

4. **Limitations section omits several important caveats.**  
   Section 6 discusses the VADER filter and the lab-recording setting, but does not mention: (a) the small sample size relative to the claims made from the benchmarks, (b) the low inter-annotator agreement for certain emotions and its implications, (c) the lack of statistical evaluation in the benchmarks, or (d) the fact that the grounding analysis is exploratory. Adding these caveats would strengthen the paper's credibility.

5. **No signer-dependent analysis.**  
   The dataset contains clips from 4 signers (Section 3.4). The paper does not examine whether certain signers were easier to annotate or whether model performance varies by signer. While this is not a requirement for acceptance, it is a natural dimension of analysis that would increase the dataset's utility.

### Trivial
None.

## Nice-to-Haves

- **Add recommended train/validation/test splits** for the dataset, stratified by sentiment or signer, to enable reproducible fine-tuning comparisons in future work.
- **Include a simple feature-based baseline** (e.g., CLIP features + linear probe, or facial landmark features) to calibrate the difficulty of the task beyond what zero-shot LLMs reveal.
- **Structure the release of the emotion cue descriptions** with cue-type categories and frequencies (e.g., how often specific non-manual markers were cited per emotion), which would increase the impact of this unique annotation layer.
- **Provide confusion matrices between annotators** for the low-agreement emotion categories, to help users understand the annotation disagreements.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No demographic information about the annotators"** — The paper states "for more details about recruitment, see Appendix A.1." The parser has stripped the appendix; this information exists in the original submission.
- **"No class distribution for the single-expression subset"** — The paper states "Appendix A.5 shows the distributions of each subset." The parser has stripped the appendix; this distribution exists in the original submission.
- **"The paper does not evaluate a simple vision backbone fine-tuned on the dataset"** — This is scope creep for a dataset paper whose contribution is the resource and zero-shot baselines. The paper explicitly states its goals in the introduction and scope; requiring a trained method is not appropriate for evaluating this contribution.
- **"Missing entries in the 'Source' column of Table 1"** — This is a PDF parsing artifact; the original table is properly formatted.
- **Critic's claim that the comparison of Krippendorff's alpha to Fleiss' kappa is "not directly comparable"** — While technically different coefficients, both are chance-corrected agreement measures used for similar purposes, and providing this context is standard practice. The broader point — that EmoSign's agreement is within a comparable range to established spoken-language emotion datasets — remains valid. This criticism is removed as overly pedantic and not a genuine flaw.

## Novel Insights

None beyond the paper's own contributions. The key novel findings are the paper's own: (1) Deaf native signers use a rich set of non-manual markers and sign modifications that go beyond facial expressions to convey emotion, documented through open-ended descriptions; (2) current MLLMs show near-complete inability to recognize emotion from visual ASL cues alone, consistent across four model families; and (3) models exhibit a positive-emotion bias and default responses (e.g., "neutral") when confronted with ASL video without captions. These are the paper's contributions and are not reframed here.

## Suggestions

1. **Add baselines and confidence intervals to the benchmark tables.** Example: report majority-class baseline performance, random-guess performance, and bootstrapped 95% CIs for wAcc and wF1. This is the single most impactful improvement and does not require new data collection.
2. **Discuss the low-agreement emotions directly.** Acknowledge that `surprise_neg` (alpha=0.119) and `disgust` (alpha=0.166) have near-chance agreement; explain possible reasons (e.g., category ambiguity, small sample); and caution that model performance on these categories should be interpreted with care.
3. **Soften the causal language around the grounding analysis.** Frame it explicitly as "qualitative observations from a small sample of examples" rather than as evidence of systematic model failure. The quantitative ablation (Tables 3–4) already provides strong evidence for text reliance.
4. **Expand the limitations section** to include discussion of sample size, low-agreement categories, and the exploratory nature of the grounding analysis, so readers can calibrate their confidence in the benchmark findings.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>