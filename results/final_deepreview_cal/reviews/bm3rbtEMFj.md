Now let me write the final consolidated review.

**Calibration Anchors Summary:**

Round 1 bracket: weak anchors at <3.5, middle anchors at 3.5-7.5, strong anchors at >7.5.
- RATE (c4w7WVs1z7): avg 4.75, Reject. Direct baseline; ELMUR is clearly stronger.
- Foundation Policies with Memory (It4KL6XnPq): avg 3.00, Reject. ELMUR is much stronger.
- Think Before You Act (FhbZ1PQCaG): avg 5.75, Reject. Similar topic; ELMUR has stronger architecture and more extensive evaluation.
- Stable Hadamard Memory (We5z3UEnUY): avg 6.50, Accept. Most comparable accepted paper; ELMUR has more diverse benchmarks but weaker theory.

Round 1 bracket: 5.0–7.0. Round 2 narrowed by comparison to SHM (6.50) and Think Before You Act (5.75). ELMUR is between these: stronger than Think Before You Act (more novel architecture, better empirical coverage) but slightly below SHM (weaker theoretical analysis, less rigorous proofs). Final score: 6.0.

---

## Summary

This paper proposes ELMUR, a transformer architecture augmented with per-layer structured external memory for long-horizon reinforcement learning under partial observability. Each layer maintains M memory slots with timestamps, interacts with tokens via bidirectional cross-attention (mem2tok read, tok2mem write) modulated by learned relative biases, and updates memory through an LRU-based policy combining full replacement for empty slots and convex blending otherwise. The method is evaluated on T-Maze (synthetic long-horizon recall up to 1M steps), POPGym (48 partial-observability tasks), and MIKASA-Robo (23 robotic manipulation tasks with visual observations).

## Strengths

1. **Genuinely impressive memory retention on T-Maze (Figure 3).** ELMUR achieves 100% success on corridors up to one million steps while all baselines decay to chance, demonstrating retention horizons ~100,000× beyond the native attention window. This is a clean, unambiguous signal that the memory mechanism works as designed.

2. **Strong performance on robotic manipulation (Table 1).** ELMUR achieves the best success rate on 21/23 MIKASA-Robo tasks with aggregate improvement of ~70% over the strongest prior baseline. On TakeItBack-v0 it reaches 0.78 vs. 0.42 for RATE, and on RememberColor3-v0 it reaches 0.89 vs. 0.65. These results show the method transfers from synthetic testing to realistic visual-manipulation domains.

3. **Thorough ablation isolating key components (Table 3, Figure 6).** The ablation cleanly demonstrates: (i) removing LRU drops success from 1.00 to 0.43, (ii) shared memory degrades to 0.45, (iii) M ≥ N is necessary for good performance, and (iv) MoE→MLP preserves accuracy (1.00). These ablations convincingly attribute performance to the memory mechanism rather than auxiliary design choices.

4. **Cross-domain leaderboard on POPGym (Table 2).** ELMUR achieves the best aggregate score (10.4 vs. 9.5 for RATE) across 48 tasks, with the largest gains on memory-intensive puzzles (1.2 vs. 0.45 for RATE) while remaining competitive on reactive tasks. This demonstrates consistent benefit across diverse POMDP settings.

5. **Computational efficiency despite memory.** ELMUR (2.1M params) runs at 6.8 ms/step, faster than RATE (7.2 ms) and DT (10.7 ms), because attention complexity depends on the bounded memory size rather than sequence length.

## Weaknesses

### Fatal
None.

### Major
1. **The theoretical analysis (Section 4) is too superficial to count as a contribution.** Proposition 1 (exponential decay under convex blending) and Proposition 2 (boundedness under convex updates) are immediate from the definitions — any reader familiar with exponential moving averages would derive them. The paper frames these as "formal guarantees on forgetting, retention horizons, and stability," which overstates their depth. The effective horizon formula assumes uniform overwriting and does not account for content-dependent tok2mem cross-attention or the LRU policy's interaction with token content. A meaningful analysis would characterize what content gets written, how the LRU and write mechanism interact, or under what conditions task-relevant information is retained vs. evicted. The strength finder's claim that these propositions provide "principled explanation for empirical retention" overstates their value; they describe exponential decay, not explain why the method works on complex tasks. **Impact:** The theoretical framing is misleading, and the paper would be better served acknowledging these as straightforward bounds and redirecting space toward empirical analysis of memory dynamics.

2. **The strongest headline results come from the simplest task, while performance on harder tasks is low in absolute terms.** The T-Maze task tests retention of a single binary cue across a corridor with no new information — a setting that plays directly to ELMUR's strengths and sidesteps the challenge of managing multiple competing memories. On the harder RememberColor5-v0 (0.19) and RememberColor9-v0 (0.23) tasks, which involve more distractors, ELMUR's absolute performance is low even though it still beats baselines. The abstract and introduction give the impression of uniformly dominant performance, but the per-task distribution of gains is uneven. The paper would be strengthened by prominently discussing failure modes under memory interference.

3. **Key experimental evidence is deferred to the appendix.** The "~70% aggregate improvement" headline on MIKASA-Robo depends on the full 23-task table (Table 8 in the appendix) — only 4 tasks are shown in the main paper's Table 1. While appendix deferral is common, the central claim of the robotics evaluation is not verifiable from the main text. Similarly, default hyperparameter values (M, λ, σ, L, S) used in the primary experiments are stated only as "Appendix, Table 7" without even ranges in the body. This is a reproducibility concern for the core results.

### Minor
1. **POPGym improvement over RATE is modest.** The aggregate improvement from 9.5 to 10.4 is incremental, and ELMUR ranks first on 24/48 tasks — a majority but not a commanding one. The gain is concentrated on puzzle tasks (1.2 vs. 0.45), while on reactive tasks all methods are within 0.2. The paper's framing as "outperforms baselines on more than half of the tasks" is accurate but should be contextualized alongside the modest aggregate margin.

2. **No dedicated limitations section.** Given that the method shows sensitivity to capacity (M < N causes sharp drops) and performance degrades on high-interference tasks (RememberColor5/9), a candid discussion of these limitations would strengthen scientific credibility. The conclusion is brief and focuses on claims.

### Trivial
None.

## Nice-to-Haves
- An empirical analysis of memory dynamics (what content gets written, how often slots are reused, effective age distribution) would be more informative than the current theoretical section.
- A controlled experiment on T-Maze that inserts distractors in the corridor would clarify whether the model is counting steps or relying on the cue never being overwritten.
- Reporting the fraction of POPGym tasks where ELMUR is statistically significantly better than each baseline (e.g., via paired test) would strengthen the statistical claims.

## Removed Points
- **"Default hyperparameters missing from body text" (moved from Major to Minor concerns):** The paper explicitly states they follow Table 7 in the appendix. This is standard practice for many conferences and does not constitute a reproducibility barrier, though providing ranges in the body would be better.
- **"MoE choice is incidental and distracting" (removed):** Including the MoE design choice in the method section is fine — it's part of the architecture description. The ablation confirms it's not essential, which is a strength (honest reporting) not a weakness.
- **"Paper does not discuss computational overhead" (removed):** The paper explicitly compares parameter counts and per-step timing (Section RQ4), showing ELMUR is faster than RATE and DT.
- **Strength: "Theoretical guarantees on memory dynamics" (removed from strengths):** As discussed under Weakness 1, these are mathematically trivial and do not constitute a genuine strength. The paper would be better off without this framing.
- **"T-Maze sidesteps the challenge of managing multiple competing memories" (weakened):** This is partially true but the paper evaluates harder tasks (MIKASA, POPGym) that do require managing multiple memories. The T-Maze is explicitly a controlled test of retention.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Replace or reframe Section 4: either present the bounds as straightforward observations without claiming "theoretical analysis," or replace the section entirely with empirical analysis of memory dynamics (e.g., slot reuse statistics, what content gets written, effective age distributions).
2. Add a main-figure summary of the full MIKASA-Robo task distribution (e.g., a bar chart or histogram) so the "~70% improvement" claim is verifiable from the body.
3. State the default values or at least ranges for key hyperparameters (M, λ, σ, L, S) in the main text, even if the full table remains in the appendix.
4. Add a brief limitations paragraph to the conclusion discussing capacity sensitivity and interference failure modes.
5. Consider a small T-Maze variant with distractors to test whether the retention mechanism handles competing information.

## Score and Decision

The paper presents a well-specified architectural contribution (per-layer external memory with dedicated cross-attention and LRU management) with extensive empirical validation across three benchmarks. The T-Maze result is decisive evidence that the mechanism achieves its design goal. The main weaknesses are that (i) the theoretical analysis is superficial and its framing as a contribution is overstated, (ii) the strongest results come from the simplest task and performance degrades meaningfully under memory interference, and (iii) some key results and hyperparameters are deferred to the appendix. These are not fatal — the method is sound, the ablations are informative, and the empirical coverage is substantial. A revision addressing these issues would significantly strengthen the paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>