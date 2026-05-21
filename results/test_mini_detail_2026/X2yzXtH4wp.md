Now I have my calibration anchors. Let me synthesize the final review.

## Summary
The paper introduces Ambig-SWE, an underspecified variant of SWE-Bench Verified, and evaluates six LLM agents on their ability to handle missing information in software engineering tasks. The authors decompose underspecificity resolution into three sub-capabilities (detection, targeted questioning, and interactive integration) and design experiments for each. Key findings include that interaction can recover up to 76% of the performance gap caused by underspecification, but most models fail to detect missing information autonomously. The strongest contribution is the diagnostic framework itself and the empirical analysis of how different models approach each sub-capability.

## Strengths
1. **Three-step decomposition provides a diagnostic framework.** The paper breaks resolution of underspecified instructions into detection, questioning, and integration — each evaluated separately (Sections 3–5). This is a conceptual improvement over prior work that treats underspecificity as a single missing detail. The framework enables targeted analysis (e.g., Qwen 3 Coder asks many questions but integrates poorly, Llama 3.1 asks vague questions and gets minimal information).

2. **Systematic multi-setting evaluation with controlled comparisons.** The Full / Hidden / Interaction design (Figure 2, Section 2.3) cleanly isolates the effect of missing information from the effect of interaction. The finding that Claude Sonnet 4 recovers 89% of its full-information performance through interaction (Hidden: 40% → Interaction: 61.4%, Full: 68%) is concrete and well-supported. The analysis of navigational vs. informational details (Table 1) adds useful granularity — showing, for example, that Qwen 3 Coder's performance actually *worsens* when given file locations it could find itself (55.43% → 52.38%).

3. **Conservative user proxy design.** The GPT-4o proxy responds only with information present in the full issue and says "I don't have that information" for missing details (Section 2.2). This avoids hallucinated answers that would confound the evaluation, a methodological improvement over less constrained proxies.

4. **Qualitative and quantitative analysis of question strategies.** Figure 4 and Section 5.3 provide concrete examples of question quality differences — Llama 3.1 asks vague questions like "Are there any existing workarounds?" while Claude Haiku asks about specific file locations and error behavior. The paper also quantifies that Claude Sonnet 4 achieves comparable information gain to Qwen 3 Coder with 50% fewer questions (4.03 vs. 6.02), identifying exploration-first as a more efficient strategy.

## Weaknesses

### Fatal
None.

### Major
1. **Synthetic underspecification diverges from real-world patterns.** The dataset is constructed by having GPT-4o strip details from well-specified SWE-Bench Verified issues. The paper's own distributional analysis (lines 67–72) confirms that natural underspecified issues contain more code snippets, error messages, file references, and conversational fragments — precisely the technical content that the synthesis procedure aggressively removes. The authors argue this is acceptable because "agents cannot access external information," but this is a non sequitur for code snippets and error messages, which directly affect what information agents have. The benchmark therefore tests a specific, artificially clean form of underspecification whose relationship to natural ambiguity is uncalibrated. The paper acknowledges this limitation but does not validate on any natural underspecified examples, even a small set to check whether trends hold.

2. **User proxy is idealized, inflating apparent interaction value.** The GPT-4o proxy is always cooperative, perfectly knowledgeable about the full specification, never forgetful, and never misleading (Section 2.2). Real users often do not know the full specification, give partial or conflicting information, or disengage. The paper acknowledges this briefly in limitations (line 285) but the entire quantitative story about interaction benefits (up to 76% gap recovery) rests on this best-case assumption. Without any stress-testing of the proxy (e.g., partial knowledge, occasional uncooperativeness), the results overstate the expected real-world value of interaction.

3. **RQ2 confounds detection with prompt compliance.** The detection experiment (Section 4) presents models with full or hidden issues under varying prompts about interaction. The metric equates "choosing to interact on a hidden issue" with "detecting underspecificity." However, under Strong Encouragement ("asking questions is critical to task success"), a model that simply follows this instruction and interacts on both types is not detecting underspecificity — it is complying. The finding that Claude Sonnet 4 achieves 89% accuracy under Strong with an FPR of only 0.03 does suggest some genuine discrimination (since pure compliance would yield high FPR), but the experiment cannot cleanly isolate detection ability from prompt-following behavior. A direct classification task ("Is this issue underspecified?") would have been a cleaner test.

### Minor
1. **Turn limit imbalance is a confound.** Claude Sonnet 4 and Qwen 3 Coder are allocated up to 100 turns, while other models get 30 (line 110). Because these models can use more turns to gather more information, their superior Interaction performance may partly reflect the extra opportunity rather than superior capability. The paper does not control for this or analyze how many turns each model actually uses.

2. **Incomplete statistical reporting.** Several important comparisons are reported without significance tests or confidence intervals — e.g., the Qwen 3 Coder performance difference with/without navigational info (55.43% vs. 52.38%, Table 1), relative recovery percentages, and the claim about Claude Haiku achieving similar relative recovery to Claude Sonnet 3.5 despite weaker coding ability.

3. **The "74% improvement" claim lacks context.** The abstract and introduction state "up to 74% improvement over the non-interactive settings" without clarifying that interaction was compelled/forced in the experiment. This framing could mislead readers into thinking models voluntarily asked questions and improved.

### Trivial
- Table 2 is dense and would benefit from visual encoding (e.g., color scale) to highlight patterns.
- The 30 vs. 100 turn allocation justification ("account for their greater reasoning and planning capacity") is asserted but not empirically supported.

## Nice-to-Haves
- **Direct detection test:** A direct classification task ("Is this issue fully specified?") would cleanly separate detection ability from interaction propensity, strengthening RQ2 considerably.
- **Proxy stress-testing:** Even one additional condition where the proxy has partial knowledge (e.g., knows 50% of missing details) would bound the interaction benefits and demonstrate robustness.
- **Cost/efficiency analysis:** A table of average API cost per resolved instance would help practitioners evaluate the practical tradeoff between interaction overhead and performance gains.
- **Human baseline:** Professional developers completing a subset of underspecified tasks with interaction would calibrate how far current models are from human-level ambiguity resolution.

## Removed Points
- *"RQ2 results for Qwen 3 Coder (0% interaction rate) raise concerns about that model's training"*: This is already discussed by the paper and is a valid finding from the experiment, not a weakness of the paper.
- *"The paper would benefit from a direct comparison of Ambig-SWE's underspecification complexity with prior datasets"*: The paper draws the relevant distinction (prior work focuses on single missing details; this work involves multiple interdependent gaps). Quantifying "how many missing details" is not straightforward given the different task structures.
- *"Missing related works"*: Removed per instructions — I cannot verify what related works exist.
- *"Prompt for generating underspecified issues not specified with temperature/number of generations"*: These are trivial implementation details impractical to include in a submission.
- *"The cosine distance metric is opaque"*: The paper acknowledges this as a limitation (line 285), and it is a secondary metric. The LLM-as-judge scores provide convergent validation.
- *Generic strengths about "addressing an important problem"*: Removed — not specific enough to be informative.

## Novel Insights
The most interesting finding that emerges from the cross-model comparison is the *disconnect between extraction quantity and task success*. Qwen 3 Coder extracts the most information (highest cosine distance, most questions) but performs comparably to or worse than Claude Sonnet 4, which asks fewer questions through an exploration-first strategy. This suggests a non-obvious training gap: current models are not optimized to *not ask* when they can infer independently. Similarly, the finding that Claude Sonnet 4 achieves similar information gain to Qwen 3 Coder with 50% fewer questions identifies a concrete axis for improving agent efficiency that is not captured by pass-rate metrics alone.

## Suggestions
1. Validate on a small set (e.g., 20–30) of naturally underspecified SWE-Bench examples (even without paired full specifications) to check whether the relative ordering of models and the benefits of interaction hold.
2. Add a direct classification condition to RQ2: present each issue and ask the model "Does this issue contain enough information to proceed?" Compare accuracy with the agentic interaction decision to isolate where the bottleneck truly lies.
3. Stress-test the user proxy with a partial-knowledge condition (e.g., the proxy knows 50% of missing details or gives slightly vague answers for some queries) to bound how sensitive the interaction benefits are to proxy quality.
4. Equalize turn limits or justify the asymmetric allocation with data on actual turn usage. Report significance tests for the key comparisons in Tables 1 and the relative recovery rates.

## Score and Decision

### Round 1 — Bracketing
I retrieved three bands:
- **Weak anchors** (avg 2.0–3.3): RExBench (3.00), Lita (3.33), APTBench (3.33), SecTest-Eval (2.00). These papers are clearly weaker than Ambig-SWE — they have narrower scope, less rigorous evaluation, or fundamental flaws.
- **Middle anchors** (avg 4.0–4.67): SWE-Refactor (4.67), SWE-Bench Pro (4.50), FeatBench (4.00), Automated Benchmark Generation (4.00). These are the most relevant comparison group. SWE-Refactor was criticized for limited refactoring scope and outdated models; SWE-Bench Pro was seen as incremental; FeatBench had limited novelty. Ambig-SWE has a more novel conceptual framework but also has methodological concerns.
- **Strong anchors** (avg 8.0): Gaia2 (8.00), "LLMs Get Lost in Multi-Turn Conversation" (8.00). These papers have cleaner methodology and more extensive evaluation. Ambig-SWE is clearly below this level.

**Round-1 bracket**: between 4.5 and 6.5.

### Round 2 — Narrowing
I retrieved anchors in (4.5, 6.5) and (5.0, 7.0):
- **VitaBench** (5.50, Accept Poster): Comparable quality — has broad real-world agent evaluation but also ideal user simulator concerns. Ambig-SWE has a more focused novel contribution (underspecification decomposition) but narrower evaluation scope. About equal.
- **OS-MAP** (5.50, Reject): Mixed reviews (4,10,4,4). The taxonomy contribution was questioned by some. Ambig-SWE's three-step framework is more clearly useful.
- **SOPBench** (5.00, Reject): Cleaner evaluation (oracle code verifiers) but the core novelty was questioned (similar to function-calling benchmarks). Ambig-SWE has clearer novelty.
- **SCUBA** (4.80, Accept Poster): Narrow scope (Salesforce-specific), strong engineering but limited novelty. Ambig-SWE is stronger in conceptual contribution.
- **AQuA** (5.50, Accept Poster): Ambiguity in VQA — different domain, similar approach to categorization.
- **UProp** (5.50, Reject): Uncertainty propagation for LLM decisions. Different domain.

### Final Score

Against the round-2 anchors: Ambig-SWE sits between the 4.80–5.00 papers (SCUBA, SOPBench) and the 5.50 papers (VitaBench, OS-MAP). It has a stronger conceptual contribution than SOPBench and SCUBA, and is comparable to VitaBench in overall quality. However, the synthetic dataset concern and the RQ2 confound are genuine limitations that prevent it from reaching 6.0. 

Relative to "LLMs Get Lost in Multi-Turn Conversation" (8.00) — the most topically similar strong paper — Ambig-SWE has a less clean experimental design (turn limit confound, proxy idealization, synthetic dataset) and a narrower scope (SWE only vs. six generation tasks). The 8.00 paper's separation of aptitude and reliability is methodologically sharper than Ambig-SWE's detection experiment.

I score this paper **5.5**. The ideas are worth pursuing, the diagnostic framework is useful, and the empirical findings are informative. However, the evaluation methodology has notable limitations that the authors should address in revision. The paper is a borderline case that could reach acceptance with substantial revisions addressing the major weaknesses.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>