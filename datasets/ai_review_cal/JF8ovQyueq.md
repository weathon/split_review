- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
I now have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes FedGWC, a hierarchical clustering method for personalized federated learning that groups clients by transforming their per-iteration empirical losses into Gaussian reward weights and constructing an interaction matrix, without requiring model updates or pre-specified cluster counts. The core idea — using Gaussian-weighted loss similarities to detect distributional homogeneity — is clean, communication-light, and practically appealing. The paper provides convergence theorems for the weight estimates (Theorems 3.1, 3.2, Proposition 3.1), a recursive splitting procedure driven by Davies-Bouldin scores, and a proposed class-adjusted clustering metric. Experiments on CIFAR-10/100 and FEMNIST show FedGWC outperforming CFL, FeSEM, and IFCA, and improving standard FL algorithms (FedAvg, FedAvgM, FedProx) and PFL methods (pFedMe, Per-FedAvg) when used as a front-end.

## Strengths

1. **Well-motivated and communication-light clustering mechanism.** The approach of using only per-iteration loss vectors (not model gradients or parameters) to infer distributional similarity is genuinely novel and practical. Communicating a single vector of S loss values per round (line 55) adds negligible overhead compared to model update transmission, and the method is compatible with any FL aggregation algorithm (Table 2). This is concretely validated: FedGWC boosts FedAvg by >10% balanced accuracy on CIFAR-100 (line 226).

2. **Consistent and often substantial empirical gains across diverse settings.** FedGWC outperforms all clustering baselines (CFL, FeSEM, IFCA) on CIFAR-100 and FEMNIST (Table 1), improves FedAvg, FedAvgM, and FedProx (Table 2), and enhances pFedMe and Per-FedAvg (Table 3). Notably, it matches or exceeds IFCA — which the paper describes as an "upper bound" due to its impractical communication budget — without requiring clients to evaluate multiple models. The gains are consistent across datasets and both clustering and accuracy metrics.

3. **Automatic determination of cluster count without a priori specification.** The recursive splitting procedure using DB scores on the affinity matrix (Section 3.3) avoids the need to pre-specify the number of clusters (required by FeSEM, IFCA) and overcomes CFL's sensitivity to gradient-norm thresholds. Figure 2 shows accuracy jumps at the detected split rounds, supporting that the splits are meaningful.

4. **Orthogonal integration with existing FL methods.** Table 2 shows that FedGWC functions as a plug-in pre-clustering step: it improves FedAvg, FedAvgM, and FedProx on heterogeneous settings without modifying their internal aggregation logic. This validates the claim (Section 1) that FedGWC is complementary, not competing, with robust aggregation methods.

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between theoretical convergence claims and the actual non-stationary FL setting.** The paper claims (line 47, 55) that the reward process $R_k^{t,s}$ is "stationary by construction" and that its "moments do not depend on the iteration," then proves convergence of the Gaussian weights $\Gamma_k^t$ to a fixed $\mu_k$ (Theorems 3.1, 3.2) under this assumption. In practice, the losses $L_k^{t,s}$ depend on the model parameters $\theta_k^{t,s}$, which change every round as the model trains — the loss distributions shift systematically over time. The rewards inherit this non-stationarity because $\hat{\mu}^{t,s}$ and $\hat{\sigma}^{t,s}$ are recomputed each round from the current round's losses. The paper neither acknowledges this gap nor provides an argument (e.g., convergence to a slowly varying target, or bounds on the drift rate) that the theory carries over. The theorems therefore apply to an idealized static process, not to the actual algorithm. This does not invalidate the empirical method (the weight update Eq. 2 is a reasonable heuristic regardless), but the presentation misleadingly implies formal guarantees that the current analysis does not deliver.

2. **Experimental evaluation lacks statistical rigor and omits critical reproducibility details.** No error bars, standard deviations, or multiple-seed results are reported for any accuracy or clustering metric. In a stochastic setting with random client sampling, model initialization, and minibatch ordering, single-run results are insufficient to distinguish genuine improvements from variance. Additionally:
   - The Dirichlet concentration parameters $\alpha$ used to generate the non-IID splits for the **main experiments** (Tables 1–3) are never stated; they are only specified for the synthetic analysis in Section 4.2.
   - Critical training details are missing: learning rate schedule, number of local epochs, participation fraction, batch size, and how hyperparameters were chosen for each baseline. The paper claims it requires "only one hyperparameter" ($\epsilon$), but the algorithm also involves $\beta$ (RBF kernel), $n_{\text{max}}$, the update coefficient sequence $\alpha_t$, and the DB threshold — none of which are listed with chosen values.

3. **Inconsistency between text and tables regarding CFL's performance.** The text states (line 158) that CFL "resulted in no splits, thereby achieving performance equivalent to FedAvg." Yet Table 1 reports CFL accuracy values (64.3 on CIFAR-10, 66.3 on CIFAR-100) that differ from the FedAvg baseline in Table 2 (71.2 on CIFAR-10, 62.1 on CIFAR-100). If CFL did not split, its results should match plain FedAvg under the same configuration. The paper must explain this discrepancy or correct the claim.

### Minor

4. **Interaction matrix construction is described in an overly complex way relative to what is computed.** Equation 5 updates $P_{kj}$ using only $\omega_k^t$ (client $k$'s own reward), with no dependence on $j$'s loss or data. Consequently, $P_{kj} = P_{kk}$ for all $j$ — the "perception of client $k$ by client $j$" language (line 93) is misleading because client $j$ plays no role in $P_{kj}$. The UPV construction and RBF kernel (Eq. 6) then effectively compare two clients' reward histories, which is a sensible clustering signal, but the paper would benefit from simplifying this description and explicitly validating whether the UPV/RBF machinery adds value over using the Gaussian weights directly.

5. **Puzzling success against the IFCA "upper bound" is not discussed.** IFCA is described as an upper bound because it communicates all cluster models to every client (line 156). FedGWC matches or exceeds IFCA on CIFAR-100 and FEMNIST (Table 1). This is a noteworthy result that warrants analysis: is IFCA suboptimal due to noisy client-level loss evaluation with limited local steps, or does the fixed cluster count disadvantage it? The paper's silence on this leaves the reader unsure whether the comparison is fair.

6. **The proposed clustering metric's connection to the Wasserstein distance is tenuous.** Equation 8 defines a scaled $\ell_2$ distance on sorted class-frequency vectors and claims it is "derived from the Wasserstein distance" (line 132). For 1D discrete distributions, the Wasserstein-$p$ distance between sorted quantiles is $(\sum |x_{(i)}-y_{(i)}|^p)^{1/p}$, making Eq. 8 a Wasserstein-2 variant. The paper should state this explicitly rather than appeal to the general Wasserstein concept without specifying $p$, and should clarify why $\ell_2$ (vs. $\ell_1$) is the appropriate choice.

7. **Synthetic analysis (Tables 4, 5) lacks baseline comparisons.** The results show FedGWC can separate clients by extreme Dirichlet parameters ($\alpha=0$ vs. $\alpha=100$) and visual domains with high Rand Index scores, but no other clustering method (CFL, FeSEM, IFCA) is shown for comparison. Without such baselines, the numbers primarily demonstrate that FedGWC can separate clearly distinct groups — a near-tautological result under these extreme settings.

### Trivial

- Figure 2 x-axis is unlabeled (presumably communication rounds).
- The conclusion's claim "without increasing computational cost" (line 245) slightly oversells — spectral clustering on a $K\times K$ matrix incurs $O(K^3)$ cost, which is negligible for $K=100$ but worth noting for larger federations.

## Nice-to-Haves

- A hyperparameter table listing all chosen values ($\epsilon$, $\beta$, $n_{\max}$, $\alpha_t$, DB threshold) would greatly aid reproducibility.
- A sensitivity analysis for the two main hyperparameters ($\epsilon$ and the DB threshold) would strengthen the paper's robustness claims.
- Reporting results over multiple random seeds (≥3) with standard deviations is the single most impactful improvement the authors could make.

## Removed Points

- **"DB threshold of 1 is arbitrary"** — Removed. The threshold of 1 is standard in clustering literature (DB < 1 indicates well-separated clusters); the paper correctly cites this convention (line 113).
- **"Missing related work"** — Removed per instruction. I cannot independently verify which works are missing, and the paper's related work section (Section 2) covers the main lines of clustered FL (CFL, IFCA, FeSEM, Multi-Center FL).
- **"Stationarity claim only refers to definition, not process" framing as fatal** — Demoted from Fatal to Major. The stationarity gap is real, but the core algorithm (weight updates + interaction matrix + spectral clustering) does not depend on the formal convergence proof to be effective; the theory is presented as motivation (line 61: "to rigorously motivate the construction"), not as the sole basis for the method's validity.
- **Generic area-of-concern sweeps** — Removed several speculative "could the metric be measuring a proxy?" type criticisms that lacked specific anchoring in the paper's text.
- **Strength about novel metric** — Weakened. The metric is essentially standard clustering metrics applied to sorted class frequencies; its connection to Wasserstein distance is imprecise, and the novelty is modest.

## Novel Insights

A genuinely novel observation that emerges from cross-examining the reviews is that the interaction matrix $P$ (Eq. 5) is effectively **not pairwise at all**: its $(k,j)$ entry depends only on $\omega_k^t$, not on $\omega_j^t$ or any property of client $j$. This means the matrix carries no more information than the set of per-client Gaussian weight time series. The subsequent UPV construction and RBF kernel (Eq. 6) do create a meaningful pairwise signal — $\|v_k^j - v_j^k\|$ measures how differently two clients' reward histories evolve — but the path from the "interaction matrix" to the affinity matrix involves substantially more machinery than is acknowledged. This suggests a simpler alternative baseline exists: directly compare the Gaussian weight trajectories $\gamma_k^t$ between clients (e.g., with a distance on the weight time-series vectors) and cluster on that. Whether the paper's more complex construction outperforms such a simpler baseline is an open question that an ablation could resolve.

## Suggestions

1. **Reframe the theoretical section explicitly as a heuristic motivation**, or adapt it to the non-stationary setting (e.g., prove convergence to a time-varying target or show that the weights track a slowly changing mean). The current framing promises more rigor than it delivers.

2. **Add error bars** (≥3 seeds) to all tables and specify the exact $\alpha$ values and training hyperparameters used in each experiment. This is the single most important revision for credibility.

3. **Clarify the CFL inconsistency**: explain why CFL's reported accuracy differs from plain FedAvg if no splits occurred, or correct the claim.

4. **Add an ablation study** comparing the full UPV/RBF affinity construction against a simpler baseline of clustering on Gaussian weight vectors directly. This would either justify the extra complexity or simplify the method.

5. **Discuss why FedGWC matches/exceeds IFCA** despite IFCA's higher communication budget.

6. **Specify the exact Wasserstein variant** being used for the adjusted metric and clarify the choice of $\ell_2$ over $\ell_1$.
