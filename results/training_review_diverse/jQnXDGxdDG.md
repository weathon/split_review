Now I have a thorough understanding of the paper and can verify all claims. Let me construct the final review.

## Summary

The paper introduces FIRM (Focused In-distribution Representation Modeling), a multi-positive contrastive loss for anomaly detection. FIRM applies SupCon-style multi-positive pairing to in-distribution (ID) samples — encouraging tight clustering — while retaining NT-Xent-style single-positive pairing for synthetic outliers — preserving their diversity as hard negatives. Experiments on CIFAR-10/100, Fashion-MNIST, Cats-vs-Dogs, and MVTec-AD show FIRM outperforming prior contrastive methods such as CSI and DROC, with ablation studies confirming consistent superiority over both NT-Xent and SupCon.

## Strengths

- **Strong and consistent empirical results.** Table 1 shows FIRM (with rotation-based synthetic outliers) achieving a mean AUROC of 92.4% on CIFAR-10, versus CSI's 85.2% and DROC's 87.6%; adding OE pushes this to 97.4%. These gains hold across CIFAR-100, Fashion-MNIST, and Cats-vs-Dogs. The improvement is substantial by the standards of this benchmark.

- **Ablation studies clearly validate the design.** Table 4 directly compares FIRM against NT-Xent and SupCon using identical scoring and outlier generation. FIRM outperforms both in AUROC and AULC on all four datasets, with relative AUROC gains of up to 7.8% over NT-Xent on CIFAR-10. This provides direct evidence that the multi-positive-for-ID / single-positive-for-outliers recipe is more effective than either existing alternative for anomaly detection.

- **Robustness across scoring methods.** Performance improves monotonically from cosine similarity ($s_{\mathrm{con}}$) to rotation ensemble ($s_{\mathrm{shift}}$) to full ensemble ($s_{\mathrm{ens}}$), demonstrating that FIRM learns representations amenable to simple post-hoc scoring and test-time augmentation.

## Weaknesses

### Fatal

None.

### Major

- **Modest novelty: FIRM is a direct, natural hybrid of existing contrastive losses.** The loss combines SupCon's multi-positive strategy (applied to ID samples) with NT-Xent's single-positive strategy (applied to synthetic outliers). The paper acknowledges this integration (line 61: "Our approach integrates elements from both NT-Xent and SupCon losses"). While the motivation — that NT-Xent over-diversifies ID and SupCon collapses outliers — is sound, the resulting formulation follows almost algorithmically from these observations. The paper does not articulate a non-obvious design principle or explain why this specific combination was non-trivial to arrive at. The contribution is more "insightful engineering" than a new learning paradigm, and the paper's framing does not fully compensate for this with unusually deep analysis or surprising margins. This limits the paper's impact as a methodological contribution.

- **Internal contradiction between homogeneity motivation and multiclass OOD evaluation.** The paper's central motivation is that FIRM is needed because ID is naturally homogeneous (unimodal) in anomaly detection, and NT-Xent's pressure toward diversity is harmful. Yet one of the claimed contributions is strong performance on *unlabeled multiclass* OOD detection, where CIFAR-10 (10 classes) serves as ID — precisely the non-homogeneous setting. The paper acknowledges this mismatch (line 120: "FIRM's hyperparameters were tuned for anomaly detection rather than the unlabeled multiclass setting") but still presents it as a contribution ("extending the applicability… demonstrating capabilities while handling non-homogeneous and multimodal ID"). This creates a logical tension: either FIRM is designed for homogeneous ID (and the multiclass results are a curiosity needing separate justification), or FIRM is robust across settings (and the homogeneity argument should not be so central to the motivation). The current framing undermines the paper's conceptual coherence.

- **Core claim about representation quality is supported only by qualitative evidence.** The paper's narrative — NT-Xent over-diversifies ID, SupCon collapses outliers, FIRM strikes the right balance — rests on the loss landscape visualization (Figure 1) and t-SNE plots for one dataset (MVTec-AD, Figure 2). No quantitative measures of intra-class compactness, inter-class separation, or outlier diversity are extracted from the learned representations across the benchmark datasets. The paper cannot show *how* FIRM's representations differ from those of NT-Xent/SupCon in measurable terms. This limits the paper's ability to explain *why* FIRM outperforms alternatives, turning the central explanatory claim into an illustration rather than evidence.

### Minor

- **Sensitivity to k in k-NN scoring is underexplored.** Main results (Table 1) use k=5, while ablation comparisons (Table 4) use k=1, with no systematic analysis of how FIRM's performance or relative advantage varies with k. It is unclear whether FIRM's superiority is robust across different nearest-neighbor regimes or is specific to the chosen k.

- **Disentanglement of OE benefit vs. loss design is incomplete.** FIRM w/ OE consistently outperforms FIRM without OE, but the paper does not explicitly analyze whether FIRM derives disproportionately more benefit from OE than NT-Xent does. The ablations hint at this pattern but do not quantify it, leaving open whether the gains come primarily from OE's additional negatives rather than FIRM's multi-positive design.

- **No discussion of failure modes or limitations.** The paper does not discuss cases where FIRM's pressure toward a single ID cluster could be harmful — for example, when ID is naturally multimodal (multiple normal operation modes in industrial settings) or when the class-imbalance within ID is severe. A brief limitations section would strengthen the paper's intellectual honesty and practical utility.

### Trivial

None.

## Nice-to-Haves

- Quantitative characterization of the learned representation space (e.g., average pairwise cosine similarity among ID samples and among synthetic outliers, separation gap) to directly validate the loss landscape argument.
- Sensitivity analysis of the temperature parameter τ and batch size — the paper mentions this analysis in Section 3.2 (likely in figures stripped by the parser), so this is already partially addressed.
- Brief discussion of computational overhead relative to NT-Xent and SupCon (asymptotically the same, but a note would help).
- Exploration of whether FIRM's advantage persists with different OE source distributions (e.g., in-distribution-near vs. far outliers).

## Removed Points

- *"The loss landscape analysis does not quantify alignment/diversity"* — kept as a major weakness (it is substantively correct). However, the related suggestion to add quantitative measures is moved to Nice-to-Haves.
- *"The paper should include sensitivity analysis of temperature τ and batch size"* — removed (moved to Nice-to-Haves) because the paper states this analysis is conducted (line 127: "we examine … the behavior of the FIRM loss function under different temperature values τ and batch sizes"); the results likely appear in figures stripped by the parser.
- *"The paper does not discuss computational overhead of FIRM"* — moved to Nice-to-Haves; this is a minor omission, not a structural flaw.
- *"Missing limitations section"* — kept as a minor weakness (the paper's conclusion is very brief and does not discuss limitations).

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's main empirical findings and surface two issues that the authors should address (the homogeneity-motivation contradiction and the qualitative-only representation analysis), but do not produce a synthesized insight that the paper itself does not already contain.

## Suggestions

1. Reconcile the homogeneity assumption with the multiclass OOD experiments. Either reframe those experiments as an exploratory investigation with explicit caveats, or adapt the loss for multimodal ID (e.g., by treating each augmented view as its own cluster anchor). The current framing weakens the paper's internal logic.

2. Add quantitative representation-space statistics (e.g., average pairwise cosine similarity of ID samples, average pairwise cosine similarity of synthetic outliers, and the separation gap between ID and outlier representations) across the benchmark datasets. This would turn Figure 1 from an illustration into evidence and directly support the paper's central explanatory claim.

3. Include a brief limitations paragraph discussing when FIRM may hurt performance (multimodal ID, imbalanced ID classes, small batch sizes where multi-positive has few ID samples to pull from).

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>