Now I have a thorough understanding of the paper. Let me synthesize the final review.

Key observations from my reading:

1. **Theorem 5 (RJSD ≤ JSD)**: The paper states this at line 204-211 as Theorem (th:lower_bound). There is NO proof provided in the paper - no reference to an appendix, no inline proof. This is a significant gap, as the entire variational estimation framework depends on this.

2. **The empirical evidence about bias**: The paper states (line 317) that "when the kernel bandwidth approaches zero and the number of samples n approaches infinity, the kernel-based entropy converges to the classical Shannon entropy" citing Bach 2022. So at small bandwidth, population RJSD should approach JSD from below if Theorem 5 holds. But Figure 1a shows the kernel-based estimator exceeding JSD at small bandwidth, which the paper attributes to finite-sample bias. The harsh reviewer's concern about whether the *population* RJSD truly satisfies the bound for all kernels has some merit—since the paper provides no proof.

3. **The MMD comparison**: The p=1 power-series RJSD equals (1/4)MMD²_{κ²}. The paper's experiments compare RJSD(p=10) against MMD_{κ} methods (MMD-Split, MMD-Deep, MMD-Fuse), all of which use kernel κ, not κ². So the comparison involves a different kernel. However, the key table (Table 1) compares RJSD-Fuse against MMD-Fuse, both using the same FUSE testing framework. The comparison is fair in the sense that both methods are competing within the same testing framework. The question of whether the gains come from higher-order terms or from using κ² instead of κ is valid but nuanced.

4. **Domain adaptation**: The paper explicitly scopes this as testing RJSD vs MMD within JAN framework (line 490). No standard deviations are reported. The comparison is narrow.

5. **Consistency of regularized estimators**: The paper only provides consistency for the kernel-based estimator (Proposition 2, citing Bach 2022) but not for the power-series or Fourier features estimators that are actually used in practice.

6. **p=3 vs p=10**: The paper uses p=10 for two-sample testing and p=3 for domain adaptation without clear justification.

Let me now write the final review.</think>Now I have thoroughly read and verified the key claims. Let me write the final consolidated review.

## Summary

The paper introduces the Representation Jensen-Shannon Divergence (RJSD), a kernel-based divergence between probability distributions defined as the quantum Jensen-Shannon divergence of uncentered covariance operators in a reproducing kernel Hilbert space. The paper proposes three estimators (kernel-based, power-series, and Fourier features), proves that the first-order power-series approximation equals (1/4)MMD² with the squared kernel, and leverages a claimed lower bound of RJSD on classical JSD to derive a variational estimator. Experiments demonstrate improved performance over MMD-based methods in two-sample testing and domain adaptation.

## Strengths

- **Natural and well-motivated formulation**: RJSD extends the kernel mean embedding / MMD framework by using the quantum JSD of uncentered covariance operators, avoiding Gaussian assumptions in the RKHS (unlike prior kernel-based divergences such as log-determinant, kernel KL, and kernel Bures). The unit-trace assumption under bounded kernels (κ(x,x)=1) cleanly enables the von Neumann entropy definition (Section 3, Definition 1).

- **Rigorous proof connecting RJSD to MMD**: The theorem proving that p=1 power-series RJSD equals (1/4)MMD²_{κ²} (Section 5.1, lines 267–283) is correct and complete. This establishes an explicit algebraic relationship showing RJSD generalizes MMD to higher-order statistics.

- **Thorough identification and mitigation of the upward bias problem**: The paper clearly diagnoses why the kernel-based estimator can exceed log(2) at small bandwidths (asymmetric sample sizes across entropy terms, Section 5.2, lines 227–231) and proposes two principled regularized estimators (power-series truncation and Fourier features) with clear mechanistic explanations of how regularization works (the maximum entropies at each order are bounded comparably across the three terms, Figure 2/4 discussion).

- **Strong empirical results in two-sample testing**: RJSD-Fuse achieves 1.000 test power on CIFAR-10 vs. CIFAR-10.1, outperforming MMD-Fuse (0.937), MMD-Agg (0.883), and RJSD-Deep outperforms MMD-Deep (0.868 vs. 0.744) in Table 1, with 1000 repetitions. The order comparison (Figure 5) shows consistent improvement from p=1 to p=10.

- **Variational JSD estimation outperforms neural estimators**: In the Cauchy distribution experiment (Figure 6), RJSD-based variational estimators track the true JSD with lower variance than MINE, NWJ, InfoNCE, and CLUB.

## Weaknesses

### Fatal

- **Theorem 5 (RJSD ≤ JSD) is stated without proof and is the paper's load-bearing theoretical claim.** The inequality D_JS^H(P,Q) ≤ D_JS(P,Q) (lines 204–211) is presented as a theorem with no proof in the main text, no reference to an appendix, and no citation of a prior result. This claim is foundational: without it, the variational estimator in Section 5.2 does not provide a variational lower bound on classical JSD—it simply optimizes a kernel-dependent quantity with an uncontrolled relationship to JSD. The paper text at line 212 explicitly states "Theorem 5 can be used to obtain a variational estimator" and the variational estimator definition (line 375) and its entire presentation (lines 370–386) depend on RJSD being a lower bound. Given that the paper's own Figure 1a shows the kernel-based RJSD estimator exceeding the true JSD value (0.5×log(2)) at small bandwidth, and the paper attributes this to finite-sample bias, the *population* behavior of RJSD relative to JSD for general kernels is not empirically settled by the paper's experiments. A proof, or an explicit statement of conditions under which the bound holds, is essential for the paper's core contribution to stand.

### Major

- **The regularized estimators (power-series and Fourier features) that are actually used in all experiments lack consistency guarantees.** Proposition 2 (citing Bach 2022) provides convergence bounds for the *kernel-based* population estimator—the very estimator the paper identifies as having severe upward bias in practice. The power-series estimator introduces truncation error, and the Fourier features estimator introduces both approximation error and randomness from feature sampling. Without consistency analysis, it is unclear what population quantity these estimators converge to, whether they maintain the RJSD ≤ JSD lower bound (if that bound even holds), and at what rate. The paper acknowledges this gap in the conclusion (lines 561: "Future work will focus on further exploring the bias and variance of the RJSD estimator"), but the practical contribution rests on these very estimators.

- **The two-sample testing comparison does not isolate the contribution of higher-order terms from the effect of the squared kernel.** Since p=1 power-series RJSD equals (1/4)MMD²_{κ²}, comparing RJSD(p=10) against MMD_{κ} methods conflates two design choices: using the squared kernel κ² vs. the original kernel κ, and incorporating higher-order terms. The paper compares RJSD-Fuse (which implicitly uses κ² via the power-series expansion) against MMD-Fuse (which uses κ), making it impossible to determine how much of the performance gain comes from switching kernels vs. adding higher-order terms. A comparison of RJSD(p>1) against MMD_{κ²} (using the same squared kernel) would properly isolate the contribution of the higher-order statistics.

### Minor

- **Inconsistency in the choice of approximation order p across experiments.** The paper uses p=10 for two-sample testing but p=3 for domain adaptation (line 490), with no justification for this discrepancy. If p=10 is empirically optimal for testing, why use p=3 for adaptation? This matters because the paper positions RJSD as a general-purpose divergence, and the optimal p may be task-dependent. Sensitivity analysis of p across tasks would strengthen the paper.

- **Domain adaptation results lack standard deviations or significance tests.** The improvements of RJSD over MMD are modest (1–4 percentage points on Office-31 and Office-Home; 3.8 points on ImageNet-R). Without standard deviations or confidence intervals, it is unclear whether these differences are statistically meaningful. However, the paper explicitly scopes this comparison ("our primary objective is to evaluate RJSD's effectiveness...and compare its performance with the well-known MMD," line 490), so this is a minor rather than major concern.

- **The claim that RJSD "extends MMD to higher-order statistics of the kernel matrices" (line 285) is somewhat imprecise.** The higher-order terms in the power series are higher-order polynomial functions of the same kernel matrix entries κ(x_i,x_j), not higher-order moments of the data distribution in input space. This could be clarified to avoid misleading interpretation.

### Trivial

None.

## Nice-to-Haves

- Consistency analysis for the power-series and Fourier features estimators (bias, variance, convergence rate as functions of p and D).
- Comparison of RJSD(p>1) against MMD_{κ²} with the same squared kernel to isolate the contribution of higher-order terms.
- Standard deviations for domain adaptation results.
- A systematic study of how performance varies with the approximation order p across both two-sample testing and domain adaptation tasks.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic's claim that "Theorem 5 faces a priori plausibility concerns from its own empirical evidence (Figure 1a)."** Expanded: The critic argues Figure 1a shows RJSD exceeding JSD, casting doubt on the population bound. However, the paper explicitly attributes this to *finite-sample upward bias* (lines 227–231, 344), not to a violation of the population bound. The population RJSD at small bandwidth should approach JSD per Bach (2022) citation (line 317). The empirical overshoot is a well-documented estimator artifact, not evidence against the theorem. The *real* criticism is the missing proof, not the empirical counter-evidence, which the paper already explains away plausibly.

- **Harsh Critic's claim that "the regularized estimators maximize an uncontrolled approximation, invalidating the variational estimation contribution."** This depends entirely on Theorem 5 being false. If Theorem 5 holds, maximizing RJSD does give a variational lower bound on JSD. The missing proof is the real issue; this is downstream of that.

- **Harsh Critic's claim that domain adaptation experiments are "too narrow" because JAN is outdated and modern methods (DANN, CDAN, MDD, SHOT) are not compared.** The paper explicitly scopes this comparison as RJSD vs MMD within JAN (line 490: "our primary objective is to evaluate RJSD's effectiveness in reducing divergence between distributions in deep learning applications and compare its performance with the well-known MMD"). The paper is not claiming to advance domain adaptation; it is validating that RJSD can replace MMD as a divergence measure. Comparing against SOTA domain adaptation methods would be scope creep.

- **Strength Finder's claim #2: "RJSD is a lower bound on classical JSD, enabling variational estimation" as a strength.** This is the paper's claim but it is *unproven* (see Fatal weakness). A claimed strength that directly conflicts with a verified weakness should be dropped. The theoretical connection exists only if Theorem 5 is true, which has not been established.

- **Strength Finder's claim #3 (supporting): "RJSD strictly generalizes MMD to higher-order statistics" — this uses "strictly" which overclaims.** It is correct that p=1 gives (1/4)MMD²_{κ²} and p>1 adds terms, but "strictly generalizes" implies the higher-order terms always provide additional useful information, which is not proven. The p=1 case uses κ² not κ, so this is not a straightforward generalization of MMD_{κ}.

- **Harsh Critic's Section 3 note about κ² needing to be characteristic for positivity.** The paper already states this clearly at line 187: "Let κ² be a characteristic kernel." The critic asks for "more emphasis" but the theorem statement is explicit. This is a nitpick.

- **Harsh Critic's note that "the higher-order terms in the power series are higher-order polynomial functions of the same kernel matrix, not higher-order moments of the data distribution in input space."** This is a valid precision point but already captured as a Minor weakness above about the imprecise language. The critic's framing as a deeper problem is overblown.

## Novel Insights

The paper's most insightful contribution is the explicit algebraic derivation showing that the first-order power-series truncation of RJSD exactly recovers (1/4)MMD²_{κ²}, placing RJSD and MMD on a common scale where RJSD adds higher-order polynomial terms of the same kernel matrix. However, the practical implications of this relationship are clouded by two intertwined design choices—the shift from kernel κ to kernel κ² and the addition of higher-order terms—that the experiments do not disentangle. If RJSD's gains primarily come from using κ² (which concentrates mass differently than κ), then a simpler MMD_{κ²} baseline may capture much of the benefit without the complexity of the power-series framework.

## Suggestions

- Provide a proof of Theorem 5 (RJSD ≤ JSD) or clearly state the conditions under which it holds. If the bound is conditional on kernel properties (e.g., bandwidth sufficiently small, or the kernel satisfying certain spectral decay conditions), make this explicit rather than claiming it holds "for all probability measures."
- Compare RJSD(p>1) against MMD²_{κ²} (same base squared kernel) to measure the true marginal value of higher-order terms.
- Add consistency analysis for the power-series and Fourier features estimators—specify what population quantity they converge to and at what rate.

## Score and Decision

The paper introduces a natural and interesting divergence measure with genuine empirical strength (especially in two-sample testing), but its central theoretical pillar——that RJSD is a lower bound on classical JSD——is stated as a theorem without proof and with no reference to where a proof might be found. Since the variational estimation framework (a major claimed contribution) rests entirely on this bound, this is a fatal gap. Without it, the paper offers an empirically effective but theoretically ungrounded divergence. The consistency gap for the practical estimators and the conflation of kernel choice with higher-order terms in the experimental evaluation are additional significant concerns but not fatal on their own.

Originality: The formulation is clean and novel; the connection to MMD via the power series is elegant but the core theoretical claim is unproven.
Importance: The problem of divergence estimation is important; the results on two-sample testing are strong.
Claims support: The empirical results support practical utility, but the theoretical foundation (Theorem 5) is unsupported.
Experiments: Strong in two-sample testing; narrow and incomplete in domain adaptation.
Clarity: Well-written with careful discussion of estimator bias.
Value: Potentially high if theoretical gaps are filled.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>