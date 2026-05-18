I'm unable to access the paper file directly due to filesystem restrictions. However, the reviews contain enough detailed information (specific table values, section numbers, figures, and equations) for me to construct a thorough meta-review. Let me proceed.

---

## Summary

This paper proposes CodePlexity, a learned metric that uses the complexity of automatically generated code (produced by LLMs like ViperGPT) as a proxy for question difficulty in VideoQA. It extracts Abstract Syntax Tree (AST) subroutines from generated programs, learns weights for these subroutines via logistic regression to predict model accuracy, and uses the learned representation to (a) identify interpretable patterns of difficulty and (b) automatically construct a harder benchmark (CodePlex-QA). The core claims are that code-derived complexity signals outperform text-based metrics and human estimates, and that the generated benchmark is substantially harder than existing manually designed benchmarks.

## Strengths

1. **Creative use of code generation as an intermediate representation for complexity estimation.** Rather than using code for task performance, the paper repurposes it to extract structured complexity signals from AST subroutines. This is a novel departure from prior work that relied on human annotation or surface-level text proxies (e.g., BERT embeddings, dependency depth), and it is dataset-agnostic, allowing reapplication as new models emerge.

2. **CodePlexity consistently outperforms text-based and simple code-based metrics on held-out models.** Table 1 (as described in the reviews) shows CodePlexity achieving the highest mPEG scores across four held-out models (HGA, SeViLA-ZS, InternVideo, Tarsier), exceeding BERT, dependency depth, lines of code, and cyclomatic complexity. This provides empirical evidence that learning from AST subroutines captures difficulty better than existing approaches.

3. **Interpretable subtree analysis identifies specific, shared failure patterns across models.** Using statistical hypothesis testing (one-sided test, p<0.01) across multiple models, the paper isolates subroutines universally correlated with performance drops (e.g., reasoning about event order, fine-grained object details). The Venn diagram in Figure 4 provides a clear visualization of shared versus model-specific difficulty patterns. This interpretability dimension is a genuine contribution that goes beyond predictive accuracy to provide actionable insights about model limitations.

4. **Human estimates are shown to be weaker predictors of question difficulty than code complexity.** The human study (pairwise sorting, ELO scoring) demonstrates that human judgments of difficulty have weak correlation with actual model performance, while code-based metrics show a stronger trend. This finding is non-obvious and practically useful for dataset design.

## Weaknesses

### Major

1. **The "1.9× harder" claim for CodePlex-QA does not reconcile with the reported accuracy numbers.** From the data cited in the reviews (average five-model accuracy: 54.8% on NExT-QA, 34.16% on CodePlex-QA, with 20% random chance baseline), computing the ratio of gaps above random gives 34.8/14.16 ≈ 2.46, not 1.9. Even alternative formulas (ratio of accuracies, ratio of error rates) do not yield 1.9. The paper states this factor "after factoring out random chance," but the arithmetic with the published numbers does not match. This is not a minor rounding issue—it affects the headline claim for the automatically generated benchmark (Section 5.2). The authors must clarify the exact computation and either correct the number or reconcile it with Table 2.

2. **The predictive advantage of CodePlexity over Cyclomatic Complexity is marginal, yet the paper frames it as a clear advance.** According to the described Table 1 results, CodePlexity improves mPEG over Cyclomatic Complexity by only 0.04 (HGA) and 0.06 (SeViLA-ZS), with zero gain on InternVideo and Tarsier. Cyclomatic Complexity is a zero-parameter, learning-free metric, so gains of 0.04–0.06 on a [0,1] scale are modest. The paper's central framing in Sections 1 and 3.2 positions CodePlexity as a superior predictive metric; the evidence supports only a marginal improvement over a trivial baseline. The real contribution lies in the interpretability (subtree analysis), not in predictive power, and the text should be recalibrated accordingly.

### Minor

3. **No multiple comparison correction in the subtree significance analysis.** The one-sided test (p<0.01) is applied to potentially thousands of subtree features without correction. Without Bonferroni or FDR correction, the set of significant subtrees $S^*$ may contain many false positives. The paper's interpretability claims depend on these subtrees being genuinely informative; this gap weakens that evidence.

4. **Limited human study does not support the generality of the conclusion.** The human study (150 questions, 30 subjects, single dataset) is used to support the claim that "humans struggle to accurately estimate which questions are hard." While the result is plausible, the sample is small and restricted to NExT-QA. The generality of the human-limitation conclusion is not established.

5. **ViperGPT serves as both the code generator and appears in the training set for CodePlexity.** This circularity means the subtree weights are partially learned to explain ViperGPT's own errors, which are already reflected in the generated code structure. The paper should explicitly discuss whether this inflates the correlation and ideally ablate ViperGPT from $M_{train}$ to verify the results hold for code generated by other models.

6. **No error bars or confidence intervals in Table 1.** The mPEG values are reported as single numbers without uncertainty estimates. Given the small held-out evaluation set (20% of NExT-QA validation), bootstrapped confidence intervals would allow readers to assess whether the differences between metrics are meaningful.

7. **Missing details on the logistic regression model.** The paper does not report the number of subtree features, the degree of feature overlap, whether L1/L2 regularization was applied, or training convergence checks. For a learned metric that is a core contribution, these details matter for reproducibility and for assessing overfitting risk.

8. **No analysis of code generation success rate.** The method assumes every question can be translated into a valid executable program. The paper should report how many questions in NExT-QA produce executable code and whether excluded questions differ systematically in complexity.

### Trivial

- None.

## Nice-to-Haves

- The subtree analysis findings (reasoning about event order, fine-grained object details) are well-known challenges in VideoQA. The paper would benefit from explicitly acknowledging prior work and emphasizing that the novelty is the *data-driven discovery* of these patterns, not the patterns themselves.
- A simple ablation excluding ViperGPT from the training set would strengthen the claim that CodePlexity generalizes to code from different generators.
- Reporting bootstrapped confidence intervals for mPEG values in Table 1 would improve the interpretability of the comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that the subtree findings are not new and the paper overstates them* — This is a presentation concern rather than a substantive weakness. The value is in the data-driven discovery methodology, which the paper already describes.
- *Criticism about overfitting risk from high-dimensional features without regularization details* — Kept as Minor #7 but downgraded from the critic's framing. The concern is valid but standard for a conference paper; including regularization details would strengthen, not invalidate.
- *Criticism that the paper lacks a novel method* — The paper's contribution is a metric/analysis tool, not a novel VideoQA method. This is the wrong expectation class.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the "1.9×" computation.** Provide the exact formula, the per-model accuracy numbers, and step-by-step derivation. If an error exists, correct it. If a non-standard definition is used (e.g., based on difficulty quantile ratios rather than simple accuracy gaps), explain it explicitly.

2. **Recalibrate the contribution framing.** Lead with the interpretable subtree analysis as the primary contribution and present CodePlexity's predictive improvement over Cyclomatic Complexity honestly as modest but complemented by the interpretability benefit.

3. **Apply multiple comparison correction** to the subtree significance tests (Bonferroni or FDR) and report whether the identified subtrees survive correction.

4. **Report code generation success rates** and analyze whether failed generations are systematically biased toward easier or harder questions.

5. **Add bootstrapped confidence intervals** to Table 1 and report the number of subtree features and regularization used in the logistic regression model.

## Score and Decision

The paper presents a genuinely novel idea—using code structure as an interpretable proxy for question difficulty—and provides evidence that it outperforms text-based metrics. The interpretable subtree analysis is a real contribution. However, two issues prevent stronger recommendation: (a) the "1.9× harder" benchmark claim does not reconcile with the reported accuracy numbers, which undermines a headline result; and (b) the predictive improvement over a trivial baseline (Cyclomatic Complexity) is marginal, yet the paper's framing overstates it. The remaining issues (multiple comparisons, missing details, limited human study) are addressable. With a corrected or clarified benchmark claim, honest recalibration of the framing, and additional statistical rigor, the paper could be a solid contribution. In its current form, the overstatement and the unverified benchmark number are significant concerns.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>