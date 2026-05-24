## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a PINN framework that unifies two strategies: (i) a CP-like dimension decomposition within each expert using a shared MLP that processes coordinate-index pairs (reducing parameters vs. per-dimension networks), and (ii) a dense Mixture-of-Experts router that automatically partitions the spatial domain without predefined subdomains or interface conditions. The authors also introduce Variable Interpretability (VI), a metric based on principal angles between learned and ground-truth per-dimension subspaces. Experiments on Poisson, Wave, Burgers, and Linear Transport equations demonstrate parameter efficiency, interpretable component recovery, and automatic shock/stripe detection through the MoE gates.

## Strengths

- **Shared-MLP design is practical and well-validated.** Table 1 demonstrates substantial parameter reduction (e.g., 5,392 vs. 26,640 for 5d Poisson), and Figure 2 shows the shared MLP matches or exceeds independent per-dimension MLPs in accuracy while using far fewer parameters. The 10d Poisson experiment (line 143) provides a genuine capacity-matched comparison: shared MLP (5,392 params) achieves ℓ₂ error 1.25×10⁻³ vs. 1.29×10⁻¹ for a standard PINN with 4,929 parameters — a two-order-of-magnitude improvement at comparable capacity.

- **VI metric addresses a real gap.** Prior dimension-decomposition PINN methods (Cho et al. 2023, Liu et al. 2024) lack any quantitative measure of per-dimension alignment. The VI metric is mathematically well-defined (QR + singular values of subspace cross-product), and Table 2 shows it behaves sensibly — reaching VI≈1 for separable solutions when rank r is sufficient. The 1d Wave experiment (Figure 3) visually corroborates that high VI corresponds to genuine recovery of the analytical sin/cos factors.

- **MoE gates produce visually compelling domain partitions.** Figures 4–5 show the router cleanly separating the shock at x=0 for Burgers and recovering diagonal stripes for Linear Transport, without any manual region specification. The error drop on Burgers from K=1 (0.21) to K=2 (0.001) is dramatic. The paper also reports consistency across five random seeds and robustness to 5% noise in boundary/initial data.

- **The combination is genuinely novel.** Integrating CP-style dimension decomposition inside MoE experts for PINNs, with the shared-MLP indexing trick to keep parameter counts low, is a creative synthesis not present in prior work.

## Weaknesses

### Fatal

None.

### Major

- **No comparison with existing domain-decomposition PINN methods.** The paper discusses XPINN, cPINN, APINN, and BPINN in related work (Section 2.2) and positions automatic, interface-free decomposition as a primary contribution. Yet it never benchmarks against any of these methods on Burgers or Transport, where the ground-truth partition is known and could be supplied to those baselines. Without this comparison, a reader cannot judge whether the automatic MoE decomposition offers practical advantages over simply giving XPINN the correct shock location. This is the most significant experimental gap in the paper.

- **No capacity-controlled ablation for the MoE setup.** The Burgers error drops from 0.21 (K=1, single expert) to 0.001 (K=2, two experts + router). But K=2 approximately doubles the expert parameters and adds a 5-layer router MLP. While the magnitude of improvement strongly suggests that domain decomposition — not just added capacity — drives the gain, an experiment with a wider/deeper single-expert model matched to the K=2 total parameter budget would make this separation of effects unambiguous. (Note: the paper does provide a capacity-matched comparison for the dimension-decomposition component in the 10d Poisson experiment; the gap is specific to the MoE domain-decomposition claim.)

### Minor

- **VI measures subspace inclusion, not per-dimension component identifiability.** As the paper itself acknowledges (Section 3.2), when the ground-truth factor has rank s < r, VI=1 means the exact subspace is contained in the learned r-dimensional subspace — which is weaker than the learned components individually matching the true factors. The paper partially addresses this through Figure 3's visual component plots, but the gap between "subspace containment" and "interpretable components" merits more discussion, especially for problems where the true factors are not known to be low-rank.

- **No quantitative analysis of router specialization.** The paper asserts that dense MoE "avoids expert collapse" (Section 3.3), but provides only visual gate heatmaps as evidence. Quantitative measures — router output entropy during training, pairwise correlation of expert predictions, sensitivity to initialization — would strengthen confidence that the method reliably induces specialization rather than converging to near-identical experts in some runs. The five-seed consistency check is mentioned but the actual plots are not visible in the main text.

- **Evaluation limited to separable, low-dimensional problems.** All benchmarks have analytically separable solutions and at most 10 spatial dimensions. The paper acknowledges that VI requires separable reference solutions (Conclusion), but the domain-decomposition claim would be more convincing if tested on a problem where the optimal partition is less obvious than a single vertical shock or diagonal stripes.

### Trivial

- The SPINNs comparison sentence on page 4 is truncated mid-thought ("because the router breaks the"), though this appears to be a parser artifact rather than an author error.

## Nice-to-Haves

- A quantitative router analysis (entropy of gate distributions, expert output diversity) would make the specialization claim more convincing without requiring new baselines.
- Testing on a non-separable or higher-dimensional PDE would stress-test both the domain decomposition and the VI metric.
- Reporting measured GPU memory usage in absolute terms (not just percentages) would strengthen the memory-efficiency claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The 10-layer MLP has ~33k parameters vs. the shared MLP's 5k, making the comparison misleading"** — REMOVED. The paper provides a genuine capacity-matched comparison in the 10d Poisson experiment (line 143: 5,392 vs. 4,929 parameters), where the shared MLP still achieves dramatically better accuracy. The Figure 2 comparison with a deeper vanilla PINN is an additional demonstration, not a flawed control.

- **"No experiment controls for total capacity" in the dimension-decomposition setting** — REMOVED (for the Poisson case). The 10d Poisson experiment explicitly does this. The capacity concern remains valid only for the MoE domain-decomposition setting (retained as Major above).

- **"Appendix was stripped; the paper is incomplete as presented"** — REMOVED per instructions. The parser strips appendices from all papers; the original submission includes this content.

- **"The paper asserts dense MoE avoids expert collapse, but this is opposite to common observation"** — PARTIALLY REMOVED. The qualitative claim is debatable but the core concern about lack of quantitative evidence is retained as Minor. The framing as "opposite to common observation" is speculative and removed.

- **"VI metric's usefulness in any non-trivial setting is unclear"** — WEAKENED and moved to Minor. The paper is transparent about the metric's assumptions and the VI scores behave sensibly across tested problems. The concern is real but the paper does not overclaim.

- **"No discussion of variance across dimensions or how VI relates to prediction quality"** — REMOVED. Table 2 reports means with standard deviations across seeds, and the paper separately reports ℓ₂ errors. The VI and accuracy are different constructs by design.

- **"The Linear Transport case with clearly separable regions is hand-picked"** — REMOVED. The paper acknowledges a smooth-transition variant exists and defers it to the appendix; this is standard experimental practice, not cherry-picking.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface insights that the paper itself had not already identified (e.g., the paper already acknowledges VI's reliance on separable reference solutions and the need for more general metrics).

## Suggestions

- The single most impactful addition would be a comparison against at least one domain-decomposition PINN baseline (XPINN or APINN) on the Burgers and Transport problems. Supply the baseline with the ground-truth partition; this would directly test the claimed advantage of automatic decomposition.
- For the MoE capacity concern, train a single-expert model with width/depth scaled to match the K=2 total parameter budget and report the error. This is a straightforward ablation that would cleanly separate the effect of domain decomposition from added capacity.
- Add a table or figure showing router output entropy and expert-output correlation across training for a representative run. This would quantitatively support the specialization claim without requiring new baselines.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison to 3D |
|--------|-----------|-------|-------------------|
| R5FzCFR5yU (Hybrid Numerical PINNs) | 3.33 | R1 | 3D has substantially more novelty and better experimental support |
| Q9OGPWt0Rp (Connecting Solutions via PINNs) | 5.25 | R1/R2 | Comparable in ambition; 3D has broader experiments across 4 PDE families |
| 5rfj85bHCy (HyResPINNs) | 5.00 | R1/R2 | 3D has more diverse contributions and more PDE benchmarks |
| 4KKqHIb4iG (Backprop-free PDE solvers) | 5.60 | R2 | Most comparable anchor; both have strong ideas with experimental gaps; 3D slightly weaker on rigor |
| y5B0ca4mjt (PIG: Physics-Informed Gaussians) | 6.50 | R2 | PIG has cleaner execution, more thorough experiments, and theoretical backing; 3D is clearly below |

**Round-1 bracket:** 5.0–7.0 based on comparison with low (3.33), middle (5.00–5.25), and high (7.60–8.00) anchors.

**Round-2 narrowing:** The paper sits between the 5.60 "Backprop-free" anchor (similar strengths and gaps, but that paper had more extensive benchmarks) and the 6.50 "PIG" anchor (better execution, theoretical proof). The missing comparison to domain-decomposition PINN baselines is the decisive factor preventing a higher score. The paper is comparable to the 5.60 anchor — both have genuinely novel ideas and good results, but experimental gaps hold them below the acceptance threshold for venues at this level.

**Final score: 5.5. Decision: Reject.** The core ideas (shared-MLP dimension decomposition, VI metric, MoE-driven automatic domain decomposition) are creative and well-motivated. The shared-MLP design is convincingly validated. However, the domain-decomposition contribution — presented as a primary innovation — cannot be properly assessed without comparison to existing domain-decomposition PINN methods (XPINN, APINN, etc.). This is a significant experimental gap that a rebuttal could address, but as the paper stands, it prevents the work from meeting the bar for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>