Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes WBU (Wasserstein Believer), a model-based RL algorithm for POMDPs that learns a latent space model (via a Wasserstein Auto-Encoded MDP, WAE-MDP) and an approximate belief update rule (parameterized by normalizing flows). The core contribution is a theoretical framework with two value-difference bounds: Theorem 1 bounds the gap between returns in the original POMDP and the latent POMDP by a sum of trainable losses; Theorem 2 guarantees that the learned belief representation captures the value function whenever those losses are small. The algorithm assumes state access during training (but not execution) and separates belief learning from policy optimization, using a feed-forward sub-belief encoder without back-propagation through time. Experiments on POPGym (RepeatPrevious, StatelessCartPole) and MinAtar (SpaceInvaders) variants compare WBU against R-A2C and DVRL, with WBU showing advantages on long-term memorization and noise robustness.

## Strengths

1. **Theoretical guarantees for belief learning in POMDPs.** The paper provides two formal theorems (Thm. 1 and Thm. 2, Sect. 3.2) that bound the value difference between the original POMDP and the latent POMDP in terms of local losses, belief loss, and on-policy regularizers. Theorem 2 further guarantees that the learned belief representation preserves value-function closeness. No prior POMDP RL method (including DVRL, R‑A2C) offers explicit guarantees of this form, as the paper correctly notes.

2. **Principled separation of belief learning from policy optimization.** The belief encoder is trained solely by minimizing the belief loss (KL divergence), and the policy gradients do not flow into the belief encoder (Sect. 4, Fig. 2). This clean separation ensures that belief improvement directly targets representation quality, unlike methods that implicitly compress histories through the RL objective.

3. **Feed-forward belief encoder without back-propagation through time.** The sub-belief encoder is a simple feed-forward network called recursively, avoiding BPTT (Sect. 4, lines 345–349). This design choice is motivated by the insight that early time-step beliefs are easier to infer, in contrast to value/policy learning where later time-steps carry more accurate gradients.

4. **Flexible belief distributions via normalizing flows.** The paper uses Masked Auto-Regressive Flows (MAF), which can represent complex, non-Gaussian belief distributions (Sect. 4). This overcomes the limitation of approaches like DVRL that assume independent normal distributions.

5. **Demonstrated long-term memorization and noise robustness.** In the RepeatPrevious environment (Fig. 1), WBU is the only method that exhibits mid- to long-term memorization. In noisy variants of StatelessCartPole and SpaceInvaders, WBU achieves competitive or superior rewards with lower variance than baselines.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baseline comparison.** The experiments compare WBU against only two baselines: R-A2C and DVRL. Several relevant methods are missing: (a) FORBES, which also uses normalizing flows for POMDPs and is discussed in the related work (line 56), could directly test whether the WAE-MDP latent model plus belief loss provides benefits over flow-based compression trained with the RL objective; (b) a simple feed-forward baseline with stacked frames, which the paper itself acknowledges as a mitigation for short-term memory tasks (line 424); (c) other model-based or model-free POMDP methods that learn latent dynamics. This narrow comparison makes it difficult to assess whether WBU's performance stems from its theoretical framework or simply from having privileged state information during training.

2. **No ablation studies.** The paper does not isolate the contributions of its key components: the belief loss, the on-policy regularizers (on-policy reward/transition losses, Eqs. 288–291), and the MAF architecture. Without ablations (e.g., WBU minus the belief loss, WBU with a Gaussian belief instead of normalizing flows, or WBU with BPTT enabled), it is unclear which design decisions drive the observed performance.

3. **The BPTT-avoidance claim is unsupported.** The paper argues that BPTT is unnecessary and "might even be harmful" for belief learning (lines 347–349) because early time-steps are easier to infer. This argument is intuitive but not empirically validated — no comparison is provided between WBU's feed-forward encoder and a version that trains the same architecture with BPTT. Since the sub-belief encoder is called recursively, the distinction is in the gradient propagation path, not in the forward computation. A direct comparison would substantially strengthen this claim.

### Minor

1. **Theory-practice gap: most theoretical loss terms are not measured.** The value-difference bounds (Thm. 1 and Thm. 2) are expressed in terms of multiple loss terms: local reward loss, local transition loss, observation loss, on-policy reward loss, on-policy transition loss, and belief loss. Only the belief loss is empirically reported (Fig. 1). Without measuring whether the other losses are actually small in practice, the bounds serve as motivation but not as verified guarantees. This weakens the paper's central claim that "our approach comes with theoretical guarantees on the quality of our approximation."

2. **t-SNE analysis is qualitative.** The t-SNE visualization (Fig. 2, SpaceInvaders) shows that beliefs with close coordinates have close values, which is consistent with Theorem 2. However, this evidence is qualitative and shown for only one environment. A quantitative metric (e.g., correlation between belief distance and value difference, or a nearest-neighbor regression test) would provide stronger support.

3. **The practical algorithm uses KL divergence, not Wasserstein distance.** The theory (Thm. 1, Thm. 2) is stated in terms of Wasserstein distance, but the practical optimization uses KL divergence as a proxy (lines 375–377), justified via Pinsker's inequality in the zero-temperature WAE-MDP limit. The paper acknowledges this gap (lines 376–377) but does not analyze how large the gap might be given realistic empirical loss values. Similarly, the non-zero observation variance (Remark 1) deviates from the zero-variance assumption in Theorem 2.

4. **The state-access assumption (Assumption 1) is not stress-tested.** While the paper provides a thorough justification of this assumption (lines 179–187) and acknowledges relaxation as future work (line 477), the experiments do not investigate how performance degrades when states are noisy or only partially available during training. This limits understanding of the method's robustness in settings where clean state access is not guaranteed.

5. **No discussion of failure modes or computational cost.** The paper does not discuss when the learned belief update might diverge (e.g., when the latent model is inaccurate due to limited data or function approximation error) and does not report training time or sample efficiency relative to baselines.

### Trivial
None.

## Nice-to-Haves

- Including stacked-frame baselines (as the paper mentions at line 424) would strengthen evaluation on short-term memory tasks.
- A sensitivity analysis of key hyperparameters (e.g., observation variance, temperature in WAE-MDP, normalizing flow architecture) would be useful for practitioners.
- Reporting the additional loss terms (local losses, observation loss, on-policy losses) alongside returns would help directly connect the theory to the experiments.
- A version of the algorithm that relaxes the state-access assumption (e.g., learning the WAE-MDP from observations only) would clarify the cost of this assumption.

## Removed Points

These points were raised by one or both reviews but are removed for the reasons noted; treat them with caution.

- **"Belief loss measured for only one environment"** — The figure caption (Fig. 1) states that belief loss is reported "during learning for WBU" in the same multi-panel figure alongside returns across environments. The critic's claim that it is measured in only one environment is not supported by the paper text.
- **"5 seeds is minimal; no statistical tests"** — Five seeds with standard error plots is standard practice in deep RL. Statistical significance tests are not universally required.
- **"Missing Dreamer/PlaNet comparisons"** — Dreamer and PlaNet target visual motor tasks with image observations; the POPGym environments used here are not image-based. A direct comparison is not well-matched to the paper's experimental setup. (FORBES remains a relevant missing comparison, kept above.)
- **"The 'without using RNNs' claim is overstated"** — The paper clearly explains (lines 342–349) that the sub-belief encoder is a feed-forward network called recursively without BPTT, and explicitly distinguishes it from RNNs on the gradient-propagation axis. This is a fair and accurate characterization.
- **"State-access assumption is under-justified"** — The paper devotes a full paragraph (lines 179–187) to justifying this assumption with several concrete scenarios (simulators, extra sensors, SimToReal, model-based design). The point about not stress-testing it is kept as a minor weakness, but the claim that it is "under-justified" is not accurate.
- **"Theorem 2's bound includes 1/P(history)"** — The bound already contains an epsilon slack term that absorbs the probability weighting; this is a standard form in theoretical RL and the paper does not claim the bound is tight in practice.

## Novel Insights

A genuinely novel observation emerges from the interplay of the two reviews: the paper's strongest empirical result (RepeatPrevious long-term memorization) directly aligns with what its theory would predict — that explicitly minimizing belief error enables maintaining information over many time steps where RNN-based methods trained end-to-end on the return objective lose it. This suggests that the separation of concerns (belief fidelity → representation quality → policy optimization) may be particularly valuable precisely in the regime where the auxiliary signal (value gradients) is weakest (long-range dependencies). If the paper had measured the belief loss and the local transition loss on the RepeatPrevious task and shown that WBU keeps these losses small while baselines do not, it would have closed the theory-practice loop convincingly. The reviewers did not articulate this as a unified insight; it emerges from juxtaposing the theoretical apparatus with the specific experimental condition where the theory predicts a clear advantage.

## Suggestions

1. **Broaden the baseline set.** At minimum, add FORBES and a stacked-frame feed-forward baseline. If feasible, include a Dreamer-style baseline on the MinAtar environments.
2. **Perform ablation studies.** Compare WBU to variants without the belief loss (training the encoder with the RL objective only), with Gaussian beliefs instead of MAF, and with BPTT enabled for the sub-belief encoder.
3. **Measure the theoretical loss terms.** Report the local reward/transition losses, observation loss, and on-policy losses from Theorem 1 alongside returns for at least one environment. Show that reductions in these losses correlate with improvements in return.
4. **Quantify the t-SNE analysis.** Compute a quantitative measure (e.g., correlation between Wasserstein distance in belief space and absolute value difference) to support the qualitative t-SNE visualization.
5. **Test the state-access assumption.** Compare WBU trained with clean states to a variant trained with noisy or partially observed states to quantify the value of this assumption.

## Score and Decision

The paper makes a genuine theoretical contribution — providing formal value-difference bounds for belief learning in POMDPs is novel and valuable. The algorithm design (separation of belief and policy optimization, feed-forward encoder, normalizing flows) is principled and technically sound. The experimental results show promise, particularly on long-term memorization.

However, the evaluation is too narrow to fully substantiate the claims: only two baselines are compared, no ablation studies isolate the contribution of key components, and the theoretical loss terms that underpin the guarantees are largely unmeasured in practice. The theory-practice gap means the central claim — that the algorithm provides operational guarantees — remains unverified. With major revisions addressing these issues, this work could become a strong paper.

**Score:** 5.0  
**Decision:** Reject (requires major revision: broader baselines, ablation studies, and empirical connection of theory to practice)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>