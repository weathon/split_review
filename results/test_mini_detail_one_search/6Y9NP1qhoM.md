## Summary

This paper addresses misinformation injection in LLM-based Multi-Agent Systems (MAS). It introduces MISINFOTASK, a dataset of 108 multi-topic tasks with seeded misinformation arguments, and proposes ARGUS, a training-free two-stage defense framework that adaptively localizes misinformation propagation channels and uses goal-aware reasoning to correct misinformation. Experiments across four LLM families, three attack types (Prompt Injection, RAG Poisoning, Tool Injection), and five topologies show that ARGUS consistently reduces Misinformation Toxicity (MT) by ~28% on average and improves Task Success Rate (TSR) by ~10% over attack-only baselines, while outperforming Self-Check and G-Safeguard defenses.

## Strengths

- **Comprehensive and consistent empirical gains across 24 conditions (Table 1):** ARGUS achieves the lowest MT and/or highest TSR in 23 of 24 evaluated cells across four LLMs (GPT-4o-mini, GPT-4o, DeepSeek-V3, Gemini-2.0-flash) and three attack types. The average MT reduction is 28.18% (PI), 20.38% (RP), and 35.95% (TI), with TSR improvements of ~10.33% — a clear and consistent signal.

- **Well-designed ablation studies (Tables 2, 3):** Removing each submodule (Dynamic Localization, CoT Revision, Multi-Turn Correction) degrades performance, confirming that each component contributes. The weight ablation (Table 3) shows that information relevance (γ) is the most important score, but the combination of all three is necessary for optimal performance — a concrete, actionable design insight.

- **Temporal analysis confirms propagation curtailment (Figure 5):** MT decreases round-by-round under ARGUS (e.g., Tool Injection MT drops from ~4.5 at round 1 to ~1.2 at round 5) while attack-only MT continues to rise. This longitudinal evidence directly supports the claim that ARGUS stops misinformation propagation, not just mitigates its final effect.

- **Topology-agnostic transferability (Figure 6):** ARGUS reduces MT across five distinct MAS topologies (Chain, Full, Self-Determined, Circle, Star) for all three injection methods, demonstrating generalization beyond a single graph structure.

- **Novel dataset fills a documented gap:** MISINFOTASK provides 108 complex, multi-topic tasks with 4–8 plausible fallacious arguments and ground truths per task, specifically designed for misinformation injection evaluation — addressing the lack of datasets tailored to this problem.

## Weaknesses

### Major

- **Unvalidated LLM judge as the sole evaluation metric.** Both MT and TSR are computed via `Score(·,·)`, a semantic consistency score produced by GPT-4o-2024-08-06 (Section 3.2, line 88; Section 5.1, line 194). The paper provides no evidence of the judge's reliability: no calibration against human judgments, no agreement analysis, and no investigation of whether the judge is itself susceptible to the misinformation it is meant to detect. The entire quantitative evaluation rests on this proxy, and its validity is asserted rather than demonstrated. This is the most significant evidential gap.

- **Small dataset with limited statistical power.** MISINFOTASK contains 108 tasks (Section 3.1, line 66), split across five categories (~20 per category). With overlapping standard deviations in several Table 1 cells (e.g., GPT-4o-mini Tool Injection MT: 2.67 ± 3.11 — SD larger than the mean), and no statistical significance testing (e.g., paired tests, bootstrapping), it is unclear whether the reported differences between ARGUS and the best baseline are reliable or noise. The paper does not report per-category results, so we cannot assess whether performance is uniform across task types.

- **No analysis of how goal inference accuracy affects downstream correction quality.** Figure 4 shows goal identification accuracy ranges from ~0.55 to ~0.80 across conditions, meaning the corrective agent may be "chasing the wrong target" in a substantial fraction of cases. The paper reports this accuracy but does not analyze whether higher goal inference accuracy correlates with lower MT in subsequent rounds, leaving a key link in the causal chain unsubstantiated.

### Minor

- **Reliance on LLM's internal knowledge creates a structural limitation.** The paper defines misinformation as "content that contradicts the factual knowledge implicitly stored in the parameters of an LLM" (Section 2.3, line 58). ARGUS's `a_cor` detects misinformation by comparing messages against its parameterized knowledge. When the LLM's training data contains the same misinformation, or when factual knowledge is absent, the correction will fail. The paper acknowledges this for dynamic information (Section 7) but does not address the broader problem: the method cannot fundamentally verify facts, only compare against the LLM's own beliefs. This is a design-inherent limitation, not a fixable oversight.

- **G-Safeguard's inconsistent behavior is not discussed.** For GPT-4o-mini under RAG Poisoning, G-Safeguard's MT (5.19) is worse than attack-only (4.95), suggesting the defense actively harms performance in some configurations. The paper reports this result but offers no analysis or explanation.

- **No concrete examples of tasks or corrections.** The paper never shows a single task instance from MISINFOTASK or a correction produced by ARGUS. This makes it difficult to assess task difficulty, the plausibility of the misinformation, or the quality of the corrective statements.

- **Ambiguity in ablation descriptions.** In Table 2, "w/o Multi-Turn Corr." causes a large degradation (MT from 3.50 to 4.63 for PI), but it is unclear what this ablation actually removes — whether `a_cor` only acts in a single round, or is entirely disabled after one interaction. The paper should clarify this.

- **Computational cost not quantified.** Section 7 acknowledges computational overhead qualitatively, but no token counts, additional LLM calls, or latency measurements are reported. Given that ARGUS requires embedding computations, semantic similarity searches, and multiple CoT reasoning calls per round, this information is needed to assess practical deployability.

### Trivial

- The approximate numerical values in the OCR-rendered tables (Figures 4–6) make precise verification difficult.
- The reference to "Appendix G" for prompts and "Appendix B.4" for strategy details is present, but these sections are not accessible in the extracted text.

## Nice-to-Haves

- **Add a baseline using external knowledge retrieval.** A simple fact-checking agent that retrieves from Wikipedia or a trusted database and issues corrections would directly test the value of ARGUS's internal-knowledge-activation approach versus relying on external sources. This would also address the circular dependency concern.
- **Validate the LLM judge against human annotators** on a subset of 50–100 tasks. If the LLM judge aligns with human judgments, this would drastically raise confidence in all reported numbers.
- **Report per-category results** (Conceptual Reasoning, Factual Verification, etc.) to identify where ARGUS excels and struggles.
- **Conduct a controlled study** linking goal-inference accuracy (Figure 4) to downstream MT reduction per round.
- **Discuss broader threat models** (e.g., gradual contamination, multiple compromised agents) as future work directions.

## Removed Points

These points were flagged in the input reviews but are removed here for the following reasons:

- **"Baselines don't include a natural competitor for misinformation"** — The paper explicitly positions itself as among the first to address misinformation specifically (Section 1, line 28: "most of these methods have not focused their defensive strategies on covert yet dangerous misinformation"). Comparing against general-purpose robustness methods (Self-Check, G-Safeguard) is the best available comparison. The suggestion of a fact-checking baseline is a valid nice-to-have but not a weakness of the current evaluation.
- **"Dataset includes seeded arguments, not naturally occurring"** — This is standard red-teaming methodology. The paper transparently describes its construction process (Section 3.1).
- **"Section 4.2 reads as prompt engineering"** — The level of description is typical for LLM-based system papers. The three-stage process (identification, resonance, reconstruction) is conceptually clear, and prompts are referenced in the appendix.
- **"The threat model is narrow"** — The paper clearly specifies its threat model (single compromised agent at round 1, Section 3.3). This is a reasonable starting point; discussing extensions is a nice-to-have.
- **"Missing related works"** — The paper has a dedicated Related Works section (Section 6) covering both attack and defense literature.
- **"No inter-annotator agreement on dataset filtering"** — While a quantitative quality metric would strengthen the dataset description, the manual filtering is described with clear criteria. The dataset is a supporting contribution, not the paper's primary claim.
- **"Bootstrap problem in adaptive localization"** — The paper handles this explicitly: initial localization (Section 4.1.1) uses only topological scores, so no goal inference is required for round 1. Adaptive re-localization (Section 4.1.2) kicks in for r > 1 using already-inferred goals from prior rounds.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any synthesized observation that the authors themselves do not already articulate.

## Suggestions

1. **Validate the evaluation pipeline.** Report human-machine agreement on MT and TSR for a subset of tasks. If the LLM judge aligns with human judgments, the quantitative results become interpretable. If not, the paper needs to demonstrate that conclusions survive different scoring methods.
2. **Add statistical significance testing.** Given the small dataset (108 tasks) and overlapping standard deviations, paired tests (e.g., Wilcoxon signed-rank across tasks) or bootstrapping would substantiate that ARGUS is reliably better than baselines.
3. **Show a concrete example.** Include one task from MISINFOTASK with its misinformation arguments, ground truth, and an actual correction produced by ARGUS. This would help readers assess the difficulty and plausibility of the scenarios.
4. **Report per-category results.** This would reveal whether ARGUS works uniformly across task types and help guide future work.
5. **Clarify the "Multi-Turn Correction" ablation.** Explain what removing this component concretely means (e.g., single-round intervention vs. no intervention at all).

## Score and Decision

**Calibration Anchors** (all from the deepreview corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| Bp2axGAs18.md (On the Resilience of MAS with Malicious Agents) | 5.20 | Similar topic, similar scope of experiments. Current paper has stronger empirical design (ablation, topology analysis, temporal analysis) but shares limitations about dataset size and metric validation. Comparable quality. |
| NAbqM2cMjD.md (Prompt Infection) | 5.20 | Similar topic about MAS vulnerabilities. Current paper focuses on defense (stronger practical contribution) with more comprehensive experiments across 4 LLMs. Comparable quality. |
| GiHLTtfbB5.md (Adversarial Attacks on Cooperative Multi-agent Bandits) | 4.40 | More theoretical, narrower scope. Current paper is broader in empirical scope and has a clearer practical contribution. Slightly stronger. |
| 46xYl55hdc.md (Single-agent Poisoning Attacks) | 7.00 | Rigorous theoretical paper with proofs. Not directly comparable (game theory vs. empirical LLM systems). Higher bar for theoretical contribution. |
| kgZFaAtzYi.md (Cracking the Collective Mind) | 3.50 | Similar topic but much weaker: limited to 2-agent, 2-round setups. Current paper is clearly stronger in scope, experimental depth, and contribution. |
| 0VZP2Dr9KX.md (Baseline Defenses for Adversarial Attacks) | 5.25 | Similar defense-focused paper with comparable evaluation concerns. Current paper has stronger multi-dimensional evaluation. Comparable quality. |
| IGzaH538fz.md (GNNCert) | 8.00 | Formal certification paper with rigorous proofs. Not directly comparable. Represents a different standard of contribution. |

The paper makes a genuine contribution to an understudied problem and provides a solid, multi-faceted evaluation. However, the unvalidated LLM judge and small dataset (108 tasks) with no significance testing are real methodological gaps that prevent the claims from being fully supported. The paper is comparable to the ~5.0–5.5 anchor papers in quality.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>