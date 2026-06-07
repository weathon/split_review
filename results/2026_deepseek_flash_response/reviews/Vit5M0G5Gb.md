## Summary

This paper proposes a theoretical framework for understanding saddle-to-saddle (stage-like) learning dynamics across neural network architectures. It presents two rigorous static-landscape results — embedded fixed points (Theorem 1) and invariant manifolds (Theorem 3) — that hold for a broad class of architectures covering fully-connected, convolutional, and attention-based networks. It then develops heuristic dynamical arguments showing how timescale separation — either data-driven (singular-value gaps in linear networks, Theorem 4) or initialization-driven (distinct unit growth rates in quadratic/self-attention networks, Proposition 5) — steers gradient flow through these saddles along invariant manifolds. Experimental validation in Figure 2 confirms the predicted effects of width, data spectrum, and initialization on plateau dynamics.

## Strengths

- **Clean generalization of embedded fixed points to modern architectures.** Theorem 1 extends the Fukumizu & Amari (2000) fixed-point hierarchy by adding two new construction types (Equations 6 and 7) for homogeneous and linear-additive activations, and by explicitly mapping them to convolutional and self-attention architectures. The paper shows concretely that each saddle visited during learning in Figure 1B–G falls into one of these categories.

- **Identification and formalization of two distinct timescale separation mechanisms.** The paper disentangles data-driven separation (between singular-vector directions, Theorem 4) from initialization-driven separation (between units, Proposition 5), showing they lead to different weight structures — low-rank weights versus sparse weights. This is validated by Figure 2B where equalizing singular values (κ=0) eliminates plateaus in linear networks but not in linear self-attention, exactly as the theory predicts.

- **Testable predictions empirically confirmed.** Section 6 derives and validates non-obvious predictions about width (Figure 2A: increasing width does not speed up linear networks but does shorten plateaus in self-attention), data spectrum (Figure 2B: power-law exponent controls plateau length), and initialization structure (Figure 2C: large low-rank initialization near invariant manifolds produces a previously unobserved regime with exponential drop then plateaus). These predictions are concrete, falsifiable, and correctly borne out.

- **Explicit conditions delimiting when saddle-to-saddle dynamics occurs.** Section 7 provides two clear necessary conditions (escape path must follow invariant manifolds; initialization must be near an invariant manifold with fewer effective units) and uses them to explain counterexamples (tanh networks violate condition (i); large isotropic initialization violates condition (ii)). This gives the theory falsifiable scope rather than claiming universality.

## Weaknesses

### Major

- **Central dynamical claim rests on heuristic/approximate analysis, not rigorous proof.** The paper's strongest claim — that saddle-to-saddle dynamics *explains* simplicity bias — depends on the dynamical analysis in Section 5, which is explicitly heuristic (line 119: "we develop **heuristic arguments**"). Theorem 4 analyzes a linearized system (Equation 10) rather than the full gradient flow (Equation 9); the paper states the latter is "approximately" captured but provides no formal error bound on the approximation. Proposition 5 for the quadratic case relies on a scalar ODE analogy (v̇ = v², Equation 15) that strips away unit coupling and the role of the data matrix. The abstract and introduction do not hedge accordingly — they present the dynamical mechanism as established fact ("shows that saddle-to-saddle dynamics operates by…") rather than as a plausible account supported by heuristic analysis and simulation. The gap between the rigorous static results (Theorems 1 and 3, which are genuinely general) and the approximate dynamical claims means the paper provides a *plausible mechanism* with *compelling circumstantial evidence*, not a proven dynamical account.

- **Scope of dynamical analysis does not match the title/abstract framing.** The title and abstract promise a framework that "explains a simplicity bias across neural network architectures," but the dynamical analysis in Section 5 covers only two-layer networks where φ is a homogeneous polynomial in the weights (linear and quadratic cases). This covers linear networks, quadratic networks, and linear self-attention, but does *not* cover: ReLU networks (shown in Figure 1D–E but analyzed only qualitatively), general nonlinear activations (tanh, etc.), or deep networks. The paper acknowledges this in the Discussion (line 228), but the framing mismatch between the bold claims ("universal mechanism," "across architectures") and what is actually analyzed is a significant issue.

### Minor

- **The quadratic case analysis is notably weaker than the linear case.** Proposition 5's proof sketch (lines 178–186) reduces the coupled vector-valued dynamics to a scalar ODE v̇ = v². The claim that "the rest of the units is O(ε) almost surely" (line 177) is asserted rather than rigorously derived from the full coupled system in Equation (14). While the scalar analogy gives intuition, the actual dynamics couples v_i and u_i through Σ_yZ, and it is not made clear when this coupling can be ignored.

- **Experiments lack error bars or multiple-run statistics.** The simulations in Figure 2 show single loss curves without variability across random seeds. Given that the quadratic case's dynamics depend on random initialization (Proposition 5), and that the plateau shortening claims are quantitative, showing error bars or multiple runs would materially strengthen confidence that the observed effects are systematic rather than coincidental.

### Trivial

- Line 99 contains a panel reference error: "(E,F)" should be "(F,G)" — panel (E) is ReLU convolutional (Equation 6 case), not Equation (5).

## Nice-to-Haves

- A formal error bound on the approximation gap between the linearized system (Equation 10) and the full gradient flow (Equation 9) for the linear case would substantially raise the evidentiary bar.
- A brief discussion connecting the paper's "effective width" notion of simplicity to prior spectral/Fourier-based simplicity bias definitions (Rahaman et al., Kalimeris et al.) would help situate the contribution.

## Removed Points

- **Harsh Critic's Issue #3 (novelty relative to Fukumizu & Amari):** Removed. The paper handles this properly in Remark 1, clearly attributing Equations (4)–(5) to prior work and claiming Equations (6)–(7) as extensions. The contribution is in synthesis across modern architectures and the dynamical connection, not in claiming the fixed-point observations are entirely new.
- **Harsh Critic's claim about line 99 panel ordering:** Removed from weaknesses; demoted to Trivial (textual error, does not affect the science).
- **Harsh Critic's concern about quadratic networks not being re-introduced in Section 5.2:** Removed; minor presentation point with no substance.
- **Various formatting, reproducibility nitpicks about undisclosed hyperparameters, missing appendix material:** All removed per guidelines (parser artifacts or non-issues).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension between the paper's bold framing and the heuristic nature of its dynamical analysis, which the authors themselves acknowledge in the Discussion. This gap is not a novel observation — it follows directly from reading the paper carefully.

## Suggestions

1. **Recalibrate the framing** in the abstract and introduction to accurately reflect what is proven (static landscape: Theorems 1 and 3) versus what is argued heuristically with supporting simulations (dynamical mechanism). For example, replace "explains a simplicity bias" with "provides a framework for understanding simplicity bias" and qualify the "across architectures" claim to note that the full dynamical mechanism is rigorously demonstrated for homogeneous polynomial activations.

2. **Strengthen the quadratic case analysis** by either (a) providing a more rigorous treatment of the coupled dynamics in Equation (14) beyond the scalar analogy, or (b) explicitly stating the additional assumptions needed to decouple the units and providing a formal bound on the approximation error. Even a mild improvement (e.g., showing the key conclusion holds under more general conditions on Σ_yZ) would substantially raise the paper's evidentiary bar.

3. **Add error bars or confidence bands** to the experimental curves in Figure 2 — at minimum for the key quantitative claims (plateau length vs. width in Figure 2A, plateau length vs. κ in Figure 2B).

## Score and Decision

**Initial bracket (Round 1):**  The low-band anchors (avg 2.00–3.40) were papers with much less technical substance or purely critical/opinion pieces — our paper is clearly stronger. The high-band anchors (avg 7.60–8.00) were papers with fully rigorous theoretical analyses — our paper's dynamical analysis is less rigorous. This bracketed the paper between approximately 4.5 and 7.0.

**Narrowing (Round 2):** Within the bracket, the paper was compared against:
- J4Dvxv7WnG (7.00, accepted, deep linear EOS): more rigorous dynamics, narrower scope → our paper is weaker.
- PvJnX3dwsD (6.40, accepted, quadratic models/catapult): similar mix of theory + heuristics, comparable.
- wFD16gwpze (7.33, accepted, scaling laws): more rigorous analytical derivations → our paper is weaker.
- QgwAYFrh9t (5.75, accepted, hierarchical polynomials): narrower, more tailored architecture → our paper is comparable or slightly stronger.
- 381QSrWdF2 (5.50, rejected, SGD balance): limited model, questioned generalizability → our paper is clearly stronger.
- s1zO0YBEF8 (6.50, accepted, compositional generalization): focused delivery matching claims → our paper is weaker in claim-evidence alignment.

**Final score:** 6.0. The paper has genuine contributions — the static landscape framework (Theorems 1 and 3) is clean and broadly applicable, the identification of two distinct timescale separation mechanisms is insightful, and the experimental predictions are validated. However, the central dynamical claim is supported by heuristic analysis rather than rigorous proof, and the scope of actual dynamical analysis (two-layer, homogeneous polynomial activations) is narrower than the title and abstract suggest. These weaknesses are substantial but not fatal — the paper would benefit from recalibrated framing rather than additional results.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>