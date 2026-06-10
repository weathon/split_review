Now I have the full picture. Let me construct the consolidated review.

## Summary

The paper proposes Cond-FiP, an amortized approach for zero-shot inference of Structural Causal Models (SCMs) from observations and causal graphs. It extends the FiP fixed-point framework (Scetbon et al., 2024) by conditioning on dataset embeddings produced by a transformer encoder, enabling a single model to infer functional mechanisms across diverse SCMs without per-dataset training. Experiments show competitive performance with per-dataset methods (FiP, DoWhy, DECI) on noise prediction, sample generation, and interventional generation, including generalization to larger graphs and out-of-distribution settings.

## Strengths

- **Zero-shot SCM inference is achieved and validated across multiple tasks**: Tables 1–3 systematically demonstrate that Cond-FiP matches or beats per-dataset baselines without any test-time training. The most striking result is on non-linear OOD settings (ROUT, d=50, Table 1), where Cond-FiP achieves RMSE 0.14 vs. FiP's 0.23, DoWhy's 0.29, and DECI's 0.29 — a notable case where the amortized model outperforms methods trained from scratch on each dataset.

- **Generalization to larger graphs (d=50, d=100) despite training only on d=20**: The shaded rows in all three tables show that Cond-FiP, trained exclusively on 20-node graphs, maintains competitive or superior performance at 50 and 100 nodes (e.g., Table 1, d=100 RIN: Cond-FiP 0.10 vs. FiP 0.16, DoWhy 0.20). This is genuine extrapolation to unseen problem sizes that per-dataset methods cannot match.

- **Zero-shot interventional generation without explicit training on interventional data**: As stated at line 263, Cond-FiP "never explicitly trained for interventional tasks" yet achieves competitive results in Table 3 (e.g., d=10 LOUT: 0.07 vs. DoWhy 0.05, FiP 0.07). This provides evidence that the learned functional mechanisms capture the true causal structure rather than merely memorizing observational mappings.

- **Robustness across distribution shifts**: Cond-FiP generalizes to the C-Suite simulator (different SCM configurations than training) and to OOD settings where graph distribution, noise distribution, and parameter ranges all shift simultaneously (Pout). The large-scale pre-training on ~4 million SCMs with diverse topologies (Erdős–Rényi, scale-free, Watts–Strogatz, stochastic block models) and function classes (linear, RFF) provides a credible basis for this robustness.

## Weaknesses

### Fatal
None.

### Major

1. **No evaluation with imperfect/predicted causal graphs — a critical gap between the paper's framing and practical applicability.** The method requires the true causal graph as input at test time. The paper acknowledges this (lines 120–121) and briefly gestures at amortized structure learning methods as a solution, but this is not substantiated by any experiment. Causal discovery from observations is itself an open challenge, and errors in the estimated graph would propagate through Cond-FiP in unpredictable ways. The paper never evaluates this scenario — not even a simple sensitivity analysis with corrupted graphs or graphs predicted by an amortized structure learner. Since the entire method hinges on having the correct graph, this substantially limits the practical contribution. The claimed framing of "zero-shot SCM inference from observations" (abstract, line 12) is imprecise: the method infers SCMs from observations *and given causal graphs*. While the contributions section (line 44) correctly states "given their causal graphs," the abstract and introduction's broader framing could mislead readers about the method's end-to-end capabilities.

2. **The two-stage training pipeline is a significant design choice that is never interrogated.** The encoder is first trained to predict functional evaluations at observed points (via MSE on F(x) = x - n), producing dataset embeddings via max-pooling. The decoder (Cond-FiP) is then trained separately using these frozen embeddings. The encoder's objective (point-wise prediction of F(x) at observed points) is not identical to the decoder's objective (learning the full function z → F(z) over the entire space). Representations that are good for point-wise prediction may not be optimal for function reconstruction, but this mismatch is never discussed, and no end-to-end variant (where decoder gradients flow back to the encoder) is ablated. Given that the encoder embeddings are the sole conduit of dataset information into Cond-FiP, this design choice could silently limit performance, and the paper provides no analysis of this.

### Minor

3. **Performance pattern is uneven across settings but presented as uniformly "on par".** Cond-FiP systematically underperforms on linear settings (Table 1, LIN: 0.06 vs. DoWhy's 0.03 and FiP's 0.04 across all graph sizes) while outperforming on non-linear OOD (ROUT). The paper states results as "on par" and "competitive" without analyzing this pattern. A more informative stance would be to explain why amortization helps on non-linear OOD (e.g., regularization from diverse training functions) but hurts on simple linear settings where per-dataset methods can fit more tightly.

4. **No runtime or computational cost comparison.** The core motivation for amortization is to avoid per-dataset training. Yet the paper provides no wall-clock time or FLOPs comparison between Cond-FiP inference (forward pass through two transformer models) and per-dataset training of FiP, DoWhy, or DECI. Without this, the practical benefit of amortization is asserted but not quantified.

5. **Small test set sizes for statistical confidence.** Each experimental cell uses only 6–9 SCMs per condition (line 208), totaling 120 test datasets. The reported standard errors reflect variation across SCMs rather than repeated samples, making it difficult to assess whether observed differences between methods are statistically reliable, especially for the smaller effect sizes.

6. **Design choices are not ablated or justified.** The paper uses max-pooling over the sample dimension for dataset embeddings (line 133) without comparing to mean-pooling or attention-based aggregation. The adaptive layer normalization design (line 146) is not evaluated against alternatives (concatenation, cross-attention). These are non-trivial architectural decisions that constitute the method's claimed novelty. While the paper references ablations in an appendix, the main paper itself contains zero analysis of these choices.

7. **No dedicated limitations section.** The paper has no candid discussion of its known limitations (reliance on known graphs, restriction to ANMs, synthetic training distribution, two-stage design). A limitations section would strengthen credibility and help readers understand the method's scope.

### Trivial

8. **C-Suite results (Figure 1) rely on a figure whose y-axis scale is difficult to read.** The caption notes "The y-axis denotes the RMSE" but no numerical scale is clearly visible. A table with numerical values would be more informative.

## Nice-to-Haves

- A runtime comparison (Cond-FiP inference time vs. per-dataset FiP training time) would concretely quantify the amortization benefit.
- An end-to-end training ablation (gradients from decoder loss flowing to encoder) would clarify whether the two-stage design is optimal or if joint training improves results.
- A sensitivity analysis with corrupted or predicted graphs would directly address the most significant practical limitation.
- Including at least one numerical ablation (e.g., max-pooling vs. mean-pooling) in the main paper rather than the appendix would strengthen the presentation.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Real-world experiment should be in main paper**: The paper references a real-world experiment in the appendix (line 262). The appendix exists in the original submission; this is a presentation choice, not a missing experiment.
- **Pre-training advantage of ~4e6 SCMs not acknowledged**: This is inherent to amortized learning — the whole point of pre-training is to enable zero-shot inference. The paper transparently describes the training scale.
- **Several "missing analyses"** (e.g., when Cond-FiP fails, sensitivity to training SCM count): These request additional experiments beyond reasonable scope for a single paper.
- **Encoder training clarity (line 105)**: The paper states the objective clearly enough; the critic's confusion is resolvable upon re-reading.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an experiment with predicted/corrupted graphs to address the most significant practical limitation. Even if performance degrades, quantifying the degradation would be valuable.
2. Report wall-clock inference time for Cond-FiP vs. per-dataset training time for FiP to quantify the amortization benefit.
3. Add a brief analysis of the performance pattern across settings (why Cond-FiP lags on linear but excels on non-linear OOD).
4. Include at least one ablation of a key design choice (e.g., max-pooling vs. mean-pooling) in the main text.
5. Add a limitations paragraph in the conclusion or discussion.
6. Provide numerical values for the C-Suite results rather than relying solely on the figure.
7. Clarify the abstract's framing to consistently state that the method requires causal graphs as input, not observations alone.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Weak Accept</decision>