## Summary

MermaidFlow introduces a declarative graph representation for agentic workflows using the Mermaid markup language, cleanly separating planning from execution. It couples this representation with safety-constrained evolutionary programming operators (crossover, mutation, insertion, deletion) that preserve type correctness and static verifiability. The paper reports consistent improvements over 13 baselines across GSM8K, MATH, HumanEval, and MBPP, along with higher generation reliability (~90% valid code vs. ~50% for code-based AFlow) and better token efficiency.

## Strengths

- **Consistent SOTA across four benchmarks (Table 1):** MermaidFlow achieves the highest average score (80.75%), outperforming the best baseline MaAS (79.35%) by 1.40 points and the second-best automated method AFlow (78.67%) by over 2 points. The gains are most pronounced on the harder MATH benchmark (+2.61% over AFlow).

- **Substantially higher generation reliability (Section 5.3):** The paper reports that MermaidFlow consistently yields >90% success rate in producing valid executable Python code, compared to AFlow's ~50%. This is a direct empirical demonstration of the central thesis: the declarative, typed graph space makes LLM-based optimization far more reliable than operating over raw Python code.

- **Provably closed search space (Lemma 1, Section 4.1):** The paper formally states and argues closure: for any workflow in the valid space \(\mathcal{S}\) and any operator in \(\mathbb{O}\), the resulting graph remains in \(\mathcal{S}\). This distinguishes MermaidFlow from prior work where mutations frequently produce invalid states requiring expensive filtering.

- **Concrete case study illustrating composable evolution (Figure 4):** The HumanEval example traces how crossover between two parent workflows (one introducing a test node, the other a diverse ensemble) yields an improved child, with generated Python code faithfully preserving the combined structure. This grounds the abstract operators in a concrete, interpretable example.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification in experimental results (Table 1, Figure 3):** Results are reported as averages over only 3 runs with no variance, confidence intervals, or significance tests. On benchmarks where the margin over the strongest baseline is modest (GSM8K: +0.92% over MaAS; HumanEval: +1.30% over MaAS), it is impossible to assess whether these differences are meaningful or within noise. The training curves in Figure 3 show a single trajectory with no multiple-seed variation. This is the most significant gap in the evaluation, given that the claims of "consistent improvements" rest on these numbers.

- **"Guarantee" claim is stronger than what the system delivers (lines 88, 192-194):** The paper states it is "the first agentic workflow framework to **guarantee static graph-level correctness across the entire generation process**." However, the paper later acknowledges that "when using an LLM to generate a new Mermaid graph, the resulting Mermaid code may sometimes violate predefined safety constraints" and relies on a *post-hoc checker* to detect violations and regenerate. Lemma 1 correctly proves that the *operators* are closed under type constraints, but the end-to-end process depends on a checker that filters and regenerates. This is a meaningful overstatement — the paper would be more credible describing high validity rates rather than a formal guarantee.

### Minor

- **LLM-as-Judge component is not validated (Section 4.2):** The paper uses an "LLM-as-Judge" to select among candidates before expensive rollout-based evaluation. This is a significant methodological choice that could dominate search outcomes, yet its agreement with actual execution scores is never reported or ablated. Without validation, it is unclear whether the judge selects genuinely better workflows or introduces its own bias.

- **Token efficiency claim is anecdotal (Section 5.3):** The paper states that "when AFlow and MermaidFlow both surpass 52% on the MATH dataset, they consume 6.9e4 and 2.7e4 tokens respectively." This single data point is provided without describing how it was measured, over how many runs, or how the threshold was selected. This is a compelling claim that would benefit from a systematic comparison (e.g., total cumulative token usage over all search rounds).

- **>90% success rate for Mermaid→Python translation is stated without dedicated presentation (Section 5.3):** This claim is central to the paper's motivation but appears in passing without a dedicated figure, table, or failure analysis. Minor textual duplication in the paper suggests this was presented hastily.

- **MaAS baseline result on MBPP is cited as reported in the MaAS paper (Table 1, asterisk):** The authors did not reproduce this baseline, which departs from the otherwise consistent experimental control.

### Trivial
None.

## Nice-to-Haves

- Validate the LLM-as-Judge rankings against actual execution scores on a held-out set, or replace it with a cheaper proxy.
- Report cumulative token usage for all methods over the full search, not just at one performance threshold.
- Include a failure analysis of Mermaid→Python translation: how do failures occur and do they require human intervention?

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First" claim and positioning (Harsh Critic, Issue 3):** The criticism that the paper overstates its novelty and that the type system is only "user-specified strings" is not a substantive weakness. Every paper makes first-to-do-X claims, and the paper adequately differentiates itself from related work. The type system is described as domain-specific, which is a reasonable design choice.

- **Formatting/presentation nitpicks:** The harsh critic's notes about missing formal grammar for types, or Mermaid's "built-in static verifiability" being misleading, are too speculative or reflect the stripped appendix (Appendix A.1 is referenced). The paper appropriately handles the distinction between Mermaid syntax checking and its custom rules.

- **Strength Finder generic strengths:** Several strengths from the Strength Finder were removed or merged because they were generic (e.g., "Optimization LLM scaling translates to predictable gains" — this is a straightforward consequence of using stronger LLMs) or redundant with the main strengths already listed.

## Novel Insights

The reviews do surface one observation that goes beyond the paper's own claims: the trade-off between the "guarantee" framing and the checker-based implementation reveals a broader tension in the LLM+formal-methods space. Many systems claim formal properties while relying on LLMs whose outputs cannot be guaranteed a priori, then use a verifier as a safety net. The paper would benefit from explicitly acknowledging this pattern and positioning the checker not as an afterthought but as an integral component of the guarantee. This is a framing insight, not a technical flaw, but it would make the contribution more intellectually honest and reproducible.

## Suggestions

1. **Add error bars or confidence intervals** to Table 1 and Figure 3. Run each experiment at least 5 times with different seeds and report standard deviations.
2. **Rephrase the "guarantee" claim** (line 88) to describe the system's approach more precisely: e.g., "the first agentic workflow framework to enforce static graph-level correctness through combined type-safe operators and a compiler-level checker."
3. **Validate the LLM-as-Judge** by comparing its rankings against actual execution scores on a held-out sample, and include this analysis in the main paper.
4. **Present the >90% success rate** and the token efficiency comparison as dedicated figures or tables with error estimates.
5. **Reproduce the MaAS baseline on MBPP** or acknowledge the discrepancy more clearly.

## Score and Decision

### Round 1 — Bracketing

Three queries on "agentic workflow generation evolutionary search declarative graph representation":

- **Low band (<3.5):** Scores 2.50–3.00. Papers with fundamental flaws or withdrawn. Examples: "Simultaneous Generation and Improvement" (3.0), "Unifying All Species" (2.5). MermaidFlow is clearly stronger than these — it has a well-motivated contribution and positive empirical results.

- **Middle band (3.5–7.5):** Scores 4.80–7.00. Most relevant papers here. "Flow: Modularized Agentic Workflow Automation" (6.25, Poster) uses AOV graphs for workflow automation — similar topic, accepted. "Benchmarking Agentic Workflow Generation" (6.40, Poster). "Self-Evolving Multi-Agent Collaboration Networks (EvoMAC)" (7.00, Poster). "Large-Scale Dynamic Graph Generation" (4.80, Withdrawn). "Decision Tree Induction via LLMs (LLEGO)" (6.25, Poster).

- **High band (>7.5):** Scores 7.75–8.00. Oral/spotlight papers. "LLM-SR" (8.0, Oral). "Sample-Efficient Quality-Diversity" (8.0, Spotlight). MermaidFlow is not at this level — its evaluation lacks the rigor expected of top-tier papers.

**Initial bracket:** 5.5–7.0

### Round 2 — Narrowing

Two queries within (4.5, 6.5) and (6.0, 7.5):

- **Agent Workflow Memory** (avg 4.80, Reject): Rejected for novelty concerns, data leakage, missing comparisons. MermaidFlow has a clearer contribution and stronger evaluation. **MermaidFlow is clearly stronger.**

- **Flow: Modularized Agentic Workflow Automation** (avg 6.25, Poster): Uses AOV graphs for dynamic workflow adjustment. Evaluated on custom tasks (game dev, slide creation, website building) rather than standard reasoning benchmarks. Weaknesses include missing statistical detail and limited task diversity. **MermaidFlow has stronger evaluation (4 standard benchmarks) and a more clearly novel representation (Mermaid + typed EP operators). MermaidFlow is slightly stronger.**

- **Decision Tree Induction (LLEGO)** (avg 6.25, Poster): Also LLM + evolution. Solid but with concerns about LLM necessity and missing ablation. **MermaidFlow has stronger empirical results across more benchmarks. Comparable quality.**

- **EvoMAC** (avg 7.00, Poster): Self-evolving multi-agent networks with both a method and a benchmark contribution. Thorough experiments. **MermaidFlow is slightly weaker due to missing statistical rigor that EvoMAC provides.**

- **DyVal** (avg 6.50, Spotlight): Dynamic evaluation benchmark, different contribution type but similar quality tier. **Comparable quality.**

### Final Score Determination

MermaidFlow is clearly above the reject threshold (4.80) and the weak-poster range. It is comparable to or slightly stronger than Flow (6.25) and LLEGO (6.25), and slightly weaker than EvoMAC (7.00) due to the missing statistical rigor. The paper has a genuine and well-executed contribution with clear empirical support, held back primarily by (1) the overclaimed guarantee language and (2) the absence of any variance reporting. On balance, this places the paper in the solid poster range.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>