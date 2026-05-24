## Summary

This paper proposes three one-step diffusion-based solvers (CMILP, SCMILP, MFILP) for integer linear programming (ILP), drawing on consistency, shortcut, and meanflow models for speed. The key technical contributions are: (1) adapting one-step diffusion models to generate feasible ILP solutions end-to-end, achieving orders-of-magnitude speedup over prior diffusion-based ILP solvers (IP Guided DDPM/DDIM); (2) an Iterative Integer Projection (IIP) layer that enables differentiable handling of non-binary integer variables without costly binarization; and (3) a momentum-based gradient descent scheme for objective-guided sampling. Experiments span binary ILP benchmarks (set cover, facility location, combinatorial auction) and non-binary datasets (inventory management, synthetic random ILPs).

## Strengths

- **Dramatic inference speedup over prior diffusion-based ILP solvers.** Table 1 shows compelling evidence: on the binary set cover (SC) dataset, CMILP achieves 100% sample feasibility in ~22 s whereas IP-Guided DDIM requires 65 minutes for 99.8% feasibility. On non-binary IM-(50,5,2) (Table 2), MFILP reaches 70.5% sample feasibility in 2.1 s vs. DDIM's 46.0% in 6 minutes. These speed advantages (50–1000×) are the paper's strongest empirical result.

- **The IIP layer is a clean and practical solution for non-binary ILP.** The projection function \(f_{\text{proj}}(x) = x - \sin(2\pi x)/(2\pi)\) (Eq. 3) is differentiable, converges rapidly to integer values (visualized in Fig. 2), and avoids the exponential variable explosion from binarization. Table 4 provides direct evidence: on IM-(50,5,2), the proposed methods achieve 88–90% dataset feasibility, while their binarized variants collapse to 3%. This is a genuine technical contribution.

- **End-to-end feasibility without solver-based post-processing.** On binary SC and CA datasets, CMILP, SCMILP, and MFILP all achieve 100% dataset feasibility and high sample feasibility (88–100%), whereas Neural Diving alone gives 0% dataset feasibility on SC and CF (Table 1). This supports the claim that one-step diffusion can produce feasible solutions without relying on traditional heuristic post-processing.

- **The conceptual reframing of existing IP guidance as a single gradient step** (Section 3.3) provides a principled motivation for introducing multi-step GD and momentum, even though the individual components (GD, momentum) are standard.

## Weaknesses

### Fatal

None.

### Major

- **Non-binary baseline adaptation is not specified, clouding the core non-binary comparison.** The paper evaluates IP Guided DDPM and DDIM (originally designed for binary ILP) on non-binary datasets (Tables 2, 3, 6) but never states how these baselines were adapted. Were they run on the raw non-binary data (in which case they would not naturally handle integrality), or were they binarized (which the paper itself shows collapses performance — Table 4)? Table 4 provides a binarized comparison for only two small IM datasets; the main non-binary tables lack this context entirely. Without knowing the adaptation pathway, the reader cannot interpret whether the proposed methods' advantage comes from the IIP layer or from unfair comparison against poorly-adapted baselines. This is the single most significant weakness in the experimental design.

- **Solution quality (optimality gap) is often too poor for practical use, even on binary problems.** On binary SC, all three proposed methods achieve 88–92% gap vs. IP Guided DDIM's 68.5% and PS's 71.7% (Table 1). On CF, gaps are 76–83% vs. DDIM's 54.6%. On non-binary IM-(50,5,10), gaps exceed 100% (Table 2). While speed is the advertised advantage, a solver producing solutions with 80%+ optimality gap is of limited practical value regardless of speed. The paper acknowledges this in the limitations section, but understates its severity — the gaps are often an order of magnitude larger than those of traditional solvers run for comparable or even shorter wall-clock times (e.g., Gurobi solves Random-(2000,20,2) in 42 s with 0% gap; Table 6).

- **Ablation studies are insufficient to validate claimed contributions.** Three claimed technical contributions (one-step diffusion adaptation, IIP layer, momentum guidance) would each benefit from systematic ablation. Currently: (i) the momentum ablation (Table 5) tests only one method (SCMILP) on one dataset (IM-(50,5,10)) with modest gains (2% gap, 4% dataset feasibility) — no results for CMILP, MFILP, or other datasets. (ii) There is no ablation of the IIP layer (e.g., training with varying \(K\), comparing vs. without IIP, vs. sigmoid rounding). (iii) There is no comparison across the three diffusion variants (CMILP vs. SCMILP vs. MFILP) that explains when one should be preferred over another, nor any analysis of their relative computational costs.

### Minor

- **Method description is partly unclear.** The CMILP loss (Eq. 6) uses a Dirac delta centered at the optimal solution \(x^*\) as the target; the mapping from the standard consistency loss to this formulation is described only briefly. The loss functions for SCMILP and MFILP are deferred to the appendix (removed by the parser), making it impossible to fully reconstruct what distinguishes the three variants from each other or from standard shortcut/meanflow training. The derivation of the objective-guided sampling (Eqs. 7–8) cites prior work (Graikos et al., 2023; Li et al., 2024) but the connection between the variational free energy and the final implemented gradient update is not spelled out clearly enough for a reader unfamiliar with those papers.

- **No statistical uncertainty reported.** No standard deviations, confidence intervals, or multiple-seed results are provided for any metric. Given the stochasticity of diffusion sampling, this makes it difficult to assess whether reported improvements (e.g., the ~2% gap reduction from momentum in Table 5) are statistically meaningful.

- **Sample feasibility is low on larger non-binary instances.** On Random-(2000,20,2) (Table 6), sample feasibility is only 11.7–14.8%, meaning the user must generate many samples per instance to obtain a feasible solution, which increases effective runtime. The paper uses "sample feasibility" as a metric but does not discuss the practical implications of low per-sample feasibility.

- **Missing comparison with DiffILO on non-binary data.** DiffILO (Geng et al., 2025b) is compared only on binary problems (Table 1). If DiffILO can handle non-binary ILP (even through binarization), a comparison on the non-binary datasets would strengthen the paper; if not, this should be stated explicitly.

### Trivial

- The first row for IM-(50,5,5) in Table 2 lists "ris" and "feasupn" — these appear to be abbreviated names for rins and feaspump introduced in Section 4.1 but the inconsistent naming is confusing.
- Table 2 lists "SCMILP (Ours)" twice (rows 8 and 9) when one entry is presumably CMILP.

## Nice-to-Haves

- A runtime vs. gap Pareto analysis on a representative dataset, showing where the proposed methods are practically useful (e.g., gap < 10%) would help contextualize the speed-optimality trade-off.
- An analysis of IIP convergence behavior — how does performance vary with \(K\) (projection iterations) at test time?
- Reporting variance across random seeds (e.g., 3 seeds) for gap and sample feasibility on at least one dataset per category.

## Removed Points

*"The code is not yet released"* — Cited models, benchmarks, and code availability statements are assumed valid per review guidelines.  
*"Appendix content (referenced but removed by parser)"* — Parser-stripped content is assumed to exist in the original submission.  
*"The loss in Eq. 6 collapses to direct regression to a single \(x^*\), which would not produce a distribution over feasible solutions"* — The paper explicitly states it is adapting the consistency loss for the ILP setting where \(x^*\) is known, using the Dirac delta as a target distribution; this is a deliberate design choice, not a flaw.  
*"Missing related works"* — Per protocol, cannot verify existence or absence of related works without external sources.  
*"Formatting/style nitpicks"* — Parser introduces formatting artifacts not present in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new observation that the authors missed.

## Suggestions

1. **Clarify the non-binary baseline setup.** Specify exactly how IP Guided DDPM and DDIM were adapted for non-binary data. If they were run on the raw non-binary data without modification, this must be stated and the implications discussed. If binarized, report the binarized variable counts and time penalties transparently for all non-binary tables, not just the two small IM cases in Table 4.

2. **Add systematic ablations.** At minimum: (a) training without the IIP layer (replace with hard rounding) to isolate its contribution; (b) gradient descent without momentum (GD) for all three methods on at least 2–3 datasets; (c) a comparison of CMILP vs. SCMILP vs. MFILP with controlled architecture and inference budget.

3. **Report variance.** Add standard deviations across 3 random seeds for gap and sample feasibility on a representative dataset per category.

4. **Improve method description.** Provide pseudocode or explicit loss definitions for SCMILP and MFILP in the main text. Clarify the connection between Eq. 7 and the implemented gradient update. The Dirac delta notation in Eq. 6 should be explained more carefully — what distance function \(d\) is used in practice (MSE?), and how is the delta distribution materialized during training?

5. **Discuss practical use cases.** Show at least one setting (dataset size, time budget) where the solution quality is within a practical threshold (e.g., gap < 10%) while maintaining the speed advantage. The current framing ("fast but 80% gap") is not compelling.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|--------------------------|
| joMMM9eadc (diffusion for IP, guided sampling) | 6.25 (Reject) | R1,R2 | Most directly comparable; clearer methodology, only binary. Current paper handles non-binary and is faster but has larger gaps and less clear method. Slightly weaker. |
| FPfCUJTsCn (DiffILO, differentiable ILP) | 7.20 (Accept) | R1 | Significantly stronger paper — unsupervised, clean theory, solid experiments. Current paper is clearly below this. |
| 6JDpWJrjyK (DISCO, diffusion for CO) | 5.75 (Reject) | R1,R2 | Different domain (TSP/MIS). Similar incremental-innovation concerns and limited ablations. Current paper tackles harder constraint satisfaction problem and has more comprehensive eval; comparable quality. |
| McfYbKnpT8 (L2P-MIP, presolve learning) | 6.50 (Accept) | R2 | Different problem (presolve config). Strong execution. Current paper is weaker. |
| 7TXdglI1g0 (bisection projection for feasibility) | 5.20 (Reject) | R2 | Different problem. Current paper is somewhat stronger. |

**Round-1 bracket:** [4.0, 6.5] (between weak anchors ~3 and strong anchors ~8).  
**Round-2 narrowing:** The most comparable anchor is joMMM9eadc at 6.25 (rejected). The current paper is slightly weaker due to larger optimality gaps and less clear methodology, placing it below 6.25. It is moderately above the 5.2–5.75 range of less related papers.  
**Final placement:** Closer to the lower end of comparable diffusion-for-ILP papers, around **5.5**.

The paper tackles a worthwhile problem (fast neural ILP solvers for non-binary variables) and has a genuine technical contribution in the IIP layer, along with impressive speed results. However, the experimental comparison on non-binary problems is not properly controlled (baseline adaptation undisclosed), the optimality gaps are often too large for practical use, and the ablation support for claimed contributions is thin. These weaknesses collectively make the paper fall short of the acceptance threshold for a top venue in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>