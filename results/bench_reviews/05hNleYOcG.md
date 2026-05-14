Now I have everything I need. Let me construct the final review.

## Summary

PLAGUE proposes a three-phase plug-and-play framework (Planner, Primer, Finisher) for automated multi-turn LLM jailbreaking, inspired by lifelong-learning agents. The framework decomposes the attack lifecycle into plan generation, context-building via progressive priming, and final exploitation, with a memory bank that stores successful strategies for retrieval across attack goals. Evaluated on HarmBench against five frontier models (o3, o1, DeepSeek-R1, Claude Opus 4.1, Llama 3.3-70B), PLAGUE achieves strong results, including 81.4% SRE on o3 and 97.8% on DeepSeek-R1, outperforming existing multi-turn attacks.

## Strengths

- **Well-structured framework with clear design motivation.** The three-phase decomposition (Planner → Primer → Finisher) is a principled disentanglement of plan generation, context building, and final exploitation. Unlike prior attacks that entangle these functions (e.g., ActorBreaker focuses on planning, GOAT on iterative query refinement), PLAGUE's modular separation provides a clean design space for studying what makes multi-turn attacks succeed.

- **Comprehensive ablation establishing causal contribution of each component.** Table 3 shows a controlled additive ablation starting from a GOAT baseline on o3: adding backtracking (+0.025 SRE), reflection (+0.149), planner (+0.012), and strategy retrieval (+0.041). This quantifies each component's marginal contribution and supports the claim that the framework architecture is deliberate, not ad hoc.

- **Plug-and-play modularity validated with component swaps.** The paper demonstrates that replacing the Finisher with Crescendo boosts ASR on Claude Opus 4.1 from 0.465 to 0.673 (Table 4), and integrating ActorBreaker's planner improves diversity by 15.47% with negligible ASR degradation (Figure 3). These results directly support the claim that PLAGUE functions as a flexible framework rather than a fixed attack.

- **Efficient query budget despite added Planner phase.** Table 5 shows PLAGUE uses comparable or fewer target LLM calls than Crescendo (e.g., 3.85 vs. 3.14 on o3) while achieving substantially higher ASR, and far fewer calls than ActorBreaker (3.85 vs. 5.57 on o3). The Planner phase adds only a single attacker LLM call per objective.

- **Evaluation across a diverse and challenging set of models.** Testing on five leading models (including reasoning models o3, o1, DeepSeek-R1) with both SRE and binary-ASR metrics on the full 200-sample HarmBench set, averaged over three runs, provides a thorough empirical basis.

## Weaknesses

### Fatal
None.

### Major

- **Baseline modifications raise questions about fair comparison.** The paper claims an "apples-to-apples comparison" (line 465) but modifies every baseline in ways that affect comparability. GOAT is given the Rubric Scorer (which PLAGUE uses), ActorBreaker is limited to K=2 actors (whereas the original uses more), and Crescendo has its backtracking mechanism removed. While these changes are transparently described and have reasonable justifications (matching the 6-turn budget, aligning with ASR@K evaluation), the "apples-to-apples" framing overstates the degree of control. The key concern is asymmetry: PLAGUE uses backtracking while Crescendo's backtracking is disabled; ActorBreaker's full multi-actor design is truncated. The headline gains (32.14% on o3, 40.2% on Opus 4.1) compare PLAGUE against baselines whose standard configurations were altered. The paper would be strengthened by also reporting baseline performance in their original configurations side-by-side, so readers can see the impact of the modifications directly.

### Minor

- **Conflating SRE with ASR could mislead readers.** The paper states "We use SRE and ASR interchangeably in our work" (line 456) and reports percentages like "81.4%" in the body and Table 2. Since StrongREJECT is a continuous score in [0,1], 81.4% SRE does not mean 81.4% of attacks succeeded — it means the average harmfulness score is 0.814. The paper does report Bin-ASR (66.2% for o3) alongside SRE in all tables, which mitigates this concern. However, the text emphasizes SRE as the primary metric, and the abstract/conclusion use the "30% improvement" framing without clarifying which metric is referenced. A simple clarification (e.g., "SRE@2 (mean StrongREJECT score)") would resolve this.

- **Lifelong learning contribution is modest.** The retrieval of successful strategies (RSS) improves SRE from 0.773 to 0.814 on o3 (~5% relative) and from 0.431 to 0.465 on Claude (~8% relative). While this is a positive contribution, the gains are small compared to other components like reflection (+0.149 on o3). The lifelong-learning framing (title, motivation) overstates the role of this component relative to its empirical impact. The strategy memory is initialized with only two Crescendo examples, and the retrieval threshold (0.6 cosine similarity, max 2 examples) lacks justification or sensitivity analysis.

- **Hyperparameter thresholds lack sensitivity analysis.** The Primer scoring bar (7/10), Finisher backtracking threshold (3/10), and success criterion (8/10) are presented without any analysis of how results vary with these choices. Similarly, the asymmetry in backtracking (removing turns from the target's history but keeping them in the attacker's) is stated but not explained. These choices affect the attack behavior and should be justified or ablated.

### Trivial

- Figure 2's caption states "PLAGUE scales linearly," but the plot shows saturation after 6 turns. The full caption ("scales linearly...until it plateaus") is accurate, but the standalone phrase is imprecise.

- The diversity experiment (Appendix C.2) uses a configuration (ActorBreaker planner with PLAGUE) that differs from the main results configuration, making the diversity/ASR connection across settings unclear.

## Nice-to-Haves

- Reporting confidence intervals or variance measures (over the three runs) would help assess the stability of the results given the stochasticity of multi-turn attacks.
- A sensitivity analysis on the Rubric Scorer thresholds and the strategy retrieval similarity threshold would strengthen the methodological grounding.
- Testing on additional recent models (e.g., GPT-4.1, Gemini 2.5 Pro) and evaluating cross-model transfer of the lifelong learning memory would demonstrate broader generalizability.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Unfair baseline configurations invalidate the claimed improvements (Structural)"**: The harsh critic frames this as a fatal flaw. The paper is transparent about all modifications and provides reasonable justifications for each (budget control, metric consistency). GOAT's modifications (adding Rubric Scorer, disabling history) could actually *help* GOAT, not hurt it. The critic's claim that this "undermines the paper's central claim" is overblown; this is a methodological concern, not a fatal error.

- **"The framework is not a fixed method but requires model-specific customization"** (about Claude using Crescendo Finisher): This misreads the paper's central claim. PLAGUE's *plug-and-play* design is explicitly presented as a strength — the ability to swap components for different models is a feature, not a weakness.

- **"Missing related works"**: No external verification is possible.

- **"Missing appendix / proofs / references"**: The parser strips appendix content; these exist in the original submission.

- **"Table 1 categories are subjective"**: This is a minor presentation nitpick that doesn't affect the paper's technical contribution.

- **"Not showing failure cases"**: A nice-to-have, not a weakness.

- **"Missing larger dataset / more models"**: Many of these requests are scope creep for an already-comprehensive evaluation on 5 frontier models with 200 HarmBench samples.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the "apples-to-apples" claim.** Report baseline performance in their *original* configurations alongside the modified versions in a supplementary table. This would allow readers to see precisely how modifications affect each baseline and validate that PLAGUE's gains hold against unmodified baselines.

2. **Disambiguate SRE from ASR in the text.** Use "SRE" when referring to the StrongREJECT score and reserve "ASR" for the binary attack success rate. Add a sentence clarifying that SRE is a continuous harmfulness score, not a success rate.

3. **Add sensitivity analysis for key thresholds.** Report how the Primer/Finisher scoring thresholds (7/10, 3/10, 8/10) and the strategy retrieval similarity threshold (0.6) affect results, even if only on one model.

4. **Tone down the lifelong-learning framing.** The memory retrieval component is a useful incremental addition, but it is not the central driver of PLAGUE's performance. The title and abstract should more accurately reflect that the main contribution is the three-phase framework architecture, with lifelong learning as a supporting feature.

## Score and Decision

**Anchor papers used for calibration:**

| Paper | Avg Score | Path | Comparison to PLAGUE |
|-------|-----------|------|---------------------|
| GRAF (multi-turn jailbreak) | 4.40 | f9BuANYtJf.md | PLAGUE has cleaner methodology (no response fabrication), stronger results, and more thorough evaluation. PLAGUE is clearly stronger. |
| SEMA (multi-turn jailbreak) | 5.00 | 6eSNG1VNkl.md | Both accepted (SEMA as Poster). PLAGUE uses a framework approach vs. SEMA's training-based approach. Comparable thoroughness; PLAGUE has stronger results on harder frontier models. |
| Morpheus (jailbreak agent) | 5.00 | 11z2ZV85eV.md | Mixed reviews (2,6,4,8); rejected. PLAGUE's three-phase design is more principled than Morpheus's prompt-engineering-based "metacognition." PLAGUE's evaluation is more comprehensive (200 HarmBench samples vs. 50). |
| CoaxChain (multi-turn jailbreak) | 3.50 | 6yCZEruFu9.md | PLAGUE avoids the surrogate-model dependence that was CoaxChain's fatal weakness. PLAGUE's fully blackbox approach is cleaner and more practical. |
| MAPA (multi-turn VLM jailbreak) | 2.50 | h0lOaeDwF2.md | PLAGUE evaluates on harder frontier models with more thorough baselines. Clearly stronger paper. |
| Capability-Based Scaling | 5.00 | 1InFGGz1D5.md | Different contribution type (empirical study vs. framework). Both accepted (Poster). Comparable methodology quality. |

PLAGUE is a solid paper that proposes a well-motivated, modular framework for multi-turn jailbreaking backed by thorough ablation and strong empirical results. The main weakness is the baseline comparison methodology — the modifications to baselines are transparently described but the "apples-to-apples" framing overstates the degree of control. This concern is real but not fatal, and the overall contribution (the three-phase framework design, the systematic ablation, and the plug-and-play validation) is genuine and practically useful for the red-teaming community. Relative to the calibration anchors, the paper sits at the same tier as accepted papers like SEMA (5.0) and above rejected papers like GRAF (4.4) and CoaxChain (3.5).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>