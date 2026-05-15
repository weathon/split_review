Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper tackles imbalanced novel class discovery (NCD) in point cloud segmentation, extending prior work (NOPS) that assumed equal class sizes. The authors propose (1) a semi-relaxed Optimal Transport formulation with an adaptive regularization schedule that relaxes the uniform prior as training progresses, and (2) a dual-level representation that enforces regional consistency using DBSCAN-based spatial grouping. Experiments on SemanticKITTI and SemanticPOSS show consistent improvements over NOPS (e.g., +7.7% average novel mIoU on SemanticPOSS, +4.1% on SemanticKITTI).

## Strengths

- **Adaptive regularization for imbalanced NCD is well-motivated and effective.** The paper identifies a genuine limitation of prior work (equal-size constraint on novel classes) and proposes a data-dependent annealing scheme for the regularization weight γ in the semi-relaxed OT formulation. Evidence: Table 5 shows adaptive γ (44.2 mIoU) substantially outperforms the best fixed γ (36.0), demonstrating that relaxation of the uniform prior must be adaptive, not static (Sec. 3.3, Table 5).

- **Dual-level representation incorporating spatial context provides clear gains.** The method augments point-level predictions with region-level consistency via DBSCAN clustering and shared prototypes. Ablation Table 4 shows the region branch adds 4.2% mIoU on top of adaptive regularization alone (44.2 → 48.4 on Split 0), and confusion matrices (Fig. 2) show reduced cross-class noise, directly supporting the claim that regional consistency improves segmentation quality.

- **Consistent, substantial improvements across diverse settings.** On SemanticPOSS (Table 1), the method achieves average novel IoU of 30.2% vs. NOPS 22.5% (+7.7%). On the harder imbalanced splits (Table 2), gains reach +7.6% on Split 0. On SemanticKITTI (Table 3), average novel IoU is 27.5% vs. NOPS 23.4% (+4.1%). These results hold across 4 splits with varying class composition.

- **Robustness to misspecified number of novel classes.** When the number of novel classes is estimated (|C<sup>u</sup>| = 3 vs. GT = 4), the method still achieves 53.47% novel mIoU vs. NOPS 31.95% (Table 9), demonstrating practical utility beyond the oracle-knowledge setting (Sec. 3.5).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are well-supported by the experimental evidence. No methodological flaw invalidates the central claims.

### Minor

- **The hyperparameter indicator's reliability as a selection criterion is not fully validated.** The paper uses an indicator I = L + γ·KL(...) computed on the training set to select ρ and T, and shows it correlates with novel IoU on Figs. 4–5. While this is a standard approach in unsupervised/NCD settings (where novel class labels are unavailable by definition), the correlation is imperfect: e.g., ρ = 0.001 yields a lower indicator value but worse mIoU (33.11) than ρ = 0.005 (44.21). The claim that the indicator provides a "balanced evaluation" (Sec. 3.4) would benefit from a more systematic analysis — e.g., reporting the indicator—mIoU correlation across all ρ/T values, or validating on a held-out subset using known-class IoU as an auxiliary signal. This does not undermine the paper's results (the chosen hyperparameters are reasonable and tested across multiple splits), but the selection procedure's claimed rigor is slightly overstated.

- **DBSCAN-based region generation is not analyzed for sensitivity or quality.** The method relies on DBSCAN (ε = 0.5, min_samples = 2) to produce regions for the dual-level representation (Sec. 3.2). The paper states only that "95% of the point clouds are included" but provides no statistics on region counts, region sizes, purity w.r.t. ground-truth labels, or stability across runs. Since the region branch contributes 4.2% mIoU improvement (Table 4), its robustness to small changes in DBSCAN parameters is relevant but unexamined. Adding a brief sensitivity analysis would strengthen the paper.

- **The comparison of adaptive γ against step decay/cosine annealing baselines could be more informative.** The paper shows adaptive γ (44.2) substantially outperforms step decay (best 34.6) and cosine annealing (best 36.1) on Split 0 (Tables 6–7). These baselines start at γ = 1 and decay every epoch, which is reasonable but represents one design choice. The gap is large (8–10%), and while this supports the claim that epoch-driven schedules are inferior, the paper would be stronger by also testing a schedule that starts from a higher initial γ (e.g., γ₀ = 5 or 10) with slower decay, to better isolate the benefit of the "data-dependent" condition vs. simply having a non-uniform, slowly decaying γ. As presented, the comparison is valid but leaves room for the concern identified.

- **Several implementation details are underspecified.** (a) It is not stated whether regions are generated once at the start of training or recomputed as features evolve (Sec. 3.2: "during training, we first utilize DBSCAN" is ambiguous). (b) Prototype initialization for known classes (from labeled data?) is not described. (c) Whether the "T iter" in Eq. 5 refers to epochs or gradient steps is not specified — given T = 10 and total epochs = 10, it is likely epochs, but this should be stated explicitly. These are minor clarity issues that do not affect reproducibility but would benefit from clarification.

### Trivial

- In the ablation table (Table 4), the baseline row is described only as "baseline which employs equal-size constraints." A precise description (whether it is a re-implementation of NOPS or a stripped version of the proposed method) would aid interpretation.

## Nice-to-Haves

- Report DBSCAN region statistics (count, size distribution, purity) and a sensitivity analysis for ε and min_samples to confirm the region branch's robustness.
- Include a qualitative comparison with and without the region branch to visualize its corrective effect (the paper shows one example in Fig. 1, but a side-by-side would be more informative).
- A brief analysis of whether training for more than 10 epochs further improves results would address concerns about early stopping.

## Removed Points

- *Issue 1 (Hyperparameter selection is "fundamentally flawed" / "methodologically invalid"):* This criticism is too harsh and ignores the realities of NCD, where novel class labels are unavailable on any subset. Using a training-set-based indicator is standard practice in unsupervised/clustering literature. The paper additionally validates the indicator by showing its correlation with actual novel IoU. The concern about circularity is theoretically reasonable but applies to virtually all unsupervised hyperparameter selection methods, and the paper's approach is at least as principled as alternatives. Moved from "fatal" to "minor" with appropriate framing.

- *Claim that the step decay and cosine annealing comparisons are "unfair" and "not properly calibrated":* The paper tried 5 different λ values (0.1, 0.3, 0.5, 0.7, 0.9) for step decay and 5 different min γ values for cosine annealing. This is a reasonable search. The accusation of improper calibration is speculative and unsupported. The gap may genuinely reflect the superiority of data-dependent scheduling. Moved from "evidential" severity to "minor" with a suggestion for additional baselines.

- *Criticism about 10 epochs being short:* The authors follow the same setting as in prior work (NOPS) and claim to reproduce NOPS with their code. Without evidence that longer training changes results, this is a speculative concern.

- *Criticism that the ablation baseline is "not precisely defined" and "likely their own weaker baseline":* The paper explicitly states "compared to baseline which employs equal-size constraints." This is sufficiently clear for an ablation study, and the relative improvements are measured consistently.

- *Strength Finder's claim that hyperparameter selection is "principled" and a "practical contribution":* This overstates the case. The indicator is a reasonable heuristic but not rigorously principled. The strength is retained with appropriate caveats but reframed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the practical realities of unsupervised hyperparameter selection in NCD and ideal experimental rigor, but neither reviewer identifies a genuinely novel observation about the method or problem that the paper itself does not already articulate.

## Suggestions

1. **In the camera-ready revision, add a brief DBSCAN sensitivity analysis** (ε = 0.3, 0.5, 0.7; min_samples = 1, 2, 3) showing region counts, coverage, and impact on final mIoU. This directly addresses the most substantive remaining concern.

2. **Clarify the hyperparameter indicator's limitations.** Acknowledge that the indicator is a heuristic, report the correlation coefficient (or a table of indicator vs. mIoU for all ρ/T values tried), and note that the chosen range is robust but the indicator should not be treated as a perfect proxy.

3. **Add a note about region generation timing:** explicitly state whether DBSCAN is run once at the start of training or periodically, and clarify the "T iter" unit in Eq. 5.

## Score and Decision

The paper makes a clean, well-motivated contribution to an under-explored problem (imbalanced NCD in point cloud segmentation). The core ideas — adaptive regularization via data-dependent γ annealing and dual-level representation — are clearly articulated and validated by consistent, sometimes large, improvements across two datasets and multiple splits. The weaknesses are minor (DBSCAN sensitivity analysis missing, some presentation underspecifications) and addressable in a camera-ready version. No fatal flaw undermines the central claims.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>