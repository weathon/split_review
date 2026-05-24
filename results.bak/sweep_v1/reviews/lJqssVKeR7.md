## Summary

This paper proposes HiSo, a Hessian-informed federated zeroth-order optimization method that accelerates convergence by learning a global diagonal Hessian approximation from scalar-only communicated updates. The key insight is that the Hessian can be reconstructed from the same scalar update values already transmitted, preserving dimension-free communication while incorporating curvature information. Theoretically, the paper provides convergence guarantees and shows that under a well-approximated Hessian condition, the rate becomes independent of model dimension \(d\) and Lipschitz constant \(L\). Empirically, HiSo demonstrates 1.4–5.4× speedup in communication rounds over DeComFL across multiple LLM fine-tuning tasks.

## Strengths

1. **Novel integration of Hessian information into ZO-FL while preserving scalar-only communication.** The design of learning a diagonal Hessian approximation from the already-transmitted scalar updates (Eq. 12) is clever — it incurs zero additional communication overhead. This cleanly resolves the tension between curvature-aware optimization and dimension-free communication (Section 4.2).

2. **First ZO-FL convergence theory enabling dimension-free rates under the low whitening rank condition.** Corollary 1 establishes \(\mathcal{O}(\sqrt{\zeta/mR})\) convergence independent of \(d\) and \(L\) when the Hessian is well-approximated, and Corollary 3 extends this to multiple local updates (\(\tau>1\)) — an open challenge for DeComFL. Theorem 1 itself does not require the well-approximated condition, providing a fallback guarantee.

3. **Empirical acceleration across diverse LLM tasks.** Table 2 shows consistent 1.4–5.4× speedups (29–80% communication savings) in rounds to match DeComFL's best accuracy across SST-2, QQP, and SQuAD with OPT-350M through OPT-2.7B. These savings are relative to an already dimension-free baseline.

4. **Transparent treatment of theoretical assumptions.** The paper explicitly states that the well-approximated condition is "hard to determine" for LLMs and that HiSo degenerates to DeComFL performance if the approximation fails (Section 5.2 remarks). The main theorem (Theorem 1) is not contingent on this condition.

5. **Empirical evidence of long-tail Hessian distribution.** Figure 5 (right) plots the learned diagonal Hessian entries, showing a long-tailed distribution consistent with the low-effective rank assumption used in the theory.

## Weaknesses

### Major

- **The dimension-free convergence rates are conditional on an unverified property of the learned Hessian.** Corollaries 1 and 3 assume the "well-approximated condition" (Definition 17) holds — i.e., that \(\operatorname{Tr}(H^{-1/2}\Sigma H^{-1/2}) = \zeta\) is independent of \(d\). The paper provides no theoretical guarantee or controlled empirical measurement that HiSo's learned \(H_r\) actually satisfies this. The acceptance of this assumption is acknowledged in the text ("Although it is hard to determine if this approximation holds in the context of LLMs"), but the advertised headline results ("first such result for ZO methods in FL" that is "independent of \(d\) and \(L\)") rest entirely on it. A tractable experiment measuring \(\zeta\) in a small model where the Hessian can be approximated would substantiate the claim. Without it, the theoretical contribution is a rate conditional on an unverified condition rather than a property of the algorithm.

### Minor

- **The OPT-1.3B/QQP anomaly is under-explained.** In Table 3, HiSo's total communication cost (96.67 KB) is more than double DeComFL's (43.95 KB) for full convergence, but the paper describes it as "only a little higher." While HiSo achieves higher final accuracy (64.20% vs. 63.25%) and Table 2 shows it matches DeComFL's best accuracy with less communication (29.30 KB), the discrepancy between the two tables is not discussed. A clear explanation of whether this reflects poor Hessian approximation, suboptimal hyperparameters, or the cost of reaching a higher accuracy plateau would strengthen the presentation.

- **Limited experimental scale for a federated setting.** The LLM experiments use only 6 total clients with 2 sampled per round, which is far from realistic FL deployments. No experiments with heterogeneous data partitions (e.g., controlled non-IID splits via Dirichlet distributions) are conducted for the LLM tasks. A more realistic FL evaluation would strengthen the practical claims.

- **No convergence curves for LLM experiments.** Table 3 reports only final values; without accuracy-vs-round plots or error bars over multiple seeds, it is difficult to assess variance or verify that reported costs are not cherry-picked. The MNIST experiment (Figure 5) provides such curves, but the LLM experiments do not.

- **Missing compressed-first-order baselines.** The comparison against first-order methods (FedAvg, FedAdam) uses full-gradient transmission (TB-level), making the communication savings appear extreme. A baseline like FedAvg with top-k gradient compression or QSGD would provide a more informative communication-accuracy trade-off comparison, though the qualitative picture (ZO methods at KB vs. FO methods at TB) is unlikely to change.

### Trivial

- The claim that HiSo "delivers higher test accuracy than all ZO baselines across all tasks" (Abstract) is factually supported by Table 3, but accuracy gaps are small (e.g., 90.34% vs. 90.22% on SST-2 OPT-1.3B) and standard deviations overlap. The claim is technically correct but the practical significance is modest in some cases.

## Nice-to-Haves

- Direct measurement of \(\zeta\) (the whitened Hessian trace) for a small network where \(\Sigma\) can be estimated, to validate whether the well-approximated condition holds.
- A momentum variant of HiSo, which the paper notes could be added "without additional communication costs," would be a natural extension to explore.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Theoretical contribution is fundamentally undermined — a tautology"** (Harsh Critic #1). Removed: the paper is transparent about the condition being an assumption, Theorem 1 does not require it, and conditional guarantees are standard in ML theory. The paper frames this as a "plausible explanation" for fast practical convergence, not a proven property of HiSo. This is not a fatal structural flaw.
- **"Algorithm 1 is a trivial refactoring of DeComFL"**. Removed: the paper's main contribution is HiSo, not the generalized framework alone. Algorithm 1 serves as scaffolding to enable Hessian-informed updates within the scalar-only paradigm, which is the actual contribution.
- **"Only 6 clients is not representative"**. Weakened to Minor from Major: the paper's 6-client setting is acknowledged and ZO LLM experiments are expensive, but the evaluation would be stronger with larger FL setups.
- **Formatting nitpicks, speculation about missing appendix content**. Removed per instructions.
- **"No related work on missing baselines"**. Removed: without external sources I cannot confirm what works exist or are missing.
- **Strength Finder generic strengths** (e.g., "the paper addresses an important problem"). Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The two inputs largely agree on the core strengths and weaknesses, with the main novelty being the honest assessment that the dimension-free rates are conditional. The most interesting observation from reviewing the discussion is the tension between the theoretical framing (first dimension-free rate for ZO in FL) and the caveat that the necessary condition is unverified — the paper is admirably transparent but this transparency does not resolve the gap. The practical question of whether HiSo's diagonal Hessian approximation actually achieves the whitening effect in LLMs remains open and would be a natural direction for future work.

## Suggestions

1. Add a controlled experiment (e.g., a small MLP or CNN where the full Hessian can be approximated via Hutchinson's method) that measures \(\zeta = \operatorname{Tr}(H^{-1/2}\Sigma H^{-1/2})\) under HiSo's learned \(H\), and compares it to \(Ld\) and \(L\kappa\). This would ground the theoretical acceleration claim.

2. Explain the OPT-1.3B/QQP discrepancy: why does HiSo's total communication cost exceed DeComFL's at full convergence despite requiring fewer rounds to match DeComFL's best accuracy? A sentence clarifying whether this reflects the cost of pushing to a higher accuracy plateau, or a limitation of the Hessian approximation on that task, would resolve the apparent contradiction.

3. Include convergence curves (accuracy vs. round, with error bars over multiple seeds) for at least one representative LLM task per model size, to give readers confidence that the reported round counts are not cherry-picked.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `omrLHFzC37.md` (DeComFL, ZO-FL baseline) | 6.25 | HiSo extends this work with Hessian information and shows faster convergence. The theoretical contribution is novel but conditional on an unverified assumption. HiSo is slightly weaker in execution (fewer clients, no convergence curves) but adds algorithmic novelty. **HiSo ≈ DeComFL.** |
| `bEqI61iBue.md` (HiZOO, single-node Hessian ZO) | 5.67 | HiZOO tackles Hessian-informed ZO for single-node LLM fine-tuning. HiSo tackles the harder FL setting and has stronger convergence theory. **HiSo ≳ HiZOO.** |
| `9BiVepgmWW.md` (LOZO, low-rank ZO FT) | 7.00 | LOZO has stronger experiments (larger models, more tasks) and a cleaner theoretical framing. HiSo addresses the harder FL setting but the experiments are less extensive. **HiSo ≲ LOZO.** |
| `ZuazHmXTns.md` (PAdaMFed, parameter-free FL) | 7.60 | Very strong theoretical paper with minimal assumptions. HiSo's theory is more conditional and less clean. **HiSo < PAdaMFed.** |
| `zqXANcFO9T.md` (compressed decentralized learning) | 1.67 | Paper with flawed assumptions and weak contributions. HiSo is substantially stronger in both theory and experiments. **HiSo ≫ this.** |
| `C7XoUdJ5ZC.md` (FLAIR, FL with CVAE) | 3.00 | Paper with unsubstantiated claims and weak validation. HiSo's claims are better supported. **HiSo ≫ FLAIR.** |
| `DJRd4IQHGQ.md` (FeedSign, 1-bit FL) | 5.25 | Proposes an orthogonal approach (1-bit communication). HiSo has stronger theory but similar experimental scope. **HiSo ≈ FeedSign.** |

The paper sits in the solid-accept range relative to the calibration corpus. It makes a genuine algorithmic contribution (Hessian-informed ZO in FL with scalar-only communication) and provides a theoretical framework that, while conditional, goes beyond prior work (DeComFL). The experiments show clear acceleration. The main limitations — the conditional nature of the strongest rates and the modest experimental scale — are common in this area and do not undermine the core contribution. Compared to the DeComFL paper (accepted with avg 6.25), HiSo offers additional algorithmic novelty but has slightly weaker empirical validation.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**