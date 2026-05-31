## Summary

The paper introduces Neural Predictor-Corrector (NPC), a reinforcement learning framework that replaces hand-crafted heuristics in predictor-corrector solvers across four diverse homotopy problem classes: robust optimization (GNC), global optimization (Gaussian homotopy), polynomial root-finding (homotopy continuation), and sampling (annealed Langevin dynamics). NPC formulates the PC parameter selection as an MDP, uses PPO to train policies that adaptively control predictor step size and corrector termination, and employs amortized training to enable zero-shot deployment on unseen instances. Experiments across all four domains demonstrate 70–85% reductions in corrector iterations while maintaining comparable accuracy.

## Strengths

- **First unified treatment of four diverse homotopy problems under a common PC structure.** The paper provides explicit homotopy interpolation formulas (Eqs. 1–4) for GNC, GH, HC, and ALD, and identifies their shared predictor-corrector architecture. This unification is concretely demonstrated rather than merely asserted, and it is a prerequisite for a general solver.

- **Complete RL formulation of the PC control problem.** Algorithm 1 and the MDP definition (state: homotopy level, corrector statistics, convergence velocity; actions: step size, termination threshold) provide the first explicit RL parameterization of the full PC loop across homotopy classes. This is a genuinely new design that goes beyond prior work on learning individual components.

- **Consistent and substantial efficiency gains across all four tasks.** Tables 1–5 report large reductions in corrector iterations (GNC: ~70–80%, GH: ~30–50%, HC: ~70–80%, ALD: ~73–74%) and corresponding runtime reductions, while maintaining accuracy comparable to classical baselines. The consistency across structurally different problems is the strongest evidence for the method's viability.

- **Cross-instance generalization demonstrated empirically.** The GNC agent trained on a single sequence (Aquarius) generalizes to unseen sequences (bunny, cube, dragon) and to a different task (multi-view triangulation). The GH, HC, and ALD agents trained on randomized instances generalize to fixed benchmarks. This supports the amortized training claim.

- **Ablation study validates each state component's contribution.** Table 6 shows that removing any single component (homotopy level, corrector tolerance, corrector iteration, convergence velocity) increases iterations, confirming the informativeness of the state design. Corrector statistics (tolerance, iteration) are the most impactful.

- **Superior numerical stability on challenging instances.** In Table 3, SLGH_d and PGS fail on Himmelblau (f(x*)=2.57, 1.18) while NPC achieves f(x*)=0.00. In Table 2, IRLS GNC produces large point errors (log(E_p)=1.74, 0.50) while NPC matches Classic GNC accuracy (~ -4.7 to -5.0). In Table 4, NPC achieves 100% success rate on all polynomial systems.

## Weaknesses

### Fatal
None.

### Major
- **No variance or significance reporting.** All results in Tables 1–5 are point estimates (averages over 50 trials) without standard deviations, confidence intervals, or error bars. While the efficiency improvements are large enough (70–85%) that variance is unlikely to reverse the qualitative conclusions, the accuracy comparisons (e.g., W₂=11.57 vs. 11.91 on the 40-mode GMM in Table 5) lack the statistical context needed to assess whether differences are meaningful. The ablation study (Table 6) also reports only a single ∆Iter value without variance. This is the most significant evidential gap in an otherwise well-executed experimental section.

### Minor
- **Cross-task transfer in GNC experiments lacks motivation.** The NPC agent trained on point cloud registration (Aquarius sequence) is evaluated on multi-view triangulation (Table 2) without any discussion of why transfer between these structurally different tasks is expected or plausible. The state representation is generic (homotopy level, corrector statistics, convergence velocity), which may explain the transfer, but the paper does not make this argument. The *empirical* results are positive, but the reasoning gap leaves this looking unplanned rather than principled.

- **Claim that self-supervised training "fails" is unsupported.** Section 4.2 argues that self-supervised learning is inadequate because the future contribution of a step size depends on unknown local geometry. This is a plausible argument, but no empirical comparison to a supervised or self-supervised baseline is provided. Including even a simple baseline (e.g., supervised step-size prediction from local trajectory features) on one domain would substantiate the motivation for RL.

- **GNC training uses a single instance, not a distribution.** The GNC agent is trained on a single point cloud sequence (Aquarius), unlike the other three domains where training uses randomized problem instances. This weakens the "amortized training" claim for GNC specifically, though the positive cross-instance generalization results partially mitigate this concern.

- **Scalability to higher-dimensional problems is not addressed.** All experiments use low-dimensional problems (2D functions, small polynomial systems, up to 10-dim sampling) with a small 2×16 MLP policy. The paper does not discuss whether this architecture would scale to higher-dimensional settings or what limitations might arise.

### Trivial
- **Algorithm 1's corrector convergence criterion is ambiguously stated.** Line 6 checks `H(x_{t_n}, t_n) ≤ epsilon_n` as a while-loop condition. The homotopy function value H being below a tolerance is not the standard convergence criterion for correctors across all four domains (e.g., for Langevin sampling, the corrector does not minimize an objective). This may be clarified in the appendix (which is stripped by the parser), but as presented in the main text, it is confusing.

## Nice-to-Haves
- A brief sensitivity analysis of the reward weighting coefficients λ₁, λ₂ would improve reproducibility and show how the accuracy-efficiency trade-off is controlled.
- Reporting per-trial distributions or worst-case performance (failure rate, tail behavior) would strengthen the efficiency claims and address concerns about stability.

## Removed Points
- **Baseline under-specification (Harsh Critic #3):** The critic argues that "Classic GNC," "Classic HC," and "Classic ALD" are not parameterized. However, the paper states "Details are provided in Appendix A" for all problem-specific implementations. The appendix is stripped by the parser; these details exist in the original submission. Additionally, these are well-known methods with standard implementations cited in the paper.

- **"Unification overclaimed" (Abstract/Introduction framing):** The critic claims the unification novelty is overstated. However, the paper provides explicit, concrete homotopy formulations (Eqs. 1–4) and identifies the shared PC structure across four domains that have developed largely independently. The paper does not claim to invent the homotopy paradigm but rather to provide the first systematic unified formulation across these specific domains with a practical solver. This is a reasonable contribution claim.

- **Predictor mechanism under-specified:** The critic asks for the specific prediction mechanism (linear extrapolation, higher-order) as a weakness. The PC framework is intentionally domain-agnostic; domain-specific prediction mechanisms are standard in each field and detailed in the appendix. This level of abstraction is appropriate for the main text describing a general framework.

- **CPL/iDEM runtime omission:** The paper explicitly explains why runtimes for CPL and iDEM are not comparable (different hardware, C++ vs Python, per-task training costs). The critic's request for "normalized estimates" goes beyond standard practice.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add standard deviations (or per-trial distributions) to all tables (1–6). Even a supplementary table with mean ± std would dramatically improve the evidential quality.
2. Add a brief discussion in Section 5.2 explaining why the GNC policy trained on point cloud registration transfers to multi-view triangulation, highlighting the generic nature of the state representation.
3. Include a supervised or self-supervised baseline for at least one domain (e.g., GH) to substantiate the claim that RL is necessary.
4. Add a limitations paragraph discussing scalability to higher-dimensional problems and the current low-dimensional scope.
5. Clarify the corrector convergence criterion in Algorithm 1, or note that domain-specific criteria are used in practice.

## Score and Decision

**Calibration process:**

Round 1 (Bracketing): Searched "reinforcement learning for optimization solvers" in three score bands.
- Weak band (≤3.5): Anchors at 3.40, 3.40, 3.00, 3.00 (e.g., XTxdDEFR6D at 3.40, SrnTGdJKYG at 3.00) — rejected papers with weak experiments or poor framing.
- Middle band (3.5–7.5): Anchors at 3.75, 5.75, 4.00, 5.75 (e.g., Y3haavNdBX at 3.75, CFLEIeX7iK at 5.75, wsb9GNh1Oi at 5.75).
- Strong band (≥7.5): Anchors at 8.00, 8.00, 8.00, 8.00 (e.g., 5t57omGVMw, OOxotBmGol) — accepted papers with strong theoretical foundations or comprehensive evaluation.

**Round 1 bracket:** Narrowest plausible range: **4.5–7.0**.

Round 2 (Narrowing within bracket): Searched two queries within the bracket.
- jqVj8vCQsT (5.60, "Learning a Neural Solver for Parametric PDE"): Scores ranged 3–8; the paper has similar learning-to-optimize framing but weaker baselines and unclear experiments. The NPC paper is stronger — cleaner experiments, broader scope, clearer contributions.
- wsb9GNh1Oi (5.75, "Learning Multiple Initial Solutions"): Acceptable but rejected paper with limited dimensionality and novelty concerns. NPC is stronger — broader scope (4 domains vs 3 control tasks), more novel methodology.
- scdGzuwC9u (6.00, "Reoptimization for MILP"): Good paper with some concerns about baseline fairness. NPC is comparable in quality — both have clear contributions and solid experiments, but NPC's missing variance reporting is parallel to the mild baseline concerns in scdGzuwC9u.
- 9Fh0z1JmPU (6.50, "Progressively Refined Differentiable Physics"): Accepted with solid methodology and clear savings demonstrated. NPC has a broader scope but less polished experimental reporting (no variance). NPC is slightly weaker than this anchor.

**Final score:** 6.0. The paper sits above the 5.75 anchors (broader scope, more novel unification + RL formulation) but below the 6.50 anchor (missing variance reporting, appendix-dependent details). The core contribution — a unified RL-based PC solver across four homotopy problem classes — is solid and novel. The experimental evidence is broad and consistently positive. The main gap (no variance reporting) is serious but addressable and does not undermine the clear efficiency gains.

The paper is an **Accept** at ICLR. It makes a genuine contribution to the intersection of homotopy methods and reinforcement learning, with consistent empirical support across diverse domains. The missing variance reporting should be addressed in the camera-ready version.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>