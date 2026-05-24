Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper investigates how to approach language model pre-training under fixed data and unlimited compute — a regime the authors argue will become increasingly relevant as compute grows faster than web text. The key insight is to evaluate recipes by the asymptote of their scaling laws (as parameter count or ensemble size → ∞) rather than at a fixed compute budget. The paper shows that: (1) standard recipes of epoching and parameter scaling overfit under data constraints; (2) aggressively tuning weight decay (up to 30× larger than standard) enables monotone parameter scaling and yields a predictable loss asymptote; (3) ensembling independently trained models achieves a lower asymptote than parameter scaling alone; (4) composing both yields a joint asymptote equivalent to 5.17× data efficiency over the baseline at 200M tokens. The paper further shows these gains can be realized at smaller model sizes via distillation, and that validation loss improvements transfer to downstream benchmarks.

## Strengths

- **Novel and well-motivated framing**: The paper introduces a clean thought experiment — pre-training under fixed data and no compute constraints — and proposes evaluating recipes by their scaling law asymptotes. This is a genuinely useful conceptual tool that is more appropriate for the data-constrained regime than compute-optimal comparisons. The framing is clearly laid out in the introduction (Section 1) and consistently applied throughout.

- **Actionable finding on regularization**: The paper demonstrates that optimal weight decay for over-parameterized, data-constrained models is dramatically larger than standard practice (0.1 → 3.2 for the 1.4B model, a 30× increase; Section 3, Figure 3). This is a concrete, actionable result that practitioners can immediately apply. The finding that correctly tuned regularization enables monotone loss decrease proportional to ~1/N (exponent 1.02 vs Chinchilla's 0.34) is both surprising and well-supported by the experiments shown.

- **Ensemble scaling beats parameter scaling**: The paper provides compelling evidence that under a fixed total parameter budget, an ensemble of small models (scaling K) achieves a lower loss asymptote than a single large model (scaling N), with the K=3 ensemble already surpassing the regularized recipe's asymptote (Section 4.2, Figure 4). This contradicts conventional wisdom from some theoretical models and is a genuinely interesting empirical finding. The connection to multi-view theory (Allen-Zhu & Li, 2023) provides a plausible explanatory mechanism.

- **Validation loss improvements transfer to downstream benchmarks**: Holding out all benchmark evaluations until after recipe selection, the paper shows a consistent monotonic relationship between validation loss and downstream error, with the best ensemble achieving 9% lower average error than the unregularized baseline across PIQA, SciQ, and ARC Easy (Section 7, Figure 9). This validates the loss-asymptote metric as a proxy for real capability improvements.

- **Well-structured and clearly written**: The paper follows a logical progression from standard recipe → regularized recipe → ensemble recipe → joint scaling → data scaling → distillation → downstream tasks. The abstract and Figure 1 provide an excellent high-level summary of the entire argument.

## Weaknesses

### Major

- **Quantitative claims rest on nested extrapolations without out-of-sample validation**: The headline 5.17× data efficiency figure is the endpoint of a chain of power-law fits: asymptotes from K-laws (5 points per law) are fed into N-laws (4 points), whose asymptotes are fed into D-laws (4 points). No experiment directly validates any of these predictions — e.g., training a standard-recipe model on the predicted amount of additional data and showing its loss matches the forecast. The paper acknowledges the laws are "expected to be noisy" (Section 5.3) and reports ±0.02 asymptote variance from run-to-run noise (footnote 2), but does not propagate this uncertainty through the nested chain nor report confidence intervals for the final efficiency ratios. This makes the precise numerical claims (2.29×, 3.03×, 5.17×) difficult to trust at face value. The qualitative direction (regularization and ensembling improve data efficiency) is well-supported; the specific multipliers are not.

- **Distillation experiments lack a data-quantity control**: In both ensemble distillation (Section 6.1) and self-distillation (Section 6.2), the student is trained on a mixture of the original D tokens and D′ synthetic tokens from the teacher. The paper does not specify D′ in the main text, nor does it include a control where the student is trained on D tokens plus an equivalent amount of synthetic tokens from a weaker source (e.g., a noised or untuned model). This means the observed improvement cannot be cleanly attributed to knowledge transfer from the teacher — it could be partly or entirely due to the student seeing more total training tokens. The claim that distillation "preserves 83% of the ensemble gain" and the interpretation of self-distillation as beneficial are therefore confounded. For a paper centered on data efficiency, this gap is particularly salient.

### Minor

- **Scale of experiments limits the scope of conclusions**: All primary experiments use 200M–1.6B tokens and models ≤1.4B parameters, which are small by contemporary pre-training standards. The paper acknowledges this and uses data-scaling law extrapolation to argue that gains persist (Section 5.3), but the extrapolations themselves are fit on only four token counts (200M → 1.6B). The paper would be stronger with even a single mid-scale validation point (e.g., a regularized model at 10B tokens). That said, the paper is a proof-of-concept study and does not claim to be at production scale; the framework itself is scale-agnostic.

- **Joint scaling hyperparameters are heuristic**: The procedure for the joint scaling recipe (Section 4.3) uses a heuristic of "2× epochs and 0.5× weight decay" relative to the optimal regularized hyperparameters, rather than a full coordinate descent search. The paper is transparent about this being a heuristic, but the sensitivity of the final joint asymptote to this choice is not examined.

- **Baseline could be stronger**: The standard recipe baseline tunes epoch count and learning rate but uses the default weight decay of 0.1. This makes the regularized recipe's improvement a combination of weight decay tuning and epoch tuning. The paper is upfront about this (Section 3 explicitly states the default 0.1), but an additional baseline that also tunes weight decay at standard scales would sharpen the claim that aggressive weight decay specifically is the key intervention.

### Trivial

- The main text defers several important experimental details to the appendix (e.g., "details in Appendix F" for distillation, "full details in Appendix B" for training). Some of these — particularly the distillation token count D′ — belong in the main text given their centrality to the claims.

## Nice-to-Haves

- Directly validating one asymptote-based prediction by training a standard-recipe model on the claimed equivalent data amount and comparing losses would substantially strengthen the framework's credibility.
- Reporting bootstrap confidence intervals or propagated uncertainty for the data-efficiency ratios would replace point estimates with informative ranges.
- Varying the ratio of real to synthetic tokens in the distillation experiments would clarify the relative contributions of extra data vs. knowledge transfer.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's mention of "Appendix I.1, not available for review"**: Removed per hard rules — the parser strips appendices; they exist in the original submission. The paper does reference this sensitivity analysis in footnote 2.
- **Harsh critic's concern about "run-to-run variance of ±0.02" being comparable to the gap between regularized (3.43) and ensemble (3.34) asymptotes**: The gap is 0.09, which is more than 4× the reported ±0.02 variance. This specific comparison was overstated. However, the broader point about uncertainty not being propagated through nested fits remains valid.
- **Harsh critic's general concerns about "could the metric be measuring a proxy?" or "are confounders controlled?"**: These are area-of-concern sweeps without specific anchors in the paper. Removed.
- **Strength Finder's generic strength about "the paper addresses an important problem"**: This is superficial. The problem framing is indeed good, but this alone is not a concrete strength. The specific framing innovations are already captured in the first strength.
- **Strength Finder claiming distillation findings as unqualified strengths**: The distillation findings are real but are qualified by the missing control. The relevant strength has been qualified in the review.

## Novel Insights

The paper's central insight — that under fixed data and unlimited compute, recipes should be compared by the asymptote of their scaling laws rather than at a fixed compute budget — is genuinely novel and useful. It reframes the comparison of training algorithms in a way that is well-suited to the data-constrained regime. The empirical finding that ensemble scaling can achieve a lower asymptote than parameter scaling, even under a fixed total parameter budget, challenges the assumption (common in both theoretical and empirical work) that a single large model is always preferable. The demonstration that self-distillation with a mixture of real and synthetic tokens can outperform the teacher model is also noteworthy, as it contradicts the recent narrative around model collapse from self-generated data.

## Suggestions

- Add at least one direct validation of the scaling-law predictions: for a single data scale, train a standard-recipe model on the claimed equivalent data amount and compare.
- Report the synthetic token count D′ for distillation experiments in the main text, and include a control that uses non-teacher synthetic tokens to isolate the knowledge-transfer effect.
- Propagate uncertainty from the individual power-law fits through the nested chain to produce confidence intervals for the data-efficiency ratios, rather than presenting them as point estimates.

## Score and Decision

**Originality**: The framing of asymptote-based comparison under infinite compute and the specific findings (aggressive weight decay, ensemble > parameter scaling) are novel. **Importance**: The research question is timely given projections about data vs. compute growth. **Claims supported**: Qualitative claims are well-supported; quantitative claims (precise efficiency multipliers) outrun the evidence. **Soundness**: Core methodology (controlled experiments with tuned hyperparameters) is sound; extrapolation chain and distillation controls are weaker. **Clarity**: Well-written and logically structured. **Value to community**: The framework and qualitative findings are likely to influence how researchers think about data-constrained pre-training, even if the precise numbers should be treated as preliminary.

**Round 1 bracket**: 4.5–6.5. The paper is clearly above the rejected anchors at 4.5 (single environment, train loss only) and 5.20 (lacking novelty), but below the accepted 8.0 anchor (465+ runs, validated predictions) and the accepted 6.50 anchor (104 models, out-of-sample validation).

**Round 2 narrowing**: Compared to anchor `7rzA6aEASo` (5.60, "No Free Lunch from Random Feature Ensembles"), our paper is stronger: it has more novel findings (ensembles beat single models, the opposite conclusion), better empirical validation, and clearer practical takeaways. Compared to `iZeQBqJamf` (6.50, "Language models scale reliably with over-training"), our paper is weaker: it lacks out-of-sample validation of predictions and operates at smaller scale, though it has a more creative framing. The paper sits between these two but closer to the 6.50 anchor in terms of contribution quality, held back primarily by the unvalidated quantitative claims.

**Final score**: 6.0 — a solid contribution with a creative framework and interesting findings, but the quantitative claims need more grounding before they can be taken as established results. Accept.

**Anchor summary**:
- `iZeQBqJamf` (6.50, round 1): Similar scaling-law methodology but with out-of-sample validation and larger scale. Our paper is weaker on validation rigor.
- `xGM5shdGJD` (5.20, round 1): "Hitchhiker's Guide to Scaling Law Estimation" — meta-study of scaling law fitting. Our paper is more novel.
- `D0XpSucS3l` (4.50, round 1): Scaling laws for agents, single environment, train loss. Our paper is substantially stronger.
- `wg1PCg3CUP` (8.00, round 1): "Scaling Laws for Precision" — 465 runs, validated predictions, extensive. Our paper is clearly weaker.
- `7rzA6aEASo` (5.60, round 2): "No Free Lunch from Random Feature Ensembles" — opposite finding (single model beats ensembles). Our paper is more novel and empirically richer.
- `54KcduuYeG` (5.50, round 2): "AutoScale" — similar extrapolation concerns, less novel framing. Our paper is comparable or slightly stronger.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>