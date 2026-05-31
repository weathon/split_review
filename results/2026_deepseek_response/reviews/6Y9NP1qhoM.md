## Summary

This paper studies misinformation injection in LLM-based Multi-Agent Systems (MAS), proposing two contributions: (1) MISINFOTASK, a dataset of 108 realistic tasks with task-specific misinformation arguments and ground truths, designed specifically for MAS misinformation research; and (2) ARGUS, a training-free two-stage defense framework that adaptively localizes critical communication channels via topological and semantic scoring, then uses Chain-of-Thought reasoning from a corrective agent to rectify misinformation. Experiments across three injection types, four LLMs, and five topologies show ARGUS reduces Misinformation Toxicity (MT) by ~28% and improves Task Success Rate (TSR) by ~10% over the attack-only baseline.

## Strengths

- **MISINFOTASK fills a genuine gap in MAS security research.** Existing MAS security datasets focus on overtly malicious or jailbreak inputs. MISINFOTASK provides 108 tasks with 4-8 plausible-yet-fallacious arguments per task, covering Conceptual Reasoning, Factual Verification, Procedural Application, Formal Language Interpretation, and Logic Analysis (Section 3.1). The dataset is designed for the specific challenge of covert misinformation, which the paper correctly distinguishes from malicious content (Section 2.3).

- **ARGUS achieves consistent performance gains across diverse conditions.** Table 1 reports MT reductions and TSR improvements across four LLMs (GPT-4o-mini, GPT-4o, DeepSeek-V3, Gemini-2.0-flash) and three injection types. The method consistently outperforms Self-Check and G-Safeguard baselines, with ARGUS achieving the best (bolded) MT/TSR in nearly every model×attack cell.

- **The adaptive re-localization mechanism is well-motivated and validated.** The combination of topological importance (edge betweenness centrality), semantic relevance to inferred misinformation goals (Eq. 5-7), and communication frequency (Eq. 8) with dynamic re-deployment each round (Section 4.1) is principled. Figure 4 shows the corrective agent identifies attacker goals with reasonable accuracy (0.5-0.8), providing direct evidence that the goal-inference component works.

- **Temporal analysis demonstrates active propagation curtailment.** Figure 5 tracks MT over 5 rounds: without defense, MT rises steadily (from ~4.5 to ~5.2 for PI/RP); with ARGUS, MT decreases round by round (from ~4.5 to ~3.2 for PI+ARGUS). This shows the framework actively curtails propagation rather than masking effects.

- **Ablation studies verify component necessity.** Table 2 shows removing dynamic localization, CoT revision, or multi-turn correction each degrades performance (e.g., Prompt Injection MT increases from 3.50 to 4.55, 3.90, and 4.63 respectively). Table 3 confirms the combined scoring function is needed for optimal defense, with information relevance being the most critical factor.

- **Generality across topologies.** Figure 6 tests five distinct MAS topologies (Chain, Full, Self-Determined, Circle, Star) and shows ARGUS consistently reduces MT across all, demonstrating the method does not rely on a specific graph structure.

## Weaknesses

### Fatal
None.

### Major
- **Missing variance reporting despite multiple trials.** The paper states "three independent experimental trials" (Figure 2 caption) were conducted per data point, yet Table 1 reports only point estimates. The subscript numbers (e.g., 4.54<sub>0.40</sub>) appear to be differences from Attack-only, not measures of variance — these subscripts are never explained in the caption or text. No standard deviations, confidence intervals, or significance tests are reported anywhere. With 108 task instances and the inherent stochasticity of LLM-based evaluations, the observed improvements (~10% TSR, ~28% MT reduction) may or may not be reproducible. **This is the single most significant weakness**, as it undermines confidence in the core quantitative claims. The paper acknowledges the computational overhead of ARGUS (Section 7) but does not report run-to-run variance — a fixable issue that would substantially strengthen the evidence.

### Minor
- **Key hyperparameter values unreported.** The values of *k* (number of monitored edges), θ*_m_* (TSR threshold in Eq. 1), and θ*_sim_* (similarity threshold in Eq. 6) are not stated in the main text. These parameters are central to the adaptive localization mechanism, and their absence makes replication difficult.

- **MT metric's construct validity is unvalidated.** MT measures semantic consistency between the final output and the misinformation goal, scored by an LLM judge (GPT-4o). While TSR is a co-metric that partially addresses this concern, the paper does not validate that MT correlates with actual harm or human judgment. An output that accidentally aligns with the misinformation's language (but is otherwise correct) could score high MT. The 28.17% MT reduction claim would be strengthened by human annotation correlation or a more direct behavioral measure.

- **Dataset size per category not analyzed.** MISINFOTASK contains 108 tasks across five categories, but the paper does not report per-category task counts, difficulty distributions, or whether certain categories are harder to defend against. The construction pipeline (LLM-sampling → manual filtering) is described only briefly. While 108 tasks is a reasonable starting point for a specialized red-teaming dataset, the lack of categorical granularity limits understanding of where the dataset's strengths and weaknesses lie.

- **Baseline defenses not designed for misinformation.** Self-Check (prompted self-reflection) and G-Safeguard (GNN-based edge pruning) are reasonable representatives of prior MAS defense work, but neither targets misinformation specifically. The comparison would be strengthened by including a lightweight fact-checker baseline that queries the core LLM (or a separate trusted LLM) for verification of suspicious claims.

- **Computational cost unquantified.** Section 7 acknowledges computational overhead, but the paper does not measure or report the additional inference cost (number of extra LLM calls per round, added latency, cost per task) imposed by ARGUS. This information is needed for practitioners to assess the practical deployability of the method.

### Trivial
- "re-teaming dataset" in Section 1 (line 22) is a typo for "red teaming."
- The abstract reports two different MT reduction numbers ("approximately 28.17%" and "approximately 38.24%") — these likely refer to different aggregations but the discrepancy is confusing without explanation.
- Table 1 subscripts are never explained in the caption; the reader must guess their meaning.

## Nice-to-Haves
- A case study or error analysis showing which tasks ARGUS fails on and why.
- Per-category breakdown of results to identify which misinformation categories are hardest to defend against.
- A systematic sweep of α, β, γ weight values (rather than only extreme-value ablations of setting them to 0 or 1).

## Removed Points
These points were removed from the original reviews after verification:

- **"Edge betweenness centrality choice not justified" (Harsh Critic):** Edge betweenness is a standard and well-motivated choice for identifying structurally central edges in a graph. The paper provides a clear definition (Eq. 2). Questioning this without evidence that another measure would be superior is scope creep.
- **"ARSGUS oversells novelty relative to prior injection-defense work" (Harsh Critic):** The paper clearly distinguishes misinformation from malicious content (Section 2.3) and scopes its claims accordingly. The method's goal-aware reasoning and adaptive localization are genuinely novel relative to prior MAS defense work.
- **"The attack methods are generic and could carry either malicious or misinformation content" (Harsh Critic):** The paper explicitly defines misinformation (Section 2.3) and the attack methods inject task-specific plausible fallacies that match this definition.
- **Formatting/style complaints, missing appendix contents, missing related work citations:** Removed per hard rules (parser-stripped appendix, no external verification of missing citations).
- **Generic/sycophantic strengths from Strength Finder** (e.g., "this paper addresses an important problem") removed — only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observations about the paper that the paper itself does not articulate. The main synthesized insight is the confirmation that the paper's weakest link is experimental rigor (missing variance), not methodology — this clarifies the paper's revision path.

## Suggestions

1. **Report variance and statistical tests.** For each condition in Table 1, report standard deviations across the three independent trials (which the paper confirms exist). Add bootstrap confidence intervals on the TSR improvement. This single change would substantially strengthen the paper.

2. **Explain the subscript notation in Table 1** in the caption or text. These currently appear to be differences from Attack-only, which is useful information, but the reader should not have to guess.

3. **Report key hyperparameter values** (*k*, θ*_m_*, θ*_sim_*) in the main text, and add a brief complexity analysis (number of extra LLM calls per round, total added cost per task).

4. **Add a lightweight fact-checker baseline** that queries a trusted LLM for verification — this would strengthen the comparison by showing ARGUS outperforms even a natural, task-specific competitor.

5. **Include a per-category breakdown** of results to show how ARGUS performs across different kinds of misinformation.

## Score and Decision

**Calibration process:**

*Round 1 — Bracketing:*
- Weak anchors (<3.5, query: "misinformation detection multi-agent system defense LLM"): avg scores 2.33–3.00. Paper is clearly above these.
- Middle anchors (3.5–7.5): avg scores 4.75–6.60. Paper sits in this range.
- Strong anchors (>7.5): avg scores 8.00. Paper is clearly below these.
- **Bracket: [4.0, 7.0]**

*Round 2 — Narrowing:*
- **Bp2axGAs18** (5.20, Reject) — "On the Resilience of MAS with Malicious Agents": Similar topic (MAS security), less structured methodology. **Current paper is stronger** (clearer method, more comprehensive evaluation).
- **NAbqM2cMjD** (5.20, Reject) — "Prompt Infection: LLM-to-LLM Prompt Injection within MAS": Comparable structure (dataset + defense), but current paper's method is more novel. **Current paper is slightly stronger.**
- **EP6n8LCEK6** (5.50, Reject) — "Understanding Prejudice and Fidelity of D2C MAS": Similar structure with benchmark + analysis. **Current paper is comparable or slightly stronger.**
- **D6zn6ozJs7** (6.60, Accept) — "MMFakeBench: Multimodal Misinformation Detection Benchmark": Better-resourced evaluation with 3,300 samples and human evaluation. **Current paper is weaker** (smaller dataset, no human validation of metrics).
- **YauQYh2k1g** (6.25, Accept) — "Dissecting Adversarial Robustness of Multimodal LM Agents": More rigorous threat modeling and evaluation framework. **Current paper is weaker** (less systematic evaluation of failure modes).

The paper sits between the ~5.2–5.5 reject-level MAS security papers and the ~6.25–6.60 accept-level papers. It has genuine contributions (task-specific dataset, novel defense method) and broad evaluation across LLMs and topologies, but is held back by the absence of statistical variance reporting — the core evidential weakness that prevents the quantitative claims from being fully persuasive. The method itself is sound and the problem is well-motivated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>