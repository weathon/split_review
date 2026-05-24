## Summary

This paper introduces **RLIE**, a framework that combines LLM-based natural-language rule generation with logistic regression (Elastic Net regularization) for probabilistic rule weighting, plus error-driven iterative refinement. The key idea is a division of labor: LLMs handle local semantic tasks (generating rules, judging rule satisfaction via ternary {+1,0,-1} outputs) while a classical linear model handles global aggregation and calibration. On six real-world classification benchmarks, RLIE with DeepSeek-V3 achieves the best or second-best Accuracy/Macro-F1 against strong baselines. The paper also systematically compares four inference strategies and reports the counterintuitive finding that the simple Linear-only combiner outperforms feeding rules, weights, and predictions back into an LLM.

---

## Strengths

1. **Clean hybrid design with a principled division of labor.** The framework separates local semantic reasoning (LLM generates rules and judges rule coverage) from global probabilistic aggregation (logistic regression with Elastic Net). This is a well-motivated architecture that avoids both the brittleness of pure symbolic rule systems and the unreliability of using LLMs for weighted integration. The ternary judgment (+1,0,–1) with coverage-based filtering (threshold γ) is a sensible way to handle partial rule applicability.

2. **Systematic evaluation of inference strategies (E1–E4) reveals a non-trivial finding.** Table 2 shows that Linear-only (E1) outperforms all LLM-based strategies (E2: rules only, E3: rules+weights, E4: rules+weights+linear prediction) across six datasets and two LLM backbones. This is the paper's most interesting contribution — it provides empirical evidence that LLMs struggle to integrate weighted probabilistic information during inference, supporting the paper's proposed division of labor. This finding offers practical guidance for practitioners building rule-based systems.

3. **Consistent empirical advantage on real-world benchmarks.** RLIE (DeepSeek-V3) achieves the best accuracy on 5 of 6 datasets (Dreadit: 82.3, Headline: 67.0, Citations: 64.6, LLM Detect: 90.7, Reviews: 70.9) and is top-2 on all six, outperforming HypoGeniC, IO Refinement, and zero-shot baselines using the same backbone LLM (Section 5.1, Table 1). This demonstrates that the hybrid approach generalizes across diverse text classification tasks.

4. **Targeted iterative refinement via prediction-error-based hard example selection.** Unlike prior work that uses random sampling or simple rule accuracy for refinement, RLIE selects hard examples based on the logistic regression model's prediction errors (Section 3.3). This creates a tight coupling between rule generation and probabilistic weighting that previous LLM-based rule learning methods lack.

---

## Weaknesses

### Fatal

None. Despite the issues below, none invalidate the paper's core claims.

### Major

1. **Missing standard deviations in the main results tables, despite claiming to report them.** Section 4.3 states: *"Each experiment was repeated at least three times, and we report the mean and standard deviation of the results."* However, **neither Table 1 nor Table 2 shows any standard deviations** — every entry is a single number (e.g., "82.3 / 82.3"). With test sets of only 300 samples, observed differences of 1–2 percentage points (e.g., 67.0 vs. 66.8 on Headline in Table 2) could easily fall within sampling noise. Without variance information, the reliability of every comparative claim in the paper — including the central finding that Linear-only outperforms LLM-based strategies — cannot be assessed. This is a significant evidential gap for an empirical paper making multiple comparative claims.

2. **Contradictory LLM specification in text vs. tables.** Section 4.3 (line 304) states: *"All experiments involving LLMs utilized gpt-4o-mini with the temperature set to 1×10^{-5}"*. Yet Table 1 lists the backbone for all baselines as DeepSeek-V3 and the backbones for RLIE as Qwen3-Next-80B, Qwen3-235B, and DeepSeek-V3. Table 2 similarly lists DeepSeek-V3 and Qwen3-235B as backbones for inference strategies. This is a direct contradiction that creates confusion about which LLM actually performs rule generation, rule judgment, and inference. The fair comparison in the table (RLIE DeepSeek-V3 vs. baselines DeepSeek-V3) is internally consistent and likely correct, but the text is clearly wrong, and the reader has no way to tell whether gpt-4o-mini was used for some other purpose. This must be resolved before the results can be fully trusted.

### Minor

1. **Small dataset splits limit generalizability.** Training/validation/test splits are fixed at 200/200/300 samples. While the paper uses six diverse tasks, results on such small splits may not generalize to larger-scale settings. The paper acknowledges this implicitly but does not discuss how the method might scale.

2. **No analysis of learned rule set properties in the main text.** The paper claims RLIE produces compact, interpretable rule sets, but the main text provides no quantitative information about: (a) the number of rules surviving Elastic Net regularization, (b) rule diversity or redundancy, (c) concrete examples of learned rules and their learned weights. Such analysis (even a brief case study) would substantially strengthen the paper's claims about interpretability and knowledge discovery.

3. **No measurement of LLM judgment consistency.** The framework relies on LLM ternary judgments (±1,0) for rule coverage, but the paper never measures how consistent these judgments are across repeated applications. If the LLM's rule judgments are noisy, the logistic regression weights would be unreliable.

### Trivial

- The four inference strategies in Figure 1 are redundantly described (text appears twice in the diagram caption).

---

## Nice-to-Haves

- **Statistical significance testing** (e.g., paired bootstrap or McNemar's test) would strengthen confidence in the comparative results, especially given the small test sets. Standard deviations would be a prerequisite for this.
- **Ablation of iterative refinement** (e.g., one-shot rule generation vs. multiple refinement rounds) to quantify the benefit of the iterative loop.
- **Qualitative analysis of prediction flips** between E1 and E4, to understand why the LLM's integration degrades performance (does it override correct predictions? does it ignore weights?).

---

## Removed Points

The following points from the input reviews were removed with justification:

- **"LLM contradiction invalidates the main comparison"** (from Harsh Critic): Overstated. While the contradiction is confusing, the table clearly shows the backbone LLM for each method. The key comparison (RLIE DeepSeek-V3 vs. baselines DeepSeek-V3) is internally fair and traceable from the table. The text error does not invalidate the comparison, though it must be corrected.
- **"No statistical significance testing is a fatal gap"** (from Harsh Critic): Demoted to Nice-to-Have. Multi-run means with std would be sufficient; formal significance testing is good practice but not universally required at top venues, and many accepted papers do not include it.
- **Strengths about "superior performance via hybrid rule learning"** and **"principled iterative refinement"** from Strength Finder: Kept as-is (verified against the paper).
- **Various generic/scope-creep weaknesses** from Harsh Critic (e.g., requesting larger datasets, asking the paper to solve problems outside its scope, speculative concerns about data leakage): Removed as they are not specific identified flaws in the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews raise valid concerns about missing variance reporting and an LLM specification inconsistency, but do not surface a fundamentally novel observation that the paper itself misses.

---

## Suggestions

1. **Fix the LLM specification.** Clarify in Section 4.3 which LLM is used for each operation (rule generation, rule judgment, inference strategies E2–E4). If gpt-4o-mini was used for some auxiliary purpose, explain what. If it was an error, correct it and state clearly that DeepSeek-V3 (and Qwen3 variants) were the backbone LLMs.

2. **Add standard deviations (or error bars) to Tables 1 and 2.** The paper already runs three repeats — simply report the ± values or put them in parentheses. Without these, the reader cannot assess whether the reported advantages are significant.

3. **Include a table or figure showing learned rule properties** for at least one dataset: number of rules retained after Elastic Net, top-weighted rules with their coefficients, and an example rule application.

4. **Add an ablation comparing one-shot rule generation vs. full iterative refinement** on a representative dataset to quantify the benefit of the iterative loop.

---

## Score and Decision

**Calibration anchors used (from human-reviewed corpus):**

| Path | Avg Score | How it compares to this paper |
|------|-----------|-------------------------------|
| `BpIbnXWfhL.md` (RuAG, Accept) | 6.33 | Similar topic — LLM rule learning for reasoning. RuAG uses MCTS for rule search; RLIE uses logistic regression + iterative refinement. RLIE has cleaner evaluation design but missing std reporting and an LLM contradiction. Slightly weaker. |
| `zDjHOsSQxd.md` (End-to-End Rule Induction, Accept) | 6.25 | Differentiable ILP from raw data. Stronger theoretical contribution but tested on simpler tasks. RLIE is comparable in quality but has more practical real-text evaluation. |
| `tAmfM1sORP.md` (HtT, Reject) | 4.75 | Earlier LLM rule-learning paper tested only on synthetic tasks with weaker baselines. RLIE is substantially stronger — real datasets, proper baselines, more sophisticated method. |
| `51WraMid8K.md` (Probabilistic Perspective on Unlearning, Accept) | 8.00 | Unrelated topic. Much higher-scoring paper with formal contributions. Not directly comparable. |
| `BeOEmnmyFu.md` (Playing Language Game, Reject) | 2.50 | Unrelated topic. |
| `ly10tMV6cD.md` (Structure-Rich Text Benchmark, Reject) | 3.25 | Unrelated topic. |

**Positioning:** The paper sits between the HtT paper (4.75, clearly weaker — synthetic-only evaluation) and RuAG (6.33, slightly stronger — better method description, no LLM contradiction issue). The core methodology and evaluation design are compelling, but the missing variance reporting and unresolved LLM specification are concrete issues that prevent a higher score.

**Overall assessment:** The paper proposes a well-motivated hybrid framework, demonstrates consistent empirical gains, and reports a genuinely interesting finding about LLMs' inability to integrate weighted rules. However, in its current form, the absence of reported variance in the main results (despite claiming to report it) is a significant oversight for an empirical paper, and the contradictory LLM specification undermines reader confidence. These are fixable issues, and the core contribution has real value.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>