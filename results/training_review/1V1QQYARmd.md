Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes an unsupervised OOD detection method that uses the $k$-NN radius on intermediate neural network embeddings, normalized by the expected in-distribution $k$-NN radius and aggregated across layers. The key insight is that training the classifier with label smoothing improves separability between ID and OOD points in embedding space (the "Label Smoothed Embedding Hypothesis"). The paper provides finite-sample theoretical guarantees for $k$-NN based OOD detection (Theorems 1, 2, Corollary 1) and a proposition modeling why label smoothing helps, along with empirical validation on several benchmark datasets.

## Strengths

- **Label smoothing consistently improves $k$-NN OOD detection across diverse settings.** Table 1 shows ROC-AUC improvements in 14 of 15 dataset pairings when label smoothing ($\alpha=0.1$) is applied, often by large margins (e.g., Fashion MNIST → SVHN: 0.959 vs. 0.887). The ablation on $\alpha$ (Figure 2, right) confirms the pattern across four dataset pairs, and Table 2 shows per-layer improvement.

- **The method outperforms strong baselines including POEM, despite POEM's unfair advantage.** POEM has access to an outlier pool that overlaps with the test OOD distribution (the paper explicitly acknowledges this). The proposed method still achieves higher ROC-AUC on 11 of 15 pairings, with large margins in several cases (e.g., MNIST → EMNIST Digits: 0.999 vs. 0.599).

- **Simple, practical, and fully unsupervised.** The method uses Euclidean distance with $k=1$ as default, aggregates over a few layers, and requires no OOD validation data for tuning. The ablations confirm robustness to hyperparameter choices, making the method easy to deploy.

- **Ablation studies provide useful practical guidance.** The impact of $k$ (Figure 2, left), $\alpha$ (Figure 2, right), and layer selection (Table 2) are systematically studied. The consistent outperformance of $k$-NN over SVM and Isolation Forest on the same embeddings (Table 1) isolates the value of the $k$-NN density estimator itself.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-method disconnect.** Theorems 1 and 2 and Corollary 1 derive finite-sample guarantees under the assumption that data are drawn i.i.d. from a density $f$ on a compact subset of $\mathbb{R}^d$. However, the proposed method operates on *learned neural network embeddings* — deterministic, data-dependent transformations of the input — for which the i.i.d. density assumption is not justified. Proposition 1 does directly address the label smoothing mechanism, but under an idealized contraction mapping $\phi$ whose correspondence to actual label smoothing is asserted rather than derived or empirically verified. The theoretical results thus provide general motivation for $k$-NN-based OOD detection but do not specifically support the method as implemented. The paper's claim that it offers "new theoretical insights into the use of $k$-NN for OOD detection" (Section 5) is partially accurate — the results *are* novel for the OOD context — but the gap between the theory's assumptions and the method's actual operating regime is a significant limitation that the paper does not adequately address.

2. **Missing standard baselines.** The evaluation omits several widely-used deep OOD detection methods that are standard in recent literature — most notably Mahalanobis distance (Lee et al., 2018), Energy-based OOD (Liu et al., 2020), and DICE (Sun & Li, 2022). The paper includes DeConf (which improves ODIN) and POEM (state-of-the-art), but without these additional baselines, it is difficult to contextualize the method's performance within the full landscape of OOD detectors. This is partially mitigated by the ablative baselines (SVM, Isolation Forest, Robust $k$-NN on the same embeddings) which control for the representation, but the missing modern baselines remain a gap.

### Minor

3. **$k=1$ contradicts the theoretical framing.** The method uses $k=1$ and the ablation (Figure 2) shows performance degrades with larger $k$. However, Theorem 1 requires $k \geq 2^8 \cdot \log(2/\delta)^2 \cdot d \log n$, which is incompatible with $k=1$. Density estimation theory typically predicts variance reduction with larger $k$, but here larger $k$ hurts performance. This suggests the method is not performing density estimation but rather using a nearest-neighbor distance as an outlier score. The paper should acknowledge this and explain why $k=1$ (a non-consistent density estimator) works best for this particular application.

4. **Distance metric not controlled in Robust $k$-NN comparison.** Robust $k$-NN uses cosine similarity (as in the original paper) while the proposed method uses Euclidean distance. The performance difference could partially reflect metric choice rather than the methodological distinction (label distribution vs. distance-based scoring). An ablation controlling the distance metric would strengthen the comparison.

5. **Limited scale of evaluation.** Experiments are conducted on relatively small-scale datasets (MNIST, Fashion MNIST, SVHN, CIFAR-10, CelebA) with simple architectures (3-layer DNN, LeNet-5). It is unclear whether the findings generalize to larger-scale settings (e.g., ImageNet-1K with ResNet or WideResNet backbones) that are now standard in OOD detection research. The paper uses ImageNet-32 as an *OOD* source but not as in-distribution.

6. **DeConf underperformance not fully explained.** The paper reports that tuning DeConf's $\epsilon$ never helped and that DeConf underperformed the simple softmax control. Without further analysis (e.g., showing that the method was implemented correctly), it is unclear whether this reflects a genuine limitation of DeConf in these settings or a mismatch in implementation/hyperparameters.

### Trivial

7. **Framing imprecision about softmax avoidance.** The paper claims to "avoid using the softmax probabilities altogether" (Section 1), but the classifier is trained with label smoothing (which uses a softmax). The method avoids using softmax *outputs* for the OOD score, not softmax entirely. The distinction is minor and the method's actual approach is clear from context.

## Nice-to-Haves

- **Quantitative clusterability analysis**: Silhouette scores, intra-class vs. inter-class distances, or separation measures on embeddings with and without label smoothing would directly test the Label Smoothed Embedding Hypothesis beyond the single histogram pair in Figure 1.
- **Ablation on distance metric** (Euclidean vs. cosine) to isolate the method's advantage over Robust $k$-NN.
- **Embedding visualizations** (t-SNE/UMAP) across multiple dataset pairs to visually confirm improved separability.

## Removed Points

These points were flagged in the input reviews but removed per the synthesis rules:

- **POEM unfair advantage as a weakness**: The asymmetry favors the baseline (POEM has access to an outlier pool), not the author's method. Per instructions, this asymmetry strengthens the paper's case. The paper explicitly acknowledges the advantage.
- **Standard error reporting format**: The summary statistics for standard errors across 15+ table entries is standard practice and not a genuine weakness.
- **"Theoretical results are just re-derivations from Dasgupta & Kpotufe (2014)"**: The paper acknowledges using similar techniques and correctly identifies the novel contribution as applying these to OOD detection with finite-sample guarantees — a different application domain from the original mode estimation.
- **Missing appendix / proof details**: These are parser artifacts; the original submission contains them.
- **Formatting/style nitpicks**: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the core empirical finding (label smoothing improves $k$-NN OOD detection on intermediate embeddings) but do not surface unexpected patterns or reconciliations beyond what the paper reports. The main insight from the synthesis is that the theoretical apparatus (Theorems 1-2) and the practical method ($k=1$ on learned embeddings) are more loosely coupled than the paper suggests — but this is a critique, not a novel discovery.

## Suggestions

1. **Bridge the theory-method gap** by either (a) explicitly stating that the theory addresses $k$-NN OOD detection in the original data space as general motivation, while the embedding case is a separate empirical contribution, or (b) deriving or citing guarantees for $k$-NN on transformed/pushforward distributions.
2. **Add standard modern baselines** (Mahalanobis distance, Energy-based OOD, DICE) to the main comparison table.
3. **Reframe $k=1$** honestly as a nearest-neighbor distance score rather than density estimation, and discuss why this works well for OOD detection despite not being a consistent density estimator.
4. **Control for distance metric** in the Robust $k$-NN comparison (e.g., run Robust $k$-NN with both cosine and Euclidean distance).
5. **Evaluate on at least one larger-scale benchmark** (e.g., CIFAR-100 or Tiny ImageNet as ID with a ResNet backbone) to assess scalability.
6. **Add quantitative clusterability metrics** (silhouette score, intra/inter-class distance ratios) to directly validate the Label Smoothed Embedding Hypothesis.

## Score and Decision

The paper presents a simple, practical OOD detection method with clear empirical support for the core claim that label smoothing improves $k$-NN-based OOD detection on intermediate embeddings. The ablations are well-designed and the method outperforms several baselines, including a state-of-the-art method (POEM) that operates under favorable conditions. However, the paper's weaknesses — particularly the disconnect between the theoretical results (which assume i.i.d. data in the original space) and the actual method (which uses $k=1$ on learned embeddings), the omission of several standard baselines, and the moderate evaluation scale — are substantive. The paper has real contributions but is not yet as strong as it could be. The method itself is valuable and the empirical findings are credible, making this a borderline acceptance at a mid-tier venue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>