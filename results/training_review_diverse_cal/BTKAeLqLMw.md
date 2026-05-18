Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper investigates what makes "good data" for instruction tuning alignment, studying three dimensions — complexity, quality, and diversity. It proposes evolution-based scoring methods (Evol Complexity and Evol Quality) that train a LLaMA-1-7B scorer on ChatGPT-ranked evolved variants of a small seed set (2K Alpaca samples), then combines these scores with an embedding-based diversity filter (Repr Filter) in a score-first, diversity-aware selection algorithm. The resulting DEITA models achieve strong alignment results (e.g., DEITA-Mistral-7B with 6K SFT samples reaching 7.22 MT-Bench) using over 10× less data than comparable open-source models, and the paper demonstrates that the framework generalizes across LLaMA-1, LLaMA-2, and Mistral backbones.

## Strengths

- **Novel evolution-based scoring for complexity and quality.** The idea of evolving a single seed sample into variants, having ChatGPT rank them together in one prompt for fine-grained discrimination, and training a lightweight scorer on the resulting scores is clever and yields measurable gains. Table 1 shows Evol Complexity achieves 6.27 MT-Bench on X\_sota (vs. 5.84 random), and Table 2 shows Evol Quality achieves 6.19 (vs. 5.84 random), outperforming baselines including Direct Scoring, Instag Complexity, and Instruction Node.

- **Demonstrated extreme data efficiency across architectures.** DEITA consistently reaches state-of-the-art alignment with 6K–10K SFT samples across three backbone families. Table 5 shows DEITA-Mistral-7B 6K achieves 7.22 MT-Bench vs. Mistral-7B-Instruct-v0.1 (6.84) and zephyr-beta (7.34 with 200K SFT+60K DPO). DEITA-LLaMA2-13B 6K (6.65) matches LLaMA2-13B-Chat which uses >100K SFT + >1M RLHF data.

- **Comprehensive controlled studies isolating each dimension.** The paper systematically studies complexity (7 baselines), quality (3 baselines), and diversity (2 baselines) in separate controlled experiments (Tables 1–3), providing clear evidence that each dimension contributes to alignment performance. This structured investigation is a methodological contribution in itself.

- **Simple, practical selection algorithm.** The score-first, diversity-aware approach (Algorithm 1) is straightforward and clearly described — sort by score, then iteratively filter by embedding distance. The simplicity increases the likelihood of adoption and makes the method easy to implement and build upon.

- **Strong generalization across backbone architectures.** The method is validated on LLaMA-1-13B, LLaMA-2-13B, and Mistral-7B with consistent improvements, demonstrating that the findings are not architecture-specific.

## Weaknesses

### Fatal

None.

### Major

- **Missing threshold value and sensitivity analysis for the Repr Filter.** The diversity filter's threshold τ is given as "0." (cut off) in the paper (line 295), and no sensitivity analysis is reported showing how results change with different τ values. Since the Repr Filter's behavior (how aggressively it rejects redundant samples) entirely depends on this threshold, and the method's strong results could depend on a carefully tuned value, this is a significant gap. A reader cannot reproduce the method or assess whether the threshold was tuned on the evaluation benchmarks. The paper should provide the actual threshold and at minimum a sweep over τ ∈ [0.7, 0.99] for one backbone and budget.

- **No ablation of the score combination formula.** The combined score is s = c × q (product), but the paper never compares this to alternatives: c + q, max(c, q), min(c, q), or using only c or only q with the *same* diversity filter and score-first procedure. The controlled studies show Evol Complexity alone (top-K, no Repr Filter) achieves 6.27, Evol Quality alone achieves 6.19, and Repr Filter alone (random ordering) achieves 6.17 on X\_sota — while the combined DEITA achieves 6.46. Because each controlled study uses a different selection procedure (top-K vs. iterative Repr Filter), we cannot determine how much of the 6.46 comes from the combined score vs. the score-first ordering alone. This makes it difficult to evaluate the paper's claim that "three dimensions" are necessary. A clean ablation using the same Repr Filter with different scoring formulas would resolve this.

### Minor

- **Performance decline at larger budgets is not adequately investigated.** Figure 3 shows a clear peak at ~6K–10K followed by a decline at larger budgets. The paper offers one explanation — "the proportion of truly good data is limited" — but does not investigate whether this is caused by the fixed diversity threshold failing to maintain diversity at larger budgets, or whether the scoring metric's relationship with downstream performance is non-monotonic. This pattern is unusual for a selection method (one would expect plateauing rather than declining) and deserves deeper analysis.

- **No error bars or confidence intervals.** All results are reported as single-point estimates (e.g., 6.46 MT-Bench, 77.08% AlpacaEval). Given the known variance in LLM-as-judge evaluations (GPT-4 scoring of MT-Bench), and given that many comparisons hinge on differences of 0.1–0.3 points, the absence of standard deviations or multiple-run averages makes it impossible to assess statistical significance.

- **Cross-domain scorer generalization is asserted but not formally validated.** The Evol Complexity and Evol Quality scorers are trained only on 2K Alpaca seed samples (evolved into ~12K training examples) but applied to pools containing ShareGPT, UltraChat, WizardLM, Dolly, OAssit, and FLAN data. While the paper shows the method works on both X\_sota and X\_base (which differ in composition), it does not directly validate whether the scorer's rankings generalize across data sources (e.g., by comparing scorer rankings on ShareGPT vs. Alpaca subsets).

- **DPO results are not attributable to the data selection contribution.** The paper's best headline numbers (7.55 MT-Bench, 90.06% AlpacaEval) come from DEITA-Mistral + DPO, where the DPO data (10K pairs from UltraFeedback) is *randomly sampled*, not selected by any of the paper's methods. The paper states these are "for reference points," but the title and abstract prominently feature these numbers as part of the data-efficiency claim, which is misleading.

- **Asymmetric selection procedures across controlled studies.** The complexity and quality controlled studies use simple top-K selection, while the diversity study uses an iterative Repr Filter. This makes cross-dimension comparisons difficult — for example, we cannot tell if Evol Complexity + Repr Filter would outperform DEITA's combined approach.

### Trivial

- The evolution prompt details for Evol Quality are described only briefly ("enhancing helpfulness, augmenting relevance, enriching depth, fostering creativity, and supplying additional details") — the exact prompts would aid reproducibility.

- The Alpagasus comparison is limited to 50K data pools due to ChatGPT cost, which the paper acknowledges but which limits the fairness of the comparison.

## Nice-to-Haves

- Report the computational cost of the evolution process (ChatGPT API calls for 2K × 5 evolutions + ranking) to help practitioners evaluate adoption costs.
- A controlled comparison where a scorer is trained on 2K samples scored directly by ChatGPT (without evolution) would isolate whether the advantage of Evol Complexity/Quality comes from the evolution-based ranking scheme vs. simply having a trained scorer.
- An adaptive threshold strategy for the Repr Filter (e.g., decreasing τ as the selected set grows) could potentially avoid the performance decline observed at larger budgets.

## Removed Points

- **"No discussion of the choice of backbone for the scorers"** — Trivial implementation detail; LLaMA-1-7B is a reasonable choice consistent with the paper's compute budget. Removed per hard rule on trivial implementation details.
- **"Reproducibility concern about scorer training data being too small"** — The paper shows the scorers work on two different pools (X\_sota and X\_base), which provides empirical validation of the approach. The concern about seed size is partially addressed by the results.
- **"The paper should also test on domain Y / additional tasks"** — The paper already covers MT-Bench, AlpacaEval, and Open LLM Leaderboard (4 tasks), which is a representative evaluation suite. Scope creep.
- **Various parser-artifact formatting complaints** — These are parser issues, not author errors.

## Novel Insights

The most interesting synthesis from the reviews is the tension between the paper's methodological rigor in isolating each dimension (complexity, quality, diversity) and the relative lack of rigor in combining them. The controlled studies for individual dimensions are carefully executed with multiple baselines, yet the combined method (DEITA) is presented without a similarly careful ablation of the combination formula. This means we know each dimension matters individually, but we don't know if the specific product formula is genuinely better than simpler alternatives (like using just complexity with the Repr Filter). The reviewer also identifies an interesting paradox: the paper's strongest evidence for the importance of "good data" (the non-monotonic scaling curve where performance declines at larger budgets) is also its least explained finding. If more data hurts even with a selection method, the community needs to understand why — is it a fixed-threshold issue, or does the scoring metric capture something with a non-monotonic relationship to downstream performance?

## Suggestions

1. Provide the missing threshold value and add a sensitivity study (τ sweep from 0.7 to 0.99) for at least one backbone and budget.
2. Add an ablation comparing c×q, c+q, c-only-ReprFilter, and q-only-ReprFilter to justify the product formula.
3. Add error bars (at minimum, run each experiment 2–3 times with different random seeds for training).
4. Investigate the performance decline at larger budgets — is it due to the fixed Repr Filter threshold? Show what happens with an adaptive threshold.
5. Clarify in the abstract and results that DPO results are not attributable to the data selection method and present the pure SFT contributions as the primary results.
6. Release the exact prompts used for evolution and scoring to facilitate reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>