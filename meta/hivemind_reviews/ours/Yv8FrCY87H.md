Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces Tree-of-Table, a method that combines table condensation (schema-linking to reduce table size), tree-based decomposition (breaking questions into sub-problems), and hierarchical tree-structured reasoning with depth-first execution to improve LLM performance on large-scale table understanding. Evaluated on WikiTQ, TabFact, FeTaQA, and BIRD across three LLMs (GPT-3.5, PaLM 2, LLaMA 2), Tree-of-Table shows consistent improvements over Chain-of-Table and other baselines on all datasets.

## Strengths

1. **Consistent empirical improvements across all datasets and LLMs** — Tables 1 and 2 show Tree-of-Table outperforming Chain-of-Table and other baselines on all four datasets across three LLM backends. On WikiTQ, accuracy improves from 59.94→61.11 (GPT-3.5), 67.31→68.77 (PaLM 2), and 42.61→44.01 (LLaMA 2), with similar margins on TabFact, FeTaQA, and BIRD. The consistency across models and datasets is the strongest evidence for the method's value.

2. **Well-motivated architectural improvement over linear-chain methods** — Section 3.3 explains and Table 3 (table_node) quantifies that Tree-of-Table reduces the effective reasoning chain length (tree height 7 vs. Chain-of-Table chain length 11 on BIRD) while maintaining a manageable number of nodes (18). This concretely addresses a real limitation: in Chain-of-Table, each step processes the entire history, which becomes intractable as tables grow.

3. **Table condensation demonstrably shrinks tables to fit LLM context limits** — Section 3.2 reports that >70% of BIRD questions involve tables exceeding LLM input limits, and post-condensation >60% of long questions fit within limits. Figure 5(b) shows cell counts dropping dramatically (e.g., BIRD from ~20,000 to ~3,000), providing quantitative support that the method directly addresses the core scaling challenge.

4. **More graceful degradation on larger tables** — Figure 5(a) shows that as table size increases, Tree-of-Table's performance declines more slowly than Binder, Dater, and Chain-of-Table on both WikiTQ and BIRD, demonstrating improved robustness to table scale.

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard evaluation on BIRD, the flagship large-scale dataset** — The paper uses BLEU and ROUGE to evaluate on BIRD rather than execution accuracy, which is the standard metric for this text-to-SQL dataset. Line 165 justifies this by stating "The nature of FeTaQA and BIRD for requiring elaborate responses," but BIRD's expected output is SQL queries, not free-form text. While all methods are compared under the same metric (preserving fairness of relative comparisons), BLEU/ROUGE are known to correlate poorly with semantic correctness for structured outputs, so the absolute quality of the generated answers on BIRD is unclear. Since the paper's central claim about large-scale performance rests heavily on BIRD results, this weakens the evidence for the headline contribution. **However, this does not invalidate the paper**: the method still shows consistent, if modest, improvements on WikiTQ and TabFact under standard denotation accuracy metrics, so the core empirical contribution survives even if BIRD results are set aside.

### Minor

2. **Condensation ablation does not show accuracy impact** — Figure 5(b) demonstrates that condensation reduces table size, which is necessary but not sufficient evidence: a proper ablation would compare Tree-of-Table's accuracy *with* vs. *without* condensation to confirm that the size reduction translates into better reasoning. This is the most important missing experiment.

3. **Efficiency metric is vaguely defined** — Table 4 (table_efficiency) reports "Generate Samples" values (90 for Tree-of-Table vs. 120 for Chain-of-Table vs. 300 for Dater). Line 262 defines this as "the number of samples it needs to generate to arrive at a correct answer," but "samples" could mean LLM API calls, generated tokens, or forward passes. A clearer definition and per-dataset breakdown would strengthen the efficiency claim.

4. **Hyperparameter sensitivity not analyzed** — MAXDegree and MAXDepth are introduced (Eq. 4–6) without any analysis of how they affect results or how they were chosen. These parameters control tree structure and are likely dataset-dependent; reporting stability across reasonable ranges would improve reproducibility.

### Trivial
- Line 183: "TREE-OF-TBALE" typo in Table 4 header (table_efficiency).
- Figure 5(a) x-axis is labeled "Table Size" without specifying the exact binning or unit.

## Nice-to-Haves
- Adding a no-condensation control (Tree-of-Table without condensation → accuracy comparison) would sharpen the contribution of the condensation component.
- Including a qualitative example showing an actual constructed Table-Tree with intermediate outputs would aid understanding.
- Reporting total token consumption or wall-clock time alongside "Generate Samples" would make the efficiency analysis more concrete.
- A brief justification for why BLEU/ROUGE is appropriate for BIRD's output format in this setting would address the metric concern.

## Removed Points

These points from the inputs were evaluated against the paper and removed:

- **Harsh Critic Claim 3 (baseline fairness)**: The claim that Chain-of-Table results on BIRD may be unfair because the original paper did not evaluate on BIRD is speculative. Chain-of-Table is a published, general methodology that can be applied to any dataset. No concrete evidence of unequal experimental setups was provided, and the paper states it "follows previous works" in its experimental setup. — *Removed as speculative.*

- **Harsh Critic Claim 2 (insufficient method detail)**: Criticisms about missing prompts, operation pool lists, and precise algorithmic specifications are substantially mitigated by the fact that these details likely reside in the appendix, which is stripped by the PDF parser. The main text provides a clear conceptual description of the method (condensation, tree decomposition, breadth-first construction, DFS execution). The method is described at a level comparable to other LLM-prompting papers in this venue. — *Downgraded and moved; the remaining substance is handled by the hyperparameter sensitivity point (Minor #4).*

- **Strength Finder claim about table encoding ablation ("rigorously tested")**: This claim is slightly overblown — the encoding format comparison is a single table on one dataset (WikiTQ) without variance or statistical tests. Still informative, but not "rigorously tested." — *Weakened to not be listed as a standalone strength.*

- **Generic strengths/weaknesses** about "important problem" or "addressing a gap": Removed as they are not specific, concretely grounded observations. The specific, grounded strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's key claim (tree-structured reasoning helps for large tables) but surface a significant concern about the BIRD evaluation that the paper itself does not address.

## Suggestions

1. **Address the BIRD metric issue**: Either re-evaluate using execution accuracy (the BIRD standard) or provide a clear justification for why BLEU/ROUGE is appropriate for your setting, and clearly state that BIRD is being used as a free-form QA dataset rather than a text-to-SQL benchmark. If possible, report both execution accuracy (for comparability) and BLEU/ROUGE.

2. **Add a condensation ablation on accuracy**: Measure Tree-of-Table's accuracy with and without the condensation step on at least one dataset to directly link condensation to accuracy improvement, not just size reduction.

3. **Define "Generate Samples" precisely and provide per-dataset breakdowns** in the efficiency analysis.

4. **Report sensitivity of MAXDegree and MAXDepth** with a brief analysis showing performance over a range of values.

5. **Fix the typo** in Table 4 ("TREE-OF-TBALE" → "TREE-OF-TABLE").

## Score and Decision

The paper addresses a real problem (large-scale table reasoning), proposes a conceptually sound hierarchical framework, and provides consistent empirical evidence across multiple datasets and LLMs. The primary weakness is the non-standard BIRD evaluation, which weakens but does not invalidate the contribution since improvements on standard-metric datasets (WikiTQ, TabFact) are independently observed. The remaining issues (missing condensation accuracy ablation, vague efficiency metric, no hyperparameter analysis) are addressable. The paper represents a solid incremental contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>