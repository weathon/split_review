- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary
This paper proposes M³PC, a framework that uses a single pretrained bidirectional masked trajectory model to perform Model Predictive Control (MPC) at test time through mask ensembles. By combining multiple mask patterns (action reconstruction, forward dynamics, reward/return prediction), the model serves as both a policy and world model without architectural changes. The method is evaluated on D4RL locomotion, RoboMimic manipulation, and real-world tasks, showing improvements in offline RL, online finetuning, and goal-reaching scenarios.

## Strengths
- **Test-time MPC consistently improves offline RL over the same pretrained model without retraining**: Table 1 shows M³PC-M (the no-extra-training variant) outperforms the base BTM on all six D4RL tasks, raising the total from 372.8 to 395.9 (+6.2%). This provides clear evidence that the MPC mechanism alone adds value, using the same pretrained weights.
- **Substantial online finetuning gains over prior O2O methods**: Table 2 reports M³PC achieves a total improvement of +101.0 with 200K online samples (reaching 530.8), versus ODT's +45.3 (422.7) and IQL's +4.5 (405.5). M³PC outperforms ODT in five of six datasets, with especially large margins on halfcheetah-medium (+18.1 vs. −0.6) and halfcheetah-medium-replay (+18.8 vs. +0.4).
- **Zero-shot goal reaching for unseen behaviors via backward M³PC**: Section 4 and Figure 4 demonstrate that backward M³PC (path inference + inverse dynamics masks) can drive agents to goal states not present in training data (e.g., walker splits, halfcheetah flipping) — a capability not achieved by single-mask methods [UniMASK, MaskDP].
- **Ablation confirms unified pretraining is more effective than separate policy/world models**: Figure 5 shows that two separately pretrained specialized models do not improve over the unified BTM when used for MPC, supporting the claim that unified pretraining captures richer representations beneficial for planning.
- **Ablation shows both uncertainty-aware action reconstruction and planning are necessary**: Figure 6 demonstrates that the combination of uncertainty-aware NLL loss with planning-based action resampling yields substantially better online sample efficiency than either component alone, and naive Gaussian noise exploration leads to collapse.
- **Real-world manipulation success**: Table 3 reports that on Can-Real, M³PC achieves 0.70 success rate vs. DT's 0.50, demonstrating applicability beyond simulation.

## Weaknesses

### Fatal
None.

### Major
- **Goal-reaching results are presented only qualitatively, with no quantitative success rates or comparisons**: Section Q2 and Figure 4 show only visual demonstrations of three goal-reaching tasks (halfcheetah flipping, walker splits, hopper wiggling). The paper mentions comparing to a single-mask baseline but provides no success rates, no statistical summary, and no table of results. Since goal generalization to OOD states is listed as a core contribution (line 29: "effectively guiding agents to specified goal states—even when these states are out-of-distribution"), the absence of quantitative evaluation is a significant evidential gap. The reader cannot assess whether the method works reliably or if the shown examples are cherry-picked.

- **The "without any additional parameter training" framing in the abstract conflates the pure no-training variant with the best-performing variant that uses a separately trained value function**: The abstract (line 4) states that M³PC "significantly improves the decision-making performance of a pretrained trajectory model **without any additional parameter training**." However, M³PC-Q — which achieves the paper's strongest offline results (Table 1: 429.8 total) and is used in the online finetuning comparisons (Table 2) — relies on "a standalone value estimator updated in a dynamic programming way proposed in IQL" (line 106). The pure variant M³PC-M (395.9) supports the no-training claim, but the abstract and introduction do not qualify this separation, potentially leading readers to attribute the entire 429.8 to test-time MPC alone. The online finetuning comparisons (Table 2) are reported under "M³PC (Ours)" without noting that this variant uses an additional trained value function, while ODT and IQL are compared without a similar auxiliary component.

### Minor
- **M³PC underperforms simple baselines on some manipulation tasks**: In Table 3, M³PC achieves 0.28 on Square-MH vs. BC's 0.53, and 0.77 on Lift-MG vs. DT's 0.93. This weakens the claim of general applicability to manipulation domains, though the method does well on other tasks (Can-Pair, Can-Lim, Can-Real).
- **No ablation isolates the value function contribution from the MPC planning contribution in the offline setting**: The comparison between M³PC-M (Monte Carlo RTG) and M³PC-Q (IQL value) shows the value function helps, but there is no baseline using the IQL value function *without* MPC. This makes it impossible to determine how much of the offline gain (372.8→429.8) comes from better value guidance vs. the planning loop itself. (The existing ablation in Figure 6 only covers the online phase.)
- **The "two prediction steps" phrasing is ambiguous about total computational cost**: Line 106 states "M³PC requires only two prediction steps for planning at each timestep." Algorithm 1 shows that for each of N candidates, two predictions ([FD] mask + [RP] mask) are needed, totaling 2N forward passes per timestep. The parallel prediction benefit is correctly described as mitigating horizon-length scaling, not candidate-count scaling, but a reader could misinterpret "two prediction steps" as the total cost.
- **Limited real-world evidence**: The real-world manipulation results (Can-Real) are based on 20 trials on a single task, providing limited support for claims of real-world robustness.
- **No hyperparameter sensitivity analysis**: The method depends on several parameters (number of candidates N, decay parameter λ, planning horizon, softmax temperature ξ) with no ablation or sensitivity study.

### Trivial
None.

## Nice-to-Haves
- Analysis of the learned dynamics model's prediction accuracy on a held-out validation set, to contextualize MPC quality.
- A comparison against a ground-truth-dynamics MPC upper bound (e.g., using the simulator's dynamics) to establish how close M³PC's planning is to perfect-model performance.
- Wall-clock timing measurements comparing M³PC to TT and BTM, honestly accounting for the O(N) candidate cost.
- Justification for the 200K-step online budget (ODT's original paper sometimes uses more steps), with learning curves showing convergence.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder's claim that M³PC-Q achieves "15.3% improvement without any additional training"**: Factually incorrect. M³PC-Q uses a separately trained IQL value function. The improvement without additional training is M³PC-M's 6.2% (395.9 vs. 372.8). — *Removed because it is factually wrong.*
- **Harsh Critic's criticism about the paper not citing related work**: Not appropriate — I cannot verify missing citations without external sources. — *Removed per hard rules.*
- **Harsh Critic's framing that M³PC-M "underperforms TT and IQL" as a fatal weakness**: M³PC-M (395.9) is slightly below TT (403.0) and IQL (401.0) but this is a modest gap, and the paper's core claim is improvement over the same BTM, not SOTA. The improvement from BTM (372.8) to M³PC-M (395.9) demonstrates the mechanism works. The criticism is valid as context but not as a decisive weakness. — *Demoted from severe to minor factual context.*
- **Harsh Critic's claim that "the pure MPC version does not outperform existing strong baselines" is a decisive weakness**: The pure MPC version (M³PC-M) improves the same model by 6.2% and reaches near parity with TT and IQL. Combined with the online finetuning results, this is a reasonable demonstration. — *Overstated; not fatal.*
- **Harsh Critic's "The method is interesting and worth pursuing, but the evidence as presented is insufficient to warrant acceptance"**: Overly harsh conclusion not fully supported by the evidence. The paper has clear contributions, especially in online finetuning. — *The weaknesses identified are real but addressable; the paper has genuine contributions that warrant acceptance with revisions.*
- **Generalized speculation-based criticisms** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?"): These were raised as area sweeps without specific anchors in the paper. — *Removed as ungrounded speculation.*

## Novel Insights
The harsh critic correctly identified a tension between the paper's framing and its experimental setup: the "no additional training" claim in the abstract is technically supported only by the M³PC-M variant, but the headline results conflate the value-function-augmented variant (M³PC-Q) with the pure mechanism. This is a real framing problem. However, the strength finder's observation about the clean comparison between M³PC-M and BTM is also important — it does show that the core MPC mechanism adds value (6.2%) without any auxiliary training, which is a genuine and non-trivial result. The true novelty of the paper lies not in MPC per se, but in the insight that a single bidirectional masked model, through mask ensembles, can serve all roles needed for test-time planning (action proposal, dynamics roll-out, reward/return evaluation). This is a clever architectural insight that future work could build on, even if the current paper's evaluation has gaps.

## Suggestions
1. **Provide quantitative goal-reaching metrics** — report success rates over multiple seeds (at least 10) for each of the three goal-reaching tasks, with comparison to the single-mask baseline [UniMASK/MaskDP]. This is essential to substantiate the claimed contribution.
2. **Clarify the "no additional training" claim** in the abstract and introduction by explicitly distinguishing the M³PC-M variant (no extra training) from M³PC-Q (which additionally trains a value function). The introduction should state what each variant contributes.
3. **Add an ablation** comparing: (a) BTM + IQL value (greedy, no MPC), (b) M³PC-M, and (c) M³PC-Q in the offline setting. This would cleanly isolate the value function contribution from the planning contribution.
4. **Report wall-clock time** per timestep for M³PC vs. TT and BTM, including the effect of N candidates, to replace the ambiguous "two prediction steps" phrasing with transparent cost accounting.
5. **Add hyperparameter sensitivity** for N, λ, and ξ. Show how performance varies with these choices.
