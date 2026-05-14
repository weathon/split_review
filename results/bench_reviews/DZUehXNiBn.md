## Summary

This paper proposes VISTA, a modular framework for causal structure learning that decomposes the global DAG learning problem into per-node Markov Blanket subgraphs, runs arbitrary base learners on each subgraph, aggregates edge-direction evidence via an exponential-decay weighted voting scheme, and enforces acyclicity through a greedy Feedback Arc Set heuristic. The framework is model-agnostic, parallelizable, and operates purely at the edge level. The authors provide finite-sample error bounds and an asymptotic consistency result for the weighted voting aggregation, and demonstrate consistent improvements in FDR (50–80% reduction) and runtime across six base learners, multiple graph families, and scales up to 300 nodes.

## Strengths

- **Model-agnostic modular design with broad empirical validation**: VISTA operates purely on edge-level outputs and imposes no assumptions on base-learner inductive biases. It is demonstrated plug-and-play with NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, and CAM across linear and nonlinear data (Table 1, Table 2, Appendix F.4). The coverage guarantee of Proposition 3.1 ensures no true edge is lost in the decomposition.

- **Substantial empirical accuracy and runtime gains**: Across all tested base learners, graph types (ER, SF), and scales (n=30–300), VISTA-WV reduces FDR by 50–80% relative to standalone baselines while keeping TPR ≥ 0.70 (Table 1). Parallel subgraph processing yields significant runtime reductions (Table 3; e.g., NOTEARS from 1473s to 1097s at n=100, GOLEM from 109s to 26s).

- **Retraining-free hyperparameter sweeps**: Because λ appears only in the final aggregation, the precision–recall trade-off can be explored by simply recomputing scores from cached votes without retraining any base learner. The paper uses a single fixed operating point (λ=0.5, t=0.7) across all experiments, avoiding per-dataset tuning, and reports full sweep curves for transparency (Figure 4).

- **Clear ablation via naive voting baseline**: The naive voting (NV) variant quantifies the recall boost from overlapping Markov Blankets alone, while the weighted voting (WV) adds calibrated filtering. The enormous gap between NV (FDR~0.85) and WV (FDR~0.08–0.35, Table 1) convincingly isolates the contribution of the exponential weighting.

- **Modest but positive real-data signal**: On the Sachs protein-signaling network (11 nodes), VISTA reduces SHD and SID relative to baseline solvers (Table 4), providing some evidence of real-world applicability despite the small scale.

## Weaknesses

### Major

- **Theoretical analysis rests on an independence assumption that does not hold for the actual method**: All probabilistic bounds (Theorems 3.2, 3.4, 3.5; Lemma E.1) treat votes from different local subgraphs as independent binomial trials. In practice, subgraphs are learned from the same dataset with heavily overlapping variable sets, so directional decisions are strongly dependent. The paper acknowledges this (lines 405–409: "the bound should be interpreted as a qualitative guide") but continues to present the bounds as formal guarantees and advertises them as a key contribution. The asymptotic consistency result (Theorem 3.5), which is the paper's central theoretical claim, rests entirely on this same independence model. No analysis is provided for how dependence affects the error bounds, nor is there empirical investigation of vote correlations. This substantially weakens the theoretical contribution.

- **Asymptotic consistency condition is inconsistent with the framework's structural properties**: Theorem 3.5 requires m (subgraphs per candidate edge) to grow as C log n. However, the paper's own structural analysis (Appendix E.2) shows that for Erdős–Rényi graphs, m_ij concentrates around 2 with occasional Poisson increments that vanish as n grows. The Markov-blanket decomposition proposed by VISTA does not produce m growing logarithmically with graph size. The asymptotic guarantee therefore does not describe the behavior of VISTA as implemented, and the claim that "the required number of independent subgraphs per edge grows only logarithmically with the graph size" (line 474–475) is misleading when applied to the proposed method.

### Minor

- **λ choice does not clearly satisfy the theoretical interval**: The paper claims λ=0.5 lies within the feasible interval from Theorem 3.4 (Equation 5). For edges with the typical support count m=2 identified in Appendix E.2, the lower bound is λ > 0.60 (at t=0.7), which λ=0.5 does not satisfy. The paper does not specify which value of m was used to verify the claim. Since the theory is already acknowledged as a qualitative guide, this inconsistency is not fatal but it erodes precision in connecting theory to practice.

- **Markov Blanket identification method is not specified**: The entire divide step depends on accurate MB detection, and while the framework is agnostic to the choice of MB estimator, the experiments must have used a specific one. The omission obscures the sensitivity of VISTA to MB errors and limits reproducibility. The discussion of MB stability (Figure 1) is described as an empirical observation but the actual identification algorithm is unnamed.

- **No comparison to simpler confidence-weighting baselines**: The paper compares only against naive (unweighted) voting. A natural control—thresholding on raw proportion A/m with a minimum-count rule, or a linear penalty on m—would isolate whether the specific exponential form 1−e^(−λm) provides benefit beyond a more conventional confidence-based pruning. Without this, the exponential design choice is justified only by the theoretical derivation (which is under an independence assumption) and the Bayesian prior interpretation (Appendix D.1), not by comparative evidence.

- **Real-data evaluation is limited**: The Sachs network experiment (Table 4) uses only 2 base learners and 11 nodes. TPR drops for both baselines when VISTA is applied, and the SHD/SID improvements are modest (SHD: 16→16 and 18→15). Claims of consistently improving structural accuracy across arbitrary algorithms are not convincingly supported from this single small-scale network.

### Trivial

- The presentation of the theoretical bounds in the main paper is notationally dense and could benefit from a clearer separation between results that hold under the independence assumption and practical guidance.

## Nice-to-Haves

- An empirical investigation of vote correlations across subgraphs, and a sensitivity study of the error bounds under simulated dependent votes, would substantially strengthen the credibility of the theoretical motivation.
- An ablation where MB identification is deliberately weakened (e.g., using a noisier estimator) to show how robust VISTA is to MB estimation quality.
- A visualization of a full-pipeline example on a medium-sized synthetic graph showing the original MB subgraphs, weighted scores, and the final graph after FAS and filtering.

## Removed Points

These points were raised by reviewers but are removed from the main review for the stated reasons:

- **"The theoretical guarantees are founded on an unrealistic independence assumption, rendering the claimed error bounds non-credible"** — The paper explicitly acknowledges this limitation (lines 405–409: "the bound should be interpreted as a qualitative guide") and frames it as future work. The point is retained as a major weakness above but with the acknowledgment noted, and reclassified from "structural/fatal" to "major" because the paper is transparent about the limitation.

- **"The naive voting variant produces catastrophically high FDR"** — This is presented as a finding of the paper itself, not as a hidden flaw. The paper correctly uses NV to demonstrate why weighted voting is necessary. Not a weakness.

- **"GreedyFAS errors are not accounted for in global error bounds"** — The paper acknowledges this in the conclusion (lines 829–831): "the FAS projection guarantees acyclicity, it may also prune edges that are weakly supported yet correct." The limitation is disclosed. Moved from a major criticism to a noted limitation.

- **"Comparison with DCILP" / "missing baseline comparisons"** — The paper does compare with DCILP (Table 5 in Appendix F.2). 

- **"Undirected edges are partially wasted"** — The paper explicitly addresses this (lines 233–235): "If an undirected adjacency X−Y is returned, it is treated as providing no directional vote in the aggregation." This is by design.

- **Formatting/style/typo complaints** — These are parser artifacts, not author errors.

- **"Missing appendix" / "missing proofs"** — The parser strips appendix sections; they exist in the original submission (the paper references Appendices D, E, F extensively).

- **Strength Finder claim about "rigorous theoretical guarantees for aggregation"** — Weakened substantially by the independence assumption caveat. Dropped as a standalone strength.

- **Strength Finder claim that "λ=0.5, t=0.7 lies within (5)"** — Kept as a minor weakness due to the m=2 discrepancy noted above.

## Novel Insights

None beyond the paper's own contributions. The divide-and-conquer via Markov Blankets with exponential-decay voting is a sensible combination, and the retraining-free λ sweeping from cached votes is a practically useful observation, but neither constitutes a novel insight beyond what the paper itself presents.

## Suggestions

- Either replace the current theoretical presentation with an analysis that does not rely on independence (e.g., using dependency-aware concentration inequalities), or explicitly reframe the bounds as idealized illustrations and remove claims of formal error control and asymptotic consistency for the actual method. The current presentation overclaims given the acknowledged caveat.
- Specify the MB identification algorithm used in experiments and discuss its expected error characteristics. Even a brief note in the experimental setup would substantially improve reproducibility.
- Add a simple linear or minimum-count baseline (e.g., retain edge if A/m ≥ t' and m ≥ m_min) to isolate the benefit of the exponential form. This is a low-cost addition that would strengthen the empirical argument.
- Expand the real-data evaluation beyond Sachs, or acknowledge the limited scope of that evaluation more explicitly.

## Score Calibration

Anchor papers compared:

- **WtbPaWO8lH** (avg 6.00): Voting-theoretic ensemble for causal discovery. Similar theoretical limitations acknowledged; comparable empirical breadth. VISTA has broader base-learner coverage and runtime analysis, but its theory-practice gap (asymptotic condition not met by the method) is more severe. VISTA is slightly below this anchor.
- **N9RyL52z7y** (avg 4.50): Ensemble CI test, divide-and-aggregate framework with solid experiments but limited novelty. VISTA has broader applicability, more baselines, and more significant empirical gains. VISTA is above this anchor.
- **3lFAyPa9Fe** (avg 4.00): Agentic divide-conquer framework with multiple experimental and presentation weaknesses. VISTA is clearly above this anchor.
- **lejOV6j3cj** (avg 5.00): FLOP algorithm with strong empirical results on linear data, some theoretical backing, limited to linear models. VISTA is model-agnostic and has broader applicability but weaker theory. Comparable contribution level.
- **mA78uXqcnl** (avg 7.00): Strong theoretical contribution with novel identifiability results for Hawkes processes. VISTA is clearly below this anchor.
- **vSAWV43kvs** (avg 3.00): Severely limited foundation model approach with misleading framing. VISTA is clearly above this anchor.
- **RCdjovlkbl** (avg 3.50): Theoretical analysis of causal inference in GRL. VISTA is above this anchor.
- **vaMVik1WmL** (avg 4.80): FastKCI, a scalable kernel-based CI test. Similar divide-and-conquer motivation. VISTA is comparable or slightly above.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>