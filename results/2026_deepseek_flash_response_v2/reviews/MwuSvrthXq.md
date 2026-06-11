## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. Its core contributions are: (1) a weighted cross-attention (WeCA) layer that places compatibility coefficients outside softmax normalization, enabling the architecture to handle varying environment sizes without fixed-size embeddings; (2) a skip-action mechanism integrated into a single-pass generation map, with formal guarantees (Theorem 1) that it closes the surjectivity gap inherent in list scheduling; and (3) the LDDGNN for encoding dependencies via longest directed distance. Empirical results on TPC-H and Computation Graphs datasets show up to 18.1% improvement over heuristics and 7.7% over the best neural baseline, with near-heuristic runtime.

## Strengths

1. **The WeCA design with compatibility outside softmax is novel and well-motivated.** Section 3.1 gives a concrete counterexample showing that inside-softmax placement renders tasks with identical attributes but different compatibility profiles indistinguishable. This is not just a theoretical concern — the ablation (Table 3) empirically confirms it: WeCA-inside+LDDGNN achieves only 10.5% improvement vs. the full WeCA+LDDGNN's 14.0% on TPC-H-30, and the gap widens on TPC-H-50 (9.5% vs. 11.4%).

2. **Theorem 1 provides formal guarantees beyond empirical demonstration.** The theorem proves termination within 2n steps, positive probability assigned to optimal solutions, the necessity of skip actions for surjectivity across all instances, and the existence of scores enabling optimal greedy selection. This is a genuinely theoretical contribution showing that the generation map with skip actions covers the optimal solution space, whereas list scheduling alone cannot.

3. **Single-pass efficiency is convincingly validated.** Table 1 reports WeCAN-Greedy at 0.15–1.72s on TPC-H, competitive with HEFT (0.18–1.86s) and orders of magnitude faster than the multi-round neural baseline PPO-BiHyb (20.48–179.19s). This directly supports the claim of near-heuristic inference speed.

4. **Environment fluctuation experiments (Figure 2) demonstrate generalization.** Under fixed training, WeCAN-S(256) achieves 20.4% improvement (more pools) vs. OneShot-S(256)'s 9.2%, and 19.3% (more task types) vs. 10.2%. This supports the claim that WeCA's lack of fixed-size constraints enables cross-configuration adaptability.

5. **The ablation study (Table 3) systematically isolates each component.** Every variant replacing either WeCA (inside, decoder-only, final-only) or LDDGNN (GAT forward, GAT bidirectional) produces strictly worse makespan, with a controlled degradation chain from 14.0% down to 0.5% (and even −4.2% for WeCA-final-only). Each component's role is verifiable.

## Weaknesses

### Fatal
None.

### Major
1. **The skip action's contribution is not disentangled from the architecture on standard datasets.** On the main TPC-H and Computation Graphs benchmarks (Tables 1, 2), WeCAN is evaluated only with skip actions enabled. The ablation study (Table 3) tests architectural components (WeCA placement, GNN type) but does not include a no-skip variant. The skip-action benefit is demonstrated only on the artificial heavy-task setup (Figure 3, 1% heavy tasks). Consequently, a reader cannot determine how much of the reported 7–10% improvement over One-Shot comes from the WeCA+LDDGNN architecture versus the skip action on standard instances. Since the paper positions the skip action as a major contribution (contribution 3 in the introduction), this is a significant experimental gap that should be addressed with a "WeCAN without skip" baseline on the original datasets.

2. **The PRO-BALM baseline in Figure 3 is undefined in the main text.** The baselines section (Section 5.1) lists CP, SFT, MOPNR, Tetris, HEFT, PPO-BiHyb, and One-Shot. PRO-BALM appears only in Figure 3's heavy-task experiment without a definition, citation, or contextualization. A baseline appearing in a main figure should be referenced in the main text's baselines section. (It may be defined in the stripped appendix, but the main text should at least cite the description.)

### Minor
1. **The non-auto-regressive decoder choice is acknowledged but under-justified in the main text.** The paper states (line 137) that it uses a non-auto-regressive decoder "for improving scalability" and defers a comparison to Appendix B (stripped). However, the choice has significant implications — scores are computed once upfront, meaning the scheduler cannot re-evaluate priorities based on scheduling progress. A brief intuition in the main text about why this choice does not hurt solution quality would strengthen the paper.

2. **The skip score formula's functional form lacks justification.** The formula \(u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c\) uses a polynomial decay in \(k\). The paper does not motivate why polynomial rather than exponential decay, or why \(2n\) is the normalization factor. While the formula appears to work empirically, a brief rationale or ablation over different decay functions would strengthen confidence in this design choice.

3. **No small-instance optimality gap quantification.** Section 4 analyzes the optimality gap theoretically, and Theorem 1 shows skip actions enable surjectivity, but there is no small-scale experiment (e.g., 10–20 tasks with MILP-computed optimal solutions) to quantify how close WeCAN (with or without skip) actually gets to optimal. Even a limited study would calibrate the practical significance of the theoretical gap.

### Trivial
- The extracted text contains duplicated figure captions (lines 105–111). This is likely a PDF parser artifact rather than an author error.

## Nice-to-Haves
- A "WeCAN without skip" baseline on the standard TPC-H and Computation Graphs datasets would directly measure the skip action's contribution on non-heavy-task instances.
- Training convergence curves (reward vs. episode) would help validate that REINFORCE reliably drives the policy toward favorable score regions.
- Clarifying the relationship to One-Shot (Jeon et al., 2023) — noting that WeCAN extends One-Shot with (i) a WeCA+LDDGNN encoder and (ii) skip actions during decoding — would help readers understand the delta.
- A brief ablation over different skip score decay functions would strengthen confidence in the chosen formula.

## Removed Points
These points were flagged by reviewers but are removed from the main review for the reasons stated:
- **"Theorem 1(iv) is only an existence guarantee, not a learnability guarantee"** — The paper is precise: it says "there exist scores... enabling optimal solution." It does not claim RL guarantees finding them. The paper also discusses variance challenges (Section 4.2). This is a correct statement of what Theorem 1 proves, not a weakness.
- **"The \(\rho\) hyperparameter is never explained or used"** — \(\rho(v)\) is used as a task attribute vector in the WeCA encoder (line 117). It is part of the input representation.
- **"Tetris as reference inflates improvement percentages on TPC-H-100"** — The ablation (Table 3) is only on TPC-H-30 and TPC-H-50, where Tetris is indeed the best heuristic. The main results (Table 1) correctly compare against per-dataset best heuristics.
- **"Missing training hyperparameters in main text"** — Training details are referenced to Appendices D, E, and H, which is standard practice for ML papers.
- **Pure formatting/style nitpicks** — Removed as parser artifacts / non-substantive.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a weakness or strength that the paper's own framing misses, though the missing skip-ablation experiment is a genuine gap in the evaluation that the paper does not acknowledge.

## Suggestions
1. Add a "WeCAN without skip" baseline to Tables 1 and 2 so readers can attribute gains to the architecture versus the skip action on standard instances.
2. Define PRO-BALM in the main text (or at least reference its appendix description).
3. Add a brief main-text explanation of why the non-auto-regressive decoder is sufficient, or when it might fail relative to an auto-regressive variant.
4. Include a small-scale optimality gap analysis using MILP on tiny instances (10–20 tasks) to ground the theoretical claims empirically.
5. Provide a brief motivation or ablation for the skip score decay function.

**Calibration anchors for score determination:**

*Round 1 (Bracketing):*
- `10eQ4Cfh8p` — FJSP RL (avg 3.00). Significantly weaker: poorer evaluation, unclear contributions, missing baselines. Our paper is substantially stronger.
- `b9aCXHhdbv` — DRL-PP (avg 4.50). Weaker: limited evaluation, no formal theory, missing ablation. Our paper is clearly above.
- `8WtBrv2k2b` — Quantum resource scheduling RL (avg 5.00). Comparable domain (RL scheduling) but our paper has clearer methodology and stronger theoretical grounding.
- `jBYQAtzp5Z` — Scheduling with predictions (avg 6.80). Stronger on theory but is a pure theory paper in a different subfield. Hard to compare directly.
- `7BLXhmWvwF` / `9pW2J49flQ` — Robotics/LTL papers (avg 8.00). Different domain, higher standard. Our paper is not at this level.

*Round 2 (Narrowing within bracket 5.0–7.0):*
- `Cs6MrbFuMq` — HexGen-2 (avg 6.00, scores 5,6,8,5). Heterogeneous scheduling for LLM inference. Similar to our paper in having a novel formulation with one notable evaluation gap (similar missing ablation). Our paper has better theoretical component and ablation studies but a similar evaluation gap.
- `aKivEaIbN2` — NASGraph (avg 4.67, scores 3,6,5). Lighter contribution. Our paper is stronger.

**Final score:** 6.0. The paper has a genuinely novel architectural contribution (WeCA with outside-softmax compatibility), formal theoretical guarantees, and convincing empirical results on realistic benchmarks. However, one of its claimed contributions (the skip action) lacks a direct ablation on standard datasets, which prevents full validation of the attribution of gains. This is a significant but not fatal gap — the core WeCA architecture contribution stands independently, and the overall method outperforms strong baselines. The paper is a solid contribution above borderline (5.0) but not at the strong accept level (7.0+).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>