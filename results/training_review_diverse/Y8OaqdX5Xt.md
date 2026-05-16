Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me compose the final consolidated review.

---

## Summary

This paper proposes PToM (Planning with Theory of Mind), a multi-agent algorithm for few-shot adaptation to unseen policies in sequential social dilemmas (SSDs). PToM combines a two-level Bayesian opponent modeling module (intra-episode and inter-episode goal inference) with an MCTS planning module that samples opponent goal combinations from the inferred belief distribution. The method is evaluated in three SSD environments (sequential stag-hunt, sequential snowdrift, sequential prisoner's dilemma) against LOLA, SI, A3C, PS-A3C, and rule-based opponents. The results consistently show PToM achieving higher normalized scores than baselines in both self-play and few-shot adaptation settings across most matchups.

## Strengths

- **Novel and well-motivated hierarchical architecture integrating ToM-based goal inference with MCTS planning.** PToM explicitly combines goal-conditioned opponent policies, Bayesian belief updates at two temporal resolutions, and MCTS planning under goal uncertainty (Section 4, Section 4.1). This addresses the genuine challenge that pure ToM methods struggle with efficient reasoning and planning, while planning-only methods lack opponent modeling. The design is grounded in cognitive science (hierarchical goal reasoning) and avoids the nested belief inference of I-POMDP, making it computationally feasible in sequential environments.

- **Temporally two-level belief updating (intra-ToM and inter-ToM) is a technical improvement over prior ToM approaches that assume static opponent goals.** Intra-ToM (Eq. 1) performs Bayesian updates within an episode based on observed actions, enabling rapid response to in-episode behavior changes. Inter-ToM (Eq. 2) uses a time-discounted Monte Carlo estimate across episodes to provide accurate priors (Section 4.1). The concrete example in Section 5.2 (SSH, where PToM corrects false beliefs about exploiters) illustrates how the two levels work together: intra-ToM corrects inference within an episode while inter-ToM accelerates convergence across episodes.

- **Empirical evaluation across three structurally distinct SSD paradigms (SSH, SS, SPD) with multiple baselines demonstrates consistent superiority.** PToM achieves the highest min-max normalized scores in the large majority of self-play and few-shot adaptation matchups (Tables 1, 2). In self-play, PToM achieves near-optimal reward in SS and ties the Nash equilibrium in SPD. In few-shot adaptation, PToM outperforms all baselines in most row/column combinations across the three environments, including against exploiters in SSH and SS where the gap is large (Section 5.2). This breadth across three canonical dilemma types (assurance, chicken, prisoner's dilemma) supports the claim of generality.

- **PToM avoids the joint-action-space explosion of multi-agent MCTS by using goal-conditioned policies to simulate opponent behavior and sampling goal combinations.** The comparison with Direct-OM (which uses opponent modeling without MCTS) shows PToM consistently outperforming it, demonstrating that the planning component adds value beyond goal inference alone (Section 5.2).

## Weaknesses

### Fatal
None.

### Major

- **LI-Ref and Direct-OM are never defined, making key parts of the experimental results uninterpretable.** Table 2's caption states "normalization bounds set by the rewards of LI-Ref and the random policy," but LI-Ref is never introduced or described anywhere in the paper. Without knowing what LI-Ref is, the reader cannot determine whether a normalized score of 0.8 is good or merely adequate. Similarly, "Direct-OM" appears in Tables 1 and 2 and is mentioned in the text (Section 5.2) as a comparison point, but the paper provides no description of its design, training procedure, or how it differs from PToM. This is a significant documentation gap that undermines the evaluation.

- **No variance, confidence intervals, or multiple-seed results are reported for any experiment.** Multi-agent evaluation is inherently high-variance, and single-point estimates can be misleading, especially when differences between methods are modest (e.g., SPD results in Table 2(c)). Without any measure of statistical significance or even standard deviations, the reader cannot assess whether the reported differences are reliable or could disappear with different random seeds. This is a basic expectation for empirical MARL research.

- **The training procedure for the goal-conditioned policy contains an unresolved training-inference gap.** The opponent modeling module trains a neural network π_ω(a_j|s, g_j) using a cross-entropy loss (Eq. 3) on data tuples (s_j^{K,t}, a_j^{K,t}, g_j^{K,t}) "collected from episodes" (Section 4.1). However, the paper never explains how the goal label g_j for an *opponent* is obtained during training. The problem formulation states that "j's true goal is inaccessible to i" (Section 3). If the model is trained only on self-play data where all agents are PToM and goal labels are known by design (e.g., from a centralized replay buffer), then the model learns to predict behavior of PToM-like agents under known goals—not arbitrary unseen opponents. When later confronted with a LOLA or SI agent, the goal-conditioned policy may assign poorly calibrated likelihoods. The paper does not close this loop, and the method as described is underspecified on a critical detail that affects the validity of the entire few-shot adaptation claim.

### Minor

- **The ablation study is described in a single sentence with no quantitative results in the main paper.** Section 5.2 states: "Ablation study indicates that inter-ToM and intra-ToM play crucial roles in adapting to agents with fixed goals and agents with dynamic goals, respectively. Moreover, if opponent modeling is not conditioned on goals, the self-play and few-shot adaptation abilities are greatly weakened." No numbers, tables, or figures support these claims. While the appendix may contain details (the parser strips these), the main text alone is insufficient for the reader to evaluate the importance of each component.

- **Key MCTS and algorithm hyperparameters are not reported.** The number of MCTS samples N_s (introduced in Section 4.1), the search depth, the computational budget per step, the Boltzmann rationality coefficient β (introduced in Eq. 5), and the inter-ToM horizon weight α (Eq. 2) are all given no values or ranges. The network architectures, learning rates, and training details for PToM and baselines are not provided. This makes the results difficult to reproduce and assess.

- **The claim about "emergence of social intelligence" (including "self-organized cooperation" and "alliance of the disadvantaged") is mentioned in the abstract and one sentence in Section 5.2 without any quantitative evidence or systematic analysis.** If this is a claimed contribution, the paper should show measured behavioral metrics (e.g., frequency of joint stag hunts, timing of cooperative actions, conditions under which the alliance forms). As it stands, this is an unsupported assertion.

- **The adaptation phase allows opponents to "update their parameters if possible" (Section 5.2), which conflates adaptation to a fixed unseen policy with online learning against a co-adapting opponent.** These are different problem settings with different evaluation norms. The paper would benefit from clearly separating the two or justifying why they are treated together.

- **The hand-defined goal set is a genuine limitation that restricts the method to domains where goals are discrete and enumerable a priori.** The paper acknowledges this in the conclusion ("a clear definition of goals is needed for PToM"), which is commendable, but the scope of the contribution is reduced accordingly. The method performs classification over known templates rather than open-set goal discovery. This is worth flagging for readers considering real-world applications.

### Trivial
None.

## Nice-to-Haves

- **Comparison against more recent opponent-modeling and planning-based MARL methods** (e.g., M-FOS (Lu et al., 2022), Bayes-ToM, or planning-based approaches) would strengthen the empirical evaluation. The current baselines (LOLA 2018, SI 2019, A3C 2016, PS-A3C 2018) are somewhat dated. The paper's related work section does cite more recent work, but the experiments do not compare against them.

- **Wall-clock time or computational cost analysis** would help readers assess the practical applicability of PToM's online MCTS planning against simpler feedforward baselines.

## Removed Points

These points from the input reviews were identified as not valid and are listed here for transparency:

- **Criticism of the belief update derivation (Eq. 1)**: The reviewer claimed the simplification to b ∝ b·Pr(a|s,g) drops a dependency on the state transition that makes the equation invalid. This is incorrect as a criticism of the method—the derivation is a standard Bayesian update for goal recognition where the observed state trajectory is conditioned on, and the transition likelihood cancels or is absorbed into the normalization. The final update rule (Bayesian update of goal beliefs using action likelihoods only) is standard practice in the goal-recognition literature (Baker et al., 2017; Zhi-Xuan et al., 2022). Removed as a misunderstanding of standard methodology. *(Source: Harsh Critic, Critical Issues #1 and Section 4 section notes)*

- **Criticism that "no derivation is provided" for the intra-ToM update**: The derivation is explicitly provided in Eq. (1) with a three-line expansion. Removed as factually wrong. *(Source: Harsh Critic, Section 4.1 notes)*

- **Pure formatting/style nitpicks about table readability and prose style**: Removed per formatting artifact rules. *(Source: Harsh Critic, various)*

- **Criticism questioning whether cited baselines exist or are available**: Not present in the inputs. Not applicable.

- **"The 5-timestep termination rule in SSH is crucial; it is not stated whether all baselines are trained under the same rule"**: This is a reasonable question but concerns a standard experimental-control assumption. All agents in self-play (including baselines) are trained in the same environment with the same termination rule, as is standard. The paper describes the environment with the rule; there is no suggestion that different agents experienced different rules. Downgraded to Trivial-level concern; moved here since it does not affect any result interpretation. *(Source: Harsh Critic, Section 5.1 notes)*

- **Demand for comparison with I-POMDP and more discussion of representational assumptions**: The paper clearly states that I-POMDP's nested belief inference is computationally impractical in complex sequential environments—this is a well-known limitation, not an oversight. The paper's choice to avoid I-POMDP is defensible and the positioning is adequate. *(Source: Harsh Critic, Section 2 notes)*

- **Complaint that "the paper should also discuss how goal sets could be learned"**: This is scope creep—the paper acknowledges the limitation and identifies it as future work. Calling it a weakness rather than a direction for future research is unreasonable for a conference paper with a stated scope. *(Source: Harsh Critic, Critical Issues #3 and conclusion notes)*

- **Complaint that "the paper does not specify how the number or nature of goals is determined"**: The goal sets are defined by the environment semantics (Section 3, Section 5.1), which is standard for SSD benchmarks. Not an omission. *(Source: Harsh Critic, Section 3 notes)*

## Novel Insights

Beyond the paper's own contributions, the reviews surface a clear structural tension in the PToM approach: the method's key strength—hierarchical Bayesian goal inference with planning—depends on a fixed, pre-enumerated goal set and requires goal-labeled opponent data during training that is not naturally available in the few-shot adaptation setting. This tension between the method's reliance on structured supervision (known goal sets, labeled trajectories) and its claimed few-shot generalization to *unseen* opponents is not fully resolved. The paper would benefit from making the training-data generation process (including how goal labels are obtained) completely explicit, as this is the linchpin connecting the method's components. The reviews also highlight that the paper's evaluation, while broad in environments, is thin on statistical rigor—a pattern that is common in MARL papers but that undercuts the reliability of the reported results.

## Suggestions

1. **Define LI-Ref and Direct-OM clearly**, and add a dedicated subsection or paragraph in the experimental setup describing all baselines and normalization references.
2. **Run experiments with at least 5 random seeds and report means and standard deviations** (or confidence intervals) for all conditions. This is essential for MARL evaluation.
3. **Explicitly describe the opponent model training data pipeline**: how are (state, action, goal) tuples collected? Are goal labels available during centralized training? If so, state this clearly. If not, describe how the issue is addressed (e.g., EM, self-supervised learning, or restricting the claim).
4. **Add a quantitative ablation table** (even in the main text) showing the contribution of inter-ToM, intra-ToM, and goal-conditioned modeling separately.
5. **Report the values of MCTS parameters** (N_s, search depth, β, α) and key training hyperparameters (learning rate, network architecture dimensions).
6. **Either provide quantitative evidence for the "emergence of social intelligence" claim or remove it** from the abstract and main text, as it currently lacks support.

## Score and Decision

The paper proposes a novel and well-motivated architecture that combines hierarchical ToM-based goal inference with MCTS planning, and demonstrates consistently strong empirical results across three diverse SSD environments against several baselines. The core idea is sound and the contribution is potentially significant for the MARL/ToM community.

However, the evaluation has serious documentation gaps: LI-Ref and Direct-OM are undefined, no variance is reported, the opponent model training procedure is critically underspecified on how goal labels are obtained, and the ablation study is not quantified. These are fixable issues, but as presented, the evidence does not fully support the claimed contributions with sufficient rigor.

A score of 6 reflects that the paper has a genuine contribution that a program committee should take seriously, but the experimental presentation and methodological clarity need substantial improvement before the claims can be fully trusted.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>