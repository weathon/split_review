Now I have thoroughly read the paper and all calibration anchors. Let me synthesize my final review.

---

## Summary

This paper studies pre-training under fixed data and unlimited compute, a regime motivated by the observation that compute grows much faster than available web text. The key contributions are: (1) showing that properly tuned weight decay (up to 30× larger than standard practice) restores monotonic scaling in parameter count under data constraints, (2) proposing the asymptote of a scaling law as the metric for comparing recipes under infinite compute, and (3) demonstrating that ensembling independently trained models, and composing ensembling with parameter scaling, achieves lower loss asymptotes than scaling a single model alone, yielding a 5.17× data efficiency improvement at 200M tokens. The paper further shows these gains persist across token scales, can be compressed into smaller models via distillation, and transfer to downstream benchmarks.

## Strengths

- **Novel evaluation framework**: The asymptote-based metric for evaluating data-constrained pre-training recipes under infinite compute is a genuinely new framing. It unifies regularization, ensembling, and parameter scaling under a single comparative framework and shifts evaluation from "performance at fixed compute" to "best possible performance given unlimited compute." This is clearly motivated and applied consistently throughout Sections 3–5.

- **Careful hyperparameter tuning vindicates the approach**: The coordinate descent search for locally optimal hyperparameters at each parameter count (Appendix C.1) is methodical and well-documented. Appendix C.2 convincingly demonstrates that naive hyperparameter transfer across scales produces misleading conclusions, justifying the tuning cost.

- **Heavy weight decay restores clean power-law scaling**: The finding that tuning weight decay to values 30× standard practice (Figures 3, 11, 12) eliminates overfitting and produces a monotone power law \(L \propto N^{-1.02}\) for models up to 140× Chinchilla-optimal is clearly shown and well-supported by both the main experiments and the extrapolation test in Appendix K.3.2 (predicting 1.5B and 3.2B model losses with errors of 0.005 and 0.008).

- **Ensembling beats parameter scaling, and they compose**: The demonstration that ensembling achieves a lower asymptote than parameter scaling alone (Figure 4) and that joint scaling composes the benefits (Figure 5) is an interesting and non-obvious finding. The connection to the multi-view theory of Allen-Zhu & Li (2023) provides plausible mechanistic intuition.

- **Transparent about limitations**: The paper is notably honest about uncertainty. Appendix I.1 acknowledges the asymptote estimation is "quite noisy" and advises readers to interpret the numbers "with a grain of salt." The data-scaling conclusions are appropriately hedged as "preliminary analysis" (Section 5.3).

- **Rebuttal additions significantly strengthen the paper**: The extrapolation test (K.3.2), goodness-of-fit table (K.3.1), additional benchmarks (K.4), new model sizes with fixed aspect ratios (K.1), and the continued pre-training experiment (Appendix A) address many concerns that would otherwise have been weaknesses.

## Weaknesses

### Fatal

None. The core claims are supported; the paper does not have errors that invalidate its contributions.

### Major

- **Small number of data points limits confidence in asymptote estimates**: The parameter scaling laws are fit to only 4 model sizes (150M–1.4B), and the ensemble scaling laws use only 5 member counts (K up to 5 or 8). While the extrapolation test in Appendix K.3.2 provides some validation (predicting 1.5B and 3.2B model losses), the three-tier fitting procedure for joint scaling (Figure 7) compounds uncertainty across nested extrapolations. The difference between the joint scaling asymptote (3.17) and the regularized asymptote (3.43) is 0.26, which is substantially larger than the reported seed-to-seed variance of 0.02, so the qualitative ranking likely holds, but the precision of the claimed 5.17× data efficiency multiplier should not be taken literally. The paper already acknowledges this in Appendix I.1, but the main text could be more explicit about the compounding uncertainty.

- **Narrow downstream evaluation limits claims about generalization**: The downstream evaluation uses only 3 benchmarks (PIQA, SciQ, ARC Easy) that are known to be relatively easy and may saturate quickly. The rebuttal adds 4 more (ARC-Challenge, HellaSwag, LAMBADA, Winogrande), which helps, but the total set remains limited for models at 150M–1.4B scale. While the correlation between validation loss and downstream accuracy is clear (Figure 9 / Figure 22), stronger evidence that the asymptote improvements translate to meaningful capability gains would require a broader benchmark suite.

### Minor

- **Baseline recipe limited to weight decay regularization**: The standard recipe uses only weight decay (tuned or default 0.1) and does not compare against dropout, stochastic depth, or data augmentation. While weight decay is the dominant regularizer in modern LM pre-training and the paper's core insight is about weight decay specifically, a single dropout baseline would strengthen the claim that heavy weight decay is the key intervention rather than just one of several effective regularization strategies. This does not undermine the paper's main findings—the regularized recipe clearly outperforms the standard one—but it limits claims about the uniqueness of weight decay as the solution.

- **Data-scaling law extrapolations are preliminary**: The four token counts (200M–1.6B) span only an 8× range, and the paper's claim that data efficiency improvements "will persist at higher token counts" (Section 5.3) relies on asymptotic statistics arguments (equal fitted asymptotes ~1.9 and exponents ~0.23–0.24). The paper appropriately hedges this as "preliminary analysis," but readers should not overinterpret the 5.17× multiplier as a guaranteed constant.

### Trivial

- The ensemble hyperparameter heuristic (2× epochs, 0.5× weight decay) is empirically motivated but one counter-example is reported for the 1.4B/200M setting (Appendix D.4), which the paper handles correctly by using the actual best run. No action needed.

## Nice-to-Haves

- Comparison against at least one alternative regularizer (e.g., dropout) to contextualize the weight decay findings.
- Uncertainty bands on the power-law fit figures in the main text.
- Analysis of ensemble member diversity (output disagreement, weight subspace overlap) to strengthen the multi-view argument beyond a literature citation.
- Test at larger token counts (e.g., 6.4B) with at least one model size to validate data-scaling law extrapolations.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

**From the harsh critic:**

1. **"No cross-validation against held-out scales, no goodness-of-fit diagnostics"** — REMOVED. The rebuttal update (Appendix K.3) provides both: R² values above 0.999 for all main scaling laws (K.3.1) and an extrapolation test predicting 1.5B and 3.2B model losses with errors of 0.005 and 0.008 (K.3.2). This criticism is factually incorrect after the rebuttal.

2. **"The asymptote estimates rest on unvalidated extrapolations from very few data points"** — PARTIALLY REMOVED / REWRITTEN. The paper explicitly acknowledges this in Appendix I.1: "We note that this is a limited stress-test and that it is likely our asymptote estimation procedure is quite noisy... We advise taking these asymptotes with a grain of salt." The criticism is recharacterized as a major weakness about limited data points rather than absent validation.

3. **"The claim that the exponent of 1.02 is 'high' relative to Chinchilla's 0.34 is misleading"** — REMOVED. The paper explicitly notes the contexts differ (data-constrained vs. compute-constrained) and provides an explanation: "This suggests that when we better leverage the data, there is faster improvement from larger models." This is a reasonable interpretation, not misleading.

4. **"The heuristic for tuning ensemble hyperparameters is not justified theoretically"** — REMOVED. The paper never claims theoretical justification; it explicitly calls it a "heuristic" and provides empirical validation in Appendix D.4 across multiple parameter counts.

5. **"The baseline standard recipe is not representative of reasonable practice"** demand for dropout, stochastic depth, etc. — PARTIALLY REWRITTEN. Weight decay is the standard regularizer in LM pre-training, and the paper's contribution is about weight decay specifically. Moved to minor weakness rather than the structural issue the harsh critic claimed.

6. **"The two-tier and three-tier scaling law fitting compounds uncertainty... the resulting number (3.17) likely has an error bar large enough to overlap with the regularized asymptote (3.43)"** — WEAKENED. The harsh critic speculates about error bars without evidence. The paper's sensitivity analysis shows asymptote variance of ~0.02, which is much smaller than the 0.26 gap between 3.17 and 3.43.

7. **"Distillation results muddy data efficiency interpretation because synthetic data adds tokens"** — REMOVED. The paper is studying infinite compute; generating synthetic data is a legitimate way to leverage compute. The data amounts are disclosed in Appendix F. This is scope creep.

8. **"The claim of a '9% improvement' inflates perceived benefit"** — REMOVED. The paper reports both absolute and relative numbers clearly in Appendix G. The 9% relative error reduction is standard reporting practice.

9. **"The continued pre-training experiment appears to be a late addition with limited analysis"** — REMOVED. This is a supplementary experiment in the appendix and is analyzed appropriately for its scope (Table 1, Appendix A).

10. **Formatting/style nitpicks about figures, table formatting, typos** — REMOVED per hard rules.

**From the Strength Finder (dropped):**

- None. All identified strengths are concrete, cite specific sections/figures, and are verified against the paper.

## Novel Insights

Beyond the paper's contributions, a genuinely novel methodological insight emerges from the reviews: the asymptote-based evaluation framework is a natural complement to the standard compute-constrained paradigm, and its logic—comparing recipes by their best-possible rather than compute-normalized performance—could apply to other resource-constrained ML settings (e.g., data-constrained fine-tuning, limited-expert-demonstration RL). The paper's transparency about the inherent uncertainty in asymptote estimation (Appendix I.1) also serves as a useful cautionary note for future work adopting this framework.

## Suggestions

- Move the extrapolation test (Appendix K.3.2) and R² table (K.3.1) into the main body or a prominently referenced appendix section. These directly address the most natural criticism of the work and should not be buried in rebuttal materials.
- Add a brief discussion in Section 5.3 about the limitations of data-scaling law extrapolation from 4 token counts, similar to the honesty shown in Appendix I.1.
- Include a single dropout baseline at one parameter count (e.g., 300M) to contextualize the weight decay findings.

## Calibration Anchors

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| Unified Neural Scaling Laws | `dnuIoVjeGR.md` | 3.00 (Reject) | That paper proposed an overly expressive scaling law without theoretical motivation and had limited validation. Our paper has a clearer contribution, better empirical grounding, and is more transparent about limitations. Significantly stronger. |
| From Acceleration to Saturation | `nrVbL1CK1A.md` | 4.00 (Reject) | Both study scaling phenomena at modest scale (1.1B vs 1.4B max params). That paper has a narrower finding (saturation effect) with limited mechanistic explanation. Our paper has a broader set of interventions (regularization, ensembling, distillation) composing into a coherent framework. Clearly stronger. |
| Model Merging Scaling Laws | `vpKXTmMtBQ.md` | 5.50 (Reject) | Similar topic (model combination scaling laws), but that paper is more descriptive with less novel framing. Our paper's asymptote-based evaluation framework is more innovative. Comparable or slightly stronger. |
| Can Small Training Runs Reliably Guide Data Curation? | `2FZC0c06jP.md` | 6.50 (Accept) | Both identify a practical problem in standard methodology (fixed-HP proxies vs fixed weight decay) and propose a simple solution. That paper has stronger theoretical backing. Our paper has a more diverse set of interventions. Roughly comparable quality. |
| How to Train Data-Efficient LLMs | `yKUbw7q1IA.md` | 6.80 (Accept) | Both study data efficiency. That paper has more extensive experiments (22 data curation techniques, hundreds of runs) and larger scales. Our paper has a more novel conceptual framing (asymptote-based evaluation). Slightly weaker on experimental breadth but comparable on contribution novelty. |
| The Art of Scaling RL Compute for LLMs | `FMjeC9Msws.md` | 7.50 (Oral) | Both propose frameworks for evaluating scaling under a particular resource regime (RL compute vs data-constrained). That paper has 400K GPU-hours, a systematic ablation of design choices, and clear actionable recipes. Our paper is smaller-scale and more preliminary. Noticeably weaker. |

The paper sits in the 6.0–6.5 range. It has a genuinely novel framing, well-executed experiments at its scale, and important transparency about limitations. The limited downstream evaluation, small number of data points for asymptote estimation, and narrow baseline comparison prevent it from reaching the 7+ range. Relative to the anchors, it is clearly stronger than the 3.0–4.0 papers, comparable to the 6.5 paper but slightly weaker on experimental breadth, and noticeably below the 7.5 oral.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>