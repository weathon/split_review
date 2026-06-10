## Summary

This paper presents a large-scale empirical study of data scaling laws in imitation learning for robotic manipulation. The authors collect over 40,000 demonstrations across four manipulation tasks using UMI hand-held grippers and train Diffusion Policies to study how generalization performance scales with the number of training environments, objects, and demonstrations. The key findings are that (1) generalization scales approximately as a power law with the number of environments/objects, (2) diversity of environments and objects matters far more than the absolute number of demonstrations per setting, and (3) a practical recipe of 32 environment–object pairs with 50 demonstrations each yields ~90% zero-shot success on unseen environments and objects, validated on two held-out tasks.

## Strengths

- **Large-scale empirical study with rigorous evaluation.** The paper collects >40k demonstrations and executes >15k real-world rollouts (Abstract, lines 4–5), testing exclusively on unseen environments/objects. The evaluation protocol uses a multi-point scoring system (0–3 per step) with simultaneous blinding across policies and identical initial conditions (Section 3, "Evaluation" paragraph, lines 94–95), enabling finer-grained comparisons than binary success/failure. This scale and rigor substantially surpass prior works (UMI, RUMs) that did not conduct systematic scaling studies.

- **Quantified power-law trends with correlation coefficients.** The paper provides log-log fits (Fig. 5, Section 4.2, lines 160–166) with reported correlation coefficients *r* for object, environment, and combined scaling curves. Unlike prior qualitative work in robotics, the paper explicitly fits *Y = βX^α* and reports fitted equations. The paper also honestly reports weak correlations for demonstration counts (*r* = −0.62 and −0.79; Fig. 5 caption, line 184), demonstrating intellectual integrity.

- **Empirically demonstrates that diversity dominates demonstration count.** Multiple experiments converge on this finding: in object generalization, the gap between 12.5% and 100% of demonstrations nearly disappears at 32 training objects (line 118); in environment generalization, 50% and 100% usage lines overlap (line 138); in the combined setting, 25% and 100% lines overlap (lines 146–148). This is a concrete, replicated result that prior work did not quantify.

- **Validated strategy on held-out tasks with practical efficiency.** The recommended strategy (32 env–object pairs, 50 demos per pair) is derived from Pour Water and Mouse Arrangement, then independently validated on two *new* tasks (Fold Towels, Unplug Charger) that were not used to derive the laws. Table 1 (lines 201–202) reports ~90% success rates with standard deviations across all four tasks, and the paper notes this required only one afternoon with four data collectors (line 213). This demonstrates both generalizability and practical utility.

- **Controlled model scaling experiments with actionable conclusions.** Section 7 (Tables 2–3, lines 250–271) provides controlled ablations showing: scaling the visual encoder (ViT-S/14 → ViT-L/14) yields consistent gains (0.66 → 0.90), scaling the action diffusion U-Net does *not* help (small: 0.88, large: 0.83), and both pre-training and full fine-tuning are essential (LoRA: 0.72 vs full: 0.90; frozen/scratch near zero). These provide concrete architectural guidance beyond the core data-scaling contribution.

## Weaknesses

### Major

- **No variance information for the scaling trend, making robustness unverifiable.** Each configuration (e.g., training with 4 randomly selected out of 32 objects) uses a **single random draw** of environments/objects/pairs and a **single training run** (lines 114–116, 136, 146). Without repeating the random subset selection (3–5 draws per configuration) or training with multiple seeds, the reported power-law trends could be artifacts of particular subset choices or training stochasticity. With only 6 data points per curve, a single "lucky" or "unlucky" draw at a given *m* could substantially shift the fitted exponent. The paper's central claim — that generalization follows a power law with environments/objects — lacks the evidential support that variance estimates would provide. This does not invalidate the practical findings (the verification experiment stands independently), but it weakens the "scaling law" claim considerably.

### Minor

- **The evaluation metric (tester-assigned score) lacks documented reliability.** The scoring system (3 points per step, normalized to [0,1]) is described without a detailed rubric distinguishing scores 1, 2, and 3 for each task (line 95). No inter-rater reliability is reported, and it is unclear whether multiple testers were used or whether the same tester scored all rollouts. This matters because the scaling curves (the paper's central quantitative evidence) rely entirely on these scores. The paper partially mitigates this by reporting success rates alongside normalized scores in the verification experiment (Table 1), and the two metrics correlate well — but success rates are not provided for the main scaling experiments (Figs. 3–5), so the subjective scores are the sole quantitative support for those trends.

- **The data collection strategy recommendation ("one unique object per environment") is derived from a single experimental configuration.** The heatmap experiment (Fig. 6) uses 16 environments with 4 objects each, and the conclusion that "as the number of environments increases (e.g., to 16), the performance gap... becomes negligible" (line 180) is based on one configuration without repetition or testing at larger *M*. The subsequent claim that "for large-scale data collection, where the number of environments typically exceeds 16" (line 180) is an assumption, not a tested finding. The strategy's ultimate success is validated on held-out tasks, which partially compensates, but the specific claim about the vanishing benefit of multiple objects per environment rests on thin evidence.

### Trivial

- Line 142 has a typo: "Generlization" → "Generalization".
- Line 136 has a typo: "vaild" → "valid".

## Nice-to-Haves

- Report success rates (alongside normalized scores) for the main scaling experiments (Figs. 3–5), not just for the verification table. This would ground the subjective scores in an interpretable metric.
- Provide inter-rater reliability for the scoring system, or use automated success detection where feasible.
- Describe the diversity of the 32 environments and 32 objects in more detail (e.g., what types of environments, how objects differ) so readers can assess generalization difficulty.
- Clarify the UMI-to-robot action space mapping and whether domain shift between the hand-held gripper and the evaluation robot is a concern.

## Removed Points

These were considered and removed with justification:

- **Criticism that "object generalization experiment does not measure what it claims"** (Harsh Critic, Point 3). *Removed* — The paper clearly separates three experimental conditions: object-only (same environment), environment-only (same object), and combined (both vary). The full "any object in any environment" claim is validated by the combined experiment (Section 4.1, third sub-section) and the verification section (Section 5), not by the object-only experiment alone. The paper is precise about what each experiment tests.
- **Criticism that the power-law claims are unsupported because the paper does not report p-values/confidence intervals.** *Partially demoted* — The lack of statistical significance testing is a real issue, but it is subsumed by the broader "no variance information" weakness above. The paper uses hedging language ("approximately," "roughly") throughout, and the r values for demonstration counts are frankly reported as weak. The core evidential gap is the absence of repeated draws, not the absence of a p-value.
- **Criticism about the introduction overclaiming scope.** *Removed* — The paper explicitly scopes itself to single-task policies, within a single object category, using one data collection method and one algorithm (line 16): "We do not consider task-level generalization at this stage."
- **Criticism that the model scaling section is too preliminary.** *Removed* — The paper explicitly calls this "preliminary explorations" (line 18) and the section title says "Beyond Data Scaling." The paper is appropriately modest about the scope of these experiments.
- **Criticism about the 1,191 prediction being speculative.** *Removed* — The paper explicitly says "We leave the verification of this prediction for future work" (line 166), showing appropriate caution.
- **Criticism about "one afternoon" conflating data collection time.** *Moved to Nice-to-Have* — Very minor qualification.

## Novel Insights

The most novel insight to emerge from this review — beyond the paper's own contributions — is the asymmetry between what the paper establishes convincingly and what it claims as its headline result. The paper's practical contribution (the verified data collection strategy yielding ~90% success with modest effort) is well-supported by the held-out verification and does not depend on the power-law framing. The "scaling law" claim, while plausible and visually suggestive, is the part of the paper most vulnerable to the core evidential weakness (no repeated random draws). This suggests the paper would be strongest if it presented the power-law fits as supporting observations for the practical strategy rather than as independent discoveries of equal weight.

## Suggestions

1. **Add repeated random draws** — For at least one representative experiment (e.g., environment-object pairs at 100% demonstrations), repeat the random subset selection 3–5 times per *m* and train each with 2–3 seeds. Report the variance as error bars or shaded regions on the log-log plots. If the trends survive this stress test, the scaling claim is significantly strengthened. If they do not, the paper should recalibrate its claims accordingly.

2. **Report success rates for the main scaling experiments** — Add a supplementary figure or table showing success rates (or a binarized version of the scoring metric) alongside normalized scores for Figs. 3–5. If the trends are similar, this substantially increases confidence in the metric.

3. **Document the evaluation rubric** — Provide a concrete description of what score 1, 2, and 3 mean for each step of each task, and report whether multiple testers were used with inter-rater agreement. This would make the evaluation reproducible and increase confidence in the quantitative results.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>