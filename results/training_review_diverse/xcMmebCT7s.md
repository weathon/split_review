Now I have a thorough understanding of the paper and all reviewer inputs. Let me construct the final consolidated review.

---

## Summary

This paper presents three integrated contributions: (1) **PPIRef**, the largest non-redundant dataset of 3D protein–protein interfaces (322K structures, 46K unique interfaces), built using a new scalable deduplication algorithm **(iDist)** that is 480× faster than iAlign with 99% precision and 97% recall; (2) **PPIformer**, an SE(3)-equivariant transformer pre-trained on PPIRef via structural masked modeling; and (3) a thermodynamically motivated fine-tuning strategy using log-odds ratios of predicted amino acid probabilities to predict ΔΔG. The model is evaluated on non-leaking splits of SKEMPI v2.0 and two realistic case studies (SARS-CoV-2 antibody optimization and staphylokinase engineering), showing improved generalization over existing ML methods.

## Strengths

1. **PPIRef is the largest non-redundant PPI dataset by a substantial margin.** The dataset contains 322K PPI structures (PPIRef300K), deduplicated to 46K unique interfaces (PPIRef50K) — roughly 5× more unique interfaces than DIPS (9K) and 9× more than MaSIF-search (5K) — filling a genuine gap in available training data for PPI learning.

2. **iDist enables structural deduplication at unprecedented scale.** The paper validates iDist against the established iAlign algorithm on 1,646 PPIs (2.7M pairwise comparisons), achieving 99% precision and 97% recall while being 480× faster. This scalability is what makes the PPIRef dataset construction feasible and enables the revealing analysis of data leakage in existing benchmarks (53–88% of test examples in prior DIPS splits have near-duplicates in training data).

3. **On non-leaking SKEMPI splits, PPIformer substantially outperforms existing ML methods.** On five held-out PPIs (Table 1), PPIformer achieves Spearman correlation 0.44 ± 0.03 vs. GEMME (0.38, +16%) and RDE-Network (0.24, +83%). The non-leaking split design directly addresses the data leakage problem the paper identifies, making this a more realistic estimate of generalization than prior evaluations.

4. **Thermodynamically principled fine-tuning via log-odds ratio.** The formulation (Equation 5) derives ΔΔG prediction directly from the pre-training cross-entropy loss, enforcing antisymmetry (ΔΔG_wt→mut = −ΔΔG_mut→wt) by construction without requiring two forward passes. This is a clean and principled adaptation of the pre-training objective.

5. **Practical utility demonstrated in realistic design scenarios.** In the SARS-CoV-2 antibody case study, PPIformer ranks a favorable mutation at rank 0.20% (P@1=100%); in the staphylokinase case, it ranks two strongly favorable mutations at top-1 and top-2 positions (P@1=100%, P@5%=75%, P@10%=87.5%). Both cases show superiority over baselines in ranking quality.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation isolating the effect of pre-training (structural gap).** The paper's central claim is that self-supervised pre-training on PPIRef improves downstream ΔΔG prediction. However, no experiment compares the full pipeline to an otherwise identical model trained *from scratch* on the SKEMPI fine-tuning data alone. Without this control, the reported gains could be attributed to the PPIformer architecture, the coarse-grained representation, or the thermodynamic fine-tuning loss — not necessarily to pre-training. Since the pre-training claim is a highlighted contribution, this omission weakens the evidence for it. This is fixable and does not invalidate the full pipeline's performance, but it prevents the paper from supporting a key advertised benefit.

### Minor

2. **Baseline comparison protocol is insufficiently specified for the SKEMPI evaluation.** Table 1 does not state whether the baseline methods (particularly RDE-Network, which requires supervised fine-tuning on SKEMPI) were retrained on the same non-leaking split used for PPIformer. For zero-shot methods (GEMME, MSA Transformer, ESM-IF), the comparison is naturally fair since they do not require training data. However, for RDE-Network, if its numbers are taken from prior work using a different (potentially leaking) split, the comparison is not controlled. The gap is large (0.44 vs 0.24 Spearman), so the conclusion is unlikely to reverse, but the paper should clarify this explicitly. The SARS-CoV-2 case study caption transparently states baseline values are reproduced from prior work, but the main SKEMPI evaluation lacks a similar statement.

3. **Test set is small and per-PPI variance is not reported.** The main SKEMPI evaluation averages over only 5 held-out PPIs. Standard deviations across random seeds are reported for PPIformer, but not the variation *across individual PPIs*. A single PPI with many mutations could dominate the aggregate. Per-PPI Spearman correlations (with error bars) would substantially strengthen the evaluation and reveal whether improvements are consistent or driven by a single favorable case.

4. **iDist threshold and deduplication procedure are underspecified.** The paper states the iDist threshold is "estimated to approximate iAlign" but does not provide the exact threshold value or detail the calibration procedure. The number of clusters formed during PPIRef deduplication is also not reported — only the final count (322K → 46K). These details are needed for reproducibility.

5. **No statistical significance tests for any comparison.** The paper claims superiority over baselines but reports no significance tests (e.g., bootstrap, Wilcoxon) for the Spearman correlation or other metrics. Given the small test set (5 PPIs), this would help assess whether the observed differences are reliable.

### Trivial

6. **Abstract framing could be misinterpreted.** The abstract states "outperforming other state-of-the-art methods on new, non-leaking splits," but the force-field method flex ddG outperforms PPIformer on all metrics (Spearman 0.55 vs 0.44). The body correctly clarifies this refers to ML methods and acknowledges flex ddG's superiority, but a reader skimming the abstract could over-interpret the claim.

7. **Virtual β-carbon choice is stated but not empirically justified.** The paper uses virtual Cβ directions instead of real Cβ coordinates for flexibility, but provides no ablation or analysis supporting this design choice over alternatives.

## Nice-to-Haves

- An ablation removing label smoothing and/or inverse-frequency weighting from the pre-training loss to show whether these regularizations contribute to downstream performance.
- Per-PPI breakdown of results for the 5 test PPIs, showing consistent trends.
- Reporting PPIformer's own inference/training time (beyond noting flex ddG is 5 orders of magnitude slower) to help readers judge practical applicability.
- Additional dataset statistics for PPIRef (e.g., number of unique PDB entries, interface size distribution, protein family diversity).

## Removed Points

These points are flagged to be removed per the rules; treat them with caution.

- **"The paper does not report how many near-duplicates were identified within PPIRef during deduplication"** — The paper *does* report this: PPIRef300K (322K) deduplicated to PPIRef50K (46K). The size reduction (from 322K to 46K) is explicitly stated. Removed as factually incorrect.
- **"Precision and recall can be misleading"** — The paper already acknowledges this: "we emphasize that these metrics can be misleading when selecting a model for a practical application" (line 180). Removed as already addressed by the paper.
- **"Exact split sizes not in main text"** — Per rule: remove weaknesses about missing appendix content, as the parser strips appendix sections.
- **"Missing related works"** — Per rule: do not mention missing related works without external sources to confirm their existence.
- **"Missing hyperparameters in main text (batch size, learning rate, etc.)"** — Per rule: remove nitpicks about reproducibility details that are standard to place in appendix.

## Novel Insights

A genuinely novel observation from synthesizing the reviews is that the paper's evaluation strategy — constructing a non-leaking split and independently verifying that prior splits have 53–88% leakage — creates a tension in the baseline comparison. The very claim that prior splits leak makes it *harder* for PPIformer to outperform baselines whose numbers were obtained on those easier (leaking) splits, because the leaking splits inflate their apparent performance. This means PPIformer's superiority is likely *understated* rather than overstated, a point the paper does not explicitly leverage. Conversely, the lack of a from-scratch ablation means we cannot separate how much of PPIformer's success comes from pre-training vs. the architecture and fine-tuning loss. The paper would be strengthened by explicitly addressing this asymmetry.

## Suggestions

1. **Add a from-scratch baseline**: Train PPIformer on the SKEMPI fine-tuning data alone (no PPIRef pre-training), keeping architecture and loss identical. If the pre-trained version outperforms it, the pre-training contribution is confirmed.
2. **Clarify baseline evaluation protocol**: Explicitly state whether each baseline was retrained on the same non-leaking split or whether numbers are transferred from prior work. If transferred, note the expected bias direction.
3. **Report per-PPI results**: Provide a table or figure showing Spearman correlation (with seed-based error bars) for each of the 5 held-out PPIs individually, so readers can assess consistency.
4. **Release the exact iDist threshold**: Document the calibrated threshold value that approximates iAlign, and report deduplication statistics (number of clusters, cluster size distribution) for PPIRef.

## Score and Decision

The paper makes three genuine contributions (PPIRef dataset, iDist algorithm, PPIformer with thermodynamically motivated fine-tuning) and presents convincing evidence that the full pipeline outperforms existing ML methods on non-leaking splits. The main weakness — absence of a from-scratch ablation for the pre-training claim — is a real gap but does not invalidate the pipeline's demonstrated performance; the dataset and iDist contributions stand independently. The baseline comparison concern is mitigated by the large performance margins and the fact that most ML baselines are zero-shot methods unaffected by training split differences. These issues are addressable in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>