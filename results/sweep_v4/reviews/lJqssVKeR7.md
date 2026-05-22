Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes **HiSo**, a Hessian-informed zeroth-order (ZO) federated optimization method for fine-tuning LLMs. The key innovations are: (1) a generalized scalar-only communication FL framework that decouples dimension-free communication from ZO-SGD, enabling integration of more powerful optimizers; and (2) the HiSo algorithm itself, which learns a global diagonal Hessian approximation from the scalar gradient values already transmitted, providing curvature-aware preconditioning without any additional communication cost. Theoretically, under a "well-approximated Hessian" condition, the paper proves convergence rates independent of model dimension \(d\) and Lipschitz constant \(L\), and extends the analysis to multiple local updates (\(\tau>1\)) — a setting prior ZO-FL work could not handle. Empirically, HiSo achieves 1.4–5.4× speedups over DeComFL across OPT-350M/1.3B/2.7B on SST-2, QQP, and SQuAD.

## Strengths

- **Elegant conceptual insight (Section 3.3, Algorithm 1):** The paper observes that dimension-free communication in ZO-FL only requires updates to be representable by scalars and seeded random directions, not ZO-SGD specifically. This generalized framework is cleanly articulated and opens the door to incorporating optimizers beyond vanilla ZO-SGD.

- **Hessian learning at zero communication cost (Section 4.2, Eq. 12):** The method repurposes the already-communicated global gradient scalars to build an exponential-moving-average diagonal preconditioner. Both server and clients reconstruct the same \(H\) without transmitting any second-order information — this is a genuinely clever and practical design.

- **First convergence analysis for ZO-FL with \(\tau > 1\) (Corollary 3):** Prior DeComFL analysis was restricted to one local step per round. HiSo's extension to multiple local updates is a genuine theoretical advance, and the identification that low-effective-rank alone is insufficient (the whitening property helps) is insightful.

- **Consistent empirical speedups across multiple LLMs and tasks (Table 2):** HiSo reduces communication rounds by 1.4–5.4× relative to DeComFL across three model sizes and three tasks, with higher final accuracy. The results are clean, the improvements are meaningful, and the per-round communication cost is identical to DeComFL.

- **Transparent discussion of theoretical limitations (Section 5.2 Remarks):** The paper explicitly acknowledges that the well-approximated condition "is hard to determine... in the context of LLMs" and that failure degrades to DeComFL performance. This honesty about the scope of the theory is commendable.

## Weaknesses

### Major

- **The central theoretical advance depends on an assumption with weak empirical validation.** The claimed dimension-free convergence rate (Corollaries 1–3) hinges entirely on the "well-approximated Hessian" condition (Definition, Eq. 17), which requires \(\mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2}) \le \zeta\) with \(\zeta \ll d\). The paper provides two pieces of supporting evidence: a synthetic log-normal eigenvalue simulation (Figure 4) and a CNN MNIST experiment showing a long-tailed Hessian distribution (Figure 5, right). Neither directly measures the whitening trace \(\zeta\) during LLM fine-tuning — the very setting the paper targets. The condition must hold *uniformly* across iterations and for the surrogate \(\Sigma_{r,k}\), which is itself loosely defined as "a PSD matrix that upper-bounds Hessian at \(x_{r,k}\)." The paper's own acknowledgement that this is "hard to determine... in the context of LLMs" correctly characterizes the gap: the headline theoretical result is more a plausible explanation for observed fast convergence than an established guarantee for the proposed algorithm.

### Minor

- **Missing ablation that isolates the Hessian preconditioner.** The paper never runs HiSo with the Hessian update disabled but everything else identical (i.e., \(H_r \equiv I\) while keeping the generalized framework and model-reset mechanism). Since Corollary 2 essentially says this reduces to DeComFL, such an ablation would cleanly show that the empirical speedup comes from the Hessian preconditioner and not from other algorithmic differences (e.g., the model-reset mechanics or improved implementation). This is the most natural experiment to support the paper's central claim.

- **Conceptual subtlety around the "well-approximated" definition is insufficiently explained.** The paper states: "If \(H\) is the perfect approximation of \(\Sigma\), then \(\zeta = d\)." This means the "perfect" Hessian approximation gives the *worst* (largest) whitening trace, making the well-approximated condition trivially fail. The paper's follow-up ("\(H \approx \mathrm{Diag}(\Sigma + \epsilon\mathbf{1})\) is a more effective inverse value") hints at a Wiener-filtering intuition but does not clarify why a "Hessian-informed" method should deliberately avoid approximating the Hessian eigenvalues. The tension between the "Hessian-informed" framing and the fact that the condition requires \(H\) to *not* be close to \(\Sigma\) (in the eigenvalue sense) is never resolved, which weakens the intuitive motivation for the algorithm's design.

- **Communication cost comparison in Table 2 favors HiSo by design.** The speedup metric reports rounds for HiSo to *match DeComFL's best accuracy*, not to reach its own best accuracy. Since HiSo's final accuracy is higher (Table 3), the reported round counts are a lower bound on its full convergence cost. The per-round costs are identical, so the speedup in total communication to reach each method's *own* optimum would be smaller than the reported ratios. This does not invalidate the results, but the framing inflates the advantage.

- **Learning rate choices in Corollary 1 vs. Theorem 1 constraints.** Theorem 1 requires \(\eta \le \min(\frac{\beta_\ell}{mL}, \frac{1}{8\bar{\rho}}, \frac{\beta_\ell}{4(\tau-1)}) \sqrt{\frac{1}{L(d+2)}}\). Corollary 1 takes \(\eta = \sqrt{m\beta_\ell/\bar{\rho}R}\) for \(\tau=1\). The factor \(\sqrt{1/(L(d+2))}\) is not obviously absorbed into this expression; it would require the well-approximated condition to tighten \(\bar{\rho}\) sufficiently. The paper does not verify compatibility for meaningful ranges of \(R\). If the constraint is violated, the convergence bound of Theorem 1 does not apply and the claimed rate in Corollary 1 is unsupported.

- **Ambiguity in the Hessian update equation.** Equation 12 uses \([\Delta x_{r,0}]^2\) in the main text, while the earlier formulation in the algorithm description uses \(|\Delta x_{r,\tau}^{(i)}|^2\) with client index \(i\). It is unclear whether the global aggregated \(\Delta x_r\) or per-client \(\Delta x_{r,k}^{(i)}\) is used, and whether clients can locally reconstruct \(H\) without extra communication. The paper says "the vector \(\Delta x_{r,k}\) can be represented by scalars" but the notation conflates client-specific and global quantities. The detailed algorithm table deferred to Appendix D should clarify this, but the main text should be unambiguous.

- **Small FL system (6 clients, 2 sampled per round).** While common in LLM fine-tuning work due to computational constraints, this setting does not test robustness to the client heterogeneity and sparse participation patterns typical of larger FL deployments. Scaling to 50–100 clients would strengthen the empirical evaluation.

### Trivial

- The E[‖u‖²_Σ] → 2d entry in Table 1 under the "Low Effective Rank" row for the Hessian-informed case is confusing: it appears to be a typo intended for a column header or the L-smoothness row.

## Nice-to-Haves

- Adding momentum (as the paper mentions in a footnote) would be a natural, low-effort extension that likely yields further speedups.
- Measuring the actual whitening trace \(\zeta\) via Hutchinson's method on smaller models during training would directly validate the central theoretical assumption.
- Comparing to FL+LoRA (first-order fine-tuning with low-rank adapters) in the main text would ground the practical trade-off between ZO's extreme compression and LoRA's moderate compression with higher accuracy.

## Removed Points

The following criticisms from the Harsh Critic were removed or significantly weakened after verification:

- **Missing LoRA baseline comparison (Issue 3 and "Missing Experiments"):** The paper states in Section 6 that "other FL+PEFT baselines" are presented in Appendix E. Since the appendix is stripped by the parser, we cannot confirm whether this comparison is adequate, but the claim that it is *entirely omitted* is factually incorrect based on the main text. Removed.

- **"No comparison to HiSo without Hessian update (H=I)" (partially addressed):** While technically correct that this specific ablation is missing from the main text, Corollary 2 notes that DeComFL is exactly HiSo with \(H_r \equiv I\). DeComFL *is* this ablation. The critic's framing is misleading. However, the paper does not include a *within-paper* control where only the Hessian update is toggled (keeping the generalized framework, seeds, etc. identical). The milder version of this criticism is retained as a Minor weakness.

- **"Well-approximated condition is a strong unverified assumption" as a *fatal* flaw:** The critic framed this as fatal. However, the paper openly acknowledges the assumption's limitations, Theorem 1 does not require it, and the paper states performance degenerates to DeComFL otherwise. This is a significant limitation but not a fatal invalidation — downgraded to Major.

- **Criticism about $\Sigma_{r,k}$ not being formalized:** The paper describes $\Sigma_{r,k}$ as "a PSD matrix that upper-bounds Hessian at $x_{r,k}$," which is clear enough for a convergence analysis context. Removed as overly pedantic.

- **Criticism about FedAvg converging in "far fewer rounds":** The paper correctly reports total communication cost (TB for first-order vs. KB for ZO methods), not just per-round cost. The extreme ratio (up to 90 million times) is derived from total costs, not per-round. Removed as factually incorrect.

- **Criticism about "missing FedZO comparison in Figure 5":** FedZO's communication cost is dimension-dependent and thus not directly comparable in a per-round-cost-equal setting. The paper compares HiSo to DeComFL because they share identical per-round communication, which is the fair comparison. Removed.

## Novel Insights

The two reviews largely converge on the paper's strengths and weaknesses but frame them differently. An observation that emerges from the synthesis: the paper's use of "Hessian-informed" terminology creates an expectation of curvature approximation that the actual algorithm does not deliver. The well-approximated condition requires \(H\) to make \(\mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) small, which means \(H\) should be *large* in directions where \(\Sigma\) has small eigenvalues — the opposite of what a Hessian eigenvalue approximation would do. The algorithm (Eq. 12) actually tracks an RMSProp-style running average of squared gradient components, which is known to behave like a diagonal Fisher information preconditioner. The paper would benefit from reframing around this connection rather than straining to call it "Hessian-informed." This reframing would also explain the whitening behavior: RMSProp's scaling naturally compresses directions with low gradient variance (equivalently, low curvature), which is precisely what the well-approximated condition encodes.

## Suggestions

1. **Add the \(H_r \equiv I\) ablation.** Run HiSo with the Hessian update disabled (keeping everything else) and compare to HiSo. This is the single most important missing experiment and would directly confirm that the speedup is due to curvature information.

2. **Validate the whitening trace \(\zeta\) empirically.** For OPT-125M on SST-2, approximate the Hessian diagonal via Hutchinson's method and compute \(\mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) at several training points. Even a rough measurement would significantly strengthen the theoretical claims.

3. **Clarify the well-approximated condition's meaning.** Revise Section 5.1 to explain why "perfect" eigenvalue approximation gives \(\zeta = d\) (bad) while the desired behavior is more like a diagonal Fisher/RMSProp preconditioner. Consider renaming the condition to "well-conditioned whitening" or similar to avoid confusion.

4. **Reconcile Corollary 1 and Theorem 1 learning rate constraints.** Either show that the well-approximated condition implies \(\sqrt{1/(L(d+2))} \le \sqrt{m\beta_\ell/\bar{\rho}R}\) for practical \(R\), or revise the theorem to remove the \(\sqrt{1/(L(d+2))}\) factor.

5. **Recompute Table 2 with symmetric metrics.** Report either (a) rounds/communication for each method to reach its own best accuracy, or (b) both methods' accuracy at a fixed communication budget. This avoids the asymmetric framing that currently inflates the speedup.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/omrLHFzC37.md` (DeComFL) | 6.25 | Direct predecessor with cleaner theory (no extra assumption) but less algorithmic novelty. This paper adds Hessian-informed ZO but the theory is on shakier ground. Comparable quality, slightly weaker on theory. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZAMoxm86KV.md` (FZO with trajectory surrogates) | 3.67 | Weaker paper — assumptions not standard in FL, computation cost unaddressed. Current paper is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZuazHmXTns.md` (PAdaMFed) | 7.60 | Stronger paper — problem-parameter-free with rigorous theory. Current paper has weaker theoretical guarantees due to unverified assumption. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EcetCr4trp.md` (FL feature learning theory) | 5.75 | Comparable — both have real contributions but significant limitations in scope. Current paper's practical algorithm is stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DJRd4IQHGQ.md` (FeedSign) | 5.25 | Similar level — both propose clever communication-efficient ZO methods with some theoretical caveats. This paper has stronger theory. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IsHWcsk4Fz.md` (FedADM) | 3.00 | Weaker paper — limited novelty. Current paper is clearly stronger. |

The paper presents a genuinely novel algorithm with a clever design insight and clean empirical results. The main weakness is that the headline theoretical claim depends on an assumption with weak empirical support. This places it below top-tier work (6+) where the theory is well-grounded, but meaningfully above weak papers (3-4). It is comparable to the DeComFL paper it builds upon, with slightly more algorithmic novelty but a less air-tight theoretical contribution. Score of **5.5** reflects a solid paper with real contributions that falls short of the strongest work due to the gap between its theoretical claims and their verification.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>