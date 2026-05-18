Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper introduces FB-CPR, which combines forward-backward (FB) zero-shot reinforcement learning with a latent-conditioned distribution-matching regularizer that steers unsupervised policies toward imitating unlabeled motion capture trajectories. The result is a behavioral foundation model for a 358-dimension, 69-action SMPL humanoid that can solve reward optimization, goal reaching, and motion tracking tasks in zero-shot (no task-specific training or planning). Experiments across 45 reward tasks, 50 goal poses, and 990 test motions from AMASS show FB-CPR achieves 73.4% of task-specific top-line performance and outperforms the closest zero-shot competitor (ASE) by a factor of 1.4× across all categories, with a human evaluation confirming more natural behaviors than pure reward maximization.

## Strengths

1. **Novel algorithm with strong zero-shot performance on complex humanoid control.** FB-CPR is the first method combining FB zero-shot RL with behavior regularization, enabling zero-shot whole-body control in a 358D state / 69D action space. Table 1 shows it attains 73.4% of task-specific top-line performance and outperforms ASE (the closest zero-shot baseline) by 1.4× across all evaluation categories. The method generalizes across three qualitatively different task types (reward, goal, tracking) without any task-specific fine-tuning.

2. **Extensive and rigorous evaluation across diverse tasks and metrics.** The paper evaluates on 45 reward tasks, 50 goal-reaching poses, and 990 test motions from AMASS, using returns, success rate, proximity, EMD, and tracking success rate, all with mean and std over 5 seeds. A human evaluation with 50 raters (Figure 3) adds qualitative validation — FB-CPR is rated as equally successful as TD3 at solving tasks but significantly more human-like. This breadth of evaluation convincingly demonstrates the model's generality.

3. **Comprehensive ablation studies isolating each component.** Figure 4 systematically ablates: removing the unsupervised FB term hurts performance (top right), a latent-conditioned discriminator outperforms state-only (top left), online FB-CPR substantially beats offline FB-AW (bottom right), and scaling model capacity and dataset size both improve results (bottom left). These experiments provide clear evidence that each design choice is necessary.

4. **Principled technical contribution with clear distinction from prior work.** The paper derives how to embed unlabeled trajectories into the FB latent space via ER_FB and use a latent-conditional discriminator for distribution matching (Section 3, Eqs. 7–11). It explicitly contrasts this design with related methods (marginal state matching in AMP/ASE, end-to-end encoders in CALM) and shows why the conditional formulation matters — the FB representation serves as both motion encoder and unsupervised value function, not just an embedding.

5. **Human evaluation demonstrates behavioral quality that reward metrics miss.** Despite TD3 achieving higher numeric reward, the human study (Figure 3) shows FB-CPR and TD3 have similar task success rates, but FB-CPR is rated as more human-like. This confirms the regularization is doing exactly what it is designed to do — producing natural behaviors rather than exploiting reward hacks.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by evidence. The issues below are addressable gaps, not structural flaws.

### Minor

1. **The controlled comparison with ASE does not fully rule out architecture/capacity effects.** The paper states "We use a comparable architecture and hyperparameter search for all models" (line 169), but does not explicitly confirm whether ASE's network capacity (width, depth) matched FB-CPR's. The scaling experiment (Section 4.2) shows that a 2× larger model yields significantly improved performance over the 1× model reported in Table 1, which naturally raises the question: is FB-CPR's 1.4× advantage over ASE primarily driven by the conditional discriminator or by a better-tuned/taller actor-critic backbone? The ablations in Figure 4 (top left, top right) address this partially — they show that both the latent-conditioned discriminator and the unsupervised FB term contribute — but do not directly compare against a version of ASE with identical network capacity. This is a gap in the experimental reasoning, not a fatal flaw, because the method clearly works and the ablations validate the core design.

2. **The discriminator's non-stationary target is acknowledged but not analyzed.** The discriminator relies on ER_FB to embed trajectories, but ER_FB uses the backward embedding B which is being trained concurrently (line 206 acknowledges this: "a more formal and theoretical understanding of these components is still missing"). This creates a moving target — the "true" embedding of a given trajectory changes as B updates. The paper does not discuss whether this causes practical instability or whether it merely acts as an additional source of stochasticity. The experiments show the method works robustly, so the concern is empirical rather than structural, but a diagnostic (e.g., tracking the embedding variance of held-out trajectories over training) would strengthen the contribution.

3. **The offline FB-AW comparison uses data collected by FB-CPR itself, not a purely unsupervised dataset.** The paper collates all 30M transitions from an online FB-CPR agent and trains FB-AW offline on this data (line 191). As the authors note, "no dataset with our criterion exists," but this conflates the effect of the data distribution (already shaped by the regularization) with the offline learning algorithm. A comparison against offline FB trained on data from a purely unsupervised exploration policy (e.g., uniform latent sampling or curiosity-driven exploration) would be a cleaner test. The paper's conclusion "highlighting the difficulty of offline policy optimization" is too broad given this confound.

### Trivial

1. **The success-rate threshold for tracking is not specified in the main text.** The paper defines tracking success as remaining "within a given distance (in joint position and rotation)" (line 159), citing Luo et al., 2021. The exact threshold should be stated in the main experimental section for self-containedness.

2. **Discriminator regularization techniques are not discussed.** The discriminator uses a standard GAN loss (Eq. 9), but the paper does not specify whether any stabilization techniques (gradient penalties, spectral normalization, label smoothing) were used. Given the 358D state space and 8902 training motions, overfitting could be a concern.

3. **The planning-baseline data pipeline could be better described.** The paper builds an action-labeled dataset for MPPI/DIFFUSER/H-GAP by combining replayed Goal-GAIL trajectories with FB-CPR's replay buffer (line 167). It is not explicitly stated whether all planning methods used the identical dataset split, though this seems likely. The poor performance of MPPI and H-GAP (not reported in Table 1) suggests any data advantage did not bias the comparison, but clarification would help.

## Nice-to-Haves

- Characterize the non-stationarity of the discriminator target by tracking ER_FB embeddings of a fixed set of held-out trajectories over training and measuring their variance.
- Analyze which reward/goal tasks are hardest relative to the training set's motion coverage, connecting difficulty to dataset composition.
- Provide explicit confirmation (e.g., parameter counts) that ASE's architecture matched FB-CPR's at the 1× scale.
- Extend the wall-clock "zero-shot" timing (currently given for reward tasks: ~12 seconds) to goal-reaching and tracking inference.

## Removed Points

- **"The definition of 'behavioral foundation model' is loose / ASE is a predecessor"**: The paper clearly cites ASE, discusses differences (zero-shot reward optimization capability that ASE lacks), and stakes a defensible claim about being the *first* BFM for *all three* task types in zero-shot. This is a framing preference, not a weakness. Removed as scope creep.
- **"The paper never checks whether reward/goal performance correlates with motion diversity"**: Nice-to-have, not a weakness. Removed to Nice-to-Haves.
- **Most of the "Missing Parts and Places to Improve" section**: These are suggestions the critic themselves frames as "not required for acceptance" and are either already addressed in the appendix or are presentation preferences.
- **Critic's suggestion about training offline FB on random/curiosity data for the offline ablation**: Moved to Nice-to-Haves since it is a valid methodological ideal but the paper pragmatically acknowledges the dataset constraint.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the authors themselves do not already make.

## Suggestions

1. Add a controlled experiment running ASE with the exact same network architecture (parameter counts, layer widths) as FB-CPR's 1× model, even if only on the reward-based tasks, to decouple method effects from capacity effects.
2. Add a diagnostic figure tracking the ER_FB embedding of a fixed set of held-out trajectories over the course of training to characterize the non-stationarity of the discriminator target.
3. State the tracking success threshold (distance in joint position/rotation) explicitly in the main experimental section rather than deferring entirely to Luo et al., 2021.
4. Note whether any GAN stabilization techniques (spectral normalization, gradient penalties) were applied to the discriminator.
5. Clarify in Section 4 that all planning baselines (MPPI, DIFFUSER, H-GAP) were trained on the identical action-labeled dataset.

## Score and Decision

This paper presents a well-motivated algorithmic contribution with thorough empirical validation. The weaknesses identified are minor — they concern experimental exposition and control rather than threatening the core claims. The method is clearly described, the ablations are informative, and the human evaluation provides a meaningful qualitative dimension. The paper would benefit from the suggested controlled comparison with ASE and discriminator stability analysis, but these do not undermine acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>