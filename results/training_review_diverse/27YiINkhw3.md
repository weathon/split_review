I now have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes ToolDec, a finite-state machine (FSM) guided decoding algorithm that constrains LLM generation to produce only syntactically valid tool calls (correct tool names, type-conforming arguments, correct argument count). ToolDec constructs FSMs from tool API signatures and masks out invalid tokens during decoding. The paper demonstrates that ToolDec eliminates syntax errors in tool calls across three domains (math functions, knowledge graph relations, RESTful APIs), achieves competitive or better accuracy compared to ToolLLM, ToolkenGPT, and RestGPT, and shows strong generalization to unseen tools without needing per-tool fine-tuning or in-context documentation.

## Strengths

1. **Zero syntax errors across all tool types, convincingly demonstrated**: Figure 4 and Table 4 show that ToolDec reduces tool-related errors (non-existent tool names, invalid argument types, wrong argument count) from 10–30% for ToolLLM and ToolkenGPT to 0% across ToolEval and FuncQA. This is the paper's cleanest result and directly supports its core technical claim.

2. **Generalization to unseen tools without per-tool retraining or in-context documentation**: On FuncQA with 9 unseen math functions, ToolDec maintains accuracy comparable to its seen-tool performance while ToolkenGPT drops sharply (Figure 5a). On KAMEL, as unseen tools increase from 60 to 204, ToolDec maintains accuracy above 0.7 while all baselines fall below 0.3 (Figure 5b). On RestBench, ToolDec achieves an 8-point higher correct path rate than RestGPT despite removing all in-context documentation (Table 5). These results collectively validate the method's ability to leverage tool names as semantic cues.

3. **Comprehensive evaluation across three distinct domains**: The paper validates ToolDec on math functions (FuncQA), knowledge graph relations (KAMEL), and real-world REST APIs (RestBench/ToolEval), demonstrating that the approach is not limited to toy settings and can handle multi-tool workflows with complex APIs.

## Weaknesses

### Fatal
None.

### Major
1. **Overstated claim about "no need for fine-tuning" in the abstract and introduction.** The paper's abstract states that ToolDec enables "effective[ly] select[ing] tools using only the information contained in their names, with no need for fine-tuning." However, in the generalization experiments on FuncQA and KAMEL (Section 5.1), the authors explicitly "fine-tune the embedding of a single special token \<T\> to represent all tools" on a set of seen tools. Only the RestGPT comparison (Section 5.2) — which uses Vicuna, an already instruction-tuned model — truly requires no additional fine-tuning. The paper's framing conflates "no need for per-tool fine-tuning for unseen tools" (which is demonstrated and valuable) with "no need for fine-tuning at all" (which is only true in some settings). This distinction should be clearly delineated: ToolDec solves *which* tool to call and *how to invoke it* without per-tool training, but the *when to call a tool* decision still requires some training signal (either fine-tuning a trigger token or relying on an instruction-tuned model's inherent capability). The abstract and introduction should be revised to accurately reflect this.

### Minor
2. **Missing comparison with other constrained-decoding frameworks applicable to tool use.** The paper compares against ToolLLM (in-context learning) and ToolkenGPT (fine-tuning), but does not compare against general-purpose constrained-decoding frameworks such as *guidance*, *LMQL*, or *Outlines*, which also support constraining LLM generation to a grammar or FSM and have been applied to structured output tasks including tool calling. While these frameworks are not tool-use-specific, a comparison would help isolate whether ToolDec's specific FSM construction offers advantages over generic grammar-constrained decoding applied to the same tool-use tasks, or whether the gains are primarily from constrained decoding itself. Adding such a comparison (or at minimum discussing why it was omitted) would strengthen the paper's claims.

3. **The "2x speedup" claim is based on a selective comparison.** The abstract claims "as much as a 2x speedup," which is achieved comparing ToolDec (12.0s) against ToolkenGPT *with backtrace* (24.1s, Table 4). The backtrace variant is an optional recovery mechanism in ToolkenGPT, not the default mode. Against ToolkenGPT *without backtrace* (12.5s), the difference is negligible (12.0s vs. 12.5s). The paper transparently reports both numbers, but the "as much as 2x" framing in the abstract is misleading because the more natural comparison shows minimal speedup. The speedup claim should be qualified to specify it applies to the backtrace-enabled variant, or dropped from the abstract.

4. **Insufficient detail on FSM construction for complex API signatures.** Section 3.1 and Section 4.2 mention a "JSON-based function argument FSM" for handling RESTful APIs, but provide no specification of how it handles nested objects, arrays, optional parameters, or context-dependent argument structures that real-world REST APIs (such as TMDB endpoints with optional query parameters) require. The paper states "any grammar checker that tells the set of valid next tokens suffice," which is theoretically correct but sidesteps the engineering reality of building a practical grammar for arbitrary REST APIs. Providing at least one worked example (FSM for a representative complex API) would substantially improve reproducibility and the reader's ability to assess the method's generality.

### Trivial
5. **No discussion of edge cases in argument parsing.** The paper does not discuss whether the "IntFSM" handles edge cases such as negative numbers, leading zeros, or scientific notation, or whether any valid but syntactically unconventional tool calls could be erroneously blocked. A brief discussion of FSM design decisions for argument types would be helpful.

## Nice-to-Haves

- **Stronger ICL baselines on KAMEL**: The few-shot and zero-shot baselines on KAMEL are limited by context length, as the paper acknowledges. A retrieval-augmented ICL baseline that selects relevant tool documentation dynamically would provide a more meaningful comparison for large tool sets.
- **Ablation isolating name FSM vs. argument FSM**: The paper does not ablate the contribution of the tool-name trie separately from the argument-type FSM. Applying only the name constraint or only the argument constraint would clarify which component drives the error reduction.
- **Computational overhead analysis**: While inference time is reported, the per-step cost of computing the masked vocabulary (zeroing out invalid tokens) is not measured. For large tool sets or large vocabularies, this could become non-negligible, and a wall-clock breakdown of ToolDec vs. unconstrained decoding would be informative.

## Removed Points

- **"The paper does not analyze cases where ToolDec might prevent correct but unconventional tool calls"** → Kept as Trivial weakness 5, which is a reasonable request for completeness.
- **"Win Rate metric relies on automatic evaluator"** → The paper already transparently reports the 75.8% correlation with human annotators (Section 4.1). This is a standard limitation of automatic evaluation, not a weakness specific to this paper.
- **"KAMEL ICL baselines are weak"** → The paper acknowledges the context-length limitation, and the RestGPT comparison fills the gap with a stronger ICL baseline. Weakened to Nice-to-Have.
- **"No formal definition of syntax errors"** → Figure 4 shows three error types with clear operational definitions (name error, argument type error, number of arguments error). A formal definition would be nice but is not missing in a way that harms understanding.
- **"No ablation isolating name FSM from argument FSM"** → Moved to Nice-to-Haves, as the combined system's performance is the relevant result for the paper's claims.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully recontextualizes the work beyond what the authors already present.

## Suggestions

1. Revise the abstract and introduction to clearly distinguish between (a) the *when* decision (which may require training or instruction-tuned capabilities) and (b) the *which* and *how* decisions (which ToolDec handles without per-tool training or in-context documentation). Use precise language such as "requires no per-tool fine-tuning" rather than "no need for fine-tuning."
2. Add a comparison with a general grammar-constrained decoding baseline (e.g., Outlines + tool schema as CFG) on at least one benchmark to demonstrate whether ToolDec's specific FSM design matters or whether the gains are from constrained decoding broadly.
3. Qualify the speedup claim in the abstract to reflect the comparison condition (backtrace-enabled vs. no backtrace), or replace it with the more conservative comparison against the no-backtrace variant.
4. Provide the FSM construction for one representative complex API (e.g., a TMDB endpoint with nested parameters) in an appendix or supplementary material, even if it is just a schematic.

## Score and Decision

The paper presents a technically sound idea — using finite-state machines to constrain LLM decoding for tool calls — and demonstrates its effectiveness in reducing syntax errors and enabling generalization to unseen tools. The empirical evaluation is solid across multiple domains. The main issues are overclaiming in the abstract (the "no fine-tuning" framing) and a few omissions (comparison with other constrained-decoding methods, insufficient detail on complex API grammar construction, and selective speedup reporting). None of these are fatal; all are addressable with revisions. The core contribution — that FSM-guided decoding can eliminate tool call syntax errors and generalize to unseen tools using only tool names — is valid and practically useful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>