- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3
Now I have all the evidence needed. Let me synthesize the final review.

## Summary

This paper demonstrates that LLMs exhibit a systematic backward planning bias (lower success rates when planning from goal to initial state across all tested domains), proposes a simple "problem flipping" technique — swapping initial and goal states so the LLM plans forward in the flipped problem — and shows that combining forward and flipped plans with self-verification (Fwd-Flip) improves success rates by 4–24% over forward-only planning across three text-based planning domains (Graph Planning, Array Transformation, Blocksworld). The method is tested with GPT-3.5-turbo, GPT-4-turbo, and GPT-4o, and the paper provides analyses linking the improvement to both asymmetry exploitation and increased candidate diversity.

## Strengths

1. **Clear empirical demonstration of backward bias.** Table 1 reports consistently lower backward planning success across all four settings (e.g., 39.5%→20.5% in Blocksworld, 82.5%→76.7% in undirected graphs), establishing a robust empirical finding.

2. **Correlation between LLM performance and BFS direction difficulty.** Figure 2 (computations_flip.pdf) shows that LLM success rate in a direction correlates with the number of BFS computations required in that direction, linking LLM behavior to classical planning complexity.

3. **Consistent improvements from flipping.** Table 2 shows Fwd-Flip achieving the highest success rate in 7 of 8 settings, with gains like 69.5%→86.5% in directed Graph Planning and 39.5%→48.5% in Blocksworld. The improvements generalize across GPT-3.5-turbo, GPT-4-turbo, and GPT-4o (Figure 7).

4. **Mechanistic analysis via diversity.** Figure 6 (diversity-success) shows that Fwd-Flip generates more unique candidate plans, providing a concrete explanation for why combining directions helps beyond simple averaging of forward and backward performance.

5. **Honest treatment of limitations.** The paper acknowledges the self-verification failure with GPT-3.5-turbo (line 240), errors from flipping directed graphs (line 241), the initial/goal asymmetry issue in Blocksworld (line 253), and the settings where reasoning-to-flip fails (directed graphs, Array Transformation, Blocksworld — Table 3).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented, and no verified weakness invalidates the main results.

### Minor

1. **Action invertibility assumption is acknowledged but under-discussed.** The paper states (line 131) that "each action can be inverted" as an assumption, but gives only a single sentence to this restriction. In real-world planning domains (e.g., irreversible actions in robotics, cooking, manufacturing), many actions do not have simple inverses. The paper would benefit from explicitly discussing how restrictive this assumption is and what classes of problems it excludes, rather than treating it as a technical detail.

2. **Explanation for backward bias is speculative and unsupported.** The paper attributes the backward bias to "the forward autoregressive nature of LLM output generation, as well as biases from the training dataset" (lines 33, 115), using speculative language ("may be attributed to," "conjecture"). No evidence or analysis is provided for either claim. This does not affect the main contribution (the flipping method works regardless of why the bias exists), but the framing somewhat overstates what is known about the cause of the bias.

3. **Self-verification reliability is a confound for weaker models.** The paper finds that GPT-3.5-turbo's self-verification fails completely in Blocksworld (line 240). While the paper acknowledges this, the mechanism by which flipping helps is not fully disentangled: does improvement come from generating different (more diverse) candidates, from better self-verification on flipped candidates, or both? The diversity analysis partially addresses this, but controlled experiments with oracle verification would clarify the mechanism and the method's generalizability to weaker models.

4. **No dedicated limitations section.** The paper scatters various limitation acknowledgments throughout the experiments (self-verification reliability, directed graph flipping errors, Blocksworld asymmetry), but has no single limitations paragraph in the conclusion. Consolidating these would help readers understand the scope and boundary conditions of the method.

### Trivial
None.

## Nice-to-Haves
- Adding a systematic failure analysis of backward planning (categorizing error types) would strengthen the claim about the nature of the bias and potentially suggest even better mitigations.
- Extending the diversity analysis (Figure 6) with quantitative diversity metrics (e.g., edit distance between candidates) would strengthen the causal claim that diversity mediates the improvement.
- The reasoning-to-flip experiment (Table 3) uses M=1, which the paper justifies, but exploring M>1 could reveal whether the LLM's direction selection benefits from multiple attempts.
- While not necessary for the paper's scope, a brief discussion of how the LLM-specific backward bias differs from the classical planning setting (where backward search is often as efficient as forward search) would contextualize the contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Table formatting concerns** (extra symbols, broken lines): These are PDF-to-text parser artifacts, not author errors.
- **Missing comparison with bidirectional search**: The harsh critic themselves noted this is "not a missing experiment" — the paper is not claiming a new search algorithm. Scope creep.
- **Missing formal significance tests**: Confidence intervals are reported and mostly non-overlapping. Statistical tests are not standard practice for this type of empirical comparison, especially given the clear gaps.
- **Request for a larger dataset / more models**: The three domains and three LLMs are already adequate coverage for the claims made.
- **Generic "evaluation lacks rigor" / "baselines may not be fair"**: These are area-of-concern sweeps without specific anchors in the paper. The baselines are clearly described and appropriate for the research question.
- **Speculative fatal flaws** (e.g., "if normalization were X, values would be impossible"): These depend on assumptions not present in the paper.

## Novel Insights
None beyond the paper's own contributions. The reviewers did not surface any observation about the paper's findings that the authors had not already made themselves. However, the convergence between the two reviewers' assessments is noteworthy: both agree the paper is solid, the core claims are supported, and the main value of additional work would be in deepening the mechanistic understanding rather than in fixing errors.

## Suggestions
1. Add a dedicated limitations paragraph to the conclusion, covering: (a) the action invertibility assumption and what problem classes it excludes, (b) the reliance on self-verification quality and implications for weaker LLMs, (c) the text-based, relatively small state-space nature of the evaluated domains.
2. Conduct a qualitative analysis of backward planning failures (do errors come from wrong action order, state confusion, or prompt confusion?) to either support or refine the claimed explanation for the backward bias.
3. Run an ablation with an oracle verifier (ground-truth instead of LLM self-verification) to separate the effect of diverse candidate generation from the effect of verification quality.
