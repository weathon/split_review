Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper introduces a library-based relearning framework to address shortcut learning in continual learning. The authors invoke the information bottleneck principle to argue that replay buffers are insufficient for recovering information lost to shortcut learning, and propose maintaining a larger unbiased "library" of past data, quizzing the model to detect information loss, and selectively relearning from a small informative subset. The method (CLOM+RL) shows substantial improvements over strong baselines on CIFAR and TinyImageNet benchmarks.

## Strengths

1. **Addresses an underexplored problem with a well-motivated framework.** Shortcut learning is a genuine issue in continual learning that most prior work does not explicitly tackle. The paper's core idea — maintain a larger unbiased library of past data to detect and recover lost information — is intuitive, practically motivated, and goes beyond simple buffer-based replay.

2. **Consistent and substantial performance gains.** CLOM+RL outperforms all baselines in Table 1 across five dataset/task configurations, with gains that increase with the number of tasks (e.g., larger margins on CIFAR100-20T than CIFAR100-10T). This pattern directly supports the claim that shortcut learning accumulates over time and that the library-based approach mitigates it.

3. **Orthogonality of the relearning component.** Table 2 demonstrates that applying relearning (+RL) improves three different categories of CL methods (regularization-based LwF, replay-based Der++ and BiC, and task-ID-based CLOM). This shows the framework is a general plug-in enhancement beyond a single architecture.

4. **Active quiz mechanism for computational efficiency.** The active quiz (Table 3) is a creative way to detect when relearning is needed, reducing computation while still improving over no-relearning baselines. This addresses a practical concern about the cost of accessing a larger library.

## Weaknesses

### Fatal
None.

### Major

1. **Single-head methods (Der++, BiC): missing adaptation details.** The difficulty score (Eq. 4) and relearning loss (Eq. 6) are defined in terms of task-specific logit subvectors ($\mathbf{p}_t$ for within-task, $\mathbf{p}_{t'}$ for inter-task). The method description (Section 4, Figure 3) assumes separate classifier heads per task. While the difficulty score *could* be adapted for single-head methods by grouping output classes by task origin, the paper provides **no description** of how this is done for Der++ and BiC, which use a single shared classifier. Without this explanation, the results in Table 2 for Der+++RL and BiC+RL are not supported by the described method.

2. **Missing essential ablations that isolate the claimed contribution.** The paper does not provide:
   - A comparison of the difficulty-score-based selection against **random selection from the same library**. Figure 5 varies difficulty level and library size but includes no random baseline. Without this, the claim that the selection method matters is unsubstantiated.
   - A control where CLOM is given **access to the same additional data** (e.g., replay buffer enlarged to match library buffer size). The paper states "just increasing replay-buffer size is not feasible" but never tests what happens when it *is* increased to 5000 (the library size). The observed gains could partly reflect simply having more data, rather than the library+selection mechanism.

3. **No statistical significance or variance reporting.** Results are reported as single numbers without standard deviations, confidence intervals, or multiple seeds. Continual learning is known to be sensitive to random seeds, task order, and initialization. This is a significant concern, especially given the 700-epoch per-task training regime (which could amplify seed sensitivity).

4. **Missing comparison with the most directly related prior work.** The paper cites OnPro (Wei et al., 2023) as "among the few attempts to address [shortcut learning] within continual learning" but does not compare against it in experiments. For a paper whose central claim is addressing shortcut learning in CL, omitting the only directly competing approach weakens the empirical contribution.

### Minor

1. **Theory-algorithm gap.** The information bottleneck analysis (Section 3) motivates the high-level need for "relearning" and a knowledge-rich library, and this is a valid contribution. However, it does not constrain or explain the specific algorithmic choices: the Fourier-derived transformation function (Eq. 5, parameter $c$), the quiz threshold $\lambda$, or the hinge regularizer margin $\gamma$. These are designed heuristically. The paper does not compute mutual information in the full experimental setting (the only MI plot, Figure 1b, lacks methodological details on how it was estimated). The theoretical contribution is thus more of a post-hoc narrative than a generative design principle.

2. **Baseline results are taken from prior papers, not re-implemented with the same training budget.** The paper trains its feature extractor for **700 epochs** per task using supervised contrastive loss, but baseline numbers are "noted as reported on the results of the works in Kim et al. (2022a) and Lin et al. (2024)." If the original baselines used fewer epochs or different learning schedules, the comparison may be unfair. The paper should state whether baselines were re-implemented with the same training setup, or acknowledge the discrepancy.

3. **Difficulty score may be affected by logit scale differences across tasks.** The score $D_t^i = \max(\mathbf{p}_{t'}^i - \max \mathbf{p}_t^i)$ relies on comparing logits from different task classifiers. Without calibration (the paper notes CLOM+c uses a calibration transform), scale differences across tasks could dominate this score rather than genuine sample difficulty. The paper does not discuss this or provide evidence that the score is robust to scale variation.

4. **Sensitivity of hyperparameters $c$ and $\lambda$ is not studied.** The transformation parameter $c$ (Eq. 5, varied 1.5–2.5) and the quiz threshold $\lambda$ (set to 100 for CIFAR10-5T) control important aspects of the method, but no sensitivity curves are provided. The paper's Figure 5 ablation varies library size and difficulty level but does not vary $c$ or $\lambda$.

5. **Active quiz trade-off not analyzed.** Table 3 shows selective relearning drops accuracy from 83.39% (always relearn) to 79.63% (selective) — a nearly 4pp reduction. The paper states this "significantly reduces computation" but does not quantify the computation saved or analyze whether the trade-off is favorable relative to simpler alternatives (e.g., relearning every $k$ tasks).

### Trivial
None.

## Nice-to-Haves

- A comparison of difficulty-score-based selection versus random selection from the library.
- Visualizing selected high-difficulty vs. moderate-difficulty samples to demonstrate that the method targets genuinely informative points (e.g., attention maps before/after relearning).
- Sensitivity curves for hyperparameters $c$ and $\lambda$.
- Total wall-clock time comparison across methods, not just linear scaling arguments.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Structurally incompatible with single-head methods"** (Critic's Critical Issue #1): The difficulty score is defined using task-grouped logits, not separate model architectures. For single-head CIL methods, one can still group output classes by their originating task to compute $\mathbf{p}_t$ and $\mathbf{p}_{t'}$. The method is adaptable; the real issue is the **missing description** of this adaptation (kept in Major #1 above). The "structural incompatibility" framing overstates the problem.
  
- **"The transformation function is unnecessarily complex; a simple sinusoidal function is the result"** (Critic's Section-by-Section): This is a presentation preference. The Fourier derivation is used to justify a design choice, and the resulting function is clean. The complexity is not a flaw — it's a reasoned derivation.
  
- **"Difficulty score may be dominated by scale differences across tasks"** (Critic's Section-by-Section): This is speculative. While plausible, the paper provides no evidence that this occurs, and the results are strong across multiple datasets. Kept as a minor concern but downgraded from the reviewer's implied severity.
  
- **"The paper does not compare computational cost in terms of total wall-clock time"**: The cost analysis in Section 4 focuses on the *additional* cost of the library buffer and selection, which is appropriate since the 700-epoch feature extractor cost is shared with baselines. A full wall-clock comparison is a nice-to-have, not a missing essential.

## Novel Insights

Beyond the paper's own contributions, what emerges from the reviews is a clear tension: the paper presents a practically effective framework (library + relearning + active quiz) with strong empirical results, but the supporting structure — theoretical grounding, ablation controls, and adaptation details for non-task-ID methods — is thinner than the empirical claims require. The most interesting unresolved question is whether the gains come primarily from **access to more data** (the library being larger than the replay buffer) or from the **specific selection mechanism** (difficulty-score-based filtering). Resolving this would substantially strengthen the paper's narrative that shortcut learning, not data quantity, is the key bottleneck being addressed.

## Suggestions

1. **Clarify the adaptation for single-head methods** (Der++, BiC). Provide explicit details on how $\mathbf{p}_t$ and $\mathbf{p}_{t'}$ are defined when there is a single shared classifier, or remove these results if the method cannot be cleanly adapted.

2. **Add critical ablations:** (a) Compare difficulty-score-based selection vs. random selection from the library. (b) Compare CLOM+RL against CLOM with a replay buffer enlarged to the library size (5000). These directly test whether the library concept and the selection mechanism are responsible for the gains.

3. **Report results over multiple seeds** (at least 3–5) with standard deviations to establish statistical reliability.

4. **Include OnPro as a baseline** in the experimental comparison, given the shared focus on shortcut learning in CL.

5. **Provide sensitivity analysis** for key hyperparameters $c$ and $\lambda$, and methodological details for the MI computation in Figure 1b.

## Score and Decision

The paper introduces a well-motivated idea and presents strong empirical results on multiple benchmarks. However, the evaluation lacks essential controls (random selection baseline, data-amount control, variance reporting) and a key detail (adaptation to single-head methods) that are necessary to validate the claimed contributions. The core idea is promising, and the primary CLOM+RL results are compelling, but the paper needs significant revision before its contribution can be fully assessed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>