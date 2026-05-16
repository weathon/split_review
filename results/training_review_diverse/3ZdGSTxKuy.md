Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper introduces a new "atypical" video dataset (5,486 videos from sci-fi, animation, unintentional, and abnormal/surveillance sources) and studies whether exposing a video action recognition model to such atypical data via outlier exposure (OE) improves OOD detection. Using UCF101 as in-distribution data and testing on HMDB51, MiT-v2, and synthetic noise, the authors show that fine-tuning a ResNet3D-50 with atypical OE data consistently improves OOD detection metrics over a no-OE baseline and often over OE with Kinetics400. The paper further demonstrates that increasing the categorical diversity of atypical samples yields additional gains.

## Strengths

- **First dedicated atypical video dataset for open-world learning.** The paper collects and curates a novel resource (Section 3.1, Table 1) that explicitly targets visual content far from standard action-recognition benchmarks — sci-fi, animation, unintentional actions, and anomaly/surveillance footage. This fills a real gap, as existing video datasets emphasize typical human activities.

- **Clear evidence that OE with atypical data improves OOD detection over a no-OE baseline.** Table 2 shows consistent gains on multiple OOD test sets (e.g., AUROC on HMDB51 improves from 70.0 to 82.3 with atypical OE). The baseline comparisons (no OE, noise OE, Diving48 OE) provide a meaningful frame of reference independent of the Kinetics400 comparison.

- **Systematic demonstration that categorical diversity of atypical samples helps.** Figures 4–5 and Table 3 show that combining more atypical categories (abnormal, unintentional, sci-fi, animation) yields progressively better and more stable OOD detection performance. This goes beyond a simple "atypical data helps" result and provides a more nuanced insight about diversity being the driving factor.

- **Extends outlier exposure methodology to the video domain.** Prior OE work focused on images and text (Hendrycks et al., 2019). Validating that the same principle transfers to video action recognition opens a new direction for video open-world learning and provides a strong baseline for future work.

## Weaknesses

### Fatal
None.

### Major

- **The central comparison (atypical vs. Kinetics400) confounds data atypicality with dataset size.** The atypical dataset contains 5,486 videos while Kinetics400 contains ≈240,000 — a 40× difference. Without subsampling Kinetics400 to match the atypical size, the observed advantage cannot be cleanly attributed to atypicality versus curation quality, dataset scale, or insufficient fine-tuning epochs for the larger set. This is the paper's headline comparison and the confound reduces confidence in the core claim that "atypical data outperforms typical data" for OE. (The baseline comparisons in Table 2 — no OE, noise OE, Diving48 OE — are not affected, but the most directly relevant comparison to a "typical" video dataset is.)

### Minor

- **No verification that the atypical data is distributionally distinct from the test OOD sets.** The paper asserts (Section 4.2.3) that the atypical dataset is "significantly different from the categories in these common video datasets" but provides no quantitative evidence. The abnormal subset (UCF Crime, ShanghaiTech) includes surveillance footage of fighting, stealing, shooting — actions that have semantic parallels in HMDB51 (punch, kick, shoot gun). A feature-space analysis (e.g., nearest-neighbor distances between atypical samples and OOD test samples) would substantially strengthen the claim that observed improvements are not partly due to distributional leakage.

- **Diversity ablation (Figures 4–5) confounds the number of categories with total sample count.** Adding more atypical categories also increases total videos, so the improvement could be driven by more data rather than by categorical diversity per se. A cleaner ablation would hold the total number of videos fixed while varying the number of categories, or at minimum acknowledge this confound as a limitation.

- **No variance reporting across multiple runs.** All results (Tables 2–3) are reported as point estimates without standard deviations or confidence intervals. Given that fine-tuning for only 5 epochs involves stochasticity, this makes it difficult to assess whether the observed differences are statistically significant.

- **The abnormal subset dominates the dataset (85% of total videos), but this imbalance is not discussed as a limitation.** The ablation study partially addresses this by showing results with different category combinations, but the paper does not explicitly acknowledge that the overall results may be driven primarily by the abnormal data.

- **No public dataset release statement is provided.** For a paper whose contributions include a new dataset, the absence of a public release plan or link limits the community's ability to build on this work.

- **The t-SNE analysis (Figure 6) is purely qualitative and does not directly visualize model decision boundaries after OE with different datasets.** The figure shows feature distributions of the *datasets themselves* rather than how the model's feature space changes after OE fine-tuning. While suggestive, this does not constitute strong evidence for the claimed boundary-spreading effect.

### Trivial

- **Missing preprocessing details.** The paper describes trimming clips to "action-rich segments" (Section 3.2) but does not report video duration, frame rate, resolution, or specific trimming criteria. Adding these details would aid reproducibility.

## Nice-to-Haves

- Add at least one more real OOD test set (e.g., use Kinetics as ID and UCF101 as OOD) to strengthen generalization claims.
- Show a curve of OOD performance vs. fine-tuning epochs for both Kinetics400 and atypical OE to rule out underfitting of the larger K400 set.
- Discuss whether the cost of collecting/curating atypical data is justified relative to simpler alternatives (e.g., stronger baselines, data augmentation).
- Include a quantitative measure of feature separation (e.g., Fisher discriminant ratio) to complement the qualitative t-SNE.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper should justify cost of atypical data relative to simpler alternatives."** → This expects the paper to solve a broader engineering tradeoff that is outside its stated exploratory scope. Moved to Nice-to-Haves.
- **"The paper says 'For D_OE, Kinetics400 and atypical data ... are used' but figure legend shows them separately — no spatial comparison."** → The figure does plot both distributions in the same space, and the paper compares their spread. The reviewer appears to have partially misread the figure. The valid sub-concern (qualitative nature) is kept in Minor above.
- **"Missing video duration/frame rate/resolution details"** → Trivial; added to Trivial section above, not removed.

## Novel Insights

The reviews surface a genuine tension that the paper itself does not fully resolve: the claim that *atypicality* (rather than curation quality, dataset size, or distributional overlap) drives the OOD detection improvements is interesting but under-evidenced. The diversity ablation comes closest to isolating the key mechanism, but even there the size confound blunts the conclusion. A cleaner insight would emerge if the paper could show that *within the same total number of videos*, datasets with broader categorical diversity (i.e., mixing atypical categories) outperform homogeneous atypical datasets. The reviews collectively point to this as the single most impactful experiment that is still missing.

## Suggestions

1. **Control for dataset size in the Kinetics400 comparison.** Randomly subsample Kinetics400 to match the atypical dataset size (≈5.5k videos) and repeat the main experiment. If atypical still outperforms size-matched Kinetics400, the core claim is strongly supported. This is the single most important revision.
2. **Add a quantitative distributional overlap analysis.** Compute feature-space nearest-neighbor distances between atypical samples and OOD test samples to verify that improvements are not due to leakage.
3. **Control total sample count in the diversity ablation.** Keep total videos fixed (e.g., 1,000 or 2,000) while varying the number of atypical categories. This cleanly separates diversity from quantity.
4. **Report standard deviations over at least 3 random seeds** for all main results. This is standard practice and would substantially increase confidence in the findings.
5. **Add a public dataset release statement** and discuss the imbalance in dataset composition as a limitation.
6. **Acknowledge all confounds explicitly** in a Limitations subsection rather than leaving them for reviewers to discover.

## Score and Decision

The paper asks a compelling and under-explored question, introduces a useful new resource, and provides multiple lines of suggestive evidence. The main empirical result (atypical OE improves OOD detection over no OE) is well-supported. However, the headline comparison with Kinetics400 is confounded by dataset size, the diversity ablation is confounded by sample count, and the risk of distributional overlap with test OOD sets is not evaluated. These issues are fixable and do not invalidate the paper's core contributions, but they prevent the current version from being a fully convincing demonstration. With the suggested controls and analyses, this would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>