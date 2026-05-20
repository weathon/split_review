Now I have enough information for calibration. Let me compile the final review.

**Calibration Summary:**
- **Round 1 bracket**: Initial bracketing placed MermaidFlow between weak anchors (2.0-3.2) and strong anchors (8.0). Narrowest plausible range: 4.0–6.0.
- **Round 2 narrowing**: Compared against 7 anchors in the 4.0–5.5 range:
  - EvoMAS (4.50, Reject): Similar evolutionary MAS topic but unclear writing. MermaidFlow is better formalized → higher.
  - JudgeFlow (4.00, Reject): Similar domain, incremental novelty. MermaidFlow has stronger novelty → higher.
  - AutoRAS (4.00, Reject): Complex, hand-crafted primitives. MermaidFlow is cleaner → higher.
  - Agent-REINFORCE (5.50, Reject): Strong results but missing baselines. MermaidFlow comparable.
  - Agentic Predictor (5.50, Accept Poster): Thorough experiments but moderate novelty. MermaidFlow has stronger formalism but weaker evaluation → slightly lower.
  - GTool (5.00, Accept Poster): Graph-based approach accepted despite concerns. MermaidFlow comparable.
  - Misevolve (5.50, Accept Poster): Different paper type (safety analysis).
  
**Final calibrated score: 5.0.** MermaidFlow has a genuine formal contribution (declarative Mermaid representation + EP operators with closure guarantee) and consistent empirical results, but the evaluation confound (representation + search algorithm vary simultaneously) is a significant weakness that limits the strength of empirical claims. Comparable to GTool (5.00) in overall quality: clear contribution with notable methodological concerns.

---

## Summary

This paper introduces MermaidFlow, a framework for agentic workflow optimization that represents workflows as typed, declarative Mermaid graphs rather than imperative Python code. It defines six constraint-preserving evolutionary operators (Node Substitution, Addition, Deletion, Edge Rewiring, Subgraph Mutation, Crossover) and proves (Lemma 1) that the space $\mathcal{S}$ is closed under these operators, so that every generated candidate remains in the safe, statically verifiable subspace. On four benchmarks (GSM8K, MATH, HumanEval, MBPP), MermaidFlow achieves the highest average score (80.75%), outperforming the best baseline (MaAS, 79.35%) by 1.4%.

## Strengths

1. **Novel declarative graph representation for workflows (Section 3.1–3.2).** The paper formalizes agentic workflows as $G(\mathcal{V}_{[\tau,\alpha]}, \mathcal{E}_{[\rho]})$ using Mermaid, a typed, compiler-verifiable graph language. This cleanly separates planning from execution — unlike code-based approaches where structure and logic are entangled. The formalism defines a constrained search space $\mathcal{S}$ where all elements are valid and executable by construction, which is both novel and practically motivated.

2. **Well-defined correctness-preserving evolutionary operators with formal closure guarantee (Section 4.1).** Six atomic operators are each defined with explicit type-consistency conditions. Lemma 1 proves $\forall G \in \mathcal{S}, \forall \mathcal{O} \in \mathbb{O}, \mathcal{O}(G) \in \mathcal{S}$ — the search space is closed under valid operator application. This theoretical grounding distinguishes MermaidFlow from prior heuristic search methods that lack structural guarantees.

3. **Consistent improvement across all four benchmarks (Table 1).** MermaidFlow achieves the best result on every task (GSM8K: 92.39%, MATH: 55.42%, HumanEval: 92.87%, MBPP: 82.31%), outperforming both hand-crafted and automated multi-agent baselines. The average margin over the runner-up (MaAS at 79.35%) is 1.40%.

4. **Ablation studies provide supporting evidence (Section 5.3).** The learning curves show faster convergence on MATH relative to AFlow. Table 2 demonstrates that stronger optimization LLMs yield better workflows, confirming the structured search space translates optimization gains into performance. MermaidFlow achieves >90% valid Python code generation vs. AFlow's ~50%, and requires ~2.7e4 tokens vs. ~6.9e4 tokens at comparable performance.

## Weaknesses

### Major

- **Confounded experimental design: representation and search algorithm vary together.** MermaidFlow uses Mermaid graphs + EP, while AFlow uses Python + MCTS and ADAS uses Python + heuristic-guided expansion. Because both the representation *and* the search algorithm differ, the observed improvement cannot be cleanly attributed to either component. The paper's core thesis is that the declarative representation enables better search, but this claim is not isolatable from the change in search algorithm. Crucially, no ablation applies the same search method to both representations (e.g., EP on Python code, or MCTS on Mermaid graphs). This is the single most significant weakness: it prevents the paper from supporting its central causality claim about representation quality. The indirect evidence (>90% vs ~50% code generation success rate) is suggestive but not a controlled isolation.

### Minor

- **"Static graph-level correctness guarantee" is overstated (Section 4.1 vs. Lemma 1).** Lemma 1 is a theoretical statement about the operators themselves: if applied correctly, the result stays in $\mathcal{S}$. However, the operators are *implemented by an LLM*, and the paper acknowledges that "the resulting Mermaid code may sometimes violate predefined safety constraints" and relies on a checker to regenerate. The claim of "guarantee[ing] static graph-level correctness across the entire generation process" (Introduction) conflates the theoretical closure property with an empirical filtering procedure. The authors should more clearly separate the theoretical guarantee from the practical LLM-faithfulness concern.

- **LLM-as-judge is used without validation (Section 4.2).** The framework uses an LLM-as-judge to select which candidate workflow to evaluate via rollout. No analysis of judge accuracy, correlation with actual execution performance, or comparison against alternatives (e.g., random selection) is provided. While this does not affect the validity of reported scores (the selected candidate is still evaluated via real validation), it means the search efficiency and candidate quality depend on an unvalidated component.

- **Performance margins are modest and lack statistical significance (Table 1).** The average improvement over the runner-up is 1.40%. On MBPP, MermaidFlow (82.31%) is essentially tied with MaAS (82.17%). On HumanEval (92.87% vs. MaAS 91.57%) and GSM8K (92.39% vs. MaAS 91.47%), the margins are ~1%. No error bars, confidence intervals, or significance tests are reported, making it impossible to assess whether these differences exceed noise.

- **Evaluation is limited to two domains (math reasoning and code generation).** While these are standard benchmarks, the paper claims MermaidFlow provides a "task-agnostic programming layer." Generalization to more diverse settings (e.g., tool use, open-ended QA, long-form generation) is not demonstrated.

### Trivial

- The figure labels and caption in Figure 4 appear to be duplicated in the text due to the rendering format. The code snippet shown in the figure caption is difficult to parse from the extracted text (likely a PDF rendering artifact rather than an author error).

## Nice-to-Haves

- An ablation that fixes the search algorithm and varies only the representation (e.g., EP on Mermaid vs. EP on parsed Python-workflow graphs) would cleanly isolate the claimed benefit.
- Reporting pass rates of LLM-generated Mermaid code through the static checker (e.g., a table showing generation validity rates across iterations) would provide concrete evidence for the reliability advantage.
- A cost-effectiveness analysis including the overhead of the checker and LLM-as-judge calls would help practitioners evaluate the practical trade-offs.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. *"The generated Python code shown contains syntax errors (e.g., mismatched parentheses)"* — The code appears in a figure (Figure 4) whose text is corrupted by PDF-to-text extraction artifacts. The original paper claims the code is executable. Without access to the original figure, this cannot be verified from the extracted text.

2. *"The paper does not acknowledge that some methods (e.g., GPTSwarm) also use graph-level abstractions"* — The paper explicitly addresses this in Section 2: "GPTSwarm (Zhuge et al., 2024) and FlowReasoner (Gao et al., 2025) organize workflows as agent interaction graphs, but lack formal semantics."

3. *Pure formatting nitpicks* about presentation structure, figure placement, etc. — These are PDF extraction artifacts, not author errors.

4. *Criticism about missing appendix content* — The parser strips appendices from all papers; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same observations: the formal contribution (Mermaid representation + EP operators) is genuine and well-presented, but the evaluation confound prevents clean attribution of the empirical gains to the representation itself. No reviewer identified a weakness or insight about the paper that goes substantially beyond what the paper's own framing provides.

## Suggestions

1. **Isolate the representation effect.** Run EP on both Mermaid graphs and a comparable graph format derived from Python workflows (or run MCTS on Mermaid graphs). This controlled experiment is the single most impactful addition the paper could make.
2. **Report statistical significance.** Add error bars, confidence intervals, or paired significance tests across multiple runs (the paper says results are averaged over 3 runs but provides no variance information).
3. **Validate the LLM-as-judge.** Report the correlation between judge scores and actual execution performance on a held-out set of candidates. Show that judge-based selection does not degrade search quality compared to alternatives.
4. **Report generation validity rates quantitatively.** Show the pass rate of LLM-produced Mermaid code through the static checker across iterations, and compare with AFlow's code generation pass rate on the same tasks.
5. **Tone down the "guarantee" language.** Clearly distinguish between the theoretical closure property of operators (Lemma 1) and the empirical filtering procedure used when LLM implementation deviates.

## Score and Decision

**Bracket determination (Round 1):** The paper sits well above the weak anchors (avg 2.0–3.2, papers with fundamental execution gaps) and well below the strong anchors (avg 8.0, papers about unrelated topics with exceptional quality). The narrowest initial bracket is 4.0–6.0.

**Narrowing (Round 2):** Compared against 7 anchors in the 4.0–5.5 range:
- EvoMAS (4.50, /home/wg25r/review_agent/human_reviews_2026/0rJUulYnow.md): Similar evolutionary MAS topic, unclear writing. MermaidFlow is better formalized → higher.
- JudgeFlow (4.00, /home/wg25r/review_agent/human_reviews_2026/HYSqpiiZlc.md): Incremental over AFlow. MermaidFlow has stronger novelty (new formal representation) → higher.
- AutoRAS (4.00, /home/wg25r/review_agent/human_reviews_2026/8Bk0AMtyKf.md): Complex framework with hand-crafted primitives. MermaidFlow's formalization is cleaner → higher.
- Agent-REINFORCE (5.50, /home/wg25r/review_agent/human_reviews_2026/9G8Rhlp1AD.md): Strong results but missing baselines. MermaidFlow comparable in quality but has a different type of confound.
- Agentic Predictor (5.50, /home/wg25r/review_agent/human_reviews_2026/7oeKDZsmWp.md): Thorough experiments but moderate novelty. MermaidFlow has stronger formal contribution but weaker evaluation → slightly lower.
- GTool (5.00, /home/wg25r/review_agent/human_reviews_2026/bn47cqGQ7l.md): Graph-based approach accepted despite some concerns about assumptions. MermaidFlow comparable in overall quality.
- Misevolve (5.50, /home/wg25r/review_agent/human_reviews_2026/Fd1jgQQW28.md): Different paper type (safety analysis of evolving agents). Not directly comparable.

**Final score: 5.0.** The paper has a genuine formal contribution and consistent empirical results, but the confounded evaluation (representation + search algorithm varied simultaneously) is a significant weakness that limits the strength of the central claim. The paper falls between clearly reject-level papers (4.0–4.5) and the more thoroughly evaluated accept-level papers (5.5+), comparable to GTool (5.00) in overall assessment.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>