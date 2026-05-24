Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper presents PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). It introduces three components: Balanced Prototype Assignment (BPA) via optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) via GRU-based inference-time updates to capture unseen normal variations, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange between RGB and surface-normal modalities. The method is evaluated on MVTec 3D-AD, Eyecandies, and Real-IAD D3, showing strong few-shot performance and computational efficiency.

## Strengths

- **Clear motivation and well-designed framework.** The paper correctly identifies why existing MAD methods (cross-modal alignment and memory-bank approaches) fail under extreme data scarcity, and the three-component design (BPA, APR, MNC) is logically motivated to address specific failure modes. The use of balanced optimal transport for prototype assignment is technically sound.

- **Strong empirical gains across multiple benchmarks.** PIRN achieves consistent improvements over strong baselines under 5-, 10-, and 50-shot settings on both MVTec 3D-AD and Eyecandies (e.g., +3.9 AUROC_I at 5-shot on MVTec 3D-AD, +4.0 at 10-shot on Eyecandies). These gains hold across all three evaluation metrics (AUROC_I, AUROC_P, AUPRO).

- **Single-modality vs. multi-modality ablation (Table 3) cleanly validates MNC.** The 4–5 point AUROC_I improvement from RGB+SN over the best single modality in 5-shot and 10-shot settings directly demonstrates that MNC's cross-modal communication is effective in data-scarce regimes. This is the strongest individual piece of evidence for any single component.

- **Computational efficiency is a genuine advantage.** PIRN achieves the best AUROC_I (0.922) at 10-shot with 85% fewer FLOPs and 4.35× faster inference than FIND, showing that the performance gains do not come at the cost of impractical runtime.

- **Hyperparameter ablation studies (Tables 5, 6, 7) systematically explore design choices.** The ablations on prototype count K, decoder depth L, and aggregation strategy provide practical guidance and confirm the selected configurations.

## Weaknesses

### Major

- **Table 2 contains a contradiction that undermines the ablation validation of BPA.** The paper claims "Removing each component from the full model results in a consistent performance drop." However, row 4 (APR + MNC without BPA) achieves **AUROC_I = 0.967** and **AUROC_P = 0.998**, both *higher* than the full model's 0.922 and 0.991. Only AUPRO favors the full model (0.966 vs. 0.947). Furthermore, the 0.967 AUROC_I value is suspiciously high — it exceeds even PIRN's *all-shot* performance (0.963) and is 45 points above the best 10-shot baseline (0.885). This suggests either a data error (typo, column misalignment) or that BPA *harms* detection when combined with APR+MNC, directly contradicting the paper's stated claims. This must be resolved before the results can be taken at face value.

- **No variance or statistical significance reporting.** The few-shot settings (5, 10, 50 samples) involve very small training sets where results can vary substantially across random draws, yet the paper reports only single-run numbers with no standard deviations or confidence intervals. Without this, it is impossible to assess whether the reported 2–4 point AUROC_I gains are robust or within sampling noise. This is standard practice expected in few-shot evaluation papers.

### Minor

- **FIND baseline is excluded from the main accuracy comparison (Table 1).** The paper compares with FIND (Li et al., 2025) only in the computational efficiency table (Table 4), where FIND achieves 0.921 AUROC_I on 10-shot — essentially tied with PIRN's 0.922. While the efficiency comparison is informative, excluding FIND from the primary few-shot accuracy benchmark weakens the claim of "superior performance." The paper should either include FIND in Table 1 or explain why it is not a directly comparable baseline.

- **"BFA" typo in Table 2 column header.** The first column is labeled "BFA" rather than "BPA". This does not affect the substance but suggests careless presentation.

### Trivial

None.

## Nice-to-Haves

- An analysis of APR's sensitivity to anomalous inputs during inference refinement. The paper argues that OT assignment suppresses anomalous contributions, but the balanced marginal constraint guarantees every prototype receives some mass from every patch. A synthetic experiment or case study demonstrating that prototypes are not corrupted by anomalies during update would strengthen the paper.

- A dedicated limitations section. The method updates prototypes at test-time using potentially anomalous data, which is a non-trivial design choice that deserves discussion of failure modes.

## Removed Points

- **Criticism that FIND "is omitted" entirely from the paper.** REMOVED — the paper does cite and compare with FIND in Table 4 (computational efficiency). The criticism is about its absence from the main accuracy table, which I have retained as a minor weakness above. The harsher framing ("omitted") is inaccurate.
- **Strength Finder's generic claims** (e.g., "addressed an important problem", "comprehensive ablation studies") — REMOVED these where they are superficial or already covered by more specific strengths.
- **Criticism about missing related works comparison with HVQ-Trans.** REMOVED — the paper discusses HVQ-Trans in the related work section. Empirical comparison is a nice-to-have, not a required weakness.
- **"Overclaims given unresolved ablation issue."** REMOVED as speculative framing.

## Novel Insights

None beyond the paper's own contributions. The core observation — that OT-based balanced prototype assignment and inference-time refinement can improve few-shot MAD — is well articulated by the authors.

## Suggestions

1. **Resolve Table 2.** Clarify whether the 0.967/0.998 values for row 4 are correct. If they are a typo, correct them. If they are correct, explain why APR+MNC without BPA achieves higher AUROC_I/P than the full model, and whether this indicates BPA is harmful in certain configurations.
2. **Report means and standard deviations** over at least 3 random seeds for all few-shot settings, using different random draws of the training subset.
3. **Include FIND in the main few-shot accuracy table** or provide a clear justification for its exclusion (e.g., different backbone, different input modality, or concurrent/subsequent publication).
4. **Add a limitations paragraph** discussing at what point BPA becomes unnecessary or harmful (e.g., as training samples increase), and how APR handles out-of-distribution test samples.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
Three queries on related topics returned papers in three bands:
- Low band (<3.5): Papers scoring 2.5–3.0 (e.g., CLIP-LAD at 3.0, D3AD at 3.0) — papers with fundamental flaws or marginal contributions.
- Middle band (3.5–7.5): Papers scoring 4.25–5.67 (e.g., PTAD at 4.25, Prototype-oriented Fast Refinement at 5.50, Model Selection at 5.67) — papers with reasonable ideas but notable weaknesses.
- High band (>7.5): Papers scoring 8.0 — clearly strong papers with no significant methodological issues.

**Initial bracket:** PIRN sits between the middle band and high band — it has genuine contributions and solid experiments, but the Table 2 issue prevents it from reaching the 6+ range. Bracket: **4.5–6.0**.

**Round 2 — Narrowing:**
- "Prototype-oriented Fast Refinement Model" (5.50, Reject): Similar few-shot AD with prototypes. PIRN is a more complete framework (not just a plugin) with broader evaluation, but has the Table 2 issue. Slightly stronger than this anchor.
- "Learn hybrid prototypes for time series AD" (5.60, Accept): Different domain; comparable in comprehensiveness.
- "Model Selection of Anomaly Detectors" (5.67, Reject): Similar quality level but cleaner experimental validation.
- "One-for-All Few-Shot AD" (6.40, Accept): Comparable domain, accepted despite some presentation issues. PIRN has a more serious unresolved experimental inconsistency.
- "AnomalyCLIP" (6.17, Accept): Comprehensive evaluation on 17 datasets. PIRN's evaluation is narrower and has the Table 2 issue.

PIRN is stronger than the 4.25 PTAD paper but weaker than the 6.17/6.40 accepted papers due to the unresolved Table 2 contradiction. It sits closest to the 5.50–5.67 rejected papers but is slightly weaker because the Table 2 contradiction is more central than the issues in those papers.

**Final score: 5.0 — The paper has genuine contributions and mostly solid experiments, but the major inconsistency in Table 2 undermines confidence in a core claimed contribution. The paper should not be accepted in its current form. If the authors can satisfactorily explain or correct the ablation anomaly, it could become a solid contribution.**

**Anchors consulted (all rounds):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| bESxQeXTlo (CLIP-LAD) | 3.00 | R1 | Weaker — fundamental logical AD issues |
| 7jUQHmz4Tq (D3AD) | 3.00 | R1 | Weaker — diffusion AD with less novel contribution |
| Vi6p2TeujL (PTAD) | 4.25 | R1 | Weaker — complex framework, less clean evaluation |
| gTsLBDMZrL (Proto-Fast-Refine) | 5.50 | R1/R2 | Similar topic, PIRN is more complete but has the Table 2 issue |
| 8TBGdH3t6a (H-PAD) | 5.60 | R1/R2 | Different domain (time series), comparable quality |
| J2we1sVd9m (OT-OOD) | 4.60 | R1 | Weaker — simpler method with mixed reviews |
| HW2lIdrvPb (Model Selection) | 5.67 | R2 | Similar quality, PIRN has bigger unresolved issue |
| Zzs3JwknAY (One-for-All Few-Shot) | 6.40 | R2 | Stronger — more comprehensive, accepted |
| buC4E91xZE (AnomalyCLIP) | 6.17 | R2 | Stronger — 17 datasets, accepted |
| JDiER86r8v (MMAD) | 6.50 | R2 | Stronger — benchmark paper, accepted |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>