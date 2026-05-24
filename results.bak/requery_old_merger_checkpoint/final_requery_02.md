Now I have all the information I need. Let me write the consolidated review.

## Summary

**Round 1 bracket:** Based on the calibration search, the weak anchors (avg ~2-3) and strong anchors (avg ~8) help me bracket this paper. The most topically similar anchors sit in the 5.5-6.5 range. PIRN is clearly much stronger than the 4-5.5 papers and comparable to the 6-6.5 papers. **Round 1 bracket: 5.5–6.5.**

**Narrowing within bracket:** The One-for-All Few-Shot AD paper (6.40, accepted) addresses a related prototype-based few-shot AD problem but with a different paradigm. AnomalyCLIP (6.17, accepted) tackles zero-shot anomaly detection. Both have cleaner evaluations (more baselines, some error bars) but PIRN has three datasets, more extensive ablations, and efficiency analysis. PIRN is slightly weaker in evaluation rigor (missing FIND baseline in main table, no error bars) but stronger in method novelty and scope (multimodal). Placing it at **6.0** is appropriate — it is a solid paper with real contributions and meaningful but fixable evaluation gaps.

Here is the full review:

---

## Summary

PIRN proposes a prototype-driven intra-modal reconstruction framework for few-shot multimodal anomaly detection. The key innovations are: (1) Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, (2) Adaptive Prototype Refinement (APR) for online adaptation to unseen normal variations, and (3) Multimodal Normality Communication (MNC) for cross-modal prototype knowledge transfer. The method achieves SOTA results on MVTec-3D-AD, Eyecandies, and Real-IAD with dramatically lower computational cost (85% fewer FLOPs vs. FIND).

## Strengths

1. **Consistent few-shot gains across multiple benchmarks**: Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.9 AUROC_I (5-shot), +3.7 (10-shot), +2.4 (50-shot) and on Eyecandies by +3.6, +4.0, +2.2 in the same settings — direct evidence that the method succeeds in data-scarce regimes where prior work degrades.

2. **Component-wise ablation confirms all three innovations matter**: Table 2 isolates BPA, APR, and MNC; removing each from the full model produces a measurable drop (e.g., removing APR drops AUROC_I from 0.922 to 0.883, removing MNC drops to 0.916), proving that balanced assignment, adaptive refinement, and cross-modal communication each contribute independently to the reported gains.

3. **State-of-the-art accuracy at drastically lower cost**: Table 4 reports PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs, contradicting the assumption that better few-shot AD must be more expensive. The efficiency comparison includes both M3DM and CFM as well.

4. **Interpretable evidence of discriminative prototype encoding**: Figure 4 plots token displacements in PCA space and shows anomalous tokens undergo larger shifts than normal tokens during reconstruction, with histograms confirming clear separation — this directly supports the claim that prototypes act as normality anchors.

5. **Design-space validation via systematic ablations**: Tables 5 and 6 ablate codebook size K and decoder depth L across multiple settings; the optimal K=10 and L=2 are consistent, and performance drops with too many or too few prototypes/layers, showing the paper's design choices are empirically grounded.

## Weaknesses

### Major

1. **Missing FIND baseline from main few-shot comparison (Table 1)**: The paper cites FIND as "the recent SOTA" and reports its performance (0.921 AUROC_I on 10-shot MVTec-3D-AD) in the efficiency comparison (Table 4), but FIND is absent from the main few-shot table (Table 1). Given that FIND achieves near-identical accuracy to PIRN (0.921 vs. 0.922) on the 10-shot setting, omitting it from the main comparison is a significant gap. The paper's claims of consistent superiority would be strengthened by including FIND in Table 1, or by clearly stating why FIND cannot be directly compared (e.g., different backbone, different input requirements).

2. **No variance reporting for few-shot results**: The paper reports results for 5-shot, 10-shot, and 50-shot settings without standard deviations or multiple random trials. In few-shot anomaly detection, the specific sample selection can substantially affect results, and some pixel-level margins over baselines are very small (e.g., AUROC_P gains of +0.002 to +0.006, AUPRO gains of +0.003 to +0.006). Without error bars from at least 3 random seeds, the statistical significance of these improvements cannot be assessed. This is a standard expectation in the field.

### Minor

3. **APR's robustness assumption lacks empirical validation**: The paper argues that anomalous patches are assigned "diffusely" across prototypes during APR's OT-based context extraction, contributing weakly to prototype updates. This is a plausible theoretical justification but is never empirically validated. No analysis is provided for cases where this assumption might break (large anomalous regions, subtle whole-image anomalies). The ablation shows APR's contribution is modest (0.922 vs 0.916 without APR), so this is not a fatal flaw, but the paper would benefit from a targeted experiment quantifying context vector corruption under known anomalies.

4. **Real-IAD D3 comparison is supplementary and not perfectly controlled**: The Real-IAD evaluation uses full-shot (not few-shot) data and compares against D³M which uses a tri-modal representation (2D + Pseudo-3D + 3D) while PIRN uses RGB + surface normals. The paper acknowledges this difference but does not include baselines with the exact same input modalities. Since this experiment is secondary to the paper's few-shot focus, this is a minor concern rather than a major one.

### Trivial

5. Table 8 formatting has OCR artifacts making some values difficult to parse (several columns appear misaligned).

## Nice-to-Haves

- An analysis (synthetic or real) measuring when APR's OT-based context extraction breaks down — e.g., insertion of known anomalies of varying sizes and measurement of context vector deviation.
- A comparison against INP-Former with a more sophisticated multimodal adaptation (e.g., using the same MNC-style fusion but with INP-Former prototypes) would strengthen the claim that PIRN's specific design choices matter.
- A brief study on the sensitivity of few-shot results to the choice of training samples.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add FIND to the main few-shot comparison table (Table 1), or clearly explain why it cannot be fairly compared.
2. Report mean and standard deviation over at least 3 random few-shot splits for all main results.
3. Add an empirical analysis of APR's robustness to anomalies — e.g., synthetically injecting known anomalies into test images and measuring how much the context vector deviates from the true normal prototype.
4. Clean up the Real-IAD table formatting and add a note about the modality differences between compared methods.

---

## Score and Decision

**Calibration summary of anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| bESxQeXTlo (CLIP-LAD) | 3.00 | R1-bracket | Much weaker — limited evaluation, single dataset |
| MbtUctg3KW (Generalized AD) | 2.50 | R1-bracket | Much weaker — limited evaluation, different problem |
| O0vy7hHqyU (Fake News) | 3.00 | R1-bracket | Different problem, lower quality |
| 3ZdGSTxKuy (Harry Potter) | 2.00 | R1-bracket | Different problem, weak |
| Vi6p2TeujL (PTAD) | 4.25 | R1-bracket | Weaker — tabular domain, less clear method |
| gTsLBDMZrL (Prototype-oriented Refinement) | 5.50 | R1-bracket | Most similar topic, rejected. PIRN is clearly stronger (more datasets, ablations, multimodality, efficiency) |
| J2we1sVd9m (Prototype OT for OOD) | 4.60 | R1-bracket | Different task, weaker evaluation |
| 8TBGdH3t6a (H-PAD) | 5.60 | R1-bracket | Different domain (time series), accepted. PIRN compares favorably |
| 3P87ptzvTm (Multiple Transport) | 5.00 | R1-bracket | Unrelated topic |
| 3WB5hT27zf (Partial OT) | 5.33 | R1-bracket | Unrelated topic |
| Zzs3JwknAY (One-for-All Few-Shot) | 6.40 | R2-narrow | Few-shot AD, accepted. PIRN has broader evaluation but less clean baselines |
| JDiER86r8v (MMAD) | 6.50 | R2-narrow | Benchmark paper, different contribution type |
| buC4E91xZE (AnomalyCLIP) | 6.17 | R2-narrow | Zero-shot AD, accepted. PIRN comparable in quality |
| ybFRoGxZjs (ThermalGaussian) | 6.60 | R2-narrow | Different topic (3D rendering) |
| ENv1CeTwxc (Segment Any 3D) | 6.50 | R2-narrow | Different topic (3D segmentation) |

**Round 1 bracket:** 5.5–6.5
**Narrowing:** R2 anchors in 6.0–6.5 (One-for-All, MMAD, AnomalyCLIP) show papers of similar ambition with stronger evaluation hygiene. PIRN's method is novel and well-ablated, but the missing FIND baseline and lack of error bars are real gaps that the 6.0–6.5 papers generally address.

**Final score rationale:** PIRN has genuine contributions (BPA, APR, MNC) with strong empirical support across multiple benchmarks and impressive efficiency. The missing FIND baseline and lack of variance reporting are significant but fixable evaluation gaps. The paper is stronger than those at 4–5.5 but slightly below the clearest 6.5+ papers due to these evaluation limitations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>