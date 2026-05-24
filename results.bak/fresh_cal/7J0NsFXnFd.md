Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me produce the final consolidated review.

## Summary

This paper proposes RL-CFR, a framework that combines reinforcement learning with counterfactual regret minimization for dynamic (state-dependent) action abstraction in imperfect-information extensive-form games. The key idea is an MDP formulation where states are public information, actions are feature vectors mapped to action abstractions, and rewards are the PBS-value difference between the chosen abstraction and a fixed default. Applied to Heads-up No-limit Texas Hold'em, RL-CFR achieves 64±11 mbb/hand against the authors' ReBeL replication and 84±17 mbb/hand against Slumbot.

## Strengths

- **Novel MDP formulation for action-abstraction selection (Section 4).** The paper defines states as public states, actions as 2K-dimensional vectors mapped to action abstractions via a parameterized function \(f\), and rewards as PBS-value differences. This provides a principled optimization target for dynamic abstraction selection, going beyond prior fixed-abstraction approaches (Moravčík et al., 2017; Brown et al., 2020).

- **Large-margin head-to-head results against strong baselines (Table 1).** RL-CFR defeats the authors' ReBeL replication by 64±11 mbb/hand (600,000+ hands, AIVAT-reduced variance) and Slumbot by 84±17 mbb/hand (250,000+ hands). These margins are well above the 50 mbb/hand threshold commonly considered significant in poker, and the sample sizes are large enough for statistical confidence.

- **Lower exploitability than the fixed-abstraction baseline.** RL-CFR achieves 17 mbb/hand exploitability vs. 20 mbb/hand for the ReBeL replication (evaluated over 10,000 random river-stage states). This provides complementary evidence that the dynamic abstraction does not sacrifice strategic soundness for win-rate.

- **Favorable computation-performance trade-off.** Against FINE-GRAIN (a finer fixed abstraction with 8 actions), RL-CFR shows a comparable or better win-rate while using only ~4/7 of the solving time (Table 2), illustrating the claimed computational advantage of targeted dynamic abstraction.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed comparison against ReBeL with unvalidated replication.** The abstract states RL-CFR "defeats ReBeL," but the comparison is exclusively against the authors' own replication, whose fidelity to the original ReBeL system (Brown et al., 2020) is not established. The replication beats Slumbot by only 16 mbb/hand; the paper provides no evidence this is consistent with published ReBeL performance. While the body does clarify "ReBeL's replication" in the contributions and experimental sections, the abstract's unqualified phrasing and the lack of any cross-validation against the original system's expected strength make the headline result difficult to interpret. The internal comparison (RL-CFR vs. the replication trained under identical conditions) is still informative, but the claim "defeats ReBeL" as stated in the abstract overreaches.

### Minor

- **Table 2 results lack statistical significance, unreported in the paper.** The MUL-ACTION comparison (21±26 mbb/hand over 100,000 hands) and FINE-GRAIN comparison (23±28 mbb/hand) both yield 95% confidence intervals that include zero. The paper presents these as positive evidence ("RL-CFR beats...") without acknowledging that the margins are not statistically significant. This is a straightforward oversight in presentation that should be corrected.

- **State representation choice (PS vs. PBS) not ablated.** The MDP compresses the Public Belief State to a public state, discarding belief distribution over private hands (Section 4). While the paper notes a computational rationale ("public states of non-root nodes are fixed during CFR iterations"), it provides no ablation or empirical justification that the reduced PS representation retains enough information for optimal abstraction selection. This is a design choice whose impact on performance is unexamined.

- **Gaussian exploration strategy underspecified.** The framework adds Gaussian noise to the action vector for exploration (step ②, Section 5), but the noise scale, decay schedule, and whether it is applied throughout training or only initially are not reported. This affects reproducibility and the assessment of exploration effectiveness.

- **PBS value network trained solely on default abstraction data.** The PBS value network used for reward computation in both the selected and default abstraction subgames is trained exclusively on data generated from the default fixed abstraction (Section 6). The paper does not investigate whether this network generalizes accurately to PBS states encountered under substantially different (selected) abstractions, which could introduce systematic bias into the RL reward signal.

- **No limitations or failure case discussion.** The paper has no section discussing limitations. A number of design choices (hand-crafted action mapping, single-game evaluation, PS vs PBS choice, computational cost of solving two subgames per step) would benefit from explicit acknowledgment and discussion of their scope.

### Trivial

- **Total training wall-clock time not reported.** The paper states the action/critic training cost is ~40% of the PBS value network cost, and that 60 threads are used for data generation, but absolute wall-clock time is missing. This makes it difficult to assess practical training cost.

- **Minor hyperparameter underspecification.** Optimizer parameters beyond learning rate (e.g., β₁, β₂ for Adam), gradient clipping settings, and target network update mechanics for the actor-critic are not reported.

## Nice-to-Haves

- Comparing against a finer-grained fixed abstraction that matches the average size of the dynamic abstraction's game tree, to better isolate the benefit of adaptivity vs. total branching factor.
- A simple sanity-check experiment: RL-CFR against the default fixed abstraction using the *same* PBS value network and CFR setup, controlling for all confounds except the abstraction selection mechanism.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The baseline comparison is fundamentally invalidated"** — The critic frames this as a fatal flaw that invalidates the primary result. However, the paper makes clear in the body that the comparison is against their replication, and the RL-CFR vs. Slumbot result (84±17 mbb/hand) stands independently. The critic's claim that the replication is "far below" original ReBeL's expected performance is speculative, not verifiable from the paper. The overclaim issue is retained in Major above.

- **"Reward computation is circular and potentially biased"** — The critic calls this a "methodological error." In ReBeL-style methods, the PBS value network predicts equilibrium values for PBS states based on the subgame below, independent of the parent node's abstraction choice. Whether the training distribution causes meaningful degradation for non-default abstractions is an untested hypothesis, not a demonstrated flaw. Moved to Minor above with appropriate framing.

- **"The CLIP(2.5(x_i+1)×pot) function has no justification"** — Factually incorrect. The paper states: "Based on human experience and inspired by prior studies (Hawkin et al., 2011; 2012), a reasonable range for a raising scale other than all-in is [0,5]×pot." The factor 2.5 is a straightforward linear mapping from x_i ∈ [-1,1] to that range.

- **""can be trained from scratch" contradicted by pre-training"** — The PBS value network is itself trained from scratch as part of the system. "From scratch given only the rules" is standard usage meaning no external data or pre-trained models; training a value network via self-play is consistent with this claim.

- **"Slumbot is not representative of modern HUNL play"** — The paper justifies Slumbot as the only publicly available HUNL AI offering online testing. The suggestion of Pluribus is misaligned (Pluribus targets 6-player poker, not HUNL). Speculative and outside the paper's stated scope.

- **"Action network only 20k parameters...questionable"** — The sufficient parameter count depends on the complexity of the mapping from public state to good abstractions. The critic provides no evidence of underparameterization.

- **"ReBeL algorithm usage is ambiguous"** — The paper clearly describes using the PBS value network and CFR to solve depth-limited subgames, which is the standard application of ReBeL-style methods.

- **Grammar/formatting/typo nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a novel observation that the authors themselves missed — they largely amplify concerns the paper partially addresses (replication fidelity, statistical rigor) or raise speculative concerns about design choices that would need experimental evidence to validate.

## Suggestions

1. **Quality the abstract's claim.** Replace "defeats ReBeL" with "defeats our replication of ReBeL" or provide evidence that the replication is competitive with published ReBeL results (e.g., benchmarking against a common opponent using an established protocol).
2. **Acknowledge Table 2's confidence intervals.** Add a sentence noting that the MUL-ACTION and FINE-GRAIN comparisons, while directionally positive, do not reach statistical significance in 100,000 hands.
3. **Add an ablation study.** Compare using PS vs. PBS as the MDP state to empirically justify the compression choice.
4. **Report the Gaussian noise parameters.** Specify the scale, whether it decays, and whether it is used during evaluation.
5. **Add a limitations section.** Discuss the computational cost (solving two subgames per PBS step), generality to non-poker IIEFGs, and the hand-crafted components of the action mapping.
6. **Report absolute training wall-clock time** to help readers assess practical feasibility.

## Score and Decision

The paper introduces a genuinely novel MDP formulation for dynamic action abstraction in IIEFGs and provides strong primary evidence (large-margin wins against two baselines, lower exploitability) that the approach works in a challenging domain. The weaknesses are real but addressable: the headline comparison needs more careful phrasing, a few experimental details are missing, and one supplementary table lacks statistical significance acknowledgement. No flaw identified is fatal to the core contribution. On balance, the paper represents a solid contribution that, with relatively minor revisions, would be a valuable addition to the literature.

**Originality:** High — the MDP-RL-CFR combination for dynamic abstraction is novel.  
**Importance of research question:** High — action abstraction is a known bottleneck in large IIEFGs.  
**Claims supported:** Moderately well, with caveats about the ReBeL comparison and Table 2.  
**Soundness of experiments:** Good for the primary results; supplementary results are weaker.  
**Clarity of writing:** Clear overall; the MDP formulation and framework are well explained.  
**Value to community:** Good — provides a new paradigm for abstraction selection.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>