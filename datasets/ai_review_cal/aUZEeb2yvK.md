- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and can carefully cross-check all claims. Let me produce the consolidated review.

---

## Summary

This paper introduces QMP (Q-switch Mixture of Policies), a framework for sharing behavior across tasks in multi-task reinforcement learning via selective off-policy data collection. At each state, a task's Q-function selects which policy from the full set of task policies to execute for one step, thereby incorporating helpful behaviors from other tasks without biasing the training objective. The paper provides theoretical claims about monotonic improvement and convergence, a didactic illustrative example, and experiments across manipulation, locomotion, and navigation domains showing that QMP provides complementary gains on top of parameter-sharing, data-sharing, and no-sharing MTRL baselines.

## Strengths

1. **Novel and principled form of information sharing for MTRL.** Prior behavior-sharing methods (Distral, DnC) use regularization to a common policy, which biases individual task objectives when tasks conflict. QMP instead shares behaviors only during data collection, keeping each task's training objective unbiased. This is a clean and well-motivated conceptual advance. (Lines 36-41, 125-127)

2. **Consistent empirical complementarity across diverse frameworks.** Figure 3 (complementary experiments) shows QMP providing additive or synergistic gains on top of No-Sharing, Parameter-Sharing, and Data-Sharing baselines across 6 environments. The Maze Navigation result is especially compelling: Parameter-Sharing + QMP outperforms both Parameter-Sharing alone *and* No-Sharing + QMP, demonstrating that behavior sharing and parameter sharing combine constructively. (Lines 410-420, Fig. 3)

3. **Strong ablation isolating the value of selective selection.** The comparison of QMP vs. QMP-Uniform (60% success) and QMP-Domain-Knowledge (early plateau) in Figure 7 cleanly demonstrates that the Q-switch mechanism itself — not just the presence of multiple policies — drives the performance gains. (Lines 494-496, Fig. 7)

4. **Empirical evidence of selective identification of conflicting behaviors.** Figure 6a tracks mixture probabilities for Multistage Reacher Task 0: the conflicting Task 4 policy is selected at very low rates throughout training, while overall sharing from other tasks decreases as the task's own policy improves. This directly supports the claim that the Q-switch discriminates between helpful and harmful sharing. (Lines 457-458, Fig. 6)

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1's pointwise Q-value guarantee is not adequately justified by the reasoning in the main text.** Theorem 1 claims that $Q^{\pi_i^\text{mix}}(s_t, a_t) \geq Q^{\pi_i}(s_t, a_t)$ for all state-action pairs. The justification provided (lines 225-226) is that the $\arg\max$ operation in Eq. 6 "ensures that the selected policy $\pi_i^\text{mix}$ optimizes the SAC objective at least as well as $\pi_i$ itself." This reasoning addresses single-step action selection, but the claim is about the Q-function of the full mixture policy (which is non-stationary and follows a different trajectory distribution than any individual base policy). Pointwise Q-value dominance does not obviously follow from per-state KL improvement of the selection rule. The proof is deferred to the appendix, but the main text should provide a clear sketch of why the claim holds; the current sketch is insufficient and gives an impression of overclaiming. This is the paper's most significant weakness because it inflates the theoretical contribution beyond what the intuitive argument supports.

2. **The practical approximation of the selection criterion is presented without analysis.** Line 207 states that in practice, the expectation in Eq. 6 is estimated by evaluating $Q$ on the mean action of each policy, and the entropy term is dropped. This replaces $\mathbb{E}_{a\sim\pi'}[Q(s,a)] + \alpha\mathcal{H}(\pi')$ with $Q(s, \mu_{\pi'}(s))$. For stochastic policies with nonlinear Q-functions, $\mathbb{E}[Q(s,a)] \neq Q(s,\mathbb{E}[a])$, and dropping the entropy term could systematically disadvantage high-entropy (more exploratory) policies. The paper does not study the impact of this approximation, nor does it discuss whether the theoretical guarantees (which apply to the ideal criterion) survive under the approximation.

3. **The claim that QMP is "at least as sample-efficient" is not formally substantiated.** The paper argues that larger policy improvement steps → fewer iterations to convergence (Figure 4, Theorem 2 cited in appendix). Even if one accepts the per-iteration improvement claim, the relationship between "larger per-iteration improvement" and "sample efficiency" depends on data distribution and coverage properties that are not analyzed. The didactic example (Section 5.2) uses fixed auxiliary policies, not the concurrent learning setting, so it does not substitute for this analysis. The formal claim of guaranteed sample efficiency is stronger than what the evidence supports.

### Minor

1. **No wall-clock time or computational cost reporting.** QMP requires evaluating $N$ policies and $N$ Q-functions at each decision step. For MT50 ($N=50$), this is a substantial overhead. The paper mentions this briefly (line 207) but does not report wall-clock time or analyze whether the sample efficiency gains offset the per-step computational cost. This is important for practitioners evaluating the method.

2. **Baseline scope is limited in one direction.** While the complementary experiments appropriately use simple, popular base methods (multi-head SAC, UDS), the behavior-sharing comparison uses DnC (2018) as the main prior-work baseline. The paper's core claim is to introduce a *new form* of sharing (behavioral policy sharing), so comparison with the most directly relevant prior work on behavior sharing is natural. Still, including one more recent MTRL method (e.g., PCGrad or a gradient-based approach) in one environment would have strengthened the positioning relative to broader MTRL literature.

3. **Limited discussion of failure modes.** The conclusion mentions that improvement is limited by "the degree of shareable behaviors and the suboptimality gap" (line 505), but does not discuss scenarios where QMP could hurt — e.g., when all task policies are poor early in training, the mixture might repeatedly select poor actions, or the Q-function's estimation error could systematically select harmful policies. A candid discussion of such failure cases would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- An analysis (even brief) of how using the mean-action approximation affects selection quality vs. the exact criterion would significantly strengthen confidence in the practical method.
- Wall-clock timing data for a representative environment would help practitioners assess the compute-vs.-efficiency tradeoff.
- Including QMP on top of one more recent MTRL method (e.g., PCGrad or a soft-modularization approach) in a single environment would sharpen the complementary claim.

## Removed Points

- **Criticism that the KL-to-E[Q]+αH equivalence is approximate.** The harsh critic claimed the equivalence holds "only if the target is exactly exp(Q/α)/Z," but this is the standard SAC target and the equivalence is exact (D_KL = -1/α(E[Q]+αH) + const). This criticism is factually incorrect and is removed.

- **Criticism about missing proof sketch in main text / deferred proofs.** Rules state: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections; they exist in the original submission." The substantive core of the theoretical criticism (that the pointwise claim is not clearly justified by the reasoning given) is retained in Major weakness #1; the complaint about the proof being absent from the main text is removed.

- **Criticism that the didactic example uses fixed policies and does not demonstrate simultaneous learning.** The paper explicitly frames this as an illustration of the mechanism (Section 5.2) and states that the MTRL experiments address the simultaneous learning case (line 289). The criticism is addressed by the paper and is removed.

- **Complaints about statistical significance testing, overlapping shaded regions, confidence intervals.** Learning curves with mean/std over 5 seeds is standard practice in the RL community. Removed as a style/format nitpick.

- **Criticism that hyperparameter tuning may disadvantage baselines.** Using the same hyperparameters across methods is standard practice. Removed as speculative.

- **Complaint that the "overestimation" statement lacks justification.** The paper provides justification (line 210: "the soft policy evaluation step stays the same, i.e., it uses π_i and not π_i^mix"). Removed as the paper does address this.

- **Strength Finder's claim #5 about the didactic example being a core strength.** The didactic example is illustrative but limited (uses fixed policies, not the concurrent MTRL setting). It is better characterized as supporting intuition, not a core strength. Downgraded from the strengths list.

- **Strength Finder's claim about "Theorem 2" (mislabels Theorem 1) and the pointwise guarantee being a strength.** Given the concerns about this theorem's justification, this is not an unambiguous strength. Removed; the theoretical claim is discussed as a weakness.

## Novel Insights

The reviews surface one genuinely interesting tension that the paper itself does not fully engage with: the practical approximation (using $Q(s, \mu(s))$ without the entropy term) is quite distant from the theoretically justified criterion, yet the method works well empirically. This suggests either that (a) the entropy term matters less in practice than theory suggests, (b) the mean-action approximation introduces a beneficial inductive bias, or (c) the method's success is robust to significant deviations from the ideal selection rule. Understanding which of these holds could yield useful insights for the broader RL community and is worth investigating.

## Suggestions

1. In the main text, replace the overly strong pointwise Q-value guarantee with a more carefully qualified statement. For instance, state that $\pi_i^\text{mix}$ is at least as good as $\pi_i$ at optimizing the per-state SAC improvement objective, which empirically leads to faster learning (as supported by ablations). Reserve the stronger formal claim for the appendix with a rigorous proof.

2. Add a short paragraph or ablation that analyzes the mean-action approximation. A simple experiment comparing full-criterion selection vs. the approximate version (even on the didactic 2D point task) would ground the practical implementation in evidence.

3. Include wall-clock training time for at least one environment (e.g., MT10) to help readers assess the computational cost tradeoff.

4. Expand the limitations paragraph to explicitly acknowledge scenarios where QMP could be detrimental (e.g., early training when all policies and Q-functions are poor, or when estimation error dominates selection).
