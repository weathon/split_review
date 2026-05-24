Now I have sufficient anchor context. Let me write the final consolidated review.

## Summary

This paper identifies a theoretical limitation of HiResCAM: its explanations are not uniquely determined because softmax is invariant to additive shifts of all logits, which propagates to a matrix-valued ambiguity in the spatial maps. The authors propose **ContrastiveCAMs** (class-vs-class difference maps) that are provably invariant to this shift, and use them to develop **Core-Focused Cross-Entropy (CFCE)**, a training loss that penalizes reliance on non-core image regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE dramatically shifts model reliance from spurious non-core features to core regions, validated by accuracy under core-region ablation, RFS, and downstream segmentation performance.

## Strengths

- **Clean theoretical identification of a genuine limitation in a widely-used interpretability method.** Theorem 3.2 proves that HiResCAM explanations admit an arbitrary matrix-valued shift $M$ with no change to the predicted probabilities, which is a formal demonstration that these maps can be arbitrarily misleading. Theorem 3.5 proves that ContrastiveCAMs are $M$-invariant, providing a principled fix.

- **ContrastiveCAMs provide strictly more information than standard CAMs.** The granular class-vs-class explanations (Definition 3.3) reveal which regions drive discrimination between specific pairs of classes — information that standard per-logit maps cannot surface. Proposition 4.1 shows a direct functional relationship between ContrastiveCAMs and softmax probabilities, which is a tighter connection than the logit-level relationship in Eq. (3).

- **Dramatic and consistent empirical evidence that CFCE shifts models away from non-core features.** On Hard-ImageNet (Table 2), accuracy under Gray Mask ablation drops from 75.94% (CE) to 41.78% (CFCE), and ContrastiveCAM IoU rises from 30.27% to 89.22%. RFS goes from negative (-0.23) to positive (0.224). These are large, consistent changes across multiple independent metrics.

- **The evidence does not rest on a single metric.** Core-region ablation (Gray Mask, BBOX, Tile) and RFS are fully independent of the ContrastiveCAM training procedure — they measure real-world reliance on core regions. The PASCAL VOC downstream segmentation experiment provides further validation that the learned features transfer to dense prediction tasks.

- **Demonstrated practical applicability with weak supervision.** Oxford-IIIT Pets results (Section 5.2) show that SAM auto-generated masks and even bounding boxes achieve competitive IoU (83.95% and 79.13% respectively on binary validation), lowering the barrier to using the method.

## Weaknesses

### Fatal

None.

### Major

None. The weaknesses below are genuine but do not invalidate the paper's core claims.

### Minor

- **The connection between Core-Constrained Risk Minimization (CCRM) and CFCE is heuristic.** Definition 4.4 imposes a hard constraint ($\sum_c \|(1-H)\odot\text{CAM}^{\text{Cntrst}}\| = 0$), while Definition 4.5 replaces it with an additive penalty ($+\sum (1-H)\odot|\text{CAM}^{\text{Cntrst}}|$). Theorem 4.6 claims consistency between the two risks, but the proof is deferred to the appendix. The main text does not derive CFCE as a Lagrangian relaxation or formally establish that minimizing CFCE enforces the CCRM constraint. This weakens the claimed theoretical grounding of the central methodological contribution. A sketch of the proof or a more explicit statement about the nature of the connection (e.g., "CFCE is a proxy that approximates CCRM in practice, as validated by our experiments") would strengthen the paper.

- **ContrastiveCAM IoU is a partially circular validation metric for CFCE-trained models.** CFCE and its KL-regularized variant explicitly optimize a function of ContrastiveCAM maps, so measuring ContrastiveCAM IoU for these models is partly checking whether the optimization succeeded rather than providing independent evidence of alignment. The paper does not acknowledge this circularity. The concern is mitigated because the paper's strongest evidence comes from *independent* metrics (core-region ablation accuracy, RFS), and GradCAM IoU (a different explanation method) is also reported. The paper should explicitly center the ablation/RFS results and treat ContrastiveCAM IoU as a sanity check.

- **The accuracy–alignment trade-off is acknowledged but not discussed.** On Hard-ImageNet, unablated accuracy drops from 94.25% (CE) to 90.35% (CFCE+KL) — roughly 4% absolute. The caption of Table 2 notes "at the cost of some un-ablated performance," but there is no discussion of when this trade-off is acceptable, how it varies across datasets, or whether it can be mitigated (e.g., by tuning the CFCE weighting). For practitioners deciding whether to adopt the method, this is important context.

- **Computational overhead of computing ContrastiveCAMs during training is not reported.** Computing $\text{CAM}^{\text{Cntrst}}$ requires gradients of each logit w.r.t. feature maps, which adds a backward pass per class pair in a naive implementation. Training time, FLOPs overhead, or any description of an efficient implementation is absent. This is a practical concern for scalability.

- **No limitations section.** The paper would benefit from a paragraph explicitly discussing: (a) reliance on core-region masks (though approximate masks are shown to work), (b) the accuracy trade-off noted above, (c) computational cost, and (d) that the theoretical analysis assumes a single-layer linear classifier $h$ (Eq. 1).

### Trivial

None.

## Nice-to-Haves

- **A saliency-based regularization baseline** (e.g., penalizing Gradient×Input or GradCAM on non-core regions) would help isolate whether the benefit is specific to ContrastiveCAM or achievable with any attribution map during training.
- **Ablation of loss components** — the paper presents CFCE and CFCE+KL but does not ablate the core-focus term vs. the KL term individually to quantify each component's contribution.
- **Statistical significance tests** on key comparisons (e.g., pairwise t-tests on ablation accuracy) would increase confidence given the reported variability in some metrics.

## Removed Points

- The harsh critic's claim that the softmax-invariance issue is not unique to HiResCAM is partially correct, but the paper already traces the root cause to softmax (Proposition 3.1) and frames the result as a limitation of HiResCAM maps specifically — which is accurate, since it is HiResCAM explanations that inherit the ambiguity. This is not a genuine weakness.
- Criticism about "CE w/ Arch" baseline description being in the appendix — the appendix is removed by the parser, so this cannot be evaluated as a weakness of the submission.
- Criticism about Theorem 4.6's proof being in the appendix — standard practice; the parser strips appendices.
- Several strength-finder claims that were generic or sycophantic (e.g., "the paper addressed an important problem") have been omitted.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a sketch of Theorem 4.6's proof in the main text, or explicitly reframe CFCE as a heuristic penalty with empirical justification rather than a theoretically-derived constraint.
2. Add a paragraph explicitly acknowledging the circularity of ContrastiveCAM IoU and clarifying that the core-region ablation and RFS metrics are the primary evidence for feature alignment.
3. Discuss the accuracy–alignment trade-off explicitly — e.g., with a small table or plot showing unablated accuracy vs. ablation accuracy across methods, and a brief discussion of when the trade-off is worthwhile.
4. Report training-time overhead (e.g., wall-clock time per epoch) for the CFCE variants.
5. Add a "Limitations" subsection — even a few sentences addressing mask dependency, accuracy trade-off, computational cost, and the single-layer classifier assumption.

## Score and Decision

**Bracket determination (Round 1):** Calibration search over three bands: weak (scores < 3.5), middle (3.5–7.5), strong (> 7.5). The paper is clearly above the weak band (scores 2.5–3.4 in that band belong to papers with incoherent or trivial contributions) and clearly below the strong 8+ band (major theoretical breakthroughs or SOTA results). Initial bracket: **4.5–6.5**.

**Narrowing (Round 2):** Searched anchors in the 4.5–6.5 and 5.5–7.5 ranges for topically similar papers.

| Anchor | Avg Score | Round | Comparison to paper under review |
|--------|-----------|-------|----------------------------------|
| Non-negative Contrastive Learning (NCL) | 5.75 | R2 | Accepted. Similar theoretical contribution (NMF connection). Weaker experiments (CIFAR-10/100, ImageNet-100) and smaller improvements. Paper under review has stronger empirical results. |
| INTR (Interpretable Transformer) | 6.00 | R2 | Accepted. Clever idea but mostly qualitative evaluation. Paper under review has stronger quantitative evidence but less novelty in architectural design. |
| Monosemanticity & Robustness | 5.80 | R2 | Accepted. Good range of experiments but concerns about monosemanticity measurement. Similar maturity. |
| Causal Alignment (medical) | 6.00 | R2 | Accepted. Domain-specific application, solid experiments. Comparable rigor. |
| R3-ProtoPNet | 5.75 | R2 | Rejected. Despite decent votes, the limited evaluation (one dataset) and hand-crafted nature held it back. Paper under review has broader evaluation. |
| Improving ProtoPNets with RLHF | 5.75 | R2 | Rejected — limited to CUB-200 only. |

The paper under review compares favorably to the 5.75–6.00 anchors: its theoretical contribution is cleaner than most, its experiments span three datasets with independent metrics, and the downstream transfer result adds conviction. The main weaknesses (heuristic CFCE derivation, circularity in one metric, unreported computational cost, accuracy trade-off not discussed) are real but do not undermine the core contribution. The paper sits at or slightly above the typical 5.75 anchor.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>