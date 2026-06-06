## Summary

HOMIL proposes a higher-order MIL framework for WSI classification extending ABMIL with: (1) adaptive DBSCAN-based patch clustering into compact cluster representations, and (2) a second-order representation from a covariance matrix of cluster features, compressed via row-wise 1D convolution and double max-pooling. Results on CAMELYON16 and TCGA-NSCLC demonstrate consistent improvements over ABMIL and competitive or lower runtime than more complex dynamic baselines.

---

## Rebuttal Assessment

### Weakness: "Attention-weighted covariance" claim inconsistent with the actual formula
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author's technical clarification has genuine merit: attention weights *do* enter the covariance computation through the centering step ($\tilde{\mathbf{g}}_k = \mathbf{g}_k - \mathbf{v}^{(1)}$ where $\mathbf{v}^{(1)}$ is attention-weighted). This is verified in Section 4.3.3. The additional argument — that uniform outer-product weighting intentionally preserves variance from low-attention pathological clusters — is a reasonable post-hoc justification, but it is **not present in the paper itself**. The paper's Section 4.1 continues to describe the second-order stream as computing "an attention-weighted covariance matrix," which is demonstrably inaccurate given the formula $\mathbf{C} = \sum_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$. All revisions are promised for camera-ready, not reflected in the current paper. The theoretical motivation in Sections 3.1–3.2 still overstates the attention-weighting of the covariance term.
- **Score impact:** Weakness downgraded (from major to minor-major borderline) — the centering argument is partially valid but post-hoc and not in the paper.

---

### Weakness: Covariance vectorization discards most off-diagonal structure
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes that learned 1D convolution kernels can adaptively identify informative covariance patterns, and the ablation in Table 3 confirms SOM contributes (+1.0% ACC, +0.72% AUC). Verified in paper. However, the ablation shows only that *some* covariance information is useful; it does not demonstrate the current row-wise max-pooling compression is adequate relative to alternatives (diagonal extraction, log-Euclidean, low-rank projection). The design remains ad hoc with $m=64$, $T=4$ unjustified. All comparison ablations are promised for revision.
- **Score impact:** Weakness unchanged — empirical value confirmed but compression adequacy undemonstrated.

---

### Weakness: No statistical significance testing despite modest margins over nearest competitor
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author usefully distinguishes two regimes: (1) HOMIL vs. ABMIL, where 2.26% ACC gap on CAMELYON16 and 2.19% on TCGA-NSCLC both exceed the ABMIL SE (2.18% and 2.05% respectively) and are consistent across all 6 metric-dataset combinations. This is a reasonable argument for practical significance, verified in Tables 1-2. (2) HOMIL vs. HMIL on TCGA-NSCLC (+0.35% ACC, within noise), where the author appropriately concedes. However, the paper's abstract still reads "significantly improves the state-of-the-art performance" — verified at line 9. The abstract language is unchanged; the revision is promised. The CAMELYON16 comparison to MambaMIL (+0.50% ACC, HOMIL SE = 2.43%) is also still within overlapping noise.
- **Score impact:** Weakness downgraded for ABMIL comparison only; "state-of-the-art" language weakness unchanged in the paper.

---

### Weakness: DBSCAN "pathological region → small cluster" claim is asserted but unvalidated
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as resolution — Author honestly acknowledges the limitation. Section 4.2 asserts: "pathological patches—rare but diagnostically crucial—form small clusters or remain as outliers." This is stated again in the paper without empirical validation. No visualization, no enrichment analysis on CAMELYON16 patch-level annotations. All validation is promised for revision. Weakness stands in the current paper.
- **Score impact:** Weakness unchanged.

---

### Weakness: Ablation conducted only on CAMELYON16
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as resolution — Author acknowledges and promises TCGA-NSCLC ablation in revision. Verified: Section 5.4 explicitly states the ablation is on CAMELYON16 only, and Table 3 confirms. Component contributions on the larger, more clinically complex dataset are unknown.
- **Score impact:** Weakness unchanged.

---

### Weakness: Time comparison is asymmetric and should be more prominently flagged
- **Author's response:** Refute
- **Assessment:** Convincing — Author correctly notes the disclosure appears explicitly in Section 5.2 and in Table 1/2 captions (verified at line 240: "total computational time across 5 folds (seconds) (including clustering for HOMIL, or training+inference only for other methods)"). Even under this inclusive accounting, HOMIL outperforms nearly all baselines on time. This was already flagged for removal in the original review; the author's refutation is sound.
- **Score impact:** Not a weakness.

---

## Strengths
- **Consistent, multi-metric gains over ABMIL**: Verified in Tables 1 and 2 — ACC +2.26%/+2.19%, F1 +2.94%/+2.19% on both datasets, with margins exceeding ABMIL's own SE on each dataset. Convergent across all 6 metric-dataset combinations.
- **Ablation validates both CM and SOM independently**: Table 3 confirms CM removes 71% runtime overhead and CM+SOM together outperform ABMIL, ABMIL+CM (w/o SOM), and ABMIL+SOM (w/o CM).
- **Genuine runtime efficiency under fair accounting**: Even including DBSCAN clustering time, HOMIL at 310s (CAMELYON16) and 3685s (TCGA-NSCLC) outperforms or matches all attention-based baselines while achieving top performance.
- **Principled statistical framing**: Section 3.1–3.2 cleanly motivates second-order statistics, and Figure 2(b) shows non-trivial convergence of both fusion weights ($\alpha^{(1)} \approx 0.6$, $\alpha^{(2)} \approx 0.45$), consistent with complementary contributions.

---

## Weaknesses

### Fatal
None.

### Major

- **Theoretical framing overstates attention weighting in covariance**: Section 4.1 describes an "attention-weighted covariance matrix" but the formula is $\mathbf{C} = \sum_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$ with no attention weights on outer products. The centering-through-attention-mean defense is partially valid but post-hoc and not in the paper. The ablation does not compare weighted vs. unweighted outer products. The claim that attention shapes the covariance is indirect and overstated throughout the paper.

- **No statistical significance testing for state-of-the-art comparisons**: The abstract says "significantly improves the state-of-the-art" (line 9). On TCGA-NSCLC, HOMIL's margin over HMIL is +0.35% ACC (HOMIL SE = 2.47%). On CAMELYON16, margin over MambaMIL is +0.50% ACC (SE = 2.43%). Neither is statistically distinguishable. The ABMIL comparison is more credible (margins exceed SEs) but no formal test is reported.

### Minor

- **Covariance vectorization is ad hoc without principled justification or alternatives**: Row-wise 1D convolution + double max-pooling reduces each covariance row to one scalar. No ablation against diagonal extraction, low-rank projection, or log-Euclidean alternatives. The paper provides no explanation for the choice of $m=64$, $T=4$.

- **DBSCAN interpretive claim unvalidated**: The assertion that pathological patches form small clusters in feature space (Section 4.2) has no empirical backing. Patch-level annotations exist on CAMELYON16 to test this directly but are not used.

- **Ablation restricted to CAMELYON16**: Table 3 ablates only on the smaller dataset (399 slides, binary task). CM and SOM contributions on TCGA-NSCLC (1050 slides, subtyping) are unknown.

### Trivial

- **Promised revisions not in paper**: Five significant improvements are promised for camera-ready (terminology fix, significance tests, TCGA-NSCLC ablation, vectorization comparison, DBSCAN visualization) but are not present in the reviewed paper and cannot be credited.

---

## Nice-to-Haves
- Implementing and ablating true attention-weighted outer products ($\mathbf{C} = \sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$) would resolve the theory–implementation tension
- Adding a third dataset (e.g., TCGA-RCC or survival prediction) would strengthen robustness claims
- WSI visualization overlaying DBSCAN cluster size against known metastasis regions would validate the paper's biological narrative

---

## Novel Insights

The paper's central observation — computing covariance centered at the attention-weighted mean provides complementary information to ABMIL's mean aggregation — is sound in principle and empirically supported by the ablation. The more interesting finding is the convergence behavior in Figure 2(b): fusion weights do not collapse ($\alpha^{(1)} \approx 0.6$, $\alpha^{(2)} \approx 0.45$), suggesting genuine complementarity rather than redundancy. The efficiency insight is also noteworthy: performing DBSCAN compression *before* covariance computation (rather than after) achieves a 0.16–0.18 compression ratio, making the otherwise intractable $O(K^2 d^2)$ covariance computation practical.

---

## Suggestions

1. **Run fold-level Wilcoxon signed-rank tests** for HOMIL vs. ABMIL and HOMIL vs. best competitor per dataset; replace "significantly improves the state-of-the-art" with quantitative claims.
2. **Implement and ablate true attention-weighted covariance** ($\mathbf{C} = \sum_k a_k \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$) — if performance is similar to the unweighted version, the paper can honestly argue that uniform weighting is the better design choice for preserving rare-cluster variance.
3. **Add TCGA-NSCLC ablation** (CM and SOM) to Table 3.
4. **Validate DBSCAN semantics**: overlay cluster sizes on CAMELYON16 slides and compute enrichment of small clusters in metastasis-annotated regions.
5. **Compare vectorization alternatives**: diagonal only, log-diagonal, low-rank projection — verify the current row-wise 1D conv + max-pool is necessary.

---

## Score and Decision

**Rebuttal impact summary:**

The rebuttal makes two partially valid points that were not fully appreciated in the original review: (1) attention weights *do* influence the covariance through the centering step, partially mitigating the formula inconsistency weakness; (2) the HOMIL vs. ABMIL gap is consistent across 6 metric-dataset combinations and exceeds ABMIL's SE, providing reasonable (if informal) convergent evidence. The time-asymmetry critique was already not a genuine weakness.

However, the rebuttal does not produce new paper evidence — all substantive improvements are promised for revision. The three remaining major weaknesses (terminological/theoretical imprecision, no significance tests, ad hoc vectorization) and two minor weaknesses (DBSCAN validation, ablation scope) are unresolved in the paper as submitted. The rebuttal partially downgraded two major weaknesses to minor-major status but did not resolve them.

The score moves from 5.0 to 5.0 — the partial mitigation of the formula inconsistency weakness and the reasonable argument about ABMIL margins are counterbalanced by the fact that the paper itself has not changed. The paper remains a solid engineering contribution with genuine empirical value but insufficient theoretical rigor and missing ablations for a strong ICLR acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>