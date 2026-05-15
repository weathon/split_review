Now I have a thorough understanding of both the paper and the reviews. Let me compose the final consolidated review.

## Summary

This paper proposes Tool Decoding, a training-free method that enhances LLMs' tool-use capabilities by integrating constrained decoding (for format/selection correctness) with "order consistency" — shuffling the order of tool parameters and applying majority voting across multiple generated tool calls to improve parameter value accuracy. The method is motivated by a fine-grained three-stage error analysis (awareness, selection, call) that highlights selection, format, and value errors as the primary bottlenecks. Experiments on API-Bank and BFCL V2 Live across 10+ models report large gains over greedy and beam search baselines, with some 7B models surpassing GPT-3.5 and GPT-4.

## Strengths

- **Well-motivated fine-grained error taxonomy**: The paper decomposes tool usage into three stages (awareness, selection, call) with five error types. This analysis is more precise than prior coarse categorizations (e.g., API-Bank's "Has Exception") and directly motivates the design of Tool Decoding's components (Section 2, Figure 3). The finding that format, selection, and value errors dominate is empirically grounded across multiple models.

- **Clever exploitation of order-invariance in tool calls**: The order consistency mechanism — shuffling parameter order + majority voting — is a novel and intuitively sound idea. Unlike prior constrained-decoding methods (Zhang et al., 2023; Wang et al., 2023a) that only enforce syntax, this approach targets value errors without requiring training. Table 2 demonstrates that no single parameter order is universally best, while aggregation across orders surpasses every individual order.

- **Consistent and large-magnitude performance gains**: Across more than 10 models spanning generalist and tool-finetuned architectures, Tool Decoding improves total accuracy substantially on both benchmarks (Figure 5). Even if the magnitude is partially inflated by baseline choices (see Weaknesses), the gains are consistent enough to suggest genuine benefits. The method enables 7B-level models (deepseek-coder-6.7b, xLAM-7b-r) to match or exceed GPT-3.5/GPT-4 on API-Bank.

- **Training-free and plug-and-play**: The method requires no additional training, integrates with existing prompting approaches (Table 3 shows compatibility with ICL), and generalizes to new tools given structured documentation. This is a practical advantage over fine-tuning-based alternatives.

- **Ablation partially validates order consistency**: Table 4 shows a positive correlation between the number of order-sampled tool calls (oc limit) and the reduction in value errors across four models, providing evidence that majority voting across parameter orders is responsible for value-error improvements.

## Weaknesses

### Fatal
None.

### Major

- **Headline results compared against weak, single-sample baselines without controlling for the benefit of multi-sample aggregation**: The main results (Figure 5) compare Tool Decoding (which uses up to 12 samples with constrained decoding, order shuffling, and majority voting) against greedy search and beam search — both single-sample, deterministic strategies. The paper does not include a controlled baseline of "N samples with temperature + majority voting without constrained decoding" nor "constrained decoding + N samples from a single order (no shuffling) + majority voting." This makes it impossible to disentangle how much of the reported "70%+ improvement" comes from: (a) the inherent benefit of sampling and voting, (b) constrained decoding alone, or (c) the novel order shuffling mechanism. The paper acknowledges inspiration from self-consistency but never empirically controls for the sampling+ voting effect itself. This undermines the central quantitative claims.

### Minor

- **Incomplete ablation isolating the components**: The ablation study (Table 4) only measures value error reduction within Tool Decoding as oc varies. It does not report total accuracy, selection errors, or format errors for constrained decoding alone (oc≤1) versus full Tool Decoding. Figure 6 compares greedy search directly to full Tool Decoding but omits the intermediate condition of "constrained decoding without order consistency." Since the paper claims constrained decoding "eliminates format errors and reduces selection errors," a direct comparison of constrained decoding alone vs. greedy on these error types would cleanly substantiate that claim.

- **Unexplained increase in value errors**: Figure 6 shows that value errors increase (not just shift) under Tool Decoding relative to greedy search across all four models examined. The paper attributes this to "uncovering underlying value errors that were previously masked by other issues" (line 128), but provides no evidence — no case studies, no tracing of whether these are genuinely unmasked versus newly introduced by the method (e.g., through constrained decoding interactions or order shuffling artifacts). This explanation, while plausible, requires rigorous backing.

- **No direct empirical comparison to prior training-free constrained-decoding methods**: The paper cites Zhang et al. (2023), Wang et al. (2023a) (constrained decoding for tool syntax) and Wang et al. (2024) (reranking for values) in Section 5, and correctly notes their limitations, but never benchmarks against them. Since Tool Decoding is positioned as a superior training-free alternative, direct comparison on total accuracy would strengthen that positioning. (The partial ablation with oc≤1 partially addresses this for value errors but not for total accuracy or selection/format errors.)

- **Table 2 does not control for sample count**: Table 2 shows that aggregating across orders beats any single order, but does not compare against taking the same number of samples from a single fixed order with the same voting mechanism. The improvement could partly reflect more samples rather than order diversity itself.

### Trivial

- The GPT-4 version used for comparison is not specified (e.g., GPT-4-0613 vs. GPT-4-turbo), making the "surpass GPT-4" claim somewhat ambiguous.
- Figure 5 uses bar charts without absolute accuracy labels on the y-axis, making it difficult to read precise values.

## Nice-to-Haves

- A controlled baseline of N-samples + majority voting (temperature sampling) without constrained decoding or order shuffling, to isolate the sampling benefit.
- Direct empirical comparison against prior constrained-decoding methods (Zhang et al., 2023; Wang et al., 2023a) and the reranking approach (Wang et al., 2024) on total accuracy.
- Case studies tracing whether newly appearing value errors under Tool Decoding are genuinely unmasked or introduced by the method.
- Per-parameter type accuracy breakdown (string, number, enum values) to better understand where order consistency helps or hurts.

## Removed Points

The following points from the reviews were removed with justification:

- **Criticism that self-consistency (Wang et al., 2023b) should be compared as a baseline without modification**: The paper explicitly acknowledges (line 91) that self-consistency requires diverse reasoning paths, which are absent in tool-call generation. Self-consistency cannot be directly applied to tool usage without a mechanism like order shuffling. The more appropriate baseline (multi-sample + majority voting without constraints) is already listed as a Nice-to-Have above. The critic's phrasing oversimplifies the applicability issue.

- **Criticism that "no temperature/nucleus sampling parameters are reported for baselines"**: Greedy search is deterministic (temperature=0) and beam search is also deterministic given fixed beam width. This complaint misunderstands the baselines used. The beam width is a hyperparameter that could be specified, but this is a trivial omission, not a substantive weakness.

- **Criticism that the error analysis in Section 2 uses "only six models" and "representativeness is unclear"**: The paper evaluates error distributions across generalist and tool-finetuned models of varying scales (Figure 3), and additionally analyzes 70B-scale models (Figure 7, cited in text). The coverage is reasonable for an error analysis study; demanding exhaustive model coverage for a descriptive analysis is scope creep.

- **Criticism that the paper does not explain why error categories "hold for other models or benchmarks"**: The error taxonomy is derived from the logical structure of tool usage (awareness → selection → call), not from empirical observations of specific models. The taxonomy is inherently general; the empirical analysis merely confirms which error types dominate in practice.

- **The claim that "improvements exceeding 200%... is statistically meaningless without absolute baselines"**: This is an overstatement. Percentage improvements are standard when baselines are reported alongside. The baselines are reported in Figure 5 (absolute accuracy), even if they are weak baselines. The issue is the baseline choice, not the reporting format.

## Novel Insights

The most interesting observation that emerges across the reviews is a meta-level tension: the paper's core technical contribution (order consistency) is a clever adaptation of self-consistency's logic to a domain where standard self-consistency cannot apply (tool call generation has no "reasoning paths" to vary). The paper correctly identifies this gap, and the method of shuffling parameter order as a source of diversity is principled — it exploits an invariances unique to tool calls (order-invariant parameters). However, the reviews expose that the paper simultaneously fails to control for the simpler baseline of "just sample many times and vote" (which would work even without the order-invariance insight). This creates a situation where the novelty is real but the evidence does not cleanly separate it from a trivial alternative. The paper would be substantially stronger if it showed that order shuffling provides benefits beyond uniform-temperature sampling with the same sample count — i.e., that the *structured* diversity from shuffling matters beyond just *more* diversity.

## Suggestions

1. **Add a controlled multi-sample baseline**: Run temperature/nucleus sampling with the same number of samples (up to 12) and majority voting *without* constrained decoding and *without* order shuffling. This isolates the benefit of sampling itself from the benefit of the proposed components.

2. **Add a "constrained decoding + single-order multi-sample" baseline**: Apply constrained decoding but sample the same parameter order multiple times with temperature, then vote. This isolates the benefit of order shuffling specifically (diversity across orders) from the benefit of constrained decoding + sampling generally.

3. **Rigorously trace the source of increased value errors**: For at least 10-20 cases where value errors appear under Tool Decoding but not under greedy search, manually inspect whether the value would have been correct in greedy but was impossible to reach (e.g., due to a format error interrupting the generation early) versus whether the value is genuinely new and erroneous. Present this as a small case-study table.

4. **Report total accuracy for the ablation conditions**: Extend Table 4 to include total accuracy (not just value error reduction) for oc≤1 (constrained decoding only) and higher oc values, so readers can see the overall impact of order consistency on end-to-end performance.

5. **Specify the GPT-4 version** used for comparison and the exact evaluation protocol for those comparisons.

## Score and Decision

This paper tackles a well-motivated problem with a clever, training-free approach. The error taxonomy is a useful contribution, and the order-consistency mechanism is genuinely novel. However, the experimental evaluation has a significant gap: the main results compare against weak single-sample baselines without controlling for the inherent benefit of multi-sample aggregation, making it impossible to cleanly attribute the reported gains to the proposed components rather than to sampling+ voting itself. The partial ablation and the unanalyzed increase in value errors further weaken the evidence. The core ideas have merit, but in its current form, the paper does not provide sufficient experimental support for its strong claims.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**