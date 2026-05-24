Now I have all the information I need. Let me write the consolidated review.

## Summary

PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection, introducing three innovations: Balanced Prototype Assignment (BPA) via optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) for inference-time adaptation to unseen normal variations, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. Experiments on MVTec-3D-AD, Eyecandies, and Real-IAD D3 show consistent improvements over baselines with substantially lower computational cost.

## Strengths

- **Consistent few-shot gains across multiple benchmarks**: Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.9 AUROC_I (5-shot), +3.7 (10-shot), and +2.4 (50-shot), and similar gains on Eyecandies. The improvements hold across all three shot settings and both datasets, demonstrating genuine effectiveness in data-scarce regimes.

- **Component-wise ablation confirms all three innovations matter**: Table 2 isolates BPA, APR, and MNC; removing each produces a measurable drop (e.g., removing APR drops AUROC_I from 0.922 to 0.883, removing BPA drops it to 0.828). This validates that each design choice independently contributes to the reported gains.

- **State-of-the-art accuracy at drastically lower cost**: Table 4 reports PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This directly refutes the assumption that better few-shot AD requires higher cost.

- **Interpretable evidence of prototype encoding**: Figure 4 visualizes token displacements in PCA space, showing anomalous tokens undergo larger shifts toward normal prototypes than normal tokens. The histograms confirm clear separation, providing direct evidence that the prototype codebook acts as a normality anchor.

- **Design-space validation via systematic ablations**: Tables 5 and 6 ablate codebook size K and decoder depth L across multiple shot settings, showing the chosen K=10 and L=2 are empirically grounded rather than arbitrary.

## Weaknesses

### Major

- **Missing FIND baseline from main few-shot results**: FIND (Li et al., 2025) is cited as a "recent SOTA" and compared in the efficiency table (Table 4), where it achieves 0.921 AUROC_I on the 10-shot MVTec-3D-AD setting — nearly matching PIRN's 0.922. Yet FIND is absent from the main few-shot comparison (Table 1). Including it would significantly strengthen the evaluation. The paper should either add FIND to Table 1 or explain why it cannot be directly compared.

- **No error bars or variance reporting**: All few-shot results are reported as point estimates without standard deviations or multiple random seeds. In few-shot settings where the choice of training samples can substantially affect results, this omission is significant. Some margins are very tight (e.g., pixel-level AUROC differences of 0.002–0.006 over INP-Former), making it impossible to assess statistical significance. The paper should report mean and std over at least 3 random seeds.

### Minor

- **APR's robustness to anomalies is asserted but not validated**: The paper claims anomalous patches are "assigned more diffusely across prototypes" and thus "contribute weakly" to context vectors, but provides no empirical analysis of when this mechanism might fail (e.g., large contiguous anomalous regions or subtle consistent shifts). The ablation in Table 2 shows APR contributes a modest +0.006 AUROC_I at 10-shot, so this is not a fatal issue, but the core assumption deserves a dedicated validation experiment (e.g., synthetic injection of anomalies with controlled size/severity).

- **Real-IAD D3 evaluation is supplementary and has uncontrolled comparisons**: Table 8 compares PIRN (RGB + surface normals) against D³M (RGB + Pseudo-3D + 3D) and various single-modality baselines. While the paper acknowledges D³M uses tri-modal inputs and frames this as supplementary, the absence of methods using the exact same input modalities (RGB + surface normals) makes it difficult to isolate PIRN's advantage on this dataset. The paper scopes this correctly as "highly competitive performance" rather than SOTA, so this is a minor concern.

- **Missing detail on few-shot training procedure**: The paper states "60 epochs in few-shot tasks" but does not specify whether early stopping or a validation set is used, nor whether this is sufficient to avoid overfitting with only 5–10 training samples. An ablation on epoch count or training dynamics would be informative.

### Trivial

None.

## Nice-to-Haves

- Compare PIRN against a version with APR disabled at test time across more settings (not just 10-shot) to better quantify the benefit of dynamic adaptation.
- Provide per-category breakdowns for the main few-shot results (currently deferred to appendix).
- Analyze how the OT-based context extraction in APR behaves under controlled anomaly sizes/severities.

## Removed Points

- **INP-Former baseline adaptation is unfair**: REMOVED — The harsh critic claims the adaptation "entirely discards INP-Former's core contribution" of test-time prototype extraction. This is factually incorrect. The two-stream adaptation applies INP-Former independently per modality, each stream performing test-time prototype extraction on its own modality's input. This is the natural and standard way to adapt a 2D method to multimodal inputs. Adding cross-modal fusion to INP-Former would be unfair in the opposite direction (giving it capabilities it was not designed for).

- **Formatting/style nitpicks about Real-IAD table**: REMOVED — The table formatting issues mentioned by the harsh critic are parser artifacts, not author errors.

- **General concern that APR blurs normality/anomaly line**: The paper explicitly addresses this through OT-based context extraction (anomalous patches diffuse across prototypes) and GRU gating. This is a reasonable theoretical justification, and the ablation shows APR provides modest gains (0.922 vs 0.916), meaning the core method does not collapse without it.

## Novel Insights

The review surface reveals an interesting tension: PIRN's total computational cost (103G FLOPs) is dominated by the frozen DINOv2 encoder, not the prototype decoder. This means the prototype-based reconstruction pipeline adds almost negligible overhead beyond feature extraction — a finding that generalizes beyond this specific paper. Papers proposing complex multi-stage decoders for anomaly detection should benchmark against the cost of the encoder itself, since the encoder often dominates.

## Suggestions

1. **Add FIND to the main few-shot comparison** (Table 1) or provide a clear justification for its exclusion. This is the most impactful fix.
2. **Report mean and standard deviation over 3+ random few-shot splits** for all key results, especially where margins are tight.
3. **Validate APR's robustness empirically**: create a controlled experiment where anomalies of known size/severity are synthetically inserted, and measure context vector corruption.
4. Clarify the few-shot training protocol (early stopping, validation split, overfitting analysis).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (3 queries, 12 anchors total):**

| Anchor | Score | Round | Comparison to PIRN |
|--------|-------|-------|-------------------|
| bESxQeXTlo (CLIP-LAD) | 3.00 | R1 | Much weaker; rejected due to limited evaluation |
| MbtUctg3KW (Generalized AD) | 2.50 | R1 | Much weaker; poor generalization analysis |
| O0vy7hHqyU (Fake News Detection) | 3.00 | R1 | Unrelated topic; weaker |
| 3ZdGSTxKuy (Harry Potter) | 2.00 | R1 | Unrelated; weaker |
| Vi6p2TeujL (PTAD tabular) | 4.25 | R1 | Weaker; complex framework with unclear contributions, rejected |
| gTsLBDMZrL (Prototype-oriented Fast Refinement) | 5.50 | R1 | Most similar topic; PIRN is stronger (better evaluation, clearer ablations, multimodality) |
| J2we1sVd9m (Prototype OT for OOD) | 4.60 | R1 | Weaker; limited domain |
| 8TBGdH3t6a (H-PAD time series) | 5.60 | R1 | Comparable quality but different domain; PIRN more thorough |
| cJs4oE4m9Q (Orthogonal Hypersphere) | 8.00 | R1 | Stronger; cleaner evaluation, no missing baselines |
| TPZRq4FALB (Multi-modal TTA) | 8.00 | R1 | Stronger; more rigorous evaluation |
| 9Cu8MRmhq2 (Multi-granularity Correspondence) | 8.00 | R1 | Stronger; different topic |
| cNmu0hZ4CL (Noisy Neural OT) | 8.00 | R1 | Stronger; different topic |

**Round 1 bracket:** 4.5–8.0

**Round 2 — Narrowing (2 queries, 10 anchors total):**

| Anchor | Score | Round | Comparison to PIRN |
|--------|-------|-------|-------------------|
| gTsLBDMZrL (Prototype-oriented Fast Refinement) | 5.50 | R2 | Weaker; rejected with methodological concerns |
| J2we1sVd9m (Prototype OT for OOD) | 4.60 | R2 | Weaker |
| 8TBGdH3t6a (H-PAD time series) | 5.60 | R2 | Comparable quality but different domain |
| 3P87ptzvTm (Optimal Multiple Transport) | 5.00 | R2 | Different topic; weaker |
| 3WB5hT27zf (Partial OT for SSL) | 5.33 | R2 | Different topic; weaker |
| Zzs3JwknAY (One-for-All Few-Shot AD) | 6.40 | R2 | Comparable; accepted with similar evaluation scope |
| JDiER86r8v (MMAD benchmark) | 6.50 | R2 | Different contribution (benchmark paper) |
| buC4E91xZE (AnomalyCLIP) | 6.17 | R2 | Comparable; accepted with methodological questions |
| ybFRoGxZjs (ThermalGaussian) | 6.60 | R2 | Different topic |
| ENv1CeTwxc (Segment Any 3D Object) | 6.50 | R2 | Different topic |

PIRN sits cleanly between the 5.5 rejected anchor (gTsLBDMZrL) and the 6.4 accepted anchor (Zzs3JwknAY). It is stronger than the former (better evaluation, clearer contributions) but has evaluation gaps (missing FIND baseline, no error bars) that the latter addresses. The appropriate score is **6.0**, reflecting a solid paper with meaningful contributions that needs targeted improvements in experimental rigor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>