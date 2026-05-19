- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes **Tool Decoding**, a training-free, plug-and-play decoding method that improves LLM tool usage by combining constrained decoding (to enforce format correctness and valid tool names) with order consistency and majority voting (to improve parameter-value accuracy). Motivated by a fine-grained error analysis that identifies selection, format, and value errors as the primary failure modes, the method is evaluated across 10+ models on API-Bank and BFCL V2•Live, reporting substantial improvements over greedy and beam search baselines.

## Strengths

- **Fine-grained error analysis isolates the three dominant failure types (selection, format, value).** Section 2 and Figure 3 decompose tool usage into awareness/selection/call stages and further categorize call errors, providing clear motivation for the two components of Tool Decoding. This analysis goes beyond prior coarse taxonomies.

- **Constrained decoding demonstrably eliminates format errors and reduces selection errors without training.** Section 3.1 describes how a token tree built from structured tool documentation restricts vocabulary during tool-name and optional-key generation. Figure 6 shows that Tool Decoding nearly eliminates format and key errors across representative models.

- **Order consistency with majority voting reduces value errors, with controlled ablation confirming the mechanism.** Section 3.2 and Table 2 show that aggregating across different required-parameter orders outperforms any single order. Table 4 provides a clean ablation: as the upper limit on order samples (oc) increases, the proportion of value-error reduction rises monotonically across all four models tested, isolating order consistency from the mere effect of additional sampling.

- **Consistent large-magnitude improvements across a diverse set of models and benchmarks.** Figure 5 reports total accuracy on API-Bank and BFCL V2•Live for five generalist models and one tool-finetuned model. Every model improves substantially over greedy search and beam search, with gains exceeding 70% (relative) for nearly all models.

- **Seamless integration with existing approaches.** Table 3 shows Tool Decoding combines effectively with in-context learning, and the method is evaluated on a tool-finetuned model (xLAM-7b-r), demonstrating compatibility with fine-tuning approaches.

## Weaknesses

### Fatal

None.

### Major

- **Main results (Figure 5) are presented only as bar charts without exact numeric values.** The paper's central evidence consists of bar charts with no accompanying table of exact accuracy numbers. The reader cannot determine precise improvement magnitudes, and claims such as "two 7B models surpass GPT-4" cannot be independently checked against exact values. For a methods paper making strong comparative claims, this is a significant presentation gap.

- **No end-to-end accuracy is reported for constrained decoding alone (without order consistency) on the full benchmarks.** The ablation in Table 4 measures only the proportion of *value error reduction* at different oc limits, not total accuracy. Without a full-benchmark constrained-decoding-only baseline, the individual contributions of the two components (constrained decoding vs. order consistency) cannot be disentangled. This is a gap in the evaluation design.

- **GPT-4 comparison lacks sufficient supporting detail.** GPT-4 performance is shown only as horizontal reference lines in Figure 5 with no numeric values provided or cited. The paper does not report whether the same Tool Decoding method could be applied to GPT-4, does not provide per-category breakdowns on the four BFCL categories used (to show where the advantage lies), and does not discuss GPT-4's variance or the conditions under which the reference scores were obtained. The headline claim of "surpassing GPT-4" needs more transparent evidence.

- **The initial error analysis motivating the method (Section 2, Figures 2–3) is conducted on UltraTool with Qwen1.5 models, while the main evaluation uses different benchmarks (API-Bank, BFCL V2•Live) and diverse model families.** The paper does not verify that the error distributions on the evaluation benchmarks match those observed on UltraTool. Figure 3 does show error distributions for API-Bank, but with different models than the Qwen1.5 series used in the stage analysis. The connection between the motivating analysis and the evaluated scenarios could be tighter.

### Minor

- **The choice of oc ≤ 12 is stated without justification.** The paper sets an upper limit of 12 order samples but does not explain why this value was chosen or whether similar gains can be achieved with fewer samples (which would reduce computational cost). For latency-sensitive applications this is relevant.

- **The "retaining only those that meet the parameter type requirements" step is mentioned but not described.** After generating candidate tool calls, the paper states that only those meeting parameter type requirements are retained (Section 3.2), but the mechanism for this validation is not specified. This is a detail that could affect reproducibility.

- **The claim that "tool awareness is relatively straightforward" is based solely on Qwen1.5 models on UltraTool.** While the paper explicitly scopes out awareness errors from the method, the basis for this claim is narrow (one model family, one benchmark). Broader evidence would strengthen this premise.

- **The proportion of benchmark data excluded from evaluation is not reported.** API-Bank excludes the "Plan + Retrieve + Call" category (1 of 3 categories) and BFCL V2•Live excludes "Relevance" and "Irrelevance" (2 of 6 categories), but the paper does not state what fraction of total benchmark examples this represents, making it difficult to assess evaluation coverage.

- **Tool Decoding slightly increases value errors (Figure 6), which the paper attributes to unmasking previously-hidden errors.** The paper discusses this candidly, but the net effect is that the method does not reduce *all* error types—it reshuffles them, with order consistency providing only partial mitigation. This nuance inherently limits the claimed comprehensiveness.

### Trivial

None.

## Nice-to-Haves

- Including a supplementary table with exact accuracy numbers and standard errors (or bootstrap confidence intervals) for all model–benchmark combinations would substantially strengthen the evidence, especially for the GPT-4 comparisons.
- Reporting per-category results on the four BFCL V2•Live categories used would make the claimed superiority over GPT-3.5/GPT-4 more transparent.
- A brief discussion of the computational cost of oc ≤ 12 and whether similar gains are achievable with fewer samples would improve practical utility.

## Removed Points

These points were flagged by the reviewers but are removed (with justification) from the main weaknesses:

- *"No confidence intervals, no statistical tests"* — Barring exact numbers is the real issue; confidence intervals/statistical tests are not standard practice for single-run large-benchmark evaluations in this field. Moved to Nice-to-Haves.
- *"The benchmarks may be saturating or may favor Tool Decoding"* — Speculative; no evidence in the paper supports or refutes this. Removed.
- *"Order consistency assumes all parameter keys are known; this works for structured APIs but not free-form tool descriptions"* — This describes the method's stated scope (structured tool documentation), not a flaw. Removed.
- *"The connection between the analysis and method could be tighter"* — Generic suggestion without a concrete anchor. Removed.
- *"The comparison overlooks that GPT-4 is a general-purpose model not specifically tuned for tool use"* — GPT-4 is a reasonable strong baseline regardless of specialization. Removed as scope creep.
- Generic praise from Strength Finder (e.g., "the paper addresses an important problem"). Removed; only specific, evidence-grounded strengths are retained.

## Novel Insights

A genuinely novel synthesis from the two reviews is that **Tool Decoding exposes a fundamental trade-off in plug-and-play tool-use improvement**: eliminating format and selection errors via constrained decoding inadvertently _increases_ value errors because hidden parameter-value mistakes are unmasked once surface-level errors are resolved. Order consistency partially mitigates this, but the net effect is an error redistribution rather than a uniform reduction. This dynamic—where fixing easy errors reveals harder ones—is a phenomenon worth studying in its own right and could guide future work on tool-use decoding.

## Suggestions

1. Add a table with exact accuracy numbers for all model–benchmark combinations shown in Figure 5, ideally with GPT-4 reference scores explicitly stated and sourced.
2. Include a full-benchmark baseline for constrained decoding alone (without order consistency) so readers can isolate the contribution of each component.
3. Provide per-category breakdowns on BFCL V2•Live for the four used categories to clarify where GPT-4 is surpassed and where it is merely approached.
4. Report the fraction of benchmark examples excluded when omitting certain categories.
5. Justify or experimentally motivate the choice of oc = 12 as the upper sampling limit.
