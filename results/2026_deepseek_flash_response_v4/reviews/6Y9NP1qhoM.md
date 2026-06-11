## Summary

This paper introduces MISINFOTASK, a 108-task red-teaming dataset for misinformation injection in LLM-based Multi-Agent Systems, and ARGUS, a training-free two-stage defense framework combining adaptive localization (topological importance + semantic relevance to inferred misinformation goals + message frequency) with goal-aware multi-round persuasive rectification. Experiments across 4 LLMs, 3 attack types, and 5 topologies show consistent improvements, with average MT reduction of ~28% and TSR improvement of ~10%.

## Strengths

1. **Training-free adaptive localization combining three complementary signals** — The framework scores each communication channel via a weighted combination of topological importance (edge betweenness centrality), semantic relevance to inferred misinformation goals, and message frequency. The ablation study (Table 3) confirms each component contributes, with the full composite outperforming any subset, supporting the design rationale.

2. **Consistent defense improvement across diverse settings** — Table 1 shows ARGUS achieves the lowest MT in 9/12 and the highest TSR in 11/12 LLM×attack configurations, tested across GPT-4o-mini, GPT-4o, DeepSeek-V3, and Gemini-2.0-flash. For example, with GPT-4o-mini under Tool Injection, MT drops from 5.78 (attack-only) to 2.67 and TSR rises from 68.75% to 89.66%—substantially exceeding Self-Check and G-Safeguard.

3. **Empirical demonstration of misinformation propagation dynamics** — The round-by-round tracking (Figure 5) shows MT rises monotonically across rounds without defense (confirming the snowballing nature of misinformation), while ARGUS steadily reduces MT round by round. This provides direct evidence that the framework curtails propagation within the information flow.

4. **Generalization across five MAS topologies** — Figure 6 tests Chain, Full, Self-Determined, Circle, and Star topologies, showing ARGUS reduces MT under all three attack types uniformly across all five structures. This topology-agnostic improvement goes beyond prior work that evaluated on fewer graph structures.

## Weaknesses

### Fatal
None.

### Major
1. **No variance or statistical significance reporting in main results** — Table 1 reports only point estimates with no standard deviations, confidence intervals, or any measure of variability. The caption of Figure 2 states "data points represent the outcomes from three independent experimental trials," confirming that replicates exist, but Table 1 collapses these into single values. This makes it impossible to assess whether observed improvements (some modest, e.g., GPT-4o-mini TSR under RAG Poisoning: 69.77% with ARGUS vs. 66.14% with Self-Check, a 3.6pp gap) are statistically reliable. This is a significant gap for an experimental ML paper.

2. **Subscript inconsistencies in Table 1** — For DeepSeek-V3 under Self-Check, the subscript values (which represent deltas from Attack-only, as confirmed by every other entry in the table) do not match the reported metric values. Specifically, for Prompt Injection: Attack-only MT=4.96, Self-Check MT=3.90 with subscript 0.06 (expected delta ≈1.06); for RAG Poisoning: Attack-only MT=4.85, Self-Check MT=4.70 with subscript 1.15 (expected delta ≈0.15). While likely transcription errors, these inconsistencies undermine confidence in data presentation and must be clarified.

3. **Only two defense baselines** — The evaluation compares against Self-Check (a simple reflection prompt) and G-Safeguard (GNN-based). Additional baselines such as AgentPrune (graph pruning), consensus-based methods, or other recently proposed defenses would provide a more convincing comparison. The paper does not specify whether G-Safeguard was retrained for the MISINFOTASK domain or used off-the-shelf, which affects the fairness of comparison.

### Minor
1. **LLM-as-judge from the same model family as core agents** — The evaluation uses GPT-4o-2024-08-06 as the judge for semantic consistency scoring, while GPT-4o and GPT-4o-mini serve as core agents. Using an evaluator from the same model family could introduce systematic bias. An independent judge (e.g., from a different model family or human evaluation on a subset) would strengthen the validity of the reported metrics.

2. **Goal inference accuracy not fully connected to downstream performance** — Figure 4 shows goal-inference accuracy ranges ~50-80% depending on attack type and category. The paper does not analyze how inference errors affect downstream localization quality or defense outcomes. However, the "w/ Ground Truth" ablation (Table 2) shows only modest additional improvement over full ARGUS, which partially mitigates this concern.

3. **Only one MAS architecture tested** — The platform (planning agent → main graph → conclusion agent) is a specific design. The paper does not explore generalization to fully decentralized, hierarchical, or swarm-based MAS architectures. The paper acknowledges this implicitly as a scope limitation.

### Trivial
- The DeepSeek-V3 Self-Check subscript inconsistencies in Table 1 (detailed under Major above) appear to be typos and should be corrected.

## Nice-to-Haves
- Human evaluation on a subset of outputs to validate the LLM-as-judge scoring
- Quantitative analysis of ARGUS's computational overhead (additional LLM calls per round vs. baselines)
- Release details for MISINFOTASK (license, format, access) — important for a dataset contribution
- Testing on additional non-frontier LLMs to strengthen generalization claims

## Removed Points

The following points from the harsh critic are removed with justification:

- **"Circular evaluation design"**: The critic claimed circularity because misinformation is defined relative to LLM knowledge and the judge is from the same family. However, the evaluation uses g_mis^k, which are **predefined dataset goals** (Section 3.2) that underwent manual filtering (Section 3.1). The LLM judge scores **semantic consistency** between the MAS output and this fixed target — not "truth" relative to the judge's own parametric knowledge. This is not circular. The same-family concern is valid but is retained as a Minor weakness above.

- **"Misinformation definition conflates factual correctness with LLM conformity"**: The paper explicitly scopes its definition in Section 2.3 ("Within the context of this paper, we specifically define misinformation as content that contradicts the factual knowledge implicitly stored in the parameters of an LLM") and acknowledges the limitation in Section 7. The paper is transparent about the scope of its operational definition; this is not a structural flaw.

- **"Dataset size (108 tasks) is too small"**: For a specialized red-teaming dataset with 4-8 structured arguments per task and manual filtering, 108 tasks is reasonable. No evidence is provided that this undermines the results.

- **"Betweenness centrality assumes shortest paths — invalid for MAS"**: Betweenness centrality is used only for initial localization (r=1) before interaction logs exist (Section 4.1.1). Adaptive re-localization in subsequent rounds (Section 4.1.2) relies on semantic relevance and frequency signals, which are topology-independent and do not assume shortest-path routing.

- **"No human evaluation"**: Human evaluation of misinformation detection is not standard practice for every NLP/methodology paper. The paper uses LLM-as-judge, which is common in recent literature. This is moved to Nice-to-Haves.

- **Various pure speculation points** (e.g., "the appendix may specify X but..."): Speculative claims about content in missing appendices are removed per the guidelines.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add variance reporting.** Report standard deviations or confidence intervals across the three experimental trials confirmed in the Figure 2 caption for all Table 1 metrics. This is the single highest-leverage improvement.
2. **Clarify and correct subscript values in Table 1.** State explicitly what subscript values represent and correct the apparent DeepSeek-V3 Self-Check inconsistencies.
3. **Add an independent evaluator.** Validate results on a subset using a different model family as the LLM judge to rule out systematic bias from same-family evaluation.
4. **Expand defense baselines.** Include at least one additional baseline (e.g., AgentPrune, consensus-based filtering) to broaden the comparison.
5. **Quantify overhead.** Report the number of additional LLM calls per round incurred by ARGUS and compare to baselines.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): "I Want to Break Free! Persuasion and Anti-Social Behavior of LLMs in Multi-Agent Settings" (3.00), "Very Large-Scale Multi-Agent Simulation with LLM-Powered Agents" (3.00) — these are substantially weaker papers with vague contributions and poor evaluation
- Middle band (3.5-7.5): "On the Resilience of Multi-Agent Systems with Malicious Agents" (5.20, Reject), "Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems" (5.20, Reject), "Dissecting Adversarial Robustness of Multimodal LM Agents" (6.25, Accept), "Baseline Defenses for Adversarial Attacks Against Aligned Language Models" (5.25, Reject)
- Strong band (>7.5): "Backtracking Improves Generation Safety" (8.00), "Curiosity-driven Red-teaming for Large Language Models" (8.00) — these are top-tier papers on different topics

**Round 2 (Narrowing within bracket):**
- "On the Resilience of Multi-Agent Systems with Malicious Agents" (5.20) — similar MAS security topic. The current paper is **stronger**: more comprehensive evaluation (4 LLMs vs 2), more sophisticated defense framework, a dedicated dataset, clearer presentation
- "Prompt Infection" (5.20) — similar MAS injection topic. The current paper is **slightly stronger**: broader LLM coverage, more sophisticated defense (ARGUS vs simple LLM tagging), better presentation
- "Agent Security Bench (ASB)" (6.25, Accept) — comprehensive agent security benchmark. The current paper is **weaker**: less comprehensive evaluation, fewer scenarios, no variance reporting, but has a novel defense framework that ASB lacks
- "Dissecting Adversarial Robustness of Multimodal LM Agents" (6.25, Accept) — agent robustness evaluation. The current paper is **weaker**: less realistic evaluation environment, no error bars, but proposes a defense (unlike this anchor's evaluation-only focus)

**Narrowing reasoning:** The paper is clearly above the 5.20 anchors (stronger method, broader evaluation, cleaner presentation) but below the 6.25 anchors (less rigorous evaluation, no variance reporting, fewer baselines). The most comparable anchor is "Prompt Infection" at 5.20, from which the current paper differentiates itself through a more sophisticated defense framework, broader LLM coverage, and a dedicated dataset.

### Final Assessment
The paper makes genuine contributions: ARGUS is a novel, well-motivated defense framework with a clear two-stage design, and MISINFOTASK fills a gap in evaluation resources for MAS misinformation. The experimental evaluation covers important dimensions (4 LLMs, 3 attacks, 5 topologies) and shows consistent improvements. However, the absence of variance reporting in the main results table and the limited baseline comparison prevent the evidence from being fully convincing at its current level of rigor. The table inconsistencies, while minor, add to the impression of incomplete polish. With added variance reporting, additional baselines, and clarification of the table values, the paper would be considerably strengthened. The core ideas are sound and likely publishable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>