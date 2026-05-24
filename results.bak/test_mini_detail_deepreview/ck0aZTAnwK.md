Now I have enough calibration data. Let me synthesize the final review.

**Initial bracket (Round 1):** 5.5 – 7.0

**Round 2 narrowing:** Compared against anchors:
- "Language models scale reliably..." (6.5, accepted) — similar scaling law methodology, comparable quality
- "Scaling Law with LR Annealing" (6.75, rejected) — had theoretical flaws; this paper is sounder
- "Data Contamination" (6.75, rejected) — mixed reviews, comparable methodological concerns
- "No Free Lunch from Ensembles" (5.6, rejected) — directly topical, but the current paper's empirical findings are richer and more surprising
- "Hitchhiker's Guide" (5.2, rejected) — weaker; this paper has a clearer contribution

The paper sits around 6.0 — a solid paper with genuine contributions, above acceptance threshold, but the uncertainty quantification gap keeps it from the 7+ range.

---

## Summary

This paper studies pre-training under fixed data and abundant compute. It shows that (1) standard recipes overfit under data constraints, (2) increasing weight decay by 30× over standard practice yields monotonic parameter scaling, (3) ensembling many small models achieves a lower loss asymptote than scaling a single large model, and (4) distillation can compress most ensemble gains into smaller models. The central methodological contribution is evaluating recipes by their loss asymptote (as parameter count or ensemble size → ∞) rather than by performance at a fixed compute budget. The headline quantitative result is 5.17× data efficiency at 200M tokens for the joint scaling recipe.

## Strengths

- **Discovery that optimal weight decay is 30× larger than standard practice under data constraints:** The paper shows that jointly tuning weight decay (up to 3.2 vs. standard 0.1), learning rate, and epoch count produces monotone power-law scaling in parameter count for models up to 140× the Chinchilla ratio (Figure 3, Section 3). This is a clear, empirically grounded finding that directly challenges current practice.

- **Ensemble scaling beats parameter scaling and the two compose:** Ensembles of 300M models reach a lower asymptote (3.34) than the regularized single-model asymptote (3.43) at the same total parameter count, with a crossover visible at moderate ensemble sizes (Figure 4). The joint scaling recipe (taking both N,K → ∞) achieves asymptote 3.17, demonstrating that better algorithms can leverage extra compute for data efficiency (Section 4).

- **Data efficiency gains persist across token scales:** Data scaling laws fitted at 200M–1.6B tokens show similar exponents (0.23–0.24) across all recipes, implying the relative gains are approximately constant factors as data increases — the improvements are not artifacts of the smallest token budget (Section 5.3).

- **Distillation preserves most ensemble gains in smaller models:** Distilling an 8-ensemble of 300M models into a 300M student retains 83% of the ensemble's loss improvement over the regularized 300M model and beats the regularized recipe's asymptote (Figure 8, Section 6). This validates practical applicability.

- **Validation loss improvements transfer to downstream benchmarks:** The best ensemble outperforms the best unregularized model by 9% on average across PIQA, SciQ, and ARC Easy, and validation loss ordering matches downstream error ordering for all recipes (Figure 9, Section 7).

## Weaknesses

### Major

- **No uncertainty quantification on the headline numbers.** The paper's central quantitative claims — the 5.17× data efficiency factor, the joint scaling asymptote of 3.17 — are obtained by stacking power-law fits: first fitting loss vs. parameter count (4 points → asymptote), then for ensembles fitting loss vs. ensemble size (up to 5 members → asymptote → fit vs. parameter count → double-limit asymptote), then fitting those asymptotes vs. token count (4 data points). Each fit has few degrees of freedom. The paper provides a sensitivity analysis for one level (±0.02 loss over 3 seeds, line 117–118) but does not propagate uncertainty through the multi-step chain. Without confidence intervals or a bootstrap analysis, the reader cannot assess whether the 5.17× figure is robust or could be, say, 3× or 8× under plausible variation. This is the paper's most significant evidential gap.

### Minor

- **Ensemble hyperparameters use heuristics, not optimized tuning.** The joint scaling recipe (Section 4.3) uses heuristic hyperparameters (2× epochs, 0.5× weight decay of the regularized recipe) rather than a full search. The paper acknowledges this (line 147) and notes that "slightly overfitting each ensemble member" can improve performance (line 151). This means the ensemble scaling law and the joint asymptote are estimates of a particular operationalization, not necessarily the best possible. The paper's core qualitative finding (ensembles beat parameter scaling) is robust, but the exact numerical asymptote for the joint recipe has this additional source of uncertainty.

- **Distillation procedure is underspecified.** The paper uses unconditional generation to produce synthetic distillation data (Section 6.1) but provides no details on generation temperature, number of synthetic tokens, mixture ratio of real to synthetic data, or filtering. The self-distillation result is surprising (a 300M student matching the regularized asymptote) and the community would benefit from a fully specified procedure. (This is a presentation gap rather than an evidential one, as the paper's main claims do not depend on distillation.)

- **The 9% downstream improvement is not explicitly defined.** The paper says the best ensemble outperforms the best unregularized model "by over 9% on average" (Section 7) but does not state whether this is relative accuracy improvement or relative error reduction. From Figure 9, it appears to be relative error reduction; this should be stated explicitly.

- **Power-law fits rely on few data points.** Parameter scaling laws use 4 points (150M–1.4B), ensemble scaling uses 4 points (K=1,2,3,5), and data scaling laws use 4 token budgets (200M–1.6B). While this is consistent with the scaling law literature, the exponents (especially the parameter exponent of 1.02, which is much larger than Chinchilla's 0.34) carry high uncertainty. The paper notes this exponent is large but does not quantify its sensitivity.

- **Baseline selection affects the headline factor magnitude.** The 5.17× figure compares the joint scaling recipe against a baseline with fixed weight decay 0.1. The paper transparently reports 2.29× for the regularized recipe alone (which tunes weight decay). A significant fraction of the total improvement comes from tuning weight decay, and the abstract could more clearly separate these contributions rather than leading with the combined 5.17× number.

### Trivial

None.

## Nice-to-Haves

- A bootstrap or leave-one-out analysis propagating uncertainty through the full power-law chain would substantially strengthen the paper's evidential standing.
- A single experiment tuning ensemble member hyperparameters for a 300M ensemble of size 3 would show whether the ensemble scaling law shifts when optimized for the ensemble objective.
- A brief discussion of how the results relate to "No Free Lunch from Random Feature Ensembles" (which found K=1 optimal under fixed total parameters) would help contextualize why the data-constrained + abundant compute setting reverses this conventional wisdom.

## Removed Points

1. **"Epoch search limited to powers of two"** — This is standard practice in scaling law experiments and is not a weakness.
2. **"Missing related work"** — Cannot be verified without external knowledge; removed per instructions.
3. **Formatting/style nitpicks** — Removed per instructions.
4. **Criticism about baseline selection inflating improvement claims (strong version)** — The paper is fully transparent about the breakdown and explicitly reports the 2.29× regularized improvement. The critic's claim that "55% comes from simply tuning weight decay" is a derived number that the paper does not hide. Demoted to Minor.
5. **Generic "reproducibility concerns" about unreleased models/datasets** — The paper cites existing, known entities (DCLM, etc.) and states it will open-source code and WandB logs (Section 12).

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper's strongest conceptual finding — that ensemble scaling beats parameter scaling — is strikingly at odds with the "No Free Lunch from Random Feature Ensembles" result (K=1 optimal) from the theoretical literature. The key difference appears to be the data-constrained (repeated data) vs. fresh-data regime: when data is fixed and repeated, models overfit to different features, creating the "multi-view" diversity that makes ensembling effective. This suggests a more general principle: the relative value of ensembling vs. parameter scaling depends critically on whether data or compute is the binding constraint. The paper's empirical demonstration that regularization (high weight decay) is the enabling condition for monotonic parameter scaling under data constraints is also underappreciated in the current scaling law literature, which typically studies compute-optimal or data-rich settings.

## Suggestions

1. **Quantify uncertainty on the 5.17× figure** — Even a simple bootstrap over the power-law fits (resample residuals and re-fit) would give the reader a sense of how tight the estimate is. This is the single change that would most improve the paper.
2. **Optimize ensemble hyperparameters for at least one setting** — Show that the ensemble scaling law does not change directionally when hyperparameters are tuned for the ensemble objective rather than inherited from the single-model recipe.
3. **Clarify the 9% metric** — State explicitly whether it is relative error reduction or relative accuracy improvement.
4. **Specify the distillation data generation procedure** — Add temperature, synthetic token count, and real/synthetic mixture ratio to the main text.

## Score and Decision

**Calibration summary:**

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7LZjuA4AB2.md` | 3.00 | 1 | Weak anchor: pre-training for distribution shift, clearly below this paper |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XUzHegCq6f.md` | 3.00 | 1 | Weak anchor: parameter ensemble method, clearly below this paper |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/D0XpSucS3l.md` | 4.50 | 1 | Middle anchor: scaling laws for agents/world models, less well-executed than this paper |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iZeQBqJamf.md` | 6.50 | 1 | Strong middle anchor: over-training scaling laws, accepted. Similar execution quality, slightly narrower scope. This paper is comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xGM5shdGJD.md` | 5.20 | 1 | Middle anchor: scaling law estimation guide, rejected (mixed reviews). This paper has a clearer contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vPOMTkmSiu.md` | 6.60 | 1 | Strong middle anchor: downstream scaling laws for MT, accepted. Comparable execution quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wg1PCg3CUP.md` | 8.00 | 1 | Strong anchor: scaling laws for precision, extremely well-executed. This paper is clearly below. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/o9YC0B6P2m.md` | 6.75 | 2 | Narrowing anchor: scaling law with LR annealing, rejected due to theoretical flaws. This paper is sounder. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7rzA6aEASo.md` | 5.60 | 2 | Narrowing anchor: ensembles vs single models (random features), rejected. Directly topical; this paper has richer empirical findings. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` | 6.75 | 2 | Narrowing anchor: data contamination, rejected. Comparable methodological concerns but this paper has stronger novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Kb1bIuGuax.md` | 4.75 | 2 | Narrowing anchor: weight decay bias, rejected. This paper's empirical scope is broader. |

**Round 1 bracket:** The paper sits between the weak anchors (2–3) and strong anchors (7.5–8). The plausible range is [5.5, 7.0].

**Round 2 narrowing:** The paper is comparable to the accepted "Language models scale reliably with over-training" (6.5) — both are scaling law papers with clear contributions and methodological limitations. It is stronger than the rejected "Hitchhiker's Guide" (5.2) and "No Free Lunch from Ensembles" (5.6). It is weaker than the top-tier "Scaling Laws for Precision" (8.0). Within the bracket, the paper sits closest to the 6.0–6.5 range.

**Final score: 6.0.** The paper makes genuine contributions (asymptote evaluation framework, demonstration that ensembles beat parameter scaling under data constraints, 30× higher optimal weight decay). The experiments are internally consistent and the qualitative findings are robust. However, the lack of uncertainty propagation on the headline 5.17× figure, the heuristic ensemble hyperparameters, and the underspecified distillation procedure prevent it from reaching the 7+ tier. The paper is clearly above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>