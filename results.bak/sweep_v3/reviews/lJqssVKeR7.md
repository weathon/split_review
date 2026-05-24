Now I have all the calibration context I need. Let me synthesize the final review.

## Summary

This paper proposes **HiSo**, a Hessian-informed zeroth-order federated optimization method that accelerates convergence by learning a global diagonal Hessian approximation while strictly preserving scalar-only (dimension-free) communication. The authors first present a generalized scalar-only communication FL framework that decouples dimension-free communication from vanilla ZO-SGD, then derive HiSo's Hessian-informed update direction and its communication-free Hessian learning rule. Theoretically, they prove a convergence rate of $\mathcal{O}(\sqrt{\zeta/mR})$ under a well-approximated Hessian condition — independent of model dimension $d$ and Lipschitz constant $L$ — and extend the analysis to multiple local updates ($\tau>1$), a setting DeComFL could not handle. Empirically, across LLM fine-tuning tasks (OPT-350M to 2.7B on SST-2, QQP, SQuAD), HiSo achieves 1.4–5.4× speedup in communication rounds and 29%–80% communication savings over DeComFL while maintaining the same per-round communication cost.

## Strengths

1. **Generalized scalar-only communication framework (Section 3.3, Algorithm 1).** The paper observes that the crucial element for dimension-free FL is the scalar representation of updates, not the specific ZO-SGD rule. This decoupling is a clean conceptual contribution that enables integrating adaptive and second-order optimization methods within the scalar-only constraint.

2. **Hessian-informed update without extra communication (Section 4, Equations 8–10 and 12).** The derivation from a constrained least-squares subproblem to an update that approximates natural-gradient descent is mathematically sound, and the closed loop (the global Hessian is learned from the same scalar-representable update vectors) requires no Hessian-related communication — preserving the key advantage of ZO methods.

3. **Convergence rate independent of $d$ and $L$ under low whitening rank (Corollaries 1 and 3).** The paper introduces the notion of whitening rank $\zeta = \mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})$ and proves that HiSo achieves $\mathcal{O}(\sqrt{\zeta/mR})$ for $\tau=1$ and a rate still independent of $d$ and $L$ for $\tau>1$. This is the first result for ZO methods in FL that resolves the $\tau>1$ setting that DeComFL could not handle.

4. **Consistent empirical speedup across LLM tasks (Table 2).** HiSo reduces communication rounds by 1.4–5.4× against DeComFL under the same per-round communication budget, with higher final test accuracy (Table 3). The savings (TB → KB) against first-order methods are dramatic and practically relevant.

5. **Learned Hessian distribution confirms low effective rank (Figure 5).** The visualization of the learned diagonal $H$ across >25,000 indices shows a highly skewed long-tail distribution, providing direct evidence that the whitening rank $\zeta$ is much smaller than $d$, which supports the theoretical acceleration mechanism.

## Weaknesses

### Major

1. **The "Hessian-informed" mechanism rests on an unverified link between the learning rule and the actual Hessian.** The Hessian learning rule (Eq. 12) updates $H$ via an EMA of squared components of $\Delta x$ — essentially an RMSProp-style second-moment accumulator. The paper acknowledges this (footnote 2: "More accurately, our method resembles RMSProp") and transparently notes (line 298–299) that the well-approximated condition is an assumption for the corollaries, not a guarantee. Nevertheless, the central scientific claim — that curvature information is being captured and exploited — is not directly supported. The paper does not verify that the learned $H$ correlates with the true Hessian diagonal (e.g., on a small model where the Hessian can be computed), nor does it ablate against a non-Hessian adaptive diagonal (pure RMSProp-style scaling without any Hessian interpretation). Without such validation, the observed acceleration could be attributed to adaptive preconditioning rather than Hessian-specific curvature correction. The paper's theoretical and empirical results remain useful either way, but the claimed mechanism is less certain than the framing suggests.

2. **Small-scale FL setup limits empirical generality.** The LLM experiments use only 6 clients (2 sampled per round), which is far from the tens-to-hundreds of clients typical in FL. The CNN experiment uses 64 clients but with mild non-IID (Dirichlet $\alpha=1$). The paper does not evaluate HiSo under stronger data heterogeneity or larger client populations, making it unclear whether the communication savings and speedup hold in more challenging settings where client drift and variance are more severe. The theory includes heterogeneity terms, but the experiments do not stress-test them.

### Minor

1. **The convergence theory is conditional on an assumption that is not validated.** The clean dimension-independent rate $\mathcal{O}(\sqrt{\zeta/mR})$ depends on the well-approximated condition (Definition). The paper is honest about this and Theorem 1 does not require the condition, but the central theoretical selling point is conditional. The paper would benefit from a discussion of when this condition is likely to hold and some empirical probe (e.g., comparing learned $H$ to the true Hessian diagonal on a small CNN).

2. **Missing ablation isolating the source of acceleration.** The comparison between HiSo and DeComFL conflates two differences: the preconditioner and the perturbation distribution (isotropic vs. whitened). An ablation comparing HiSo against a version that uses the same adaptive diagonal scaling but replaces $H^{-1/2}u$ with a simple per-coordinate scaling of isotropic $u$ (i.e., an RMSProp-like ZO update) would isolate whether the benefit comes from the whitened direction or purely from adaptive magnitude scaling.

3. **The convergence criterion for "until convergence" is not precisely defined.** Table 2 reports rounds "required to fully converge" for DeComFL and rounds "needed to match DeComFL's best test accuracy" for HiSo. These are different standards, making the speedup factor depend on DeComFL's convergence criterion, which is not quantified (e.g., no tolerance threshold). Clarification is needed.

### Trivial

- The paper does not report wall-clock time or compute cost per round; a brief complexity note would help practitioners.
- The 90 million× communication savings headline (vs. first-order methods) is driven primarily by ZO's dimension-free property, not uniquely by HiSo's acceleration. This is stated in comparison with first-order baselines, but the phrasing could be clearer.

## Nice-to-Haves

- A direct empirical check of the diagonal Hessian approximation on a small model (e.g., the CNN used for Figure 5) comparing learned $H$ entries against the computed diagonal of the empirical Fisher or Hessian.
- FL experiments with more clients (20–50) and stronger non-IID partitions ($\alpha=0.1$ or 0.5).
- An RMSProp-ZO ablation as described above.
- Reporting standard deviations across multiple seeds explicitly (the ± values in Table 3 suggest multiple runs, but the paper should state this).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper does not discuss the memory overhead of storing the diagonal Hessian."** — The paper explicitly states (line 191): "the diagonal matrix approximation avoids the $d^2$ storage for the Hessian matrix." This is already addressed.
- **"The analysis assumes a fixed global Hessian $H_r$ shared across clients... clients may have different local Hessians."** — The paper uses a global EMA, and the theory includes bounded heterogeneity (Assumption 3) and bounded learned Hessian (Assumption 4). This is a standard design choice, not a flaw.
- **"The headline factor [90 million times] might be misattributed."** — The paper clearly states "compared to first-order baselines" and the comparison is between TB-level first-order communication and KB-level ZO communication. This is accurate.
- **"The synthetic simulation in Figure 4 uses a log-normal eigenvalue distribution and assumes the ideal $H$ is the diagonal of $\Sigma$."** — Figure 4 is explicitly presented as an illustrative simulation to show how the whitening transformation can reduce effective rank. It does not claim to validate the learning rule.
- **"The paper claims 'up to 90 million times communication savings' compared to first-order baselines."** — This claim is properly scoped (against first-order methods) and numerically correct given the orders of magnitude difference.

## Novel Insights

The reviewers' analysis surfaces one genuinely novel observation beyond the paper's own contributions: HiSo's Hessian learning rule (Eq. 12) is mathematically equivalent to maintaining an EMA of squared ZO update components, which is structurally identical to RMSProp's second-moment estimate of gradients. This means the method could be equivalently described as "scalar-only RMSProp for ZO-FL" without invoking Hessian theory. The paper's theoretical framework (the whitening rank analysis in Section 5.1) is what distinguishes it — it provides a rigorous explanation for why such an adaptive diagonal can accelerate ZO convergence beyond what the low-effective-rank assumption alone provides, regardless of whether the learned $H$ corresponds to the true Hessian diagonal. The conflation of the RMSProp-style heuristic with Hessian approximation is the paper's main tension: the theory explains *what kind of preconditioner would work* (one that whitens the Hessian), but the actual learning rule is justified heuristically.

## Suggestions

1. Add an experiment on a small model (e.g., the CNN) comparing learned $H$ against the computed diagonal of the empirical Fisher or Gauss-Newton Hessian to validate the "Hessian-informed" claim directly.
2. Include an ablation: HiSo vs. a version that replaces the whitened perturbation $H^{-1/2}u$ with an isotropic $u$ scaled by per-coordinate adaptive factors (pure "ZO-RMSProp" without the Hessian interpretation).
3. Scale up the FL experiments to at least 20–50 clients with stronger non-IID partitions ($\alpha = 0.1, 0.5$) to demonstrate robustness.
4. Clarify the convergence criterion used in Table 2 (what threshold or plateau rule determines "convergence") and standardize it across methods.
5. Report total run-time / wall-clock time to give a complete picture of the practical trade-offs.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZuazHmXTns.md` (PAdaMFed) | 7.60 | Stronger paper: solves a fundamental FL problem (parameter-free) with clean theory and no unverified assumptions. HiSo is narrower and its central mechanism is less validated. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/omrLHFzC37.md` (DeComFL) | 6.25 | Direct baseline. HiSo extends it with a generalized framework, Hessian-informed acceleration, and τ>1 theory, with clear empirical speedups. HiSo is the stronger paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bEqI61iBue.md` (HiZOO) | 5.67 | Single-node Hessian-informed ZO. HiSo tackles the harder FL setting with scalar-only communication and provides more extensive FL theory. Stronger contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DJRd4IQHGQ.md` (FeedSign) | 5.25 | Different approach (1-bit voting). HiSo has cleaner theoretical framing and more convincing empirical results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZAMoxm86KV.md` (FZooS) | 3.67 | Significantly weaker: questionable assumptions, limited experiments. HiSo is far more solid. |

The paper makes genuine contributions: the generalized scalar-only framework, the Hessian-informed ZO design under dimension-free communication, the $\tau>1$ convergence analysis, and consistent empirical speedups. However, the central "Hessian-informed" claim is not fully validated — the learning rule is an RMSProp-style heuristic whose connection to the actual Hessian is asserted but not proven. The theory is honest about this (Theorem 1 does not need the condition), but the paper's headline contribution is weakened by the gap. The empirical validation is convincing within its scope but the small-scale FL setup (6 clients) limits generality.

Relative to the anchors: clearly stronger than DeComFL (6.25) — it extends that framework in meaningful algorithmic, theoretical, and empirical ways. Not as strong as PAdaMFed (7.60), which solves a more fundamental problem and has cleaner theory. A score of **6.5** reflects a solid, above-acceptance-bar paper with a clear contribution tempered by a meaningful but not fatal limitation in the central mechanistic claim.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>