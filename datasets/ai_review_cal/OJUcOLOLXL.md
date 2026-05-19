- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper proposes RethinkMCTS, a framework that uses MCTS to search at the *thought* (reasoning strategy) level for code generation, and introduces a "rethink" operation that leverages block-level, execution-feedback-driven verbal feedback to correct erroneous thoughts within the search tree. The method is tuning-free and evaluated on APPS and HumanEval with GPT-3.5-turbo and GPT-4o-mini, achieving consistent improvements over eight baselines including ToT, LATS, PG-TD, Reflexion, and RAP.

## Strengths

1. **Novel and well-motivated core contribution.** The rethink operation — using fine-grained block-level execution feedback to regenerate erroneous thoughts in the search tree — is clearly differentiated from prior work: Reflexion stores memories of past mistakes but does not correct the thought trace, and ToT/LATS search over reasoning or code but do not integrate execution feedback to refine thoughts. The paper explicitly scopes its claims and the contrast is accurate. (Lines 19–20, 126–129)

2. **Consistent and substantial empirical results.** Table 1 shows RethinkMCTS outperforms all eight baselines across every setting (APPS introductory/interview/competition and HumanEval) with both GPT-3.5-turbo and GPT-4o-mini. The gains are particularly large for GPT-3.5-turbo (HumanEval: 89.02% vs. next-best ToT 84.15%; APPS-interview pass@1: 38 vs. ToT 33). These are not cherry-picked metrics.

3. **Ablation studies validate the design choices.** Figure 3 (fig:ablation) quantifies the contribution of verbal feedback, block-level analysis, the rethink operation, and self-evaluation separately. The verbal feedback component has the largest impact, consistent with the paper's motivation. The block-level analysis matters more on HumanEval (fewer public tests), matching the paper's hypothesis. Table 4 (tab:wikipedia_only) further shows rethink increases the proportion of high-quality code in the entire search tree (53.29% vs. 48.30% on HumanEval).

4. **Search granularity study provides empirical justification for the thought-level design.** Figure 3 (fig:action_level) compares token-, line-, code-, and thought-level search, showing thought-level substantially outperforms the others for GPT-3.5-turbo. This directly supports the paper's claim that modeling the reasoning process matters.

5. **Dual evaluation is compared against a reasonable alternative (self-generating tests).** Table 3 (tab:lm_vs_gentests) shows direct self-evaluation achieves better or comparable pass@1 while self-generating tests boost pass rate but not pass@1, with a plausible explanation provided.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **No statistical variance or confidence intervals reported.** The method involves stochastic LLM sampling at multiple steps (thought generation, code evaluation, self-evaluation), yet all results are point estimates. For GPT-4o-mini on HumanEval, the margin over ToT/LATS is 94.51% vs. 93.29% — a 1.22 percentage point difference that could fall within noise. While most comparisons are larger (especially for GPT-3.5-turbo), the lack of any variance reporting or multiple-run analysis weakens the rigor of the tightest comparisons.

2. **The "w/o Rethink" ablation condition lacks an explicit operational definition in the ablation text.** The paper defines the rethink operation clearly in Section 4 (lines 126–129) and the comparison in the "Effectiveness of Rethink" section (lines 222–225) describes the condition as MCTS "without applying rethink." However, the ablation study in Section 6 (lines 188–193) discusses "w/o VF" and "w/o blockInfo" but not what "w/o Rethink" actually entails (e.g., does the node keep its erroneous thought and continue expanding from it? Does it fall back to some default behavior?). The answer is inferable from context (standard MCTS without the rethink step), but the paper would benefit from stating it explicitly.

3. **The self-evaluation score's predictive validity is not analyzed.** The reward when all public tests pass is a weighted combination \(a \cdot v^{\text{test}} + b \cdot v^{\text{llm}}\). While the ablation shows removing self-evaluation hurts performance (Figure 3), the paper does not analyze whether \(v^{\text{llm}}\) actually correlates with private test pass rate or whether the fixed weights (0.8, 0.2) are sensible. A correlation analysis on a held-out set would strengthen the justification for the reward formulation.

4. **The ablation text omits discussion of the "w/o Self-Eval" bar.** Figure 3's caption lists self-evaluation as one of the ablated components, but the main text (lines 188–193) only discusses w/o VF and w/o blockInfo, not w/o Self-Eval. The reader has to infer the impact from the figure alone.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis on the dual evaluation weights \((a, b)\) would strengthen confidence in the reward design.
- A discussion of the computational overhead (LLM calls per rollout, block-level analysis cost) would help practitioners assess trade-offs.
- The paper could note that the search granularity study (Figure 3 right) only uses GPT-3.5-turbo, and the conclusion may not hold for weaker models — the paper already acknowledges this for token-level search but could be more explicit.

## Removed Points

- **"Prompt templates not shown / reproducibility concern"** — Removed per hard rule: missing appendix content is a parser artifact, not an author error. The templates exist in the original submission.
- **"ToT baseline should be stated as not using execution feedback"** — Removed: the paper already states this (line 143: "while it does not contain detailed feedback and the rethinking process").
- **"Claim 'first to search and refine thought process' is overreaching"** — Removed: the paper's claim is specifically about searching *and refining* via execution feedback; the critic acknowledges this is novel. The claim is appropriately scoped.
- **"Parent node error origin concern"** — Removed: the paper provides two concrete reasons for not regenerating parent nodes (lines 127–128: reward invalidation and prior refinement), which is a reasonable design decision explicitly defended.
- **"Missing limitations discussion"** — Removed: this is a generic request applicable to any paper and does not identify a specific flaw in the presented work.
- **"Search granularity generality limited"** — Moved from weakness to nice-to-have: the paper acknowledges the issue for token-level search and appropriately scopes its claims.

## Novel Insights

The reviews surface one insight worth noting: the "w/o Rethink" vs. "increased rollouts" comparison (Figure 4) is arguably the strongest evidence for the paper's central efficiency claim — that correcting erroneous thoughts is more cost-effective than exploring more paths. This framing (efficiency of correction vs. brute-force search) is more compelling than the raw score gains in Table 1, and the paper could foreground it more. The human reviews do not contribute genuinely novel observations beyond what the paper's own analysis provides.

## Suggestions

1. Add a brief sentence in the ablation study (Section 6) describing what each ablated variant does operationally — especially "w/o Rethink" (standard MCTS without the rethink step, expanding from the erroneous thought) and "w/o Self-Eval" (using only \(v^{\text{test}}\) as the reward when all public tests pass).
2. Report results from 3–5 runs with different random seeds for at least HumanEval and one APPS subset, or provide a justification for single-run reporting if the variance is negligible.
3. Include a correlation analysis (or at least a qualitative discussion) of whether the LLM self-evaluation score \(v^{\text{llm}}\) aligns with private test pass rate on a validation set.
