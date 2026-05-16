Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes BroGNet, a graph neural stochastic differential equation (neural SDE) framework that learns Brownian dynamics directly from trajectory data. The key architectural innovation is a hard constraint enforcing Newton's third law on predicted pairwise forces, which guarantees zero net force and exact linear-momentum conservation (Theorem 1). The authors demonstrate BroGNet on linear spring, non-linear spring, and binary linear spring systems, showing it outperforms several baselines (NN, BNN, BFGN, BDGNN, BNequIP) and achieves zero-shot generalization to systems two orders of magnitude larger than those in the training set and to unseen temperatures.

## Strengths

- **Zero-shot scalability to unseen system sizes and temperatures (Section 4.3, Figure 5)**: Because BroGNet is a GNN with parameters independent of particle count, models trained on 5-particle systems generalize without retraining to 50- and 500-particle systems (two orders of magnitude larger) while maintaining comparable trajectory rollout error. Models trained at T=1 also generalize to T=10 and T=100. This inductive scalability is a direct consequence of the graph-based formulation and is not possible with non-graph baselines (NN, BNN). This is the paper's strongest empirical finding.

- **Exact momentum conservation via architectural bias (Eqs. 7–8, Theorem 1, Figure 6)**: By summing forces from incoming edges and subtracting forces from outgoing edges, BroGNet guarantees zero net force. This produces a momentum error near zero (Figure 6), while all other models (including the soft-constraint MIBDGNN) exhibit non-zero error. This hard constraint is physically principled for interaction forces satisfying Newton's third law.

- **Data efficiency (Section 4.5, Figure 7)**: BroGNet maintains low rollout error when trained on as few as 100–1000 data points, whereas graph baselines (BFGN, BDGNN, MIBDGNN, BNequIP) degrade more sharply. This is attributed to the strong inductive bias from the hard momentum constraint.

- **Clean experimental design isolating momentum conservation**: The controlled comparison among BroGNet (hard constraint), BDGNN (no constraint), and MIBDGNN (soft constraint) allows attribution of performance differences to the type of momentum bias. The paper honestly reports that MIBDGNN outperforms BroGNet on predictive metrics (Section 4.2) while BroGNet achieves superior momentum conservation (Section 4.4).

- **First GNN + conservation-law framework for learning multi-particle Brownian dynamics**: While neural SDEs exist in the literature, the specific combination of graph-based modeling, a learnable SDE drift+diffusion, and a physically grounded hard constraint for interacting particle systems is novel and fills a genuine gap.

## Weaknesses

### Fatal
None.

### Major

- **The paper's central framing overclaims the benefit of the hard constraint relative to the soft-constraint alternative.** The abstract states that momentum conservation "provides superior performance on learning dynamics" without qualification, and Section 4.4 claims the hard constraint "contributes to its improved performance." However, the paper's own results in Figures 2–4 show that the soft-constraint variant MIBDGNN *significantly outperforms* BroGNet on all three primary metrics (trajectory rollout error, Brownian error, position error) across all three systems. The paper acknowledges this in Section 4.2 ("Interestingly, we observe that the MIBDGNN significantly outperforms BROGNET") and in the conclusion, but the core framing—from the abstract through the claims in Sections 3.1 and 4.4—continues to assert "superior performance" from the hard constraint without reconciling the countervailing evidence. The result is a tension between the paper's promotional narrative and its empirical findings. The paper would be better served by clearly framing the trade-off: the hard constraint gives exact zero-net-force and data efficiency at the cost of some predictive accuracy relative to the soft constraint, rather than claiming unqualified superiority.

### Minor

- **The novelty claim about learning SDEs from data is overstated.** The paper states "to the best of the authors' knowledge, no attempt has been made to learn the dynamics of Brownian systems in particular, or SDEs in general, from their trajectory" (Section 1). This is too broad: Neural SDEs (e.g., Kidger et al. 2021, Li et al. 2020) learn both drift and diffusion functions from trajectory data. The paper's genuine novelty lies in the *combination* of graph-based modeling + hard conservation laws for multi-particle *Brownian* dynamics, which should be claimed precisely rather than as a blanket statement about all SDE learning.

- **"Momentum conservation" is conceptually imprecise for overdamped Brownian dynamics.** The dynamics are governed by a first-order SDE (Eq. 2) in the overdamped limit, where acceleration is neglected and momentum is not a state variable. Theorem 1 correctly enforces zero net force (Newton's third law) on the deterministic component, which is a valid inductive bias for inter-particle forces. However, the paper equates this with "linear momentum conservation" without adequately discussing that the stochastic term imparts random momentum changes, so the total system does not conserve momentum in the usual sense. This does not invalidate the method but weakens the theoretical framing and could mislead readers about what property is being enforced and why it matters.

- **The per-particle KL divergence metric ignores cross-particle correlations (Section 4.1).** The KL divergence is computed independently per particle assuming univariate normal distributions. In interacting particle systems, cross-particle correlations are important, and the current metric may not capture whether the joint distribution over all particles is learned correctly.

- **Statistical rigor is limited.** Key comparisons (e.g., BroGNet vs. MIBDGNN in Figures 2–4) are described with language like "significantly outperforms," but no confidence intervals or formal hypothesis tests are reported. While the box-plot-style figures show distributions over 1000 forward simulations (100 initial conditions × 10 random seeds), the lack of explicit statistical testing weakens the evidential weight of the comparisons.

### Trivial
None.

## Nice-to-Haves

- **Ablation of the soft-constraint strength:** The paper compares BroGNet against a single instantiation of MIBDGNN. Varying the weighting coefficient of the momentum regularization term in MIBDGNN's loss could help characterize the landscape between hard and soft constraints and reveal whether the hard constraint has advantages in certain regimes (e.g., very small data, where the paper's data efficiency experiment already provides some evidence).

- **Time-step sensitivity analysis:** The paper notes that the learned dynamics are "optimal for the Euler Maruyama integrator." Reporting sensitivity to Δt at test time would clarify the method's robustness.

- **External field experiment:** The paper explicitly limits itself to systems without external fields. A simple experiment with a weak constant external field (which should break exact momentum conservation) would test the method's scope and help define where the hard constraint remains beneficial vs. where it becomes limiting.

- **Joint-distribution evaluation:** Reporting a metric that captures cross-particle correlations (e.g., Wasserstein distance on the full state vector, or pairwise marginal KL divergences) would strengthen the evaluation for interacting systems.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Zero-shot generalization section does not compare MIBDGNN vs BroGNet individually":** The reviewer claimed Section 4.3 "does not show how MIBDGNN compares to BroGNet—it treats them as a group." This is factually incorrect. Figure 5 explicitly shows trajectory rollout error for BFGN, BDGNN, MIBDGNN, BNequIP, and BroGNet separately. Removed.

- **"BNequIP adaptation not clearly specified":** The paper states BNequIP uses equivariant GNNs to predict force vectors, and the SDE integration (Eq. 10) handles the diffusion term. This is sufficient description for a baseline. Removed as a nitpick.

- **Demand for "more baselines" / "missing related works":** Not permissible to mention missing related works per instructions — the reviewer has no way to confirm what exists. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely interesting observation: the soft constraint (MIBDGNN) outperforms the hard constraint (BroGNet) on predictive accuracy, yet the hard constraint gives better data efficiency and exact physical consistency. This suggests a nuanced trade-off landscape where the soft constraint provides more flexible learning (by not enforcing exact zero-net-force, allowing the model to absorb small errors in force prediction), while the hard constraint regularizes more aggressively, which pays off in low-data regimes. This tension—rarely explored in the physics-informed learning literature—is noted but left unresolved by the paper; it points toward a potentially useful design space where hybrid or adaptive constraint mechanisms could be explored.

## Suggestions

1. **Reframe the central claim** to honestly reflect the trade-off: the hard constraint guarantees exact zero-net-force and improves data efficiency, while the soft constraint (MIBDGNN) yields higher accuracy on trajectory metrics. Clarify in the abstract that "superior performance" refers to comparisons against baselines without any momentum bias (BDGNN), not against the soft-constraint alternative.
2. **Acknowledge the neural SDE literature** more precisely, and claim novelty specifically for the combination of GNN + hard conservation law for multi-particle Brownian dynamics rather than broadly claiming first-ever SDE learning from trajectories.
3. **Add a discussion of momentum conservation in the overdamped regime** (Section 2 or 3) explaining why enforcing Newton's third law on forces is the correct inductive bias even though momentum is not a classical state variable in this setting.
4. **Report confidence intervals** for the key BroGNet vs. MIBDGNN comparisons.
5. **Include MIBDGNN in the data efficiency plot (Figure 7)** in the main paper (it appears it may already be there, but should be highlighted in the discussion).

## Score and Decision

This paper presents a competently designed framework with a clean ablation study and a genuinely impressive zero-shot generalization result. The GNN + hard-constraint + SDE combination is novel and the empirical evaluation is fairly thorough. However, the paper's central claim—that the hard momentum-conservation constraint provides "superior performance"—is contradicted by its own best-performing variant (MIBDGNN) on the primary evaluation metrics, and the paper does not adequately resolve this tension. This framing issue, combined with an overstated novelty claim and some conceptual imprecision, weakens the contribution as presented. The paper would need a major revision in framing (honestly reporting the hard-vs-soft trade-off) and stronger justification for why the hard constraint is valuable despite lower accuracy. In its current form, the contribution does not fully hold up to the claims made.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>