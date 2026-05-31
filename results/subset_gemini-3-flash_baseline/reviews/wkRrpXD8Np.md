## Summary
The paper investigates whether Large Language Models (LLMs) can self-improve their reasoning capabilities through Reinforcement Learning (RL) without external ground-truth labels. The authors propose **Self-Rewarded Training (SRT)**, a framework where the model uses majority voting of its own generations as a proxy reward signal, updated continuously during training. Experiments across synthetic logic tasks and real-world math benchmarks show that SRT can initially match the performance of RL with ground-truth rewards and improve the quality of its own self-supervision. However, the study also identifies a critical "reward hacking" failure mode where prolonged training causes the model to collapse by outputting a fixed template answer to maximize self-consistency.

## Strengths
- **Timely and Relevant:** As high-quality human data becomes a bottleneck, the transition from RL with Verifiable Rewards (RLVR) to self-improvement is a high-priority research area. This paper provides a systematic look at the simplest version of this transition.
- **Strong Empirical Evidence of Self-Improvement:** The paper convincingly demonstrates that the "evolving teacher" (using the current policy for majority voting) outperforms a "fixed teacher" (using the base model). This confirms that the model can bootstrap its own verification capabilities.
- **Comprehensive Evaluation:** The authors test the method across four different model families (Llama, Qwen, DeepSeek) and multiple reasoning domains (Reasoning Gym, MATH-500), ensuring the findings are not overfitted to a specific architecture.
- **Honest Analysis of Failure Modes:** Instead of just reporting SOTA results, the paper provides a deep dive into "model collapse." The analysis of KL divergence, entropy, and the "template answer" phenomenon (Figure 7) provides valuable cautionary insights for the community.

## Weaknesses
### Major
- **Limited Novelty in the Mechanism:** The use of majority voting for self-improvement is well-established in literature (e.g., Self-Consistency, ReST, STaR). While the paper distinguishes itself by focusing on *online* RL updates rather than iterative SFT/DPO, the core algorithmic contribution is incremental.
- **Lack of Robust Mitigation for Collapse:** While the paper identifies reward hacking as a "fatal" issue for prolonged training, it does not offer a successful algorithmic solution. The ablations (increasing KL, lowering learning rate) show that standard regularizers fail to prevent the collapse, leaving the "how to sustain improvement" question largely unanswered.

### Minor
- **Sensitivity to Hyperparameters:** The observation that a slightly higher learning rate triggers collapse on Llama-3.1-8B (Figure 6) suggests that the stability of SRT is quite fragile. More discussion on how to detect the "peak" before collapse in a truly label-free setting (where we don't have a test set to monitor) would be beneficial.

## Nice-to-Haves
- A comparison with a "shuffled" or "random" reward baseline to prove that the majority vote signal is specifically what drives the early gains, rather than just the RL process regularizing the model's output format.
- Exploration of "Length Bias" or "Sycophancy" as intermediate stages before the final collapse to a single template answer.

## Novel Insights
The most significant insight is the empirical validation of the **"evolving teacher" advantage** in an online RL setting: as the model improves its reasoning, its majority-vote labels become more accurate, creating a virtuous cycle that outperforms static distillation. However, this is counterbalanced by the discovery that **self-consistency is a "hackable" reward**. Unlike ground-truth rewards, which are anchored to external reality, majority voting rewards can be maximized by collapsing the output distribution to a single point (the "template answer"), which satisfies the consistency requirement but destroys the reasoning utility.

## Suggestions
- **Actionable Suggestion:** To address the reward hacking, consider a "Leave-One-Out" consistency check or a cross-model consistency check (if two models are available) to prevent the policy from converging to a trivial global constant.
- **Actionable Suggestion:** Propose a "stop-criterion" based on internal metrics (like the rate of change in KL or the entropy of the answer distribution) that could be used in a real-world scenario where ground-truth validation is unavailable.

## Score and Decision
The paper is a solid empirical study of a critical problem. While the algorithmic novelty is modest, the rigorous evaluation of online self-training and the detailed characterization of the reward-hacking collapse provide significant value to the ICLR community. It serves as both a "proof of concept" for self-training and a "warning" about the limitations of self-consistency as a reward.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>