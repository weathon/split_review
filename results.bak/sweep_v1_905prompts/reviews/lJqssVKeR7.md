Now I have all the information I need. Let me compile the final review.

## Summary

This paper proposes **HiSo**, a federated zeroth-order optimization method that incorporates a learned diagonal Hessian preconditioner while preserving scalar-only (dimension-free) communication — no extra Hessian-related information is transmitted. The method builds on the DeComFL framework by: (1) generalizing the scalar-only communication paradigm beyond vanilla ZO-SGD, (2) introducing a Hessian-informed update direction, and (3) learning a global diagonal Hessian approximation from the communicated scalars at zero additional communication cost. Theoretically, the paper provides convergence analysis showing that under a "well-approximated Hessian" condition, HiSo can achieve rates independent of model dimension \(d\) and Lipschitz constant \(L\) (Corollary 1), and it extends this theory to multiple local updates (\(\tau > 1\), Corollary 3), which DeComFL could not handle. Empirically, HiSo achieves 1.4–5.4× speedup in rounds and 29–80% communication savings over DeComFL on OPT-350M to OPT-2.7B models across SST-2, QQP, and SQuAD.

---

## Strengths

- **Generalized scalar-only communication framework (Algorithm 1).** The paper correctly identifies that ZO-SGD is not the only algorithm compatible with scalar-only FL. Algorithm 1 cleanly decouples the communication protocol from the specific optimization algorithm, enabling Hessian-informed updates and potentially other methods to be plugged in while preserving dimension-free communication. This is a valuable conceptual abstraction over DeComFL's tightly-coupled design.

- **First convergence theory for Hessian-informed ZO in FL with dimension-free communication.** Theorem 1 and Corollaries 1–3 provide rigorous non-convex convergence guarantees. Corollary 3 extends the analysis to multiple local updates (\(\tau > 1\)), which DeComFL could not support under its low-effective-rank assumption — the paper correctly identifies this as resolving an open question from the DeComFL analysis. The novel quantity \(\zeta\) (low whitening rank) is a genuine theoretical contribution that formalizes how Hessian preconditioning can shrink the effective variance.

- **Empirical speedups over DeComFL are consistent and non-trivial.** Across all three LLM fine-tuning tasks and three model sizes (OPT-350M to OPT-2.7B), HiSo reliably converges faster than DeComFL (1.4–5.4× in rounds) while achieving higher final accuracy. The communication cost savings (up to 80%) are from fewer rounds, not from per-round compression tricks — a clean demonstration of algorithmic advantage.

- **Zero-extra-communication Hessian learning is clever.** Using the global update scalars \(\Delta x_r\) (which must be communicated anyway for model reconstruction) to estimate a diagonal Hessian via EMA of squared values (Eq. 12) is a practically motivated mechanism that costs no additional bandwidth. The MNIST ablation (Figure 5) shows the learned Hessian exhibits a long-tailed distribution consistent with the low-effective-rank assumption, providing some empirical grounding.

---

## Weaknesses

### Major

- **The central theoretical claim (dimension-free convergence under the well-approximated Hessian) rests on a condition that is not validated for the models and tasks studied.** Corollaries 1–3 depend on the "well-approximated Hessian" condition (Definition, Eq. 17) and the claim that \(\zeta \ll L\kappa \ll Ld\). The only evidence offered is a toy simulation with 200 log-normal eigenvalues (Figure 4). For the actual OPT models used in experiments, the paper does not measure \(\zeta\), does not confirm that the learned \(H_r\) approximates the true Hessian, and does not show that the whitening compresses the eigenvalue distribution. The paper acknowledges this gap honestly ("Although it is hard to determine if this approximation holds in the context of LLMs…"), but this leaves the paper's headline theoretical results — the dimension- and \(L\)-independent rates — as plausible explanations rather than established guarantees for the claimed setting. This gap is significant because the well-approximated condition requires more justification than DeComFL's low-effective-rank assumption (which at least has prior empirical support in the LLM literature).

- **The Hessian learning heuristic (Eq. 12) is not analyzed, and the feedback loop between update direction and Hessian estimate is not addressed.** The diagonal Hessian \(H_r\) is updated using the squared global update vectors \([\Delta x_r]^2\), but \(\Delta x_r\) itself was preconditioned by the *current* \(H_r\). This creates a circular dependency: the update direction depends on \(H_r\), and \(H_r\) is estimated from the update direction. Assumption 4 (bounded learned Hessian) treats \(H_r\) as given and does not establish whether the update rule (Eq. 12) converges to a meaningful curvature estimate or could diverge. While Adam/RMSProp-style heuristics are standard in optimization, the paper does not connect Eq. 12 to the directional second derivative (Eq. 11) it references, nor justify why \(|\Delta x|^2\) serves as a Hessian proxy beyond informal intuition. An ablation comparing Eq. 12 to simpler alternatives (fixed diagonal, squared ZO gradient norms) would substantially clarify the source of the improvement.

- **Experimental scope is limited.** The LLM experiments use only 6 clients (2 sampled per round) — a toy cross-silo setup that does not reflect cross-device FL with hundreds or thousands of clients. All experiments are on OPT models (350M–2.7B); whether HiSo transfers to other architectures (LLaMA, Gemma, etc.) or generation tasks is not shown. The gap to first-order methods remains substantial (e.g., SST-2 on OPT-1.3B: 90.34% HiSo vs. 92.86% FedAdam), yet the paper does not discuss this candidly.

### Minor

- **The "90 million times communication savings" claim conflates HiSo's specific contribution with the underlying ZO scalar-only framework.** The dramatic savings over first-order methods (TB→KB) come from the ZO dimension-free framework already established by DeComFL, not from HiSo's Hessian innovation. HiSo's marginal improvement over DeComFL is 29–80% in communication cost — respectable but dwarfed by the ZO-vs-FO gap. The paper's abstract and introduction present this figure without distinguishing the source of savings, which could mislead readers about the magnitude of HiSo's specific contribution.

- **The convergence bound in Theorem 1 depends on unobservable quantities \(\bar{\rho}\) and \(\bar{\phi}\)** (involving \(\mathrm{Tr}(H_r^{-1/2}\Sigma H_r^{-1/2})\) and \(\mathrm{Tr}(H_r^{-1})\)). These are not connected to measurable or controllable algorithm parameters, limiting the bound's practical interpretability as a guide for hyperparameter selection.

- **No discussion of computational overhead at clients.** While \(H_r^{-1/2}\) is cheap for a diagonal matrix (element-wise operation), the paper should explicitly state the per-step computation cost. Clients must also sample from \(\mathcal{N}(0, H_r^{-1})\), which, while straightforward for a diagonal covariance, is not the same as the standard normal sampling in DeComFL.

- **No comparison with existing Hessian-aware ZO methods in non-FL settings** (e.g., Ye et al. 2018, Zhao et al. 2025, HELENE, HiZOO). While the paper cites these works, it does not discuss how HiSo's Hessian learning compares to theirs, leaving the reader to infer differences.

### Trivial

- The paper states the MNIST experiment uses 64 clients (Section 6) but the LLM experiments jump to 6 clients without explaining this choice.

---

## Nice-to-Haves

- Measure \(\zeta\) (the whitened trace) empirically for the OPT models used in experiments, even approximately on sub-networks, to validate the well-approximated Hessian condition.
- Include a cross-device simulation (100+ clients, low participation rate) to demonstrate scalability.
- Run an ablation comparing Eq. 12 against: (i) a fixed diagonal Hessian, (ii) squared ZO gradient norms as a Hessian proxy, and (iii) no Hessian (DeComFL). This would isolate the benefit of the dynamic update versus curvature information in general.
- Compare against at least one non-ZO efficient FL method (e.g., FedAvg+LoRA) to contextualize the accuracy–communication trade-off.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about missing hyperparameter details for baselines.** The Appendix (stripped by the parser) likely contains these; removing.
- **Claim that "the Hessian learning dynamics could diverge."** While the feedback loop is unanalyzed, this is speculative. The paper's boundedness assumption prevents divergence; the weakness kept above is about lack of analysis, not risk of divergence.
- **Criticism that "Theorem 1 bound could be worse than DeComFL if \(H_r\) is poor."** The paper's "degenerates into DeComFL" claim is slightly imprecise, but Assumption 4 bounds \(H_r\) away from zero, so pathological blowup is prevented. Demoted to a minor note within the first Major weakness.
- **Claim that the generalized framework novelty is "modest"** — opinion, not a concrete weakness.
- **"No comparison with FedAvg+LoRA"** — the paper states the appendix includes FL+PEFT baselines. Since the appendix is stripped, this cannot be verified but the paper should get the benefit of the doubt.
- **Criticism about FedZO TB-level communication costs** — the reviewer speculates without the stopping criterion, which is likely in the Appendix.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

- Add an experiment measuring the whitened trace \(\zeta\) for the actual models used (even a small-scale measurement would substantially strengthen the theoretical claim).
- Include an ablation study for the Hessian learning rule (Eq. 12) comparing against simpler curvature proxies.
- Clearly separate the ZO-framework savings (inherited from DeComFL) from HiSo's marginal savings in the framing of communication cost claims.
- Expand the FL setup to at least 20–50 clients to demonstrate that the method scales beyond small cross-silo settings.

---

## Score and Decision

### Calibration

**Round 1 bracket:** The paper sits between 5 and 7 based on anchors:

| Anchor | Path | Avg Score | Round | Comparison to this paper |
|--------|------|-----------|-------|-------------------------|
| DeComFL | omrLHFzC37 | 6.25 | 1 | Direct predecessor; HiSo extends it with Hessian info and τ>1 theory, but has less experimental validation |
| "Compressed Decentralized Learning" | zqXANcFO9T | 1.67 | 1 | Clearly weaker; unrelated topic |
| FedADM | IsHWcsk4Fz | 3.00 | 1 | Clearly weaker; no ZO or dimension-free aspect |
| HELENE | zuOnOAHBMy | 4.00 | 2 | Hessian+ZO but no FL; weaker theory-experiment alignment |
| FeedSign | DJRd4IQHGQ | 5.25 | 2 | Related ZO-FL space; lower overall quality |
| HiZOO | bEqI61iBue | 5.67 | 2 | Hessian+ZO single-node; comparable quality, more experiments |
| DeComFL | omrLHFzC37 | 6.25 | 2 | Direct predecessor, stronger validation |

**Round 2 narrowing:** The paper is clearly stronger than HELENE (4.00) and FeedSign (5.25). It is comparable to HiZOO (5.67) — both introduce Hessian-informed ZO with theory and experiments, though HiZOO has broader model coverage. It is somewhat weaker than DeComFL (6.25) in terms of experimental validation completeness and assumption verification. The bracket narrows to **5.0–6.0**.

**Final score:** **5.5**. The paper's core idea is well-motivated and cleanly executed, the theoretical contributions are meaningful (especially the τ>1 analysis), and the empirical speedups are consistent. However, the central theoretical claim rests on an unverified assumption, the Hessian learning dynamics are unanalyzed, and the experimental scope is limited. The paper makes a real but incompletely supported contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>