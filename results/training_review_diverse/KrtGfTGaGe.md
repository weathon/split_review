Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper proposes the Wasserstein Belief Updater (WBU), a model-based RL algorithm for POMDPs that learns a latent model of the environment (via a WAE-MDP) and an explicit belief update mechanism (via a feed-forward belief encoder trained without BPTT). The main claimed contributions are (1) theoretical value-difference bounds (Theorems 1 and 2) linking the quality of the learned latent model and belief representation to the expected return in the original POMDP, and (2) an algorithm that learns a belief update rule with representational guarantees that existing RNN-based methods lack. Experiments on three partially observable environments (RepeatPrevious, StatelessCartPole, SpaceInvaders) show that WBU can succeed at a long-term memorization task where R-A2C and DVRL fail.

## Strengths

- **Novel theoretical analysis with formal guarantees.** Theorems 1 and 2 provide value-difference bounds expressed in terms of local, on-policy, belief, and observation losses. These are the first guarantees of their kind for a learned belief update mechanism in POMDPs that does not rely on RNN hidden states. The bounds connect the quality of the latent model and the belief representation to the expected return — a structural contribution that existing methods like DVRL and R-A2C lack.

- **Demonstrated long-term memorization without RNNs.** In the RepeatPrevious environment (POPGym), WBU is the only method that successfully learns to recall the card suit seen 8 steps earlier, while both R-A2C and DVRL fail (Fig. 3). This provides direct evidence that the learned belief update can function as a sufficient statistic for long-range history, which is the paper's central empirical claim.

- **Clean separation of belief learning from policy learning.** The architecture decouples the belief encoder (trained via KL minimization against the latent POMDP's exact belief update) from the policy (trained via A2C on the resulting sub-beliefs). This means policy gradients do not corrupt the representation, which is solely learned by the belief encoder. This design choice is principled and well-motivated.

- **Use of normalizing flows for non-Gaussian beliefs.** The MAF-based parameterization of the belief distribution lifts the Gaussian restriction common in prior work (e.g., DVRL), extending the method to a broader class of POMDPs without distributional assumptions.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap in the loss functions.** The theoretical bounds (Thms. 1 and 2) are expressed in terms of Wasserstein distances and the observation loss L_obs (Eq. 3, defined using total variation distance involving the true observation function O). However, in practice the algorithm minimizes KL divergence as a proxy for Wasserstein (Sec. 4, "On-policy KL divergence"), and the observation loss L_obs requires computing TV(O(·|s',a), ···) which itself depends on the unknown true observation function O. The paper acknowledges these proxies (KL bounds Wasserstein in the zero-temperature limit via Pinsker; the WAE-MDP's reconstruction loss is used alongside L_obs) but does not explain how L_obs is actually optimized in the implemented system, nor does it report its empirical value. The result is that the theorems establish *conditional* guarantees relying on quantities that are not directly or verifiably minimized. While some gap between theory and practice is normal, the paper would benefit from a clearer operational mapping between the theoretical loss families and what the optimizer actually computes.

2. **Narrow experimental evaluation.** The paper tests on only three environments (RepeatPrevious, StatelessCartPole, SpaceInvaders) with only two baselines (R-A2C and DVRL, the latter from 2018). Neither DreamerV2/V3-style methods nor FORBES (which the paper cites) are compared empirically — FORBES is discussed only as related work. The StatelessCartPole results show WBU matches but does not exceed R-A2C final performance; the main positive result is on RepeatPrevious alone. With only 5 seeds per condition and no statistical significance testing, the empirical evidence for the method's generality is thin. The paper's title and framing suggest a general-purpose solution for POMDPs, but the experiments do not yet support that breadth.

3. **No ablation study.** The algorithm involves multiple interacting loss terms: local reward loss, local transition loss, on-policy reward loss, on-policy transition loss, belief loss, and an observation loss. Without ablations, it is unclear which components drive the results. This is especially important because the WAE-MDP training, the belief encoder training, and the policy training are interleaved, and the contribution of each to downstream performance is unknown.

4. **Limited reproducibility details in the paper itself.** Hyperparameters (learning rates, network sizes, optimizer, batch size, number of environment steps) are not reported. The reproducibility statement points to code in supplementary material, but the main text should include key experimental settings.

### Minor

1. **No dedicated limitations section.** The paper acknowledges the state-access assumption (Assumption 1) but does not discuss failure cases — e.g., when the learned latent model is poor, when observations are highly stochastic and the KL proxy becomes inaccurate, or when the state space is very high-dimensional and training the embedding requires many state observations.

2. **Qualitative-only t-SNE analysis.** Figure 4 shows a t-SNE visualization of beliefs with the claim that "latent beliefs clustered together have indeed close values." No quantitative metric (e.g., correlation between Wasserstein distance of beliefs and value difference, clustering purity) is provided. The belief loss plot (Fig. 3) shows a decreasing trend but is not compared against the internal representation quality of baselines.

3. **The claim that early time-steps are "easier to infer" for belief learning (motivating the no-BPTT architecture) is stated without empirical support.** While the intuition is reasonable, the paper does not provide evidence (e.g., per-timestep belief loss curves, comparison of BPTT vs. no-BPTT variants) that this architectural choice does not harm performance when the latent model is imperfect.

4. **No wall-clock time comparison.** One claimed advantage of avoiding BPTT is faster training, but no runtime comparison with R-A2C is provided.

### Trivial
None.

## Nice-to-Haves
- An experiment on a more challenging long-term memory benchmark (e.g., T-Maze, Memory) where RNN-based baselines clearly fail would substantially strengthen the claim.
- A direct comparison of the belief loss (in Wasserstein or KL terms) between WBU and baseline methods' internal representations would quantify the representation quality gap.
- Reporting how L_obs (the observation loss) evolves during training would help bridge the theory-practice gap.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. "The claim in Section 3.1 that the latent POMDP is 'equivalent' to the original is overstated." — The paper cites a formal equivalence result (Chatterjee et al., 2016) for the refined POMDP construction, not for the learned model. The critic conflated a mathematical equivalence with a learning guarantee. The paper's wording is standard and accurate.

2. "The notation in Section 3.2 is confusing because state, observation, action ~ H is a shorthand." — The paper explicitly defines this shorthand on line 270. The notation is clear in context.

3. "Missing appendix / proofs in appendix." — The parser strips appendix sections; they exist in the original submission.

4. "Formatting/style nitpicks and grammar issues." — These are parser artifacts, not author errors.

5. Criticisms questioning the existence or release status of cited works. — Per hard rules, all cited entities are assumed to exist.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify which of the theoretical losses (local reward, local transition, on-policy reward, on-policy transition, observation loss, belief loss) are directly optimized in the implementation and which are proxies — and how each proxy connects to its theoretical counterpart. A table mapping theory → practice would help.

2. Add an ablation study that isolates at minimum: (a) belief loss only, (b) belief loss + local losses, (c) all losses. This would clarify which terms drive the RepeatPrevious memorization result.

3. Expand the experimental evaluation to include at least one additional long-term memory task (e.g., from the POPGym suite) and compare against a more recent baseline (e.g., FORBES or a Dreamer variant adapted for discrete observations).

4. Report key hyperparameters in the main text and include statistical significance tests (e.g., Mann-Whitney U across seeds) for the main results.

5. Add a limitations paragraph discussing cases where the state-access assumption is violated, the latent model is poor, or the observation function is highly stochastic.

## Score and Decision

The paper makes a genuine theoretical contribution — the value-difference bounds for a learned belief update are novel and well-derived. The core algorithmic idea (separating belief learning from policy learning via a feed-forward encoder trained against the latent model's exact update) is principled. However, the experimental validation is too narrow for the claimed generality, the theory-practice gap in the loss functions is not adequately bridged, and the absence of ablation studies makes it difficult to attribute results to specific components. The paper would benefit from major revisions before being competitive for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>