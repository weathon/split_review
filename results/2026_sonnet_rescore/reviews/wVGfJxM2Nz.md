## Summary

The paper presents a comparative empirical study arguing that structure-preserving inductive biases (SPD manifold constraints for dissipative systems, symplectic structure for conservative systems) enable smaller models to outperform larger, structure-naive baselines on out-of-distribution generalization and long-horizon stability. Two use-cases are investigated: Riemannian optimization of a linear state-space model (LSSM) for heat-transfer system identification, and a symplectic Hamiltonian neural network (SHNN) for the 18-dimensional Fermi-Pasta-Ulam-Tsingou (FPUT) system. The methods themselves (RAdam via `geoopt`, SHNN from David & Méhats 2023) are imported directly from prior work; the paper's contribution is the comparative demonstration and geometric framing.

---

## Strengths

- **Conservative case: compelling quantitative evidence for the size-vs-structure tradeoff.** Table 2 and Figure 3 show that a 1,441-parameter SHNN achieves roll-out MSE ~8.9×10⁻⁹ and drift RMS ~1.3×10⁻³, while the best LSTM (97,074 parameters, 67× larger) reaches roll-out MSE ~1.7×10⁻⁶ and drift RMS ~5.9. This 2–3 order-of-magnitude advantage in stability metrics at a fraction of the parameter count is the paper's single most convincing piece of evidence and directly supports the stated thesis.

- **Clear geometric grounding connecting physics to the learning problem.** Section 2.1.1 rigorously explains why Φ_A = e^{Aτ} lands on the SPD manifold Sym⁺_n when A is stable, making Riemannian gradient updates geometrically interpretable. Section 2.2 derives the symplectic two-form and uses Figure 2 to visualize how energy drift corresponds to trajectories crossing Hamiltonian level sets — this is pedagogically effective and makes the inductive biases interpretable rather than ad hoc.

- **Effective visual argument for phase-space stability.** Figures 4a–4c directly juxtapose a 1,441-parameter SHNN trajectory staying on the correct energy level set against a 97,074-parameter LSTM trajectory drifting across level sets, making the abstract claim about geometric structure tangible and immediately convincing for the conservative case.

- **Systematic model-size sweep for the conservative use-case.** Table 2 covers 16 SHNN and 16 NeuralODE configurations across L ∈ {1,2,4,8} and W ∈ {18,36,72,144}, revealing that increasing size improves one-step accuracy across all models but fails to cure rollout instability or energy drift for structure-naive models — a non-trivial and informative finding.

---

## Weaknesses

### Fatal
None. The core quantitative finding in the conservative case (Table 2) is not invalidated by the issues below.

### Major

- **Dissipative experiment confounds three distinct factors, making it impossible to attribute results to Riemannian optimization specifically.** The main dissipative comparison pits LSSM variants against RF, XGBoost, and LSTM, but these differ simultaneously in (a) model class (LSSM matches the true system exactly; the true system *is* a 2D LSSM), (b) initialization (Table 3 shows the LSSM starts from a physics-derived A matrix already close to the truth), and (c) optimization geometry (RieOpt vs. EucOpt). The only controlled comparison between these factors is RieOpt vs. EucOpt. But looking at Table 1, EucOpt (Chicago T_ext1: 3.35e+00) already beats RF (2.41e+01) and XGBoost (2.23e+01) by an order of magnitude — without any Riemannian constraint. This means the LSSM model class and its physics initialization account for most of the OOD advantage, not the SPD constraint. Meanwhile, on in-distribution London T_ext2, XGBoost (1.06e-01) outperforms RieOpt (5.07e-01). The paper's Section 3.1.1 attributes Chicago OOD generalization to "structure-aware" modeling, but the real driver is that the LSSM is the correct model class for this system. The Riemannian vs. Euclidean margin (RieOpt vs. EucOpt) is real but moderate, and the far larger RF/LSTM gap is model-class driven, not optimization-geometry driven. The dissipative case does not cleanly demonstrate the claimed benefit of Riemannian SPD optimization.

- **Missing ablation isolating symplecticity from ODE architecture in the conservative case.** The SHNN's advantage over LSTM conflates at least three factors: (a) continuous-time ODE formulation (vs. discrete-time RNN), (b) symplectic integrator (implicit midpoint rule), and (c) Hamiltonian parameterization. ODE-structured models are known to generalize better in physical simulation even without symplectic structure. The paper compares SHNN against a standard NeuralODE (which has the ODE structure but not the Hamiltonian/symplectic constraint) and against LSTM (which lacks both). However, a NeuralODE with a symplectic integrator but without the Hamiltonian parameterization would isolate whether the Hamiltonian parameterization itself is doing work beyond what the integrator provides. Without this ablation, the claim that "symplectic structure is the key driver" is only partially established by the SHNN vs. NeuralODE comparison.

### Minor

- **NeuralODE baseline shows three-orders-of-magnitude variance across configurations, acknowledged only briefly.** Table 2 reveals drift_RMS values ranging from ~1.194 (L=2, W=144) to ~1.802×10³ (L=2, W=36) for NeuralODE — a factor of ~1500. Section 3.2.1 notes "NeuralODEs vary widely" without further discussion. Given this instability, the bolded "best" NeuralODE in Table 2 may reflect favorable initialization rather than a representative best. At minimum, reporting results over multiple seeds for NeuralODE would clarify whether the variance is architectural or stochastic.

- **OOD quantitative results for the conservative case are visualization-only.** Figures 4b and 4c show SHNN and LSTM rollouts from perturbed unseen initial conditions, but no MSE or drift numbers are reported for these conditions. The paper's core thesis concerns OOD generalization, yet the most direct OOD evidence for the conservative case is presented only visually, making it impossible to assess the magnitude of the advantage quantitatively.

- **Training convergence claim (Section 3.1.1) lacks quantitative support.** The paper states that structure-naive models "demonstrate significantly slower" convergence, referencing Figures 7 and 8. These figures are not included in the main body and no epoch counts, convergence curves (in the text), or numerical comparisons are provided to substantiate "significantly." This claim should either be quantified or softened.

### Trivial

- **Equation 7 notation inconsistency.** The loss function in Eq. 7 is written as "Φ_A T_i + Φ_B T_i" but Eq. 4 defines the model as Φ_A T_t + Φ_B U_t — the second term should use U_i (input) not T_i (state).

---

## Nice-to-Haves

- Plotting Φ_A eigenvalue trajectories during optimization for both RieOpt and EucOpt would directly demonstrate that the SPD constraint actively prevents instability, rather than just reporting final MSE differences.
- Adding error bars (multiple seeds) for the NeuralODE and LSTM configurations would strengthen the credibility of Table 2.
- A tabulated version of the OOD initial-condition results from Figures 4b/4c would directly support the OOD generalization claim for the conservative case.
- A NeuralODE with a symplectic integrator (but no Hamiltonian parameterization) as an additional baseline would complete the ablation and allow cleaner attribution of the SHNN advantage.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — SPD data generation favoring SHNN:** The critic notes that leapfrog-generated training data is "approximately symplectic by construction, which naturally favors a model that enforces symplecticity." This is not a flaw — physical systems *are* symplectic, and demonstrating that a model exploiting this structure wins is precisely the paper's point. Removed as it mischaracterizes the experimental setup.

- **Harsh Critic — Abstract over-compresses distinction between use-cases:** The critic argues the unified framing is misleading because SPD and symplectic structure are different. The paper's Section 2 explicitly discusses this distinction, and the unifying thread (geometric inductive biases enabling smaller models) is coherent enough. This is scope creep rather than a real flaw.

- **Harsh Critic — PINNs framed as contrast but not used as baselines:** The introduction discusses PINNs as the main prior work, but baselines are RF/XGBoost/LSTM/NeuralODE. This is a reasonable framing choice (PINNs are contextual motivation, not the competing approach), not a methodological error.

- **Strength Finder — "Rigorous experimental design":** The dissipative experimental design has the confounding issues described above, so this strength cannot be retained without qualification. Dropped in favor of the more accurate characterization above.

---

## Novel Insights

Beyond the paper's own stated contributions, the harsh critic's review surfaces one genuinely useful methodological observation: the RieOpt vs. EucOpt ablation in the dissipative case is actually the paper's cleanest controlled comparison, and expanding it (e.g., showing Φ_A eigenvalue trajectories for both methods, documenting how often EucOpt escapes the SPD region) would convert a table entry into a mechanistic demonstration. The energy drift visualization (Figure 4) is already the paper's strongest asset; applying the same idiom to the dissipative case — showing whether EucOpt's iterates leave the SPD manifold — would create a visually unified argument across both use-cases.

---

## Suggestions

1. **Reframe the dissipative case conclusion.** Acknowledge explicitly that the RF/XGBoost/LSTM vs. LSSM gap reflects model-class mismatch, not Riemannian optimization. Reposition RieOpt vs. EucOpt as the key finding, and quantify how much the SPD constraint contributes (e.g., rate of eigenvalue constraint violations for EucOpt).

2. **Add a symplectic-integrator NeuralODE baseline.** This single addition would substantially strengthen the paper's attribution of SHNN's advantage to the Hamiltonian/symplectic structure rather than the ODE architecture alone.

3. **Report multi-seed statistics for NeuralODE.** Given the three-orders-of-magnitude drift variance, at least 3–5 seeds per configuration would make Table 2 statistically credible.

4. **Add a quantitative OOD table for the conservative case.** Even a small table reporting rollout MSE and drift_RMS for the unseen initial conditions in Figures 4b/4c would directly substantiate the OOD generalization claim that is central to the paper's thesis.

---

## Evaluation on Key Axes

**Originality:** Low. Both methods (RAdam/geoopt for SPD optimization, SHNN from David & Méhats 2023) are existing; the contribution is a comparative demonstration. The geometric framing is clear but not novel.

**Importance of research question:** High. Understanding whether geometric inductive biases reduce model-size requirements is a practically and theoretically important question for physics-informed ML.

**Claims supported by evidence:** Partially. The conservative-case claim (symplectic structure → smaller, more stable model) is well-supported by Table 2 and Figures 3–4. The dissipative-case claim (Riemannian optimization → OOD stability) is confounded and only partially supported.

**Soundness of experiments:** Moderate. The conservative experiment is systematic and the metrics are appropriate. The dissipative experiment has confounding issues that weaken attribution. Neither experiment reports confidence intervals.

**Clarity of writing:** Good overall. Geometric intuition is well-developed; the connection between Φ_A = e^{Aτ} and SPD is clearly explained.

**Value to research community:** Moderate. The paper provides a clear tutorial-style demonstration of geometric ML for dynamics, but falls short of establishing definitive new empirical findings due to experimental design gaps.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>