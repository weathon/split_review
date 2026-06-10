## Summary

This paper identifies a limitation of Maximum Mean Discrepancy (MMD) for distribution closeness testing (DCT): the same MMD value can arise from distribution pairs with substantially different RKHS norms, making MMD less informative for comparing closeness levels across multiple pairs. The authors propose Norm-Adaptive MMD (NAMMD), which rescales MMD by $4K - \|\mu_{\mathbb{P}}\|^2 - \|\mu_{\mathbb{Q}}\|^2$, so that the distance grows with the norms of the distributions. They provide theoretical analysis (asymptotic normality, concentration bounds, sample complexity, and power comparisons with MMD) and experiments on synthetic and image data.

## Strengths

1. **Figure 1 clearly demonstrates a genuine, previously unaddressed limitation of MMD.** The figure shows four distribution pairs with the same MMD (0.15) but substantially different RKHS norms, different estimator variances, and different p-values. This concretely illustrates that MMD is less informative for comparing closeness levels across multiple distribution pairs — a problem prior DCT and MMD literature had not identified.

2. **Theorem 8 provides explicit sample complexity upper bounds for the NAMMD test.** The bounds in Section 4.1 are expressed in terms of $\mathrm{NAMMD}(\mathbb{P},\mathbb{Q},\kappa)-\epsilon$ and standard normal quantiles, giving a clear theoretical characterization of the test's efficiency in both the two-sample ($\epsilon=0$) and DCT ($\epsilon>0$) settings.

3. **Table 1 shows consistent empirical improvement over MMD across 4 kernel types and 5 datasets.** The NAMMD test achieves higher mean test power than MMD under Gaussian, Laplace, Mahalanobis, and Deep kernels on blob, hdgm, higgs, mnist, and cifar. The systematic nature of the improvement (bold entries across configurations) supports the claim that the norm-adaptive rescaling helps beyond any single favorable kernel or dataset.

4. **The case studies (Section 5.2) demonstrate practical utility in evaluating model performance similarity without labels.** On ImageNet variants (Figures 3-4) and adversarially perturbed CIFAR-10 (Figure 5), NAMMD distance correlates with ground-truth accuracy/confidence margins while MMD does not capture the same ordering, and NAMMD achieves higher test power in DCT testing.

## Weaknesses

### Fatal
None.

### Major

1. **The central power-dominance guarantee uses a practically weak constant ($\varsigma \ge 1/65$).** Theorems 10 and 12, which are the paper's main theoretical justification that NAMMD outperforms MMD, include a claim that NAMMD correctly rejects when MMD fails with probability $\varsigma \ge 1/65 \approx 0.015$. A lower bound of ~1.5% means the claimed advantage could occur in as few as 1.5% of cases. While this mathematically proves strict dominance (a non-trivial result), it does **not** provide any reasonable quantification of how much better NAMMD is in practice. The paper's abstract and introduction assert "higher test power" without caveating the extreme weakness of this bound. The experiments fill this gap somewhat, but the theory — presented as the paper's headline theoretical contribution — is too loose to be practically meaningful.

2. **The NAMMD denominator is justified only heuristically.** The rescaling $4K - \|\mu_{\mathbb{P}}\|^2 - \|\mu_{\mathbb{Q}}\|^2$ is motivated by the intuition that "we separate two distributions more effectively at the same MMD distance with larger norms" (Section 3, Remark). However, no principled criterion (e.g., variance stabilization, power maximization, decision-theoretic objective) is used to derive this specific form. Any decreasing function of $\|\mu_{\mathbb{P}}\|^2 + \|\mu_{\mathbb{Q}}\|^2$ would produce similar directional behavior. The paper would be substantially stronger if it derived the scaling from a formal requirement rather than leaving it as a heuristic choice that could be varied.

### Minor

1. **The DCT experiment (Table 2) compares against total-variation-based methods only on simple discrete distributions (50 support elements),** while the paper's framing emphasizes extending DCT to complex data like images. On complex data (the case studies in Section 5.2), the comparison is only against MMD — no external DCT baseline. The paper argues that existing DCT methods cannot handle complex data, so no baseline exists for complex-data DCT. This is a reasonable defense, but the disconnect between the framing ("extends DCT to complex data") and the experimental validation (TV-DCT comparison on simple data, MMD comparison on complex data) should be acknowledged and discussed transparently.

2. **The condition in Theorem 12 ($\|\mu_{\mathbb{P}_1}\| + \|\mu_{\mathbb{Q}_1}\| < \|\mu_{\mathbb{P}_2}\| + \|\mu_{\mathbb{Q}_2}\|$) is claimed to be "often met in practice" without any supporting evidence.** If this condition fails, the theorem's conclusion may not hold. Given that the condition is crucial for extending the Theorem 10 result from two-sample testing to the DCT setting, some empirical validation or discussion of when it holds would strengthen the work.

3. **The paper's motivation somewhat conflates two distinct issues.** The paper shows that MMD is constant while p-values vary, attributing this to MMD being "less informative." The actual mechanism is that the *estimator's variance* changes with the distribution norms (since variance = $1 - \|\mu\|^2$ for the kernel values bounded by 1), while the population MMD itself is a well-defined metric. The paper modifies the distance measure rather than addressing the variance issue directly. This is a legitimate approach, but the framing occasionally slides between criticizing the population MMD and criticizing the inference procedure without clearly distinguishing the two.

### Trivial
- The condition "if $\cdot_{m}\geq C^{\prime}$" in Theorem 10 appears to have a formatting issue.
- Some equations have garbled or incomplete expressions (e.g., the asymptotic distribution under the null), though these are likely parser artifacts.

## Nice-to-Haves
- Derive the denominator from a formal criterion (e.g., variance stabilization, or maximizing a specific notion of test power).
- Empirically validate the Theorem 12 condition across datasets.
- Discuss whether the factor-of-2 range in the denominator ($[2K, 4K]$) is sufficient to produce the observed improvements, and under what conditions the denominator could be small or degenerate.

## Removed Points

These points from the inputs were removed or downgraded with justification:

1. **"Constants C' and C'' depend on distributions in unspecified ways"** (Harsh Critic) — Removed. This is standard in concentration bounds; constants depending on the underlying distribution are the norm in theoretical computer science and nonparametric statistics. Not a weakness.

2. **"No discussion of numerical stability"** (Harsh Critic) — Removed. This is a minor omission that is not standard practice to include; moved to Nice-to-Have implicitly.

3. **"Small-sample behavior of the denominator... Is this enough to produce the claimed improvements?"** (Harsh Critic) — Removed as speculative. The experimental results demonstrate improvement across multiple settings; speculating that the denominator range is too small without evidence is not a grounded criticism.

4. **Strength: "Theorem 10 proof that NAMMD strictly dominates MMD"** (Strength Finder) — The strength claim that Theorem 10 is "a rigorous mathematical demonstration that NAMMD achieves strictly higher test power under the same kernel" is kept but tempered by the weakness discussion above. The theorem *does* prove strict dominance, but the bound's weakness is the important caveat.

5. **Strength: "Theorem 12 proof that the same dominance extends to DCT"** (Strength Finder) — Same caveat as above; the quantitative weakness of the bound is the relevant framing.

6. **Various formatting/style nitpicks** (Harsh Critic) — Removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights track the paper's own analysis (identifying MMD's limitation with varying norms, proving dominance with weak constants) without adding genuinely novel observations.

## Suggestions

1. Strengthen the theoretical guarantee: replace the $\varsigma \ge 1/65$ bound with either (a) explicit power comparisons under specific distribution families, (b) conditions under which NAMMD's power strictly dominates MMD's by a practically meaningful margin, or (c) asymptotic relative efficiency calculations.

2. Derive the denominator from a formal criterion rather than heuristic intuition. Even a post-hoc justification (e.g., "this specific form stabilizes the variance across distribution pairs with different norms") would substantially improve the paper's theoretical foundations.

3. Validate the condition $\|\mu_{\mathbb{P}_1}\| + \|\mu_{\mathbb{Q}_1}\| < \|\mu_{\mathbb{P}_2}\| + \|\mu_{\mathbb{Q}_2}\|$ empirically on the datasets used in the paper, and discuss cases where it might fail.

4. Acknowledge the disconnect between the complex-data framing and the TV-DCT comparison more explicitly, and explain why MMD is the natural baseline on complex data.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>