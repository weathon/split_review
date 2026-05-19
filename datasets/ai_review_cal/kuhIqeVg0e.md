- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
ChemAgent introduces a framework that improves LLM performance on complex chemical reasoning problems by building a structured, self-updating library of three memory types (planning, execution, knowledge) from decomposed sub-tasks. The library is constructed from a development set, retrieved during inference, and dynamically updated with newly solved problems. Experiments on four SciBench chemical reasoning datasets show consistent accuracy improvements over existing methods including StructChem, with gains of up to 46% (GPT-4) over direct reasoning.

## Strengths
- **Consistent and substantial accuracy gains across multiple datasets and backbones (Table 1):** ChemAgent with GPT-4 achieves an average score of 57.16 across four datasets, outperforming StructChem by 9.50 points and direct reasoning by ~37 points. The improvement is particularly striking on CHEMMC (28.21 → 74.36, +46%). The pattern holds across GPT-3.5, GPT-4, and Llama3 backbones, demonstrating robustness.

- **Systematic ablation of memory components (Table 2):** The paper isolates the contribution of each memory type (planning, execution, knowledge) by removing them independently. Removing any component reduces accuracy, providing quantitative evidence for the framework's multi-component design rationale.

- **Memory quality analysis with a non-obvious finding (Table 3):** Comparing GPT-4-generated memory vs. GPT-3.5-generated memory vs. a hybrid reveals an 8% accuracy difference. The hybrid memory performing worst is a non-trivial finding that surfaces an interesting failure mode—mixing memory sources of different quality can confuse the LLM.

- **Error taxonomy grounded in specific examples (Section 3.5, Figure 7):** The paper identifies three distinct failure modes, including the insightful finding that high semantic similarity between a retrieved memory and the current problem can still produce misleading results when a critical property differs (e.g., adiabatic vs. non-adiabatic processes). This provides concrete direction for future work on selective retrieval.

- **Demonstrated self-evolution over time (Section 3.3, Figure 5):** The self-evolution experiment on the MATTER dataset shows performance improving and converging as the memory pool grows with each iteration, providing direct evidence that the dynamic updating mechanism works as intended.

## Weaknesses

### Fatal
None.

### Major
- **Asymmetric baseline comparison confounds the headline claims.** ChemAgent builds its library from the *entire* development set and retrieves up to six memory instances per query, while baselines such as StructChem and Few-shot+Python use only a handful of fixed examples. The "w/o memory" ablation partially addresses this (the decomposition pipeline alone still outperforms StructChem), but the paper does not include a controlled experiment that isolates whether the gains come from the *structure* of the decomposed memories or simply from having a larger, searchable corpus of examples. A comparison against a standard RAG baseline that retrieves raw (undecomposed) problems from the same development set would be the cleanest way to establish that the decomposition into planning/execution memory adds value beyond corpus scale. Without this, the reported 10–15% improvement over StructChem is confounded by an asymmetric information advantage. This is the most significant weakness.

- **No variance reporting for main results.** All accuracy numbers in Tables 1–4 are single-point estimates without confidence intervals, error bars, or multiple-trial results. Given the modest test set sizes (e.g., 90 problems for MATTER), the 2.9% absolute improvement from memory and the 5% improvement from the refinement module could fall within random variation. The self-evolution experiment (Figure 5) reports error margins from two runs, demonstrating the authors *can* do this; the main results should follow suit.

- **Self-evolution experiment uses the test set as a training signal.** Section 3.3 enriches the library with *correct solutions from the test set* as inference proceeds. While the same problem cannot be used on itself, the library is still populated with answers to other test problems, meaning later test instances benefit from exposure to earlier test instances. The paper correctly frames this as a continual-learning analysis rather than a standard evaluation, but the lack of a hold-out set or a test-time-adaptation baseline makes it difficult to interpret how much of the observed improvement is genuine learning vs. data leakage by proxy. This experiment is best treated as suggestive rather than evidential.

### Minor
- **The largest contributing memory component ($\mathcal{M}_k$) is not a stored/library memory.** Table 2 shows that removing Knowledge Memory ($\mathcal{M}_k$) causes the largest performance drop. However, $\mathcal{M}_k$ is generated on the fly by the LLM recalling formulas from its parametric knowledge—it is not part of the library and could be added to any baseline with a simple prompt. The paper acknowledges this implicitly but should more clearly distinguish which components of the framework are genuinely novel contributions vs. prompt engineering that any method could adopt.

- **Missing aggregate statistics for error types.** The error analysis in Section 3.5 presents a qualitative case study with three error categories (Figure 7), but the paper does not report how frequently each error type occurs across the full test sets. A quantitative breakdown would help readers understand which failure modes dominate and where to focus future improvements.

- **No sensitivity analysis of retrieval count.** The paper tests only one configuration (up to 2 planning + 4 execution memories). There is no analysis of how varying the number of retrieved memories affects performance, which would help understand the method's robustness and inform deployment decisions.

- **Synthetic memory generation is not analyzed.** When no similar sub-task is found in the library, the LLM generates "synthetic" execution memories. The paper provides no analysis of how often this triggers, whether these synthetic examples are of comparable quality to retrieved ones, or whether they help or hurt performance.

- **The ablation replacing $\mathcal{M}_e$ with fixed human-written examples is asymmetric.** When $\mathcal{M}_e$ is removed, the paper substitutes "two fixed human-written few-shot examples." This compares LLM-generated memories against expert-crafted examples—a difference that conflates memory *source* (LLM vs. human) with memory *structure* (retrieved vs. fixed). A cleaner ablation would replace $\mathcal{M}_e$ with an automatic retriever on raw problems.

### Trivial
- The cost analysis bubble chart (Figure 6) is difficult to read; a table with exact token counts would be clearer.

## Nice-to-Haves
- Include a table showing how often each error type occurs across the full test sets.
- Test sensitivity to retrieval count (vary the number of retrieved plan/execution memories).
- Expand the error analysis into a limitations section discussing when the method fails (e.g., misleading memory, topics not covered by the dev set, computational cost).
- Include a controlled experiment comparing against a RAG baseline that retrieves raw problems from the same development set using the same embedder, to isolate the value of the memory decomposition structure.
- Report results over multiple trials or with confidence intervals for the main tables.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Paper does not contrast with contemporary LLM memory frameworks (MemGPT, RET-LLM)"** — This is a request for additional related work discussion. The instructions forbid mentioning missing related works since the reviewer cannot verify what was or was not included in the original submission with a complete bibliography.
- **"Prompt details and Table 6 not provided"** — The parser strips appendix content, tables, and images from the extracted text. These exist in the original submission.
- **"Dataset statistics not shown"** — Same as above; Table 6 is referenced in the paper but was stripped by the parser.
- **"Missing appendix, missing proofs"** — Same parser-stripping issue.
- **"Pure formatting/style nitpicks"** about the bubble chart and presentation — These are minor presentation preferences, not substantive weaknesses (the bubble chart concern is kept in Trivial as it has a concrete alternative).
- **Strength Finder claim that the paper addresses "an important problem"** — This is generic and superficial; every paper in the domain addresses an important problem. Not included as a strength.
- **"9.50-point improvement" characterization** from the Strength Finder — While factually correct, this conflates absolute difference (57.16 - 47.66 = 9.50) with the paper's stated "9.50%" relative improvement phrasing. Keeping the substance but not the framing as a standalone strength.

## Novel Insights
The most interesting observation that emerges from combining the reviews is the tension around $\mathcal{M}_k$: the ablation study identifies it as the most impactful memory component, yet it is also the least novel (it is simply the LLM's own parametric knowledge prompted on the fly). This reveals a broader methodological challenge for retrieval-augmented frameworks in specialized domains—if the largest gains come from reminding the model of facts it already "knows" but fails to recall, then the contribution of the structured library ($\mathcal{M}_p$ and $\mathcal{M}_e$) is harder to isolate from simple prompt engineering. The paper's own hybrid-memory experiment (Table 3), where mixing memory sources *hurts* performance, further underscores that memory quality and compositionality are under-explored dimensions. Together, these findings suggest that future work should focus not just on *whether* memory helps, but on *when* each memory type helps and how to prevent retrieval from introducing confusion rather than clarity.

## Suggestions
1. **Add a RAG baseline** that retrieves raw (undecomposed) problems from the development set using the same embedder and similarity threshold. This is the single most important control experiment to establish that the decomposed memory structure adds value beyond corpus scale.
2. **Report variance** for all main results, either through multiple runs with different random seeds or via bootstrap confidence intervals. The small test set sizes make this essential for establishing statistical reliability.
3. **Present aggregate error type frequencies** alongside the qualitative case study to give readers a clear picture of which failure modes dominate.
4. **Run a controlled experiment on the role of $\mathcal{M}_k$:** add a simple "recall relevant formulas" prompt to a baseline (e.g., StructChem or the "w/o memory" variant) and measure whether it closes the gap, to properly attribute the contribution of the knowledge memory component.
5. **Acknowledge the self-evolution experiment's test-set limitation** more prominently and, if feasible, add a comparison against a static baseline that does not update during inference to quantify the benefit of dynamic updating.
