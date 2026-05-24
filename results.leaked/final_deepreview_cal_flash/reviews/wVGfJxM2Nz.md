Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper presents an empirical study arguing that geometry-informed inductive biases (SPD manifold constraint via Riemannian optimization for dissipative systems; symplectic structure for conservative systems) enable dramatically smaller models with better generalization than structure-naive baselines. Two case studies are examined: a 2D heat transfer system identified via linear state-space models with Riemannian optimization, and an 18D Fermi-Pasta-Ulam-Tsingou system modeled with Symplectic Hamiltonian Neural Networks (SHNNs). The SHNN experiment provides the strongest evidence: a 1,441-parameter SHNN achieves rollout MSE ≈ 8.9e-09 and energy drift RMS ≈ 1.3e-03, whereas a 97,074-parameter LSTM yields rollout MSE ≈ 1.7e-06 and drift ≈ 5.9.

## Strengths

1. **Compelling evidence that structure preservation yields dramatic improvements in model efficiency.** Table 2 and Figure 3 show that a 1,441-parameter SHNN outperforms all LSTM and NeuralODE variants (up to 97,074 parameters) on rollout MSE and energy drift by multiple orders of magnitude. The systematic sweep over hidden layers and widths — covering 16 SHNN configurations, 16 NeuralODE configurations, and 4 LSTM configurations — demonstrates that the advantage of structural priors is not an artifact of a particular model size.

2. **The conservative-case energy-drift analysis provides mechanistic insight into why structure-naive models fail.** Figure 4 overlays predicted trajectories on the true Hamiltonian energy surface, visually showing that SHNNs stay close to the correct energy level while LSTMs "jump" between levels. The drift RMS metric quantifies this, and the paper correctly identifies non-conservation of energy as the root cause of poor long-horizon generalization.

3. **Clean comparison of Riemannian vs. Euclidean optimization for the dissipative case.** Both RieOpt and EucOpt start from the same physics-derived initial state matrix (line 85) and share the same LSSM functional form. RieOpt (SPD-constrained) achieves lower MSE on both London test data and Chicago out-of-distribution data (e.g., Chicago T_ext1: 1.36 vs. 3.35 for EucOpt, Table 1), cleanly isolating the benefit of the SPD manifold constraint.

4. **The paper connects two structurally different energy regimes — dissipative (SPD) and conservative (symplectic) — under a unified geometric framework.** This goes beyond demonstrating a single architecture and positions structure preservation as a cross-domain principle, lending breadth to the thesis.

## Weaknesses

### Fatal
None. The core claim — that structure-preserving inductive biases enable smaller, more generalizable models — is supported by at least one reasonably clean experiment (the SHNN vs. LSTM/NeuralODE comparison on FPUT). The identified weaknesses weaken the evidence but do not invalidate the central argument.

### Major

1. **No uncertainty quantification; all results appear to be from single runs.** Tables 1 and 2 report point estimates without error bars, confidence intervals, or mention of multiple random seeds. This is a significant gap for a comparative study whose claims depend on differences that could be within the noise of random initialization (e.g., NeuralODE drift RMS ranges from 1.2 to 3.7e+02 across configurations in Table 2, suggesting high variance). Without multiple seeds, it is impossible to assess whether the reported trends are statistically robust or whether the ordering of methods could change under different initializations.

2. **Asymmetric comparison in the dissipative case: LSSM methods receive a physics-derived initial state, while black-box baselines do not.** The paper states (line 85): "We start with an initial state matrix A that is derived from Physics but misspecified (see Table 3)". RieOpt and EucOpt both benefit from this initialization; RF, XGBoost, and LSTM do not. The paper attributes RieOpt's superior generalization on Chicago data to "structure-awareness," but the black-box models had to learn the dynamics entirely from London data without this strong prior. The comparison between RieOpt and EucOpt remains clean (both start from the same physics-derived point, differ only in the optimization constraint), which partially supports the claim, but the paper's overall argument would be significantly strengthened by an ablation where RieOpt is initialized from a random SPD matrix to isolate the effect of the constraint itself versus the benefit of the physics prior.

3. **Missing HNN baseline in the conservative case bundles the symplectic integrator effect with the Hamiltonian parameterization.** The paper compares SHNN (Hamiltonian parameterization + symplectic implicit midpoint integrator) against LSTM and NeuralODE, but not against a standard HNN (Hamiltonian parameterization + non-symplectic integrator such as Dormand–Prince). This makes it impossible to tell how much of the advantage comes from the Hamiltonian parameterization and how much from the symplectic integrator. Adding an HNN baseline would directly answer this and substantially strengthen the paper's claims about which structural component matters.

4. **Technical inaccuracies in the geometric motivation (Section 2.1.1).** The description of the s-plane to z-plane mapping is garbled: it mentions "wrapping the stable eigenvalues located in the left half-plane (i.e., Re(λ_i) < 0) within the unit circle in the s-plane where Re(λ_i) > 0" (line 79). The s-plane does not have a unit circle (that is the z-plane), and eigenvalues with Re(λ_i) > 0 are unstable in continuous time, not stable. The paragraph also claims that matrices on the boundary of the SPD manifold are "bistable" — this term is used loosely and does not correspond to standard control-theoretic usage (zero eigenvalues imply marginal stability, not bistability). While these inaccuracies do not affect the experimental results, they undermine confidence in the geometric foundations that motivate the approach and should be corrected.

### Minor

1. **Equation (7) contains a typo:** the loss term reads Φ_B T_i but should be Φ_B U_i to match Equation (4). This is a reproducibility issue.

2. **The dissipative example is intrinsically low-dimensional (2 states, ~5 parameters), limiting the force of the "smaller models" argument.** A 5-parameter model outperforming an LSTM is unsurprising given the strong physics prior; a higher-dimensional dissipative system would provide a more convincing demonstration.

3. **The conservative case uses a single training trajectory (30,000 steps) from one initial condition.** Models may overfit to the specific dynamics of that trajectory, and the paper does not discuss this limitation or test generalization to trajectories from different initial conditions in a controlled way.

4. **No computational cost analysis.** The paper advocates for "smaller models" but does not discuss that Riemannian optimization (geoopt) and the implicit midpoint integrator (which requires solving a nonlinear system at each step) incur computational overhead that may partially offset the parameter savings.

5. **The LSTM sweep varies only hidden width, not number of layers** (line 187). A deeper LSTM may perform better, though the paper acknowledges this choice.

6. **Rollout is evaluated over only 1,000 steps.** For Hamiltonian systems, the distinguishing behavior of structure-preserving methods is most visible over much longer horizons (10,000+ steps). The energy drift metric partially addresses this, but the paper does not confirm that the 1,000-step results are indicative of longer behavior.

### Trivial

1. Inconsistent citation: "Xueréb Conti et al. (2023)" (line 256) vs. "Xuereb Conti et al. (2023)" (line 407).
2. The claim that "structure-naive models (RF, XGBoost and LSTM) seem to roll-out the test segments accurately" (line 179) is an overstatement for the LSTM, which obtains London MSE of 25.7 for T_ext1 — the worst in Table 1.

## Nice-to-Haves

- Run RieOpt from a random SPD matrix initialization to isolate the effect of the SPD constraint from the physics prior.
- Add HNN (with a non-symplectic integrator) as a baseline for the conservative case.
- Report all metrics with mean ± std over at least 5 random seeds.
- Vary the training data size (e.g., 10%, 25%, 50% of the trajectory) to directly test the claim about data efficiency.
- Evaluate longer rollouts (10,000+ steps) for the conservative system.
- Provide a computational cost comparison (training time, inference cost) for all methods.

## Removed Points

These points were identified by the reviewer but are removed from the main weaknesses for the reasons stated:

1. *"The dissipative system has only two states, so the LSSM has 5 parameters — it is trivially small. Showing that a 5-parameter model outperforms an LSTM... is not evidence of a principle."* — This criticism is valid but downgraded to Minor (issue #2 above) because the paper's core claim about model size is better supported by the 18D FPUT case; the dissipative example primarily illustrates the benefit of the SPD constraint (RieOpt vs. EucOpt), not model-size reduction per se.

2. *"A meaningful demonstration would require a higher-dimensional dissipative system."* — This requests experiments beyond the paper's stated scope; moved to Nice-to-Haves as a suggestion for future work.

3. *"Figure 4 captions mention dashed/white ellipses but figures are not visible in the parsed text."* — This is a PDF parsing artifact, not an author error.

4. *"The paper should also provide quantitative trajectory error metrics for unseen initial conditions."* — The paper already reports rollout MSE and energy drift, which are quantitative trajectory metrics; this specific request is partially addressed.

5. *"The roll-out MSE for the conservative case is only reported for 1,000 steps."* — Kept as Minor (#6) but note the energy drift metric partially compensates.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the paper itself does not already articulate.

## Suggestions

1. Add multiple random seeds (± std) to all experiments, especially for LSTM and NeuralODE which exhibit high variance in Table 2.
2. Add an HNN baseline to the conservative case to disentangle the Hamiltonian parameterization from the symplectic integrator.
3. Add a RieOpt ablation with random SPD initialization to the dissipative case.
4. Correct the technical inaccuracies in Section 2.1.1 (s-plane/z-plane mapping, bistability claim).
5. Fix the typo in Equation (7) (Φ_B U_i instead of Φ_B T_i).
6. Discuss the limitation of the asymmetric comparison (physics prior for LSSM, none for black-box models) explicitly.
7. Add a computational cost comparison table.

## Calibration Report

**Round 1 — Bracketing:** Queries across three bands (avgs < 3.5, 3.5–7.5, > 7.5) on structure-preserving ML and symplectic/Hamiltonian NN topics. Weak band returned anchors at 2.0–3.0 (clearly weaker than this paper). Middle band returned anchors at 5.75–7.0 (most comparable). Strong band returned anchors at 7.6–8.0 (clearly stronger). **Initial bracket: 4.5–7.0.**

**Round 2 — Narrowing:** Two queries targeting 4.0–6.5 and 5.5–7.0 on structure-preserving NN comparisons and symplectic Hamiltonian benchmarks. Retrieved anchors:
- "Learning Chaotic Dynamics with Embedded Dissipativity" (4.67) — proposes a novel architecture with formal guarantees but experiments are on simple low-D systems with missing baselines; the paper under review has stronger empirical demonstration (SHNN on 18D FPUT) but less rigorous methodology.
- "Dynamical Similarity Analysis" (5.25) — not closely related in topic.
- "Collective variables of neural networks" (6.00) — not closely related.
- "Learning Dynamical Systems with Helmholtz-Hodge Decomposition" (5.80) — proposes a GP-based method with theory and simple experiments; comparable overall quality to the paper under review.
- "Cross Domain Generalization of Hamiltonian Representation" (5.75, Accept) — applies meta-learning to HNNs, has some experimental gaps; comparable quality.
- "Poisson-Dirac Neural Networks" (6.60, Accept) — proposes a novel architecture with solid experiments; stronger.
- "Port-Hamiltonian Architectural Bias" (7.00, Accept) — proposes a novel method with theory and strong experiments; clearly stronger.

**Final score determination:** The paper is weaker than the novel-method papers at 6.6–7.0. It is comparable to the empirical/meta-learning papers at 5.75–5.80 but has additional experimental gaps (no error bars, asymmetric comparison) that those papers partially avoid. The paper is clearly stronger than the weak-band anchors (2.0–3.0) and the dissipativity anchor (4.67). **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>