Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper extends the primal-dual hybrid gradient (PDHG) method to structured nonconvex-nonconcave minimax problems whose saddle-subdifferential operator satisfies the weak Minty variational inequality (MVI) condition. The authors construct a novel Legendre function that nonlinearizes the PDHG preconditioner via the Bregman proximal point (BPP) framework, yielding two algorithms: SA-GDmax (which assumes an exact max-oracle) and SA-MGDA (which uses finite inner gradient steps). They prove O(1/k) convergence rates under the weak MVI condition using a new Bregman-distance-based optimality measure that upper-bounds the squared gradient norm. The method exactly recovers PDHG on bilinear problems and is empirically demonstrated on a toy problem and a fair classification task.

## Strengths

1. **Novel extension of PDHG to nonconvex-nonconcave settings under weak MVI.** The paper constructs a Legendre function \(h(u,v)=\frac{1}{2\tau}(\|u\|^2+\|v\|^2)-\phi(u,v)\) (Section 5.1) that generalizes the PDHG preconditioner. To my knowledge, this is the first PDHG-like method with convergence guarantees under the weak MVI condition, bridging a gap between bilinear PDHG and general nonconvex-nonconcave problems.

2. **O(1/k) convergence guarantee with a new optimality measure.** Theorem 3 establishes \(\min_{i=1,\dots,k} D_h(x_i,x_{i-1}) \le \frac{D_h(x_*,x_0)}{(1-\rho(1/\tau+L))k}\) for SA-GDmax. The Bregman distance \(D_h(x_i,x_{i-1})\) serves as the optimality measure, and the paper proves it upper-bounds the squared subgradient norm (Theorem 1). Both EG+/CEG+ and SA-GDmax achieve O(1/k) rates on squared gradient norm, but the Bregman distance formulation is novel and may offer practical advantages.

3. **Exact recovery of PDHG for bilinear problems.** When \(\phi\) is bilinear, the method exactly reduces to PDHG (Section 5.1), inheriting PDHG's known practical strengths in that structured setting. This provides a principled continuity from known efficient algorithms to more general regimes.

4. **BPP with projection extends the range of \(\rho\).** The paper develops a BPP variant with a separating hyperplane projection (Lemma 3, Theorem 2) that relaxes the condition from \(\rho L_h < 1\) to \(\rho L_h < 2\). This directly extends the range of \(\rho\) for which SA-GDmax with projection converges (Theorem 4: \(\rho < 2/(2L+\hat{L})\)).

5. **Practical variant with provable total complexity.** SA-MGDA (Algorithm 1) replaces the exact max-oracle with \(J=O(\log\epsilon^{-1})\) inner proximal gradient steps, achieving total gradient complexity \(O(\epsilon^{-1}\log\epsilon^{-1})\) to reach an \(\epsilon\)-stationary point (Theorems 5 and 6). This matches the exact SA-GDmax outer rate up to a log factor.

6. **Empirical validation.** On a toy problem that satisfies the weak MVI condition (Section 7.1, Figure 1), SA-GDmax outperforms CEG+ and regularized GDmax. On a fair classification task (Section 7.2, Figure 2), SA-GDmax consistently yields higher worst-category test accuracy than baselines across two learning rates, with tight confidence intervals from 50 runs.

## Weaknesses

### Fatal
None.

### Major

- **Unsupported claim about worst-case superiority over extragradient methods (Section 1, line 17).** The paper states: "The extragradient method also has the \(O(1/k)\) rate ... but in terms of the squared gradient norm that is upper bounded by our new optimality measure. This implies that the SA-GDmax can be superior to the extragradient in the worst case." The reasoning is logically incomplete: both methods achieve \(O(1/k)\) on the squared gradient norm (EG+/CEG+ directly, SA-GDmax via the bound \(D_h \ge \frac{\|s\|^2}{2L_h}\)). The fact that \(D_h\) is an upper bound on the squared gradient norm does not by itself establish a tighter rate on that norm — one would need to compare constants, which the paper does not do. The later hedging in Section 6.1 ("it is possible that we have a gain") is more appropriate. This sentence should be revised to accurately describe the relationship: both methods achieve \(O(1/k)\) rates, and the Bregman distance formulation offers a complementary perspective that may yield practical advantages (as seen empirically). The core contribution does not depend on this claim, so the issue is correctable.

### Minor

1. **Compact derivation of SA-GDmax from BPP (Section 5.1).** The paper states that rewriting the BPP inclusion \((\nabla h + M)x_{k+1} \ni \nabla h x_k\) with \(h\) in (5) yields the SA-GDmax updates, and provides the resulting argmin/argmax forms. The derivation is described in a few sentences and the connection between the inclusion and the argmax formulation for \(v\) is not fully expanded step-by-step. A more detailed derivation (with explicit sign handling in the saddle operator) in the appendix would significantly strengthen confidence in the theoretical guarantees for readers unfamiliar with this machinery. I verified the algebra independently and it is correct, but the presentation is too compressed.

2. **Complexity comparison with extragradient methods lacks full transparency (Section 6.2).** The paper notes SA-MGDA's total complexity \(O(\epsilon^{-1}\log\epsilon^{-1})\) "matches the complexity of the SA-GDmax up to a logarithmic factor," which is accurate as a comparison between SA-MGDA and SA-GDmax. However, the paper does not directly compare this to the \(O(\epsilon^{-1})\) complexity of EG+/CEG+ (which require no inner iterations). Given Table 1's framing of the methods as alternatives under the same weak MVI condition, the \(\log\epsilon^{-1}\) gap relative to extragradient methods should be explicitly acknowledged and discussed (e.g., whether a fixed number of inner steps with warm-start could close this gap).

3. **No guidance on step size \(\tau\) selection in practice (Section 5.1).** The theoretical conditions give an interval \(\tau \in (\frac{\rho}{1-\rho L}, \frac{1}{L+\hat{L}})\) but the experiments use only two fixed values (0.01 and 0.001) without a sensitivity analysis. Practical guidance on choosing \(\tau\) within the admissible range would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- The paper could briefly discuss whether the inner iterations in SA-MGDA can be replaced with a fixed (small) number of steps while maintaining O(1/k) convergence (with a possibly worse constant), which would make the comparison with EG+/CEG+ more direct.
- A sensitivity analysis of the step size \(\tau\) would be helpful for practitioners.

## Removed Points

These points were flagged by the reviewer but are removed after verification against the paper:

- **"The fair classification experiment is not known to satisfy the weak MVI condition, so the theoretical guarantees do not apply... the empirical evaluation would be more convincing if it included at least one problem that is known to satisfy weak MVI."** — The paper already includes a toy example (Section 7.1, lines 281, 288) that is explicitly stated to satisfy the weak MVI condition, and the fair classification experiment is honestly scoped as a practical test outside the theoretical regime. This criticism is factually incorrect.

- **"The assumption of an efficient exact maximization oracle for SA-GDmax is very strong... The narrative sometimes treats SA-GDmax as the primary method and SA-MGDA as an afterthought."** — The paper explicitly develops SA-MGDA as the practical variant, states that SA-GDmax requires "a computationally cheap exact maximization oracle" (Section 6.1, line 245), and frames SA-MGDA as "a first attempt to making the SA gradient method more practical" (Section 5.2). The paper is transparent about this limitation.

- **"The paper should acknowledge the \(\log\epsilon^{-1}\) gap in complexity between SA-MGDA and extragradient methods."** — This was kept as Minor weakness #2 above, but the reviewer's framing as a major omission is too strong; the paper's actual claim is about SA-MGDA vs. SA-GDmax, which is accurate.

## Novel Insights

Beyond the paper's own contributions, one interesting observation emerges from the reviews: The relationship between the Bregman distance \(D_h(x_i,x_{i-1})\) and the squared gradient norm creates an interesting asymmetry in how convergence is measured. SA-GDmax's O(1/k) guarantee on \(D_h\) translates to an O(1/k) guarantee on \(\|s\|^2\) with a constant factor \(2L_h\). This is the same asymptotic rate as EG+/CEG+, but the Bregman distance may track a different notion of progress — one that reflects the problem's geometry via the coupling \(\phi\). Conversely, the equivalence also means that if EG+/CEG+ has a tighter constant on \(\|s\|^2\), that does not preclude SA-GDmax from converging faster on the Bregman measure. The empirical results suggest this may happen in practice, but the theoretical comparison of constants remains an open question worth exploring.

## Suggestions

1. **Revise the comparative claim in the introduction** (line 17) to state honestly that both SA-GDmax and EG+/CEG+ achieve O(1/k) rates on the squared gradient norm, and that SA-GDmax's rate is in terms of a Bregman distance that upper-bounds this norm, rather than claiming implied superiority.

2. **Add a step-by-step derivation** in the appendix showing how the BPP inclusion \((\nabla h + M)x_{k+1} \ni \nabla h x_k\) expands into the explicit \(u\) and \(v\) updates, with careful handling of the signs of the saddle operator \(M_\phi\) and the composite terms \(\partial f, \partial g\).

3. **Add a brief complexity comparison table or paragraph** that directly compares SA-MGDA's \(O(\epsilon^{-1}\log\epsilon^{-1})\) total complexity to EG+/CEG+'s \(O(\epsilon^{-1})\), and discuss whether the log factor can be mitigated.

4. **Provide guidance on choosing \(\tau\)** in practice (e.g., a recommended default or a simple grid search strategy).

## Score and Decision

The paper makes a genuine theoretical contribution — the first principled extension of PDHG to nonconvex-nonconcave problems under the weak MVI condition — with clean O(1/k) rates and an interesting Bregman-distance-based optimality measure. The main claims are sound; the derivation, while compact, is correct. The weaknesses are presentation-level and a single overclaimed comparative statement in the introduction, none of which undermine the core contribution. The paper is suitable for acceptance provided the authors address the main presentation and overclaim issues.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>