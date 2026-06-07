Now let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence
- strength 3 with evidence

## Weaknesses
### Fatal
None.

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
(if any)

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

---

Now produce the final consolidated review following your instructions. Remember: many of the harsh critic's points may be nonsensical or overly picky — cross-check everything against the actual paper before including it.## Summary

ELMUR augments each transformer layer with per-layer external memory, bidirectional cross-attention (mem2tok/tok2mem), and an LRU-based update mechanism for long-horizon decision-making under partial observability. The method is evaluated via behavior cloning on T-Maze (synthetic cue recall), MIKASA-Robo (23 visual robotic manipulation tasks), and POPGym (48 puzzle/control tasks).

## Strengths

- **Extreme retention on T-Maze (Figure 3).** ELMUR achieves 100% success rate on corridors up to one million steps with L=10 context and S=3 segments, while every baseline (RATE, DT, BC-LSTM, TrXL, DMamba, **RMT**) degrades significantly. This cleanly demonstrates that the memory mechanism retains information across vastly longer horizons than the attention window. The generalization experiment (Figure 4) showing seamless transfer across training/validation lengths is a nice addition.

- **Component-level ablation (Table 3).** The ablation cleanly isolates contributions: baseline ELMUR scores 1.00±0.00, shared memory collapses to 0.45±0.03, removing LRU drops to 0.43±0.22, and removing both LRU and relative bias drops to 0.22±0.11. This provides direct evidence that the per-layer design and LRU management — not just extra parameters — drive performance.

- **Clean architectural design with good exposition.** The per-layer memory with dedicated read/write cross-attention, relative bias for temporal grounding (using the same embedding table with reversed signs for read vs. write), and LRU-based update are each well-motivated. Algorithms 1 and 2 provide sufficient pseudocode for reproduction. The relative bias scheme (clamping to finite range, sharing the table with sign-reversal) is clean and principled.

- **Broad evaluation across diverse benchmarks.** ELMUR is tested on synthetic discrete (T-Maze), continuous-action visual robotics (MIKASA-Robo, 23 tasks), and diverse puzzle/control tasks (POPGym, 48 tasks). Achieving the best aggregate scores on all three benchmarks is more comprehensive than typical memory-RL papers that focus on one or two domains.

## Weaknesses

### Major

1. **Overclaiming of the "theoretical analysis" (Section 4).** The paper lists "We provide a theoretical analysis of LRU-based memory dynamics" as one of three explicit contributions (line 33). However, Proposition 1 is a simple unrolling of a first-order recurrence (Eq. 9) — straightforward algebra that any reader would infer from the update rule definition. Proposition 2 (boundedness under convex combination of bounded inputs) is a trivial consequence of convexity: every convex combination of vectors in a ball stays in that ball. The effective horizon formula $H(\epsilon) = M \cdot L \cdot \ln(\epsilon)/\ln(1-\lambda)$ follows directly from the half-life algebra. There is no analysis of representational capacity, interference between competing memories, convergence properties, or how the memory interacts with the transformer's own representations. While the mathematics is correct, presenting this as a standalone "theoretical contribution" inflates the paper's substance. This section would be appropriate as an informal remark in the method description.

2. **The "100,000× beyond attention window" framing exploits task simplicity.** The claim derives from T-Maze: L=10 context, 1M-step corridor → 1,000,000/10 = 100,000. However, T-Maze is a one-bit memorization task — a single binary cue at the start with no task-relevant information during the corridor walk. Any memory system that can store one embedding without it being overwritten should succeed here, since the LRU policy will never select that slot for replacement (no new salient information arrives). Notably, BC-LSTM and RATE already achieve ~0.7 on the million-step corridor (Figure 3), showing that even basic recurrence handles this task tolerably. The dramatic 100,000× framing suggests qualitatively unprecedented capability, when the task is essentially a stress test for basic memory retention rather than complex memory management under interference.

### Minor

3. **POPGym results show only modest aggregate gains.** On all 48 tasks, ELMUR scores 10.4 vs. RATE at 9.5 (less than 1 point difference). On reactive tasks (15), ELMUR (9.2) is tied with DT (9.3) and RATE (9.1) within rounding. On puzzle tasks (33) — where memory should matter most — the improvement is 1.2 vs. 0.45 (0.75 points). The paper claims "first on 24 of 48 tasks," which is consistent with many small-margin wins. Without per-task breakdowns or significance tests showing *large* wins on a substantial subset, the practical significance of the aggregate improvement is unclear.

4. **Missing Block-Recurrent Transformer baseline.** The related work (line 294) discusses Block-Recurrent Transformers (Hutchins et al., 2022) as a closely related architecture that recycles hidden states across segments, yet it is not included as an experimental baseline. RMT *is* included in Figure 3 (correcting a claim in one of the input reviews), which partially addresses this gap. However, Block-Recurrent Transformer is among the most directly comparable segment-level recurrence architectures and its omission weakens the evaluation.

5. **Selective presentation of per-task results.** Only 4 of 23 MIKASA-Robo tasks appear in Table 1 (with the rest deferred to an appendix that does not appear in the extracted text). The paper makes strong claims — "best success rate on 21 out of 23 tasks" and "improving the aggregate success rate by about 70%" — but the per-task distribution that would let readers assess whether wins are concentrated on easy tasks or spread broadly is not visible in the main paper. A summary table of per-task outcomes (or at least a histogram of win margins) in the main body would substantially strengthen the evaluation.

6. **Ablation reveals λ is not critical.** Figure 6a shows that when $M \geq N$ (sufficient memory capacity), performance is insensitive to $\lambda$ across a wide range. This undercuts the claimed importance of the LRU blending factor — it matters primarily when memory is under-provisioned. The paper should acknowledge this honestly.

### Trivial

7. **Undisclosed hyperparameters.** The number of experts, top-k routing, capacity factor for the DeepSeek-MoE FFN are not specified. The value of $D_{\max}$ (maximum relative distance for the bias table) is never stated. Since the ablation shows MoE → MLP yields identical performance (1.00), these omissions are not fatal but should be documented.

## Nice-to-Haves

- A more challenging memorization task (e.g., multi-cue WMaze with interference between competing cues) would better justify the LRU design and distinguish ELMUR from simpler recurrent alternatives.
- Including Block-Recurrent Transformer as a baseline.
- Pairwise significance tests across the 48 POPGym tasks to support the "first on 24/48" claim.

## Removed Points

- **Claim that RMT is not included as a baseline (Harsh Critic #4).** Removed as factually incorrect: Figure 3 clearly plots "RMT" alongside the other baselines. The paper does include Recurrent Memory Transformer.
- **Criticism about missing appendix content.** Removed per instructions: the appendix exists in the original submission and was stripped by the parser. The paper explicitly references Appendix Table 8 for full MIKASA-Robo results.
- **Criticism that paper frames itself about RL but uses BC.** Retained as a trivial note but downgraded from "critical issue" — BC from demonstrations is a standard IL approach, and the RL framing is common in this line of work.
- **Generic demands for larger datasets, more models, confidence intervals.** Removed as noise: the evaluation already uses 3 benchmarks, multiple baselines, and 3-4 runs per condition, which is standard for this field.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"). Removed as too generic to be informative.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Re-frame Section 4.** Either remove the "theoretical analysis" as a billed contribution or replace it with genuinely informative analysis — e.g., analyzing how memory interference scales with competing cues, or providing retrieval accuracy bounds under the LRU policy. The current algebra is fine as an informal remark within the method section.

2. **Tone down the 100,000× framing.** Acknowledge that T-Maze is a one-bit memorization task and that the result demonstrates the memory *can* retain information indefinitely when no interference occurs. The framing should match the evidence.

3. **Include a per-task result table in the main paper** (or make a clear supplementary table easily navigable from the main text). The reader needs to see whether ELMUR's wins on MIKASA-Robo and POPGym are large-margin wins on important tasks or thin-margin wins across many tasks.

4. **Disclose the missing hyperparameters** (MoE configuration, $D_{\max}$).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (topically similar papers):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `N581Nje6fH` (Long Horizon Episodic Decision Making) | 1.50 | R1 | Much weaker: vague method, poor evaluation |
| `It4KL6XnPq` (Foundation Policies with Memory) | 3.00 | R1 | Weaker: smaller scope, POPGym-focused, no robotics |
| `We5z3UEnUY` (Stable Hadamard Memory for RL) | 6.50 | R1 | Comparable topic (memory + RL + POPGym). SHM was accepted; its reviewers praised theoretical guarantees but noted unclear novelty. ELMUR has a cleaner architecture and broader evaluation but weaker theory and more overclaiming |
| `FhbZ1PQCaG` (Think Before You Act: DT with Memory) | 5.75 | R1 | Weaker: narrower evaluation (Atari + Meta-World), fewer baselines, less clear architectural description |
| `Ts95eXsPBc` (Spatially-Aware Transformers) | 7.00 | R1 | Stronger: more novel integration of spatial cognition, but different focus area |
| `Oq8bDXRf4F` (Cognitive Map under Uncertainty) | 5.25 | R1 | Weaker: narrower scope, less rigorous evaluation |

**Round 2 — Narrowing (5.0–7.5 band):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `5iWim8KqBR` (Memory-Efficient Algorithm Distillation) | 5.50 | R2 | Weaker: more niche focus on in-context RL distillation |
| `9DrPvYCETp` (Shared Memory for Multi-agent Pathfinding) | 5.33 | R2 | Different setting (MARL), weaker evaluation |
| `UENQuayzr1` (Efficient Cross-Episode Meta-RL) | 5.75 | R2 | Accepted despite novelty concerns. ELMUR has stronger ablations and clearer contribution |
| `o3pJU5QCtv` (EC-Diffuser: Entity-Centric BC) | 6.25 | R2 | Different focus (object-centric manipulation), similar score tier |
| `UpQLu9bzAR` (VICtoR: Hierarchical Rewards) | 6.00 | R2 | Different focus (reward design), similar score tier |

**Round 1 bracket:** Between 5.0 and 7.0.

**Narrowing:** ELMUR is clearly stronger than the 5.75 rejected paper (Think Before You Act) — it has a better-described architecture, more baselines, broader evaluation, and cleaner ablations. It is slightly weaker than the 6.5 accepted paper (Stable Hadamard Memory) — SHM's theoretical stability guarantees were seen as a genuine contribution by its reviewers, whereas ELMUR's theoretical section is overclaimed elementary algebra. The paper's genuine contributions (architectural design, T-Maze retention, ablation study, evaluation breadth) place it in the 6.0 territory.

**Final score: 6.0** — a solid paper with a genuine architectural contribution and broad evaluation, but held back by overclaiming of the theoretical analysis and inflated headline framing. The paper could move up after revision if the presentation is better calibrated to match the evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>