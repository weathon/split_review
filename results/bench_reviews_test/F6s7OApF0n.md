## Summary
The paper introduces CMBO, a cost-sensitive multi-fidelity Bayesian optimization framework that explicitly maximizes a user-specified utility function trading off cumulative cost against validation performance. Its three components are: (i) a utility-based EI acquisition that picks both a configuration and a future epoch Δt to maximize utility improvement, (ii) a stopping criterion that smoothly interpolates regret-based and PI-based termination via a Beta-CDF, and (iii) a transfer-learned PFN learning-curve extrapolator trained with a two-step LC mixup. CMBO is evaluated on LCBench, TaskSet, PD1, and a self-collected RoboFlow100 LC dataset.

## Strengths
- The reframing of multi-fidelity BO around a user-specified utility (instead of an a-priori fixed budget) is a clean and underexplored operationalization. Eq. (2) is a sensible utility-EI that also chooses Δt jointly with the configuration, and Fig. 7a/b empirically demonstrate the intended behavior — Δt shrinks as the BO progresses and ground-truth regret of the chosen configuration is lower than baselines.
- The Beta-CDF interpolation between regret-based and PI-based stopping (Eqs. 3–5) is a tidy unification with two interpretable extremes; Fig. 7d confirms the interior optimum exists.
- The two-step LC mixup (across datasets first to preserve inter-configuration correlations, then across configurations) is a simple and well-motivated augmentation for PFN training, and Fig. 6 supports it on PD1.
- Ablation in Table 3 isolates the three components and shows monotone improvement under PD1.

## Weaknesses

### Fatal
None.

### Major
- **Headline metric is the same utility CMBO uniquely optimizes.** Tables 1, 2, and 4 report normalized regret of *U*. Eq. (2) is the EI of *U*, while baselines (DyHPO, iFBO, FSBO, DPL, BOHB, DEHB) are run unmodified against last-epoch validation performance with no knowledge of *U* or α. Any α > 0 therefore gives CMBO a structural advantage independent of surrogate quality, dynamic Δt, transfer learning, or stopping. The α = 0 setting in Fig. 4 is the only apples-to-apples comparison and CMBO's edge there is much smaller (e.g., comparable to FSBO on LCBench). The central claim of "significantly outperforms all the previous multi-fidelity BO and transfer-BO baselines" is therefore not cleanly supported. A utility-aware wrapper around at least FSBO/iFBO/DyHPO (e.g., EI of *U* with their surrogates) is needed to credit the acquisition itself, as opposed to merely the objective gap.
- **The "Estimated utility" column in Table 2 is constructed from iFBO's own trajectory.** Section 4 / Table 2 caption: the estimated utility is built by assuming the user wants a better trade-off than iFBO. This makes iFBO a worst-case method against this column by construction and is therefore not evidence that CMBO would dominate under genuine user preferences. The "Estimated" column should be dropped or replaced with utilities elicited independently of any baseline.
- **Stopping-criterion mixing coefficient β tuned on the test benchmarks.** Footnote 2 grants CMBO an extra knob (β) that baselines are not allowed, and Fig. 7d — used to choose β = e⁻¹ — is a sweep over the same benchmarks the method is then evaluated on. The stopping-criterion contribution cannot be cleanly attributed without selecting β on a held-out split (or CV across benchmarks).

### Minor
- **Utility-elicitation experiment is a parametric sanity check, not validation of practitioner usability.** Fig. 2 fits a utility from synthetic preferences sampled from a known parametric utility. The motivating premise — that real users can specify *U* more easily than budgets — is not directly tested. A small user study, even with a handful of practitioners, would substantively support the framing.
- **Variance reporting is suspicious.** Tables 1, 2, and 4 contain many ±0.0 entries across heterogeneous methods (e.g., FSBO, Quick-Tune†, several CMBO cells). With 5 seeds, stochastic acquisition optimization, and PFN inference, this likely reflects rounding to one decimal that obscures real variance, and combined with no significance testing it makes "significantly outperforms" language hard to evaluate when several rows differ by a tenth of a point.
- **Mixup ablation is single-benchmark.** Fig. 6 is on PD1 only. Given mixup is credited as the largest single contributor (per the strength claim and Table 3), an ablation on at least one other benchmark would be convincing.
- **PD1 preprocessing alters the LC distribution PFNs were trained on.** Excluding diverged configurations and linearly interpolating LCs to length 50 is a non-trivial intervention; the effect on transfer is not measured.
- **Algorithm 1, line 4** reads `n* ← argmax_{n∈C} A(n)` with C the set of partial LCs. As written, this excludes never-selected configurations from the selection. The text suggests new configurations should be admissible; the notation should clarify whether C is the partial-LC history or the candidate set, since these read inconsistently.

### Trivial
- Cost-sensitive HPO and BO-with-user-preferences — central to the framing — are deferred to §A. The body of §2 would benefit from at least a paragraph contextualizing CMBO against prior cost-aware BO.
- Fig. 5 caption acknowledges "cherry-picked examples"; per-task aggregates (deferred to §H) should be the headline.
- §5 has no limitations / threats-to-validity discussion; the objective-mismatch issue in particular deserves explicit acknowledgement.

## Nice-to-Haves
- Pareto plots of (best validation performance vs. cumulative cost) per method per task — these are the cost-sensitive comparison the paper actually wants and are agnostic to any choice of *U*.
- Decompose CMBO's gain into (a) utility-aware acquisition, (b) dynamic Δt, (c) PI-augmented stopping, (d) mixup transfer, on more than one benchmark.
- A small utility-elicitation study (5–10 practitioners) on real HPO preferences would strongly substantiate the motivating story.

## Removed Points
*These points were flagged and dropped/weakened from the main review; treat with caution.*
- "Quick-Tune† materially modified" — the paper explicitly explains the modification (their setup does not include pretrained model selection or non-uniform wall-times) and marks the method with †. This is a transparent and reasonable adaptation, not a misrepresentation.
- "Two iFBO rows in Table 1 with different citations (Kadav 2023 / Kadavourian 2024) confuse DPL and iFBO" — almost certainly a citation/parser rendering artifact; the body text consistently distinguishes DPL (Kadra 2023) from iFBO (Rakotoarison 2024). Removed under the no-typo/parser rule.
- "Object-detection dataset has architecture-level leakage" — only a 17-LC/task concern; with 30 tasks split 20/10 across architecture×dataset combinations and meta-train/meta-test split documented, the concern is plausible but not clearly demonstrated. Worth a sentence rather than a major point.
- Generic "missing related work" / "appendix-deferred details" complaints — removed per hard rules.

## Novel Insights
None beyond the paper's own contributions. The reviewers correctly identify that the utility-aware framing simultaneously makes the proposed method natural to construct and difficult to evaluate fairly against utility-agnostic baselines — that tension is the central methodological observation the authors should engage with explicitly.

## Suggestions
- Wrap at least FSBO/iFBO/DyHPO with an EI-of-*U* acquisition to isolate the contribution of CMBO's acquisition from objective mismatch.
- Promote α = 0 results to the main experiments and report per-task mean ± std with paired significance tests; do not round σ to one decimal.
- Tune β on a held-out split or via leave-one-benchmark-out CV; report sensitivity rather than picking the test-set optimum.
- Add at least one cross-benchmark mixup ablation.
- Add a small real user-preference study, even informal, to ground the Bradley–Terry pipeline.
- Add a Limitations section acknowledging the objective-mismatch issue and the synthetic nature of the Bradley–Terry recovery experiment.

## Calibration

Anchors retrieved (all from `calibration_search`):
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/SA19ijj44B.md — avg 7.33 (BNN surrogates for BO; high). Stronger empirical rigor and a more disciplined evaluation; CMBO is below this bar.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/1jcnvghayD.md — avg 7.25 (continual VLL BNN BO; high). Cleaner empirical case than CMBO.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/YhfrKB3Ah7.md — avg 7.40 (PABBO preferential amortized BO; high). Closest in spirit (preferences in BO) but with much tighter evaluation.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/wPStvOAtjR.md — avg 5.25 (LAMDA two-phase multi-fidelity HPO; mid). Comparable scope and contribution density to CMBO; strong topical anchor.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/fLWqIWPMDH.md — avg 5.25 (memoization-aware cost-aware BO; mid). Very close topical match; cost-aware BO with similar borderline reception.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/vq8BCZYAdj.md — avg 5.20 (multi-fidelity symbolic optimization; mid). Topically adjacent multi-fidelity work in the same band.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/IiAckbuccF.md — avg 4.25 (nonmyopic BO in dynamic cost settings; low). Closest low anchor; CMBO has stronger empirical breadth and a more polished pipeline, so should sit above this.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/diKykN0Yaa.md — avg 3.00 (memory-pruning BO; low). Clearly weaker than CMBO; not a tight comparison.

CMBO has a genuinely novel framing, a sensible mechanism, and broad benchmark coverage, but the headline empirical claim is structurally inflated by the objective mismatch and the test-set β selection. That puts it firmly in the borderline cluster with fLWqIWPMDH/wPStvOAtjR (~5.25) rather than the 7-tier or the 4-tier.

## Score and Decision
MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>