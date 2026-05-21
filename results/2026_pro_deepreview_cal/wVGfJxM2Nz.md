Now I have all the calibration data I need. Let me synthesize the final review.

**Bracket assessment:**
- Round 1 bracketing: The paper sits between the middle band (~4.67–6.60). The low-band papers (2.5–3.4) had severe gaps this paper doesn't have. The high-band papers (8.0) have more comprehensive experiments and stronger theoretical contributions than this paper.
- Round 2 narrowing: AZGIwqCyYY (5.75, Accept) is the closest topically — a Hamiltonian dynamics paper with incomplete generalization evaluation. The current paper is similar in quality but slightly weaker on novelty and OOD evaluation thoroughness. XqDM97DtMf (4.67, Reject) has deeper experimental and theoretical problems. The paper lands between them.

**Final score: 5.5, Accept (borderline).**

The paper makes a solid contribution — the systematic SHNN vs LSTM comparison on FPUT is genuinely well-done and informative. But the OOD generalization claims need qualification, and the dissipative baselines lack detail. The paper is worth accepting but the authors should address the OOD evaluation gap.

Now let me write the review.## Summary

This paper presents a comparative study arguing that embedding geometric inductive biases into machine learning models of dynamical systems enables robust generalization with much smaller models. Two use cases are examined: (1) Riemannian optimization of a linear state-space model constrained to the symmetric positive definite (SPD) manifold for a dissipative heat-transfer system, and (2) symplectic Hamiltonian neural networks (SHNNs) for the conservative Fermi–Pasta–Ulam–Tsingou (FPUT) chain. The strongest result is the conservative case, where a systematic sweep over model sizes shows that a compact SHNN (1,441 parameters) achieves rollout MSE and energy drift orders of magnitude better than an LSTM with 97,074 parameters, with the energy drift vividly visualized on the Hamiltonian energy surface.

## Strengths

- **Compelling model-size sweep on FPUT**: Table 2 and Figure 3 present a rare, systematic comparison across SHNN, NeuralODE, and LSTM with 16 architecture configurations each. A 1,441-parameter SHNN achieves test rollout MSE orders of magnitude below the best LSTM (97,074 parameters) while keeping energy drift RMS near 10⁻³ vs. 5.9 for the LSTM. This directly substantiates the claim that geometric inductive biases dramatically reduce the model size needed for robust long-horizon prediction.

- **Visual diagnosis of energy drift as a failure mode**: Figure 4a–c projects the FPUT trajectory onto 2D slices of the Hamiltonian and overlays the true energy level set. The SHNN stays confined to the correct level while the LSTM visibly drifts across level sets, providing a clear geometric explanation for the quantitative degradation in rollout and energy drift. This is an effective pedagogical tool for the argument.

- **SPD manifold constraint demonstrates clear benefit for dissipative system identification**: Table 1 shows that Riemannian optimization on the SPD manifold (RieOpt) yields test MSE of 0.40/1.36 (London/Chicago) vs. 1.28/3.35 for Euclidean optimization (EucOpt) on the same LSSM formulation, and catastrophic errors for RF, XGBoost, and LSTM on the OOD Chicago climate. The RieOpt vs. EucOpt comparison cleanly isolates the value of the manifold constraint within the same model class.

- **Unified treatment across physical regimes**: The paper connects dissipative (SPD manifold) and conservative (symplectic manifold) dynamics under a single geometric thesis, and provides concrete algorithmic recipes (Riemannian Adam via `geoopt`, symplectic integration via implicit midpoint) that are reproducible.

## Weaknesses

### Fatal
None.

### Major

- **Conservative OOD generalization is supported only by a single qualitative visualization**: The paper's central claim is that structure-preserving models generalize robustly across operating conditions. For the conservative FPUT system, this claim rests on Figure 4b,c — a single perturbed initial condition shown qualitatively for SHNN and LSTM. No quantitative metrics (rollout MSE, energy drift RMS) are reported across a set of out-of-distribution initial conditions. The test-set evaluation (Table 2, Figure 3) measures interpolation along the same dynamical regime (chronological continuation of the training trajectory), not generalization to new regimes. Since a single trajectory can be cherry-picked, this is a significant evidential gap for a claim the paper treats as central.

### Minor

- **"Volumes of data" claim is untested**: The introduction (line 17) states that structure-preserving biases "reduce reliance on large models and volumes of data," but the experiments vary only model size, not dataset size. The claim about data volume should be removed or explicitly tested.

- **Dissipative baseline configurations are not described**: No details are given on how RF, XGBoost, and LSTM were configured for the heat-transfer task (input features, lag order, autoregressive training protocol, hyperparameter selection). This makes the comparison difficult to reproduce or independently assess, though the main RieOpt vs. EucOpt comparison is well-specified.

- **Dissipative comparison partially conflates geometric structure with stability**: The structure-naive baselines (RF, XGBoost, LSTM) lack any built-in stability mechanism, making their failure on OOD autoregressive rollout unsurprising. The EucOpt baseline partially addresses this (same LSSM formulation, no SPD constraint, worse but still stable), but a stability-constrained non-geometric baseline (e.g., spectral normalization) would more cleanly isolate the specific value of the SPD manifold geometry. The current comparison demonstrates that stability helps, but not uniquely that the geometric encoding is necessary.

### Trivial

- The abstract could more precisely reflect what was varied (model size) rather than implying data-volume results that were not tested.
- The phrase "identify ... using a linear state-space formulation ... via Riemannian optimization" in the abstract slightly overstates novelty — Riemannian optimization for SPD matrices is an established tool; the contribution is the comparative study.

## Nice-to-Haves

- A comparison of SHNN with a standard HNN (without symplectic integration) would help separate the benefit of the symplectic integrator from the Hamiltonian parameterization.
- A discussion of limitations: both systems are low-dimensional and synthetic; the known Hamiltonian/SPD structure is exploited; the methods require a priori knowledge of the geometric form that may not be available in practice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Riemannian optimization for SPD matrices is a known tool"** (from Harsh Critic Section-by-Section Notes on abstract): This is a scope criticism. The paper does not claim to invent Riemannian optimization; it applies it to system identification and conducts a comparative study. The contribution framing is reasonable.
- **"Missing justification for optimisation choices"** (Harsh Critic Missing Parts): The paper describes the loss function (Eq. 7), the optimizer (RAdam), the geodesic update (Eq. 9), and the learning rate. While more detail would be nice, the core recipe is provided and this does not rise to the level of a weakness.
- **"Ablation on HNN vs. SHNN"** (Harsh Critic): The harsh critic themselves notes this is "not a requirement." Kept as nice-to-have only.
- **Strength Finder generic strengths about "important problem"**: These are not concrete and have been removed.
- **"Reproducibility concerns" as a fatal-level claim**: The harsh critic framed missing baseline details as a methodological gap; I've kept it as Minor since the core RieOpt/EucOpt comparison is well-described and the baseline gap is about fairness assessment, not inability to assess the main result.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add quantitative OOD evaluation for the conservative FPUT system: rollout MSE and energy drift RMS across a set of perturbed initial conditions, with error bars over multiple seeds.
- Either add a stability-constrained non-geometric baseline for the dissipative case (e.g., spectral normalization on the state transition matrix) or explicitly frame the current comparison as demonstrating the benefit of built-in stability, acknowledging that the SPD manifold is one effective way to achieve it.
- Remove or qualify the "volumes of data" claim unless explicitly tested.

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| XqDM97DtMf (Chaotic Dynamics) | 4.67 | R1 | This paper is stronger: XqDM97DtMf had severe theoretical concerns, weaker experiments, and missing quantitative OOD metrics across the board. |
| 2AWZTv6kgV (PNDE) | 4.75 | R1 | This paper is stronger: PNDE had significant novelty concerns and comparable experimental gaps, but lacked the well-executed model-size sweep that anchors this paper. |
| AZGIwqCyYY (Hamiltonian Meta-Learning) | 5.75 | R2 | This paper is slightly weaker: AZGIwqCyYY has similar generalization-evaluation gaps but stronger novelty (cross-domain meta-learning). This paper's model-size sweep is more thorough, but its generalization claims are less well-supported. |
| U1DjXQeJRx (PoDiNNs) | 6.60 | R1 | This paper is weaker: PoDiNNs has stronger theoretical contribution and more convincing experiments across diverse systems. |
| fU8H4lzkIm (PhyMPGN) | 8.00 | R1 | This paper is significantly weaker: PhyMPGN has comprehensive experiments, strong generalization results, and clear SOTA performance. |

**Round 1 bracket:** 4.5–6.5, based on comparison with XqDM97DtMf (4.67) below and U1DjXQeJRx (6.60) above.

**Round 2 narrowing:** The paper is most comparable to AZGIwqCyYY (5.75). Both papers have a solid core contribution with generalization claims that are not fully supported by the experimental evidence. This paper's model-size sweep is more systematic, but AZGIwqCyYY's cross-domain ambition gives it a slight edge in novelty. The conservative OOD evaluation in this paper being purely qualitative is a real limitation. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>