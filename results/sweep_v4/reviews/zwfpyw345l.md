Now I have sufficient calibration. Let me produce the final review.

---

## Summary

This paper proposes a hierarchical multi-level attention model (token-level, function-level, module-level) for learning code state representations used in reinforcement learning. The authors combine transformer-based sequential attention with graph attention mechanisms and evaluate on three code-related RL tasks (code completion, program repair, algorithmic problem solving). While the high-level idea — multi-level attention respecting code structure — is conceptually sensible, the paper is fatally undermined by extremely poor writing quality, an underspecified methodology, an irreproducible experimental setup, and internal inconsistencies that render the claimed results unverifiable.

## Strengths

- **Three distinct attention mechanisms for different code granularities**: Equations (1)–(3) define separate attention computations for token-level (with relative positional encodings), function-level (AST-based with edge features), and module-level (with function metadata). This is a concrete architectural proposal that follows the paper's stated goal.

- **Ablation study isolates component contributions**: Table 2 shows that removing each attention level degrades performance (token-level: −6.2%, function-level: −3.6%, module-level: −2.4%, uniform attention: −4.5%), providing some evidence that all three levels contribute.

- **Task-dependent attention patterns reported**: Section 6.3 notes that module-level attention focuses on nearby modules for code completion (avg distance 2.1 edges) but spreads further for program repair (3.8 edges), which offers qualitative insight into model behavior.

- **End-to-end RL optimization through the hierarchy is specified**: Equation (6) and the surrounding text explain that policy gradients propagate through all attention layers, distinguishing the approach from methods that learn code embeddings independently of the RL objective.

## Weaknesses

### Fatal

1. **The paper is written in largely incoherent English with garbled sentences throughout.** Examples include: "code Sequential or Tele-centric analysis yet, usually these techniques are restricted to either sequential or structural aspects Peps by itself" (line 19); "Current methods often generate embeddings that are either without context being aware of the token of the word embeddings" (line 21); "The hierarchical cherry-picking of the code embedding system" in the Conclusion (line 352, intended to say "hierarchical"). Such pervasive language quality issues make it impossible to determine whether the technical content is sound. The paper explicitly states "We use LLM polish writing based on our original paper" (line 356), suggesting the authors attempted automated polishing but produced a result that is still not publication-ready.

2. **The RL framework and experimental tasks are not defined, making the evaluation irreproducible.** Line 169 states "Each task was implemented as a Markov Decision Process (MDP)" but never specifies the state space, action space, reward function, or transition dynamics for any of the three tasks. The action space description in line 229 — "token-level edits (insert/replace/delete) and (complexity raising functions, name changes of variables)" — is vague and inconsistent across tasks. Without formal MDP definitions, the experimental results have no clear grounding.

3. **Critical internal inconsistencies undermine trust in the results.**
   - **Training steps mismatch**: Section 5.5 specifies 90,000 RL training steps, but Figure 2's x-axis only goes to 50,000 steps.
   - **Unidentified baselines in scalability analysis**: Figure 3 and its accompanying table use "Baseline 1" and "Baseline 2" without ever identifying which methods they correspond to, invalidating the scalability claims.
   - **Unreported statistical tests**: Section 5.4 claims "statistical significance tested via paired t-tests (p < 0.01)" but no p-values, test statistics, or confidence intervals appear anywhere in the paper.

### Major

4. **No variance or confidence intervals reported for any experimental result.** Table 1 reports single-point estimates for every metric with no standard deviations, number of runs, or confidence intervals. Given that RL experiments are inherently noisy, the reported improvements (e.g., 6.6 BLEU points over CodeBERT) cannot be assessed as statistically meaningful.

5. **The core architectural integration is underspecified.** The method section describes how the three attention levels interact only as "switches back and forth between processing sequences through transformer layers, propagating info using graph attention layers, and the relative balance between these pathways is learned" (line 153). Equation (5) concatenates four representation vectors, but the dimensions are not given, and how the gradient flows from the RL objective through each attention module is not described beyond a one-sentence claim. This is insufficient for reproducibility.

6. **Key claims are stated without supporting evidence.** The paper claims (line 320) that "Memory consumption is linearly proportional to program size with our model, compared to quadratic growth for sequence transformers" but provides no runtime, memory profiling, or comparison data to support this.

### Minor

7. **The background section (Section 3) recites textbook knowledge about ASTs, GNNs, and attention without connecting it to the proposed method**, occupying space that could be used for architectural detail.

8. **The APPS dataset usage for the "algorithmic problem solving" RL task is non-standard and not explained.** APPS was designed for code generation from natural language descriptions, not for a setting where actions are code modifications in an RL loop. The paper does not describe how the environment was implemented.

### Trivial

9. Equation (1) uses $\mathbf{R}_{i-j}$ representing "learnable relative position embeddings" but does not specify the number of learned embeddings, their dimensionality, or whether they are shared across attention heads.

10. The overall structure uses lowercase "our model" inconsistently in figures/tables, and there are minor formatting issues throughout.

## Nice-to-Haves

- Release of code and environment implementations would substantially strengthen reproducibility.
- An actual code example with attention weight visualizations at each level would help readers understand what the model learns.
- Comparison against a broader set of modern code representation models (beyond the five fairly basic baselines) would better situate the contribution.

## Removed Points

These points were flagged by the reviewers but are removed here for the reasons given:

- *Criticism about the "Gomez et al., 2025" reference being suspicious/made-up* — Per policy, all cited references are assumed to exist. This criticism is removed.
- *Claim that the paper does not state whether CodeBERT was fine-tuned* — Line 177 explicitly says "fine-tuned for RL." This sub-point is factually incorrect.
- *Claims about missing appendix content, proofs, or references* — The parser strips these sections from all papers; the original submission likely contains them. Removed per policy.
- *Claim that the method's novelty cannot be evaluated because equations lack a computational graph* — While the specification is indeed insufficient, equations (1)–(8) do exist and the architecture diagram (Figure 1) conveys the flow. The criticism overstated the absence of any description.
- *Several strength finder claims that were generic or delusional* — e.g., "consistent state-of-the-art results" (the results lack variance bars, so this is an unsupported strength), "scalability analysis with linear memory growth" (the claim is stated but not evidenced).
- *Demand for cross-task evaluation* — This is a nice-to-have, not a necessary experiment for acceptance.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight that the paper itself does not claim (or fail to claim).

## Suggestions

1. **Complete rewrite for clarity.** The garbled English throughout must be resolved by the authors (not by an automated LLM polisher) so that the technical content can be evaluated.
2. **Formally define each RL task as an MDP.** Provide explicit state space, action space, reward function, and transition dynamics for code completion, program repair, and algorithmic problem solving.
3. **Report all results with variance** (at least 5 seeds).
4. **Resolve the 90,000 vs. 50,000 steps inconsistency** and identify "Baseline 1" and "Baseline 2" in Figure 3.
5. **Provide a clear computational graph** showing how the three attention levels are integrated and how gradients flow through each module.
6. **Either report the claimed t-test results or remove the statement.**

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Anchor | Avg Score | Comparison to current paper |
|---|---|---|
| `OXIIFZqiiN` (IGCP) | 1.50 | Both papers have incoherent writing and were suspected of being LLM-generated. The current paper has more structure (equations, tables) but similar language quality issues. |
| `51cjeYcXjs` (Malware Search) | 2.50 | This paper has clearer writing and a more coherent method description. The current paper is weaker on clarity. |
| `N18Z2MkMEa` (FALCON) | 3.00 | FALCON also had writing issues but presented a coherent method. The current paper's method is far less specified. |
| `DgGdQo3iIR` (GEPCode) | 4.33 | A decently-written paper with clear method and solid experiments. Much stronger than the current paper. |
| `4ytRL3HJrq` (Nova) | 5.60 | Hierarchical attention for code, well-written with rigorous experiments. Far exceeds the current paper in all dimensions. |
| `vfzRRjumpX` (CodeSage) | 5.75 | Strong code representation learning paper with thorough evaluation. Not comparable in quality. |
| `SnDmPkOJ0T` (REEF) | 8.00 | High-quality accepted paper. Illustrates the standard the current paper falls far short of. |

The paper is positioned near the bottom of the calibration distribution, comparable to papers scoring 1.5–3.0. The core idea is sensible but the execution — in writing quality, methodological specification, and experimental rigor — is fundamentally insufficient for acceptance.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>