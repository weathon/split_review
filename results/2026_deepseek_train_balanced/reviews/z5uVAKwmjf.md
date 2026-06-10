## Summary

This paper introduces AFlow, a framework that uses Monte Carlo Tree Search (MCTS) to automatically optimize agentic workflows represented as code. Workflows are defined as sequences of LLM-invoking nodes connected by code-based edges, and AFlow searches over prompts and edge configurations using MCTS with a soft mixed-probability selection mechanism, LLM-driven expansion, execution evaluation, and experience backpropagation. The paper reports a 5.7% average improvement over manually designed methods and a 19.5% improvement over the automated baseline ADAS across six benchmarks, and demonstrates cross-model transferability and cost-performance Pareto improvements.

## Strengths

- **MCTS adaptation for workflow search is well-motivated and clearly specified**: The paper reformulates workflow optimization as a search over code-represented graphs and introduces a soft mixed-probability selection mechanism (Eq. 1) that combines uniform and score-weighted distributions. Algorithm 1 provides a clear specification, and this is a structural improvement over the linear heuristic search used by prior automated methods like ADAS.

- **Consistent improvement over all six manual baselines on all six datasets**: Table 1 shows AFlow (80.3% average) outperforming every manually designed method (best manual: CoT-SC at 76.0%) using the same executor model (GPT-4o-mini) for all comparisons. This is a clean, apples-to-apples evaluation that isolates the benefit of the discovered workflow structure.

- **Demonstrated cross-model transferability of discovered workflows**: Table 2 shows that workflows discovered with one executor (GPT-4o-mini or DeepSeek-V2.5) transfer to GPT-4o (96.2% on HumanEval), Claude-3.5-sonnet (95.4%), and others — in some cases outperforming workflows optimized for those models directly. This goes beyond what prior automated workflow papers demonstrated.

- **Ablation confirms autonomous structure discovery without human-designed operators**: On GSM8K, AFlow without operators reaches 93.1%, surpassing all manual baselines, and autonomously develops ensemble-like structures (Section 5, Fig. 4). This directly supports the paper's thesis of progress toward automated workflow optimization.

- **Clean, formal problem formulation**: Section 3 provides a well-structured formal definition of the workflow optimization search space \( \mathcal{S} = \{(\mathcal{N}, E)\} \) with explicit node parameters (model, prompt, temperature, output format) and edge types, providing a reusable foundation for future research.

## Weaknesses

### Major

- **The headline "19.5% improvement over automated approaches" relies on a single, anomalously weak baseline.** This figure comes from comparing AFlow (80.3%) against ADAS (67.2%) — the *only* automated method in the main results table (Table 1). ADAS itself underperforms the simplest baseline (IO, 72.8%) on 5 of 6 datasets (MBPP: 53.4 vs. 71.8; MATH: 35.4 vs. 48.6; HumanEval: 82.4 vs. 87.0; HotpotQA: 64.5 vs. 68.1; GSM8K: 90.8 vs. 92.7). The paper discusses GPTSwarm (the most directly comparable MCTS-adjacent method), AutoFlow, and Symbol in related work (Section 2, line 54) but includes none in the evaluation. The central claim of superiority over automated workflow optimization methods is therefore unsubstantiated for the most relevant competitors. This significantly weakens one of the paper's two headline quantitative claims.

- **No uncertainty measures reported in main results.** Table 1 reports point estimates only (averages across three runs), with no standard deviations, confidence intervals, or significance tests. Some margins are small: 0.7 points on GSM8K (93.5 vs. 92.8 MultiPersona) and 1.8 points on DROP (80.6 vs. 78.8 CoT-SC). The paper states it computes mean and standard deviation during evaluation (Section 4, line 201: "We test each generated workflow 5 times on the validation set, computing mean and standard deviation") but omits these from the main table. Without variance estimates, the smallest improvements cannot be assessed as statistically meaningful.

### Minor

- **The "fully automated" framing is somewhat overstated relative to the evidence provided in main results.** Operators — predefined, human-authored node combinations (Ensemble, Review & Revise, Test, etc.) — are used in all main experiments and transfer analyses. While the ablation on GSM8K (Section 5, Fig. 4) shows that AFlow works without operators (93.1%), the distinction between search *with* and *without* human-provided operators should be more prominent in the presentation of main results. The abstract and contributions list do not communicate this nuance.

- **Cost-efficiency claim is documented in tabular form only for HumanEval.** The abstract claims smaller models outperform GPT-4o at 4.55% cost; this is supported with a table and Pareto figure for HumanEval, but no table shows whether this pattern holds across the other five datasets. The claim is qualified as "on specific tasks" in the abstract but broadened in the main text (Section 5, line 314).

- **Validation set construction via high-variance selection is not analyzed.** The paper selects "a subset of problems that exhibit high variance in scores" from five blank-template runs (Section 4, line 185). The effect of this selection on optimization quality or potential bias is not examined.

- **Freezing model M, temperature τ, and format F in the search space is declared but unexamined.** Section 3.2 (line 130) justifies this simplification for efficiency, but no ablation investigates what search quality may be lost relative to the full parameter space defined in Section 3.1.

### Trivial

None.

## Nice-to-Haves

- Ablation on more than one dataset (GSM8K) to confirm the operator-free benefit generalizes.
- Brief empirical check of whether fixing M, τ, and F (vs. searching over them) affects optimization quality.
- The "named node" concept mentioned in related work (line 56) could be formally defined or removed.

## Removed Points

- The harsh critic's claim that the paper's characterization of ADAS's limitations as "purely about efficiency limitations" is unsupported — this is a judgment about framing tone, not a factual error, and the paper backs its claim with experimental data. Removed.
- The point about "single-step modification in the case study being underspecified" — overly granular; the case study adequately describes the iterative process. Removed.
- The harsh critic's claim that AFlow's improvement over ADAS on MBPP/MATH is "57%" — this is factually correct per Table 1 and retained in context; the issue is baseline quality, not the calculation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear evaluative tension: the paper's strongest contribution — MCTS-based search over code-represented workflows with demonstrable advantages over manual methods and transferable structure discovery — is solidly supported. But its most eye-catching quantitative claim (19.5% over automated approaches) rests on a single baseline comparison against ADAS, which itself underperforms trivial IO on most datasets. Adding GPTSwarm (the most relevant MCTS-adjacent competitor, already discussed in related work) would substantially close this gap.

## Suggestions

1. **Add GPTSwarm and at least one other automated workflow optimization method (AutoFlow or Symbol) to the main comparison table.** If these cannot be run for practical reasons, state why explicitly rather than discussing them in related work without evaluation.
2. **Report standard deviations or per-trial results** for all entries in Table 1. The paper already computes these during validation (line 201).
3. **Provide a table of cost-performance comparisons across all six datasets**, not just HumanEval, to substantiate the cost-efficiency claims.
4. **Analyze the effect of the high-variance validation set selection** (e.g., compare against random selection).
5. **Tone down the "fully automated" framing** or clearly distinguish search-with-operators vs. search-without-operators in the abstract and introduction.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>