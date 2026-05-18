Now I have all the information I need to produce the final consolidated review.

## Summary

This paper proposes TOOLDEC, a finite-state machine (FSM) guided decoding algorithm for tool-augmented LLMs. The key idea is to construct an FSM from tool signatures (names and argument types) and use it to constrain decoding so that only syntactically valid tool calls are generated. TOOLDEC is demonstrated as a drop-in enhancement for both in-context learning (ToolLLM) and fine-tuning (ToolkenGPT) paradigms, completely eliminating tool-related syntax errors across all experiments. The paper further shows that TOOLDEC generalizes to unseen tools without additional fine-tuning or in-context documentation across three domains: math functions (FuncQA), knowledge graph relations (KAMEL), and real-world REST APIs (RestBench), achieving substantial gains over baselines (up to 8×).

## Strengths

- **Zero syntax errors, empirically validated across two paradigms**: Figure 4 and Table 4 show that TOOLDEC reduces tool-related errors (name, argument, type) to 0% across both ToolLLM (in-context learning) and ToolkenGPT (fine-tuning) setups. In FuncQA_multi (Table 4), TOOLDEC achieves 0% tool error rate vs. 27.9%–38.2% for baselines. This directly validates the core claim.

- **Strong generalization to unseen tools across three diverse domains**: On FuncQA (9 unseen math tools, Figure 5a), TOOLDEC maintains high accuracy while ToolkenGPT collapses. On KAMEL (up to 204 unseen knowledge relations, Figure 5b), TOOLDEC keeps near-constant accuracy as the tool count grows while all baselines plummet. On RestBench (Table 5), TOOLDEC achieves 32% correct path rate *without* in-context documentation, outperforming the baseline (24%) that *has* documentation. This evidence supports the paper's second main claim convincingly.

- **Inference speedup from eliminating erroneous tool calls**: Table 4 shows TOOLDEC reduces average inference time per problem on FuncQA_multi substantially vs. both ToolkenGPT variants — achieving roughly 2× speedup over the backtrace variant. The speedup is a direct, well-explained consequence of eliminating failed tool calls that waste decoding steps.

- **Drop-in compatibility across paradigms**: Section 4.2 describes how TOOLDEC integrates with ToolLLM (ReAct-based planning, requiring three FSM components including a JSON argument FSM) and with ToolkenGPT (only constraining arguments). Tables 3 and 4 show improved results in both settings with no architectural changes, demonstrating broad applicability.

- **Automatic FSM construction from tool signatures**: Section 3.1 and Figure 2 detail the trie-based construction for tool names and sub-FSM composition for argument types (e.g., IntFSM). The method does not require manual grammar design per tool.

## Weaknesses

### Fatal
None.

### Major

- **Under-specified handling of complex argument types, limiting the generality claim.** The paper claims TOOLDEC handles "arbitrary tool arguments" via FSMs, but the description falls short in critical places. For ToolLLM, a "JSON-based function argument FSM" is mentioned (line 133) with no detail on how nested objects, optional fields, or arrays are handled — structures common in real REST APIs. The paper states "any grammar checker that tells the set of valid next tokens suffice" (line 95), but this hand-waves the complexity. For RestBench (line 192), the authors explicitly use an LLM to rewrite APIs into a simpler function-call format, circumventing the original REST structure. This is a significant departure from the claimed generality. The reader cannot assess whether the FSM approach works out-of-the-box for, say, a REST endpoint expecting a JSON body with nested lists, or whether manual simplification or rewriting is always needed. The paper should clarify the scope of FSM construction and, where it falls short, explicitly state limitations rather than claim full generality.

### Minor

- **The generalization claim rests on an untested boundary condition.** Section 3.3 explicitly states two assumptions: (i) LLMs know plausible tool names, and (ii) tool names are semantically meaningful. The paper mentions (line 106) that if names are poor, an LLM can rename them, but this is neither implemented nor evaluated. All experiments use tools with highly descriptive names (multiply, number_of_children, search_movie). Without evidence that the method works when names are opaque, misleading, or when the LLM has no prior knowledge of plausible function names, the generalization claim is supported only under favorable conditions. The authors are transparent about the assumption, but the paper would be strengthened by stress-testing this boundary.

- **The "no fine-tuning" framing is imprecise.** The abstract claims TOOLDEC has "no need for fine-tuning" (line 8), and the conclusion says "without additional fine-tuning data" (line 217). However, Section 5.1 reveals that the <T> mode-switching token is indeed fine-tuned (embedding tuned on seen tools, lines 177–179). The paper's actual achievement — that TOOLDEC requires *no additional fine-tuning for new unseen tools* — is valuable and correct, but the unqualified phrasing could mislead readers into thinking absolutely no fine-tuning is involved anywhere.

- **Inference speedup data is only reported for one experimental setting (FuncQA).** The abstract claims "as much as 50% less inference time" and "2x speedup," but the only timing data is from the ToolkenGPT experiments (Table 4). No inference time is reported for the ToolLLM experiments, even though the paper states that TOOLDEC "resulted in shorter inference time" (line 113) in that setting too. The existing claim is technically accurate ("as much as") but would be stronger if timing data were reported consistently.

- **Parsing procedure for free-text baselines on KAMEL is not described.** The accuracy metric on KAMEL (line 183) is "the proportion of responses that invoke the correct knowledge relation." For TOOLDEC this is straightforward (the FSM enforces valid names), but for the free-text baselines (prompting, few-shot, zero-shot), it is unclear how responses are parsed to determine which relation was invoked. If this relies on pattern matching or an LLM-as-judge, the procedure should be described to ensure fair comparison.

- **No statistical variance or significance reported for any result.** Key comparisons (e.g., Table 3 win rates, Table 4 accuracy, Figure 5 results) are reported as point estimates without confidence intervals or standard deviations. While single-run evaluation is common in the field, the absence is noticeable especially where TOOLDEC only marginally beats a baseline (e.g., 66.2% vs. 64.7% on FuncQA_multi in Table 4 — though the exact numbers are in the image).

### Trivial

- Section 3.3 discusses why TOOLDEC generalizes but could benefit from a concrete example showing the FSM gracefully handling an unseen tool name at runtime.
- The paper lacks a dedicated limitations discussion in the main text.

## Nice-to-Haves

- Report inference time for the ToolLLM experiments to support the speedup claim in that setting.
- Add a brief analysis explaining *why* fuzzy matching fails to improve win rate while TOOLDEC succeeds (the paper notes it's because "wrong APIs could often be chosen" but does not elaborate).
- Discuss the overhead of constructing FSMs for the ToolLLM setting (JSON schema parsing, trie construction).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The 'drop-in replacement' claim is softened because building FSMs required integration work"* — The paper uses "drop-in replacement" for the decoding algorithm specifically, which is accurate; integration overhead is expected and discussed (Section 4.2).
- *"Data contamination concern for Vicuna/TMDB"* — Speculative; no evidence that Vicuna was exposed to TMDB APIs during training, and this is not a standard concern raised in tool-use papers.
- *"Missing related works"* — Removed per instructions (cannot verify external sources).
- *"Missing appendix/limitations section"* — Removed per instructions (parser strips appendices; they exist in the original submission).
- *"Pure formatting/style nitpicks"* — Removed per instructions.
- Several generic area-sweep speculations from the harsh critic (e.g., "could the metric be measuring a proxy?") — Removed for lacking a concrete anchor in the paper.
- Some strengths from the Strength Finder that are generic or sycophantic (e.g., "this paper addressed an important problem") — Removed as they lack specific, concrete content tied to the paper's evidence.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely converge on the paper's own framing: that FSM-constrained decoding eliminates syntax errors and enables generalization via tool names alone. No cross-review synthesis revealed a non-obvious insight about the method or the problem that the paper itself does not already articulate.

## Suggestions

- **Clarify FSM construction for complex types.** Provide a concrete example (or reference to a known construction method) showing how nested JSON schemas, optional fields, and arrays are handled. If the current approach does not handle them out-of-the-box, state this explicitly as a limitation rather than claiming full generality.
- **Stress-test the naming assumption.** Run an experiment where tool names are partially obfuscated (e.g., replaced with non-indicative strings) to measure how TOOLDEC's generalization degrades. This would directly validate the boundary condition acknowledged in Section 3.3.
- **Rephrase the "no fine-tuning" claim** to precisely state: "no additional fine-tuning is needed for unseen tools" (as opposed to "no fine-tuning" in absolute terms).
- **Report inference time for the ToolLLM experiment** (Experiment I) or remove the unqualified speedup claim from that section.
- **Describe the parsing pipeline** for free-text baselines on KAMEL to rule out evaluation bias.

## Score and Decision

Originality: The core technique (FSM-constrained decoding for tool call validity) is a simple but effective combination of existing ideas (constrained decoding + FSMs), applied to an important problem. The generalization finding — that constraining to valid tool names enables zero-shot selection — is a valuable empirical result.  
Importance of research question: High. Syntax errors in tool calls are a practical bottleneck in deployed tool-augmented LLMs.  
Claims supported: The central claims (zero syntax errors, generalization, speedup) are well-supported by experiments, though the scope of FSM construction for complex types is overstated.  
Soundness: Experimental design is appropriate and comparisons are fair. The generalization experiments are particularly well-designed with controlled seen/unseen splits.  
Clarity: Generally clear and well-structured. Some framing imprecisions ("no fine-tuning," speedup scope).  
Value to community: High. The method is simple, practical, and achieves strong results. It should be easily adoptable by practitioners.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>