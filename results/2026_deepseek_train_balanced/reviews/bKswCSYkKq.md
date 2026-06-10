## Summary

This paper proposes NBSP (Neuron-level Balance between Stability and Plasticity), a method for continual deep reinforcement learning that identifies "RL skill neurons" via a goal-oriented correlation score between neuron activations and task success, then freezes them via gradient masking while using experience replay for additional stability. The method is evaluated on Meta-World and Atari task pairs, comparing against EWC, ANCL, and a self-variant.

## Strengths

1. **First neuron-level treatment of stability-plasticity in DRL, with supporting evidence.** The paper is the first to address both stability and plasticity simultaneously at the neuron level in DRL. The empirical comparison (Figure 4) shows NBSP achieving near-perfect success rates on both tasks across the evaluated Meta-World task pairs, while network-level methods (EWC, ANCL) consistently fail on at least one dimension.

2. **Goal-oriented RL skill neuron identification tailored to DRL.** Unlike prior skill-neuron methods that focus on input-triggered activations (Bau et al., 2020; Gurnee & Tegmark, 2023), Section 3.2 (Eqs. 1–4) defines a scoring function measuring correlation between neuron activation and task *outcome*, capturing both positive and negative correlations (Eq. 4). The comparison against Importance-based NBSP (Figure 4) validates that this identification method matters: Importance-based NBSP works on only some task pairs while RL-skill-neuron NBSP works consistently across all four.

3. **Systematic ablation revealing the critic's pivotal role.** Section 4.3 (Figure 6) ablates NBSP applied to only the actor (NBSP-Actor) vs. only the critic (NBSP-Critic), showing NBSP-Critic consistently outperforms NBSP-Actor in knowledge retention. The paper provides a mechanistic explanation grounded in actor-critic training dynamics (lines 162–163): the critic's target network uses exponential moving average, enabling recursive knowledge preservation while integrating new skills. This is a non-trivial and verifiable insight.

4. **Simple, parameter-free design.** The method (Section 3.3, Eqs. 5–6) requires no auxiliary networks, additional parameters, or modular architecture modifications — only binary gradient masking on identified neurons and standard experience replay. This contrasts with methods like ANCL (which requires a separate auxiliary network) and EWC (which introduces per-parameter importance weights).

5. **Generalization across continuous and discrete control.** NBSP is evaluated on both Meta-World (continuous control, binary success metric) and Atari (discrete control, return-based metric), demonstrating the approach is not tied to a specific DRL algorithm or environment type.

## Weaknesses

### Major

1. **The neuron selection criterion is not specified — a critical hyperparameter is missing.** Section 3.2 (line 78) states: "The neurons with the highest scores are identified as RL skill neurons" and "the number of RL skill neurons varies depending on the complexity of the task." No threshold, percentage per layer, absolute count, or selection rule is given. This is the central control parameter of the method: it directly determines how many neurons are frozen and therefore the strength of both stability preservation and plasticity constraint. Without this information, the method cannot be reproduced, and it is impossible to assess whether the results are robust to this choice or carefully tuned to achieve the reported performance. This is a specification gap in the core methodology, not a minor implementation detail.

2. **The termination-based evaluation protocol introduces a confound.** Section 4.1 (line 117) and all figure captions state: "Training terminates upon reaching stable optimal performance or maximum steps for each task." This means different methods train for different numbers of steps — a slow-learning method gets more training steps while a fast-learning method terminates earlier. This conflates convergence speed with final performance and makes cross-method comparisons of both training curves and final performance bars unreliable. A fixed-step evaluation protocol is standard in continual RL and would be far cleaner.

3. **Baseline comparison is too narrow to support the claim of "significantly outperforming existing approaches."** The paper compares against only two existing methods (EWC, ANCL) plus a self-variant (Importance-based NBSP). Missing are: (a) simple baselines such as L2 regularization on all parameters or freezing early layers, which would test whether the sophistication of neuron-level selection actually matters beyond naive regularization; (b) methods specifically designed for plasticity loss in DRL, which the paper itself cites as key motivation (Nikishin et al., 2022a; Abbas et al., 2023). For a paper claiming significant outperformance across domains, three baselines on a modest number of task pairs is insufficient evidence.

### Minor

4. **Last-layer exclusion is stated without justification.** Line 78 excludes "neurons in the last layer" from identification. In an actor-critic network, the output layer maps learned representations to actions/values and is arguably the most task-specific part of the network. The paper offers no rationale for this exclusion, leaving readers unsure whether this choice materially affects the results.

5. **Limited diversity in task pairs.** The Meta-World tasks tested are all reversible variants of each other (open→close, close→open; open→close, close→open). These share nearly all structure, making the continual learning problem relatively easy. Genuinely different task sequences (e.g., drawer-open → window-close) would provide stronger evidence. The paper reports "four task pairs with varying combinations of difficulty" (line 115) but does not enumerate their composition in the text.

6. **The RL skill neuron identification method lacks deeper validation.** The comparison against Importance-based NBSP shows the identification method matters, but there is no analysis of what kinds of neurons are selected (which layers, how many, typical activation patterns), no sensitivity analysis on the scoring binarization, and no causal intervention to directly demonstrate these neurons encode task-specific knowledge rather than being simply correlated with performance.

### Trivial

7. Atari game names are not listed in the text (line 169 only says "two irrelevant and two relevant game pairs"; names appear only in the rendered Figure 7).

## Nice-to-Haves
- A causal intervention study (ablating identified RL skill neurons and measuring task-specific performance drops) would strengthen the claim that these neurons encode task-specific skills.
- Sensitivity analysis on the neuron selection threshold (e.g., top-1%, top-5%, top-10%) would clarify how critical this parameter is.
- Comparing against a simple "freeze all parameters except last layer" baseline would quantify the added value of selective neuron freezing.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Harsh Critic: "Correlation is not causation"** — The paper does not claim a causal mechanism; it claims the identification method is useful for the masking strategy, which is validated empirically against Importance-based NBSP. This is a generic concern, not a specific identified flaw.
- **Harsh Critic: "First work claim is overblown because Sokar et al. 2023 does neuron-level analysis in DRL"** — Sokar et al. addresses dormant neurons for plasticity only, not the simultaneous balance of stability and plasticity at the neuron level in DRL. The paper's claim is narrower and defensible.
- **Harsh Critic: "Only 2 task pairs appear in the main results"** — The paper explicitly states "For all four task pairs evaluated" (line 137). While the text only names two pairs explicitly, the paper asserts four were evaluated. This criticism appears based on a misreading.
- **Harsh Critic: "The paper should compare against Progressive Neural Networks, CLEAR"** — Removed per the "missing related works" rule; verifying these specific baselines requires external sources not available to the meta-reviewer.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify the neuron selection criterion** — report the exact number or percentage of neurons selected per layer, and provide a sensitivity analysis varying this threshold (e.g., top-1%, top-5%, top-10%).
2. **Replace the termination-based evaluation protocol** with a fixed-number-of-steps evaluation for all methods, or at minimum report results at matched step counts.
3. **Add simple baselines** (L2 regularization, layer freezing) and at least one DRL-specific plasticity-loss method to the comparison.
4. **Provide justification for the last-layer exclusion**, and test whether including the last layer changes results.
5. **Test on at least one non-reversible task pair** in Meta-World to demonstrate the method handles genuinely different tasks.
6. **Add an analysis of which neurons are selected** (layer distribution, activation characteristics, score distribution) to demystify the identification method.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>