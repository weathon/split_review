## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a PINNs framework that (1) uses a shared MLP with indexed inputs for parameter-efficient dimension decomposition, (2) introduces a Variable Interpretability (VI) metric based on subspace alignment to quantify how well learned per-dimension components match ground-truth factors, and (3) employs a dense Mixture-of-Experts (MoE) router for automatic domain decomposition without predefined subdomains or interface conditions. Evaluated on Poisson (5d, 10d), Wave (1d, 2d), Viscous Burgers, and Linear Transport equations.

## Strengths

1. **Shared-MLP design with indexed inputs (Section 3.1, Table 1):** Replacing per-dimension independent MLPs with a single MLP that takes both coordinate value and dimension index as input yields substantial parameter reductions — e.g., from 26,640 to 5,392 for 5d Poisson, and the advantage grows with dimensionality (10d: 53,280 vs. 5,392). This directly addresses the scalability bottleneck of prior dimension-decomposition approaches. The reduction is cleanly documented and the architecture is clearly described.

2. **Variable Interpretability (VI) metric (Section 3.2, Table 2, Figure 3):** A mathematically principled, scale-invariant metric based on subspace alignment (QR decomposition + SVD of the cross-Gram matrix). Table 2 systematically measures VI across six problem settings and varying rank r, and Figure 3 demonstrates that VI can monitor per-dimension learning progress during training — a capability absent from prior decomposition-based PINN methods. The metric is well-defined and the paper is transparent about its interpretation (subspace containment vs. identity).

3. **MoE-driven domain decomposition without predefined interfaces (Section 3.3, Figure 4):** The dense MoE router learns soft partitions automatically. For Viscous Burgers, the ℓ₂ error drops from 0.2108 (K=1, no decomposition) to 0.0011 (K=2), and the router discovers the shock at x=0. The paper reports results over five random seeds and tests with up to 5% noisy boundary/initial conditions, showing the decomposition is driven by intrinsic PDE geometry rather than initialization. Figure 5 similarly demonstrates meaningful decomposition for the Linear Transport equation.

4. **Consistency and robustness analysis (Section 4.3):** The paper reports results over five random seeds and tests robustness to noise, which is more thorough than single-run evaluations common in this area.

## Weaknesses

### Fatal

None.

### Major

1. **No quantitative comparison against the most relevant baselines — SPINNs and APINNs.** The paper positions itself as improving upon dimension-decomposition PINNs (SPINNs is cited at line 80 with explicit comparison claims) and domain-decomposition PINNs (APINNs, which uses soft gating similar in spirit to MoE, is cited at line 46). Yet every accuracy, convergence, and parameter-count comparison is drawn only against "vanilla PINNs" — a baseline far behind the state of the art for these problems. The reader cannot assess whether 3D outperforms SPINNs, XPINNs, or APINNs because no accuracy numbers, convergence curves, or parameter counts for those methods appear anywhere. The claim that the framework "improves both computational efficiency and solution accuracy" is unsubstantiated for the methods it claims to improve upon. The comparison against "independent MLPs" (a self-constructed per-dimension baseline) is informative for the shared-vs-independent ablation but is not a standard published baseline. **This is the most consequential omission; without it, the paper's central empirical claims cannot be properly evaluated.**

2. **The 10d Poisson comparison (line 139) compares against a vanilla MLP that lacks the inductive bias the method exploits.** The shared MLP architecture explicitly encodes the product-separable structure of the solution via Eq. 3 (CP-decomposition form), while the vanilla PINN baseline (4-layer MLP, width 64) has no such inductive bias. The shared MLP's strong performance (1.25×10⁻³ error vs. 1.29×10⁻¹) is expected given it embeds the solution's known structure. SPINNs, which also encodes separability via a different mechanism, would be the proper baseline to demonstrate whether the shared-MLP design offers advantages beyond the separable inductive bias itself.

### Minor

1. **VI metric's demonstrated scope is limited to problems where the factorization is already known from the analytical form.** The paper acknowledges (lines 100, 208–209) that VI requires reference solutions that are dimension-separable, and suggests constructing separable approximations (e.g., truncated Fourier series) for non-separable cases — but this is not demonstrated or analyzed. The contribution framing ("a novel, quantitative, scale-invariant metric to evaluate dimension-wise interpretability") overstates the scope relative to what is actually shown: VI is validated only on problems where the factorization is already known. Additionally, when s < r, VI=1 means the ground-truth subspace is contained in the predicted subspace (not identical to it), meaning extra predicted dimensions have no physical interpretation — the paper is transparent about this, but it weakens the interpretability claim.

2. **MoE-driven domain decomposition is insufficiently differentiated from APINNs' soft gating.** The related work (line 46) notes APINNs already uses "soft gating mechanisms to allow more flexible domain decomposition." Since both APINNs and the proposed approach learn soft partitions automatically, the novelty lies primarily in the combination with dimension decomposition — which should be stated more precisely. The paper does not explain what distinguishes its dense MoE from APINNs beyond architecture details, nor does it compare accuracy against APINNs.

3. **Technical gap: differentiation through the router.** The paper states (line 80–81) that SPINNs' forward-mode AD is "not directly compatible with MoE because the router breaks the..." but the sentence is cut off and the technical resolution is never described. Since end-to-end training is claimed (line 110), the reader needs to understand how gradients flow through the combined dimension-decomposition + router architecture.

4. **The dimension decomposition alone performs poorly on Burgers (K=1 error: 0.2108), and the MoE accounts for virtually all of the improvement.** This suggests the two components are not synergistic for non-separable problems. The paper would benefit from ablating what a K=2 standard MLP (no dimension decomposition) achieves on Burgers to isolate whether MoE alone drives the improvement.

### Trivial

None.

## Nice-to-Haves

- Ablation showing (a) standard MLP K=1, (b) dimension decomposition K=1, (c) standard MLP K=2/MoE, (d) full 3D K=2 on Burgers, to isolate component contributions.
- Demonstration of VI on a problem where the factorization is constructed (e.g., via Fourier series) rather than given analytically.
- Comparison of training time vs. SPINNs at equivalent accuracy levels, rather than just parameter counts.
- Analysis of scaling to higher dimensions (50d, 100d).

## Removed Points

- **"Convergence comparison is potentially misleading":** Removed. The paper is transparent about training budgets — it explicitly states the shared/independent MLPs terminate at 11,400 steps and vanilla PINN at 23,400, and reports errors at each model's termination. The figure truncation is clearly explained.
- **"Missing classical solver comparison":** Removed. Scope creep — the paper evaluates against neural PDE solvers, and the motivating problems (high-dimensional, sharp features) are explicitly those where classical solvers struggle.
- **"Independent MLPs not a published method":** Merged into Major weakness 1 rather than as a standalone point.
- **"VI measures convergence quality, not interpretability":** Removed as a standalone point — the paper acknowledges the optimization difficulty effect. Merged into Minor weakness 1's framing.
- **Generic related-work complaints (missing citations):** Removed — the issue is missing quantitative comparison, not missing citations. The paper does cite SPINNs, XPINNs, and APINNs.
- **"Scope of empirical problems is narrow" / "only up to 10d":** Moved to Nice-to-Haves. The problems tested are standard PINNs benchmarks and the paper's scope (4 PDEs, multiple dimensions) is reasonable for a conference paper.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface evaluation gaps rather than new perspectives on the method.

## Suggestions

1. **Add SPINNs and APINNs as baselines** in all relevant experiments. Without this, the paper's central empirical claims cannot be properly evaluated.
2. **Ablate the dimension decomposition and MoE components independently** on Burgers — specifically compare standard MLP K=1, dim-decomp K=1, standard MLP K=2/MoE, and full 3D K=2.
3. **Clearly differentiate the MoE approach from APINNs' soft gating** — either explain architectural differences, show improved accuracy, or precisely scope the novelty to the combination with dimension decomposition.
4. **Explain how gradients flow through the router + dimension decomposition** architecture.
5. **Demonstrate VI on a problem where the factorization is not trivially known** from the analytical form.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| R5FzCFR5yU.md (Hybrid Numerical PINNs) | 3.33 | R1 | Clearly weaker — fundamental flaws in problem framing |
| hghJJJUJJR.md (DimOL) | 3.00 | R1 | Clearly weaker — different domain (operator learning) |
| SYiOxXWlKU.md (EPINN) | 2.50 | R1 | Clearly weaker — single activation function change |
| BvMuyqPvk1.md (MoE DeepONets) | 4.33 | R1 | Slightly weaker — comparable MoE ideas, less interpretability contribution |
| MUL7tKvNei.md (M²M) | 4.00 | R2 | Clearly weaker — unsupported claims, incorrect theory |
| 5rfj85bHCy.md (HyResPINNs) | 5.00 | R1/R2 | Comparable — different weakness profile: limited PDE benchmarks vs. missing baseline comparisons |
| tl63stKeSC.md (Learnable Quadrature) | 4.50 | R2 | Comparable — similar score level |
| Q9OGPWt0Rp.md (Connecting Solutions) | 5.25 | R2 | Slightly stronger — more complete evaluation despite limited PDE scope |
| ApjY32f3Xr.md (PINNacle) | 5.25 | R2 | Different category (benchmark paper) |
| q4AEBLHuA6.md (GP PDE Solver) | 5.75 | R1 | Stronger — accepted, more complete evaluation |

**Round 1 bracket:** 4.0–5.5
**Narrowing:** After reading HyResPINNs (5.00, reject) and "Connecting Solutions" (5.25, reject), our paper's missing baseline comparison (no SPINNs/APINNs) is more consequential than their scope limitations. Comparing against M²M (4.00, reject) and MoE DeepONets (4.33, reject), our paper is clearly stronger. The paper sits between these bands.
**Final score justification:** The paper has genuine contributions — the shared-MLP design is clean and effective, the VI metric is mathematically principled, and the MoE decomposition produces interpretable partitions. However, the missing comparison against the most relevant baselines (SPINNs, APINNs) is a significant evaluation gap that prevents proper assessment of the paper's claimed advantages. Score 4.5 reflects a paper with promising ideas that needs substantially stronger empirical validation before acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>