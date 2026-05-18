Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper extends multi-step inverse kinematics to the challenging setting of Finite-Memory POMDPs (FM-POMDPs), where the agent-centric state is decodable from a short history but not from a single observation. The paper theoretically analyzes several inverse-kinematics-based objectives (All History, Forward Jump, Masked Inverse Kinematics, and their action-augmented variants), deriving their Bayes-optimal classifiers. It shows that MIK+A (Masked Inverse Kinematics with actions) provably recovers the agent-centric state via a reduction to Lamb et al. (2022), while alternative approaches such as AH+A collapse to trivial predictors and FJ+A can fail in constructed counterexamples. Experiments on navigation tasks with direct state estimation and on visual offline RL with induced partial observability support the theoretical findings.

## Strengths

- **Theoretical characterization of Bayes-optimal classifiers (Section 3.1).** The paper derives closed-form solutions for all proposed objectives, showing that MIK+A's optimal classifier depends only on agent-centric states $s_t$ and $s_{t+k}$ (Equation 1), AH reduces to a one-step inverse model, and AH+A collapses to a constant predictor. This cleanly explains why MIK+A can succeed where others fail.

- **Explicit counterexample proving failure of Forward-Jump objectives (Section 3.2, Figure 2).** The paper constructs an FM-POMDP with $m=3$ where FJ and FJ+A cannot separate states because they lack access to intermediate $k$ values ($k=2,3$), while MIK+A works. This negative result rigorously demonstrates a case where the theoretical guarantee does not hold for FJ+A.

- **Direct empirical validation of state recovery in navigation (Section 4.1, Table 2, Figure 4).** In acceleration-control tasks with exogenous noise, MIK+A achieves the lowest state estimation error (e.g., 0.0% on "No Curtain" and 0.8% on "One Curtain"), while AH+A performs worst. The paper directly measures state recovery (not just proxy metrics), providing clean evidence for the central theoretical claim.

- **Identifies the double-edged role of past actions (Sections 3.1, 4.1).** The paper theoretically shows that augmenting with actions can either enable recovery (MIK+A) or cause catastrophic failure (AH+A collapses to trivial prediction), and experimentally confirms that AH+A has near-zero action-prediction loss yet poor state estimation. This nuanced finding distinguishes the contribution from naive baselines.

- **Demonstrates robustness in challenging visual offline RL with partial observability (Section 4.2, Figures 6, 7).** When observations are randomly patched and frames are zeroed, MIK+A significantly outperforms baselines (ACRO, DRIML, CURL, etc.) on Cheetah-Run, Walker-Walk, and Humanoid-Walk domains, showing that the insights translate to practical high-dimensional settings.

## Weaknesses

### Fatal

None.

### Major

1. **Future decodability (Assumption 2) is a strong condition whose robustness to violations is not analyzed.** The paper's central guarantee depends on both past and future decodability. The paper acknowledges that future decodability is violated in the navigation experiments (collisions with walls, line 133: "The agent's velocity before hitting the wall is then not decodable from any number of future observations"), and the empirical success despite these violations suggests robustness. However, the paper provides neither a theoretical characterization of how performance degrades under approximate future decodability nor a systematic empirical ablation varying the severity of violations. Since this assumption is novel to this work (unlike past decodability, which is inherited from Efroni et al. (2022b)), the reader lacks a clear understanding of when MIK+A works in practice and when it breaks down.

### Minor

1. **The empirical near-equivalence of FJ+A and MIK+A is acknowledged but the framing undersells the gap between theory and practice.** Section 3.2 shows a counterexample where FJ+A fails, and Table 1 lists FJ+A as having a "negative theoretical result." Yet in the navigation experiments (Table 2, Figure 4), FJ+A and MIK+A perform similarly. The paper honestly notes this (Section 4.1: "Another finding is that FJ+A and MIK+A are fairly similar, which suggests that the theoretical counterexample for FJ+A may not imply poor performance"), which is transparent but creates tension with the stronger theoretical claims. The paper would benefit from characterizing the conditions under which the FJ+A counterexample arises in practice and when it does not, rather than leaving the reader to reconcile the theory and evidence themselves.

2. **The pixel-based experiments (Section 4.2) evaluate downstream RL performance rather than directly measuring state recovery.** This is acknowledged in the paper's framing ("we also demonstrate the usefulness of the proposed objectives"), but it means the visual experiments don't directly confirm that the learned representation is the true agent-centric state — they only show better downstream task performance. The main state recovery evidence comes from Section 4.1 (navigation). While downstream performance is practically meaningful, adding a direct probe of state recovery in a pixel domain (e.g., using a simulator with ground-truth agent-centric state and controlled visual exogenous noise) would strengthen the connection between theory and the high-dimensional setting.

3. **The mapping from the theoretical assumptions to the pixel experiment setup (random patching + frame-zeroing) is not explicitly discussed.** The theory assumes an FM-POMDP with finite observation space, $m$-step past decodability, and $n$-step future decodability. The pixel experiments use continuous observations with randomized masking, where the decodability length $m$ may not be well-defined or constant. The paper does not discuss how the theoretical assumptions carry over to this setting.

4. **The self-prediction (SP) auxiliary objective is introduced (line 133) and shown to improve results, but its effect on the theoretical guarantee is not analyzed.** Since SP modifies the training objective with a term that involves learning a forward dynamics model, it is unclear whether it preserves the guarantee of recovering only the agent-centric state or whether it might introduce information from the exogenous noise. A brief theoretical discussion or an ablation isolating SP's effect would clarify this.

5. **No standard deviations or confidence intervals are reported for state estimation errors in Table 2.** Given that multiple random seeds were used, reporting variability would help assess the significance of the differences between methods.

### Trivial

- The paper references Theorem 5.1 of Lamb et al. (2022) but does not restate it, making the reduction hard to verify without external reading. A brief summary of the theorem's statement would improve self-containedness.

## Nice-to-Haves

- A systematic study of MIK+A's robustness under varying degrees of future-decodability violation (e.g., by controlling the frequency or severity of collisions in the navigation environment).
- A direct probe of whether the learned representation in the pixel experiments (Section 4.2) isolates agent-centric information from exogenous noise (e.g., linear probe on a held-out ground-truth state, controllability check, or decoding accuracy for agent-relevant vs. irrelevant attributes).
- Architecture details for the forward-backward sequence model (number of layers, hidden dimension, pooling strategy) could aid reproducibility.

## Removed Points

- *"The counterexample for FJ/FJ+A depends on a specific observation construction... It would be helpful to know whether environments with this structure actually arise in practice."* — The paper explicitly presents this as a theoretical counterexample (an existence proof of failure), not as a common-case finding. This is standard practice in theoretical analysis; the criticism misunderstands the purpose of a counterexample.

- *"The paper's reliance on Lamb et al. (2022) is heavy, but the reduction is sketched rather than formally stated."* — While the paper could be more self-contained, relying on prior work and sketching the reduction is standard and within acceptable norms for a conference paper.

- *The harsh critic's "Other Observations" about the FJ counterexample being an existence proof only is reframed by the paper's own language as exactly that — a counterexample. Not a weakness.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension between the paper's theoretical framing (FJ+A fails) and the empirical results (FJ+A works similarly to MIK+A), but the paper itself acknowledges this tension. The reviews do not add a novel synthesis beyond what the paper already states.

## Suggestions

1. Add a systematic robustness analysis for violations of future-decodability — either theoretical (e.g., bounds on state recovery error under approximate decodability) or empirical (varying the severity of violations in a controlled setting). This would directly address the strongest limitation of the current work.
2. Provide a direct state-recovery evaluation in a pixel-based domain with ground-truth agent-centric state (e.g., a rendered simulator with known position/velocity) to bridge the theory and the visual experiments.
3. Clarify the practical significance of the FJ+A counterexample: when do the conditions that cause FJ+A to fail actually arise in realistic environments, and when is the failure mode avoidable?
4. Add standard deviations/confidence intervals to Table 2.

## Score and Decision

This paper makes a genuine theoretical contribution by rigorously analyzing which inverse kinematics objectives recover the agent-centric state in FM-POMDPs — a setting that prior work on agent-centric state discovery had not addressed. The theoretical analysis is sound (the Bayes-optimal classifier derivations, the counterexample for FJ+A, and the reduction to Lamb et al. (2022) for MIK+A), and the navigation experiments directly validate the core claim of state recovery. The pixel experiments demonstrate practical utility even if they do not directly confirm state recovery. The main weaknesses are (a) insufficient stress-testing of the novel future-decodability assumption, and (b) a tension between the theoretical critique of FJ+A and its empirical success. Neither issue invalidates the core contribution; both are addressable. The paper is clearly written, and the combination of theory + clean navigation experiments + challenging visual RL experiments makes it a valuable contribution to the community.

**MY FINAL SCORE: <score>7.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**