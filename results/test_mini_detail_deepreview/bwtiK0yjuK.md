Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). The authors propose a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), establish consistency for the number and locations of change points, and — most notably — derive the first limiting distributions for change point estimators in the network literature. A fully data-driven confidence interval procedure is also developed. Experiments on simulated data (four scenarios, two underlying models) and a real agricultural trade network demonstrate strong performance against generic competitors (gSeg, kerSeg).

## Strengths

1. **First limiting distributions for change point estimators in network data.** Theorem 2 provides the asymptotic distribution of refined change point estimators in the vanishing jump regime — a result the paper correctly identifies as new to the network literature. This is a genuine theoretical contribution that goes well beyond the consistency results common in prior work.

2. **Consistency guarantees with sharp rates.** Theorem 1 establishes that Algorithm 1 correctly estimates the number of change points and localizes them within error \(O(\kappa_k^{-2}\log T)\). Remark 1 correctly notes this improves on the online rate in Wang et al. (2025) by removing a dependence on \(d^2 m_{\max} + nd + Lm_{\max}\).

3. **Clear, well-structured presentation.** The two-stage algorithm (seeded binary segmentation + low-rank tensor refinement) is clearly defined, the theoretical assumptions are stated explicitly and discussed, and the confidence interval construction is given as a reproducible step-by-step procedure.

4. **Strong empirical performance.** Across all four simulation scenarios in Table 1, CPDmrdpg achieves near-zero error on all metrics, while generic competitors (gSeg, kerSeg) show inflated Hausdorff distances and frequent errors in estimating the number of change points. The method remains robust even when Model 1 is violated (Scenarios 2 and 3). Table 2 reports coverage and length of the confidence intervals.

5. **Real-data demonstration with interpretable findings.** The change points detected in the agricultural trade network (1991, 1999, 2005, 2013) align with documented geopolitical and policy events, and the confidence intervals from Section 3.1 are computed and reported.

6. **Honest discussion of limitations.** Section 5 acknowledges the \(\Delta = \Theta(T)\) spacing assumption, the vanishing-jump restriction on inference, and the temporal independence assumption, pointing to specific relaxation strategies.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Confidence interval validation limited to high-SNR settings.** The CI coverage in Table 2 is strong (often 100%) but the average lengths are extremely narrow (e.g., 0.003 for Scenario 1, \(n=100\)). Since the true change points are integer-valued, sub-unit widths on the original time scale indicate very high estimator precision under strong SNR. However, the paper does not include a lower-SNR calibration — for instance, a setting closer to the theoretical lower bound of Assumption 2 — to verify that coverage remains reliable when the estimator is less precise. Coverage in Scenario 3 (76.67% at \(n=100\)) hints at deterioration, but no dedicated study is provided. This would strengthen the practical utility claim.

2. **Odd-even data splitting acknowledged but not justified.** The paper states (line 119) that the implementation uses a single observed sequence split into odd and even indices for the two pairs \(\{A, A'\}\) and \(\{B, B'\}\), and that mutual independence of the four sequences is "imposed for theoretical convenience." No argument is given for why this practical approach satisfies the independence requirements of the theory. While the claim is plausible (conditional independence given the latent positions and weight matrices), the gap between the theoretical assumption and practical implementation is left unaddressed.

3. **Main-text baselines are generic; key comparisons are appendix-only.** The main experiments compare CPDmrdpg only against gSeg and kerSeg — generic methods not designed for multilayer networks. The paper mentions comparisons with Wang et al. (2025) and deep-learning baselines in Appendix G.1, but no summary of those results appears in the main text. Given the claim of "substantial outperformance over existing state-of-the-art algorithms" in Section 1.1, a headline sentence or a reference to the appendix results in the main text would strengthen the claim.

4. **Real-data \(T=35\) is small for asymptotic inference.** The confidence intervals for the agricultural trade network are derived from asymptotic theory (\(T \to \infty\)), but \(T=35\) is a short time horizon. The sub-unit CI widths (e.g., (5.97, 6.03) for time point 6) should be discussed with a caveat about the applicability of the asymptotic approximation. The paper does not include such a discussion.

### Trivial

- TH-PCA is central to Stage II and Section 3, but Definition 5 only names it and references Algorithm 2 in the appendix. A one-sentence description of what TH-PCA does (e.g., "a low-rank Tucker decomposition estimator with truncation") would improve main-text readability.
- The description of the refined scan statistic in Definition 5 appears to contain a typographical glitch in the raw text (\(|\tilde{\mathbf{P}}^{...} / \tilde{\mathbf{P}}^{...}|_{\mathbb{F}}, \tilde{\mathbf{A}}^{...}|\)), which may be a parser artifact.

## Nice-to-Haves

- A brief practical heuristic for choosing the Tucker rank inputs to TH-PCA (beyond the fixed values \(r_1=r_2=15, r_3=L\) used in experiments).
- Reported computation times for the simulated settings to help readers assess scalability.
- A note on whether the confidence intervals can be extended to the non-vanishing jump regime (mentioned as future work in Section 5).

## Removed Points

- **Concern about "missing related works"**: Not included because I have no external sources to verify.
- **Concern about TH-PCA being "incomplete" in main text**: Downgraded to trivial (a one-line summary would help but the appendix reference is standard).
- **Concern that the paper does not report scalability beyond asymptotic complexity**: Moved to nice-to-have.
- **Strength about "interpretable real-data results with valid confidence intervals" being a "supporting strength"**: Kept but rephrased as a genuine strength — the real-data demonstration with CIs is concrete evidence of practical utility.
- **Strength Finder's "theoretical coverage of both vanishing and non-vanishing jump regimes"**: Kept the factual claim but note the non-vanishing regime results are in the appendix.
- **Harsh Critic's point that "the confidence interval simulation step should justify why the discretized grid approximates the argmin of the continuum process"**: This is standard practice in the change point inference literature (see e.g., Xu et al. 2024, cited in the paper). The discretization of the Brownian argmin by i.i.d. Gaussian sums is a well-established approximation. Removed as a nitpick.
- **Harsh Critic's point about "no discussion of how to choose Tucker ranks"**: Moved to nice-to-have.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely new insight about the method or its implications that the authors did not already provide.

## Suggestions

1. Add a dedicated low-SNR calibration experiment for the confidence intervals, or at minimum a discussion explaining why sub-unit widths are not evidence of over-confidence and under what SNR conditions practitioners should trust the intervals.
2. Clarify the independence argument for the odd-even splitting approach with a brief paragraph explaining why it satisfies the theoretical mutual-independence assumption.
3. Add a single sentence in the experimental section summarizing the Appendix G.1 comparison results (e.g., "CPDmrdpg also outperforms Wang et al. (2025) and Li et al. (2024); see Appendix G.1").
4. Include a caveat about \(T=35\) in the real-data analysis, noting that the confidence intervals rely on asymptotic theory and the sub-unit widths should be interpreted with caution.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ZHTYtXijEn.md (DIRAD continual learning) | 2.33 | 1 | Completely different topic; weak paper, not comparable |
| AxYTFpdlvj.md (Graph Decoding via GRDPG) | 2.00 | 1 | Different topic; weak paper, not comparable |
| sTI75sFQkn.md (dFCExpert) | 3.25 | 1 | Different topic (brain fMRI); not comparable |
| F8l0llkMk0.md (Map Equation Neural) | 3.33 | 1 | Different topic |
| vjHCyOWc7h.md (Mixture SBM Multiplex) | 4.40 | 1 | Same general area (multiplex graphs) but different problem; this paper has weaker experiments and less clear presentation. **Our paper is substantially stronger.** |
| ILqA09Oeq2.md (Nested Matrix-Tensor) | 6.20 | 1 | Relevant comparison — similar theoretical depth in tensor methods. This paper has weaker experiments (no real data) and some presentation issues. **Our paper is comparable or slightly stronger.** |
| SJ9lqUalq1.md (γ-Orthogonalized Tensor Deflation) | 5.25 | 1 | Tensor theory paper with less clear practical relevance. **Our paper is stronger.** |
| YtGtIAYDV3.md (Node-based Multiple Graph Learning) | 3.67 | 1 | Different problem; not directly comparable. |
| EUSkm2sVJ6.md (Dataset Usage Inference) | 7.60 | 1 | Completely different topic; not comparable |
| A3YUPeJTNR.md (Waiting for Accurate Predictions) | 8.00 | 1 | Completely different topic; not comparable |
| KbetDM33YG.md (Online GNN Evaluation) | 8.00 | 1 | Completely different topic; not comparable |
| uHLgDEgiS5.md (Training Data Influence) | 8.00 | 1 | Completely different topic; not comparable |

**Round 1 bracket:** 4.5 – 7.5 (the paper is clearly stronger than the 4.40 Mixture SBM paper and sits below the 7.5+ level which contains only unrelated topics).

**Round 2 (Narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| I5MquO1g7R.md (TV-HMM Change Point Detection) | 4.75 | 2 | Change point detection paper. Much weaker experiments (marginal improvement, simplistic setup), unclear advantages. **Our paper is substantially stronger on all dimensions.** |
| oP7arLOWix.md (KOWCPI conformal prediction) | 6.00 | 2 | Different problem (time-series conformal prediction). Not directly comparable. |
| ltZ9ianMth.md (RobustTSF) | 5.50 | 2 | Different problem. Not comparable. |
| 8TBGdH3t6a.md (H-PAD anomaly detection) | 5.60 | 2 | Different problem. Not comparable. |
| ZwhHSOHMTM.md (Dynamic functional connectome) | 6.67 | 2 | Different domain (neuroscience). Not directly comparable. |
| ZYm1Ql6udy.md (Bayesian Bi-clustering) | 6.67 | 2 | Different domain. Not comparable. |
| 8bjspmAMBk.md (Quality Measures Dynamic Graphs) | 7.50 | 2 | Dynamic graphs but different problem (evaluation metrics for generative models). Highly polished paper with broad applicability. **Our paper has deeper theoretical novelty but narrower scope.** |
| PkpNRmBZ32.md (SSMs as ConvNets) | 7.50 | 2 | Completely different topic. |

**Final assessment:** The paper delivers genuinely novel theoretical contributions (first limiting distributions for change point estimators in networks), a well-designed algorithm, and solid empirical validation including real data. The weaknesses are minor and addressable. Compared to the nearest anchor (Nested Matrix-Tensor, 6.20), this paper has stronger experiments (including real data), clearer presentation, and comparable theoretical rigor. It is clearly stronger than the TV-HMM paper (4.75) and weaker only than papers on completely different topics that achieved very high scores. The score 6.5 reflects a strong paper with minor, bounded weaknesses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>