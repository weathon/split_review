## Summary

The paper proposes **Guided Hybrid Policy Optimization (GHPO)**, a framework for addressing reward sparsity in Reinforcement Learning with Verifiable Rewards (RLVR) for LLMs. The core idea is to detect "difficult" samples online by checking whether all G sampled responses in a GRPO group receive zero reward, and then adaptively augmenting the query with partial ground-truth solution traces before resampling. This creates a dynamic curriculum that blends on-policy RL for solvable problems with guided imitation for otherwise intractable ones, with a multi-stage hint ratio schedule and an optional cold-start phase. Experiments on Qwen2.5-7B (Base and Math) demonstrate ~5% average improvement over GRPO across six math benchmarks.

---

## Strengths

- **Well-identified and quantified problem.** The observation that Qwen2.5-7B-Instruct fails 52% of NuminaMath-1.5 problems provides concrete, dataset-level motivation for the capacity-difficulty mismatch claim, and Figure 3 shows this problem persists (60%+ difficult queries) throughout training—not just at initialization.

- **Lightweight difficulty detection.** The method requires no additional model, no external scoring oracle, and no offline preprocessing: it reuses the exact group rollouts already computed by GRPO, adding minimal overhead. This practical appeal is a genuine strength over alternatives like LUFFY, which needs off-policy demonstrations, or hard-coded curriculum partitions.

- **Consistent empirical gains across settings.** GHPO outperforms GRPO on five of six benchmarks in both the Math3to5 and NuminaMath-S settings, and the gains transfer to a stronger base model (Qwen2.5-Math-7B), lending credibility that the improvement is not dataset-specific noise.

- **Training dynamics corroborate the narrative.** The gradient norm curves (Figure 4d) showing GHPO's smaller, more stable norms provide mechanistic evidence for the claimed training stability benefit, going beyond simple accuracy numbers.

- **Ablation against static-hint curriculum learning.** Comparing GHPO against GRPO-CL-H0.5 (fixed 50% hint ratio + curriculum learning) directly tests whether adaptive guidance is necessary, and the result favors GHPO, isolating the contribution of dynamic difficulty detection.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with LUFFY (the closest prior work).** LUFFY [Yan et al. 2025] explicitly combines on-policy RL with off-policy imitation demonstrations using a hybrid approach conceptually identical to GHPO's goal of balancing exploration and guided learning. The authors cite LUFFY in the related work but do not include it as a baseline. Without this comparison, it is impossible to assess how much of GHPO's gain is attributable to the adaptive switching mechanism versus simply mixing RL with any form of imitation guidance.

2. **The implicit SFT problem is not addressed.** Figure 3 shows that ~60% of problems persistently receive hints across training. When ω is large (most of the solution is provided), the augmented query effectively reveals the answer, and RL on the augmented prompt degenerates toward SFT on the ground-truth trace. The authors' own cited work ("SFT memorizes, RL generalizes") motivates the RL approach precisely because SFT lacks generalization. The paper does not ablate against simply running SFT on ground-truth traces for the hard problems—the comparison most directly needed to validate that GHPO's RL formulation over augmented queries genuinely provides the generalization benefits claimed over SFT.

3. **Core algorithmic component (multi-stage hint ratio schedule) is delegated entirely to a stripped appendix.** Section 3.4 describes the adaptive hint ratio ω as the key contribution for "consistent learning for policy improvement" but provides no schedule, formula, or intuition in the main text. The hint extraction template (Appendix B.1–B.2) is similarly unavailable. Readers cannot evaluate or reproduce the method from the main paper alone. (Noting parser-stripped appendix per instructions, but the main text provides insufficient description even by standalone standards.)

### Minor

1. **No variance estimates on small benchmarks.** AIME2024 has ~30 problems; AMC2023 has ~40 problems. The reported differences (e.g., GRPO: 0.131 vs. GHPO: 0.133 on AIME24 in Table 1) are within single-problem noise. Reporting confidence intervals or standard deviations across multiple seeds is essential for interpreting these results.

2. **High volatility in difficulty detection (Figure 3) is unexplained.** The proportion of detected difficult problems oscillates between 0.2 and 0.9 within short training windows. This suggests strong batch-composition sensitivity. The paper does not discuss whether this volatility introduces gradient-distribution instability or how it interacts with the multi-stage ω schedule.

3. **Computational overhead of double rollout is not analyzed.** For hard samples, GHPO first samples G responses to detect difficulty, then samples another G responses on the augmented query. The effective compute per hard sample is roughly 2×. No wall-clock time, throughput, or GPU-hour comparison against GRPO is provided.

4. **Domain generalization is untested.** All experiments are in mathematics. The introduction claims general applicability to RLVR, but no code, programming, or scientific reasoning experiments are included.

### Trivial

- "Assumption 1" is formally styled as a mathematical assumption with heavy notation but is empirically validated rather than proven; the formal framing adds confusion without adding rigor.

---

## Nice-to-Haves

- A comparison against DAPO's dynamic sampling filter (which discards 0-accuracy and 1-accuracy samples) on the same benchmarks would clarify whether GHPO's advantage over DAPO is data efficiency (uses all data) vs. guidance quality.
- An ablation varying the cold-start length N would help practitioners tune the method.
- Qualitative examples showing how sampled responses with and without hints differ in reasoning structure would strengthen the narrative about GHPO enabling "more elaborate reasoning."

---

## Novel Insights

GHPO surfaces a practically important observation: reward sparsity in RLVR is not a dataset property that can be fixed at preprocessing time—it is persistently high (≥60% of samples remain at zero reward across 160+ training steps) because model capability and dataset difficulty co-evolve. This motivates *online* difficulty detection rather than static curriculum partitioning, and the finding that static curriculum learning with fixed hints (GRPO-CL-H0.5) underperforms adaptive detection by ~2% supports this. The gradient norm analysis providing mechanistic evidence that guided imitation for hard samples actually stabilizes policy updates—rather than destabilizing them through distributional shift—is a useful empirical finding for the field. However, the core hybrid RL+imitation idea is shared with LUFFY, and the "provide hints for hard problems" intuition is broadly anticipated in the curriculum learning literature, limiting the degree to which these insights are fully novel.

---

## Suggestions

- Include LUFFY as a direct baseline, ideally using the same training data and evaluation benchmarks.
- Add an ablation comparing GHPO against SFT-only training on hard-problem ground-truth traces (to isolate whether the RL component on augmented queries provides generalization benefits beyond SFT).
- Move the multi-stage hint ratio schedule description into the main text with at least a table or figure, so the algorithm is self-contained.
- Report results with multiple seeds or with confidence intervals, particularly for small benchmarks like AIME24 and AMC23.

---

## Score and Decision

GHPO is a practically motivated, lightweight method that shows consistent improvements over GRPO across multiple settings. The core insight—detecting zero-reward batches online and injecting solution traces—is simple and effective. However, the missing comparison with LUFFY (the most directly relevant prior method), the unaddressed concern that 60%+ of training time may devolve into implicit SFT (without a direct SFT ablation), and the incomplete description of the hint ratio schedule in the main text are significant issues that prevent confident acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>