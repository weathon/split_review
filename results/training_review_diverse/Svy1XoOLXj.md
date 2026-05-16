Now I have all the information needed. Let me produce the final consolidated review.

## Summary

BiLoRA proposes a bi-level optimization framework for LoRA-style adapters: it parameterizes low-rank incremental matrices in a pseudo-SVD form and trains the pseudo singular vectors (lower level) and pseudo singular values (upper level) on disjoint data subsets. The paper motivates this by arguing that training all adapter parameters on a single dataset causes overfitting, and evaluates on 10 NLU/NLG datasets with RoBERTa, DeBERTa, and GPT-2 models.

## Strengths

- **Novel bilevel formulation for LoRA adapters.** The idea of separating pseudo singular vectors and values into two coupled optimization levels is a genuine departure from prior methods (LoRA, AdaLoRA) that train all adapter parameters jointly. The formulation is cleanly presented (Section 3.2) and the interdependence between levels is clearly specified.

- **Consistent empirical improvements across tasks, models, and settings.** BiLoRA outperforms LoRA and AdaLoRA on every single task reported: across RoBERTa-base/large (Table 1), DeBERTa-v3-base (Table 2), and GPT-2 medium/large (Table 3), the improvements are uniform. While margins are modest (typically 0.2–2.1 points), the consistency across 10 datasets and 3 model families is strong evidence the method confers a real advantage.

- **Faster convergence and lower total training time.** Table 7 shows BiLoRA achieves lower total training time than LoRA across all GLUE datasets despite the more complex bilevel setup, because it converges in far fewer epochs. The explanation (Softmax initialization yields larger initial singular values, enabling larger learning rates) is plausible and the data is reported.

- **Robustness to design choices.** Ablations on singular value parameterization (Real-Value, Softmax, Approximately Binary, Table 5) and the orthogonality regularizer weight γ₁ (Table 6) show BiLoRA outperforms LoRA under all tested variants, reducing concerns about hyperparameter sensitivity.

- **Scales to very large models.** Results on DeBERTa-XXL (1.5B parameters, Table 4) demonstrate the method is not limited to smaller architectures.

## Weaknesses

### Fatal
None.

### Major

- **The overfitting reduction mechanism is asserted but not directly evidenced.** The paper's central motivation is that training all adapter parameters on a single dataset "often leads to overfitting" (Section 1, line 17), and that BiLoRA alleviates this by separating parameters across data subsets. However, no direct evidence of overfitting is provided: there are no training vs. validation loss curves, no comparisons of train/validation gaps between LoRA/AdaLoRA and BiLoRA. The circumstantial evidence cited (larger gains on small datasets like CoLA, RTE, MRPC — Section 4.2, line 146) is weak — the margin differences are modest (1.4–2.1 points), and STS-B (also small) shows a gain of only 0.4 points. The method's empirical success is credible regardless, but the paper would be substantially stronger if it directly tested whether the train-validation gap narrows as claimed.

### Minor

- **Inconsistent data-split strategies across experiments without justification.** For NLU (Section 4.2, line 144), the training set is split 8:2 into D₁ and D₂. For NLG (Section 4.3, line 157), the training set is used as D₁ and the *validation set* as D₂. These are different setups: D₂ is a subset of training data in NLU but truly held-out data in NLG. The difference is explainable — for GLUE the dev set is used as test (line 144), leaving no separate validation set — but the paper does not articulate this reasoning, leaving readers to wonder whether the NLU results might be weaker because D₂ is not truly held-out. A brief justification would resolve this.

- **Bilevel optimization algorithm is under-specified.** The paper states it uses the Betty library (lines 142, 155) but does not specify the concrete bilevel algorithm (implicit differentiation, iterative differentiation, truncated unrolling, etc.), the number of inner-loop steps per outer-loop step, convergence criteria, or how the lower-level argmin is approximated. While citing Betty is helpful, these details matter for reproducibility and for understanding the method's practical cost.

- **No sensitivity analysis for the data-split ratio.** The 8:2 split ratio is fixed for all NLU tasks (line 144) with no ablation varying it (e.g., 9:1, 7:3, 5:5). The method's behavior could depend on this ratio, especially on small datasets where 20% of training data represents very few examples.

- **No standard deviations or significance tests reported.** Given that many improvements are <1 point (e.g., QQP: 92.2 vs 92.0, MNLI-mm: 90.8 vs 90.6), the absence of variance estimates makes it hard to assess robustness. Five runs are averaged (Table 2 caption), but the spread is not reported.

- **Scaling experiments limited to three small GLUE tasks.** The DeBERTa-XXL results (Table 4) cover only MRPC, RTE, and STS-B — all small datasets where BiLoRA's advantage may be largest. Results on larger tasks (MNLI, QNLI, SST-2) from the same benchmark would be more informative for scaling claims.

- **Computation cost analysis incomplete.** Table 7 reports total training time but not per-step time or per-epoch time. The explanation about larger learning rates is plausible but would benefit from a controlled experiment showing LoRA with the same learning rate and convergence criterion.

### Trivial

- **The Softmax parameterization confound is not isolated.** The paper attributes Softmax's advantage over Real-Value to non-negativity (Section 4.4), but Softmax also normalizes values (they sum to 1), which changes effective step sizes. These factors are not disentangled, though the claim of robustness across parameterizations remains valid.

## Nice-to-Haves

- A theoretical discussion or toy example illustrating how data splitting helps generalization would strengthen the paper's framing.
- A discussion of potential failure cases (e.g., when D₁ is noisy or insufficient) would be useful for practitioners.
- An ablation comparing BiLoRA (Softmax) with a version of LoRA that also uses Softmax singular values (without bilevel training) would isolate the effect of bilevel optimization from the parameterization change.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"LoRA is often praised for preventing overfitting"** — This is the reviewer's opinion and does not contradict the paper's claim that LoRA/AdaLoRA can still overfit to training data within its parameterization. The paper's claim is about a specific overfitting risk for singular values, not about LoRA being more overfit-prone than full FT.
2. **"The data splitting could hurt generalization"** — This misunderstands bilevel optimization, where the upper-level data acts as a validation mechanism. The consistent empirical improvements across all tasks show this concern does not materialize.
3. **"No theoretical justification"** — The paper is an empirical methods paper; theoretical analysis is a nice-to-have, not a core weakness.
4. **"No discussion of when BiLoRA might fail"** — A reasonable suggestion but not a weakness of the current contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the core idea (bilevel separation of singular vectors and values) is novel and empirically effective, but do not surface a deeper insight that the paper itself misses.

## Suggestions

1. **Directly test the overfitting hypothesis** on 2–3 datasets: plot training loss and validation loss curves for LoRA, AdaLoRA, and BiLoRA. This single analysis would substantially strengthen the paper's core claim.
2. **Unify the data-split description**: explicitly note that for GLUE the dev set is used as test (following standard practice), necessitating an internal training split, whereas for E2E NLG a separate validation set is available.
3. **Report per-step time and per-epoch time** alongside total time in Table 7.
4. **Add standard deviations** to all result tables, especially given modest margins.
5. **Ablate the split ratio** (e.g., 9:1, 7:3, 5:5) on 2–3 tasks.
6. **Specify the bilevel algorithm** used by Betty for this work (e.g., number of inner-loop steps, approximation method).

## Score and Decision

The paper proposes a novel and well-motivated method with consistent empirical support across diverse tasks and models. The primary weakness is that the claimed mechanism (overfitting reduction) is asserted rather than directly demonstrated, and several experimental details are under-specified. However, the empirical pattern — BiLoRA outperforms LoRA/AdaLoRA on all 10 datasets — stands on its own regardless of whether the overfitting narrative is precisely correct. The contribution is real and the paper is methodologically sound. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>