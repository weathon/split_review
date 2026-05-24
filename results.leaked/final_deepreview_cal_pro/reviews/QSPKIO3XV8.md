Now I have a clear picture. Let me synthesize everything into the final review.

---

## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a unified PINN framework that combines CP-style dimension decomposition with Mixture-of-Experts (MoE) domain decomposition. Within each expert, a shared MLP processes coordinate–index pairs to produce per-dimension functions with drastically fewer parameters than independent per-dimension networks. The authors also introduce Variable Interpretability (VI), a metric that uses QR decomposition and singular values to measure subspace alignment between learned per-dimension components and ground-truth factors. At the MoE level, a router adaptively partitions the domain so experts specialize in local regions without predefined subdomains or interface conditions. Experiments on Poisson, Wave, Burgers, and Transport equations demonstrate parameter efficiency, interpretability measurement, and adaptive domain decomposition.

## Strengths

- **Parameter efficiency via shared MLP is well-demonstrated.** Table 1 shows the shared MLP uses 5,392 parameters vs. 26,640 for independent MLPs on 5D Poisson, and the parameter count stays constant as dimensionality grows (identical 5,392 for 10D Poisson). On 10D Poisson with comparable parameter budgets (5,392 vs. 4,929), the shared MLP achieves ℓ₂ error of 1.25×10⁻³ vs. 1.29×10⁻¹ for a standard PINN — a two-order-of-magnitude improvement at similar capacity (Section 4.2).

- **The VI metric provides a principled, quantitative tool for measuring interpretability of dimension-decomposed representations.** The metric uses QR decomposition and singular values of Q_F^⊤ Q_G to measure subspace alignment, yielding values in [0,1]. Table 2 shows VI reaches 99.99% at r=4 for 5D Poisson, confirming recovery of the true sin(πx_i) components. Figure 3 demonstrates that VI captures learning dynamics (low-frequency components learned before high-frequency ones), adding diagnostic value beyond a single final number.

- **The MoE-driven domain decomposition produces meaningful, automatic partitions with large accuracy gains.** On viscous Burgers' equation, with K=2 experts, the router autonomously identifies the shock at x=0 as the splitting boundary (Figure 4), reducing relative ℓ₂ error from 0.2108 (K=1) to 0.0011. On the linear transport equation, learned gates for K=3 and K=4 align with the diagonal stripe structures of the solution (Figure 5). These partitions are consistent across random seeds and robust to 5% noise in initial/boundary conditions.

## Weaknesses

### Major

- **No experimental comparison against existing domain decomposition PINN baselines (APINNs, XPINNs).** The paper's central claim is that the MoE router enables automatic domain decomposition "without requiring predefined subdomains or explicit interface conditions." However, APINNs (Hu et al., 2023), which the paper itself cites in Section 2.2, already uses soft gating mechanisms for flexible domain decomposition. The paper never experimentally compares against APINNs, XPINNs, or any other domain decomposition method. Without these comparisons, the claimed advantage of the MoE approach over existing methods is unsubstantiated. This is the most significant weakness and directly undermines a core contribution.

- **The integrated 3D framework is never tested on a problem that is simultaneously high-dimensional and has sharp features.** The dimension decomposition is evaluated on smooth problems (Poisson up to 10D, Wave 1D/2D), while domain decomposition is evaluated on low-dimensional problems with sharp features (Burgers 2D, Transport 2D). The abstract and introduction frame 3D as addressing both "high-dimensional settings and when modeling solutions with sharp features," but no experiment tests the combination. The Burgers and Transport experiments do use dimension decomposition inside each expert, but they are only 2D — they do not demonstrate that the combined framework scales to high dimensions with sharp features.

### Minor

- **VI is only applicable to separable PDEs with known reference factorizations.** The paper acknowledges this in the conclusion ("VI relies on reference solutions that are dimension-separable"), but the abstract and introduction present VI as a general interpretability measure without this qualification. For the non-separable Burgers and Transport problems used to showcase domain decomposition, VI cannot be meaningfully computed. This limits the practical scope of the metric, and the framing should be more precise throughout.

- **The behavior of VI on the Wave equation with r=1 is not adequately explained.** For the 1D Wave equation with c=5 and c=10, r=1 yields low VI (49.26% and 41.71% respectively) even though the analytic solution u(t,x)=sin(πx)cos(cπt) is exactly a rank-1 product of two univariate functions. The paper states that "r=1 is no longer sufficient for full interpretability" but does not explain why a rank-1 factorization would fail for a rank-1 solution. This suggests the model's internal representation may not directly correspond to the analytic factorization, and the VI metric may be capturing a different phenomenon than what is claimed.

- **The shared MLP comparison against vanilla PINNs on 5D Poisson uses architectures of very different capacities.** The vanilla PINN uses a 10-layer MLP (width 64) while the shared MLP uses 2 hidden layers — a comparison that conflates architectural depth with the benefit of dimension decomposition. The paper does provide a fair comparison on 10D Poisson (4 layers, comparable parameters), which partially addresses this, but the prominently displayed Figure 2 comparison is misleading.

### Trivial

- **The robustness test (5% noise) is mentioned but deferred to Appendix C**, which is stripped in the review copy. The main text should at minimum summarize the finding.

## Nice-to-Haves

- A sensitivity analysis of the router architecture (depth, width, activation) on the quality of the learned domain decomposition.
- A study of how the rank r inside experts interacts with the MoE gating (e.g., does increasing r change the learned partition?).
- Wall-clock time and GPU memory comparisons against baselines for the domain decomposition experiments.
- A discussion of what happens when the true solution is not low-rank — does the decomposition still yield a useful approximation?

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper mischaracterizes the novelty of its domain decomposition."** The harsh critic claimed the paper contradicts itself by citing APINNs (which uses soft gating) while claiming all existing approaches require predefined partitions. The paper does say APINNs "use soft gating mechanisms to allow more flexible domain decomposition," and then states "all existing approaches require predefined partitions." Without access to the APINNs paper to verify whether it truly requires predefined partitions, this accusation is speculative. The real issue is the lack of experimental comparison, which is kept as a Major weakness.

- **"The comparison of shared MLP against independent MLPs is too narrow."** The paper does show the shared MLP works well on the problems tested (separable Poisson, Wave). The criticism that it's not tested on non-separable problems is partially scope-creep — the dimension decomposition is explicitly designed for separable/low-rank structure. However, the fair-comparison concern about the 5D vanilla PINN baseline is kept as a Minor weakness.

- **"The lack of comparison to APINNs/XPINNs is fatal"** — kept but as Major, not Fatal, because the paper has other contributions (shared MLP, VI) that stand independently, and the domain decomposition results (Burgers error reduction) are genuinely impressive even without the baseline comparisons.

- **Strength Finder's "Robustness and consistency" strength** — the evidence is deferred to appendix (stripped). Kept as a supporting observation but not elevated to a main strength.

- **Strength Finder's "Scalability and reusability" strength** — the fine-tuning claim is also deferred to appendix. The parameter-count independence from dimension is already captured in the first strength; the fine-tuning claim is weakened by being appendix-only.

## Novel Insights

The combination of CP-style dimension decomposition with MoE-based domain decomposition within a single end-to-end trainable PINN framework is a genuinely interesting architectural idea. The VI metric's use of QR decomposition to compare subspaces (rather than individual component vectors) is a clever way to handle permutation and scaling invariance. The observation that the router naturally discovers physically meaningful partitions (the shock at x=0 in Burgers, diagonal stripes in transport) without explicit interface losses suggests that soft gating alone, when combined with the right expert architecture, can serve as an effective domain decomposition mechanism.

## Suggestions

- The single most impactful addition would be to compare against APINNs on the Burgers and Transport problems. This would directly test whether the MoE router offers advantages over existing soft-gating approaches. If APINNs performs similarly, the paper should acknowledge this and clarify what (if anything) the MoE design adds — perhaps ease of training, stability, or integration with dimension decomposition.
- Run the 3D framework on a 5D (or higher) PDE with sharp features — for example, a multi-dimensional Burgers-type equation or a high-dimensional transport problem with discontinuities. This would validate the central claim that the integrated framework handles both challenges simultaneously.
- Reframe VI more precisely in the abstract and introduction: it is a verification tool for separable problems with known factorizations, not a general interpretability measure for arbitrary PDEs.
- Include a short explanation for why r=1 gives low VI on the Wave equation with c=5,10 despite the theoretically rank-1 solution.
- Bring the noise-robustness results into the main text, even as a brief paragraph.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| zUlK1qMIcE (Active partitioning) | 3.00 | R1 | Much weaker — different domain, limited validation |
| SYiOxXWlKU (EPINN) | 2.50 | R1 | Much weaker — narrow ODE contribution |
| BvMuyqPvk1 (MoE DeepONets) | 4.33 | R1 | Similar MoE theme but operator learning, not PINN |
| MUL7tKvNei (M²M) | 4.00 | R1 | Multi-expert for PDEs but different approach |
| 5rfj85bHCy (HyResPINNs) | 5.00 | R1/R2 | Comparable quality — novel PINN architecture, limited PDE benchmarks, experimental gaps. Current paper has more PDE types and a more unified framework but similar baseline gaps. |
| LXVZQpEb2y (DisentangO) | 5.50 | R3 | Comparable — interpretability focus, limited empirical validation of interpretability claims. Current paper's VI is more concretely validated but domain decomposition comparison gap pulls it down. |
| jqVj8vCQsT (Neural Solver) | 5.60 | R3 | Split reviews; interesting idea but weak experiments. Current paper has stronger experiments but clearer gaps. |
| ApjY32f3Xr (PINNacle) | 5.25 | R2 | Benchmark paper, different category. |
| y5B0ca4mjt (PIG) | 6.50 | R2 | Stronger — theoretical proof, sufficient baselines, detailed ablation. Current paper is weaker. |
| hj9ZuNimRl (MM-PDE) | 6.00 | R2 | Stronger — theoretical analysis + empirical validation. Current paper is weaker. |

**Round 1 bracket:** [4.0, 6.5] based on comparison against weak (2.5-3.4), middle (4.0-5.0), and strong (7.6-8.0) anchors.

**Round 2/3 narrowing:** The paper sits between HyResPINNs (5.00) and DisentangO (5.50). It has more empirical breadth than HyResPINNs (4 PDE families vs. 2, plus a novel interpretability metric) but shares similar experimental gap issues. It has a more concretely validated interpretability contribution than DisentangO but lacks that paper's theoretical analysis. It is clearly weaker than PIG (6.50) and MM-PDE (6.00), which have stronger validation and/or theoretical grounding.

**Final score: 5.0.** The paper's strengths (parameter-efficient shared MLP, VI metric, adaptive domain decomposition with impressive Burgers results) are offset by a major weakness: no comparison against directly relevant domain decomposition baselines (APINNs, XPINNs) that would substantiate the claim of automatic partitioning without predefined subdomains. The lack of an integrated high-D + sharp-features experiment further weakens the central framing. The paper is a solid borderline contribution with real ideas but insufficient experimental validation for its strongest claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>