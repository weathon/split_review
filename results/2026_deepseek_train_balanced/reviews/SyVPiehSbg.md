## Summary

This paper proposes ActNet, a neural network architecture derived from Laczkovich's 2021 variant of the Kolmogorov Superposition Theorem (KST), argued to be better suited for practical deep learning than the original KST used by KANs. The paper proves universal approximation with bounded depth, provides a stable initialization scheme, and evaluates ActNet on PINN benchmarks where it consistently outperforms KANs (often by orders of magnitude) and is competitive with strong MLP baselines like Siren. ActNet also achieves lower errors than published SOTA results on three challenging PDE benchmarks.

## Strengths

- **Consistent and dramatic outperformance over KANs across all PINN benchmarks.** Table 1 shows ActNet beating KANs on every PDE benchmark, frequently by orders of magnitude (e.g., Poisson w=16: ActNet relative L2 6.3e-4 vs KAN 1.8e-1; Helmholtz w=32: ActNet 1.2e-1 vs KAN 1.6e+0). This directly supports the core claim that the Laczkovich-based architecture outperforms KANs in physics-informed settings.

- **Provably stable initialization with closed-form variance correction.** Theorem 3 provides a clean result: at initialization with N(0,I) inputs, each ActLayer output entry has mean 0 and variance 1, with convergence to standard normal as N or d grows. The closed-form expressions for μ(ω_i,p_i) and σ(ω_i,p_i) in equations (6–8) are explicit and computable — a concrete mathematical property many architectures lack formal guarantees for.

- **New state-of-the-art results on challenging PINN benchmarks.** Table 2 shows ActNet surpassing published SOTA results from the JaxPi library (Wang et al., 2023) on Advection (9.50e-5 vs 6.88e-4), Kuramoto–Sivashinsky first window (1.34e-5 vs 1.42e-4), and full KS (8.53e-2 vs 1.61e-1). These are genuine improvements over well-known PINN results.

- **Strong theoretical grounding and architectural motivation.** The analysis of different KST variants (Table 1 in the paper) makes a clear case for why Laczkovich's formulation is preferable — O(d) inner functions vs O(d²) for the original KST. The universal approximation theorem (two ActLayers, width scaling linearly with d) and the parameter complexity analysis (O(L·m·(m+N)) vs KAN's O(Lm²(G+K))) are both concrete advantages.

- **Thorough experimental protocol.** The comparison section (4.1) uses multiple parameter counts (4 levels), 12 hyperparameter configurations per architecture, 3 seeds per config, and for Poisson/Helmholtz, 6 frequency values — totaling over 2,500 trained networks for the Poisson case alone. The use of exact boundary enforcement removes an orthogonal confounding factor.

## Weaknesses

### Major

- **Unsubstantiated claim about vanishing derivatives.** The abstract and contribution list (line 24) state: "ActNet does not have vanishing derivatives, making it ideal for physics-informed applications." This claim is never supported anywhere in the paper — no gradient analysis, no theorem about gradient norms, no experiment measuring gradient propagation through depth. The basis functions are sinusoids (which individually do not saturate), but vanishing gradients in deep networks arise from the product of Jacobians across layers. A composition of sinusoidal layers feeding into linear layers and summation operations can still suffer from gradient pathologies depending on weight magnitudes and depth. Since this claim appears as a stated contribution, it must be substantiated or removed. Given that the core results do not depend on it, the authors should remove or significantly qualify it.

- **Misleading "ablation studies" section.** Section 4.1 is titled "Ablations Studies" and the experiments are repeatedly referred to as "ablations" (lines 211, 216, 220). However, these experiments compare ActNet against KAN and Siren at varying parameter counts — this is a baseline comparison, not an ablation. An ablation would isolate individual components of ActNet (e.g., sinusoidal basis vs. other bases, with/without the Λ matrix, with/without linear projections, varying basis size N). The architecture has several design knobs, none of which are ablated. The reader cannot tell which design choices are essential. The experiments themselves are valuable, but the mislabeling inflates the apparent depth of analysis.

### Minor

- **Theorem 2's guarantee is narrower than claimed for deep networks.** The theorem proves that for a *single* ActLayer at initialization with N(0,I) input, each output entry has mean 0 and variance 1, converging to standard normal as N or d grows. However, the paper claims (line 186) this "implies that the activations of an ActNet will remain stable as depth and width increase." For deep compositions, the output of layer ℓ becomes the input to layer ℓ+1, and this distribution may not be N(0,I) — the theorem does not automatically iterate across depth. The gap is meaningful because activation stability across depth depends on distributional assumptions propagating, which is not shown.

- **SOTA comparison uses literature baselines without matched-condition re-runs.** Table 2 compares ActNet against published results from the JaxPi library. While informative, the absence of Siren and KAN baselines run under identical conditions on these benchmarks makes it difficult to assess whether ActNet genuinely improves upon the state of the art or benefits from different training setups. Since the paper's Section 4.1 already runs Siren and KAN on other PDEs, extending this comparison to the Advection and KS benchmarks would substantially strengthen the SOTA claims.

- **No runtime comparison despite acknowledging slower speed as a limitation.** The Discussion section lists "slower computational speed when compared to plain MLPs" as the primary limitation of ActNet, but no wall-clock times are reported. Given that the experiments already compare architectures at matched parameter counts, reporting training times would straightforwardly quantify this trade-off.

### Trivial

None.

## Nice-to-Haves

- Include gradient norm measurements across layers during PINN training to substantiate (or retract) the vanishing derivatives claim.
- Perform actual component-level ablations: vary basis functions (B-splines, RFF), remove the Λ matrix, remove linear projections, vary N systematically.
- Report wall-clock training times to quantify the acknowledged speed trade-off.
- Extend the SOTA benchmarks to include Siren and KAN under the same experimental protocol.

## Removed Points

These points are flagged to be removed; treat them with caution.

- Garbled text about "Universality Theorem 1 economizes" — does not convey a coherent criticism; removed.
- "Missing appendix / proof not in text" — The parser strips appendices from all papers; proofs in the appendix are normal and should not be penalized.
- Generic requests for larger datasets or more models — not tied to a specific gap; the current scale (2,500+ networks) is already extensive.
- Strength about "addressing an important problem" — generic; the paper's genuine strengths are specific and evidence-backed; removed.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated claims without identifying unanticipated implications or contradictions.

## Suggestions

1. Remove or substantiate the "no vanishing derivatives" claim — it is currently an unsupported assertion that weakens credibility. Since it is not needed for the main results, simply removing it from the contribution list would be simplest.
2. Rename Section 4.1 to "Baseline Comparisons" and add a brief actual ablation (e.g., varying the basis functions or removing the Λ matrix) to genuinely validate architectural choices.
3. Report training wall-clock times to quantify the stated speed limitation.
4. Clarify the scope of Theorem 2: state precisely that the guarantee applies to a single ActLayer at initialization, and discuss the extent to which it propagates to deeper compositions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>