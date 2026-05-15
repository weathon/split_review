Now I have a clear picture of the paper and can verify each claim against the source.

## Summary

Herald introduces a structural-information-aware pipeline for generating a large NL-FL parallel dataset from Mathlib4 (Lean 4). The key innovation is a hierarchical, dependency-aware translation process that translates theorems in topological order of their dependency DAG, combined with dual augmentation (tactic-based subgoal extraction and LLM-based paraphrasing). The authors fine-tune DeepSeek-Prover-Base 7B on this dataset to create the Herald Translator, reporting 93.2% on miniF2F-test and a successful autoformalization of a Stacks Project section.

## Strengths

- **Hierarchical dependency-aware translation (Sections 3.1.1)** is a genuine structural innovation. Prior work translates statements in isolation; Herald instead extracts the dependency DAG of Mathlib4 via Lean-Jixia and translates in topological level order, ensuring the LLM has NL annotations of all dependencies before translating the target theorem. This addresses a clear failure mode in prior work and is well-motivated by the paper's own analysis.

- **Dual augmentation strategy (Sections 3.2.1–3.2.2)** is creative and addresses two real problems: data scarcity and distribution imbalance. The tactic-based augmentation extracts subgoal statements from intermediate proof states (validated by the Lean compiler), producing 580k additional statements from ~110k proved theorems. The LLM-based augmentation (logical equivalence rewriting, abstract substitution, omission of implicit conditions, multilingual translation) diversifies NL phrasing. Both are principled approaches to dataset expansion.

- **Strong miniF2F results**: Herald achieves 93.2% (test) / 96.7% (valid) on miniF2F, a 20+ point improvement over InternLM2-Math-Plus-7B (73.0%/80.1%) and ~43 points over TheoremLlama (50.1%/55.6%). Even accounting for evaluation protocol questions, the gap is large enough on a standard benchmark to represent genuine progress.

- **Human-in-the-loop refinement (Section 3.1.1)**: Six rounds of feedback from five PhD-level mathematicians produced explicit principles incorporated into translation prompts. This is a more rigorous approach to NL quality than the purely automatic bootstrapping in TheoremLlama or Lean-STaR.

- **Practical demonstration on graduate-level literature (Section 4.3)**: The pipeline successfully autoformalized a full section of the Stacks Project (Normal Extensions, Tag 09HL) into runnable Lean 4 code with only two minor theorem modifications needed. This goes beyond textbook-exercise evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation protocol for baselines is insufficiently specified, raising questions about fairness**: The paper states it compared Herald "with several models in similar settings" (line 227) but never clarifies: (a) whether baselines were run zero-shot or fine-tuned, (b) whether the same Pass@128 inference budget was used for baselines, and (c) whether the back-translation + NLI validation pipeline (Section 4.1.2) was applied to baseline outputs or only to Herald's. The note about "manually adding a generic header" and "truncating generation to obtain a maximal possible statement" (line 257) for baselines suggests non-standardized handling. Since Herald is fine-tuned on 580k+ NL-FL pairs while baselines may not be comparably trained, the gap on internal datasets (22.5% vs 7.5%) cannot be confidently attributed to the Herald methodology without controlled experiments. The authors should either (i) fine-tune all baselines on the same training data, or (ii) clearly document the exact evaluation protocol used for each baseline.

- **Dataset statistics contain arithmetic inconsistencies that undermine trust in reporting**: 
  - The abstract (line 5) and contributions (line 28) state the dataset contains "580k valid statements" (as the total), while Table 1 lists 291k original statements + 580k augmented statements = 871k total. Whether 580k is the total or only the augmented portion is never clarified.
  - The introduction (line 22) and contributions (line 29) report TheoremLlama's miniF2F score as 55.0%, but Table 1 correctly reports it as 50.1% (test) — the abstract (line 5) correctly uses 50.1%. The incorrect 55.0% appears twice in the paper.
  - Section 3 (line 70) reports "45k NL-FL proof pairs" while the abstract and Table 1 say 44k.
  
  These are fixable presentation errors but they create the impression of carelessness with numbers, which is especially problematic for a paper whose central claims are quantitative.

### Minor

- **Internal test sets (Extract Theorem, College CoT) are only 200 samples each with no confidence intervals or error bars reported**: The paper acknowledges these are "shuffled subsets of 200 samples each" (Table 2 caption). For N=200, a single success or failure changes the reported percentage by 0.5 percentage points. The lack of any variance estimation makes it impossible to assess whether the reported gaps (e.g., 22.5% vs 7.5%) are statistically robust. The authors should report bootstrapped confidence intervals or at minimum note the standard error.

- **Quality validation of the generated dataset is superficial**: The only quality assessment is a brief "case study" (Section 4.2) that acknowledges issues ("notations and formulas are either well-written... or poorly copied from formal language," "the level of detail... is closer to formal language"). No quantitative human evaluation, inter-annotator agreement, or systematic error classification is provided. Given that the paper criticizes prior NL-FL datasets for having "intrinsic weaknesses of LLMs" (Section 2, line 58) — a concern that applies equally to Herald's own LLM-based augmentation — the lack of rigorous validation is a gap. A human evaluation of 200–500 sampled pairs across augmentation sources would significantly strengthen the paper.

- **Back-translation uses InternLM2-Math-Plus-7B as a validator (Section 4.1.2), which is also a baseline**: The validation pipeline uses InternLM2-Math-Plus-7B to back-translate Herald's formal outputs back to NL for an NLI consistency check. This creates a potential confound: if this filter aggressively discards outputs that InternLM2 cannot back-translate, Herald's reported accuracy may be inflated relative to baselines that are not subjected to the same filter. The paper should clarify whether all models' outputs pass through the same validation pipeline or whether the table reports raw generation accuracy for baselines and filtered accuracy for Herald.

### Trivial

- Inconsistent proof pair count: Section 3 says "45k NL-FL proof pairs" while abstract and Table 1 say "44k." Minor typo.
- The "55.0% vs 50.1%" discrepancy for TheoremLlama is limited to the Introduction and Contributions — the Abstract correctly reports 50.1%. An editorial fix.

## Nice-to-Haves

- An ablation study training separate models on only original statements, only tactic-augmented, and only LLM-augmented data would quantify each augmentation strategy's contribution.
- An error analysis of the 6.8% of miniF2F-test statements that Herald fails on (syntax errors vs. semantic errors vs. missing imports) would help identify the method's remaining limitations.
- Evaluation on additional standard formalization benchmarks (e.g., ProofNet, FIMO) would strengthen claims of generality beyond miniF2F.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Abstract says TheoremLlama 55.0%"** — This is factually incorrect. The abstract (line 5) correctly says 50.1%, matching Table 1. The 55.0% appears in the Introduction and Contributions, not the abstract. The reviewer's framing was inaccurate.

- **"The 110k vs 291k inconsistency"** — The 110k refers to the count of theorems *with proofs* used for tactic-based augmentation, while 291k refers to all statements (including definitions, instances, structures, etc.) informalized by the pipeline. These are different counts for different sub-corpora; this is not necessarily an inconsistency, though the paper could clarify this.

- **"Only one Stacks Project section attempted; prover proved only one theorem — too thin to demonstrate real-world applicability"** — This criticism understates the result. The paper's claim is about *formalization* (translating NL mathematics into runnable Lean code), not about automated proving. The entire section was successfully formalized into Lean 4 code with only two theorem modifications. The fact that the auto-prover only proved one theorem is presented transparently as a limitation and a direction for future work, not as a core claim.

- **"The 1,000 manually annotated examples are opaque"** — While the paper could say more about the annotation process, requiring a detailed cost/quality breakdown for a training-set construction detail is not standard for a systems paper. This is a reasonable implementation detail, not a flaw.

- **"The critique of prior NL-FL datasets applies equally to Herald's own LLM-based augmentation"** — This is partially true but ignores that Herald's augmentation pipeline includes the Lean compiler for formal validation and the back-translation + NLI pipeline for semantic validation, which is more rigorous than the prior work it criticizes. The critique applies but is weakened.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension well: the paper's core methodological contribution (hierarchical dependency-aware translation) is novel and well-motivated, but the evaluation is reported with insufficient rigor to fully substantiate the claimed margins of improvement, particularly on internal datasets. The most important unresolved question is whether the 20+ point gap on miniF2F would persist under a fully controlled evaluation where all models share the same training data, inference budget, and validation pipeline.

## Suggestions

1. **Clarify the evaluation protocol in full**: State explicitly (a) whether each baseline was fine-tuned or used zero-shot, (b) whether the same Pass@128 budget was used for all models, (c) whether the back-translation/NLI filter was applied to all models' outputs or only Herald's, and (d) the exact post-processing applied to each model's raw generations.

2. **Fix the dataset statistics**: Reconcile the abstract's "580k valid statements" with Table 1's 291k + 580k breakdown. Decide whether "580k" refers to the total or the augmented portion and be consistent throughout.

3. **Report confidence intervals for the 200-sample datasets**: A simple bootstrapped 95% CI would address the reviewer concern about statistical significance.

4. **Include a small human evaluation of dataset quality**: Have 2–3 expert annotators rate 200 sampled NL-FL pairs (50 from each augmentation source) for correctness and naturalness, with agreement metrics. This need not be large to be informative.

5. **Correct the TheoremLlama score**: The Introduction (line 22) and Contributions (line 29) should use 50.1% (test) to match the table and abstract, not 55.0% (which is close to the valid split).

## Score and Decision

The paper presents a well-motivated methodological contribution (hierarchical dependency-aware translation) with creative data augmentation strategies and a practical demonstration on the Stacks Project. The miniF2F results are impressive even conservatively assessed. However, the evaluation reporting is incomplete in ways that make the headline numbers difficult to fully interpret — particularly the unspecified baseline protocol and the dataset statistic inconsistencies. These are fixable with clarification and minor corrections, not fatal flaws. The core contribution is solid and the paper represents meaningful progress for the NL-FL dataset generation and autoformalization community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>