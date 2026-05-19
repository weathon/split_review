- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper addresses three shortcomings in subspace inference for Bayesian neural networks: subspace construction, subspace evaluation, and inference efficiency. It proposes (1) a block-averaging (BA) construction strategy that partitions the SGD trajectory into blocks and averages within blocks to better approximate the full-trajectory subspace at the same memory cost as the tail-trajectory (TT) baseline; (2) novel subspace-evaluation metrics based on the Bayes factor and prior predictive (testing-data evidence); and (3) a randomized quasi-Monte Carlo importance sampling (RQMC-IS) method for posterior predictive inference in low-dimensional subspaces. Experiments on UCI regression and CIFAR classification benchmarks show that BA subspaces yield higher test log-likelihoods and classification accuracies than TT subspaces across a range of inference backends (VI, ESS, NUTS, RQMC-IS).

## Strengths

- **Block-averaging construction demonstrably improves subspace quality over tail trajectory.** Table 1 shows the BA subspace has an angular distance of only ~5° from the full-trajectory subspace, versus ~89° for TT — making BA nearly aligned with the ideal while TT is nearly orthogonal. Figure 1 visualizes that BA subspaces capture more high-likelihood weights. Algorithm 1 provides an online implementation with the same O(M) memory and O(n) time complexity as TT.

- **Novel evaluation metrics for subspaces using Bayes factors and evidence ratios.** Section 4.2 formally defines subspace evidence (Def. 1), Bayes factor (Def. 2), and testing-data evidence (Def. 3) — giving a principled quantitative framework for comparing subspaces directly, rather than relying only on downstream task metrics. Figure 3 uses these to show that BA subspaces yield Bayes factors close to 1 against the full-trajectory subspace while TT shows strong evidence against for small M, corroborating the angular-distance findings.

- **RQMC-IS provides efficient inference with proven convergence.** Theorem 2 establishes an O(N^{−1+ε}) RMSE rate for the RQMC-IS estimator under standard assumptions. Table 2 validates this empirically: RQMC-IS with N=1024 achieves RMSE 0.029, outperforming ESS (0.132) and VI (0.212) at lower computational cost (1,024 vs. 5,000+ forward passes).

- **Broad empirical evaluation across regression and classification.** Results span 11 UCI datasets (small and large) with fully-connected networks, plus CIFAR-10/10-C with VGG16 and PreResNet164. Tables 4–7 show consistent (though modest) improvements of BA+VI+RQMC over TT+VI across these settings.

## Weaknesses

### Fatal
None.

### Major

1. **The proposal distribution *q* for importance sampling is never explicitly specified.**  
   Section 4.3 introduces the SNIS and RQMC-IS estimators, discusses the inverse CDF transform \(F_q^{-1}\), and states that the induced posterior "could be similar to a standard multivariate Gaussian" — but the paper never commits to what *q* actually *is* in the experiments. Without knowing whether *q* is a standard Gaussian, a moment-matched Gaussian, or something else, the IS estimator is underspecified and the results in Table 2 cannot be reproduced from the main text. The convergence guarantees in Lemma 1 and Theorem 2 depend on *q* being a valid proposal with appropriate support; the reader cannot verify this without knowing the actual choice.

2. **Key performance tables (4–7) lack uncertainty quantification.**  
   Tables 4, 5, 6, and 7 report test log-likelihoods and classification accuracies as point values without standard deviations, confidence intervals, or any statement about statistical significance. This is in contrast to Table 1 and Figure 3, where the paper *does* report mean±sd and error bars. Many of the claimed improvements are modest (e.g., Table 6: accuracy differences of <0.5 pp). Without error bars, the reader cannot assess whether the observed gains are reliable or reflect noise from a single run.

3. **Comparison baselines are limited to the tail-trajectory method on real datasets.**  
   On UCI and CIFAR (Tables 4–7), BA is compared only against TT (and FT where feasible, which is mostly on the synthetic example). No comparisons are provided against random subspaces (Li et al. 2018), last-layer subspaces (Kristiadi et al. 2020; Daxberger et al. 2021a), or other PCA-based constructions (e.g., from multiple SWA snapshots). The paper cites these methods in the related work but does not include them in the experimental comparison. This narrow baseline set makes it difficult to judge whether BA is a genuinely better construction strategy or merely better than a single known baseline.

### Minor

1. **The Bayes factor (subspace evidence) computation is not described in the main text.**  
   Section 4.2 defines the marginal likelihood integral \(p(D\mid\mathcal{Z})\) but never explains *how* it is computed — whether by simple Monte Carlo from the induced prior, bridge sampling, Laplace approximation, or another method. This is not a fatal issue because the appendix likely contains the details (the paper states "The detailed experimental setup…are provided in Appendices B, C, and D"), and for a conference paper a brief sentence in the main text (e.g., "we approximate Eq. 6 using simple Monte Carlo with \(S\) samples from the induced prior \(p_{\mathcal{Z}}(z)\)") would suffice. Nevertheless, as presented, the reader cannot assess whether the Bayes factors in Figure 3 and Tables 3a/3b are reliable.

2. **No guidance is given for choosing the number of blocks *M*.**  
   Algorithm 1 and Figure 3 vary *M*, but the paper provides no heuristic, sensitivity analysis, or practical recommendation for how practitioners should set this hyperparameter. A brief ablation or rule of thumb would improve practical utility.

3. **The assumption that the induced posterior is approximately Gaussian is not empirically verified.**  
   Section 4.3 motivates IS by noting that the induced posterior "could be similar to a standard multivariate Gaussian." A simple diagnostic — comparing effective sample size under a Gaussian proposal versus a heavier-tailed alternative, or a normality test on the mapped trajectory weights — would strengthen the justification. This is an easy fix for a rebuttal or revision.

4. **Table 2's comparison does not specify which subspace (BA, TT, or FT) is used.**  
   The caption says "RMSE of posterior predictive estimations in different subspaces" without stating *which* subspace construction is employed. Since this table is used to argue for the efficiency of RQMC-IS, the subspace choice could affect the results.

### Trivial
None.

## Nice-to-Haves

- Ablation comparing the induced prior on *z* (via the linear transformation of the original weight prior) versus a hand-specified standard Gaussian prior on *z*, to validate the claim in Section 3.2 that using the induced prior matters.
- Explicit statement about whether the RQMC-IS method is gradient-free (it appears to require only forward passes), which is a practical advantage over NUTS/VI that is not highlighted.

## Removed Points

- **Criticism that the paper's claim "no metrics designed to directly evaluate subspaces" is too strong (citing Piironen & Vehtari 2017).** Removed per the rule against introducing missing related works that cannot be independently verified from the paper.
- **Criticism that the Bayes factor computation gap is "fatal" or "structural."** Downgraded to Minor because the appendix (stripped by the parser) likely contains the implementation details; the main-text gap is a clarity issue, not an invalidation of the contribution.
- **Criticism about "missing appendix, missing proofs in appendix, or absent references."** These are parser artifacts and removed per instructions.
- **Strength Finder's generic/superficial claims** (e.g., "this paper addressed an important problem"): removed as they lack concrete content tied to specific evidence in the paper.

## Novel Insights

The most interesting observation from the reviews is the asymmetry between the paper's careful reporting of uncertainty in the subspace-evaluation metrics (Figure 3 with error bars, Table 1 with mean±sd) and the complete absence of any uncertainty reporting in the downstream-performance tables (4–7). This suggests that the authors invested more rigor in the evaluation contribution (Bayes factors, evidence ratios) but treated the downstream prediction results as a standard "our method vs. baseline" comparison, even though the margins are small on several datasets. Cross-checking, this pattern is unusual for a paper that claims both a construction contribution and an evaluation contribution — one would expect consistent reporting practices across both.

## Suggestions

1. Add standard deviations (across at least 3 runs or train-test splits) to all entries in Tables 4–7.
2. Explicitly state the proposal distribution *q* used in the IS/RQMC-IS experiments (e.g., "a standard multivariate Gaussian \( \mathcal{N}(0, I_k) \)").
3. Add a one-sentence description of the evidence-integral approximation method to Section 4.2 (e.g., "We approximate \(p(D\mid\mathcal{Z})\) via Monte Carlo: \(\frac{1}{S}\sum_{s=1}^S p_{\mathcal{Z}}(D\mid z_s)\) with \(S\) draws from the induced prior \(p_{\mathcal{Z}}(z)\)").
4. Include at least one additional baseline (random subspace or last-layer subspace) on a subset of datasets to contextualize the BA improvement.
