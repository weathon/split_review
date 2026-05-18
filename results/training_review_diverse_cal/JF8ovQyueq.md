Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes FedGWC, a clustering-based personalized federated learning method that groups clients by data distribution similarity. The key idea is to transform per-client empirical loss trajectories into Gaussian rewards, estimate their expectations via stochastic approximation, and build an interaction matrix from which an affinity matrix is constructed for spectral clustering. The method is evaluated on CIFAR-10, CIFAR-100, and FEMNIST, showing accuracy improvements when combined with FedAvg, FedAvgM, and FedProx, and outperforming CFL, FeSEM, and IFCA on clustering quality metrics.

## Strengths

- **Consistent accuracy gains across aggregation algorithms**: FedGWC + FedAvg improves balanced accuracy on CIFAR-100 from 24.15% to 30.33%, and similar gains hold for FedAvgM and FedProx (Table 2). These gains are shown across multiple datasets and are largest on the most heterogeneous settings, where meaningful clustering matters most.

- **Novel use of loss trajectories for client similarity**: Rather than relying on model updates (gradient norms, parameter distances) or raw data, FedGWC clusters clients using only the empirical loss trajectory communicated per round. The idea that clients with similar data distributions exhibit similar loss dynamics is intuitive and practically appealing, since losses are already computed during training at no extra computational cost.

- **Automatic cluster determination with over-splitting control**: The algorithm autonomously determines when to split via MSE convergence detection on the interaction matrix, and selects the number of clusters using a Davies-Bouldin threshold. This addresses a practical pain point in clustered FL — CFL is noted to be hyperparameter-sensitive and often splits too aggressively or not at all, while FeSEM and IFCA require a preset number of clusters.

- **New Wasserstein-derived clustering metric**: The class-adjusted clustering metric (based on ranked class frequency vectors) provides a principled way to evaluate cluster cohesion under class imbalance. While the metric itself is simple, the connection to Wasserstein distance gives it theoretical grounding.

- **Domain shift detection**: Controlled experiments (Section 4.2) show FedGWC successfully separates clients by visual domain (clean, noisy, blurred images) with Rand-Index scores approaching 1.0, suggesting applicability beyond label-skew heterogeneity.

## Weaknesses

### Fatal

None.

### Major

- **Unsupported stationarity claim undermines the theoretical framing**. The paper asserts that the reward processes are "stationary by construction" and "do not depend on t" (Section 3.2, lines 47, 55). This is not justified and is likely false: the empirical loss $L_k^{t,s}$ depends on the model parameters $\theta_k^{t,s}$, which change each round. The distribution of losses therefore shifts systematically as training proceeds. The convergence theorems (3.1, 3.2) rely on standard stochastic approximation results that assume a fixed target $\mu_k$ — but if the target itself drifts across rounds, the theorems as stated do not apply to the actual process. This does not necessarily invalidate the algorithm (it may work well as a heuristic), but it means the paper's claimed theoretical guarantees for the Gaussian weights are unsupported. The authors should either (a) provide a rigorous justification for why stationarity holds, (b) reframe the theory to characterize convergence to a time-varying target, or (c) drop the theoretical claims and position the method as empirically motivated.

- **The interaction matrix lacks a clear justification as a pairwise similarity measure**. The entry $P_{kj}$ accumulates the reward $\omega_k^t$ (client $k$'s own alignment with the round's average) across rounds where both $k$ and $j$ are sampled (Eq. 5). The paper claims this estimates "the expected perception of client $k$ by client $j$" and that a large value "suggests that the two clients are well-represented within the same distribution." However, $\omega_k^t$ measures client $k$'s fit to the *current round's sample average* — it does not directly encode anything about client $j$'s distribution. While the intuition that co-sampled similar clients will both tend to have high rewards may hold in expectation under certain conditions, no argument or analysis is given. The downstream construction of the affinity matrix $W$ via UPVs and RBF kernels partially addresses the asymmetry concern (the UPV comparison $v_k^j$ vs. $v_j^k$ does use both directions), but the fundamental question of what $P_{kj}$ actually estimates remains unanswered.

- **Experimental details essential for reproducibility are absent from the paper**. The main text does not state the number of clients, participation ratio, local epochs, batch size, learning rate, or communication rounds for any of the benchmark experiments in Tables 1–3. The Dirichlet concentration parameters are only given for the analysis experiments in Section 4.2, not for the main benchmark results. Without these, the results cannot be reproduced or meaningfully compared to other work. The code is referenced to supplementary material, but basic experimental settings belong in the paper itself.

### Minor

- **The claim of "only one hyperparameter" is overstated**. The paper states "FedGWC requires only one hyperparameter" (Section 4.1, paragraph 1). In practice, the algorithm requires: the forgetting factor $\alpha_t$ (or a constant $\alpha$), the MSE convergence threshold $\epsilon$, the RBF kernel bandwidth $\beta$, and the maximum number of clusters $n_{\max}$ (which appears in the DB-index-based cluster selection but its value is never stated). Even if some of these are set to reasonable defaults, calling it "only one" is misleading and the paper should be transparent about all tunable parameters.

- **The domain detection experiment (Table 5) lacks baselines**. The high Rand-Index scores for FedGWC on separating clean/noisy/blurred domains are presented without comparison to other clustering methods (e.g., FeSEM, IFCA, or even simple baselines like k-means on loss values). It is unclear whether this capability is unique to FedGWC or would be achieved by any reasonable clustering approach in a setting with three clearly distinct visual domains.

- **The proof of Proposition 3.1 (variance reduction) is deferred to the appendix** and its assumptions are not stated in the main text. If it assumes the rewards are i.i.d. across rounds for a given client, this would not hold due to the changing model — mirroring the stationarity issue. The proposition's relevance to the actual algorithm is unclear without verifying its assumptions.

- **"Unbiased perception vectors" is a potentially misleading name**. The term "unbiased" here refers to excluding self and comparison-target entries from the UPV, not to statistical unbiasedness. While the design choice is clear, the terminology could confuse readers expecting a statistical guarantee.

### Trivial

- **Naming inconsistency**: The abstract uses "FedGW" while the rest of the paper uses "FedGWC." This should be unified.
- **The Wasserstein-adjusted metric** (Section 3.5) is presented as a new contribution but is simply rank-sorting class frequency vectors before computing an L2 distance and scaling by $1/C$, then plugging into standard clustering metrics. While the connection to Wasserstein distance is noted, it is a straightforward adjustment. This is fine as a practical tool but is not a deep theoretical contribution — the paper should calibrate how it presents this.

## Nice-to-Haves

- **Add a random clustering baseline**: Splitting clients into random groups of the same sizes as FedGWC's output would help confirm that the Gaussian-weight-based grouping, rather than just the variance reduction from smaller groups, is responsible for the accuracy gains.
- **Quantify communication overhead**: The paper states FedGWC "does not impose significant communication overhead" without reporting numbers. The per-round communication of $S$ loss values per sampled client should be measured and compared to baselines like CFL (gradient norms) or IFCA (all cluster models).
- **Report error bars or standard deviations** for the main results. Given stochasticity in FL training and clustering outcomes, variance estimates would strengthen confidence in the reported improvements.
- **Specify the maximum number of clusters $n_{\max}$** used in the DB-index search and whether this value varies across datasets.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"The Wasserstein-adjusted metric is introduced but never used to evaluate FedGWC's own clustering"**: The metric IS used — Table 1 reports adjusted Silhouette and adjusted Davies-Bouldin scores that are based on this metric. The reviewer misread the experimental section. [Removed as factually wrong.]

2. **"Comparing CFL and FeSEM on the Wasserstein-adjusted metric is inherently unfair"**: All methods are being evaluated on their ability to group clients with similar class distributions — which is the common goal of clustered FL. Using a metric that measures that ability is appropriate, not biased. [Removed as factually wrong / strawman.]

3. **"CFL often produced no splits, making its scores equivalent to FedAvg. This does not constitute a fair comparison"**: The paper transparently reports CFL's behavior under attempted optimal tuning. This is a legitimate experimental finding, not an unfair comparison. [Removed as strawman.]

4. **Reproducibility concerns about code/dataset existence**: The paper states code is in the supplementary material. By policy, cited resources are assumed to exist. [Removed per hard rules.]

5. **"The paper refers to 'unbiased perception vectors' but does not prove they are unbiased for any quantity"**: The term "unbiased" refers to the design choice of excluding self and comparison-target entries, not statistical unbiasedness. The naming is clear in context. [Removed — the criticism misunderstands the term. However, the potential for confusion is noted in Minor weaknesses above.]

## Novel Insights

None beyond the paper's own contributions — the reviews do not surface a perspective that meaningfully reframes or extends the paper's findings.

## Suggestions

1. **Fix the theoretical framing**: Remove or substantially revise the stationarity claim. The Gaussian weights can be presented as an online heuristic inspired by stochastic approximation, without claiming that the convergence theorems apply to a provably stationary process. Alternatively, provide a proper justification for why the expected reward converges despite the changing model.
2. **Provide a clearer justification for the interaction matrix**: Explain why accumulating $\omega_k^t$ across rounds where $j$ is co-sampled yields a meaningful measure of pairwise distribution similarity. Include a toy example or synthetic experiment showing that $P_{kj}$ correlates with actual distribution similarity.
3. **Add random clustering and k-means-on-loss baselines** to demonstrate that FedGWC's specific clustering mechanism, not just variance reduction from smaller groups, drives the improvements.
4. **Report all experimental settings** (number of clients, participation rate, local epochs, batch size, learning rate, rounds) in a table in the main paper.
5. **Be honest about the hyperparameter count** — list all tunable parameters and their default values, and include a sensitivity analysis for the most critical ones ($\beta$, $\epsilon$).

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>