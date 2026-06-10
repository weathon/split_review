## Summary

This paper proposes Eidetic Learning, a sparsity-based continual learning method that prevents catastrophic forgetting by (i) iteratively pruning each task to its minimal subnetwork, (ii) freezing those important neurons, and (iii) severing synapses from recycled neurons to frozen ones to satisfy two sufficient conditions (Persistence and Resistance). The method is evaluated on Permuted MNIST, Sequential CIFAR100, and Imagenette with MLP and ResNet architectures.

## Strengths

- **Clean formalization of sufficient conditions for zero forgetting (Section 2, lines 53–57):** The paper explicitly states Persistence (important neurons remain unchanged) and Resistance (unimportant neurons disconnected from important ones) as jointly sufficient conditions for preventing forgetting. This provides a crisper theoretical framing than regularization approaches that only soften parameter changes, and the empirical result in Figure 1 (flat accuracy curves across tasks) directly validates that these conditions achieve their aim.

- **BN handling without per-task architectural modifications (Section 3.1, lines 115–117):** The paper specifies a concrete mechanism for batch normalization — freezing β,γ, preventing running statistics from updating, and keeping BN in evaluation mode for previous tasks. The paper correctly distinguishes this from prior work (Kaushik et al., 2021) that requires separate BN layers per task, and the empirical results (Table 4, Figure 4) confirm this scheme works with standard ResNet architectures.

- **No task ID required at inference (Section 1, line 19; Section 4, lines 175–176):** The paper introduces a learned task classifier to eliminate the need for known task IDs at inference, addressing a practical limitation of prior sparsity-based methods (PackNet). The cost is quantified (~1.8% accuracy drop relative to oracle routing), making the trade-off transparent.

- **Constant hyperparameter count per ANN (Table 1; Section 2, line 60):** Unlike CLNP whose hyperparameter complexity scales linearly with layers, EideticNets use only a constant number (pruning step size and stop threshold), simplifying deployment.

## Weaknesses

### Fatal
None.

### Major

1. **"Provable" claim is not substantiated by any formal mathematical argument.** The paper's title and abstract lead with "provable" and "prove," yet the paper contains zero theorems, lemmas, definitions, or proofs. The two sufficient conditions (Persistence and Resistance) are stated in prose and argued informally, but no formal argument establishes that the training procedure actually satisfies these conditions, nor is there a proof that they guarantee output invariance for all inputs across all tasks. For a submission to ICLR that advertises provability as a headline contribution, this is a significant overclaim. The paper should either provide actual formal statements and proofs, or remove the "provable" framing and present the method as empirical with intuitive guarantees.

2. **No baseline comparisons on two of three benchmarks (CIFAR100 and Imagenette).** Tables 4 (ResNet50 / CIFAR100) and 5 (ResNet18 / Imagenette) report only the proposed method's own results. There are no comparisons against EWC, SI, MAS, GEM, A-GEM, DER, LwF, PackNet, or any other standard continual learning method. The only baseline comparison is on Permuted MNIST (Table 3). Without baselines, it is impossible for a reader to assess whether the reported ~76% accuracy on the final CIFAR100 task is competitive, strong, or weak relative to existing approaches. This substantially limits the paper's empirical contribution.

### Minor

1. **Scope of the claimed "guarantee" narrows considerably under the paper's own caveats.** The method guarantees preservation only when: the network has sufficient excess capacity (task-dependent and not guaranteed), iterative pruning successfully identifies minimal subnetworks (the paper itself notes Taylor pruning fails to prune uniformly), the task classifier correctly identifies the task ID (1.8% accuracy drop reported), and the setting is task-incremental (class-incremental explicitly excluded). These caveats are acknowledged (Section 5), but the abstract and introduction frame the guarantee in absolute terms without these qualifications. The gap between the headline claim and the contingent reality should be closed.

2. **No ablation studies isolating design choices.** The paper does not ablate individual components (e.g., what happens if only Persistence is enforced without Resistance? Is the Resistance condition necessary, or would freezing alone suffice? How does performance degrade if the pruning stop threshold is loosened?). These ablations would strengthen confidence in the method's design rationale.

3. **BN handling mechanism is underspecified for joint inference.** The paper describes freezing BN statistics for previous tasks (Section 3.1) but does not fully explain how the network selects the correct BN statistics at inference when the same BN layer processes inputs from different tasks. The empirical results suggest it works, but the mechanism for switching between task-specific BN statistics is not described, leaving a gap in the claimed "guarantee."

4. **No analysis of capacity exhaustion.** The method's feasibility depends on excess capacity being available for each new task. The paper does not analyze how many tasks a given network can support before capacity runs out, nor what happens when it does (e.g., graceful degradation vs. sudden failure). This is critical for understanding practical deployment limits.

### Trivial
None.

## Nice-to-Haves

- Analysis of task ordering effects (does a complex task consumed first leave insufficient capacity for later tasks?)
- Runtime and computational cost characterization of iterative pruning across tasks
- Ablation on the effect of different pruning ratios and stop thresholds
- Comparison on standard Split CIFAR-100 (10-task) or 5-Datasets benchmarks

## Removed Points

These points were flagged by reviewers but are removed for the reasons given:

- **"Resistance condition transitivity claim is unsubstantiated"** (Harsh Critic): The reviewer goes on to say "actually this is fine" — the concern is self-resolved and does not constitute a real weakness.
- **"No experiments on Split CIFAR-100, 5-Datasets, MiniImageNet"** (Harsh Critic): The paper already evaluates on Sequential CIFAR100 (10 tasks) and Imagenette. Demanding specific dataset variants is scope creep; the existing benchmark set is reasonable.
- **"Hyperparameter selection on 3 tasks may not transfer to 10 tasks"** (Harsh Critic): Speculative — the paper's validation procedure is standard and the empirical results show it works.
- **"The residual connection handling notation is garbled"** (Harsh Critic): Parser artifact, not a paper problem. The method description is conceptually clear.
- **"BN concern about joint inference"** as a fundamental issue: While retained as Minor weakness #3 (the mechanism is underspecified), the reviewer's framing of it as a major gap is overstated given the positive empirical results.
- **Strength Finder's generic description of Figure 1**: Kept as valid — Figure 1 is indeed strong evidence, not generic praise.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's strong claims and their limited formal/empirical support, but do not independently identify new insights about the method or problem.

## Suggestions

1. **Remove or formally substantiate the "provable" claim.** Either add a proper theorem-and-proof section establishing that the Persistence and Resistance conditions guarantee output invariance and that the training procedure satisfies them, or reframe the paper as an empirical method with strong intuitive guarantees.
2. **Add baselines on CIFAR100 and Imagenette.** Even 2–3 standard methods (e.g., EWC, PackNet, a joint-training upper bound) would allow readers to calibrate the reported numbers.
3. **Add ablation studies** isolating the contribution of the Resistance condition (synapse deletion) vs. Persistence alone (freezing).
4. **Characterize capacity exhaustion** — e.g., train until capacity runs out and report how many tasks a given architecture can support.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>