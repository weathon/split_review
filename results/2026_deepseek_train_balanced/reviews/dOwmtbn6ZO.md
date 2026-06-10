## Summary

The paper proposes AVUA, an LLM-agent-based framework for video understanding that combines query-adaptive frame sampling, self-reflective evaluation/refinement, and long-term memory. The method dynamically selects frames based on the query rather than using static/uniform sampling. Evaluated across four benchmarks (Egoschema, Ego4D NLQ, MovieChat, NextQA), the method reports improved accuracy with fewer frames accessed. A systematic ablation study confirms that each architectural component contributes meaningfully.

## Strengths

1. **Well-designed ablation study showing causal contribution of each component.** Table 1 (Egoschema) shows that removing any component — memory, evaluator, sampler, or refiner — substantially degrades accuracy. The gap from bare ReAct (42.02%) to the full method (66.98%) using the *same* LLM backbone (Claude-3-Sonnet) provides controlled evidence that the proposed components drive performance, not just a stronger base model.

2. **Direct empirical evidence that the agent adapts to textual cues in queries.** The NextQA analysis (Section "Questions including textual vs. non-textual cues," Figure 4) shows that questions with temporal cues access fewer frames on average (10.56 vs. 12.26) and concentrate frame access in the relevant temporal region. This goes beyond an efficiency claim to directly demonstrate the *adaptive* behavior that is the paper's core thesis.

3. **Consistent improvements on benchmarks with standard evaluation protocols.** On Egoschema (66.98% vs. 62.4%, ~93% fewer frames) and Ego4D NLQ (IoU=0.5: 17.1% vs. 7.47%, ~80% fewer frames), the method outperforms strong agent baselines on well-established, reproducible metrics (multiple-choice accuracy, IoU). These results are trustworthy and do not depend on any non-standard evaluation protocol.

4. **Well-motivated problem framing.** The paper correctly identifies that existing methods either use static uniform sampling or pre-build a memory from uniformly-sampled frames, neither of which adapts to the query at inference time. The proposed architecture (policy generation → planning/sampling → evaluation → refinement → memory) is coherently designed to address this limitation.

## Weaknesses

### Major

1. **MovieChat evaluation uses an unvalidated LLM-as-judge protocol.** The paper states: "we utilized Claude-3.5-sonnet as an evaluator to evaluate whether the prediction matches with the ground truth answer... counting only the instances with confidence over 80 (out of 100) as correct." No human validation, cross-metric calibration, or agreement analysis is provided for this protocol. The baselines (MovieChat, VideoChat, VideoLlaMA) were evaluated under different protocols. Since the MovieChat result (84.8% with 13.59 frames vs. MovieChat's 62.3% with 2048 frames) is the paper's most dramatic improvement — and is heavily emphasized in the framing — the lack of standardized evaluation is a significant methodological gap. An LLM evaluator may be systematically biased toward answers that share stylistic features with the method's output, and without validation one cannot distinguish real gains from evaluator bias.

2. **Cross-paper SOTA comparisons do not control for the LLM backbone.** The main results tables compare against published numbers from LLoVi, VideoAgent, and LifelongMemory — methods that use different underlying LLMs and toolkits. A portion of the reported improvement could stem from using Claude-3-Sonnet rather than the proposed adaptive sampling. The ablation study provides a controlled comparison (ReAct → full method with the same backbone), but the paper's headline "SOTA" framing does not reflect this caveat.

### Minor

3. **Efficiency reporting is incomplete.** The paper reports only frames accessed as the efficiency metric, but the method incurs multiple LLM calls per query: policy generation, iterative ReAct planning (potentially many turns), sampler suggestions, evaluator assessment, refiner diagnosis/refinement, and memory retrieval. Each call consumes tokens and latency. A baseline accessing more frames but using fewer/cheaper LLM calls (e.g., a single-pass uniform sampler) could be more efficient in wall-clock or dollar cost. Reporting total LLM calls, tokens, or latency alongside frames would make efficiency claims more meaningful.

4. **No variance or significance reporting.** No confidence intervals, standard deviations, or significance tests are provided. The improvements on NextQA (+1.4%) and Ego4D IoU=0.3 (+2.1%) are modest, and without variance estimates it is impossible to assess whether these differences are meaningful given the stochasticity of LLM-based methods.

### Trivial

5. **Inconsistent frame percentage formatting.** The Ego4D NLQ main table reports "avg 98 (0.002%)" while the ablation table reports "98 (.002)". The next column shows "23.987(.00)" with no percentage at all. These appear to mix proportion and percentage notation inconsistently.

## Nice-to-Haves

- Validate the MovieChat LLM judge against human judgments on a representative subset (~100 examples) and report agreement rates.
- Report total LLM API calls and token counts alongside frame counts.
- Add bootstrap confidence intervals on all main results.
- Ablate using a cheaper LLM (e.g., GPT-3.5) to test whether the framework's gains hold with a weaker backbone.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Uncontrolled comparisons / paper provides no experiment that holds the LLM and tools fixed"** — Factually inaccurate. The ablation study (ReAct baseline in Table 1) uses the *same* LLM (Claude-3-Sonnet) and the same tools, providing exactly this controlled experiment. The critic's claim that the 25-point ablation gap "raises suspicion" is speculation without supporting evidence. The valid sub-concern about cross-paper backbone mismatches is retained in Weakness #2 above.
- **Strength Finder: "MovieChat result is an unusually large margin of improvement"** — Conflicts with verified Weakness #1 (unvalidated evaluation protocol). A result cannot be a strength if its evaluation basis is unreliable.
- **Harsh Critic speculating that ReAct might be "poorly tuned"** — No evidence for this speculation; removed per filtering rules.
- Generic complaints about missing related works, reproducibility details, formatting nitpicks, etc. — Removed per hard rules.

## Novel Insights

The most noteworthy observation across the reviews is the unusual structure of the evidence. The ablation-controlled comparison (ReAct → full method) on Egoschema shows a 25-point jump (42.02% → 66.98%). This gap is *so* large that it simultaneously (a) provides strong causal evidence that the components matter, and (b) raises the question of whether the ReAct baseline was reasonably configured. The paper does not analyze what the bare ReAct agent's trajectories look like — does it default to sampling a single frame? Does it get stuck in loops? — which is precisely the analysis that would illuminate *why* the components help. This is a missed analytical opportunity rather than a fatal flaw, but it means the paper's evidence for *how* its method works is much thinner than its evidence for *that* it works.

## Suggestions

1. Replace the MovieChat LLM-as-judge evaluation with human evaluation on a held-out subset, or validate it thoroughly and report agreement metrics.
2. Report total LLM API calls and token counts alongside frame counts.
3. Add bootstrap confidence intervals to all main results.
4. Fix the inconsistent frame percentage notation across tables.
5. Qualify "SOTA" claims by noting that cross-paper comparisons use different backbones; present the ablation-controlled comparison as the primary evidence.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>