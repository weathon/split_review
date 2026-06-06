## Summary

SCaSML (Simulation-Calibrated Scientific Machine Learning) is a framework that improves pre-trained PDE solvers at inference time without retraining. The core idea is a "Structural-preserving Law of Defect": for a semi-linear parabolic PDE, the error of any surrogate model itself satisfies a semi-linear parabolic PDE of the same structural form (Fact 2.3), enabling Multilevel Picard (MLP) stochastic simulation to correct the surrogate's output. A key theoretical result (Theorem 2.5) shows the final error is bounded by the *product* of the surrogate error and the simulation error, formally yielding a faster convergence rate. Experiments across five high-dimensional PDEs (up to d=160) show consistent 20–80% L² error reductions over base surrogates (PINN and GP), with especially dramatic improvements when standalone MLP fails entirely.

---

## Strengths

- **Novel structural-preservation insight (Fact 2.3):** The paper proves that the defect $\tilde{u} = u - \hat{u}$ satisfies a semi-linear parabolic PDE with the exact same structure as the original problem, complete with a modified nonlinear term $\tilde{F}$. This is not obvious and is the key enabling insight for the entire framework—it means efficient branching Monte Carlo solvers (MLP) can be applied to the defect without reformulation.

- **Product-error theoretical guarantee (Theorem 2.5):** The bound $\|\tilde{U}_{N,M} - \tilde{u}\|_{L^2} \leq E(M,N) \cdot C_F \cdot e(\tilde{u})$ concretely characterizes the synergy between surrogate accuracy and simulation fidelity. This directly implies a reduction in required compute to reach a target accuracy from $O(d\varepsilon^{-(2+\delta)})$ for naive MLP to $O(d\varepsilon^{-(2+\delta)} e(\tilde{u})^{2+\delta})$ for SCaSML (Corollary E.9).

- **Compelling high-dimensional experiments, especially LOG/LQG (Table 1):** In the LQG control problem at d=100–160, standalone MLP produces relative L² errors of 5.27–5.63 (far exceeding 1.0, worse than predicting zero), while SCaSML achieves 0.055–0.099—a reduction of 11.7% to 30.8% over the PINN surrogate. This demonstrates that SCaSML solves a fundamentally different problem than "just spending more compute," since more MLP compute alone produces catastrophic results.

- **Empirical confirmation of faster scaling (Figure 4):** Log-log plots comparing GP surrogate and SCaSML across d=20–80 consistently show a steeper slope for SCaSML, directly supporting the theoretical claim that the convergence rate exponent improves beyond $-\gamma$.

- **Plug-and-play with heterogeneous surrogates:** The Viscous Burgers results (VP-PINN and VP-GP rows, Table 1) demonstrate 16–58% L² error reductions using both PINN and GP surrogates without any modification to the correction procedure, confirming broad applicability.

- **Comprehensive validation across diverse PDEs:** Five distinct semi-linear parabolic PDEs—linear convection-diffusion (d=10–60), viscous Burgers (d=20–80), LQG HJB control (d=100–160), and diffusion-reaction (d=100–160)—with statistical significance $p \ll 0.001$ (Appendix G.4) provide strong evidence for generalizability.

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistency between informal and formal convergence rate claims:** Throughout Sections 2.1 and 2.4, the paper repeatedly and informally asserts that SCaSML achieves a convergence rate of $O(m^{-\gamma - 1/2})$. However, Corollary 2.6—the formal theorem—states the rate as $O(m^{-\gamma - 1/2 + \alpha(1)})$, where $\alpha(1)$ is not defined, bounded, or interpreted anywhere in the main body. If $\alpha(1) \geq 1/2$, the corollary does not actually establish a rate improvement over the base surrogate. The Figure 4 empirical slopes are consistent with an improvement, but the formal statement remains ambiguous. The informal text in Section 2.1 ("the final statistical error becomes $m^{-\gamma-1/2}$") and Section 2.4 ("SCaSML therefore attains a convergence rate that surpasses…") set up an expectation that the formal result does not unambiguously fulfill. This should be resolved—either bound $\alpha(1)$ explicitly in the main text or qualify the informal claims to match the formal statement.

- **Fixed-budget comparison is deferred to an appendix despite being central to the paper's practical claim:** The paper claims "elastic compute" benefits and "inference-time scaling," but the primary evidence for this framing—that SCaSML outperforms baselines *given a fixed total computational budget* (train + inference)—appears only in Appendix G.7. In Table 1, SCaSML consistently uses 2–100× more wall-clock time than the surrogate alone (e.g., LCD 10d: 0.45s surrogate → 13.31s SCaSML). The natural question—could one achieve the same SCaSML accuracy by simply training the surrogate longer or running standalone MLP with more samples for the same total time?—is the crucial comparison that distinguishes the method from plain compute scaling. For LOG/LQG, where standalone MLP catastrophically fails, this comparison is less critical; but for LCD, VB-PINN, and DR, it is the central empirical argument. At minimum, the key finding from Appendix G.7 should appear in the main text.

### Minor

- **Abstract slightly overclaims the typical improvement range:** The abstract states SCaSML reduces error "by 20-80%." This accurately characterizes most experiments, but the Diffusion-Reaction results—which the paper itself explicitly reports as "6.6% to 10.9%"—fall well below 20%. A more accurate characterization would be "up to 80% in most settings and 6–11% in already-accurate surrogate settings."

- **Assumption 2.4 requires $W^{1,\infty}$ error control with no discussion of its plausibility for PINNs:** Assumption 2.4 requires both $L^\infty$ residual control and $W^{1,\infty}$ error control on the defect. For PINN surrogates—which dominate the experiments—convergence guarantees typically hold in weaker integral norms. The paper applies SCaSML to PINNs trained for $10^4$ iterations on 60–160d problems without remarking on whether Assumption 2.4 is realistic or approximate in that setting. A brief remark on this gap would improve the paper's credibility.

- **Differing clipping thresholds between standalone MLP and SCaSML's correction step are not decomposed:** For DR, standalone MLP uses a clipping threshold of 10 while SCaSML uses 0.01; for LQG, 10 vs. 0.1. The paper justifies this by "the smaller magnitude of the defect," which is theoretically coherent. However, the Table 1 comparison between "naive MLP" and SCaSML's correction step conflates the variance reduction from the warm-start and the tighter admissible clipping regime. The contribution of each factor to the observed improvement is not isolated anywhere in the paper.

### Trivial

- **Figure 3b uses different y-axis scales across four subplots without annotation:** The improvement percentage axis ranges from 55–72.5% for VP-GP, 50–65% for VB-PINN, 26–31% for VP-PINN, and 0–10% for LQG—yet all four subplots are presented at similar visual scale. A note on the axis differences would prevent misreading the LQG result as showing similar absolute improvement to the others.

- **Quadrature MLP is introduced in Section 2.3 but not used in experiments without explanation:** The paper introduces two MLP variants and then exclusively uses Full-history MLP in all experiments without explaining why Quadrature MLP is less suitable. A single sentence would suffice.

---

## Nice-to-Haves

- A brief discussion of the regime where SCaSML is *not* expected to help—e.g., when the surrogate is so inaccurate that the defect PDE has a large Lipschitz constant and MLP simulation of the defect itself diverges—would improve the paper's practical guidance. Assumption 2.4 is the formal gate but provides no intuition for when it breaks down.

- For the LOG/LQG case, an explanation of *why* standalone MLP fails catastrophically (likely because $-\|\nabla u\|^2$ has large Lipschitz constant in high dimensions causing MLP variance to explode) would sharpen the contribution narrative considerably and help readers understand which problem structure makes SCaSML most valuable.

- Measuring the empirical convergence rate exponents from Figure 4 (fitting slopes on the log-log plots) and comparing them to the theoretical $\gamma + 1/2 - \alpha(1)$ would directly connect the formal bound to the visual evidence and provide a way to empirically estimate $\alpha(1)$.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The LLM inference-time scaling framing is a loose analogy."** Removed because this is a positioning choice, not a scientific error. The analogy is explicitly framed as illustrative, and the technical substance of the paper does not depend on it.

- **Harsh Critic: "SCaSML is not distinguished from control-variate methods in Monte Carlo PDE literature."** Removed under the rule against missing related works—we cannot confirm specific prior works without external sources.

- **Harsh Critic: "Section 2.1 informal argument skips the derivative term in the variance computation."** Removed as a minor presentation nuance. The $W^{1,\infty}$ term enters formally through Assumption 2.4, and the informal argument is explicitly labeled as intuition-building. The paper is not claiming rigor in that informal section.

- **Strength Finder: "Addresses an important problem."** Removed as generic—importance of high-dimensional PDEs is not a specific strength of this particular paper.

---

## Novel Insights

The paper's most structurally interesting observation—that the surrogate defect satisfies a semi-linear PDE with the *same nonlinear coupling structure* as the original problem—has a non-obvious implication reviewers did not fully surface: the difficulty of solving the defect PDE scales with the surrogate's accuracy, not with the original problem's difficulty. This means the inference-time compute budget for SCaSML can be *much* smaller than for standalone MLP, and the method improves as the surrogate improves rather than facing a fixed computational cost. The LOG/LQG results illustrate the extreme of this: standalone MLP on the full problem requires prohibitive variance control while SCaSML's defect problem (with a good PINN warm start) is tractable. This is a qualitatively different regime than variance reduction by warm-starting, and the paper would benefit from articulating this "difficulty transfer" interpretation more explicitly.

---

## Suggestions

1. Define or bound $\alpha(1)$ in the main text (even as a reference to the appendix result), or replace the informal rate claim $m^{-\gamma-1/2}$ in Sections 2.1 and 2.4 with $m^{-\gamma-1/2+\alpha(1)}$ to match Corollary 2.6 exactly.
2. Promote the core finding of Appendix G.7 (fixed-budget comparison) to the main text—even a single paragraph or figure would substantially strengthen the "inference-time scaling" framing.
3. Qualify the abstract's "20-80%" claim to note the 6-11% improvement range for already-accurate surrogates (DR).
4. Add a brief remark in Section 2.4 on the practical meaning of Assumption 2.4 for PINN surrogates, acknowledging that it may hold approximately rather than exactly.
5. Annotate Figure 3b with the y-axis ranges to prevent visual misreading of the LQG subplot.

---

## Score and Decision

**Originality (4/5):** The defect PDE structural preservation idea (Fact 2.3) and its combination with Multilevel Picard simulation is a novel and elegant contribution. The convergence rate improvement framing is original.

**Importance of Research Question (4/5):** High-dimensional PDEs are genuinely challenging, and a plug-and-play inference-time correction framework that provably improves any pre-trained solver addresses a significant practical gap.

**Claims Supported (3/5):** Empirical support is strong and comprehensive. The theoretical claims are mostly well-supported, but the gap between the informal convergence rate ($m^{-\gamma-1/2}$, stated five or more times) and the formal result ($m^{-\gamma-1/2+\alpha(1)}$, with $\alpha(1)$ undefined in the main text) is a genuine presentation problem that creates potentially misleading impressions. The fixed-budget comparison supporting the core "inference-time scaling" claim is only in the appendix.

**Soundness of Experiments (4/5):** Five diverse PDEs, two surrogate types, dimensions up to 160, statistical significance testing, and scaling law verification constitute a thorough experimental suite. The different clipping thresholds are theoretically justified, though not fully decomposed.

**Clarity of Writing (3/5):** The paper is generally well-written, but the informal/formal convergence claim mismatch and the deferred fixed-budget comparison are notable structural clarity issues for readers trying to evaluate the core contribution.

**Value to Research Community (4/5):** The framework is practical (no retraining, compatible with any surrogate), theoretically grounded, and applicable across a broad class of PDEs. The LOG/LQG results demonstrating success where standalone simulation fails entirely make a compelling case for adoption.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>