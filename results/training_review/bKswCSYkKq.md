Here is my final consolidated review, verified against the paper at every point.

---

## Summary

This paper proposes NBSP (Neuron-level Balance between Stability and Plasticity), a method for continual DRL that identifies "RL skill neurons" via a correlation-based metric and then applies gradient masking to freeze those neurons during new-task learning, combined with experience replay. Evaluated on four Meta-World task pairs and four Atari game pairs, NBSP shows consistently better knowledge retention and new-task learning than EWC, ANCL, and an importance-based variant. The paper also includes an ablation revealing that the critic network is more critical than the actor for the stability-plasticity balance.

## Strengths

1. **Novel and well-motivated neuron-level framing for the stability-plasticity dilemma in DRL.** The paper convincingly argues that stability and plasticity are rooted in individual neuron behavior, and that operating at the neuron level offers finer-grained control than network-level regularization or architectural approaches. The idea of identifying task-relevant neurons via their correlation with task success is a reasonable starting point.

2. **Consistent empirical advantage across two diverse benchmarks.** On Meta-World (continuous control, binary success metric), NBSP achieves near-1.0 success rates on both tasks for all four task pairs (Figure 4). On Atari (discrete control, return-based metric), NBSP again shows best knowledge retention and competitive new-task learning (Figure 7). The advantage holds across both domains, supporting generalization.

3. **Insightful actor-critic dissection.** The ablation comparing NBSP-Actor, NBSP-Critic, and full NBSP (Figure 6) is the paper's most informative experiment. The finding that the critic plays a more critical role — and the mechanistic explanation (target-network recursion in the critic, indirect actor constraint) — is a genuine contribution that aligns with and extends prior observations (Ma et al., 2024).

4. **Simple, parameter-efficient design.** NBSP introduces no auxiliary networks, no architectural modifications, and no additional parameters — only gradient masking and standard experience replay. This practical advantage over modularity-based methods (e.g., ANCL's auxiliary network) is real and well-articulated.

## Weaknesses

### Fatal

None.

### Major

1. **No ablation isolating gradient masking from replay.** The ablation in Section 4.3 (Figure 5) compares only three conditions: Base, Replay-Only, and NBSP (masking + replay). There is no Masking-Only condition. Since replay alone provides partial improvement, the unique contribution of gradient masking cannot be quantified. The paper claims "especially the prominent role of gradient masking technique" (Section 4.3), but this claim is unsupported without a Masking-Only arm. **Why this matters:** It conflates two mechanisms, making it impossible to determine whether the success of NBSP is driven by masking, replay, or their specific interaction.

2. **No causal validation that the identified neurons encode task-specific knowledge.** The core contribution is identifying neurons that "are essential for knowledge retention." Yet the only validation is that NBSP (masking these neurons) beats Importance-based NBSP (masking different neurons). This is an indirect, comparative validation. There are no neuron perturbation experiments (e.g., ablating identified neurons during the first task to verify performance drops), no analysis of identification stability across seeds, and no justification for thresholding at the mean. **Why this matters:** The entire method hinges on whether these neurons are truly task-critical. Without causal evidence, the reader must take on faith that the correlation-based metric finds the right neurons.

3. **Critical hyperparameters unspecified.** The paper does not specify (a) the number of neurons selected as skill neurons (only "varies depending on task complexity"), (b) the replay interval \(k\), or (c) how \(T\) (the "evaluation step") is determined across the 10 evaluation episodes. These are not trivial implementation details — they directly affect the method's behavior and reproducibility.

### Minor

1. **Statistical claims not backed by tests.** The paper uses phrases like "significantly outperforms existing approaches" (abstract) but provides no formal significance tests — only standard error bars. With only 5 seeds and 4 task pairs per benchmark, the results could be legitimate but the claim of significance is asserted rather than demonstrated. (Standard error bars are shown, which is standard for the field, so this weakens but does not invalidate the claim.)

2. **Limited baseline scope, though not unreasonable.** The paper compares against EWC, ANCL, and a self-variant. This covers one regularization method and one modularity method. A random-neuron freezing baseline (testing whether any frozen subset achieves similar results) is notably absent and would directly test whether the identification method matters or just the act of freezing some neurons.

3. **The neuron identification metric uses the same data for threshold computation and evaluation.** The standard activation \(\bar{a}(\mathcal{N})\) and standard evaluation \(\bar{q}_\theta\) (Eqs. 1–2) are computed from the same \(T\) steps used to compute the positive accuracy (Eq. 3). This creates a circular dependency that could inflate the accuracy measure. A held-out validation set would be more appropriate.

4. **Atari results are weaker but still supportive.** As the paper's figures show (and the text acknowledges implicitly), on some game pairs all methods including NBSP experience first-game performance drops. The claim "successfully strikes a balance" is more relative than absolute on Atari compared to Meta-World.

### Trivial

- Figure 4 x-axis labels are missing — the unit of the x-axis (presumably training steps) is not stated.
- The description of \(T\) as "the evaluation step" (line 58) is ambiguous; the paper later clarifies that evaluation uses 10 episodes, but the connection to \(T\) in Eq. (1) is never explicitly made.

## Nice-to-Haves

- **Random-neuron freezing baseline.** Comparing NBSP to freezing an equal number of randomly chosen neurons would directly test whether the identification method matters.
- **Longer task sequences (>2 tasks).** The paper only evaluates 2-task pairs. Testing cumulative forgetting and plasticity over longer sequences would better demonstrate robustness.
- **Stability analysis of neuron identification.** Reporting whether the identified RL skill neurons are consistent across random seeds or across different evaluation runs would help assess reliability of the method.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"First" neuron-level work overclaim (Harsh Critic #4).** The paper claims "first work that addresses both stability and plasticity loss simultaneously in DRL at the level of neurons." Sokar et al. (2023), cited in the paper, addresses plasticity loss (dormant neuron recycling) but not stability. The claim is specifically about addressing **both** simultaneously, which the paper does and Sokar et al. does not. This criticism is factually incorrect.

- **"Ignores modularity-based methods" (Section-by-Section Notes).** The paper explicitly cites Anand & Precup (2024) as a modularity-based method (line 14) and includes ANCL (a modularity method) as a baseline. This criticism is factually incorrect.

- **"Missing related works" (general).** Per guidelines, I do not list missing related works, as I cannot independently verify their content.

- **Reproducibility nitpicks about standard CleanRL hyperparameters.** The paper states it uses CleanRL's SAC implementation, which is a well-documented, standard codebase. Concerns about unspecified architectural details beyond the method-specific parameters (\(k\), number of neurons) are standard-practice nitpicks typical of a parser-stripped submission.

- **Formatting/style nitpicks, typos, grammar issues.** These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful insight worth noting: the absence of a Masking-Only ablation and the lack of causal validation for the neuron identification method are interconnected gaps — together they leave the paper's central mechanism (that the *specific* identified neurons drive the benefit) only weakly supported. Conversely, the actor-critic dissection finding is genuinely interesting and emerges as the paper's strongest empirical contribution, independently of whether the identification method is fully validated.

## Suggestions

1. **Add a Masking-Only ablation.** This is the single most important missing experiment. Without it, the contribution of gradient masking cannot be separated from that of experience replay.

2. **Add a random-neuron freezing baseline.** This would directly test whether the specific identification method matters, or whether freezing any fixed subset of neurons (of the same size) yields similar results.

3. **Provide causal validation of skill neurons.** The simplest experiment: on the first task alone, ablate (zero-out activations of) the identified neurons and measure performance drop. A significant drop would confirm they encode task-relevant knowledge.

4. **Specify the number of selected neurons per task and the replay interval \(k\).** These are essential for reproducibility.

5. **Clarify how \(T\) (evaluation steps) relates to the 10-episode evaluation protocol described in Section 4.1, and use a held-out set for computing the standard activation threshold.**

## Score and Decision

This paper tackles an important problem with a clean, well-motivated idea, and it produces competitive empirical results on two benchmarks. The actor-critic ablation is a genuine contribution. However, the paper has significant evidential gaps: the core neuron identification method lacks causal validation, the ablation design cannot isolate the effect of gradient masking from replay, and several key hyperparameters are unspecified. These gaps prevent the paper from being fully convincing in its current form. The contributions are real but incompletely supported.

**Score:** 5.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>