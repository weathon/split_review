## Summary

This paper models multi-step LLM preference alignment as a two-player constant-sum Markov game with per-step preferences, a novel formulation that generalizes single-step, chain-of-thought, and multi-turn scenarios. It proposes MPO (natural actor-critic) and OMPO (optimistic online gradient descent), provides a theoretical convergence guarantee of O(ε⁻¹) to ε-approximate Nash equilibrium for OMPO, and reports experiments on MT-bench-101 with Mistral-7B. The theoretical framework is interesting, but the paper suffers from a significant disconnect between the algorithm analyzed theoretically and the one actually run, and the empirical validation is too thin to support the claimed practical significance.

## Strengths

- **Novel formulation of multi-step RLHF as a two-player Markov game with per-step preferences.** The paper unifies single-step, chain-of-thought, and multi-turn alignment under one framework (Section 3, Examples 1–3), provides a concrete Bellman equation (Lemma 1), value difference lemma (Lemma 2), and occupancy-measure factorization (line 130). This goes substantially beyond bandit-level formulations in prior Nash-learning work (Munos et al., 2024; Wu et al., 2024).

- **Non-trivial theoretical convergence analysis.** The paper identifies that the partially observable nature of the Markov game prevents trivial extension of Alacaoglu et al. (2022) and describes how OMPO bypasses this by parameterizing the game over occupancy measures (line 19), yielding an O(ε⁻¹) convergence rate. This is a genuine technical advance, not incremental.

- **Practical implementation that avoids a separate critic network.** By using Monte Carlo estimation with a pre-trained pairwise reward model (PairRM) to estimate the Q-function (line 166), the paper provides a concrete computational recipe that connects the game-theoretic framework to real LLM alignment without requiring a learned value function approximator.

- **Ablation study supporting the step-wise design choice.** Figure 1(b) shows that using only the per-step preference at state \(s_h\) achieves similar winning rates to conditioning on the full trajectory suffix \([s_h,\dots,s_{H+1}]\), providing some empirical justification for the per-step approach.

## Weaknesses

### Fatal
None.

### Major

1. **Disconnect between the theoretically analyzed algorithm and the practical implementation.** The MPO update analyzed in Section 4.1 (line 154) uses the full Q-function \(Q_h^{\pi^t,\pi^t}(s,a,s',a')\), which includes expected future rewards from step h+1 to H (Equation 97). In practice (line 166), the paper states: "we estimate \(Q(s_h, a_h, s_h, a_h')\) by \(\mathbb{P}([s_h, a_h], [s_h, a_h'])\) to enhance the efficiency." This replaces the multi-step Q-function with the immediate per-step preference, discarding all future reward terms. The paper provides no argument — theoretical or empirical — that this simplified estimator preserves any of the convergence properties proven for the full update. The ablation in Figure 1(b) compares conditioning on the *observed* suffix \([s_h,\dots,s_{H+1}]\) vs. single step \([s_h]\), but the theoretical Q-function requires *expectation* over future trajectories under the opponent's occupancy measure — a fundamentally different object. The paper's headline theoretical guarantees therefore do not directly apply to the algorithm that was actually deployed, leaving an unresolved gap at the heart of the contribution.

2. **Limited experimental scope relative to claimed practical significance.** The experiments use only one base model (Mistral-7B-Instruct-v0.2), one dataset (MT-bench-101), and three iterations. No human evaluation is reported; the sole evaluation metric is GPT-4o mini scores over 3 rounds. No standard errors, confidence intervals, or significance tests are provided. For a paper whose third contribution is "practical implementations" with "considerable improvement," this level of evidence is insufficient to convincingly establish practical value. The math reasoning experiments are deferred to an appendix (inaccessible in the extracted text), so they cannot be assessed.

3. **Potential evaluation confounding from model selection.** The final model is chosen based on the highest winning rate against the base model as determined by PairRM (line 166) — the same model used to provide training supervision. This creates a risk that model selection favors methods exploiting PairRM's specific biases rather than reflecting genuine alignment quality. No discussion of this confound is provided.

### Minor

1. **Convergence rate comparison confounded by different feedback protocols.** The paper claims O(ε⁻¹) vs. O(ε⁻²) compared to Wang et al. (2023), Swamy et al. (2024), and Shani et al. (2024). However, those prior works use final-state preferences while this paper uses step-wise preferences — the problem settings differ on more than just the algorithm. Faster convergence (in policy updates) is partly attributable to the richer feedback (H signals per trajectory vs. 1), not solely to the algorithmic innovation. The comparison conflates two distinct sources of improvement.

2. **Unvalidated assumption about the per-step preference oracle.** PairRM — presumably trained on complete conversations — is used to provide preference comparisons at arbitrary partial prefixes \([s_h, a_h]\). No validation is provided that these partial-conversation preferences correlate with human judgment or are meaningful when the oracle cannot see the conversation's resolution. This assumption is foundational but unexamined.

3. **Missing strong baselines for multi-turn alignment.** The comparison is limited to DPO, SPPO, and Step-DPO variants adapted from bandit settings. Methods specifically designed for multi-turn RLHF (e.g., PPO with a step-wise reward model, rejection sampling, ReST) are not included, making it unclear whether the game-theoretic formulation adds practical value over simpler alternatives.

### Trivial
None.

## Nice-to-Haves

- A controlled ablation using only final-step preferences (setting per-step rewards to zero for \(h < H\) and only using the final comparison) would directly isolate the value of step-wise feedback from final-state-only signals.
- If the practical algorithm were modified to use proper multi-step Q-value estimation (even via Monte Carlo rollouts with sampled future steps), the theory-practice gap would be resolved.

## Removed Points
These points from the input reviews were removed per the filtering rules; treat them with caution:

- **Notation/formatting criticism about the learning rate expression** (line 151 containing garbled "loTg  Hπ2"): parser artifact, not present in original submission.
- **Criticism about Table 1 not being visible** in extracted text: parser artifact.
- **Strength about "comprehensive baseline comparison"**: conflicts with verified weakness about missing baselines.
- **Criticism about math reasoning tasks being deferred to appendix**: parser strips appendix content from all papers; not assessable.
- **Generic strengths about the problem being well-motivated or important**: removed as superficial/not specific to the paper's concrete content.

## Novel Insights

None beyond the paper's own contributions. The key observation from synthesis is that the paper's two main contributions — the theoretical convergence analysis and the practical algorithm — operate on substantially different versions of the method, and neither the paper nor the reviews identify a satisfying resolution within the current submission.

## Suggestions

1. **Bridge the theory-practice gap.** Either (a) modify the practical algorithm to use proper multi-step Q-value estimation (e.g., Monte Carlo rollouts sampling future steps under the current policy, or a learned value function) so it aligns with the theoretical analysis, or (b) develop theoretical guarantees for the one-step estimator, perhaps showing it corresponds to a specific relaxation whose convergence can be bounded.
2. **Substantially expand the empirical evaluation.** Add at least one more model family (e.g., Llama-3-8B), include human evaluation or a broader set of automated metrics, report variances/confidence intervals, and extend to more iterations to show convergence trends.
3. **Add a controlled ablation removing per-step feedback** (only using final-state preferences) to directly demonstrate that step-wise signals provide actionable information beyond what a final-state oracle could offer.
4. **Disentangle the convergence rate comparison** by distinguishing between improvements due to denser feedback and those due to the algorithmic innovation (optimistic gradient descent + occupancy-measure parameterization).

## Score and Decision

**Overall assessment:** The paper's formulation of multi-step RLHF as a two-player Markov game is novel and the theoretical analysis is technically substantive. However, the structural disconnect between the theory (which analyzes a full Q-function update) and the practice (which uses a one-step proxy with no convergence guarantees) undermines the paper's coherence. The experimental evaluation is too narrow to convincingly demonstrate practical significance. The paper would need significant revision — either aligning theory with practice or providing theory for the actual implementation, alongside substantially stronger empirical evidence — to meet the standard of a top conference.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>