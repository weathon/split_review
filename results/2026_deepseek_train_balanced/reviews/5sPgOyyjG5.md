Now I have thoroughly verified all the reviewer claims against the paper. Let me write the final consolidated review.

---

## Summary

The paper proposes the Feynman-Kac Operator Expectation Estimator (FKEE), a two-stage pipeline for estimating $\mathbb{E}_{X\sim P}[f(X)]$: first train a Neural SDE ("diffusion bridge model") whose terminal distribution matches $P$, then train a PINN to solve the Feynman-Kac PDE whose solution at the initial condition gives the desired expectation. The claimed contributions are linking sampling to high-dimensional PDEs, introducing a versatile diffusion bridge model, and expanding the scope of expectation estimators beyond LLN/ETMC.

## Strengths

- **Principled error decomposition.** The paper cleanly decomposes the encoding loss into discretization error and structural error via the Wasserstein-2 distance triangle inequality (Equation 2), providing a clear conceptual framework for the diffusion bridge model. This framing is more structured than typical ad-hoc neural SDE fitting.

- **Clear two-use-case formulation of the diffusion bridge model.** The paper explicitly distinguishes between matching terminal distributions (resampling/generation) and matching entire Markov chain trajectories (Equations 5–6, Algorithm 1), giving a reusable recipe beyond a single application.

- **Practical diagonal-diffusion computational shortcut identified.** The paper notes (lines 226–228) that when the diffusion coefficient $\sigma$ is diagonal (as in Langevin diffusion), the PDE loss reduces from a full Hessian to only second-order partials of diagonal elements, lowering PINN training overhead.

## Weaknesses

### Fatal

- **The experiments section contains zero quantitative results, making every empirical claim unverifiable.** Section 5 (lines 295–304) describes three experiments in purely qualitative prose with no tables, figures, numerical comparisons, error bars, runtimes, convergence curves, or variance measurements. The partition function experiment claims "comparable accuracy with only 2000 points" and "reducing computation time" without providing any accuracy numbers, computation times, or named baselines. The diffusion bridge evaluation and baseline experiments similarly describe outcomes that are not shown. The abstract states that the paper "demonstrate[s] the advantages…through various concrete experiments," but no concrete evidence is present in the submitted document. This is not a matter of needing more experiments — the paper provides no experiment at all to support its central claims. This alone is decisive for rejection.

### Major

- **Unsubstantiated claim about PINNs overcoming the curse of dimensionality.** The paper asserts (line 28) that PINNs "effectively overcome the curse of dimensionality" and (line 264) are "meshless PDE solvers that can address the curse of dimensionality," but provides no citation, analysis, or experimental support for this claim applied to the Feynman-Kac PDE. The literature shows that standard PINNs degrade severely beyond roughly $d=10$ without specialized architectures, which is precisely the regime the paper targets ($n=15$ Ising model). This core methodological premise is stated as fact without evidence, and the paper's brief acknowledgment (lines 259–264) that "Error analysis for this equation can be found in many works" does not address the known practical difficulties.

- **"Universality" of the diffusion bridge model is asserted without construction.** The paper claims (line 26) that the SDE in equation (1) "encompasses a broad class of SDEs that share identical transition densities with the Markov chains in the MCMC algorithm" and that this creates a "universal sampler." However, the paper only concretely connects to Langevin diffusion (which already has a well-known SDE formulation). How Metropolis-Hastings, Gibbs sampling, Hamiltonian Monte Carlo, slice sampling, or any discrete-state MCMC method maps to an SDE of the form $dX_t = b dt + \sigma dW_t$ is not established. The claimed universality is asserted without construction.

- **Theoretical contributions are largely standard or inherited without meaningful extension.** Theorem 31 is a standard Euler-Maruyama convergence bound in Wasserstein distance, traceable to classical SDE approximation theory. Theorem 37 states "The proof is based on [Bernton2017OnPE]. However, the key difference is that we introduced a loss function control term, which enhances the result" — without specifying what the control term is, how it modifies the proof, or what it enhances. Theorem 38 simply combines the previous two results. The paper advertises "theoretical properties of this universal diffusion bridge model" (abstract) but the actual theoretical content is either standard or borrowed from prior work with an unspecified modification.

### Minor

- **The claimed advantage of weaker assumptions on $f$ is misleading.** The paper contrasts (line 292) "f ∈ C^2" (required for the Feynman-Kac PDE to have a classical solution) with Lipschitz continuity (a *sufficient* condition for MCMC concentration inequalities). These are incomparable: $C^2$ is a *necessary* condition for the classical PDE solution to exist, while Lipschitz is a sufficient (not necessary) condition for finite-sample MCMC error bounds. The PINN approach introduces its own regularity requirements (non-convex optimization convergence, collocation coverage, spectral bias) that are not discussed. The framing suggests a clear advantage that dissolves on scrutiny.

- **No discussion of PINN training challenges.** The paper uses the standard PINN loss with weighting parameters $\lambda_1, \lambda_2$ (line 243) but does not discuss known practical difficulties: balancing multiple loss terms often requires adaptive weighting (e.g., via gradient statistics or NTK analysis), spectral bias limits high-frequency learning, and collocation point placement significantly affects accuracy. These are well-known obstacles that directly impact the proposed method's viability, and their absence is a significant gap for reproducibility.

### Trivial

None.

## Nice-to-Haves

- A single synthetic low-dimensional experiment ($d=1$ or $d=2$) with known ground truth, showing FKEE accuracy, variance across runs, runtime, and comparison to a standard MCMC expectation estimator would fundamentally change the paper's evaluability.
- A concrete construction showing how a non-Langevin MCMC algorithm (e.g., Metropolis-Hastings) maps to the SDE form would substantiate the universality claim.

## Removed Points

These points are flagged as removed; treat them with caution.

- **Strength about "consistency of Wasserstein-based structural loss"** — Removed because Theorem 37's claimed novelty hinges on an unspecified "loss function control term" (line 164) that is not described, making the contribution unverifiable from the paper as written.
- **Strength about "concrete relaxation of assumptions on f"** — Removed because, as verified, the comparison between $C^2$ and Lipschitz is apples-to-oranges (necessary vs. sufficient conditions for different problems).
- **Strength about "explicit framing of two motivating questions"** — Removed as generic; posing questions in an introduction is standard structure, not a distinctive contribution.
- **Harsh critic's point about "method replaces one hard problem with another"** — Not removed; subsumed into Major weakness 1 (PINN curse of dimensionality) with specific anchoring to the paper's claim on line 28.
- **Harsh critic's point about "experiments vacuous"** — Not removed; verified and elevated to Fatal.
- **Any criticism questioning availability of cited references/models** — Not present in inputs; no action needed.

## Novel Insights

None beyond the paper's own contributions. The core conceptual framework (using the Feynman-Kac PDE to replace Monte Carlo averaging) is interesting, but the paper does not provide sufficient evidence — experimental or theoretical — to evaluate whether it works in practice. The reviews surface this gap but do not add insight about the method itself.

## Suggestions

1. **Provide at least one complete experiment** with known ground truth, accuracy metrics, baseline comparison, and variance reporting — even on a low-dimensional synthetic problem. Without this, the paper cannot be evaluated.
2. **Substantiate or remove the curse-of-dimensionality claim** by either citing evidence for PINNs on high-dimensional Feynman-Kac-type PDEs or qualifying the scope.
3. **Specify the "loss function control term"** in Theorem 37's proof and show how it modifies the result from Bernton et al. (2017).
4. **Provide concrete SDE formulations for specific MCMC algorithms** beyond Langevin diffusion to support the universality claim.
5. **Acknowledge and discuss PINN training challenges** (loss balancing, spectral bias, collocation) with proposed mitigation strategies.

## Score and Decision

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>