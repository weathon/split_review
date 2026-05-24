Now I have all the data I need. Let me compile the final review.

**Round 1 bracket**: Between 5 and 7 (based on bracketing search: middle-band anchors GAA-PtrNet 4.50, DEFT 5.00, DOPPLER 4.50; clearly above all of these in terms of contribution depth and empirical thoroughness)

**Round 2 narrowing**: Compared against RLAF (6.50, Accept Poster) and ATLAS (6.40, Accept Poster). The paper is comparable to RLAF — RLAF has a cleaner paradigm but WeCAN has stronger theory and more thorough ablations. The paper is stronger than GAA-PtrNet (4.50, Reject), DEFT (5.00, Accept Poster), and DOPPLER (4.50, Accept Poster).

**Final score**: 6.5 — a solid contribution with well-supported claims, clear architectural novelty, formal theory, and thorough experiments, held back from the 7+ range by minor weaknesses (limited neural baselines, skip-score design could be better justified) that do not threaten the core claims.

Now writing the review.

Let me also think about what "removed points" I need to document:

1. Harsh critic's "gap between theory and practice" - I'm keeping this as Minor (reframed), not removing it entirely.

2. "Missing appendix proofs" - REMOVE per rules about missing appendix.

3. "Missing related works" - REMOVE per rules.

4. The format/style nitpicks - REMOVE.

Let me also check: "The theoretical analysis of the optimality gap of list scheduling is conceptually sound... but the theorem statements rely on the appendix for proof. The paper should at least sketch the proof steps." - This is about missing proof in appendix. Per rules: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references." So I should remove this.

Actually, re-reading more carefully, the critic says "The paper should at least sketch the proof steps in the main text to make the argument self-contained." This is slightly different - it's about the main text lacking proof sketch, not about the appendix being missing. But it's still about wanting proof details that were deferred to an appendix. I'll treat this as removed per the rules, or keep it as a very minor suggestion.

Let me just write the review now.## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. The framework introduces a weighted cross-attention (WeCA) layer that integrates compatibility coefficients as an attention bias outside softmax, enabling adaptable encoding across varying numbers of pools and task types. It also provides a theoretical analysis of the optimality gap in list-scheduling-based methods and introduces a skip-action mechanism in the single-pass setting that, together with a longest-directed-distance GNN (LDDGNN) for dependencies, closes this gap while maintaining computational efficiency. Experiments on TPC-H and Computation Graphs benchmarks show consistent makespan improvements over heuristic and neural baselines, with particularly strong gains on heavy-task and environment-fluctuation scenarios.

## Strengths

- **Weighted cross-attention layer provides a principled solution to heterogeneous adaptability.** The WeCA layer (Section 3.1, Equation 3) places compatibility coefficients as a diagonal bias outside the softmax, which the paper convincingly argues preserves fine-grained information about a task's overall compatibility profile (e.g., distinguishing two otherwise identical tasks that differ in how many pools they are compatible with). This design is validated in Figure 2, where WeCAN achieves 20.4% improvement over the best heuristics when the number of pools changes, versus 9.2% for One-Shot.

- **Formal theoretical analysis of list-scheduling's optimality gap with a concrete solution.** Section 4 proves (Theorems 1 and 2) that list scheduling cannot guarantee optimal solutions, establishes a criterion for surjectivity of generation maps, and shows that the proposed skip-action mechanism in Algorithm 1 restores surjectivity while preserving single-pass inference. Figure 3 provides direct empirical validation: on TPC-H-30-heavy, WeCAN with skip achieves 8.3% improvement over HEFT, while the non-skip variant achieves only 2.6%.

- **Strong empirical performance with competitive inference speed.** On TPC-H-100 (Table 1), WeCAN-Greedy achieves a makespan of 62,587 (vs. best heuristic 70,137 and best neural baseline 66,173) with a runtime of 1.72s — lower than One-Shot-S(256) (9.85s) and orders of magnitude faster than PPO-BiHyb (179.19s). Similar patterns hold on Computation Graphs (Table 2) across Erdős-Rényi, Layer, and Stochastic Block graphs.

- **Thorough ablation studies confirm the necessity of each architectural component.** Table 3 systematically ablates WeCA placement (outside vs. inside softmax, decoder-only variants) and LDDGNN (vs. GAT), showing each component contributes meaningfully. On TPC-H-30, the full model achieves 14.0% improvement over Tetris, while removing WeCA layers entirely yields only 0.5%.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited neural baselines reduce the strength of the "state-of-the-art" claim.** The paper compares against only two neural schedulers: PPO-BiHyb (2021) and One-Shot (2023). While One-Shot is the natural single-pass competitor and PPO-BiHyb is a well-known prior RL method, the paper does not include any of the more recent neural schedulers it cites in the related work (e.g., Zhou et al. 2022, Zhadan et al. 2023, Wang et al. 2025). The paper would benefit from either including at least one additional recent baseline or providing explicit justification (e.g., code unavailability, task-setting mismatch) for the omissions. The headline claim of "outperforming state-of-the-art methods" is empirically supported against the included baselines, but the set is narrow enough to be a concern.

- **The skip-action score formula is pragmatically motivated but undersupported.** The formula $u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c$ is introduced without comparison to simpler alternatives (e.g., a learned constant per-instance, or a lightweight per-step MLP that activates only when skip is considered). The paper's ablation (Figure 3) compares skip vs. no-skip, which validates the mechanism's importance, but does not isolate whether the specific functional form matters. The design rationale ("prevents the skip action from being overly prioritized") is reasonable but would be stronger with empirical justification that this particular form outperforms alternatives.

- **The theoretical guarantee of optimality (Theorem 1(iv)) is an existence result, not a learnability guarantee.** The theorem states that *there exist scores* enabling greedy optimal selection, but does not analyze whether REINFORCE training can reliably discover such scores. The paper acknowledges that the skip action introduces variance and claims that clustering poor solutions in the high-$u_a$, high-$u_c$ region reduces training variance, but provides no empirical analysis of training stability, return variance, or convergence behavior under the skip mechanism. These issues are common to most theory-grounded RL papers and do not invalidate the contribution, but the paper would benefit from acknowledging this gap between representational capacity and empirical learnability.

### Trivial

- PPO-BiHyb results are reported without standard deviation (Tables 1–2), while One-Shot and WeCAN are reported with multiple seeds. Clarifying whether PPO-BiHyb is deterministic under its beam search or whether variance was simply omitted would improve reproducibility.
- The TPC-H dataset modifications (random memory constraints and task types) are described as deferred to Appendix D (removed). A brief summary of the distribution of these modifications (number of task types, compatibility coefficient generation) in the main text would aid reproducibility.

## Nice-to-Haves

- An ablation comparing the proposed skip score formula against simpler alternatives (constant per-instance score, lightweight MLP per step) would strengthen the methodological contribution.
- A brief limitations section acknowledging that the method assumes a static environment (pools and tasks known at start) and does not handle dynamic arrivals would improve completeness.
- A few more sentences of intuition about the LDDGNN attention mask and bias construction in the main text (rather than deferring entirely to Appendix G) would improve readability.

## Removed Points
These points are flagged to be removed per filtering rules; treat them with caution.

- *"The paper should sketch the proof steps in the main text"* — Removed per rule about missing appendix content (proofs are in Appendix A, which is stripped by the parser).
- *"The paper should add more related works"* — Removed per rule on missing related works; the reviewer cannot confirm which works exist or are relevant.
- *"The experiments should include variance for PPO-BiHyb"* — Moved to Trivial (see above) because PPO-BiHyb uses beam search which is effectively deterministic; this is a presentation clarification rather than an evidential gap.
- *Formatting/presentation nitpicks* (typos, figure sizing, notation) — Removed per rules as parser artifacts or style points with no bearing on soundness.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. Add at least one more recent neural baseline (e.g., from the cited Zhou et al. 2022 or Wang et al. 2025) or provide explicit justification for why it cannot be included.
2. Add a brief ablation comparing the proposed skip score formula against one or two simpler skip-score strategies (e.g., a learned constant per instance, or a lightweight MLP that runs only when a skip is considered).
3. Add a short paragraph in the main text summarizing the LDDGNN attention mask construction, so the reader can follow the architectural intuition without consulting the appendix.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| GAA-PtrNet (UbWy2QVmke) | 4.50 | R1 middle | WeCAN is clearly stronger — better theory, ablations, and architecture motivation |
| DEFT (yVFOdLjd7V) | 5.00 | R1 middle | WeCAN is stronger — DEFT was criticized for missing ablations; WeCAN has thorough ablations |
| DOPPLER (OQQK8gMC5H) | 4.50 | R1 middle | WeCAN is stronger — cleaner methodology and more comprehensive evaluation |
| RLAF (NfWrLOKnfk) | 6.50 | R2 narrow | Comparable — RLAF has a cleaner paradigm but WeCAN has stronger theory and more thorough ablations |
| ATLAS (QBvxXzHdZx) | 6.40 | R2 narrow | Different contribution type (dataset paper); not directly comparable |
| Foundation Models for Industrial Scheduling (qRjLjYrvMi) | 6.00 | R2 narrow | WeCAN is stronger — more focused contribution and cleaner evaluation |
| DASH (bMi5ssfPoM) | 6.00 | R2 narrow | Different problem (LLM attention scheduling); not directly comparable |

**Round 1 bracket**: [5, 7] — the paper is clearly above the 4.5 anchors (GAA-PtrNet, DEFT, DOPPLER) in contribution depth and empirical rigor.

**Round 2 narrowing**: Compared against RLAF (6.50) and ATLAS (6.40). The paper is comparable to RLAF — slightly weaker on paradigm novelty but slightly stronger on theory depth and ablation thoroughness. This places it at 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>