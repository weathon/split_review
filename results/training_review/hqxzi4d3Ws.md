Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper applies classical randomized smoothing (Cohen et al., 2019; Tecot & Hsieh, 2021) to certify robustness against parameter gate noise in parameterized quantum circuit (PQC) classifiers. The guarantee ensures that perturbations δ satisfying ‖δ ⊙ σ⁻¹‖₂ < ½(Φ⁻¹(p_A)−Φ⁻¹(p_B)) do not change the smoothed classifier's prediction. The authors show a natural connection between this objective and Evolutionary Strategies (ES), enabling optimization of both θ and per-parameter σ. Experiments on cluster phase classification (12 qubits) and SPT state preparation classification (8 qubits) demonstrate the method's ability to achieve measurable certified robustness.

## Strengths

- **Practically relevant problem and clean application of randomized smoothing to PQC parameter noise**: Parameter gate noise is a real issue in NISQ devices, and the paper correctly identifies the opportunity to apply randomized smoothing in this setting. The connection between the robustness bound and the ES objective (Section 3.2) is conceptually elegant — by changing the objective to compute the margin ½(Φ⁻¹(p_A)−Φ⁻¹(p_B)), practitioners can optimize for certified robustness using a gradient-free optimizer already common in the VQA community.

- **Well-designed geometric evaluation metrics**: The paper reformulates the bound as a hyper-ellipsoid and defines interpretable, dimension-independent metrics (Certified Area Geometric Mean, Semi-Axis Average, Semi-Axis Standard Deviation) in Section 4. These metrics capture different aspects of robustness and enable comparison across tasks with different dimensionalities.

- **Demonstration on two distinct quantum tasks with qualitative insights**: The experiments on cluster phase classification (12 qubits) and SPT state preparation (8 qubits) show that the method achieves measurable certified robustness (e.g., certified area geometric mean up to ~0.018 and semi-axis average up to ~0.045). The different robustness-variance correlations observed across tasks — strong in cluster phase, weaker in SPT — provide potentially useful empirical observations about parameter sensitivity that could inform future work.

- **General and function-agnostic framework**: The method can be applied to any PQC classifier (Definition 3.1) and is transparently extensible to parameterized state preparation circuits (Section 5.3) and combinable with other error-mitigation methods.

## Weaknesses

### Fatal
None.

### Major

- **No baseline comparisons in any experiment**: Every experimental result (Figures 1, 2) shows only the proposed method's robustness–accuracy trade-off. There is no comparison against standard PQC training without smoothing, Gaussian noise augmentation (the standard way to obtain a good smoothed classifier), a uniform-σ version of the method, or existing quantum certified robustness approaches (e.g., SDP-based methods, other randomized smoothing variants). Without baselines, the reader cannot determine whether the method provides any benefit over trivial alternatives. This is the single most significant weakness — it undermines the paper's ability to demonstrate that its training procedure is valuable.

- **Overclaimed novelty in framing**: The central theoretical result (Theorem 3.1) is explicitly a direct application of classical randomized smoothing (Cohen et al., 2019; Tecot & Hsieh, 2021) to the PQC setting, as the paper itself acknowledges on line 61: "we develop randomized smoothing certified robustness theory (Tecot & Hsieh, 2021) under the setting of PQC classifier." However, the abstract and introduction frame this as "provably guaranteed learning theory with quantum circuits" and "provably noise-resilient training theory," which overstates what is new. The paper's contribution is in the *application and training framework*, not in a new theoretical result. The framing should be adjusted to accurately reflect this.

### Minor

- **Per-parameter σ advantage claimed but unsubstantiated**: The paper repeatedly claims that per-parameter σ provides more flexibility than a uniform robust radius (e.g., lines 85, 199). However, no ablation compares the proposed method to a version with a single scalar σ. The robustness–variance correlation plots show that learned σ values vary across parameters, but this does not demonstrate that per-parameter σ improves performance over uniform σ. This claim remains speculative without an ablation study.

- **Computational cost of training not discussed**: The training procedure requires estimating p_A and p_B via Monte Carlo sampling at each ES iteration, while σ itself is being updated. The paper does not specify how many noise samples are used, how many forward passes are required per iteration, or the total simulation wall-clock time. While implementation details may be in the missing appendix, the main text should at minimum give the reader a sense of the computational budget. Given the small scale of the experiments (8–12 qubits, 50 samples), this cost may be negligible, but the omission leaves the method's practicality unclear.

### Trivial

- Very small-scale experiments (8–12 qubits, 50 training samples). While acceptable for a proof of concept, the paper would benefit from discussing scaling behavior or limitations more concretely.
- The QCNN architecture is described only at a high level ("rotational and control X, Y, Z gates") with no parameter count or circuit depth specified, hindering reproduction.

## Nice-to-Haves

- An ablation comparing per-parameter σ with a uniform σ baseline would substantially strengthen the paper's claims about the value of per-parameter flexibility.
- A comparison with standard Gaussian noise augmentation (training on noisy parameters and then certifying) would establish whether the proposed ES-based training provides an advantage over simpler approaches.
- A discussion of computational cost (number of forward passes, wall-clock time, number of noise samples used for estimating p_A/p_B) would help the reader assess practicality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's claim that the method is "likely computationally intractable as described" and "the method cannot be assessed, reproduced, or trusted to work beyond trivial toy problems"**: This is overstated. The paper's experiments (8–12 qubits, 50 samples) are small but functional. The method was successfully run, demonstrating feasibility at this scale. The critic's concern about a "feedback loop" where "σ is being updated...creating a feedback loop that could bias the estimates" is not supported by evidence — this is a standard property of training randomized smoothed classifiers, and the paper acknowledges the accuracy-robustness trade-off (Section 3.3). The criticism reads as speculation about intractability rather than a verified flaw.

- **Harsh Critic's claim that the method is "irreproducible from the main text" due to missing appendix**: The appendix was stripped by the parser. The paper references Sections B.1–B.3 for implementation details, which exist in the original submission. This is a known parser artifact, not an author error.

- **Harsh Critic's claim that Theorem 3.1 "contains no new reasoning" and this is "structural" / "the paper's core contribution does not stand"**: While the theorem itself is an application of known results, the paper's core contribution is the *framework and training method* (applying randomized smoothing to PQCs + connecting to ES + per-parameter σ + geometric metrics). The theorem is a component, not the entirety of the contribution. The paper is transparent about the source. However, the *framing* overclaims (addressed above as a major weakness).

- **Strength Finder's claim that the theory "is stronger than heuristic robustness"**: This is not a conflict with any weakness but is generic phrasing. It is kept implicitly in the strengths above.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same issues (no baselines, overclaimed novelty) but diverge on severity. The most interesting observation from the reviews is the disconnect between how the paper frames its contribution ("provably guaranteed learning theory") and what it actually delivers (an application of existing theory to a new domain). This highlights a broader trend in interdisciplinary ML/physics papers where the novelty and difficulty lie in the *transfer* of ideas, not in new mathematical results — a framing challenge the authors should address.

## Suggestions

1. **Add baseline comparisons**: Compare against (a) standard PQC training without smoothing, (b) Gaussian noise augmentation during training, and (c) a uniform-σ version of the proposed method. This is essential to demonstrate the value of the approach.

2. **Adjust framing**: Replace "provably guaranteed learning theory with quantum circuits" with more precise language such as "applying randomized smoothing guarantees to PQC parameter noise through an ES-based training framework." Accurately describe what is new (the application domain, the connection to ES, the geometric metrics) versus what is existing (the randomized smoothing bound itself).

3. **Add ablation for per-parameter σ**: Directly compare the proposed method against a version that uses a single scalar σ to empirically validate the claimed advantage.

4. **Report training cost**: Specify the number of Monte Carlo samples used for estimating p_A/p_B, the number of ES iterations, and the total number of circuit evaluations required. This helps the reader assess practicality.

5. **Expand experiments**: Even a simple comparison against standard Gaussian augmentation on the same tasks would substantially strengthen the paper's conclusions.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>