## Summary

This paper presents a systematic empirical study of prompt optimization for Large Reasoning Models (LRMs), examining both whether LRMs benefit from prompt optimization and whether they serve as superior prompt optimizers compared to standard LLMs. Using an MCTS-based optimization framework on ACE05 event extraction as the primary task, and generalizing to Geometric Shapes and NCBI Disease NER, the authors compare DeepSeek-R1 and OpenAI o1 (LRMs) against GPT-4.5 and GPT-4o (LLMs) in both task model and optimizer roles. The main finding is that LRMs benefit substantially more from prompt optimization than LLMs and generate more effective, concise, rule-grounded prompts when serving as optimizers.

---

## Strengths

- **Timely and well-motivated research question**: The premise—whether LRMs still require prompt engineering—directly addresses an active debate in the community. The paper is arguably the first to study this question systematically and fills a genuine gap.
- **Systematic multi-role experimental design**: Testing all four models in the optimizer role against all four task models (4×4 matrix), at two training set scales (ACE_low, ACE_med) and two search depths (1 and 5), produces a comprehensive picture of LRM vs. LLM behavior.
- **Qualitative analysis of optimized prompts (Table 2)**: The paper provides concrete evidence for *why* LRMs are better optimizers—they produce concise, rule-grounded instructions with specific exception handling (e.g., article stripping, pronoun resolution, span-normalization rules), while LLMs focus on generic formatting instructions. This mechanistic insight is informative.
- **Convergence and stability analysis (Fig. 4)**: The finding that DeepSeek-R1 as optimizer yields faster convergence and lower variance across task models is a practically useful insight for MCTS-based prompt optimization.
- **Generalization to two additional tasks**: The results on Geometric Shapes and NCBI Disease NER corroborate the main EE findings, increasing confidence in the general applicability of the conclusions.

---

## Weaknesses

### Fatal
None.

### Major

1. **Quantized DeepSeek-R1 vs. unquantized closed-source models**: DeepSeek-R1 is deployed locally at 2.5-bit quantization due to compute constraints, while all other models (o1, GPT-4.5, GPT-4o) are accessed at full precision via API. The paper cites general benchmarks for quantization robustness, but there is no specific evidence that 2.5-bit precision preserves the model's ability to generate high-quality natural language prompts—a generation task that may be more sensitive to quantization than mathematical reasoning. This makes the DeepSeek-R1 vs. o1 comparisons difficult to interpret cleanly, since any observed differences could be partially attributable to quantization artifacts rather than model family differences.

2. **Inconsistent no-optimization baseline across experimental blocks**: In Table 1, GPT-4o's no-opt baseline is 12.68 on the ACE_low block and 12.68 on the MCTS depth-5 ACE_med block, but inexplicably rises to 26.30 in the MCTS depth-1 ACE_med block. Since the no-opt baseline should be independent of training set choice or MCTS depth (it is the raw model score), this inconsistency is unexplained and raises concerns about experimental reproducibility. All other models (GPT-4.5, o1, DS-R1) show consistent no-opt baselines across blocks, making GPT-4o's anomaly stand out. The paper provides no comment on this.

3. **Absence of statistical significance testing**: Dev and test sets are 100 and 250 examples respectively. Many key comparisons are within 1–3 AC F1 points (e.g., o1 vs. GPT-4.5 as optimizers in several settings). Without confidence intervals or significance tests, it is unclear which differences reflect genuine model advantages versus sampling noise, particularly for the nuanced optimizer comparisons in RQ3.

4. **Reduced event type scope not fully justified**: The study uses only 10 of ACE05's 33 event types, citing concerns about prompt length. While this is an acknowledged limitation, it is also a key experimental constraint that limits practical relevance—real-world EE systems operate over full schemas. It is unclear whether the optimizer advantage of LRMs would hold or widen with longer, denser schemas.

### Minor

1. **Generalization experiments use only self-optimization**: Table 3 (Geometric Shapes, NCBI) only reports each model optimizing itself, unlike the main EE analysis which includes cross-model optimization. This provides a more limited picture of whether LRMs are better *general-purpose* optimizers beyond EE.

2. **Survival plot (Fig. 5a) uses only one task model**: The survival analysis is conditioned on DeepSeek-R1 as the task model—the combination that most favors DeepSeek-R1 as optimizer. Showing this for all task models or aggregating would provide a more balanced picture of optimizer quality.

3. **Batch prompting introduces a confound**: The paper notes using batch prompting during evaluation and observes a "performance gain over single-question querying." Since batch prompting has known effects on output quality, its interaction with LRM vs. LLM behavior is not fully controlled or studied.

### Trivial

- The summary figure (Fig. 1 and accompanying table) lists both "Best LRM, DeepSeek-R1 (No Optimization)" and "Average LLM performance as M_task" as 16.47, which is likely coincidental but may confuse readers at first glance.

---

## Nice-to-Haves

- It would strengthen the paper to include ablations comparing full-precision DeepSeek-R1 (even on a small subset) against the quantized version to bound the quantization effect.
- Adding confidence intervals to Table 1 values (e.g., via bootstrap resampling over the dev/test sets) would directly address the statistical reliability concern.

---

## Novel Insights

Beyond the headline finding that LRMs are better at both consuming and generating prompts, the most genuinely novel insight is the *style asymmetry* between LRM- and LLM-generated prompts: LRMs produce action-oriented, exception-rich, rule-based instructions with illustrative examples (Table 2), while LLMs default to format-centric scaffolding. This behavioral distinction—potentially rooted in the extended chain-of-thought training of LRMs—suggests that LRMs have internalized a more task-analytic mode of instruction generation. The complementary finding that DeepSeek-R1 achieves peak task performance with shorter prompts than o1 (despite the latter generating longer, more exhaustive prompts) hints at model-specific prompt style preferences that could inform optimizer-model matching strategies in future work.

---

## Suggestions

- Clarify the GPT-4o no-opt baseline discrepancy (26.30 in ACE_med depth-1 vs. 12.68 elsewhere) in the paper.
- Report bootstrap confidence intervals or paired significance tests for the main optimizer comparison results.
- Include cross-model optimization (e.g., LRM optimizing LLM task models) in the generalization experiments, consistent with the main EE study design.
- Briefly discuss whether the findings would likely hold or differ under full-precision DeepSeek-R1 deployment.

---

## Score and Decision

The paper asks a timely and practically important question, employs a consistent experimental framework, and produces interpretable findings with good qualitative depth. The main weaknesses—quantized model comparison, an unexplained baseline inconsistency, and absent significance tests—reduce confidence in specific numerical claims but do not invalidate the overall picture. The contributions are primarily empirical, and the paper provides actionable insights for practitioners deploying LRMs in structured extraction pipelines.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>