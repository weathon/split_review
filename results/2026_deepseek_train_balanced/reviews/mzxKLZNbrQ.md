## Summary

This paper introduces Youku-mPLUG, a 10M-pair Chinese video-text dataset collected from Youku (the largest publicly available dataset of its kind), along with human-annotated downstream benchmarks for video category classification (100K), retrieval (38K), and captioning (171K). It also proposes mPLUG-Video, a modularized decoder-only model with a frozen LLM and only 1.7% trainable parameters. The primary contribution is the dataset release; the model is a secondary contribution.

## Strengths

- **First publicly available large-scale Chinese video-language pre-training dataset.** Table 1 (lines 24–34) shows that all prior Chinese datasets (ALIVOL-10M, Kwai-SVC-11M, CREATE-10M, CNVid-3.5M) are marked unavailable, while Youku-mPLUG is the only one publicly released. This concretely fills a documented gap.

- **Largest public Chinese downstream benchmark covering three tasks.** Table 2 (lines 45–59) shows 365K human-annotated samples across retrieval, classification, and captioning — broader coverage than any existing Chinese benchmark, all publicly available.

- **Demonstrable pre-training benefit on the paper's own benchmarks.** Table 4 (lines 253–263) shows ALPRO with Youku-mPLUG pre-training achieving 78.15% top-1 accuracy vs. 69.40% without (a 12.6% relative gain from the dataset alone, holding modality constant).

- **Documented annotation quality control.** Section 3.2 specifies concrete annotator qualification thresholds (error rate >2.5% leads to disqualification) and multi-annotator verification for validation/test sets (three annotators for classification, "more than three" for captioning).

- **Data leakage prevention within benchmarks explicitly documented.** Lines 151 and 154 specify that clips from the same video or sharing the same title are exclusively assigned to either training or testing sets.

## Weaknesses

### Major

- **"State-of-the-art" claim on self-created benchmarks is circular.** The paper claims mPLUG-Video "achieves a new state-of-the-art result on these benchmarks" (abstract, line 6; line 65; line 285; contribution item 4). These benchmarks were created by the same paper; no external model has ever been evaluated on them. Claiming SOTA where there are no prior entries is not informative — it is reporting raw scores. The correct framing would be establishing initial baselines. This is a persistent framing problem throughout the paper.

- **No cross-dataset evaluation on established benchmarks.** For a dataset paper, the central question is whether pre-training on Youku-mPLUG transfers to existing benchmarks (e.g., VATEX Chinese, MSRVTT). The paper provides no such experiment. The only evaluation is on tasks built from the same video source as the pre-training data. This gap means the dataset's external utility remains asserted rather than demonstrated.

- **Title signal creates a confound in the benchmarks.** The pre-training data uses video titles as paired text (Section 3.1). The classification annotation process asks annotators to confirm categories based on "videos and their titles" (line 148). The retrieval task incorporates titles into text queries (line 154). The ablation in Table 4 shows a language-only model (no video input) achieves 59.31% top-1 accuracy, meaning titles alone carry substantial predictive signal. This raises the concern that models may learn title-to-category correlations rather than genuine video understanding, and the benchmarks may not cleanly separate these factors.

- **Suspicious numerical values in results tables that may indicate reporting errors.**
  (1) In Table 2 (lines 222–226), mPLUG-2 and mPLUG-Video (1.3B) have *identical* ROUGE (52.9) and CIDEr (67.7) scores despite being different architectures with different BLEU-4 and METEOR scores. This is highly unusual and requires explanation.
  (2) In Table 3 (lines 239–242), mPLUG-2 and both mPLUG-Video variants show *identical* V2T and T2V retrieval scores at every rank (e.g., R@1 = 38.45 for both directions for mPLUG-2), while ALPRO shows the expected asymmetry (27.00 vs. 26.63). This pattern across multiple models needs clarification — it may indicate a reporting error or an unusual evaluation protocol.
  (3) The Table 3 caption says "we report the average of R@1, R@5 and R@10" but the columns show R@1, R@2, R@10 for V2T (different metric set), which is inconsistent.

- **mPLUG-Video's catastrophic retrieval performance undermines the method contribution.** The model achieves R@1 of 7.01 (1.3B) and 7.62 (2.7B) compared to mPLUG-2's 38.45 (Table 3) — roughly 5× worse. The paper attributes this to the frozen LLM hindering cross-modal feature extraction (line 213), which essentially acknowledges the proposed architecture is fundamentally unsuitable for a core video-language task. Claiming overall SOTA on the benchmark suite while failing catastrophically on one of three tasks is misleading. This model is not a meaningful contribution to retrieval.

### Minor

- **No external model comparisons on the benchmarks.** The only models evaluated are ALPRO, mPLUG-2, and mPLUG-Video — all from the same research lineage. While creating new benchmarks makes broad comparison difficult, the paper could evaluate at least one externally developed Chinese-capable model (e.g., VideoLLaMA, VideoChat) on the classification or captioning tasks to calibrate difficulty.

- **No analysis of potential data leakage between pre-training and benchmark test sets.** Both come from Youku. The paper addresses within-benchmark leakage (lines 151, 154) but does not discuss whether videos in the downstream test sets could also appear in the pre-training data. This is a standard concern for dataset papers and should be addressed.

- **Small human evaluation sample.** The zero-shot instruction understanding evaluation (Section 4.4) uses only 65 instructions from 50 videos (line 278). This sample is too small to support generalizable conclusions about video understanding ability, and no confidence intervals are reported.

- **The 23.1% improvement headline uses a selective baseline.** The figure in the abstract (line 4) is computed relative to the vision-only, no-pretraining baseline (63.51% → 78.15%), not the more natural comparison of both-modalities without pretraining (69.40% → 78.15%, which yields 12.6%). The number is traceable from Table 4, but the choice inflates the headline result.

- **No confidence intervals or variance estimates anywhere.** No experiment reports standard deviations or confidence intervals, despite fine-tuning runs typically showing variance.

### Trivial

- The CLIP similarity threshold used for quality filtering (Section 3.1, line 128) is not reported.
- "Balanced distribution" across categories (line 62) is claimed but not quantified beyond a figure.
- Table 3 caption mentions R@1/R@5/R@10 but columns show R@1/R@2/R@10 for V2T — likely a reporting inconsistency.

## Nice-to-Haves

- Evaluate on an existing cross-dataset benchmark (e.g., VATEX Chinese) to demonstrate the pre-training data's value beyond the paper's own ecosystem.
- Compare against the alternative of pre-training on machine-translated English data (e.g., WebVid with Chinese translated captions) to show that native Chinese data provides additional value.
- Analyze what fraction of the 400M → 10M reduction (97.5% filter rate) is attributable to each filtering criterion, to help the community understand data quality in the raw Youku pool.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- **"No comparison to prior Chinese datasets (ALIVOL, Kwai-SVC, etc.)"** — Removed because the paper explicitly documents (Table 1, line 82) that these datasets are not publicly available, making comparison infeasible.
- **"Related work doesn't discuss what kinds of videos Youku contains"** — Removed because Section 3 describes 45 categories across 20 super-categories with a dedicated figure (Fig. 3), which addresses this.
- **"Annotation relies on Youku's noisy prediction model"** — Removed because the paper explicitly acknowledges the model's ~94% accuracy is "not entirely reliable" and describes manual verification by multiple annotators (line 148), addressing this concern.
- **"Model comparison should include VideoLLaMA, VideoChat"** on benchmarks — Partially valid but weakened: these models are designed for open-ended QA, not classification/retrieval, so their absence on those specific tasks is reasonable. The human evaluation does compare to VideoLLaMA (Section 4.4).
- **"No analysis of vocabulary coverage or linguistic diversity"** — Generic request. The paper provides word length statistics and category distributions. Removed as insufficiently specific.
- **"Missing CLIP threshold for similarity filtering"** — Demoted to Trivial (present in that section above).

## Novel Insights

None beyond the paper's own contributions. The core insight — that releasing the first public large-scale Chinese video-language dataset fills a real gap — is the paper's primary contribution, and the reviews do not surface an additional synthetic insight beyond this.

## Suggestions

1. Reframe all "state-of-the-art" claims as establishing initial baselines on a new benchmark suite. This is both more accurate and more useful to the community.

2. Add at least one cross-dataset experiment: pre-train on Youku-mPLUG and evaluate on VATEX Chinese (or MSRVTT with translated captions). This single addition would substantially strengthen the paper's core claim about the dataset's utility.

3. Address the suspicious identical scores in Tables 2 and 3 — either correct any reporting errors or explain why different architectures produce identical metric values.

4. Analyze and report potential overlap between pre-training videos and benchmark test videos.

5. Report confidence intervals or standard deviations for at least the main results.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>