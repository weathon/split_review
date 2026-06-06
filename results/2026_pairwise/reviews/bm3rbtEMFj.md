Now I have enough understanding of the paper to write the draft review. Let me draft it before running calibration searches.Now I'll run the 5 bracketing calibration searches across all bands simultaneously:Now I have all the information needed. Let me write the final review.

---

## Summary
ELMUR (External Layer Memory with Update/Rewrite) augments each transformer layer with a structured external memory track. The key components are: layer-local memory embeddings that persist across segments, bidirectional cross-attention (mem2tok/tok2mem) for read/write, and an LRU update rule that fills empty slots via full replacement before blending new content convexly into the least-recently-used slot. The method is evaluated under imitation learning on three benchmarks designed to test memory under partial observability: the synthetic T-Maze, the diverse POPGym suite (48 tasks), and the MIKASA-Robo robotic manipulation suite.

---

## Strengths

- **Striking T-Maze retention result (Figure 3):** ELMUR achieves 100% success on T-Maze corridors up to 10^6 steps using only L=10, S=3, while all baselines (RATE, RMT, DT, BC-LSTM, TrXL, DMamba) substantially degrade. This is a concrete, stark demonstration of the architecture's extended memory capacity — retaining information approximately 100,000× beyond the native attention window.

- **Cross-domain consistency with real puzzle-task advantage (Table 2):** On the independent POPGym benchmark, ELMUR achieves the best aggregate score (10.4 vs. 9.5 for RATE), with a meaningful advantage on the puzzle subset (1.2 vs. 0.45 for RATE, while DT and BC-LSTM score below zero). This independently-validated result is the paper's most credible empirical contribution.

- **Ablation study clearly isolates key design contributions (Table 3, Figure 6):** Removing LRU drops performance from 1.00±0.00 to 0.43±0.22; removing both LRU and relative bias further reduces to 0.22±0.11; shared (non-per-layer) memory scores only 0.45±0.03. Figure 6 additionally confirms the M≥N capacity threshold. These ablations cleanly attribute ELMUR's gains to identifiable design choices.

- **Computational efficiency maintained (Section 5.2 RQ4):** Despite added memory and cross-attention, ELMUR runs at 6.8±0.5ms per step, below RATE (7.2ms) and DT (10.7ms), using only 2.1M parameters. Complexity is bounded by memory size, not sequence length.

- **No degradation on fully observable MDPs:** All models including ELMUR achieve 500±0 on CartPole-v1 (Section 5.2 RQ5), confirming memory mechanisms do not introduce instability on standard MDP tasks.

---

## Weaknesses

### Fatal
None.

### Major

- **In-group evaluation undermines the strength of headline claims.** Both the MIKASA-Robo benchmark (Cherepanov et al., 2026a) and the primary comparison baseline RATE (Cherepanov et al., 2026c) originate from the same research group as the ELMUR authors. The abstract's "70% improvement" and "21 out of 23 tasks" figures rest entirely on this in-group evaluation. The paper does not acknowledge this conflict, and there is no structural mitigation (e.g., demonstrating that benchmark/baseline implementations are independent). Compounding the concern, RATE's variance on TakeItBack-v0 is 0.42±0.24 (Table 1) — implying inconsistent or failed convergence rather than a stable well-tuned baseline. The independent POPGym results are more credible, but the largest headline claims specifically depend on evaluations that cannot be treated as fully independent.

- **T-Maze mechanistic gap.** ELMUR achieves 100% success at corridor length 10^6 even though: (a) gradients are detached between segments (`sg(m^{i-1})`, Section 3), preventing direct cross-segment credit assignment, and (b) per the LRU algorithm (Algorithm 2), the initial cue slot eventually becomes the least-recently-used target and should be overwritten after M complete LRU cycles. Section 5.2 (RQ1) provides no mechanistic account of how the cue survives to step 10^6. The theoretical analysis (Section 4) assumes each slot is updated uniformly once every M segments, but the result is only consistent if the model learns adaptive refreshing or distributes the cue across slots — neither of which is discussed. Without this explanation, the paper's most striking result is empirically impressive but mechanistically uninterpreted.

### Minor

- **POPGym framing overstates the breadth of gains.** The abstract's "outperforms baselines on more than half of the tasks" (24/48) and the aggregate score improvement (10.4 vs. 9.5) obscure a meaningful regime distinction. Table 2 shows that on the 15 reactive tasks, ELMUR (9.2), RATE (9.1), DT (9.3), and BC-LSTM (9.1) are functionally identical. ELMUR's genuine advantage is confined to the puzzle subset (1.2 vs. 0.45). Presenting the aggregate conflates a real signal (puzzles) with a non-signal (reactive tasks).

- **M hyperparameter sensitivity without practical guidance.** Figure 6 demonstrates a sharp performance cliff when M<N (where N is the number of segments needed to solve the task). Since N is task-dependent and not observable a priori, there is no practical guidance for setting M in new tasks. The paper acknowledges but does not resolve this.

- **Propositions 1 and 2 overstate theoretical content.** Proposition 1 (Eq. 9) is a direct unrolling of the exponentially weighted moving average formula — it is the definition of the convex update rule, not a derived result. Proposition 2 is a one-sentence observation that convex combinations of bounded vectors remain bounded. These are correct and useful for exposition, but calling them "propositions" inflates their significance. Furthermore, the effective horizon formula H(ε) assumes each slot is overwritten uniformly once per M segments, an assumption that may not hold if the model learns to preferentially refresh important slots.

- **Selection of 23 out of 32 MIKASA-Robo tasks is unexplained.** Table 1's caption directs readers to "results for all 32 MIKASA-Robo tasks in Appendix, Table 8," but the "21 out of 23 tasks" headline claim is never reconciled with the full 32-task suite in the main text. The criterion for selecting 23 tasks for the primary headline is not stated.

- **Ablations conducted on a single task (RememberColor3-v0).** Whether conclusions generalize — e.g., that MoE→MLP has no accuracy cost, or that relative bias gives only modest gains — is not verified on POPGym puzzle tasks or TakeItBack.

### Trivial

- The No-LRU ablation yields 0.43±0.22 — a large variance suggesting inconsistent rather than uniformly poor performance. This detail deserves a sentence of discussion.

---

## Nice-to-Haves

- Visualizing slot write patterns during T-Maze trajectories (which slots are active, whether the initial cue slot is periodically refreshed) would make the paper's most striking result interpretable rather than merely impressive.
- Restructure POPGym results to lead with the puzzle/reactive split, positioning the aggregate aggregate score as secondary.
- A practical heuristic for choosing M (e.g., relating it to the expected number of discrete critical events or decision points in a task) would make the architecture more directly usable.
- An evaluation with multiple competing cues that must simultaneously survive LRU eviction would more directly test whether the LRU policy makes intelligent eviction decisions.
- A brief note acknowledging the in-group relationship between ELMUR, MIKASA-Robo, and RATE — and characterizing why the comparison is still informative (e.g., same preprocessing pipeline, consistent evaluation protocol) — would strengthen the credibility of those results.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing RMT as a named baseline in Table 1/Table 2**: RMT appears in Figure 3 but not in the main tables. Per hard rules, missing related work / baseline comparisons are not flagged.
- **"21/23 depends on stripped appendix"**: Appendices are assumed to exist; the paper explicitly cites Appendix Table 8.
- **Reproducibility / undisclosed hyperparameters**: The paper defers hyperparameters to Appendix Table 7. This is standard practice.
- **MoE vs MLP inconsistency as a "weakness"**: The paper justifies MoE on computational efficiency grounds (Section 5.2 RQ4), not accuracy alone. Calling it "unmotivated" misreads the paper's stated rationale.
- **"Abstract implies only 24/48 wins" as a weakness**: The paper accurately describes "more than half." This is not a strength to falsify.

---

## Novel Insights

The most genuinely interesting unresolved question raised by this paper is the LRU eviction paradox: given (a) gradient detachment between segments and (b) an LRU policy that must eventually overwrite every slot, how does ELMUR's initial-cue slot survive to step 10^6 in the T-Maze? Two candidate explanations emerge from the architecture but are never discussed: (1) the model learns emergent rehearsal — periodically writing the readout of the cue slot back into the LRU target, effectively refreshing it without being explicitly trained to do so; or (2) information is distributed across multiple slots via convex blending, such that no single slot's loss is catastrophic. The first would be a notable emergent memory maintenance behavior; the second would imply the effective capacity exceeds M under structured blending. Both are genuinely interesting findings that would change how we understand bounded LRU memory for sequence learning. The theoretical analysis (Section 4) implicitly assumes neither mechanism, and therefore does not actually explain the paper's headline empirical result.

---

## Suggestions

1. Add a visualization or analysis of slot write patterns during a T-Maze episode — specifically, track whether the slot written at step 1 (the cue) is periodically refreshed or whether information spreads across slots. This directly addresses the most important unresolved question.
2. Explicitly note in the MIKASA-Robo section that the benchmark and RATE baseline share a research group with the authors, and characterize why the experimental setup remains informative (uniform preprocessing, fixed seeds, identical observation inputs for all methods).
3. Restructure Table 2 framing to present puzzle vs. reactive tasks as primary results, with aggregate as secondary — the real contribution is on puzzles.
4. Provide a brief practical guideline for setting M given unknown task complexity.

---

## Score and Decision

**Evaluation on key axes:**

- **Originality:** Moderate-high. The combination of layer-local external memory, bidirectional cross-attention per-layer, and LRU management is a principled and clean extension of prior segment-recurrence methods (TrXL, RMT). The design is specific enough to be genuinely novel, not merely incremental.
- **Importance of research question:** High. Long-horizon partial observability is a real bottleneck in robotics and RL, and memory-efficient approaches to this problem are actively needed.
- **Claims well-supported:** Mixed. The T-Maze claim is empirically strong but mechanistically underexplained. The POPGym puzzle claim is genuinely supported. The MIKASA-Robo headline figures have the in-group evaluation concern.
- **Soundness of experiments:** Moderate. 3 seeds, 100 evaluation episodes is standard for the field; the evaluation protocol is consistent across methods. The main validity concern is evaluation independence, not experimental design per se.
- **Clarity of writing:** Good. Algorithm 1 and Algorithm 2 are precise; the method is well-specified.
- **Value to the research community:** Solid. The architecture is clean, reproducible (code released), and the T-Maze + POPGym results provide genuine benchmarks for future memory-augmented IL/RL work.

Calibration anchors: RATE (c4w7WVs1z7, 4.75) is the direct predecessor which ELMUR improves upon; Stable Hadamard Memory (We5z3UEnUY, 6.5) is a comparable memory-for-RL paper with similar breadth; AMAGO (M6XWoEdmwf, 7.5) represents a stronger, broader contribution in the same space. ELMUR sits between SHM and RATE in terms of contribution, slightly below SHM due to the in-group evaluation concern making the largest empirical claims partially non-independent. Score: **6.0**, **Accept** (borderline).

# Selected Anchors

<related>["N581Nje6fH", "1mMjZvEhwH", "It4KL6XnPq", "c4w7WVs1z7", "T1pUS4GZZq", "We5z3UEnUY", "M6XWoEdmwf", "M992mjgKzI"]</related>

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>