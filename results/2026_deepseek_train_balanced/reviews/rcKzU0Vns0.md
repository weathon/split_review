## Summary

This paper proposes SISOM, a method that uses enriched feature-space distance ratios (blending inner-to-outer class distances with an energy score) to address both active learning and out-of-distribution detection within a single framework. The method computes gradient-weighted feature representations via KL-divergence, defines a distance ratio relative to nearest same-class and different-class samples, and dynamically combines this ratio with an energy score based on feature-space separability. SISOM achieves top-1 accuracy on three AL benchmarks (CIFAR-10, CIFAR-100, SVHN) and strong near-OOD detection performance across OpenOOD benchmarks.

## Strengths

- **First explicit joint design for AL and OOD detection, backed by evidence that naive migration fails.** The paper is the first to design a method for both tasks, and demonstrates that NAC (a strong OOD detector) underperforms random selection in AL (line 323), while CoreSet (an AL method) ranks near the bottom on OOD benchmarks (e.g., 75.69 near-OOD AUROC on CIFAR-100, Table 3). This validates the non-triviality of the unification.

- **Consistently top-tier near-OOD detection across three OpenOOD benchmarks.** SISOM-EN achieves 91.76 near-OOD AUROC on CIFAR-10 (1st), 78.59 on ImageNet (1st), and 80.96 on CIFAR-100 (2nd). It is the only method in the top three for near-OOD across all three benchmarks, demonstrating robustness that no single baseline (ASH, NAC, KNN, GEN) achieves — each of those ranks last on at least one benchmark (lines 468–469).

- **Top-1 active learning performance on three diverse datasets.** SISOM achieves the highest final accuracy on CIFAR-10, CIFAR-100, and SVHN, outperforming CoreSet, Badge, Loss Learning, and Random selection (Figs. 2, 3, 4). On CIFAR-100, it overtakes diversity-based methods in later cycles (line 351), showing scalability to larger class counts.

- **Adaptive r_avg mechanism for blending distance and energy scores.** The method computes r_avg (Eq. 8) as a data-dependent proxy for feature-space separability and uses it to dynamically weight between the distance ratio and the energy score (Eq. 9). This is a principled way to handle datasets where latent space quality varies. The mechanism is validated: on CIFAR-100, where energy (80.91) outperforms the pure distance ratio (79.42), the combined SISOM-EN (80.96) surpasses both (Table 3).

- **Qualitative t-SNE validation of the decision-boundary targeting claim.** Figure 6 compares SISOM, CoreSet, and Loss Learning on SVHN after one AL cycle, showing that SISOM simultaneously covers decision boundaries and unexplored regions — directly confirming the method's design principle translates into observable behavior.

- **Reduced subset selection for computational efficiency.** The method selects a representative 10% subset via class-wise ProbCover to avoid full pairwise distance computation. The ablation (Table 4) shows this maintains or slightly improves performance while cutting computational cost.

## Weaknesses

### Major

- **OOD ranking claims are selectively reported.** The abstract and conclusion state "first place in two of the widely used OpenOOD benchmarks and second place in the remaining one" (lines 8, 526). This is misleading: SISOM-EN is 1st on CIFAR-10 (both near and far OOD) and 1st on ImageNet *near-OOD*, but on ImageNet *far-OOD* it ranks 9th (89.04 vs. ASH's 95.74, Table 1), and on CIFAR-100 *far-OOD* it ranks 6th (79.80 vs. NAC's 86.56, Table 3). The paper prioritizes near-OOD rankings (justified in lines 470–471 by citing OpenOOD's view that near-OOD is "the more challenging task"), but neither the abstract nor the conclusion qualifies the claim accordingly. A reader would reasonably infer overall benchmark leadership, which the far-OOD results do not support. This is not fatal — the near-OOD consistency is real — but the presentation overstates.

- **Energy + distance ratio combination (Eq. 7) mixes potentially incompatible scales without normalization.** The score $\hat{r}_i = \min(r_{avg}, 1) \cdot E_i + \max(1 - r_{avg}, 0) \cdot r_i$ (line 246) linearly combines the energy score $E(x) = -\log\sum\exp(f(x)_i)$ (unbounded above, can be large in magnitude) with the distance ratio $r_i = d_{in}/d_{out}$ (a quotient of Euclidean distances in [0,∞) but typically bounded in practice). The scalar weights $\min(r_{avg},1)$ and $\max(1-r_{avg},0)$ are ratios, not normalization constants. The paper provides no analysis showing the two components have comparable scales in practice or that one component does not dominate simply due to magnitude differences. The empirical success of SISOM-EN is legitimate, but the mechanism is unexplained, and the claimed advantage rests on results that could emerge from one component dominating.

- **"Unified" framing overreaches relative to the evaluation.** The paper claims a "unified solution for both AL and OOD detection" (line 6) and states the method "effectively addresses open-world applications" requiring both tasks concurrently (lines 27–28, 527). Yet AL and OOD are evaluated in completely separate pipelines: AL experiments train models from scratch per cycle (Sec. 5.1), while OOD experiments use fixed OpenOOD checkpoints (line 358). There is no experiment that trains a model via SISOM-based AL and then evaluates its OOD detection performance, nor any demonstration of synergy or compatibility in a real pipeline. The paper itself acknowledges this: "In future work, we plan to combine the two tasks that are currently separated as independent steps" (line 529). The contribution — a shared score function that works well for both tasks evaluated independently — is real, but the "unified" and "open-world application" framing implies a stronger integration than is demonstrated. A more measured framing would better match the evidence.

### Minor

- **No statistical rigor for AL experiments.** The figures state "indicated standard errors" (captions of Figs. 2, 3, 4) but the paper provides no information about the number of independent runs, random seeds, or whether differences between SISOM and the runner-up are statistically significant. Given that some margins are visually small (e.g., SVHN in Fig. 3 — "a narrow margin," line 340), this information is needed to assess whether the claimed advantages are robust.

- **Pseudo-label usage for OOD scoring is ambiguous.** The distance ratio $r = d_{in}/d_{out}$ (Eq. 6) requires a predicted class $c$ for computing $d_{in}$. For AL, pseudo-labels are clearly used (line 166). For OOD detection, it is ambiguous whether the model's prediction on potentially OOD inputs is used as the "pseudo-class" — applying nearest-class reasoning to OOD inputs could be problematic if the model confidently misclassifies OOD samples. The paper should clarify whether this step differs between the two tasks.

- **No computational cost comparison.** SISOM involves gradient computation per sample (backward pass for KL divergence), multi-layer feature concatenation, and pairwise distance computations. A comparison of runtime and memory relative to baselines (e.g., Energy and MSP, which are nearly free) would be needed to assess practical deployability, especially for the large-scale settings the paper targets.

### Trivial

- None.

## Nice-to-Haves

- A unified pipeline experiment: train a model through AL cycles using SISOM's selection strategy, then evaluate its OOD detection performance vs. other strategies. This would directly substantiate the "unified" framing.
- Analysis of when and why the energy+ratio combination helps, e.g., controlled experiments on datasets with deliberately degraded feature separation.
- Report the specific layers selected for concatenation in Eq. 2 and the ProbCover radius used for reduced subset selection.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- **"CoreGCN is listed but never referenced in results":** Removed — the figure legends (which would show included methods) are not text-readable, so this claim cannot be verified from the paper as written. The method is listed among baselines (line 276), and lack of an explicit textual mention in results does not constitute a flaw.
- **"NAC is never referenced in AL results":** Factually incorrect — line 323 explicitly states "NAC does not show a better performance than Random."
- **Missing BALD / MC Dropout baselines:** Scope creep — the included baselines (CoreSet, Badge, Loss Learning, CoreGCN) are standard for the setting.
- **Missing hyperparameters relegated to appendix:** The parser strips appendix content from all papers; these exist in the original submission per venue policy.
- **Reproducibility concerns about undisclosed trivial implementation details:** Standard for this venue's page limits.
- **Formatting/style nitpicks:** Parser artifacts, not author errors.
- **Missing related works:** Cannot be verified without external sources.
- **General speculation about confounders without concrete anchor in the paper:** Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Recalibrate the OOD claims.** Either qualify them as "near-OOD" in the abstract and conclusion, or report an aggregated ranking (e.g., average rank across near and far OOD) to give a more complete picture.
2. **Add a unified pipeline experiment** that trains a model through AL cycles with SISOM selection and then evaluates its OOD detection, even if preliminary. This would transform the "unified" claim from conceptual to demonstrated.
3. **Report the number of AL runs and significance tests** for the figures shown with error bars.
4. **Include a brief analysis of the relative scale of the energy score vs. the distance ratio** in the combination (Eq. 7), or add a normalization step to the combined score.
5. **Clarify the pseudo-label handling** for OOD detection in Section 4.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>