Now I have verified all key claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper provides a theoretical analysis of sequential gradient descent (GD) on continual linear classification problems. When tasks are jointly separable and presented cyclically or randomly, the paper proves that sequential GD converges in direction to the joint (offline) max-margin solution—despite each individual task's GD bias being toward its own max-margin direction. It also gives non-asymptotic bounds on cycle-averaged forgetting (showing it decays at rate O(ln⁴J/J²)) and extends the analysis to the non-separable setting with a faster Õ(J⁻²) convergence rate to the unique global minimum.

## Strengths

- **First proof that sequential GD converges in direction to the joint max-margin solution under cyclic task ordering (Theorem 3.2).** The decomposition \(\boldsymbol{w}_k^{(t)} = \ln(\frac{K}{M}t)\,\hat{\boldsymbol{w}} + \boldsymbol{\rho}_k^{(t)}\) with bounded \(\boldsymbol{\rho}_k^{(t)}\) directly establishes directional convergence: \(\lim_{t\to\infty} \boldsymbol{w}_k^{(t)}/\|\boldsymbol{w}_k^{(t)}\| = \hat{\boldsymbol{w}}/\|\hat{\boldsymbol{w}}\|\). This contrasts with the projection-based SMM algorithm (Evron et al., 2023), which does not always converge to the offline max-margin direction, and is a genuine extension of the single-task implicit bias literature (Soudry et al., 2018) to a continual multi-task setting.

- **Non-asymptotic analysis of cycle-averaged forgetting that ties task alignment to forgetting behavior (Theorems 3.3 and 3.4).** The upper and lower bounds on \(\mathcal{CF}(J)\) are expressed in terms of \(N_{p,q}\) and \(\bar{N}_{p,q}\)—aggregates of positive/negative inner products between data points of different tasks. The bounds capture both positive forgetting (catastrophic forgetting) and negative forgetting (backward knowledge transfer), and the rate O(ln⁴J/J²) is faster than the loss convergence rate O(ln²J/J). The synthetic illustration in Figure 3 demonstrates the qualitative match between the bounds and observed behavior for aligned vs. contradicting tasks.

- **Extension to random task ordering (Theorems 4.1 and 4.2).** The paper proves that the same directional convergence to the joint max-margin solution holds almost surely under uniformly random task presentation, with a learning rate condition \(\eta < 2\phi^2/(\beta\sigma_{\max}^4)\) that is independent of the number of tasks \(M\) and steps \(K\)—a cleaner condition than the cyclic case. This shows the result is not an artifact of deterministic cycling.

- **Analysis of the non-separable case with a faster rate (Theorem 5.2).** For settings where no linear classifier solves all tasks simultaneously, the paper establishes an \(\tilde{\mathcal{O}}(J^{-2})\) convergence rate to the unique global minimum \(\boldsymbol{w}_\star\), leveraging local strong convexity on a compact set (Lemma 5.1). This extends the scope beyond the separable regime and covers realistic scenarios with task conflict.

## Weaknesses

### Fatal
None.

### Major

- **The core implicit bias theorem (Theorem 3.2) depends on the non-degeneracy condition (Assumption 3.2).** This assumption requires every support vector to have a unique dual coefficient. While the paper notes that (a) the assumption "holds for almost all datasets sampled from a continuous distribution" (p. 4) and (b) the analogous single-task result in Soudry et al. (2018) holds without it, the paper's headline directional convergence result for the continual setting is formally proven only under this condition. The authors state they "believe that directional convergence... will hold even without Assumption 3.2" but "did not pursue removing the assumption because it does not offer substantial additional insights" (p. 5). This is a genuine limitation: the paper's most central theorem is conditional on a restriction that the authors themselves consider technically removable but choose not to remove. A reader is left uncertain whether the proof technique is too brittle to handle the general case or whether the difficulty of removal is simply higher than suggested.

### Minor

- **The step-size schedule for the non-separable case (Theorem 5.2) depends on the cycle count \(J\), which is unknown at training time.** The step size is \(\eta = \min\{\frac{1}{2\sqrt{2}KB},\; \frac{1+2\sqrt{2}}{2\sqrt{2}KJ}\ln(J^2 \cdot \max\{1,\dots\})\}\). While this yields the \(\tilde{\mathcal{O}}(J^{-2})\) rate, the schedule cannot be implemented without foreknowledge of the horizon \(J\). A fixed step-size analysis would connect more naturally with the separable-case analysis and have clearer practical relevance. This issue is secondary because the paper's main contribution is in the separable setting, but it weakens the non-separable result's significance.

- **The local strong convexity parameter \(\mu\) (Lemma 5.1) can become arbitrarily small when the non-separability measure \(b\) is tiny.** The paper acknowledges (p. 10) that the radius of the compact set \(\mathcal{W}\) can be \(O(1/b)\), and \(\mu\) can consequently be very small for nearly-separable data. This means the exponential term \(\exp(-\mu J / (1+2\sqrt{2})B)\) in Theorem 5.2 can be extremely slow, potentially overshadowing the \(\tilde{\mathcal{O}}(J^{-2})\) rate. The implication for near-separable settings is not discussed.

### Trivial

- **Typo in Theorem 4.1 (p. 9):** \(\lim_{t\to\infty} \boldsymbol{x}_i^{\top}\boldsymbol{w}_k^{(t)} = 0\) should read \(\to\infty\) (as correctly stated in Theorem 3.1). A zero margin contradicts the separable-classification claim.
- **Theorem 4.2 phrasing:** "with probability \(^{\,I}\)" contains a formatting artifact; the surrounding text correctly uses "almost surely," so this is a minor presentation issue.

## Nice-to-Haves

- The paper does not discuss how the per-task budget \(K\) should be chosen or how results degrade for very small/large \(K\). Since the learning rate bounds and forgetting rates depend on \(K\), a brief comment on its role would be helpful.
- A few additional synthetic simulations (varying \(M\), dimension, and task alignment levels) would strengthen confidence that the forgetting bounds in Theorem 3.4 track actual forgetting, not merely bound behavior.

## Removed Points

These points from the inputs are excluded with justification:

- **Criticism that \(N_{p,q}\) and \(\bar{N}_{p,q}\) "do not necessarily capture the actual behavior of forgetting."** The paper's claim is that the bounds *involve these quantities*, establishing a theoretical link between task alignment and forgetting. The bounds express what they claim. The illustrative example (Figure 3) is appropriate for a theory paper. This is a speculative concern, not a demonstrated flaw.
- **Criticism about limited experimental scope.** The paper is a theory contribution; experiments are illustrative and appropriate for this genre. The calibration statement agreed with this, making the criticism internally inconsistent.
- **Criticism about the "small learning rate" restriction.** Standard for this type of analysis (Soudry et al. 2018 and the entire implicit-bias literature use similar restrictions).
- **Formatting/parser artifacts** (garbled text, missing union symbols, "Beyond linear model.4."). These are PDF extraction errors, not author mistakes.
- **Generic concerns** that upper bounds might be loose ("it could just be loose for smaller \(m,k\)"). This is true of all upper bounds and is not a specific identified problem.
- **Missing related works.** Cannot be verified without external sourcing.

## Novel Insights

The reviewer inputs do not surface any genuinely novel observation that goes beyond the paper's own contributions. The main insight—that sequential GD in a continual setting inherits the implicit bias toward the joint max-margin direction, despite task-specific biases pulling in different directions—is already well articulated by the paper itself and supported by the theoretical results.

## Suggestions

1. Provide a proof sketch or at minimum a more detailed discussion of why removing Assumption 3.2 is nontrivial. If the single-task proof (Soudry et al., 2018) handles the general case, clarify what specifically breaks in the multi-task setting; if the proof would go through with minimal changes, consider including it.
2. For the non-separable case (Theorem 5.2), add a fixed-step-size corollary (even with a slower rate like \(O(1/J)\) or \(O(\ln^2 J/J)\)) so that the result does not depend on foreknowledge of the horizon \(J\).
3. Fix the typo in Theorem 4.1 ("= 0" → "→∞").

## Score and Decision

This paper makes a solid theoretical contribution by extending implicit-bias analysis to the continual learning setting—a genuine and nontrivial extension. The results are novel, the proofs appear rigorous, and the writing is clear. The main weakness (Assumption 3.2) is acknowledged and known to be mild, but its presence limits the generality of the headline result. The secondary weaknesses (J-dependent schedule, small-μ issue) are minor. On balance, the paper merits acceptance.

**Originality:** High — first characterization of GD's implicit bias in continual linear classification.  
**Research question:** Important — bridges the gap between single-task implicit bias theory and continual learning.  
**Claims supported:** Well supported, with the caveat about Assumption 3.2.  
**Soundness:** Good — clear assumptions, explicit theorem statements, transparent about limitations.  
**Clarity:** Good — well-structured, though some bounds are unavoidably dense.  
**Value to community:** Significant — provides theoretical grounding for the empirical observation that simple sequential training can mitigate forgetting with repetition.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>