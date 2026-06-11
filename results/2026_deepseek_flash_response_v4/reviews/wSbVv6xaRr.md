## Summary

This paper proposes FedMPDD, a federated learning algorithm that compresses client gradients by computing their directional derivatives along *m* random Rademacher vectors and transmitting only the *m* scalar projections (plus a seed). The server reconstructs a gradient estimate using the same random vectors. Averaging *m* projections overcomes the variance bottleneck of a single projection, achieving O(1/√K) convergence. Empirically, the method reduces communication while providing resistance to gradient inversion attacks (low SSIM).

## Strengths

1. **Diagnoses and fixes the single-projection convergence bottleneck.** The paper identifies that a single projected directional derivative has variance scaling as O(√d), forcing step size η = O(1/(d√K)) and convergence O(d/√K). By averaging *m* projections (m logarithmic in d), FedMPDD recovers O(1/√K) convergence matching FedSGD (Theorem 2). This is a genuine algorithmic insight grounded in the paper's own analysis — rare among compression-focused FL papers.

2. **Convincing empirical demonstration of a joint three-way trade-off under tight budgets.** Table 2 (CIFAR-10, 0.9 GB budget) is the paper's strongest evidence: FedMPDD (m=600, 0.2% of d) achieves 40.8% test accuracy with SSIM=0.14, while compression-only baselines (Top-k, lp-proj, SA-FedLora, QSGD) leak substantial information (SSIM 0.74–0.93) and LDP variants either leak or blow through the budget. FedMPDD is the only method that simultaneously stays within budget, achieves competitive accuracy, and keeps SSIM < 0.22. Table 1 (MNIST) shows a similar pattern with higher absolute accuracy (77.4%).

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between privacy claims and evidence.** The paper repeatedly uses "inherent privacy guarantees," "provable privacy against GIAs," and "concrete privacy guarantee" (lines 9, 32, 136, 144, 148), but the support has critical gaps:
   - **Lemma 2's bound depends on an unquantified constant.** The lower bound on data reconstruction error (Eq. 7) is proportional to 1/(L_v(x)²), where L_v(x) is the Lipschitz constant of the loss gradient with respect to the input data. For deep neural networks, this constant can be very large, yet the paper never measures, bounds, or even discusses L_v(x) for any model in the experiments. When L_v(x) is large, the bound provides no meaningful protection. A theorem whose practical force depends on an unexamined quantity is not a guarantee.
   - **No formal privacy metric.** Privacy is measured via SSIM under two specific gradient inversion attacks. SSIM is attack-dependent — a stronger attack could reconstruct data with far higher fidelity. The paper's language of "guarantees" conflates empirical robustness against known attacks with the formal, composable guarantees that the term "privacy guarantee" conventionally implies in this community.
   - **Unfair LDP comparison.** The paper argues LDP has "fluctuating" privacy because its relative reconstruction error scales with 1/||g_i||² (line 144). But this conflates a heuristic metric with LDP's formal (ε,δ) guarantee, which is calibrated to function sensitivity and is *independent* of gradient magnitude. The paper should compare against DP methods at a *fixed ε budget* rather than faulting LDP on an apples-to-oranges heuristic.
   - **Multi-round composition (Remark 2) receives insufficient prominence.** The bound T × m < d limits practical training. For d=300k and m=600, T < 500 rounds — many FL runs require more — yet this limitation is mentioned only in a remark and never discussed in the abstract or conclusion.

2. **Missing baselines for joint compression and privacy.** The paper claims "joint communication efficiency and privacy" but does not compare against methods designed for both, such as compressive DP (Amiri et al. 2021, which the paper cites) or LDP coupled with a compression scheme. The compression-only baselines (QSGD, Top-k, lp-proj, SA-FedLora) were never designed to provide privacy, so finding they leak information is expected. Including proper joint baselines would be necessary to substantiate the "joint" claim.

3. **LDP baselines untethered from formal DP budgets.** The Laplace noise variances (0.1, 0.5, 1, 10) are used without connecting them to standard (ε,δ) values. Reporting the ε budget is standard practice in DP literature; without it, the comparison between FedMPDD's attack-specific SSIM and LDP's formal guarantee is uncalibrated.

### Minor

1. **Practical gap in the convergence bound.** Theorem 2 shows O(1/√K) matching FedSGD asymptotically, but the bound includes ε G² / √K where ε = O(√(log(d)/m)). For practical values of m ≪ d, this additive term can be non-negligible, meaning the constant in the rate may be substantially worse than FedSGD. The paper does not discuss this gap.

2. **Inconsistency between Algorithm 2 and Remark 1 on computation.** Algorithm 2 (line 6) explicitly computes the full gradient g_i(x_k), then adds O(dm) inner products. Remark 1 then suggests JVP can avoid computing the full gradient entirely. While the paper acknowledges this possibility, the algorithm as presented does not reflect the claimed savings, and the conditions for JVP being beneficial (m < hpT/(h+p)) are deferred to the appendix.

3. **Modest absolute accuracy on CIFAR-10.** FedMPDD achieves 40.8% under 0.9 GB budget. While this is the best among constrained methods, Top-k (k=600) reaches 38.1% — only 2.7% lower — despite being a simple sparsification method with no privacy mechanism. The paper should more prominently acknowledge the accuracy sacrifice relative to unconstrained FedSGD (which would likely exceed 70%).

### Trivial
None.

## Nice-to-Haves
- Quantify or bound L_v(x) for the models used, or remove Lemma 2's reliance on this unquantified quantity.
- Include methods designed for joint compression+privacy (e.g., Amiri et al. 2021, DP+QSGD) in the baseline comparison.
- Report what ε-DP values the Laplace noise levels correspond to.
- Measure wall-clock time or throughput, not just bits.
- Report results on non-IID data splits for the privacy evaluation.

## Removed Points

These points were raised by the reviewers but are excluded from the main weaknesses for the reasons noted:

- **"Novelty is substantially overstated; method is standard random projection"** — The critic's framing understates the paper's specific diagnostic (single-projection convergence bottleneck → multi-projection fix) and the JL-based analysis supporting it. The seed-based reconstruction is also a practical contribution. The "fundamentally new paradigm" language is ambitious, but this is a framing concern, not a technical flaw. Removed as not supported by the evidence — the method's core mechanism (multi-projection averaging with Rademacher vectors) is presented with a clear theoretical motivation that goes beyond a generic application of random projections.

- **"Lemma 1 doesn't directly imply data cannot be reconstructed"** — This is a restatement of the L_v(x) issue already covered in Major Weakness #1. Merged.

- **"The ε term in the convergence bound needs careful interpretation"** — Already covered in Minor Weakness #1. Merged.

- **"Top-k is only 2.7% below FedMPDD so practical advantage is narrow"** — This ignores the massive privacy gap (SSIM 0.91 vs 0.14). The advantage on the joint objective is clear from the evidence. Removed.

- **Strength: "Formal privacy lemmas that link rank-deficiency to a lower bound"** — The verified weakness (L_v(x) unquantified, no formal privacy metric) undermines the practical force of these lemmas. The weakness wins. Removed.

- **Strength: "Explicit treatment of multi-round privacy composition"** — The critic correctly identifies that T × m < d is a practical limitation, not a strength. The weakness wins. Removed.

- **Strength: "Rademacher over Gaussian for lower variance"** — This is a minor implementation detail, not a core strength. Removed.

- **Various formatting/typo nitpicks** — Parser artifacts, not author errors. Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The key observations about single-projection variance scaling and the JL-based multi-projection fix are already articulated in the paper.

## Suggestions

1. **Reformulate the privacy narrative honestly.** Replace "inherent privacy guarantees" and "provable privacy" with language like "empirical resistance to gradient inversion attacks" or "attack-dependent privacy from rank-deficient encoding." The current claims will not withstand scrutiny from privacy researchers.

2. **Quantify or remove Lemma 2's dependence on L_v(x).** Either bound L_v(x) for the models in the experiments, or restructure the lemma as a conditional result ("if L_v(x) ≤ C then...") and discuss what values of C are realistic.

3. **Include joint baselines.** Add compressive DP (Amiri et al. 2021) or LDP+QSGD to the comparison. If FedMPDD genuinely outperforms these on the joint objective, this would be a strong result.

4. **Connect LDP noise to formal ε budgets.** Report what ε values the Laplace noise levels correspond to and calibrate the comparison accordingly.

5. **Surface the T × m < d limitation.** Add a brief discussion in the abstract or conclusion about the practical implications of the multi-round composition bound.

## Score and Decision

**Round 1 — Bracketing:** Searched three bands: low (<3.5), middle (3.5–7.5), high (>7.5). Low anchors (FedComLoc 3.0, compressed decentralized learning 1.67, FedADM 3.0) are much weaker — basic compression integration without theoretical insight. High anchors (7.5+) are not topically similar (DRO, Nash equilibria). Middle-band anchors are the relevant comparison. Initial bracket: **[4.0, 6.5]**.

**Round 2 — Narrowing within bracket:**
- *MAPA* (avg 5.0) — Model-agnostic projection adaptation for FL. Same family of random-projection + seed-sharing technique. Rejected. Our paper has more comprehensive experiments, better convergence theory, and an additional privacy dimension. **Our paper is stronger than MAPA** (~+0.5).
- *SAFL* (avg 4.5) — Sketched adaptive FL with convergence theory. Rejected. Our paper has a more concrete algorithmic contribution. **Our paper is stronger than SAFL** (~+1.0).
- *LASER* (avg 5.83) — Low-rank compression for wireless FL. Rejected (with mixed reviews: 3,8,6,6,6,6). Stronger on large-scale empirical validation (GPT-2) and practical motivation (noisy channels). **Our paper is slightly weaker than LASER** (~-0.3).

**Final calibration:** The paper sits between MAPA (5.0) and LASER (5.83), with stronger theory and empirical coverage than MAPA but with a significant privacy overclaim issue that LASER doesn't have. The privacy overclaim is a central weakness that would prevent acceptance but is fixable through honest reformulation. Score: **5.5**.

**Decision: Reject.** The core compression mechanism has merit and the empirical joint trade-off evidence is compelling, but the paper fundamentally overclaims on privacy. The language of "inherent privacy guarantees," "provable privacy," and the unfair comparison against LDP's formal DP framework using heuristic metrics are significant honesty problems in the paper's central narrative. These issues could be addressed in a major revision that honestly repositions the contribution, adds proper baselines, and connects LDP noise to formal ε budgets.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>