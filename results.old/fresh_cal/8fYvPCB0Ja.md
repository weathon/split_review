Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper introduces FairDD, the first framework to incorporate protected-attribute (PA) fairness into dataset distillation. It identifies that vanilla DDs fail to mitigate and actually amplify PA bias present in original datasets, and proposes a simple fix: replace the single distribution-matching target (which is dominated by the majority group) with synchronized matching to all PA-wise group centers. This reformulation (Eq. 5) removes the sample-ratio weighting that causes bias, and Theorem 4.2 shows that the new objective upper-bounds the vanilla one under convex distances, so optimizing FairDD maintains target-attribute coverage. Experiments across four DD methods (DM, DC, IDC, DREAM) and six datasets show dramatic fairness improvements (e.g., C-MNIST FG IPC=10: DEO_M drops from 100 to 17) while simultaneously improving accuracy.

## Strengths

1. **Theoretical guarantee of bias removal.** Theorem 4.1 proves that under MAE/MSE distance, FairDD's optimal synthetic signal is the arithmetic mean of all PA-group expectations — independent of group sample ratios — directly countering the ratio-weighted convergence of vanilla DDs (Eq. 3). This is a clean, formal argument that the core idea works at the signal level.

2. **Large, consistent fairness gains across multiple DD paradigms.** Table 1 shows that FairDD reduces DEO_M from near‑100 (vanilla DM, DC, IDC, DREAM) to values ranging from ~6–33 across five synthetic-bias datasets and CelebA. The improvement holds for both Distribution Matching and Gradient Matching methods, demonstrating versatility.

3. **Accuracy does not degrade and often improves substantially.** Table 2 shows that FairDD raises accuracy far above vanilla DDs (e.g., C-MNIST FG IPC=10: DM 25.01 → 94.61 with FairDD). This counters the typical fairness-accuracy trade-off and supports the claim that FairDD improves coverage of the full distribution.

4. **Robustness to varying bias severity and initialization.** Table 4 (ablation on biased ratio 0.85–0.95) shows vanilla DM's DEO_M jumps from 70 to 100 as bias increases, while FairDD stays ≈10 across all settings. Table 5 shows FairDD is far less sensitive to synthetic-image initialization than vanilla DM.

5. **Cross-architecture generalization.** Table 3 shows that synthetic data distilled with FairDD (on ConvNet) transfers its fairness properties to AlexNet, VGG11, and ResNet18 with nearly identical DEO values (e.g., C-MNIST FG: DEO_M ≈ 9–10 across all architectures).

## Weaknesses

### Fatal
None.

### Major

- **Missing group-balanced random sampling baseline.** The paper compares FairDD against *Random* (random sampling from the imbalanced original dataset) and against vanilla DDs. A natural baseline is a **group-balanced random subset**: for each class, sample an equal number of real images from each PA group (at the same total IPC). This would directly test whether the fairness improvements come from FairDD's synthetic generation process or simply from rebalancing the group distribution — an operation requiring no distillation. If a group-balanced random subset achieves comparable DEO values, FairDD's novelty is partly about accuracy maintenance rather than fairness innovation per se. If FairDD clearly dominates, the method's synthetic generation is confirmed as the key factor. This experiment is the most important missing piece for sharpening the paper's claims.

### Minor

- **No variance or standard deviation reported.** The paper reports only point estimates across all tables. Given the small IPC values (10, 50, 100) and the stochasticity in both distillation and training, reporting means without error bars weakens the statistical evidence. At least 3 runs with standard deviations should be reported for the main results.

- **Gap between theoretical optimality and practical optimization.** Theorem 4.1 characterizes the optimal synthetic signal under the assumption that the optimization reaches the optimum (a fixed-point analysis). The paper states this assumption (lines 96, 151) but does not empirically examine how close the actual synthetic images get to this theoretical ideal, or discuss the implications of non-convex optimization on the practical validity of the theorem. A simple empirical check (measuring achieved signal expectations vs. the theoretical optimum) would bridge this gap.

- **Computational overhead not discussed.** Computing expectations per PA group per class requires multiple forward passes per class (one per group). For 10 groups, this is roughly 10× the forward-pass cost of vanilla DD during distillation. The paper does not report runtime comparisons, which would inform practical use.

### Trivial

- None.

## Nice-to-Haves

- **Comparison to a simple in-processing fairness baseline** applied to vanilla DD (e.g., reweighting the distillation loss by inverse group frequency) could further isolate the benefit of the architectural design.
- **An additional real-world fairness dataset** (e.g., UTKFace, FairFace) would strengthen generality claims, though the current set (5 synthetic-bias + CelebA) is adequate for a first paper on this topic.

## Removed Points

These points were flagged by reviewers but are excluded from the main review for the following reasons:

- **"Adversarial Matching" in title is a misnomer.** The method uses synchronized matching, not adversarial training. This is a naming preference, not a substantive weakness — the paper clearly describes the method (synchronous matching to PA-group centers). Removed as a style/framing nitpick.
- **Missing related works** — The meta-reviewer cannot verify claims about missing references and should not speculate.
- **Theoretical analysis "less supportive than claimed"** — The paper explicitly states (lines 96, 151) that the analysis assumes the optimum is reachable. The assumption is transparently declared; this is standard practice for fixed-point analysis and does not misrepresent the theory.
- **Request for additional real-world dataset** — Scope creep for a first paper establishing a new subarea (fair DD). The paper already evaluates on 5 synthetic-bias datasets plus CelebA, which is reasonable.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for a cleaner disentanglement (group-balanced sampling baseline) but do not reveal a flaw or insight not already present in the paper.

## Suggestions

1. **Add a group-balanced random sampling baseline** (highest priority). For each class, sample IPC/|A| images from each PA group (handling remainders appropriately). Train on this subset and report fairness and accuracy alongside the current results. This will cleanly separate the effect of group-balancing from the effect of synthetic generation.
2. **Report standard deviations** over at least 3 independent distillation + training runs for all main tables (Tables 1, 2).
3. **Add a runtime comparison** between FairDD and vanilla DD for the same IPC to quantify the computational overhead.
4. **Include an empirical check** of Theorem 4.1: measure the achieved signal expectation of the synthetic data and compare it to the arithmetic mean of PA-group expectations.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>