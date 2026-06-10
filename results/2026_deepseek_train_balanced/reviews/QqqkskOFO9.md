## Summary

This paper identifies a genuine limitation in off-policy actor-critic RL: a gradient-based actor can get stuck in local optima of a non-stationary, non-convex Q-function. The authors propose SAVO, which trains a sequence of K actor-critic modules where each successive critic's landscape is "pruned" by lower-bounding it at the best Q-value found by previous modules. The final action is selected by the primary critic from among all K proposals. Experiments are reported on continuous control (MuJoCo, with "Hard" variants) and large-discrete action spaces (a mining task, RecSim recommender systems).

## Strengths

1. **Clean formalization of successive critic pruning.** The objective $Q_i(s,\{a_0,\ldots,a_{i-1}\},a_i) = \max_{j=0\ldots i} Q(s,a_j)$ (Eq. 3) crisply defines how each module's landscape is lower-bounded by the best Q-value found so far. No prior actor-critic work formalizes this specific sequential lower-bounding mechanism.

2. **Ablation isolates the successive-conditioning mechanism.** The SAVO-no-link ablation removes the list encoder (each actor-critic pair operates independently without communication), while retaining the pruning objective. The paper reports that full SAVO outperforms SAVO-no-link, demonstrating that the *successive linkage* of actors (not just having multiple candidates) drives improvement. This is a clean causal isolation of the core architectural idea.

3. **Performance profile methodology.** The paper adopts the rigorous evaluation framework from Agarwal et al. (2021) using performance profiles with rank-based aggregated statistics across all tasks and seeds, which is notably more robust than cherry-picking individual benchmark results.

4. **Controlled "Hard" environments.** The paper explicitly constructs Hard MuJoCo variants by inducing regions of validity (discontinuities) in the action space. This directly tests the specific failure mode (local optima from discontinuities) that SAVO claims to address, rather than relying only on existing benchmarks.

5. **Visual analysis of the pruning effect.** The paper attempts to directly visualize the Q-value surfaces of $Q_0$, $Q_1$, and $Q_2$ (Figure 3) to show stepwise removal of local optima — a form of evidence that goes beyond end-task performance to probe the claimed mechanism.

## Weaknesses

### Fatal

None.

### Major

1. **Core technical mechanism lacks analysis of neural network approximation.** The pruning objective trains $Q_i$ via regression to approximate $\max(Q(s,a_i), \text{baseline})$, where baseline $= \max_{j<i} Q(s,a_j)$. This target function is piecewise with a kink at the boundary $Q(s,a_i) = \text{baseline}$. The gradient $\nabla_a Q_i$ is intended to vanish below the baseline and equal $\nabla_a Q$ above it, but the paper provides **no analysis** of whether neural networks can accurately approximate this non-smooth function, how approximation error affects the gradient signal propagated to the successive actors, or whether the empirical "smoothing" the paper claims (Figure 3) reflects the pruning mechanism versus mere function-approximation smoothing. The claim that successive landscapes are "more tractable" rests on an untested assumption that this piecewise target is learnable by standard neural networks with the same ease as the smooth primary critic. This is the paper's most significant analytical gap.

2. **Zero numerical results reported in the text.** The results section (6.1.2) contains only qualitative claims ("SAVO outperforms all the baselines," "SAVO was able to outperform all the baselines") backed by figures the reader must see in the PDF. No final-return tables, no summary statistics, no error bars, no effect sizes appear anywhere in the manuscript text. For an empirical paper that claims improvement across 7+ environments (Hopper-Hard, Walker2D-Hard, Mine World, RecSim, RecSim-Data, and Easy continuous tasks), this is a severe reporting gap. The reader cannot quantitatively assess the magnitude or statistical reliability of SAVO's claimed advantages.

3. **"Hard" environments are critically underspecified for reproducibility.** The paper states (Section 5.2) that discontinuities are introduced by "inducing regions of validity outside which actions are not executed," but gives **no details**: what fraction of the action space is valid? How are these regions determined? Are they randomized across seeds or fixed? Are they the same across all tasks? Without this information, the results cannot be reproduced, and the reader cannot assess whether the modification creates a realistic challenge or one specifically tailored to SAVO's multi-actor architecture.

4. **Missing SAC baseline weakens the scope claim.** The paper explicitly states (Section 3.1) that "the identified challenge and ideas are broadly applicable to any algorithm training actors to optimize the critic with gradient ascent, including SAC." SAC with entropy regularization partially mitigates the local-optima problem the paper identifies. By omitting SAC from the comparison, the paper avoids the baseline most likely to bound its claims. If SAC already handles local optima well through its entropy bonus, the practical significance of SAVO is reduced; if SAC does not, showing that SAVO outperforms it would strengthen the paper considerably.

### Minor

1. **K is not specified for main experiments.** Algorithm 1 takes K as a parameter, but the main results (Figure 2, Section 6.1.2) never state what K value was used. The ablation (Section 6.5) varies K among 1, 3, 5, but the reader does not know which value produced the primary results. This is a basic reproducibility detail.

2. **Easy continuous control results are ambiguous.** Section 6.1.2 states: "In Easy-continuous control tasks, the findings revealed that baseline models consistently performed better than more challenging tasks (Hard)." This sentence is grammatically garbled and does not state whether SAVO outperforms baselines on these tasks or not. If SAVO does not outperform baselines on standard (non-Hard) MuJoCo benchmarks, this should be stated plainly and would limit practical significance.

3. **Computational cost analysis is incomplete.** Section 6.5 compares memory cost against performance, but SAVO also requires K forward passes through critics per step (5× the critic evaluations of TD3 when K=5). The paper does not report wall-clock time or FLOPs, which are the practically relevant cost metrics. The claim that "performance gain would surpass the memory gain" compares quantities in incommensurate units.

4. **Training stability is not discussed.** Training K actors and K critics simultaneously (each $Q_i$ learning from a piecewise target with non-stationary baseline) raises convergence concerns that are not addressed. No discussion of whether the successive critics destabilize each other or how the conditioning mechanism interacts with the FiLM-based conditioning over training.

5. **Q-value improvement analysis (Figure 4a) compares against a strawman baseline.** The paper compares SAVO's action-value improvement against a baseline that "repetitively samples actions in close proximity to a single selected action" — this is TD3+Sampling. The paper does not compare against the more natural baselines of: (a) simply sampling K random actions from the primary actor's output distribution, or (b) selecting the best of K independently sampled actions from K independently trained actors (no linkage). The SAVO-no-link ablation partially addresses (b) but combines it with the pruning objective.

### Trivial

None.

## Nice-to-Haves

- Include tabular summaries of final performance (mean ± std across seeds) for all environments and methods, in addition to figures.
- Provide a formal derivation of $\nabla_a Q_i$ in terms of $\nabla_a Q$ and the baseline to clarify the gradient signal.
- Specify the "Hard" environment construction in enough detail for reproducibility (fraction of valid space, generation procedure).
- Report wall-clock time or per-step FLOPs alongside memory cost.
- Add SAC as a baseline to bound the claims of general applicability.
- State the K value used for main experiments explicitly.
- Clarify whether OU noise was chosen for a specific reason rather than the standard Gaussian noise used in TD3.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The core pruning objective is underspecified — textual description and equations describe different things."* **Removed because**: the text ("lower bounded by the previous best actions' Q-value") and the equation ($\max_{j=0\ldots i} Q(s,a_j)$) are consistent. Both describe the same lower-bounding operation. The valid concern about neural network approximation of the piecewise target is retained in Major Weakness #1 above.

- *"Lower-bounded by TD3 claim is not justified."* **Removed because**: it is factually wrong for K=1. With K=1, Algorithm 1's selection $\Pi(s) = \arg\max_{a\in\{\pi_0(s)\}} Q(s,a) = \pi_0(s)$ and the target $Q(s_{t+1}, \Pi(s_{t+1}))$ matches standard TD3. SAVO with K=1 is exactly TD3.

- *"No architecture details, network sizes, learning rates, etc."* **Removed because**: these details (if present) would reside in the appendix, which is stripped by the PDF parser. Per policy, missing appendix content is not a valid weakness.

- *"Conditioning mechanism is underspecified."* **Removed because**: the paper specifies deep-set encoding and FiLM conditioning (Section 4.2, item 2), which is adequate specification for a main-paper method description.

- *Strength: "Direct visual evidence that pruning removes local optima."* **Downgraded from a standalone strength** because the visual evidence (Figure 3) cannot be evaluated from the text alone, and the description relies on qualitative interpretation ("warm colors indicate higher Q-values") without quantitative metrics. The paper's *attempt* at this analysis is noted in Strengths #5.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments surface the key analytical gap (whether NNs can learn the piecewise pruned target) and the reporting insufficiency, but do not add a synthetic insight beyond what the paper itself claims.

## Suggestions

1. **Provide numerical results.** Add a table reporting the mean ± std of converged episode returns for every method on every environment (with the K value used). The qualitative-only reporting is the most significant barrier to evaluating the paper.

2. **Analyze the gradient of the pruned critic.** Derive $\nabla_a Q_i$ in terms of $\nabla_a Q$ and the baseline, and discuss how neural network approximation error affects the actor update. At minimum, report the empirical mean-squared error of $Q_i$ in fitting its target during training to show the approximation is faithful.

3. **Specify the "Hard" environments fully.** Describe the procedure for inducing regions of validity: what percentage of the action space is valid, how these regions are defined (random? fixed? task-specific?), and whether they are consistent across seeds.

4. **Add SAC as a baseline.** Since the paper claims broad applicability to "any algorithm training actors to optimize the critic with gradient ascent, including SAC," showing that SAVO also benefits SAC (or explaining why the entropy bonus does not suffice) is necessary to support the scope claim.

5. **Clarify K for main experiments and Easy-task results.** State the K value used in Figure 2 explicitly, and clarify whether SAVO outperforms baselines on standard (non-Hard) MuJoCo tasks or only on the Hard variants.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>