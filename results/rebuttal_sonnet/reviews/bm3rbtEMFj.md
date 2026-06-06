## Summary

ELMUR (External Layer Memory with Update/Rewrite) is a transformer architecture for long-horizon imitation learning under partial observability. Each transformer layer maintains a bounded external memory, interacts with it via bidirectional cross-attention (tok2mem, mem2tok), and updates it via an LRU policy that fills empty slots by full replacement, then refreshes the least-recently-used slot by convex blending with factor λ. A formal analysis of exponential forgetting and memory boundedness accompanies the method. ELMUR is evaluated on T-Maze (synthetic), POPGym-48 (diverse benchmark), and MIKASA-Robo (robotic manipulation), demonstrating strong long-horizon retention and competitive performance across domains.

---

## Rebuttal Assessment

**Weakness:** In-group evaluation for the "70% improvement" claim (MIKASA-Robo / RATE)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author makes a genuinely persuasive meta-argument: ELMUR beats RATE by a large margin on the very benchmark RATE's authors designed (0.89 vs. 0.65 on RememberColor3-v0, 0.78 vs. 0.42 on TakeItBack-v0, per Table 1). If the benchmark were tuned to favor an in-group method, ELMUR should not be able to outperform that method by such wide margins. The five baselines in Table 1 also include fully independent methods (DT, BC-MLP, CQL, Diffusion Policy), all of which ELMUR leads. The rebuttal correctly identifies independent POPGym and T-Maze results as corroboration. However, the promise to "add a transparency statement in revision" does not count — the paper itself still does not acknowledge the shared authorship relationship, which is a real gap.
- **Score impact:** Weakness downgraded (from major to moderate concern)

---

**Weakness:** Missing mechanistic explanation for T-Maze success at 10^6 steps under LRU eviction
- **Author's response:** Partially address
- **Assessment:** Unconvincing — The rebuttal offers two candidate mechanisms: (i) selective write suppression via relative bias, and (ii) slow decay for small λ. Crucially, the author explicitly admits "neither candidate has been confirmed through slot-level analysis or λ-sweep experiments." I verified this directly in the paper: Section 4 provides the theoretical formula H(ε) = M·L·ln(ε)/ln(1-λ), explicitly calling it a "conservative lower bound," and notes that "in practice, effective horizons are often much longer (Figure 3)" — but provides no explanation of the gap. For M=3, L=10, even with λ=0.01, H ≈ 20,000 steps — still ~50× shorter than the empirically observed 10^6 steps. The mechanistic story for how content survives ~100,000 LRU cycles is genuinely absent from the paper. The rebuttal's "write suppression via relative bias" argument is plausible but unprecise: Algorithm 2 forces the LRU slot to be updated regardless of the relative bias — the relative bias affects the cross-attention *content* written to that slot, and the model could learn to write near-zero updates to the LRU slot — but this is neither stated nor verified in the paper. The promise to conduct and report slot-level analysis "before camera-ready" does not resolve this in the current submission.
- **Score impact:** Weakness unchanged

---

**Weakness:** POPGym framing overstates breadth of advantage
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes that the paper body (Section 5.2 RQ4) already makes the puzzle/reactive distinction: "largest gains on memory puzzles (1.2 vs. 0.45 for RATE; DT and BC-LSTM score below zero). On reactive tasks, ELMUR stays competitive." I verified this in Table 2 and the RQ4 paragraph. The weak framing is in the abstract only. The rebuttal commits to revise the abstract — this is a revision promise and doesn't count, but the body-text concern is legitimately diminished.
- **Score impact:** Weakness downgraded to minor

---

**Weakness:** Ablation confined to a single task (RememberColor3-v0)
- **Author's response:** Acknowledge
- **Assessment:** Honest but unresolved — The author acknowledges this is a genuine scope limitation and commits to adding a POPGym ablation in revision. That promise does not count per evaluation protocol. The weakness stands.
- **Score impact:** Weakness unchanged

---

**Weakness:** RMT baseline appears in Figure 3 but absent from Table 1 and Table 2
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The explanation (RATE is the representative of the segment-recurrence family, and RMT was evaluated on T-Maze specifically for that architectural comparison) is reasonable and consistent with Section 5.1's stated baseline selection criteria. However, the omission is still unexplained in the paper itself, and the rebuttal commits to adding a clarifying sentence in revision. Architecturally, RATE does closely parallel RMT (both use segment recurrence with special memory tokens), so the representativeness argument is defensible.
- **Score impact:** Weakness downgraded to trivial

---

**Weakness:** MoE-FFN motivation undermined by its own ablation
- **Author's response:** Partially address
- **Assessment:** Convincing — I verified this in the paper. Section 3 states MoE is chosen "scaling capacity without proportional compute." Section 5.2 RQ5 explicitly states "replacing MoE-FFN with MLP-FFN preserves accuracy while improving computational efficiency." The author correctly identifies that the ablation *confirms* rather than contradicts the paper's efficiency-focused rationale. The opening sentence of Section 3 ("MoE improve parameter efficiency and specialization") could be read as implying accuracy benefit, but the broader context makes the intent clear. This weakness was slightly misframed in the original review.
- **Score impact:** Weakness removed

---

**Weakness:** Propositions 1 and 2 are technically elementary
- **Author's response:** Acknowledge
- **Assessment:** Honest — The author concedes these are trivially derived (geometric series unrolling; convex hull closure) and commits to reframing them as "formal observations" or "lemmas." The weakness stands as assessed but was always trivial.
- **Score impact:** Weakness unchanged (trivial)

---

## Strengths

- **Striking T-Maze extrapolation (Figure 3):** With only L=10 context length and S=3 training segments, ELMUR achieves 100% success on T-Maze corridors up to 10^6 steps, roughly 100,000× the attention window, while all baselines degrade substantially. Verified in Figure 3 caption: "ELMUR achieves 100% success even under this extreme extrapolation."
- **Real POPGym gains on memory-intensive puzzles (Table 2):** On the 33 puzzle tasks, ELMUR scores 1.2 vs. 0.45 for RATE, and substantially higher than DT (−3.5) and BC-LSTM (−0.2). This is verified directly in Table 2. The advantage on the memory-relevant subset is unambiguous.
- **Principled, well-specified architecture:** Algorithm 1 and Algorithm 2 provide complete pseudocode for both the layer update and the LRU block. Relative bias for grounding token-memory temporal distance is a thoughtful design choice, verified in Equations 6-7.
- **Ablation confirms critical components (Table 3):** Removing LRU drops RememberColor3-v0 from 1.00±0.00 to 0.43±0.22; removing both LRU and relative bias further drops it to 0.22±0.11. The M ≥ N phase transition in Figure 6 is a clear and informative result.
- **Competitive efficiency (Section 5.2, RQ4):** ELMUR (6.8±0.5 ms, 2.1M parameters) runs faster than RATE (7.2±0.3 ms) and DT (10.7±0.1 ms). Verified in RQ4 discussion.
- **Strong manipulation results in Table 1:** ELMUR dominates on MIKASA-Robo across all five baselines (including four fully independent ones). TakeItBack-v0: 0.78±0.03 vs. 0.42±0.24 (RATE). The large margins over non-in-group baselines are independently meaningful.

---

## Weaknesses

### Fatal
None.

### Major
- **Missing mechanistic explanation for T-Maze success at 10^6 steps under LRU eviction.** The theoretical bound (H(ε) = M·L·ln(ε)/ln(1-λ)) predicts a retention horizon many orders of magnitude shorter than the empirically observed 10^6 steps for any reasonable M, L, λ. The paper flags the discrepancy as a "conservative lower bound" but provides no explanation. The rebuttal offers two speculative mechanisms, both explicitly unconfirmed by experiment. For the paper's most striking headline result, this unexplained gap remains a significant weakness.

### Minor
- **In-group benchmark relationship not disclosed in paper.** MIKASA-Robo (Cherepanov et al., 2026a) and RATE (Cherepanov et al., 2026c) share a first author with the present work. The paper does not acknowledge this relationship. The rebuttal's argument that "ELMUR beats in-group RATE by large margins" limits the severity, but the lack of disclosure is a transparency issue.
- **Ablation scope limited to RememberColor3-v0.** No ablation verifies LRU importance on POPGym puzzle tasks or T-Maze. Cross-domain ablation claims are therefore not fully supported.
- **RMT excluded from main comparison tables without explanation.** RMT is plotted in Figure 3 but absent from Table 1 and Table 2 without stated justification. Rebuttal offers a reasonable explanation but it is not in the paper.
- **POPGym abstract framing.** "Outperforms baselines on more than half of tasks" buries the more informative puzzle/reactive partition, though the body of the paper (Table 2, RQ4) already makes this distinction correctly.

### Trivial
- **Propositions 1 and 2 are algebraically elementary.** Calling them "propositions" slightly inflates their technical weight; "formal observations" or "lemmas" would be more accurate. Acknowledged by authors.

---

## Nice-to-Haves
- Slot-level visualization of which memory slot is overwritten at each segment on T-Maze, to determine if the cue slot is actively refreshed — this would provide the mechanistic story the paper currently lacks for its headline result.
- Explicit transparency statement in Section 5.1 noting the shared authorship of MIKASA-Robo and RATE.
- At least one ablation on a POPGym puzzle task (e.g., Minesweeper, Concentration) to confirm that LRU is critical beyond RememberColor3-v0.
- Abstract revised to foreground "ELMUR is the strongest method on memory-intensive puzzle tasks, with no regression on reactive tasks" rather than the "24/48" aggregate framing.

---

## Novel Insights

The most interesting unexplored implication raised by this work is whether ELMUR learns an emergent form of memory rehearsal — a mechanism by which the model learns to produce near-zero writes to the LRU slot targeting the oldest (cue-containing) entry, effectively preventing overwrite via the content of the cross-attention write rather than the slot selection mechanism. This would be a learned, implicit active maintenance strategy enabled by the relative bias in the tok2mem path, mirroring biological working memory rehearsal. This possibility is hinted at by the paper's own "conservative lower bound" caveat in Section 4 and by the rebuttal's mention of write suppression, but neither the paper nor the rebuttal provides evidence for or against it. If confirmed, it would transform a surprising empirical result into a meaningful theoretical insight about emergent memory management in bounded-memory transformers.

---

## Suggestions

1. Run a slot-index logging experiment on T-Maze: record which slot is selected by the LRU rule at each segment and whether the cue slot survives. Cross this with a λ sweep (0.0, 0.05, 0.1, 0.3, 0.5) to determine whether survival depends on λ or on learned write suppression.
2. Add a transparency statement to Section 5.1 explicitly noting that MIKASA-Robo and RATE are from the same research group.
3. Run the "No LRU" ablation on at least one POPGym puzzle task (Minesweeper or Concentration) to extend the component analysis beyond a single task.
4. Revise the abstract to foreground the puzzle-task gains (1.2 vs. 0.45 on 33 tasks) rather than the less informative "24/48" framing.

---

## Score and Decision

**Rebuttal impact assessment:**
- In-group concern: Downgraded from major to minor. The argument that ELMUR substantially outperforms in-group RATE on the in-group benchmark is genuinely persuasive. The independent POPGym and T-Maze results remain corroborating.
- T-Maze mechanistic gap: Unchanged as major. The rebuttal acknowledges the gap honestly, offers speculative mechanisms, but provides no confirmatory evidence. Promises slot-level analysis for revision — does not count.
- MoE weakness: Removed; the paper's framing was correctly efficiency-focused as the author demonstrates.
- Other minor/trivial concerns: Largely unresolved in the paper; revision promises don't count.

**Net effect:** The rebuttal resolves one trivial weakness (MoE), partially mitigates one major concern (in-group), and honestly acknowledges the remaining gaps. The mechanistic gap in the headline T-Maze result remains the most significant unresolved issue. The paper's independent empirical strengths (POPGym puzzle dominance, T-Maze extrapolation, efficiency) are confirmed from the paper itself. The rebuttal is competent and honest but does not materially change the paper's standing.

The score remains 6.0 — solid accept-level contribution, held back from 6.5 by the unexplained T-Maze mechanism and the in-group disclosure gap.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>