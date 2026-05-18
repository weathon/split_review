Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me write the final consolidated review.

---

## Summary

This paper proposes DrS (Dense reward learning from Stages), a method that learns reusable dense rewards for multi-stage robotic manipulation tasks. The key idea is to train per-stage discriminators to classify success vs. failure trajectories (using the sparse reward signal) rather than agent vs. demonstration trajectories as in GAIL/AIL — a distinction that remains discriminative at convergence because the gap between success and failure does not shrink as the policy improves. Experiments on three ManiSkill task families with 1,000+ object variants show that the learned reward, when frozen and reused to train RL agents on unseen test objects, substantially outperforms semi-sparse rewards and prior reward-learning baselines, approaching human-engineered reward quality on two of three tasks.

## Strengths

1. **Clean, principled insight for reusable rewards**: The paper correctly identifies why GAIL-style rewards are not reusable — at convergence the discriminator outputs 1/2 for both agent and demonstration trajectories. Replacing the agent/demo classification target with success/failure classification (derived from the sparse reward) removes the adversarial dynamic and preserves discriminative information. This is well-explained in Section 4.1 and Fig. 2, and the distinction from AIL is clearly articulated.

2. **Strong empirical evidence across substantial scale**: Experiments on three task families with non-overlapping train/test objects (74→1600 YCB→EGAD for Pick-and-Place, 10→50 faucets, 4→6 cabinets) provide a rigorous test of reusability. DrS consistently outperforms semi-sparse rewards and both VICE-RAQ and ORIL across all tasks. On Pick-and-Place and Turn Faucet, DrS achieves success rates comparable to human-engineered rewards (Fig. 5).

3. **Dramatic reduction in human engineering effort with demonstrated robustness**: The paper provides a concrete comparison — the human-engineered reward for Open Cabinet Door requires "over 100 lines of code, 10 candidate terms, and tons of 'magic' parameters," while DrS only needs two boolean stage indicators. Ablations (Fig. 6, 7) show the method is robust to different numbers of stages and threshold definitions, meaning the user does not need to engineer stages precisely.

4. **Practical algorithmic design**: The method integrates off-policy SAC with per-stage replay buffers, enabling efficient data reuse and stable discriminator training without the on-policy overhead of original GAIL. This design choice directly supports the strong empirical results.

## Weaknesses

### Fatal
None.

### Major

1. **No empirical analysis of discriminator behavior over training, leaving the core reusability claim partially unsubstantiated.** The paper argues (Section 4.1) that the success/failure gap "remains intact and does not shrink," but never actually measures this. As the policy improves, the agent generates fewer failure trajectories, so the negative data becomes increasingly stale. The discriminator could be exploiting temporal or trajectory-level features of old failures that do not generalize to new test tasks. A simple experiment — measuring discriminator accuracy on held-out success/failure trajectories from a random policy and a near-optimal policy at various points during training, or plotting the distribution of discriminator outputs for both classes — would substantially strengthen the paper. Without this, the reusability claim is plausible but not firmly grounded.

2. **Reusability is demonstrated only across object variants, despite broader motivational framing.** The introduction motivates reusability by arguing that rewards can transfer across different gripper morphologies (two-finger vs. three-finger gripper) and action spaces. The experiments, however, only test transfer across different objects within the same task family — same robot, same action space, same stage indicator definitions. This is a meaningful but considerably narrower form of reusability. The paper should either narrow the claims to match the evidence or demonstrate transfer across at least one more challenging dimension (different robots, action spaces, or sim-to-real).

### Minor

3. **The reward learning phase itself is not evaluated.** The paper evaluates DrS entirely by reusing the learned reward on test tasks, but never reports whether the reward can support successful RL on the *training* tasks it was learned from. This is a basic sanity check — if the closed-loop process (Algorithm 1) fails on training objects, the fact that it works on test objects would demand explanation. The fine-tuning results (Section 5.4.2) partially address this by showing the byproduct policy can be fine-tuned, but direct training-task performance curves would be more informative.

4. **It is unclear whether demonstrations were used in the experiments.** The algorithm specifies demonstrations are optional (Algorithm 1), and the abstract says "from sparse rewards and demonstrations if given," but the experimental section never states whether demonstrations were actually provided for any of the three task families. If they were used, the setup should be described; if not, this is a stronger result that should be highlighted. This needs clarification.

### Trivial

5. **Minor gaps in documentation**: The paper mentions early-stopping discriminator training "once its success rate is sufficiently high" but does not define this threshold or analyze its sensitivity. The α hyperparameter sensitivity is not explored beyond noting α<1/2 preserves ordering.

## Nice-to-Haves

- The two successful baselines (VICE-RAQ and ORIL) both achieve zero success, making parts of the comparison less informative. Adding a contrastive-embedding-based reward (e.g., VIP, R3M) or a recent success-conditioned method would provide a more meaningful signal about DrS's relative position among data-driven reward learning approaches.
- An analysis of computational cost scaling with the number of stages (N separate buffers and discriminators) would help practitioners assess the method for tasks with many stages.
- A robustness experiment showing how few training objects are needed for effective reward reuse (e.g., training on only 5 YCB objects vs. 74) would strengthen the practical claims.

## Removed Points

These points from the reviewers were evaluated against the paper, found to be inaccurate, overblown, or outside the paper's scope, and are noted here only for transparency:

- **Stage indicator "contradiction" (Critic Weakness 3)**: The paper clearly states "stage indicators are only required during RL training, but not required when deploying policy to the real world" (line 38, line 140). The reward reuse phase IS RL training — the paper never claims otherwise. This criticism is based on a misreading; the paper is internally consistent.
- **VICE-RAQ/ORIL failure making comparison "trivial"**: The paper acknowledges these baselines failed during their own reward learning (Section 5.3). The primary comparison is against semi-sparse rewards (a natural baseline for this setting) and human-engineered rewards (the upper bound). The paper beats both meaningfully. The critic's preferred baselines (R3M, VIP) are representation learning methods, not reward learning methods for this setting.

## Novel Insights

The key insight — that replacing the agent/demo classification target with success/failure classification eliminates the convergence-to-1/2 problem that makes GAIL rewards non-reusable — is simple and effective. The reviewer-generated critiques surface an interesting subtlety: the paper's argument that the success/failure gap "does not shrink" is theoretically correct (no adversarial pressure to close it), but the *practical* concern is whether the gap remains *informative* as the failure distribution shifts from policy-induced failures to historical/stale failures. A properly designed analysis of discriminator generalization would distinguish whether DrS works because the discriminator learns genuinely reusable features of task progress, or because the empirical evaluation happens to involve test objects where the same features are discriminative. The paper would benefit from engaging with this distinction explicitly.

## Suggestions

1. Add an analysis of discriminator behavior: plot accuracy on held-out success/failure trajectories from different policy checkpoints throughout training, and show the distribution of discriminator outputs for both classes at convergence. This directly addresses the most concerning gap in the paper's evidence.
2. Report training-task performance curves from the reward learning phase as a basic sanity check.
3. Explicitly state whether demonstrations were used in each experiment and, if so, how many trajectories per task.
4. Either narrow the motivation to match the experimental scope (cross-object reusability) or add at least one experiment demonstrating cross-morphology or cross-action-space transfer.
5. Report the early-stopping threshold for discriminator training and briefly discuss its sensitivity.

## Score and Decision

This is a solid paper with a clean, practical idea and strong empirical validation at a meaningful scale. The core contribution — that replacing the adversarial agent/demo classification with success/failure classification yields reusable rewards — is well-motivated and convincingly demonstrated on 1,000+ task variants. The method drastically reduces the human effort required for reward engineering in multi-stage manipulation tasks. The weaknesses are genuine but addressable: missing discriminator analysis, a modest gap between motivation and evaluation scope, and some documentation gaps. None of these threaten the paper's core claims, and they can be addressed with additional analysis and more precise framing.

**Originality**: Good — the success/failure distinction over GAIL's agent/demo distinction is a simple but novel contribution.  
**Importance**: Good — reducing reward engineering effort is a practically significant problem.  
**Claims**: Mostly well-supported, with one notable gap (discriminator analysis).  
**Soundness**: Good — experimental methodology is appropriate and ablations are well-designed.  
**Clarity**: Good — the method is clearly explained and well-illustrated.  
**Value**: Good — the method is practical and could be adopted by practitioners.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>