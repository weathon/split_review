Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper studies automatic data selection for instruction tuning by measuring data along three dimensions—complexity, quality, and diversity. It proposes DEITA, a score-first diversity-aware selection strategy: complexity and quality scores are predicted by small LLaMA-1-7B scorers trained on ChatGPT-ranked evolution variants, then combined via multiplication, and samples are selected iteratively with an embedding-based diversity filter (Repr Filter). The core empirical claim is that DEITA, trained on only 6K–10K SFT samples, matches or outperforms models trained on orders-of-magnitude more data—e.g., DEITA-Mistral-7B (6K SFT) achieves 7.22 MT-Bench vs. 5.89 for random selection, and with DPO reaches 7.55 MT-Bench/90.06% AlpacaEval, comparable to zephyr-beta (200K SFT + 60K DPO).

## Strengths

- **Systematic controlled study across three data dimensions with clean isolation.** The paper separately studies complexity (Table 1), quality (Table 2), and diversity (Table 3) in controlled experiments on LLaMA-1-13B, each time comparing multiple baselines. For each dimension, the proposed metric (Evol Complexity, Evol Quality, Repr Filter) outperforms all baselines, e.g., Evol Complexity achieves 6.27 MT-Bench vs. 5.84 random on X_sota (Table 1).

- **Strong empirical results demonstrating dramatic data efficiency.** DEITA-Mistral-7B (6K SFT) achieves 7.22 MT-Bench and 80.78% AlpacaEval, outperforming zephyr-beta-sft (200K SFT, 5.32 MT-Bench) and Vicuna-13B-v1.3 (125K SFT, 6.39 MT-Bench). With DPO added (6K SFT + 10K DPO), it reaches 7.55 MT-Bench and 90.06% AlpacaEval, comparable to zephyr-beta (200K + 60K DPO) — an order-of-magnitude data reduction. These results hold across three backbone models (LLaMA-1-13B, LLaMA-2-13B, Mistral-7B) and multiple evaluation benchmarks.

- **Cost-effective scoring pipeline with practical value.** Evol Complexity and Evol Quality train small LLaMA-1-7B scorers on a 2K seed dataset scored once by ChatGPT, then apply them to the full pool without additional API calls. This avoids the prohibitive cost of per-sample ChatGPT annotation required by Direct Scoring and Instruction Node baselines.

- **Data scaling analysis revealing diminishing returns.** Figure 4 shows that DEITA with 3K samples matches using all 300K samples, and performance plateaus/declines beyond 6K–10K. This supports the paper's central thesis that careful selection matters more than raw quantity.

- **Robustness across data pools of different quality.** The proposed metrics perform well on both X_sota (high-quality) and X_base (lower-quality) pools. For instance, Evol Complexity achieves 5.57 on X_base vs. 4.93 random, while Instag Complexity drops to 4.98 (Table 1).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented.

### Minor

- **No variance or statistical significance reported for MT-Bench / AlpacaEval.** The paper reports single-run evaluation without confidence intervals, standard deviations, or multiple random seeds. While single-run evaluation is common practice on these benchmarks, several comparative claims rely on modest margins (e.g., DEITA-LLaMA2-13B_6K at 6.65 vs. LLaMA2-13B-Chat at 6.65 — a tie; DEITA-LLaMA2-13B_10K at 6.79 vs. LLaMA2-13B-Chat at 6.65). Without variance estimates, the reader cannot assess whether the finer-grained differences are reproducible or within evaluation noise. The large-gap claims (DEITA-Mistral-7B at 7.22 vs. random at 5.89) are robust to this concern, but the fine-grained ones are not.

- **Missing ablation: combined score (c × q) vs. individual dimensions within the same selection framework.** The controlled studies evaluate complexity alone (Table 1) and quality alone (Table 2), and the combined DEITA method (Table 4) outperforms both individually. However, the paper never directly ablates whether the product c × q outperforms either c-only or q-only selection when the diversity filter is held constant. The choice of multiplication over sum or max is stated without justification or comparison. These are empirical questions the paper's framework is well-suited to answer but does not.

- **Data scaling comparison may not be apples-to-apples on training schedule.** Figure 4 claims that 3K DEITA samples match using all 300K samples (100× reduction), but the paper does not specify whether the full 300K model was trained for the same number of steps/epochs as the DEITA subsets. If the "all" model was trained for 1 epoch while DEITA models received more epochs, the comparison conflates data efficiency with compute budget. This does not undermine the paper's main results (which compare to published baselines with their own training recipes), but it weakens the specific 100× claim.

- **Scorer generalization to different base models and data distributions is not analyzed.** The Evol Complexity and Evol Quality scorers are trained on LLaMA-1-7B using Alpaca seed data, then applied to score samples from ShareGPT, UltraChat, and WizardLM (ShareGPT) for selecting data to train LLaMA-2 and Mistral models. The paper provides no analysis (e.g., correlation with human judgments, or even score distributions across pools) to verify that the scorers generalize. The strong final results on Mistral suggest reasonable generalization, but an explicit check would strengthen the claim.

### Trivial

- **Diversity threshold τ is cut off in the extracted text** (line 295: "We set threshold τ as $0."). The actual value needs to be provided for full reproducibility. If this is a parser artifact, the authors should verify it renders correctly.

- **No dedicated limitations section.** The paper does not discuss potential limitations such as the reliance on ChatGPT for seed data scoring, the narrow seed dataset (Alpaca-only), or the sensitivity of the diversity threshold.

## Nice-to-Haves

- Ablation comparing top-\(m\) scored samples with vs. without the Repr Filter (diversity-aware step) to isolate the contribution of diversity within the DEITA pipeline.
- Report results with at least 2–3 random seeds or confidence intervals on MT-Bench, at least for the main comparisons.
- Analysis of scorer generalization: a simple correlation plot between scorer predictions and human/intended rankings on a held-out sample from each data pool.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Unfair comparison: Alpagasus limited to 50K while DEITA uses full 300K pool."** The paper transparently acknowledges this limitation in footnotes throughout all tables. The constraint is inherent to the baseline method (Alpagasus requires per-sample ChatGPT annotation, which is cost-prohibitive on 300K samples). This is not an unfair design choice by the authors — it is a practical limitation of the baseline that DEITA was designed to overcome. Comparisons are labelled accordingly.

- **"Mistral random baseline (5.89) is considerably lower than LLaMA-1 random baseline (5.84)."** This is factually incorrect: 5.89 > 5.84. The reviewer's criticism that these numbers suggest noisy baselines is unsupported. If anything, the higher Mistral baseline makes DEITA's improvement (7.22 vs. 5.89) even more impressive.

- **"Missing prompt details and scoring scale for Evol Complexity."** These details are standard content for appendices, and the parser strips appendix content. The prompt methodology is described in the main text (one prompt with 6 evolution variants per seed sample, scoring for relative differences). The paper states the seed dataset size (2K from Alpaca) and the base model (LLaMA-1-7B).

- **"Missing training hyperparameters (batch size, learning rate, epochs)."** Training details are standard for appendix placement. The parser strips these sections.

## Novel Insights

None beyond the paper's own contributions. The reviews add methodological scrutiny but do not surface novel findings about the paper's subject matter.

## Suggestions

- Add variance estimates (at minimum, report the range or standard deviation across multiple evaluation runs on MT-Bench, or cite established variance figures from prior work to contextualize reported differences).
- Add an ablation table comparing: (a) c-only + diversity, (b) q-only + diversity, (c) c×q without diversity filter, (d) c×q + diversity filter, and (e) c+q + diversity filter — to empirically justify each component of the pipeline.
- In the data scaling discussion, clarify whether all points on the curve (including the "all 300K" point) were trained with the same number of total optimization steps / epochs; if not, note this as a caveat.

## Score and Decision

The paper makes a solid, practical contribution to automatic data selection for instruction tuning. The controlled studies are well-designed, the proposed method is cost-effective and consistently outperforms baselines, and the empirical results convincingly demonstrate that careful selection on 6K samples can match models trained on orders-of-magnitude more data. The weaknesses are real but evidential rather than structural — they concern missing ablations, variance reporting, and hyperparameter documentation that would strengthen rather than invalidate the claims. The core contribution is sound, and the paper is appropriate for a full-length publication.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>