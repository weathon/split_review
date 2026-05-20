## Summary

This paper proposes HOMIL (Higher-Order Multi-Instance Learning), a framework for WSI classification that augments attention-based MIL with second-order statistics. The key ideas are: (1) using DBSCAN to cluster patches into groups, reducing the effective bag size, (2) computing both a first-order (attention-weighted mean) and second-order (covariance matrix) representation from cluster-level features, and (3) fusing them via learned attention weights. Experiments on CAMELYON16 and TCGA-NSCLC show HOMIL achieving the best accuracy, AUC, and F1 among 10 methods, with substantially lower runtime than comparable approaches.

## Strengths

1. **Principled statistical reframing of MIL aggregation.** The paper explicitly formalizes ABMIL as estimating the first-order moment of patch representations (Section 3.1) and motivates higher-order moments to capture variability beyond the mean (Section 3.2). This is a clean conceptual lens that differentiates the work from heuristic-driven MIL extensions.

2. **Competitive results and major computational efficiency gains.** On CAMELYON16, HOMIL achieves 96.98% ACC with 310s total runtime across 5 folds, compared to ABMIL at 94.72%/455s and MambaMIL at 96.48%/7200s (Tables 1–2). On TCGA-NSCLC, the runtime advantage over HMIL (3,685s vs. 32,400s) and MambaMIL (3,685s vs. 25,200s) is dramatic while still achieving top metrics. These results suggest clustering-based compression can reduce computation without sacrificing accuracy.

3. **Ablation study validating both components.** Table 3 decomposes the contribution of clustering (w/o CM: −1.26% ACC, +71% time) and second-order moment (w/o SOM: −1.00% ACC) on CAMELYON16, showing both contribute positively and synergistically. This provides clean empirical evidence for the design choices.

4. **Shared feature extractor and consistent evaluation protocol.** All methods use CONCH features and 5-fold patient-level cross-validation with the same splits, ensuring fair comparison. This is a methodological strength that many WSI papers lack.

## Weaknesses

### Fatal

None.

### Major

1. **Misalignment between theoretical framing and actual method (Section 3.2 vs. Section 4.3.3).** The abstract states "we compute the covariance matrix of the patch representation vectors across the entire slide," and Section 3.2 derives Σ = Σᵢ (hᵢ − μ)(hᵢ − μ)ᵀ explicitly over *patches*. However, the method (Section 4.3.3) computes C = Σₖ (gₖ − v⁽¹⁾)(gₖ − v⁽¹⁾)ᵀ over *clusters* — a different quantity that discards intra-cluster variance through mean-pooling. The introduction does briefly note that "both moments are computed based on cluster representations," but the abstract and the entire theoretical motivation section create a misleading impression that patch-level covariance is being computed. The paper never acknowledges this discrepancy nor justifies why cluster-level covariance is a suitable proxy for patch-level covariance. This is a significant presentation problem that undermines reader trust in the paper's core narrative.

2. **Adaptive granularity claim is asserted without direct evidence.** The paper repeatedly claims DBSCAN "forms large clusters for abundant normal tissues and small clusters for rare pathological regions" (Sections 1, 4.1, 4.2) and that this "enables variable-resolution processing that preserves diagnostic information." This is presented as a central contribution, yet the paper provides zero direct evidence: no cluster size distributions, no visualization of cluster composition, no verification that pathological regions indeed form smaller clusters, and no annotation-overlay analysis. Only the overall compression ratios (0.18, 0.16) are given, which say nothing about whether clustering is "adaptive" in a diagnostically meaningful sense. The ablation study (w/o CM) shows clustering helps, but this could reflect noise reduction or computational regularization rather than adaptive granularity specifically.

3. **No statistical significance testing.** Performance differences between HOMIL and the closest competitor HMIL are within one standard error on both datasets (CAMELYON16: 96.98±2.43 vs. 96.19±4.18; TCGA-NSCLC: 93.24±2.47 vs. 92.89±1.45). With only 5 folds, the reported improvements — especially over HMIL, which also uses higher-order statistics — cannot be assessed as reliable without a paired significance test. Given that the paper claims "significantly improves the state-of-the-art," the absence of even a basic paired t-test is a notable gap.

### Minor

4. **Insufficient discussion of the most directly related competitor (HMIL).** HMIL (Jin et al., 2025) also incorporates higher-order statistics into MIL and is the most relevant baseline. Yet it receives no discussion in the Related Work section and no analysis of how HOMIL's approach differs (e.g., cluster-level vs. patch-level covariance, DBSCAN vs. other grouping). Given that the ACC gap between HOMIL and HMIL is the smallest among top methods, this omission prevents readers from understanding whether HOMIL is a genuine advance or an incremental variation.

5. **The "attention-weighted covariance" label is imprecise.** Section 4.3.3 calls C = Σₖ (gₖ − v⁽¹⁾)(gₖ − v⁽¹⁾)ᵀ an "attention-weighted covariance matrix." While the centering term v⁽¹⁾ = Σ aₖ gₖ is attention-weighted, the outer-product sum assigns equal weight to each cluster regardless of its attention score aₖ. This design choice is not acknowledged, justified, or compared to an alternative where attention weights modulate the outer products (aₖ · (gₖ−μ)(gₖ−μ)ᵀ). This is a relatively minor imprecision in terminology but indicates a gap in methodological reflection.

6. **Key hyperparameters set without justification.** PCA dimension d′=32, 1D-convolution kernel size m=64, and T=4 kernels are specified in Section 5.2 with no rationale or sensitivity analysis in the main paper. The sensitivity analysis is referenced to the appendix (which is not evaluable). Given that PCA reduction from 512→32 could discard diagnostically relevant variation needed for clustering, the lack of ablation on this choice is a gap.

### Trivial

7. The time column definition ("including clustering for HOMIL, or training+inference only for other methods") is clear but could be phrased more straightforwardly: total pipeline time for HOMIL vs. total pipeline time for other methods.

## Nice-to-Haves

- Show cluster size distributions and overlay cluster assignments on WSI patches to visually validate the "adaptive granularity" claim.
- Report a paired t-test comparing HOMIL vs. ABMIL and HOMIL vs. HMIL across the 5 folds.
- Extend the ablation study (Table 3) to TCGA-NSCLC to confirm the CAMELYON16 findings generalize.
- Add a comparison to an attention-weighted covariance variant (aₖ · (gₖ−μ)(gₖ−μ)ᵀ) to justify the uniform-weight design choice.

## Removed Points

- "The second-order representation is not actually attention-weighted" — kept as Minor (point 5) but demoted from the critic's stronger framing. The criticism is factually correct (equal-weight outer product) but the term "attention-weighted covariance" is standard usage when the *centering* is attention-weighted; this is a terminology imprecision, not a methodological flaw.
- "PCA dimension d'=32 could discard diagnostically relevant variation" — kept as Minor (point 6) but noted as a gap, not a demonstrated flaw.
- Points about missing appendix content — removed per instructions (parser strips appendices from all papers).
- Pure formatting/style nitpicks from the Section-by-Section notes — removed as parser artifacts or non-substantive.
- The critic's claim that "the paper never acknowledges this discrepancy" (between patch-level and cluster-level) — the paper *does* acknowledge it in the introduction ("Both moments are computed based on cluster representations rather than individual patches"). However, the abstract and Section 3.2 remain misleading, which is the real issue (kept as Major weakness 1 with corrected framing).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Align the abstract and Section 3.2 with the actual method.** Replace "patch representation vectors" with "cluster-level feature representations" throughout, or explicitly state: "As a computationally tractable proxy for patch-level covariance, we first group similar patches via DBSCAN, then compute the covariance of cluster-mean features." This single change would resolve the most distracting issue in the paper.

2. **Validate the adaptive clustering claim directly.** Show 3–4 representative slides with: (a) cluster size histograms, (b) spatial overlay of clusters colored by size, and (c) at least one example where small clusters correspond to annotated tumor regions (even if only qualitatively). Without this, the "adaptive granularity" narrative remains an untested hypothesis.

3. **Report statistical significance.** A paired t-test (5 folds × 2 classes) comparing HOMIL to ABMIL and HMIL is straightforward and would substantially strengthen the paper's claims.

4. **Move hyperparameter sensitivity to the main paper.** Show that results are stable across a range of d′, m, and T values. The current dependence on an unreviewable appendix weakens the empirical contribution.

5. **Discuss HMIL in the Related Work section.** Explain what HMIL does, how it computes higher-order statistics, and specifically how HOMIL differs. This is necessary for readers to evaluate whether the paper represents a conceptual advance.

## Score and Decision

**Bracketing:** Round 1 identified weak anchors at 2.0–3.33 (rejected/withdrawn WSI-MIL papers), middle anchors at 4.0–6.5, and no relevant strong (>7.5) anchors. The paper was initially bracketed between 4.0 and 6.5.

**Narrowing:** Round 2 retrieved additional anchors. Key comparisons:
- **MMPL (avg 4.0, Reject):** Had anomalous results and unsubstantiated efficiency claims. HOMIL has cleaner, more consistent results and a stronger conceptual motivation — clearly above this anchor.
- **ASMIL (avg 6.0, Poster):** Cleaner problem formulation, no theory-method mismatch, experiments on 3 WSI + 5 non-WSI datasets. HOMIL is weaker in both presentation clarity and experimental breadth.
- **MAMMOTH (avg 6.5, Poster):** 8 MIL methods × 19 tasks with thorough ablations. HOMIL is considerably less comprehensive.
- **CLS-Tuned Attention (avg 2.5, Withdrawn):** Poor presentation, overclaims, limited novelty. HOMIL is clearly stronger.

HOMIL sits above the reject-tier anchors (4.0) but below the accept-tier anchors (6.0+). The paper has a genuine contribution and competitive results, but the presentation issues (theory-method mismatch, unvalidated adaptive clustering claim, no significance testing) prevent it from meeting the acceptance bar.

**Final Score:** 5.0 — Marginally below the acceptance threshold. The core idea is sound and the empirical results are promising, but the paper overstates its contributions relative to what is actually validated. A substantially revised version addressing the major weaknesses could be considered for acceptance at a future venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>