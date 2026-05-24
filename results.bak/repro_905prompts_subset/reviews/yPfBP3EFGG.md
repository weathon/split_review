Now I'll write the consolidated final review.

## Summary

This paper proposes STNAdam, a stochastic variant of Adam for "nonconvex + weakly-convex" composite optimization that employs a novel two-track iteration framework. The algorithm maintains two intertwined trajectories — an extrapolation track governed by Nesterov momentum and a regular update track with Adam-style adaptive conditioning — that interact to guide the optimization. The paper provides a convergence analysis under the Kurdyka-Łojasiewicz (KL) property, establishing almost-sure convergence to a stationary point with explicit rates (linear, sublinear, or finite depending on the KL exponent), and validates the method on low-light image enhancement (LIE) tasks where STNAdam-SARAH achieves the best PSNR (22.26), SSIM (0.906), and LPIPS (0.050) among eleven compared algorithms.

## Strengths

- **Novel two-track coupled iteration framework.** The paper introduces a genuinely new algorithmic architecture that simultaneously maintains an extrapolation trajectory and a regular update trajectory, interactively driven by Nesterov momentum and Adam-style adaptive conditioning. This goes beyond existing single-track variants (NAdam, SAdam, SNAdam) and is concretely specified in Algorithm 1, Steps 3–5, and visualized in Figure 1(d).

- **Comprehensive convergence analysis under the KL property.** Theorem 1 establishes almost-sure convergence of the STNAdam sequence to a stationary point, and Theorem 2 provides explicit convergence rates (linear, sublinear, or finite) depending on the KL exponent. These results hold for a general class of variance-reduced gradient estimators (SAGA, SARAH, SVRG, SPIDER) with adaptive hyper-parameter scheduling, making this one of the more complete theoretical treatments of a stochastic Adam variant for the "nonconvex + weakly-convex" composite setting.

- **Convincing empirical performance on LIE.** Table 2 shows that all three STNAdam variants (SGD, SAGA, SARAH) outperform the corresponding single-track counterparts (SGD, SAdam, SNAdam) on the LOL benchmark, and STNAdam-SARAH achieves state-of-the-art results across all three metrics. The joint denoising results in Table 3 further demonstrate practical robustness. The ordering STNAdam-SARAH > STNAdam-SAGA > STNAdam-SGD > SNAdam > SAdam ≥ SGD provides internal consistency.

- **Compatibility with multiple variance-reduced estimators.** The algorithm is instantiated with SGD, SAGA, and SARAH estimators, with explicit update formulas given for each (Section 2). The results show clear improvement as variance reduction increases, demonstrating the framework's flexibility.

## Weaknesses

### Major
None.

### Minor

- **No explicit ablation of the two-track mechanism.** While the comparison STNAdam-SGD vs SGD (18.06 vs 14.80 PSNR) provides implicit evidence that the two-track framework helps — since both use the same non-variance-reduced gradient estimator, the main algorithmic difference is the two-track mechanism plus the adaptive conditioning details — a cleaner ablation (e.g., STNAdam with only the regular track, or with only the extrapolation track) would directly attribute the observed gains to the two-track design rather than to other accumulated algorithm choices. This is the single most impactful experiment missing from the paper.

- **Theory-practice gap for SGD.** The convergence theory (Lemma 1, Theorems 1–2) assumes a variance-reduced gradient estimator satisfying specific MSE bound and geometric decay conditions. The paper correctly notes that "SGD does not exhibit variance reduction" (Section 2). However, STNAdam-SGD is included in experiments without explicitly stating that the theoretical convergence guarantees do not apply to this variant. This creates a disconnect between the theoretical claims and one of the experimental configurations.

- **Parameter update intervals rely on unobservable constants.** The intervals for γₖ₊₁, λₖ₊₁, αₖ₊₁ in (6)–(8) depend on theoretical constants (V₁, V_T, ρ, M, s, L, τ) that are not specified, estimated, or even given order-of-magnitude values. No procedure for computing these constants from data is provided, and the experiments do not report what values or heuristics were actually used. This limits the practical implementability of the claimed "adaptive hyper-parameter scheduling that removes hand-tuning."

- **Limited empirical evaluation.** Results are reported on a single benchmark (LOL) without error bars, standard deviations, or multiple runs. The per-iteration timing (e-05 seconds) is reported without clarifying the experimental setup (e.g., number of iterations, batch size, convergence criteria). Evaluation on additional optimization problems (e.g., logistic regression with nonconvex regularizers, network training) would strengthen the claim of generality beyond LIE.

- **Hyperparameter choices for baselines not reported.** No information is given about the learning rates, β₁, β₂, batch sizes, or number of iterations used for SGD, SAdam, or SNAdam, making it difficult to assess whether these baselines were reasonably tuned.

### Trivial
None.

## Nice-to-Haves

- A one-track vs two-track ablation study (STNAdam with the extrapolation track disabled) would directly verify the core algorithmic claim.
- Evaluation on a standard nonconvex optimization benchmark (e.g., neural network training, matrix factorization) would demonstrate generality beyond LIE.
- Reporting hyperparameter settings and conducting a sensitivity analysis for the stochastic Adam variants would improve reproducibility.

## Removed Points

The following points from the reviewers are removed with justification:

- **"Invalid comparison against LIE-specific methods"** — The paper clearly separates its claims: (i) optimizer performance is compared against single-track algorithms (SGD, SAdam, SNAdam); (ii) practical performance on the LIE task is compared against custom LIE methods. Both comparisons are standard and appropriate. The LIE methods are not claimed to solve the same optimization problem for optimizer-benchmarking purposes; they are domain baselines for the application task. This criticism conflates two distinct claims.

- **"Time units (e-05 seconds) are implausibly small"** — Per-iteration times for small image patches on a GPU are legitimately in this range. No evidence of error.

- **"Comparison against SNAdam is not an ablation because it differs in multiple ways"** — This is correct but the point is already covered by the explicit "no ablation" weakness above. The STNAdam-SGD vs SGD comparison does provide some implicit evidence.

- **"No error bars or statistical significance"** — Common in optimization papers reporting single runs on a benchmark; noted as minor under "limited empirical evaluation" rather than as an independent weakness.

- **"Lemma 1 is essentially an assumption, not a property proven for concrete estimators"** — The paper states the proof is "analogous to that presented in Bertsekas & Tsitsiklis (1989); Wang & Han (2023)" and provides the conditions that define variance-reduction. It's standard in optimization to cite prior results for estimator properties.

## Novel Insights

The two-track coupling idea is the most interesting conceptual contribution. Unlike prior accelerated Adam variants that use one corrected momentum to produce a single iterate, STNAdam maintains two coupled sequences: one driven by the bias-corrected momentum estimate (the "regular" xᵏ track) and one driven by the second-time-corrected momentum (the "extrapolation" x̃ᵏ track), linked through a convex combination weight λₖ₊₁. This creates a compositional update where the extrapolation point is formed from a blend of the current regular iterate and the previous extrapolation iterate, then both tracks are updated via proximal-gradient steps with different step sizes. The analysis then shows that this coupling produces a descent on a carefully constructed energy function Gᵏ that jointly tracks all the relevant error terms. The idea of using two intertwined trajectories to simultaneously widen the update neighborhood and improve the iteration direction is genuinely creative and could inspire further work on multi-track optimization architectures.

## Suggestions

- Add a dedicated ablation experiment: compare STNAdam with the two-track mechanism against a version with the extrapolation track disabled (i.e., using only one of the two proximal-gradient updates), keeping all other algorithm components identical. This would directly validate the core algorithmic contribution.
- Explicitly clarify the scope of the theoretical guarantees: state that Theorems 1–2 apply to variance-reduced estimators (SAGA, SARAH, SVRG, SPIDER) and not to plain SGD, and position STNAdam-SGD results as empirical exploration.
- Either provide concrete strategies to estimate the theoretical constants in (6)–(8) for practical use, or report what heuristic values were actually used in the experiments and how they were chosen.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Searched three bands for "stochastic Adam optimizer convergence nonconvex composite optimization":

- Low band (avg < 3.5): anchors at 1.67 (AProx, Reject), 2.50 (AdamE, Reject), 2.50 (Exact linear-rate, Reject), 3.25 (Federated composition, Reject).
- Middle band (3.5 < avg < 7.5): anchors at 4.25 (Adam under non-uniform smoothness, Reject), 4.25 (Online learning meets Adam, Reject), 6.25 (Inexact stochastic PPA, Accept), 6.67 (Last-iterate SGD, Accept).
- High band (avg > 7.5): anchors at 7.60, 8.00 (tight lower bounds, DRO, Nash equilibria — all Accept).

The paper is clearly above the low band and clearly below the high band, placing it in the middle band. The initial bracket was (3.5, 7.5).

**Round 2 — Narrowing.** Searched within (3.5, 5.5) for KL-based stochastic optimization and within (5.0, 7.0) for Adam+LIE topics. Topically similar anchors: 5.00 (Stochastic Hamiltonian descent, Reject — scores 6,3,6), 5.00 (High-probability composite + VI, Reject — scores 5,5,5), 6.40 (Interpretable unsupervised LIE, Accept — not an optimizer paper), 6.00 (Exposure bracketing LIE, Accept — not an optimizer paper).

Comparing against the stochastic Hamiltonian descent paper (5.00, Reject): that paper has very clean almost-sure convergence theory for a class of clipped/normalized momentum methods but was criticized for limited novelty beyond applying standard ODE techniques. This paper has more algorithmic novelty (two-track framework) but has evaluation gaps (no ablation, theory-practice gap). They are comparable in overall strength. The high-probability composite optimization paper (5.00, Reject) was considered technically sound but limited in novelty and lacking experiments. This paper has more novelty and experiments, making it slightly stronger.

**Final score: 5.0.** The paper sits above the purely incremental contributions at 4.25 but falls short of the clean, complete packages at 6.25+. The two-track framework is genuinely novel and the theory is solid, but the missing ablation, theory-practice gap for SGD, impractical parameter intervals, and limited empirical scope prevent this from being a fully convincing package.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>