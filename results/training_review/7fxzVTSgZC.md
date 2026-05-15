Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper studies Offline Imitation Learning (OIL) and proposes BCDP (Behavioral Cloning with Dynamic Programming), which uses transition information from low-quality offline data (even random exploration) to guide a policy toward states visited by the expert. The key idea is to separate learning into two components: behavioral cloning on expert data to ensure good behavior on expert-observed states, and dynamic programming (via Q-learning with an indicator reward) on unlabeled offline data to maximize the discounted probability of reaching expert-observed states. The paper provides a theoretical lower bound (Proposition 1) motivating this approach and demonstrates strong empirical results across 28 D4RL settings.

## Strengths

- **Novel and well-motivated framing for utilizing low-quality data.** The paper identifies an important gap: prior OIL methods assume the auxiliary dataset contains at least some expert-like high-quality data. BCDP reframes the problem from "identify expert transitions in the offline data" to "use transition dynamics to navigate toward expert-observed states." This is a conceptually clean departure from prior work that yields practical benefits.

- **Consistent and large empirical gains, especially with purely random offline data.** In Table 1, BCDP achieves the best or second-best score on 23 of 28 tasks. On random-data settings (e.g., maze2d-large-random: 97.3 vs. BC-exp 14.9; ant-random: 108.1 vs. BC-exp 9.7), the improvements are dramatic. The claim that low-quality data can be helpful—not harmful—is convincingly supported.

- **Quantitative evidence for the claimed mechanism.** The Distance Reduction Gain (DRG) analysis in Figure 4 directly shows that BCDP reduces the distance to expert-observed states and achieves higher long-term returns on states far from expert data. This connects empirical performance to the paper's core intuition.

- **Systematic ablation across expert data budgets.** Figure 3 varies expert trajectories from 1 to 5 (or 10 to 50 for Adroit) and shows BCDP consistently outperforms DemoDICE, OTIL, and DWBC, demonstrating robustness to extreme expert scarcity.

## Weaknesses

### Fatal
None.

### Major

- **The comparison against UDS+TD3+BC is confounded, weakening claims about the source of BCDP's advantage.** The paper treats UDS+TD3+BC "as an ablation study of our approach" (Section 4.1). However, TD3+BC's policy objective includes a behavioral cloning penalty (the squared-action deviation) on *all* data, while BCDP applies log-likelihood BC *only* on expert data. This means UDS+TD3+BC is not a clean ablation of BCDP minus a component—it differs in *how* BC is targeted. BCDP's large advantage over UDS+TD3+BC could stem from (a) the targeted-BC design, (b) the log-likelihood vs. squared-error BC form, (c) the different hyperparameter α vs. λ, or a combination. The paper provides no ablation comparing BCDP to a version without its BC term (α=0), nor to UDS with a pure offline RL algorithm that lacks a BC regularizer (e.g., vanilla TD3 or CQL). While this does not invalidate BCDP's overall empirical success, it makes it difficult to attribute the gains cleanly to the proposed mechanism vs. incidental design choices.

- **The theoretical connection between Proposition 1 and the practical algorithm is heuristic-level, not formally established.** Proposition 1 proposes maximizing the discounted probability of the policy reaching *expert-observed states*. The algorithm instead learns a Q-function with reward \(r(s,a)=\mathbb{I}[(s,a)\in D^E]\) and then maximizes \(Q(s,\pi(s))\). The Q-function with this reward captures the discounted probability of reaching *expert transitions* (state-action pairs), not expert states. These are not equivalent: reaching an expert state via a non-expert action yields zero immediate reward, and the connection between the two objectives depends on the BC component ensuring good actions on expert states. The paper states "To implement the proposition" (Section 3.2, line 130) but provides no formal argument or approximation analysis linking the Q-objective to the state-distribution maximization in Proposition 1. This leaves the theory and algorithm partially disjoint.

### Minor

- **The "first attempt" claim is overstated in its current phrasing.** The abstract states "make the first attempt to demonstrate that low-quality data is also helpful for OIL." Prior work (Sasaki & Yamashina, 2021; Kim et al., 2022; Xu et al., 2022a) studies offline IL with suboptimal data, though under the assumption of some expert-like content in the auxiliary set. The paper's contribution lies in demonstrating benefits from data with *no* expert-like content—a meaningful distinction—but the blanket "first attempt" phrasing invites unnecessary controversy. A more precise claim (e.g., "first to demonstrate that purely random offline data with zero expert-like content can significantly improve OIL") would be both accurate and stronger.

- **No controlled study varying the proportion of expert-like transitions in the offline data.** The paper's thesis is that low-quality data can be helpful, but the experiments only test discrete data types (random-v2, medium-v2, etc.) rather than smoothly interpolating the proportion of expert-like trajectories in the offline set (e.g., 0%, 25%, 50%, 100% expert-like content). A continuous analysis would more directly validate the claim and reveal potential failure modes.

- **Figure 3 lacks error bars or confidence intervals.** The comparison under varying expert budgets is informative, but without error bars (especially given the small seed count of 3), it is difficult to assess whether the observed gaps are statistically meaningful.

- **Some BC-exp scores on Adroit tasks are near-perfect (door-expert: 100.3, pen-expert: 99.5),** suggesting the 50-expert-trajectory setup may not be particularly challenging for these tasks. This is briefly explainable (some D4RL Adroit tasks are simpler) but should be explicitly discussed, as it affects how much weight to put on those results.

### Trivial

- Lemma 1 uses \(N^E\) (superscript) while Section 2.1 defines \(N_E\) (subscript). These clearly refer to the same quantity (number of expert trajectories), but the inconsistency is distracting.
- The connection between the generalized BC objective (Equation 4) and the paper's own Equation 9 is not explicitly discussed. Making the link clear would help readers situate BCDP in the existing framework.

## Nice-to-Haves

- **Comparison with UDS using an offline RL algorithm without intrinsic BC regularization** (e.g., vanilla TD3 or CQL) to isolate the effect of the BC-on-expert design.
- **Ablation of BCDP's BC term** (setting α=0 in Equation 9) to separate the contribution of Q-learning from the BC-on-expert loss.
- **DRG analysis on locomotion tasks** would strengthen the claim that the mechanism generalizes beyond low-dimensional navigation.
- **Hyperparameter sensitivity of α** (Equation 9) across different task families.

## Removed Points

- **Criticism about "N^E not defined"**: The paper defines \(N_E\) in Section 2.1 (line 39, "N_E trajectories"), so \(N^E\) in Lemma 1 is a minor notation variant of the same quantity. The reviewer's point is a notation inconsistency, not a missing definition. Kept as trivial.
- **Criticism about "no normalization or clipping mentioned for indicator reward"**: This is standard practice in TD3-based implementations and not a meaningful omission. Removed.
- **Criticism about Proposition 1's "existence or uniqueness not discussed"**: Proposition 1 presents a conceptual optimization objective, not a formal existence theorem. Requesting measure-theoretic rigor in an empirical systems paper is scope creep. Removed.
- **Criticism about "the bound is taken as-is; no attempt to specialize it"**: Lemma 1 is cited from prior work as relevant background; the paper's contribution is Proposition 1 and its lower bound (Equation 7), not Lemma 1. The reviewer's expectation is misaligned with the paper's scope. Removed.
- **Criticism about "the paper does not provide a controlled experiment that isolates the benefit of low-quality data per se... comparing performance with random vs. no offline data"**: The paper *does* compare against BC-exp (which uses no offline data), and BCDP with random data outperforms BC-exp. This *is* a controlled comparison showing low-quality data helps. The reviewer's claim is factually incorrect. Removed.
- **Strength Finder strength 5 ("simple, minimally engineered implementation")**: Generic claim lacking specific evidence of simplicity relative to baselines. Dropped.
- **Strength Finder: "robust ablation across data and expert budgets"** partially conflicts with the verified weakness about Figure 3 lacking error bars. The strength is retained because the trend is clear across multiple settings, but the conflict is noted.

## Novel Insights

The reviews surface an interesting tension: the paper's strength and weakness stem from the same source. BCDP's practical success is clearest where theory provides the weakest guidance (navigation domains with clean topology, where "reaching expert states" is a well-defined geometric objective), and more ambiguous where the theory ought to apply but the mechanism is harder to verify (locomotion tasks, where state-space distances are less semantically meaningful). This suggests the paper's real contribution may be the general principle of "use transition dynamics as a bridge to expert states" rather than the specific theoretical framing, and future work might profitably explore alternative bridge-building mechanisms (e.g., successor features, reachability analysis) that maintain the practical benefit while tightening the theory-practice link.

## Suggestions

1. Provide an ablation removing the BC term from BCDP (α=0) to isolate the contribution of Q-learning with the indicator reward.
2. Compare against UDS with an offline RL algorithm that has no intrinsic BC penalty (e.g., CQL or vanilla TD3) to make the UDS comparison cleaner.
3. Add a continuous data-quality ablation varying the fraction of expert-like trajectories in the offline dataset.
4. Add error bars to Figure 3 and discuss the near-perfect BC-exp scores on door-expert/pen-expert.
5. Tighten the "first attempt" claim to specify "purely random offline data with zero expert-like content."

## Score and Decision

The paper proposes a genuinely novel perspective on offline imitation learning and backs it with strong and broad empirical results. The weaknesses are real but not fatal: the theory-algorithm connection is heuristic-level (common in NeurIPS empirical papers), and the UDS comparison could be cleaner but does not invalidate the overall empirical story. The core idea is simple, intuitive, and demonstrably effective. With moderate revisions (ablations, clarified comparisons, and toned-down novelty claims), this would be a solid contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>