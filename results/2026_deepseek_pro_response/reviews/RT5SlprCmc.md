Now I have all the calibration data I need. Let me finalize.

**Round 1 bracket:** 5.0–6.5 (weaker than ETD at 6.75, stronger than SCR at 4.75)

**Round 2 narrowing:** BS-MPC at 5.50 (Accept, incremental), DCSL at 6.33 (Accept, more comprehensive evaluation), ETD at 6.75 (Accept, strongest). Our paper has more novelty than BS-MPC but less evaluation breadth than DCSL/ETD. The unspecified quasimetric and TDMadDist framing are real but addressable gaps. **Final: 6.0.**

---

## Summary

This paper proposes MadDist and TDMadDist, two algorithms for learning the Minimum Action Distance (MAD) between states from unlabeled state trajectories using asymmetric (quasimetric) distance functions. The key innovations are a scale-invariant loss formulation that prevents distant trajectory pairs from dominating optimization, native support for quasimetric distances to capture irreversible dynamics, a simple new quasimetric (d_simple), and a diverse benchmark suite with known ground-truth MAD. Results show MadDist outperforms QRL and Hilbert baselines on correlation metrics and a downstream planning task, achieving perfect success rates on four of six OGBench PointMaze environments.

## Strengths

- **Scale-invariant loss is a genuine, well-motivated improvement**: Equation 5 divides the squared error by (j − i), preventing state pairs far apart on a trajectory from dominating the optimization purely due to larger raw errors. This is a concrete advance over the unscaled MSE in Steccanella & Jonsson (2022), and the strong empirical results in Figure 3 are consistent with this design choice mattering.

- **Asymmetric modeling demonstrably improves representation quality**: In strongly asymmetric environments — KeyDoorGridWorld (irreversible key pickup) and CliffWalking (directional shortcut via falling) — MadDist significantly outperforms the symmetric Hilbert baseline on both Pearson correlation and Ratio CV (Figure 3). This directly validates the paper's core thesis that quasimetric distances are necessary for faithful MAD approximation in irreversible domains.

- **Diverse benchmark suite with known ground-truth MAD**: The paper constructs environments spanning discrete/continuous state spaces, stochastic/deterministic dynamics, symmetric/asymmetric transitions, and noisy observations (Section 7, lines 210–218), each with computable ground-truth MAD. This enables rigorous quantitative comparison that was missing from prior work, and the inclusion of Stitch and Giant OGBench variants tests compositionality and long-horizon reasoning.

- **Strong downstream planning results**: MadDist achieves 1.00 ± 0.00 success on four of six OGBench PointMaze environments (Table 1), including Stitch variants (requiring composition from disconnected trajectories) and Large/Giant variants (testing long horizons), decisively outperforming QRL and Hilbert baselines.

- **d_simple is a practical contribution**: The proposed quasimetric (Equation 3) is a weighted combination of max-ReLU and mean-ReLU, provably satisfying the triangle inequality and latent positive homogeneity (Appendix B). Its simplicity relative to IQE or Wide Norm makes it an attractive default choice.

## Weaknesses

### Fatal
None.

### Major

- **Quasimetric used in main results is never specified in the body**: Section 5 devotes substantial space to three quasimetrics (d_simple, d_WN, d_IQE), and d_simple is presented as a novel contribution. Yet nowhere in the main text — not in Section 7, nor in any figure or table caption — does the paper state which quasimetric produced the results in Figure 3 or Table 1. The reader is told (line 222) that Appendix E contains an ablation showing robustness to this choice, but the body should specify this basic experimental detail. Since d_simple is claimed as a contribution, readers cannot determine from the body alone whether the headline results were obtained with the novel quasimetric or with an existing one like IQE.

- **TDMadDist is presented as a co-equal contribution despite consistent underperformance**: The abstract and introduction treat TDMadDist as one of two novel algorithmic contributions. Yet TDMadDist underperforms MadDist on every metric in Figure 3 and is beaten by MadDist on 5 of 6 planning tasks in Table 1. The paper acknowledges this (line 226: "TDMadDist underperforms the MadDist and QRL algorithm") but merely restates the result without investigating why the bootstrapping mechanism fails to improve over direct supervised learning. Presenting TDMadDist as a co-equal contribution weakens the paper's contribution claims.

### Minor

- **Seed count inconsistency**: The main text (line 220) states "five independent runs" while Figure 3 captions (lines 230, 232, 238, 240) state "three random seeds." This factual inconsistency should be resolved.

- **Contrastive loss L_r (Eq. 6) has thin motivation**: L_r penalizes random state pairs whose learned distance falls below d_max, encouraging d_θ(s, s') ≥ d_max for arbitrary pairs. Two random states could legitimately be near each other; forcing them apart encodes an implicit assumption about state space sparsity. The paper provides no ablation or analysis of this term's contribution.

- **Abstract slightly overstates experimental scope**: The abstract claims MAD "naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping." The experiments demonstrate a planning task (Table 1) using learned distances as a heuristic, which is a form of goal-conditioned behavior but is not full integration into an RL algorithm or reward shaping, neither of which is demonstrated.

### Trivial
None.

## Nice-to-Haves

- Adding Laplacian-based or time-contrastive baselines (discussed in Section 2) would strengthen the empirical case that asymmetry matters, even though these methods are conceptually distinct from MAD approximation.
- Including NoisyGridWorld results in the main body (currently in Appendix F) would more prominently demonstrate robustness to observation noise.
- Specifying the architecture used for φ_θ (MLP size, layers) in the main text rather than only in Appendix D would improve readability.
- A sensitivity analysis for key hyperparameters (w_r, w_c, H_c, d_max) in the main text would aid reproducibility.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Garbled Equation 9**: The harsh critic noted Eq. 9 is "unintelligible" — this is a PDF parser artifact corrupting the LaTeX rendering, not an author error. Removed per formatting nitpick rule.

- **Zero-variance planning results are "suspicious"**: The harsh critic speculated that 1.00 ± 0.00 success rates across runs warrant explanation. If the planning procedure is deterministic given the learned distances and the distances are sufficiently accurate, perfect success is expected. This is speculative and not verifiable as a flaw from the paper text alone. Removed.

- **No wall-clock times or parameter counts reported**: Not a standard requirement for representation learning papers unless the paper makes explicit efficiency claims (which it does not). Moved to nice-to-have.

- **Missing environments (NoisyGridWorld, UMaze) from main results**: The paper explicitly states these are in Appendix F (line 222) and describes them in the body. Not a weakness — the paper is transparent about this.

- **"State representation methods" language in abstract is too broad**: The harsh critic flagged this as an overclaim, but in context "existing state representation methods" refers to the methods discussed in the paper's scope. The two baselines (QRL and Hilbert) represent the main relevant approaches: quasimetric learning and Hilbert-space MAD embedding. The language is reasonable in context.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the observation that the TDMadDist underperformance is interesting in its own right — the TD bootstrapping approach that works well for value functions may not transfer straightforwardly to distance learning — but the paper itself already acknowledges this gap.

## Suggestions

- State explicitly in Section 7 or in the Figure 3/Table 1 captions which quasimetric was used for the main results. If d_simple was used and Appendix E shows it matches or beats IQE/WN, bring that ablation result into the main text — it directly supports one of the paper's three claimed contributions.
- Either diagnose TDMadDist's underperformance (e.g., through ablations on the target network update rate β, the horizon of the bootstrap, or the quality of the 1-step target) or reframe the paper around MadDist as the primary contribution, with TDMadDist as an instructive extension or negative result.
- Resolve the seed count inconsistency between the text (five runs) and Figure 3 captions (three seeds).
- Include an ablation of the contrastive loss L_r (setting w_r = 0) to justify its inclusion, or provide a clearer motivation for why encouraging arbitrary state pairs to be separated is beneficial for MAD learning.

## Score and Decision

**Calibration anchors considered:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| State Chrono Representation (SCR) | oEzY6fRUMH | 4.75 | R1 | Our paper has stronger evaluation, better motivated contributions, more coherent methodology |
| BS-MPC | F07ic7huE3 | 5.50 | R2 | Our paper has more novelty; BS-MPC was criticized as incremental |
| Dynamic Contrastive Skill Learning (DCSL) | 8egnwady4b | 6.33 | R2 | DCSL has more comprehensive evaluation; our paper has cleaner, better-supported core contributions |
| Episodic Novelty Through Temporal Distance (ETD) | I7DeajDEx7 | 6.75 | R1/R2 | ETD has more complete evaluation with direct RL integration; our paper has narrower scope |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowed to:** 5.5–6.0. The paper has genuine contributions (scale-invariant loss, quasimetric approach, benchmark suite) supported by strong results, but is held back by two addressable major weaknesses (unspecified quasimetric, TDMadDist framing) and several minor presentation gaps. These weaknesses do not invalidate the core MadDist contribution but do prevent the paper from being a clear accept. A rebuttal could address the major issues straightforwardly.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>