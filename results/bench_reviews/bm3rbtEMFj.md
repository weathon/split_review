Now I have all the anchors. Let me calibrate and write the final review.

**Calibration summary:**

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| RATE (kByN4v0M3e) | 4.5 | Accept (Poster) | Most similar paper — same group, similar topic (memory-augmented transformer for offline RL/POMDPs). ELMUR has better probing analysis and ablation but similar overclaiming issues. RATE accepted despite these. |
| MIKASA-Robo (9cLPurIZMj) | 6.5 | Accept (Poster) | Benchmark paper from same group. Stronger contribution (new benchmark), but ELMUR's architecture + probing analysis is also substantial. |
| MemER (1dH4ARGdwD) | 5.0 | Accept (Poster) | Memory for robotic control. Similar goals, different approach. Modest incremental novelty but accepted. |
| PRISM (5SMNtmJFGa) | 3.5 | Reject | Visuomotor memory paper — rejected due to missing baselines and formatting. ELMUR has more thorough baselines. |
| PO-Dreamer (QklhZ70C49) | 3.5 | Withdrawn/Reject | Memory for POMDPs — rejected for testing memory claims on non-memory tasks. ELMUR does test on actual memory tasks. |
| NeuMa (clCsSQ5rKg) | 2.0 | Reject | Weak paper with vague claims — ELMUR is far more rigorous. |

ELMUR sits above RATE (4.5) in rigor (better probing, more thorough ablations) but below MIKASA-Robo (6.5) in contribution novelty. I assign **5.0** — comparable to MemER (5.0), which was accepted as Poster.

---

## Summary

This paper proposes ELMUR, a transformer architecture augmented with per-layer external memory slots, bidirectional token-memory cross-attention (read/write), and an LRU-based update rule that uses convex blending when all slots are filled. The method is evaluated on T-Maze (synthetic), POPGym (48 puzzle/control tasks), and MIKASA-Robo (32 robotic manipulation tasks with RGB observations) in an imitation learning (BC) setting. Key results include 100% success on T-Maze up to 1M steps (100,000× the attention window), improvements on POPGym (10.41 aggregate vs RATE's 9.54), and best success rate on 21 of 23 MIKASA-Robo tasks with non-zero baseline performance.

## Strengths

- **Clean, interpretable memory architecture.** The separation of read (mem2tok) and write (tok2mem) cross-attention, combined with the LRU update rule (fill empty slots by replacement, then convex blend the LRU slot), is well-motivated and clearly described in Algorithm 1. The relative bias formulation for temporal grounding between tokens and memory anchors is a neat design choice.

- **Thorough memory probing analysis (Appendix A.9–A.11).** Post-hoc probing demonstrates that ELMUR's memory slots encode task-relevant latent variables (target color) with near-perfect decodability shortly after the cue appears, and that the representation remains stable throughout the episode. PCA visualization, inter-slot similarity analysis, and cross-attention map inspection all corroborate that the model performs targeted, one-shot writes followed by stable retention. This kind of mechanistic verification is rare and valuable in memory-augmented policy papers.

- **Systematic ablation study (Table 3, Figure 6).** The ablation cleanly isolates the contribution of each component: removing LRU drops score from 1.00 to 0.43, sharing memory across layers drops to 0.45, and removing both relative bias and LRU drops to 0.22. The ablation also explores the effect of memory size M, blending factor λ, initialization scale σ, and segment configuration, providing practical guidance.

- **Broad evaluation across diverse benchmarks.** The paper evaluates on synthetic (T-Maze), puzzle/control (POPGym-48), and simulated robotic manipulation (MIKASA-Robo with RGB observations), demonstrating generality beyond a single domain.

## Weaknesses

### Fatal
None.

### Major

- **The T-Maze "100,000× horizon" result tests only passive single-bit retention, not active memory management.** The T-Maze task requires storing exactly one binary fact (left vs. right cue) at the start of a corridor with no new information. The model achieves 100% success at 1M steps because the slot containing the cue is never overwritten — the other slot(s) handle all subsequent updates during the empty corridor. This is confirmed by the paper's own update-pattern analysis (Figure 10). While this is a valid test of retention horizon, it does not test the kind of active memory management the paper motivates (e.g., the cooking robot tracking multiple ingredients over time). The "100,000×" framing in the abstract and title implies a more general capability than what is actually demonstrated. The paper should characterize this as a passive retention stress-test and add tasks requiring dynamic memory updates (e.g., tracking a changing variable, accumulating multiple facts, or following switching rules).

- **The theoretical analysis (Section 4) does not explain the key empirical results and includes a trivial proposition.** Proposition 1 (exponential forgetting) and the effective horizon formula assume uniform rotation through M slots. However, Figure 10 shows that the model performs targeted writes: the slot containing the critical cue is never overwritten once filled. This means the half-life formula (H₀.₅ ≈ M·L·ln2/λ, which for T-Maze gives ~270 steps) is irrelevant to the 1M-step result — the mechanism is not gradual decay but preservation of an untouched slot. Proposition 2 (boundedness of convex combinations) is mathematically trivial and does not merit a proposition. The theory section would benefit from being reframed as a formal description of the update dynamics rather than claiming to explain the empirical retention results.

- **ELMUR fails on 9 of 32 MIKASA-Robo tasks with no analysis of why.** The paper's main-text framing ("21 out of 23 tasks") selectively excludes the 9 tasks where *all* methods (including ELMUR) score zero: BunchOfColors3/5/7, SeqOfColors3/5/7, ChainOfColors3/5/7. These tasks — which require tracking multiple colors or sequences — are precisely the kind of active memory management the method claims to enable. The full results are correctly disclosed in Table 8 (appendix), but the main text never discusses or analyzes why ELMUR fails on these tasks. At minimum, the paper should characterize the failure modes and discuss whether the limitation is slot capacity, write-scheduling, or attention distraction.

### Minor

- **The POPGym improvement over RATE is modest.** ELMUR's aggregate return is 10.41 vs RATE's 9.54 — roughly a 9% improvement, not the 70% reported for MIKASA-Robo. The paper accurately reports this but the juxtaposition with the larger MIKASA-Robo claim could be misleading without context.

- **The "No rel. bias" ablation scores 0.95 (near perfect)** on RememberColor3-v0 (Table 3), which undermines the paper's emphasis on temporal biases as a key design component. The critical components are LRU and per-layer memory, not the relative bias.

- **The paper is titled and framed around "Long-Horizon RL Problems" but all experiments use imitation learning from demonstrations**, not online RL with sparse rewards (the method never interacts with the environment during training beyond the provided expert dataset). While the environments themselves have sparse-reward structure, this framing mismatch should be acknowledged more clearly.

- **Proposition 2 (boundedness) is mathematically trivial** — any convex combination of bounded vectors is bounded. Stating this as a formal proposition gives the theoretical section an inflated appearance.

### Trivial
- The related work section (Section 6) is comprehensive but excessively long (~100 citations), making it harder to identify the key distinctions from the most relevant prior work.
- MoE FFNs are described as improving "parameter efficiency" while the ablation shows MLP→MoE replacement improves "computational efficiency" — these refer to different efficiency metrics and are not contradictory, but the phrasing could be clarified.

## Nice-to-Haves
- A task requiring active memory management (e.g., tracking a changing variable, accumulating multiple facts, or following a switching rule) would substantially strengthen the claim that ELMUR's LRU blending mechanism is useful beyond passive retention.
- Moving the probing analysis (Appendix A.9–A.11) into the main paper would improve the paper significantly — it is the most novel and convincing evidence that the method works as intended.
- Measuring how many times each memory slot is actually updated per episode on T-Maze and harder tasks would help connect the theory to practice.

## Removed Points
*The following points raised by the reviewers were removed or moved here per the meta-review rules:*

- **"MoE improves parameter efficiency vs MoE→MLP improves efficiency — contradictory."** Not contradictory: MoE improves parameter efficiency (sparse activation, more capacity per parameter), while MLP improves computational efficiency (simpler forward pass). These are distinct metrics. **Removed (factually wrong).**
- **"Paper never verifies that memory slots are actually rotated uniformly."** Figure 10 in the appendix shows the update pattern. The paper does verify this. **Removed (appendix exists in original submission).**
- **"The paper does not specify the cross-attention dimension."** The paper specifies model dimension d, number of heads H, and the relative bias table. Cross-attention dimension follows from these. **Removed (nitpick).**
- **"Missing related works"** per the meta-reviewer instructions. **Removed (per instruction).**
- **Formatting/typo nitpicks** (e.g., "broken characters, garbled text"). **Removed (parser artifact).**

## Novel Insights

The review process surfaces an interesting tension that the paper does not fully grapple with: the method's strongest result (1M-step T-Maze) arises from a mechanism that is *simpler* than the theoretical apparatus used to explain it. The probing analysis reveals that ELMUR works by performing a single targeted write into a memory slot and then *never touching that slot again* — which is exactly the behavior of a write-once memory. The LRU blending rule (with its exponential decay analysis) is essentially unused during the long retention phase; it only matters when the agent must juggle multiple pieces of information across a *bounded* active window. This suggests that the paper's theory (exponential forgetting via convex blending) is actually a description of the *failure mode* of the memory system under capacity pressure, not the mechanism that produces the headline result. The probing analysis, by showing that the method's success comes from sparse, one-shot writes and stable preservation, tells a more honest and interesting story than the theoretical framing. A paper that led with this insight — "ELMUR achieves extreme retention not through gradual blending but by writing once and preserving untouched" — would be stronger and more intellectually honest.

## Suggestions

1. **Tone down the "100,000×" claim** and clarify that the T-Maze result tests passive single-bit retention. Add a task requiring active memory management (e.g., switching rules, accumulating counts) to demonstrate the LRU blending mechanism under memory pressure.

2. **Move the memory probing analysis (Appendix A.9–A.11) into the main paper** — it is the strongest evidence that the architecture works as intended and should replace the less informative theoretical section.

3. **Discuss the 9 zero-score MIKASA-Robo tasks in the main text.** Explain why ELMUR (and all baselines) fail on BunchOfColors, SeqOfColors, and ChainOfColors, and what this reveals about the method's limitations.

4. **Reframe the theoretical section** as a formal description of the update dynamics rather than claiming to "explain" the 1M-step result. Add a discussion of when blending matters vs. when simple preservation suffices.

5. **Explicitly acknowledge the IL-only evaluation setting** in the title/abstract framing, and discuss the gap between BC evaluation and the motivating RL problem.

## Score and Decision

**Score: 5.0** — The paper presents a well-engineered architecture with clean design, thorough ablations, and rare mechanistic verification via memory probing. However, the central claims are overblown: the "100,000× horizon" result tests only passive single-bit retention, the theory does not explain the empirical behavior, and the main text selectively reports MIKASA-Robo results. These are addressable weaknesses, and the core architectural contribution is solid.

Compared to anchors:
- **RATE (4.5, Accept)**: Same research group, similar topic. ELMUR has better probing analysis and ablations, similar overclaiming issues. ELMUR is slightly stronger → **5.0**.
- **MemER (5.0, Accept)**: Similar tier contribution — solid engineering with real evaluation on memory tasks. Comparable quality.
- **PRISM (3.5, Reject)**: Missing baselines and weaker probing. ELMUR is stronger.
- **PO-Dreamer (3.5, Withdrawn/Reject)**: Tested memory claims on non-memory tasks. ELMUR at least tests on explicit memory tasks.
- **MIKASA-Robo (6.5, Accept)**: Stronger contribution (new benchmark) but different paper type. ELMUR's architecture + probing is solid but less novel.
- **NeuMa (2.0, Reject)**: Much weaker paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>