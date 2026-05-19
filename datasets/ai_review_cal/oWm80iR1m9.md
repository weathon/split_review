- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces SOP-Agent, a framework that guides general-purpose AI agents using Standard Operating Procedures (SOPs) represented as decision graphs. The agent traverses the graph via selective depth-first search, with filtered tool sets at each step. The system is evaluated across five domains (ALFWorld, HotpotQA, code generation, data cleaning, and a newly introduced customer service benchmark), showing performance that broadly exceeds general-purpose agents and is competitive with domain-specific systems.

---

## Strengths

1. **Novel decision-graph representation of SOPs with adaptive DFS traversal (Section 3.1–3.3).** The paper formalizes SOPs as decision graphs where nodes are candidate actions and edges are IF/ALWAYS conditions. The selective DFS traversal using function calls enables dynamic branching and plan adaptation going beyond prior hardcoded workflows (MetaGPT) or strictly sequential flows (FLAP), which the paper explicitly contrasts (Section 2, discussion of Roy et al. 2024).

2. **First benchmark for grounded decision-making in customer service (Section 5.1).** The Grounded Customer Service Benchmark covers 5 industries × 10 use cases = 50 test scenarios with path accuracy and leaf accuracy metrics. SOP-Agent achieves 99.8% overall path accuracy. The paper is upfront that the benchmark primarily serves to evaluate SOP-grounded agents and the baselines are included "solely to identify gaps" rather than as competitive comparisons (line 192).

3. **Strong empirical versatility across four distinct domains.** The paper evaluates on embodied decision-making (ALFWorld), multi-hop QA (HotpotQA), code generation (HumanEval/MBPP), and data cleaning. The SOP-Agent outperforms AutoGPT by 66.2% (zero-shot ALFWorld), achieves 86.6 Pass@1 on HumanEval (competitive with domain-specific coding systems), and attains 100% success on data cleaning tasks. This breadth supports the claim of versatility.

4. **SOP engineering procedure achieves near-perfect robustness on the new benchmark (Section 5, Algorithm 2).** The manual refinement process is described clearly, and the 99.8% accuracy result directly supports the paper's third contribution.

---

## Weaknesses

### Fatal
*None.* The paper has real methodological gaps, but they do not invalidate the core contribution.

### Major

1. **Missing ablation isolates the graph traversal mechanism from SOP content.** The paper never compares SOP-Agent (decision graph + DFS traversal + filtered tools) to a version of the same base agent that receives the identical SOP as a flat textual prompt *without* graph traversal. Such an ablation is essential to attribute gains to the graph-based mechanism rather than to the domain knowledge content of the SOP itself. The paper repeatedly claims that the selective DFS traversal and filtered action space improve robustness (e.g., Conclusion, line 207), but no experiment controls for the confound that the SOP's information content alone (delivered as text) might produce similar results. In the customer service benchmark (Section 5), the baseline is a zero-shot ReAct receiving bullet-point SOP text — but this differs from the SOP-Agent in more than just the graph (different base agent setup, different prompt structure), making an apples-to-apples comparison impossible.

2. **The conversion from natural-language SOP to decision graph is not explained.** The paper states that SOPs are "pseudocode-style written in natural language" and are "represented as decision graphs" (Section 3.1, line 52), but never specifies how this representation is constructed. Is the SOP authored directly as a graph by the user? Is there a parsing step? The paper provides no protocol, template, example decision graph, or algorithm for this step. For a framework whose core claim is enabling users to build complex domain-specific agents via natural language workflows, the actual mechanism by which a user's natural-language description becomes a formally traversable graph structure remains opaque, harming reproducibility.

### Minor

3. **HotpotQA results show only marginal gains (+1.6% EM, +0.02 F1).** The paper acknowledges this (line 116) and pivots to behavioral ablation (search/lookup patterns). The behavioral changes (fewer redundant searches, deeper lookups) are interesting but do not translate into meaningful accuracy gains on the primary metric. This weakens the claim that SOP guidance substantially improves search-and-reasoning performance.

4. **No statistical significance or confidence intervals reported.** None of the experiments report variance, confidence intervals, or statistical tests. Given moderate sample sizes (134 ALFWorld tests, 200 HotpotQA questions), this is a concern — especially for the 4.5% ALFWorld improvement over ReAct, which could be within noise.

5. **Benchmark generation uses GPT-4 to propose SOPs, potentially biasing results toward GPT-4-based agents.** The paper acknowledges this risk (line 192: "our dataset creation process inherently introduces biases") but does not mitigate it. Since both SOP-Agent and the ReAct baseline use GPT-4, this partly addresses the concern, but the benchmark's construction methodology introduces a confound between task difficulty and model capabilities.

6. **No systematic analysis of failure modes.** The ALFWorld experiment notes that "sometimes the LLM doesn't follow the SOP" (line 98) but provides no quantitative analysis of when or why this occurs. The 0.2% failure cases in the customer service benchmark are not analyzed. Understanding these failure patterns would strengthen the paper's claims about robustness.

7. **Method description lacks formal specification.** The DFS traversal and branching mechanism are described textually but no formal pseudocode or algorithm block is provided. Given that the paper emphasizes pseudocode-style SOPs, providing actual pseudocode for the traversal procedure would aid reproducibility.

### Trivial

8. The claim of being "the first system for building complex domain-specific agents with natural language workflow" (line 22) requires more precise scoping — FLAP (Roy et al., 2024, cited) and AutoGPT+P (Birr et al., 2024, cited) already use predefined workflows, though they don't handle branching/looping as SOP-Agent does. The claim holds if qualified to "first system handling branching and looping without planners or simulators," which is what the related work section actually argues (line 35).

---

## Nice-to-Haves

- A controlled ablation comparing SOP-Agent (with decision graph) to the same base agent given the same SOP as structured text (without graph traversal or filtered tools). This would definitively isolate the contribution of the graph mechanism vs. SOP content.
- Reporting LLM query counts and cost per task, which is relevant for practical deployment.
- Testing robustness to noisy, incomplete, or inconsistent SOPs, since real-world users may not write optimal workflows.
- Including plain-Act/ReAct baselines without SOP in the code generation experiments (Section 4.3) to quantify the value added by the code-generation SOP.

---

## Removed Points

These points from the harsh critic are flagged to be removed; treat them with caution:

- **"Unfair comparisons across all experiments"** — The critic frames comparisons as "unfair" because SOP-Agent gets domain knowledge via SOPs while baselines do not. However, this is the paper's core thesis: injecting domain knowledge via SOPs improves performance. The comparison is not unfair, it's missing a specific ablation (see Major weakness #1). Moving to Major #1 with proper framing.
- **"Scores above 90 are now common; 86.6 is below recent systems" (code generation)** — The paper compares against AgentCoder, MetaGPT, MapCoder, L2MAC, OctoCoder, ANPL, and Parsel. The critic's reference to "SWE-agent" and unspecified 90+ systems is not verifiable from the paper's data, and the paper's comparisons are to contemporaneous published methods. Removed as speculative.
- **"Abstract/Introduction overclaim"** — The paper's own related work (Section 2) distinguishes its approach (branching/looping without planners) from prior workflow grounding methods. The claim is appropriately scoped given that differentiation. Removed.
- **"Section 3 branching description is confusing"** — The paper clearly describes the two scenarios for indistinguishability and the dummy-function-call fallback (lines 66–68). This is a concrete description, not a vague one. Removed.
- **"Not testing generalization to datasets with unseen issues or SOPs" (data cleaning)** — This demands scope outside what the paper set out to demonstrate (a feasibility study of SOP-guided data cleaning). Nice-to-have, not a weakness.
- **"AutoGPT+IL comparison is misleading"** — The IL model is trained on expert demonstrations, but the SOP is also hand-crafted. Both incorporate domain knowledge through different channels; the comparison is apples-to-apples in that both use external knowledge. Removed.
- **Strength Finder items about "strong empirical versatility" etc.** — Kept where they are concrete and edition-specific. Removed generic/superficial praise that lacked specific grounding.

---

## Novel Insights

The most interesting observation emerges from the HotpotQA behavioral analysis (Table 4): even though the SOP only marginally improves primary metrics, it substantially changes *how* the agent searches — reducing redundant queries and increasing lookup depth. This suggests that SOP guidance primarily affects the agent's exploration strategy rather than its final answer accuracy, which raises the question of whether SOPs' value is in process regularization rather than outcome improvement. The reviewer set did not surface this tension explicitly in their analyses; it emerged from cross-referencing the behavioral results with the mixed accuracy findings.

---

## Suggestions

1. **Add the central ablation:** compare SOP-Agent (decision graph + DFS + filtered tools) against the same base agent receiving the identical SOP as a structured textual prompt without graph traversal, on at least one task (ALFWorld or the customer service benchmark). This is the single most important experiment missing from the paper.

2. **Clarify the SOP authoring process.** Provide an explicit example/template showing the input format (is it JSON? YAML? free text with a specific structure?) and explain how the decision graph is constructed from it. If it's manual, state that clearly. A figure with an end-to-end example from user input to graph traversal would address the reproducibility gap.

3. **Report variance** (standard deviations or confidence intervals) for all main results, particularly where sample sizes are modest (ALFWorld: 134 tests, HotpotQA: 200 questions).

4. **Provide formal pseudocode** for the DFS traversal algorithm (Section 3.3) to match the paper's emphasis on pseudocode-style methods.

---

**Originality:** 7/10 — Decision-graph representation of SOPs with DFS traversal is a novel synthesis of existing ideas (workflow grounding + decision graphs + LLM agents), but the individual components are not entirely new.  
**Importance of research question:** 8/10 — Integrating domain knowledge into general-purpose agents is a practically important problem.  
**Claims well-supported:** 5/10 — The overall empirical demonstration is strong, but the central claim about the graph mechanism's value is not adequately isolated from the value of the SOP content itself.  
**Soundness of experiments:** 6/10 — Breadth is good, but the missing ablation and lack of statistical significance reporting are notable gaps.  
**Clarity of writing:** 7/10 — Generally well-structured and readable, though the method section would benefit from formal specification.  
**Value to community:** 7/10 — The benchmark and the framework concept are useful; the paper would be strengthened by addressing the identified weaknesses.
