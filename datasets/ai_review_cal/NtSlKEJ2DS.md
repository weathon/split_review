- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
I have thoroughly verified all reviewer claims against the actual paper. Here is my final consolidated review.

---

## Summary

This paper extends optimal transport (OT) from bipartite graphs to general graphs by replacing marginal constraints with flow balance constraints, introducing Optimal Flow Transport (OFT). To make the problem amenable to GPU-accelerated matrix iterations, the authors propose entropic regularization with a virtual self-flow mechanism and derive the OFT-Sinkhorn algorithm — an iterative method that alternates updates of scaling vectors, a kernel matrix, and output flows. The framework is further extended to incorporate node and edge capacity constraints, connecting it to the minimum-cost flow (MCF) problem. Experiments on synthetic (Uniform-MCF, NETGEN) and large sparse graphs show that OFT-Sinkhorn achieves substantial speedups over CPU-based exact solvers while maintaining small objective error.

## Strengths

1. **First entropic-regularized, GPU-friendly matrix-iterative method for flow problems on general graphs.** The paper bridges entropic OT and network flow theory by deriving a Sinkhorn-like algorithm that operates on arbitrary graphs with flow balance constraints, not just bipartite structures. Tables 1–3 demonstrate that the method solves large MCF instances in a fraction of the time required by CPU-based exact solvers (e.g., 0.17s vs. hundreds of seconds on 10k-node instances).

2. **Principled formulation of entropic OFT with virtual self-flow.** The introduction of virtual flow d (each node sends d units to itself, with D_{ii}=0) is a clever device that resolves two key obstacles: isolated nodes that would otherwise have zero flow (preventing matrix iterations), and the inability to directly convert flow balance constraints into marginal-like constraints. The reformulation in Eq. 5 is non-trivial and makes the Sinkhorn framework applicable.

3. **Closed-form optimality characterization for the regularized problem.** Proposition 2 provides the explicit parameterization of the optimal coupling (P = diag(u)K diag(v) with u⊙v=1, and q computed from K, u, v, s). This gives a concrete target for the iterative algorithm and mirrors the structure of classical entropic OT, which is elegant and enables the Sinkhorn-like updates in Eq. 8–10.

4. **Extension to capacity-constrained MCF.** Section 3.3 shows how node capacities (via q truncation) and edge capacities (via K truncation, Proposition 3) can be incorporated into the iterative scheme while preserving GPU-friendliness. This is a genuine practical extension beyond prior graph-OT methods (Le et al., 2022; 2024) that cannot handle capacity constraints.

5. **Numerical stability across a wide parameter range.** Figure 5 systematically evaluates the algorithm across ε ∈ [5×10⁻¹, 1×10⁻⁴] and convergence thresholds ∈ [1×10⁻², 1×10⁻⁵], showing smooth time/cost behavior with NaN only at extreme values.

## Weaknesses

### Fatal
None.

### Major

1. **Convergence theorem stated without proof or proof sketch.** Theorem 1 claims linear convergence in the Hilbert projective metric at rate O(λ²ˡ), but the main text provides no proof or even a proof sketch. The definition of λ(K) = maxₗ λ(K^(l)) is given, but the mathematical analysis required to show that the contraction factor is ≤1 for all iterates (especially given that K changes each iteration) is absent. Since the abstract and introduction advertise a "theoretical guarantee for global convergence," the reader cannot evaluate whether this claim is substantiated. The proof may reside in a stripped appendix, but a theorem carrying this much weight needs at least a high-level argument in the main text.

2. **No CPU baseline of the proposed method.** The paper compares its GPU-implemented OFT-Sinkhorn (RTX 4090) against CPU-only baselines (Real, ZKW, Gurobi, pns, lemon on an Intel i9-10920X). While the contribution is specifically a *GPU-friendly* algorithm, the absence of a CPU execution of the same method makes it impossible to separate algorithmic efficiency from hardware acceleration. A CPU run of OFT-Sinkhorn would isolate how much of the speedup is due to the algorithm's structure vs. GPU parallelism.

### Minor

3. **Algorithm 1 uses a fixed iteration count, not a convergence check.** The pseudocode runs for L iterations unconditionally, with no explicit stopping criterion. The Err convergence threshold (defined in the caption of Figure 5 as ∥P1−Pᵀ1−s∥) is referenced in the ablation study but not incorporated into Algorithm 1's loop logic. This makes the pseudocode incomplete as a specification.

4. **Lack of variance/uncertainty measures in all tables.** Tables 1–3 report point estimates (solution time and objective) without standard deviations, confidence intervals, or per-instance breakdowns. Figure 5 averages over 4 instances but does not show variability. Without this information, it is difficult to assess the stability and reliability of the reported improvements.

5. **Ablation study is purely qualitative.** Figure 6 shows that the marginal distribution from OFT-Sinkhorn approaches the ground truth as iterations increase, but this is demonstrated only via visual KDE plots. No quantitative metric (e.g., ℓ₁ error, total variation distance, or objective gap versus iterations) is plotted. Similarly, Figures 3–4 show sparsity trends visually but without numerical quantification.

6. **Overstatement in conclusion and framing.** The conclusion states the method "can be effectively used to solve the minimum cost flow problem," but the method provides *approximate* solutions due to entropic regularization (and capacity constraints are handled via truncation, not exact enforcement). MCF is classically understood as requiring exact, feasible solutions. The paper should more precisely characterize the regime in which approximate solutions are acceptable.

### Trivial

- The text in Section 2 runs for several pages without clear paragraph breaks (appears to be a formatting artifact of the PDF extraction).
- Algorithm 1 references equations (Eq. 8, 9, 10) without restating them in the pseudocode block, slightly impeding readability.

## Nice-to-Haves

- A sensitivity analysis for the virtual flow constant d, showing how its value affects solution quality and convergence speed.
- A discussion of the trade-off between ε, solution sparsity, and accuracy, quantified rather than just visualized.
- The per-iteration complexity (O(N²) dense vs. O(|E|) sparse) stated explicitly as a computational claim.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Mathematical inconsistency: u⊙v=1 contradicts iterative K update."** — This is a misunderstanding. The optimality condition u⊙v=1 holds at convergence; during iterations, diag(K) = d/(u⊙v) ensures P_{ii}=d is maintained, and diag(K)=d emerges naturally only at the fixed point. This is standard iterative optimization, not a contradiction. The same logic applies to vanilla Sinkhorn (marginal constraints are only satisfied at convergence).
- **"D_{ii} transition from +∞ to 0 is unjustified."** — The paper clearly states the rationale: exact OFT (Section 3.1) prevents self-transport via infinite cost; entropic OFT (Section 3.2) introduces virtual self-flow with D_{ii}=0 and P_{ii}=d to enable matrix iterations for isolated nodes. The transition is explicitly explained.
- **"Unfair comparison — GPU vs CPU is systematically biased."** — The paper's contribution is specifically a *GPU-friendly* matrix iterative method; comparing GPU-based execution against standard CPU-based MCF solvers is the relevant practical comparison. A CPU baseline of the same method would be informative (noted in weakness 2) but the comparison as run is not "unfair" or "biased."
- **"Vision dataset mentioned but never used."** — The paper discusses results on very large sparse graphs (Table 3) which includes vision-derived instances; the dataset description is standard context. (Table content is an image and cannot be fully parsed, but the text references solving these instances.)
- **"Truncation operation never defined."** — The truncation for q is defined: q^(0) = max{τ, τ+s} and the paper states that the same truncation applies at each iteration but is naturally satisfied.
- **"Convergence guarantee should be removed as a strength because proof is missing."** — The theorem is stated in the paper. The proof may reside in a stripped appendix. The weakness *about the proof not being in the main text* is retained above; the existence of the claim itself is still a stated contribution, even if incomplete.
- **"Missing related work on GPU MCF solvers."** — Per policy, I cannot assess missing citations without external sources. The paper asserts it is the first GPU-friendly matrix iterative method for MCF, which is a claim the authors are responsible for supporting.
- **"Code release as strength."** — Generic; not a scientific contribution.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper's core trick — introducing a virtual self-flow d with zero cost to create marginal-like constraints — is both the key enabler and a source of subtlety. It allows the Sinkhorn machinery to operate on flow-balance-constrained problems, but it also means the output flow q must be solved for alongside u and v, coupling the kernel update with the scaling vector updates. This three-way coupling (u, v, K) distinguishes the method from standard Sinkhorn and raises legitimate questions about whether the standard Hilbert metric convergence proof carries over without modification when K is not fixed. A careful theoretical analysis of this coupled system would be a meaningful contribution in its own right.

## Suggestions

1. Provide a proof sketch (even 2-3 sentences) for Theorem 1 in the main text, or clarify the Hilbert metric argument in a way that explicitly addresses the non-stationary kernel K^(l).
2. Run OFT-Sinkhorn on CPU (the same algorithm, same hardware, no GPU) for a subset of the benchmarks and report the CPU vs GPU timing to separate algorithmic efficiency from hardware acceleration.
3. Include standard deviations or per-instance results in Tables 1–3, and plot a quantitative convergence metric (e.g., ∥P1−Pᵀ1−s∥ or relative objective error vs. iterations) in the ablation study.
4. Add the convergence threshold check (Err) to Algorithm 1's loop termination condition.
5. Tone down the exact-MCF claims in the conclusion; clarify that the method provides approximate solutions with controlled error, which is appropriate for large-scale or high-precision settings where exact MCF solvers become impractical.
