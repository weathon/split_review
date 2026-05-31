Now let me run the calibration searches in parallel with Round 1 bracketing:**Round 1 bracket: 5.5 – 8.0**

Now Round 2, narrowing within this bracket:Now I have sufficient information to write the final review. Let me synthesize everything.

---

## Summary

This paper studies pre-training under data constraints and unlimited compute, proposing a new evaluation framework centered on the *asymptote* of a scaling law as the metric for "infinite-compute performance." The authors demonstrate that (1) careful regularization — specifically 30× larger weight decay than standard practice — enables monotone power-law scaling in parameter count, yielding an asymptote of 3.43 on DCLM; (2) ensembling independently-trained models achieves a lower asymptote (3.34) than parameter scaling alone; and (3) composing both approaches (the "joint scaling recipe") produces an asymptote of 3.17, estimated to be 5.17× more data-efficient than the baseline. Distillation is shown to recover most ensemble gains at smaller inference-time model sizes, and all improvements transfer to three downstream benchmarks.

---

## Strengths

- **Regularization unlocks monotone scaling (Section 3, Figure 3):** The joint coordinate-descent search over weight decay, learning rate, and epoch count reveals that optimal weight decay is 0.8–3.2 — 30× larger than the GPT-3 default of 0.1. This simple insight converts the non-monotone standard recipe into a clean power law fit ($\hat{\mathcal{L}} = 0.05/N^{1.02} + 3.43$), making asymptote estimation possible. The result is directly actionable and well-supported empirically.

- **Ensemble scaling outperforms single-model scaling under infinite compute (Section 4.2, Figure 4):** The paper demonstrates that ensembles of 300M models achieve a lower asymptote (3.34) than regularized single-model scaling (3.43), with both following approximately 1/K and 1/N decay rates. Notably, even a K=3 ensemble outperforms the regularized recipe's asymptote — a concrete and meaningful finding.

- **Data scaling laws show persistent efficiency gains across token counts (Section 5, Figure 7):** The paper validates that the 5× data efficiency advantage appears at 200M, 400M, 800M, and 1.6B tokens, with similar power-law exponents (0.23–0.24) across all recipes. This multi-scale corroboration strengthens confidence that the observed gains are structural rather than specific to a single scale.

- **Distillation compresses gains into smaller models (Section 6, Figure 8):** Distilling an 8-ensemble of 300M models into a single 300M student retains 83% of the ensemble's loss improvement (student: 3.36 vs. teacher ensemble: 3.32 vs. regularized baseline: 3.57), outperforming the regularized recipe asymptote. The self-distillation result (300M teacher → 300M student matching the regularized asymptote without increasing peak parameter count) is practically significant.

- **Held-out benchmark evaluation design (Section 7):** The authors explicitly state that no downstream benchmark evaluation was performed until after recipe selection based on validation loss. This commendable design prevents data dredging and makes the 9% improvement on PIQA, SciQ, and ARC Easy a genuine out-of-sample test.

---

## Weaknesses

### Fatal
None.

### Major

- **Confidence intervals absent from asymptote estimates — the central metric of the paper.** The framework's entire argument rests on comparing asymptotes: 3.43 (regularized) vs. 3.34 (ensemble) vs. 3.17 (joint). The key ensemble vs. regularized gap is only 0.09 loss. The paper reports seed-run sensitivity of ±0.02 in footnote 2, but this characterizes run-to-run variance, not fitting uncertainty from the four-point power law fits themselves. Bootstrapped confidence intervals on the extrapolated asymptote — the natural complement to the seed analysis already in the appendix — are absent. Without them, it is impossible for readers to judge whether the ordering {3.17 < 3.34 < 3.43} is statistically robust rather than a plausible but uncertain extrapolation. This matters most for the joint scaling recipe, where the 3.17 estimate involves three nested extrapolations (K→∞ per N, then N→∞, then read off the asymptote). Given that the paper's framework is explicitly built on comparing these asymptotes, presenting confidence intervals here is not optional rigor — it is the minimum needed to support the claimed ordering.

- **The headline 5.17× data efficiency figure rests on an acknowledged hyperparameter heuristic.** Section 4.3 explicitly states: "we cannot fully find locally optimal hyperparameters due to experimental constraints. Instead, we use the heuristic of taking the optimal regularized hyperparameters with 2× epochs and 0.5× weight decay." This means the joint scaling recipe's 3.17 asymptote is the output of a heuristic rather than a locally-optimal recipe, making it either an upper bound or a lower bound depending on whether the heuristic overshoots or undershoots. There is no ablation showing how sensitive the joint scaling asymptote is to this 2×/0.5× choice, and no theoretical justification for why this correction is approximately optimal. The most prominently advertised result in the paper (5.17×) is therefore its least reliable.

### Minor

- **Theoretical motivation for ensembling is invoked but not grounded in the setting.** Section 4.2 cites Allen-Zhu and Li (2023)'s multi-view framework to explain why ensembling outperforms single-model scaling, but the connection to language model pre-training on web text is asserted rather than demonstrated. It is not self-evident that web text has the "multi-view" structure required by that theory. A brief argument connecting web text diversity to the multi-view assumption — or an explicit acknowledgment that this is speculative — would strengthen the theoretical narrative.

- **The overfitting ensemble member result is buried.** Footnote 3 and Appendix D.2 note that ensemble members should be *slightly* overfitting to achieve the best asymptote, rather than using the same hyperparameters optimal for the regularized single-model recipe. This is a counterintuitive and interesting finding that has direct implications for the design of ensembles under data constraints. It deserves at least a paragraph in the main text, as it is a nontrivial design choice that affects reproducibility of the ensemble results.

- **Downstream evaluation uses only three benchmarks.** The paper correctly notes (Section 7) that PIQA, SciQ, and ARC Easy are the informative accuracy benchmarks for models at this scale per Thrush et al. (2025). This justification is reasonable, but readers should be aware that the 9% figure averages over a very small set of tasks and may not generalize beyond classification-style tasks.

### Trivial
None.

---

## Nice-to-Haves

- A brief discussion of the token-to-parameter ratio at which the regularization findings begin to apply would help practitioners assess whether their own settings are "data-constrained" in the paper's sense. The models studied run at up to 140× Chinchilla over-parameterization; at what ratio should practitioners start increasing weight decay?

- A direct empirical data efficiency measurement at the largest observed scale (1.6B tokens) across recipes — without asymptote extrapolation — would provide a concrete anchor for the scaling law predictions in Section 5. Section 5.2 mentions that the best ensemble of five 1.4B models is itself 3.75× more data efficient without asymptote extrapolation; surfacing a similar number for each recipe in Figure 7 would add reassurance.

- A short grid search around the 2×/0.5× heuristic at a single (N, K) configuration would bound how suboptimal the heuristic is and could convert the headline result from "lower bound on joint scaling performance" to "approximately optimal joint scaling performance."

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Scale mismatch with production pre-training.** The critic argues that the paper's regime (200M–1.6B tokens) is irrelevant to trillion-token pre-training where overfitting is rare. This is scope creep — the paper explicitly studies the data-constrained regime (compute >> data) and does not claim relevance beyond it. Removed.

- **Strength Finder: "Important problem" as a standalone strength.** Statements that the problem is important without pointing to specific experimental evidence are generic. The concrete evidence (Figure 3, Figure 7, Figure 8) was retained; the abstract importance framing was merged into the summary.

- **Harsh Critic: Missing goodness-of-fit statistics (R², residuals) for power law fits.** The paper fits clean power laws with visually good agreement (Figures 3, 4, 5); the absence of R² is standard in scaling-law papers of this type and is not flagged by reviewers in comparable works. Demoted to at most a trivial presentation issue, not a substantive concern. Removed as a weakness.

---

## Novel Insights

The paper's most conceptually distinctive contribution is the *asymptote as an evaluation metric*, which reorients scaling law research from "best model at a fixed compute budget" to "best achievable model with unlimited compute on fixed data." This framing reveals that the Chinchilla-optimal framework and the data-constrained framework call for fundamentally different recipes: the former rewards data-parameter balance, while the latter rewards aggressive regularization and ensemble diversity. The finding that optimal weight decay scales with over-parameterization (from 0.1 at Chinchilla-optimal to 3.2 at 140× Chinchilla), combined with the ensemble-beats-single-large-model result, suggests that classical statistical learning insights about bias-variance tradeoff remain powerful tools in the modern large-model regime when the framing is right. The self-distillation result — that a 300M model distilling from its own outputs matches the regularized recipe's asymptote — provides a low-overhead path to data efficiency that requires no increase in peak parameter count, which is operationally significant.

---

## Suggestions

1. **Add bootstrapped confidence intervals to all reported asymptotes**, especially the 3.34 vs. 3.43 comparison (gap = 0.09) and the 3.17 joint scaling estimate. This is the minimum needed to make the asymptote-ordering argument credible.

2. **Ablate the 2×/0.5× heuristic for the joint scaling recipe** at at least one (N, K) point. Even a 3×3 grid search around this heuristic would bound the suboptimality and substantially strengthen the headline claim.

3. **Elevate the "slightly overfitting ensemble members" finding** from a footnote/appendix to a short main-text paragraph with a figure. This is a counterintuitive and practically relevant result.

4. **Provide guidance on when regularization scaling applies** by including a brief discussion of token-to-parameter ratio thresholds (e.g., ">10× Chinchilla" or similar) so practitioners can quickly assess relevance to their own settings.

---

## Score and Decision

**Anchor Comparisons:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `wg1PCg3CUP.md` (Scaling Laws for Precision) | 8.00 | R1 | Similar in rigor/scope; that paper fits 465 runs vs. 4 points per law here — gives it an edge |
| `07yvxWDSla.md` (Synthetic continued pretraining) | 8.00 | R1 | Also data-constrained; similarly clean results but narrower scope (domain-specific) |
| `iZeQBqJamf.md` (LMs scale with over-training) | 6.50 | R2 | Very close topic; this paper has more novel contributions (asymptote framework, ensemble) and broader scope — clearly above |
| `FDnZFpHmU4.md` (Determine-Then-Ensemble) | 7.50 | R2 | Ensemble focus, inference setting; less related conceptually |
| `xGM5shdGJD.md` (Hitchhiker's Guide to Scaling Laws) | 5.20 | R1 | Scaling law estimation meta-study; this paper is more principled and action-oriented |
| `wFD16gwpze.md` (Neural Scaling Laws in Two-Layer Networks) | 7.33 | R2 | Theoretical scaling laws; not empirical pre-training |
| `BDisxnHzRL.md` (Scaling Laws for Downstream Performance) | 4.25 | R1 | Weaker paper, downstream prediction only |
| `T2h2V7Rx7q.md` (Multilingual Scaling Laws) | 5.25 | R1 | Narrower multilingual scope |

**Round 1 bracket:** 5.5 – 8.0

**Round 2 narrowing:** The paper is clearly stronger than "LMs scale with over-training" (6.5) — it introduces the asymptote framework and demonstrates ensemble scaling as a practical tool, while that paper primarily validates existing scaling law forms in an over-training regime. The paper approaches but doesn't quite reach "Scaling Laws for Precision" (8.0), which fits 465 training runs and is fully validated without acknowledged heuristics in its headline result. The two major weaknesses (absent confidence intervals on the asymptote, headline figure from heuristic hyperparameters) are genuine limitations of the current submission, not speculative concerns. Final score: **7.0**, reflecting a solid, genuinely novel contribution that is ready for acceptance but would be strengthened substantially by addressing the asymptote uncertainty issue.

**Axis evaluation:**
- **Originality:** High — the asymptote-as-metric framework, the 30× weight decay finding, and the ensemble-beats-large-model result are all novel.
- **Importance of research question:** High — data constraints are increasingly binding; this is a timely and underexplored problem.
- **Claim support:** Moderate-high — regularization and ensemble results are well-supported; joint scaling recipe's headline number rests on an acknowledged heuristic with no ablation.
- **Soundness of experiments:** Moderate-high — coordinate descent tuning is careful; power law fits from 4 points are standard but thin; benchmark holdout is commendable.
- **Clarity of writing:** High — the paper is well-structured and clearly presents the three-stage framework.
- **Value to research community:** High — the regularization finding is immediately actionable; the ensemble scaling insight opens new research directions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>