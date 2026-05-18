Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Tool Decoding, a training-free, plug-and-play decoding strategy that improves LLMs' ability to use external tools. The method has two components: (1) constrained decoding that restricts generation to valid tool names, format tokens, and parameter keys extracted from tool documentation, and (2) order consistency, which shuffles required parameter orders, generates multiple tool-call candidates, and aggregates them via majority voting to improve parameter-value accuracy. Experiments across 10+ models on API-Bank and BFCL V2·Live show substantial improvements, with several 7B models surpassing GPT-3.5 and GPT-4.

## Strengths

- **Fine-grained error analysis identifies concrete bottlenecks.** The paper decomposes tool usage into three stages (awareness, selection, call) and five error types (selection, format, key, value, awareness), providing quantitative distributions across models (Figure 3). This granularity—showing that selection, format, and value errors dominate—is more actionable than prior coarse taxonomies and directly motivates the method's design.

- **Constrained decoding eliminates format errors and sharply reduces selection errors without any training.** By extracting tool names and parameter keys via regex from well-structured documentation and restricting decoding to valid tokens, the method eliminates hallucinations at the tool-selection and format levels (§3.1, Figure 4). Figure 6 shows format errors are almost entirely eliminated and selection errors drastically reduced across all models.

- **Order consistency with majority voting demonstrably reduces value errors—a problem prior constrained-decoding methods do not address.** Prior work (Zhang et al., 2023; Wang et al., 2023a) enforces syntax but not value accuracy. Tool Decoding introduces structured sampling over parameter orders with majority voting. Table 4 shows a clear positive correlation between the number of sampled orders (oc) and value-error reduction (e.g., up to 23.2% for deepseek-coder-6.7b at oc≤12), confirming the mechanism works.

- **Broad experimental validation across >10 diverse models on two benchmarks.** The paper tests generalist, code, long-context, and tool-finetuned models (1.5B to 72B). On API-Bank and BFCL V2·Live, almost all models show improvements exceeding 70%, and several open-source 7B models surpass GPT-3.5 or GPT-4. The ablation in Table 4 cleanly isolates the effect of order consistency from constrained decoding.

- **Seamless integration with prompt engineering.** Table 3 shows Tool Decoding combines with in-context learning, enabling a 7B model to outperform GPT-4 under the same prompt settings—demonstrating compatibility rather than replacement.

- **Honest treatment of the value-error unmasking effect.** The paper transparently reports (Figure 6, §4.3) that fixing format and selection errors can expose previously masked value errors, correctly attributing this to unmasking rather than claiming the method reduces all error types uniformly.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the evidence presented.

### Minor

- **The value-completion detection mechanism is underspecified (§3.2).** The order-consistency pipeline requires detecting when the model has finished generating a parameter value before appending the next key. The paper states only that "the transition between two parameters is triggered when the previous value is detected as fully generated" and that candidate values are filtered by "parameter type requirements." No detail is given on *how* completion is detected—whether by a separator token, a type-based heuristic (e.g., generating until a non-matching token for a given type), or some other rule. This is the most significant missing implementation detail and affects reproducibility. It should be clarified in a revision.

- **No discussion of inference cost.** Tool Decoding replaces a single forward pass with up to oc≤12 forward passes per tool call (plus majority-voting aggregation). The paper quantifies accuracy gains but provides no discussion of wall-clock time, token-generation overhead, or relative compute compared to greedy/beam search. This gap is notable because the method is positioned as "plug-and-play" and suitable for resource-constrained environments (§6). A brief acknowledgment and rough estimate (e.g., "Tool Decoding uses at most oc forward passes per tool call, incurring roughly oc× the generation cost of greedy decoding") would suffice.

- **The self-consistency motivation sentence (§3.2) is slightly imprecise.** The paper states the method "overcomes the barrier to apply [self-consistency's] thought to tool usage due to the absence of reasoning process." Self-consistency was originally designed for CoT reasoning paths, but tool usage does have multiple paths (different parameter orders), which is precisely what order consistency exploits. The sentence can be simplified to avoid confusion—this is a minor writing issue.

### Trivial

None.

## Nice-to-Haves

- **Net-effect analysis of the unmasking phenomenon.** Figure 6 shows that value errors increase in absolute terms for some models under Tool Decoding. The paper explains this as unmasking of previously hidden errors. It would be helpful to report what fraction of test cases that were *correct* under greedy search become incorrect under Tool Decoding (the unmasking's downside) versus the net gain in correct tool calls. The total-accuracy results in Figure 5 already demonstrate that the net effect is strongly positive, so this is supplemental, not critical.

- **Direct experimental comparison with prior constrained-decoding tool-use methods.** The paper cites Zhang et al. (2023) and Wang et al. (2023a) in related work and the ablation in Table 4 (oc≤1) effectively serves as a constrained-decoding-only baseline, showing the incremental value of order consistency. A more explicit comparison would strengthen positioning but is not essential.

- **Brief note on error-distribution generalizability.** The error analysis in Figure 2 uses UltraTool while Figure 3 uses API-Bank. A sentence on whether the error-type proportions are consistent across benchmarks would help.

## Removed Points

These points are flagged as removed per policy; treat them with caution.

- The harsh critic's claim that the self-consistency analogy is odd ("the barrier is not obvious") — this is a minor writing nitpick about a single sentence. The paper's main contribution is unaffected. Moved here as a style nitpick.
- The harsh critic's point about missing comparison with prior methods framed as a weakness rather than a nice-to-have — the ablation (oc≤1) already serves as this baseline. Downgraded to Nice-to-Haves above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper itself does not already articulate.

## Suggestions

1. In §3.2, specify the exact rule used to detect parameter-value completion (e.g., "generation proceeds until the model produces a token inconsistent with the declared parameter type, at which point the value is truncated to the last valid token" or describe the actual heuristic/separator used).
2. Add a brief paragraph quantifying inference overhead: average/median number of forward passes per tool call, approximate time ratio vs. greedy decoding, and a note on how oc trades off accuracy vs. cost.
3. Clarify the self-consistency analogy in §3.2 (e.g., "While self-consistency samples diverse reasoning paths, we sample diverse parameter orders—analogous paths for tool usage").
4. Consider adding a supplementary analysis showing the number/fraction of cases where the unmasking effect degrades an originally correct output.

## Score and Decision

The paper is solid: the error analysis is insightful, the method is clean and well-motivated, and the experiments are extensive. The weaknesses are minor and addressable in a revision. The contribution is clear and practically valuable.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>