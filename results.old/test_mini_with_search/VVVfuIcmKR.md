## Summary

This paper demonstrates that using CLIP's native intra-modal features (image-image, text-text) is inherently suboptimal for intra-modal tasks like image-to-image and text-to-text retrieval. It argues that CLIP's inter-modal contrastive training objective creates a modality gap and intra-modal misalignment. To support this claim, the paper adapts Optimization-based Textual Inversion (OTI) and introduces Optimization-based Visual Inversion (OVI) to convert intra-modal tasks into inter-modal ones. Across 15 datasets, 5 VLM backbones (OpenAI CLIP, OpenCLIP, SigLIP), and multiple tasks, the paper shows that inter-modal features via inversion consistently outperform native intra-modal features, while the same inverted features hurt performance on the inherently inter-modal task of zero-shot classification — cleanly pinning the benefit to crossing modalities rather than generic feature improvement.

## Strengths

- **Comprehensive evaluation with strong causal controls.** The paper evaluates across 15 datasets, 5 backbones, and 2 retrieval tasks. Beyond breadth, the experimental design includes three distinct causal analyses: (1) a negative control showing OTI-inverted features *degrade* zero-shot classification (Table 2 right), proving the benefit comes from crossing modalities, not from inversion producing better features; (2) SLIP experiments (Table 3) showing that adding an intra-modal loss during pre-training shrinks the gap between native and inverted performance; and (3) a modality-gap ablation (Table 4) where fine-tuning with high temperature closes the gap and eliminates the inversion advantage. This layered causal evidence is the paper's strongest feature.

- **Clean negative control (zero-shot classification).** Using the same OTI-inverted features that improve image-to-image retrieval to instead harm zero-shot classification (e.g., 76.2% → 60.6% for CLIP B/32 average) is an elegant experimental design that isolates the mechanism. It rules out the alternative explanation that OTI simply learns better features.

- **Honest framing and clear limitations.** The paper explicitly acknowledges that OTI/OVI are computationally expensive (150-1000 optimization steps per sample) and that the work is a diagnostic study rather than a practical recipe. This transparency strengthens the paper's credibility.

- **Introduction of OVI.** The text-to-image inversion (OVI) symmetrically complements OTI and extends the analysis to text-to-text retrieval, showing the phenomenon is bidirectional.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No variance or statistical significance reported.** Every table reports a single number per condition with no standard deviations, confidence intervals, or multiple seeds. While the consistency across 15 datasets and 5 backbones makes the main finding robust, the absence of any variance information makes it difficult to assess whether the modest improvements (typically 1-4 mAP points) are reliably above noise. This is a standard reporting expectation for empirical papers.

- **Dogs vs Cats filtering limits interpretability of that experiment.** The Section 2 illustration filters the dataset to ensure perfect inter-modal alignment before testing intra-modal performance. This makes the point cleaner (even with perfect inter-modal alignment, intra-modal retrieval is far from perfect) but also makes the exact numbers (81.4% mAP, 71.5% R-Precision) dataset-specific to the filtered set. Reporting the unfiltered numbers as a baseline alongside the filtered ones would have made this illustrative experiment more informative.

- **Fixed optimization hyperparameters across all datasets.** The number of optimization steps (150 for OTI, 1000 for OVI) and pseudo-tokens are held constant across all 15 datasets. The paper notes that cross-validation could improve results. Showing that at least one dataset benefits from tuning, or reporting peak performance (from the early-stopping point in Fig. 3b), would strengthen the claims that the reported numbers are not accidentally low due to a one-size-fits-all configuration.

### Trivial
None.

## Nice-to-Haves

- **An efficient approximation of modality inversion.** The paper is diagnostic, but a natural extension would be to train a lightweight MLP to regress from native to complementary-modality features using a small set of image-text pairs, then evaluate whether such a learned mapping preserves the retrieval improvement. This would directly address the acknowledged computational limitation.

- **Quantify distance to the text manifold.** The distributional evidence in Fig. 3(c) is suggestive, but a scalar metric (e.g., cosine similarity to the mean text embedding of the dataset) as a function of optimization steps would more precisely support the claim that performance peaks when features are on the text manifold but not too close to the image manifold.

- **Text-to-text retrieval scope discussion.** The text-to-text task uses captioning datasets where multiple captions describe the same image. The paper acknowledges CLIP's text encoder limitations, but a brief discussion of whether this setting is representative of general text retrieval would enhance honesty without undermining the result.

## Removed Points

- **OTI/OVI asymmetry explanation is speculative.** The harsh critic flagged the explanation for why R=1 works for OTI but P=1 does not for OVI as "somewhat speculative." This is a reasonable, non-core explanation for an observed asymmetry; it does not constitute a weakness in the paper's main claims. Removed as a nitpick.

- **Missing t-SNE visualization.** The harsh critic suggested a t-SNE figure would strengthen the paper. This is a presentation preference, not a weakness. Removed.

- **"Not yet released" or reproducibility concerns about models/citations.** The paper cites existing models and benchmarks; questioning their availability reflects reviewer knowledge gaps. Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The paper's main insight — that CLIP's intra-modal features are suboptimal for intra-modal tasks and that crossing modalities via inversion helps — is clearly stated and well-demonstrated. The reviews do not surface any deeper novel observation beyond what the paper itself articulates.

## Suggestions

1. **Report variance.** Add at least a brief statement about the number of runs or seeds used and report standard deviations for key results. Even a note that the pattern held across multiple seeds for a subset of datasets would address this concern.

2. **Add a small proof-of-concept learned mapping.** Train a lightweight regressor (e.g., MLP) on a small set of image-text pairs to approximate OTI without per-sample optimization, and show that it preserves some of the retrieval improvement. This would significantly strengthen the paper's impact without changing its diagnostic framing.

3. **Include unfiltered numbers for the Dogs vs Cats experiment.** Reporting the intra-modal retrieval numbers on the *unfiltered* dataset alongside the filtered ones would make the illustrative experiment more interpretable.

## Score and Decision

**Round 1 bracket:** [5.0, 7.0]. Weak anchors (~2-3): papers with fundamental flaws or limited scope. Middle anchors (~4-5): SeMoBridge (4.50, same intra-modal misalignment topic), Closing Modality Gap for Mixed Modality Search (5.00), CLIP Behaves like BoW (5.00, Accept Poster), Closing Modality Gap Aligns Group-Wise Semantics (5.00, Accept Poster). Strong anchors (8+): papers on different topics at oral level.

**Round 2 narrowing:** Compared directly against SeMoBridge (4.50), the paper under review is clearly stronger — it evaluates on 15 datasets vs 11, uses 5 backbones vs 1, covers multiple tasks (retrieval + classification), includes a negative control, SLIP analysis, and modality gap ablation. It is at least as strong as the CLIP BoW paper (5.00, Accept Poster) and the Closing Modality Gap Group-Wise paper (5.00, Accept Poster), both of which had narrower scope. However, the paper's limitations (no practical solution, modest improvement magnitudes, no variance reporting) keep it below the 6.5-7.0 range.

**Final score: 6.0** — The paper convincingly demonstrates a real phenomenon with thorough, well-designed experiments and multiple causal controls. It is not a breakthrough (modest improvements, diagnostic rather than practical), but it is a solid, honest, well-executed study that makes a clear empirical contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>