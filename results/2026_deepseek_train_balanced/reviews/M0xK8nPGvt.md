## Summary

This paper proposes C-PSRL, a hierarchical Bayesian algorithm that extends Posterior Sampling for Reinforcement Learning (PSRL) to exploit prior knowledge expressed as a *partial* causal graph over environment variables. Rather than requiring practitioners to specify parametric prior distributions, the method takes a causal graph with known edges, considers all factorizations of the transition dynamics consistent with it, and performs hierarchical posterior sampling over both the factorization space (hyper-prior) and the transition parameters (lower-level prior). The paper provides a Bayesian regret bound that explicitly connects the degree of prior knowledge $\eta$ (number of known causal edges per variable) to an exponentially improved $\tilde{O}(\sqrt{K/2^\eta})$ term, an ancillary weak causal discovery result, and empirical validation in two small domains.

## Strengths

1. **Regret bound quantifying the benefit of causal prior knowledge (Theorem 1).** The bound $\tilde{O}((H^{5/2} N^{1+Z/2} d_Y + \sqrt{H \, 2^{d_X-\eta}})\sqrt{K})$ explicitly decomposes regret into a term for learning the transition model under the true factorization and a term $\tilde{O}(\sqrt{K/2^\eta})$ for learning the factorization itself. Step 3 of the proof (lines 208–211) cleanly derives $\max_j |\mathcal{Z}_j| \leq 2^{d_X-\eta}$, directly linking each known causal edge to an exponential reduction in the latent hypothesis space. This goes beyond prior FMDP-PSRL work (which assumes the full graph is known) and hierarchical PSRL work (which does not connect regret to causal edge counts).

2. **Empirical demonstration that C-PSRL nearly matches oracle performance in the Random FMDP domain (Figure 1a–b).** C-PSRL achieves regret "surprisingly close to F-PSRL" (which receives the full oracle causal graph), while significantly outperforming vanilla PSRL. The model-error plot (Figure 1b) confirms that C-PSRL's sampled transition models converge in $\ell_1$ distance nearly as fast as the oracle's, providing concrete evidence that the hierarchical sampling procedure can recover the true factorization from a partial graph prior.

3. **Weak causal discovery as a byproduct of regret minimization (Corollary 1).** The paper proves that after $\tilde{O}(H^5 d_Y^2 2^{d_X-\eta}/\epsilon^2)$ episodes, C-PSRL recovers a $Z$-sparse super-graph of the true causal graph under $\epsilon$-value minimality. This connects regret minimization to causal structure learning in a way that (while admittedly weak — super-graph, not exact graph) is a novel ancillary contribution.

4. **Independent parent sampling reduces hyper-prior complexity (Section 3, lines 164–166).** By exploiting the bipartite causal structure (no "vertical" edges among state variables), C-PSRL samples parents $z_j \in \mathcal{Z}_j$ independently per variable $Y_j$, avoiding a combinatorial explosion in hyper-prior parameters. This is a concrete algorithmic design choice that makes the approach computationally feasible.

5. **Scaling advantage over PSRL in larger state spaces (Figure 1d).** In the Taxi $5 \times 5$ domain, PSRL suffers linear regret after 400 episodes while C-PSRL converges to a good policy, demonstrating that the advantage of exploiting partial causal knowledge grows with problem complexity.

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm critically under-specified — the core prior and posterior updates are not defined.** Algorithm 1 (lines 141–152) states "Build the hyper-prior $P_0$ and the prior $P_0(\cdot|z)$ for each $z \in \mathcal{Z}$" (line 146) and "Compute the posteriors $P_{k+1}$ and $P_{k+1}(\cdot|z)$ with the collected data" (line 151), but the paper never specifies what parametric form either distribution takes. Is the hyper-prior a categorical distribution over $\mathcal{Z}$ (with what parameters)? Is the lower-level prior a product of Dirichlet distributions over conditional probability tables? How are evidence at episode $k$ used to update each $z \in \mathcal{Z}$ differently depending on whether $z$ is compatible with observed transitions? None of this is provided. The paper states "closed-form posterior updates" exist (line 158) without giving them. Extending the hierarchical Bayesian framework of Hong et al. (2022) from tabular MDPs to FMDPs with partial causal graphs requires concrete design choices that the paper leaves entirely to the reader. A reader cannot implement C-PSRL from this paper alone.

2. **Core motivation gap: the paper claims to avoid parametric priors but does not show how the causal graph bypasses them.** The paper argues that specifying parametric priors for PSRL "can be cumbersome in practice" (abstract, line 18) and that a causal graph prior is "more natural to specify for practitioners" (line 21). Yet C-PSRL still requires the practitioner (or algorithm) to specify parametric prior distributions at two levels: a hyper-prior over $\mathcal{Z}$ and a lower-level prior $P_0(\cdot|z)$ for each factorization $z$ (line 146). The paper never explains how these parametric distributions are *automatically derived* from the causal graph, nor does it provide a default construction (e.g., uniform over consistent factorizations, uniform Dirichlet for transitions). Without this, the claimed practical advantage — that practitioners can avoid "the intricacies of Bayesian statistics" (line 21) — does not survive the method's own requirements.

3. **No empirical validation of the paper's central theoretical claim: the $\eta$ dependency is not tested.** Theorem 1's key contribution is the $\tilde{O}(\sqrt{K/2^\eta})$ term, which predicts that regret decreases exponentially as the number of known causal edges $\eta$ increases. Yet $\eta$ is fixed at 2 throughout *all* experiments. There is no ablation varying $\eta = 0, 1, 2, \dots$ to verify that regret actually decreases with more prior knowledge. This is a significant gap between theory and empirical validation — the main theoretical insight goes untested.

### Minor

1. **Narrow experimental scope.** Only two domains are tested, both very small (Random FMDP: $d_X=9, d_Y=6, N=2$; Taxi: $d_X=5, d_Y=4$). While the paper appropriately calls them "illustrative domains," the evaluation lacks a comparison against any method that learns the factorization from data without a prior — such as Rosenberg et al. (2021), which is cited in the paper (line 310) — that would demonstrate the prior confers a practical advantage over learning from scratch. The Random FMDP evaluation also samples instances from the same prior class C-PSRL assumes, which tests internal consistency but not robustness to prior misspecification.

2. **F-PSRL (oracle) comparison omitted from Taxi.** The paper states F-PSRL is "omitted as the knowledge of the oracle prior is not available" (line 258), but Taxi is a simulated environment with known dynamics. Constructing the true factorization (taxi row, taxi column, passenger status, destination) and running F-PSRL would have provided a valuable oracle baseline in a realistic domain.

3. **Regret bound looseness under-discussed.** The first term $H^{5/2} N^{1+Z/2} d_Y$ is substantially worse than the known FMDP-PSRL bound $\tilde{O}(H d_Y^{3/2} N^{Z/2} \sqrt{K})$ from Osband et al. (2014) — an extra factor of $H^{3/2}$ and $N$. The paper acknowledges this (line 218: "additional factors of $H$ and $N$") but does not discuss whether this looseness is inherent to the hierarchical analysis or can be tightened. The second term $\sqrt{H \, 2^{d_X-\eta}}$ is exponential in $d_X-\eta$, which for realistic feature counts could dominate; the practical implications are not explored.

4. **Strong assumption for the weak causal discovery result.** The $\epsilon$-value minimality assumption (Definition 1) requires that *any* proper subgraph of the true causal graph reduces the optimal value by at least $\epsilon$. This is a strong condition — many causal edges may have negligible effect on optimal value in practice. The paper is transparent about this being an ancillary result with "weak" discovery (super-graph only), but does not discuss whether the assumption is reasonable in the motivating DTR example.

### Trivial
None.

## Nice-to-Haves
- An ablation varying $\eta$ (e.g., $\eta = 0, 1, 2, \dots, Z$) in the Random FMDP domain to empirically validate Theorem 1's $\sqrt{K/2^\eta}$ dependency.
- Explicit default prior constructions (e.g., uniform over $\mathcal{Z}$, product-of-Dirichlets for $P(\cdot|z)$) automatically derived from the causal graph, with closed-form posterior update formulas.
- A comparison against at least one method that learns the FMDP factorization from data without a prior (e.g., Rosenberg et al. 2021).
- Discussion of what happens when the causal graph prior is misspecified ($\mathcal{G}_0 \not\subseteq \mathcal{G}_*$).
- Empirical measurements of C-PSRL's computational cost as a function of $d_X, d_Y, Z$.

## Removed Points
These points were flagged for potential removal; treat with caution.

- *"The Random FMDP experiment is circular"* (Harsh Critic #3 sub-point). The paper evaluates C-PSRL on instances sampled from the prior — this is standard Bayesian evaluation methodology that tests whether the algorithm is consistent with its own assumptions. It is not circular; it is the appropriate evaluation paradigm for a Bayesian algorithm. **Removed.**

- *"500 episodes is a very short horizon"* (Harsh Critic #3 sub-point). There is no evidence this is too short for the given small domains. The results show learning occurring within this horizon. **Removed** as speculative.

- *"The regret bound has structural issues that are under-discussed"* (Harsh Critic #4). The bound's looseness is acknowledged by the paper. The extra $H^{3/2}$ and $N$ factors are real but the paper's contribution is in the *second* term ($\sqrt{K/2^\eta}$), which is novel. **Demoted to Minor.**

- *"The causal discovery ancillary result rests on a strong, unvalidated assumption"* (Harsh Critic #5). The paper calls this an "ancillary result" and explicitly labels the discovery "weak" (super-graph). The $\epsilon$-value minimality assumption is strong but the paper is transparent about it. **Demoted to Minor.**

- *Generic strength about "the problem being important"* (Strength Finder). These are not specific to this paper's contributions. **Removed.**

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Fully specify the prior construction: provide explicit formulas for $P_0$ (e.g., uniform over $\mathcal{Z}$) and $P_0(\cdot|z)$ (e.g., product of Dirichlet distributions over each conditional probability table $p_j(\cdot|x[z_j])$), and derive the closed-form posterior updates. This is essential for the method to be taken as a concrete algorithmic contribution.
2. Add an empirical ablation varying $\eta$ across multiple values (e.g., $\eta = 0, 1, \dots, Z$) in the Random FMDP domain to validate Theorem 1's central prediction.
3. Provide a default construction showing how the causal graph $\mathcal{G}_0$ is automatically converted into default parametric priors without requiring practitioner choices — this would resolve the motivation gap.
4. Add the F-PSRL oracle baseline to the Taxi experiment (the true factorization is known from the domain structure).
5. Discuss what happens under prior misspecification ($\mathcal{G}_0 \not\subseteq \mathcal{G}_*$), as this is a realistic concern.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>