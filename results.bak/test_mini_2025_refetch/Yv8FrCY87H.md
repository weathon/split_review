Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper proposes Tree-of-Table, a method that enhances LLM reasoning over large tables via (1) Table Condensation — schema-linking and merging to fit tables within context limits, and (2) hierarchical Table-Tree construction via breadth-first thought decomposition executed with depth-first search. Experiments on WikiTQ, TabFact, FeTaQA, and BIRD across GPT-3.5, PaLM2, and LLaMA2 report consistent improvements over baselines including Chain-of-Table.

## Strengths

1. **Table Condensation demonstrably addresses context-limit overflow** — Section 3.3.1 reports that over 70% of BIRD questions involve tables exceeding LLM input limits, and after condensation the length falls below the limit for more than 60% of those. Figure 4(b) quantifies the reduction (BIRD: 1,798 nodes → 348). This directly targets a key obstacle that prior methods (Chain-of-Table, Dater) do not explicitly tackle.

2. **Tree-structured reasoning reduces required depth compared to linear Chain-of-Table** — Table 3 shows that on BIRD, Tree-of-Table's average height is 7 vs. Chain-of-Table's chain length of 11; on WikiTQ it is 3 vs. 4, on TabFact 3 vs. 4. This provides empirical evidence that tree decomposition yields a more compact reasoning chain.

3. **Consistent improvements on standard metrics across three small/medium datasets** — On WikiTQ and TabFact (Table 1), Tree-of-Table outperforms all baselines including Chain-of-Table across all three LLMs. On FeTaQA (Table 2), the method improves BLEU from 32.61 to 34.73 and ROUGE-L from 0.56 to 0.58. These datasets use standard evaluation metrics, and the gains are consistent.

4. **Better sample efficiency** — Table 5 shows Tree-of-Table requires 90 generated samples to reach correct answers on BIRD vs. 120 for Chain-of-Table and 300 for Dater. While the "Generate Samples" metric is not fully defined, the reduction is substantial.

5. **Better generalization across table sizes** — Figure 4(a) shows Tree-of-Table's performance declines more gradually than Binder, Dater, and Chain-of-Table as table size increases, and it maintains the highest absolute performance at every size on both WikiTQ and BIRD.

## Weaknesses

### Major

1. **BIRD evaluation uses non-standard metrics, limiting comparability and supporting only a weak claim.** The paper evaluates BIRD using BLEU and ROUGE (Table 2). BIRD (Li et al., 2024) is a text-to-SQL benchmark whose standard evaluation metric is execution accuracy. The paper treats it as a free-form QA task without reporting execution accuracy. While the comparison among methods within Table 2 is internally consistent (all baselines use the same metrics), the results cannot be compared to the broader BIRD literature. The paper's headline claims of "superior performance" and "new benchmark" on large-scale tables (Abstract, Section 4.2) are therefore only supported within a non-standard evaluation framework. The low BLEU scores (9.90–15.70) further suggest the metric may not be well-suited to this task. **Why it matters:** This weakens the paper's central claim about large-scale table understanding. Without standard execution accuracy, the BIRD results do not carry the weight the paper assigns them.

2. **Ablation does not isolate the tree-based reasoning contribution from table condensation.** Tree-of-Table has two components: table condensation (schema-linking + merging) and tree-structured reasoning (decomposition + hierarchical execution). The ablation in Section 4.3 tests neither in isolation. There is no variant "Tree-of-Table without condensation" (applying the same tree method to the original full table) nor a variant "Chain-of-Table + condensation" (controlling for the preprocessing). Table condensation alone reduces table size by 4–5× (Figure 4b); this preprocessing likely accounts for a large fraction of the gain. The paper notes that "Chain-of-Table does not preprocess complex tables" (Section 3.6), yet presents the end-to-end improvement as evidence for the tree structure. **Why it matters:** Without this control, it is impossible to attribute the observed gains to the tree reasoning structure vs. the condensation preprocessing. This undermines the paper's core claim about hierarchical reasoning being superior.

### Minor

3. **Figure 1's motivating example is inconsistent.** The table in Figure 1 (lines 29–36) shows columns Year, Country, Consumption, Percentage Increase with data for USA, Canada, Mexico. The question asks about "SME, LAM and KAM" segments, but the illustrated table contains no Segment column. The question cannot be answered from the table that is displayed. This is the paper's central motivational figure and this inconsistency undermines its illustrative value. (Note: Figure 2's garbled "Original tables" block appears to be a PDF parsing artifact and is not relevant to this criticism.)

4. **No statistical significance or variance is reported.** All results in Tables 1, 2, and the ablation are presented as point estimates without standard deviations, confidence intervals, or runs with different seeds. Given that the improvements on WikiTQ and TabFact are 1–2% (Table 1), these could be within the noise of prompt variation. This is standard practice for this type of work, but the small margin makes it more consequential.

5. **Several implementation details are unspecified.** The paper does not state: the number of few-shot demos per prompt, the demo selection strategy, the number of LLM calls per sample for condensation, or the exact failure rate of the condensation procedure. These details matter for reproducibility and fairness of comparison.

## Nice-to-Haves

- An ablation varying MAXDepth and MAXDegree to demonstrate that the tree structure specifically adds value beyond a chain with a similar number of steps.
- Reporting execution accuracy on BIRD's dev set using the standard split, to enable comparison with the broader literature.
- An error analysis showing how often the LLM fails to generate a valid tree or produces incorrect intermediate tables.

## Removed Points

- *"Figure 2 original tables show garbled numerical data"* — This is a PDF parsing artifact, not a paper problem.
- *"Comparison with Chain-of-Table is not a fair head-to-head because of LLM call count / prompt structure"* — The paper does report sample efficiency (Table 5), and the critic's claim about "no control" for prompt structure is speculative without evidence that the baseline's prompts were disadvantaged.
- *"Section 3.3.1 analysis has no reproducibility details"* — The BIRD table-size statistics are observations about the dataset, not experimental results requiring reproducibility.
- *"Equations 4–6 are not operational"* — The equations describe the method at the appropriate level of formality for a conference paper; full operational details belong in supplementary.
- *"Table 2 BIRD baseline numbers are extremely low"* — Low absolute scores reflect task difficulty, not a methodological flaw.
- Several generic "nitpick" criticisms about presentation and missing appendix content (stripped by parser).

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis surfaces a key conflict: the paper claims a tree-structured reasoning advantage, but the ablation confound means the advantage could come primarily from the condensation step. This is the central unresolved question that neither reviewer individually addressed with this clarity.

## Suggestions

1. **Run the controlled comparison** — compare (a) Tree-of-Table without condensation vs. (b) Chain-of-Table + condensation. This is essential to attribute gains to the tree structure.
2. **Report BIRD execution accuracy** using the standard evaluation protocol. Even as a supplementary metric alongside BLEU/ROUGE, this would substantially strengthen the large-scale claims.
3. **Fix Figure 1** so the table actually contains the Segment column that the question refers to.
4. **Report variance** — run each experiment 3–5 times with different demo seeds and report mean ± std.
5. **Specify the number of few-shot demos** and demo selection strategy for reproducibility.

## Score and Decision

### Round 1 — Bracketing
Three queries on table understanding/reasoning topics with score bands:
- **Weak anchors** (avg < 3.5): "The Role of Deductive and Inductive Reasoning in LLMs" (3.40, Withdrawn), "Planning in Strawberry Fields" (3.00, Withdrawn), "GTD-LLM" (3.40, Withdrawn), "Meta-CoT" (3.00, Reject). These are lower-quality or unrelated papers. The Tree-of-Table paper is clearly stronger than these.
- **Middle anchors** (3.5 < avg < 7.5): "Chain-of-Table" (5.50, Accept poster) — the direct baseline; "TAMO" (5.75, Reject); "PoTable" (4.25, Reject); "UniPredict" (5.20, Reject). Tree-of-Table sits in this band.
- **Strong anchors** (avg > 7.5): "BIRD Bayesian framework" (8.00, Oral), "Phenomenal Yet Puzzling" (8.00, Oral), "PTaRL" (8.00, Spotlight), "miniCTX" (8.00, Oral). These are clearly stronger papers. Tree-of-Table is well below these.

**Round 1 bracket: 4.0–6.0**

### Round 2 — Narrowing
Two queries refining within the bracket:
- **Chain-of-Table** (5.50, Accept): Tree-of-Table extends this work with a novel tree structure and condensation, but has more significant evaluation gaps (non-standard BIRD metrics, confounded ablation). Tree-of-Table is slightly weaker.
- **PoTable** (4.25, Reject): Tree-of-Table has clearer novelty, broader evaluation (4 datasets vs 2), and addresses a more important gap (large-scale tables). Tree-of-Table is clearly stronger.
- **TAMO** (5.75, Reject): Comparable level of methodological contribution. TAMO was rejected due to novelty concerns and complexity; Tree-of-Table has more straightforward evaluation gaps. Roughly comparable.

**Final position:** Closer to the lower end of the bracket. The paper has a solid core idea but the two Major weaknesses (non-standard BIRD metrics, confounded ablation) are more consequential than the issues in the accepted Chain-of-Table anchor. Below Chain-of-Table (5.50) but above PoTable (4.25).

### Final Score and Decision

**Score: 5.0** — Marginally below the acceptance threshold. The paper proposes a sensible and well-motivated approach, but the evaluation has two significant gaps that prevent the core claims from being fully supported. With the suggested controlled ablation and standard BIRD metrics, the paper could be substantially strengthened.

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>