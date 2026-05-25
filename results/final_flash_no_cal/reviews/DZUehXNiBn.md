Below is the consolidated review, grounded in the actual paper text and filtered per the instructions.

---

## Summary

VISTA is a modular framework for causal structure learning that decomposes global DAG learning into node-centered Markov Blanket subgraphs, aggregates them via a weighted voting scheme (with exponential weighting by support count), and enforces acyclicity with a Feedback Arc Set heuristic. The framework is model-agnostic (works with any base learner that outputs directed edges) and fully parallelizable. The paper provides finite-sample error bounds (Theorems 3.2–3.4) and an asymptotic consistency claim (Theorem 3.5), together with experiments across six base learners, multiple graph families and sizes, and a real dataset (Sachs). The empirical results show consistent accuracy improvements (notably FDR reductions of 50–80% in many settings) and substantial runtime speedups (up to 50× for SCORE at 100 nodes).

---

## Strengths

1. **Model-agnostic framework with strong empirical validation.** VISTA is tested with six fundamentally different base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM) across synthetic (ER, SF) and real (Sachs) data. Tables 1–3 show consistent improvements in F1, SHD, FDR, and runtime over the standalone baselines. For example, NOTEARS FDR drops from 0.21→0.08 on ER5 (Table 1), and SCORE runtime drops from 10,040s→198s on 100 nodes (Table 3). The gains hold for both differentiable and combinatorial learners, supporting the claim that the aggregation mechanism, not any specific learner, drives improvement.

2. **Finite-sample theoretical analysis.** The paper provides formal error bounds (Theorem 3.2, Corollary 3.3, Theorem 3.4) that characterize the relationship between the number of subgraph votes, the weighting parameter λ, and edge-level error probabilities. While the bounds assume independent votes (acknowledged by the authors), they provide a principled framework for understanding when the weighted voting scheme should succeed and give a prescriptive feasible range for λ (Theorem 3.4).

3. **Practical hyperparameter analysis.** The sensitivity study (Figure 4) validates the precision–recall trade-off predicted by the theory, and the paper adopts a single fixed operating point (λ = 0.5, t = 0.7) across all main experiments without per-dataset tuning, demonstrating practical robustness.

4. **Computational efficiency.** The divide-and-conquer design with one-pass O(|V|²) aggregation delivers substantial runtime improvements (Table 3) without requiring ILP solvers or iterative optimization, which is a genuine practical advantage over fusion methods like DCILP.

---

## Weaknesses

### Fatal
None. No verified issue invalidates the paper's core claims.

### Major

1. **Asymptotic consistency claim (Theorem 3.5) is overstated for the sparse-graph regime studied.** The theorem requires the number of subgraphs per candidate edge to grow as *m* = *C* log *n*. In sparse graphs with constant average degree (*h* = 3, 5), each edge appears in only O(1) subgraphs—bounded by Markov Blanket sizes that do not grow with *n*. Therefore the theorem's sufficient condition is not satisfied in the experimental setting, and the claim that "the required number of independent subgraphs per edge grows only logarithmically" (presented as a consequence) is actually an assumption that is not justified for the graphs tested. The finite-sample bounds (Theorems 3.2–3.4) are unaffected, but the asymptotic consistency claim as stated does not apply to the regime the paper evaluates. This needs to be corrected: either prove consistency under bounded *m* using a different argument, or drop/qualify the claim to match the setting.

2. **Markov Blanket identification method is not specified for the main experiments.** The paper repeatedly states that VISTA is agnostic to the MB estimator and uses a generic `MB_solver(v)` in pseudocode (Figure 2), but never states which MB identification algorithm was actually used to produce any of the experimental results (Tables 1–4, Figure 1). The only mention is that "we also implemented the MB solver used in that work" for the DCILP comparison in Appendix F.2. Without this information the results cannot be reproduced, and it is impossible to separate the effect of the VISTA aggregation from the quality of the (possibly very strong or even oracle-like) MB estimator. The paper should state the MB method used and ideally include an ablation over different MB estimators.

### Minor

3. **Finite-sample bounds assume independent subgraph votes.** Theorems 3.2–3.3 are derived under a Binomial model where votes from different local subgraphs are independent. The authors acknowledge this is a "qualitative guide" (Section 3.1) because subgraphs overlap and share data. The bound therefore provides no rigorous guarantee for the realized correlated setting. This is a transparent limitation, but the paper's claims of "finite-sample error bounds" and "theoretical guarantees" should be calibrated accordingly.

4. **Theorem 3.4's uniform error-control claim does not hold for a single global λ.** The feasible λ range in Theorem 3.4 depends on the per-edge vote count *m*, which varies across edges. The paper adopts a single λ = 0.5 and *t* = 0.7 for all experiments, so the stipulated error control cannot hold simultaneously for all edges. The empirical results are still valid, but the theoretical guarantee is weaker than suggested.

5. **No ablation of the FAS cycle-breaking step.** The paper acknowledges that GreedyFAS may prune correct edges (Section 5), but provides no analysis of how many true/false edges are removed by this step. Reporting the number of cycles before and after FAS, and the fraction of true edges lost, would clarify this known limitation.

6. **No uncertainty quantification on real-data results.** Table 4 reports only point estimates (single run) on the Sachs dataset. Given the small graph (11 nodes) and stochastic base learners, confidence intervals or multiple-run statistics would help assess whether the modest SHD improvements (e.g., 16→12 for GraN-DAG) are reliable.

### Trivial

7. **"Global error" in Theorem 3.5 is not defined in the main text.** The term appears only in the probability statement Pr(global error) = *o*(1) without formal definition; the reader must infer what is being bounded.

---

## Nice-to-Haves

- A joint sensitivity sweep of both λ *and* t (Figure 4 varies λ but fixes t = 0.5, while the main tables use t = 0.7).
- A direct comparison to at least one other modular framework (e.g., DCILP) in the main paper, not only the appendix, to contextualize the relative performance.
- Bootstrap confidence intervals or multi-run statistics on the real-data results (Table 4).

---

## Removed Points

These points were raised by a reviewer but are removed (with justification), treat them with caution:

1. **"Comparison with alternative modular approaches is relegated to the appendix"** — The paper's primary claim is that VISTA improves base learners, which is tested against those base learners in the main text. The DCILP comparison is in Appendix F.2 (standard practice for supplementary comparisons). The paper does not claim "state-of-the-art versus all modular methods" as its headline result. **Grounds:** The criticism imposes a scope standard beyond the paper's stated contribution.

2. **"Pseudocode in Figure 2 is ambiguous: lam and t not defined"** — `lam` and `t` are function parameters in the `VISTA(...)` signature (line 93). The function call `WV(local_graphs, lam, t)` passes them correctly. **Grounds:** Factually wrong; the parameters are defined in the visible signature.

3. **"Missing related works"** — The instructions prohibit mentioning missing related works because I cannot verify their existence externally.

4. **General-area speculations** (e.g., "the bound then provides no rigorous guarantee for the actual (correlated) setting" framed as if the authors hid this) — The paper explicitly acknowledges the independence limitation in the same paragraph as Theorem 3.2. **Grounds:** The paper already addresses this.

5. **Formatting/style nitpicks** (e.g., "pseudocode ambiguity", typo-level issues) — Removed per the formatting-artifact rule.

---

## Novel Insights

None beyond the paper's own contributions. The key insight—using a calibrated weighted vote over Markov Blanket subgraphs with a Feedback Arc Set post-process—is already well articulated in the paper. The reviews do not surface a deeper theoretical or methodological observation that the authors themselves missed.

---

## Suggestions

1. **State the MB identification method explicitly.** This is the single most important fix for reproducibility. Also consider including an ablation comparing different MB estimators (e.g., a standard constraint-based method vs. a weaker baseline) to show VISTA's benefits are not contingent on a near-perfect MB oracle.

2. **Correct or qualify the asymptotic consistency claim.** Either prove consistency under bounded *m* (the realistic sparse-graph case), or replace the claim with a transparent statement that the asymptotic result requires *m* ∝ log *n* and is not directly applicable to the constant-degree setting studied empirically.

3. **Define "global error" in Theorem 3.5** and clarify that the finite-sample bounds (Theorems 3.2–3.4) are derived under an independence assumption, and that the extension to correlated votes remains an open question.

4. **Add an FAS ablation:** report the number of edges removed by GreedyFAS, broken down by correct/incorrect, for a representative setting. This would help readers assess the cost of the acyclicity enforcement step.

5. **Provide uncertainty estimates on the Sachs results**, e.g., by running the stochastic base learners with multiple seeds or reporting bootstrap confidence intervals.

---

## Score and Decision

The paper presents a clean, model-agnostic framework with strong empirical support across diverse base learners and settings. The two major weaknesses—the overclaimed asymptotic consistency and the unspecified MB identification method—are real but addressable: neither invalidates the core experimental contribution (VISTA consistently improves accuracy and speed), and both can be fixed in a revision. The minor weaknesses are typical for a conference paper of this scope.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>