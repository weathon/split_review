Now I'll write the final review.

## Summary

CRAFT proposes a training-free framework for customizing LLMs by (1) offline creation of a task-specific toolset — generating code solutions from training data, abstracting them into reusable functions, validating correctness, and deduplicating — and (2) online multi-view retrieval (by problem, function name, and docstring) to select relevant tools at inference. Experiments on VQA, tabular processing (TabMWP), and mathematical reasoning (MATH) show consistent improvements over several baselines including ViperGPT, PoT, LATM, and CREATOR.

## Strengths

- **Multi-view matching retrieval is empirically effective**: The ablation study shows that removing any of the three matching views (problem, function name, docstring) hurts performance, with function name ablation causing >6.6 SAcc drop. This provides concrete evidence that multi-view retrieval adds value over single-similarity approaches (BM25 alone, SimCSE alone), which the paper shows have variable and inconsistent performance.

- **Monotonic scaling with toolset size**: Across all three VQA datasets, soft accuracy increases monotonically as the toolset grows (0→261→337→525 tools), with the largest jump from 0 to 261 tools. This directly validates the core thesis that creating a curated, task-specific toolset (rather than relying on a few generic tools) is the primary driver of improvement.

- **Large and well-documented gains on VQA**: Absolute SAcc improvements of 10.4 (GQA), 18.0 (OK-VQA), and 15.2 (A-OKVQA) over ViperGPT vanilla, plus a 43.16% relative F1 improvement averaged over the best VQA baselines. VQA is a clean testbed because LLMs cannot process images without external tools, so gains must come from the toolset/retrieval quality rather than the backbone's parametric knowledge.

- **Ablation confirms necessity of abstraction step**: Removing abstraction causes a clear performance drop across all three VQA datasets, distinguishing CRAFT from naive tool-creation approaches and confirming that generalization from specific solutions to reusable tools is beneficial.

- **Low cyclomatic complexity of created tools**: Average cyclomatic complexity of 2.64 (VQA), 2.07 (tabular), 1.34 (math), all well below the threshold of 10 for well-structured code, supporting the claim that tools are reliable and not brittle.

## Weaknesses

### Fatal
None.

### Major

- **CREATOR baseline is modified in a way that disadvantages it**: The paper states (line 347): "For fair comparisons, we remove the format checking and rectifying process used in the original work and only measure the one-pass accuracy." This strips CREATOR of its core iterative verification mechanism — a defining feature of the method. Meanwhile, CRAFT retains its full pipeline (validation, abstraction, deduplication). The comparison is asymmetric: CRAFT's full multi-stage pipeline is compared against a handcuffed variant of CREATOR. If the authors want to claim that CRAFT outperforms CREATOR, they should compare against CREATOR as published, or clearly label the ablated variant and not use it to claim superiority over the actual method.

- **No statistical significance or variance reported**: All results (main experiments, ablations, scaling analysis) are presented as single-point estimates with no error bars, confidence intervals, or indication of multiple runs. LLM-based code generation and tool retrieval are inherently stochastic. Without variance estimates, it is impossible to assess whether the reported improvements (especially the fine-grained ablation differences like which retrieval view "matters most") are reliable or within the noise.

### Minor

- **Limited backbone evaluation**: Main results use only GPT-3.5-Turbo. GPT-4 is tested but only against ViperGPT (one baseline), not the full comparison suite including LATM, CREATOR, or the alternative retrieval methods. CodeLlama is dismissed in two sentences (line 365) as exhibiting "near-random performance" with no details on model variant, prompting strategy, or diagnostic analysis of the failure. The claim of "broad applicability" (line 269) would be strengthened by evidence from more than one backbone.

- **Ablation studies conducted only on VQA datasets**: The paper justifies this by noting VQA is "particularly pertinent" (line 405) since LLMs cannot process images directly, but the claim that CRAFT's components are broadly beneficial would be stronger if ablations were also performed on tabular and math tasks.

- **No ablation of the deduplication step**: The pipeline has four steps (Generation, Abstraction, Validation, Deduplication), but only Abstraction and the retrieval components are ablated. The effect of deduplication on downstream performance is never isolated.

- **Missing details on training data used for tool creation**: The paper describes "n" initial samples and "k=100" per iteration but does not report the actual number of training examples used per dataset, making it impossible to assess the data efficiency of the approach.

- **No discussion of limitations**: The paper would benefit from candid discussion of when the method might fail (e.g., noisy or small training data, tasks that cannot be decomposed into atomic code functions, scenarios where the retrieval fallback is triggered frequently).

### Trivial
None.

## Nice-to-Haves
- An ablation of the deduplication step would complete the component analysis.
- Analysis of how often retrieval returns an empty set (triggering the fallback to direct code generation) would help characterize when and why the retrieval succeeds or fails.
- Reporting the actual number of training examples used for tool creation per dataset would aid reproducibility and data efficiency assessment.

## Removed Points
- **Validation circularity (GPT-4 validating its own tools)**: The harsh critic raised a concern about GPT-4 self-validation being circular. However, the validation step checks whether the abstracted tool, when called with appropriate arguments, solves the *original problem it was created from*. This is a reasonable functional correctness check, not a circular dependence; the concern about "systematic gaps" is speculative without evidence of specific failure cases.
- **External libraries failing to improve performance as a flaw**: The paper reports this as an empirical finding that motivates tool creation. It is an observation, not a weakness in the methodology.
- **Post-hoc explanation for TabMWP exception**: While the explanation ("relatively straightforward patterns") is brief, it is a plausible interpretation consistent with the observed result, not a methodological error.
- **Community detection analysis concerns**: The speculation that the number of classes may be an artifact of the clustering algorithm's resolution parameter is not supported by evidence and the analysis is reasonable as presented.
- **Diminishing returns in scaling not highlighted**: The paper presents the scaling trend as a consistent increase; the observation of diminishing returns is not a flaw but a presentation preference.
- **LATM/CREATOR interpretations as "thin evidence"**: The paper offers plausible post-hoc explanations for why these baselines underperform (limited toolset size, insufficient diversity). These are reasonable interpretations of the observed results, not methodological weaknesses requiring formal proof.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Restore CREATOR's format checking and rectification and re-run the comparison, or clearly relabel and contextualize the ablated variant so that it is not used to claim superiority over the actual published method.
- Report results over at least 3 random seeds with means and standard deviations for the main experiments and key ablations.
- Either run CRAFT on at least one open backbone with proper prompt tuning, or provide a detailed diagnostic analysis of why CodeLlama failed (model variant, prompt format, experimental setup).
- Conduct ablations (especially for retrieval components and abstraction) on at least one non-VQA dataset to support claims of broad applicability.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>