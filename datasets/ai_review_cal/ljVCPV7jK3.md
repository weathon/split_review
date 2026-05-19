- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper addresses fairness in the "demographic scarce regime" where sensitive attributes are available only for a small labeled subset. The authors propose FairDSR, a two-stage framework: (1) training an uncertainty-aware sensitive-attribute classifier via self-ensembling with Monte Carlo dropout, and (2) enforcing fairness constraints only on samples whose predicted sensitive attribute carries low uncertainty. The key hypothesis — that low-uncertainty samples are more suitable for fairness enforcement — is validated across five benchmark datasets with multiple ablations, including a cross-validation with conformal prediction as an alternative uncertainty measure.

## Strengths

- **Uncertainty–fairness correlation is empirically well-established.** Table 1 shows a clear pattern: datasets with higher mean uncertainty in attribute predictions (e.g., LSAC at 0.66) exhibit substantially lower baseline unfairness (ΔDP=0.014) than low-uncertainty datasets (e.g., Adult at 0.15, ΔDP=0.18). Figure 1 further demonstrates that training without fairness constraints on increasingly uncertain subsets monotonically reduces unfairness across all three metrics (ΔDP, ΔEOP, ΔEOD) on multiple datasets, supporting the paper's central hypothesis with direct evidence.

- **FairDSR achieves competitive or better fairness-accuracy tradeoffs than using true sensitive attributes on specific datasets and metrics.** On Adult, FairDSR (certain) achieves ΔEOP=0.015±0.010 vs. VanillaFairness (true attributes) 0.021±0.014 — a meaningful improvement. On Compas, FairDSR (weighted) achieves ΔDP=0.027±0.016 vs. VanillaFairness 0.032±0.011 while maintaining substantially higher accuracy (0.672 vs. 0.634). These results are specific, quantified, and non-trivial: using predicted attributes can match or beat ground-truth demographic information in certain regimes.

- **The core hypothesis generalizes to a fundamentally different uncertainty measure (conformal prediction).** Section 5.3.3 shows that using conformal prediction sets to select low-uncertainty samples also yields better Pareto fronts than using full proxy attributes, for multiple coverage levels ε. Table 4 further shows that models trained without fairness constraints on uncertain-only samples (empty or two-valued sets) achieve ΔDP as low as 0.003, compared to 0.12 for certain-only samples. This ablation significantly strengthens the paper by decoupling the benefit from the specific MC-dropout mechanism.

- **Ablation on the consistency loss isolates its role.** Figure 4 shows that removing the consistency loss (λ=0) degrades the fairness-accuracy Pareto front, while still outperforming baselines that naïvely use predicted attributes. This demonstrates that the uncertainty-aware training (not just any attribute classifier) is responsible for the improvement.

- **Strong baseline coverage and thorough experimental design.** The paper compares against seven baselines spanning proxy-attribute methods (CGL, FairDA, FairRF), distributionally robust methods (ARL, DRO, CVarDRO), and preprocessing methods (KSMOTE), with 7 runs each, error bars, and Pareto-front visualizations. Three variants of FairDSR (certain, weighted, uncertain) are evaluated, showing consistent advantages over existing methods.

## Weaknesses

### Fatal
None. The core methodology is sound and the central hypothesis is well-supported.

### Major

- **The abstract's strongest claim — that FairDSR "can outperform models trained with fairness constraints on the true sensitive attributes in most benchmarks" — is not adequately supported by the main-text evidence.** On Adult, the comparison is mixed: FairDSR (certain) improves ΔEOP (0.015 vs. 0.021) but is comparable or slightly worse on ΔDP (0.007 vs. 0.005) and ΔEOD (0.018 vs. 0.017). On Compas, VanillaFairness strictly dominates FairDSR (certain) on all three fairness metrics (ΔDP 0.032 vs. 0.085, ΔEOP 0.039 vs. 0.067, ΔEOD 0.041 vs. 0.074). The FairDSR (weighted) variant does beat VanillaFairness on Compas ΔDP (0.027 vs. 0.032) but is worse on the other two fairness metrics. The remaining three datasets (CelebA, LSAC, New Adult) are referenced only in appendix figures. As presented in the main text, the evidence supports "competitive or better on certain datasets and metrics" — a weaker and more precise claim than "outperforms in most benchmarks." This overclaim risks undermining an otherwise solid contribution, as it may lead readers to expect results the main text does not display. *The authors should either (a) qualify the claim to match what the main text can verify, or (b) move sufficient evidence for all five datasets into the main body.*

### Minor

- **The operating point used for single-point comparisons (Tables 1–2) is ambiguously selected.** The paper states models were "trained...to achieve minimal fairness violation" (line 149), but it is unclear whether this means the λ that yields the lowest unfairness regardless of accuracy, or some other criterion. Since the method's strength lies in the tradeoff curve (captured well by the Pareto fronts in Figure 2), the single-point tables are informative only with a clearly stated selection rule (e.g., the point with lowest ΔEOD at ≤2% accuracy drop). Without this, the reader cannot assess whether the tables are cherry-picked. *The authors should clarify the selection rule or replace the tables with a summary of Pareto-front comparisons (e.g., area under the Pareto curve, unfairness at a fixed accuracy).*

- **The threshold R used in the consistency loss (Eq. 2) is never reported for any dataset.** While the threshold H for the downstream classifier is stated for each dataset (line 127), R — which controls the teacher-student consistency during attribute-classifier training — is described only as being "updated using a Gaussian warmup function" (line 88) with no specific initial or final values. This makes the attribute-classifier training protocol incompletely specified. *Authors should report R's value or the range searched for each dataset.*

- **The requirement of a validation set with sensitive attributes to tune H should be more explicitly discussed in the context of the demographic-scarce setting.** The paper notes that H "can be tuned over a validation set" (line 106) and uses 10% of training data for this (line 127), but this means some jointly labeled (X, Y, A) data is needed beyond D2. While this is a practical and common requirement, the framing could more clearly acknowledge this assumption.

### Trivial
None.

## Nice-to-Haves

- A brief analysis of when each FairDSR variant (weighted vs. certain vs. uncertain) is preferable would strengthen the paper (e.g., "weighted when accuracy matters more; certain when fairness priority is highest"). This is already partially discussed but could be made more systematic.
- The authors could consider reporting the area under the fairness-accuracy Pareto curve as a single summary statistic for method comparison, reducing reliance on single-point tables.

## Removed Points

- *Criticism about missing appendix content or proofs* — Removed per instructions: the parser strips appendix sections from all papers; they exist in the original submission.
- *Criticism about reproducibility due to undisclosed hyperparameters or trivial implementation details* — Removed per instructions.
- *Strength Finder's claim of "consistent outperformance across existing baselines on multiple datasets" (strength #5)* — Rephrased and merged into the baseline-coverage strength above. The original wording was slightly overstated (e.g., on Compas, CGL achieves better ΔEOP than FairDSR (certain): 0.065 vs. 0.067), so the claim was weakened to match what the data actually shows.
- *Harsh critic's concern about FairDSR dominating on "most benchmarks" when the Pareto curves may show this for all five* — The underlying concern (overclaim in abstract) is retained as a Major weakness. The speculation about appendix-only results was removed; the retained criticism focuses on what is verifiable in the main text.

## Novel Insights
None beyond the paper's own contributions. The two-step synthesis of semi-supervised uncertainty-aware attribute classification with selective fairness enforcement is the paper's own intellectual contribution.

## Suggestions

1. **Calibrate the headline claim.** Replace "outperform models trained with fairness constraints on the true sensitive attributes in most benchmarks" in the abstract and introduction with a precise statement: e.g., "achieve competitive or better fairness-accuracy tradeoffs than using true sensitive attributes on several benchmarks, particularly on ΔEOP/ΔEOD metrics." This would be both accurate and compelling.

2. **Clarify the operating point selection rule for single-point tables** (Tables 1–2). State the precise criterion used (e.g., "the λ that achieves minimal ΔEOD while maintaining accuracy within 2% of the no-fairness baseline") or replace the tables with a tradeoff summary metric (e.g., area under Pareto curve, unfairness at a fixed accuracy). The Pareto curves are already strong — the tables should not undercut them.

3. **Report the consistency-loss threshold R** for each dataset (initial value, final value after Gaussian warmup, or range searched) to ensure full reproducibility of the attribute-classifier training.

4. **Explicitly state the joint-label validation set requirement** in the problem setting section, acknowledging that tuning H requires a small held-out set with (X, Y, A).

5. **Add a brief decision rule for variant selection.** A paragraph or small table summarizing when to use FairDSR (certain) vs. (weighted) vs. (uncertain) would increase practical utility.
