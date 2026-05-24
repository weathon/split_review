Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket:** The paper sits between the weak anchors (Zb6qOouUJO at 5.75, BAX3NXJ6vU at 5.33, 2fSyBPBfBs at 4.17) and the strong anchor (fMTPkDEhLQ at 8.0). Initial bracket: **6.0–8.0**.

**Round 2 narrowing:** Comparing against mid-range anchors (A4aG3XeIO7 at 6.50, vgV4y086FY at 6.75) and upper-mid anchors (ikkvC1UnnE at 7.50). The paper is clearly stronger than the 6.5 anchors — it has a more novel conceptual contribution, both upper and lower bounds, and a more fundamental improvement. It is comparable to ikkvC1UnnE (7.50) in quality — both advance their respective areas with novel techniques and strong theoretical results — but slightly below fMTPkDEhLQ (8.0) which has fully tight bounds. **Final score: 7.5**.

---

## Summary

This paper proposes F²SA‑*p*, a family of fully first-order methods for stochastic bilevel optimization under nonconvex–strongly-convex lower-level problems. The key insight is that the existing F²SA method can be reinterpreted as a forward-difference approximation of the hypergradient; generalizing to *p*-th order finite differences yields improved SFO complexity of \(\tilde{\mathcal{O}}(p\,\epsilon^{-4-2/p})\) when the lower-level variable is *p*-th order smooth, down from the prior best \(\tilde{\mathcal{O}}(\epsilon^{-6})\). An \(\Omega(\epsilon^{-4})\) lower bound via a clean separable construction shows near-optimality for large *p*. Moderate-scale experiments on logistic regression hyperparameter tuning corroborate the practical benefit of larger *p*.

## Strengths

- **Novel conceptual insight with broad implications.** The reinterpretation of F²SA as a forward-difference approximation (Eq. 8–9, Section 3.1) is genuinely fresh, and it naturally motivates the generalization to *p*-th order finite differences via Lemma 3.1. This connects two previously separate ideas — penalty-based bilevel methods and numerical finite-difference schemes — in a way that yields immediate algorithmic improvements.

- **Substantial and rigorous complexity improvement.** Theorem 3.1, supported by the key regularity estimate in Lemma 3.2 (Lipschitzness of \(\frac{\partial^{p+1}}{\partial \nu^p \partial x} \ell_\nu\) via the Faà di Bruno formula), provides an explicit SFO bound of \(\tilde{\mathcal{O}}(p\kappa^{9+2/p}\epsilon^{-4-2/p})\). This strictly improves the prior \(\tilde{\mathcal{O}}(\epsilon^{-6})\) for all \(p \geq 2\) and interpolates toward the single-level SGD lower bound as \(p\) grows.

- **Clean lower bound establishing near-optimality.** Theorem 4.1 proves an \(\Omega(\epsilon^{-4})\) lower bound via a fully separable construction that automatically satisfies all the paper's smoothness assumptions, including the higher-order conditions. The reduction to the single-level hard instance from Arjevani et al. (2023) is simple but correct and robust, avoiding issues in prior bilevel lower-bound constructions (Section 4).

- **Well-structured and clearly motivated.** The paper situates its contribution precisely within the existing literature (Table 1, Section 2.2), carefully distinguishes its oracle assumptions from prior work (stochastic Hessian, mean-squared smoothness, joint high-order smoothness), and frames open problems honestly.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Experimental section does not directly test the theoretical claims.** The experiments report test loss and accuracy (Figure 1) rather than any stationarity metric such as \(\|\nabla\varphi\|\). While this is common in theory papers, the headline contribution is a sharper complexity bound for reaching \(\epsilon\)-stationarity, so a direct measurement — even for a single algorithm variant — would strengthen the empirical narrative. The hyperparameter search is described only as "logarithmic scale with base 10" without specific grids, selection criteria, or seed reporting, which limits reproducibility.

- **The lower bound, while clean, is a straightforward reduction.** The separable construction (matching \(f_U\) from the single-level hard instance with a simple quadratic lower-level) is correct and robust but does not exploit bilevel structure. This is not a flaw — the bound serves its purpose — but the contribution of Theorem 4.1 is primarily expository rather than technically novel.

### Trivial

- The normalized gradient step in Algorithm 1 is analyzed in the paper (Theorem 3.1 applies to Algorithm 1 as written). Remark 3.1 states that the standard (non-normalized) gradient step would also work via a more involved analysis. This remark uses "we believe," which is informal for a theory paper; a brief sketch of why the normalization does not lose the rate would improve reader confidence.

## Nice-to-Haves

- A direct measurement of \(\|\nabla\varphi(x_t)\|\) against total SFO calls for at least one \(p\) would provide a minimal empirical anchor for the complexity theory.
- Explicitly verifying that Assumption 2.5 holds for the logistic regression example (beyond the reference to Garg et al. 2021) would solidify the connection between theory and experiment.
- Specifying hyperparameter search grids, selection criteria, and random seeds for the experiments.
- A brief discussion of the per-iteration wall-clock cost for larger \(p\) (the inner loops are parallelizable, but \(p+1\) lower-level problems must be solved).

## Removed Points

These points were flagged by the harsh critic but are removed from the review for the stated reasons.

- **"Normalized-gradient outer step lacks rigorous justification."** — **REMOVED.** The paper analyzes Algorithm 1 with the normalized step; Theorem 3.1 explicitly provides convergence guarantees for this algorithm. Remark 3.1 merely notes that the *standard* (non-normalized) step would also work, which is not essential to the paper's claims. The harsh critic's concern about "what happens when \(\|\Phi_t\|\) is small" would be addressed in the stripped appendix proof of Theorem 3.1.

- **"The experimental narrative could mislead the reader into thinking that F²SA-p dominates all baselines in a fair oracle-matched setting."** — **REMOVED.** The paper extensively discusses different oracle assumptions in Section 2.2 and never claims oracle-matched dominance. The experiments are presented as a practical demonstration, not as a controlled oracle-matched comparison.

- **"The construction is somewhat trivial (the bilevel structure plays no role)."** — **REMOVED.** The harsh critic concedes this serves its purpose. Not a weakness; simplicity in a lower bound is a virtue.

- **"One could argue that the lower bound construction is somewhat trivial."** — **REMOVED.** Same point; already addressed above.

## Novel Insights

Beyond the paper's own contributions, the reviewers' synthesis highlights an interesting meta-observation: the finite-difference viewpoint may unify several seemingly distinct penalty-based bilevel methods. The connection to *p*-th order central differences (Lemma 3.1) suggests that other penalty formulations could be reinterpreted as specific choices of finite-difference stencils, potentially opening a systematic way to design and analyze fully first-order bilevel methods by importing techniques from numerical analysis.

## Suggestions

- Include a one-paragraph sketch of why the normalized gradient step does not alter the convergence rate (e.g., by bounding \(\|\Phi_t\|\) from below with high probability) to make Remark 3.1 more self-contained.
- Report \(\|\nabla\varphi(x_t)\|\) for one \(p\) against SFO calls to anchor the theory empirically, and provide full hyperparameter tuning details for reproducibility.

## Score and Decision

**Calibration anchors compared across rounds:**
- Zb6qOouUJO (5.75, rejected): Variance-reduced bilevel method; incremental contribution. Our paper is substantially more novel.
- BAX3NXJ6vU (5.33, rejected): Saddle-point escape for bilevel; solid but presentation issues. Our paper is stronger.
- 2fSyBPBfBs (4.17, rejected): Bilevel without LLSC; has proof errors. Our paper is far stronger.
- A4aG3XeIO7 (6.50, accepted): Tuning-free bilevel; practical contribution, limited novelty. Our paper has a more creative conceptual contribution.
- vgV4y086FY (6.75, rejected): DP bilevel; good novelty. Our paper has broader scope (upper + lower bounds).
- ikkvC1UnnE (7.50, accepted): DP for SOSP; closes a gap with novel techniques. Our paper is at a similar quality level.
- fMTPkDEhLQ (8.0, accepted): Tight lower bounds under high-order smoothness; technically deep and fully tight. Our paper has gaps but broader contribution.

**Round-1 bracket:** 6.0–8.0. **Round-2 narrowing** places the paper between the 6.5–6.75 anchors (clearly stronger) and the 8.0 anchor (slightly weaker due to admitted gaps). The paper is most comparable to the 7.5 anchor (ikkvC1UnnE) in quality.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>