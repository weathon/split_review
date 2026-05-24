Now I have a comprehensive understanding of the paper and both sets of reviewer comments. Let me write the final consolidated review.

## Summary

This paper proposes a spectral method that connects Predictive State Representation (PSR) learning with tensor decomposition to recover explicit POMDP transition and observation parameters from action-observation sequences. The core theoretical contribution (Theorem 1) characterizes recovery "up to a full-rank observability partition" — when states share observation distributions across all full-rank actions, the method recovers partition-level transitions and observations rather than per-state parameters. This relaxes assumptions of prior tensor methods (Azizzadenesheli et al., 2016; Guo et al., 2016). Experiments on small domains (Tiger, T-Maze, Sense-Float-Reset) show the learned model matches PSR planning performance while providing explicit likelihoods, and the reward-specification experiments demonstrate a practical advantage over black-box PSRs.

## Strengths

- **Relaxes prior tensor-method assumptions by recovering POMDP parameters up to an observability partition (Theorem 1, Section 4.1).** Prior tensor-decomposition approaches (Azizzadenesheli et al., 2016; Guo et al., 2016) required that each full-rank action has unique observation distributions per state. Theorem 1 shows that the method recovers observation and transition likelihoods even when states share observation distributions across all full-rank actions, grouping them into a partition. This is a genuine generalization that includes systems like the running Sense-Float-Reset example (Figure 1).

- **Empirically matches PSR planning performance while providing explicit observation and transition likelihoods (Figure 3, Row 4).** Across Tiger, T-Maze, and Sense-Float-Reset, the total reward from PO-UCT planning is similar for the learned model, the PSR baseline, and the ground-truth model. This shows that the explicit likelihoods extracted via the similarity transform do not degrade predictive quality needed for planning.

- **Enables state-based reward specification after learning, a capability unavailable with black-box PSRs (Figure 4).** In the noisy hallway domain, observation-based reward specification (PSR_obs) fails because ambiguous observations yield the same mixture distribution for different beliefs. State-based reward specification (Ours_state) succeeds in driving the agent to the middle state. The paper explains (Section 5) that "the uniform belief state and belief state that places all mass on the middle of the hallway yield the same mixture observation distribution weighted by the belief," making state-based rewards necessary.

- **Provides a principled method for identifying the observability partition via random-weight joint diagonalization (Lemma 1, Section 4.2).** Lemma 1 proves that with random weights, eigenvalues of the weighted sum of observation matrices are distinct almost surely exactly when two states have different observation distributions across all full-rank actions. This gives a sound theoretical basis for detecting the partition.

## Weaknesses

### Fatal
None.

### Major

- **The experimental evaluation does not clearly demonstrate or isolate the partition-level recovery regime that is the paper's headline claim.** Although the paper acknowledges that Sense-Float-Reset has a nontrivial observability partition even with rewards as observations (line 113: "Aside from the two leftmost states (when treating rewards as observations), all other states in this POMDP have the same observation distributions"), the experiments are not designed to highlight what happens when the partition is genuinely coarse. The observation/transition error plots (Figure 3, Rows 2–3) are described as measuring error "relative to ground truth" without explaining how partition-level parameters are compared against ground-truth per-state parameters. The reward-specification experiments (Section 5) are explicitly conducted on domains "whose observation and transition matrices can be fully recovered by our method" (line 312), which tests only the singleton-partition (full-recovery) case. An experiment on a domain where states truly share observation distributions across all full-rank actions — and where partition-level recovery is explicitly measured and benchmarked against full-recovery — would directly validate the paper's central claim.

- **The post-processing step to recover partition-level likelihoods (Section 4.3) is described too briefly to be reproducible.** The description states that a random block-diagonal rotation matrix R is applied, followed by scaling by diag(RP'^{-1}m_∞), but the procedure for identifying the block structure of the partition from the estimated eigenvectors, the method for constructing the random rotation, and the proof that this yields the block-diagonal structure needed for Theorem 1 are all deferred to the appendix. Without these details in the main text (or a clear algorithm box), a reader cannot assess or implement this critical step.

### Minor

- **The claim that planning performance is "not impaired" by errors in the similarity transform is stated without statistical testing.** Figure 3 (Row 4) shows the learned model's total reward is visually similar to the PSR and ground truth, but the error bars are large (standard deviation over 100 seeds) and no confidence intervals or significance tests are provided. For several domains (e.g., Tiger, T-Maze), the learned model's reward appears consistently below the PSR and ground truth. A more cautious phrasing ("comparable performance") with appropriate caveats would be more accurate.

- **No analysis of computational complexity is provided.** The method involves building a Hankel matrix from count statistics, computing an SVD, and performing joint diagonalization — all of which have scaling implications for larger state/observation spaces. Understanding the computational bottlenecks would help assess practical applicability.

- **The domains tested are very small (3–4 states).** While this is typical for spectral-method papers in this sub-area, it limits confidence in scalability to larger, more realistic POMDPs. The paper acknowledges this in the future work section but does not discuss the expected scaling behavior.

### Trivial
None.

## Nice-to-Haves
- A direct comparison against the prior tensor methods of Azizzadenesheli et al. (2016) or Guo et al. (2016) on a domain where those methods fail (e.g., due to shared observation distributions across actions) would strengthen the claim that the relaxed assumptions are practically beneficial.
- A discussion of failure modes — what happens when no actions are full-rank, or when the ergodicity assumption is violated — would help practitioners understand when the method is applicable.

## Removed Points

- **"The partition is trivial/singleton in implemented experiments."** REMOVED: The paper explicitly states at line 113 that the partition is nontrivial: "Aside from the two leftmost states (when treating rewards as observations), all other states in this POMDP have the same observation distributions." This directly contradicts the critic's assertion that the partition is singleton.

- **"The PSR comparison is unfair because it doesn't compare same reward strategy."** REMOVED: The paper already compares Ours_obs and PSR_obs (both using observation-based reward) alongside Ours_state (state-based reward) in Figure 4. The comparison is appropriate for the claim being made (state-based reward is a unique capability of the POMDP model).

- **"Missing code/hyperparameters" and "Missing appendix content."** REMOVED: The parser strips these sections from the submission. They exist in the original paper.

- **"Missing related works" and speculative claims about model availability.** REMOVED per filtering rules.

- **"EM is a weak baseline" (from harsh critic).** REMOVED: Comparing against EM is standard in the spectral-methods literature; the critic's suggestion to include Azizzadenesheli et al. (2016) is a nice-to-have, not a weakness.

- **Strength Finder generic strengths** (e.g., "this paper addressed an important problem"): REMOVED as generic/superficial.

## Novel Insights

Both reviewers correctly identify the paper's core strength (the PSR-tensor-decomposition connection and the partition-level recovery guarantee) and the same central limitation (the experiments do not clearly demonstrate the partition-level regime). The harsh critic's most useful contribution is identifying that treating reward as an observation refines the observability partition — a point the paper acknowledges in passing but does not discuss as a design trade-off. However, the harsh critic overreaches by asserting the partition is "trivial" in the experiments, which the paper's own text contradicts. The strength finder correctly identifies the reward-specification advantage as a concrete benefit of explicit likelihoods. Neither reviewer noted an interesting tension: the Sense-Float-Reset experiments DO demonstrate partition-level recovery (since the observation matrix rows for states in the same partition are correctly recovered as identical), but the paper's framing of "convergence to true POMDP parameters" obscures this. The experimental validation of partition-level recovery exists implicitly in the results but is not highlighted, which is a framing problem rather than an absence of evidence.

## Suggestions

1. Add an experiment on a domain where the full-rank observability partition is genuinely coarse (e.g., 5+ states in a single partition) and explicitly measure partition-level vs. per-state recovery quality. This would directly validate the paper's central claim.
2. Include an algorithm box or pseudocode for the post-processing step (random block-diagonal rotation + normalization), and explain how the block structure of the partition is identified from the eigenvectors in practice.
3. Soften the planning-performance claim to "comparable performance" and report confidence intervals or effect sizes alongside the point estimates.
4. Acknowledge explicitly which domains are in the full-recovery regime and which are in the partition-level regime, and discuss the implications for interpretation of the results.

## Score and Decision

Now let me perform calibration to determine the precise score.

**Round 1 — Bracketing:**

The three bands returned:
- Weak anchors (avg < 3.5): Papers scoring 2.50–3.25
- Middle anchors (avg 3.5–7.5): Papers scoring 3.75–6.80
- Strong anchors (avg > 7.5): Papers scoring 8.00

This paper sits clearly in the middle band. It has a genuine theoretical contribution and reasonable experiments, but it doesn't have the empirical breadth or theoretical depth of the 8.00 papers.

**Round 2 — Narrowing:**

Within the middle band, the most relevant anchors are:
- **FNiqaC382D** (avg 5.50): Provable Causal State Representation under Diffusion Model — rejected with mixed reviews. Our paper has clearer presentation and a more coherent story.
- **GvsCOOPxoI** (avg 6.17): Provable Learning for DEC-POMDPs — rejected primarily for format issues (excessive reliance on appendix), not content. Technically ambitious but 3× appendix.
- **1hsVvgW0rU** (avg 6.00): Sample-Efficient Learning of POMDPs with Multiple Observations — accepted as poster. Clean theoretical story, limited experimental scope, somewhat incremental over prior work.
- **U6Qulbv2qT** (avg 6.80): Multi-task PSR — accepted as poster. Strong theory but limited practical demonstration.

Our paper compares as follows: It is clearer and more self-contained than the DEC-POMDP paper (6.17), has a more novel algorithmic contribution than the "Multiple Observations" paper (6.00), and has stronger experimental validation (actual parameter recovery + planning) than the multi-task PSR paper (6.80). However, it is less theoretically rigorous than those papers (which have PAC bounds and sample-complexity guarantees) and the experiments are on very small domains. The unresolved experimental gap regarding the partition-level recovery claim also prevents it from reaching the 6+ level.

Comparing against **FNiqaC382D** (5.50): Our paper is significantly better — clearer writing, better-motivated, and the theoretical result is cleaner. This suggests our paper should score above 5.50.

Comparing against **1hsVvgW0rU** (6.00, accepted): Our paper has a more original algorithmic contribution (the PSR-tensor connection is genuinely new) but the "Multiple Observations" paper has a tighter theoretical narrative. Our paper's experimental weakness (not clearly demonstrating the partition-level regime) is a real limitation that this anchor doesn't share. This suggests our paper is slightly below 6.00.

**Final score:** 5.5. The paper makes a genuine contribution (the PSR-tensor decomposition connection is novel and theoretically sound), and the experiments do show the method works on standard domains. However, the central empirical claim about the advantage of the method (partition-level recovery) is not as clearly validated as it should be, and the small scale of experiments limits the demonstrated impact.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>