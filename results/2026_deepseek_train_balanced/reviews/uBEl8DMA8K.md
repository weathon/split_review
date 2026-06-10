## Summary

This paper proposes ANFR (Adaptive Normalization-Free Feature Recalibration), an architecture-level approach for federated learning that combines weight standardization (SWS) with channel attention (CA). The central insight is that weight standardization avoids the client-dependent distortion that activation normalization (especially BN) introduces into channel attention, allowing CA to remain active and discriminative under data heterogeneity. Experiments across five datasets (medical and natural images), six aggregation methods, and three FL scenarios (global, personalized, private) show consistent improvements over BN-ResNet, GN-ResNet, SE-ResNet, and NF-ResNet baselines.

## Strengths

- **Mechanistic analysis pinpoints *why* the combination works, not just that it works.** The paper does not merely report accuracy gains. Section 3 (Figs. 1–2) shows that after heterogeneous FL training on CIFAR-10, SE-ResNet's attention weights saturate toward 1 (rendering CA an identity operation) while ANFR maintains high variability in attention weights across channels and classes. The CSI analysis shows ANFR improves class selectivity after heterogeneous training while BN degrades it. This directly supports the claimed mechanism — that SWS preserves CA's functionality under heterogeneity — and goes beyond what prior normalization-focused FL papers (FedBN, FedTAN, FedWon, ARIA) demonstrate.

- **Concrete, measured DP advantage with a 5.7× smaller accuracy drop.** Under strict DP (ε=1), GN's accuracy drops 17% while ANFR drops only 3% (Section 4.3). This is a specific, quantified result with a plausible explanation (DP-SGD's gradient regularization disproportionately benefits NF models, consistent with prior observations). The practical significance for private FL is clear.

- **Well-controlled ablation isolating the CA+SWS synergy.** The four-model comparison (BN-ResNet, GN-ResNet, SE-ResNet=BN+CA, NF-ResNet=SWS alone, ANFR=SWS+CA) in Section 4.1 cleanly separates the effects of each component. The finding that SE-ResNet *underperforms* plain BN-ResNet on several settings while ANFR *outperforms* NF-ResNet (e.g., +3% on Fed-ISIC2019 with SCAFFOLD) is strong evidence that the benefit is from the combination specifically, formalized mathematically in Eqs. (7) vs. (10).

- **Comprehensive heterogeneity coverage.** The evaluation spans five datasets with qualitatively distinct heterogeneity types: label+quantity skew (Fed-ISIC2019), label skew+covariate shift (FedChest), heavy label skew (CIFAR-10 split-2), cross-device with covariate+quantity skew (CelebA, 9,343 clients), and staining-protocol concept drift (FedPathology). This is more thorough than typical FL architecture studies.

## Weaknesses

### Fatal
None.

### Major

1. **All experiments use ImageNet-pretrained models; no from-scratch comparison is conducted, and the limitation is not acknowledged.** The paper explicitly states (lines 86, 110) that all models — every baseline and ANFR — are pre-trained on ImageNet. This is not a flaw in relative comparisons (all models have the same pre-training), but it narrows what the experiments actually measure. The paper frames ANFR's contribution as addressing data heterogeneity *during FL training*, but the experiments measure how well different architectures *fine-tune* pre-trained representations under heterogeneous conditions. These are not the same task. Practical FL applications — particularly in medical imaging (three of the five datasets) — often cannot assume a pre-training distribution that matches the target domain. Without a single controlled experiment training from scratch (e.g., CIFAR-10 or FedPathology with randomly initialized weights), we cannot determine whether ANFR's advantages stem from FL-specific learning dynamics or from being a generally better architecture for fine-tuning under distribution shift. The paper does not discuss this as a limitation.

### Minor

2. **The central theoretical claim — that weight-derived statistics are consistent across clients — is asserted but not directly verified.** Section 3 (line 84) argues that "since weights are initialized identically and synchronized during FL, these weight-derived statistics are consistent across clients." While weights start identically each round, they diverge during local training — the very challenge FL methods address. The paper does not provide empirical measurements (e.g., cross-client variance of SWS μ, σ vs. BN μ_i, σ_i over training rounds) to substantiate this claimed advantage. The mechanistic analyses (CSI, CA weights) are informative but indirect; they show ANFR's outputs improve, not that the channel descriptor's consistency is the specific mechanism responsible.

3. **Overclaim in the conclusion.** Line 149 states ANFR is "the first method to simultaneously work in GFL, pFL, and private FL scenarios." This is inaccurate: any architecture using GN or LN can work across all three scenarios — GN is the default choice for DP FL precisely because it avoids BN's batch-statistic requirement. The appropriate claim is that ANFR performs *better* than existing alternatives across these scenarios, not that it is the first to be functional in all three.

4. **No computational overhead quantification despite claiming "minimal computational overhead."** The abstract and introduction claim minimal overhead, but the paper reports no parameter counts, FLOPs, or training-time comparisons. SE blocks add parameters; quantifying this trade-off is straightforward and expected for an architecture paper.

5. **Hyperparameter sensitivity of the SE reduction ratio (r=16) is not explored.** The standard ratio from SE-Net is used without ablation. Different values could interact with FL training dynamics.

6. **No ablation on client count or participation rate.** Fed-ISIC2019 has 6 clients and FedChest has 4; only CelebA tests the cross-device regime (9,343 clients). Whether ANFR's advantage scales with the number of clients is unclear.

7. **The paper lacks a limitations section.** Given the pre-training dependence (Point 1) and other caveats, listing limitations would strengthen rather than weaken the paper.

### Trivial

8. The split-3 CIFAR-10 partitioning (used for mechanistic analysis) is referenced only through a citation (\citep{vitfl}) without local description of the number of clients or skew severity.
9. Hyperparameters for CelebA and CIFAR-10 are inherited directly from prior work (\citep{vitfl, pieri}) without architecture-specific tuning, introducing a potential (if common) confound.

## Nice-to-Haves

- **Training from scratch experiment** (see Major weakness 1) — the single highest-leverage improvement.
- **Direct measurement of cross-client variance of weight statistics vs. activation statistics** to substantiate the theoretical claim in Eq. 7 vs. 9.
- **Convergence analysis** — reporting accuracy over rounds would show whether ANFR converges faster or to a different point, relevant for practical deployment.
- **Per-round computational cost** (parameters, FLOPs, or wall-clock time) to quantify the "minimal computational overhead" claim.
- **Client-scale sensitivity** — testing ANFR's advantage across varying numbers of clients and participation rates.

## Removed Points

- **Grad-CAM analysis is "purely qualitative" and adds "marginal evidence"** — REMOVED. Grad-CAM visualizations are standard qualitative evidence in medical imaging papers. The critic's demand for quantitative IoU with bounding boxes is a reasonable extension but not a weakness of the current paper.
- **"Lowest-performing module on each dataset outperforms all baselines" is not verifiable** — REMOVED. The tables referenced (tab:gfl, tab:cross_device, tab:ca_module_comp) exist in the original submission; extraction artifacts do not constitute a reviewer-verifiable weakness.
- **Criticism that the attention mechanism comparison claim "cannot be assessed from the text alone"** — REMOVED. The tables are present in the submission. This is a parser artifact issue.
- **Generic comments about "could the metric be measuring a proxy" or speculation about confounders without a paper anchor** — REMOVED per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an unexpected connection or perspective that the paper itself does not articulate.

## Suggestions

1. Conduct one controlled from-scratch experiment (e.g., CIFAR-10 with randomly initialized models) to show whether ANFR's advantages hold when models are not starting from ImageNet features.
2. Measure and report the cross-client variance of SWS weight statistics vs. BN activation statistics over FL rounds to directly support the theoretical argument.
3. Replace "first method to simultaneously work in GFL, pFL, and private FL" with a more precise claim about ANFR's superior *performance* across these settings.
4. Add a brief limitations paragraph acknowledging the pre-training dependence and the fact that weight statistics also diverge under client drift.
5. Report parameter counts, FLOPs, or per-round training time for all architectures.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>