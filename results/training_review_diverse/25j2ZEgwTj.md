Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper analyzes the gradient descent training dynamics of a two-layer ReLU network (width \(m\), students) learning a target composed of \(k\) ReLU neurons (teachers) under Gaussian input and squared loss. It extends prior single-teacher analyses (\(k=1\)) to the multi-teacher setting by introducing a three-phase convergence framework (alignment, tangential growth, local convergence) and proving a global convergence rate of \(\mathcal{O}(T^{-3})\). The paper also characterizes an emergent balanced-norm behavior where student neurons converging to the same teacher end up with roughly equal norms.

## Strengths

- **First global convergence proof for multi-teacher (\(k>1\)) ReLU networks with \(\mathcal{O}(T^{-3})\) rate.** Theorem 2 establishes that for any constant number of teachers \(k\) and students \(m\), gradient descent drives the loss to zero at rate \(\mathcal{O}(T^{-3})\). This goes substantially beyond prior work that was limited to \(k=1\) (Xu & Du, 2023) or the exactly-parameterized \(m=k=1\) case (Yehudai & Ohad, 2020).

- **Three-phase dynamical analysis that reveals the learning mechanism.** The paper decomposes training into explicit phases — alignment (Theorem 3), tangential growth (Theorem 4), and local convergence (Theorem 5) — with quantitative bounds for each. This framework (summarized in Table 1) provides concrete understanding of how student neurons first align with teachers, grow in magnitude, and then converge.

- **Dynamical system treatment of tangential coupling among multiple teachers.** In Phase 2, the paper models the evolution of projection deficits \(\mathbf{H}(t)\) via the matrix recursion \(\mathbf{H}(t+1) = \mathbf{A}\mathbf{H}(t) + \mathbf{Q}(t)\) and bounds convergence through eigenvalue analysis. This is the core technical advance needed for the \(k>1\) setting and represents a genuine extension over single-teacher analyses.

- **Emergent balanced-norm behavior.** Corollary 2 and Theorem 5 show that, without any explicit regularizer, gradient descent ensures that student neurons converging to the same teacher end up with approximately equal norms (e.g., \(\|w_i(T_2)\| \in [\|v\|/(3m_{\tau_i}), 3\|v\|/m_{\tau_i}]\)). This non-trivial structural property of the GD solution is a genuine finding.

- **Weaker initialization conditions and relaxed learning rate for the \(k=1\) sub-case.** The paper notes (remarks after Theorems 3 and 4) that its initialization variance condition is weaker than that of Xu & Du (2023), and the Phase 2 learning rate condition is relaxed by a factor of \(m\).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are plausible and the proof strategy is coherent. While several issues merit attention, none individually or collectively invalidate the contribution.

### Minor

- **The "implicit bias" claim is imprecise.** The abstract states that results "reveal an implicit bias toward achieving the minimum balanced \(\ell_2\)-norm in the solution." The paper proves that student neurons converge to approximately balanced norms (constant-factor proximity to equal sharing), but it does **not** formulate or verify an optimization problem whose solution is a minimum-norm interpolator, nor does it connect its balance result to the standard implicit bias literature (e.g., Chizat & Bach 2020; Lyu & Li 2020) in a formal way. The balance result itself is interesting and well-supported; the paper would be stronger if it either established the minimality property or softened the "implicit bias" framing to simply "balanced norm property."

- **Experiments are too thin to provide meaningful quantitative validation.** The numerical section (Section 5) uses a single random seed, a single initialization variance and learning rate, no error bars, and no baseline comparisons. The reference line \(\overline{17}/T^3\) is presented without justification for the chosen constant. The phase boundaries are acknowledged as "not very clear." For a theory paper, experiments are supplementary rather than evidential, so this does not undermine the theoretical contribution. However, the current experiments are too minimal to convincingly confirm the predicted \(\mathcal{O}(T^{-3})\) scaling or the phase transition timescales in a quantitative way. Adding error bars over multiple seeds and empirically verifying the predicted phase durations would significantly strengthen the paper.

- **The exponent 0.05 in Corollary 2's loss bound is unusual and unexplained.** The bound \(L(W(T_2)) \leq \frac{1}{2}k^2 \epsilon_2^{0.05} \|v\|^2\) features an exponent 0.05 that appears to be an artifact of loose bounding rather than a natural parameter. The authors should clarify how this exponent arises from the proof (a brief comment in the main text or a reference to the relevant appendix step would suffice). This does not affect the validity of the \(\mathcal{O}(T^{-3})\) rate in Phase 3, but it is a presentation gap.

- **The combination of assumptions is quite restrictive.** Assumption 1 (weak recovery), Assumption 2 (orthogonal equal-norm teachers), and Assumption 3 (balanced initialization at the partition level) together constrain the setting considerably. The paper acknowledges these limitations (Section 6 notes weak recovery as a drawback), and orthogonal-teacher assumptions are common in this literature (Zhou et al., 2021; Oko et al., 2024). Nevertheless, the gap between these assumptions and a truly "general" setting should be discussed more prominently, and the paper would benefit from a discussion of which assumptions are likely to be relaxable versus genuinely structural.

### Trivial

- The condition \(\sigma = o(\operatorname{poly}(m^{-k^2}, d^{-1/2}))\) in Theorem 2 is cryptic — "poly in what?" It should be concretely bounded (e.g., \(\sigma \leq c \cdot m^{-C k^2} d^{-1/2}\) for explicit constants \(c, C\)).

## Nice-to-Haves

- An explicit statement of the transition matrix \(\mathbf{A}\) and its eigenvalues in the main text would make the Phase 2 proof sketch more transparent and increase reader confidence. (The full derivation presumably appears in the appendix, which was stripped by the parser.)
- The paper could discuss how the results might extend to finite-sample (non-population) training, or at least note that the current analysis is in the population-loss setting.
- A brief discussion of what new technique enables the \(k>1\) extension beyond "handling interactions" — specifically, how the dynamical-system approach differs from the scalar analysis in Xu & Du (2023) — would help readers appreciate the technical advance.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Criticism that Phase 2 proof is "underspecified" / a "structural issue":** The main text provides a proof sketch (the matrix recursion \(\mathbf{H}(t+1)=\mathbf{A}\mathbf{H}(t)+\mathbf{Q}(t)\), eigenvalue analysis of \(\mathbf{A}\), bounds on \(\mathbf{Q}(t)\)). This is standard for a conference theory paper; full proof details reside in the appendix (which the parser strips). The claim that this is a "structural issue" preventing verification is unwarranted.

- **Criticism that experiments are too weak to "support the theoretical claims":** For a theory paper, experiments are illustrative, not evidential. The demand for error bars, baseline comparisons, and quantitative rate fitting applies the wrong standard.

- **Several generic/formatting nitpicks** about missing derivation details, comparison presentation, etc.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface any genuinely novel insight that the paper itself does not already articulate. The key observation — that extending from \(k=1\) to \(k>1\) requires modeling teacher–teacher interactions via a coupled dynamical system — is clearly stated in the paper.

## Suggestions

1. **Soften the "implicit bias" framing.** Either prove that the balanced configuration minimizes \(\sum_i \|w_i\|^2\) among interpolators (the natural candidate), or replace "implicit bias toward the minimum balanced \(\ell_2\)-norm" with "emergent balanced-norm property" or similar language that accurately reflects what is proved.
2. **Add basic experimental rigor.** Repeat each setting with at least 3–5 random seeds with error bars, and empirically verify that the loss slope matches \(\mathcal{O}(T^{-3})\) by fitting a power law rather than using an ad-hoc reference line.
3. **Clarify the 0.05 exponent** in the Phase 2 loss bound — briefly explain how it arises from the proof.
4. **Make the Phase 2 proof sketch more self-contained** by giving the explicit form of \(\mathbf{A}\) and stating its eigenvalue bounds in the main text. Even a one-sentence statement of the eigenvalue argument would substantially increase verifiability.
5. **Replace the cryptic \(\sigma = o(\operatorname{poly}(m^{-k^2}, d^{-1/2}))**\) with explicit polynomial conditions to help readers assess the feasibility of the initialization.

## Score and Decision

This is a solid theoretical analysis paper that makes a genuine technical contribution — extending the global convergence analysis of GD-trained ReLU networks from the single-teacher to the multi-teacher setting — using a novel dynamical system for handling teacher interactions. The proof framework is clearly motivated, the three-phase structure is natural, and the balanced-norm finding is interesting. The main weaknesses are an imprecise "implicit bias" claim, thin experiments (acceptable for a theory paper but improvable), and restrictive assumptions that are at least partially acknowledged.

The paper would benefit from revisions but is worth accepting in its current form. The core mathematical contribution is clear, and the issues identified are addressable without changing the paper's substance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>