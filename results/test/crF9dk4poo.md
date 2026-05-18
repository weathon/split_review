Now I have sufficient information to synthesize the final review. Let me write it.

## Summary

This paper proposes Interpretable Deep Clustering (IDC), a two-stage unsupervised framework for tabular (biomedical) data that provides both sample-level and cluster-level feature importance. In stage one, a gating network and autoencoder learn sample-specific sparse gates via self-supervised reconstruction. In stage two, a clustering head partitions the fixed embeddings using a per-cluster coding rate loss, while an auxiliary classifier learns a global gate matrix for cluster-level interpretability. Experiments on synthetic data (99.91% ACC), real-world biomedical tabular datasets, and image benchmarks demonstrate the method's ability to identify clusters using dramatically fewer features than competing approaches.

## Strengths

- **First unsupervised clustering method to jointly provide sample-level and cluster-level feature importance.** The two-gate design (local gates via self-supervised reconstruction, global gates via auxiliary classifier) is novel and fills a genuine gap in the literature. The synthetic data experiment (Section 6.2.1) provides clean validation: 99.91% clustering accuracy while identifying the correct per-cluster informative features with near-perfect F1, demonstrating that the framework can simultaneously cluster and select driving features.

- **Strong results on high-dimensional low-sample-size biomedical tabular data.** On six real-world tabular datasets (Table 6), IDC matches or outperforms K-means combined with feature selection methods (SRCFS, CAE, DUFS) while using only a tiny fraction of features — e.g., on the BIASE scRNA-seq dataset, improving accuracy from 32.8% (K-means) to 53.0% while identifying only 210 of 25,750 genes as relevant. These results directly support the paper's primary motivation.

- **Dramatic feature reduction without sacrificing clustering performance.** On MNIST60K, IDC uses ~16 features out of 784 while achieving 89.1% ACC (versus 83.3% without gates). On FashionMNIST, ~69 features suffice. This validates the core claim that the sparse gating mechanism can identify the truly informative subset of features for clustering.

- **Ablation study confirms the necessity of major loss components.** Table 5 shows that removing the gates total coding loss, sparse regularization, or denoising augmentation each degrades clustering ACC, supporting the design choices.

## Weaknesses

### Fatal
None.

### Major

- **The clustering objective (Eq. 6) is incompletely specified and the Figure 1 caption makes an unsupported claim.** Equation (6) defines ℒ_head as the sum of per-cluster coding rates, which makes each cluster more compact (an attractive/within-cluster force). The Figure 1 caption states "This loss is designed to push clusters apart while making each cluster more compact," but Eq. (6) contains no term that pushes clusters apart — it only compacts them. In the original MCR² (Yu et al., 2020), the repulsive force comes from subtracting the per-cluster coding rate from the *total* coding rate of all points. The paper acknowledges the existence of such a term ("In contrast to 7…") but does not include it in the optimized loss. The authors should either: (a) clarify why the fixed-K Gumbel-Softmax assignments and frozen embeddings make the repulsive term unnecessary, (b) provide theoretical or empirical evidence that the loss does not lead to collapsed or highly imbalanced clusters, or (c) adopt the full MCR² formulation. Currently, the reader cannot assess whether the clustering head is doing meaningful work or simply partitioning embeddings that were already separable from stage one. Reporting cluster-size distributions across runs would partially address this.

- **The uniqueness metric (Section 5) is conceptually ungrounded and unvalidated.** The metric rewards *different* explanations for *similar* samples (min over close pairs of the ratio of gate-distance to input-distance). The paper explicitly notes this is "opposite to the stability metric" in the supervised interpretability literature but does not justify why its opposite is desirable for unsupervised clustering. Within a cluster, similar samples should share the same driving features — otherwise the cluster-level interpretation becomes incoherent. The metric is also technically fragile: the min over all close pairs can be dominated by a single outlier, and a small denominator inflates the ratio arbitrarily. Unlike the faithfulness metric (which is validated via the monotonic accuracy-drop curve in Figure 3), uniqueness is reported as a bare number (0.69) with no validation against ground-truth feature importance. Since interpretability is a central contribution, this metric needs either strong justification or replacement with a validated alternative (e.g., sample-level precision/recall on the synthetic data, where ground-truth per-sample informative features are known).

### Minor

- **No empirical comparison to existing interpretable clustering methods.** The related work section cites Guan et al. (2011) and Frost et al. (2020) as prior interpretable clustering approaches, but the experiments compare only to post-hoc explanation methods (SHAP, Integrated Gradients, Gradient SHAP) applied to non-interpretable clustering. A direct comparison on tabular data — even on a subset of the six real datasets — would establish the advantage of the proposed approach over these baselines in terms of both accuracy and interpretability.

- **Two-stage training with frozen gates limits adaptability.** The gating network and encoder are trained on a reconstruction objective in stage one and frozen during clustering. Reconstruction-optimal features may not be clustering-optimal. An ablation that fine-tunes the gates jointly with the clustering head (or warm-starts from stage one and then unfreezes) would clarify whether this design choice is a limitation. The paper does not report such an experiment.

- **CIFAR10 results are overclaimed as "competitive."** The paper states results are "competitive" while the gap to dedicated vision methods (e.g., PICA at 81.0% ACC) appears to be very large (likely 30+ points). The paper does acknowledge it is "not designed for vision" and avoids domain-specific augmentations, which is fair, but calling a 30+ point gap "competitive" is misleading. The text should characterize these results as "moderate but expected given the method targets tabular data" rather than "competitive."

### Trivial

- The ablation study (Table 5) reports results from 10 runs but does not include standard deviations in the main text (they may be in the table image). Given that clustering results vary with initialization, including error bars would strengthen the claims.

## Nice-to-Haves

- On the synthetic data (Section 6.2.1), the paper currently reports cluster-level F1 for feature selection. Since per-sample ground-truth informative features are known for this data, reporting sample-level precision, recall, and F1 would directly validate the interpretability claim at the finest granularity.
- Comparing against VaDE or DEC on the tabular datasets (treating them as non-image deep clustering baselines) would broaden the empirical support.
- A simple analysis of cluster-size distributions (number of non-empty clusters, entropy of assignments) would empirically address the degeneracy concern about the clustering loss.

## Removed Points

- **Criticism about IDC's performance vs. DEC/IDEC/DCCS on MNIST/FashionMNIST (from Harsh Critic Point 3):** The reviewer compares methods operating on the full 784-dimensional space against IDC using ~16 features. The asymmetry favors the baselines, not the author's method. Per rule, this criticism is removed.
- **Claim that the loss "could push toward many tiny clusters" / "each point to its own cluster":** The Gumbel-Softmax produces assignments to exactly K clusters (K=10 in all experiments), making per-point singleton clusters impossible. This part of the criticism misunderstands the fixed-K constraint. The broader concern about no repulsive force is retained in Major Weaknesses above.
- **"90.1% on FashionMNIST" claim:** The paper's parsed text does not contain this number in a verifiable form (the table is an image); the reviewer's cited value does not match the contextual description (~69 features used). Removed as unverifiable from the extracted text.
- **Several generic strengths from the Strength Finder** (e.g., "comprehensive evaluation on both image benchmarks and biomedical data") are weakened to focus on the tabular data contribution, since the image results are relatively weak.

## Novel Insights

The key tension revealed by the reviews is between the paper's practical success (strong tabular results, clean synthetic validation) and its incomplete theoretical framing. The clustering objective is empirically sufficient but lacks the formal guarantees of the full MCR² formulation from which it derives. This suggests that for the tabular, low-sample-size regime the paper targets, the attractive (within-cluster) term alone may be adequate because the frozen embeddings from stage one already provide reasonable separation, and the fixed-K Gumbel-Softmax prevents degenerate partitions. If this is correct, it is a useful empirical finding worth stating explicitly. Conversely, the uniqueness metric appears to be a genuine conceptual misstep: in the unsupervised setting, sample-level interpretability is better validated by measuring whether the selected gates match ground-truth per-sample informative features (as the synthetic data allows) rather than by a formulatic opposite of stability.

## Suggestions

1. **Clarify the clustering objective.** Either justify why the within-cluster coding rate alone suffices (given fixed embeddings and fixed K), or incorporate a repulsive term. Provide empirical evidence of sensible cluster-size distributions.
2. **Validate or replace the uniqueness metric.** Use the synthetic data's per-sample ground-truth to compute sample-level precision/recall/F1 for gate selection. This directly measures what the paper claims (sample-specific feature importance) without relying on the conceptually problematic uniqueness definition.
3. **Add comparisons to Guan et al. (2011) and Frost et al. (2020)** on at least a subset of the tabular datasets to ground the claim of superiority over existing interpretable clustering methods.
4. **Adjust the characterization of CIFAR10 results** from "competitive" to something more measured (e.g., "moderate but expected for a method not designed for vision").
5. **Include standard deviations** for all multi-run experiments and report cluster-size distributions to demonstrate the loss does not produce degenerate assignments.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>