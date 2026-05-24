Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper proposes PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). The method combines three novel components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) with gated GRU updates to handle unseen normal variations at test time, and Multimodal Normality Communication (MNC) for cross-modal knowledge transfer. Experiments on MVTec-3D-AD, Eyecandies, and Real-IAD D3 show strong few-shot performance, and the method is substantially more efficient (85% fewer FLOPs) than prior work.

## Strengths

1. **Novel and well-motivated technical approach.** The three components (BPA via balanced OT, APR with gated GRU refinement, MNC via prototype alignment + cross-attention) are clearly motivated by specific limitations of prior MAD methods (codebook collapse, static prototypes, isolated modalities). The method represents a genuine synthesis of ideas not previously combined for few-shot MAD.

2. **Consistent empirical gains across multiple few-shot settings.** Table 1 shows PIRN outperforms all listed baselines on MVTec-3D-AD and Eyecandies at 5-, 10-, 50-, and all-shot settings, with AUROC_I improvements of +3.7 to +4.0 over the strongest baselines at 10-shot. Gains are consistent across both image-level and pixel-level metrics.

3. **Substantial efficiency advantage.** Table 4 demonstrates PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than FIND (the prior SOTA, 728.46G/76.09ms). This is a genuine practical strength for real-time industrial inspection.

4. **Strong ablation and analysis.** The ablation studies (Tables 2, 3, 5, 6, 7) validate the contribution of each component, the optimal prototype count (K=10), decoder depth (L=2), and the APR aggregation method. The displacement visualization (Figure 4) provides interpretable evidence that anomalous tokens undergo larger prototype-driven shifts.

5. **Clear and well-structured presentation.** The method description (Section 3) is technically precise with formal equations for the OT formulation, cross-attention, and gating mechanisms. The architecture figure (Figure 2) effectively communicates the design.

## Weaknesses

### Fatal
None.

### Major

1. **FIND (Li et al., 2025) is omitted from the main accuracy comparison (Table 1) despite being acknowledged as SOTA.** The paper includes FIND in the efficiency comparison (Table 4), where it achieves 0.921 AUROC_I on 10-shot MVTec-3D-AD — essentially tied with PIRN's 0.922. However, FIND does not appear in Table 1, which instead lists baselines that are 3–9 points lower. The paper's central claim of "consistently superior performance" is materially weakened by this omission; a reader cannot assess whether PIRN advances accuracy over the actual strongest competitor or merely matches it. While the accuracy data exists in Table 4, the separation into different tables creates an incomplete picture in the main comparison. The authors should (a) include FIND in Table 1, (b) clearly state the 0.001 gap, and (c) qualify the superiority claim given the essentially tied accuracy (while still highlighting the large efficiency advantage).

### Minor

2. **Few-shot results are reported without variance or multiple trials.** The paper reports single-point AUROC estimates for 5-, 10-, and 50-shot settings. With such small training sets, performance is sensitive to which specific samples constitute the "shot." Standard practice in few-shot AD (e.g., Fang et al., 2023; Tian et al., 2024) is to report mean and std over multiple random trials. While the reported gains over the best baseline in Table 1 are reasonably large (+3.7 to +4.0), the absence of variance information means statistical significance cannot be assessed, especially against the INP-Former baseline where gaps are smaller.

3. **APR's marginal benefit over top-k averaging is small.** Table 7 shows balanced OT (AUROC_I 0.922) vs. top-k averaging (0.921) — a 0.001 improvement. While this doesn't invalidate APR, the paper's claim that APR "dynamically expand the model's knowledge of unseen normal variations" is only weakly evidenced by the empirical comparison. The design intuition is sound, but the current numbers suggest the GRU gating, rather than the OT-based weighting, may be the main source of any improvement.

### Trivial

4. The ablation table header says "BFA" instead of "BPA" — a minor typo.

## Nice-to-Haves

- Including FIND in the main comparison Table 1 (not just in the efficiency table) would substantially strengthen the evaluation.
- Adding standard deviation over ≥5 random shot selections to the few-shot results.
- A controlled-backbone comparison where baselines use the same DINOv2 ViT-B/14 features would help isolate the method's contribution from feature quality.

## Removed Points

These points were raised by reviewers but are removed with justification:

1. **"Ablation table (Table 2) contains a numerical inconsistency (Row 4 = 0.967 vs Row 5 full = 0.922) that contradicts the claimed benefits of APR."** — REMOVED. All checkmarks in the parsed table are garbled (every row shows "✓ | ✓ | ✓"), making it impossible to determine which components are active in each row. This is a PDF parser artifact: the original submission has distinguishable checkmark patterns (✓/✗) per row that the parser collapsed. The paper text explicitly states "removing each component from the full model results in a consistent performance drop," which would correctly correspond to the original, distinguishable table. Criticisms based on the garbled output are invalid per the hard rule on parser artifacts.

2. **"Real-IAD D3 image-level results (0.873 vs D³M's 0.890) contradict the claim of consistently superior performance."** — Partially removed (downgraded from Fatal to a scope note). The abstract qualifies the superiority claim with "under challenging few-shot settings." Real-IAD D3 is evaluated in the full-shot regime; the paper never claims superiority in that setting, only "highly competitive performance." PIRN also achieves the best pixel-level AUROC (0.961) with only two modalities vs. D³M's three. No contradiction exists.

3. **Generic strengths from the Strength Finder** (e.g., "The problem selection is well-motivated") — REMOVED as generic or insufficiently specific.

4. **"The paper lacks theoretical proofs for the OT formulation"** — REMOVED. This is an empirical systems paper; theoretical analysis of the Sinkhorn algorithm beyond what is standard is not expected venue practice.

5. **Request for failure case analysis and t-SNE of prototypes** — MOVED to Nice-to-Have; these would strengthen the paper but are not required for its core contribution.

## Novel Insights

The most interesting observation from the review synthesis is a tension in the evidence for APR's contribution. The harsh critic correctly notes that the OT-based aggregation in APR (balanced OT) only marginally outperforms a simpler top-k averaging baseline (0.922 vs 0.921 AUROC_I), yet the ablation table (Table 2) attributes a large gain to APR (0.828 → 0.883 when added to the baseline). This suggests APR's benefit may come more from the GRU gating mechanism than from the OT-based context extraction — a distinction the paper does not analyze. Additionally, the fact that FIND achieves 0.921 with presumably very different methodology suggests that the 10-shot MVTec-3D-AD benchmark may be approaching saturation at ~0.92 AUROC_I, making further progress in the few-shot MAD setting contingent on harder benchmarks or different evaluation dimensions (e.g., efficiency, as PIRN already demonstrates).

## Suggestions

1. **Add FIND to Table 1** and clearly discuss the accuracy gap (0.922 vs 0.921) while emphasizing PIRN's efficiency advantage. This is the single most impactful revision.
2. **Report few-shot results with standard deviations** over multiple random seeds (≥5) to establish statistical significance.
3. **Disentangle APR's contributions**: ablate the GRU gating separately from the OT-based context weighting to clarify which mechanism drives improvement.
4. **Qualify superiority claims** to acknowledge that against the strongest competitor (FIND), PIRN is essentially tied in accuracy while being far more efficient.

## Score and Decision

**Calibration anchors** (all from `deepreview_13k_calibration`):

| Path | Avg Human Score | Comparison to PIRN |
|------|----------------|-------------------|
| `cJs4oE4m9Q.md` (Deep Orthogonal Hypersphere Compression) | 8.00 | Stronger: has theoretical proofs, rigorous experimental design, and clean presentation. PIRN is not at this level. |
| `Zzs3JwknAY.md` (One-for-All Few-Shot AD via Prompt Learning) | 6.40 | Comparable: both address few-shot AD with novel methods and solid experiments. PIRN's method is more technically sophisticated but has the FIND omission weakness. |
| `gTsLBDMZrL.md` (Prototype-oriented Fast Refinement for Few-shot IAD) | 5.50 | Slightly weaker: also uses OT for prototypes in few-shot IAD, but is a plugin method with less comprehensive evaluation. PIRN is stronger in method originality and experiment breadth. |
| `bESxQeXTlo.md` (CLIP-LAD) | 3.00 | Weaker: limited novelty, simple CLIP application. PIRN has substantially more technical depth and stronger empirical evidence. |
| `MbtUctg3KW.md` (Generalized Anomaly Detection with Knowledge Exposure) | 2.50 | Much weaker: poor writing, weak experiments, unclear contribution. PIRN is clearly stronger. |
| `6hP9JcXpNk.md` (Going beyond familiar features for deep AD) | 3.67 | Weaker: single-modality AD, limited evaluation scope. PIRN addresses a harder multimodal setting with stronger results. |
| `HW2lIdrvPb.md` (Model Selection of Anomaly Detectors) | 5.67 | Comparable but different problem (model selection vs. detection). PIRN's method contributions are more substantial. |

PIRN has genuine technical novelty (BPA, APR, MNC), strong empirical results on 3 benchmarks, and a clear efficiency advantage. However, the omission of FIND from the main accuracy comparison is a notable evaluation gap that weakens the central claim. The paper is positioned above clearly rejected papers (3–4 range) and is comparable to borderline accept/reject papers (~5.5–6.4 range), but the evaluation gap prevents it from rising to the level of a strong accept. A revised version addressing the FIND issue and adding variance estimates could be a solid paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>