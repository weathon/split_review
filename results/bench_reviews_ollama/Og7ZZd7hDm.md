Now I have a comprehensive picture of the paper. Let me write the final review.

## Summary

The paper proposes MFCGD and AdaMFCGD, two momentum-based federated compositional gradient descent algorithms for distributed nonconvex composition optimization. The algorithms combine local-SGD with STORM-type momentum-based variance reduction using three moving-average estimators (for inner function values, inner gradients, and outer gradients). AdaMFCGD extends MFCGD with a general adaptive matrix $A_t \succeq \rho I_d$ that can instantiate various adaptive learning rate schemes. The paper claims both algorithms achieve $\tilde{O}(\epsilon^{-3})$ sample complexity and $\tilde{O}(\epsilon^{-2})$ communication complexity under non-i.i.d. data, improving on prior federated composition methods.

## Strengths

- **Improved complexity rates over prior federated composition methods**: Both MFCGD and AdaMFCGD achieve $\tilde{O}(\epsilon^{-3})$ sample and $\tilde{O}(\epsilon^{-2})$ communication complexity (Theorems 1–2, Table 1), improving simultaneously on all prior federated composition methods—the previous best being Local-SCGDM with $O(\epsilon^{-4})$ sample and $O(\epsilon^{-3})$ communication complexity. This is the first federated composition method to match the single-machine lower bound rate for composition problems.

- **Clean algorithmic integration**: The algorithm (Algorithm 1) cleanly separates three momentum-based estimators ($h^m_t$, $u^m_t$, $v^m_t$) following the STORM/ProxHSGD template, and integrates them with the periodic synchronization of local-SGD. The modular structure—where the adaptive matrix is generated only at synchronization steps and held constant during local steps—is sensible and maintains the communication efficiency.

- **Explicit heterogeneity handling**: The convergence analysis explicitly accounts for non-i.i.d. data via Assumption 6 (bounded gradient divergence $\delta_f$, $\delta_g$), with the resulting bounds including a $\hat{\delta}^2$ term capturing heterogeneity effects. This ensures applicability to realistic federated settings rather than requiring i.i.d. data.

## Weaknesses

### Fatal

None.

### Major

- **Empty experiments section**: Section 6 ("Numerical Experiments") contains only subsection headers ("Robust Federated Learning" and "Task-Distributed Meta Learning") with no experimental content—no datasets, baselines, metrics, hyperparameters, or results (lines 420–426). The abstract and contributions both claim "Experimental results demonstrate efficiency of our algorithms" (line 10, line 105), but the paper provides no empirical evidence whatsoever. This is a significant gap: the theoretical complexity improvements may not translate to practical gains due to unverified constant factors, and the community has no empirical confirmation that these algorithms work as claimed.

- **Theorem parameter constraints lack constructive feasibility demonstration**: Theorems 1 and 2 impose a dense web of interdependent constraints on $c_1, c_2, c_3, \gamma, B, \Theta, n, q$ (lines 367–368, 397–398). For instance, $c_1 \geq \frac{2}{3k^3} + B$ where $B$ itself depends on $c_2/\gamma$ terms and $(c_1^2+c_3^2)/\gamma^4$, while simultaneously $c_1^2 + c_2^2 \leq \frac{(24)^4 q^2\gamma^4 L_{fg}^4 C_{fg}^4}{9\rho^4}$ and $\Theta + \frac{BC_g^2\rho^2}{(24)^2L_{fg}^2C_{fg}^2} \leq \frac{5\rho^2}{48}$. The Remark asserts "without loss of generality, let $k=O(1)$, $c_1=O(1)$..." (line 377), but this hand-waves away the circular dependencies. Without at least one explicit, numerically verified feasible parameter setting for a concrete problem instance, the theorems risk being vacuously true. While this practice is somewhat common in the optimization theory literature, the unusually complex constraint structure here makes the concern more pressing.

### Minor

- **AdaMFCGD's "same complexity" claim obscures a significant constant gap**: Theorem 1's bound for AdaMFCGD includes the factor $\sqrt{\frac{1}{T}\sum_t \mathbb{E}\|A_t\|^2}$, while Theorem 2 for MFCGD (where $A_t=I_d$) does not. The Remark after Theorem 1 bounds this factor by $2(C_f^2C_g^2+\rho)$ (line 376), which can be large when gradient magnitudes are large. The paper claims both algorithms achieve $\tilde{O}(\epsilon^{-3})$ sample complexity, which is technically correct in asymptotic notation, but the constant factor can be polynomially worse in problem-dependent constants. Since adaptive methods are motivated precisely by the setting where gradient magnitudes vary, this theoretical gap is worth acknowledging and discussing, even if it does not invalidate the asymptotic rate.

- **Table 1's "equivalent variants" phrasing creates ambiguity about baseline comparisons**: Table 1 states "i.e., $\mathbb{E}\|\nabla F(x)\|\leq \epsilon$ or its equivalent variants" (line 38–39). If any baseline uses a different stationarity measure (e.g., squared gradient norm), the complexity under a common measure could differ. The paper's own theorems use the $L_1$-norm measure $\frac{1}{T}\sum \mathbb{E}\|\nabla F(\bar{x}_t)\|$, so the ambiguity is about the baselines. While composition optimization papers typically use the norm measure, explicitly confirming each baseline uses the same measure would strengthen the comparison.

### Trivial

- The Remark after Theorem 2 says "The proof of Theorem 2 can totally follow the proofs of the above Theorem 1 with the parameter $\rho=1$" (line 406–407). This could be stated more prominently to avoid redundancy concerns.

## Nice-to-Haves

- A constructive numerical verification of feasible parameter settings for at least one problem instance would significantly strengthen confidence in the theorems.
- Sensitivity analysis of the synchronization period $q$ when the theoretically optimal $q=T^{1/3}$ cannot be set precisely (since $T$ is unknown a priori).
- Quantitative discussion of the constant-factor gap between AdaMFCGD and MFCGD, and whether it is fundamentally tied to adaptivity in the composition setting.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic Claim 3 (Stationarity measure inconsistency producing quadratic gap)**: The claim that a baseline using $\mathbb{E}\|\nabla F\|^2 \leq \epsilon$ would make its complexity $\tilde{O}(\epsilon^{-8})$ under the norm measure is an extreme interpretation. The "equivalent variants" phrasing in Table 1 is vague, but the composition optimization literature primarily uses the norm measure, and the paper's own theorems clearly use $\mathbb{E}\|\nabla F\|$. The claimed quadratic conversion is speculative without evidence that baselines actually use a different measure. Demoted to minor.

- **Harsh Critic: "unified adaptive matrix is oversold—what's unified is the placeholder for $A_t$"**: This is a subjective presentation critique. The paper does present a general framework where $A_t$ can be any matrix satisfying $A_t \succeq \rho I_d$, and provides two concrete instantiations. Whether this constitutes "unified" is a matter of framing. Removed as style nitpick.

- **Harsh Critic: "heterogeneity constants can scale with the gradient bounds—this feeds back into the complexity constants but is not reflected in the Big-O notation"**: The paper openly shows this derivation (lines 337–342) and the $\hat{\delta}^2$ term is present in the bounds. This is a known feature of the analysis, not a hidden weakness. Removed as already addressed.

- **Strength Finder: "Adaptive variant achieves same complexity as non-adaptive"**: Placed in Removed Points because this conflicts with the verified weakness that AdaMFCGD has an additional $\|A_t\|$ factor that can increase the constant. The asymptotic rate is the same, but the "no additional complexity overhead" framing is misleading about constant factors.

- **Strength Finder generic claims about "important problem" and "underdeveloped literature"**: Removed as superficial/sycophantic.

## Novel Insights

The paper's combination of momentum-based variance reduction with local-SGD for the compositional setting is a meaningful algorithmic contribution, and achieving $\tilde{O}(\epsilon^{-3})$ sample complexity matches the single-machine lower bound for composition problems. However, the entirely empty experiments section is a critical gap: a paper that makes both theoretical claims (with complex, unverified parameter constraints) and practical claims (efficiency on two tasks) but supports neither empirically raises serious concerns about real-world applicability. The AdaMFCGD variant's convergence bound carrying a large problem-dependent constant factor that grows with gradient magnitudes—the very regime where adaptivity is supposed to help—is an ironic tension that deserves deeper analysis.

## Suggestions

- Fill in the experiments section with comparisons against ComFedL, FEDNEST, and Local-SCGDM on at least the two claimed application tasks (robust FL and distributed meta-learning), including standard metrics, convergence curves, and hyperparameter settings.
- Provide at least one explicit numerically feasible parameter setting for Theorems 1–2, e.g., specify concrete values of $L_f, L_g, C_f, C_g, \sigma$ and demonstrate that the constraint system has a solution.
- Acknowledge the constant-factor gap between AdaMFCGD and MFCGD in the main text and discuss whether it represents a fundamental cost of adaptivity.

## Score and Decision

The paper makes a reasonable theoretical contribution to an important problem—improving the complexity of federated composition optimization to match single-machine rates. The algorithm design is sound and the analysis framework handles non-i.i.d. data. However, two major weaknesses significantly undermine the paper: (1) the experiments section is entirely empty despite explicit claims of empirical validation, providing no practical evidence that the algorithms work; and (2) the theorem parameter constraints are so complex and interdependent that without a constructive feasibility demonstration, the theorems could be vacuous. These issues together mean the paper's central claims—theoretical improvements and practical efficiency—lack sufficient support. The paper is promising but needs substantial revision.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>