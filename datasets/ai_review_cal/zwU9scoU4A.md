- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary
This paper introduces Graphex Mean Field Games (GXMFGs), a framework that extends mean field games to sparse graph sequences (power-law networks) using graphex theory, where most agents have finite degree — unlike graphon-based MFGs that require all agents to have infinite-degree neighbors in the limit. The authors propose a hybrid learning algorithm (HOMD) that exploits the core–periphery structure induced by sparsity, prove convergence and approximate optimality guarantees (Theorems 1–4), and validate the method on synthetic graphs and 8 real-world networks.

## Strengths
- **First formalization of MFGs on sparse graphs with finite-degree agents.** The paper rigorously defines GXMFGs using graphexes, which model power-law degree distributions and finite-degree periphery agents, whereas graphon MFGs and LPGMFGs only capture dense (or near-dense) graph sequences where all agents have diverging degree. This is a genuine theoretical advance (Section 2, Section 3).

- **Theoretical approximation guarantees for the finite-ν system.** Theorems 1–4 prove that the empirical mean field of the finite graph converges to the limiting GXMFG mean field and that the limiting policies form an approximate Nash equilibrium for large ν. These results are specific to the graphex setting and go beyond what is available for GMFG or LPGMFG on sparse graphs.

- **Hybrid learning algorithm exploiting core–periphery structure.** Algorithm 1 (HOMD) is a well-motivated design: core agents are handled via online mirror descent with discretization into M equivalence classes, while periphery agents (who do not influence core neighborhoods) are solved as standard MDPs via backward induction. This structural decomposition is a direct consequence of sparse graphex topology.

- **Evaluation on 8 real-world networks.** Table 1 reports expected total variation between the predicted GXMFG mean field and the empirical mean field on networks ranging from ~47k to ~2.3M nodes. SIS and RS models achieve TV errors mostly under 5%, and SIR errors are under 5% on 4 of 8 networks. This level of real-network validation is rare in the MFG literature.

## Weaknesses

### Fatal
None.

### Major
- **No baseline comparison to GMFG, LPGMFG, or other MARL/MFG methods.** The paper's central motivation is that GXMFGs are needed because graphon-based methods cannot handle sparse networks. Yet the synthetic experiments compare only against naive fixed-point iteration (FPI), and the real-network experiments report only absolute TV errors. The paper claims (line 268) that GXMFGs have "a crucial advantage over existing GMFG and LPGMFG models, both conceptually and empirically" — but no experiment demonstrates that GMFG or LPGMFG actually performs worse on the same data. While the theoretical inapplicability of graphons to sparse graphs is formally established in graph theory, the empirical claim that GXMFGs provide a *practical* advance over alternatives is left unsupported. Adding even a reasonable baseline (e.g., running a dense graphon MFG solver on the same networks by treating edges as uniformly likely, or comparing against a standard MFG that ignores network structure) would substantiate or temper this claim.

- **Hyperparameter selection (α^*, M, k_max) is not justified or analyzed.** The core cutoff α^*, the number of equivalence classes M, and the periphery degree cutoff k_max are all free parameters of the algorithm, yet the paper provides no guidance on how to choose them, no sensitivity analysis, and no ablation study. The theoretical results guarantee existence of some α' and ν' for the asymptotic approximation, but the practical algorithm must fix concrete values. Since the core–periphery split is the central algorithmic innovation, the lack of any empirical study of sensitivity to these choices is a significant methodological gap.

- **Full-system exploitability is not measured on real networks.** On real networks, the reported metric is the total variation between the predicted mean field and the empirical mean field under the learned policy. A low TV indicates mean-field consistency but does not measure how close the policy is to a Nash equilibrium of the finite game. The exploitability metric is only computed for the core in synthetic experiments (Figure 2). Without any optimality measure on real networks (or comparison to a baseline's TV), the paper cannot distinguish between an accurate equilibrium approximation and a self-consistent but suboptimal prediction. This weakens the evidence for the claimed equilibrium quality.

### Minor
- **Approximation error propagation is not analyzed.** The core equilibrium is approximated via OMD with discretization into M groups (line 194), and the periphery uses the approximate core MF to compute Q-values. The theoretical optimality theorems (Theorems 5–6) assume a *limiting* MFCE, not an approximate one. The paper cites existing OMD guarantees but does not discuss how discretization error (finite M) or OMD convergence tolerance affects the overall finite-system approximation quality. This gap between the asymptotic theory and the implemented algorithm is not acknowledged.

- **Computational details of the periphery MDP are underspecified.** The periphery dynamics involve a combinatorial neighborhood space 𝒢^k of possible compositions. For moderate k, this space is enormous, yet the paper does not specify how the expectation over neighborhoods is computed or approximated (lines 135–146, 221). Similarly, the graph sampling procedure for synthetic experiments (how ν is chosen, how the Poisson process is implemented in practice) is described only at the theoretical level (Section 2) without experimental parameters. These gaps hinder reproducibility.

- **The role of the stretched canonical graphon in the algorithm is unclear.** The theoretical convergence results rely on the stretched cut metric and the stretched empirical graphon (Section 2), but the learning algorithm works directly with the separable power-law graphex, never using the stretched graphon. The connection between the theoretical convergence framework and the algorithmic design could be clarified to avoid the appearance of a gap between the two.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the full HOMD algorithm to a version that applies vanilla OMD to the entire system (without the periphery MDP) would isolate the benefit of the hybrid design.
- A computational complexity analysis comparing the cost of HOMD (M core classes + k_max periphery MDPs) to alternative approaches would strengthen the paper's practical positioning.
- The paper acknowledges that some networks (e.g., Hyves) may not fit the separable power-law form well (line 270). This limitation could be elevated and discussed more explicitly, since the method's success depends on this modeling assumption.

## Removed Points
- **"α^* appears only in the theory without guidance for implementation"** — Already incorporated into Major weakness 2.
- **"Intermediate nodes 'negligible' depends on asymptotic limits not quantified"** — This is part of Major weakness 2; the hyperparameter sensitivity concern subsumes it.
- **"No formal argument why GMFG/LPGMFG cannot be applied"** — The paper does provide this argument (lines 13–15, citing graphon theory); the issue is the lack of *empirical* comparison, not the formal argument. Demoting from the critic's framing: the gap is empirical, not formal.
- **Strength Finder's "expected total variation mostly below 5%"** — While the SIS and RS results are mostly below 5%, SIR exceeds 5% on 4 of 8 networks (Flickr 8.58%, Brightkite 10.92%, Facebook 13.57%, Hyves 10.06%). The strength is retained but rephrased more accurately.
- **"Weaknesses about missing appendix/truncated sections"** — The parser may have stripped these; the original submission likely contains them.

## Novel Insights
The Harsh Critic's observation that the evaluation measures *mean-field consistency* rather than *equilibrium quality* on real networks is genuinely insightful and not something the paper itself addresses. The TV metric validates the forward model (the predicted distribution of agent states matches the observed distribution) but says nothing about whether agents are playing optimally — the exploitability metric used on synthetic data (Figure 2) would be the appropriate measure, yet is absent on real networks. This is a nontrivial observation because mean-field consistency can hold even under suboptimal policies (e.g., if the dynamics are determined primarily by the model, not by agent optimization). The paper would benefit from acknowledging this distinction explicitly.

## Suggestions
1. **Add at least one baseline comparison on real networks.** The most actionable option: construct a graphon approximation of each real network (e.g., via stochastic blockmodel fitting) and run a standard GMFG solver. Even if the GMFG baseline is clearly inapplicable (since the graphs are sparse), showing quantitatively that it produces worse TV errors or fails to converge would directly substantiate the claim of "crucial advantage."
2. **Report exploitability (or an approximation) on real networks**, or at minimum compare to the exploitability of a uniform-random policy to calibrate the TV numbers.
3. **Provide a sensitivity analysis** for α^*, M, and k_max — even a brief ablation on one network would significantly increase confidence in the algorithm's robustness.
4. **Specify how 𝒢^k enumeration or sampling is handled** in practice, along with the experimental parameters (ν values, M used, α^* values) for the synthetic experiments.
