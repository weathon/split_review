Now I have all the information needed to cross-verify each claim. Let me write the final consolidated review.

---

## Summary

This paper proposes COEBL (Competitive Co-evolutionary Bandit Learning), a novel algorithm for two-player zero-sum matrix games with bandit feedback. COEBL integrates evolutionary algorithm heuristics (Gaussian mutation + elitist selection) with the principle of optimism in the face of uncertainty, using randomized optimism rather than the deterministic optimism of UCB. The paper provides a regret bound of \(\tilde{O}(\sqrt{m^2 T})\) matching UCB's rate, and presents empirical results on Rock-Paper-Scissors, DIAGONAL, and BIGGERNUMBER games showing COEBL often outperforms EXP3, EXP3-IX, and UCB baselines.

## Strengths

- **First regret analysis for an evolutionary bandit learning algorithm in matrix games.** The paper claims and provides evidence for being the first to rigorously analyze regret of an evolutionary approach in this setting (Section 1.3, abstract). This is a genuine gap given the lack of theoretical analysis for evolutionary reinforcement learning methods.

- **Provably sublinear regret matching the deterministic optimism rate.** Theorem 2 establishes a worst-case Nash regret bound of \(2\sqrt{2c T m^2 \log(2T^2 m^2)} = \tilde{O}(\sqrt{m^2 T})\), demonstrating that randomized optimism via evolution can achieve the same asymptotic regret rate as UCB-based deterministic optimism.

- **Clear algorithmic design linking evolutionary mechanisms to optimism.** The mutation operator (Eq. 2) is explicitly designed to inject optimism by shifting the empirical mean proportionally to \(\sqrt{c\log(2T^2 m^2)/(1\vee n_{ij}^t+1)}\), and the elitist selection mechanism (lines 7–10 of Algorithm 1) provides a clear evolutionary interpretation. This allows the paper to attribute sublinear regret to a specific mechanism rather than treating the EA as a black box.

- **Evaluation across structurally diverse matrix games.** The experiments cover cyclic games (RPS), dominance-structured games (DIAGONAL), and comparison-based games (BIGGERNUMBER), with action spaces ranging from \(m=3\) to exponentially large \(2^n\) (up to \(n=7\), i.e., 128 actions). This breadth provides a more informative test than a single game.

- **Honest assessment of limitations.** The paper acknowledges that COEBL, like all tested algorithms, fails to converge to the Nash equilibrium for large action spaces (\(n\geq 4\) in DIAGONAL), and discusses the technical limitation requiring \(c\geq 8\) in the analysis (Section 5, conclusion).

## Weaknesses

### Fatal
None.

### Major

- **Abstract contradicts the paper's own related work section, overstating novelty.** The abstract states "it remains an open question whether randomised optimism can also exhibit sublinear regret" in matrix games. Yet the paper's own Section 1.4.1 states: "O'Donoghue et al. (2021) conducted a detailed regret analysis on the UCB algorithm, **Thompson Sampling**, and K-Learning. They showed sublinear regret bounds for these existing bandit baselines in matrix games." Thompson Sampling is a canonical randomized optimism algorithm, so sublinear regret for randomized optimism in matrix games is already established. The paper's actual contribution is about *evolutionary* randomized optimism specifically, but the abstract's phrasing is misleading and should be corrected.

- **Algorithm underspecification for unobserved matrix entries.** Algorithm 1 (line 4) computes \(\mathrm{Mutate}(\bar{A}_{ij}^t, \dots)\) for all \(i,j\in[m]\), and \(\bar{A}_{ij}^t\) is defined as the empirical mean of sampled entries. For entries with \(n_{ij}^t = 0\), no samples exist and the empirical mean is undefined. The paper never states what value is used for these entries (initialization to 0, or some default). While this is likely fixable (e.g., default to 0 or use the mutation's optimistic bias alone), the omission means the algorithm as presented is not fully specified, and Lemma 1's optimism guarantee technically has an undefined object for unobserved entries. The authors should clarify this implementation detail.

- **Unfair hyperparameter comparison in experiments.** COEBL's mutation rate is tuned per game (\(c=2\) for RPS, \(c=8\) for all others, Section 4), while EXP3-IX hyperparameters are taken wholesale from Cai et al. (2023) which studies Markov games under different assumptions. The paper does not discuss whether the baselines were tuned for the matrix game setting, nor does it report sensitivity of any algorithm (including COEBL) to its hyperparameters. Since COEBL benefits from per-game tuning, the "outperforms" claim is weakened without evidence that the comparison is fair.

### Minor

- **Algorithm requires knowledge of horizon \(T\) and action count \(m\).** The mutation operator's mean shift depends on \(\sqrt{c\log(2T^2 m^2)/(1\vee n_{ij}^t+1)}\), which needs \(T\) (the horizon) and \(m\) (number of actions) to be known in advance. The paper does not discuss an anytime variant or how the regret bound would degrade without knowledge of \(T\). While common in early bandit work, this limits the algorithm's applicability in truly online settings.

- **Unmotivated constant in empirical bound line.** In Figure 3, the black dotted line labeled "theoretical bound \((0.1\sqrt{K^2 T})\)" does not correspond to any constant derived from Theorem 2 (which gives \(2\sqrt{2c T m^2\log(\dots)}\)). The factor 0.1 appears arbitrary and seems chosen to fit the plots rather than derived from theory. This undermines the visual claim that COEBL stays "beneath the theoretical bound."

- **No computational cost comparison.** COEBL requires solving a linear program at each round (line 6 of Algorithm 1) to compute the mutated policy, whereas baselines (EXP3, EXP3-IX, UCB) have closed-form updates. The paper does not report wall-clock time or address this practical concern, which is relevant for large \(m\).

- **Missing analysis of why COEBL converges to Nash when baselines do not.** For DIAGONAL \(n=2,3\), COEBL's TV-distance drops to near zero while baselines diverge. The paper does not explain whether this is due to hyperparameter choices, structural properties of COEBL's selection mechanism, or some other factor. Without this analysis, the convergence claim is descriptive rather than explanatory.

- **"Outperforms" claim is too strong given RPS results.** The abstract and Section 1.3 claim COEBL "outperforms existing methods." In the RPS self-play (Figure 1), COEBL performs comparably to UCB rather than clearly outperforming it, and the ALG-vs-ALG advantage over UCB is small (Figure 2, regret ~5–10 with overlapping confidence intervals). The empirical evidence is strongest on DIAGONAL and BIGGERNUMBER, so the claim should be qualified.

### Trivial

- The paper introduces Definition 2 (p-ary games) but only experiments with ternary games. This is a minor framing issue — the definition provides useful context but is not used in any technical result.
- The constant 0.1 in the empirical bound line is not derived from the theorem.

## Nice-to-Haves
- An ablation study comparing COEBL with and without the elitist selection step would isolate whether the evolutionary selection mechanism actually improves performance, or whether the mutation alone drives the results.
- A sensitivity sweep over the mutation rate \(c\) on at least one game would demonstrate that the results are not brittle and address the hyperparameter concern.
- Comparison against Thompson Sampling (which is also randomized optimism) would clarify the paper's positioning relative to existing work.

## Removed Points
These points were identified by a reviewer but are removed or weakened here for the following reasons:

1. **"Insufficient proof / missing technical analysis" (Critical Issue 3 from harsh critic):** The paper references "supplementary material" (line 101) and the parser strips appendix/supplementary sections from all papers. The detailed proof likely exists in the original submission's supplementary material. This point is removed per policy.

2. **"Definition 2 (p-ary games) is introduced but never used":** Removed as a nitpick. The definition provides context; the paper states "we mainly focus on ternary two-player zero-sum games," so the concept is used implicitly.

3. **"Only one noise setting tested":** The paper already acknowledges this limitation in Section 5 ("investigating the algorithm's performance under different noise distributions... could yield further insights"). This is a self-acknowledged limitation, not a hidden flaw.

4. **"COEBL slightly worse than UCB at many iterations in RPS self-play":** The paper's own text describes COEBL as having "sublinear regret... similar to other bandit baselines" in RPS self-play, and the head-to-head shows a small advantage. The "outperforms" claim is more strongly supported on DIAGONAL and BIGGERNUMBER. This point is subsumed by the Minor weakness about qualifying the outperformance claim.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel interpretation that the paper itself does not provide.

## Suggestions
1. **Correct the abstract's claim about "open question whether randomised optimism can exhibit sublinear regret."** Acknowledge that Thompson Sampling already achieves this (as the paper's own related work section states), and reframe the novelty more precisely: the paper's contribution is the *first regret analysis of an evolutionary* randomized optimism algorithm for matrix games.
2. **Explicitly state the default/initial value of \(\bar{A}_{ij}^t\) for entries with \(n_{ij}^t=0\)** in Algorithm 1, and verify that Lemma 1 holds with this initialization.
3. **Add an ablation or hyperparameter sensitivity experiment** to address the per-game tuning concern. At minimum, run COEBL with \(c=8\) on RPS (not just \(c=2\)) to show the algorithm is not brittle.
4. **Derive or remove the unmotivated constant 0.1** in the theoretical bound line of Figure 3; if it is an empirical observation rather than a theoretical bound, label it clearly as such.
5. **Add a brief discussion of the anytime setting**, noting whether the doubling trick applies or how the bound degrades without knowledge of \(T\).

## Score and Decision

**Overall assessment:** This paper tackles an interesting intersection of evolutionary algorithms and bandit learning, and the core idea of designing a mutation operator that implements optimism is clever. The regret bound matching UCB's rate is a non-trivial result. However, the paper suffers from two significant issues: (1) the abstract misrepresents the state of the art by claiming randomized optimism's sublinear regret is "an open question" when Thompson Sampling already addresses it (contradicting the paper's own related work section), and (2) the hyperparameter comparison in experiments is uneven (COEBL tuned per game while baselines use default settings from a different problem domain). The algorithm also has an underspecified initialization detail for unobserved entries. These issues are fixable, but in their current form they weaken the paper's claims. The submission has genuine contributions but requires substantial revision before it can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>