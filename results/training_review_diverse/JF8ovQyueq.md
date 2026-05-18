Now I have all I need. Let me produce the final consolidated review.

## Summary

FedGWC proposes a clustered federated learning method that groups clients by computing Gaussian rewards from their empirical loss values, then builds an interaction matrix and uses spectral clustering recursively to form homogeneous client clusters. The method can be integrated with any FL aggregation algorithm (FedAvg, FedProx, pFedMe, etc.) and automatically determines the number of clusters via a convergence check and Davies-Bouldin threshold. The paper also introduces a "Wasserstein Adjusted Metric" for evaluating cluster cohesion under class imbalance.

## Strengths

- **Loss-based clustering without model updates.** FedGWC groups clients using only empirical losses transformed via Gaussian rewards, avoiding the hyperparameter sensitivity of gradient-norm based methods like CFL. This is well-motivated and explicitly contrasted with prior work (Section 3.2, Section 4.1).

- **Orthogonal integration with any FL aggregation method.** The paper demonstrates that FedGWC improves balanced accuracy when layered on top of FedAvg, FedAvgM, FedProx, pFedMe, and Per-FedAvg (citing >10% improvement on Cifar100). This orthogonal design — clustering as a drop-in layer — is a clean architectural choice that the paper validates across six different algorithms.

- **Automatic determination of cluster number.** FedGWC uses an MSE convergence threshold on the interaction matrix combined with a Davies-Bouldin score to decide when to split clusters recursively, avoiding the need to pre-specify the number of clusters (unlike FeSEM, IFCA, and Multi-Center FL). The paper explicitly compares with CFL's hyperparameter sensitivity and shows FedGWC produces reasonable cluster counts.

## Weaknesses

### Fatal
None.

### Major

1. **Unjustified stationarity assumption undermines the convergence theory.** The paper claims (Section 3.2, Eq. 1) that the rewards \(R_k^{t,s}\) are "stationary by construction" so that "their moments do not depend on the iteration" and "\(\mu_k\) does not depend on \(t\)." This is asserted without proof or justification. The loss \(L_k^{t,s} = \mathcal{L}_k(\theta_k^{t,s})\) depends on model parameters \(\theta_k^{t,s}\), which are updated each round as training progresses; the sample mean \(\hat{\mu}^{t,s}\) and variance \(\hat{\sigma}^{t,s}\) also evolve. There is no argument given for why the Gaussian transformation would render these quantities stationary. The Robbins-Monro update in Eq. 2 requires unbiased observations of a *fixed* target; if the target \(\mu_k\) is time-varying, the claimed convergence \(\Gamma_k^t \to \mu_k\) in Theorems 3.1 and 3.2 (and the extension to \(P_{kj}^t\)) is not supported. **Why this matters**: The paper presents these theorems as part of a "comprehensive mathematical framework" and "rigorous analytical examination" (Section 1), but the central assumption of the convergence analysis is unsubstantiated. This does not invalidate the empirical method *per se*, but it means the theoretical guarantees claimed do not hold as stated, and the framing as a rigorous theoretical contribution is misleading.

### Minor

2. **Affinity matrix construction is intuitive but not rigorously justified.** The interaction matrix \(P_{kj}\) is updated using only \(\omega_k^t\) (the reward of client \(k\)), not a symmetric quantity between \(k\) and \(j\) (Eq. 5). The paper then builds UPVs by deleting diagonal and reciprocal entries, and applies an RBF kernel to form a symmetric affinity matrix \(W\). The rationale connecting this pipeline to distributional similarity is described conceptually (lines 93–97) but not formally derived — no theorem or argument explains why Euclidean distance between these partial row vectors encodes similarity of data distributions. The Davies-Bouldin \(>1\) split threshold is also arbitrary.

3. **Overstated novelty of the "Wasserstein Adjusted Metric."** The proposed metric (Section 3.5) sorts class frequency vectors and computes Euclidean distance between them, then uses this as the distance in existing clustering metrics (Davies-Bouldin, Silhouette). Sorting histograms before computing distances is standard practice. The paper states the metric "derived the Wasserstein distance" (line 132) but provides no derivation or proof of this connection — only an equivalence claim. This is a reasonable adaptation for FL settings but does not constitute a novel contribution.

4. **No ablation study.** The method has multiple components (Gaussian kernel, averaging over S iterations, interaction matrix update, UPV construction, RBF affinity, spectral clustering, DB threshold). There is no analysis isolating which components are essential. Given the pipeline complexity, an ablation would significantly strengthen confidence in the design.

5. **No communication overhead analysis.** The method requires clients to send their loss vector of length \(S\) (e.g., \(S=8\) or more values) every round in addition to model parameters. The paper states there is no "significant communication overhead" (Section 2, Section 5) but provides no comparison of total bits communicated versus baselines. This is relevant for the claimed cross-device applicability.

6. **"Out-of-distribution" not concretely defined.** The paper uses this term repeatedly (Sections 3.2, 5) but never defines what constitutes an out-of-distribution client in terms of the reward or loss process. The Gaussian reward measures deviation from the *average loss*, not from a true data distribution. The mapping from loss proximity to distribution similarity is asserted but not established.

### Trivial
None.

## Nice-to-Haves

- An ablation study isolating the contribution of each component (Gaussian kernel, UPVs, spectral clustering, DB threshold).
- A communication cost comparison (total bits per round) versus baselines.
- Experiments with a larger number of clients (thousands) to support the cross-device FL claims.
- Convergence plots of the interaction matrix \(P^t\) over rounds to visualize the claimed convergence behavior.

## Removed Points

- **"Experimental results are unverifiable due to image references"** — Removed. The `![](images/...)` references are parser artifacts; images exist in the original submission. Per hard rules, formatting artifacts from PDF extraction are not author errors.
- **"Algorithm pseudocode is missing"** — Removed. The algorithms are described in text (Sections 3.3–3.4) and may be presented as formatted boxes or figures in the original submission, which are lost during text extraction.
- **"Typos, grammar, and formatting issues"** — Removed per hard rules (parser artifacts, not author errors).
- **"Convergence plots for interaction matrix mentioned but not shown"** — Removed as a weakness; this is a parser artifact (Figure 2 exists in the original submission).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's claimed "rigorous theoretical framework" and the actual unsupported stationarity assumption, but this is the standard observation that an asserted assumption without justification does not constitute rigor.

## Suggestions

1. **Revisit the theoretical framing.** Either provide a rigorous justification for the stationarity claim (under what conditions on the loss process does the Gaussian transformation yield stationary rewards?), or drop the stationarity claim and reframe the weights as online estimates with finite-time bounds without asymptotic convergence guarantees. The empirical method can stand on its own without overstated theory.

2. **Add an ablation study.** Show the effect of removing the UPV construction, using raw Gaussian weights as features, or using a simpler clustering method (e.g., k-means on weights) to identify which components drive performance.

3. **Define "out-of-distribution" concretely** in terms of the reward process. What threshold on \(\gamma_k^t\) or \(\mu_k\) separates in-distribution from out-of-distribution clients?

## Score and Decision

This paper has a genuine strength in its core design — loss-value-only clustering that is orthogonal to aggregation methods — and the empirical claims (as described qualitatively) suggest the method works. However, the theoretical analysis is built on an unsubstantiated stationarity assumption that is presented as "rigorous" but is not justified. Combined with the overclaimed novelty of the clustering metric, the missing ablation study, and the absence of communication cost analysis, the paper falls short of the standard for acceptance. The core idea is salvageable, but the paper in its current form does not deliver the theoretical rigor it promises.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>