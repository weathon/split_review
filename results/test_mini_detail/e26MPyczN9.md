Now I have a good understanding of the calibration landscape. Let me synthesize the final review.

**Round 1 bracket:** The paper sits clearly above the weak band (avg 2.5-3.0) and below the strong band (avg 8.0+). Initial bracket: (4.5, 7.5).

**Round 2 narrowing:** Comparing to anchors:
- lUWf41nR4v (4.50, Reject) — paper is clearly stronger, with more rigorous experiments
- BH8Nrt2dPf (4.25, Accept poster) — paper has much better experimental methodology
- PY56Wur7S0 (5.75, Accept poster) — comparable quality, paper under review is more rigorous
- PR6RMsxuW7 (6.25, Accept poster) — comparable, though the re-evaluation contribution is somewhat less novel than a new method
- 3K3s9qxSn7 (6.33, Accept poster) — paper under review has stronger experiments but weaker theory
- JlSyXwCEIQ (5.75, Reject) — paper under review has more comprehensive evaluation

The paper lands at approximately 6.0 — a solid contribution with well-controlled experiments that convincingly demonstrate its main re-evaluation claims, held back from being stronger by the thin proof-of-concept and informal theoretical framework.

Now writing the review.

Let me also check: the paper says Figure 7 (the wall-sparse maze) but the text before Section 5 mentions Figure 7. Let me check if Figure 7 exists in the paper...

I already searched and found: "As a proof-of-concept, we use FUNSEARCH (Romera-Paredes et al., 2024) with Qwen 3-Coder (30B) (Bai et al., 2023) to synthesize a Python program encoding a policy to solve a wall-sparse version of KAREL's Maze (Figure 7), so that wall-following strategies cannot be implemented."

The paper references Figure 7 but says "Rest of paper (reference and Appendix) is removed." at the end. So Figure 7 is likely in the appendix which was stripped. I can't verify the harsh critic's claim that "Figure 7 is referenced but not described in the body." The paper does describe the concept — "a wall-sparse version of KAREL's Maze" — just the figure itself is in the appendix. This is a limitation of the PDF extraction, not the paper. I'll note this.

Actually, the harsh critic says "The paper refers to Figure 7 (a wall-sparse maze) but never describes the environment in the text." This is partially true — the paper does say "wall-sparse version of KAREL's Maze (Figure 7), so that wall-following strategies cannot be implemented." This is a brief description but doesn't fully specify the environment. However, the harsh critic's stronger claim that "the reader cannot assess whether FUNSEARCH's BFS truly generalizes to all pathfinding problems" is valid — more details would help. I'll keep this as a minor weakness.

OK, let me now produce the final review.Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper re-evaluates influential claims that programmatic policies generalize better than neural policies in RL. Through controlled experiments on TORCS, KAREL, and PARKING, it shows that much of the reported advantage stems from experimental confounds (reward design, observation scope) rather than representational differences. The paper introduces an expressivity–discoverability framework and argues theoretically that fixed-capacity neural networks cannot represent solutions requiring instance-scaling memory (e.g., general pathfinding), providing a proof-of-concept using FUNSEARCH to synthesize BFS for a modified Karel maze.

## Strengths

- **Controlled re-evaluation across multiple benchmarks** (Torcs Table 1, Karel Table 2): The paper shows that with a cautious reward function (β=0.5), DRL generalizes to all OOD TORCS tracks (76% of seeds on G‑TRACK‑2), matching NDPS. In KAREL, augmenting the observation with the last action (a_{t-1}) allows a simple feedforward network to generalize to 100×100 grids where prior neural baselines (ConvNet, LSTM) failed. These experiments are well-controlled and directly support the paper's central thesis.

- **Experimental rigor with multiple seeds and confidence intervals** (30 seeds for TORCS β=0.5 and Karel, 15–30 for Parking, 95% CIs in Table 3). This is substantially more thorough than prior work (3 seeds in Verma et al. 2018) and provides credible evidence that results are not due to random variation.

- **Expressivity–discoverability framework** (Definitions 2 and 3): Provides a clear conceptual lens for separating whether a solution exists in a policy class from whether a search algorithm can find it. This distinction is useful for reasoning about why previous work's neural policies failed (lack of discoverability, not expressivity) and for guiding future experimental design.

- **Theoretical identification of memory-scaling as a fundamental limitation**: Section 5 clearly argues that problems whose solutions require working memory growing with input size (general pathfinding, nested subproblems) cannot be represented by fixed-capacity feedforward or recurrent networks. This argument is grounded in computational theory and correctly identifies a genuine limitation of current neural architectures.

## Weaknesses

### Fatal

None.

### Major

- **The proof-of-concept for memory-scaling is too thin to carry the weight placed on it.** The paper lists "demonstrating that programmatic representations can express solutions with instance-scaling memory that provably generalizes OOD" as a contribution, yet the evidence is three runs of FUNSEARCH (with no reported success rate, iteration budget, or variance across runs) on an environment that is never fully described in the text (Figure 7, the wall-sparse maze). The claim "Three runs of FUNSEARCH returned a correct implementation of breadth-first search, which generalizes to any pathfinding problem" conflates correctness on the evaluation instances used by the synthesizer with provable OOD generalization — without a formal proof or exhaustive test, this overstates what the experiment demonstrates. This is the paper's weakest link: the re-evaluation experiments are solid, but the positive claim about when programmatic representations *inherently* beat neural ones is not supported with commensurate evidence.

### Minor

- **The discoverability definition (Definition 3) is not operationalized.** "Within a bounded time limit" is never specified or referred to again in any experiment. "Discoverable" effectively becomes a post-hoc label for "we found a training procedure that worked." This limits the framework's usefulness as a predictive or analytical tool. The paper would benefit from either formalizing the bound or explicitly stating that discoverability is a qualitative lens rather than a formal definition.

- **TORCS generalization rates reported only for successful seeds, obscuring training reliability.** For G-TRACK-1, only 13/30 seeds learned to complete a lap; for AALBORG, only 4/15. The fractions in Table 1 (0.76, 0.69, 1.00, 1.00) are relative to these successful seeds, not all initial seeds. Reporting generalization rates out of *all* seeds (treating failed training seeds as zero generalization) would give a more complete picture of the robustness of the β=0.5 modification.

- **The drop in HARVESTER performance is left unexplained.** PPO with a_{t-1} achieves 0.59 return on small grids but only 0.04 on 100×100 — a complete collapse that the paper does not analyze. This task may itself require memory scaling (e.g., counting markers), which would actually *support* the paper's theoretical argument if discussed. Leaving it as an unexplained outlier weakens the KAREL analysis.

- **FUNSEARCH procedure is underspecified.** The paper does not report the number of iterations, the number of candidate programs evaluated, the success rate across runs, or the specific form of the wall-sparse maze. These details are needed to assess the strength of the proof-of-concept.

### Trivial

- None.

## Nice-to-Haves

- **PARKING modification**: The paper could try augmenting the DQN observation with the last action (as in KAREL) to see whether the generalization gap closes. The paper acknowledges PARKING remains challenging for both representations, and attempting such a modification would strengthen the "confounds explain the gap" narrative.

- **Memory-scaling task with neural baselines**: Training feedforward, LSTM, and transformer baselines on a true memory-scaling task (e.g., general pathfinding where wall-following fails) and showing they cannot generalize OOD would substantially strengthen the positive claim. Without this, the memory-scaling argument remains theoretical.

## Removed Points

These points are flagged to be removed — treat them with caution.

- *"The PARKING re-evaluation undermines the paper's generality"* (Harsh Critic Critical Issue 2) — **Removed.** The paper already acknowledges PARKING is challenging for both representations ("Independent of the metric considered, our results show that PARKING is a challenging domain for both types of representation") and does not claim to have closed the gap here. The abstract says "much of" not "all of" the observed gap, and the paper handles PARKING fairly by presenting both metrics.

- *"The core positive claim about memory-scaling tasks is not empirically validated because no controlled RL experiment compares neural vs programmatic"* (Harsh Critic Critical Issue 1, partial) — **Partially removed.** The criticism that a full neural-vs-programmatic comparison is missing is based on a misunderstanding: the paper's argument is about expressivity (the neural *class* cannot represent the solution), not about whether gradient search can find it. This is a theoretical claim, not an empirical one. However, the thinness of the proof-of-concept is retained as a Major weakness above.

- *"Missing related works"* — **Removed per instructions** (cannot verify existence from external sources).

- *Missing appendix content* — **Removed.** The appendix is stripped by the PDF parser; it exists in the original submission.

- *"PARKING DQN choice not justified"* — **Removed.** The paper says "Preliminary experiments showed that DQN outperformed the PPO and DDPG algorithms," which is sufficient justification.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's most useful observation is that the HARVESTER failure (dramatic OOD collapse despite the a_{t-1} modification) could be reframed as supporting the memory-scaling thesis — the paper currently presents it as a neutral data point rather than exploiting this alignment.

## Suggestions

1. **Strengthen the proof-of-concept** by reporting FUNSEARCH success rate, variance across seeds, the exact wall-sparse environment configuration, and ideally by training at least one neural baseline on the same task to demonstrate empirically that it cannot learn a generalizing solution.

2. **Operationalize discoverability** by either (a) tying it to a measurable quantity (e.g., number of reward-shaping steps, optimization landscape metrics) or (b) explicitly stating that it is a qualitative lens and removing the pretense of a formal "bounded time limit."

3. **Report TORCS generalization rates out of all initial seeds**, not just successful ones, to give a complete picture of training reliability.

4. **Analyze the HARVESTER failure** — explain why the a_{t-1} modification fails on this task and whether it constitutes an instance of the memory-scaling limitation the paper discusses.

5. **Consider reframing** the paper's contributions to downweight the proof-of-concept (demoting it to "speculative hypothesis" rather than "contribution") if these experiments cannot be substantially expanded. The re-evaluation alone is a significant contribution.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| lUWf41nR4v (programmatic RL + state machines) | 4.50 | R1 | Weaker: unresolved technical issues, fewer controlled experiments |
| BH8Nrt2dPf (horizon generalization in RL) | 4.25 | R1 | Weaker: much more limited experimental validation |
| PR6RMsxuW7 (planning + DRL) | 6.25 | R1, R2 | Comparable: similar experimental rigor, but that paper proposed a new method while this is a re-evaluation |
| PY56Wur7S0 (program synthesis with LLMs) | 5.75 | R2 | Comparable: both have clear contributions with limitations in evaluation depth |
| 3K3s9qxSn7 (representation complexity of RL) | 6.33 | R2 | Slightly stronger: more formal theoretical grounding, but less comprehensive experiments |
| JlSyXwCEIQ (CodeIt program synthesis for ARC) | 5.75 | R2 | Weaker: limited evaluation (single benchmark), this paper has broader empirical coverage |

**Round 1 bracket:** (4.5, 7.5). The paper is clearly stronger than weak-band anchors (2.5–3.0, withdrawn/rejected papers) and clearly weaker than 8.0+ papers (oral-level work with stronger theory or more comprehensive experiments).

**Round 2 narrowing:** The TORCS and KAREL re-evaluations are the paper's strongest contribution and are executed with above-average rigor (30 seeds, CIs). The conceptual framework is useful but informal. The proof-of-concept is notably weaker than the rest of the paper. Comparing to round-2 anchors, the paper sits above PY56Wur7S0 (5.75) in experimental rigor, is comparable to PR6RMsxuW7 (6.25) in overall quality but with a different contribution type (negative result vs. new method), and is below 3K3s9qxSn7 (6.33) in theoretical depth. The final score reflects a solid paper with a clear empirical contribution held back from being stronger by the thin proof-of-concept.

**Final score: 6.0** — This is a well-executed re-evaluation that convincingly demonstrates its main claim (confounds explain much of the reported programmatic advantage). The experiments are more rigorous than prior work (30 seeds, CIs). The expressivity–discoverability framework is a useful conceptual addition. However, the proof-of-concept for the positive claim (memory-scaling) is too thin to fully support the paper's scope, and the discoverability definition is not operationalized. The paper would benefit from either substantially expanding the positive evidence or narrowing the contribution framing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>