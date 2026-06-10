## Summary

ADVICE proposes a post-shielding technique for safe RL exploration in black-box environments. It uses a contrastive autoencoder, trained on data from an initial unprotected interaction phase, to learn latent representations of safe/unsafe state-action pairs, then applies KNN classification in that latent space to evaluate and correct actions during training. An adaptive mechanism dynamically adjusts the safety threshold based on recent versus historical violation rates. The paper evaluates on Safety Gymnasium tasks against DDPG, DDPG-Lag, and a Tabular Shield baseline.

## Strengths

- **Novel application of contrastive learning to post-shielding**: The use of a contrastive autoencoder to learn latent safety embeddings from unlabeled RL interaction data — without requiring prior knowledge of the environment or safety specifications — is a methodologically sound and practically relevant idea. The latent space visualizations (Figure 3, right column) provide qualitative evidence that the model separates safe from unsafe features.

- **Adaptive safety threshold with explicit sensitivity analysis**: The double-sliding-window adaptation mechanism (Equations 6–8, Algorithm 1) that adjusts the safety threshold K based on recent versus historical violation rates goes beyond static shielding approaches. Table 1 provides a sensitivity analysis over different ($h_r$, $h_d$) configurations, showing how these parameters affect K's behavior and demonstrating the system's dynamics empirically.

- **Zero prior knowledge requirement**: Unlike LTL-based shielding and approaches requiring pre-training or system models, ADVICE operates solely on information captured during standard RL interaction. This is a genuine differentiator from prior shielding literature and is clearly evidenced in the paper's framing.

- **Evaluation in continuous high-dimensional spaces**: The paper tests on Safety Gymnasium environments with continuous state/action spaces, a setting where tabular shielding is intractable and many prior shielding methods cannot scale. The core results show ADVICE reducing cumulative safety violations compared to baselines despite a 1000-episode unprotected cold-start phase.

## Weaknesses

### Fatal
None.

### Major

- **Missing neural network architecture and training hyperparameters for the contrastive autoencoder**: The paper does not specify the CA's architecture (number of layers, layer sizes, latent dimension, activation functions), optimizer, learning rate, batch size, number of training epochs, or how the MSE and contrastive losses are weighted relative to each other (they are described as "optimised simultaneously" with no balancing scheme, line 100). Since the CA is the core component that learns the safety embedding, this is a significant reproducibility gap. The reader cannot reconstruct, verify, or build upon the method without this information.

- **Potentially anomalous data in the adaptation sensitivity table (Table 1)**: For several ($h_r$, $h_d$) configurations, the reported "Consecutive Episodes" values for K=3,4,5 do not sum to the total 1000 episodes. For example, ($h_r$=4, $h_d$=25) sums to 169.07+22.10+181.35 = 372.52. Since K is bounded between $\lceil K^{max}/2\rceil=3$ and $K^{max}=5$, every episode should be accounted for. Some configurations sum close to 1000 (e.g., 977 for $h_r$=4, $h_d$=10) while others are far lower, suggesting either a reporting inconsistency or a definitional mismatch between the column label and what is actually measured (e.g., average streak length vs. total episodes). This undermines the supporting evidence for the adaptation analysis until clarified.

### Minor

- **Cold-start violations are not separated from post-shield violations in cumulative plots**: The core results (Figure 3) report cumulative safety violations over the full training run, including the 1000-episode cold-start phase where the agent is completely unprotected. The paper acknowledges this asymmetry and argues it makes the results "even more affirmative" (line 282), but a breakdown of violations before vs. after shield activation would more directly substantiate the central claim and allow readers to assess per-episode violation rates post-shield.

- **Only 3 random seeds for stochastic environments**: The results are averaged over 3 independent runs (line 239). For Safety Gymnasium environments with randomized obstacle/goal positions, this provides limited statistical power. While confidence intervals (standard error) are shown, the paper uses categorical language ("significantly reduces") without formal significance testing. More seeds would strengthen confidence in the reported trends.

- **Tabular Shield baseline is insufficiently specified**: The baseline is described as "a DDPG agent with a discretised (1 decimal place) table of terminal state-action pairs" (line 236). For the continuous, high-dimensional Safety Gymnasium state spaces, a literal table indexed by discretized state dimensions is computationally intractable. The paper does not describe how the table is organized or queried, nor whether approximate matching is used. Without this specification, the comparison cannot be properly assessed.

- **Transfer learning evidence is thin**: The transfer learning experiment (Section 5.3) is described in roughly 11 lines with only a qualitative percentage ("over 50%") and no accompanying figure, table, or numerical breakdown. The broken figure at lines 329–335 may indicate a missing figure. As presented, this potentially strong result lacks sufficient empirical support.

- **DDPG-Lag hyperparameters not justified**: The Lagrangian parameters ($\lambda=0.1$, $a=0.01$, line 235) are stated without justification or reporting of whether they were tuned. In Lagrangian methods, the multiplier learning rate critically affects behavior; an untuned value could make the baseline appear weaker than its optimal configuration, creating a risk of unfair comparison.

- **Action discretization granularity for candidate generation not specified**: Algorithm 1 (line 122) generates candidate actions by quantizing the continuous action space and taking the Cartesian product, but the paper never states the discretization level. This affects both reproducibility and the assessment of computational feasibility for higher-dimensional action spaces.

- **Loss balancing between MSE and contrastive loss not specified**: The paper states both losses are "optimised simultaneously" (line 100) but provides no weighting scheme. Contrastive autoencoders are known to be sensitive to this trade-off, and the omission hinders reproducibility.

### Trivial
None.

## Nice-to-Haves
- A per-episode or post-shield-phase breakdown of violation rates would cleanly address the main evaluation concern.
- Testing against additional standard safe RL baselines (e.g., PPO-Lagrangian, CPO) would broaden the comparison beyond DDPG-based methods.
- Computational cost measurements (time per episode, shield inference latency) would aid practitioners in assessing deployability.
- Quantifying how many features fall into each category (safe, unsafe, inconclusive) during the collection phase would clarify the training signal available to the CA.

## Removed Points
These points from the input reviews were removed with justifications:

- **"Novelty claim too broad" (Harsh Critic)**: The reviewer claimed the statement "first research work that investigates shielding for safe RL exploration in black-box environments" is too broad because Lagrangian methods also work in such settings. However, Lagrangian methods use CMDP formulations, not shielding. The claim is specifically about *shielding*, which the paper correctly distinguishes from Lagrangian methods in the related work. The criticism conflates categories.

- **"Significant amount of data collection" characterization (Harsh Critic)**: The reviewer claimed line 28 characterizes Lagrangian methods as requiring significant data collection. The actual text reads "Other research collects data in the environment before training... This requires a significant amount of data collection" — the antecedent of "this" is the *other research* (pre-training approaches), not Lagrangian methods. The reviewer misread the paragraph.

- **Limitations section framing criticism (Harsh Critic)**: The reviewer objected to the Limitations statement that ADVICE "still significantly reduces violations compared to methods that start learning from timestep t0." This is a reasonable claim about total cumulative violations. The asymmetric comparison is explicitly and repeatedly acknowledged by the paper (lines 282, 392). The criticism adds nothing new.

- **Fallback behavior as weakness (Harsh Critic)**: The reviewer noted that when no safe alternative is found, the original action is used, meaning "the shield provides no safety guarantee." This is a transparently stated design characteristic (line 164), not a hidden flaw. Every learned safety system with imperfect recall has this property. The paper does not claim formal guarantees.

- **Generic/superficial strengths (Strength Finder)**: Claims about "compatibility with high-dimensional continuous spaces" and "zero prior knowledge requirement" were retained in the strengths above but re-grounded in specific evidence from the paper rather than accepted as general statements.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Provide complete architecture and training details for the contrastive autoencoder (layer sizes, latent dimension, activations, optimizer, learning rate, batch size, loss weighting scheme).
2. Clarify the definition of "Consecutive Episodes" in Table 1 and resolve the apparent numerical discrepancy. If the metric measures average streak length rather than total episode count, rename the column and explain.
3. Add a clear breakdown of safety violations during the cold-start phase vs. after shield activation (e.g., separate curves in Figure 3 or a per-phase table).
4. Run additional seeds (at least 5–10) and report standard deviations rather than standard errors.
5. Include a supplementary table of numerical results alongside the figures for precise comparison.
6. Specify the action discretization granularity used in candidate generation (Algorithm 1, line 122).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>