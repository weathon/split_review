## Summary

This paper addresses the problem of learning the Minimum Action Distance (MAD) — the minimum number of actions to transition between two states in an MDP — from state trajectories alone, without access to reward signals or action labels. The authors propose two algorithms (MadDist and TDMadDist), a novel simple quasimetric based on ReLU operations, and an evaluation suite of environments where the ground-truth MAD is known. Empirically, MadDist substantially outperforms existing baselines (QRL and Hilbert) on representation quality metrics and downstream goal-oriented planning tasks.

---

## Strengths

- **Well-designed loss function.** The scale-invariant objective in Eq. 5 — dividing the error by the trajectory distance $(j-i)$ — is a principled improvement over the prior formulation of Steccanella & Jonsson (2022). This prevents long-horizon pairs from dominating the gradient due to larger absolute errors, and the paper clearly motivates this choice.

- **Novel evaluation suite with known ground truth.** Introducing environments (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze variants) where the exact MAD is computable is a genuine and practically valuable contribution. This enables rigorous quantitative evaluation of representation quality rather than relying on proxy measures or purely downstream task success.

- **Strong empirical performance.** MadDist achieves near-perfect or perfect success rates in all OGBench PointMaze planning tasks (Table 1), including challenging "Stitch" scenarios requiring composition of disconnected trajectories. Its representation quality (Pearson correlation, ratio CV) consistently outperforms baselines across diverse environment types, including asymmetric environments like CliffWalking and KeyDoorGridWorld where symmetric methods fail.

- **Clean quasimetric formulation.** The proposed $d_\text{simple}$ (Eq. 3) is elegant: it uses ReLU operations on embedding differences to naturally induce asymmetry and is provably a valid quasimetric satisfying the triangle inequality and latent positive homogeneity. Its simplicity is a practical advantage over IQE, which requires matrix-shaped embeddings and more complex interval union computation.

- **Appropriate action-free learning setup.** Requiring only state trajectories (no actions, no rewards) meaningfully broadens applicability to passive observation settings and transfer learning scenarios where action labels may be absent. The motivation connecting MAD to the support of the transition kernel — making it invariant to probability shifts while the support remains fixed — is well-articulated.

---

## Weaknesses

### Fatal
None.

### Major

- **TDMadDist underperforms despite being a primary contribution.** TDMadDist is listed as a main contribution alongside MadDist, yet it consistently underperforms MadDist and even QRL in most environments (Figure 3, Table 1). The paper acknowledges this ("TDMadDist underperforms the MadDist and QRL algorithm") but offers no principled explanation. Given that TD-based learning is typically beneficial for long-horizon tasks (the primary motivation for introducing bootstrapping), the persistent underperformance without clear diagnosis weakens this contribution significantly. Does the bootstrapping target degrade due to early inaccurate estimates? Is there a training instability? The lack of analysis leaves this major algorithmic contribution unexplained.

- **Downstream evaluation is narrow relative to the motivation.** The introduction prominently claims MAD "naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping." However, the only downstream evaluation is a planning task (Table 1). No experiment evaluates MAD-based reward shaping or goal-conditioned RL policy learning. This gap between the claimed scope and the actual evaluation means the central applied claims remain undemonstrated.

### Minor

- **Inconsistency in reported number of seeds.** Section 7 states "means over five independent runs" but Figure 3's caption says "three random seeds" and the description "Shaded regions indicate minimum and maximum values across three random seeds." This inconsistency should be resolved.

- **Sensitivity to $d_\text{max}$ hyperparameter unexplored.** The contrastive repulsion loss $\mathcal{L}_r$ (Eq. 6) uses $d_\text{max}$ as a hyperparameter controlling the threshold for state separation. No ablation or sensitivity analysis for this parameter is reported in the main text, despite its potential to significantly influence the learned geometry.

- **Coverage assumptions unaddressed.** The method implicitly assumes the behavior policy provides adequate coverage. The paper does not discuss what happens under poor coverage or analyze how trajectory density affects MAD estimation quality, particularly for the continuous state-space environments.

### Trivial

- Eq. 9 appears to have a parser-induced garbling (the formula includes "-12(9)"), but the accompanying prose clarifies the intent.

---

## Nice-to-Haves

- A reward shaping experiment (e.g., using $d_\text{MAD}$ as a potential-based reward bonus) would directly validate the paper's core motivation.
- An analysis of why TDMadDist underperforms — e.g., showing training dynamics, target network instability, or bootstrapping error propagation — would considerably strengthen the paper.
- Including an experiment measuring how the quality of MAD estimates degrades as dataset coverage decreases would clarify practical applicability.

---

## Novel Insights

The paper's clearest novel insight is that scale-invariant loss normalization in state-distance learning (dividing the squared error by the trajectory step count) substantially improves representation quality by preventing long-range pairs from dominating optimization. This simple modification, combined with structured quasimetric distance functions that natively support asymmetry, suggests that the existing body of symmetric MAD-learning methods has been solving a harder, unnecessarily constrained version of the problem. The introduction of $d_\text{simple}$ — a parameter-free, provably valid quasimetric based solely on ReLU differences — challenges the assumption that complex learned quasimetrics like IQE are necessary for good asymmetric distance estimation.

---

## Suggestions

- Conduct an ablation specifically diagnosing TDMadDist's underperformance (e.g., varying target network update rate $\beta$, comparing early vs. late training target quality) to either fix it or clearly characterize when TD-based MAD learning is and is not beneficial.
- Add at least one experiment demonstrating MAD estimates as reward shaping signals in a goal-conditioned RL task to substantiate the downstream application claims in the abstract and introduction.
- Clarify and reconcile the reported number of random seeds across all tables and figures.

---

## Score and Decision

The paper makes solid, well-motivated contributions: a better-designed loss, a clean quasimetric, and an evaluation suite that will be useful to the community. MadDist's empirical performance is compelling. The main detractions are the unexplained underperformance of TDMadDist (a stated main contribution), the gap between the motivational scope and the actual downstream evaluation, and the incremental nature of MadDist relative to prior formulations. On balance, the work advances the state of knowledge in representation learning for RL in a useful way.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>