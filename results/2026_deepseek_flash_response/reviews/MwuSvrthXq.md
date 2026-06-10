Now let me write the final review.

## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. Two main contributions: (1) a weighted cross-attention (WeCA) layer that integrates compatibility coefficients *outside* softmax to handle variable-size pool environments, and (2) a theoretical analysis of the list-scheduling optimality gap with a skip-action mechanism designed to close it. Results are reported on TPC-H and Computation Graphs benchmarks.

## Strengths

1. **Well-motivated WeCA layer with outside-softmax compatibility integration (Section 3.1, Eq. 3).** The paper provides a concrete example showing why placing compatibility coefficients inside softmax loses information about the breadth of compatibility across pools (lines 125–126). The ablation (Table 3) confirms this design choice is empirically consequential: outside-softmax achieves 14.0% improvement over Tetris on TPC-H-30 vs. only 10.5% for the inside variant.

2. **Theoretical analysis of the list-scheduling optimality gap (Section 4, Theorem 1).** The paper formally analyzes why list scheduling cannot guarantee optimal solutions (TS_list is not surjective) and constructs a generation map with skip actions satisfying Assumption 1. Theorem 1 proves Algorithm 1 assigns positive probability to optimal solutions and that without skip this guarantee fails for some instances. This is a legitimate conceptual contribution that goes beyond prior neural schedulers.

3. **Credible generalization experiments (Figure 2).** WeCAN maintains 20.4% improvement over heuristics with more pools (vs. One-Shot's 9.2%) and 6.7% with more pool types (vs. One-Shot's 0.9%). This directly supports the claim that the WeCA layer's attention-based design delivers adaptability advantages over fixed-size embedding approaches.

## Weaknesses

### Major

1. **Missing comparison against heterogeneous-aware neural baselines.** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) in the introduction (lines 36–48) as methods that handle heterogeneous environments with compatibility coefficients, yet never compares against any of them empirically. The main neural baseline, One-Shot (Jeon et al., 2023), is acknowledged by the paper itself (lines 28–31) as not considering compatibility coefficients or pool allocation — i.e., it was not designed for this problem setting. PPO-BiHyb (the only heterogeneous-aware neural baseline) uses beam search and is thus a structurally different approach. Without comparisons to methods that address the same problem formulation, the paper's claim of outperforming "state-of-the-art methods" is not fully supported. The improvements (7.7–9.5%) over One-Shot likely reflect that One-Shot cannot handle the problem's core difficulty, rather than demonstrating WeCAN's specific architectural superiority.

### Minor

1. **Skip-action evaluation is thin.** The skip mechanism is positioned as a central contribution (Contribution 3, Theorem 1) with theoretical weight, but the dedicated experiments test only a 1% heavy-task replacement rate (line 310). No "without-skip" ablation row appears in Table 3, which would be the most direct test. Figure 3 has labeling issues: the legend shows "WeCAN-S(256)" appearing twice (columns 0 and 3 of the table) alongside "PRO-BALM" — a term never defined in the main text — making the figure difficult to interpret.

2. **Selective variance reporting.** Tables 1 and 2 report standard deviations only for sampling-mode rows (WeCAN-S(64), WeCAN-S(256), One-Shot-S(256)). The greedy results (WeCAN-Greedy and all heuristic baselines) are reported as point estimates without variance, even though the table caption states "standard deviation among random seed." Since neural methods have stochasticity from training seeds, the reader cannot assess whether the greedy improvements are statistically significant.

3. **Unsubstantiated clustering claim.** The paper states (lines 210–211) that the skip-action design "clusters most poor solutions in the high-u_a, high-u_c region" without any analysis (theoretical or empirical) to support this claim. This claim is central to the argument that skip actions do not increase training variance, yet it is asserted without evidence.

4. **Heuristic skip-score formula.** The specific form $u_a(1 - k/(2n))^{u_b} + u_c$ (line 145) is presented without justification for why this particular functional form was chosen. The paper says it "prevents the skip action from overly prioritized" but does not clarify whether any decreasing function would suffice or whether this specific form has provable properties.

### Trivial

1. Only 10 test problems used in the ablation study (line 308), which is a small evaluation set given standard deviations ranging from 7 to 358 in Table 3.
2. No runtime overhead measurement for skip vs. no-skip, despite the paper claiming skip preserves computational efficiency.

## Nice-to-Haves

- Include at least one heterogeneous-aware neural scheduler (Zhou et al. 2022, Wang et al. 2025, or similar) in the baseline comparison.
- Extend heavy-task experiments to higher proportions (e.g., 5%, 10%, 20%) to demonstrate the monotonic trend the theory predicts.
- Add a "WeCAN without skip" row to Table 3's ablation.

## Removed Points

- **Harsh critic's point about missing appendix details:** Removed because the parser strips appendices from all papers; training details, non-auto-regressive decoder comparisons, and network specifics exist in the original submission's appendices.
- **Harsh critic's point about "fairness" of One-Shot comparison:** Weakened from "structurally unfair" to the verified claim that missing heterogeneous-aware baselines is the real issue. Comparing against One-Shot is standard practice; the problem is the omission of more relevant baselines, not the inclusion of One-Shot.
- **Criticism about theoretical guarantee vs. practical method:** The paper's Theorem 1(iv) clearly states "there exist scores" — the existential qualifier is present. The introduction's framing is somewhat ambitious but the theorem itself is precise. Moved to a minor presentation note rather than a separate weakness.
- **Strength Finder's generic strengths** (e.g., "state-of-the-art empirical results"): Weakened because the missing heterogeneous-aware baselines partially undermine the "state-of-the-art" claim. The results against heuristics and PPO-BiHyb are still valid evidence.
- **Strength that conflicts with weakness #1:** The Strength Finder's claim that WeCAN-skip experiments "provide supporting evidence" is partially retained but tempered by the thinness identified in Minor weakness #1.
- **Criticism about missing limitations section:** This is a style preference, not a substantive weakness.
- **Criticism about training details absent from main text:** Parser issue; appendices are stripped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Replace or supplement the One-Shot comparison with at least one heterogeneous-aware neural scheduler (e.g., Zhou et al. 2022 or Wang et al. 2025) that also handles compatibility coefficients. Without this, the paper's central claim — that WeCAN's architectural innovations are superior — is not adequately tested.

2. Strengthen skip-action evidence by (a) adding a "WeCAN without skip" row to the main ablation table, (b) testing heavy-task proportions at multiple levels (1%, 5%, 10%, 20%) rather than just 1%, and (c) fixing the duplicate label and undefined "PRO-BALM" in Figure 3.

3. Report standard deviations for all entries in Tables 1 and 2, including greedy results, or explain why they are not applicable.

## Calibration Anchors

All anchors from the deepreview_13k_calibration corpus:

**Round 1 (Bracketing) — score bands:**
- Low band (<3.5): bntJK4NyIW (2.00), ArJikvI6xo (3.40), 10eQ4Cfh8p (3.00), 2HN97iDvHz (3.00) — all clearly weaker than the paper.
- Middle band (3.5–7.5): daVCPIBCtQ (4.33), b9aCXHhdbv (4.50), Cs6MrbFuMq (6.00), Txxz9fBPcJ (6.00) — the 4.33–4.50 anchors are weaker; the 6.00 anchors are stronger.
- High band (>7.5): 9pW2J49flQ (8.00), 7BLXhmWvwF (8.00), stUKwWBuBm (8.00), 6PbvbLyqT6 (8.00) — clearly stronger than the paper.

**Round 2 (Narrowing, 4.5–6.5):**
- AloCXPpq54 (6.00, Accept): HRL for combinatorial optimization. Stronger evaluation and cleaner framing. Our paper is slightly weaker.
- 8WtBrv2k2b (5.00, Reject): RL for quantum resource scheduling. Similar mixed-review profile; our paper has more novel architecture but comparable evaluation gaps.
- Dgc5RWZwTR (4.75, Reject): Multi-task neural solver. Weaker than our paper.
- TbTJJNjumY (6.25, Accept): Cross-attention for VRP. Stronger evaluation and appropriate baselines. Our paper is weaker.
- DhH3LbA6F6 (6.00, Accept): RL with combinatorial actions for restless bandits. Stronger theoretical framing and evaluation. Our paper is weaker.
- DKfcxPxunu (5.75, Reject): Multi-task learning for routing. Comparable to our paper in quality but different domain.

**Round 1 bracket:** 4.5–6.5

**Narrowing:** Our paper is stronger than the 4.33–5.00 anchors (DRL-PP 4.50, DyGNeX 4.33, quantum scheduling 5.00) and comparable to the 5.75 anchor (multi-task routing, rejected). It is weaker than the 6.00–6.25 anchors (VRP cross-attention 6.25 accepted, HRL 6.00 accepted, restless bandits 6.00 accepted). The missing baselines issue and thin skip-action evidence are the primary reasons it falls below acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>