## Summary

This paper investigates whether the well-known counterintuitive likelihood phenomenon in image anomaly detection (generative models assigning higher likelihoods to OOD data) manifests in tabular anomaly detection. The authors propose a domain-agnostic definition (Definition 3.3) with two threshold parameters (β, γ), benchmark NF-SLT across all 47 tabular and 10 CV/NLP embedding datasets in ADBench against 12 baselines, and find the phenomenon is rare in tabular settings (Fail Ratio 0.02). They attribute this rarity to lower dimensionality (Theorem 5.4/Corollary 5.6) and weaker feature correlation (d Ratio, Table 4).

---

## Rebuttal Assessment

**Weakness: β and γ not stated in main text**
- **Author's response:** Partially address — argues that CIFAR-10/SVHN example (AUROC 6.4%) and 'yeast' minimum gap (0.02) jointly bound the effective range of γ; commits to moving values to main text in revision.
- **Assessment:** Partially convincing. The paper (Section 3) does confirm: "The fully rigorous formulation of Definition 3.3 is provided in Appendix B" — exact values are absent from the main text. The two anchoring examples are indeed in Section 3 and 4, and a reader can infer the order of magnitude of γ. However, the rebuttal's claim that "a reader can infer γ is calibrated against non-trivial gaps of order at least several percentage points" is rationalization — the exact β value (the fraction threshold in Eq. 2) is not bounded at all by these examples. The promise to move values to main text counts for nothing as a submitted paper.
- **Score impact:** Weakness downgraded (major → minor), but not removed. The examples provide partial grounding; both thresholds remain implicit.

---

**Weakness: Theorem 5.4 assumes independence but is applied to correlated tabular data**
- **Author's response:** Partially address — argues the paper presents a two-factor account (Section 5.1 for dimensionality under independence; Section 5.2 for the correlated regime empirically via d Ratio), and that the paper explicitly acknowledges genomics exceptions.
- **Assessment:** Partially convincing. Verified in the paper: Section 5.1 and 5.2 are genuinely separate arguments, not the same claim applied twice. Section 1 does state the acknowledgment about genomics. Section 5.2 indeed provides a distinct empirical account that does not invoke Theorem 5.4. The reviewer somewhat overstated the issue by treating the two sections as if the theorem were being misapplied to correlated data — the theorem is applied only to image experiments (Table 2), while the tabular correlated case is handled by d Ratio. However, the paper never explicitly states "Theorem 5.4 applies under independence; Section 5.2 handles the correlated case," leaving the boundary between the two explanatory threads unclear. The promise to add a clarifying sentence is a future fix.
- **Score impact:** Weakness downgraded (major → minor). The two-factor structure is real and present in the paper.

---

**Weakness: Entropy condition H(P) > H(Q) not empirically verified for tabular datasets**
- **Author's response:** Partially address — argues that even if the entropy condition were satisfied in tabular data, low dimensionality provides protection, and Table 1's Fail Ratio = 0.02 is consistent with this. Commits to adding entropy estimates in revision.
- **Assessment:** Partially convincing. The theoretical argument that low dimensionality provides protection regardless of the entropy condition is logically coherent given Corollary 5.6. However, it is not verified empirically in the paper. The key question — whether tabular anomaly tasks predominantly satisfy H(P) < H(Q) (making dimensionality irrelevant) or H(P) > H(Q) (making dimensionality the protective factor) — remains unanswered in the submitted paper. The promise to add this in revision is not present evidence.
- **Score impact:** Weakness unchanged (minor remains).

---

**Weakness: Table 2 mixed support — CIFAR-10/SVHN does not improve with ICA**
- **Author's response:** Partially address — points to Table 3 (bilinear resize with Glow), where CIFAR-10/SVHN AUROC rises from 0.0716 (32×32) to 0.4512 (8×8), as evidence already in the paper.
- **Assessment:** Convincing for the Table 3 defense. Verified directly: Table 3 (lines 168-174) shows CIFAR-10/SVHN monotonically improving with dimension reduction under the Glow/bilinear-resize setup. Section 5.1 (lines 164-176) explicitly discusses this table as providing supplementary evidence when independence is not guaranteed. The original review underweighted Table 3 by focusing only on Table 2. The reviewer was right that 2/3 ICA cases confirm Corollary 5.6, but Table 3 closes the CIFAR-10/SVHN gap with a different methodology.
- **Score impact:** Weakness downgraded (minor → trivial). Table 3 already provides the CIFAR-10/SVHN confirmation. The original review missed this.

---

**Weakness: Minimum in Equation 3 not well-motivated**
- **Author's response:** Partially address — argues minimum is a conservative criterion (if even the closest competitor exceeds γ, underperformance is uniformly substantial, not driven by outliers), consistent with Assumption 3.2's intent as a necessary condition. Commits to adding justification and robustness check in revision.
- **Assessment:** Partially convincing. The conservative interpretation rationale is logical and consistent with Assumption 3.2 as written (lines 65-67), but this rationale does not appear in the paper. The asymmetry issue noted by the reviewer — minimum makes both presence (easy if one outlier) and exculpatory tests (easy if minimum is small) easy — is not fully addressed. The promise to add a robustness check is a future fix.
- **Score impact:** Weakness unchanged (minor remains). The rationale is reasonable but absent from the submitted paper.

---

## Strengths

1. **Comprehensive benchmark across all 47 tabular and 10 CV/NLP embedding datasets in ADBench**: NF-SLT achieves Avg. Rank 3.43, Fail Ratio 0.02, Top2 Ratio 0.45 in Table 1, with explicit motivation for using all datasets (Shwartz-Ziv & Armon, 2022 anti-selection-bias argument). This is the paper's most robust finding.

2. **Genuine two-factor theoretical–empirical account**: Section 5.1 (dimensionality, independence regime) and Section 5.2 (d Ratio, correlated regime) are genuinely complementary arguments. The d Ratio links intrinsic to ambient dimension quantitatively: image d Ratio ≈ 0.002–0.019 vs. tabular ≈ 0.39–0.81 (Table 4), confirmed by synthetic experiments in Figure 1 and within-tabular bucketed thresholds in Table 4 (bottom).

3. **Table 3 CIFAR-10/SVHN confirmation via resize**: Although the ICA experiment does not confirm Corollary 5.6 for CIFAR-10/SVHN (Table 2), Table 3 shows AUROC rising monotonically from 0.0716 (32×32) to 0.4512 (8×8) for the same pair using bilinear resize, providing 3/3 confirmation across methodologies.

4. **CV/NLP embedding consistency**: Table 1 (bottom) shows NF-SLT best or near-best on 9/10 embedding datasets, and the one underperforming case (imdb, gap 0.0385) is explicitly shown to not satisfy Definition 3.3 Eq. 3. The d Ratio explanation (embedding d Ratio ≈ 18–23/1000 >> raw pixel d Ratio) is coherent.

---

## Weaknesses

### Fatal
None.

### Major
None. (Original major weaknesses both downgraded given the rebuttal partially addressed them.)

### Minor

- **β and γ absent from main text**: Exact threshold values remain in Appendix B. While the CIFAR-10/SVHN and 'yeast' examples bound γ's order of magnitude, β (the fraction threshold in Eq. 2) is not bounded by either example. The "rarity" conclusion cannot be independently assessed without these values.

- **Theorem 5.4 scope not explicitly stated**: The independence boundary between Theorem 5.4 and Section 5.2 is implicit but not stated. A reader could misread the theorem as the universal theoretical account, conflating the independence-based dimensionality argument with the correlated tabular evidence.

- **H(P) > H(Q) unverified for tabular datasets**: The entropy condition that triggers likelihood inversion is never checked for the 47 tabular datasets. The rebuttal's theoretical argument (low dimensionality protects even when condition holds) is coherent but untested in the submitted paper.

- **Minimum gap choice unjustified in paper**: The rationale (conservative necessary-condition criterion) is reasonable and consistent with Assumption 3.2, but absent from the submitted text.

### Trivial

- **CIFAR-10/SVHN non-improvement in Table 2**: This is largely resolved by Table 3, which already provides confirmation for CIFAR-10/SVHN via a different methodology. The paper could discuss the connection between Table 2 and Table 3 more explicitly.

---

## Nice-to-Haves

- Move β and γ to Section 3 with a one-paragraph sensitivity analysis.
- Explicitly delineate the independence assumption boundary between Section 5.1 (Theorem 5.4) and Section 5.2 (d Ratio) with a bridging sentence.
- Add k-NN entropy estimates for a representative subset of tabular datasets to verify or characterize the H(P) vs. H(Q) regime.
- Extend d Ratio computation to all 47 tabular datasets and include a scatter plot of NF-SLT AUROC vs. d Ratio.
- Add one sentence connecting Table 2 (ICA experiment) to Table 3 (resize experiment) to fully close the CIFAR-10/SVHN discussion.

---

## Novel Insights

The most analytically novel contribution is the d Ratio framework for linking feature correlation to likelihood-based anomaly detection performance within and across domains. By defining d Ratio as intrinsic/ambient dimension and validating its monotone relationship with correlation strength (Figure 1, synthetic Gaussian experiments), the paper provides a domain-agnostic scalar measure that explains not only the image/tabular dichotomy but also within-tabular heterogeneity: datasets with d Ratio < 0.5 disproportionately account for NF-SLT underperformance (Table 4, bottom). This re-frames the "image anomaly detection problem" as a general correlation-indexed problem, suggesting that high-correlation tabular data (e.g., genomics) may be susceptible to the same phenomenon as images.

---

## Suggestions

1. State β and γ explicitly in Section 3 alongside the CIFAR-10/SVHN and 'yeast' anchoring examples, with a brief sensitivity check (±20% threshold variation).
2. Add a sentence in Section 5.1 stating explicitly: "Theorem 5.4 and Corollary 5.6 characterize behavior under the independence assumption; the correlated tabular regime is handled empirically by Section 5.2."
3. Add a sentence connecting Table 2 and Table 3: "While the ICA-based experiment (Table 2) does not confirm Corollary 5.6 for CIFAR-10/SVHN due to residual pixel correlations in retained components, the bilinear-resize experiment (Table 3) confirms the monotone AUROC improvement for this pair."
4. Compute d Ratio for all 47 tabular datasets and add a scatter plot of NF-SLT AUROC vs. d Ratio.
5. Include approximate k-NN entropy estimates for a representative subset of tabular datasets to ground the H(P)/H(Q) discussion.

---

## Score and Decision

**Rebuttal impact summary:**

| Weakness | Original Severity | Impact |
|---|---|---|
| β/γ missing from main text | Major | Downgraded to Minor (anchors partially bound γ, but β still unconstrained) |
| Independence gap in Theorem 5.4 | Major | Downgraded to Minor (two-factor structure is genuine and present in paper) |
| Entropy condition unverified | Minor | Unchanged |
| Table 2 mixed support | Minor | Downgraded to Trivial (Table 3 already in paper provides CIFAR-10/SVHN confirmation) |
| Minimum gap unjustified | Minor | Unchanged (reasonable rationale, but absent from paper) |

The rebuttal's most impactful contribution is correctly identifying that Table 3 already provides the CIFAR-10/SVHN evidence the reviewer sought — this was a genuine misread by the reviewer. The two-factor account (Section 5.1 + 5.2) is also a genuine structural feature of the paper, not a post-hoc rationalization. These improvements justify a small upward revision.

However, the two remaining minor weaknesses (β/γ absent; independence boundary unstated) are material transparency issues that a reader encountering the paper would need to track to Appendix B. The entropy condition remains unverified in the submitted paper. These prevent a strong accept.

Compared to calibration anchors: the paper now appears closer to the accepted papers in the 5.75–6.33 range (`CJnceDksRd`, `falBlwUsIH`) than to the rejected 5.67 papers, but still lacks a novel method and has three unresolved minor weaknesses. A modest upward revision from 5.5 to 6.0 is warranted.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>