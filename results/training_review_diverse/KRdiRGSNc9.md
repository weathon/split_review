I have verified all claims against the paper. Here is the consolidated review.

---

## Summary

HumanEval-V is a benchmark of 108 Python coding tasks designed to evaluate large multimodal models (LMMs) on visual reasoning through code generation. Each task requires a model to complete a Python function based on a single image, a function signature, and a minimal textual description. The paper evaluates 19 LMMs and finds that even the best proprietary models score only 13–18.5% pass@1, while open-weight models all score below 4% pass@1. Ablation studies reveal that providing human-annotated image descriptions dramatically improves performance (GPT-4o +32.4% pass@1), and that open-weight LMMs suffer coding ability degradation compared to their LLM backbones.

## Strengths

- **Reveals previously undetected LMM limitations**: Correlation analysis (Figure 2) shows models that score highly on MMMU, MathVista, and MMVet often score near zero on HumanEval-V, demonstrating the benchmark exposes weaknesses overlooked by existing multimodal evaluations. This is a genuine contribution to understanding LMM capability gaps.

- **Identifies coding ability degradation in open-weight LMMs**: The ablation in Table 3 quantifies how open-weight LMMs consistently underperform their own LLM decoders on coding benchmarks (e.g., InternVL-2 40.1B drops 28.1% on HumanEval+), providing concrete evidence that current multimodal training strategies harm coding proficiency. The model names in the table confirm these are the actual backbone decoders, making the comparison appropriate.

- **Well-designed ablation isolating vision as bottleneck**: The "Desc. Only" experiment (Table 2), where human-annotated textual descriptions replace images, shows substantial gains for all models (GPT-4o: 13.0% → 45.4% pass@1). This cleanly separates vision-understanding failures from coding-ability failures and is a strong methodological contribution.

- **Rigorous data leakage prevention with documented evidence**: The adaptation pipeline modifies original problem contexts, algorithmic patterns, and redraws visual elements. The observed hallucination errors (e.g., GPT-4o and Claude 3.5 Sonnet incorrectly assuming clockwise ordering from CodeForces origins) provide concrete evidence that the adaptation successfully prevents memorized solutions from working.

- **Thorough evaluation coverage**: 19 models across proprietary and open-weight families, using both greedy decoding (pass@1) and sampling (pass@10, n=20), with a post-processing pipeline and parsing success rate metric to separate syntax from functional errors.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim (visual necessity) is stated but not supported by data**: The paper asserts that "GPT-4o cannot solve any of the coding tasks without access to the images" (Section 2.3) but provides **no experimental data** — no table, no pass@1 scores, no protocol description for this ablation. This is the single most important verification experiment for the benchmark. If even a few tasks can be solved from the function signature and minimal comment (~111 tokens average) alone, the claim that visual information is essential is weakened. The "Desc. Only" experiment is not a substitute: it uses rich human-annotated descriptions, not the original minimal text. **This is a structural evidential gap** because it underpins the entire contribution. The fix is straightforward — report the text-only ablation results — but the paper as submitted does not validate its core premise.

2. **No correlation coefficients reported for the cross-benchmark analysis**: Figure 2 visually shows the relationship between HumanEval-V and MMMU/MathVista/MMVet, but the paper only states "a rough positive correlation" qualitatively. Given that many models near zero on HumanEval-V while spread on other benchmarks, the floor effect is evident, but reporting Pearson/Spearman coefficients would give readers a precise, reproducible measure. This weakens the argument that HumanEval-V measures something "different" from existing benchmarks — a quantitative claim that deserves quantitative support.

### Minor

1. **No confidence intervals or variance estimates for pass@k scores**: With 108 tasks, pass@1 is measured in discrete steps of ~0.93%, and pass@10 (n=20) has non-trivial sampling variance. While single-run evaluation without CIs is standard practice in code generation benchmarking, the paper makes fine-grained comparative claims (e.g., "larger parameter size does not guarantee better performance") that would benefit from bootstrap intervals or similar to establish whether observed differences are meaningful.

2. **The mutation process is described only through one example**: The paper states that "for each suitable task, we create one or two mutations, resulting in a total of 108 coding tasks," and gives one example (changing intersection rules). While the released dataset makes exact replication possible, the lack of a more detailed description of mutation criteria makes it hard to assess how diverse the mutated tasks are from their parents and from each other.

3. **LLM decoder comparison, while valid, has a minor confound**: The paper compares LMMs against their LLM decoders (named explicitly in Table 3) and finds coding degradation. The comparison is valid — these are the actual backbone models. However, the paper states "similar parameter sizes" without noting that the LMM versions include vision encoder parameters (e.g., 40.1B vs 34.4B), which could account for small differences. The degradation is large enough that this doesn't change the conclusion, but the framing should be more precise.

### Trivial

- The list of visual element types (trees, graphs, matrices, etc.) appears in the body text but without frequency counts; a simple table would help users understand benchmark coverage.
- Figure 2 scatter plots have many points overlapping at zero; a jitter or violin plot would make the distribution clearer.

## Nice-to-Haves

- A qualitative error taxonomy (vision misinterpretation vs. algorithm error vs. syntax error) across the 19 models would strengthen the analysis beyond the single overfitting example.
- An analysis of pass rates by task difficulty (e.g., GT code statement count, visual element complexity) would help identify where LMMs fail most.

## Removed Points

- **Criticism about dataset not being available to reviewers / reproducibility concerns** (Harsh Critic): Removed per Hard Rules — the paper states the dataset will be released; questioning its existence or availability is not permitted.
- **"Formatting with wrapped text and multi-row models is a bit hard to parse"**: Removed as a pure formatting/style nitpick.
- **Criticism that "Table 4 mentions trees, graphs, matrices... but no breakdown is given"**: This information is presented in the body text (line 86), not a table; the critic's reference appears hallucinated. The underlying suggestion (a breakdown table) is retained in Nice-to-Haves.
- **Criticism that the rate of discarding tasks (40 from thousands) is "very low" and screening criteria are unclear**: The paper describes the criteria ("high-quality visual elements and moderate difficulty"). A low retention rate is compatible with careful curation; this reads as suspicion of curation rigor without evidence of a problem.
- **Strength Finder's claim that visual necessity is "validated by the finding that GPT-4o scores... 45.4% pass@1 when provided with textual descriptions alone"**: This conflates two different experiments. The 45.4% comes from the "Desc. Only" setting (human-annotated descriptions), not from the original minimal text. The strength about the design goal is kept, but the cited evidence is corrected.
- **Criticism that "the Desc. Only experiment does not prove visual necessity"**: This is correct but the point is already covered in Weakness #1 (Major). The Desc. Only experiment is a different (and valid) contribution showing vision is a bottleneck; it does not and should not have to prove the text-only case.

## Novel Insights

The single most insightful observation from the reviews is the **asymmetry between the rigor of the paper's ablations and the lack of evidence for its most fundamental claim**. The paper carefully designs a "Desc. Only" condition to isolate vision as a bottleneck and an LLM-decoder comparison to isolate coding degradation, yet fails to provide any data for the simpler and more essential validation: that the original minimal text alone cannot solve the tasks. This is not a deep methodological flaw — it is an omission that can be fixed — but it is striking because the rest of the experimental design shows the authors are clearly capable of running this check. The reviews also surface that the cross-benchmark correlation claim would benefit from a reported coefficient, which would turn a qualitative observation into a quantitative contribution.

## Suggestions

1. **Run and report the text-only ablation**: GPT-4o (or the best model) on all 108 tasks using only the function signature and comment (no image, no human-annotated description). Report per-task pass@1 and aggregate pass@1. If any task is solved above 0%, either exclude those tasks or further strip their textual cues. This single addition would close the evidential gap that currently undermines the paper's core thesis.

2. **Add correlation coefficients** (Pearson or Spearman) to the regression analysis in Figure 2 to quantify the relationship between HumanEval-V and MMMU/MathVista/MMVet.

3. **Report confidence intervals** (e.g., via bootstrap) for pass@10 estimates to help readers assess whether observed differences between models are statistically meaningful.

## Score and Decision

**Score: 6.5 / 10**

The paper introduces a well-motivated and carefully constructed benchmark that fills a genuine gap in LMM evaluation. The ablation studies are insightful, the overfitting evidence is compelling, and the main findings (vision bottleneck, coding degradation) are novel and important. However, the paper's central claim — that all 108 tasks are unsolvable without visual input — is asserted without supporting data. This is a fixable omission but it is not minor; it directly affects whether the benchmark measures what it claims to measure. A revision that provides the text-only ablation results and correlation coefficients would substantially strengthen the contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>