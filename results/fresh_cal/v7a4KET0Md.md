Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

The paper introduces SWIRL (SWitching IRL), a time-varying inverse reinforcement learning framework that incorporates history dependency at two levels: (1) decision-level (state-dependent switching between hidden modes representing different behavioral goals) and (2) action-level (reward and policy depending on recent state history, not just current state). The method is tested on simulated gridworld data, a real water-restricted labyrinth mouse dataset, and a mouse spontaneous behavior dataset. The key contributions are: (i) incorporating biologically plausible history dependency into time-varying IRL, (ii) demonstrating improved reward recovery and segmentation over simpler variants, and (iii) establishing connections between IRL-based and dynamics-based behavioral analysis.

## Strengths

- **Simulation experiment convincingly validates the core contribution.** In the gridworld simulation (Figure 2), only the full S-2 model (with both state-dependent mode transitions and history-dependent rewards) accurately recovers the true non-Markovian reward functions. S-2 achieves the highest Pearson correlation, test log-likelihood, and segmentation accuracy, while simpler variants (I-1, I-2, S-1) all fall short. This directly demonstrates that both levels of history dependency are necessary for correct inference.

- **Interpretable history-dependent reward maps aligned with biological constraints.** In the labyrinth experiment, SWIRL (S-2) infrees reward values for the water port that follow the 90-second water restriction rule: highest reward for arriving at the port (1.0), positive but lower reward for staying (0.7), and even higher reward for leaving (0.9) (Figure 3C). The paper rightly notes that "such insights would not be captured by a Markovian reward function that depends solely on the current state." The three inferred modes (water, home, explore) are interpretable and align with the experimental design.

- **State-dependent mode transitions substantially reduce fast-switching artifacts.** The comparison of segmentations in Figure 3F shows that state-dependent models (S-1, S-2) produce coherent segments of reasonable length, while independent-transition models (I-1, I-2) exhibit many rapid, uninterpretable switches. This provides direct visual evidence that the decision-level history dependency (P_z(z_{t+1}|z_t, s_t)) is behaviorally meaningful.

- **Scalability to longer, non-stereotyped trajectories than prior IRL work.** The paper notes that previous IRL applications to the same labyrinth dataset were "limited to clustered, stereotyped trajectories of only 20 time points in length" (Section 4.2), whereas SWIRL processes full 500-time-point trajectories. This represents a meaningful advance in practical applicability.

## Weaknesses

### Fatal
None.

### Major

- **Insufficiently justified comparison with ARHMM/rARHMM (Section 4.3).** The paper claims that the SWIRL policy "aligns with the emission probability of the ARHMM" because the MDP defines actions as the next syllable (state = current syllable, action = next syllable). While this makes the likelihood comparison over the same space of observed variables, the paper does not fully explain how the held-out log-likelihoods are computed to ensure an apples-to-apples comparison. The SWIRL model and ARHMM have different generative structures (one is reward-based with a policy, the other is dynamics-based with emissions), and the precise mapping between them (referenced to Section 3.5) is missing from the extracted text. The claim that "learning rewards is more beneficial for behavior segmentation" based on this comparison needs a clearer justification of the formal equivalence.

- **Limited quantitative evaluation of segmentation quality in the labyrinth experiment.** The paper provides qualitative comparisons of segmentation (Figure 3F) showing S-2 produces more coherent segments. However, no quantitative metric (e.g., agreement with external behavioral epochs from velocity/proximity, or a formal statistical test comparing segmentation quality across models) is reported. The held-out test LL differences (Figure 3E) are visible but no significance test is reported either.

### Minor

- **No explicit justification for the number of hidden modes.** The labyrinth experiment uses K=3 modes and the spontaneous behavior experiment uses K=5, but the paper does not discuss how these values were chosen (e.g., cross-validated likelihood, elbow criterion, or prior knowledge from experimental design).

- **Limited comparison with other time-varying IRL baselines.** The paper compares against multi-intention IQL (I-1) and locally consistent IRL (S-1), arguing they are special cases of SWIRL. While this is a reasonable ablation strategy, direct comparison with other established methods (e.g., DIRL, BNP-IRL) on the same datasets would strengthen the empirical positioning. The paper discusses these methods in related work but does not implement them.

- **No significance tests for key comparisons.** The held-out test LL boxplots in Figures 2 and 3 show visual separation, but no formal statistical tests (e.g., paired bootstrap, signed-rank test) are reported to confirm the reliability of the differences.

- **The "hypothesis testing" claim in Section 4.3 is underdeveloped.** The paper pivots to framing SWIRL as a hypothesis-testing tool when the history-dependent variant underperforms on the spontaneous behavior dataset, but does not provide concrete evidence that the inferred reward maps or mode segments yield novel biological insights beyond what simpler statistics could reveal.

- **Only history lengths L=1 and L=2 are tested.** No ablation or justification is given for why longer history lengths were not explored or why they would not be beneficial.

### Trivial
None.

## Nice-to-Haves

- Include a limitations section discussing the optimality assumption, sensitivity to the number of modes, computational cost, and potential issues with longer history lengths.
- Add a comparison against a baseline that uses known experimental structure (water interval, home location) to generate segmentation — the fact that SWIRL recovers this without prior knowledge is a strength that could be highlighted more explicitly.
- Report hyperparameter details (learning rates, number of EM iterations, convergence criteria, random restarts) for reproducibility.

## Removed Points

- **"Invalid likelihood comparison" (Harsh Critic #1)**: The harsh critic claims that SWIRL and ARHMM compute likelihoods on "different spaces" with "different normalizing constants." This is incorrect given the MDP formulation (state = current syllable, action = next syllable), which maps both models' likelihoods onto the same space of observed syllable sequences. The paper explicitly states (lines 91–93) that the policy aligns with the emission probability. The concern about insufficient formal justification is retained as a Major weakness above, but the "invalid" characterization is removed as factually incorrect.

- **"Incomplete and underspecified method" (Harsh Critic #2)**: The harsh critic notes that Sections 3.1–3.3 are missing from the extracted text. Per the guidelines, the parser strips these sections from all papers; they exist in the original submission. Criticizing the method as underspecified based on parser-stripped content is not valid.

- **"Pure formatting/style nitpicks" and missing-related-work criticisms**: Removed per guidelines.

- **Strength Finder's generic strengths**: Generic claims about "addressing an important problem" or "addressing an interesting question" are removed. Only concrete, evidence-backed strengths are retained.

- **"Missing limitations discussion"**: The harsh critic's suggestion about adding a limitations section is moved to Nice-to-Haves (it is a useful suggestion but not a weakness of the presented method).

## Novel Insights

The most interesting observation emerging from the meta-review is the tension between the two experiments with history dependency. In the labyrinth experiment, action-level history dependency (L=2) improves performance because the 90-second water restriction creates genuine non-Markovian structure in the reward. In the spontaneous behavior experiment, history dependency hurts (S-1, I-1 outperform S-2, I-2), which the paper attributes to the preprocessed syllable data. This asymmetry is actually informative: it suggests SWIRL's history dependency is not always beneficial and should be deployed selectively based on domain knowledge about the timescale of decision-relevant history. The paper's handling of this result (acknowledging the failure and pivoting to hypothesis testing) is honest but could be strengthened into a more systematic analysis of *when* history dependency helps.

None beyond the paper's own contributions.

## Suggestions

1. Clarify the held-out log-likelihood computation for the SWIRL vs. ARHMM comparison in Section 4.3, or replace the comparison with a metric that is transparently comparable (e.g., predictive accuracy of the next syllable, or segmentation agreement with an external criterion).
2. Add statistical significance tests (e.g., paired bootstrap or signed-rank) for the key test LL comparisons in Figures 2B, 3E, and 4B.
3. Provide a clear justification or cross-validation procedure for the choice of hidden mode count K in each experiment.
4. For the spontaneous behavior experiment, consider replacing or supplementing the LL comparison with a metric that does not rely on the formal equivalence between the two model classes, or explicitly compute the marginal likelihood under both models in a way that controls for differences in model structure.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>