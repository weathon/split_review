- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

The paper proposes ARAM, a framework for action-constrained RL that combines (1) acceptance-rejection sampling to enforce per-step action constraints without solving QPs, and (2) an augmented MDP (AUTO-MDP) with a penalty for infeasible actions to improve the acceptance rate over training. ARAM is implemented using multi-objective SAC to avoid tuning the penalty weight. Experiments on MuJoCo locomotion and resource allocation benchmarks show ARAM reduces QP operations by 2–5 orders of magnitude compared to projection-based methods while achieving competitive returns and near-perfect valid action rates.

## Strengths

- **Massive reduction in costly QP operations**: Figure 4 (log-scale) shows ARAM's cumulative QP operations are 2–5 orders of magnitude lower than DPre+, SPre+, and NFWPO across all environments (HalfCheetah, Ant, NSFnet, BSS5z). This directly supports the paper's central claim of removing the QP bottleneck.

- **Simultaneously achieves high valid action rate and low inference time**: Table 2 shows ARAM attains near-perfect valid action rates (0.98–1.0) in all domains, while Table 3 reports per-action inference time roughly one order of magnitude lower than every baseline. This is the key evidence that ARAM delivers efficient constraint satisfaction without sacrificing feasibility.

- **Faster wall-clock-time learning**: Figure 3 learning curves show ARAM reaches higher evaluation returns earlier in wall-clock time than all baselines, especially against QP-heavy methods. This confirms that low per-step overhead translates into practical convergence speed.

- **MORL ablation validates the multi-objective design**: Figure 5 shows the MORL implementation achieves both high forward reward and high valid action rate simultaneously, whereas single-objective variants with fixed preferences fail on at least one metric. This demonstrates that the dual-buffer and preference-sampling design (Section 4.3) is a genuine improvement over naive penalty tuning.

- **Framework generality**: The two modifications (ARM + AUTO-MDP) are agnostic to the base RL algorithm; the paper demonstrates this by instantiating ARAM with SAC and could be adapted to other algorithms.

## Weaknesses

### Fatal
None.

### Major

- **The training procedure for the dual-buffer design is underspecified, hindering reproducibility.** The paper introduces a "real replay buffer" for feasible transitions and an "augmented replay buffer" for infeasible transitions (Section 4.3), but does not clearly explain how the augmented infeasible transitions are generated. Since the agent only ever executes feasible actions (ARM rejects infeasible ones before environment interaction), the mechanism for obtaining "augmented infeasible transitions" must involve simulation (e.g., storing hypothetical self-loop transitions (s, a_infeasible, [0, -κ], s)). The paper references Algorithm 1 (a figure stripped by the parser) for the full procedure, but the main text should provide a self-contained description. Without this, readers cannot verify whether the augmented MDP actually guides learning or is a peripheral artifact.

### Minor

- **The paper does not report what fraction of ARAM's actions require the auxiliary projection step at test time.** The paper states (line 148) that all methods, including ARAM, use an auxiliary projection step during testing to guarantee constraint satisfaction. While Table 2 reports valid action rates (98–100%) for the raw policy output, the exact fraction of actions that still require projection is not reported. This makes the inference-time advantage less precisely quantified than it could be.

- **The penalty constant κ is introduced but its value and selection process are not discussed.** κ (line 84) determines the penalty magnitude for infeasible actions and is central to the AUTO-MDP design. The paper does not report its value, discuss how it was chosen, or analyze sensitivity to this choice.

- **Learning curves in Figure 3 lack confidence intervals or error shading.** Results are reported as averaged over five seeds, but no measure of variance is shown in the learning curves, making it difficult to assess the reliability of the observed differences.

- **The paper does not discuss the failure case where the acceptance rate is extremely low** (e.g., high-dimensional action spaces with very small or disconnected feasible sets), which is a relevant practical limitation of the ARM approach.

### Trivial
None.

## Nice-to-Haves

- Report the acceptance rate trajectory during training to directly validate the claim that AUTO-MDP improves acceptance rate over time.
- Report the fraction of ARAM's test-time actions that require the auxiliary projection step.
- Include confidence intervals or standard deviation bands in learning curves.

## Removed Points

These points from the inputs were removed (with justifications):

1. **Proposition 1 lacking proof** (Harsh Critic): Removed per instructions — proofs may exist in the appendix that was stripped by the parser. The paper claims the property, and evaluating its validity requires seeing the complete submission.
2. **FOCOPS comparison being "weak" or "expected"** (Harsh Critic): The paper (line 177) explicitly positions this comparison to demonstrate that per-step ACRL differs from long-term CMDP methods. Including it is informative, not a flaw.
3. **Critic loss equation potentially missing entropy term** (Harsh Critic): The equation is correct — the entropy term α log π(a|s) is included inside the V-function definition (line 129), which is then used in the critic loss.
4. **Generic or speculative concerns from the Harsh Critic** that lack concrete anchor in the paper (e.g., "if κ is too small...", "could the metric be measuring a proxy") — these are area-of-concern sweeps rather than identified problems.
5. **Several generic strengths from the Strength Finder** that were superficial or sycophantic (e.g., "this paper addressed an important problem") without specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel interpretation or connection that the paper itself does not already articulate.

## Suggestions

1. Provide a clear, self-contained description of how augmented infeasible transitions are generated for the dual-buffer design, including whether they are simulated hypothetical transitions (self-loop dynamics + penalty reward). Add pseudocode in the main text or appendix.
2. State the value of κ used in experiments and briefly discuss how it was chosen (tuned, set heuristically, or absorbed into the MORL framework).
3. Report the fraction of test-time actions that require the auxiliary projection step for ARAM, alongside the existing valid action rate.
4. Add error bands or confidence intervals to learning curves.
