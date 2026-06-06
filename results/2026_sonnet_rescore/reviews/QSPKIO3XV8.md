## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a PINNs-based framework that unifies (i) dimension decomposition via a parameter-efficient shared MLP that processes coordinate-index pairs, (ii) Mixture-of-Experts (MoE) driven domain decomposition that automatically partitions the solution space without predefined regions or interface conditions, and (iii) a novel Variable Interpretability (VI) metric that quantifies alignment between learned per-dimension representations and ground-truth separable factors. The framework is evaluated on Poisson, Wave, Viscous Burgers, and Linear Transport equations.

---

## Strengths

- **Parameter efficiency with competitive accuracy (Table 1, Figure 2):** The shared-MLP design reduces parameters by 5× (5d Poisson: 5392 vs. 26640) and 10× (10d Poisson: 5392 vs. 53280) compared to independent MLPs, while achieving comparable or better accuracy (ℓ₂ = 1.84×10⁻⁴ vs. 3.26×10⁻⁴ vs. 7.55×10⁻³ for vanilla PINNs on 5d Poisson). Memory reduction scales with dimensionality (30.4% memory usage at 10d Poisson).

- **Quantitative and well-defined VI metric (Table 2, Figure 3):** The VI metric provides a concrete, scale-invariant measure of interpretability. Table 2 shows it converging to 100% with modest rank r (r=4–5) for 5d and 10d Poisson, and Figure 3 provides a visualization of per-component learning dynamics over training steps—a type of analysis not present in prior dimension decomposition work.

- **Automatic, meaningful domain decomposition without predefined partitions (Figure 4, Figure 5):** The MoE router with K=2 identifies the shock at x=0 in Viscous Burgers, reducing ℓ₂ error from 0.2108±0.1252 (K=1) to 0.0011±0.0005 (K=2). For Linear Transport, the router recovers diagonal stripe structures. This is achieved end-to-end without interface loss terms or manual region specification.

- **Robustness and reproducibility (Section 4.3):** Results are reported over five random seeds; domain decompositions remain consistent across seeds and under 5% Gaussian noise on initial/boundary conditions, suggesting the decompositions reflect genuine solution structure rather than initialization artifacts.

- **High-dimensional scalability with transferability (Section 4.2):** A 5D model can be fine-tuned to 8D Poisson, whereas vanilla MLP-PINNs cannot be reused due to mismatched input dimensionality.

---

## Weaknesses

### Fatal
None.

### Major

- **Absence of comparison to any existing soft domain decomposition method.** The domain decomposition contribution is evaluated exclusively against a single-expert baseline (K=1). APINNs (Hu et al., 2023), explicitly discussed in Section 2.2 as using "soft gating mechanisms to allow more flexible domain decomposition," is the closest related method yet never appears as a comparison. XPINNs and cPINNs are similarly absent from the quantitative evaluation in Section 4.3. The paper's claim of superior "automatic and adaptive" decomposition over existing methods is therefore qualitative, not demonstrated quantitatively. Without such comparison, it is unknown whether the observed ℓ₂ improvements and recovered decompositions are better, equivalent, or inferior to existing soft-partitioning approaches.

- **Missing named SPINNs baseline.** The paper's dimension decomposition is architecturally motivated as an improvement over SPINNs (Cho et al., 2023), differing in two ways: shared MLP and backward-mode AD compatibility. While the "independent MLPs" baseline approximates the SPINNs architecture, SPINNs also uses forward-mode AD for computational efficiency, meaning a direct head-to-head on wall-clock time and accuracy is absent. The claim of superseding SPINNs in efficiency therefore remains unsubstantiated with a direct experiment. The paper commits to this framing in Section 3.1 but does not deliver the evidence.

### Minor

- **VI evaluated only on exactly separable problems.** Every problem in Table 2—5d/10d Poisson with solution ∏sin(πxᵢ), Wave equation with solution sin(πx)cos(cπt)—has a clean closed-form separable factorization. This is the easiest possible regime for VI to succeed. The Conclusion acknowledges that "VI relies on reference solutions that are dimension-separable," but no experiment on an approximately or weakly separable problem is included. The scope of the VI metric's utility is therefore untested for the majority of PDEs encountered in practice. This does not invalidate VI in the separable setting but limits the strength of the interpretability claim.

- **Missing ℓ₂ accuracy for the c=10 Wave case.** Table 2 reports VI=84.59±3.42 at r=5 for the c=10 Wave equation, but nowhere in the main text is the corresponding ℓ₂ error reported. Without this, it is ambiguous whether the sub-100% VI reflects a genuine decomposition limitation or merely a convergence failure in the PDE solution itself—two very different implications for the framework.

### Trivial

- The sentence in Section 3.1 explaining SPINNs' forward-mode AD incompatibility with MoE is cut off by a parser artifact ("...the router breaks the"). This is a parser rendering issue in the extracted PDF, not a paper issue.

---

## Nice-to-Haves

- A direct comparison to SPINNs including wall-clock time, memory, and ℓ₂ accuracy on shared benchmarks would significantly sharpen the efficiency-versus-accuracy trade-off analysis.
- Evaluating VI on a problem where the solution is approximately (but not exactly) separable—e.g., a solution dominated by a separable component with a small non-separable perturbation—would test the metric's graceful degradation and greatly expand its claimed scope.
- Reporting error bars on ℓ₂ accuracy in Figure 2 and Section 4.2 (the paper already reports them for Burgers), consistent with the five-seed protocol used for VI in Table 2.
- The smooth-transition variant of Linear Transport (deferred to Appendix C) is arguably the harder, more informative case; surfacing its quantitative results in the main paper would strengthen the domain decomposition narrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Truncated SPINNs/AD compatibility sentence is a conceptual gap."** The sentence ends mid-phrase due to PDF parsing at a page boundary. This is a parser artifact, not an author omission in the original submission. Removed per the hard rule on formatting artifacts.

- **Harsh Critic: "VI's containment interpretation is trivially weak at large r."** The paper explicitly addresses this in Section 3.2: "when s < r, VI = 1 means that the exact one-dimensional subspace is fully contained in the predicted subspace." The authors acknowledge this interpretation and argue it is "particularly relevant in practice, since r can be chosen arbitrarily large while s is often much smaller." The concern is already addressed in the paper, removing its basis as an unaddressed weakness.

- **Harsh Critic: "Shared MLP may not respect structural differences (e.g., time vs. space)"** — This is a speculative concern about a potential failure mode with no experimental evidence of failure, and the paper provides successful results on Wave equations where time and space play structurally different roles. Removed as unanchored speculation.

- **Harsh Critic: "Smooth transitions deferred to Appendix understates difficulty."** This ordering choice is noted but framed as a fatal structural omission. Results for smooth transitions do exist (Section 4.3 explicitly confirms they are in Appendix C). Demoted to a nice-to-have for surfacing in the main text.

- **Strength Finder: "The framework addresses an important problem."** Generic claim about problem importance; dropped per filtering rules.

---

## Novel Insights

The most genuinely novel synthesis from this review is the identification of a structural tension in the VI metric: the paper's dimension decomposition is specifically well-suited to separable solutions, and VI is defined only for separable solutions, creating a self-reinforcing evaluation loop. All benchmark problems are chosen from within this regime. This is not a methodological flaw in the decomposition itself—the experiments on Poisson and Wave equations are legitimate—but it means the paper provides no evidence that either the architecture or the metric generalizes beyond the separable case. The practical scope question (how often are real PDEs of interest well-approximated by separable solutions?) is the key open question the paper leaves unaddressed, and addressing it would substantially change the impact assessment.

---

## Suggestions

1. Add a quantitative comparison to APINNs on the Viscous Burgers benchmark (same viscosity, same collocation grid). This single experiment would transform the domain decomposition section from a qualitative demonstration into a comparative evaluation.
2. Add a named SPINNs baseline (or explicitly benchmark against the implementation from Cho et al., 2023) at matched parameter counts to validate the claimed efficiency improvement with a direct peer comparison.
3. Report ℓ₂ accuracy alongside VI in Table 2, including for the c=10 Wave case, so readers can correlate interpretability scores with solution quality.
4. Include at least one experiment where VI is computed against a truncated Fourier approximation of a non-separable solution, even if only as a qualitative pilot, to bound the metric's applicability.

---

**Evaluation axes:**

- **Originality:** The shared-MLP indexing trick is a clean engineering contribution; VI is a novel metric. The MoE-for-domain-decomposition angle is incremental relative to APINNs. Moderate originality overall.
- **Importance:** High-dimensional PDE solving with interpretability is a genuine challenge; the automatic domain decomposition without interface conditions is a practically valuable property.
- **Claims supported:** The accuracy and efficiency claims on dimension decomposition are well-supported. The domain decomposition claims are supported only relative to a K=1 baseline, not relative to the field.
- **Soundness:** Methodology is internally consistent and mathematically clear. Key experiments are missing, weakening the evidential chain.
- **Clarity:** Writing is generally clear; the paper is well-organized. The VI definition and motivation in Section 3.2 is particularly lucid.
- **Community value:** Useful contribution to the PINNs community, but impact is limited by the narrow evaluation scope.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>