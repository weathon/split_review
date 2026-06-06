## Summary

The paper proposes Dimension Domain Co-Decomposition (3D), a PINNs framework combining: (1) a shared MLP with coordinate-index inputs for parameter-efficient dimension decomposition, (2) a Mixture-of-Experts router for automatic domain decomposition without predefined partitions, and (3) a Variable Interpretability (VI) metric measuring subspace alignment between learned components and ground-truth factors. Experiments span 5D/10D Poisson, Wave, Viscous Burgers, and Linear Transport equations.

---

## Rebuttal Assessment

### Weakness 1: Missing SPINNs comparison
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly note that the "independent MLPs" baseline corresponds to SPINNs' architectural core (CP-decomposition with separate networks per dimension), confirmed by Section 3.1 (Eq. 2). However, they themselves acknowledge that SPINNs' use of forward-mode automatic differentiation is "a distinct computational feature not replicated by our independent MLPs baseline." This is not a minor omission: forward-mode AD affects both efficiency and the feasibility of gradient computation in high dimensions, potentially making SPINNs more competitive on accuracy than the independent MLPs proxy. The rebuttal's defense that "the primary claim is parameter and memory efficiency… not accuracy superiority over SPINNs" also does not fully hold — Section 4.2 and Figure 2 make accuracy claims for the shared MLP relative to baselines, and SPINNs would be the most natural comparison. The sentence truncation at the page break ("the router breaks the…" on line 80) remains unresolved in Section 3.3: that section describes Dense vs. Sparse MoE trade-offs but does not explicitly complete the SPINNs incompatibility argument.
- **Score impact:** Weakness unchanged

### Weakness 2: No quantitative comparison to APINNs/XPINNs
- **Author's response:** Partially address
- **Assessment:** Partially convincing but narrow. The authors reframe the claim as "automatic decomposition is sufficient to recover physically meaningful structure," not that it outperforms existing methods. This is a legitimate narrowing of scope, consistent with the paper's text ("enables automatic and adaptive domain decomposition" as distinct from claiming superiority). However, this reframing also undercuts the paper's own framing in Section 2.2, which critiques APINNs and XPINNs at length, implying 3D overcomes their limitations. Verified in the paper: the domain decomposition section (Section 4.3) contains only K=1 vs. K=2 vs. K=3 self-comparisons. The authors correctly acknowledge that "a single APINNs row on Viscous Burgers would substantially close this gap."
- **Score impact:** Weakness unchanged

### Weakness 3: VI tested only on exactly separable solutions
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a defense. The rebuttal simply accepts the reviewer's characterization, citing Section 5: "VI relies on reference solutions that are dimension-separable." No additional evidence from the paper is offered. Verified: all six Table 2 cases (5D Poisson ∏sin(πxᵢ), 10D Poisson, 1D Wave sin·cos at c=2,5,10, 2D Wave) have exact product-of-univariate factorizations. Acknowledging this doesn't reduce its impact on the metric's practical scope.
- **Score impact:** Weakness unchanged

### Weakness 4: ℓ₂ errors not reported for Wave equation cases
- **Author's response:** Partially address
- **Assessment:** Unconvincing as a defense. The rebuttal correctly identifies that 10D Poisson does report ℓ₂ alongside VI, but the Wave cases in Table 2 do not. The claim "this demonstrates the template of reporting both metrics" is weak — it shows the authors knew how to do it and chose not to do so for Wave. The ambiguity for Wave c=10 (VI=84.59% at r=5 — lowest in table) is not resolved. No new evidence provided.
- **Score impact:** Weakness unchanged

### Weakness 5: Smooth-transitions Linear Transport deferred to appendix
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal correctly confirms the case exists in Appendix C (verified by paper line 194-198: "the case with smooth transitions is deferred to Appendix C"). The paper's main text genuinely does cover the geometrically simpler case. The reviewer's concern — that this understates the challenge — is acknowledged without resolution.
- **Score impact:** Weakness unchanged

### Weakness 6: Truncated sentence in Section 3.1 (Trivial)
- **Author's response:** Acknowledge
- **Assessment:** The rebuttal claims the full argument appears in Section 3.3. Verified: Section 3.3 explains Dense vs. Sparse MoE selection but does not explicitly complete the truncated argument about why SPINNs' forward-mode AD is incompatible with MoE routing. The argument remains incomplete.
- **Score impact:** Weakness unchanged

---

## Strengths
- **Parameter efficiency concretely documented (Table 1):** Shared MLP reduces parameters from 26,640 to 5,392 for 5D Poisson and 53,280 to 5,392 for 10D Poisson; memory reduced to 30.4% for 10D (69.6% savings). These are hard numbers independent of any baseline comparison.
- **Large accuracy improvement in 10D (Section 4.2):** Shared MLP achieves ℓ₂=1.25×10⁻³ vs. vanilla PINNs 1.29×10⁻¹ on 10D Poisson with comparable parameter counts (5,392 vs. 4,929). The improvement is dramatic and the comparison is fair.
- **Automatic domain decomposition recovers physically correct structure (Figure 4-5):** K=2 on Viscous Burgers cleanly identifies shock at x=0 with ℓ₂ dropping from 0.2108±0.1252 to 0.0011±0.0005 (~190× improvement). Linear Transport recovers diagonal stripe structure. Results are consistent across five seeds.
- **VI metric mathematically sound (Table 2, Section 3.2):** Subspace containment formulation via SVD of QF^T QG is a careful and correct formalization. VI evolves interpretably during training (Figure 3) and correctly tracks learning difficulty (higher-frequency c=10 harder to decompose).
- **Fine-tuning across dimensions (Section 4.2):** 5D→8D transfer is enabled by the separable parameterization; vanilla PINNs cannot do this.
- **Robustness across seeds and noise (Section 4.3):** Five-seed consistency and 5% Gaussian noise robustness demonstrated.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing SPINNs accuracy comparison.** The "independent MLPs" proxy does not account for SPINNs' forward-mode AD, which is SPINNs' key computational innovation (distinct from just having separate networks per dimension). The paper's sentence in Section 3.1 about why forward-mode AD is incompatible with MoE is literally truncated. The rebuttal provides no new evidence that the independent MLPs baseline is a fair surrogate for SPINNs' actual performance. The central evidential gap — whether the shared MLP matches SPINNs accuracy at lower parameter count — remains open.

- **No quantitative comparison to APINNs on domain decomposition.** Section 4.3 demonstrates that MoE decomposition works, but does not demonstrate it is superior to or competitive with the directly related APINNs (Hu et al., 2023) approach, which also uses soft gating. The rebuttal narrows the claim scope honestly but the original concern about the evidential base for the broader claim stands.

### Minor

- **VI scope limited to exactly separable solutions.** Section 5 acknowledges this explicitly. The metric's practical utility as a "deployment-time diagnostic" (the review's framing) for PDEs without known exact factorizations is untested.

- **ℓ₂ errors absent for Wave equation cases.** Table 2 reports only VI for Wave cases. For Wave c=10 (VI=84.59% at r=5, lowest value), it is unknown whether this reflects PDE solution degradation or only representation interpretability failure. The rebuttal acknowledges this as a "presentation inconsistency."

- **Smooth-transitions Linear Transport in appendix.** The geometrically harder case is present in the paper (Appendix C) but not the main text. The reviewer correctly identifies this as the more diagnostic case.

### Trivial
- Truncated sentence in Section 3.1 about SPINNs/forward-mode AD incompatibility. Section 3.3 does not fully resolve it.

---

## Nice-to-Haves
- Add SPINNs (with forward-mode AD) as a baseline on 5D/10D Poisson: single most impactful change.
- Add APINNs as a baseline on Viscous Burgers: transforms Section 4.3 from demonstration to comparative evaluation.
- Report ℓ₂ errors alongside VI in Table 2 for Wave cases, particularly c=10 where VI is incomplete.
- Promote smooth-transitions Linear Transport to main paper; it is the harder and more diagnostic test.
- Test VI on one approximately separable problem to assess graceful degradation.

---

## Novel Insights

The most genuinely novel element is the coordinate-index trick: appending the dimension index j to the input (x_j, j-1) allows a single shared MLP to replace d separate MLPs without losing per-dimension specificity. This makes the architecture simultaneously parameter-efficient and dimension-agnostic (enabling cross-dimensional fine-tuning), while being MoE-compatible in a way that forward-mode AD based designs (SPINNs) are not. The VI metric's formulation via subspace containment rather than subspace identity is also a careful and non-obvious design choice: when the decomposition rank r exceeds the ground-truth factor count s, the correct question is whether the learned r-dimensional subspace *contains* the s-dimensional ground truth, which is exactly what the SVD-based VI measures. This distinction is mathematically well-motivated and could be useful beyond PINNs.

---

## Suggestions
1. Add SPINNs as a direct baseline (with its forward-mode AD) on 5D and 10D Poisson. Even a wall-clock + accuracy table would definitively establish the trade-off.
2. Add one APINNs row on Viscous Burgers to establish competitive positioning for the domain decomposition claim.
3. Add ℓ₂ errors for all Wave cases in Table 2, consistent with the Poisson reporting template.
4. Promote the smooth-transitions Linear Transport experiment to the main paper.

---

## Score and Decision

**Rebuttal impact assessment:** The rebuttal is honest — the authors acknowledge five of six weaknesses without spinning. This honesty is commendable but has the effect of *confirming* rather than alleviating the original concerns. No new evidence is presented from the paper that was not already visible to the original reviewer. The two major weaknesses (no SPINNs comparison, no APINNs comparison) remain open; the three minor weaknesses are acknowledged but unresolved. The rebuttal's one substantive argument — that the independent MLPs baseline is a fair proxy for SPINNs — is weakened by the authors' own acknowledgment that forward-mode AD is a distinct feature not replicated. The truncated sentence about forward-mode AD incompatibility further undermines confidence that the SPINNs comparison was thought through carefully.

**Score movement:** The original score of 5.0 was anchored between HyResPINNs (5.0, rejected) and a stronger upper cluster (5.25–6.00). The rebuttal provides no new evidence to move upward, and the explicit acknowledgment of gaps reinforces the weaknesses. The score remains **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>