Here is my consolidated review:

---

## Summary

This paper proposes simple spectral kernel models (KERNEL and LR KERNEL) for semi-supervised node classification, using a learnable kernelized propagation matrix \(P^{(K)} = U(\operatorname{diag}(K\alpha))U^T\) built from the eigendecomposition of the graph adjacency or Laplacian. The authors show that these models — which use no dropout, batchnorm, or per-parameter optimizers — are competitive with much more complex GNN architectures on standard benchmarks, achieving improvements of +5% and +20% on the Chameleon and Squirrel directed-graph datasets over prior spectral methods. The paper also contributes an analysis of how evaluation split conventions (sparse → public → dense → balanced) can shift reported accuracy by large margins, using simple linear models as a probe.

## Strengths

- **Substantial accuracy gains on directed graphs are clearly documented.** The KERNEL and LR KERNEL models achieve +5% on Chameleon and +20% on Squirrel over prior spectral GNN methods (Table 2, lines 16, 109), and these improvements are large enough to be meaningful even accounting for potential protocol differences. This directly supports the paper's central claim that simple spectral methods can match or exceed more complex architectures.

- **Systematic three-factor ablation study.** Section 4 ablate kernel choice (Table 3), matrix representation (Figure 2), and spectral truncation factor (Figure 3) across multiple datasets. The finding that most benchmarks retain ~90% performance even after 50% spectral truncation (line 139) is practically useful, and the observation that low-rank truncation partially homogenizes kernel sensitivity on directed graphs (Figure 1, lines 135–136) is an honest and informative empirical result.

- **Evaluation-conventions analysis is a valuable methodological contribution.** Section 5 quantitatively demonstrates that shifting from "dense" to "balanced" splits alone can boost simple linear models to ~85% of reported SOTA performance (Figure 4–5, lines 165–166). This finding is relevant to the entire SSNC benchmarking community, even if the evidence is limited to linear models.

- **Theoretical connection to low-rank matrix sensing.** Section 6 (lines 174–182) reformulates the LR KERNEL model as a rank-1 matrix estimation problem with noisy linear measurements, linking the empirical approach to established theory. While brief, this provides a formal footing absent from most purely empirical GNN papers.

## Weaknesses

### Major

- **Missing comparison against SGC — the most directly relevant simple spectral baseline.** The paper compares against GPRGNN, JACOBICONV, and ACMII-GCN (all moderately complex spectral GNNs) but omits SGC (Wu et al., 2019) and APPNP (Klicpera et al., 2019). SGC is explicitly a one-layer linear model with a fixed propagation matrix \(A^kX\) — the closest existing method to the paper's own PROPAGATED LINEAR and KERNEL models. Without this comparison, the reader cannot judge whether the kernel formulation adds value over an already-simple spectral baseline, or whether the reported numbers merely confirm that simple spectral methods (already known to work) continue to work under the favorable balanced-split protocol. This gap weakens the paper's core claim that the proposed kernel approach is what drives performance.

- **Headline improvement claims rely on cited — not re-implemented — baseline numbers.** The +5% and +20% improvements on Chameleon and Squirrel (line 16, line 109) are computed against numbers for GPRGNN, JACOBICONV, and ACMII-GCN cited from other papers (line 105). The paper's own Section 5 demonstrates that evaluation protocol changes can produce performance shifts of tens of percentage points. But the comparison uses no controlled re-implementation: the cited baselines may have used different hyperparameter tuning procedures, random seeds, early-stopping criteria, or even split versions (the paper's own methods use "balanced splits" from line 95, but it is unclear whether the cited baselines used precisely the same splits). Given the paper's thesis that evaluation conventions inflate apparent performance, this uncontrolled comparison is particularly problematic. A 20% gap warrants verification under a shared experimental pipeline.

### Minor

- **Evaluation-conventions analysis extrapolates from linear models to GNNs without direct evidence.** Section 5 demonstrates the split effect on \(XW\) and \(AXW\) models and then states that GNNs "may also experience a performance bump similar to our linear models" (line 167). The abstract frames this more strongly as showing that "recent performance improvements in GNN approaches may be partially attributed to shifts in evaluation conventions." The evidence supports this as a plausible hypothesis, but demonstrating the effect on at least one GNN architecture (e.g., a simple GCN or GPRGNN) would substantially strengthen the claim. Extrapolation from linear models to multi-layer non-linear GNNs is not automatic.

- **Computational cost of the spectral decomposition is not discussed.** The paper proposes methods that require computing the eigendecomposition (undirected) or SVD (directed) of the adjacency matrix, which is \(O(n^3)\) for large \(n\). For Pubmed (~20k nodes) this is feasible but costly; for larger graphs it becomes prohibitive. The ablation on truncation factor (Figure 3) addresses downstream complexity but not the upfront cost of obtaining the spectral factors. A methods paper targeting practitioners should at minimum acknowledge this barrier.

- **The representer theorem motivation is loose.** The paper states that the parametrization \(h(\sigma_i) = (K\alpha)_i\) is "motivated by the so-called representer theorem" (line 53). In standard RKHS regression, the representer theorem guarantees the minimizer has the form \(\sum \alpha_i K(x_i, \cdot)\) under explicit RKHS norm regularization. Here, \(\alpha\) is a free parameter trained by gradient descent with no explicit RKHS regularization, so the representer theorem does not meaningfully constrain the solution. The parametrization is a convenient functional form; the RKHS framing adds little and may mislead readers about the theoretical grounding.

### Trivial

- **Bandwidth sensitivity not reported.** The paper states that the kernel bandwidth \(\gamma\) for the Gaussian RBF and unbounded Sobolev kernels is "selected using a validation process" (line 93) but does not report the sensitivity of results to this choice or the range of values considered.

## Nice-to-Haves

- Controlled re-implementation of GPRGNN and JACOBICONV under the paper's exact pipeline (same splits, seeds, tuning protocol) would directly confirm or bound the claimed improvements.
- Reporting runtime versus graph size and truncation factor would help practitioners assess practical trade-offs.
- Adding SGC as a baseline and demonstrating the split effect on at least one GNN architecture would strengthen the paper's two central claims.
- The theoretical connection to low-rank matrix sensing (Section 6) could be expanded; in its current brief form it reads as an afterthought.

## Removed Points

- **"Evaluation conventions analysis does not test its own conclusion"** (harsh critic #3): The paper hedges its language ("may also," "may be partially attributed") and the extrapolation from linear models to GNNs is reasonable as a stated hypothesis. Downgraded from a claimed issue to minor weakness (above) rather than a structural flaw.
- **Bandwidth sensitivity (harsh critic):** Included above as a trivial weakness rather than the stronger framing the critic gave it.
- **Strength Finder strengths that are generic/delusional:** The Strength Finder's listed strengths are all concrete and evidence-backed, so none needed removal.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's main findings but do not surface an unrecognized deeper observation.

## Suggestions

- Re-run at least GPRGNN under the paper's own evaluation protocol (balanced splits, same hyperparameter tuning pipeline) to validate the +5%/+20% claims with a controlled comparison.
- Add SGC and APPNP to Table 2 to directly test whether the kernel formulation adds predictive value over the simplest spectral baselines.
- Include a brief paragraph or table quantifying the computational cost (wall-clock time to compute the SVD/eigendecomposition) for each benchmark graph.
- Report the range of \(\gamma\) values considered during validation and note performance sensitivity.

## Score and Decision

The paper makes a real contribution: the finding that simple linear models with kernelized spectral propagation match complex GNNs is important and largely well-supported, and the evaluation-conventions analysis is a useful methodological note. However, the two major weaknesses — the absence of SGC/APPNP as baselines and the reliance on cited (not re-implemented) numbers for the headline improvement claims — prevent the paper from being fully convincing at a top-venue standard as-is. The missing SGC comparison is particularly consequential because it directly tests whether the paper's core technical contribution (the kernelized propagation) adds anything over an already-established simple spectral method.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>