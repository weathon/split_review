## Summary

This paper proposes using code execution on test cases as a scalable, objective method for measuring semantic diversity of LLM generations. The authors create a dataset of 21 abstracted competitive programming problems, generate 100 programs per configuration across many model families (LLaMA-3, LLaMA3.1, CodeLLaMA, Qwen-Coder-2.5, plus commercial models), and measure lexical, syntactic, and semantic diversity. The central empirical finding — contrary to the prevailing narrative — is that instruction tuning (especially preference tuning) *increases* semantic diversity while *decreasing* lexical and syntactic diversity. The paper also demonstrates that neural diversity metrics (CodeBERTScore, ICE-Score) correlate negatively with execution-based semantic diversity, showing they are poor proxies.

## Strengths

1. **Novel execution-based semantic diversity metric for code.** The paper proposes measuring semantic diversity by executing programs on test cases and comparing outputs — an objective, scalable alternative to expensive human evaluation. The validity of this metric is concretely demonstrated in Figure 1, where it correctly captures the temperature "sweetspot" while lexical and syntactic metrics do not, and in Figure 3, which shows the pairwise metric is invariant to sample size (unlike naïve alternatives). This methodological contribution is significant and opens a new evaluation axis for code generation research.

2. **Key empirical finding that instruction tuning increases semantic diversity while decreasing lexical/syntactic diversity.** This contradicts the common narrative that preference-tuned models uniformly reduce diversity. Table 1 reports paired Wilcoxon Signed-Rank tests and Cohen's d effect sizes across multiple model families (LLaMA-3, LLaMA3.1, CodeLLaMA, Qwen-Coder-2.5), consistently showing that preference-tuned models have large to very large effect sizes for increased semantic diversity and decreased lexical/syntactic diversity. The pattern holds across model sizes and prompting strategies, and is shown more strongly for preference-tuned models than SFT-only models.

3. **Demonstration that neural diversity metrics fail to capture semantic diversity.** Figure 4 reports Spearman and Kendall's Tau rank correlations showing that CodeBERTScore, ICE-Score, lexical, and syntactic metrics are all *negatively* correlated with execution-based semantic diversity. Figure 5 provides concrete examples where CodeBERTScore assigns high similarity to semantically different programs. This is a cautionary result with practical implications: researchers should not assume neural metrics reflect content diversity.

4. **Rigorous handling of sample-size bias.** The paper adopts a pairwise diversity metric (Equation 2) and empirically demonstrates in Figure 3 that naïve metrics are confounded by sample size while the pairwise metric is invariant. This methodological rigor improves the reliability of all subsequent comparisons.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses below are substantive but addressable and do not threaten the paper's core contributions.

### Minor

1. **The semantic diversity metric is relative to a finite test suite, not exhaustive behavioral equivalence.** Two programs that behave identically on the provided test cases but differ on unseen inputs are counted as semantically identical. The paper transparently defines its metric ("we define two programs as semantically distinct iff their outputs differ across a given set of test cases," Section 4), and this operationalization is a scalable and principled choice. However, the Discussion and Conclusion refer to "semantic diversity" without always qualifying that this is test-suite-relative. Adding a sentence (or even a footnote) to the Discussion acknowledging the gap between test-suite equivalence and full behavioral equivalence — and explaining why the current measure is conservative — would sharpen the scope. This does not change any result; it is a clarity improvement.

2. **Coherent program counts per model are not reported, making it hard to assess the reliability of the coherent-subset analysis.** When base models produce very few coherent programs (e.g., 2–5), the pairwise metric (Equation 2) averages over a small number of pairs, yielding high-variance estimates. The paper reports coherence as a metric but does not report the distribution of coherent program counts per model per problem. Without this, readers cannot assess whether the coherent-subset semantic diversity estimates are reliable for the models with the lowest coherence rates. This is a transparency issue that the authors could resolve by reporting summary statistics (min, median, max coherent count per model).

3. **The problem set is limited to 21 competitive programming problems from a single genre.** While the paper is explicitly titled "A Case Study Using Code Generation" and acknowledges the limitation to code, it does not discuss generalizability *within* the code domain. Diversity patterns may differ for other coding tasks (e.g., writing unit tests, data analysis scripts, configuration files, web components). The consistent findings across multiple model families and the large effect sizes lend confidence, but the narrow problem genre bounds the conclusions more tightly than the broad language in the abstract and conclusion suggests. A clearer scope statement (e.g., "on these 21 competitive-programming-derived tasks") in the abstract would better align claims with evidence.

### Trivial
None.

## Nice-to-Haves

- **Qualitative breakdown of what kind of semantic diversity increases with instruction tuning.** Are preference-tuned models producing genuinely different algorithms, or different implementations of the same algorithm that happen to differ on test cases? A finer-grained analysis connecting syntactic and semantic metrics (e.g., by AST structure) would deepen the empirical contribution.
- **Systematic analysis of why neural metrics fail.** The paper provides helpful anecdotal examples (Figure 5) but stops short of a systematic error analysis. Understanding whether neural metrics systematically penalize certain kinds of diversity (e.g., specific control flow patterns) would strengthen the cautionary message.

## Removed Points

- The harsh critic's "Other Observation" about cost-per-token as a proxy is removed because the paper itself already says "we cannot draw stronger conclusions because these models are not well documented" — the paper is appropriately cautious, so this is not a genuine weakness.
- The harsh critic's "Other Observation" that the negative correlation finding "should not be surprising" is removed because this is an opinion about expectedness, not a flaw in the paper's methodology or claims. The paper's contribution is in demonstrating this empirically for diversity, not in claiming surprise.
- The "Missing Parts" point about prompt-specific results not being systematically reported is removed because these results were in the supplementary material (which is stripped by the parser, not absent from the original submission).
- The "Strengthening the Paper" suggestion to expand the problem set to 40–50 problems is a wishlist item; the paper is explicitly a case study (per its title), and 21 problems with paired tests across many models is appropriate for that framing.

## Novel Insights

The most interesting insight from the reviews is that the tension between the harsh critic's and the strength finder's assessments surfaces an important subtlety: the paper's central finding (instruction tuning increases semantic diversity) is simultaneously *well-supported within its scope* and *bounded by its scope* more tightly than its broad framing suggests. The execution-based metric is genuinely novel and its negative correlation with neural metrics is a practically important result, but the metric is operationalized on a fixed, finite test suite — meaning "semantic diversity" as measured is a lower bound on true behavioral diversity. Whether the finding generalizes from 21 competitive programming problems to other code tasks (testing, data analysis, configuration) is an open question that the paper's own framing partially acknowledges (via "case study") but could address more explicitly.

## Suggestions

1. Report the distribution of coherent program counts per model (min, median, max across the 21 problems) so readers can assess the reliability of the coherent-subset semantic diversity estimates.
2. Add a sentence to the Discussion explicitly noting that the semantic diversity metric is relative to the provided test suite and that two programs treated as identical could differ on unseen inputs — with an explanation of why the measure is nevertheless conservative and useful.
3. Add a brief scope qualifier in the abstract's empirical claims (e.g., "on a set of 21 competitive-programming-derived tasks") to align the headline finding more precisely with the evidence.

## Score and Decision

This is a methodologically creative paper that makes a clear contribution: a scalable, objective way to measure semantic diversity of code generations, plus a counterintuitive empirical finding (instruction tuning *increases* semantic diversity) demonstrated across multiple model families with large effect sizes. The weaknesses are genuine but modest — the test-suite-relative nature of the metric is transparently defined, the 21-problem set is acknowledged as a case study, and the missing coherence counts are easily added. The paper is sound, the claims are supported within its stated scope, and the contributions are worth sharing with the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>