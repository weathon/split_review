## Summary

This paper proposes POTEC, a two-stage algorithm for off-policy learning (OPL) in contextual bandits with large discrete action spaces. POTEC decomposes the policy into a first-stage cluster-selection policy (trained via a novel low-variance importance-weighted gradient estimator operating in the compact cluster space) and a second-stage within-cluster action-selection policy (derived from a pairwise reward regression model). The key idea is to apply policy-based learning where the action space is small (cluster level) and regression-based learning where it is large (within cluster), thereby mitigating the bias-variance dilemma that cripples standard OPL methods in large action spaces. Theoretical analysis provides bias characterization under local correctness and variance reduction guarantees, while experiments on synthetic and real-world (KuaiRec) data show substantial improvements over regression-based, IPS-PG, and DR-PG baselines.

## Strengths

- **Novel low-variance gradient estimator with rigorous theoretical grounding.** The POTEC gradient estimator (Eq. 7) applies importance weighting only in the cluster space rather than the full action space. The paper provides formal bias analysis (Theorem 3.2), variance decomposition (Proposition 3.4), and a variance reduction result (Proposition 3.5) that quantifies why cluster-level weighting helps. This is more thorough theoretical characterization than most OPL papers provide for their estimators.

- **Strong empirical evidence in the critical regime.** The synthetic experiments (Figure 2) show that when the action space reaches |A| ≥ 2,000, all baselines (IPS-PG, DR-PG, regression-based) collapse to or below the logging policy's value, while POTEC maintains stable high performance. This directly validates the core claim that POTEC resolves the variance explosion in large action spaces.

- **Weaker support requirement with empirical confirmation.** Condition 3.1 (Full Cluster Support) is strictly less restrictive than Condition 2.1 (Full Support) required by standard importance-weighting methods. Figure 4(iii) confirms this matters in practice: as the proportion of deficient actions increases, POTEC degrades much more gracefully than baseline methods.

- **Ablation study isolating the value of pairwise regression.** Figure 3 compares POTEC with pairwise regression (Eq. 9) against POTEC with standard absolute reward regression, showing both outperform DR-PG and pairwise regression provides additional consistent gains.

- **Practical viability demonstrated with learned clusters.** The method works well even when clusters are obtained via KMeans on estimated rewards, not just with ground-truth clusters, supporting real-world applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline regression models unspecified on KuaiRec, creating a confound.** The paper states (line 224) that POTEC uses Random Forest for pairwise regression on KuaiRec, but does not specify what regression models the baselines (IPS-PG, DR-PG, Reg-based) use. If baselines used neural networks while POTEC used Random Forest, any performance advantage could partly reflect the choice of regressor class rather than the POTEC framework. The synthetic experiment controls for this (all methods use the same neural architecture), so the core claims remain supported, but the KuaiRec evidence is weakened by this omission.

2. **No explicit training loop pseudocode.** The training procedure is sequential and decipherable from Section 3: (a) form clusters, (b) train the pairwise regression model $\hat{f}_\psi$ via Eq. 9, (c) derive the 2nd-stage policy $\pi_\psi^{2nd}$ from $\hat{f}_\psi$, (d) fix $\pi_\psi^{2nd}$ and train the 1st-stage policy $\pi_\theta^{1st}$ via the POTEC gradient estimator. However, the paper never states this procedure explicitly or provides pseudocode, leaving room for ambiguity. Given that the critics raised a "chicken-and-egg" concern (which is incorrect but understandable), the paper would benefit from being more explicit.

3. **Clustering quality is not analyzed.** The paper relies on action clustering (via KMeans on estimated rewards) but never reports cluster quality metrics such as within-cluster reward variance, purity, or sensitivity analyses. Since POTEC's bias depends on how well clusters preserve local correctness, the absence of any diagnostic makes it hard to assess when the method might fail.

4. **"Strict generalization of policy- and regression-based approaches" is not empirically demonstrated.** The paper claims POTEC spans a full spectrum whose endpoints are policy-based and regression-based methods (Figure 1; abstract; line 14), but does not empirically show performance interpolation as $|\mathcal{C}|$ varies from 1 to $|\mathcal{A}|$. This claim is presented as a conceptual contribution and is not verified experimentally.

### Trivial
- The claim about being "the first to formulate and propose methods specific to OPL for large discrete action spaces" (line 14) invites unnecessary pushback. The paper already carefully distinguishes its setting from OPE and RL work; the framing could be softened.

## Nice-to-Haves
- **Add a "cluster-then-IPS" baseline** that clusters actions, applies standard IPS-PG at the cluster level, and then uniformly selects actions within the chosen cluster. This would isolate whether POTEC's advantage comes from its specific two-stage decomposition or merely from operating in a reduced cluster space.
- **Provide a combined bias-variance bound** characterizing when the tradeoff is favorable (i.e., MSE(POTEC) ≤ MSE(DR) under conditions on cluster quality and $\hat{f}$ accuracy), though this is not standard practice and would strengthen rather than fix the paper.
- **Vary $|\mathcal{C}|$ from 1 to $|\mathcal{A}|$** in experiments to empirically instantiate the claimed spectrum in Figure 1.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **"Chicken-and-egg" training dependency (Harsh Critic #1):** The paper describes a clear sequential procedure: train $\hat{f}_\psi$ → derive $\pi_\psi^{2nd}$ → fix it → train $\pi_\theta^{1st}$. Section 3.1 begins "given a (pre-trained) 2nd-stage policy" and Section 3.2 shows how to construct that policy. The critic's circular dependency concern does not hold.
- **Missing action-embedding baselines (Harsh Critic #2):** The paper justifies at length (line 14) why Chandak et al. (2019) and Gu et al. (2022) operate in different settings (RL, not OPL) and cannot be directly adapted. This is a reasonable scope decision.
- **Local correctness / bias-variance tradeoff gap (Harsh Critic #4):** Providing separate bias and variance analyses is standard. A combined MSE bound, while nice to have, is not a missing requirement for a method paper. The paper's empirical results support its claims even when local correctness is violated.
- **Estimating π₀(c|x) introduces error (Harsh Critic):** The logging policy π₀(a|x) is known in standard OPL; π₀(c|x) is computed from it, not estimated. The critic misunderstood the setup.
- **Synthetic experiment inherently favors cluster structure (Harsh Critic):** Testing on data with cluster structure is the intended use case. The paper also evaluates with learned clusters and varying numbers of clusters (Figure 2(iii)), providing some robustness assessment.
- **KuaiRec reward synthesis criticism (Harsh Critic):** Using a full-feedback dataset's expected reward as the mean of a Gaussian to simulate bandit feedback is standard practice in the OPE/OPL literature. The paper's phrasing "without synthesizing the reward function" means without modeling the expected reward, which is taken from real data.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify baseline regression models for KuaiRec.** State whether IPS-PG, DR-PG, and Reg-based used neural networks, Random Forest, or something else — and ideally use the same model class across all methods to eliminate this confound.
2. **Provide training pseudocode.** A concise algorithm box showing the sequential training steps (clustering → pairwise regression → 2nd-stage policy derivation → 1st-stage policy training) would resolve ambiguity.
3. **Report clustering diagnostics.** Add metrics such as within-cluster reward variance or adjusted Rand index to help readers assess when POTEC's assumptions are satisfied.
4. **Tone down the "first to formulate" claim.** The paper's contribution is strong enough without this framing.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>