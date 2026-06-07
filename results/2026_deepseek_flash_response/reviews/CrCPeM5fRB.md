## Summary

The paper proposes SDSC (Signal Dice Similarity Coefficient), a structure-aware reconstruction metric for time-series SSL that extends the Dice coefficient from segmentation to continuous signed signals. SDSC replaces the MSE loss in the reconstruction branch of SimMTM while keeping the contrastive objective unchanged, and a hybrid loss (SDSC + MSE) is also introduced. Experiments on forecasting and classification benchmarks show comparable or marginally improved performance relative to MSE.

## Strengths

- **Concrete demonstration of MSE failure modes (Table 1, Figure 1)**: Table 1 quantitatively shows that MSE, MAE, and DTW assign deceptively low error scores to semantically meaningless signals (e.g., an inverted signal gets MSE=0.0200 despite being the semantic opposite) whereas SDSC correctly assigns 0.0000. This provides concrete motivation for a structure-aware metric.

- **Clean controlled experimental design**: Only the reconstruction loss is varied; the contrastive objective (InfoNCE) is kept fixed across all experiments. This isolation ensures that any downstream differences are attributable to the reconstruction objective, which is cleaner than typical SSL comparisons.

- **Honest treatment of SDSC's limitations**: The paper identifies that SDSC discards amplitude information and proposes a principled hybrid loss with uncertainty-based weighting (Kendall et al., 2018). The hybrid often outperforms both pure MSE and pure SDSC, demonstrating intellectual honesty rather than overselling the standalone method.

## Weaknesses

### Fatal
None.

### Major

1. **Small and inconsistent empirical improvements — the central claim is not convincingly supported.** The paper's core thesis is that SDSC improves representation quality by enforcing structural fidelity. Yet the downstream results tell a different story:
   - **Forecasting (Table 4)**: MSE=0.295 vs SDSC=0.294 — effectively identical. On Electricity, both achieve 0.200 MSE.
   - **Cross-domain frozen classification (Table 5)**: MSE (62.19%) actually *outperforms* SDSC (61.64%). The paper attributes this to "amplitude patterns" in the epilepsy dataset but provides no mechanistic analysis.
   - **In-domain frozen classification (Table 5)**: SDSC achieves 76.38% vs MSE's 75.45%, a ~0.9% improvement. However, no confidence intervals, standard deviations, or statistical significance tests are reported — it is impossible to know whether this gap is reliable or noise.
   - **Fine-tuned classification (Table 6)**: All methods converge to essentially the same performance (PCC slightly ahead at 79.76% vs SDSC's 79.60%).
   
   The paper's own framing ("improvements are moderate," "comparable downstream performance") concedes that the practical benefits are marginal. For a new-method paper at a top venue, the proposed method should clearly advance performance or provide a non-trivial new capability. The current evidence meets neither threshold.

2. **Limited evaluation breadth restricts generalizability.** Only one backbone (SimMTM) is tested. Integration into other frameworks (TI-MAE, contrastive-only methods) is explicitly deferred to future work. DILATE, directly relevant as a structure-aware time-series loss, is discussed in related work but not experimentally compared. The paper's findings may be specific to the SimMTM architecture's particular balance of contrastive and reconstruction objectives.

### Minor

3. **No variance estimates for main results.** The paper states "fixed random seeds across all runs" but does not report multiple runs with different seeds. Given the small performance gaps (~0.9% accuracy in the best case, identical in forecasting), it is impossible to distinguish signal from noise. The TILDE-Q paper (a closely related work on shape-aware losses for time series) received similar criticism and was rejected at similar scores for the same issue.

4. **The hybrid loss frequently matches or outperforms pure SDSC.** This is honestly presented, but it means standalone SDSC is rarely the best option in the paper's own results. Forecasting: Hybrid MSE=0.4783 vs SDSC MSE=0.6348 (Table 2). Classification: Hybrid (76.23%) and SDSC (76.38%) are essentially tied (Table 5). This attenuates SDSC's claimed role as a replacement for MSE.

5. **Sensitivity to the sharpness parameter α not discussed in the main text.** The paper states α=10 is used (based on Appendix A.3, which is stripped), but no analysis of how downstream results vary with this parameter is provided in the main paper.

### Trivial
6. SI-SNR is included in comparisons despite sometimes failing to converge (noted in the table caption), making those comparisons uninformative.

## Nice-to-Haves
- Analyze learned representations directly (e.g., t-SNE/UMAP visualization, nearest-neighbor retrieval, or probing tasks) to connect SDSC to representation quality, rather than only measuring downstream metrics two steps removed.
- Compare against a simple normalized MSE baseline (e.g., MSE on per-sample z-scored signals) to test whether normalization alone addresses the amplitude sensitivity concern.
- Investigate why cross-domain frozen classification favors MSE and what "amplitude patterns" means mechanistically (the current post-hoc explanation is unsupported).

## Removed Points
These points were considered but removed under the filtering rules:
- "Motivating examples are cherry-picked" — Standard practice; the examples correctly illustrate mathematical limitations of MSE. The paper does not claim these specific examples occur during SSL training.
- "Weak correlation means MSE and SDSC measure different things" — The paper already makes this point; it supports the hybrid approach, not a weakness.
- "No comparison against normalized MSE" — The paper already uses z-score normalization per channel (line 151).
- "DILATE should be compared" — Acknowledged as future work with compute constraints.
- "Gradient analysis during training" — Not standard practice for this type of paper.
- "Missing related works" — Cannot be verified externally.
- Formatting/style nitpicks — Parser artifacts.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report all main results with confidence intervals or multiple-seed variance — this is essential given the small performance gaps.
2. Include at least one additional backbone (e.g., TI-MAE) to demonstrate generalizability beyond SimMTM.
3. Analyze the learned representations directly (structural fidelity probes, nearest-neighbor retrieval) rather than only downstream metrics.
4. Provide a systematic analysis of when SDSC helps vs. hurts (e.g., gesture vs. epilepsy) to guide practical use.

## Calibration Anchors

**Round 1 (Bracketing, 3 queries):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../xJ5CF1aOOX.md` | 2.50 | 1 | Weak paper with basic flaws; our paper is clearly better (coherent method, cleaner experiments) |
| `/home/.../i4ouG6Kc8M.md` | 2.50 | 1 | Similar: weak SSL paper; our paper is better |
| `/home/.../qU1GtrDDst.md` | 1.80 | 1 | Very weak; our paper is much stronger |
| `/home/.../Y89o3LAEHX.md` | 2.00 | 1 | Weak; our paper is stronger |
| `/home/.../sz7HdeVVHo.md` | 5.25 | 1 | Structure-preserving contrastive learning (Reject). Showed clearer improvements across tasks than our paper, rejected for limited novelty |
| `/home/.../c56TWtYp0W.md` | 6.00 | 1 | GAFormer (Accept). Achieved SOTA with clear empirical gains; our paper is much weaker empirically |
| `/home/.../nphsoKxlFs.md` | 4.00 | 1 | DynaCL (Reject). Tested on 3 datasets, novelty concerns. Comparable quality to our paper |
| `/home/.../UCeZMMyjm2.md` | 4.50 | 1 | TSRM (Reject). Extensive hyperparameter tuning, modest novelty. Similar quality range |
| `/home/.../PdaPky8MUn.md` | 8.00 | 1 | Very strong paper; our paper is far below this level |
| `/home/.../hrqNOxpItr.md` | 8.00 | 1 | Very strong theoretical paper; not comparable |
| `/home/.../Dxl0EuFjlf.md` | 6.00 | 1 | TILDE-Q (Reject). Shape-aware loss for TS. Stronger empirical evidence (multiple architectures, clearer improvements) than our paper, but still rejected |

**Round 2 (Narrowing, 2 queries):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../7egJb0X9m2.md` | 5.00 | 2 | TILDE-Q (Reject). Same motivation (replacing MSE with shape-aware loss), but tested across multiple architectures and showed consistent improvements. Our paper is weaker empirically |
| `/home/.../Dxl0EuFjlf.md` | 6.00 | 2 | TILDE-Q (Reject). Higher-scoring version, still rejected. Stronger empirical evaluation than ours |
| `/home/.../nphsoKxlFs.md` | 4.00 | 2 | DynaCL (Reject). Comparable to our paper in quality |
| `/home/.../DgRdeJF0k7.md` | 5.25 | 2 | Masked Dual-Temporal AE (Reject). Stronger empirical results |
| `/home/.../yGv5GzlBwr.md` | 5.25 | 2 | TimeDART (Reject). Stronger empirical results |
| `/home/.../iI7hZSczxE.md` | 5.67 | 2 | Disentangling TS representations (Accept). Stronger empirical/theoretical contribution |
| `/home/.../N1TyUhkvjW.md` | 5.00 | 2 | TS anomaly detection (Reject). Comparable quality |

**Round 1 bracket:** 3.5 – 6.5  
**Round 2 narrowing:** After comparing against TILDE-Q (5.00-6.00, both Reject — our paper is weaker empirically despite similar motivation), DynaCL (4.00, Reject), and TSRM (4.50, Reject), I place the paper at 4.0. It is clearly above the 1.8-2.5 range of fundamentally flawed papers, but below the 5.00-6.00 range of TILDE-Q which had stronger empirical evidence (multiple architectures, clearer improvements) and was still rejected. The paper's clean formulation and honest assessment are commendable, but the empirical case is simply too weak to support its central claims.

## Score and Decision

**Score rationale:** The paper has a clear motivation, a mathematically clean formulation, and a well-controlled experimental setup. However, the empirical evidence is the decisive weakness: forecasting results are identical to MSE, the only notable improvement (~0.9% accuracy in one of four classification settings) lacks variance estimates, and cross-domain frozen classification actually favors MSE. For ICLR, a new-method paper must demonstrate that its proposed approach provides meaningful advantages over existing baselines — the current evidence is insufficient.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>