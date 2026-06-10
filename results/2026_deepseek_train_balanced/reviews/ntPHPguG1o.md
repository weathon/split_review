Here is my final consolidated review:

---

## Summary

This paper tackles unsupervised product-to-patent image retrieval, where RGB product photos must be matched against patent line drawings. The authors construct the PPIR dataset (240 test pairs, 16,850 patent pool, 3.8M unlabeled images) and systematically evaluate three domain-gap mitigation strategies, finding that jointly mapping both domains to edge maps works best. They then propose training a standard classifier on edge maps of ImageNet1K (ImageNet1K-edge) with cross-entropy loss and using the backbone as a feature extractor. Results show that supervised Swin-S (1.3M images, 16h) achieves AUC 0.80, outperforming the best unsupervised method MAE (3.8M images, ~100h) at AUC 0.79.

## Strengths

- **Tackles an underexplored and practically relevant task.** Product-to-patent image retrieval is genuinely neglected compared to text-based patent retrieval and patent-to-patent image retrieval. The paper identifies, formalizes, and provides a testbed for this problem.

- **Systematic evaluation of domain-gap mitigation strategies.** The paper evaluates three approaches (product→edge, patent→colorized, both→edge) with TSNE visualizations (Fig. 1), retrieval curves (Fig. 3a), and efficiency analysis (edge extraction at 28 imgs/s vs. generative colorization at 2 imgs/s). The finding that joint edge mapping outperforms the alternatives is empirically grounded.

- **Dataset contribution.** The PPIR dataset (testing pairs + patent pool + unlabeled pre-training data) fills a gap in the literature and is committed to public release, enabling future research in this area.

- **Supervised edge pre-training beats large RGB-pretrained models.** In Fig. 4-(2), the proposed method (1.3M images, 224×224) outperforms EVA02 (trained on large-scale datasets at 448×448) and CLIP. This is arguably the cleanest comparison in the paper and demonstrates that edge-specific pre-training has real value.

## Weaknesses

### Major

1. **Confounded comparison undermines the central supervised-vs.-unsupervised claim.** The headline comparison (Section 4.2, Fig. 4-(1)) pits supervised pre-training on ImageNet1K-edge (with 1,000-class labels) against unsupervised methods trained on PPIR-unlabeled edge maps (no labels). Two variables differ simultaneously: data source (ImageNet vs. PPIR) and supervision (labels vs. no labels). That supervised training with 1,000 semantic categories beats unsupervised training without labels is an expected outcome, not a discovery. The paper frames this as answering Q2 ("Why does supervised outperform unsupervised?"), but the experiment cannot cleanly attribute improvement to supervision versus data differences. A controlled comparison — e.g., supervised vs. unsupervised on the *same* data (both on ImageNet1K-edge, or both on PPIR-unlabeled) — is absent.

2. **The "method" contribution is standard classification training applied to edge maps — not a novel paradigm.** The proposed supervised pre-training (Section 3.3) is: (1) apply an off-the-shelf edge detector to ImageNet; (2) train a classifier with cross-entropy loss on edge maps; (3) use the backbone as a feature extractor. There is no new architecture, loss function, training strategy, or mechanism addressing edge-map sparsity. The abstract calls this "a novel supervised pre-training paradigm," but it is a straightforward engineering adaptation. The contribution is empirical, not methodological.

3. **Missing the most informative comparison: edge-supervised vs. RGB-supervised on the same task.** The paper never directly compares supervised pre-training on ImageNet1K-edge (proposed) against standard supervised pre-training on ImageNet1K-RGB, with both evaluated on edge-map inputs for the same retrieval task. This would isolate whether the *edge-specific* pre-training modality provides any benefit beyond the supervision itself. Fig. 3-(2) partially addresses this via fine-tuning, but it is not a clean head-to-head comparison. Fig. 5 claims "consistent performance improvements" but does not clearly specify the baseline being improved upon.

### Minor

4. **Test set is small (240 pairs) with no statistical significance reported.** With only 240 queries and a retrieval pool of 16,850, small differences in correct retrievals can meaningfully shift rank-based metrics. No confidence intervals, bootstrap estimates, or significance tests are provided. The paper acknowledges the size limitation (lines 158–159) but does not address the statistical reliability concern.

5. **Q2 ("Why does supervised pre-training outperform unsupervised?") is posed but never answered.** The paper demonstrates *that* supervised pre-training works better, but provides no analysis of *why* — e.g., what features the edge classifier learns, how they transfer to patent drawings, or evidence for the sparsity hypothesis beyond intuition. The answer is left as speculation.

6. **Dataset construction is underspecified.** The paper uses a language model (cited as Kenton & Toutanova, 2019 — BERT) to filter candidate patents but does not specify how it was applied, what prompts/parameters were used, or how the 240 ground-truth pairs were collected, verified, and by whom. This limits reproducibility.

### Trivial

7. **Figure numbering inconsistency.** The text (line 156) refers to "Fig. 6" but the caption below it reads "Figure 5."

## Nice-to-Haves

- Reporting Top-k retrieval accuracy (Top-1, Top-5, Top-10, Top-50) alongside AUC/AvgRank would make results more interpretable for practitioners.
- An analysis of sensitivity to the choice of edge detector (Canny, HED, etc.) would strengthen the claim of generalizability.
- A controlled experiment comparing supervised edge pre-training vs. supervised RGB pre-training (both on ImageNet, both with labels, differing only in input modality) would directly validate the central thesis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about tables not being visible in extracted text and "grammatical issues."** Removed as parser artifacts — the original submission does not have these problems.
- **Complaint that the paper does not include appendix/supplementary content.** Removed because the parser strips supplementary material from all papers.
- **Complaint that unsupervised methods should have been trained on ImageNet1K-edge instead of PPIR-unlabeled.** This is a valid controlled-experiment suggestion but training on in-domain data (PPIR-unlabeled) is also a defensible choice. The core issue (confounded comparison) is already captured in Major weakness #1.
- **Criticism that the paper's "domain gap analysis" is obvious.** The systematic comparison of three strategies with both quantitative and qualitative evidence is a genuine strength, not a weakness.

## Novel Insights

The most telling observation from this review is that the paper's strongest evidence — edge-supervised models beating massive RGB-pretrained models like EVA02 and CLIP in Fig. 4-(2) — receives less emphasis than the confounded supervised-vs.-unsupervised comparison in Fig. 4-(1). If the paper restructured its narrative around "edge-specific supervised training is more sample-efficient for this task than generic RGB-pretrained models of any scale," the contribution would be clearer and the experimental support stronger. The paper's weakest element is its framing: posing Q2 as a "why" question that the experiments cannot answer, while the actual finding ("edge-specific supervised training works") is an empirical observation, not an explanation.

## Suggestions

1. Restructure the experiments to include a controlled comparison: supervised edge-supervised vs. supervised RGB-supervised (same labels, same architecture, differing only in pre-training modality). This directly tests whether edge-specific pre-training adds value beyond standard RGB supervision.
2. Either answer Q2 with actual feature-space analysis (e.g., what does the edge classifier learn? visualized nearest neighbors, per-class accuracy on edge maps) or reframe Q2 as an empirical "does it work?" question.
3. Report confidence intervals or bootstrap estimates for all metrics given the small test set.
4. Provide clearer documentation of the dataset construction pipeline (which language model, how applied, annotation protocol).

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>