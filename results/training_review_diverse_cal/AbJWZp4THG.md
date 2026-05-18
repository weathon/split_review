Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper introduces FedAda², a class of communication- and memory-efficient jointly adaptive federated optimization algorithms. The key insight is to avoid transmitting preconditioners between server and clients (initializing client preconditioners from zero) while using SM3 compression for on-device memory efficiency. The paper provides a convergence analysis under full-batch assumptions and presents empirical results on StackOverflow (with DP), CIFAR-100, and GLD-23K, showing that FedAda² matches the accuracy of expensive joint adaptivity while being significantly more efficient.

## Strengths

- **Communication-efficient joint adaptivity without performance loss**: The paper demonstrates experimentally that skipping preconditioner transmission (zero-initializing client preconditioners) does not degrade accuracy and can even improve it under DP on StackOverflow. When measured against total transmitted bits (Figure 2), methods without preconditioner transmission converge fastest. This directly validates the core algorithmic thesis.

- **Memory-efficient local adaptivity via SM3 compression**: FedAda² uses SM3 to maintain second-order statistics at parameter-group granularity rather than per-coordinate, drastically cutting on-device memory. The experiments show this compression does not harm accuracy — on CIFAR-100 and GLD-23K, FedAda² matches Direct Joint Adaptivity while being much more memory-efficient.

- **First convergence guarantee for jointly adaptive federated optimization**: Theorem 6 and Corollary 8 provide an O(T^{-1/2}) rate for non-convex objectives under the analyzed setting. As the paper notes, to the best of the authors' knowledge, no prior convergence results exist for jointly adaptive optimization supporting methods like Adam and AdaGrad.

- **Diverse empirical validation**: The evaluation covers three datasets (StackOverflow with DP, CIFAR-100, GLD-23K with vision transformers) with 20-run confidence intervals. In all settings, FedAda² outperforms FedAvg and server-only adaptive methods, and is competitive with the expensive Direct Joint Adaptivity baseline.

## Weaknesses

### Fatal
None.

### Major

- **The convergence analysis assumes full-batch client gradients, which removes the central difficulties of federated learning (client drift, gradient noise, partial participation).** The paper (Section 5, line 19) explicitly assumes "access to full batch client gradients" and later acknowledges this as a limitation (Section 5.1, lines 72–73: "While this constraint is a limitation of our theory"). However, the abstract and main claims about convergence rates matching SOTA are stated without this caveat. Since the motivation for adaptive federated optimization is precisely to handle heterogeneity and stochasticity, a theory that abstracts these away provides limited support for the practical algorithm. The paper offers no argument — even informal — that the rates would extend to the stochastic mini-batch setting that defines real federated learning.

### Minor

- **The ε_s clipping parameter creates a gap between the theoretical analysis and the experimental implementation.** The Lipschitz constant in the analysis is defined as \(\widetilde{L} = 2\sqrt{d}G/(\eta_\ell \varepsilon_s)\), which diverges as \(\varepsilon_s \to 0\). The paper states that \(\varepsilon_s\) is "for analysis purposes" and is taken to be "negligible" in experiments. This means the regime where the analysis holds (non-trivial \(\varepsilon_s\) that keeps \(\widetilde{L}\) bounded) may not correspond to the regime used in practice, and the hidden constants in the asymptotic bound could be arbitrarily large for small \(\varepsilon_s\). The paper does not reconcile this mismatch or report the actual \(\varepsilon_s\) values used.

- **The empirical results are described only qualitatively through prose and figures, without a single numerical summary table.** The paper reports final performance relative to baselines (e.g., "FedAda² performs the best among FedAvg, FedAdaGrad, Direct Joint Adaptivity") but provides no explicit numerical table of test accuracies/losses with confidence intervals. While the figures exist in the original submission, tables would make the empirical contribution self-contained and verifiable at a glance, and would allow readers to assess the practical significance of the improvements.

- **The "Federated Blended Optimization" framework (Section 5.1) is mentioned as a contribution but is only a short conceptual paragraph, with no connection to the analysis or experiments.** It reads as an undeveloped future direction rather than a supported contribution.

- **Hyperparameter tuning details (search grid, ranges, selection criteria) are not provided.** The paper states results are "after optimal hyperparameter tuning" but does not specify what was tuned and over what ranges, which limits reproducibility.

### Trivial

- The phrase "greater than Ω(T^{1/3}) divergence in the server learning rate" (line 63) is presented as a key interpretation of Theorem 6, but how this is derived from the presented expressions is unclear without walking through the rate analysis more explicitly.

## Nice-to-Haves

- A discussion (even informal) connecting the full-batch theory to the stochastic setting would substantially strengthen the theoretical credibility. For instance, explaining whether standard stochastic approximation techniques could be applied to extend the result would help readers gauge the theory's relevance.
- Tabulating the numerical values from Figures 1–3 (final accuracy/loss ± CI, communication cost) would make the empirical contribution self-contained without relying on figures.
- Reporting the ε_s value used in experiments, and showing sensitivity to this parameter, would address the theory-practice gap.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No algorithm pseudocode in the main text"** — REMOVED (parser artifact). The extracted text shows a corrupted algorithm block ("\section{13: end for}") indicating the parser dropped the pseudocode. The original submission contains Algorithm 1 and Algorithm 5 (appendix); per the review guidelines, parser artifacts are not author errors.
- **"Figures missing from extracted text"** — REMOVED (parser artifact). The figures are embedded as images in the PDF (visible as `![](images/...jpg)` references). The text extraction process strips them; they exist in the original submission.
- **"Paper does not adequately differentiate from Reddi et al. (2021)"** — REMOVED per the guideline against raising missing related-work criticisms without external verification.
- **"Bound is non-intuitive / hard to parse"** — REMOVED (style/presentation nitpick that does not affect correctness).
- **"Blended optimization is a strength"** — REMOVED (conflicts with the verified weakness that this section is undeveloped; the strength is not supported by substantive content).

## Novel Insights

None beyond the paper's own contributions. The reviews sharpen the tension between a practical algorithmic idea (skip preconditioner transmission + SM3 compression) and a theory that does not cover the actual stochastic FL setting, but this is a standard theory-practice gap rather than a novel observation.

## Suggestions

1. **Temper the theory claims.** Clearly state in the abstract and introduction that the convergence analysis is for the full-batch deterministic setting and is a proof-of-concept, not a guarantee for the practical stochastic regime. Alternatively, add an informal argument or reference showing how the analysis might extend.
2. **Add numerical summary tables** (final accuracy/loss ± 95% CI, communication cost in bits) to complement the figures. This would make the empirical contribution self-contained and easier to assess.
3. **Report the ε_s setting** used in experiments and discuss whether the guarantee's dependence on ε_s affects the practical interpretation of the bound.
4. **Provide hyperparameter tuning details** (search ranges, selection criterion) either in the main text or an appendix accessible to reviewers.
5. **Either develop the Blended Optimization framework into a concrete contribution with analysis or experiments, or remove it** to avoid claiming an undeveloped idea as a contribution.

## Score and Decision

**Originality:** Moderate. The core idea (skip preconditioner transmission + SM3 compression) is a practical combination of known components, not a fundamentally new technique, but it fills a real gap.  
**Importance of research question:** High. Efficient joint adaptivity is a recognized bottleneck in cross-device FL.  
**Claims support:** Moderate. Empirical support is convincing; the theoretical claims are weakened by the full-batch assumption and the ε_s gap.  
**Soundness:** Moderate. The experiments are well-designed (20 runs, confidence intervals, diverse settings), but the theory has structural limitations.  
**Clarity:** Below average due to parser issues in the extracted text; the original likely has clear pseudocode and figures.  
**Value to community:** Moderate. Practitioners may find the efficiency recipe useful; theorists will note the analysis is preliminary.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>