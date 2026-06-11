## Summary
This paper proposes Medix, a two-stage framework for OOD detection leveraging unlabeled "wild data." Stage 1 filters candidate OOD samples using a greedy iterative leave-one-out procedure based on element-wise medians (EWM) of gradients from a pre-trained InD classifier. Stage 2 trains a binary OOD detector on labeled InD data and the extracted outliers. The paper provides theoretical error bounds on the filtering step and comprehensive empirical evaluation across CIFAR-10/100 with five OOD datasets against 20 baselines.

## Strengths
- **Consistent SOTA across all InD-OOD pairs**: Tables 1 and 2 show Medix achieves best FPR95 across all five OOD datasets for both CIFAR-10 (average 0.80% vs 3.40% for WOODS) and CIFAR-100 (average 5.42% vs 6.74% for WOODS). Standard deviations are small (±0.37 on CIFAR-100 average FPR95), indicating stable results.
- **Novel and well-motivated median-based approach**: Figure 1 demonstrates monotonic increase in L2-norm deviation between InD mean gradient and EWM as OOD samples increase, providing clear empirical grounding for the filtering formulation. The median is a natural robust statistic for this purpose.
- **Two-sided theoretical framework**: Theorems 4.1 and 4.2 bound both inlier and outlier misclassification rates, decomposing errors into interpretable contamination, concentration, and separation effects. Remark 4.3 validates the sub-Gaussian assumption empirically (histogram + Q-Q plot), and Theorem C.3 provides a looser bound without this assumption.
- **Practical dataset-level mixing**: Unlike WOODS and Du et al. (2024a) which require batch-level mixing ratios, Medix operates at dataset level — a more practical assumption for real-world deployment with large outsourced datasets.
- **Comprehensive baselines**: Comparison against 20 baselines spanning InD-only methods, wild-data methods, and recent approaches, following the established WOODS protocol for fair comparison.

## Weaknesses

### Fatal
None.

### Major
- **Disconnect between theoretical analysis and actual algorithm**: Theorems 4.1 and 4.2 analyze the misclassification rates of an "EWM filtering rule" (line 134: "the inlier misclassification rate of the EWM filtering rule satisfies"), which appears to be a single-shot threshold-based classification rule. However, Algorithm 1 implements a greedy iterative leave-one-out procedure that removes top-k samples per iteration, recomputing the EWM on a changing set each time. These are fundamentally different operations. Yet line 158 states "these results provide rigorous theoretical assurance that Medix minimizes both types of errors under mild assumptions" — this claim is not substantiated since the theorems don't analyze the algorithm that is actually run.

- **Misleading comparison framing in abstract and conclusion**: The abstract (line 9) and conclusion (line 262) headline "40.98% improvement in FPR95 over KNN+" — but KNN+ is an InD-only method without access to wild data. The fair comparison against WOODS (the prior SOTA for the wild-data setting) shows more modest improvements: 1.32% on CIFAR-100 and 2.60% on CIFAR-10 in FPR95. The paper does mention the WOODS comparison in the introduction (line 27) but the headline framing throughout emphasizes the less fair comparison.

- **Theoretical bounds are essentially vacuous at the sole experimental operating point**: All experiments use π = 0.5. At this value, Theorem 4.1's contamination term is π/[2(1−π)] = 0.5 and Theorem 4.2's contamination term is (1−π)/2π = 0.5. The bounds permit up to 50% misclassification from contamination alone, providing no meaningful guarantee at the experimental setting. The theory is most informative for π ≪ 0.5, a regime the paper never explores experimentally.

### Minor
- **Missing claimed baselines**: The baselines section (line 174) explicitly mentions CONJ and DRL, and the conclusion (line 262) claims to "outperform... DRL," but neither appears in Tables 1 or 2.
- **Only CIFAR-scale experiments**: All main experiments are on CIFAR-10/100. Results on a larger-scale benchmark would strengthen the "open-world" applicability claim.
- **No systematic filtering accuracy analysis**: The paper's primary contribution is the filtering stage, yet the only filtering accuracy reported is a single 2D synthetic example (12.5% error). Precision/recall of outlier extraction for the actual CIFAR settings would directly validate the core contribution.
- **No sensitivity analysis over π**: All experiments fix π = 0.5. Varying π would connect directly to the theoretical predictions and demonstrate robustness.
- **Stopping criterion in Algorithm 1 appears incorrect**: Line 110 states "while t ≤ T or |δ_max| > ε". With "or", the loop runs whenever either condition holds, only terminating when both are false (t > T AND |δ_max| ≤ ε), effectively always running to T iterations. This should likely be "and" for early stopping via ε to function.

### Trivial
None.

## Nice-to-Haves
- Report filtering accuracy (precision/recall of outlier extraction) across actual experimental settings, not just the 2D toy.
- Vary π in experiments to demonstrate robustness and connect to theoretical predictions.
- Bridge the theory-algorithm gap honestly — either scope the theorems as motivating the algorithm or provide analysis of the greedy procedure.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting/presentation nitpicks — parser artifacts, not author issues.
- Concerns about pseudo-label quality being deferred to appendix — this is standard practice and the appendix exists in the original submission.

## Novel Insights
The median-based gradient filtering approach is genuinely novel for OOD detection with wild data. The insight that removing OOD samples monotonically brings the EWM of gradients closer to the InD mean gradient (Figure 1) is intuitive and well-validated. The decomposition of theoretical errors into contamination, concentration, and separation effects provides interpretable guidance for when the method succeeds or fails. This represents a meaningful advance over the predecessor SAL framework (Du et al., 2024a).

## Suggestions
- Restructure results discussion to lead with fair comparisons against wild-data methods (WOODS, OE, Energy(w/OE)) rather than InD-only methods.
- Clearly scope the theoretical claims: state that theorems analyze an idealized EWM rule that motivates the algorithm, rather than claiming they directly guarantee the algorithm's properties.
- Add π-sensitivity experiments to bridge theory and practice.
- Report filtering accuracy metrics for CIFAR experimental settings.

## Reporting: Calibration Summary

**All anchors retrieved across rounds:**

| Round | Paper Path | Avg Score | Comparison |
|-------|-----------|-----------|------------|
| R1 & R2 | `jlEjB8MVGa.md` (Du et al., "How Does Unlabeled Data Provably Help OOD Detection?") | 6.50 | Predecessor with nearly identical setting; Medix improves on it empirically but has worse theory-algorithm alignment |
| R2 | `VTYg5ykEGS.md` ("ImageNet-OOD: Deciphering Modern OOD Detection") | 6.50 | OOD benchmarking paper, accepted |
| R2 | `mUXdysoxEP.md` ("Pursuing Feature Separation via Neural Collapse") | 6.75 | OOD detection with separation-based approach, accepted |
| R2 | `kwCHcaeHrf.md` ("SPADE: Provably Safeguarding a Classifier") | 5.50 | Provably-safe OOD detection, accepted |
| R2 | `eN0RyRVbSm.md` ("Double Descent Meets OOD Detection") | 6.50 | Theoretical OOD analysis, rejected |
| R2 | `am7BPV3Cwo.md` ("Rethinking OOD on Imbalanced Data") | 5.75 | OOD on imbalanced data, rejected |
| R2 | `0owAtTCOlU.md` ("GRIC") | 5.75 | Zero-shot OOD detection, rejected |
| R1 | `iqAbdT35hE.md` ("SMOT: Smooth Training for OOD") | 5.75 | Training strategy for OOD, rejected |
| R1 | `Cdhxv0Oz1v.md` ("GradRect: Gradient-based OOD Detection") | 4.20 | Gradient-based OOD, rejected |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed to:** 5.5–6.5. 

Medix is most comparable to Du et al. (2024a, score 6.5). It improves empirically on the predecessor and uses a more intuitive median-based approach, but has a more pronounced theory-algorithm gap and misleading comparison framing. Papers at 5.5–5.75 were consistently rejected; Medix's contribution is clearly above that threshold. The final score of 6.0 reflects a solid contribution above the typical accept/reject boundary but slightly below the predecessor due to the theory-algorithm disconnect and framing issues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>