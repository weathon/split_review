## Summary

This paper introduces the *conditional causal bandit* problem, where a single-node conditional intervention on a causal graph is selected to maximize a reward variable $Y$. The central contribution is a formal graphical characterization of the minimal globally interventionally superior set (mGISS): Theorem 13 proves that the mGISS equals the LSCA closure of Pa($Y$), and the C4 algorithm computes it in $O(|V|+|E|)$ time. A supporting result (Proposition 4) shows that conditional-intervention superiority coincides with deterministic atomic-intervention superiority, enabling cleaner proofs. Experiments on random and real-world graphs show substantial search-space reduction, and bandit experiments confirm improved cumulative regret when using mGISS.

---

## Strengths

- **Theorem 13 (complete graphical characterization)**: The paper proves that mGISS$_Y(G)$ = $\mathcal{L}^\infty(\text{Pa}(Y))$, the LSCA closure of $Y$'s parents. This is a rigorous, closed-form answer to which nodes need to be tested in single-node conditional intervention causal bandits — a question not previously addressed.

- **Proposition 4 (conditional vs. deterministic atomic superiority)**: The equivalence $X \succeq_Y^c W \Leftrightarrow X \succeq_Y^{\det,a} W$ is non-obvious. Reducing the analysis of complex conditional interventions to simpler deterministic atomic interventions is a clever conceptual move that underpins the entire theoretical development.

- **C4 Algorithm (Theorem 16 — linear time, proven correct)**: The connector concept (Definition 14, Lemma 15) provides both a clean implementation handle and an intuitive correctness argument. Linear-time computation means the method is viable as a preprocessing step even for large graphs.

- **Empirical validation of pruning**: Section 6 demonstrates >90% reduction on several large `bnlearn` graphs and substantial regret reduction on the pathfinder dataset (109 nodes). The results are consistent with the theoretical predictions about graph sparsity and depth.

- **Λ-structure characterization (Theorem 12)**: The reformulation of the LSCA closure as $\Lambda(\mathbf{U}, \mathbf{U})$ — nodes forming a $\Lambda$-structure over pairs in $\mathbf{U}$ — gives a clean graphical language that ties together the proofs and the algorithm.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Non-standard regret proxy in Figure 3**: Footnote 11 states regret is computed against "the arm that most runs concluded to be the best at the end of training," not the true best arm. Since the bnlearn models come with known CPTs, the true optimal expected reward per node is computable via Monte Carlo from the SCM directly. The current proxy could yield inconsistent baselines if mGISS and brute-force converge to different consensus estimates — particularly on small graphs (asia, sachs) where convergence by the end of training may not be guaranteed. This does not undermine the theoretical result but makes the regret curves in Figure 3 less rigorous than they could be.

- **Target-node selection creates optimistic presentation**: In both random-graph and real-world experiments, $Y$ is always set to the node with the most ancestors (Footnote 8). This maximizes the pruning benefit of mGISS, so the reported reduction figures are upper bounds on what a practitioner targeting an arbitrary node would observe. A supplementary distribution of mGISS sizes across all possible target nodes (even for one or two representative graphs) would help calibrate reader expectations.

### Trivial
- The ancestor-observation assumption ($\text{An}(X)\setminus\{X\} \subseteq \mathbf{Z}_X$) is addressed in Footnote 3 and in the motivating examples but is presented primarily as a corollary of the no-latent-confounders assumption. While mathematically it is a separate requirement — a practitioner could lack measurements of some ancestors even without latent confounders — the paper is not wrong to subsume it in its stated scope. A single sentence flagging this explicitly as a distinct assumption would improve clarity.

---

## Nice-to-Haves

- **Fix the regret computation**: Computing true best-arm reward directly from the known bnlearn CPTs would make Figure 3 definitively interpretable rather than suggestive.

- **Distribution of mGISS sizes across target nodes**: Reporting median and worst-case reductions across all candidate target nodes for one or two real-world graphs would more honestly characterize practical pruning gains.

- **End-to-end C4 trace**: A worked example tracing Algorithm 1's execution on a non-trivial graph (beyond Figure 2b's static illustration) — showing connector propagation and node inclusion/exclusion — would help readers build intuition for Section 5.

- **Union under unknown graph**: The paper states in Section 1 that for unknown graphs, C4 can be run on each candidate and results unioned, but does not analyze how union size scales with the number of candidate graphs or whether the resulting union still provides guarantees under model uncertainty. A brief formal statement would sharpen this claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic (ancestor-inclusion as separate fatal limitation)**: The critic suggested the ancestor-observation assumption is unacknowledged and could change the mGISS characterization. The paper explicitly addresses this in Footnote 3 ("we are not claiming that all variables in $\text{An}(X)\setminus\{X\}$ need to be in $\mathbf{Z}_X$...but that we can always include them under the assumptions of our problem") and gives two concrete motivating examples where all ancestors are indeed observable. Demoted to Trivial.

- **Harsh critic (Erdős-Rényi DAGs produce trees at low density)**: While true, this is acknowledged and consistent with the paper's own analysis that sparse graphs benefit more from the method. Not a flaw.

- **Strength finder (comprehensive literature positioning)**: Partially generic — the differentiation from Lee & Bareinboim (2018/2019/2020) is substantive and concrete, but the broader claim of "thorough positioning" is standard academic practice. Removed as a standalone strength; the genuine novelty relative to prior work is already captured in the other strengths.

---

## Novel Insights

The equivalence between conditional-intervention superiority (probabilistic, complex policies) and deterministic atomic-intervention superiority (Proposition 4) is the most conceptually interesting finding. It reveals that the additional richness of conditional interventions — their ability to condition on observed context — provides no structural advantage in terms of *which node* to choose: the search-space reduction achievable by observing context is fully captured by the simpler deterministic atomic setting. This insight may have broader implications for other problems involving conditional vs. hard interventions in causal systems.

---

## Suggestions

1. Replace the consensus-estimator regret baseline with Monte Carlo–estimated true best-arm reward, using the known bnlearn CPTs. This is straightforward given the available SCM structure and would make Figure 3 unambiguous.

2. Add a figure (or even a short table) showing the distribution of $|\text{mGISS}_Y(G)| / |\text{An}(Y)\setminus\{Y\}|$ across all valid target nodes $Y$ for one representative real-world graph (e.g., child or pathfinder), to complement the current max-ancestor choice.

3. Briefly state a formal guarantee (even informal) for the union-of-mGISSs approach under unknown graphs, or explicitly defer it to future work with a clear statement of what remains unresolved.

---

## Score and Decision

**Originality**: The problem (conditional causal bandits, single-node) has not been studied before, and the characterization is novel. Strong. **(4/5)**

**Importance of research question**: Bridging causal graphs and contextual bandits is genuinely important; the preprocessing framing makes the result directly usable. **(4/5)**

**Claims well-supported**: Core theoretical claims are rigorously proved. Empirical claims are directionally correct but use a non-standard regret proxy. **(4/5)**

**Soundness of experiments**: Adequate for a theory paper; the regret proxy and target-node selection are the main issues but do not invalidate the conclusions. **(3/5)**

**Clarity of writing**: Well-organized, intuition sections are helpful, definitions are precise, examples match theorems. **(4/5)**

**Value to the research community**: Provides a complete characterization and a practical linear-time algorithm for a natural problem; the preprocessing framing maximizes reuse. **(4/5)**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>