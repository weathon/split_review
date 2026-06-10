Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Adaptive Proposal Sampling (APS) and its variant a-GPS, an MH-free adaptive Gaussian proposal sampler for Bayesian neural networks. The method iteratively updates the mean and variance of a Gaussian proposal to match the local score function of the posterior, claiming this obviates the need for a Metropolis-Hastings correction. Experiments on simulated data, CIFAR10/100, and ImageNet show competitive accuracy and calibration compared to SWA, SWAG, Laplace approximation, and SGD-MC.

## Strengths

- **Strong simulated unimodal performance (Table 1, Figure 2)**: On a 1D Gaussian target, a-GPS achieves an ESS of 954 (vs NUTS's 364 and MALA's 74.9) in 0.4 seconds versus 4.6s for NUTS — an order-of-magnitude speedup. This is a concrete demonstration that the adaptive proposal can be highly efficient when its Gaussian assumption matches the target.

- **OOD detection advantage on CIFAR50-50 (Table 6)**: With WideResNet28-10 on a challenging OOD split, a-GPS correctly shows higher predictive entropy for out-of-distribution data than in-distribution data, while SGD-MC and Laplace approximation show the reverse (undesirable) pattern. This provides a specific practical scenario where a-GPS outperforms established methods on uncertainty quantification.

- **Creatively designed multi-modality diagnostic (Tables 2–4, Section 3.2.1)**: The λ-SWAG test — fitting a Gaussian to a-GPS samples and comparing predictive metrics — is an inventive self-diagnostic for detecting whether the sampler has visited multiple basins. The observed discrepancy between a-GPS-4 and 4-SWAG on CIFAR10/CIFAR100 (vs identity between a-GPS-7 and 7-SWAG) provides indirect but genuine evidence of multi-mode exploration.

## Weaknesses

### Fatal
None.

### Major

- **Central theoretical claim is unsubstantiated: no proof that the MH-free sampler converges to the posterior (lines 112–142, Eq. 3–7)**: The paper claims a-GPS is "self-adjusting towards a perfect sampler" that "obviat[es] the need for an MH correction" (Section 1.2). The justification in Section 2.1.1 proceeds: *if* the proposal q matches the mode f_i, then the mode-specific MH acceptance α_i → 1, so MH can be dropped. But the paper never proves that the update equations (3) and (7) — which match the score and a secant-approximated Hessian at a *single point* θ_t — cause q to converge to the target distribution. Matching the gradient at one point does not imply distributional convergence. Without a stationary-distribution analysis, detailed balance, or any convergence guarantee, the claim that a-GPS produces samples from the posterior is an assertion, not a demonstrated property. This is the paper's central methodological contribution, and the evidence does not support it.

- **No validation that deep learning samples actually follow the posterior (Section 3.2)**: The deep learning experiments evaluate predictive accuracy, NLL, and ECE — these are measures of predictive performance, not posterior fidelity. The method could be generating slightly perturbed warm-start weights that happen to improve calibration without any actual posterior sampling. No gold-standard posterior comparison (e.g., full-batch HMC on a small network) is provided to validate the sampling claim. For a paper whose core framing is about being an exact sampler, this evidential gap is critical.

- **Stochastic gradient bias is unaddressed (line 142)**: The paper writes "since stochastic gradients are sufficient" and cites Izmailov et al. (2021) for the claim that "differences between true gradient and stochastic gradient MCMC in deep learning are negligible." However, Izmailov et al. studied HMC *with an MH correction* — the MH step is what controls the bias from stochastic gradients. Here, without any MH correction, the bias from noisy mini-batch gradients propagates directly into every mean and variance update (Eq. 3, 7). The variance update in particular divides by ∇log f(θ_t), which with stochastic gradients can be near zero, causing σ² to explode — a concrete instability that the λ cap only patches without analysis. The paper provides no analysis of how stochastic gradient noise affects the stationary distribution of a-GPS.

- **Variance update is a noisy secant approximation with no error analysis (Eq. 7, lines 80–96)**: Equation (7) approximates the Hessian via a secant between two points (θ_t and μ_t): σ²_{t+1} = |(θ_t − μ_t) / ∇log f(θ_t)|. In a deep network with millions of parameters, estimating the curvature along each dimension from two points through a noisy gradient is extremely unreliable. The diagonal covariance assumption (line 98) compounds this, since neural network parameters are strongly coupled. The λ cap is acknowledged as a patch (line 100) but receives no analysis of how it truncates posterior tails, interacts with sampling quality, or should be chosen — yet λ is the main hyperparameter controlling exploration.

### Minor

- **Inference time numbers are confusing or contradictory (lines 222–223)**: The paper states "The time of SWA is comparable to a-GPS, even though SWA only does one forward pass, and a-GPS does 45. While SWAG only does 30 forward passes, a-GPS is still 25–30x faster." If a-GPS does 45 forward passes during inference (bottom section of the table) and SWA does 1, comparable total inference time implies each a-GPS forward pass is ~45× cheaper — which is unexplained for the same architecture. This needs clarification; as written, it undercuts a headline efficiency claim.

- **Multi-modality evidence from the λ-SWAG test is indirect and has an alternative explanation (Section 3.2.1)**: The paper interprets a discrepancy between a-GPS-λ and λ-SWAG as evidence of multi-mode exploration. However, the discrepancy could also arise from non-Gaussian structure within a single mode or from the variance cap λ truncating samples. The paper does not rule out these alternatives, and no explicit mode-hopping mechanism is described — the method simply draws from a Gaussian whose mean and variance are locally updated, which does local exploration around the warm-start.

- **No limitations section**: For a paper making strong claims about being "a step towards having both exactness and effectiveness" and a "perfect sampler," the absence of any discussion of when the method fails, its theoretical limitations, or the conditions under which the MH-free design is valid is a significant omission, especially for a top-tier venue.

### Trivial
None.

## Nice-to-Haves

- A comparison against a gold-standard posterior (e.g., full-batch HMC on a small CNN) to validate that a-GPS samples actually match the posterior distribution, not just improve calibration.
- Analysis of the variance cap λ: How should it be chosen? How does it interact with posterior tails and the number of samples?
- Wall-clock training/sampling time comparisons for the deep learning experiments (the paper provides inference time but not training time).
- A formal convergence analysis or at minimum a clear statement about what theoretical properties the method does and does not satisfy.

## Removed Points

These points from the inputs were removed with brief justification:

1. **"The justification for dropping the MH correction is circular"** (Harsh Critic #1) — Downgraded from "structural/fatal" framing. The paper's logic is conditional ("if q matches f then α→1, so MH is unnecessary") rather than circular. The real problem is that the premise (q converges to f) is unproven. This is captured in Major weakness #1 above, stated accurately as an unsubstantiated claim.

2. **"Equivocation on the score function"** (Harsh Critic #2, first part about ∇log f̄ being undefined) — The paper *does* define ∇log f̄(θ_t) on line 62: "the derivative of log f(θ_t) with respect to θ_t." The bar over f may be a notation quirk, but it is defined. The substantive issue about stochastic gradients is retained in Major weakness #3.

3. **"Unimodal experiment is best-case scenario, not surprising"** and **"mixture experiment ESS comparison is uninterpretable"** (Harsh Critic, Section 3.2 notes) — These are accurate observations but they do not rise to the level of weaknesses; they describe standard experimental design limitations that the paper itself partially acknowledges (the paper notes ESS "assumes unimodality"). The paper's simulated experiments are limited, but this is already covered by Major weakness #2 (no posterior validation).

4. **"The paper does not adequately distinguish between the proposal being Gaussian and the target being multimodal"** (Harsh Critic, Section 1.1 notes) — This is a subtlety but not a concrete weakness; the paper does distinguish these concepts (it explicitly says the proposal is Gaussian and targets can be multi-modal).

5. **Strength about "model-agnostic" (Strength Finder #3 aesthetic strength)** — This is generic and applies to many methods; it is not a specific evidence-backed strength.

6. **Strength about "single-epoch ImageNet results" (Strength Finder #4)** — This is partially valid but conflates training with inference, and the one-epoch result may simply reflect insufficient exploration. It's not a core strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the paper honestly: a-GPS is a practical heuristic for generating diverse weight perturbations from a warm-start that empirically improves calibration, **not** a theoretically justified sampler. Remove the "perfect sampler" language and claims about "obviating the need for an MH correction" without proof, or provide the proof.

2. Clarify the inference time reporting: explain how 45 forward passes can have comparable total time to 1 forward pass of SWA.

3. Add a limitations section discussing when the method is expected to work or fail.

4. Provide an analysis of the variance cap λ — its effect on sampling quality, tail behavior, and how to set it.

5. Validate against a gold-standard posterior (e.g., full-batch HMC on a small network) on a tractable problem.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>