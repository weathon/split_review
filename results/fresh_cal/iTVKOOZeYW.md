Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper proposes ψDAG, a framework for DAG structure learning that replaces the expensive matrix-exponential-based acyclicity constraints (O(d³) per iteration from NOTEARS/GOLEM/DAGMA) with a low-cost projection heuristic (O(d²)). The method alternates between unconstrained SGD, a heuristic projection that finds a "closest" topological ordering via row/column norm minimization, and constrained SGD that respects that ordering. Experiments show ψDAG scales to 10,000-node graphs where baselines exceed 36 hours for d>3,000, and it achieves modestly better structural accuracy on the 11-node Sachs protein signaling benchmark.

## Strengths

- **Scalability to 10,000 nodes empirically demonstrated.** Figures 3 and 4 (Section 5) show ψDAG converging within hours for graphs up to d=10,000 under ER2, SF2, and ER6 settings with Gaussian noise, while NOTEARS, GOLEM, and DAGMA exceed 36 hours (the allocated time limit) for d≥3,000. This provides direct evidence that the O(d²) per-iteration complexity translates into practical large-scale performance.

- **Low iteration complexity via O(d²) projection.** The projection method (Algorithm 2/alg:proj) is described as O(d²) cost (line 219), replacing the O(d³) per-iteration cost of the matrix exponential h(W) used by NOTEARS and DAGMA. The paper attributes its scaling advantage to this reduction, and the experimental results support this claim.

- **Modestly better structural accuracy on a real-world benchmark.** On the Sachs protein signaling dataset (11 nodes, Table 1), ψDAG achieves SHD=14, TPR=0.411, FPR=0.18 versus NOTEARS (SHD=15, TPR=0.294, FPR=0.26) and GOLEM (SHD=26, TPR=0.294, FPR=0.47) under the same threshold of 0.3. This shows that the method's computational advantages do not come at the expense of solution quality on at least one real problem.

## Weaknesses

### Fatal

None.

### Major

- **Missing structural accuracy metrics on synthetic data — the paper's central claim about recovering the true DAG is not empirically supported for large graphs.** The first contribution (line 23) states that the solution of the reformulated problem "recovers the true DAG." However, every synthetic experiment (Figures 2–4, Section 5, covering d=10 to d=10,000 across ER2/ER4/ER6/SF2 and three noise distributions) reports only runtime to meet an objective-value stopping criterion (line 346). No structural metrics (SHD, TPR, FPR, or any true-graph comparison) are provided for any synthetic dataset. A method that converges quickly to a poor DAG is not useful, and the reader cannot assess whether ψDAG actually finds accurate graphs at scale. The only structural metrics come from the 11-node Sachs experiment, which is too small to support scalability claims.

- **The convergence theorem for the full alternating algorithm is unsubstantiated.** The Theorem (lines 201–205) claims that the full framework (Algorithm alg:fr) — which alternates between unconstrained SGD, a heuristic projection (Algorithm 2), and constrained SGD — converges to a local minimum of the population objective at rate O(σ₁R/√T + L₁R²/T). The main text only justifies this rate for the fixed-ordering convex subproblem (line 186, referencing standard SA theory from Polyak and Nemirovski). The projection is a greedy heuristic with no optimality guarantee, and no analysis is provided for how the alternating scheme or projection errors propagate through the iterations. The gap between the fixed-ordering subproblem guarantee and the full-algorithm claim is not bridged in the visible text.

- **The projection heuristic lacks formal justification.** The method computes a "closest" topological ordering (lines 155–156, 213–214) using a greedy row/column norm minimization (Algorithm 2). The term "closest" is never formally defined, and no approximation guarantee, error bound, or analysis of when this heuristic succeeds or fails is provided. Since the entire algorithm hinges on finding a good ordering — a bad ordering would confine SGD to a suboptimal subspace — this gap is significant. The O(d²) cost is noted, but the quality side of the trade-off is unexamined.

### Minor

- **Overstated claim about SA vs. SAA recovery of the true DAG.** Lines 145–146 assert that the SA formulation's minimizer "recovers the true DAG" while NOTEARS/GOLEM/DAGMA "do not." In the population limit and under standard identifiability conditions, those SAA-based methods also recover the true DAG. The real distinction is about finite-sample bias, not a fundamental inability. The claim as written is too strong and could mislead readers.

- **Baseline failure modes raise configuration questions.** The paper reports that DAGMA fails to even run on the small Sachs dataset (11 nodes, line 365: "its iterate W diverges from the feasible domain during the first iteration") and occasionally fails on synthetic data (line 355). While the authors state they used default thresholds (line 259), these failures suggest the baselines may not have been configured optimally, which could affect the fairness of the runtime comparisons.

- **Stopping criterion not fully specified.** The convergence criterion is f(x_k) - f(\overline{x}) ≤ 0.1·f(\overline{x}) (line 346), but \overline{x} is not defined. For synthetic data it is presumably the optimum under the known ground-truth DAG, but this is not stated, leaving the reader to guess how the "true solution" value was computed.

### Trivial

None.

## Nice-to-Haves

- Report structural accuracy (SHD, TPR, FPR) on synthetic data across graph sizes (d=100, 500, 1000) to verify that fast convergence corresponds to correct graph recovery.
- Add an ablation study comparing the proposed row/column-norm projection to brute-force ordering search on small graphs (d≤10) to characterize its reliability.
- Report variance across random seeds for runtime and structural metrics.
- Include memory footprint measurements to support the claim that memory (not computation) is the primary limitation at d=10,000.

## Removed Points

These points were flagged for removal by the filtering rules; treat them with caution.

- **"Theoretical convergence claim is unsubstantiated — appendix was stripped"**: The rule says to remove criticisms about missing appendix content since the parser strips appendix sections from all submissions. The retained version of this criticism (above, Major) focuses on the substantive concern that the main-text justification is insufficient for the full alternating algorithm, not on the absence of appendix proofs. The appendix-related language was removed.

- **"Universal Stochastic Gradient Method is not described"**: The paper cites Rodomanov (2024). Per rules, nitpicks about citing rather than describing an inner optimizer are removed.

- **"Missing related works"**: Per rules, the reviewer cannot verify whether related works are missing and must not mention this.

- **"Pure formatting/style nitpicks" and "typos, grammar"**: Removed per hard rules about parser artifacts.

- **Strength "Convergence guarantee with explicit rate"** from Strength Finder: This conflicts with a verified weakness (the full algorithm's convergence is unsubstantiated). Per the rule that when a strength and weakness disagree, the weakness wins, this strength was dropped.

- **"Scalability claim not supported because primary limitation is memory"**: The paper's claim is that memory is the limitation at 10,000 nodes — this is a statement about the bottleneck, not an unsupported claim. Removed.

## Novel Insights

The most striking gap across the reviews is the disconnect between the paper's theoretical framing (population-level SA recovery of the true DAG) and its experimental design (which benchmarks runtime but not structural recovery on synthetic data). Neither review fully articulated that this disconnect is the paper's central problem: the scalability contribution is well-evidenced, but the claim that what scales is actually *structure learning* (not just optimization speed) is not directly tested. The projection heuristic itself — row/column norm minimization to recover a topological ordering — is a genuinely simple idea that could be independently useful or analyzable, but both reviews correctly flag that it receives no formal treatment. The paper would benefit from reframing as primarily a computational-acceleration contribution with structural recovery as a secondary empirical check, rather than presenting both as equally supported.

## Suggestions

1. **Add synthetic structural accuracy experiments.** Run ψDAG and baselines on synthetic graphs of varying sizes (d=50, 100, 500) and report SHD, TPR, FPR with variance across seeds. This is necessary to support the claim that the method recovers the true DAG at scale.

2. **Either provide a proof sketch for the full-algorithm convergence theorem, or downgrade the claim.** If the theorem relies on properties of the projection that are not analyzed, this should be transparently stated. A clear separation of what is proven (fixed-ordering subproblem convergence) versus what is conjectured (full alternating scheme convergence) would strengthen the paper.

3. **Analyze the projection heuristic, even empirically.** Show on small graphs (d≤10) how often the row/column-norm heuristic recovers the true topological ordering compared to brute force. This would give readers a concrete sense of the method's reliability.

4. **Clarify the stopping criterion.** Define \overline{x} explicitly, or state that it is the optimal objective value under the known ground-truth DAG for synthetic experiments.

5. **Tone down the SA-vs-SAA recovery claim.** Acknowledge that SAA methods also recover the true DAG in the population limit under identifiability, and frame the SA advantage as about finite-sample behavior.

## Score and Decision

**Originality**: The framework — replacing algebraic DAG constraints with a projection-onto-topological-ordering step — is conceptually novel and different from the NOTEARS/DAGMA line of work. The stochastic approximation framing for DAG learning is also a new perspective.

**Importance of research question**: Scalable DAG learning is an active, important problem. Reducing O(d³) per-iteration cost is practically significant.

**Claims support**: Partially. The scalability claim is well-supported by runtime experiments. The structural recovery claim is only supported on one small (11-node) real dataset. The convergence theorem is not adequately justified for the full alternating algorithm.

**Soundness of experiments**: The runtime comparisons are informative, but the lack of structural accuracy metrics on synthetic data is a significant gap. Baseline configuration is reasonable but the failure modes of DAGMA raise questions.

**Clarity of writing**: The algorithmic description is generally clear. The projection procedure is well-specified. Some claims are overstated (SA vs SAA recovery) and the stopping criterion is vague.

**Value to the community**: The core idea (projection-based DAG constraints with O(d²) complexity) could be valuable if structural recovery is confirmed at scale. The approach is simple enough to be extended.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>