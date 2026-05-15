Now I have all the information needed. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write this carefully.

---

Here is my synthesized review:

## Summary

This paper proposes a Markov Proximal Learning (MPL) framework that unifies the NTK and NNGP theories as short-time and long-time limits of a single Langevin-type dynamics for infinitely wide neural networks. The authors derive a time-dependent Neural Dynamical Kernel (NDK), obtain integral equations for the mean predictor trajectory, and identify two distinct learning phases: a fast gradient-driven phase described by the NTK and a slow diffusive phase converging to the NNGP equilibrium. The framework yields predictions about early stopping and representational drift that are explored numerically on synthetic and benchmark datasets.

## Strengths

1. **Conceptual unification of NTK and NNGP via a single time-dependent kernel.** The paper shows that the NDK at initialization equals the NTK (Sec. 3, Eq. 4) and its long-time integral yields the NNGP kernel (Sec. 4.2, Eq. 11), providing the first explicit bridge between these two previously disparate frameworks. This is the paper's most significant contribution.

2. **Exact analytical expressions for the full learning trajectory in the infinite-width limit.** Equations 9–10 provide exact integral equations for the mean predictor during and after learning, derived from first principles using the path-integral formulation. This goes beyond both the linearized NTK dynamics and the static NNGP posterior by capturing the entire trajectory.

3. **Two-phase characterization with explicit time-scale separation.** The analysis identifies a fast gradient-driven phase (timescales ∼𝒪(1)) and a slow diffusive phase (timescales ∼𝒪(1/T)), and shows how hyperparameters (T, σ², σ₀², depth) control the crossover between them (Secs. 4.1–4.3, Fig. 1a–b). This provides a clean physical picture of learning in wide networks.

4. **Novel predictions about early stopping and representational drift.** Sec. 4.4 shows that optimal early stopping can occur during the diffusive phase depending on σ₀²/σ² and depth (Figs. 2–3)—a phenomenon not captured by either NTK or NNGP alone. Sec. 5 derives conditions under which performance persists after readout freezing, identifying norm-based drift-invariant features for ReLU networks (Fig. 5). These predictions are nontrivial and potentially impactful.

5. **Recursive closed-form expression for the NDK (Eq. 13).** The NDK can be computed layer-by-layer for arbitrary activation functions with closed-form kernels (ReLU, error function, linear), enabling efficient numerical evaluation for deep networks without sampling.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient empirical validation of the core claim on benchmark datasets.** The paper's central claim is that the MPL theory accurately predicts the learning dynamics of wide neural networks, but only **one** simulation comparison is presented (Fig. 1c, synthetic orthogonal data with random binary labels). All benchmark dataset results (Figs. 2–4, CIFAR-10 and MNIST) show only theoretical predictions from solving the integral equations, with no overlay of finite-width Langevin simulations. The paper states that further comparisons appear in the SI ("SI Sec. Additional-numerics"), but even so, the main text lacks any quantitative comparison on realistic tasks. This matters because the paper positions itself as providing "the first theoretical understanding of the complete trajectory" of gradient descent learning dynamics—but whether these integral equations actually govern the mean predictor in finite-width networks trained on real data is verified only on a synthetic dataset with special structure. Without systematic comparisons across widths and datasets, this core claim is not convincingly established.

2. **The representational drift analysis (Sec. 5) is presented without simulation verification.** The histograms in Fig. 5 appear to be theoretical (derived from the path-integral marginalization), but it is never explicitly stated whether they come from the theory or from finite-width network simulations. No comparison to actual network dynamics is provided. The quantitative accuracy claims (90 % accuracy for 0/1, chance for 4/9 after decorrelation) are thus predictions of the theory, not validated results. Since the drift scenario (freezing readout while hidden layers diffuse) involves a non-standard training protocol, empirical confirmation would significantly strengthen the contribution.

3. **The replica method derivation is used without discussion of its assumptions or domain of validity.** The moment generating function (Eqs. 4–7) is derived via replica averaging, yet the paper does not discuss conditions under which replica symmetry holds or when the replica calculation is expected to be valid for the non-convex neural network loss landscape. The paper cites prior uses of the replica method in NN theory (Gardner, Bahri, etc.), but given that the entire theoretical apparatus rests on this calculation, the lack of any caveat about its heuristic nature is a gap. This does not invalidate the paper—many statistical physics results in this area rely on the replica method—but it weakens the "exact analytical" framing of the results.

### Minor

1. **Limited contextualization against prior DMFT work.** The paper mentions DMFT in the Discussion and claims its framework is "more general than continuous time gradient dynamics" and "cannot be captured by DMFT," but it does not explicitly compare the NDK integral equations to the existing DMFT equations (e.g., Mignacco et al. 2020, Bordelon & Pehlevan 2022) or show how the DMFT results emerge as a special case. A brief comparison in the main text would clarify the novelty and scope more concretely.

2. **The phrase "exact analytical expression" overstates the form of the results.** The abstract and introduction describe the derivation as yielding "an exact analytical expression for the network input-output function," but what is actually obtained are integral equations (Eqs. 9–10) that must be solved numerically. The MGF and the path integral representation are exact within the model assumptions, but the mean predictor is not in closed form. This phrasing could mislead readers about what the theory provides.

3. **Fig. 5 does not specify whether the histograms come from theory or simulation.** The caption and text describe the dynamics of the predictor distributions but do not state the source. Given the central role of this figure for the representational drift claims, this ambiguity should be resolved.

### Trivial

1. The paper states the approximation K^{d,L}(t,t')≈K^{d,L}(0,0) is valid for "t∼𝒪(1)" at low T (Sec. 4.1). The precise condition t,t' ≪ T^{-1} could be stated more explicitly to aid clarity.

## Nice-to-Haves

- A side-by-side comparison of the NDK integral equations with the prior DMFT equations from Mignacco et al. (2020) or Bordelon & Pehlevan (2022) would sharpen the claimed advantages.
- A plot of the NDK itself (e.g., K^{d,L}(t,t') as a function of t−t' for different depths) would help readers develop intuition for how the kernel evolves from NTK-like to a form whose integral gives the NNGP kernel.
- The discrete-λ extension mentioned in the Discussion (finite step size, adaptive learning rates) would be a natural and valuable extension but is beyond the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"λ and β relationship to standard gradient descent learning rate is never clarified."** — The paper explicitly states (lines 151–157) that in the large λ limit the dynamics becomes continuous-time Langevin with time in units of λ, and states "Note that all times are in units of λ" (line 211). The relationship is adequately addressed; this criticism reflects a less careful reading.

2. **"NDK is a correlation of gradients w.r.t. prior statistics, not empirical gradients; this subtlety is not discussed."** — The paper explicitly defines the NDK with the average ⟨⋅⟩_{S₀} taken over the prior statistics (Eq. interp, line 224–225), and clearly states that at initialization it equals the NTK. The definition is transparent; no hidden subtlety.

3. **"Sec. 3 (NDK) derivation sketch missing; reader referred to SI."** — Paper refers to SI for the detailed proof, which is standard. Per the rules, missing derivations deferred to the (stripped) appendix should not be flagged as a weakness.

4. **"The paper should mention that the long-time equilibrium derivation assumes σ² non-zero."** — The paper explicitly uses σ² in the definition of the regularizer (Eq. cost) and throughout the derivation; the singular nature of the no-regularization limit is mathematically self-evident. Not a meaningful omission.

5. **Strength Finder's claim of "Comprehensive numerical validation across multiple datasets and architectures."** — This overstates the evidence. The only simulation comparison is on synthetic data (Fig. 1c); benchmark dataset results are theoretical predictions without simulation verification. The strength is rephrased above in a more measured way.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface the tension between the paper's ambitious theoretical claims and the limited scope of its empirical validation—a classic challenge for theory papers in ML—but do not generate new analytical observations beyond what the paper already provides.

## Suggestions

1. **Add simulation comparisons on at least one benchmark task.** The most impactful addition would be a comparison of the theoretical predictor trajectory (from solving Eqs. 9–10) to finite-width Langevin simulations for MNIST 0-vs-1 across a range of widths (e.g., N = 100, 500, 2000) plotted in Figs. 2–3. This would directly address the single biggest gap between the paper's claims and its evidence.

2. **Add simulation verification for the representational drift predictions.** Simulate the frozen-readout protocol for a finite-width network, measure test accuracy over time, and overlay the theoretical prediction. This would convert the drift analysis from a theoretical exercise into a verified result.

3. **Add a brief caveat about the replica method's assumptions** (or a citation to rigorous work establishing its validity in this setting). Even a sentence noting that the calculation assumes replica symmetry and the absence of ergodicity-breaking would improve intellectual honesty.

4. **Clarify in the abstract/introduction that the results are integral equations, not closed-form expressions.** Rephrase "exact analytical expression" to "exact integral equations" or "exact path-integral representation" to avoid overclaiming.

## Score and Decision

The paper makes a genuine and important contribution: the MPL framework and the NDK provide the first explicit unification of NTK and NNGP, and the two-phase characterization is physically insightful. The theoretical machinery is well-motivated and the derivations are presented clearly. However, the empirical support for the central claim—that this theory accurately describes actual network dynamics—is substantially weaker than claimed. Only one simulation comparison (on a synthetic dataset) is shown in the main text, and the representational drift predictions are not validated against simulations at all. These weaknesses are addressable but real. The paper's theoretical contribution is sufficient to merit publication, but the presentation overstates the degree of empirical confirmation.

**Score: 6.0** — A borderline accept. The theoretical unification is novel and significant; the weaknesses in empirical validation are significant enough to prevent a stronger endorsement but not to warrant rejection given the primarily theoretical nature of the contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>