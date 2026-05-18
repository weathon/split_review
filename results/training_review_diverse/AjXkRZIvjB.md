Now I have a complete picture of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces GSM-Symbolic, a benchmark built from symbolic templates that generate diverse variants of GSM8K grade-school math questions by systematically varying names, numerical values, and clause counts. Using this framework, the authors conduct a large-scale study across 25 open and closed LLMs, producing four main findings: (1) model performance shows substantial variance across different instantiations of the same question, (2) models are more robust to name changes than to numerical value changes, (3) performance degrades non-linearly as clause count (difficulty) increases, and (4) adding seemingly relevant but logically irrelevant clauses (GSM-NoOp) causes catastrophic performance drops of up to 65%, even when models are given few-shot examples of the exact same question. The paper argues these findings collectively show that LLMs do not perform genuine formal reasoning but instead rely on probabilistic pattern matching.

## Strengths

- **GSM-Symbolic provides a principled framework for controllable evaluation.** By converting static GSM8K questions into symbolic templates with well-defined variable domains and constraints (Section 3.1, Figure 1), the paper moves beyond single-point accuracy metrics to study performance as a distribution. This design choice is demonstrated to be informative: Figure 2 shows that models exhibit 10–15% accuracy variance across 50 different instantiations of the same question, a phenomenon invisible in standard GSM8K evaluation.

- **Large-scale systematic evaluation across 25 models.** The paper evaluates nearly 500 model–benchmark combinations (Section 3.2), spanning models from 2B to 27B parameters plus closed models (GPT-4o, o1-mini, o1-preview). This breadth allows the paper to establish findings that hold consistently across model families, sizes, and training paradigms—not just on a cherry-picked subset.

- **GSM-NoOp reveals a deep and robust failure mode.** The finding that adding a single irrelevant clause causes up to 65% performance drops, and that this drop persists even when models receive 8-shots of the *exact same question without the NoOp clause* (Figure 8b), is the paper's strongest result. It goes substantially beyond prior work (GSM-IC, which focused on prompting mitigation) by showing the problem is deeper than surface-level distraction.

- **Fine-grained ablation of name vs. number sensitivity.** Figure 4 cleanly disentangles two sources of variation: changing only proper names shifts distributions modestly with GSM8K accuracy near the center, while changing numbers causes larger shifts and higher variance. This ablation provides concrete evidence about *what kind* of changes break models.

- **Non-linear difficulty scaling is consistent across models.** As difficulty increases (M1 → Symbolic → P1 → P2), every model shows the same pattern: mean accuracy drops and the *rate* of drop accelerates (Figure 6). This consistency across models supports the paper's hypothesis that LLMs perform probabilistic pattern matching rather than formal reasoning, since formal reasoning would degrade roughly linearly with step count.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The data contamination speculation is weakly supported and partly undercut by the paper's own ablation.** The paper states (Section 4.1, line 149) that the right-tail position of GSM8K accuracy in the GSM-Symbolic distribution "could be data contamination." However, the ablation in Section 4.2 shows that when *only names* are changed (keeping original numerical values), GSM8K accuracy is close to the center of the distribution—the drop is driven by numerical changes. If contamination were the primary explanation, the name-only condition should also show a right-tail effect, but it does not. The paper already hedges ("could be," "hinting at"), but the speculation is inconsistent with the paper's own evidence and distracts from the stronger finding that models are genuinely sensitive to numerical variation. The paper would be better off dropping this speculation entirely.

- **The inference from variance to "lack of genuine reasoning" lacks a normative baseline.** The paper treats performance variance across instantiations as evidence against formal reasoning, stating that such variance "would not be expected from a grade-school student with genuine mathematical understanding" (Section 4.2, line 186). But different numerical instantiations involve different arithmetic operations (carrying, borrowing, different magnitude numbers) that could produce variance even in a competent human reasoner. Without a human baseline or even a discussion of what level of variance *would* be consistent with genuine reasoning, this interpretive claim is undersupported. The NoOp findings (Section 4.4) provide much stronger evidence against formal reasoning independently, so this weakness mainly affects the framing in Sections 4.1 and 4.2.

- **Limited template diversity for the scope of claims.** The benchmark uses 100 templates from GSM8K (Section 3.2). While 5,000 total questions is a reasonable evaluation size, 100 templates constrain the diversity of reasoning patterns tested. The paper makes broad claims about "the limitations of mathematical reasoning in LLMs" but the evidence comes from a single source of grade-school arithmetic problems. The conclusion does note this limitation (line 326), but the paper's framing in the abstract and introduction is more expansive than the evidence base supports.

### Trivial
- **No dedicated limitations section.** The paper does not include a formal discussion of limitations. The conclusion mentions the grade-school-level scope, but the paper would benefit from a brief section acknowledging that conclusions are based on 100 templates from one dataset, greedy decoding throughout (Section 3.2), and one-shot/eight-shot settings only.

## Nice-to-Haves

- **Categorize NoOp failures by clause type.** The paper groups all NoOp additions together, but the type of irrelevant clause likely matters (e.g., clauses about "smaller than average" inviting subtraction vs. clauses about "discounts" inviting multiplication). A breakdown by clause type would deepen the phenomenological account and could reveal non-trivial patterns about which constructions models are most susceptible to.
- **Qualitative error analysis on GSM-Symbolic.** The paper does not systematically analyze *what* models get wrong when they fail on value-changed instantiations. Are errors primarily arithmetic miscalculations, misinterpretation of problem structure, or systematic off-by-one issues?
- **Human baseline or reference point for variance.** Even a small-scale comparison (e.g., a handful of humans on a subset of instantiations) would clarify whether the observed variance pattern is pathological or within a reasonable expected range.

## Removed Points

- *Criticism that the paper does not release the benchmark/templates in the current submission.* Per the hard rules, cited models, tools, benchmarks, and datasets are assumed to exist. The paper describes GSM-Symbolic and its templates; questions about release status/format do not affect the validity of the scientific contribution.
- *Criticism about missing appendix content, proofs, or references.* The parser strips these sections from all papers; they exist in the original submission.
- *Suggestion to compare against closed-source models requiring weight access for probing experiments.* GSM-Symbolic is a benchmark for evaluating reasoning, not a mechanistic analysis tool; closed models are evaluated on the benchmark itself as appropriate.

## Novel Insights

The synthesis of the reviews surfaces a tension the paper does not fully address: the contamination speculation (Section 4.1) and the name-vs-number ablation (Section 4.2) are in partial conflict. The right-tail effect of GSM8K accuracy is attributed to possible contamination, yet the ablation shows the effect nearly vanishes when only names change—implying numerical sensitivity, not contamination, drives the drop. The paper's strongest narrative thread (the NoOp results) is independent of this, but Sections 4.1–4.2 would benefit from reframing around what the data actually supports. A second insight from cross-referencing the reviews: the paper's core interpretive move—from variance to lack of formal reasoning—rests on an unstated assumption about how much variance a competent reasoner *should* exhibit. Making this assumption explicit and providing even a rough bound (e.g., perfect-reasoner simulation with controlled noise) would substantially tighten the argument.

## Suggestions

1. **Remove or substantially temper the data contamination speculation** (Section 4.1, line 149; contributions list, line 69). The paper's own ablation in Section 4.2 provides a more parsimonious explanation (numerical sensitivity). Reframe the GSM8K-to-GSM-Symbolic drop as a direct demonstration of sensitivity to numerical variation—this is itself an important finding and does not require invoking contamination.

2. **Add an explicit caveat to the variance-based claims** in Sections 4.1 and 4.2, acknowledging that the normative level of variance for a competent reasoner on these problems is unknown. Alternatively, simulate a perfect reasoner with controlled arithmetic noise to provide a reference point.

3. **Add a brief limitations paragraph** covering the scope (100 GSM8K templates, grade-school level only, greedy decoding) and noting that broader claims about "mathematical reasoning" may not generalize to harder math (e.g., algebra, geometry, competition problems).

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>