I have verified all claims against the paper. Here is my final consolidated review.

---

## Summary

This paper proposes Bold Actor Conservative Critic (BACC), a model-free RL algorithm for continuous control that uses a double-Q softmax operator to construct two policies: a "bold" exploration policy \(\pi_E\) derived from the maximum of two Q-functions (greedy Q) and a conservative optimization policy \(\pi_O\) derived from the minimum (conservative Q). The policy \(\pi\) is trained by minimizing KL-divergence to \(\pi_O\), while \(\pi_E\) guides data collection. Experiments on MuJoCo and Roboschool benchmarks show strong results, particularly a large improvement on Humanoid-v2.

## Strengths

1. **Novel Q-value-guided exploration mechanism using overestimation constructively.** The paper identifies that taking the maximum of two Q-functions (greedy Q) increases the probability mass on high-Q actions beyond what a single Q-function provides, and exploits this overestimation to construct a bolder exploration policy. Figure 2 provides an intuitive visualization, and Figure 5(c) empirically confirms that \(\pi_E\) (greedy Q) outperforms \(\pi_Q\) (single Q) for exploration on Humanoid-v2.

2. **Clear empirical breakthrough on the challenging Humanoid-v2 environment.** Figure 3(a) shows BACC achieving roughly 8k average return in 3M steps on Humanoid-v2 — a substantial improvement over SAC, TD3, OAC, and RRS. This demonstrates that Q-value-guided OOD exploration is particularly effective in high-dimensional, complex control tasks.

3. **Explicit formulation linking conservative Q-values to stable policy learning.** While prior methods (e.g., TD3, SAC) empirically use the minimum of two Q-functions for policy gradients, this paper explicitly frames the policy update as minimizing KL divergence between a parameterized policy and a conservative policy \(\pi_O \propto \exp(Q^{\min})\), providing a cleaner justification for the design choice.

4. **Ablation directly validating the exploration policy design.** Figure 5(c) compares exploration with \(\pi_E\) (greedy Q) against \(\pi_Q\) (single Q) on Humanoid-v2 and shows clear performance gains for \(\pi_E\), directly supporting the claim that the overestimation-based exploration strategy is beneficial.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Overclaimed empirical results relative to evidence.** The abstract and introduction claim "superior performance compared to previous state-of-the-art methods across a range of environments." However, the results in Figure 3 show clear superiority only on Humanoid-v2. On Ant-v2, BACC is worse than RRS. On HalfCheetah-v2, it is more sample-efficient but achieves comparable final performance. On Walker2d-v2, Hopper-v2, and Swimmer-v2, results are essentially tied with baselines. The paper's own narrative descriptions (line 242) are more measured than the abstract, but the abstract-level claim should be refined to accurately reflect the evidence.

2. **Theorem 1 is stated without clarifying its relationship to the method's claims.** Theorem 1 states that "the value function \(Q_t\) converges to the optimal value function \(Q^*\)" under the DDQS operator. But the paper later claims (line 16) that "both two Q functions will eventually converge to the optimal Q-function" — it is not clear from the theorem statement whether "\(Q_t\)" refers to \(Q^1\), \(Q^2\), \(Q^{\max}\), or \(Q^{\min}\), or how the theorem guarantees convergence of both independently learned Q-functions to \(Q^*\). This gap between the stated theorem and the claims built on it undermines the theoretical narrative. (If the proof is deferred to an appendix that was stripped by the parser, the main text still needs to clarify the logical connection.)

3. **No confidence intervals or error bars on learning curves.** The paper reports mean curves over 6 seeds but provides no confidence intervals, standard deviations, or significance tests. Given the claim of "superior performance," statistical characterization is needed to assess whether observed differences are meaningful, especially on environments where performance is comparable.

4. **The finite-sample approximation for \(\pi_E\) is unanalyzed.** The exploration policy \(\pi_E\) is defined over the entire continuous action space (Equation 4), but in practice (Section 4.4) it is approximated by uniformly sampling \(s_n\) actions from a range \([\mu - s_r\sigma,\; \mu + s_r\sigma]\) and normalizing weights. The paper does not analyze how the hyperparameters \(s_n\) and \(s_r\) affect the quality of this approximation, whether high-Q actions outside the sampled region could be systematically missed, or how this approximation affects the theoretical guarantees. An ablation study on \(s_n\) and \(s_r\) would substantially strengthen the paper.

5. **Hyperparameter sensitivity of \(s_n, s_r, \beta_t\) is not studied.** These three key hyperparameters are introduced (Section 4.4) but never ablated. Without understanding their sensitivity, the reader cannot assess how robust the reported results are to different settings.

### Trivial

1. **The logical flow from Equation (2) to Equation (3) is confusing.** The paper introduces Equation (3) by saying "If we can sample actions from the policy \(\pi\) as follows…" but \(\pi\) has not yet been defined at that point in the exposition. The paper does subsequently clarify the prerequisite (line 156: "this transition necessitates that the actions sampled from \(\pi\) are as consistent as possible with the actions sampled from \(\pi_E\)"), but the presentation could be restructured for clarity.

2. **The temperature parameter \(\alpha\) from the maximum entropy objective (Section 2) is mentioned in the preliminaries but never specified in BACC.** The Q-function update (Equation 9) includes \(-\log\pi\) without an \(\alpha\) coefficient. It appears the paper implicitly sets \(\alpha=1\), but this is never stated. The interaction, if any, between \(\alpha\) and the \(\beta_t\) parameter is also not discussed.

## Nice-to-Haves

- Compare to more recent sample-efficient RL methods (e.g., REDQ, DroQ) to contextualize the empirical contribution.
- Provide wall-clock time or FLOPS comparison — sampling \(s_n\) actions per state and evaluating two Q-networks adds overhead relative to standard SAC.
- Study whether the improvement on Humanoid can be explained by a simpler mechanism (e.g., beneficial hyperparameter tuning) rather than the Q-value-guided exploration specifically.

## Removed Points

These points from the reviewer input were removed with justification:

- **"Inconsistency between the Q-function learned and the policies derived from it"** — REMOVED. This criticism is factually incorrect. The reviewer claims the policy should be proportional to \(\exp(Q - \log\pi)\), but in soft Q-learning / SAC, the policy is proportional to \(\exp(Q_{soft})\) where the soft Q-function already incorporates the entropy through its backup operator. The paper's formulation (\(\pi_O \propto \exp(Q^{\min})\) and Q-target including \(-\log\pi\)) is consistent with the SAC framework. No inconsistency exists.

- **"Exclusive policy is not new / missing citations"** — REMOVED per the rule against demanding missing related works. The paper does not claim novelty of the problem statement.

- **"The sentence about prerequisites is never followed up"** — REMOVED. The paper explicitly states (line 156) that the prerequisite is that "actions sampled from \(\pi\) are as consistent as possible with the actions sampled from \(\pi_E\)" and then describes how to learn \(\pi\) accordingly.

- **"Missing algorithm pseudocode"** — PARTIALLY REMOVED (downgraded). The algorithm is described textually in Section 4.4; the main text references line numbers that may correspond to an algorithm box stripped by the PDF parser.

- **"Missing proof for Theorem 1"** — REMOVED per the rule that parser-stripped appendix content (proofs) is not a valid weakness. However, the related point about the unclear logical connection between Theorem 1 and the method's claims is retained as a Minor weakness above.

## Novel Insights

The most interesting pattern across the reviews is the tension between the paper's strong empirical finding on Humanoid-v2 and its relatively thin theoretical scaffolding. The paper's core insight — that the overestimation property of \(\max\{Q^1, Q^2\}\) is actually *useful* for exploration even though it is detrimental for value estimation — is genuinely clever and worth developing. The practical success on Humanoid suggests this direction has real potential. However, the paper would benefit from clarifying that the theoretical claims are at the level of intuition-building (extending DBS to double Q) rather than a rigorous convergence proof of the full practical algorithm, since the finite-sample approximation and the decoupled Q-functions introduce gaps between theory and practice that are not analyzed.

## Suggestions

1. **Tone down the abstract-level claims.** Replace "superior performance across a range of environments" with a more precise characterization that highlights the strong result on Humanoid and honestly notes where results are comparable or mixed.

2. **Clarify Theorem 1's scope and relation to the method.** Specify which quantity \(Q_t\) refers to and whether the theorem guarantees convergence of both \(Q^1\) and \(Q^2\) individually, or only of the Bellman operator's fixed point. If the full proof is deferred to an appendix, include a proof sketch or intuitive justification in the main text.

3. **Add error bars / confidence bands to all learning curves.** With 6 seeds, standard errors or 95% confidence bands would greatly increase confidence in the reported comparisons.

4. **Include an ablation study on \(s_n\) and \(s_r\).** Show how varying these parameters affects the quality of \(\pi_E\) and downstream policy performance. This would address the main concern about the finite-sample approximation.

5. **Specify the value (or tuning procedure) of \(\alpha\)**, or clearly state that it is fixed to 1 and how this interacts with \(\beta_t\).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>