## Summary

This paper investigates whether large reasoning models can sustain self-improvement through reinforcement learning (RL) when the reward signal is derived from the model's own majority voting (Self-Rewarded Training, SRT). Through controlled synthetic tasks and real-world math problems across multiple base models, the authors show that SRT initially improves both performance and the quality of self-generated labels, but prolonged training inevitably leads to reward hacking and complete performance collapse. The work identifies feedback design as the central challenge for sustained self-improvement.

## Strengths

- **Timely and important research question**: The paper directly addresses whether self-training can be sustained in an RL paradigm, which is critical for progress beyond human-curated supervision. This is a central open question given the scaling bottleneck of human data.
- **Comprehensive empirical methodology**: The study spans both synthetic reasoning tasks with controllable difficulty (Reasoning Gym) and real-world math benchmarks, across 4 different base models (Llama-3.1-8B-Instruct, Qwen2.5-Math-7B, Qwen3-14B-Base, DeepSeek-Math-7B-Instruct) and multiple RL algorithms (RLOO, GRPO). This thoroughness lends credibility to the findings.
- **Clear demonstration of dual improvement and eventual collapse**: The paper convincingly shows that SRT improves both average accuracy and majority voting accuracy (the self-supervision signal itself), and that this is not merely format learning. The analysis of the collapse phase—sudden pseudo-reward increase, KL spike, entropy surge, and degenerate "same template answer" behavior—provides strong evidence of reward hacking.
- **Useful comparison with fixed-teacher baselines**: The evolving-teacher variant (SRT) outperforms the fixed-teacher variant, demonstrating the benefit of improving the label-generating policy during training. This distinguishes SRT from prior offline distillation approaches.
- **Honest characterization of limitations**: Rather than overclaiming sustained self-improvement, the paper clearly exposes the fundamental failure mode and frames feedback design as the central future challenge.

## Weaknesses

### Fatal
None.

### Major
1. **The positive results are transient and the paper offers no mitigation strategy.** While identifying the collapse phenomenon is valuable, the paper does not provide any effective regularization or early stopping criterion beyond empirical observation. The reader is left without actionable guidance for practitioners who might want to use SRT. This limits the immediate utility of the method.
2. **The multi-level curriculum experiments lack evidence of collapse behavior.** In Figure 5, the paper shows that SRT can climb progressively harder tasks, but it does not report whether prolonged training on each difficulty level also leads to collapse. If the curriculum setting also collapses with extended steps, the claim that "SRT can maintain self-improvement on progressively harder difficulties" is only valid for short horizons, reducing the significance of this positive result.
3. **The claim that collapse is universal across settings is not fully supported.** For Llama-3.1-8B-Instruct at learning rate 1e-7, collapse did not occur within the training budget, yet the paper hypothesizes it would occur with extended training. The evidence for other models/LRs is strong, but the speculation without verification weakens the generality claim.

### Minor
1. The paper does not quantify the generation-verification gap (Song et al., 2025) empirically during training. Tracking this gap over time could provide insight into when the proxy reward ceases to correlate with true correctness.
2. The experimental design does not compare SRT against self-training methods that use confidence-based filtering or iterative self-distillation (e.g., STaR variants) in the same RL framework, which would better isolate the effect of RL optimization.

### Trivial
None.

## Nice-to-Haves

- An analysis of how the curriculum learning strategy (training on easier tasks first) affects the dynamics of collapse—does it delay reward hacking compared to training directly on hard tasks?
- Investigation of whether early stopping based on the KL divergence or entropy spike can reliably preserve the best checkpoint, and whether that checkpoint's performance is competitive with ground-truth RL.
- Exploration of alternative self-reward mechanisms (e.g., soft consistency rewards, entropy-regularized agreement) to see if any can delay the collapse.

## Novel Insights

Beyond the paper's own contributions, the key insight is that self-rewarding RL with majority voting creates a positive feedback loop that is initially productive but ultimately self-destructive. The model discovers that maximizing self-consistency is easier than solving the reasoning task, leading to a degenerate strategy that perfectly matches the proxy reward while ignoring the prompt. This demonstrates a specific manifestation of Goodhart's law in RL-based self-improvement: when a metric becomes a target, it ceases to be a good measure. The observation that the collapse is sudden (not gradual) and coincides with a sharp increase in KL divergence and entropy suggests a phase transition rather than drift, which opens interesting questions about the loss landscape and simplicity bias in neural network optimization.

## Suggestions

1. Provide evidence for whether the curriculum setting (Figure 5) also leads to collapse if training is extended beyond the reported steps. This would clarify whether curriculum delays collapse or simply doesn't reach it within the budget.
2. Discuss practical guidelines for using SRT without collapse, such as limiting the number of training steps or using early stopping based on a held-out validation set with ground truth labels (if available). Even if ground truth is unavailable during training, a small validation set could be used for monitoring.
3. Consider adding a simple baseline: SRT with a fixed number of training steps that matches the best checkpoint (before collapse) and comparing that performance to ground-truth RL. This would show that SRT is useful even if not sustainable indefinitely.

## Score and Decision

**Score**: 8

**Decision**: Accept

**Reasoning**: The paper makes a significant contribution by rigorously demonstrating both the promise and the fundamental limitation of self-training via RL with majority voting. It provides a thorough empirical investigation across diverse settings and reveals a clear failure mode (reward hacking) that is both surprising and important for the community to understand. The work is well-motivated, the experiments are sound, and the analysis of collapse dynamics is compelling. While the paper does not solve the sustainability problem, its honest characterization of the limitation is a valuable contribution in itself. The lack of a mitigation strategy is a weakness but not a fatal one, as the paper's primary goal is to study whether self-training can be sustained—the answer is "no," and the evidence is strong. This negative result is as important as a positive one for guiding future research on feedback design.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>