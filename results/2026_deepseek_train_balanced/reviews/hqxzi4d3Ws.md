## Summary

This paper applies classical randomized smoothing (Cohen et al., 2019; Tecot & Hsieh, 2021) to certify robustness of parameterized quantum circuit (PQC) classifiers against parameter gate noise. The key idea is to construct a "smoothed" PQC classifier by adding Gaussian noise to circuit parameters during training, then certify that small parameter perturbations will not change the classifier's output. The paper observes that this training procedure aligns structurally with Evolutionary Strategies (already used for PQC optimization), enabling a natural implementation via objective-function substitution. Experiments on two quantum phase classification tasks (cluster phase and SPT state preparation, 8–12 qubits) demonstrate the resulting robustness-accuracy trade-off.

## Strengths

- **Provable robustness certificate for PQC parameter noise (Theorem 3.1):** The paper derives a concrete, mathematically precise bound—any perturbation δ satisfying ‖δ ⊘ σ‖₂ < ½(Φ⁻¹(p_A) − Φ⁻¹(p_B)) leaves the smoothed classifier's prediction unchanged. Prior quantum certified robustness work (Weber et al., 2021; Du et al., 2021; Huang et al., 2023) focuses on input perturbations or measurement noise; this paper targets parameter gate noise, which is a distinct and practically relevant error source for NISQ hardware with continuously-parameterized gates.

- **Non-uniform σ per parameter (Definition 3.3, diagonal covariance Σ):** Unlike standard randomized smoothing with a single scalar σ, the method assigns an independent σᵢ per parameter. The semi-axis standard deviation analysis (Section 4.2) confirms that different parameters exhibit markedly different noise sensitivities in the cluster phase task, validating the advantage of per-parameter radii over a uniform robust radius.

- **Dimensionality-aware robustness metric (Section 4):** The paper reformulates the certificate as a hyper-ellipsoid equation (∑ δᵢ²/(s_e σᵢ)² < 1) and proposes the certified area geometric mean V^(1/D) as a metric. This provides an interpretable, dimension-normalized way to compare robustness across circuits with different numbers of parameters, going beyond raw accuracy or a single scalar radius.

- **Empirical demonstration on two tasks with different robustness-variance structure:** The method is tested on cluster phase classification (12 qubits) and SPT state preparation classification (8 qubits), with the latter certifying noise in both the state-preparation and classification circuits. The paper honestly documents that the robustness-variance correlation differs between tasks (strong in cluster phase, weaker in SPT), and discusses possible explanations rather than over-claiming.

## Weaknesses

### Fatal

None.

### Major

1. **No baselines, comparisons, or controls in any experiment.** The paper reports only absolute robustness numbers for its proposed method (certified area geometric mean 0.002–0.018, semi-axis average 0.005–0.045). There is no comparison against: (a) standard (non-robust) PQC training evaluated under the same parameter noise, (b) existing quantum certified robustness methods (Weber et al. 2021; Du et al. 2021; Huang et al. 2023, all cited in the paper), or (c) a trivial baseline. Without knowing what accuracy and noise tolerance standard training achieves, the reader cannot assess whether the method provides any practical benefit over the status quo. For a paper whose title promises "provably noise-resilient training," the evidence that the method actually *improves* resilience over existing practice is absent. This is verifiable from Sections 5.2 and 5.3, which contain no comparative baselines.

2. **The theoretical contribution is applying an existing classical technique to a new variable, not new theory.** Theorem 3.1 is the standard L₂ randomized smoothing certificate from Cohen et al. (2019) / Tecot & Hsieh (2021), applied to PQC parameters rather than classifier inputs. The bound ‖δ ⊘ σ‖₂ < ½(Φ⁻¹(p_A) − Φ⁻¹(p_B)) is exactly the standard formula. The paper correctly cites Tecot & Hsieh (2021) for this, but then presents the adaptation as a core theoretical contribution ("provably guaranteed framework and theory," lines 16–17). The paper does not identify or overcome any quantum-specific technical obstacle—no discussion of how finite-shot measurement statistics, the structure of unitary evolution, or measurement collapse interacts with the certificate in a way that requires new theoretical development. This limits the paper's novelty well below what the framing suggests.

### Minor

1. **The "connection to Evolutionary Strategies" is a useful observation but oversold as an algorithmic insight.** The paper notes that ES samples from a Gaussian N(0, Σ) (its search distribution) and that the smoothed classifier also requires Gaussian sampling, concluding "if we simply change the objective function O to calculate the margin of prediction instead, we can exactly optimize for the right-hand side of Theorem 3.1 using ES" (line 100–106). This is correct but the connection amounts to "both involve Gaussian sampling." The objective the method optimizes (½(Φ⁻¹(p_A) − Φ⁻¹(p_B))) requires estimating class probabilities across many Gaussian samples, which is a fundamentally different computation from the standard ES loss (e.g., prediction error). Any optimizer compatible with gradient estimation via Gaussian sampling—including standard gradient-based optimizers for the same objective—would work. The paper frames this as a "natural connection" and a key contribution (lines 15–18), but does not explain why ES is specifically necessary or uniquely suited.

2. **The abstract and introduction overclaim without qualification.** The abstract states "provably noise-resilient training theory" and "guarantees resilience to parameter noise" without clarifying that: (a) the guarantee is statistical (based on concentration inequalities for the smoothed classifier, not a deterministic bound on the original PQC), and (b) it applies to the smoothed classifier G_σ, not the base PQC C. This is standard for randomized smoothing, but the wording invites misinterpretation as a stronger, deterministic guarantee.

3. **The paper does not quantify the computational overhead of the smoothed classifier relative to standard PQC inference.** Line 85 claims "our smoothed PQC classifier operates in practice similarly to a standard PQC classifier in both method and computational cost," arguing that standard PQCs already require multiple measurements. However, the smoothed classifier needs *many* circuit executions—one per Gaussian noise sample—to estimate p_A and p_B with sufficient confidence for certification. This cost multiplier (potentially 10³–10⁵×, depending on desired confidence) is not quantified anywhere, making it impossible for practitioners to assess the trade-off.

### Trivial

None.

## Nice-to-Haves

- The two described regularization methods (Section 3.3, deferred to Section B.2) could be briefly named or contrasted in the main text.
- Adding a proof sketch of Theorem 3.1 in the main body (even one paragraph) would help readers understand why the standard certificate transfers validly to quantum measurement statistics.
- A table summarizing train/test sizes, number of parameters, and number of Gaussian samples used would improve reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not explain why parameter noise requires a different technique than input noise":** Removed. The paper clearly states this differentiator as "instrumentation error in devices" versus "adversarial attacks on inputs or mid-circuit noise" (lines 15–17, Section 2 last paragraph). The mathematical technique (randomized smoothing) is the same, but the *problem setting* is different and the paper explicitly motivates this distinction.
- **"Most hyperparameters worked well is unverifiable":** Removed. The paper defers to Section B.1 for details; the appendix is stripped by the parser. This is a parser artifact, not an author error.
- **"No proof of Theorem 3.1 in main text":** Removed. Deferring proofs to an appendix is standard practice at this venue.
- **"Dataset size too small (50/50 samples)":** Removed as a standalone weakness. Dataset size is explicitly stated and the tasks involve expensive Hamiltonian diagonalization for ground-state generation. The real issue is the absence of baselines (covered above), not the absolute dataset size.
- **"No real hardware experiments":** Removed. Acknowledged in the limitations section (line 234). The paper does not claim hardware experiments; simulation is standard for this stage of quantum ML research.
- **Strength about "exact structural alignment" being a genuine algorithmic insight:** Demoted from strength to minor weakness #1. The connection is real but significantly less substantive than claimed; the strength finder overstates this.
- **Strength about "empirical demonstration on two distinct tasks":** Weakened by the verified major weakness about missing baselines. The demonstrations exist but their evidentiary value is limited without controls.

## Novel Insights

The most interesting observation to emerge across the reviews—and one that cuts somewhat against the paper's framing—is that the paper reveals, perhaps inadvertently, that the main intellectual hurdle in this space is not mathematical (the randomized smoothing certificate transfers nearly verbatim) but rather practical and empirical: can the smoothed classifier be trained to achieve meaningful robustness without catastrophic accuracy loss? The paper's own results show certified radii so small (0.005–0.045 per parameter in σ-units) that their practical significance is unclear even before considering the missing baselines. This suggests the field may need fundamentally new training procedures, not just certificate transfers, to make parameter-noise robustness viable for NISQ hardware.

## Suggestions

1. **Add at least one baseline comparison.** The single most impactful improvement is to train a standard (non-smoothed) PQC on the same tasks and measure its accuracy degradation under parameter perturbations of the same magnitude. This directly tests whether the method improves over the status quo.
2. **Compare against existing quantum robustness methods** (e.g., Weber et al. 2021's approach). Even if the noise models differ, such a comparison would clarify the practical advantages or disadvantages of the parameter-noise framing.
3. **Quantify the computational overhead** (number of circuit executions needed for certification vs. standard inference) so practitioners can assess the practical trade-off.
4. **Qualify the abstract's language** to clarify that the guarantee is statistical and applies to the smoothed classifier, not the original PQC.

## Score and Decision

**MY FINAL SCORE:** <score>4.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>