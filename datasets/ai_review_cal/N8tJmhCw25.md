- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have a thorough understanding of the paper and all reviewer inputs. Let me compose the final consolidated review.

---

## Summary

This paper provides the first almost sure convergence *rates* for the Stochastic Three Points (STP) derivative-free optimization algorithm across smooth nonconvex, smooth convex, and smooth strongly convex function classes. For smooth nonconvex functions, the best gradient iterate converges almost surely at a rate arbitrarily close to \(o(1/\sqrt{T})\), and the last gradient iterate converges (as a limit) both almost surely and in expectation. For convex functions, the function value gap converges at \(O(d/T)\) in expectation and arbitrarily close to \(o(1/T)\) almost surely. For strongly convex functions, an adaptive step-size variant yields geometric convergence \(O((1-\mu/(dL))^T)\) in expectation and arbitrarily close almost surely. The paper also notes that the STP best-iterate rate improves over the analogous SGD rate.

## Strengths

- **First almost sure convergence rates for STP.** Theorems 1, 5, and 7 provide the first almost sure convergence *rates* for the STP algorithm across smooth, convex, and strongly convex settings, filling a clear gap in the zeroth-order optimization literature (Abstract, Table 1). Prior work (Bergou et al., 2020; Gratton et al., 2015) gave only in-expectation or high-probability results without almost sure rates.

- **Better almost sure rate than SGD for the best gradient iterate.** The paper explicitly shows (Section 1) that STP achieves \(\min_{1\le t\le T}\|\nabla f(\theta^t)\| = o(1/T^{\frac12-\epsilon})\) while the analogous SGD result is \(o(1/T^{\frac14-\frac\epsilon2})\), a strictly faster rate for the best iterate.

- **Last-iterate convergence for smooth nonconvex functions without Łojasiewicz assumptions.** Theorems 2 and 3 establish \(\lim_{T\to\infty}\|\nabla f(\theta^T)\|_{\mathcal{D}} = 0\) both almost surely and in expectation under only smoothness, going beyond prior work (Gratton et al. treated only the best iterate; Wang & Feng required the Łojasiewicz condition). This is a nontrivial contribution because last-iterate guarantees are generally harder than best-iterate guarantees.

- **Clean, self-contained theoretical framework.** The paper provides explicit step-size constructions for each function class (e.g., \(\alpha_t = \alpha/t^{\frac12+\epsilon}\) for smooth, \(\alpha_t = \alpha/t\) for convex) and leverages a family of norms \(\|\cdot\|_{\mathcal{D}}\) that cleanly connect the search distribution to the analysis. The proof structure (descent lemma + Borel–Cantelli) is standard but well-executed.

- **Numerical experiments confirm the predicted rates.** Figures 1–3 show that, across 50 trajectories on a \(d=500\) quadratic, the best gradient iterate of STP decays at the predicted \(o(1/T^{0.49})\) rate, and STP performs competitively with RGF and GLD. This is appropriate validation for a primarily theoretical paper.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The strongly convex section uses an adaptive step-size variant that is not clearly distinguished from the standard STP template.** Theorems 6 and 7 use step sizes \(\alpha_t = |f(\theta^t + h^{-t}s_t) - f(\theta^t)|/(L h^{-t})\), which depend on the smoothness constant \(L\) and require an extra function evaluation per iteration compared to the fixed-step-size variants (three evaluations vs. two). The paper mentions "when step sizes are obtained by approximating the directional derivatives" (lines 7, 252) but never explicitly flags this as a departure from Algorithm 1, discusses the per-iteration cost difference, or addresses the practical challenge of knowing \(L\). This is a presentational gap—the results themselves are valid—but readers may not realize that Section 5 analyzes a modified algorithm with different implementation requirements.

- **The convex result (Theorem 4) requires knowledge of \(R\) (the diameter of the sublevel set).** The step size condition \(\alpha > R/\mu_{\mathcal{D}}\) depends on \(R\), which is not known a priori. Remark 5 discusses how overestimating \(R\) worsens the constant but does not address how to estimate \(R\) or what happens if it is grossly misestimated. This is a standard limitation for such analyses but is not acknowledged as a practical concern.

- **The numerical experiments are limited to a single quadratic function (\(d=500\)).** While this is acceptable for a theory paper validating predicted rates, the narrow scope (one problem instance, one-dimensionality family) leaves open questions about whether the predicted rates and behaviors hold more broadly. A second example (e.g., a non-quadratic or nonconvex function) would strengthen the empirical support.

- **The paper lacks a dedicated limitations discussion.** There is no section that steps back to discuss when the results may not apply (e.g., the smoothness constant \(L\) needed for the strongly convex variant, the diameter \(R\) needed for the convex rates, or cases where the distribution assumptions fail). Adding a brief limitations paragraph would improve completeness and help practitioners assess applicability.

### Trivial

- **Table 1 is embedded as an image.** The text renders poorly in the PDF extraction; the paper should ensure the table is machine-readable in the source.

- **Minor formatting issues in equations** (e.g., line 271 has a mismatched brace, some lines show garbled concatenation) are parser artifacts and should not affect the review.

## Nice-to-Haves

- A brief discussion contrasting the adaptive step-size variant (Section 5) with the fixed-step-size template: explicitly state that it requires three function evaluations per iteration and knowledge of \(L\), versus two evaluations and no knowledge of \(L\) for the fixed-step-size variants.
- An explicit statement in the convex section that \(R\) can be conservatively estimated or replaced by a bound when available, with the associated cost.
- A short note in the nonconvex section acknowledging that Theorem 2 provides a limit result without a convergence rate for the last iterate (the paper is transparent about this but an explicit remark would help readers).

## Removed Points

These points were raised by reviewers but removed for the reasons noted:

- *"The last-iterate result does not provide a rate—only a limit."* Removed because the paper is fully transparent about this (Table 1 says "Convergence (limit)," Remark 3 explains the gap). A reader cannot misinterpret this on careful reading; the presentation is honest.
- *"The RGF step size \(1/L\) is privileged."* Removed because the paper follows the original RGF paper's recommended step size. This is standard practice for baseline implementation, not a flaw.
- *"Missing related works."* Removed per policy: I cannot independently verify what related works exist outside the paper.
- *"Proofs deferred to appendix."* Removed per policy: the parser strips appendix content; the proofs exist in the original submission, and this is standard for conference papers.
- *"The GLD parameters are set arbitrarily."* Removed because the paper states the chosen parameters (\(r=10^{-5}, R=10^{-4}\)) and the GLD algorithm is not the focus; the experiment is illustrative.

## Novel Insights

None beyond the paper's own contributions. The review process confirms that the paper's claimed results (first almost sure rates for STP, faster than SGD for the best iterate, last-iterate convergence without Łojasiewicz) are accurate and well-supported.

## Suggestions

1. **In Section 5, add a short paragraph** explicitly contrasting the adaptive step-size variant with the standard STP template. State the per-iteration cost (3 evaluations vs. 2) and the dependence on \(L\). This would eliminate the only presentational ambiguity in an otherwise clear paper.
2. **Add a brief "Limitations" paragraph** at the end (before or after the experiments) discussing: (a) the need to know \(L\) for the strongly convex variant, (b) the need to know or bound \(R\) for the convex rates, and (c) the illustrative scope of the numerical experiments.
3. **In Remark 5 or a follow-up note**, suggest a practical strategy for choosing \(\alpha\) when \(R\) is unknown (e.g., doubling until the iterates stay within the sublevel set, at the cost of a larger constant).
4. **Consider adding a second experiment** (e.g., a small nonconvex problem or a different distribution) to broaden the empirical validation beyond the single quadratic.
