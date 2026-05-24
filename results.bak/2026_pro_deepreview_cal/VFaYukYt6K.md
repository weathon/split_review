Now I have all the calibration data I need. Let me compile the final review.

**Calibration summary across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Latent Diffusion Planning | k1qVBh5fnb | 3.40 | R1 | Weaker — different topic (imitation learning + diffusion), less novel |
| PcLast | NlBuWEJCug | 4.50 | R1 | Below our paper — similar latent-planning theme but more limited evaluation, outdated |
| Potential Based Diffusion | 1uHTIjXjkk | 4.00 | R1 | Below — fundamental theoretical issues, limited evaluation |
| H-GAP | LYG6tBlEX0 | 7.33 | R1 | Above — comparable concept (autoencoder + planning) but much stronger evaluation, scaling |
| Large Trajectory Models | r125wFo0L3 | 5.00 | R2 | Below — weaker motivation, less novel, similar evaluation gaps |
| LADS | L66G39JrM4 | 7.00 | R2 | Above — thorough experiments, clear ablations, strong baselines |
| DCWM | lfRYzd8ady | 6.67 | R2 | Above — stronger experimental validation, beats SOTA, thorough ablations |

**Bracket:** Round 1 placed the paper between ~4.5 and 7.33. Round 2 narrowed this to roughly 5.0–6.5. The paper is clearly above Large Trajectory Models (5.0) but clearly below DCWM (6.67) and LADS (7.0). It sits around 5.5 — genuine novelty with real but addressable evaluation gaps.

Now let me write the full review.

---

## Summary
The paper proposes a framework for motion planning via greedy search over highly compressed, discrete, causally ordered latent tokens learned by a conditional trajectory autoencoder. The key insight is that extreme compression (N=3 tokens, D=3) combined with adaptive soft quantization, causal self-attention, and nested dropout yields a latent space that is both semantically meaningful and efficiently searchable. At test time, arbitrary user-specified objectives can be optimized through greedy best-first token search without retraining. The authors demonstrate behavior transfer across environments, competitive motion prediction, guided maneuver generation (left turns, speed reduction), and multi-agent interaction generation on the Waymo Open Motion Dataset.

## Strengths

- **Genuinely novel technical framework**: The combination of extreme token compression (N=3, D=3), adaptive soft quantization (Eqs. 1–2), causal ordering, and nested dropout produces a latent space that a simple greedy best-first search can navigate effectively. Table 1 shows greedy search actually *outperforms* the learned encoder at reconstruction, validating the design.

- **Compelling behavior transfer experiments (Section 3.1)**: Figure 5 demonstrates that token encodings carry high-level semantic information — decoding a "left turn" token sequence in a new environment produces a context-appropriate left turn. The library-of-behaviors experiment across ~250 environments is concrete and convincing evidence of semantic compression.

- **Adaptive soft quantization solves a real training problem**: Figure 2 shows adaptive noise injection clearly outperforms fixed noise, and Table 1 confirms the trained decoder tolerates hard quantization (N_levels=2) with modest accuracy loss. This is a practical contribution that avoids codebook collapse while preserving discretization benefits.

- **Efficient and practical inference**: Greedy search with N=3, D=3, N_levels=2 requires only 24 decoder calls and achieves 115 trajectory generations/sec (Section 3.4), demonstrating real-time feasibility.

- **Multi-agent extension shows interaction consistency**: Figure 6 demonstrates that optimizing only a pedestrian's goal position causes the joint decoder to automatically adjust the vehicle's trajectory, suggesting the tokenization captures interaction constraints.

## Weaknesses

### Fatal
None.

### Major

- **Planning evaluation lacks baselines and is limited to two simple objectives**: The planning experiments (Section 3.4) test only cumulative leftward heading and final speed reduction. While Table 3 shows token search succeeds at rates of 75.5% and 63.2% respectively, there is no comparison to any alternative planning method — not gradient-based latent optimization, not a classical trajectory optimizer applied to the decoder output, not even random token sampling as a search baseline. The "None (original scenario)" baseline merely confirms the original trajectories don't satisfy the objectives. Without planning baselines, it's unclear whether greedy token search provides a genuine advantage or whether similar success could be achieved by simpler means. This undermines the paper's central claim of enabling "arbitrary user-specified objectives" as a practical planning framework.

- **Prediction experiment (Section 3.3) is poorly motivated and disconnected**: The paper switches to N=1, D=3 for prediction without explanation and uses variance minimization as the search objective with minimal justification ("we consider searching for the tokens that will minimize the variance of the final sample"). There is no analysis of whether decoder-predicted variance correlates with prediction error, no comparison to simply using a fixed centered token or other heuristic token selections beyond the "random objective" row in Table 2. The experiment reads as an afterthought rather than a principled demonstration of the search framework's flexibility.

### Minor

- **No investigation of how search effectiveness scales with latent size**: All planning experiments use N=3, D=3, N_levels=2 — an extremely compact latent space where greedy search enumerates only 24 candidates and is nearly exhaustive. The paper does not explore whether greedy search remains effective with larger token counts or dimensionalities, leaving the scalability of the approach unaddressed.

- **Multi-agent experiments lack quantitative evaluation**: Section 3.5 presents qualitative interaction generation (Figure 6) and an LLM-based understanding experiment (Table 4), but provides no quantitative metrics for interaction quality — e.g., collision rates, displacement error of non-optimized agents, or joint likelihood under the data distribution.

- **Architecture diagram notation inconsistency**: Figure 4 references "N_enc" in the bottleneck description without defining this quantity in the paper text, creating minor confusion.

### Trivial
- The soft quantization section references information-theoretic capacity (Smith, 1971) without elaboration on the connection, which would aid reader understanding.

## Nice-to-Haves
- A planning baseline using gradient-based optimization in the continuous latent space (pre-quantization) would isolate the value of discrete greedy search.
- A sweep over (N, D, N_levels) to characterize how planning success scales with latent capacity.
- Analysis of planning failure modes — the paper notes success is not expected to reach 100% but doesn't examine *why* search fails in the unsuccessful cases.
- More complex planning objectives (e.g., goal-reaching with lane constraints, dynamic obstacle avoidance) to better demonstrate the claimed flexibility.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim: "No comparison is made to any alternative that could serve as a baseline for planning"** — Partially removed. The paper does compare against "None (original scenario)" and varies search depth (1, 2, 3 tokens). However, the absence of other planning methods remains a valid concern, re-categorized above as a Major weakness.
- **Harsh Critic claim: "No ablation is provided to show that the search is necessary — e.g., what is the success rate of simply picking the token with minimal variance"** — Partially addressed. For *prediction*, Table 2 includes a "random objective" comparison. For *planning*, this ablation is indeed missing but the issue is subsumed under the Major weakness about planning baselines.
- **Harsh Critic claim about Appendix A.2 containing further planning details** — REMOVED. The appendix is stripped in the review copy; we cannot speculate about its contents.
- **Harsh Critic claim about missing limitation section** — REMOVED. While a limitation section would improve the paper, its absence is a presentation preference, not a substantive weakness.
- **Strength Finder claim: "Competitive against several established baselines" for prediction** — KEPT but qualified. Table 2 shows minADE₆ of 0.679 vs. SOTA at 0.524 (DriveGPT); the paper is competitive against older baselines but significantly behind recent methods.
- **Strength Finder claim about "Efficient inference speed"** — KEPT. The 115 trajectories/sec figure is concrete and well-supported.
- **Harsh Critic criticism about Figure 4 referencing undefined "N_enc"** — KEPT as Minor. This is a real notational issue.

## Novel Insights
The most interesting finding emerging from this work is that a latent space compressed to merely 3 tokens of 3 dimensions, with binary quantization, preserves enough information for semantically meaningful behavior transfer and goal-directed search. This suggests that trajectory data — at least in structured driving environments — has far less intrinsic dimensionality than typically assumed, and that the combination of causal ordering with nested dropout produces a naturally searchable coarse-to-fine decomposition. The fact that greedy search beats the learned encoder at reconstruction (Table 1) is a striking empirical result that could inform future work on learned planners beyond this paper's specific architecture.

## Suggestions
- Add at least one competitive planning baseline — e.g., optimize the same objectives directly in trajectory space via a classical optimizer, or perform random sampling over tokens with the same budget as greedy search.
- Either strengthen the prediction experiment with clearer motivation and analysis, or move it to the appendix to keep the paper focused on planning.
- Include a brief analysis of the ~25% failure cases in the left-turn task to characterize the limits of the approach.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>