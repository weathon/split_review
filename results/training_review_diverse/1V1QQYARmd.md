Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the consolidated review.

---

## Summary

This paper proposes an unsupervised OOD detection method that computes the $k$-NN radius of a test point relative to training embeddings at multiple intermediate layers of a neural network, normalized and aggregated into a single score. The authors show that training the network with label smoothing contracts in-distribution embeddings more than OOD embeddings (the Label Smoothed Embedding Hypothesis), which amplifies the separation in $k$-NN radii. They provide finite-sample high-probability theoretical guarantees (Theorems 1–2, Proposition 1) and demonstrate strong empirical results across nine dataset pairings, outperforming several baselines including Robust Deep $k$-NN, DeConf, one-class SVM, Isolation Forest, and POEM.

## Strengths

- **Novel combination of $k$-NN density on embeddings with label smoothing.** The paper introduces the Label Smoothed Embedding Hypothesis as a principled motivation for why label smoothing improves $k$-NN-based OOD detection, and demonstrates this effect empirically (Figure 1, Table 1). Using only the $k$-NN radius (distance) rather than neighbor label distributions makes the method unsupervised and applicable even when label information is unreliable.

- **Finite-sample high-probability guarantees for $k$-NN OOD detection.** Theorems 1 and Corollary 1 provide uniform bounds on recall and precision for identifying OOD examples using the $k$-NN radius. Theorem 2 shows that the $k$-NN radius approximately preserves the ranking by true density when density gaps are large enough. These go beyond prior asymptotic $k$-NN analyses by being tailored to the OOD setting.

- **Strong empirical performance across diverse benchmarks.** In Table 1, the proposed $k$-NN($\alpha$) method with label smoothing achieves the most bolded entries (within two standard errors of the max) across nine dataset pairings, including against POEM which is given an unfair outlier-pool advantage. The improvement is consistent across MNIST, Fashion MNIST, SVHN, CIFAR10, and CelebA.

- **Informative ablation studies.** The paper systematically studies the impact of $k$ (Figure 2, left), label smoothing amount $\alpha$ (Figure 2, right), and choice of intermediate layer (Table 2). The results provide practical guidance ($k=1$, $\alpha=0.1$ as reasonable defaults) and show that the method is robust to these hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major

- **The embeddings used for SVM and Isolation Forest baselines are not disclosed.** The paper describes SVM and IF as ablative models that "leverage the same intermediate layer representations as our method" (Section 4.3), but Table 1 reports only single columns for SVM/IF while $k$-NN has two columns ($\alpha=0$ and $\alpha=0.1$). It is never stated whether SVM/IF were evaluated on embeddings from the standard model ($\alpha=0$) or the label-smoothed model ($\alpha=0.1$). If they used $\alpha=0$ embeddings, the comparison between $k$-NN($\alpha=0.1$) and SVM/IF conflates the choice of detector with the choice of training regime. This does not invalidate the paper's core claim (the method works well), but it undermines the specific argument that "$k$-NN consistently outperforms them" as an apples-to-apples comparison. The authors should clarify which embeddings were used and, ideally, run SVM/IF on both $\alpha=0$ and $\alpha=0.1$ embeddings in a $2\times3$ design.

### Minor

- **Proposition 1 provides theoretical intuition, not a rigorous derivation from label smoothing.** The proposition assumes a specific contraction mapping $\phi$ with faster contraction for in-distribution points than for OOD points, but it does not argue that label smoothing training actually produces this particular mapping. The paper acknowledges this is "theoretical intuition" (Section 3.3), but the gap between the assumed transformation and what label smoothing actually does to embeddings limits the proposition's force as a theoretical justification.

- **Uniform averaging across layers is presented without justification.** The aggregation $\hat{T}(x) = (1/M)\sum_i \hat{T}_i(x)$ averages normalized $k$-NN radii uniformly. No discussion is given of why equal weights are appropriate or whether a learned or heuristic weighting scheme (e.g., emphasizing deeper layers) would improve performance.

- **Theory is stated for the data space, but the method operates on embedding spaces.** Assumptions 1 (Hölder continuity) and 2 (boundary smoothness) are stated for the density $f$ on $\mathbb{R}^d$. The paper does not discuss whether these properties are plausibly inherited by the embedding spaces of neural networks, leaving a gap between the theoretical guarantees and the practical setting.

- **Layer ablation (Table 2) is limited to two datasets.** The study of which single layer works best covers only Fashion MNIST and CelebA. While not a fatal omission, the conclusions about layer choice would be stronger with additional datasets.

### Trivial

- **Figure reference mismatch.** The text in Section 2 (line 70) refers to "Figure 2" when describing the distribution of 1-NN distances, but the first figure in the paper is labeled Figure 1. The reference should be to Figure 1.

## Nice-to-Haves

- **Add modern embedding-based OOD baselines.** Methods such as Mahalanobis distance (Lee et al., 2018) and energy-based detection (Liu et al., 2020) operate on intermediate representations and are natural competitors. Including them would strengthen the positioning against the state of the art, even if the proposed method remains competitive.

- **Provide more direct quantitative evidence for the embedding contraction hypothesis.** The current evidence is the 1-NN radius histograms (Figure 1). Additional metrics such as within-class vs. between-class average distances, silhouette scores, or the ratio of ID-to-OOD radii before and after label smoothing would more directly validate the claimed mechanism.

- **Discuss computational complexity at test time.** Computing the $k$-NN radius requires distances to all training embeddings, which could be prohibitive for large training sets. The paper notes that $k=1$ enables efficient index structures, but a brief analysis of runtime vs. training set size would help practitioners assess scalability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"inf" in Definition 1 (likely "inf")**: The notation $\operatorname*{inf}$ (infimum) is standard and correct in mathematical writing. This is a reviewer confusion with LaTeX markup, not a paper error.
- **"flipping" misspelled as "filpping"**: Per policy, typographical/orthographic artifacts (parser issues or minor copy-editing misses) are removed from consideration.
- **Missing appendix, proofs, or references**: The parser strips these sections; they exist in the original submission.
- **Demand for additional related work coverage**: Per policy, missing related works are not flagged since external verification is not possible.
- **General reproducibility nitpicks (e.g., undisclosed hyperparameters)**: The experimental setup is sufficiently described; remaining implementation details are standard.

## Novel Insights

The reviewers' analyses converge on the core empirical contribution (label smoothing + $k$-NN density works well) but diverge on severity. The harsh critic's most substantial point — the uncontrolled SVM/IF comparison — is genuine but fixable and does not threaten the paper's central result, since the key claim (label smoothing improves $k$-NN OOD detection) is supported by the within-method comparison (k-NN(0) vs k-NN(0.1)) and the ablation studies. The Strength Finder correctly identifies the theoretical guarantees (Theorems 1–2) as a meaningful contribution beyond prior asymptotic analyses. The most interesting tension between the reviews is whether Proposition 1 adds value: the harsh critic sees it as an unmotivated assumption, while the Strength Finder sees it as a formalization of the hypothesis. The paper's own hedging language ("theoretical intuition") suggests the truth is somewhere in between — it is a useful conceptual illustration but not a rigorous proof.

## Suggestions

1. **Clarify the SVM/IF embedding source immediately.** Add a sentence in Section 4.2 or 4.3 stating explicitly which model's embeddings (α=0, α=0.1, or both) were used for each baseline. Ideally, rerun SVM/IF on both sets of embeddings and report a full 2×3 comparison.
2. **Add a brief justification for uniform layer averaging**, or at minimum acknowledge that alternative weighting schemes are possible and note this as future work.
3. **Discuss the data-space-to-embedding-space gap** in the theory section, noting that the theoretical results apply to the feature space under the stated assumptions and that the method inherits these properties if the embedding space approximately preserves the relevant structure.

## Score and Decision

The paper makes a genuine contribution: a simple, well-motivated OOD detection method with both theoretical guarantees and strong empirical results. The main unresolved weakness — ambiguity about which embeddings were used for SVM/IF baselines — is a presentation gap that can be addressed in a minor revision and does not affect the paper's strongest contribution (label smoothing improves $k$-NN OOD detection, validated by the within-method comparison and ablations). The paper would benefit from additional modern baselines and a tighter connection between theory and practice, but these are enhancements, not structural flaws.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>