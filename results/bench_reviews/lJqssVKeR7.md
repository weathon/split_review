## Summary

The paper proposes HiSo, a federated zeroth-order (ZO) optimization method that extends DeComFL's scalar-only communication protocol to support a diagonal "Hessian-informed" preconditioner (in fact, an RMSProp-style second-moment estimator over preconditioned updates) reconstructed identically at server and clients from the already-communicated scalars. The authors prove convergence rates that, under a "well-approximated Hessian" assumption, become independent of both model dimension $d$ and Lipschitz constant $L$, and extend the analysis to $\tau>1$ local steps. Empirically, HiSo achieves 1.4–5.4× round speedups over DeComFL on OPT-125M/350M/1.3B/2.7B fine-tuning across SST-2, QQP, SQuAD.

## Strengths
- **Clean engineering observation (§3.3, Algo. 1).** Generalizing the scalar-only DeComFL communication scheme so that any update of the form $g\cdot v(\text{seed, shared state})$ qualifies is a useful and concrete contribution; it cleanly motivates how a preconditioner can be added without breaking dimension-free communication.
- **Preconditioner reconstructed with zero communication overhead (Eq. 12).** Maintaining the diagonal $H$ from $\Delta x$ values already implied by transmitted scalars genuinely preserves the MB-scale communication budget, and is the central engineering insight.
- **$\tau>1$ analysis (Cor. 3).** Extending DeComFL's convergence analysis to multiple local updates is a real theoretical advance independent of the Hessian framing, addressing an explicitly stated open question.
- **Empirical convergence improvement is real.** Across all reported LLM tasks, HiSo reaches DeComFL's best accuracy in fewer rounds (Table 2), at matched per-round cost.
- **$\nu$ robustness (Fig. 5 left).** The ablation supports the practical claim that the smoothing hyperparameter is not finicky.

## Weaknesses

### Fatal
None.

### Major
- **The "Hessian-informed" framing is not earned by the update rule (§4.2, Eq. 12).** The diagonal update $H_{r+1} = (1-\nu)H_r + \nu\,\text{Diag}(|\Delta x_r|^2+\epsilon I)$, with $\Delta x_r = g_r H_r^{-1/2} u_r$, is the RMSProp second-moment of the *preconditioned* ZO update, not an estimator of the Hessian diagonal $\text{Diag}(\Sigma)$. The paper concedes the RMSProp resemblance in footnote 2, but the entire marquee theoretical claim (Cor. 1) depends on $H$ being a "well-approximated Hessian" in the sense of Eq. 17 — a property the update rule does not provably deliver and which the paper does not directly verify on real LLMs (Fig. 4 is a synthetic 200-eigenvalue log-normal simulation; Fig. 5 right shows long-tailed $H$ but long-tails are equally consistent with squared gradients). The gap between the algorithmic mechanism and the assumption needed by the theorem is the structural weakness.
- **The "$d$- and $L$-independent" rate is conditional, not unconditional (Cor. 1, Eq. 17, Assumption 4).** The rate $\mathcal{O}(\sqrt{\zeta/mR})$ requires $\text{Tr}(H^{-1/2}\Sigma H^{-1/2})\le\zeta$ with $\zeta$ taken as $d$-independent *by assumption*, plus bounded $H$ (Assumption 4). The paper does state ("hard to determine if this approximation holds in the context of LLMs") that verification is open, but still markets the corollary as "the first such result for ZO methods in FL" and as an explanation of empirical acceleration. As written it is an implication, not an explanation, and the abstract overstates this.
- **Communication-cost claim has a counterexample in the paper's own Table 3.** The text claims HiSo "maintains the lowest communication cost in almost all tasks", but for OPT-1.3B + QQP, HiSo costs 96.67 KB vs DeComFL's 43.95 KB — more than 2× DeComFL. The authors do parenthetically note "only a little higher than DeComFL on OPT-1.3B+QQP", so this is acknowledged, but "a little higher" understates a >2× regression on the largest non-2.7B model tested. The accuracy gains over DeComFL are also typically within or only marginally above the reported std (e.g., OPT-1.3B SST-2: 90.22±0.10 vs 90.34±0.12), so the "consistently outperforms" claim is borderline.

### Minor
- **Stale-Hessian / fixed-point coupling not analyzed.** $H$ is refreshed only at round boundaries (per text: "We only update the Hessian at the beginning of one communication round"), while $\Delta x_{r,k}$ during local steps uses the frozen $H_r$ that was itself built from past $\Delta x$ generated under prior $H$. The discrepancy is absorbed into Assumption 4's bounded-$H$ condition; an explicit analysis or empirical sensitivity study would tighten the picture.
- **$L$-dependence is buried, not eliminated (Theorem 1).** The client-drift term contains $(\tau-1)^2 L/\beta_\ell$ and the step-size constraint includes $\sqrt{1/L(d+2)}$. The dimension- and $L$-independent rate only emerges after specific $\eta,\tau$ choices and assumption stacking. The abstract should make this conditionality explicit.
- **No ablation isolating the preconditioner mechanism.** A natural baseline is DeComFL+diagonal preconditioner built from $g^2$ (i.e., a true RMSProp-on-ZO control). Without it, the contribution of curvature interpretation vs. plain adaptive scaling is hard to attribute.
- **No reported variance for Table 2 speedup numbers**, while Table 3 does report std for accuracy/cost.

### Trivial
- The "up to 5×" headline is essentially driven by one OPT-350M/SQuAD cell; the typical LLM speedup is closer to 1.5–2×. Reporting the median speedup alongside the maximum would be more honest.

## Nice-to-Haves
- Direct empirical estimate of $\text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ (e.g., via Hutchinson) at a few checkpoints on one OPT model would let Cor. 1 actually "explain" the observed acceleration.
- Trajectory plot of effective rank $\zeta$ (or its proxy) across training.
- LLM-scale ablations on $\nu$, $\epsilon$, and the implicit $\beta_\ell,\beta_u$ clipping that Assumption 4 invokes.
- A control experiment with $H$ built from $g^2$ vs. $|\Delta x|^2$ to test whether the "Hessian-informed" interpretation is doing real work beyond Adam-style scaling.

## Removed Points
*These points were considered but removed; treat them with caution.*
- Harsh critic's complaint that the "Generalized framework" is inflated as a separate contribution: this is a judgment call — the framework is genuinely useful as scaffolding for the rest of the paper, and the authors do not oversell it.
- Strength Finder's "Strong empirical acceleration" with up-to-5.4× framing: kept only with caveats above; the maximum-speedup framing is partly selective.
- Generic strength about "addresses an important problem" — superficial, dropped.

## Novel Insights
None beyond the paper's own contributions. The key novel insight is the paper's own: that any update of the form $g\cdot v(\text{seed, shared state})$ is compatible with scalar-only FL, which permits server- and client-side reconstruction of a shared diagonal preconditioner without any extra bytes on the wire.

## Suggestions
- Reframe the contribution as "adaptive (RMSProp-style) preconditioning under scalar-only FL communication, with a $\tau>1$ convergence analysis," and treat the Hessian-approximation reading as motivation rather than as the basis of the headline rate.
- Add an empirical Hutchinson-style check that $\text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ is small relative to $Ld$ for one LLM at one checkpoint.
- Acknowledge in the abstract that the $d,L$-independent rate is conditional on the well-approximation assumption (Eq. 17).
- Address the OPT-1.3B+QQP communication regression explicitly in Table 3's text rather than parenthetically.

## Axis Evaluation

- **Originality:** Moderate. The framework generalization is a clean composition of DeComFL (Li et al., 2025b) and HiZOO-style preconditioning (Zhao et al., 2025). The $\tau>1$ ZO-FL convergence result is genuinely new.
- **Importance:** Real — communication is the binding constraint for federated LLM fine-tuning.
- **Support for claims:** Mixed. Empirical claims of "1–5× speedup" are real but the headline framing is selective. The marquee theoretical claim is a conditional implication marketed as an explanation.
- **Soundness:** Theorem 1 looks correct as stated; the issue is the mismatch between Eq. 12 and Eq. 17.
- **Clarity:** Generally good; Theorem 1's hidden $L$-dependence in the drift term should be stated more transparently.
- **Value to community:** A useful engineering recipe and a real $\tau>1$ analysis, but the "Hessian-informed" branding will likely cause confusion.

## Score and Decision

Anchors (all retrieved):
- `omrLHFzC37` (DeComFL) — avg **6.25**, Accept. The base paper HiSo extends; HiSo is a clear but incremental follow-up, similar polish, narrower scope.
- `ZAMoxm86KV` (Trajectory-informed federated ZO) — avg **3.67**, Reject. HiSo is clearly stronger: real LLM-scale experiments, $\tau>1$ analysis, working dimension-free protocol.
- `DJRd4IQHGQ` (FeedSign 1-bit federated FT) — avg **5.25**, Reject. Comparable scope and empirical maturity; HiSo has marginally better theoretical scaffolding but similar overclaiming.
- `9H1uctBWgF` (Ferret federated full-parameter FT) — avg **4.67**, Reject. Similar scope, similar criticisms; HiSo is slightly more polished theoretically.
- `kH5nNlgT52` (One-round federated FM FT) — avg **4.50**, Reject. Less rigorous than HiSo.
- `bEqI61iBue` (HiZOO; non-federated Hessian-informed ZO) — avg **5.67**, Accept. The direct single-node analog of HiSo's preconditioner; HiSo's federated extension is reasonable on top of that.
- `9BiVepgmWW` (Low-rank ZO for LLM FT) — avg **7.00**, Accept. Cleaner contribution and tighter empirical story than HiSo.
- `Oqk1Ui6m0n` (Hessian-Free NGD for PIML) — avg **5.00**, Reject. Similar over-promised theory vs. mechanism gap.
- `FK8tl47xpP` (Greedy L2O with convergence guarantees) — avg **6.25**, Reject. More original theory than HiSo.
- `fMTPkDEhLQ` (Tight lower bounds Hölder smooth) — avg **8.00**, Accept. Pure theory paper, not comparable in domain; included only as a high-anchor calibration point — HiSo is well below this tier.
- `xJ5N8qrEPl` (Bi-Level Optimization, Hessian-free) — avg **6.40**, Accept. More original theoretical contribution than HiSo.
- `kWsJkH1tNi`, `Ob0UafH2YI`, `Jl0aEFrp11`, `EcetCr4trp`, `WM4xiEDz2N`, `9TSv6ZVhvN`, `Cnn60wwTe1` — FL theory anchors at 2.75–5.75; HiSo is comparable to the upper half of this cluster (~5).
- `zfeso8ceqr` (Deconstructing optimizers) — avg **6.00**, Accept. Stronger empirical depth than HiSo.
- `IDxZhXrpNf` (SOAP) — avg **6.25**, Accept. Cleaner methodological contribution than HiSo.

HiSo sits between DeComFL (6.25, accepted) — which it directly extends — and the cluster of rejected federated-LLM fine-tuning works at 4.5–5.25. The work has real contributions (the scalar-only protocol generalization, the $\tau>1$ ZO-FL analysis) but the headline "Hessian-informed, $d/L$-independent" claims outrun the mechanism and the empirical evidence on real LLMs. Net: borderline below the DeComFL bar, above the rejected federated-FT cluster.

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>