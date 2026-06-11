Now I have sufficient calibration data. Let me write the final consolidated review.

**Calibration Summary:**

- **Round 1 bracket:** 4.0–5.5, based on comparison with RATE (4.75) on the low end and SHM (6.50) on the high end.
- **Round 2 narrowing:** Compared against "Think Before You Act: DT with Internal Memory" (5.75, Reject) and PANM (5.67, Reject). ELMUR has stronger ablations and more diverse benchmarks than DT-Mem but has a clear factual error (23 vs 32 task count) that DT-Mem does not.
- **Final score:** 5.0. ELMUR is clearly stronger than RATE (4.75) — its T-Maze results are clean and its ablations are thorough. But it is weaker than SHM (6.50, Accept) which has genuine theoretical contributions. The 23/32 inconsistency and thin theory place ELMUR slightly below "Think Before You Act" (5.75).

**Anchors consulted (all rounds):**
1. RATE (4.75, Reject) — Round 1, Round 2. Related work; ELMUR is stronger with cleaner T-Maze results and better ablations.
2. V-Former (4.25, Reject) — Round 2. Different focus; less relevant.
3. Foundation Policies with Memory (3.00, Reject) — Round 1. Weaker paper on similar topics.
4. Continual Task Learning (4.75, Reject) — Round 2. Different focus.
5. Think Before You Act: DT with Internal Memory (5.75, Reject) — Round 1, Round 2. Similar level but ELMUR has the 23/32 error.
6. PANM (5.67, Reject) — Round 2. Different domain (symbolic processing).
7. Stable Hadamard Memory (6.50, Accept) — Round 1. Stronger; has genuine theoretical contributions.
8. NaviFormer (6.00, Reject) — Round 2. Different domain.

## Summary

ELMUR proposes a transformer architecture augmented with per-layer external memory embeddings, bidirectional cross-attention (mem2tok read, tok2mem write), and an LRU-based update rule for long-horizon, partially observable decision-making in IL/offline RL settings. The method is evaluated on T-Maze (synthetic), MIKASA-Robo (robotic manipulation), and POPGym (puzzles/control), achieving a 100% success rate on T-Maze corridors up to one million steps, competitive results on MIKASA-Robo, and the top aggregate score on POPGym.

## Strengths

- **100% success rate on T-Maze corridors up to one million steps (Figure 3, L=10, S=3).** ELMUR achieves perfect retention while all baselines degrade sharply, with the closest competitors (RATE, BC-MLP) plateauing at ~70%. This cleanly demonstrates the method's ability to retain information across extremely long horizons and directly validates the paper's central architectural claim.

- **Systematic and informative ablation study (Table 3, Figure 6).** The paper ablates each component (shared memory, relative bias, LRU, MoE→MLP) and maps the failure regime (M < N) vs. stable regime (M ≥ N) across multiple hyperparameters (λ, σ, segment configuration). Removing LRU drops performance from 1.00 to 0.43, and shared memory drops to 0.45 — cleanly confirming both the LRU mechanism and the per-layer design. The finding that intermediate blending values λ≈0.4–0.6 are unstable and that under-provisioned memory is highly sensitive to initialization provides actionable practical guidance beyond final scores.

- **Generalization across unseen sequence lengths (Figure 4).** ELMUR trained on short corridors (9–300 steps) transfers seamlessly to validation lengths up to 9600 steps with no degradation, demonstrating that the model does not overfit to a specific horizon scale. This addresses a common failure mode in memory-augmented models where performance collapses when the test horizon exceeds the training horizon.

## Weaknesses

### Fatal
None.

### Major

1. **Internal inconsistency in the reported task count for MIKASA-Robo (23 vs. 32).** The abstract and introduction state "21 out of 23 tasks" and "21 of 23 tasks," while the Table 1 caption reads "See results for all 32 MIKASA-Robo tasks in Appendix, Table 8." This is an internal factual error in the paper. If the suite has 32 tasks, "21 out of 23" is uninterpretable (which 9 tasks are omitted?). If it has 23 tasks, the reference to 32 in the caption is wrong. The paper's central MIKASA-Robo claim depends on this number; the authors must resolve this discrepancy and ensure the abstract, body, and captions agree.

2. **Only 4 of the claimed 23/32 MIKASA-Robo tasks are shown in the main paper (Table 1).** Only RememberColor3/5/9 and TakeItBack are reported. The remaining tasks are relegated to the appendix (stripped from the extracted PDF). This makes the headline claims ("nearly doubling baseline performance," "best on 21/23 tasks," "~70% improvement") impossible to fully verify from the main paper alone. The authors should either include more tasks or justify why these 4 are representative of the full suite.

3. **The theoretical analysis (Section 4) does not substantively strengthen the paper.** Proposition 1 derives the composition of convex updates — a direct algebraic consequence of equation (8). The Corollary follows from solving (1−λ)^k = 1/2. Proposition 2 states that a convex combination of vectors with norm ≤ C also has norm ≤ C — a trivial consequence of convexity. These are all correct but amount to restating the definition of the update rule. Moreover, the "effective horizon" derivation assumes a uniform round-robin schedule, while the LRU policy selects the least recently used slot based on learned write patterns — the distribution of updates depends on tok2mem cross-attention, which the theory does not model. The paper acknowledges this only as a "conservative lower bound," but the section as presented does not constitute a novel theoretical contribution.

### Minor

1. **D_max (maximum relative distance in the bias table) is not reported anywhere in the paper.** The paper describes clamping offsets to [−D_max+1, D_max−1] but never states the value of D_max. For a paper claiming million-step retention, it matters whether the bias table can distinguish million-step offsets or whether everything beyond some threshold is uniformly clamped (meaning the relative bias provides no distance signal for far-away memories).

2. **The MoE→MLP ablation shows identical performance (1.00±0.00).** The authors note this "preserves accuracy while improving computational efficiency," which is true, but it also means MoE contributes zero accuracy gain on the ablated task. The presence of MoE in the main experiments is a confound for interpreting whether gains come from the memory mechanism or from the MoE architecture (though the ablation suggests the former). This is not a flaw per se, since the ablation honestly reports it, but it weakens the "simple framework" narrative.

3. **The POPGym aggregate advantage is modest.** ELMUR achieves 10.4 vs. RATE's 9.5 — a difference of 0.9 on a ~22-point scale (range: -12.2 to 10.4). On the 15 reactive tasks, ELMUR's 9.2 is behind DT's 9.3. The claim "outperforms baselines on more than half of the tasks" (24/48) is technically accurate, but the aggregate margin over the best competitor is small.

4. **RMT and Transformer-XL appear in Figure 3 (T-Maze) but are never defined or introduced in Section 5.1 (Benchmarks and Baselines).** The reader must infer what "TrXL" and "RMT" refer to. These acronyms should be explicitly expanded when first used.

### Trivial

- The "100,000× beyond attention window" framing is mathematically correct (10^6 / L=10 = 100,000) but conflates two mechanisms: segment-level recurrence (which any segment-recurrent system inherits) and the LRU-based external memory. The paper should contextualize this framing more carefully to avoid giving the impression that a pure attention window of length 10 is the relevant comparison point for a system with segment-level recurrence.

## Nice-to-Haves

- An analysis of what the external memory actually stores (e.g., probing memory content, nearest-neighbor retrieval of segments that influenced a given slot) would deepen the paper's argument about "explicit" memory.
- Reporting the actual M and N values used in the main MIKASA-Robo and POPGym experiments would clarify whether the LRU mechanism was ever stressed during training on these tasks.
- Including Memformer or Block-Recurrent Transformer as baselines would strengthen the comparison, though the current baseline set is already reasonable.

## Removed Points

These points were considered but removed after verification against the paper:

- **"POPGym not achieving top score on 24 of 48 tasks is a weakness"** — Removed as tautological. The paper explicitly states "top score on 24 of 48 tasks," which by definition means it did not achieve top score on the other 24. This is not a meaningful weakness.
- **"Only 3 runs is insufficient"** — Removed as generic. 3 runs with SEM reporting is standard evaluation practice in RL.
- **"T-Maze 100,000× is a straw man"** — Weakened to trivial. The paper clearly states L=10 attention window, and 10^6/10 = 100,000 is mathematically correct. The comparison against other memory-augmented systems (where ELMUR still wins at 100% vs ~70%) further validates the result. The framing is attention-grabbing but not deceptive.
- **"Theoretical analysis is a core contribution" (from Strength Finder)** — Weakened. The propositions are correct but thin; this is properly reflected in the Major weakness above.
- **Generic strengths about "addressing an important problem"** — Removed as non-specific.

## Novel Insights

The harsh critic and strength finder together reveal an interesting tension: ELMUR's strongest empirical evidence (T-Maze 100%, clean ablations) is precisely where the theory is weakest. The T-Maze result is genuinely impressive and well-validated through component ablations, but the theoretical "guarantees" add nothing beyond what is obvious from the algorithm definition. Papers in this space should either invest in a non-trivial theoretical analysis (characterizing what information is actually stored, how LRU schedules differ from round-robin in practice, etc.) or drop the theory section entirely and focus on empirical rigor.

## Suggestions

1. **Resolve the 23/32 task-count inconsistency immediately** — this is the single most important fix. Ensure the abstract, introduction, and Table 1 caption agree.
2. **Report D_max** used in the relative bias table.
3. **Report M and N** values used in the main MIKASA-Robo and POPGym experiments.
4. **Include representative MIKASA-Robo results** for more than 4 tasks in the main paper, or explain why these 4 are sufficient.
5. **Define RMT and TrXL** in the baselines section.
6. **Either strengthen the theoretical section** with analysis that goes beyond restating the update rule, or honestly downgrade the claimed contribution.
7. **Calibrate the POPGym claims** to match the modest aggregate margin.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>