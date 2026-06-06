## Summary

HOMIL (Higher-Order Multi-Instance Learning) extends ABMIL for whole-slide image (WSI) classification by augmenting the standard attention-weighted mean embedding (first-order moment) with a covariance-matrix-based second-order representation and an adaptive DBSCAN clustering step. DBSCAN reduces per-slide patch counts to ~16–18% of the original, lowering runtime while preserving diagnostic regions. The framework is evaluated on CAMELYON16 (399 slides) and TCGA-NSCLC (1050 slides), consistently outperforming nine baselines across ACC, AUC, and F1 while being substantially faster than dynamic MIL methods.

---

## Strengths

- **Consistent, concrete performance gains over ABMIL across both benchmarks.** On CAMELYON16, HOMIL achieves ACC 96.98%, AUC 99.23%, F1 96.54%—improvements of +2.26% ACC and +2.94% F1 over ABMIL (Table 1). On TCGA-NSCLC, it achieves ACC 93.24%, AUC 97.41%, F1 92.93%, improving ABMIL by +2.19% ACC and +2.19% F1 (Table 2). These are non-trivial improvements over a well-tuned strong baseline across two qualitatively different tasks.

- **Solid ablation validates each component.** Table 3 confirms both modules contribute independently: removing the clustering module (CM) degrades ACC from 96.98% to 95.72% and inflates runtime by 71% (310s → 530s); removing the second-order module (SOM) drops ACC to 95.98% and AUC to 98.51%; removing both degrades to ABMIL (ACC 94.72%). The synergy is directly demonstrated.

- **Substantial and well-documented computational efficiency gains.** Compression ratios of 0.18 (CAMELYON16) and 0.16 (TCGA-NSCLC) result in a total 5-fold runtime of 310s and 3685s, respectively—dramatically faster than TransMIL (5175s / 48710s), MambaMIL (7200s / 25200s), and HMIL (10800s / 32400s), while achieving higher accuracy than all of them on both datasets.

- **Standardized evaluation protocol.** All nine baselines share identical patient-level 5-fold splits, 512-dimensional CONCH features, and a unified training recipe, ensuring the performance comparisons are fair.

- **Informative fusion weight dynamics (Figure 2b).** The learned fusion weights converge with $\alpha^{(1)} \approx 0.6$ and $\alpha^{(2)} \approx 0.45$, consistent with the ablation showing both moments contribute meaningfully rather than one collapsing to zero.

---

## Weaknesses

### Fatal
None.

### Major

- **The covariance is mislabeled as "attention-weighted" but the formula is unweighted.** Section 4.3.3 labels Step 2 "Weighted Covariance Matrix," and Section 4.1 describes the second-order stream as computing an "attention-weighted covariance matrix." However, the actual formula is $\mathbf{C} = \sum_{k=1}^K \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$—no attention weights $a_k$ appear in the sum. Attention enters only through the centering mean $\mathbf{v}^{(1)} = \sum_k a_k \mathbf{g}_k$. A true attention-weighted covariance would be $\sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$. Since the paper's theoretical framing in Sections 3.1–3.2 explicitly motivates the covariance as the attention-weighted second-order analog of ABMIL's attention-weighted first-order moment, this inconsistency is substantive, not merely terminological. Crucially, the ablation (Table 3) does not compare the current unweighted formulation against a properly attention-weighted one, leaving the role of attention in the covariance unresolved.

- **Performance margins are modest and no significance test is reported.** On TCGA-NSCLC (Table 2), HOMIL's improvement over the next-best method (HMIL) is only +0.35% ACC and +0.10% F1—well within the reported standard errors (HOMIL SE: 2.47%, HMIL SE: 1.45%). On CAMELYON16 (Table 1), the gains are somewhat larger (+0.50% ACC, +0.85% AUC over MambaMIL) but SEs still overlap substantially. The abstract claims the method "significantly improves the state-of-the-art performance," and Section 5.3 repeats language about "significantly" outperforming baselines; however, no paired significance test (e.g., paired permutation test, Wilcoxon signed-rank) across the five folds is reported. With fold-level results available, this is straightforward to add and essential for the claim as stated.

### Minor

- **The biological interpretation of DBSCAN clustering is asserted, not demonstrated.** The paper argues (Sections 2.2, 4.1, 4.2) that DBSCAN "adaptively adjusts granularity: small clusters for rare pathological regions and large clusters for abundant normal tissues." However, DBSCAN operates on PCA-reduced *feature vectors* (32-dimensional), not spatial coordinates. Whether feature-space density in that low-dimensional space anti-correlates with pathological importance is an empirical assumption. No cluster-assignment visualization overlaid on a WSI is provided. On CAMELYON16, where patch-level annotations exist, enrichment of small clusters with tumor patches would directly test this claim. Without such evidence, the biological narrative supporting DBSCAN over simpler alternatives (k-means, spectral clustering) is unsubstantiated.

- **The covariance vectorization design is ad hoc and unablated.** A 512×512 covariance matrix is compressed to a 512-dimensional vector by row-wise 1D convolution (kernel size $m=64$, $T=4$ kernels) followed by double max-pooling (Section 4.3.3). While each per-row scalar $v_i^{(2)}$ does process the full row—and therefore encodes some off-diagonal information—the design choice of treating covariance rows as 1D signals for max-pooling has no principled motivation, and no ablation compares this to even simple alternatives (e.g., log-diagonal, symmetric rank-$r$ projection, mean-pooling over rows). Given that this compression step determines what second-order information the model actually uses, its arbitrary nature is a gap worth addressing.

### Trivial
None.

---

## Nice-to-Haves

- A visualization of DBSCAN cluster assignments overlaid on representative WSIs (with and without known pathological regions), potentially with a check that small clusters are enriched for tumor patches on CAMELYON16, would directly validate the paper's core narrative for the clustering module.
- Paired significance tests (Wilcoxon or permutation) across the five folds for the key comparisons in Tables 1 and 2 would convert suggestive improvements into statistically supported claims at minimal cost.
- An ablation replacing the unweighted covariance $\sum_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$ with a properly attention-weighted version $\sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$ would resolve the theoretical inconsistency and either strengthen or refine the framing.
- Evaluating on a third dataset (e.g., a different tissue type or cancer type) would strengthen the "robustness" claims made in Section 5.3.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Figure 2(b) suggests the second-order component adds limited marginal value."** The harsh critic interprets the convergence of $\alpha^{(2)} \approx 0.45$ as indicating limited marginal value. However, $\alpha^{(2)}$ remains near 0.45—not near zero—and the ablation in Table 3 independently shows removing SOM drops ACC by ~1% and AUC by ~0.72%. The ablation overrides this speculation.

- **Harsh Critic: "minPts=4 may not be appropriate for both datasets given a 5× difference in patch count."** The adaptive $\epsilon$ (set as the 65th percentile of nearest-neighbor distances per slide) already scales per-slide density, partially compensating for dataset size differences. The sensitivity analysis (cited as in the appendix) further addresses this. The claim requires the appendix content to evaluate, which is stripped. REMOVED per the rule against criticism requiring appendix access.

- **Harsh Critic: "Time comparison is unfair because baselines exclude DBSCAN clustering time."** The paper explicitly states in Section 5.2: "total computational time in seconds (including clustering for HOMIL, or training+inference only for other methods)." This asymmetry favors the baselines, making HOMIL's efficiency advantage a conservative lower bound. Under the hard rule, unfair comparisons that disadvantage the author are removed.

- **Strength Finder: "Statistical grounding that extends ABMIL" as a core strength.** While the probabilistic/moment-based framing is present, the mislabeling of the covariance as "attention-weighted" (a confirmed weakness) means this theoretical framing is imprecise. This strength conflicts with the verified weakness and is downgraded.

---

## Novel Insights

The most actionable insight emerging from the review is the gap between HOMIL's stated theoretical contribution and its implementation: the paper frames second-order statistics as the natural attention-weighted extension of ABMIL's first-order aggregation, but the covariance formula is unweighted in the outer-product sum ($\mathbf{C} = \sum_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$ vs. the theoretically consistent $\sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$). This is not just a labeling issue—it suggests an unexplored design variant that may perform differently and whose comparison would sharpen the theoretical claim. The paper inadvertently leaves open a more principled version of itself.

---

## Suggestions

1. **Rename the covariance or use attention-weighted outer products.** Either relabel Section 4.3.3 Step 2 as "unweighted centered covariance" or switch to $\mathbf{C} = \sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$ and add an ablation comparing both. This resolves the theoretical inconsistency.
2. **Report fold-level significance.** Given 5-fold results, add a paired Wilcoxon test for the key comparisons in Tables 1 and 2. Replace "significantly improves" with hedged language or substantiate it with the test outcome.
3. **Validate the DBSCAN biological claim with one WSI visualization.** Overlay DBSCAN cluster size (small/large) onto a CAMELYON16 slide with known tumor annotation. This takes one figure and directly supports the paper's primary narrative for why DBSCAN was chosen.
4. **Ablate the vectorization.** Compare current row-wise 1D conv+max-pooling against at least one alternative (e.g., log-diagonal of $\mathbf{C}$, mean-pooling across rows) in Table 3 to show the current choice is not trivially arbitrary.

---

## Score and Decision

**Originality:** The second-order moment framing for MIL is natural and has precedents in covariance pooling for visual recognition; the DBSCAN efficiency trick is an engineering contribution. Incremental but concrete. (3/5)

**Importance of research question:** WSI classification at scale is a high-impact medical imaging problem. (4/5)

**Claims well-supported:** Ablation (Table 3) strongly supports both components; overall performance claims supported by consistent improvements, but the "significantly improves SotA" language is unsubstantiated without significance testing, and the attention-weighted label is inaccurate. (3/5)

**Soundness of experiments:** Two datasets, standardized splits, nine baselines, informative ablation. Weakened by missing significance tests and the labeling inconsistency. (3/5)

**Clarity of writing:** Generally well-structured, but the mislabeling in Section 4.3.3 introduces genuine confusion in the core technical section. (3/5)

**Value to research community:** Practically useful: the combination of efficient clustering and second-order statistics is reproducible, demonstrably faster than dynamic MIL baselines, and achieves consistent gains. Engineers in computational pathology would find it useful. (3/5)

The paper is a reasonable incremental contribution to the WSI MIL literature with a solid ablation and genuine efficiency advantages. However, the theoretical framing's central inconsistency (claiming attention-weighted covariance but not implementing it), combined with absent significance testing for modest performance margins, prevents acceptance at current form. These are addressable with targeted revisions rather than a major overhaul, making this a borderline weak reject — the ideas merit publication after correction.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>