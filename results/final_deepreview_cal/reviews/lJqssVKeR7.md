Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize everything into a final review.

**My round-1 bracket: 5.0–7.0.** The paper is an incremental but meaningful contribution over DeComFL (score 6.25, Accept). It improves on DeComFL with a clever Hessian-learning trick and shows consistent speedups. However, the theoretical claims are more conditional and less verified than DeComFL's.

**Round 2 narrowing:** Comparing against HiZOO (5.67, Accept) — which is the single-node Hessian-informed ZO method — HiSo has a more challenging FL setting, more rigorous theory, and comparable empirical scope. HiSo is stronger than HiZOO. Against DeComFL (6.25), HiSo is comparable in quality: the algorithmic innovation is real but incremental, the theory is more fragile, and the empirical improvement is meaningful but modest in terms of final accuracy.

**Final score: 6.0** — a solid paper with a clever algorithmic idea, honest about its theoretical limitations, and with consistent (though modest) empirical evidence.

---

## Summary

This paper proposes HiSo, a federated zeroth-order (ZO) optimization method that integrates global diagonal Hessian approximations to accelerate convergence while preserving the scalar-only, dimension-free communication paradigm of DeComFL. The key algorithmic insight is that the already-communicated gradient scalars and random seeds suffice to reconstruct a diagonal Hessian approximation on both server and clients without any extra communication. The paper provides convergence analysis showing that under a "well-approximated condition" the rate can become independent of dimension \(d\) and the Lipschitz constant \(L\), and empirically demonstrates 1.4–5.4× speedups in communication rounds over DeComFL across OPT-350M to OPT-2.7B models on SST-2, QQP, and SQuAD.

## Strengths

- **Clever Hessian learning without extra communication (Section 4.2, Eq. 12).** The central algorithmic idea — using the already-communicated \(\Delta x\) vectors (which are representable by scalars) to build a global diagonal Hessian via \(\text{Diag}([\Delta x]^2)\) and exponential moving averaging — is genuinely elegant. Both server and clients can reconstruct \(H\) locally from the same scalar quantities already exchanged, so dimension-free communication is strictly preserved while curvature information is incorporated.

- **Generalized scalar-only framework (Algorithm 1).** The paper correctly identifies that scalar-only communication is not dependent on ZO-SGD specifically but on the use of scalar representations, and provides Algorithm 1 as a flexible framework that supports a broader class of optimizers. This is a clean conceptual contribution that may enable future work beyond HiSo.

- **Convergence analysis for \(\tau > 1\) (Corollary 3).** The analysis extends to multiple local updates, showing that HiSo's rate remains dimension-independent under the well-approximated condition, while DeComFL's rate (under the low-effective-rank assumption) becomes dimension-dependent again for \(\tau > 1\). This resolves an open limitation from DeComFL.

- **Consistent empirical speedups (Table 2).** Across all 9 model–task combinations, HiSo reaches DeComFL's best test accuracy in fewer rounds, yielding speedups of 1.4–5.4× with 29%–80% communication savings. The largest gains (5.4× on OPT-350M SQuAD) are substantial.

- **Robustness to the Hessian smoothing parameter \(\nu\) (Figure 5, left).** The ablation shows that varying \(\nu\) over {0.9, 0.95, 0.99} has negligible impact on convergence and final accuracy, which simplifies practical usage.

## Weaknesses

### Fatal
None.

### Major

- **The central theoretical claim of dimension-free convergence depends on an unverified and hard-to-verify condition.** The rate \(\mathcal{O}(\sqrt{\zeta/mR})\) in Corollary 1 depends on the "well-approximated condition" (Eq. 17): \(\mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2}) \leq \zeta\) with \(\zeta \ll d\). The paper provides no empirical evidence that this condition holds for the LLMs and tasks in its experiments. The toy eigenvalue simulation (Figure 4) uses a log-normal distribution chosen for convenience, not actual neural network Hessians. The CNN experiment (Figure 5, right) shows a long-tailed distribution of learned \(H\) values, which is suggestive but does not compute or bound \(\zeta\). The paper honestly states "it is hard to determine if this approximation holds in the context of LLMs" — but this admission means the headline theoretical result (the first dimension-free convergence rate for ZO methods in FL) remains a conditional statement whose premise is unsupported. Without this condition, HiSo's rate degenerates to DeComFL's. **The theory explains *what would happen if* the approximation were good, but does not establish that it *is* good in the claimed setting.**

### Minor

- **The "90 million times communication savings" claim in the abstract is not directly supported by the tables.** The largest savings calculable from Table 3 is ~34.6 million (OPT-1.3B FedAdam SQuAD vs HiSo). The 90 million figure would require a comparison with OPT-2.7B first-order methods, but those numbers are not reported. The claim should cite the specific comparison that yields this number.

- **Hyperparameter tuning details are insufficient.** The paper states methods were "tuned using their optimal learning rates" but does not report the grid, ranges searched, or number of values tried. Without this information, it is difficult to assess whether the comparison is fair to all methods.

- **No wall-clock timing is reported.** All speedup comparisons use communication rounds, which is the right primary metric when communication is the bottleneck. However, HiSo incurs additional local computation per round (Hessian update, model reconstruction from missed rounds). Reporting wall-clock time (or at least per-round computation overhead) would give a more complete picture.

- **The "safety factor of 2" in the well-approximated definition (Eq. 17) is ad hoc.** The definition lumps the \(L\)-smoothness and low-effective-rank cases into a single inequality with a factor of 2, which is not clearly motivated. A cleaner framing would separate the two regimes.

- **The "90 million times" and "5×" speedup claims in the abstract slightly overstate what the tables show.** Table 2 shows speedups ranging from 1.4× to 5.4× (so "1–5×" in the abstract is approximately correct, and the 5.4× entry supports "up to 5×"). This is not a substantial issue but the framing is slightly inflated.

### Trivial
None.

## Nice-to-Haves

- **Direct validation of the well-approximated condition on a smaller model.** For a model like OPT-125M, the paper could approximate the true Hessian diagonal (via Hutchinson trace estimation) and compute a numerical approximation to \(\zeta = \mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\), showing whether \(\zeta \ll d\) actually holds. This would ground the theoretical contribution.
- **Ablation of the Hessian update structure itself** (e.g., how many rounds before \(H\) becomes useful, whether stale Hessian information hurts after a large model change).
- **Additional model architectures beyond OPT** (e.g., LLaMA, Pythia) to demonstrate generality.
- **Wall-clock timing** to complement round-based comparisons.
- **Comparison with a ZO version of FedAvg** using adaptive scaling without Hessian information, to isolate the benefit specifically attributable to curvature versus any adaptive scaling.

## Removed Points

- Criticism about model reconstruction cost scaling with missed rounds (Section 3): This is a theoretical concern that amounts to transmitting a handful of additional scalar floats for missed rounds — negligible in practice. Removed as noise.
- Criticism about \(\Theta(d)\) memory for Hessian storage (Section 4.2): The paper correctly states this avoids \(d^2\) storage, and \(\Theta(d)\) is the baseline for any method that maintains state per parameter. Removed as not a genuine weakness.
- Criticism about comparison with uncompressed first-order methods: The paper appropriately contextualizes this as a comparison with "naive transmission," and compressed FL is outside its scope. Removed as scope creep.
- Several strength-finder claims about "important problem" and "well-written" — generic and not specific to this paper's evidence. Removed.
- Criticism that only OPT models were used: Valid suggestion but clearly outside the paper's stated scope. Moved to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Temper the theoretical framing.** The paper would be more credible if it presented the well-approximated condition as a plausible mechanism for acceleration rather than a proven guarantee. The current framing ("marking the first such result") overpromises given the unverified premise. Reframing as a rate bound that depends on the quality of Hessian approximation, with the dimension-free corollary as an idealized special case, would be more honest and strengthen the paper.
2. **Support or qualify the "90 million times" claim.** Either compute the exact comparison that gives this number from Table 3 data, or change the claim to a verifiable number.
3. **Report wall-clock or per-round overhead.** Even a single table comparing computation time per round between HiSo and DeComFL would resolve concerns about the practical cost of Hessian updates.
4. **Report the hyperparameter search grid.** A brief table or sentence describing the learning rate ranges tried and whether the same \(P=5\) was optimal for all methods would significantly strengthen the empirical evaluation.

## Score and Decision

Calibration anchors used across rounds:

| Anchor ID | Avg Score | Round | Comparison to this paper |
|-----------|-----------|-------|------------------------|
| omrLHFzC37 (DeComFL) | 6.25 | 1, 2 | Direct predecessor. HiSo is an incremental but meaningful improvement with cleverer algorithm and comparable empirical support, though with more fragile theory. Slightly weaker overall. |
| ZAMoxm86KV (FZooS) | 3.67 | 1 | A weaker ZO-FL paper with GP-based gradient estimation. HiSo is substantially stronger across all dimensions. |
| uaGNerHa1J (FedNewton) | 4.67 | 1, 2 | A second-order FL method limited to KRR. HiSo is more broadly applicable and empirically stronger. |
| bEqI61iBue (HiZOO) | 5.67 | 2 | Single-node Hessian-informed ZO. HiSo extends the idea to the more challenging FL setting with more rigorous theory. Stronger overall. |
| FK8tl47xpP (Greedy L2O) | 6.25 | 2 | Unrelated topic (L2O). Not directly comparable; included for general calibration. |
| AfhNyr73Ma (General Stability ZO) | 7.00 | 2 | Unrelated topic (stability analysis). Higher score reflects a different type of contribution. |

**Round-1 bracket:** 5.0–7.0 (anchored by DeComFL at 6.25 on the high end, and weaker ZO-FL papers around 3.5–4.5 on the low end).

**Round-2 narrowing:** Compared against DeComFL (6.25), HiSo adds a genuine algorithmic innovation but has more fragile theoretical claims and comparable empirical evidence. Compared against HiZOO (5.67), HiSo operates in a more challenging setting with more comprehensive theory. The paper sits between these two anchors, slightly closer to DeComFL.

**Final score: 6.0** — a solid paper with a clever algorithmic contribution and honest treatment of limitations. The empirical evidence is positive and consistent. The theoretical contribution would be strengthened by empirical validation of its central condition, but the paper's transparency about this limitation is commendable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>