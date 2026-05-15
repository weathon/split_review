Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes Planning with Theory of Mind (PToM), a hierarchical MARL algorithm for few-shot adaptation in Sequential Social Dilemmas (SSDs). PToM combines two modules: (1) an opponent modeling module that uses Theory of Mind to infer opponents' goals via a two-level belief update (intra-episode and inter-episode), and (2) a planning module that uses MCTS with belief-sampled opponent goals to select actions. Experiments across three SSD paradigms (sequential stag-hunt, sequential snowdrift, sequential prisoner's dilemma) show that PToM achieves strong self-play performance and consistently outperforms LOLA, SI, A3C, and PS-A3C in few-shot adaptation to unseen opponents.

## Strengths

1. **Novel hierarchical architecture that addresses a real gap in MARL.** Unlike I-POMDP and its approximations which suffer from nested belief inference, PToM explicitly maintains beliefs over opponents' goals and learns neural-network goal-conditioned opponent policies, avoiding nested reasoning while enabling tractable decision-making in complex SSDs. This is well-motivated by cognitive psychology (Section 1, Section 4) and clearly described.

2. **Two-level belief update enables adaptation at different timescales.** The intra-ToM Bayesian update (Eq. 1) allows within-episode belief revision based on observed opponent actions, while the inter-ToM update (Eq. 2) provides refined priors across episodes. The paper provides an intuitive example (Section 5.2, lines 176-192) explaining how belief correction works when facing exploiters in SSH, and references an ablation study confirming both components are important.

3. **Consistent and often large empirical advantage across three diverse SSD paradigms.** In few-shot adaptation (Table 2), PToM achieves the highest normalized scores in nearly every scenario. For instance, in SS against three exploiters, PToM scores 0.93 while the next best (A3C) scores only 0.49. In self-play (Table 1), PToM achieves 29.1 in SS (near the theoretical optimum of 30.0), substantially outperforming LOLA (27.4), SI (24.9), and A3C (25.1).

4. **Planning under uncertainty via belief sampling is a principled approach.** Rather than treating goal uncertainty as part of the environment dynamics (which would introduce bias), PToM samples opponent goal combinations from the belief and averages MCTS action-values over samples (Eq. 3, Section 4.2). This balances computational cost with planning accuracy and is clearly described.

5. **Well-motivated problem framing.** The introduction (Section 1) clearly explains why SSDs differ from zero-sum and pure-cooperative environments, why standard techniques (minimax, Double Oracle, IGM) do not transfer, and why hierarchical goal reasoning is appropriate.

## Weaknesses

### Fatal
None.

### Major

1. **Key experimental components are undefined, making results partially uninterpretable.** (a) The "Direct-OM" baseline appears in all result tables and is discussed in the text (lines 174, 196) but is never described in Section 5.1 or anywhere in the main text — its methodology is completely unknown. (b) "LI-Ref" is used as the normalization reference in Table 2 (line 178) but is never defined. Without knowing what LI-Ref is and how Direct-OM works, readers cannot properly interpret the reported normalized scores or gauge the significance of the improvements.

2. **No variance or confidence intervals reported.** Tables 1 and 2 report point estimates without any measures of variability (standard deviation, standard error, or confidence intervals). Given that MARL training involves substantial randomness across seeds, the reliability and statistical significance of the reported advantages cannot be assessed. This is a serious omission for a paper making strong empirical claims.

3. **The "emergence of social intelligence" claim is stated without any supporting evidence.** The paper asserts (line 206) that "self-organized cooperation and an alliance of the disadvantaged" emerged during multi-PToM interactions, but provides no analysis, quantitative results, case studies, or even a qualitative description of when or how this occurred. This is a one-sentence claim with no substantiation, which undermines its credibility.

### Minor

1. **Inter-ToM update (Eq. 2) does not specify how the indicator function is computed.** The term $\mathbf{1}(g_j^{K-1}=g_j)$ requires knowing the opponent's goal from episode $K-1$, which is not directly observable. The paper does not explain whether this uses a MAP estimate from the posterior, a hard decision from intra-ToM, or some other mechanism. While a reasonable implementation exists (use the argmax of the posterior), the ambiguity makes the core adaptation mechanism underspecified and leaves readers uncertain whether the method is fully specified as described.

2. **Goal sets for each environment are not listed in a single, structured place.** For SSH the goals ("hunting stags" vs. "hunting hares") are explained in the running example (lines 176-177), but for SS and SPD the goals must be inferred from the rule-based strategy descriptions (Section 5.1). A concise table or explicit enumeration per environment would improve clarity.

3. **Ablation study receives only one sentence in the main text.** The ablation results confirming the importance of intra-ToM, inter-ToM, and goal-conditioned opponent modeling (line 204) are deferred to the appendix. Given the centrality of these components to the paper's claims, at least a summary of the ablation results should appear in the main body.

### Trivial

1. MCTS hyperparameters (exploration constant $c_{\text{puct}}$, network architecture for $\theta$ and $\omega$, update frequency, number of simulations $N_s$ for each environment) are sparse. This is common for space-constrained papers but would aid reproducibility.

## Nice-to-Haves

- **Comparison with explicit few-shot/meta-learning MARL baselines** (e.g., MAML-based approaches or other ToM-based methods such as ToMAGA) would strengthen the "few-shot adaptation" claim. The current baselines (LOLA, SI, A3C, PS-A3C) are standard MARL algorithms not designed for rapid adaptation. Without such comparisons, the headline claim is benchmarked only against algorithms that are not optimized for the same capability.

- **Belief trajectory visualizations** (e.g., how the belief over an opponent's goal evolves across timesteps/episodes when facing exploiters vs. cooperators) would provide intuitive support for the adaptation mechanism described qualitatively in Section 5.2.

- **Convergence curves from self-play training** would complement the single-point self-play results in Table 1 and support the claim of "expeditious convergence."

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Circularity claim about Inter-ToM update (from Harsh Critic, Critical Issue 1, second sentence).** The critic asserts that using an inferred goal in the inter-ToM update would be "circular (the belief update depends on the point estimate it is supposed to produce)." This is incorrect: the inter-ToM update produces a *prior* for the next episode, not a posterior. The intra-ToM update then applies Bayesian inference starting from that prior. Using a point estimate (e.g., MAP) from a previous episode to inform the next episode's prior is a standard heuristic (essentially an exponentially-weighted moving average), not circular reasoning. However, the underlying concern — that the paper does not specify *how* $g_j^{K-1}$ is obtained — is legitimate and is kept as a Minor weakness above.

- **Criticism about meta-learning baselines (from Harsh Critic, Critical Issue 2) classified as Major.** This is downgraded to Nice-to-Have. The paper's contribution is a specific algorithmic architecture for adaptation, not a claim to be the best meta-learning method. Showing that PToM adapts faster than standard MARL algorithms (LOLA, SI, A3C, PS-A3C) in few interactions is a meaningful result even without meta-learning baselines, and the baselines chosen are well-established in the MARL community.

- **Criticism about MCTS detail sparsity (from Harsh Critic, Section-by-Section Notes).** This is downgraded to Trivial. Conference papers operate under tight space constraints; providing every MCTS hyperparameter in the main text is not standard practice. The paper provides the key parameters ($N_s$, $\beta$) and describes the architecture at a sufficient level.

- **Criticism about "600 timesteps" not being few-shot (from Harsh Critic, Section-by-Section Notes).** The evaluation is on the final 600 steps after 1800 steps of prior interaction. Across the three environments, this corresponds to roughly 6–20 episodes of evaluation. The same protocol is applied consistently to all methods, so the comparison is fair. The definition of "few-shot" is subjective, and the paper's usage is reasonable in context.

- **Strength Finder's "emergence of social intelligence" strength.** This conflicts with the verified Weakness (Major #3) that this claim is made without supporting evidence. Per the merge policy (disagreement → weakness wins), this claimed strength is dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define Direct-OM and LI-Ref explicitly.** Add a brief paragraph describing the Direct-OM baseline (likely a variant without ToM components) and state what LI-Ref refers to (e.g., the reward of a specific reference policy or hand-coded strategy).

2. **Report variance.** Add standard deviations (or standard errors) across multiple random seeds to all entries in Tables 1 and 2, and state the number of seeds used.

3. **Clarify the inter-ToM update implementation.** State explicitly whether $\mathbf{1}(g_j^{K-1}=g_j)$ is computed using the MAP estimate from the posterior at the end of episode $K-1$, or using a threshold-based decision from the belief distribution.

4. **Provide evidence or retract the "social intelligence" claim.** Either include a concrete analysis (e.g., behavioral metrics, example trajectories, quantitative measures of cooperation and alliance formation) or remove the claim as unsupported.

5. **List goal sets per environment in one place.** A short table or enumeration stating the goal set $G_i$ for each environment (e.g., SSH: {hunt stag, hunt hare}, SS: {remove snowdrift, free-ride}, SPD: {clean waste, collect apple}) would significantly improve clarity.

## Score and Decision

The paper presents a well-motivated and architecturally sound approach to a genuine problem in MARL. The hierarchical ToM+MCTS design is novel, the two-level belief update is principled, and the empirical results show consistent advantages across three diverse SSD paradigms. However, the evaluation is marred by missing descriptions (Direct-OM, LI-Ref) and absent variance reporting that prevent full assessment of the results. The inter-ToM update requires clarification. These issues are fixable but currently weaken the contribution's impact.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>