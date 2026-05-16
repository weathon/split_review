Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes **Tool Decoding**, a training-free decoding-time method for improving LLM tool usage. It combines **constrained decoding** (to enforce format correctness and valid tool/parameter-key selection) with **order consistency** (multiple parameter-order samples aggregated via majority voting to improve parameter-value accuracy). The method is motivated by a fine-grained error analysis decomposing tool usage into awareness, selection, and call stages. Evaluated on API-Bank and BFCL V2 Live across 10+ models, the method reports substantial gains over greedy and beam search baselines.

## Strengths

- **Training-free plug-and-play design validated across diverse models.** The method requires no fine-tuning, uses only tool documentation to extract constraints, and is demonstrated on more than 10 models spanning generalist, code, long-context, and tool-finetuned variants (Figure 5). This is a genuine practical advantage over approaches requiring tool-specific training.

- **Fine-grained error analysis that systematically identifies failure bottlenecks.** The paper decomposes tool usage into three stages (awareness, selection, call) and further splits call errors into format, key, and value errors (Table 1, Figure 3). This breakdown — and the finding that selection, format, and value errors dominate — directly motivates the two components of Tool Decoding. The analysis goes beyond the coarse error categories in prior benchmark papers.

- **Order consistency component is validated by a clear ablation.** Table 4 shows that increasing the order-consistency sampling budget (oc limit) monotonically reduces value errors across four models. Table 2 further confirms that majority voting across multiple parameter orders outperforms the best single order. This isolates the incremental contribution of order consistency over constrained decoding alone.

- **Compatibility with existing approaches.** Table 3 shows Tool Decoding can be combined with in-context learning to further boost performance, and Figure 5 shows it layers on top of tool-finetuned models (xLAM-7b-r). This demonstrates the method is complementary, not a replacement for other techniques.

## Weaknesses

### Fatal
None.

### Major

- **"Total accuracy" metric is never defined.** The paper reports "total accuracy" on API-Bank and BFCL V2 Live throughout, but never states what constitutes a correct prediction. Is it exact match of the generated tool call string? Is it whether the tool server returns a valid response? Does it follow the benchmarks' own evaluation protocols? Without this definition, the results cannot be independently interpreted or reproduced. This is a basic evidential gap.

- **No numeric results table; key claims unverifiable.** Figure 5 presents only bar charts without raw accuracy numbers. The abstract's headline claim that "almost all models demonstrate performance gains exceeding 70% on both benchmarks" cannot be verified from bar charts alone. Relative gains from near-zero baselines (e.g., Yi-1.5-6b on BFCL) can be arbitrarily large in percentage terms while being trivially small in absolute terms. The paper should provide a table with raw accuracies for all models and conditions, along with absolute and relative gains. Without this, the central empirical claims are not properly substantiated.

- **Missing comparison against prior constrained-decoding methods for tool usage.** The related work section (line 146) cites Zhang et al. (2023) and Wang et al. (2023a) as directly introducing "constrained decoding to enforce tool syntax in LLMs." Yet the experimental baselines include only greedy search and beam search — not these prior methods. The paper's own ablation (Table 4, oc ≤ 1 condition) isolates constrained decoding from order consistency, but this does not substitute for comparison against existing published implementations. Without such comparison, it is unclear whether the gains come from constrained decoding per se (already established in prior work) or from the order-consistency novelty. This gap prevents proper assessment of the incremental contribution.

### Minor

- **Evaluation protocol not specified for main results.** The paper does not state whether the main evaluation (Figure 5) uses zero-shot or few-shot prompting, what prompt format was used, or how many in-context examples (if any) were provided. Table 3 demonstrates that ICL example count affects results, making this omission consequential. Beam width for the beam search baseline is also not reported.

- **No variance or confidence intervals.** Order consistency involves sampling (oc ≤ 12), which introduces randomness. No standard deviations, confidence intervals, or multi-run statistics are reported anywhere in the paper. This is a gap for a method whose core mechanism involves stochastic sampling.

- **Unsupported claim about awareness errors.** The paper states (line 58) that "Awareness errors account for only a small proportion and are almost impossible to improve through non-training methods." The first part is supported by Figure 3; the second part — that they are impossible to improve without training — is asserted without evidence or citation and seems to go beyond what the data can show.

- **Value-error net effect not clearly reconciled.** Figure 6 shows that the full Tool Decoding *increases* value errors relative to greedy search (though "slightly"). The paper explains this as "uncovering underlying value errors that were previously masked." Table 4 then shows order consistency reduces value errors relative to the no-order-consistency baseline. However, the paper never states the net effect: does the full method have more or fewer value errors than the greedy baseline? The reader is left uncertain about whether value errors are ultimately reduced or increased, which weakens the completeness of the error analysis.

- **Beam search configuration unspecified.** The paper compares against beam search but does not report beam width or whether any hyperparameter tuning was performed for baselines.

### Trivial
- "non-compliant format ," (line 155) has an extra space before the comma — a minor formatting glitch in the extracted text (likely a parser artifact).

## Nice-to-Haves

- **Computational cost discussion.** Order consistency with oc ≤ 12 is up to 12× the decoding cost of greedy search. This trade-off should be discussed; results could be shown as a function of sampling budget.
- **Failure case analysis.** The paper does not discuss scenarios where order consistency might fail (e.g., parameters with dependencies like start/end dates, or free-form string values where majority voting may be less effective).
- **Handling of parameter-type constraints.** The paper mentions "type requirements" for parameter values but does not clarify what filtering is done for free-form vs. categorical values.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing appendix / missing proofs in appendix"** — Removed per instructions: the parser strips these sections from all papers; they exist in the original submission.
- **"Formatting/style nitpicks"** (the harsh critic's section-by-section notes about how figures are labeled, etc.) — Removed per instructions: these are parser artifacts or style preferences, not substantive issues.
- **"Different benchmarks used for stage analysis vs. error distribution"** (Figure 2 on UltraTool vs. Figure 3 on API-Bank) — Removed as scope-creep: the paper explains that stage analysis requires the UltraTool benchmark's capabilities (Figure 2) while error-type analysis uses API-Bank for its detailed annotations. Using different benchmarks for different analyses is standard practice and not a weakness.
- **"Prior constrained decoding methods already solve the problem" implication** — The harsh critic implies that prior work makes this contribution small. This is refuted by the paper's explicit discussion that prior constrained decoding methods "do not address issues such as incorrect parameter values" (line 146). The paper acknowledges prior work and positions its contribution as going beyond syntax correction to address value errors via order consistency.
- **Strength Finder's Strength #3 about "consistent large-magnitude gains"** — Tempered/qualified rather than fully removed, but the strength should be read in light of the verified weakness that raw numeric data is not provided in a table to substantiate the "70%" claim.

## Novel Insights

Beyond the paper's own contributions, the review process reveals that the key tension in this paper is between a genuinely useful, well-motivated method and an evaluation that lacks sufficient rigor to support the strong claims made. The error decomposition is the paper's most robust contribution—it is well-defined and reproducible regardless of implementation details. The method's core intuition (leveraging tool-structure at decoding time) is sound and the ablation cleanly demonstrates the additive value of order consistency. However, the decision to present results only as bar charts without a numeric table, combined with the undefined metric, undercuts what would otherwise be a strong empirical demonstration. The missing comparison against prior constrained-decoding baselines is the most consequential gap: it prevents the community from assessing whether the paper's main novelty (order consistency) actually provides additional value over existing approaches that already use constrained decoding for tool syntax.

## Suggestions

1. Add a table with raw accuracy numbers for all models and all conditions in Figure 5, along with absolute and relative gains clearly defined (absolute improvement in percentage points, not relative percentages from near-zero baselines).
2. Explicitly define the "total accuracy" metric — clarify whether it follows the evaluation protocol of each benchmark (API-Bank, BFCL) and what constitutes a correct tool-call prediction.
3. Implement and compare against the constrained-decoding methods of Zhang et al. (2023) and/or Wang et al. (2023a) on the same benchmarks. This directly addresses whether order consistency adds value beyond existing techniques.
4. Specify the evaluation protocol for the main results: zero-shot or few-shot, prompt format, number of in-context examples (if any), beam width for beam search.
5. Report the net effect on value errors: after both constrained decoding and order consistency, is the absolute count of value errors higher or lower than the greedy baseline? Decompose the error changes across components.
6. Add variance estimates for the order-consistency experiments, since sampling is involved.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>