Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper presents PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection. It introduces three components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) for test-time adaptation to unseen normal variations, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3 across 5/10/50-shot and full-shot settings, achieving consistent improvements over baselines while being substantially more efficient (4.35× faster than FIND at comparable accuracy).

## Strengths

- **Consistent few-shot gains across multiple benchmarks.** Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.7 AUROC\_I (10-shot) and +2.4 (50-shot); on Eyecandies by +4.0 and +2.2 in the same settings. The gains hold across shot levels and both datasets, providing direct evidence that the method succeeds in data-scarce regimes.

- **Component-wise ablation confirms all three innovations contribute.** Table 2 isolates BPA, APR, and MNC; removing each produces a measurable drop (e.g., removing APR drops AUROC\_I from 0.922 to 0.883, removing MNC drops to 0.916). This validates that balanced assignment, adaptive refinement, and cross-modal communication each independently contribute.

- **SOTA accuracy at drastically lower cost.** Table 4 reports PIRN achieves 0.922 AUROC\_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC\_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This demonstrates that better few-shot MAD need not be more expensive.

- **Design-space validation via systematic ablations.** Tables 5 and 6 ablate codebook size K and decoder depth L across multiple settings; optimal choices (K=10, L=2) are consistent, and performance degrades with too few or too many prototypes/layers, showing design choices are empirically grounded.

- **Interpretable evidence of prototype-based normality encoding.** Figure 4 plots token displacements in PCA space and shows anomalous tokens undergo larger shifts than normal tokens during reconstruction, with histogram separation — directly supporting the claim that prototypes act as normality anchors.

## Weaknesses

### Major

- **Missing SOTA baseline from main few-shot comparison.** FIND (Li et al., 2025) is cited for surface normal generation and compared in the efficiency table (Table 4) where it achieves 0.921 AUROC\_I on the 10-shot setting — nearly matching PIRN's 0.922. Yet FIND is absent from the main few-shot comparison table (Table 1). As FIND is explicitly described as "the recent SOTA" on MVTec-3D-AD, this omission weakens the paper's central claim of "consistently achieving superior performance." The authors should include FIND in Table 1 or explain why a fair comparison is infeasible.

- **Lack of error bars for few-shot results.** Few-shot anomaly detection is known to be sensitive to which specific training samples are drawn. The paper reports no variance across random seeds or few-shot splits. Some margins over baselines are small (e.g., AUROC\_P differences of +0.002–0.006), making it impossible to assess statistical significance. Reporting mean and std over at least 3 random trials with different few-shot splits is standard practice and essential given these margins.

### Minor

- **APR's robustness assumption is unvalidated.** The paper argues that anomalous patches are assigned "diffusely" across prototypes during OT-based context extraction, contributing only weakly to prototype updates. This is a plausible theoretical claim, but no empirical analysis is provided (e.g., statistics on prototype update magnitudes for normal vs. anomalous inputs, or a synthetic experiment injecting known anomalies). The ablation ("wo APR") shows APR contributes ~0.6 AUROC\_I, so this is not fatal, but validating the claimed robustness mechanism would strengthen the paper.

- **Real-IAD comparison is supplementary but not perfectly controlled.** The Real-IAD D3 results use the full-data (not few-shot) setting and compare against D³M which uses tri-modal inputs (RGB+Pseudo-3D+3D) versus PIRN's dual-modal (RGB+surface normals). The paper acknowledges these differences, but the section would benefit from including baselines that use the same input modalities. The claim that PIRN "significantly outperforms D³M in specific categories" is cherry-picked from 2 out of 20 categories and should be contextualized.

- **FIND could appear in more places.** Beyond the main table, the paper compares FIND only on the 10-shot setting in the efficiency table. Showing FIND's performance across all shot settings (5-shot, 50-shot) would strengthen the evaluation.

### Trivial

- None of consequence.

## Nice-to-Haves

- An ablation of the APR's inference-time adaptation with APR disabled at test time (comparing training-only vs. adaptive prototypes) is partially done in Table 2 but would benefit from a dedicated study across shot settings with error bars.
- The paper could clarify whether early stopping or a validation split is used during few-shot training (60 epochs with 5-10 samples could lead to overfitting without monitoring).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add FIND to the main few-shot comparison table (Table 1) across all shot settings, or justify its exclusion.
2. Report mean and standard deviation over at least 3 random seeds for all few-shot results.
3. Provide an empirical analysis of APR's robustness: e.g., measure context vector deviation when known anomalies are inserted, or compare prototype update magnitudes for normal vs. anomalous test samples.

## Score and Decision

### Round-1 bracket

I first searched three score bands: weak anchors (avg < 3.5), middle anchors (3.5–7.5), and strong anchors (7.5+). The weak anchors (e.g., CLIP-LAD at 3.00, Generalized AD at 2.50) are clearly below PIRN. The middle anchors include closely related few-shot AD papers (prototype-oriented fast refinement at 5.50, One-for-All few-shot AD at 6.40). Strong anchors (8.00) are cleaner papers with minimal evaluation gaps. This bracketing placed PIRN between roughly 5.5 and 7.0.

### Round-2 narrowing

I then searched within the (4.5, 6.0) and (6.0, 7.5) bands for more topically similar anchors. Key comparisons:

- **Prototype-oriented Fast Refinement (gTsLBDMZrL, 5.50, Reject):** Uses OT for prototype refinement in few-shot industrial AD. PIRN is clearly stronger — more thorough evaluation (3 datasets vs. 3), better ablation design, clearer writing, and addresses the harder multimodal setting.
- **H-PAD (8TBGdH3t6a, 5.60, Accept):** Prototype-based time series AD. PIRN has more thorough evaluation and clearer motivation but both papers have comparable evaluation rigor.
- **PTAD (Vi6p2TeujL, 4.25, Reject):** Prototype tabular AD. PIRN is substantially stronger in clarity, evaluation breadth, and result consistency.
- **One-for-All Few-Shot AD (Zzs3JwknAY, 6.40, Accept):** Multi-class few-shot AD. PIRN has more comprehensive ablations and broader evaluation (3 datasets × multiple shots), though both have some evaluation gaps (missing baselines).

### Final calibration

PIRN is stronger than the 5.5-level papers and comparable to the 6.0–6.5 papers. The missing FIND baseline and lack of error bars are real weaknesses that prevent a higher score. A score of **6.0** reflects a solid paper with genuine contributions and a generally strong evaluation, held back by specific evaluation gaps that are addressable in revision. The core technical contributions (BPA via balanced OT, APR with gated GRU updates, MNC with prototype alignment) are novel and well-validated by the ablation study.

### Anchors consulted

| Anchor | Score | Round | Comparison to PIRN |
|--------|-------|-------|-------------------|
| bESxQeXTlo (CLIP-LAD) | 3.00 | 1 | Much weaker |
| MbtUctg3KW (Gen. AD) | 2.50 | 1 | Much weaker |
| O0vy7hHqyU (Fake News) | 3.00 | 1 | Different domain, weaker |
| 3ZdGSTxKuy (Harry Potter) | 2.00 | 1 | Different domain, much weaker |
| Vi6p2TeujL (PTAD) | 4.25 | 1 | Weaker method/evaluation |
| gTsLBDMZrL (Proto. Refine.) | 5.50 | 1,2 | Weaker in evaluation breadth and method clarity |
| J2we1sVd9m (Proto. OT OOD) | 4.60 | 1,2 | Different task, weaker |
| 8TBGdH3t6a (H-PAD) | 5.60 | 1,2 | Comparable rigor, different domain |
| 3P87ptzvTm (Multi OT) | 5.00 | 2 | Different task, less relevant |
| 3WB5hT27zf (Partial OT) | 5.33 | 2 | Different task, less relevant |
| Zzs3JwknAY (One-for-All) | 6.40 | 2 | Comparable strength, different paradigm |
| JDiER86r8v (MMAD) | 6.50 | 2 | Different focus (benchmark, not method) |
| buC4E91xZE (AnomalyCLIP) | 6.17 | 2 | Comparable strength, some evaluation gaps |
| ybFRoGxZjs (ThermalGaussian) | 6.60 | 2 | Different domain, less relevant |
| ENv1CeTwxc (Segment3D) | 6.50 | 2 | Different task, less relevant |
| cJs4oE4m9Q (Orthogonal HS) | 8.00 | 1 | Stronger, cleaner evaluation |
| TPZRq4FALB (Test-time Adapt) | 8.00 | 1 | Stronger, different task |
| 9Cu8MRmhq2 (Norton) | 8.00 | 1 | Stronger, different domain |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>