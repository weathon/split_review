Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes DIFAIR, a method for learning neural network representations where each dimension is explicitly associated with a specific class via anchored hyperspheres in the feature space. The approach extends Class Anchor Clustering (CAC) from logit space to feature space, allocating multiple dimensions per class and using a thresholded Euclidean loss to allow instances to spread within hyperspheres. The method is evaluated on Open-Set Recognition (OSR) benchmarks, and the representations are visually analyzed. The paper is notably transparent about a key failure mode: features within a class converge to nearly identical values rather than differentiating across dimensions, and OSR performance does not surpass strong baselines.

## Strengths

- **Novel anchoring in feature space with per-class multi-dimensional allocation**: DIFAIR anchors in the feature space (unlike CAC which anchors in logit space) and allocates $\mathcal{N}$ dimensions per class. This structural design is a genuine departure from prior anchoring methods, and Figure 3a demonstrates that the dimension-to-class mapping is clearly visible in the learned representations — unlike the entangled representations from cross-entropy training where features cannot be assigned to classes.

- **Hypersphere-based loss with explicit semantic tolerance**: The thresholded Euclidean loss (Eq. 2) stops penalizing when a representation is within radius $r$ of its anchor, deliberately allowing instances of the same class to spread inside the hypersphere and activate features associated with other classes. This design choice is explicitly motivated for semantic proximity (Section 3.3) and is a principled departure from CAC's hard clustering.

- **Honest diagnostic analysis of a key failure mode**: The paper goes beyond standard AUROC reporting by visualizing the learned representation structure (Figure 3a) and analyzing weight convergence (Figure 3b). This analysis reveals that DIFAIR's features are duplicated across dimensions within a class — weights converge to near-identical values per class group (std. dev. ~0.015 vs. ~0.15 across all weights). The paper explicitly identifies this as a failure, discusses it in Section 5.2, and suggests future directions. This level of post-hoc interpretability analysis of one's own method is valuable and rare.

- **Fair experimental comparison**: The paper re-implements CAC under the same training protocol (600 epochs, RandAugment, Vaze et al. splits), ensuring that performance differences are not artifacts of different training setups.

- **Insight about evaluation metric choice**: The paper tests both distance-to-anchor and Maximum Output Score (MOS), showing that MOS significantly improves DIFAIR's AUROC. This finding about metric suitability for anchored representations is useful for future work.

## Weaknesses

### Fatal
None. The paper's core claims are appropriately scoped (the title includes "Towards," the contributions list the loss function, OSR evaluation, and visualization/analysis as separate deliverables). The method does not fully succeed at its stated objective, but the paper is transparent about this limitation, and the contributions as listed are delivered.

### Major

- **The method does not produce differentiated features within a class — the central technical objective is unmet.** The paper's key design goal is to learn multiple *distinct* features per class, each expressed on a separate dimension. The paper's own analysis (Section 5) shows that instead, features of the same class are activated with close values and the corresponding convolution weights converge to near-zero standard deviation within each class group. The paper acknowledges this — "features of the same class are still activated with close values" — but this means the method fails at what it was designed to do. The paper presents this as an area for future improvement, but in its current form the loss function does not enforce intra-class feature diversity, and no mechanism (e.g., orthogonality or decorrelation regularization) is included to address this. This limits the paper's contribution to "we proposed an approach and diagnosed why it doesn't work as intended."

- **OSR performance does not support the claim that this representation benefits open-set detection.** The paper hypothesizes that class-associated, interpretable representations would improve OSR, but Table 1 shows that DIFAIR (even with MOS) underperforms or at best matches simpler baselines. As the paper itself discusses, "both CAC and DIFAIR exhibit lower AUROC scores compared to the MLS baseline." The trade-off between class separation and semantic proximity is acknowledged, but it effectively means the central hypothesis — that this representation would aid OSR — is unsupported by the experimental evidence. If the method does not yield competitive OSR performance *and* does not deliver differentiated features, the primary motivations for the approach are both undermined.

### Minor

- **The interpretability evaluation is thin.** The paper claims the representation is interpretable because each dimension is associated with a class, and Figure 3a does demonstrate this structural property. However, there is no evaluation of whether individual dimensions correspond to semantically coherent visual patterns. No human evaluation, no per-dimension activation maps, no analysis of whether dimensions reliably fire for specific visual concepts. The claim is about structural interpretability (dimension-to-class mapping), which is supported, but the reviewer's skepticism about the depth of the interpretability analysis is reasonable. Even a simple within-class vs. across-class variance analysis or mutual information with annotated concepts would strengthen the claim.

- **No hyperparameter sensitivity analysis.** The paper uses $\mathcal{N}=5, \alpha=10, r=0.4\times\sqrt{2\mathcal{N}\alpha^2}$ without any ablation study. Given that the feature duplication issue is central, it is important to know whether varying $\mathcal{N}$ (e.g., $\mathcal{N}=1$ or $\mathcal{N}=2$) changes the behavior. No exploration of the radius $r$ is provided despite it being a key parameter controlling the tolerance for cross-class feature activation.

- **No variance reporting or statistical significance.** Results are reported as averages over 5 splits but without standard deviations or confidence intervals. Given that performance differences between methods are often small, some results may be within the noise.

### Trivial
None.

## Nice-to-Haves

- A regularization term penalizing correlation or cosine similarity among dimensions within the same class group could directly address the feature duplication issue.
- Visual evidence (e.g., class activation maps per dimension) showing whether individual DIFAIR dimensions respond to distinct visual patterns would substantially strengthen the interpretability claim.
- An investigation into *why* the weights converge to near-identical values — is this an optimization artifact (symmetric initialization + symmetric loss)? Would breaking symmetry via random per-dimension filter initialization help?

## Removed Points

- **Criticism about the method's "failure" being presented as a weakness the paper already acknowledged**: The harsh critic's Critical Issue 1 is retained as a Major weakness because even though the paper is transparent about it, the fact remains that the method's central technical objective is unmet. Transparency is commendable but does not resolve the problem. However, the framing as "fatal" is softened to "major" because the paper's contributions include the diagnostic analysis itself.

- **Criticism about the method not being "verifiable" or "not yet released"**: Not present in the reviews; no action needed.

- **Formatting/style nitpicks**: None present in the reviews.

## Novel Insights

The key insight emerging from this review — and from the paper itself — is that *intra-class feature differentiation does not emerge automatically from a simple anchored-distance loss even when the representation space has spare dimensions*. The naive intuition that allocating $\mathcal{N}$ dimensions per class and optimizing with a thresholded Euclidean loss would cause each dimension to learn a distinct feature is false: the network converges to a degenerate solution where all $\mathcal{N}$ dimensions within a class encode essentially the same information. This is a useful negative result for the community, as it shows that anchoring methods need explicit diversity-promoting mechanisms. Additionally, the finding that Maximum Output Score (MOS) is a better OSR metric for this representation than raw distance-to-anchor highlights a mismatch between the training objective (distance-based) and the optimal evaluation strategy (magnitude-based), suggesting that future loss designs should consider the evaluation metric during training.

## Suggestions

1. **Reframe the paper's contribution more explicitly** around the diagnostic finding. Currently, the paper reads as a methods paper where the method partially fails. A stronger framing would position DIFAIR as an analysis framework for understanding what kinds of losses produce differentiated representations, with the negative result as a featured contribution rather than a limitation.

2. **Add a simple diversity-promoting term** to the loss (e.g., cosine-similarity penalty or orthogonality constraint among dimensions of the same class) to demonstrate whether the feature duplication issue is fundamentally architectural or can be resolved with better optimization. Even a proof-of-concept on a single dataset would significantly strengthen the paper.

3. **Include variance/std. dev.** for the main OSR results and at least one ablation (e.g., varying $\mathcal{N}$) to demonstrate robustness.

4. **Add per-dimension feature visualization** (e.g., activation maximization per filter or Grad-CAM per dimension) to move the interpretability claim beyond structural assignment toward semantic meaningfulness.

## Score and Decision

This paper proposes a well-motivated approach and is commendably honest about its limitations. The diagnostic analysis of feature duplication is a valuable contribution. However, the method does not achieve its primary technical objective (differentiated features within a class), the OSR results do not support the claimed benefits of the representation, and the interpretability evaluation is thin. The paper reads more as an exploratory analysis with an unsolved problem than as a paper that establishes a working new approach. In its present form, the paper does not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>