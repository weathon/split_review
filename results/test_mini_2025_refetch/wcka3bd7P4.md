Now I have thorough understanding. Let me compose the final consolidated review.

## Summary

FROND replaces the integer-order derivative in continuous GNNs (GRAND, CDE, GREAD, etc.) with Caputo fractional derivatives of order β ∈ (0,1], introducing non-local, memory-dependent dynamics. The paper provides a random-walk interpretation of the resulting fractional diffusion process, proves algebraic convergence Θ(t^{−β}) for the linear case (Theorem 2), and extends six existing continuous GNN architectures to their fractional counterparts. Experiments on node and graph classification show consistent improvements over the integer-order baselines, particularly on tree-structured datasets where gains are substantial.

## Strengths

- **Principled theoretical foundation for oversmoothing mitigation.** Theorem 2 proves that the solution of the fractional diffusion equation F-GRAND-l converges to stationarity at a slow algebraic rate Θ(t^{−β}) rather than the exponential rate of the integer-order Markovian case. This formal connection between fractional order and convergence rate is novel and directly supports the claim that FROND mitigates oversmoothing through a grounded mechanism.

- **Clean non-Markovian random walk interpretation.** Theorem 1 establishes that the solution of F-GRAND-l corresponds to a random walk whose transition probabilities depend on the walker's full history (Eq. 11). When β→1 the walk reduces to the standard Markovian walk of GRAND-l, showing the framework is a proper generalization.

- **Consistent improvements across diverse continuous GNN backbones without added parameters.** Tables 1, 2, and 4 show that FROND variants (F-GRAND-l, F-GRAND-nl, F-CDE) outperform their integer-order counterparts on nearly all datasets. The gains are particularly large on tree-structured data (Airport: +17.6%, Disease: +17.9%). The framework extends to GRAND++, GREAD, and GraphCON (Appendix E), demonstrating it is a general drop-in enhancement.

- **Empirical validation of oversmoothing mitigation in very deep networks.** Figure 2 shows F-GRAND-l maintaining stable test accuracy up to 128 layers, whereas GRAND-l degrades significantly on the Airport dataset. This provides concrete experimental support for the algebraic convergence predicted by Theorem 2.

- **Dataset-dependent optimal β revealed by ablation.** Table 3 shows Cora prefers β=0.9 while Airport prefers β=0.1, supporting the premise that integer-order (β=1) is not universally optimal and that the adjustable memory can be tailored to graph topology.

## Weaknesses

### Major

- **Marginal gains on standard benchmarks with overlapping error bars.** On 8 of 10 datasets (Cora, Citeseer, Pubmed, CoauthorCS, Computer, Photo, CoauthorPhy, ogbn-arxiv), F-GRAND-l's gain over GRAND-l is ≤1.2%, and in most cases the standard deviations overlap substantially. The paper's language ("significantly bolster the performance," line 268) overstates the magnitude of these improvements. While the gains are directionally consistent, the evidence does not support a claim that the fractional framework provides practically meaningful benefits on standard homophilic benchmarks.

- **No error bars on the oversmoothing experiment.** Figure 2, which is the paper's most direct empirical evidence for Theorem 2, appears to show single-run results without confidence bands or multiple-seed variability. The comparison between F-GRAND-l and GRAND-l on Airport is compelling, but without error bars or multiple seeds it is difficult to judge whether the observed behavior is robust. Given that the GRAND-l baseline itself has high variance on Airport (std 9.6 in Table 1), this is a notable omission.

- **Missing comparison to simpler non-Markovian mechanisms.** The paper attributes the oversmoothing benefit to the specific fractional-derivative memory. However, alternatives such as residual/skip connections (GCNII, APPNP) or simple dense connectivity can also introduce non-Markovian dynamics. Without comparing to such baselines, it is unclear whether the benefit comes from the *specific* fractional memory structure or from any mechanism that breaks the Markovian assumption. This leaves the reader unable to isolate the contribution of the fractional calculus framework.

### Minor

- **The connection between β and fractal dimension remains speculative.** While the paper motivates fractional derivatives via fractal media and cites relevant physical theory (Nigmatullin, 1992; Tarasov, 2011), the experiments only show that different β values work better for different datasets. The claim that the optimal β "could reveal the degree of fractality" is not substantiated by any quantitative link between β and a computed fractal dimension of the graph. The paper would benefit from acknowledging this more clearly.

- **The oversmoothing experiment only covers the linear variant (F-GRAND-l).** The theoretical analysis (Theorem 2) only applies to the linear diffusion case. The nonlinear variants (F-GRAND-nl, F-CDE, etc.) also show improved depth stability, but the paper does not discuss whether the algebraic convergence guarantee extends to them or whether a different mechanism is at play.

### Trivial

- The figure caption for Figure 2 is duplicated three times (lines 226-230), a parsing artifact that should be cleaned.
- Table 1 uses mixed formatting (some β rows use `<math>` tags, others use plain LaTeX).

## Nice-to-Haves

- A direct numerical verification of the algebraic convergence rate: for the linear case, compute $\|\mathbf{X}(t) - \boldsymbol{\pi}^\top \sum_i \mathbf{x}_i\|$ from the numerical solution and fit a power law to confirm the exponent is close to β. This would bridge the theory (Theorem 2) and the numerical solver.
- Report error bars (multiple seeds) for the oversmoothing experiment (Figure 2).
- Include a table of training time and relative memory usage on representative datasets (e.g., Cora, Airport, ogbn-arxiv) for F-GRAND vs. GRAND.

## Removed Points

- **Theoretical guarantees do not transfer to the numerical solver / memory window not reported.** The paper explicitly states that the basic predictor is used (Section 4, line 199) and references Appendix C.3 for the short-memory principle and Appendix D.6 for computational complexity. Since the appendix is stripped by the parser, these criticisms cannot be verified against the paper as presented. The critic's speculation about memory truncation weakening the algebraic convergence is not a verifiable flaw from the available text.
- **No analysis of computational overhead.** The paper references "computational complexity of F-GRAND in Appendix D.6" (line 201). Per the hard rules, missing appendix content should not be counted as a weakness.
- **Statistical significance tests requested.** Standard practice in this community is to report means and standard deviations over random splits rather than paired t-tests; the paper follows this convention. Requesting a different standard is a soft preference, not a weakness.
- **The random walk perspective "not used for computation."** Many GNN papers provide theoretical interpretations that are not directly used for computation (e.g., the heat diffusion interpretation of GRAND itself). This is not a weakness — the random walk perspective is presented as an interpretation, which is its stated purpose.

## Novel Insights

The human reviewers collectively highlight a tension between the paper's strong theoretical machinery (algebraic convergence proof, non-Markovian random walk interpretation) and the modest empirical returns on standard benchmarks. This mirrors a broader pattern in the continuous GNN literature: papers that introduce principled dynamical-system frameworks often face the challenge that their improvements are concentrated in niche settings (here, tree-structured/fractal graphs) while being marginal on standard benchmarks. The most incisive observation from the reviews is that the paper's central causal claim — "fractional memory → algebraic convergence → oversmoothing mitigation" — is supported at the level of the continuous FDE but not directly verified at the level of the discrete numerical solver actually deployed. Filling this gap (e.g., by numerically confirming the Θ(t^{−β}) rate from the Adams-Bashforth-Moulton solver) would substantially strengthen the argument. The fractal dimension connection (β ↔ graph fractality) is an intriguing direction that the paper gestures at but does not empirically substantiate, and this would be a natural target for future work.

## Suggestions

1. Provide multiple-seed results with error bars for the oversmoothing experiment (Figure 2).
2. Tone down the language about "significant" improvement on datasets where the gain is ≤1.2% and error bars overlap.
3. Add a comparison to a simple residual-connected GRAND variant (e.g., GRAND with dense skip connections) to isolate the specific benefit of the fractional framework vs. any non-Markovian mechanism.
4. If space permits, include a small numerical verification that the basic predictor preserves the Θ(t^{−β}) algebraic rate predicted by Theorem 2.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- *Weak anchors* (avg 2.50–3.40): Papers on oversmoothing/GNN initialization with generic contributions. FROND is clearly stronger — it has novel theory and consistent (if modest) empirical gains.
- *Middle anchors* (avg 3.67–6.60): The most relevant is "When Graph Neural Networks Meet Dynamic Mode Decomposition" (avg 6.60, accepted Poster), which connects GNNs to Koopman/DMD theory with similar empirical patterns and similar reviewer criticisms (marginal gains, missing scalability analysis). FROND is comparable: the theory is arguably cleaner (a single clean algebraic rate result vs. DMD approximation theory), but the empirical gains are slightly more modest on standard benchmarks.
- *Strong anchors* (avg 8.00+): Papers with deep theoretical analysis (graphon approximations, Hölder stability, NTK convergence). FROND is not at this level — the theory only covers the linear case and the empirical scope is less ambitious.

**Round 1 bracket:** 5.0–7.5.

**Round 2 — Narrowing:**
- "Oversmoothing as Loss of Sign" (avg 5.25, Rejected): Also addresses oversmoothing with theory + experiments. FROND is notably stronger: its theory is cleaner, the experiments are more extensive, and the baselines are more complete. The rejection of that paper was driven partly by outdated baselines and questionable theory, neither of which applies here.
- "When Graph Neural Networks Meet Dynamic Mode Decomposition" (avg 6.60, accepted Poster): The closest comparison. Both papers introduce a principled theoretical framework from another field (DMD/Koopman vs. fractional calculus) into continuous GNNs, both show consistent but modest gains, and both face similar criticisms (minor improvements, missing runtime analysis). FROND is slightly weaker empirically (DMD had SOTA on some tasks) but slightly stronger theoretically (the algebraic convergence is a crisp, directly relevant result). Overall comparable.
- "Diffusing to the Top" (avg 5.75, accepted Poster): Uses diffusion for hyperparameter tuning. FROND has stronger theoretical grounding.

**Final score:** 6.0. The paper makes a principled theoretical contribution (algebraic convergence for fractional graph diffusion) and demonstrates consistent improvements, but the practical significance is undercut by marginal gains on most standard benchmarks (≤1.2%) and the lack of error bars on the key oversmoothing figure. The framework is novel, general, and well-motivated; the weaknesses are addressable but real.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>