Now I have enough calibration anchors to form a final judgment. Let me synthesize everything into the review.

**Round 1 Bracket:** The paper sits clearly above the weak band (3.0-3.4: papers with fundamental novelty/clarity issues) and below the strong band (7.5+: transformative contributions like NoPoSplat at 8.0). Initial bracket: **5.0 to 7.0**.

**Round 2 Narrowing:** Compared against Ref-Gaussian (6.50, Accept) and the 5.75 anchors (RAIN-GS, IBGS — both Reject):
- D²GS is clearly stronger than the 5.75 papers, which had more marginal gains and less compelling evaluations
- D²GS is comparable to but slightly weaker than Ref-Gaussian (6.50), which had a more novel problem setting and a cleaner contribution, though both share some evaluation gaps
- **Final score: 6.0**, borderline Accept

Let me write the review now.

---

## Summary
D²GS proposes a unified framework for sparse-view 3D Gaussian Splatting that addresses two identified failure modes: near-field overfitting (via Depth-and-Density Guided Dropout, DD-Drop) and far-field underfitting (via Distance-Aware Fidelity Enhancement, DAFE). The paper also introduces Inter-Model Robustness (IMR), a new distribution-based metric for quantifying stability across training runs. Experiments on LLFF and MipNeRF360 show SOTA results, with D²GS outperforming the previous best method DropGaussian by 0.59 dB PSNR on LLFF 3-view.

## Strengths
- **Well-motivated problem analysis:** The paper provides concrete evidence (Figure 1) of near-field overfitting and far-field underfitting in sparse-view 3DGS, showing Gaussian primitive counts differ dramatically between dense and sparse settings. This analysis motivates the two complementary modules cleanly.
- **Effective method with SOTA results:** D²GS achieves 21.35 PSNR on LLFF 3-view (1/8 res.), outperforming DropGaussian (+0.59 dB), CoR-GS (+0.90 dB), and other strong baselines. Gains hold on MipNeRF360 (+0.35 dB over DropGaussian), confirming broad effectiveness (Tables 1–2).
- **Thorough component and hyperparameter ablations:** Tables 4–6 systematically validate each component (density score, depth score, depth-based layering, DAFE), test sensitivity to dropout rates and weights, and confirm compatibility with three different monocular depth estimators. The ablations demonstrate robustness to parameter choices and depth prior quality.
- **Clear qualitative improvements:** Figure 4 shows D²GS preserving sharper geometric details and avoiding the blurring/artifacts visible in 3DGS, CoR-GS, and DropGaussian.

## Weaknesses

### Fatal
None.

### Major
- **Ablation baseline does not isolate DD-Drop from existing dropout:** The paper states "Our implementation is built on DropGaussian" (Section 4), but the central component ablation (Table 4) starts from vanilla 3DGS (PSNR 19.22). Since DropGaussian already employs dropout, the ablation cannot distinguish gains attributable to the proposed depth-and-density guidance from gains that any dropout strategy would provide. The gains shown (19.22 → 21.17 from DD-Drop components) conflate "having dropout" with "having DD-Drop specifically." While the full pipeline beats DropGaussian in Table 1 (21.35 vs. 20.76), this comparison involves the complete system including DAFE, so the specific value of DD-Drop over DropGaussian's own dropout remains unquantified. A controlled ablation starting from DropGaussian with its dropout disabled (or comparing DD-Drop vs. uniform dropout at matched rates) would directly address this.

- **IMR metric lacks validation and has unexplained anomalies:** IMR is presented as a contribution but (i) the aggregation formula (Eq. 14, log of ratio of squared sum to sum) is introduced without derivation or justification of what property it captures; (ii) no correlation is shown between IMR and rendering-quality variance (e.g., standard deviation of PSNR/SSIM across the same 10 runs); (iii) Table 3 shows vanilla 3DGS achieves a better IMR (3.162) than DropGaussian (3.205), despite DropGaussian having substantially better rendering quality (PSNR 20.76 vs. 19.22 in Table 1). The paper never discusses this counterintuitive result. Without validation tying IMR to practically meaningful outcomes, the metric remains an unvalidated proposal rather than a contribution.

### Minor
- **No computational cost or runtime analysis:** The method adds monocular depth estimation, per-step DD-Drop computation, and (for IMR) optimal transport. Training time, memory footprint, and inference overhead relative to baselines are not reported, which matters for practitioners.
- **No failure case or limitation discussion:** The conclusion restates contributions without addressing when the method might fail (e.g., poor monocular depth in textureless or reflective regions, scenes with extreme near-far ratios breaking the tertile partitioning, or reliance on SfM initialization).
- **DAFE hyperparameter τ tuned on evaluation set:** The paper reports "selecting the top 5% of the farthest depth values yields the best performance" (Section 4, Table 5). If this was tuned per-dataset or per-scene on test data, it risks overfitting to the evaluation scenes. The paper should clarify whether τ=5% was chosen on a validation split.
- **Depth score orientation ambiguity:** Eq. 1 uses min-max normalized depth d̃_i. Near-field Gaussians should receive higher dropout probability since they are the overfitting region, but if depth is normalized with near=0 and far=1, near Gaussians get low scores. The paper does not clarify whether depth is inverted. The strong empirical results suggest the orientation is correct in practice, but this should be stated explicitly for reproducibility.

### Trivial
- The paper would benefit from reporting confidence intervals or standard deviations for PSNR/SSIM in Tables 1–2 given the instability documented in Figure 3.

## Nice-to-Haves
- Extending IMR to the MipNeRF360 dataset would provide a more complete picture of the metric's behavior across different scene types.
- An experiment comparing DD-Drop against a simple uniform dropout (matched for dropout rate) would directly quantify the benefit of the depth-and-density guidance.
- Reporting IMR with error bars (e.g., standard deviation across the 10 training runs) would help assess whether differences like 3.039 vs. 3.109 are statistically meaningful.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"The claim that DropGaussian uses 'uniformly dropping Gaussian primitives' may misrepresent the method"* — REMOVED. DropGaussian's own paper describes its dropout; this paper characterizes it relative to DD-Drop. Not a factual error in this paper.
- *"The IMR uses a first-order Taylor approximation... the fidelity of these approximations is not examined"* — MOVED to minor/background. The paper acknowledges the approximation and states the derivation is in the appendix (which is stripped). The harsh critic's framing as a fatal flaw is disproportionate; many metrics use approximations without explicit fidelity analysis.
- *"The global layering into tertiles with fixed attenuation factors (0.3, 0.7) is a heuristic that may not transfer"* — DOWNGRADED to observation. The paper explicitly states the method aims to introduce depth prior "without strongly relying on such partitioning" and the attenuation factors work across two different datasets (LLFF and MipNeRF360), suggesting reasonable transferability.
- *"The IMR table reports only a scalar value... Without error bars on IMR itself, one cannot judge whether the difference is statistically meaningful"* — MOVED to Trivial. This is a presentation preference, not a methodological flaw.
- *"The introduction's promise of a 'comprehensive evaluation' overstates the scope"* — REMOVED. Rhetorical nitpick; the evaluation is reasonably comprehensive for the venue.
- *"The motivation figure relies on a single scene and a single baseline"* — REMOVED. Figure 1 is illustrative motivation, not an experimental claim. The quantitative experiments span multiple scenes.

## Novel Insights
The paper's observation that sparse-view 3DGS exhibits a spatially structured failure mode — near-field overfitting with excessive Gaussian density and far-field underfitting with insufficient coverage — is well-articulated and supported by concrete primitive-count evidence. The dual-response strategy (probabilistic dropout for overfitted regions, targeted loss for underfitted regions) is a coherent design principle that could generalize beyond the specific dropout and loss implementations proposed here.

## Suggestions
- Re-center the component ablation on DropGaussian: start from DropGaussian with its own dropout disabled, then add DD-Drop components progressively. This would cleanly isolate the contribution of spatial guidance over any dropout.
- Validate IMR by correlating it with the standard deviation of PSNR/SSIM across the 10 independent runs, and discuss the 3DGS-vs-DropGaussian anomaly. If validation cannot be provided, consider framing IMR as a diagnostic analysis rather than a primary contribution.
- Add a brief limitations paragraph and report training/inference time relative to DropGaussian and 3DGS.

## Score and Decision

**Calibration anchors:**
- GeoGS3D (3.40, Reject): significantly weaker — fundamental clarity/novelty issues; D²GS is far stronger
- I86z54CL2y (3.40), NLRo4qhg6t (3.00), ZDoaLbOFaP (3.00): all weak rejects with major methodological gaps; not comparable
- RAIN-GS (5.75, Reject): decent but incremental 3DGS modification, practical relevance concerns; D²GS has stronger results and clearer motivation
- IBGS / vkj5ARRCeY (5.75, Reject): novel idea but marginal gains (0.02 CD), much slower; D²GS shows more meaningful improvements
- Ref-Gaussian / xPxHQHDH2u (6.50, Accept): two-component 3DGS extension, SOTA results, good ablations, some approximation/novelty concerns; D²GS is comparable but slightly weaker due to the ablation baseline issue and under-validated IMR metric
- NoPoSplat (8.00, Accept): transformative contribution, clearly stronger; not in D²GS's tier

**Round 1 bracket:** 5.0–7.0
**Round 2 narrowing:** D²GS sits between the 5.75 and 6.50 anchors, closer to 6.0. It is clearly better than the 5.75 papers (stronger results, better ablations, clearer motivation) but has more significant evaluation gaps than Ref-Gaussian at 6.50 (specifically the ablation baseline issue and unvalidated IMR metric).

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>