Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes TOOLDEC, a finite-state machine (FSM) guided decoding algorithm for tool-augmented LLMs. It constrains token generation to valid tool names and type-conforming arguments at each decoding step, guaranteeing syntax-error-free tool calls. The method is applied as a drop-in enhancement to both in-context learning (ToolLLM, RestGPT) and fine-tuning (ToolkenGPT) baselines, demonstrating elimination of tool-related errors, improved task performance, and modest speedups on several benchmarks. The paper also claims that TOOLDEC generalizes to unseen tools without additional fine-tuning or in-context documentation.

## Strengths

- **Guaranteed elimination of all syntactic tool-call errors is convincingly demonstrated.** Across both ToolEval (REST APIs) and FuncQA_multi (math functions), TOOLDEC reduces tool name errors, argument type errors, and formatting errors to zero (Figure 4, Table 4). This is not merely a theoretical guarantee—the paper shows this translates into measurable improvements in win rate, pass rate, and accuracy. The error rate reductions from ~20-28% to 0% on FuncQA_multi (Table 4) are clean and unambiguous.

- **Broad applicability across different LLM paradigms and tool domains.** TOOLDEC is integrated with an in-context learning method (ToolLLM on 10k+ REST APIs), a fine-tuning method (ToolkenGPT on math functions), and another ICL method (RestGPT on real-world web services). The experiments span mathematical functions, knowledge graph relations, and complex RESTful APIs, demonstrating genuine generality.

- **Principled and automatic FSM construction from tool signatures.** The FSM is built directly from tool names (via a trie) and argument types (via sub-FSMs), as described in Sections 3.1–3.3. This makes adoption of new tools fully automatic—no manual grammar writing or data collection is needed—which is a practical advantage over alternatives like fuzzy matching or backtrace.

- **Real (if modest) benefits on the ToolEval benchmark.** On the challenging I2-Category and I3-Instruction subsets, TOOLDEC-enhanced ToolLLM achieves higher win rate and pass rate than the base ToolLLM, fuzzy matching variants, and even ChatGPT (Table 3). This demonstrates that eliminating syntax errors has downstream task-level benefits.

## Weaknesses

### Fatal
None.

### Major

- **The headline "8x better" generalization claim against ToolkenGPT (FuncQA, Figure 5a) compares methods with fundamentally different architectural capabilities, overstating the result.** ToolkenGPT requires a trained embedding per tool; it literally cannot generate names for tools it was not fine-tuned on. TOOLDEC, by contrast, uses the FSM to constrain generation from the full tool list regardless of fine-tuning. The drop to near-0% for ToolkenGPT on unseen tools is an architectural limitation, not a failure of generalization in any typical sense. The 40-80% accuracy TOOLDEC achieves on unseen tools is genuine and interesting, but the "8x" framing (based on comparing a near-zero baseline against TOOLDEC's non-zero accuracy) inflates the significance. The comparison is fairer on KAMEL (Figure 5b), where ICL baselines with access to tool descriptions are included and TOOLDEC still dominates. The authors should reframe this result to emphasize the *capability difference* (FSM enables zero-shot tool selection that fine-tuned embeddings cannot provide) rather than claiming "8x better generalization."

### Minor

- **The RestGPT experiment (Section 5.2) confounds two variables: adding the FSM and removing in-context documentation.** The comparison is RestGPT with full documentation (27% CP) vs. RestGPT+TOOLDEC without documentation (35% CP). While this demonstrates that TOOLDEC can operate without documentation, it does not isolate the FSM's contribution—the shorter prompt (1974 → 880 tokens) could independently improve reasoning. The authors should have included RestGPT without documentation and without FSM (which would likely get 0% since it cannot call tools) and RestGPT without documentation but with FSM to fully attribute the gain. The result is still informative, but the causal claim is weaker than presented.

- **The speedup claims (2× faster, 50% less inference time) are only demonstrated on FuncQA_multi (13 tools) and lack analysis of FSM overhead.** The paper reports wall-clock inference time for FuncQA_multi but does not measure or discuss the computational cost of FSM operations (token subset computation, trie traversal) at each decoding step. On larger tool sets like ToolEval (10,000+ APIs), the FSM overhead could dominate runtime. No speedup measurements are reported for the larger-scale experiments (ToolEval, KAMEL with 234 tools, RestBench with 55 APIs). The speedup benefits at scale are therefore unsubstantiated.

- **The two assumptions underlying the generalization claim (Section 3.3) are stated but not empirically tested.** The paper assumes (i) LLMs know plausible-sounding tool names and (ii) tool names are meaningful and indicative of their usage. These are critical for the method's core mechanism, yet the paper provides no analysis of when these assumptions hold or fail. For example, the paper does not report how often the LLM assigns high probability to the correct tool name vs. wrong plausible-sounding names, nor does it analyze failure cases where tool selection is incorrect. This makes it difficult to assess the method's limitations.

- **No ablation of the fine-tuned `<T>` token in the generalization experiments (Section 5.1).** The generalization setup fine-tunes a single `<T>` token embedding and uses the FSM for tool name selection. The contribution of the fine-tuned token vs. the FSM is not disentangled. Could the FSM alone (without the fine-tuned token) achieve similar results? This would strengthen the "no fine-tuning needed" claim.

### Trivial
None.

## Nice-to-Haves
- A controlled RestGPT experiment: RestGPT without documentation and without FSM vs. RestGPT without documentation with FSM, to isolate the FSM's contribution.
- Scalability analysis: measure FSM construction time, per-step overhead, and total inference time on the ToolEval scale (10k+ tools).
- Failure case analysis: when TOOLDEC selects the wrong tool, what does the LLM's probability distribution look like? This would validate or refute the assumptions in Section 3.3.
- Comparison with other constrained decoding frameworks (e.g., Guidance, LMQL) to contextualize the technical novelty.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. *"The method still requires the tool's API signature to construct the FSM—this conflates 'no documentation in the prompt' with 'no documentation needed.'"* — The paper is explicit (Section 1, Section 3) that the FSM is constructed from tool signatures. The distinction between "in-context documentation" and "API signature for FSM construction" is clearly maintained; this criticism reflects a misreading.

2. *"Section 3.2 mode switching description is not precise enough to replicate."* — The description covers both cases (self-decided via special tokens, and external planner via ReAct), and Section 4.2 provides implementation details for both ToolLLM and ToolkenGPT. This is within the norm for conference paper method descriptions.

3. *"Experiment I results are merely a direct consequence of the method, not an empirical discovery."* — Empirical verification of a theoretically guaranteed property is standard practice and valuable; many "obvious" guarantees fail in practice.

4. *"The 'Prompting' baseline on KAMEL is not a relevant comparison."* — This baseline is included as an additional reference (following Hao et al., 2023), not as a primary comparison. The paper's main KAMEL comparisons are against few-shot, zero-shot (which have tool information), and ToolkenGPT.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's two contributions: the syntax error elimination result is clean and well-supported but unsurprising (constrained decoding guarantees constraint satisfaction); the generalization claim is more novel but less rigorously supported. This is a common pattern in constrained decoding papers—the guarantee is the easy part, the empirical demonstration that the constraint helps task performance is the harder part, and the generalization to new settings requires careful experimental design to avoid overclaiming.

## Suggestions

1. **Reframe the generalization claim.** Acknowledge that the comparison against ToolkenGPT on FuncQA is between fundamentally different mechanisms. Emphasize the *capability* TOOLDEC provides (zero-shot tool selection from names alone) rather than framing it as "8× better generalization."

2. **Add a controlled RestGPT experiment.** Run RestGPT without documentation and without FSM (baseline) vs. RestGPT without documentation with FSM, even if only on a subset of RestBench, to isolate the FSM's contribution.

3. **Measure and report FSM overhead at scale.** Provide per-token overhead measurements and analyze how FSM construction/query time scales with the number of tools, especially in the ToolEval setting (10k+ APIs).

4. **Ablate the fine-tuned `<T>` token.** In the generalization setup, compare TOOLDEC with and without the fine-tuned `<T>` token to determine whether any fine-tuning is needed at all.

5. **Add a failure analysis.** Report when TOOLDEC selects wrong tools and analyze whether this occurs because the LLM assigns low probability to the correct name or because multiple plausible names compete. This would validate the assumptions in Section 3.3.

The paper's core contribution—FSM-constrained decoding for syntax-error-free tool calls—is solid, clearly explained, and practically useful. The generalization experiments show a real capability that fine-tuning approaches lack. However, the "8× better" framing overreaches, and several experimental design choices weaken the causal claims. With measured framing and additional controls, this would be a stronger paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>