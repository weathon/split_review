Here is my consolidated final review, after cross-checking every claim against the paper.

---

## Summary

This paper introduces a reward-free pre-training framework for Generative Flow Networks (GFlowNets). It trains an outcome-conditioned GFlowNet (OC-GFN) to reach any target outcome using only self-supervised exploration data from a GAFlowNet, then adapts the pre-trained model to downstream tasks via an amortized predictor that approximates an otherwise intractable marginalization over outcomes. Experiments on GridWorld, bit sequences, TF binding, RNA generation, and antimicrobial peptide design show that OC-GFN can achieve near-100% success in reaching arbitrary outcomes and that the fine-tuned policy outperforms GFN-from-scratch, MCMC, and DQN baselines in mode discovery and top-K scores.

---

## Strengths

1. **Novel and well-motivated formulation of reward-free pre-training for GFlowNets.** The paper identifies a genuine gap — GFlowNets must be trained from scratch for each new reward — and proposes outcome conditioning as a principled solution. The idea of learning a single OC-GFN that can be converted (in principle without retraining, via Eq. 6) to sample from any reward that is a function of the outcome is elegant and grounded in GFlowNet theory (citing Bengio et al. 2023).

2. **Contrastive training + outcome teleportation demonstrably solve the sparse-reward and long-horizon challenges in pre-training.** Ablation studies on GridWorld (Fig. 2b–d) cleanly isolate the contributions: disabling outcome teleportation degrades sample efficiency in larger maps, and disabling both OT and contrastive training causes collapse as the outcome space grows. In bit sequence generation, OT is essential for learning at all (Fig. 4a–c). These ablations are convincing evidence that the proposed techniques are the key enablers.

3. **Consistent and substantial improvements over multiple baselines across diverse biological sequence design tasks.** OC-GFN with the amortized predictor discovers more modes faster and achieves higher top-100 scores than GFN-from-scratch, MCMC, and DQN on TF binding (Fig. 8), RNA (Fig. 9), and AMP generation with a search space of 20⁵⁰ (Fig. 10). The t-SNE visualization in Fig. 8e provides qualitative confirmation of broader coverage. This across-the-board improvement on practical tasks is the paper's strongest empirical contribution.

4. **The amortized predictor is a practical solution to a real computational bottleneck.** The paper correctly identifies that the Monte Carlo marginalization in Eq. 4 is intractable for large outcome spaces. Learning \(N(s'|s)\) with a GFlowNet-like constraint (Eq. 11) is a clever approach, and the GridWorld visualization (Fig. 1d) shows the amortized policy matches the target distribution nearly as well as the Monte Carlo version.

5. **Diverse trajectory generation under outcome conditioning.** The paper visualizes (Fig. 3) that OC-GFN learns multiple distinct paths to the same target, a property that standard goal-conditioned RL typically lacks and that can aid generalization to structurally similar downstream tasks.

---

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in the total compute budget for downstream comparisons.** The paper compares OC-GFN (pre-trained + fine-tuned) against baselines (GFN from scratch, MCMC, DQN) trained *only* on the downstream task. The pre-training stage — GAFlowNet training, OC-GFN training, predictor network updates — consumes substantial additional computation. The paper reports results as a function of "steps during the course of training" (lines 365, 388) without clarifying whether this is *fine-tuning steps only* for OC-GFN versus *total steps* for baselines, or whether both are plotted on comparable axes. If the x-axis reflects only fine-tuning steps for OC-GFN, the observed improvements in mode discovery may partly reflect more total computation rather than superior algorithmic efficiency. This ambiguity directly affects the central claim of "efficient adaptation" and should be resolved either by clarifying the x-axis definition or by adding a controlled-budget comparison (e.g., allowing the scratch GFN as many total steps as pre-training + fine-tuning combined on at least one task).

### Minor

2. **Missing natural baseline: goal-conditioned RL with hindsight experience replay (HER).** The paper explicitly describes its contrastive training as "related to goal relabeling" (line 159) and acknowledges connections to goal-conditioned RL (lines 27, 82–84, 326). The paper's structural approach is a goal-conditioned policy trained with success relabeling and a form of reward shaping (outcome teleportation). A direct comparison against a goal-conditioned DQN or PPO + HER, trained on the same exploration data from GAFlowNet, would isolate whether the GFlowNet flow-matching formulation provides a concrete benefit over reward-maximization for diversity and sample efficiency. The paper does compare against DQN (which is not goal-conditioned) and against GFN from scratch, so the existing baselines are not weak, but a GCRL+HER baseline would address the most natural question from readers familiar with the RL literature and would substantially strengthen the paper's claims.

3. **Algorithm 2 training details are underspecified for reproduction.** Line 220 states "Collect a trajectory τ with \(N(s'|s)\)" — but \(N\) is unnormalized, and no policy is specified for exploration (e.g., softmax over \(N\), ε-greedy over the normalized policy). Line 221 samples outcomes \(y\) from a "tempered/ε-greedy version of \(Q(\cdot|s',s)\)" but does not specify the initialization or exploration schedule for \(Q\), which depends on \(N\) at initialization. The practical implementation paragraph (lines 276–281) provides some context but leaves key decisions (exploration strategy, how the alternating training loop is bootstrapped, stability across seeds) unspecified. Given that this is the core mechanism for fine-tuning, more detail would meaningfully improve reproducibility.

---

### Trivial

- The paper uses "contrastive training" to describe what is essentially off-policy goal relabeling. The paper itself connects this to hindsight experience replay (line 159), so the terminology is not misleading, but "success relabeling" or "goal relabeling" would be more standard and descriptive.
- Success rate plots (e.g., Fig. 2, 4, 7) show means but some individual curves would benefit from error bars/shading being more clearly visible.
- The AMP success rate (Fig. 9a) plateaus near ~95% — the paper could briefly comment on why coverage is not perfect in this largest space.

---

## Nice-to-Haves

- Add a quantitative distribution-matching metric (e.g., KL divergence or earth mover's distance) for the GridWorld distribution plots (Fig. 1) to complement the visual comparison.
- Report pre-training data coverage statistics (e.g., fraction of reachable states visited by GAFlowNet) for the non-GridWorld tasks to verify that OC-GFN actually learns to reach *any* outcome as claimed.
- Include a brief limitations paragraph discussing cases where pre-training might fail (e.g., GAFlowNet cannot cover the space, or the outcome space is so large that relabeling provides insufficient signal).
- Report wall-clock time or number of function evaluations for the Monte Carlo vs. amortized marginalization to quantify the efficiency gain.

---

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper. Treat them with caution if encountered elsewhere.

- **"Contrastive training is misnamed"** — The paper itself relates the procedure to goal relabeling (line 30, 159). This is a nomenclature preference, not a weakness.
- **"Proposition 1 / Proposition 2 are tautologies"** — These are standard consistency conditions (if loss=0 then correct behavior). Every GFlowNet paper that includes such propositions does so; they are not intended as deep theorems but as formal grounding.
- **"The framing should avoid over-promising the no-retraining property"** — The paper carefully qualifies this with "in principle" (lines 34, 79, 197) and then provides the amortized predictor as a practical alternative. The framing is appropriate.
- **"Outcome teleportation is equivalent to standard DB with additive constant"** — The ablation (Fig. 2, 4) empirically validates that this specific form helps. A theoretical derivation would be nice but its absence is not a weakness.
- **Complaints about missing appendix content, style/formatting issues, or doubts about cited model/dataset availability** — These reflect parser artifacts or reviewer knowledge gaps, not author errors.

---

## Novel Insights

The reviews surface one subtle tension that the paper could address more directly: the claim that GFlowNets can be adapted to new rewards "without retraining" (which is true in theory via Eq. 6) sits in tension with the paper's actual method, which does require fine-tuning (learning \(N\) and \(Q\)). The amortized predictor is motivated as an efficiency solution for intractable marginalization, but the reader is left wondering in what practical regime the Monte Carlo conversion (without retraining) would be feasible and how its cost compares. A brief discussion of this trade-off — when the no-retraining path is viable vs. when amortization is needed — would strengthen the narrative arc between the theoretical promise and the practical algorithm.

---

## Suggestions

1. **Clarify the x-axis** in all downstream-task plots (Figures 5, 8, 9, 10): state explicitly whether it is fine-tuning steps only or total steps including pre-training. Ideally, add at least one controlled-budget experiment where the scratch GFN is given as many total steps as pre-training + fine-tuning combined, to directly address the fairness concern.
2. **Add a goal-conditioned RL baseline** (e.g., DQN + HER or PPO + HER) trained on the same GAFlowNet exploration data, on at least one or two tasks (GridWorld and bit sequences would suffice). This would isolate whether the GFlowNet formulation contributes meaningfully beyond the goal-conditioned RL approach.
3. **Provide explicit exploration details for Algorithm 2**: specify how trajectories are sampled from \(N\) (e.g., softmax temperature, ε-greedy schedule), how \(Q\) is initialized, and how the bootstrapping loop is stabilized at the start of training.
4. **Disambiguate the naming**: consider renaming "contrastive training" to "success relabeling" or "off-policy goal conditioning" to align with the RL literature that the paper already cites.

---

## Score and Decision

The paper makes a novel and practically relevant contribution to the GFlowNet literature. The core idea is clever, the method is sound, the ablations are informative, and the experiments span multiple challenging domains. The main weaknesses — the compute-budget ambiguity and the absence of a goal-conditioned RL baseline — are real but addressable in a revision; they do not invalidate the core contribution. The paper would benefit from clarifications and an additional baseline, but in its current form it represents a solid step forward for pre-training in GFlowNets.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>