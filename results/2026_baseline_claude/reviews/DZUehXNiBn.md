Now I have the full paper content. Let me write my review.

---

## Summary

VISTA (Voting-based Integration of Subgraph Topologies for Acyclicity) is a modular, model-agnostic framework for large-scale causal structure learning. It decomposes the global DAG learning problem into overlapping local subproblems via Markov Blanket (MB) identification, applies any off-the-shelf base learner to each subgraph in parallel, and integrates local directed edges through an exponentially-weighted voting scheme followed by a Greedy Feedback Arc Set (FAS) step to enforce acyclicity. The paper provides finite-sample error bounds and an asymptotic consistency result, supported by extensive synthetic experiments with six diverse base learners and one real-world evaluation.

---

## Strengths

- **Practical model-agnosticity demonstrated convincingly**: VISTA wraps six structurally different base learners (CAM, NOTEARS, DAG-GNN, GOLEM, SCORE, GraN-DAG) spanning continuous-optimization, score-based, and neural approaches. Improvements in SHD/F1 are consistently observed across all combinations (Tables 1–2), confirming that gains come from the aggregation rule rather than any particular estimator.

- **Substantial and consistent runtime reduction**: Table 3 shows 3–11× speedups at n=300 for all tested learners. Because subproblems are independent, the acceleration is architectural (parallelism) rather than algorithmic, and the trend scales convincingly with n.

- **Theoretically grounded voting calibration**: Theorem 3.4 provides an explicit admissible interval for λ (Eq. 5) that translates into concrete guidance for practitioners. The sensitivity study in Figure 4 confirms the predicted smooth precision–recall trade-off, and the single fixed operating point (λ=0.5, t=0.7) is not post-hoc selected but declared in advance. This is an unusually honest experimental design choice.

- **Clean coverage guarantee**: Proposition 3.1 (every true edge appears in at least one MB subgraph) is a trivial but essential correctness prerequisite; its explicit statement provides a clear foundation for the entire pipeline and links the decomposition soundly to the aggregation.

---

## Weaknesses

### Fatal
None. The core empirical claims—consistent improvement in F1/SHD and runtime reduction—are not invalidated by any identified flaw.

### Major

1. **The independence assumption in the theoretical core is structurally violated.** Theorem 3.2 (and the asymptotic consistency result that inherits from it, Theorem 3.5) assumes votes from different local subgraphs are independent Bernoulli trials. But by construction, overlapping MB neighborhoods share both data points and shared nodes, inducing non-trivial correlation among edge votes. The paper acknowledges this and suggests treating the result as "qualitative," but this caveat substantially weakens the paper's theoretical contribution. The sample-complexity bound (Corollary 3.3) and the log-n scaling for consistency (Theorem 3.5) cannot be taken quantitatively under dependent votes. The theory needs either a formal dependency structure analysis (e.g., graph-dependent mixing conditions, or union bounds over only non-overlapping subsets), or the claims should be more carefully scoped as heuristic guidance.

2. **Asymptotic consistency requires p > t and q < t (δ_p, δ_q > 0), but these are not mild conditions in practice.** For a weak base learner like GraN-DAG (Table 1: baseline F1=0.06 on ER5, n=100), it is entirely plausible that q ≥ p for certain edge types, breaking the theorem's premise. The paper claims "our assumptions are quite mild and practically easy to satisfy" (Sec. 3.2), but provides no empirical calibration of p and q for any experiment to verify this claim holds even approximately.

3. **NV is consistently worse than the unaided baseline across nearly all metrics and should not be presented as a meaningful framework variant.** In Table 1, every NV row has FDR in [0.84, 0.95] — far exceeding the baseline — while F1 collapses to [0.06, 0.27]. The text correctly explains why (NV cannot distinguish strong from weak support), but then spends significant space on NV in Section 3.1 as a stepping stone concept. As presented, NV misleads readers into thinking VISTA has two usable modes when it effectively has one.

### Minor

1. **The comparison with DCILP is deferred to the appendix**, yet DCILP is the closest algorithmic competitor identified in the introduction and related work. Given that DCILP's main weakness is claimed to be solver overhead, placing the head-to-head comparison in an appendix makes it hard to validate the efficiency claims against the most natural baseline.

2. **Sole real-data experiment is on an 11-node graph (Sachs).** The Sachs network is nearly small enough that any reasonable method will find it trivially; MB identification on 11 nodes is exact. This makes it impossible to assess whether VISTA's scalability and robustness claims hold in real (non-synthetic) settings at n ≥ 100. A gene regulatory network or biological network with ≥ 50 nodes would be a stronger validation.

3. **VISTA-WV sometimes offers only marginal improvement over the base learner.** For NOTEARS on ER5 (n=100, Table 1), the F1 improvement is 0.76 → 0.79. The paper discusses percent reductions in FDR (50–80%) but these figures are calculated relative to cases with large absolute FDR. For already-competitive baselines, the benefit is minor.

4. **The latent confounding problem from subgraph restriction is acknowledged but not mitigated.** Restricting the learner to the MB subgraph induces unobserved confounders (non-MB parents), which can produce spurious edges with high confidence. The paper notes this limitation and states that FAS + thresholding "can mitigate part of these redundant edges," but offers no empirical analysis of how often these confounded edges survive into the final graph.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An analysis of how MB estimation error propagates: even a simple ablation varying MB quality (e.g., by using MBs with controlled recall/precision) would clarify how robust the framework is to imperfect decomposition.
- Providing at least an approximate form of the consistency result under weakly dependent votes (e.g., using m-dependence or graphical decay of correlations) would rescue much of the theoretical contribution.
- Including the DCILP comparison in the main body with matched experimental settings.

---

## Novel Insights

The paper's most genuinely novel observation is the role of the exponential weight (1 − e^{−λm}) as a soft confidence modulator: unlike hard-threshold voting, it smoothly interpolates between ignoring and fully trusting edge votes as a function of total co-occurrence m. The resulting smooth precision–recall trade-off (Figure 4), which plateaus exactly when the weight saturates to 1, offers practitioners a theoretically principled and empirically validated single hyperparameter to sweep post-hoc without rerunning base learners. This reuse of cached vote counts—yielding a retraining-free operating-point sweep—is practically attractive and not present in prior MB-based frameworks.

---

## Suggestions

- Formally quantify or bound the correlation among subgraph votes using the graph's spectral or topological properties, or restrict the theoretical claims to non-overlapping partitions where independence is exact.
- Calibrate p and q empirically for each (base learner, graph family) pair and verify δ_p, δ_q > 0 before invoking Theorem 3.5.
- Move the DCILP comparison to the main experimental section and include runtime alongside accuracy metrics.
- Add at least one real-data experiment with n ≥ 50 (e.g., a subset of a curated gene network).
- Either remove the NV variant from Table 1 or reframe it purely as a recall upper bound rather than a usable algorithm.

---

## Score and Decision

VISTA is a practical, well-engineered framework that consistently reduces computational cost and improves causal discovery accuracy across a broad range of base learners. The weighted-voting design is clean, the precision–recall analysis is transparent, and the fixed-hyperparameter evaluation discipline is commendable. The major limitation is a theoretical one: the independence assumption at the heart of the finite-sample and asymptotic guarantees is structurally violated by the overlapping MB design, and the paper's caveat ("interpret as qualitative") does not resolve this gap. The real-data evaluation is also very limited. Nonetheless, the empirical contribution stands on its own and the framework is likely to be useful to practitioners working on large-scale causal discovery.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>