Now I have all the evidence needed. Let me construct the final consolidated review.

## Summary

This paper studies RL generalization under both distribution shifts and state/action space expansions — a setting more general than typical fixed-space transfer RL. The authors propose CSR, which learns causal latent representations with structural masks, then uses a three-step pipeline (distribution shift detection via prediction-error thresholding → causal graph expansion if needed → pruning of irrelevant variables) to adapt with minimal data. Experiments on CartPole, CoinRun, and Atari show strong performance compared to RL baselines that assume fixed state/action spaces.

## Strengths

1. **Addresses a genuinely broader generalization setting.** Most RL generalization work assumes fixed state and action spaces. This paper tackles scenarios where new latent variables (e.g., enemies in CoinRun, friction in CartPole) or new actions appear, and formulates both distribution shifts and space expansions within a single framework. The CoinRun example in the introduction (levels where enemies emerge that never appeared during training) concretely motivates the problem.

2. **Strong empirical results across multiple benchmarks.** On CartPole (Table 1), CSR achieves the maximum score on all four tasks while baselines fail on space-expansion tasks (Tasks 3–4). On Atari 100K (Table 2), CSR obtains the highest mean final scores in all five tested games. On CoinRun (Fig. 3b), CSR converges faster and to higher rewards. These results are consistent across environments.

3. **Ablations confirm the contribution of the causal structure (D) and expansion strategy.** Fig. 3c shows that including the structural masks D yields faster and higher reward than without D in Atari games. Fig. 3d compares expansion strategies and shows the Self-Adaptive method outperforms Random and Deterministic expansions.

4. **Theoretical identifiability results provide formal grounding.** Theorems 1–3 and Corollary 1 establish conditions under which the latent variables, the domain-specific change factor θ, and newly added state variables are component-wise identifiable. While the assumptions are strong for visual environments, the theory differentiates CSR from purely heuristic adaptation methods.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against dynamic-architecture methods that also handle space expansions.** The paper cites DEN, PackNet, APD, CPG, and Learn-to-Grow in Related Work as "dynamic neural networks" that "address sequences of tasks that require dynamical modifications to the network architecture" (end of Section 5), yet evaluates against none of them. Since these methods also expand network capacity when new tasks arrive, the reader cannot tell whether CSR's performance comes from its causal machinery or simply from being *any* method that expands its representation space. This is the central comparison needed to establish the value of the causal approach specifically. Without it, the strong CartPole results (500/500 across all tasks) could reflect the fact that CSR expands its latent space, not that it does so via causal representations.

2. **The binary mask (D) optimization procedure is not specified.** The paper treats D as binary masks {0,1} and states that the L1 regularization term J_reg "induces certain entries of D to transition from 1 to 0 during model estimation" (Section 3.3). Binary variables cannot be directly optimized via gradient descent with L1 penalties without a relaxation (e.g., Gumbel-Straight-Through, concrete relaxations, or a separate discrete search). The paper never states how this is done. Since the entire claim of "causal structure learning" and "pruning" rests on whether D can be meaningfully estimated, this is a significant reproducibility gap.

### Minor

1. **Threshold-based detection mechanism lacks empirical validation or sensitivity analysis.** The paper sets τ* as the final prediction loss on the source task M₁ and uses it as a universal cutoff to decide between distribution shift and space expansion (Section 3.1). No analysis is given for whether this threshold reliably separates the two cases under varying noise levels, random initializations, or different task sequences. A pure distribution shift could plausibly produce a higher prediction error than a small space expansion, leading to misclassification. The paper should at least characterize the separation margin on synthetic data.

2. **Self-Adaptive expansion strategy has unquantified overhead.** The paper acknowledges that "each search step requires extensive training time for models with different expansion scales, making the search process highly time-consuming" (Ablation Study), but reports no wall-clock time or sample complexity for this inner search. Since the baselines do not perform any architecture search, the advantage may partly reflect greater compute rather than algorithmic superiority.

3. **Number of random seeds and source of variance not reported.** The paper reports standard deviations in Tables 1–2 but never states how many seeds were used or whether the variance is over seeds or over evaluation episodes within a single run. The CartPole results showing 500.0 (±0.0) across all four tasks — including tasks with friction and new actions — is unusual and requires clarification of the evaluation protocol.

4. **"Minimum Adaptation Steps" is imprecisely defined.** The caption of Table 1 says this refers to "the minimal amount of data required for models to generalize to new tasks, as illustrated in Fig. [cartpole figure]." The threshold for "generalizing" (e.g., first time average reward crosses a threshold? 90th percentile?) is not stated, and no variance is reported for these values.

5. **Theoretical assumptions (invertible g, linear additive transitions, differentiable functions) are not verified in the experimental domains.** While this is common in ML papers — theory under idealized conditions, experiments in messier real settings — the disconnect is notable because the detection and expansion decisions rely on the thresholds and empirically learned representations, not on the identifiability guarantees. The paper would benefit from a brief discussion of when the assumptions are likely to hold or break.

### Trivial

- Atari experiments use 5 of 26 games without justifying why these five are representative or whether the pattern holds more broadly. This is not a fatal flaw given the space constraints but limits generality claims.
- Action expansion is mentioned in the CartPole experiment (Task 4 adds new force values) but the method section (Section 3.2) focuses entirely on state expansion, saying "the action variables are observable, we can directly obtain the relevant information." The action expansion mechanism deserves its own description.

## Nice-to-Haves

- A sensitivity analysis for the detection threshold τ*, showing the distribution of prediction errors under pure distribution shifts vs. space expansions on a synthetic validation set.
- Validation of the learned causal masks D against ground-truth causal structure in a controlled simulated environment where the generative process is known.
- Wall-clock cost comparison between CSR's Self-Adaptive expansion and simpler heuristics.

## Removed Points

These points were flagged by reviewers but are removed after verification:

1. **"Causal graph pruning definition misses variables important for policy learning"** — Removed because the paper's definition of compact state representation explicitly includes variables that "influence other state variables s_{j,t+1} (k≠j)" (Section 3.3, line 196). The critic's example ("it affects another state that affects reward") is already covered. The critic misread the definition.

2. **"Comparison to Dreamer/AdaRL/DQN is fundamentally inequitable"** — Partially removed from being framed as a fatal flaw. The baselines are standard in RL and show that the setting is genuinely hard. The valid sub-concern (missing dynamic-architecture baselines) is preserved as Major weakness #1. The framing that comparing against fixed-space methods is "fundamentally inequitable" is overwrought — showing that methods that can't handle space expansions fail at space expansion tasks is informative.

3. **"Paper doesn't adequately position itself against prior work"** — Downgraded to Removed because the Related Work section (lines 295–299) does cite the relevant dynamic-architecture methods and discusses limitations of prior work. The positioning is adequate given typical paper length constraints; the real gap is the missing *experimental* comparison, which is already captured in Major #1.

4. **"Identifiability theorems are disconnected from experiments"** — Downgraded from a major criticism to Minor #5. The disconnect is real but typical in ML: theory provides formal guarantees under specific assumptions while experiments validate practical performance. This does not invalidate either component, and many papers operate at this level.

5. **"SA is a nested RL problem with unexamined tractability"** — The paper does acknowledge the overhead (line 291). The valid sub-concern about missing wall-clock reporting is preserved in Minor #2. The framing as a "nested RL problem whose tractability is unexamined" overstates: SA is a simple search over expansion scales, not a full nested RL problem.

## Novel Insights

None beyond the paper's own contributions. The reviews are mostly convergent with the paper's claims, offering quality-control critiques rather than new conceptual angles.

## Suggestions

- **Foremost, address the binary mask optimization gap:** Specify whether D is optimized via Gumbel-Softmax relaxation, straight-through estimation, continuous relaxation with post-hoc thresholding, or a separate discrete search. Without this, the core causal learning claim is not reproducible.

- **Add at least one dynamic-architecture baseline** adapted to the RL setting (e.g., a version of Dreamer whose latent dimension grows when prediction error spikes). This would directly test whether CSR's causal machinery provides benefit beyond simply expanding the representation.

- **Validate the threshold empirically:** Show prediction error histograms for distribution-shift vs. space-expansion tasks in at least one environment (e.g., the simulated experiments) to demonstrate there is a clean separation margin.

- **Report the number of seeds** and clarify what the parenthesized (±) values in Tables 1–2 represent (standard deviation over seeds, or over evaluation episodes, or both). Clarify the "Minimum Adaptation Steps" definition and report its variance.

- **Report wall-clock time** for CSR's adaptation pipeline, especially the SA search overhead, so readers can judge the practical cost.

## Score and Decision

The paper tackles a real and under-explored problem (RL generalization with state/action space expansions), proposes a creative three-step causal framework, and demonstrates strong empirical results. However, two major issues — the missing dynamic-architecture baselines that would isolate the value of the causal machinery, and the un- specified optimization of the binary causal masks that undermines reproducibility — prevent the paper from being accepted in its current form. The empirical contributions are promising but incomplete as a result.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>