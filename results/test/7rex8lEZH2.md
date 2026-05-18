Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Prompt Diffuser, a method that reframes prompt tuning for pre-trained decision transformers in offline RL as conditional generative modeling using diffusion models. Instead of optimizing prompts from an initialization (which is sensitive to prompt quality), Prompt Diffuser generates prompts from random noise via a conditional diffusion model, conditioned on returns-to-go and timesteps. To generate prompts that exceed training dataset quality, the method incorporates downstream task guidance through gradient projection. Experiments on four meta-RL control tasks show Prompt Diffuser outperforming existing prompt-tuning baselines in few-shot settings and demonstrating robustness to prompt initialization.

## Strengths

- **Generative paradigm eliminates prompt initialization sensitivity**: The paper identifies that traditional prompt tuning in RL is highly sensitive to prompt quality (Section 2.3, Figure 1) and proposes a conditional diffusion model that generates prompts from random noise. Table 2 (ablation on prompt initialization) convincingly shows that Prompt Diffuser achieves consistent performance across Expert, Medium, and Random prompt initializations, while Prompt-Tuning DT degrades sharply — this is a conceptually novel and practically valuable shift from optimization-based to generation-based prompt tuning.

- **Gradient projection for incorporating downstream guidance**: To generate prompts exceeding dataset quality, the method integrates downstream task loss into diffusion via gradient projection (Eq. 8–9), avoiding gradient conflicts between the diffusion loss and the task loss. The ablation (Figure 2) demonstrates that the projection technique consistently outperforms using either single loss or a naive sum, directly supporting the claim that high-quality prompts can be generated beyond the dataset distribution.

- **Strong few-shot generalization**: In Table 1, Prompt Diffuser achieves the best average reward (474.4) among all few-shot fine-tuning methods on four meta-RL tasks, surpassing Prompt-Tuning DT (450.3) and Prompt-DT-FT (450.0), and approaching the full-data upper bound (496.6). The method consistently outperforms all baselines on every individual task.

## Weaknesses

### Fatal
None.

### Major

1. **Zero-shot inference protocol is not described.** The paper reports a striking zero-shot result (Table 3: Prompt Diffuser 329.2 vs. baselines 52.7 on Ant-dir-OOD), but the inference procedure for this setting is never specified. The model is a conditional diffusion model requiring condition \(y(\tau^*)\) (returns-to-go and timesteps) to generate prompts. The paper states that "no additional trajectories from the target tasks are available" in zero-shot (line 446), yet Algorithm 1 only describes few-shot inference where the condition is constructed from a trajectory sampled from \(\mathcal{D}_{test}\). How the condition is obtained when \(\mathcal{D}_{test}\) is empty — whether a default condition, task metadata (e.g., goal direction), or unconditional generation is used — is never explained. Without this clarification, the striking 6× improvement over baselines is difficult to interpret or reproduce. This is not a fatal flaw (the main contribution is few-shot, and the zero-shot protocol likely follows a reasonable procedure) but is a significant omission that must be addressed.

2. **Performance advantage over the strongest baseline is concentrated in one environment with no statistical significance analysis.** Across the four tasks in Table 1, Prompt Diffuser's advantage over Prompt-Tuning DT is: Cheetah-dir +3.8 (945.3 vs. 941.5, std 7.2 vs. 3.2), Cheetah-vel +4.2 (−35.3 vs. −39.5, std 2.4 vs. 3.7), Ant-dir +4.2 (432.1 vs. 427.9, std 6.7 vs. 4.3), and MW reach-v2 +83.2 (555.7 vs. 472.5, std 6.8 vs. 29.0). The large gap on MW reach-v2 drives most of the 24.1-point average improvement; on the other three tasks, the differences are within one standard deviation of the baseline. The paper reports "significant performance improvements" (line 398) but provides no statistical tests (e.g., confidence intervals, paired bootstrap) to establish reliability. Given that 3/4 tasks show small margins and the baselines themselves exhibit non-trivial variance, the paper should either provide significance-aware reporting or temper the strength of its claims.

3. **Gradient projection implementation is underspecified.** The paper defines a subspace \(S_{DM}^{\bot} = \text{span}\{B\} = \text{span}\{[u_1, \dots, u_M]\}\) with bases "extracted from \(\nabla L_{DM}^{\bot}\)" (lines 242–249), but never specifies how the basis \(B\) is computed, initialized, or updated during training. \(\nabla L_{DM}\) is a vector per mini-batch, so its orthogonal complement is a high-dimensional space — the extraction of a finite basis from it is nontrivial and critical for reproducibility. The notation \(M\) (number of bases) is also undefined. This is the core technical novelty of the guidance mechanism, and its implementation details are essential.

### Minor

1. **Parameter count confound is not discussed.** Prompt Diffuser uses 0.17M tunable parameters (1.24% of PLM), while Prompt-Tuning DT uses only 0.24K (0.0018%) — a 700× difference. The paper reports these counts but does not acknowledge that some of the improvement could stem from having a larger tunable capacity rather than the diffusion mechanism specifically. This is not a fatal issue (the methods are architecturally different), but it should be discussed.

2. **Key implementation details omitted.** The number of diffusion steps \(N\) is never specified numerically (line 260 only says "restrict... to a relatively small value"). The noise prediction network \(\epsilon_\theta\) is described as "MLP-based" (line 157) with no details on hidden sizes, number of layers, or activation functions. These omissions hinder reproducibility.

3. **OOD evaluation is limited.** The out-of-distribution experiment (Table 3, few-shot column) uses only one environment (Ant-dir) and one condition. Although the ablation is acknowledged as preliminary, the OOD generalization claim would benefit from broader evidence or explicit caveats about the limited scope.

### Trivial
None.

## Nice-to-Haves

- The ablation shows that DM-only performs well on some tasks (e.g., Cheetah-dir, Cheetah-vel) while guidance helps more on others (MW reach-v2, Ant-dir). An analysis of what task properties predict when guidance is most beneficial would deepen the contribution.
- The sensitivity of the hyperparameter \(\lambda\) (Eq. 9) to performance could be briefly discussed or bounded, since the paper fixes \(\lambda=1\) across all environments.
- For the zero-shot results, even a brief description (e.g., "we condition on the goal direction as a proxy for \(y(\tau^*)\)") would resolve the ambiguity discussed in Weakness #1.

## Removed Points

- **"Prompt length comparability"**: The critic questioned whether baselines used the same prompt length \(K^*=5\). The paper explicitly states "prompts of length \(K^*=5\) are utilized" for all methods in Table 1's caption. The concern about historical usage is irrelevant to the reported comparison. **[Removed: clearly addressed by the paper]**

- **"Simple addition (ab:all) underperforms, suggesting misaligned losses"**: The paper itself identifies the gradient conflict problem and proposes gradient projection as the solution. The poor performance of simple addition is part of the paper's motivation for its technical contribution, not a weakness. **[Removed: the paper uses this observation to motivate its method]**

- **"Paper claims DM-only can only match original dataset, but DM-only performs well on some tasks"**: The DM-only loss constrains prompts to the training data distribution, which the paper acknowledges. Guidance improves upon this, and the paper shows relative improvements. The fact that DM-only performs reasonably on easier tasks is not contradictory — the claim is about exceeding the dataset quality, not about absolute performance. **[Removed: not a genuine weakness]**

- **"Statistical significance testing"**: While the lack of significance testing is noted as a Major weakness above, the specific demand for "paired t-test or confidence intervals" from runs with only 3 seeds is somewhat beyond standard RL practice. The concern about variance overlap remains valid but the strict demand for formal significance tests is weakened. **[Downgraded to Major, but softened framing]**

## Novel Insights

The key insight that emerges from synthesizing the reviews is that Prompt Diffuser's main innovation — replacing optimization-based prompt tuning with generative prompt synthesis — is clearly validated by the initialization robustness experiments (Table 2), which is the paper's strongest and most original result. However, the few-shot performance advantage (Table 1) is more nuanced than the paper presents: the method is better, but the margin is task-dependent and concentrated. The gradient projection technique, while effective in ablation, remains the most opaque component methodologically. The zero-shot result is potentially the most impactful finding (6× improvement) but is paradoxically the least documented procedure in the paper, creating a significant gap between claimed impact and evidenced support.

## Suggestions

1. **Clarify the zero-shot inference protocol**: Explicitly state what condition \(y(\tau^*)\) is used when no target-task trajectories are available. If the goal direction or task metadata serves as the condition, describe how. If unconditional generation is used, state this. A separate algorithm block or paragraph for zero-shot inference would resolve the ambiguity.

2. **Add statistical characterization of the main results**: Report per-task confidence intervals (e.g., bootstrapped across seeds) and discuss which differences are reliable. If running more seeds is feasible, do so. At minimum, add explicit caveats about tasks where the margin is within one baseline standard deviation.

3. **Specify gradient projection implementation**: Describe how the basis \(B\) is constructed and maintained. State whether it is computed per mini-batch or accumulated, and clarify the number of basis vectors \(M\). Pseudocode or a reference to an existing implementation of this technique would substantially improve reproducibility.

4. **Report missing implementation details**: Provide the numerical value of \(N\) (diffusion steps), and the architecture of \(\epsilon_\theta\) (hidden dimensions, layer count, activation function). These are standard reproducibility requirements for any paper using diffusion models.

5. **Acknowledge the parameter count difference**: Add a brief discussion of whether the larger tunable parameter budget in Prompt Diffuser (vs. Prompt-Tuning DT) might contribute to the performance gap, and ideally include an ablation controlling for parameter count.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>