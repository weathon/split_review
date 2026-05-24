Now I have enough information to write the consolidated review. Let me synthesize everything.

---

## Summary

This paper addresses the breakdown of conformal prediction (CP) coverage guarantees for time-dependent PDE surrogate models, caused by temporal distribution shift breaking exchangeability. The authors prove that in function space, the TV distance between solution distributions at different times can be 1 (Theorem 4.1), motivating a discretized approach. For linear PDEs with Gaussian initial conditions, they derive the closed-form Gaussian distribution of discretized solutions over time (Theorem 4.2) and propose likelihood-ratio reweighting for weighted CP. Experiments on a synthetic second-order PDE and a thermography dataset show the method (WCP) maintains target coverage where naïve CP and LSCI fail.

## Strengths

- **Theorem 4.1 is a genuine, non-trivial contribution.** The proof that for the heat equation with a Gaussian random initial condition, the TV distance between solution distributions at any two distinct times is exactly 1 provides a rigorous impossibility result in function space. This formally justifies why a discretized approach is necessary and why simple corrections (e.g., Barber et al.'s TV-based bound) cannot salvage function-space CP. This result stands independently of the rest of the method.

- **Clear problem formalization and motivation.** The paper carefully sets up the pushforward-of-measures formalism (Section 4.1) and gives concrete visual examples of coverage degradation (Figure 2). The connection between non-stationarity in time-dependent PDEs and the failure of exchangeability-based CP is well articulated.

- **Empirical demonstration of the method's behavior.** Table 1 and Figure 3 show that WCP maintains near-target coverage across prediction horizons and instability regimes. The method honestly reports infinite bands when the distribution shift is too large (tracked by n_∞), which is a principled failure mode — better than silently undercovering as naïve CP and LSCI do. The thermography experiment (appendix A.6) provides a real-world data point.

- **Computational efficiency.** WCP runs in seconds on 5000 test samples versus ~40 minutes for LSCI (Section 5), making it practical for deployment.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical gap in the weighted CP justification (Section 4.4).** Weighted CP (Barber et al., 2023) requires the likelihood ratio of the *full data point* between test and calibration distributions. The full data point is the pair (u_0, u_t): the nonconformity score (maximum absolute error over space) depends on both the initial condition u_0 (through the surrogate model's prediction) and the solution u_t. The paper instead uses the ratio of *marginal* densities of u_t alone (Equation 1). The marginal ratio p_{t+δ}(u_t)/p_t(u_t) does not in general equal the required joint ratio dP_{t+δ}(u_0, u_t)/dP_t(u_0, u_t), and the paper provides no argument for why this substitution preserves the coverage guarantee. This means the central claim that WCP provides "exact coverage guarantees" or "formal guarantees" is not adequately justified by the theoretical machinery presented. The empirical results, while promising, do not rescue the theoretical foundation.

### Minor

- **Assumption of known PDE dynamics limits scope.** The method requires exact knowledge of the PDE operator A, source term r(t), initial distribution parameters, and discretization (Section 4.3–4.4). While reasonable for controlled physical systems, the paper does not discuss how estimation errors in these quantities would affect coverage or whether the TV-distance correction from Barber et al. (2023) could be applied as a safeguard. This narrows the practical applicability relative to the strength of the claims.

- **Limited baseline comparisons.** The experiments compare only against naïve CP and LSCI. The paper mentions adaptive conformal inference (Gibbs & Candès, 2021) in related work but does not include it as a baseline. While the paper argues these methods provide only asymptotic guarantees, including one would contextualize WCP's finite-sample performance more convincingly. The existing comparisons are adequate for demonstrating undercoverage of exchangeability-based methods, but a broader comparison would strengthen the empirical case.

- **Overstatement of empirical findings in some regimes.** In Table 1 with a = −0.005, naïve CP already achieves coverage at or above 90% (0.91–0.99), making WCP's advantage marginal in that regime. The claim that WCP is "the only method providing reliable coverage" (Section 5) should be qualified to note that in weakly unstable regimes, simpler methods may suffice.

### Trivial

- Theorem 4.2's derivation (Gaussian + linear transformation = Gaussian) is elementary and the paper treats it as a main result; the novelty lies in the application context, not the derivation itself.

## Nice-to-Haves

- A discussion of robustness to estimation error in the PDE parameters or initial distribution, perhaps using the TV-distance bound from Barber et al. (2023) that the paper already cites.
- Inclusion of an adaptive/online CP baseline (e.g., Gibbs & Candès, 2021) to show where WCP's finite-sample guarantee provides concrete advantages over asymptotic methods.
- An explicit statement of the conditions under which the marginal density ratio equals the required joint density ratio, or a reformulation of the nonconformity score to make the marginal ratio valid.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh Critic: "Incorrect construction of the likelihood weights (fatal)."** → RETAINED as Major. The substance of this criticism is valid: the paper uses marginal rather than joint density ratios without justification. However, demoted from Fatal to Major because (a) the gap is potentially addressable through a revised theoretical argument (e.g., reformulating the score or deriving joint weights), and (b) Theorem 4.1 has independent value regardless. The empirical method may still work as a well-motivated heuristic even if the theoretical justification needs revision.

- **Harsh Critic: "Weak experimental baselines — Gibbs & Candès 2021 not included."** → Retained as Minor (weakened). The paper discusses this method in related work and provides a rationale (asymptotic guarantees only). Including it would improve but not determine the paper's fate.

- **Strength Finder: "Practical efficiency over peers"** → Retained as a minor strength; it's a concrete fact (seconds vs. 40 minutes) but efficiency alone doesn't rescue the theoretical gap.

- **Strength Finder: "Realistic and well-motivated assumptions"** → Retained but noted as context-dependent. The Gaussian assumption is common in the literature but the assumption of known PDE parameters is a limitation.

- **Removed: Harsh Critic's assertion that this is "fatal"** → Demoted to Major as explained above; a fatal flaw must be unambiguous given what's on the page, and while the gap is real, there exist plausible paths to fix it.

- **Removed: Harsh Critic's claim about "unrealistic dependence on exact knowledge of dynamics" being a severe limitation** → Weakened to Minor. In the linear PDE setting the paper studies, assuming the PDE is known is standard and reasonable. It's a scope limitation, not a flaw.

- **Removed: Harsh Critic's Section-by-Section note about Theorem 4.1 being "largely tangential"** → Removed. The theorem directly motivates the shift to discrete space and is a genuine contribution.

## Novel Insights

The key tension revealed by this paper — and by its review — is that the structure of PDE solution operators creates a distinctive challenge for importance-weighting in conformal prediction. Because the solution u_t is a deterministic function of the initial condition u_0, the joint distributions P_cal(u_0, u_t) and P_test(u_0, u_{t+δ}) have a peculiar relationship: the marginal of u_0 is identical in both, but the conditional P(u_t | u_0) changes. Standard covariate-shift CP doesn't apply (the "covariate" u_0 hasn't shifted), and the general weighted CP of Barber et al. runs into support-mismatch issues because the conditional distributions are Dirac deltas at different locations. This means that neither standard formalism cleanly covers this setting, and a genuinely new theoretical bridge is needed — simply plugging marginal density ratios into the weighted CP formula is not sufficient without additional justification.

## Suggestions

- The most important fix is to rigorously justify Equation (1). Options include: (a) deriving the correct joint density ratio for the (u_0, u_t) pair under the discretized model, (b) reformulating the nonconformity score to depend only on u_t (e.g., using a model-free score), or (c) proving that under the linear-Gaussian structure the marginal ratio does in fact equal the required joint ratio (or provides a valid bound).
- Add a discussion of what happens when PDE parameters are estimated rather than known — even a brief worst-case analysis using the TV-distance correction would significantly strengthen practical credibility.
- Qualify the "only method providing reliable coverage" claim to reflect regimes where naïve CP already achieves target coverage.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `v8RDgaEtE2` (CP under bias) | 2.50 | R1 (low) | Our paper is substantially stronger — has theory, experiments, clear problem |
| `LwAG269lIq` (PDE discovery, adjoint) | 3.00 | R1 (low) | Our paper has clearer contributions and empirical validation |
| `fzZfju8y0g` (In-context neural PDE) | 3.40 | R1 (low) | Our paper is better motivated and has clearer results |
| `GkJCgUmIqA` (PINN with trSQP) | 3.00 | R1 (low) | Our paper is stronger in theoretical grounding |
| `cF6OoaYcRa` (Calibrated physics-informed UQ) | 4.50 | R1/R2 (mid) | Our paper has stronger theory (Theorems 4.1, 4.2) and better baselines |
| `tl63stKeSC` (Learnable quadrature for PDEs) | 4.50 | R2 (mid) | Our paper is more focused and empirically grounded |
| `WwQdcQROmb` (SafeConPhy) | 4.00 | R1 (mid) | Our paper has cleaner methodology |
| `5KqveQdXiZ` (Science-constrained learning) | 5.25 | R1/R2 (mid) | Comparable — both have interesting theory with practical gaps |
| `AKAz88zYLB` (CP for dose-response) | 5.80 | R2 (mid) | Slightly weaker — our theoretical gap is more significant than theirs |
| `LxkgScfHKf` (Conformal training, reduced variance) | 4.50 | R2 (mid) | Our paper is more ambitious in scope |
| `x4ZmQaumRg` (AL4PDE benchmark) | 7.00 | R1 (high) | Clearly stronger — comprehensive, well-executed |
| `fU8H4lzkIm` (PhyMPGN) | 8.00 | R1 (high) | Much stronger — major contribution with strong results |
| `uKZdlihDDn` (Diffusion graph networks) | 7.60 | R1 (high) | Much stronger |
| `A3YUPeJTNR` (Hidden cost of waiting) | 8.00 | R1 (high) | Not directly comparable (different domain) |

**Round 1 bracket:** The paper sits between the 4.50 anchors (weaker CP-for-PDEs papers) and the 7.00+ anchors (strong, well-executed contributions), roughly in the 4.5–6.0 range.

**Round 2 narrowing:** Within the bracket, the paper is clearly stronger than the 4.50 CP-for-PDEs papers (which lacked theory and baselines). It is comparable to the 5.25 SCL paper — both have real theoretical contributions paired with practical limitations. It is slightly weaker than the 5.80 dose-response CP paper, which had a cleaner (if incremental) methodology. The primary differentiator is the theoretical gap in the weighted CP justification: this is a significant issue that prevents a higher score, but the paper has genuine merits (Theorem 4.1, clear motivation, working empirical method) that place it above the clearly weak papers.

**Final score: 5.0.** The paper addresses an important problem, has a non-trivial theoretical result (Theorem 4.1), and demonstrates a practically useful method. However, the central methodological claim — that weighted CP with marginal density ratios provides exact coverage guarantees — is not adequately justified, which significantly weakens the contribution. This is a borderline paper that could become accept-worthy if the theoretical gap is addressed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>