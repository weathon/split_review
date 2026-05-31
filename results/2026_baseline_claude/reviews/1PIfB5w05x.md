## Summary

This paper studies sparse signal recovery when observations come from two quality tiers: $n_1$ high-quality measurements with small noise variance $\sigma_1^2$ and $n_2$ low-quality measurements with larger variance $\sigma_2^2$. The authors introduce the **Price of Quality** ($\gamma$), defined as the number of low-quality samples that replace one high-quality sample under the derived sufficient conditions, and study $\gamma$ across information-theoretic and algorithmic recovery regimes. They show that in the agnostic information-theoretic setting $\gamma \leq 2$ (upper bounded, independent of noise levels), while in the informed setting $\gamma$ can be arbitrarily large. For algorithmic recovery via the LASSO, they prove that the phase-transition threshold is identical to the homogeneous-noise case and depends only on $\sigma_{\text{avg}}^2 = (n_1\sigma_1^2 + n_2\sigma_2^2)/n$, revealing a striking robustness of computational recovery to noise heterogeneity.

---

## Strengths

- **Novel and well-motivated problem formulation.** Formalizing the mixed-quality data setting for sparse recovery is timely (e.g., LLM-labeled vs. human-labeled data) and, to the best of available knowledge, has not been done before. The two-setting structure (agnostic vs. informed) cleanly isolates the role of noise provenance.

- **Surprisingly clean Price of Quality characterization.** The $\gamma \leq 2$ bound in the agnostic IT case (equations 13–14) is counterintuitive and tight in the limit $\sigma_1^2/\sigma_2^2 \to 0$. The argument reducing it to a simple log-ratio inequality is elegant and verifiable by inspection of equation (9).

- **Non-trivial LASSO extension.** Theorem 3 extends Wainwright (2009) to heterogeneous noise through a QR / Haar-measure argument that circumvents the failure of the classical Wishart structure. The result is both necessary and sufficient on sample size, and the regularization condition (28) depends on the noise only through $\sigma_{\text{avg}}^2$, matching the homogeneous case with that average—a clean and useful finding.

- **Sharp informed IT condition.** Theorem 2 arises from an exact optimization of the Chernoff exponent (rather than a relaxation), and the resulting $\gamma$ formula (18) exhibits the three asymptotic regimes (19)–(21) cleanly, including $\gamma \to \infty$ in the low-SNR$_2$/high-SNR$_1$ regime, which has clear practical implications.

- **Concrete comparison of IT vs. algorithmic sensitivity.** The paper's central message—that the IT threshold differentiates sample quality while the algorithmic (LASSO) threshold does not—is a genuinely novel observation that fits naturally into the literature on Overlap Gap Property and algorithm–information gaps.

---

## Weaknesses

### Fatal
None.

### Major

1. **Agnostic IT condition is sufficient only, and tightness is unclear.** The authors acknowledge (Remark 3.2) that the condition (9) arises from a relaxation of a cubic Chernoff equation. The primary quantity of interest—$\gamma \leq 2$—is therefore only an upper bound on the Price of Quality under a possibly loose sufficient condition. It is conceivable that the true agnostic IT threshold implies $\gamma \leq c < 2$ for some $c$, or even $\gamma \equiv 1$ (no benefit to quality at all). Without establishing necessity, the bound $\gamma \leq 2$ lacks a matching lower bound showing it is actually achieved.

2. **No algorithmic analysis in the informed setting.** The contrast between the informed and agnostic IT thresholds ($\gamma$ unbounded vs. $\leq 2$) is the paper's central message, yet the analogous contrast for LASSO recovery is left entirely open. The paper identifies the technical obstruction (loss of Wishart structure; Remark 4.2) but does not provide even a partial result or a matching lower bound for the informed LASSO.

### Minor

1. **No empirical verification.** A brief simulation illustrating the $\gamma \leq 2$ bound and the LASSO's average-noise behavior would substantially strengthen the paper's accessibility and verify the asymptotic theory at practical dimensions.

2. **Binary-signal assumption scope.** While the reduction from $\mathcal{C}_{p,s}(1)$ to $\{0,1\}^p$ is standard (Remark 3.1), the stated results are quantitatively for binary signals. The generalization to real-valued signals via rescaling is informal and not tracked through the Price of Quality expressions.

### Trivial

- Equation (12) displays $\sigma_1^4$ in the denominator of the first log term, which appears inconsistent with equation (9) (where $2\sigma_2^2$ appears in that denominator). The downstream asymptotic analysis (eqs. 13–14) uses the correct form and is unaffected; this is likely an OCR artifact.

---

## Nice-to-Haves

- A matching lower bound for the Price of Quality in the agnostic IT setting would greatly strengthen Theorem 1 (even showing $\gamma \geq c > 1$ for some explicit $c$ would be informative).
- Extending Theorem 3 to correlated designs (as in Wainwright 2009) or $k > 2$ quality tiers would broaden applicability.
- A numerical experiment sweeping $(n_1, n_2)$ near the boundary of condition (9) would let readers calibrate how loose the sufficient condition is in practice.

---

## Novel Insights

The most genuinely novel insight in the paper is the *asymmetry* between information-theoretic and algorithmic robustness to noise heterogeneity. In the agnostic IT setting, the Price of Quality is capped at 2 regardless of how extreme the noise ratio $\sigma_2^2/\sigma_1^2$ is—meaning that without noise provenance, the marginal value of high-quality annotations is fundamentally limited. In contrast, the LASSO threshold is entirely indifferent to individual noise levels and cares only about $\sigma_{\text{avg}}^2$, which paradoxically means that *all samples are treated equally* at the algorithmic level even when they differ substantially in quality. Together, these findings suggest that in practice the benefit of annotating data with high-quality labels lies primarily in the information-theoretic (statistical) regime, and only when noise provenance is tracked and exploited by the decoder; for the regularized regression practitioners commonly deploy, noise heterogeneity is essentially invisible.

---

## Suggestions

- Prove a lower bound on $\gamma$ in the agnostic IT setting (even a constant lower bound $\gamma \geq 1 + c$ for small SNR would pin down the true behavior and clarify whether $\gamma \leq 2$ is tight).
- Add a simulation section: plot the empirical recovery probability of (8) and LASSO as functions of $n_1/n_2$ to visually confirm the phase transitions and the $\gamma = 2$ boundary.
- Clarify the expression in eq. (12) to remove the apparent $\sigma_1^4$ inconsistency with eq. (9).
- State Proposition 4.1 as a corollary of Theorem 3 for clarity; the current separation between the theorem and the noise-scaling condition makes the algorithmic result slightly harder to parse.

---

## Score and Decision

The paper is technically sound, addresses a novel and well-motivated problem, and produces clean, interpretable results. The LASSO result (Theorem 3) is tight and technically non-trivial; the informed IT result is cleanly sharp; and the Price of Quality framework is a useful conceptual contribution. The main shortcomings—insufficient conditions in the agnostic IT case and absent algorithmic analysis for the informed setting—reduce the paper's completeness but do not invalidate its contributions. For ICLR this sits clearly above the median theoretical submission.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>