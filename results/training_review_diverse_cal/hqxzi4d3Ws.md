I now have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper applies randomized smoothing — a classical certified robustness technique — to certify parameterized quantum circuit (PQC) classifiers against **parameter noise** (perturbations to gate parameters, rather than input noise or decoherence). The smoothed classifier averages predictions over Gaussian-perturbed parameters, and a Neyman–Pearson bound guarantees unchanged predictions for any perturbation within an ellipsoidal region. The paper draws a connection to Evolutionary Strategies (ES) as a training mechanism and adds variance regularization to handle the accuracy–robustness trade-off. Experiments on two phase-classification tasks (cluster phase and SPT state preparation) demonstrate trade-off curves.

## Strengths

- **Novel application domain for randomized smoothing**: While quantum randomized smoothing exists for input noise and measurement noise (Du et al., 2021; Weber et al., 2021), this paper is the first to systematically apply it to parameter/gate noise — a practically relevant noise source in NISQ devices where continuously parameterized gates suffer instrumentation error. This domain shift is non-trivial because it requires certifying the classifier parameters themselves rather than the data inputs.

- **Practical training connection via Evolutionary Strategies**: The observation that the randomized-smoothing training objective (maximizing the robustness bound) can be naturally integrated into the ES framework — an optimizer already used in the VQA community for its gradient-free nature — is a practically useful insight. The ability to jointly optimize circuit parameters θ and per-parameter noise tolerances σ within a single ES loop is a clean formulation that could lower the barrier to adoption.

- **Well-designed evaluation metrics**: The certified area geometric mean, semi-axis average, and semi-axis standard deviation (Section 4) provide interpretable, dimension-normalized quantities for comparing robustness across experiments. The semi-axis standard deviation is particularly insightful, revealing how uniformly or non-uniformly different parameters tolerate noise.

- **Explicit treatment of the accuracy–robustness trade-off**: Variance regularization (Section 3.3) with hyperparameter sweeps generates meaningful trade-off frontiers, and the different robustness–variance correlations observed across the two tasks (strong in cluster phase, weak in SPT) provide empirical insight that goes beyond a single-number evaluation.

- **Flexibility to certify both classifier and state-preparation circuits**: The SPT experiment (Section 5.3) certifies parameters in both the state-preparation circuit and the QCNN classifier, demonstrating composability.

## Weaknesses

### Major

- **The training objective is mathematically ill-posed as written (Section 3.2).** The paper defines the ES objective as  
  `argmax_{θ,σ} E_{ε~N(0,Σ)} O(θ+ε,x,y)` with  
  `O(θ+ε,x,y) = 1/2 (Φ^{-1}(p_A) - Φ^{-1}(p_B))`.  
  Here, `p_A` and `p_B` are distributional quantities — they are probabilities over the entire Gaussian measure, not functions of a single realized ε. Consequently, `O` does not vary with ε for fixed (θ,σ,x,y), making the expectation vacuous and the ES gradient estimation procedure (which relies on evaluating the objective at sampled θ+ε) undefined. The textual description ("calculate the margin of prediction instead") suggests a different, sensible procedure, but the mathematics does not match. The paper claims this enables "exact" optimization of the bound, but no concrete algorithm is given for how `p_A`, `p_B` would be estimated from finite samples or integrated into the ES loop. **This is the most serious weakness**: a reader cannot determine what was actually optimized in the experiments, and the claimed "natural connection to ES" is not substantiated.

- **No experimental baselines or comparisons.** All reported results show trade-off curves for the proposed method alone. There is no comparison to (a) a standard PQC classifier trained without robustness considerations, (b) training with simple additive Gaussian noise on parameters (which the smoothed classifier already approximates), or (c) prior quantum certified robustness methods. The authors report certified radii as small as 0.005–0.045 semi-axis average and say these "could be sufficient for certain systems," but without baselines or calibration against known gate error rates, a reader cannot assess whether the method provides meaningful practical robustness or merely confirms that small perturbations do not change predictions.

### Minor

- **Limited theoretical novelty.** Theorem 3.1 is a direct application of the Cohen et al. (2019) randomized smoothing bound (via Tecot & Hsieh's per-coordinate variant) to the parameter space of PQCs. No quantum-specific analysis is provided — e.g., the fact that measurement outcomes are already probabilistic is not exploited in any new way. The paper's novelty lies in the application domain and training procedure, not in new certification theory.

- **The training algorithm is underspecified.** There is no pseudocode or explicit description of how `p_A` and `p_B` are estimated from finite noise samples, how many samples are used per gradient step, or how the ES update rule handles the bound objective. Table 1 (presented as an image) may contain this information, but the main text lacks even a sketch sufficient for reproducibility.

- **The SPT experiment's training details are ambiguous.** The paper certifies parameters in both the state-preparation circuit and the QCNN, but it is unclear whether the state-preparation parameters are also trained via the same ES procedure or are fixed during certification.

### Trivial

- **Definition 3.2 imprecision.** The definition says a PQC is noise-resilient if predictions are unchanged "for any noisy perturbation δ from a certain distribution," while Theorem 3.1 certifies for **any** δ within a deterministic ℓ₂ bound. The "from a distribution" language is at odds with the certified guarantee.

## Nice-to-Haves

- Relating the certified radii to known gate error rates in existing NISQ devices (e.g., typical phase errors of 10⁻²–10⁻³ rad) would help readers judge practical significance.
- An ablation showing the effect of variance regularization strength on the trade-off would strengthen the empirical analysis.
- Comparing to simple noise injection during training (without certification) would disentangle the benefit of the smoothed classifier from the benefit of the ES-based training.

## Removed Points

These points from the reviewer inputs are flagged for removal; treat with caution:

1. **"Proof of Theorem 3.1 is in the appendix" / "Missing appendix"**: The proof being in the appendix is standard and the appendix exists in the original submission (parser-stripped). Removed per "REMOVE weaknesses about missing appendix."
2. **"Generalizability is asserted, not demonstrated"**: This is a generic criticism applicable to nearly every paper; removed as it does not specifically identify a flaw in the paper's argument.
3. **Strength Finder's strength about "Exact compatibility with ES"**: This claimed strength directly conflicts with the verified weakness about the incoherent training objective formulation. Per the rule that weaknesses beat strengths, this is moved here.
4. **Any formatting/typo criticisms**: Removed per hard rules about parser artifacts.
5. **Missing related works**: Removed per hard rule — I cannot verify the existence of missing references.
6. **"The paper does not use methods the reviewer prefers"**: Removed per rule about reviewer taste versus genuine weaknesses.

## Novel Insights

The most interesting observation from this review process is that the paper's **claimed training methodology is fundamentally mis-specified at the mathematical level** — the objective function cannot be evaluated as written — yet the experimental results still appear to show reasonable trade-off curves. This suggests the actual implementation uses a different, well-defined objective (likely a per-sample margin or a finite-sample estimate of the bound), and the disconnect is purely in the paper's mathematical exposition. However, the fact that this gap was not caught before submission is concerning. The paper would benefit enormously from a precise, step-by-step algorithmic description that clarifies what is actually being optimized.

## Suggestions

1. **Fix the training objective formulation.** Replace the ill-defined `O(θ+ε,x,y) = 1/2(Φ^{-1}(p_A)-Φ^{-1}(p_B))` with a concrete, implementable procedure. For example: for each data point (x,y), draw K noise samples ε_k, evaluate the per-sample classifier margin `m_k = C(θ+ε_k,x)_{(1)} - C(θ+ε_k,x)_{(2)}`, and define the objective as the average margin. Or: estimate p_A,p_B from K samples and define the objective as the finite-sample bound estimate. The key is that the objective must be a function of the sampled ε.
2. **Add at least one baseline.** A standard (non-smoothed) PQC trained on the same tasks, evaluated under the same parameter noise, would immediately contextualize the robustness gains.
3. **Provide a concrete algorithm** (pseudocode) showing the complete training loop: how many noise samples per gradient step, how `p_A`/`p_B` are estimated or approximated, how the ES update rule operates on the objective.
4. **Clarify novelty relative to Tecot & Hsieh (2021).** The paper already cites this work as the per-coordinate randomized smoothing basis — explicitly stating what is new beyond applying that framework to PQC parameters.
5. **Calibrate the certified radii** by relating them to realistic gate error rates in existing devices (e.g., Bluvstein et al., 2022; 2024).

## Score and Decision

The core idea — certifying parameter noise in PQCs via randomized smoothing with ES training — has genuine potential for the NISQ community. However, the paper contains a **major unresolved weakness**: the training objective as mathematically defined is incoherent (the expectation does not depend on the sampled variable), so the claimed training methodology cannot be evaluated or replicated from the description. Combined with the lack of baselines, which makes it impossible to assess the method's practical value, the paper is not ready for acceptance in its current form.

**Overall assessment:** The paper's core claim of a "provably noise-resilient training theory and algorithm" is only partially supported — the certification theorem is sound, but the training algorithm is not properly defined, and the experiments lack comparative context. Substantial revision is needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>