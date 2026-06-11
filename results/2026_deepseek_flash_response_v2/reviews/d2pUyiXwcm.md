## Summary

This paper proposes SCaSML, a hybrid framework that combines pre-trained surrogate models (PINNs, GPs) with Multilevel Picard (MLP) Monte Carlo simulation to correct surrogate errors at inference time without retraining. The core idea is to derive a "Structural-preserving Law of Defect" — a PDE describing the surrogate's error that preserves the semi-linear structure of the original problem — and solve it via MLP. The authors prove a product-form error bound with an improved convergence rate and demonstrate empirical results on PDEs up to 160 dimensions.

## Strengths

1. **Product-form error bound (Theorem 2.5) providing genuine convergence acceleration.** The global L² error bound is multiplicative: ‖Ũ_{N,M} − ũ‖ ≤ E(M,N) · (C_F e(ũ)). This yields an improved scaling law O(m^{−γ−1/2}) versus O(m^{−γ}) for the surrogate alone or O(m^{−1/2}) for naive MLP — a non-trivial theoretical contribution that goes beyond additive error bounds in prior hybrid methods.

2. **Structural-preserving Law of Defect (Fact 2.3) enables direct application of high-dimensional Monte Carlo solvers.** The derivation shows the defect PDE retains the semi-linear parabolic structure of the original equation, allowing established Feynman–Kac-based solvers (MLP) to be used without modification. This cleanly differentiates the approach from classical defect-correction designed for grid-based discretizations.

3. **Empirical demonstration across diverse high-dimensional PDEs up to 160 dimensions.** The experiments span linear convection-diffusion (10–60d), viscous Burgers (20–80d) with two surrogate types (PINN, GP), HJB/LQG (100–160d), and diffusion-reaction (100–160d). SCaSML consistently achieves the lowest errors across nearly all configurations.

4. **Principled rationale for Monte Carlo as the correction method.** The spectral bias argument (Section 2.1) — that neural surrogates learn low frequencies first, making the residual high-frequency, while Monte Carlo's convergence is independent of smoothness — provides concrete reasoning that goes beyond generic "hybrid" claims.

## Weaknesses

### Major

1. **The experimental comparison uses asymmetric clipping thresholds and an undertuned MLP baseline.** In three of four problem families (VB, HJB/LQG, DR), SCaSML and the naive MLP use different clipping thresholds (e.g., VB: MLP clips at 1.0, SCaSML at 0.01; HJB: MLP at 10, SCaSML at 0.1; DR: MLP at 10, SCaSML at 0.01). Only LCD uses the same threshold for both (lines 234, 242, 250, 296). Since clipping is a well-known variance stabilization technique with strong effects on Monte Carlo estimators, the asymmetric treatment makes it impossible to tell whether SCaSML's advantage stems from its method or from a more favorable clipping setup. Additionally, the naive MLP uses a minimal configuration (N=2 levels, M=10 base samples) across all problems, producing pathological 500%+ errors on the LQG problem (Table 1: 5.27–5.63 relative L²). Presenting this as "pure simulation often fails" (line 224) while SCaSML succeeds is misleading — the results show an undertuned MLP fails, not that pure simulation fundamentally cannot work at similar cost.

2. **The convergence analysis rests on an unverified assumption (Assumption 2.4) linking residual error to function error.** The core theoretical claim (improved convergence rate from O(m^{−γ}) to O(m^{−γ−1/2}), Corollary 2.6) depends on Assumption 2.4, which asserts that the PDE residual ε and W^{1,∞} error of the defect both scale like the surrogate error e(û) via constants C_{F,1} and C_{F,2}. However, ε involves first and second-order derivatives of the surrogate (Equation 6), and it is well-known that neural networks can have much larger derivative errors than function errors — especially for the Laplacian. The paper provides no justification, bound, or direct empirical validation that this assumption holds for neural surrogates. While assumptions in theoretical analysis are standard, this one is central to the claimed acceleration and should be justified more carefully. The empirical scaling law verification (Figure 4) provides indirect support but does not directly validate the assumption.

3. **Headline claims exceed what the reported data support.** The abstract states SCaSML "reduces the error of various surrogate models... by 20-80%." The maximum reduction in Table 1 is ~66% (VB-PINN 20d), not 80%. Several configurations fall below the 20% lower bound (VB-PINN 80d: ~16%; DR: 7–11%; LQG: 12–31%). The "up to 80%" figure in the conclusion (line 328) is also unsupported. The computational overhead is substantial (SCaSML is 5–235× slower than the surrogate alone, and 1.3–12× slower than naive MLP) but is not mentioned in the abstract. These claims should be calibrated to match the data.

### Minor

1. **No variance estimates or error bars for Monte Carlo results in the main paper.** Table 1 and Figure 3 report only point estimates. For a Monte Carlo method where variance is the primary concern, the absence of any uncertainty quantification is a notable omission. The paper defers statistical significance (p ≪ 0.001) to the appendix, but standard errors or confidence intervals should appear in the main paper.

2. **The computational cost-benefit analysis is missing.** SCaSML is consistently slower than both the surrogate and the naive MLP, often by 1–2 orders of magnitude relative to the surrogate alone. For the DR problem, the error reduction is only 7–11% while runtime increases by 183–235×. The paper frames this as "elastic compute" (lines 33, 103, 328) but provides no Pareto or cost-benefit analysis to help practitioners assess the trade-off.

### Trivial

None.

## Nice-to-Haves

- An ablation study isolating the effect of clipping thresholds would clarify whether SCaSML's advantage persists under matched clipping.
- A Pareto-front analysis (accuracy vs. total compute cost) would better substantiate the "elastic compute" framing.
- Empirical validation of Assumption 2.4 (e.g., plotting ‖ε‖ vs. e(û) across training sizes) would strengthen the theoretical claims.

## Removed Points

- **"The LLM inference-time scaling analogy is substantively shallow":** Removed — this is a subjective opinion about framing, not a technical weakness. The analogy is clear and consistent with the paper's message.
- **"The product error bound is 'not a product in the usual sense'":** Removed — the bound is literally multiplicative. This misinterprets the paper.
- **"The LCD PINN may be undertrained (speculative)":** Removed — while the large errors on a linear problem are noteworthy, declaring undertraining without running controlled experiments is speculative.
- **"Reference solution for HJB may be noisy":** Removed — the paper states it uses "sufficiently large sample sizes (e.g., 100d)." Speculating about noise without evidence is not a valid criticism.
- **All missing appendix / missing related works / missing proofs criticisms:** Removed per meta-instructions — the parser strips appendices from all papers; missing citations cannot be confirmed as absent without external knowledge.

## Novel Insights

None beyond the paper's own contributions. The reviews did not uncover any perspective that the paper itself does not articulate.

## Suggestions

1. Fix the headline claims to match the data: state "up to 66%" instead of "up to 80%," and qualify the computational overhead in the abstract.
2. Run the naive MLP baseline with a properly configured setting (more levels, optimal sample allocation) under identical clipping conditions as SCaSML, and report results transparently.
3. Include standard errors or confidence intervals on all main results (Table 1, Figure 3, Figure 4).
4. Either provide a theoretical justification for Assumption 2.4 in the context of neural-network surrogates, or include an empirical study validating it.

---

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing):** Searched for physics-informed PDE papers across three score bands.
- Weak band (<3.5): Papers like "Hybrid Numerical PINNs" (3.33), "EPINN" (2.50), "trSQP-PINN" (3.00). These are basic PINN papers with limited theory and experiments. SCaSML is clearly stronger.
- Middle band (3.5–7.5): Papers like HyResPINNs (5.00), PPI-NO (4.33), "Connecting Solutions" (5.25). SCaSML has stronger theoretical contributions and more extensive experiments.
- Strong band (>7.5): "Oscillatory State-Space Models" (8.00) — not topically similar.

**Round 2 (Narrowing):** Searched with more specific hybrid/Monte Carlo/PDE terms for two bands below and above 6.0.
- Lower band (<6.0): HyPER (5.00, Accept), Automatic Neural Spatial Integration (4.00, Reject). SCaSML is stronger than both due to genuine theoretical novelty and higher-dimensional experiments.
- Upper band (6.0–11): SINGER (6.33, Accept), Active Learning for PDE Solvers (7.00, Accept), Progressively Refined Differentiable Physics (6.50, Accept). SINGER (6.33) is the most comparable — a high-dimensional PDE solver with theory — but SCaSML has more serious experimental fairness issues (asymmetric clipping vs. SINGER's merely oversold semigroup property).

**Anchors read in full:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| HyResPINNs | 5.00 (Reject) | R1 | Stronger theory, more experiments → SCaSML better |
| PPI-NO | 4.33 (Reject) | R1 | Stronger theory, cleaner method → SCaSML better |
| Connecting Solutions | 5.25 (Reject) | R1 | Comparable scope, SCaSML has more novel theory |
| HyPER | 5.00 (Accept) | R2 | SCaSML has better theory, more PDE families, higher dims |
| Auto Neural Spatial Integration | 4.00 (Reject) | R2 | SCaSML clearly stronger in both theory and experiments |
| SINGER | 6.33 (Accept) | R2 | SCaSML goes to higher dims (160 vs 20) but has more severe experimental fairness issues |

**Final calibration:** SCaSML is stronger than the 5.0 anchors (HyPER, HyResPINNs) due to genuine theoretical novelty and broader experiments, but weaker than the 6.33 anchor (SINGER) because the experimental fairness issues — asymmetric clipping and an undertuned baseline — undermine confidence in the core empirical comparisons. The inflated claims further reduce trust. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>