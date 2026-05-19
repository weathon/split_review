- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have a thorough understanding of the paper and all review claims. Let me write the consolidated review.

## Summary

This paper identifies the one-to-many mapping problem in point cloud completion — where an incomplete point cloud can correspond to multiple valid complete shapes, creating contradictory supervision signals. The authors propose a completion consistency loss that enforces consistent completions across multiple partial views of the same object. Two variants are introduced: self-guided (consistency among predictions from different views) and target-guided (consistency of predictions with the full ground-truth cloud). Experiments on three networks (PCN, AxFormNet, AdaPoinTr) and two benchmarks show consistent performance improvements without any architectural changes.

## Strengths

- **Consistent performance gains across multiple architectures and datasets.** On ShapeNet55, the consistency loss improves mean CD by 27% for PCN (1.46→1.07), 25% for AxFormNet (1.21→0.91), and 4.8% for AdaPoinTr (0.83→0.79), all under the controlled setting where the only difference is the loss function (Table 4). This demonstrates the loss is broadly applicable, not tied to a single architecture.

- **Improved generalization to unseen categories.** On ShapeNet34 (where 21 categories are withheld during training), the performance gap Δ between seen and unseen categories is substantially reduced: PCN Δ drops from 0.82 to 0.30, AxFormNet Δ from 0.20 to 0.13 (Table 5). This indicates the consistency loss acts as a useful regularizer for out-of-distribution completion.

- **Well-designed ablation and control experiments.** The paper rules out the trivial explanation that gains simply come from more training data by showing that tripling training epochs (without consistency loss) does not replicate the improvement (Section 4.3, "Number of Training Samples"). The ablation of scaling factors α and β (Table 6) provides useful insight into the interaction between self-guided and target-guided losses.

- **Clear motivation with toy-dataset evidence.** The controlled toy-dataset experiment (Table 3) provides direct evidence that the one-to-many mapping problem materially degrades completion performance, grounding the paper's motivation in empirical observation.

## Weaknesses

### Major

- **Unsupported claim that simple networks with consistency loss match complex networks.** The paper states: "PCN with consistency loss achieves a mean CD of 1.07·10⁻³, which is better than the mean CD of PoinTr (1.09·10⁻³)" and "AxFormNet with consistency loss achieves a mean CD of 0.91·10⁻³, which is better than the mean CD of SeedFormer (0.92·10⁻³)" (Section 4.2.1). However, PoinTr and SeedFormer were **not retrained under the same optimized training conditions** (AdamW, cosine annealing) used for the consistency-loss experiments. The paper's own Section 2.2 demonstrates that simply switching the training strategy improves PCN from 4.08 to 2.37 — a massive gain. There is no reason to believe PoinTr or SeedFormer would not also improve under the same optimized training recipe. This comparison is therefore unfair, and the headline claim about matching SOTA is not supported by the evidence as presented. The core contribution (consistency loss improves networks under controlled conditions) remains intact, but this secondary claim overstates the results.

### Minor

- **Self-guided consistency loss contains a design nuance not discussed.** The self-guided loss computes CD between predicted complete clouds from different views: \(\hat{\mathbb{P}}^{\text{com}}_{k,i} = \hat{\mathbb{P}}^{\text{mis}}_{k,i} \cup \mathbb{P}^{\text{inc}}_{k,i}\). Since \(\mathbb{P}^{\text{inc}}_{k,i}\) (the input points) differ across views, the CD computation includes distances between these fixed input points. Gradients can flow from the predicted missing points \(\hat{\mathbb{P}}^{\text{mis}}_{k,i}\) toward nearest neighbors in the *other view's input points* \(\mathbb{P}^{\text{inc}}_{k,j}\) — a spurious signal because the other view's input region is not the ground-truth missing region. The ablation partially mitigates this concern: the optimal configuration uses a small α=0.1 (damping self-guided's influence), and self-guided alone still helps (CD 1.56 vs baseline 1.60). But the paper should acknowledge and analyze this behavior.

- **The number of views \(n\) is fixed at 3 without investigation.** The paper does not study the effect of \(n\) on performance, computational cost, or gradient quality. Understanding this trade-off is important for practical deployment.

- **Batching strategy is unclear.** The paper states batch size 64 for PCN with \(n=3\). It is not specified whether each GPU forward pass processes \(64 \times 3 = 192\) point clouds or whether views are handled differently. This affects memory and reproducibility.

- **No discussion of failure cases or limitations.** The paper does not address scenarios where the consistency loss could be detrimental (e.g., symmetric objects where different views legitimately produce different completions, or cases where very different view geometries produce inconsistent training signals).

### Trivial

- Equation (3) notation: \(\mathcal{L}^{\text{rec}}_{i,k}\) is introduced inside the total loss but its relationship to \(\mathcal{L}^{\text{rec}}_k\) (Equation 1) could be clearer. Specify that \(\mathcal{L}^{\text{rec}}_{i,k} = \text{CD}(\hat{\mathbb{P}}^{\text{mis}}_{k,i}, \mathbb{P}^{\text{mis}}_{k,i})\).

## Nice-to-Haves

- Retrain PoinTr and SeedFormer (or at least one representative) under the same training strategy as the consistency-loss models to validate the matching-SOTA claim. Alternatively, retract the claim and position the contribution as "improving existing networks under controlled conditions."
- Report training overhead (additional time/memory per batch) so practitioners can weigh benefit vs. cost.
- Study the effect of varying \(n\) (number of views) to provide practical guidance on the trade-off.
- Compare self-guided loss computed on predicted complete clouds (as proposed) vs. predicted missing clouds only, to isolate the gradient issue noted above.

## Removed Points

*The following points raised by the reviewers are removed with justification:*

- **"Section 3 notation is ambiguous"** — This is a formatting/parsing issue; the relationship between \(\mathcal{L}^{\text{rec}}_{i,k}\) and \(\mathcal{L}^{\text{rec}}_k\) is clear enough given the surrounding text. Downgraded from a kept minor to removed.
- **Harsh Critic's "Generic criticism about training conditions not being identical"** — The paper explicitly states in Section 4.1.2 that the three main networks (PCN, AxFormNet, AdaPoinTr) are trained with "the same training strategy, e.g., identical problem formulation, optimizer, number of iterations, batch size, and learning rate schedule." This is a controlled comparison for the core claim. The unfair-comparison weakness (above) is specific to the PoinTr/SeedFormer *reference numbers*, not the main controlled experiments.
- **Strength Finder's claim about PCN+con matching PoinTr being a standalone strength** — This strength is retained but caveated in the main review. It is not removed entirely but is weakened by the major weakness above.
- **Harsh Critic's demand to "retrain PoinTr and SeedFormer"** — Moved to Nice-to-Haves as a suggestion, not a fatal flaw. The paper's core contribution is still valid even without this comparison.
- **Speculative claim about "contradictory supervision signals when two views have very different input regions"** — This is a generic concern without specific evidence that it manifests in practice. Moved to Nice-to-Haves as a discussion suggestion.

## Novel Insights

The harsh critic's observation about the self-guided loss's gradient path through input-point correspondences across views is a genuinely novel technical insight not discussed in the paper. It identifies a concrete mechanism by which the self-guided loss could introduce noise: predicted missing points from view \(i\) are gradient-pushed toward the input points of view \(j\) (which are not the ground-truth missing region). This insight could motivate a cleaner variant where self-guided consistency is computed only on predicted missing points. The paper's ablation (small optimal α) is consistent with this analysis and hints that the community may benefit from such a refinement.

## Suggestions

1. **Fix the PoinTr/SeedFormer comparison.** Either retrain them under identical conditions (AdamW, cosine annealing, same epochs) and report the results, or explicitly retract the matching-SOTA claim and reposition the contribution as "improving networks under controlled conditions." The paper is strong enough without this overclaim.

2. **Add a brief discussion of the self-guided gradient issue.** Acknowledge that CD between predicted complete clouds includes input-point distances, and note that the optimal small α mitigates this. Optionally include a controlled ablation comparing self-guided on complete vs. missing-only predictions.

3. **Include an analysis of the number of views \(n\).** Even a simple experiment with \(n \in \{1,2,3,5\}\) would provide valuable practical guidance.

4. **Clarify the batching implementation** in the main text or supplement.
