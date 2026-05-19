- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
I now have a solid understanding of the paper and all reviewer claims. Let me compose the final review.

## Summary

The paper proposes GPS-SSL (Guided Positive Sampling), a method that replaces standard data-augmentation-based positive pair generation in Self-Supervised Learning (SSL) with nearest-neighbor sampling from a separately designed embedding space $g_\gamma$. Any pretrained model (supervised, CLIP, VAE, MAE) can serve as $g_\gamma$. GPS can be applied off-the-shelf to any SSL method (SimCLR, BYOL, VICReg, NNCLR). The central claim is that GPS reduces SSL's reliance on carefully handcrafted data augmentations by shifting the burden to designing informative embedding spaces instead. Experiments on CIFAR-10, Aircrafts, PathMNIST, TissueMNIST, and a Hotel-ID dataset show significant improvements, especially under weak augmentations (e.g., 85.58% vs. 37.51% linear probing on CIFAR-10).

## Strengths

1. **Dramatic improvement under weak augmentations substantiates the core claim.** On CIFAR-10 with only random horizontal flip, GPS-SimCLR achieves 85.58% linear probing accuracy versus 37.51% for baseline SimCLR (Table 2 / abstract). This directly validates the claim that GPS reduces DA dependency.

2. **Generality across SSL frameworks and datasets.** GPS is applied to four distinct SSL methods (SimCLR, BYOL, VICReg, NNCLR) and evaluated on five datasets from different domains (natural images, fine-grained aircraft, medical images, hotel photos). All four methods improve when augmented with GPS, especially on under-studied datasets. This demonstrates GPS is not tied to a single SSL family.

3. **Theoretical grounding that subsumes prior methods.** Proposition 1 formally shows that GPS recovers standard SSL (when $g_\gamma$ is a bijection and $\tau\to 0$), input-space nearest neighbors, and NNCLR as special cases by tuning $(g_\gamma, \tau)$. This provides a principled unification and makes explicit how GPS extends existing positive sampling strategies. (Verified: the proposition is correct—$DA(x)$ is a stochastic operator per line 90, so $(DA(x),DA(x))$ in the $\tau\to0$ limiting case recovers standard SSL pairs, not a degenerate same-augmentation pair.)

4. **Ablation isolating the source of improvement.** The paper compares SSL and GPS training when both start from the *same* pretrained weights (supervised ImageNet or CLIP; Table 5). GPS still outperforms (e.g., on Aircrafts from CLIP initialization: 63.74% vs. 57.70%). This controls for the confound that GPS's gain might come solely from a stronger backbone initialization.

5. **Robustness to hyperparameter changes.** When the learning rate is varied across three orders of magnitude (0.1, 0.3, 1.0), GPS-SimCLR maintains top-1 accuracy within a ~2.3% range on CIFAR-10 (86.05–88.35%), while baseline SimCLR drops from 90.73% to 83.57% (Table 4). This is a practically useful property.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric comparison between GPS and baselines in the main experimental setup.** In the primary results (Table 2), GPS methods use a pretrained embedding $g_\gamma$ (e.g., supervised ResNet-50, CLIP) as a source of nearest-neighbor positive pairs, while baseline SSL methods have no access to this external signal. This makes it difficult to determine how much of the gain comes from the nearest-neighbor *mechanism* vs. simply having additional semantic information. The paper partially addresses this with an ablation (Table 5) where both GPS and baselines start from the same pretrained weights—and GPS still wins—but a stronger control would give baselines access to $g_\gamma$ in some other form (e.g., as a regularizer or feature extractor for clustering). Without such a control, the exact source of improvement is not fully isolated. This does not invalidate the paper's core contribution (the GPS mechanism itself is the contribution), but it weakens the ability to make mechanistic claims about *why* GPS works.

2. **No statistical reporting of variance.** All main results (Table 2, Table 3) are reported as single numbers with no standard deviations, confidence intervals, or number of seeds. The learning-rate ablation reports "best performance" across a sweep, which masks variance. Since some improvements under strong augmentations are modest (e.g., TissueMNIST: 75.60% vs. 71.10% for GPS-BYOL vs. BYOL), the reader cannot assess whether these differences are reliable. This is the most significant evidential gap in the paper. The dramatic weak-augmentation improvements are unlikely to be overturned by variance, but the paper should still follow standard practices.

### Minor

1. **Design choice of furthest-neighbor selection is not motivated or ablated.** GPS selects the *furthest* point within the $\tau$-ball (Equation 3 argmax), which is an unusual design compared to the more intuitive nearest or random selection. The paper provides no motivation for this choice and does not ablate it against alternatives. This is a methodological gap worth addressing.

2. **The role of $\tau$ is not discussed or ablated.** The neighborhood radius $\tau$ controls the size of the candidate set for positive sampling and is thus a key hyperparameter, yet the paper does not discuss how it is set, whether it is dataset-dependent, or how sensitive results are to it.

3. **Theorem 1 relies on strong assumptions acknowledged by the authors but still undersells its practical scope.** The theorem requires $g_\gamma$ to be invariant to the target DA and that every augmented view appears separately in the dataset (Equation 8). The authors honestly note this is "quite impractical," which limits the theorem's role from an actionable guarantee to a conceptual motivating statement. This is fine for a motivation but should be presented as such.

### Trivial
None.

## Nice-to-Haves
- Adding a control experiment where baseline SSL methods also receive the $g_\gamma$ embeddings in some non-NN form (e.g., as a regularization term or as targets for a distillation loss) to fully isolate the contribution of the NN-sampling mechanism.
- An ablation of $\tau$ values and nearest-vs-random-vs-furthest neighbor selection within the ball.
- Results on a larger-scale dataset (e.g., ImageNet-100 or DomainNet) to demonstrate scalability, though the paper's focus on under-studied domains makes this optional.
- Brief runtime comparison in tabular form (seconds/epoch) rather than just a qualitative claim.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that Proposition 1(ii) is wrong ("degenerate, does not recover standard SSL").** The paper explicitly states (line 90) that "the DA operator includes the random realisation of the DA." Thus $(DA(x), DA(x))$ in the $\tau\to0$ case produces two different stochastic augmentations of $x$, which is exactly standard SSL (Equation 2). The critic's interpretation that this produces the same augmented image twice is factually incorrect. **REMOVED.**

- **Harsh Critic's suggestion that 37.51% on CIFAR-10 is cherry-picked / needs more context in the abstract.** The paper specifies the weak augmentation set (random horizontal flip only, line 135) and references the relevant table. The 37.51% figure is for SimCLR with this minimal augmentation, which is entirely plausible. The abstract appropriately flags a striking result and directs to the main text for details. **REMOVED.**

- **Strength Finder's "dramatic improvement under weak augmentations" conflicts with Harsh Critic's "cherry-picked" framing.** The weakness is removed; the strength remains as it is factually supported. **No conflict.**

- **Harsh Critic's criticism that Theorem 1 assumptions are too strong.** The paper transparently acknowledges the impracticality ("That result is quite impractical as designing such a mapping $g_\gamma$ may prove as arduous as design its underlying DA, but nevertheless provides a great motivation"). This is a conceptual motivation, not a claimed practical result. Downgraded to Minor. **MOVED to Minor.**

- **Harsh Critic's point about missing discussion of other SSL methods that use external knowledge (SWAV prototypes, ReSSL).** The reviewer cannot verify missing related work without external sources. Per instructions, this is removed. **REMOVED.**

## Novel Insights

The reviews together surface a productive tension: the paper's central appeal—moving the design burden from DA to embedding spaces—is both its strength and the root of its evaluation challenge. The harsh critic correctly identifies that the main experiments confound the GPS mechanism with the additional information channel it opens. However, the paper's own ablation (same-initialization comparison) partially addresses this, and the "unfairness" is inherent to the contribution: GPS *is* a mechanism for injecting prior knowledge. The more interesting question, not fully resolved by either review, is whether the specific nearest-neighbor-in-a-fixed-embedding-space mechanism has unique advantages over simpler alternatives (e.g., using $g_\gamma$ to compute a regularizing loss term on top of standard SSL). None beyond the paper's own contributions.

## Suggestions

1. Report means and standard deviations over at least 3 random seeds for all main tables. For the learning-rate ablation, report mean performance across the sweep rather than best-only.
2. Add an ablation comparing furthest-neighbor selection against nearest-neighbor and random selection within the $\tau$-ball.
3. Discuss how $\tau$ is chosen in practice and include a sensitivity analysis.
4. Consider a control where the baseline SSL method receives $g_\gamma$ information through a different mechanism (e.g., a feature-matching regularizer) to further isolate the effect of the NN-sampling mechanism.
