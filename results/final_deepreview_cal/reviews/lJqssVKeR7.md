Now I have sufficient context to write the final review. Let me synthesize my analysis.

---

## Summary

The paper proposes **HiSo**, a federated zeroth-order optimization method that integrates a diagonal preconditioner (motivated as a Hessian approximation) into the scalar-only communication framework of DeComFL. The key idea is to use an exponential moving average of squared update vectors to learn a per-coordinate scaling matrix \(H_r\), then sample perturbation directions from \(\mathcal{N}(0, H_r^{-1})\) so that the expected update approximates a Newton-style preconditioned gradient — all while preserving dimension-free (scalar-only) communication. The authors provide convergence analysis under a "well-approximated Hessian" condition and demonstrate 1.4–5.4× communication-round speedups over DeComFL on LLM fine-tuning benchmarks (OPT-125M through OPT-2.7B, on SST-2, QQP, SQuAD).

## Strengths

- **Generalized scalar-only FL framework (Section 3.3, Algorithm 1):** The paper decouples scalar-only communication from the specific choice of ZO-SGD, showing that any optimizer whose update can be expressed via scalars and shared random seeds fits the paradigm. This abstraction is clean and enables the design of HiSo and potentially future methods.
- **Empirical speedup over the direct predecessor DeComFL (Table 2):** HiSo reduces communication rounds by 29–80% across nine model/task configurations, with speedups of 1.4–5.4×. The experiments are conducted on realistic LLM fine-tuning tasks (SST-2, QQP, SQuAD) at scales from 125M to 2.7B parameters.
- **Extended convergence theory with multiple local steps (Corollary 3):** The analysis extends DeComFL's results to the \(\tau > 1\) case with Hessian preconditioning, showing that under the low whitening rank assumption the rate remains independent of \(d\), while DeComFL's rate would degrade. This resolves a gap left open by prior work.
- **Robustness and ablation evidence (Figure 5):** The method shows insensitivity to the Hessian smoothing parameter \(\nu \in \{0.9, 0.95, 0.99\}\) on MNIST, and the learned diagonal entries exhibit a long-tail distribution consistent with the low effective rank intuition.

## Weaknesses

### Fatal

None. The harsh critic's claim of a "fatal inconsistency" (that the Hessian update rule drives \(H_r\) to a multiple of the identity matrix) is based on a mathematical error: it treats the gradient scalar \(g = \frac{1}{\mu}(f(x+\mu H^{-1/2}u) - f(x))\) as constant with respect to the random direction \(u\), when in fact \(g \approx u^\top H^{-1/2}\nabla f\) depends strongly on \(u\). A correct expectation calculation yields \(\mathbb{E}[(\Delta x)_i^2] = (H^{-1})_{ii} \cdot (2(H^{-1})_{ii}(\nabla f)_i^2 + \|H^{-1/2}\nabla f\|^2)\), which does not reduce to a simple multiple of \((H^{-1})_{ii}\) and does not force \(H\) toward identity. The algorithm does not suffer from the claimed structural contradiction.

### Major

- **The connection between the Hessian update rule (Eq. 12) and the theoretical "well-approximated" condition (Eq. 17) is not established.** The update \(H_{r+1} = (1-\nu)H_r + \nu\,\text{Diag}(|\Delta x|^2)\) is presented as a heuristic — analogous to how Adam/RMSProp use squared gradients to estimate second moments — but the paper provides no derivation, proof, or even informal argument that this EMA converges to a quantity resembling the Hessian diagonal. The theoretical corollaries that yield dimension- and \(L\)-independent rates all depend on the well-approximated condition. The paper acknowledges this gap in the Remarks (end of Section 5.2) and notes that at worst HiSo degenerates to DeComFL, but it remains a significant disconnect between the algorithm's claimed mechanism and the theory that supports it. This should be addressed in a rebuttal: either by providing analysis of what the EMA actually estimates, or by repositioning the theory as an "oracle" analysis of what would happen *if* a good Hessian approximation were available.

- **No empirical validation that the learned \(H_r\) actually approximates the Hessian (rather than, e.g., an RMSProp-style variance estimate).** Section 6 and Figure 5 show the distribution of learned \(H\) values and note a long tail, but a long-tailed distribution of squared-update magnitudes is expected from *any* EMA of squared quantities in deep networks and does not distinguish Hessian structure from gradient second-moment structure. A comparison against a finite-difference Hessian-diagonal estimate on a small-scale problem, or an experiment that ablates whether using the learned \(H\) as a sampling covariance yields better-conditioned updates than using a comparable RMSProp-style preconditioner, would strengthen the central mechanistic claim. The paper references Appendix F.7.2 for "more direct evidences," but the appendix is not available in the submission.

### Minor

- **The paper's exposition somewhat over-claims what is being learned.** The update rule is repeatedly referred to as learning a "global diagonal Hessian approximation," but the mechanism (EMA of squared \(\Delta x\) entries) is structurally identical to Adam/RMSProp's second-moment estimator, which estimates gradient variance, not the Hessian. The actual role of \(H_r\) is better described as an adaptive diagonal preconditioner whose relationship to curvature is aspirational rather than derived. The paper's own footnote acknowledges the RMSProp resemblance, but the main text language could be more precise.
- **The DeComFL comparison in Table 2 uses an asymmetric metric:** DeComFL's rounds are counted to "full convergence" while HiSo's are counted to "match DeComFL's best test accuracy." While this is a reasonable way to show acceleration, the asymmetry should be explicitly justified and both methods' full convergence behavior compared as well.

### Trivial

- Several equation references and notation details are slightly inconsistent (e.g., the shift between Eq. (12) and the preceding inline version, the use of \(H_{r,\tau}\) vs. \(H_r\)). These do not affect comprehension.

## Nice-to-Haves

- Including a LoRA-based FL baseline (as the paper itself briefly acknowledges) would help contextualize the absolute communication savings, since LoRA is the practical standard for parameter-efficient federated fine-tuning.
- An ablation comparing HiSo against a variant that uses the same \(H_r\) update but samples \(u \sim \mathcal{N}(0,I)\) (i.e., an RMSProp-style scaling without Hessian-informed search directions) would help disentangle the benefit of curvature-informed sampling from the benefit of adaptive per-coordinate learning rates.

## Removed Points

These points were flagged by reviewers but are removed from the final review with justification:

- **"Fatal inconsistency: the Hessian update drives H toward identity" (Harsh Critic):** Removed. The mathematical claim is incorrect; it treats \(g\) as independent of \(u\) when computing \(\mathbb{E}[(\Delta x)_i^2]\). The actual expectation does not force \(H\) toward identity.
- **"The theoretical analysis is for an oracle method not realized by HiSo" (Harsh Critic):** Softened and moved to Major. The paper acknowledges the gap and Theorem 1 does not require the well-approximated condition; only the corollaries do. The theory is conditional, not invalid.
- **"The algorithm does not learn a Hessian approximation at all" (Harsh Critic):** Softened. The update rule is heuristic and its connection to the Hessian is not proven, but the critic's claim that it *cannot* learn anything curvature-related is based on flawed math. What it actually learns is an open question.
- **"Should include confidence intervals / more baselines / different experimental setups" (various):** Moved to Nice-to-Haves where appropriate; these are scope preferences, not flaws.
- **"Missing related work on [X]" (implicit):** Removed per hard rules — we do not fabricate missing references.
- **"Formatting/typo concerns":** Removed per hard rules — these are parser artifacts.

## Novel Insights

The paper's use of the "low whitening rank" \(\zeta = \text{Tr}(H^{-1/2}\Sigma H^{-1/2})\) as a quantity controlling ZO gradient variance is a clean conceptual contribution. By recognizing that a diagonal preconditioner can whiten the Hessian and compress the effective dimensionality of the ZO variance term, the analysis provides a unified explanation for why ZO methods can converge much faster than the pessimistic \(\mathcal{O}(d)\) bound — an observation that had been made empirically but not theoretically articulated in this way. The extension of this idea to the federated setting with multiple local steps is technically non-trivial and resolves a gap from prior work.

## Suggestions

- The authors should compute the actual expectation \(\mathbb{E}[(\Delta x)_i^2]\) (as a function of \(\nabla f\) and \(H\)) and analyze what the EMA in Eq. (12) converges to under stationarity assumptions. This would either (a) validate the Hessian-approximation claim or (b) reposition \(H_r\) as an adaptive preconditioner whose benefits are explained through a different mechanism than Hessian approximation. Either outcome would strengthen the paper.
- A small-scale experiment comparing the learned \(H_r\) entries against finite-difference Hessian-diagonal estimates would directly address the Major weakness and is feasible for the MNIST CNN experiment already in the paper.

## Score and Decision

**Bracketing (Round 1):**
- Weak band (score < 3.5): `ZAMoxm86KV` (FZooS, 3.67 — rejected), `Jl0aEFrp11` (2.75), `Og7ZZd7hDm` (3.25). HiSo is clearly stronger than these — it has cleaner theory, better empirical results, and a more practical algorithm.
- Middle band (3.5–7.5): `omrLHFzC37` (DeComFL, 6.25 — accepted), `bEqI61iBue` (HiZOO, 5.67 — accepted), `AbJWZp4THG` (FedAda², 5.00 — rejected), `Cy5IKvYbR3` (5.75), `DJRd4IQHGQ` (5.25). The DeComFL paper (6.25) is the direct predecessor. HiSo extends it with Hessian-informed preconditioning and stronger empirical results.
- Strong band (>7.5): `ZuazHmXTns` (7.60 — unrelated problem-parameter-free FL), `5t57omGVMw` (8.00 — unrelated linear solvers). These are not topically comparable.

**Initial bracket:** HiSo sits in the 5.5–6.75 range, likely above HiZOO (5.67) and at or above DeComFL (6.25).

**Narrowing (Round 2):**
- `bEqI61iBue` (HiZOO, 5.67): HiZOO proposes Hessian-informed ZO for single-node LLM fine-tuning. HiSo extends this idea to federated learning, adds the scalar-only communication framework, provides more sophisticated theory (low whitening rank, τ>1 analysis), and has stronger empirical evaluation. **HiSo is clearly stronger than HiZOO.**
- `omrLHFzC37` (DeComFL, 6.25): The direct predecessor. HiSo adds a nontrivial algorithmic layer (Hessian-informed preconditioning) and shows 1.4–5.4× speedup. The theory is extended. The main weakness (gap between heuristic H-update and theoretical assumption) is comparable in severity to DeComFL's weaknesses (questions about whether ZO is needed at all, limited baselines). **HiSo is at least as strong as DeComFL, with a slight edge from the additional algorithmic contribution.**
- `cznqgb4DNv` (Decentralized Sporadic FL, 7.00): A strong paper with a unified framework and convergence guarantees. HiSo is less theoretically complete (the heuristic-to-theory gap) and targets a narrower problem, so HiSo is somewhat below this anchor. **HiSo < 7.00.**

**Final placement:** HiSo is stronger than HiZOO (5.67) and at least on par with DeComFL (6.25). The additional contributions (generalized framework, Hessian-informed ZO-FL, τ>1 theory) merit a score slightly above DeComFL. I assign **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>