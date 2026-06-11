Here is the final consolidated review.

---

## Summary

ELMUR augments each transformer layer with a structured external memory managed by an LRU-based convex blending rule, using bidirectional cross-attention for token-memory read/write. It achieves 100% success on T-Maze corridors up to 1M steps (100,000× beyond its attention window), nearly doubles baseline performance on MIKASA-Robo visual manipulation tasks (e.g., 0.89 vs. 0.65 on RememberColor3), and obtains top scores on 24 of 48 POPGym tasks, while running faster per-step than RATE or DT.

## Strengths

1. **100% success rate on T-Maze up to 1M steps, 100,000× beyond the attention window.** Trained with only L=10 context and S=3 segments, ELMUR achieves perfect retention on corridors of length 10^6 while all baselines collapse to near-random (Figure 3, RQ1). This is the paper's strongest empirical evidence and a genuinely striking result.

2. **Dominant performance on visual robotic manipulation with ~70% aggregate improvement.** On MIKASA-Robo, ELMUR achieves the best success rate on 21 out of 23 tasks, with strong gains on TakeItBack (0.78 vs. 0.42) and RememberColor3 (0.89 vs. 0.65) over the next-best method RATE (Table 1).

3. **Systematic ablation isolating each component's contribution.** Table 3 and Figure 6 decompose ELMUR into shared memory, relative bias, LRU, and MoE→MLP variants. Removing LRU drops the score from 1.00 to 0.43, and removing both LRU and relative bias drops to 0.22. The M≥N capacity condition is clearly demonstrated.

4. **Length generalization across orders of magnitude.** Trained on sequences of 3–300 steps, ELMUR maintains 100% success on validation lengths from 9 to 9600 steps (Figure 4), demonstrating it does not overfit to a fixed context scale.

5. **Computational efficiency despite larger capacity.** ELMUR (2.1M params) runs faster per-step (6.8±0.5 ms) than both RATE (7.2±0.3 ms) and DT (10.7±0.1 ms) on T-Maze (Section 5.2 RQ4).

## Weaknesses

### Major

1. **Ablation baseline vs. main evaluation inconsistency on RememberColor3-v0.** The ablation (Table 3) reports Baseline ELMUR at 1.00±0.00 (60/60 successes) on RememberColor3-v0, while the main evaluation (Table 1) reports 0.89±0.07 (~267/300) on the same task. The paper notes the ablation uses 20 episodes vs. 100 episodes for the main evaluation, but the difference is far larger than sampling noise would explain (p < 0.001 by any standard test). Without stating whether the ablation uses a different λ, M, σ, or model variant (e.g., λ=0 as noted for some ablation subplots in Figure 6), the reader cannot determine whether the ablation "baseline" matches the configuration that produced the headline results. This undermines the interpretability of the entire ablation study.

2. **Numerical discrepancy in MIKASA-Robo task count.** The abstract and introduction claim "21 out of 23 tasks" on MIKASA-Robo, while the caption of Table 1 references "all 32 MIKASA-Robo tasks" (with only 4 shown in the main paper). The reader cannot determine whether 23 or 32 tasks were evaluated, or what explains the difference. The headline claim about robotic performance depends on this count and is not fully verifiable from the main text.

3. **Hyperparameter λ not reported for main experiments.** The blending factor λ is described as a "tunable hyperparameter," but its value is never stated for the headline results in Table 1, Figure 3, or Figure 4. The ablation (Figure 6a) shows performance depends strongly on λ. This affects reproducibility.

### Minor

1. **100,000× claim conflates segment-level recurrence with the novel external memory mechanism.** The paper attributes the 100,000× figure to the architecture, but a significant portion comes from segment-level recurrence (used by Transformer-XL and others). The ablation shows LRU is critical (no-LRU drops to 0.43 on RememberColor3), but no experiment compares ELMUR against itself with only cached hidden states (no external memory) on T-Maze. Such an ablation would cleanly isolate what cross-attention + LRU adds beyond standard recurrence.

2. **Theoretical analysis does not explain the strongest empirical result.** Proposition 1 derives exponential forgetting under repeated overwrites, giving H(ε) = M·L·ln(ε)/ln(1-λ). The paper acknowledges this is a "conservative lower bound," but the gap is enormous: the formula predicts far smaller horizons than the 1M steps observed. The anchor-refresh effect (a slot that is continuously read/written avoids LRU selection) likely dominates, but this is not formalized. The theory and the paper's most impressive result remain disconnected.

3. **MoE→MLP ablation achieves identical performance (1.00±0.00) to the full model.** The paper claims MoE "improves parameter efficiency and specialization," yet the ablation shows no performance benefit on the tested task.

4. **"Nearly doubles" claim is accurate for TakeItBack but not for all tasks.** The introduction says ELMUR "nearly doubles baseline performance on MIKASA-Robo." On TakeItBack (0.78 vs. 0.42) this holds, but on RememberColor5 (0.19 vs. 0.15) and RememberColor9 (0.23 vs. 0.17) improvements are modest. The 70% aggregate improvement is more precise.

### Trivial

None.

## Nice-to-Haves

- A T-Maze ablation comparing ELMUR against itself with memory disabled (only cached hidden states, as in Transformer-XL) would cleanly separate recurrence vs. external memory contributions.
- Reporting λ, M, and segment configuration alongside the headline results in Table 1 and Figure 3.
- Clarifying the 23 vs. 32 MIKASA-Robo task count in the main paper body.

## Removed Points

- **DT baseline unfairness** (removed as scope creep): The entire evaluation tests memory under limited context — DT's failure with short context is the expected behavior that motivates the work, not a weakness of the evaluation.
- **Relative bias vanishing gradient speculation** (removed as unsubstantiated): No evidence that large-offset entries suffer from vanishing gradients in practice.
- **Proposition 2 triviality** (removed as not a real weakness): Formal boundedness guarantees are a standard contribution in theoretical sections.
- **Missing per-task statistical testing for POPGym** (removed as exceeding norms): 100 episodes × 3 runs with SEM is standard RL evaluation practice.
- **Missing memory visualization/probing** (removed as beyond scope): A reasonable extension but not a required contribution for a methods paper.
- **Missing total training time and GPU memory** (removed as minor; efficiency data already provided).

## Novel Insights

The key observation from the reviews — which the paper itself does not fully articulate — is that the paper's strongest empirical result (1M-step retention on T-Maze) appears to rely on a positive feedback loop: a slot that is continuously read and written will have its anchor time refreshed and will not be selected as "least recently used," so it persists indefinitely. This anchor-refresh effect means the effective horizon is not governed by the exponential decay formula in Proposition 1 (which applies when a slot IS overwritten). Instead, the paper's best result depends on the architecture's ability to avoid overwriting important slots — a mechanism that is described qualitatively but not formalized. Bridging this gap between the formal theory and the dominant empirical behavior would substantially strengthen the paper.

## Suggestions

1. **Resolve the ablation discrepancy** by stating the hyperparameters (λ, M, σ, L, S) used in the ablation vs. main evaluation, or by running the ablation under the same 100-episode protocol as Table 1.
2. **Clarify the 23 vs. 32 MIKASA-Robo task count** in the main paper body.
3. **Report the default λ for all main experiments.**
4. **Run a controlled ablation on T-Maze** comparing ELMUR against a variant with only cached hidden states (no external memory) to isolate the contribution of cross-attention + LRU beyond standard recurrence.
5. **Replace "nearly doubles"** with the more precise "~70% aggregate improvement" when describing MIKASA-Robo results in the introduction.

## Calibration Anchors

**Round 1 (Bracketing):**
- N581Nje6fH (1.50, Reject) — Much weaker than ELMUR
- It4KL6XnPq (3.00, Reject) — Foundation Policies with Memory; much weaker
- 324fOKW1wO (3.33, Reject) — Much weaker
- N18Z2MkMEa (3.00, Reject) — Unrelated, much weaker
- FhbZ1PQCaG (5.75, Reject) — Think Before You Act (internal memory for DT); weaker than ELMUR
- UENQuayzr1 (5.75, Accept) — ECET meta-RL; weaker than ELMUR
- c4w7WVs1z7 (4.75, Reject) — RATE (direct baseline); ELMUR clearly stronger
- LSxE03S4fp (4.75, Reject) — Weaker
- 9pW2J49flQ (8.00, Accept) — Stronger, cleaner paper
- PdaPky8MUn (8.00, Accept) — Stronger, cleaner paper
- agPpmEgf8C (8.00, Accept) — Stronger paper
- DzGe40glxs (8.00, Accept) — Stronger paper

**Round 2 (Narrowing):**
- Ts95eXsPBc (7.00, Accept) — Spatially-Aware Transformers; stronger, cleaner reporting
- Pj06mxCXPl (6.67, Accept) — Transformers Learn TD Methods; different focus, stronger theory
- Pj3ErOxlLo (6.00, Reject) — NaviFormer; comparable quality and similar issue level
- 5iWim8KqBR (5.50, Reject) — Memory-Efficient Algorithm Distillation; weaker
- R3Tf7LDdX4 (6.00, Accept) — MCNN for Imitation Learning; cleaner paper but less impressive core result
- T1pUS4GZZq (5.75, Reject) — Large Recurrent Action Model; weaker

**Round 1 bracket:** [5.5, 7.0]  
**Round 2 narrowing:** Closest anchors are R3Tf7LDdX4 (6.00), Pj3ErOxlLo (6.00), and c4w7WVs1z7 (4.75). ELMUR has a stronger core contribution than RATE (4.75) and is comparable in quality to MCNN (6.00) and NaviFormer (6.00). Its reporting inconsistencies (ablation discrepancy, task count) are more significant than MCNN's weaknesses but its core empirical results are stronger. The paper is clearly below the 7.00+ level of SAT or DeepLTL because of these internal consistency gaps.  
**Final score:** 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>