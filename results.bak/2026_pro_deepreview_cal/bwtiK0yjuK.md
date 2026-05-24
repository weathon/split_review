Now I have a clear picture. Let me write the consolidated review.

---

## Summary

This paper presents the first framework for offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). The authors propose a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), prove consistency in estimating both the number and locations of change points (Theorem 1), derive the first limiting distributions for network change point estimators (Theorem 2), and develop a data-driven confidence interval procedure. Extensive simulations across four scenarios and a real-world agricultural trade network analysis demonstrate strong empirical performance against existing baselines.

## Strengths

- **Genuine novelty — first offline CP framework for dynamic multilayer networks.** The paper addresses a problem not previously studied in the literature. The two-stage algorithm design (seeded binary segmentation + TH-PCA refinement) is thoughtfully motivated by the low-rank Tucker structure of the expected CUSUM tensors (Section 2.3), and the computational complexity of $O(Tn^2 L r \log^2(T \vee n))$ is clearly reported.

- **Rigorous theoretical guarantees (Theorem 1).** The consistency result proves $\tilde{K} = K$ and $|\tilde{\eta}_k - \eta_k| \leq C_c \log(T) / \kappa_k^2$ with probability at least $1 - CT^{-c}$, under an SNR condition (Assumption 2) that naturally extends the single-layer condition of Wang et al. (2021) to the multilayer setting. The localization rate of order $\kappa_k^{-2}\log(T)$ improves substantially over the online-setting rate of Wang et al. (2025).

- **First limiting distributions for network change point estimators (Theorem 2).** The derivation of a two-sided Brownian motion functional as the limiting distribution, under the vanishing jump regime, has no prior analogue in the network change point literature. This result directly enables the data-driven confidence interval construction in Section 3.1.

- **Strong and comprehensive empirical validation.** Across all four simulation scenarios (Table 1), CPDmrdpg achieves near-perfect change point count estimation and negligible Hausdorff distances, while competitors (gSeg, kerSeg) frequently add or miss change points. The method remains robust under model misspecification (Scenarios 2 and 3). Confidence intervals achieve nominal 95% coverage in Scenarios 1, 2, and 4 at $n=100$ (Table 2). The real-world agricultural trade analysis detects change points (1991, 1999, 2005, 2013) that align with well-known geopolitical events — German reunification, WTO conferences, and the Bali Package — demonstrating practical interpretability.

## Weaknesses

### Fatal

None.

### Major

- **Theory-practice gap in data splitting.** Algorithm 1 assumes four mutually independent adjacency tensor sequences for theoretical analysis, but the practical implementation uses only two split sequences via odd-even splitting (acknowledged on lines 119–120: "imposed for theoretical convenience"). The theoretical results (Theorems 1 and 2) are proved under the four-sequence assumption and do not directly apply to the evaluated procedure. The paper acknowledges the discrepancy but does not discuss whether the guarantees extend to the two-sequence approach or quantify any potential loss in statistical efficiency. This is a methodological gap between what is proved and what is run.

- **Strong uniformity in Assumption 1(ii)–(iii).** The rank and singular-value conditions are stated for *any* interval $0 \leq s < t < e \leq T$, which is a very strong requirement — the intervals that appear in the algorithm are data-dependent, and uniform control over all possible intervals is a heavy assumption. The paper notes (lines 205–209) that working intervals contain exactly one change point with high probability, implying bounds on the relevant ranks, but this argument is deferred to Appendix E and the assumption as stated remains more general than what the proofs require. Readers may be uncertain about the range of models satisfying these conditions.

### Minor

- **CI coverage degradation under misspecification.** In Scenario 3 (where Model 1 is violated — changes occur only in community sizes within one layer), 95% CI coverage drops to 76.67% at $n=100$ (Table 2). The paper notes this is due to model violation and small layer-specific changes, and coverage improves at $n=150$ (95.33%), but does not analyze *why* the violation specifically damages coverage — whether through variance estimation bias or a shift in the limiting distribution.

- **Inference restricted to vanishing jumps.** The confidence interval procedure (Section 3.1) is provided only for the vanishing jump regime ($\kappa_k \to 0$). The non-vanishing regime results are deferred to Appendix A. The paper acknowledges this limitation (Section 5), but it narrows the immediate practical scope of the inference procedure.

- **Threshold $\tau$ selection is not fully automated.** The threshold is set as $\tau = c_{\tau,1} n \sqrt{L} \log^{3/2}(T)$ with $c_{\tau,1} = 0.1$ as a fixed constant drawn from the theoretical window in Theorem 1. While the paper reports sensitivity analysis over $c_{\tau,1} \in \{0.05, \dots, 0.25\}$ (Appendix G.1), some practical guidance for data-driven threshold selection would improve accessibility.

### Trivial

None.

## Nice-to-Haves

- A brief discussion of why gSeg fails so dramatically (e.g., whether the default $\alpha = 0.05$ is poorly calibrated for tensor edge-count statistics) would help readers understand the performance gap.

- Including the U.S. air transport CI results (deferred to Appendix G.2) in the main text, or at least noting whether similarly narrow intervals occur there, would strengthen the practical evidence.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that Assumption 1 justification is a "brief heuristic" with no theoretical grounding.** The main text (lines 205–209) provides concrete reasoning: working intervals contain one change point, bounding the relevant ranks by $\text{rank}(Q(\eta_k)) + \text{rank}(Q(\eta_{k+1}))$. The full argument is in Appendix E (stripped by the parser). The harsh critic's uncertainty about the appendix content cannot be the basis for a weakness — removed per the rule that speculative criticisms depending on unseen appendix content must be demoted or removed.

- **Harsh critic's "missing parts" complaint about real-data CIs for only one dataset.** The U.S. air transport results are explicitly referenced as being in Appendix G.2. The parser strips appendices; the content exists in the original submission.

- **Strength Finder's generic strengths about "important problem" and "interesting question."** These are superficial framing strengths without concrete anchors — removed.

## Novel Insights

The paper's combination of seeded binary segmentation with TH-PCA-based refinement is well-suited to the multilayer tensor structure, and the derivation connecting the expected CUSUM tensors to Tucker representations (via the $\mathbf{S} \times_1 X \times_2 X \times_3 \tilde{Q}^{s,e}(t)$ decomposition in Section 2.3) provides a clean bridge between the change point problem and low-rank tensor estimation. The confidence interval construction via simulation of the limiting two-sided Brownian motion functional is a practical innovation that could be adapted to other change point settings.

## Suggestions

- **Close the data-splitting gap:** Either (a) modify the practical procedure to use modulo-4 partitioning into four disjoint interleaved subsets, which would align the implementation exactly with the theory with minimal practical impact (effective sample size remains $T/4$ per sequence), or (b) extend the theoretical analysis to cover the odd-even two-sequence approach, quantifying any efficiency loss.

- **Refine Assumption 1:** State the assumption conditions more precisely on the intervals that actually arise in the algorithm (those containing at most one change point), rather than uniformly over all possible intervals. Discuss when the rank conditions follow from more primitive assumptions on the weight matrices $\{W_{(l)}(t)\}$.

- **Analyze Scenario 3 CI coverage:** Investigate whether the coverage drop stems from biased variance estimation ($\hat{\sigma}_{k,k'}^2$) or from a shift in the limiting distribution under misspecification. This would clarify when the CI procedure can be trusted in practice.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| TV-HMM change point (I5MquO1g7R) | 4.75 | R1 | Our paper has stronger theory and much clearer empirical gains over baselines |
| Community recovery w/ side info (zhFyKgqxlz) | 5.75 | R2 | Our paper has experiments, real data, and clearer novelty |
| NetInfoF (KY8ZNcljVU) | 7.33 | R2 | NetInfoF has more polished presentation and strong practical value, but a potentially incorrect proof; our paper's theory is sounder though has a practice-theory gap |
| DUCI (EUSkm2sVJ6) | 7.60 | R1 | Cleaner contribution with fewer theoretical gaps; our paper's theory is more substantial but less tight |
| Hidden Cost of Waiting (A3YUPeJTNR) | 8.00 | R1 | More polished, but different domain; our paper has more technical depth but less theoretical tightness |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** The paper is clearly stronger than the community recovery paper (5.75 — no experiments, limited novelty) and the TV-HMM paper (4.75 — weak empirical gains). It is somewhat below the NetInfoF paper (7.33) and DUCI (7.60), which have tighter theory-to-practice alignment and fewer acknowledged gaps. The paper lands at **6.5**: a solid contribution with genuine novelty, strong theory, and comprehensive experiments, held back by a theory-practice gap in data splitting and strong uniformity assumptions that are not fully resolved in the main text.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>