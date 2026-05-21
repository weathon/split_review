Now I have enough calibration data. Let me synthesize the final review.

Here's my calibration summary:

**Round 1 anchors:**
- DeComFL (omrLHFzC37): avg 6.25 — the direct predecessor; accepted with scores 5,6,6,8
- FedZO-surrogate (ZAMoxm86KV): avg 3.67 — rejected; fundamental issues
- FeedSign (DJRd4IQHGQ): avg 5.25 — rejected; novelty concerns

**Round 2 anchors:**
- LOZO (9BiVepgmWW): avg 7.00 — accepted; ZO + LLM fine-tuning, low-rank structure
- AdaFisher (puTxuiK2qO): avg 6.25 — accepted; second-order optimizer
- FOSI (NvbeD9Ttkx): avg 6.25 — accepted; hybrid first/second order

**Bracketing:** Round 1 placed the paper between ~5.5 and 7.5. Round 2 narrows: HiSo is clearly above DeComFL (6.25) since it directly improves it, but below LOZO (7.00) whose core idea is more fundamental and experiments more extensive. HiSo sits around 6.5 — a solid accept.

---

## Summary
This paper proposes HiSo, a federated zeroth-order (ZO) optimization algorithm that learns a global diagonal Hessian approximation from the scalar updates already transmitted in the DeComFL dimension-free communication framework. By using this learned preconditioner to guide ZO perturbation directions, HiSo accelerates convergence while strictly preserving scalar-only communication. The paper provides convergence guarantees under a well-approximated Hessian condition, shows that the rate can become independent of model dimension and Lipschitz constant, and demonstrates 1.4–5.4× communication-round speedups over DeComFL on OPT-model LLM fine-tuning benchmarks.

## Strengths
- **Clever algorithmic design with no extra communication cost**: The core idea — learning a diagonal Hessian approximation from the squared scalar updates that are already communicated — is genuinely elegant. The server and clients can independently reconstruct the same global preconditioner \(H_r\) without transmitting any additional Hessian-related information (Section 4.2, Eq. 12). This directly addresses the tension between wanting curvature information and preserving dimension-free communication.

- **Empirical speedup over the prior state-of-the-art**: Across OPT-350M, 1.3B, and 2.7B models on SST-2, QQP, and SQuAD, HiSo reaches DeComFL's best accuracy in 1.4–5.4× fewer communication rounds (Table 2), while also achieving higher final test accuracy (Table 3). The communication costs remain at the KB level throughout.

- **Theoretical analysis that handles multiple local updates**: Theorem 1 and Corollary 3 provide convergence guarantees for \(\tau > 1\) local steps under a low-whitening-rank condition, closing a gap left by DeComFL which lacked convergence analysis for multiple local updates. The theory offers a plausible mechanism (via the whitening rank \(\zeta\)) for why ZO methods can converge faster than the pessimistic \(\mathcal{O}(d)\) bound.

- **Well-structured and clearly motivated**: The paper builds naturally from the DeComFL framework, explains the generalized scalar-only communication abstraction (Algorithm 1), derives the Hessian-informed update (Eqs. 5–10), and integrates everything cleanly (Section 4.3). The research question is clearly stated and the tension between curvature information and communication budget is well-articulated.

## Weaknesses

### Fatal
None.

### Major
- **The well-approximated Hessian condition is assumed, not verified for the proposed algorithm**: The convergence rate improvements in Corollaries 1–3 (independence from \(d\) and \(L\)) depend entirely on the learned \(H_r\) satisfying the well-approximated condition (Definition, Section 5.1). However, \(H_r\) is constructed via an exponential moving average of squared updates (Eq. 12), which resembles RMSprop's gradient-scale estimator rather than a principled Hessian approximation. The paper provides no proof or direct empirical measurement that the resulting \(H_r\) actually whitens the Hessian as assumed. The paper does acknowledge this limitation explicitly (remarks at end of Section 5.2: "Although it is hard to determine if this approximation holds in the context of LLMs…"), and the worst-case fallback to DeComFL is noted. But the claim of dimension-independent convergence is stated prominently (abstract, introduction, corollaries) and the gap between what the theory requires and what the algorithm provides weakens the theoretical contribution. A direct measurement of \(\mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) on a tractable proxy, or a convergence bound that degrades smoothly with approximation quality, would substantially strengthen this.

### Minor
- **Narrow model and task coverage in LLM experiments**: All LLM fine-tuning experiments use only the OPT model family (125M–2.7B) on three tasks (SST-2, QQP, SQuAD). While this is sufficient to demonstrate the method, broader coverage (e.g., LLaMA-family models, additional task types) would strengthen the generality claim. The federated setup is also modest (6 clients total, 2 sampled per round).

- **No ablation on the number of perturbation directions \(P\)**: \(P = 5\) is used throughout all ZO experiments without justification or sensitivity analysis. Since \(P\) directly trades per-round computation (function evaluations) for gradient estimate variance, understanding this trade-off is important for practical deployment.

- **The generalized scalar-only framework (Algorithm 1) is largely a reframing of DeComFL**: While the abstraction is clean and useful for exposition, it does not constitute a substantial standalone contribution. The key novelty lies in the Hessian-informed ascent direction and the \(H_r\) learning rule within that framework, not in the framework itself.

- **Smoothing parameter \(\mu\) sensitivity is not investigated**: The ZO perturbation size \(\mu\) governs the bias-variance trade-off of the finite-difference estimator. Theorem 1 includes an \(O(\eta\mu)\) bias term, but the paper provides no analysis of how \(\mu\) is chosen or how sensitive results are to its value in the LLM experiments (only the Hessian smoothing parameter \(\nu\) is ablated, in Fig. 5 left, on MNIST).

### Trivial
- The description of when \(H\) is updated could be clearer. The text states updates occur "at the beginning of one communication round" (line 152), Eq. (12) uses \(\Delta x_{r,0}\) consistent with this, but the illustrative reconstruction loop (lines 197–198) shows \(H_{t+1}\) updating at every missing-round step. The intended semantics are recoverable but the presentation could be unified for clarity.

## Nice-to-Haves
- A direct empirical measurement of the whitening effect — e.g., computing \(\mathrm{Tr}(H^{-1/2}\hat{\Sigma}H^{-1/2})\) on a small model where \(\hat{\Sigma}\) can be estimated, or tracking the variance of the ZO gradient estimator over rounds — would provide compelling support for the theory.
- Scaling experiments with larger client pools (tens to hundreds) and more heterogeneous data partitions would strengthen the practical case.
- Reporting per-round computation time or function evaluation counts in the main text (the paper mentions these are in Appendix E) would help readers assess the practical speedup beyond communication rounds alone.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Gap between theory and algorithm is fatal/structural"** — The harsh critic framed this as a fatal evidential gap. However, the paper explicitly acknowledges the conditional nature of the convergence rate ("Although it is hard to determine if this approximation holds…") and states that worst-case performance degenerates to DeComFL. The abstract qualifies the claim with "under some Hessian approximation assumptions." This is a real weakness (retained above as Major) but not a fatal one — the algorithm demonstrably works and the theory provides a plausible explanatory framework.

- **"Computation time not reported"** — The paper states that computation time comparisons are in Appendix E. Since the appendix is stripped and we cannot verify, this concern is speculative. Retained as a Nice-to-Have suggestion to move some of this to the main text.

- **"Up to 90 million times communication savings is misleading"** — Comparing against full-model-upload first-order methods (FedAvg, FedAdam) is standard practice in the ZO-FL literature; DeComFL itself makes similar comparisons. The paper also mentions comparisons against PEFT baselines in Appendix E. This is no more misleading than what the field accepts as standard.

- **"The method is not compared against compressed or parameter-efficient FL methods"** — The paper states that such comparisons exist in Appendix E. Cannot verify; removed as speculative.

- **"The learned H histogram does not support the whitening hypothesis"** — The harsh critic asserts this but the histogram (Fig. 5 right) showing long-tail distribution is presented as evidence for the low-effective-rank assumption, not as direct whitening evidence. The paper is clear about what the figure shows. The critic's objection is to the strength of evidence, not an error. The concern about direct whitening evidence is already captured in the Major weakness.

- **"H update description is inconsistent"** — Examined carefully: the text says update "at the beginning of one communication round" and Eq. (12) uses \(\Delta x_{r,0}\). The illustrative loop shows updates per missing round, which is the reconstruction case. These are describing different scenarios (active round vs. reconstruction of missed rounds) and are not contradictory. Retained only as a Trivial clarity issue.

- **"6 clients is too small"** — While small, this is standard for initial FL papers. Retained as a Minor concern about scope rather than a standalone weakness.

- **Strength Finder: "Generalized scalar-only FL framework" as a core strength** — This is primarily a reframing of DeComFL's protocol. Demoted; the real contribution is what's built on top of it.

## Novel Insights
The most interesting insight emerging from the synthesis is the tension between the theoretical mechanism (whitening the Hessian) and the practical mechanism (EMA of squared updates, à la RMSprop). The paper's theory argues that if \(H\) whitens the Hessian, the ZO gradient variance becomes dimension-independent. But the algorithm uses a rule that tracks gradient magnitude, not curvature. In practice, these two quantities may correlate for LLMs — parameters with large gradients often coincide with high-curvature directions — but the paper does not explore this connection. A deeper investigation into why RMSprop-style preconditioning empirically accelerates ZO optimization would be a valuable contribution beyond what this paper currently provides.

## Suggestions
- Reframe the theoretical contribution more carefully: present the convergence rate as an upper bound parameterized by the quality of the Hessian approximation (e.g., a rate that depends on \(\zeta\) and degrades to the DeComFL rate when \(H = I\)), rather than stating dimension-independence as a property of the algorithm.
- Add a small-scale experiment that directly measures the whitening effect, e.g., on the CNN/MNIST setup where the Hessian can be approximated, to bridge the theory-practice gap.
- Report the value of the ZO smoothing parameter \(\mu\) used in LLM experiments and include a brief sensitivity check.
- Unify the \(H\) update description to avoid confusion between the per-round update and the missing-round reconstruction case.

## Score and Decision

**Calibration anchoring:**

| Anchor | Avg Score | Round | Comparison to HiSo |
|--------|-----------|-------|---------------------|
| DeComFL (omrLHFzC37) | 6.25 | R1 | HiSo directly improves DeComFL; clearly stronger |
| FedZO-surrogate (ZAMoxm86KV) | 3.67 | R1 | HiSo is substantially stronger |
| FeedSign (DJRd4IQHGQ) | 5.25 | R1 | HiSo has stronger empirical results and cleaner theory |
| LOZO (9BiVepgmWW) | 7.00 | R2 | LOZO has more extensive experiments and a more fundamental low-rank idea; HiSo is slightly weaker |
| AdaFisher (puTxuiK2qO) | 6.25 | R2 | Comparable quality; HiSo's FL-specific cleverness slightly edges it |
| FOSI (NvbeD9Ttkx) | 6.25 | R2 | Comparable; HiSo's contribution is similarly incremental but practically useful |

**Bracket from Round 1:** ~5.5–7.5  
**Narrowed by Round 2:** HiSo is clearly above DeComFL/AdaFisher/FOSI (~6.25) and below LOZO (~7.0). The paper makes a genuine, practical improvement over the prior state-of-the-art with a clever algorithmic idea and supporting theory, but the theoretical claims are conditional on an unverified assumption and the experimental scope is somewhat narrow. **Score: 6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>