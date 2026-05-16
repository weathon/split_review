Now I have all the information needed to produce the final consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper proposes MEHA, a single-loop Hessian-free algorithm for nonconvex-nonconvex bilevel optimization (BLO). The key idea is to use a Moreau-envelope reformulation of the lower-level problem, convert the constrained reformulation into a penalized problem, and then apply alternating proximal gradient updates with a single-step approximation of the proximal point. The paper provides non-asymptotic convergence rates (O(1/K^{(1-2p)/2}) for the stationarity residual of the penalized problem) under only L-smoothness assumptions—avoiding the PL condition or convexity required by prior Hessian-free BLO methods. Experiments on synthetic problems, few-shot learning, data hyper-cleaning, and neural architecture search show competitive speed and accuracy.

## Strengths

- **First single-loop Hessian-free algorithm with non-asymptotic guarantees without PL/convexity.** As shown in Table 1, MEHA is the only method that simultaneously achieves Hessian-free, single-loop, and non-asymptotic convergence while requiring only L-smoothness of the LL objective. Prior Hessian-free methods (BOME, V-PBGD, SLM, GALET) all require the PL condition and/or use double-loop structures. This is a genuine advance in the theory of nonconvex BLO.

- **Convergence theory under genuinely mild assumptions.** Theorem 1 establishes convergence rates for the penalized reformulation's stationarity residual (O(1/K^{(1-2p)/2})) and constraint violation (O(1/K^p)) requiring only that the UL and LL objectives are L-smooth (with weak convexity and nonsmoothness allowed for the general case). No convexity, PL condition, gradient boundedness, or compactness assumptions are needed—strictly weaker than all prior Hessian-free BLO methods in Table 1.

- **Consistent empirical advantages across diverse benchmarks.** MEHA achieves the fastest convergence times on synthetic nonconvex problems (e.g., 0.774s vs. 5.062s for BOME at dimension=1, Table 2), the highest test accuracy on NAS (96.07%, Table NAS), and the best accuracy/F1 on data hyper-cleaning (Table meta). The parameter sensitivity analysis (Table 4) demonstrates stable convergence across a wide range of hyperparameter choices (steps vary from 86–199), indicating the method is not brittle.

- **Handles nonsmooth lower-level objectives.** The algorithm directly supports nonsmooth $g$ via proximal steps. Experiments on Lasso (Eq. LNS) and group Lasso hyperparameter selection validate that MEHA obtains lower test error with less time than baselines, extending BLO methodology beyond the smooth setting.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported, and no single weakness invalidates the contribution.

### Minor

- **The convergence guarantee is for a penalized reformulation, and the connection to the original BLO's hypergradient stationarity requires additional assumptions.** Theorem 1 proves convergence of $R_k$, the stationarity residual of the penalized problem (Eq. problem_pen), and shows constraint violation $\varphi(x^K,y^K)-v_\gamma(x^K,y^K) \to 0$. For the general nonconvex LL case, the reformulated problem is equivalent to a *relaxed* BLO where the LL constraint is first-order stationarity (Section 2.1, lines 241–253). This is a meaningful contribution—first-order stationarity of the LL is the natural optimality condition for nonconvex LL—but the abstract's phrasing "non-asymptotic convergence analysis for general nonconvex BLO problems" could mislead readers into expecting convergence to stationary points of the original BLO's hypergradient. The paper does address this connection (lines 427–429, Theorem 2), but only for the strongly convex LL case. Recalibrating the abstract/introduction claims to match what is proved for the general case would improve clarity.

- **Missing ablation on the single-step $\theta$ approximation.** A controlled experiment comparing MEHA's cheap single-step approximation of $\theta_\gamma^*$ against a version using the exact proximal minimizer (solved to high precision) on synthetic problems would directly validate that the approximation does not significantly degrade convergence. The sensitivity analysis varies hyperparameters but does not isolate this design choice. This is the most impactful addition the authors could make.

- **Baseline coverage is inconsistent across experiments.** Table 1 lists IAPTT-GM, GALET, BOME, V-PBGD, SLM, and MEHA, but no single experiment includes all of these. The synthetic nonconvex case (Table 2) compares only BOME, BVFIM, IAPTT; the NAS table (Table NAS) includes DARTS variants, RHG, CG, IAPTT but not V-PBGD or BOME (though V-PBGD does appear in the few-shot/hyper-cleaning table). While no paper can benchmark every method on every task, a more consistent core set of recent Hessian-free BLO baselines across experiments would strengthen the empirical claims.

- **The connection between $R_k$ and standard BLO optimality could be clearer for the general nonconvex case.** The paper acknowledges (lines 427–429) that the hypergradient $\nabla\Phi(x)$ may not be well-defined for nonconvex LL and provides the connection only under strong convexity (Theorem 2). For the general case, a brief explanation of why $R_k$ is the *right* measure—i.e., that it encodes joint stationarity of UL gradient and LL first-order conditions—would help readers assess what the theory guarantees.

- **In the "Computation Efficiency under Large Scale" table, the baselines (Grid, Random, TPE) are hyperparameter search methods rather than BLO algorithms.** While IGJO and VF-iDCA (BLO methods) are included in the group lasso experiment (Table lasso), the large-scale nonconvex table (tab:large_scale) lacks recent BLO baselines. This makes speed comparisons harder to attribute to the algorithm versus baseline selection.

### Trivial

- Table captions for synthetic experiments (e.g., Table 2, tab:numerical) report only time; the convergence tolerance is referenced in Section sec:detail (appendix). Including the tolerance explicitly in the main text or table caption would improve self-containedness.

- The relationship between the three error bounds in Theorem 1 (with parameters $p$ and the two different rates) could benefit from a brief informal summary after the theorem statement.

## Nice-to-Haves

- An ablation isolating the effect of the single-loop $\theta$ approximation vs. exact proximal solution on synthetic problems.
- Reporting FLOPs or gradient evaluations alongside wall-clock time for synthetic experiments.
- A brief discussion of the per-iteration computational overhead relative to double-loop methods.

## Removed Points

These points are flagged for removal (treated with caution):

- **"Inconsistency" between Figure 1 ("some other methods fail to converge") and Table 2 reporting BOME time**: These are different experiments—Figure 1 is the LL convex case (Eq. LLC), while Table 2 is the LL nonconvex case (Eq. LNC). No inconsistency exists. *Removed as factually wrong.*

- **"The paper does not provide evidence that small $R_k$ corresponds to being close to a solution of the original BLO"**: The paper explicitly establishes (Section 2.1, lines 241–253) that the reformulation is equivalent to a relaxed BLO with first-order LL stationarity constraints—precisely the right notion for nonconvex LL. *Removed as it ignores the paper's own explanation.*

- **"Stopping criteria not reported"**: The paper references convergence criteria in Section sec:detail (line 487). These exist in the appendix of the original submission (stripped by the parser). *Removed as parser artifact.*

- **"Grid/Random/TPE are not BLO baselines — unfair comparison"**: IGJO and VF-iDCA (BLO methods) are included in related experiments (Table lasso). Grid/Random/TPE are standard hyperparameter optimization baselines for the hyperparameter selection tasks tested. Different tasks invite different baselines. *Removed (scope-creep complaint).*

- **Pure formatting/style nitpicks** (e.g., phrasing suggestions about what the paper "should consistently refer to"). *Removed per hard rules.*

## Novel Insights

The reviews surface one genuinely interesting tension that the paper does not fully resolve: MEHA's main selling point is handling *general* nonconvex LL without PL/convexity, yet its cleanest quantitative guarantee (Theorem 2, convergence of $\|\nabla\Phi(x)\|$) requires exactly the strong convexity that prior work already addresses. For the general nonconvex case, the theory guarantees convergence of the penalized reformulation's stationarity—which connects to *first-order stationarity* of the LL, not to the hypergradient. This is a meaningful but different type of guarantee. The paper's framing treats this as a unified contribution, but the two regimes (general nonconvex vs. strongly convex LL) offer qualitatively different guarantees, and the paper would benefit from drawing this distinction more sharply rather than smoothing it over.

## Suggestions

1. **Reframe the abstract and introduction** to say: "We provide non-asymptotic convergence analysis for a Moreau-envelope-based reformulation of nonconvex-nonconvex BLO; this reformulation is equivalent to the original BLO under convexity/PL and to a first-order relaxation otherwise." This is honest and still positions the paper as a clear advance.

2. **Add an ablation study** comparing MEHA against a version that solves for $\theta^*_\gamma$ exactly (to high precision) on a synthetic problem. This would directly validate that the single-step approximation is not harming performance.

3. **Include V-PBGD and BOME consistently** in at least the synthetic nonconvex and NAS experiments to make baseline coverage more systematic. If computational cost is a barrier, justify exclusions.

4. **Add a one-paragraph informal summary after Theorem 1** explaining what each rate means and how they interact (especially the role of $p$ in trading off stationarity vs. feasibility).

## Score and Decision

The paper makes a genuine contribution: a single-loop Hessian-free algorithm for nonconvex-nonconvex BLO with non-asymptotic rates under the weakest assumptions in the literature. The weaknesses are real but not structural—they concern framing precision and experimental thoroughness, not validity of the core results. With the suggested revisions (especially reframing the theoretical claims and adding an ablation), the paper would be clearly acceptable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>