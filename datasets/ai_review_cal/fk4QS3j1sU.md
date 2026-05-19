- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6
Now I have verified all claims. Let me produce the consolidated review.

## Summary

PoTable proposes a table-based reasoning method that mimics a human analyst's workflow by splitting the process into five logical stages (initialization, row selection, data type cleaning, reasoning, final answering), each with LLM-based planning and Python code generation executed in real-time by a Python interpreter with error recovery. The key claims are: (1) a human-like stage split improves reasoning quality, and (2) using an *open-world* (unconstrained) operation space rather than a fixed operation pool allows more flexible reasoning. Experiments on WikiTQ and TabFact with GPT-4o-mini and Llama-3.1-70B show consistent accuracy improvements over Binder, Dater, Chain-of-Table, and TabSQLify, with GPT-based PoTable achieving 4–6% absolute gains.

## Strengths

- **Large and consistent accuracy gains across datasets and backbones.** Table 1 shows PoTable outperforms all baselines on all three evaluation sets under both GPT-4o-mini and Llama-3.1-70B. The GPT improvements are substantial (+4.38 pp on WikiTQ dev, +5.87 pp on WikiTQ test, +4.30 pp on TabFact). The LLAMA improvements, while smaller (+1.44 to +3.34 pp), are still consistently positive. This directly supports the core claim of state-of-the-art accuracy.

- **Ablation study validates the stage-split contribution.** Figure 3 compares full PoTable against removing or adding stages. The "only reasoning" setting (no row selection or data type cleaning) drops 0.6–1 pp on WikiTQ and ~3 pp on TabFact. The paper also finds that adding a column selection stage *hurts* performance, a non-obvious result that provides genuine insight into when stage splits help versus hinder. This is concrete causal evidence for one of the two claimed novelties.

- **The method produces executable, stage-annotated code as output.** The case study (Figure 4) shows that PoTable generates complete Python programs with clear comments demarcating each stage's operations. This is more informative than Binder's single-shot program or Chain-of-Table's black-box atomic operations, providing a genuine explainability benefit beyond raw accuracy.

## Weaknesses

### Fatal
None.

### Major

- **The open-world operation space claim is not separately ablated.** The paper lists two explicit novelties (Section 2.5): (1) human-like stage split, and (2) open-world operation space. The ablation study (Figure 3) tests only stage-split variants. There is no experiment that constrains the operation pool (e.g., limiting the planner to a fixed set of pandas operations resembling Chain-of-Table's pool) while keeping the stage split intact. Without this, the relative contribution of each claimed novelty is unknown — the gains could be primarily from the staging, primarily from the open-world flexibility, or from their interaction. The paper's own framing in Section 2.5 elevates both to equal standing, making this gap consequential for the claimed contributions.

- **No statistical variance or confidence information.** All results in Table 1 are single-point accuracies. On LLAMA, PoTable's TabFact improvement over Chain-of-Table is only +1.44% (87.06 vs. 85.62). LLM-based code generation with sampling is inherently stochastic (temperature, retry outcomes), yet the paper reports no standard deviations, multi-run averages, or even a note about run-to-run stability. This makes it impossible to assess whether the smaller LLAMA gains are stable or within noise. While single runs are common in this area, the paper should at minimum acknowledge the limitation.

### Minor

- **Cost/efficiency trade-off is undocumented.** PoTable makes multiple LLM calls per sample (one planning call per stage, one code generation call per operation, plus up to 10 retries per operation on error). This is almost certainly far more expensive than Binder (a single program generation call) or Chain-of-Table (one planning call + final LLM query). Accuracy gains are reported, but the corresponding cost in API calls, latency, or tokens is never mentioned. A method that achieves +4% at 10× the cost is a different contribution from one achieving it at comparable cost. This omission limits practical assessment.

- **Ablation study uses only the GPT backbone.** The ablation in Figure 3 is conducted only with GPT-4o-mini. Repeating it on LLAMA would strengthen the claim that the stage split is generally beneficial and not a quirk of the GPT model.

- **Few-shot prompting examples are not described.** The paper mentions "three self-made examples" for planning and final-answer code generation (lines 124, 127, 211) but does not describe their content or selection process. This is a minor reproducibility gap, though presumably the examples would appear in supplementary materials.

### Trivial
- The paper calls the stage split "human-like" (line 99, 103, 179) but provides no supporting evidence from cognitive science — it is a design analogy. This is a presentation choice, not a flaw, but the framing slightly overstates the claim. A brief acknowledgment that this is an intuitive split rather than a validated cognitive model would be cleaner.

## Nice-to-Haves

- **Constrained-operation ablation.** Adding a variant of PoTable that restricts the planner to a fixed pandas operation set (similar to Chain-of-Table's atomic pool) would cleanly separate the stage-split contribution from the open-world contribution. If open-world still wins, both claims are supported. If not, the paper should honestly reframe its contributions.

- **Error analysis and stage-usage statistics.** It would be informative to report how often retries occur per stage, which error types are most common, and how often the row selection / data type cleaning stages actually modify the table (vs. being no-ops).

- **A "single-stage, stepwise" baseline.** A variant without the explicit stage split but still generating code stepwise per operation would help isolate whether the benefit comes from the *specific five stages* or simply from decomposing the process into multiple steps.

## Removed Points

These points were identified in the reviews but are removed here because they are factually wrong, speculative, or do not constitute genuine weaknesses:

- **Abstract missing "GPT-based" qualifier.** The harsh critic claimed the abstract states "over 4% higher absolute accuracy" without specifying GPT. This is factually wrong — line 12 reads: "*GPT-based* PoTable achieves over 4% higher absolute accuracy..." The qualifier is present. **Removed (factually incorrect).**

- **Chain-of-Table scores "appear lower than expected."** The reviewer speculates that Chain-of-Table's reported scores (e.g., 55.60 on WikiTQ test) are lower than the original paper's numbers. The original Chain-of-Table paper used GPT-3.5 and GPT-4, while this paper uses GPT-4o-mini — a different, less capable model. There is no ground-truth expectation to violate. **Removed (speculative, no factual anchor).**

- **Case study is only one sample / not statistically meaningful.** Single-sample case studies are standard practice in NLP papers for qualitative illustration. This is not a weakness; no reader expects statistical significance from a figure showing generated code. **Removed (not a genuine weakness by community standards).**

- **Generic "more baselines" / "larger dataset" / "add more models" style criticisms.** These did not appear in the specific reviews for this paper, but any such generic sweep would be removed as category-driven noise.

## Novel Insights

None beyond the paper's own contributions. The reviews did not uncover insights about the method that the paper itself does not articulate.

## Suggestions

1. **Add a constrained-operation ablation.** Run PoTable with a restricted set of ~15–20 common pandas operations (matching Chain-of-Table's style) while keeping the five-stage split. Compare against full open-world PoTable. This is the single most important experiment to strengthen the paper.
2. **Report variance or run-to-run stability.** Even a brief note ("we ran a 100-sample subset three times and observed std < 0.5%") would substantially increase confidence in the results, particularly the smaller LLAMA gains.
3. **Document average LLM call count and estimated cost per sample** for PoTable versus at least one baseline (e.g., Binder). This allows readers to assess the accuracy/cost trade-off.
4. **Acknowledge the open-world limitation** in the paper itself if the ablation cannot be added, and soften the dual-contribution framing to reflect which claim is directly supported by evidence.
