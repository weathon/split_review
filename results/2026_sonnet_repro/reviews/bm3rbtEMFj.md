Now let me do the calibration search to score this paper.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

ELMUR (External Layer Memory with Update/Rewrite) is a transformer architecture for long-horizon imitation learning under partial observability. Each transformer layer maintains a bounded external memory, interacts with it via bidirectional cross-attention (token→memory `tok2mem`, memory→token `mem2tok`), and updates it via an LRU policy that fills empty slots by full replacement, then refreshes the least-recently-used slot by convex blending with factor λ. A formal analysis of exponential forgetting and memory boundedness accompanies the method. ELMUR is evaluated on T-Maze (synthetic), POPGym-48 (diverse benchmark), and MIKASA-Robo (robotic manipulation), demonstrating strong long-horizon retention and competitive performance across domains.

---

## Strengths

- **Striking T-Maze extrapolation (Figure 3):** With only L=10 context length and S=3 training segments, ELMUR achieves 100% success on T-Maze corridors up to 10^6 steps — roughly 100,000× the attention window — while all baselines degrade substantially. The corresponding generalization heatmap (Figure 4) shows seamless transfer across the full 9–9600 step training/evaluation matrix.

- **Real POPGym gains on memory-intensive puzzles (Table 2):** On the 33 puzzle tasks, ELMUR scores 1.2 vs. 0.45 for the next-best method (RATE), and substantially higher than DT (−3.5) and BC-LSTM (−0.2). This is an independent benchmark and the advantage is unambiguous on the memory-demanding subset.

- **Principled, well-specified architecture:** Algorithm 1 and Algorithm 2 provide complete pseudocode for both the layer update and the LRU block. The method is reproducible from the main paper alone, and the relative-bias mechanism for grounding token-memory temporal distance is a thoughtful design choice.

- **Ablation confirms critical components (Table 3):** Removing LRU drops RememberColor3-v0 from 1.00±0.00 to 0.43±0.22; removing both LRU and relative bias further drops it to 0.22±0.11. Figure 6 additionally shows that M ≥ N is a clear phase transition for success — these ablations pin down what drives the method.

- **Competitive efficiency (Section 5.2, RQ4):** Despite richer memory, ELMUR (6.8±0.5 ms per step, 2.1M parameters) runs faster than RATE (7.2±0.3 ms) and DT (10.7±0.1 ms). Bounded memory size keeps complexity independent of sequence length.

---

## Weaknesses

### Fatal
None.

### Major

- **In-group evaluation for the headline "70% improvement" claim.** The MIKASA-Robo benchmark (Cherepanov et al., 2026a) and the primary memory-augmented transformer baseline RATE (Cherepanov et al., 2026c) appear to originate from the same research group as the ELMUR authors. The paper's strongest aggregate claim — "nearly doubles the performance of strong baselines on MIKASA-Robo, ranking first on 21/23 tasks and improving the aggregate by ~70%" — rests entirely on a benchmark and leading baseline that cannot be treated as fully independent. The paper does not acknowledge this relationship. Additionally, the headline figure of 21/23 tasks is cited to Appendix Table 8, making it unverifiable from the main text. The more independently credible POPGym results (Table 2) show meaningful but more modest gains (10.4 vs. 9.5 overall). Authors should explicitly acknowledge the in-group benchmark relationship and either provide additional independent evaluation, or clearly distinguish the MIKASA-Robo claims from the independently verifiable POPGym and T-Maze results.

- **Missing mechanistic explanation for T-Maze success at 10^6 steps under LRU eviction.** Section 3 establishes that once M slots are full, the LRU policy overwrites the least-recently-used slot every M segments. At T=10^6, L=10, there are 100,000 segments — far more than M (set to 3 during training). Under a simple LRU cycle, the original cue slot eventually becomes LRU and is overwritten by convex blending. Yet ELMUR achieves 100% success. The paper does not explain this: does the model learn to periodically refresh the cue slot (rehearsal)? Does λ→0 effectively freeze blended slots, meaning the cue content decays at rate (1−λ)^k ≈ 1 for very small λ? This is the most surprising result in the paper, and Section 5.2 (RQ1) presents it without any mechanistic story. The theoretical analysis in Section 4 assumes each slot is overwritten on a uniform cadence, which may not hold if the model learns selective refresh. Explaining this would transform the T-Maze result from impressive-but-opaque into a genuine insight about emergent memory rehearsal or about parameter selection.

### Minor

- **POPGym framing overstates breadth of advantage.** The abstract says ELMUR "outperforms baselines on more than half of the tasks" (24/48), which technically means it also underperforms on the other 24. The real story from Table 2 is clear and worth stating directly: on the 33 memory-intensive puzzle tasks, ELMUR leads substantially (1.2 vs 0.45); on the 15 reactive tasks, all methods are within noise of each other (ELMUR 9.2, RATE 9.1, DT 9.3, BC-LSTM 9.1). Distinguishing these regimes in the abstract would make the claims more precise and defensible.

- **Ablation is confined to a single task (RememberColor3-v0).** Table 3 and Figure 6 ablate on this one task. No ablation verifies which components matter on T-Maze or POPGym-puzzle tasks. Since the paper's core claim is cross-domain generalization, confirming that LRU is critical on at least one other task (e.g., a POPGym puzzle) would strengthen confidence in the component analysis.

- **RMT baseline appears in Figure 3 but is absent from Table 1 and Table 2.** Recurrent Memory Transformer (RMT; Bulatov et al., 2022) is plotted as a curve in Figure 3 (T-Maze) and is architecturally among the closest relatives of ELMUR (segment-recurrence with special tokens). Its exclusion from the main comparison tables is unexplained, and its inclusion would sharpen the differentiation from prior segment-recurrence methods.

### Trivial

- **MoE-FFN motivation is undermined by its own ablation.** Table 3 row "MoE → MLP: 1.00 ± 0.00" shows identical accuracy. The motivation in Section 3 ("MoE improve parameter efficiency and specialization") is reasonable for efficiency, but the paper initially presents it as a key design feature. Clarifying that MoE is chosen for computational efficiency (not accuracy) would remove this internal inconsistency.

- **Propositions 1 and 2 are stated as structural results.** Proposition 1 is a direct unrolling of the geometric series in Eq. (8) — algebraically elementary. Proposition 2 follows in one line from the convex combination staying in the convex hull of bounded inputs. Both are correct and useful for formal exposition, but calling them "propositions" slightly inflates their technical weight.

---

## Nice-to-Haves

- A visualization of which memory slots are written at which time steps on T-Maze — particularly whether the cue slot is actively refreshed or whether its information is distributed across slots via blending — would make the RQ1 result interpretable and reveal whether rehearsal is an emergent behavior.

- Designing an evaluation condition where multiple important cues must simultaneously survive in memory (forcing genuine LRU trade-offs between competing important information) would sharpen the memory capacity narrative and distinguish ELMUR from simpler single-item retention mechanisms.

- Reporting a selection criterion for the 23-of-32 MIKASA-Robo tasks used in the main evaluation (the criterion for the omitted 9 tasks is not stated in the main text).

- Guidance for setting M in practice when N (the number of required segments) is unknown for a new task would be practically valuable, given the sharp phase transition shown in Figure 6.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"T-Maze measures only the easiest possible case"** — The harsh critic argues T-Maze requires retaining "effectively a single bit" and is therefore too easy. While it is true that T-Maze only requires retaining one cue, the 10^6-step extrapolation from 30-step training contexts is nevertheless a meaningful stress test of any memory mechanism. The critique conflates task cognitive complexity with memory difficulty; 100,000 overwrites of bounded slots is a genuine memory challenge regardless of the information content. Removed as exaggerated framing.

- **"MIKASA-Robo 21/23 relies on stripped appendix"** — Per protocol, appendices exist in the original submission. The appendix reference is not a paper flaw. Removed as a formatting/parser artifact concern.

- **"Detachment of memory between segments prevents gradient flow across segments"** — This (sg(m^{i-1})) is the standard practice in Transformer-XL, RMT, and RATE; it is not a flaw unique to ELMUR and the paper explicitly acknowledges this design. Removed as not a distinguishing weakness.

- **Effective horizon formula assumes uniform LRU cadence** — The harsh critic says this assumption may not hold if the model learns selective refresh. This is a valid *mechanistic question* (kept as the second Major weakness) but the formula itself is explicitly stated as a "conservative lower bound" in Section 4. The formula criticism as a standalone weakness is removed; it is merged into the mechanistic explanation gap.

- **"No comparison with online RL baselines"** — The paper explicitly scopes these out (Section 5.1: "We do not compare with online RL baselines, since they assume interactive data collection with exploration, yielding incomparable training budgets"). Removed as scope-creep criticism of an explicitly justified design choice.

---

## Novel Insights

The most genuinely interesting observation that the reviewers surface — but that the paper itself does not fully develop — is the potential emergence of memory rehearsal in the LRU architecture. ELMUR achieves perfect T-Maze performance at 10^6 steps despite an LRU cycle that should eventually target the original cue slot. If the model learns to periodically write the cue slot's content back into itself (either directly or via blended propagation across slots), this would be an emergent form of active maintenance that mirrors biological working memory rehearsal, and that no current formal analysis of transformer memory systems has characterized. This would also have direct implications for the effective-horizon formula: the "conservative lower bound" on H(ε) could become tight or loose depending on whether rehearsal is learned, and understanding this distinction would open a line of theoretical work on learned vs. policy-driven memory management.

---

## Suggestions

1. **For the T-Maze mechanistic gap**: Run ELMUR on T-Maze with λ spanning 0 to 0.5, and separately log which slot index is overwritten at each segment. Determine empirically whether the cue slot is refreshed before becoming LRU-oldest. This experiment is cheap and would be the single most informative addition to the paper.

2. **For the in-group evaluation concern**: Add a paragraph in Section 5.1 explicitly noting that MIKASA-Robo and RATE are from the same research group, acknowledge the potential for benchmark-method alignment, and point readers to POPGym and T-Maze results as independent corroboration.

3. **For the ablation scope**: Run the "No LRU" ablation on at least one POPGym puzzle task (e.g., Minesweeper or Concentration) to confirm LRU's necessity is not task-specific.

4. **For POPGym framing**: Reframe abstract and introduction to foreground "ELMUR is the strongest method on memory-intensive puzzle tasks (33 tasks), with no regression on reactive tasks" rather than the aggregate "outperforms on 24/48" framing.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `N581Nje6fH.md` | 1.50 | R1 | Weak memory-transformer paper, much more superficial than ELMUR |
| `It4KL6XnPq.md` | 3.00 | R1 | Foundation policies + memory, GRUs on POPGym; much narrower scope than ELMUR |
| `We5z3UEnUY.md` | 6.50 | R1/R2 | Stable Hadamard Memory for RL — similar goals, comparable theoretical rigor; ELMUR is broader in evaluation and has stronger empirical results but shares the in-group concern |
| `c4w7WVs1z7.md` | 4.75 | R1 | RATE (ELMUR's primary baseline); ELMUR clearly surpasses this in architecture, theory, and evaluation breadth |
| `9pW2J49flQ.md` | 8.00 | R1 | DeepLTL for LTL in RL — strong theory; different domain, not comparable |

**Round 1 bracket: 5.5 – 7.0**

**Round 2 (Narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `FhbZ1PQCaG.md` | 5.75 | R2 | Decision Transformer with internal memory; rejected — narrower evaluation, weaker theoretical grounding than ELMUR |
| `We5z3UEnUY.md` | 6.50 | R2 | Most topically similar accepted paper; similar structure (theory + POMDPs + RL benchmarks). ELMUR has broader cross-domain evaluation and more striking empirical results, but comparable in-group concern weaknesses |
| `XYdstv3ySl.md` | 6.50 | R2 | 3D spatial memory for visual perception; different domain, accepted — not directly comparable |
| `h7aQxzKbq6.md` | 6.00 | R2 | Hierarchical manipulation transformer; different problem, accepted |

**Round 2 narrowing:** ELMUR is clearly above the 5.75 rejected anchor (FhbZ1PQCaG). It is closely comparable to Stable Hadamard Memory (6.50, accepted). Both have a theoretical analysis of memory retention, multi-benchmark evaluation on POMDPs, and principled memory management. ELMUR's T-Maze and POPGym results are stronger, but SHM evaluated on a slightly more diverse RL setting (meta-RL). The in-group benchmark concern in ELMUR is real and partially analogous to the "how were baselines tuned?" concern in SHM. On balance, ELMUR is at least as strong as SHM — arguably slightly stronger in empirical rigor — but the mechanistic T-Maze gap and the in-group MIKASA-Robo concern are genuine issues that keep it from rating higher.

**Final Score: 6.0** — Solid accept-level contribution; above the 5.75 rejected anchor and at the lower end of the accepted 6.5 papers given the in-group evaluation concern and the unexplained T-Maze mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>