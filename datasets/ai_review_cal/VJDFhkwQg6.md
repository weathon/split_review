- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3
Now I have all the information needed for a thorough cross-verification. Let me compose the consolidated review.

## Summary

The paper proposes Federated Contrastive GFlowNets (FC-GFlowNets), a divide-and-conquer framework for GFlowNets in federated settings where the target distribution is the product of local (sensitive) rewards held by different clients. It introduces two main contributions: (1) the **federated balance condition** (Theorem 1), a necessary and sufficient condition for correctly aggregating locally trained GFlowNets into a global model sampling from the product of rewards, with an error propagation bound (Theorem 2); and (2) **contrastive balance (CB)** , a reformulation of GFlowNet training criteria that avoids parameterizing the partition function, with a theoretical connection to variational inference (Theorem 3). Experiments on four small-scale tasks (grid-world, multisets, sequences, phylogeny) show that FC-GFlowNet matches a centralized GFlowNet trained with full reward access.

## Strengths

- **Provable federated balance condition (Theorem 1, Corollary 1):** Provides the first necessary and sufficient condition for correctness when aggregating GFlowNets from different clients. The derivation is sound and the loss function follows naturally.
- **Theoretical error propagation bound (Theorem 2):** Quantifies how local approximation errors (bounds on balance ratios per client) propagate to the global model via an additive bound on Jeffrey divergence. This cleanly formalizes the catastrophic failure phenomenon familiar from parallel MCMC.
- **Empirical validation showing FC-GFlowNet matches centralized GFlowNet (Table 1, Figures 2–5):** Across all four tasks, FC-GFlowNet achieves L1 distances and top-800 rewards within one standard deviation of the centralized model (trained with direct reward access), while the PCVI baseline is orders of magnitude worse. This directly supports the core claim.
- **Single communication round:** The method requires only one client→server exchange (abstract, Section 3.1), making it communication-efficient and practically attractive for federated settings.
- **Contrastive balance connection to VI (Theorem 3):** Shows that on-policy gradients of the CB loss equal the gradient of the KL divergence D_KL[p_F || p_B], extending the characterization of GFlowNets as variational inference.
- **CB shows faster convergence in non-terminal-state tasks (Figure 6):** On multiset generation and phylogeny, CB loss achieves lower L1 error than TB, DB, and FL during training, while using fewer parameters (no flow network or partition function estimator).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited experimental scale:** All four tasks use small state spaces (18×18 grid = 324 states; multisets of size 8 with 10 types; sequences of unspecified maximum length; phylogeny with 4 species). The paper does not demonstrate that FC-GFlowNet scales to the compositional object spaces for which GFlowNets are designed (e.g., molecular graphs, longer sequences). While this is acceptable for a first theoretical exposition, the claim that FC-GFlowNet "enables distributed Bayesian inference over discrete objects" remains speculative without evidence on larger problems.

- **Lack of discussion on the reward-vs-policy distinction:** The paper motivates the federated setting by stating that clients "might be reluctant to openly disclose their rewards" due to their "sensitive nature" (line 14, line 69), yet the solution sends locally trained policies to the server. The paper does not discuss the extent to which sharing policies mitigates the original disclosure concern. For a perfectly trained GFlowNet, the ratio p_F(τ)/p_B(τ|x) is proportional to R(x), so the server could in principle reconstruct information about the local reward. A brief discussion acknowledging this gap (even a statement that this is standard in FL and orthogonal to the paper's core contribution) would strengthen the paper. Note: the paper does *not* claim formal privacy or differential privacy — this weakness is about the framing, not a broken privacy guarantee.

- **PCVI baseline is trivially weak:** The parallel categorical VI baseline factorizes each local distribution as a product of independent categoricals, which cannot capture dependencies between positions. Its poor performance is unsurprising and uninformative. However, the paper's *primary* baseline is the centralized GFlowNet (which FC-GFlowNet matches), so this is a minor issue.

### Trivial

- **Abstract overstates CB novelty:** The abstract calls CB a "novel concept" that provides "necessary and sufficient conditions for the correctness of general GFlowNets." The paper's own Lemma 1 proof says "the result follows directly from (Malkin et al., 2022, Proposition 1)," indicating CB is a reformulation of trajectory balance that eliminates the partition function parameter. The paper also correctly cites Zhang et al. (2023a) as having first proposed minimization of the variance of a TB-based estimate. The abstract wording could be more measured.

- **No error bars on CB comparison curves (Figure 6):** The training curves for DB, TB, FL, and CB do not show variability (e.g., confidence intervals or standard deviations from multiple runs), making it hard to assess the significance of CB's advantage.

- **Top-800 metric not fully explained:** The paper reports "average log reward of top-800 scoring samples" (Table 1) without clarifying whether these are the 800 highest-reward samples from the *learned distribution* or from the *ground truth* distribution. While context suggests the former, explicit definition would help.

## Nice-to-Haves

- A complexity/cost breakdown of the federated aggregation step (drawing pairs of trajectories from each client's policies, computing ratios, etc.) would help practitioners judge feasibility at scale.
- Extending the phylogeny experiment to non-constant branch lengths or more species would strengthen the distributed Bayesian inference claim.
- A comparison between CB and the Zhang et al. (2023a) variance-based loss on wall-clock time would clarify whether the theoretical equivalence yields practical differences.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Privacy claim is unsupported (structural mismatch)" → Demoted from Fatal to Minor.** The critic frames this as a "privacy claim," but the paper never uses the word "privacy" or claims differential privacy. It simply states that clients are "reluctant to openly disclose their rewards" — a standard federated learning framing. The question of whether policies leak reward information is valid but does not invalidate the core contribution. Retained as a minor weakness about missing discussion (see above).

2. **"Remark 1 circular dependency" → Removed.** The critic claims the expectation in Equation 6 creates a circular dependency because it depends on the global backward policy. However, Remark 1 characterizes the *fixed point* of the optimization (what the aggregated model samples from if federated balance is achieved), not a training procedure. This is a standard way to describe the invariant distribution; there is no circularity.

3. **"Missing citation to Zhang et al. (2023a)" → Removed.** The paper explicitly cites Zhang et al. (2023a) in lines 16 and 129, and notes the connection.

4. **"Corollary 1 formula garbled" → Removed.** This is a PDF parsing artifact, as noted at the top of the instructions.

5. **"CB is straightforwardly equivalent to TB" as a novelty concern → Moved to Trivial.** The paper's own Lemma 1 proof acknowledges the connection to Malkin et al. (2022), and the paper cites Zhang et al. (2023a). The abstract's framing as "novel" is slightly overstated but the paper properly contextualizes CB internally. Kept as a trivial wording issue.

6. **Missing architecture/parameter count details → Removed.** The paper states "more details in supplement" (line 217); the appendix was stripped by the parser. This is a known limitation.

7. **"Federated balance loss requires full-support sampling distribution" concern → Removed.** The paper explicitly states this requirement (Corollary 1: "let ν be some full-support probability distribution over pairs of terminal trajectories"). The critic's concern about zero support is already addressed.

8. **"Theorem 3 holds only for on-policy sampling" → Weakened to Nice-to-Have.** The paper acknowledges in Section 2 (line 49) that training uses an exploratory policy π. This gap between theory (on-policy) and practice (exploratory sampling) is standard in all GFlowNet training, not specific to this paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a brief discussion (even a paragraph) connecting the problem framing (clients won't share rewards) to the solution (clients share policies). Acknowledge that information leakage from policies is possible in principle, explain why sharing policies is still practically meaningful (e.g., policies are compressed representations, the server never sees R_n(x) directly, standard FL conventions), or scope the claim accordingly.

2. Include at least one experiment on a moderately larger state space (e.g., molecules with ~50 building blocks, or longer sequences of length 20+ with larger vocabularies) to build confidence in scalability. If this is too expensive, add a scaling plot showing error vs. state space size in a controlled synthetic setting.

3. Add error bars or confidence intervals to the CB comparison curves (Figure 6) and clarify the number of independent runs.

4. Replace or supplement the PCVI baseline with a method that is not trivially incapable — e.g., an ensemble distillation approach where samples from local GFlowNets are pooled and a single GFlowNet is trained on them, or a product-of-experts MCMC approach. This would make the comparison more informative.
