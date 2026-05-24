Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper tackles the important problem of covert misinformation injection in LLM-based Multi-Agent Systems (MAS). It introduces **MISINFOTASK**, a dataset of 108 tasks with per-task misinformation goals and fallacious arguments for red-teaming MAS, and proposes **ARGUS**, a two-stage training-free defense framework combining adaptive graph-based localization of critical communication channels with goal-aware Chain-of-Thought rectification. Experiments across 4 LLMs, 3 attack vectors, and 5 topologies show that ARGUS consistently reduces misinformation toxicity (avg ~28% MT reduction) and improves task success rates over the attack-only baseline and two prior defense methods.

## Strengths

1. **MISINFOTASK fills a specific gap in MAS misinformation evaluation.** Prior datasets focus on overtly malicious/jailbreak content or use simple QA tasks. MISINFOTASK (Section 3.1) provides 108 tasks across 5 categories (Conceptual Reasoning, Factual Verification, Procedural Application, Formal Language Interpretation, Logic Analysis) with per-task misinformation goals, plausible fallacious arguments, and ground-truth refutations — enabling systematic study of covert misinformation rather than overt attacks. This is the first dataset explicitly designed for this purpose.

2. **ARGUS achieves consistent MT reduction and TSR improvement across diverse settings.** Table 1 shows ARGUS achieves the lowest MT and highest TSR in 11 of 12 LLM×attack conditions, outperforming both Self-Check and G-Safeguard. The average MT reduction relative to attack-only is 28.18% (Prompt Injection), 20.38% (RAG Poisoning), and 35.95% (Tool Injection). The corresponding TSR improvements are substantial — e.g., +21.41 pp for Tool Injection on GPT-4o-mini.

3. **Adaptive re-localization combining topology, frequency, and semantic relevance is quantitatively superior to static placement.** Table 3 ablations show that removing the information-relevance weight (γ) degrades MT from 3.73 to 4.59, and removing both topology and relevance (α & γ) degrades to 4.79. The full three-component score is necessary for optimal performance, providing clear evidence that dynamic semantic-aware monitoring improves over topology-only or frequency-only baselines.

4. **Ablation confirms each module contributes meaningfully.** Table 2 shows that removing dynamic localization, CoT revision, or multi-turn correction each produces a clear degradation in MT and TSR (e.g., w/o Dynamic Local. drops TSR from 75.93 to 68.52 on Prompt Injection). The w/ Ground Truth upper bound further validates that the full pipeline has room to improve, keeping the defense grounded.

5. **Robustness across five distinct topologies is demonstrated.** Figure 6 shows ARGUS consistently reduces MT under Chain, Full, Self-Determined, Circle, and Star structures for all three injection types, confirming that the graph-aware localization transfers across MAS connectivity patterns.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against contemporary SOTA MAS defenses.** The paper cites AgentPrune (Zhang et al., 2024b) and AgentSafe (Mao et al., 2025) in the related work but evaluates neither as baselines. AgentPrune is structurally closest to ARGUS (graph pruning defense) and would provide a directly informative comparison. Without at least one additional SOTA baseline, it is unclear whether ARGUS's gains are due to its specific design (adaptive re-localization + goal-aware correction) or simply reflect that *any* defense improves over the attack-only baseline. The comparison to G-Safeguard is informative but limited — G-Safeguard is an edge-pruning method, while ARGUS uses message rectification, making them non-comparable in mechanism.

2. **Unaddressed temporal contradiction undermines a central claim about misinformation propagation.** The paper states (Sec. 5.3) that "in the absence of any defense mechanism, the system's MT progressively escalates with an increasing number of rounds, which underscores the contagious and insidious nature of misinformation attacks." However, Figure 5 shows that under Tool Injection, MT *decreases* from ~4.5 (Round 1) to ~2.2 (Round 3) without any defense — a ~50% reduction. This directly contradicts the "progressively escalates" claim for this attack type. The paper provides no discussion or explanation for why Tool Injection behaves differently, raising questions about whether the observed ARGUS improvement for Tool Injection is partly due to natural recovery rather than the defense mechanism. The paper should either explain this phenomenon or qualify the claim.

### Minor

3. **Abstract contains an inconsistent numerical claim.** The abstract states (line 32): "reducing misinformation toxicity by approximately 38.24% across various core LLMs," while the body (Sec. 5.2, line 226) reports a per-attack breakdown averaging to 28.17%, which matches the other part of the abstract (line 16). The 38.24% figure does not correspond to any reported computation, and the abstract appears to contain two different numbers for the same claim. This should be corrected.

4. **Critical hyperparameters k and θ_sim are not specified.** The localization mechanism (Eq. 4, 9) selects the top-k edges for monitoring, but k is never given a value. The threshold θ_sim in Eq. 6 also remains unspecified. The ablation study tests α, β, γ but not k or θ_sim, creating a reproducibility gap. Specifying these values and ideally providing sensitivity analysis for k would substantially strengthen the paper.

5. **The 108-task dataset, while acceptable as a seed set, provides a narrow evaluation foundation.** With 108 tasks across 3 attacks × 4 LLMs × 5 topologies, the effective per-condition sample is small. The paper does not report confidence intervals, effect sizes, or variance across tasks. For a paper that introduces a dataset *and* uses it as the sole evaluation benchmark, providing statistical reliability evidence (e.g., bootstrap confidence intervals, per-task breakdowns) would strengthen the generalizability claims.

6. **Metric subscript notation in Table 1 is unclear.** The subscript values (e.g., "4.54 <sub>0.40</sub>") appear to denote the absolute difference from the attack-only baseline rather than standard deviations. This interpretation is not explicitly stated in the table caption or main text, making it difficult for readers to assess experimental variability. The paper should clarify this notation.

### Trivial

7. **N_norm in Eq. 2 is stated as "a normalization factor" without specification.** While the maximum possible betweenness centrality is a natural choice, the paper should state this explicitly for completeness.

## Nice-to-Haves

- **Report computational overhead.** The Limitations section acknowledges cost, but providing actual metrics (additional LLM calls per round, total token usage, wall-time increase) would help practitioners assess the defense's practicality.
- **Human evaluation on a subset of MT scores.** Since MT measures the output's alignment with the misinformation goal, validating that low MT truly reflects successful correction (rather than the system ignoring misinformation for unrelated reasons) via human annotation on a sample would increase confidence in the metric.
- **Ablation comparing against random localization.** The paper shows that the full localization scoring matters, but does not include a baseline that randomly selects k edges to monitor. This would isolate the benefit of the scoring mechanism itself.

## Removed Points

*These points were raised by reviewers but removed after verification against the paper:*

- **"Goal-aware Intent Inference accuracy is modest (~0.5–0.8) and the paper should show it's sufficient."** The paper directly demonstrates sufficiency: ARGUS works (Table 1, Figure 6) despite this accuracy level, and Table 3 shows that removing the relevance score (which depends on goal inference) degrades performance. The accuracy is adequate for the system to function.
- **"G-Safeguard comparison is uninformative because it uses edge pruning vs. ARGUS's message rectification."** This overstates the issue. Comparing different defense families (pruning vs. correction) is standard practice and informative for readers. However, the missing baselines (point 1 in Major) are a distinct concern.
- **"The average MT improvement over G-Safeguard is only ~0.4 points."** The actual average improvement is ~0.55 (computed from Table 1 avg MT columns across 4 LLMs). Moreover, ARGUS also substantially improves TSR (e.g., +12.3 pp on Gemini-2.0-flash). This criticism miscounts.
- **"Evaluation of G-Safeguard suggests it's not designed for misinformation, making comparison less meaningful."** G-Safeguard is a published MAS defense (Wang et al., 2025b); its performance in this setting is a valid empirical finding, and the comparison is meaningful even if G-Safeguard was designed for broader threats.
- **"The ablation of Multi-Turn Corr. and Dynamic Local. may be redundant."** Table 2 shows different impacts (w/o Dynamic Local.: MT 4.55; w/o Multi-Turn Corr.: MT 4.63), suggesting they capture distinct aspects of the pipeline. The labels could be clearer, but the criticism overstates the redundancy.
- **"Dataset construction should report human agreement on quality filtering."** This is a reasonable request but not a core weakness; the paper describes the criteria and manual curation process.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the temporal dynamics of misinformation propagation appear to be attack-type-dependent. Prompt Injection and RAG Poisoning show the expected "escalation" pattern (MT increasing over rounds without defense), but Tool Injection shows monotonic *decrease* — agents appear to self-correct on tool-based misinformation over time, possibly because tool outputs are more easily verified against reality than prompt-injected or RAG-poisoned knowledge. This suggests that defense mechanisms may need to be attack-type-aware rather than uniform, and that the natural recovery effect in Tool Injection should be accounted for when measuring defense efficacy. The paper misses an opportunity to study this interesting asymmetry.

## Suggestions

1. **Add AgentPrune as an additional baseline.** This is the most informative missing comparison — it is a graph-pruning defense contemporaneous with G-Safeguard, structurally closer to ARGUS's localization stage, and would clarify whether ARGUS's gains come from its localization + correction pipeline or just from any graph-aware intervention.
2. **Explain or qualify the Tool Injection temporal anomaly.** Report the full per-method temporal breakdown (make Figure 5 show all six curves with more granular data) and discuss why Tool Injection MT decreases without defense. Adjust the "progressively escalates" claim to acknowledge attack-type dependence.
3. **Specify k and θ_sim; add sensitivity analysis for k.** Report what k value was used across experiments and show how varying k (e.g., 1 to N edges) affects MT and TSR. This resolves the reproducibility gap.
4. **Correct the 38.24% figure in the introduction** to match the 28.17% reported in the abstract and the per-attack breakdown in Section 5.2.
5. **Clarify the subscript notation in Table 1** — state explicitly whether subscripts denote difference-from-baseline, standard deviation, or another quantity.

## Score and Decision

**Anchors used for calibration:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Monitoring LLM-based MAS Against Corruption Attacks (ezFhE6hufB) | 6.00 | R1 | Stronger baseline coverage, same topic area; rejected |
| When Agents "Misremember" Collectively (yIoMqDes7O) | 5.50 | R1/R2 | Larger benchmark (4,838 qs), simpler defense; accepted Poster |
| Thinking as Society (nHW64r5KFG) | 5.50 | R2 | Misinformation detection via multi-agent distillation; accepted Poster |
| A2ASecBench (LfdFnakqGJ) | 5.50 | R2 | Protocol-specific security benchmark; accepted Poster |
| This Is Your Doge (N4O70NauD9) | 5.00 | R1/R2 | Deception in MoA, limited scenarios; rejected |
| Conformity Dynamics in MAS (WZxgyxL6rw) | 4.00 | R1 | Analysis-only, no defense method; rejected |

**Round 1 bracket**: 4.0–6.0  
**Round 2 narrowing**: The paper is stronger than the Conformity Dynamics paper (4.00) and This Is Your Doge (5.00) due to more substantial contributions (dataset + defense + multi-dimensional evaluation). It is comparable to but slightly weaker than the 5.50 anchors (Mandela Effect, A2ASecBench, Thinking as Society) which either had larger-scale evaluation or more complete baselines. It falls short of the 6.00 anchor (Monitoring LLM-based MAS) which had better baseline coverage despite being rejected.  
**Final score**: **5.0**

The paper makes a genuine contribution — the first dataset targeting covert misinformation in MAS and a principled two-stage defense — but the evaluation has substantive gaps (missing SOTA baselines, unaddressed temporal contradiction, unspecified hyperparameters) that prevent it from meeting the acceptance bar for ICLR. The core ideas are sound and the weaknesses are addressable with additional experiments and more careful reporting.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>