- Decision: Accept
- Avg Score: 5.67
- Scores: 8, 8, 1
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper studies DP-FTRL (correlated noise) for private learning. It provides asymptotic analyses for mean estimation and linear regression, establishing that DP-FTRL's asymptotic suboptimality scales with the effective dimension $\edim$ rather than the ambient dimension $d$. It derives closed-form near-optimal noise coefficients, proposes \ourprivftrl (a single-parameter Toeplitz family), and validates empirically on CIFAR-10 and StackOverflow, matching or outperforming prior state-of-the-art at much lower computational cost.

## Strengths

1. **Sharp theoretical separation for linear regression**: Theorem 2 provides matching upper (via \ournoisyftrl) and lower (for all noise coefficients) bounds on asymptotic suboptimality, showing that DP-SGD's error scales with ambient dimension $d$ while DP-FTRL's error scales with effective dimension $\edim = \tr(\mathbf{H})/\|\mathbf{H}\|_2$. When eigenvalues decay rapidly ($\edim \ll d$), this yields a large polynomial improvement. The tightness is corroborated by simulation (Fig. 2, slopes nearly match theoretical predictions).

2. **Analytical closed-form noise coefficients for mean estimation**: Theorem 1 gives the exact optimal noise coefficients $\beta_t^\star = (-1)^t \binom{1/2}{t} (1-\eta)^t$ for mean estimation and proves the asymptotic suboptimality $\Theta(\eta^2 \rho^{-1}\log^2(1/\eta) + \eta \sigma^2)$ vs. DP-SGD's $\Theta(\eta \rho^{-1} + \eta \sigma^2)$, establishing strict improvement at all learning rates $\eta$. The anti-correlated interpretation is physically intuitive and correctly attributed.

3. **Computationally efficient anytime mechanism**: \ourprivftrl uses $O(1)$ generation cost and $O(T)$ per-step cost (via Toeplitz structure), compared to the $O(T^3)$ generation and $O(T^2)$ per-step cost of prior state-of-the-art (Multi-Epoch). Table 3 gives a clear comparison. The empirical results show it matches or slightly outperforms ME on StackOverflow while being far more efficient.

4. **Empirical validation on two modalities**: On CIFAR-10, \ourprivftrl reaches 69.26% at $\varepsilon=10$, nearly matching ME (70.83%) and outperforming all other anytime mechanisms. On StackOverflow it surpasses ME across all $\varepsilon$ by $\approx 0.3$ pp. These results demonstrate that the theoretical insights translate to practical gains.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming "exponential" separation**: The paper repeatedly states "exponential separation between \noisysgd and \noisyftrl" (subsection heading, line 343) and "exponentially better" (line 345). The explicit example given (eigenvalues $(1, 1/d, \ldots, 1/d)$) yields a ratio of $d / \log^2 d$ — a **polynomial** improvement in $d$, not exponential. Even in the strongest case (constant $\edim$), the ratio is $\Theta(d / \log^2 d)$. This is an unbounded/polynomial separation, not exponential. The contribution is strong enough without this mischaracterization; the inflated language risks misleading readers and should be corrected throughout.

### Minor

- **Finite-time bound requires a restrictive condition that depends on $d$**: The finite-time guarantee for \ourprivftrl (Section 2.3) applies only when $T \ge \tilde\Omega(\kappa^2 \edim^2 d / \rho)$. While the bound itself (lines 438-441) correctly replaces $d$ with $\edim$ in leading terms, the prefactor condition scales with $d$, meaning the favorable dimension-dependence only kicks in at a very large $T$. The paper acknowledges the asymptotic origin ("We leverage these asymptotic results") but the gap between the clean asymptotic claim and the practical finite-$T$ regime deserves more explicit discussion, particularly since deep learning experiments use multiple epochs (line 561 notes this difference in setup).

- **No ablation of the $\nu$ parameter**: The proposed method has one tunable parameter $\nu$, and the paper only states it "is tuned." Given the claim that Eq. (8) with a single parameter captures near-optimal behavior, a sensitivity analysis (accuracy vs. $\nu$ at fixed $\varepsilon$) would strengthen the practical claim and confirm robustness.

- **Finite-time bound condition conflates $d$ and $\edim$ in the presentation**: The paper states "the dimension $d$ in DP-SGD's bound effectively becomes $\kappa \edim / T$ for DP-FTRL" (line 445). This is a helpful summary, but the actual comparison requires the reader to parse dense expressions (lines 428-443) and the condition $T \ge \tilde\Omega(\kappa^2 \edim^2 d / \rho)$ that rescales the comparison regime. The claimed simplification is partially misleading as stated.

### Trivial
None.

## Nice-to-Haves
- An ablation plot of accuracy vs. $\nu$ for a fixed $\varepsilon$ on CIFAR-10 would confirm robustness of the single-parameter family.
- Reporting wall-clock time or memory usage for the deep learning experiments (beyond the $O(T)$ vs $O(T^3)$ asymptotic comparison) would strengthen the practical efficiency claim.

## Removed Points

These points were raised in the reviews but are removed or corrected here for the reasons stated:

1. **"Finite-time bound still contains $d$ term (e.g., $d\edim/(\rho T^2)$)"** — REMOVED (factually incorrect). The actual bound for \ourprivftrl at lines 438-441 contains no $d$ term; $d$ appears only in the SGD bound and the condition for the bound to apply. The critic misread the bound.

2. **"Convex program overstates contribution in abstract"** — REMOVED. The abstract says "as the solution to a convex program for general convex functions," which accurately describes the bound in Theorem 3. The paper explicitly states (line 511) that using the optimized program for algorithm design is left for future work. No overstatement.

3. **"Missing sensitivity analysis for finite $T$"** — REMOVED. Table 2 explicitly gives $\gamma_T(\bfbeta)^2 = \log(1/\nu)$ for $\nu$-noisyftrl, which is the finite-$T$ sensitivity.

4. **"Privacy amplification makes DP-SGD comparison unfair"** — REMOVED. The paper already acknowledges this (lines 591, 606) and notes that without amplification the gap would be larger. The comparison is properly caveated.

5. **"Hyperparameter selection for ME may be unfair"** — REMOVED. Speculative; no evidence that prior work's hyperparameters were inappropriate.

6. **"Anti-PGD derivation not justified"** — REMOVED. The paper states the result is proved in the appendix (\S\ref{sec:two-step-noise}), which is standard practice.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an unstated limitation or implication that the authors themselves missed.

## Suggestions

1. **Replace all instances of "exponential separation" with accurate language.** Suggested alternatives: "polynomial separation," "unbounded improvement," "improvement from dimension $d$ to effective dimension $\edim$," or "dimension-free asymptotics."
2. **Add a brief discussion of the finite-time condition.** Clarify that the bound itself replaces $d$ with $\edim$ but requires $T \ge \tilde\Omega(\kappa^2 \edim^2 d / \rho)$ — explain why this condition arises and whether it is satisfied in typical deep learning settings.
3. **Add an ablation plot** for $\nu$ at a fixed $\varepsilon$ on CIFAR-10 to confirm the method is not overly sensitive to this single tunable parameter.
