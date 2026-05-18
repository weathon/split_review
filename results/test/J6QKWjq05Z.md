Now I have thoroughly verified the paper against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes TreeDQN, an off-policy reinforcement learning method for learning branching heuristics in Branch-and-Bound (B&B) for Mixed Integer Linear Programs. The method adapts Double Dueling DQN to the tree MDP formulation where each action produces two child states, uses a mean squared logarithmic error (MSLE) loss to optimize the geometric mean of tree sizes, and leverages experience replay for sample efficiency. The paper claims three contributions: (1) a proof that the tree Bellman operator is contracting in mean, (2) a modified learning objective for geometric mean optimization, and (3) the TreeDQN algorithm. On a set of five NP-hard combinatorial optimization benchmarks, TreeDQN achieves lower geometric mean tree sizes than a REINFORCE baseline while requiring far fewer training episodes.

## Strengths

1. **Dramatically improved sample efficiency**: TreeDQN requires 21–560 training episodes to reach its best checkpoint, compared to 3,000–22,500 for the REINFORCE baseline (Table: numepisodes). This is a concrete, orders-of-magnitude reduction that directly addresses the high cost of solving MILPs during training.

2. **Consistent outperformance of prior RL method on test tasks**: On all five test distributions (Table: test), TreeDQN achieves a lower geometric mean tree size than REINFORCE (e.g., Set Cover: 57 vs 249, Facility Location: 392 vs 521). The method also generalizes reasonably to larger instances, beating REINFORCE on 3 of 5 transfer tasks (Table: transfer).

3. **Well-motivated loss function with supporting ablation**: The MSLE loss is motivated by the long-tailed distribution of B&B tree sizes (Fig. 2), and the ablation (Table: abl) shows it beats standard MSE in 4 out of 5 tasks, often by a meaningful margin (Maximum Independent Set: 47 vs 60).

4. **Honest distributional analysis via P-P plots**: The paper provides P-P plots (Fig. 6) that reveal nuanced behavior — TreeDQN excels on easier instances but can lag on harder ones for Maximum Independent Set. The paper openly discusses this limitation, which builds trust in the evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **The contraction-in-mean proof (Theorem 4.1) is not justified as stated.** The paper defines contraction in mean as \(\|TV - TU\|_\infty = p \cdot \|V - U\|_\infty\) with \(\mathbb{E}[p] < 1\). The derivation yields \(\|T^\pi V - T^\pi U\|_\infty \leq \gamma(p_+ + p_-) \|V - U\|_\infty\) and the proof claims \(\mathbb{E}[p_+ + p_-] < 1\) because "the tree is finite." This is insufficient. In the B&B setting with DFS node selection, every non-leaf node produces exactly two children (\(p_+ = p_- = 1\) for internal nodes), so \(p_+ + p_-\) is either 0 or 2. The expectation depends on the state distribution, which is not specified or controlled, and the mere finiteness of the tree does not resolve this. Furthermore, the experiments use \(\gamma = 1\) (Table: params), which tightens the requirement further. The argument does not constitute a valid proof, and this is listed as Contribution 1. The theorem can likely be repaired (e.g., with \(\gamma < 1\) and a proper weighted norm), but as presented it is unsupported. However, this does *not* invalidate the empirical results — the TreeDQN algorithm can work without this theorem, and the paper could drop or relocate the theoretical claim without harming the core contribution.

### Minor

1. **The REINFORCE baseline comparison, while valid, is not as strong as it could be.** The paper reports REINFORCE results from Scavuzzo et al. (2022), which is a published peer-reviewed baseline. However, the paper does not report wall-clock training time, does not perform a hyperparameter search for the baseline on these specific task distributions, and does not include the "tMDP+optimal" variant from Scavuzzo et al. (which uses optimal upper bounds during training and is the closer off-policy analog). Adding these would strengthen the sample-efficiency and performance claims. The claim of "significantly exceeds" would benefit from a statistical test (e.g., paired t-test or Wilcoxon) on the 40-instance evaluations.

2. **The connection between the contraction theorem and the algorithm is overstated.** Section 4.3 states "According to Theorem 4.1, the Bellman operator for a tree MDP process is contracting in mean. Hence, we can adapt DQN to minimize tree difference error." In practice, DQN works in many settings without such a theorem, and the theorem is not used to derive any specific algorithmic component (learning rate, architecture, convergence bounds). Framing the theorem as essential to the method inflates its role. This is not a fatal issue but the paper would be more honest presenting the theorem as an attempt at theoretical justification rather than a foundation.

3. **The paper uses \(\gamma = 1\) (undiscounted returns, Table: params), yet the contraction proof requires discounting to help establish \(\mathbb{E}[p] < 1\).** While undiscounted returns are standard in episodic finite-horizon settings, the choice conflicts with the theoretical framing. The authors should either use \(\gamma < 1\) and handle the resulting bias, or explicitly justify why \(\gamma = 1\) is acceptable despite the theoretical claims.

4. **No statistical significance tests.** The claims of outperformance (e.g., "significantly exceeds") are made without statistical tests. Given the high relative standard deviations (often >40%), adding confidence intervals or hypothesis tests would substantially strengthen the empirical claims.

### Trivial

- The paper mentions "Double Dueling DQN" but does not specify the dueling architecture (how the value and advantage streams are computed), the number of GCNN layers, or the hidden dimensions. These details would aid reproducibility.
- The ε-decay function is listed as a parameter in Algorithm 1 but its form is never described.

## Nice-to-Haves

- A wall-clock training time comparison between TreeDQN and REINFORCE would make the sample-efficiency claim more concrete (beyond episode counts).
- An ablation comparing tree-MDP DQN against a standard (temporal) MDP DQN would isolate the benefit of the tree-structured update from the loss function improvement.
- Reporting results from Scavuzzo et al.'s "tMDP+optimal" variant would provide a stronger off-policy baseline.

## Removed Points

These points from the reviewers were verified against the paper and found to be incorrect, misinformed, or not genuine weaknesses:

- **"The loss function in Algorithm 1 does not actually implement geometric-mean optimization"** (Harsh Critic, Issue 2): The reviewer claims the MSLE loss cannot optimize the geometric mean because each (s,a) pair has a single bootstrapped target. This is incorrect. In expectation over the data distribution, minimizing the per-sample MSLE loss \(\mathbb{E}[(\log|Q(s,a)| - \log|R|)^2]\) yields the conditional geometric mean \(\exp(\mathbb{E}[\log|R| \mid s,a])\). The stochastic gradient update using bootstrapped targets is a standard Monte Carlo approximation of this expectation. The paper's explanation (line 147) is informal but the core claim is sound. **[REMOVED — factually incorrect criticism]**

- **"The contraction theorem and algorithm are essentially disconnected"** (Harsh Critic, Issue 4): The claim that the theorem "is not used to derive any algorithmic component" is true of many theoretical justifications in applied RL papers. The theorem provides motivation for applying DQN to tree MDPs. This is a standard role for theoretical results in the literature. **[REMOVED — not a genuine weakness; standard practice]**

- **"P-P plot interpretation is sloppy"** (Harsh Critic, Other Observations): The reviewer claims "If one curve is higher than another, then the corresponding CDF is larger" is wrong because curves cross. But the paper itself acknowledges this for Maximum Independent Set: "When the tasks become more complex, it falls behind Imitation Learning and finally behind REINFORCE." The paper is transparent about where the claim does and does not apply. **[REMOVED — the paper already addresses this]**

- **"Ablation study shows inconsistent benefit"** (Harsh Critic, Other Observations): The MSLE loss beats MSE in 4 out of 5 tasks (Table 5). The single failure (Facility Location: 392 vs 352) is a minor exception, not an "inconsistent" result. The paper accurately states "for the majority of the tasks agent trained with a modified loss function achieves a lower geometric mean." **[REMOVED — mischaracterization of the data]**

- **"REINFORCE comparison not credible"** framed as fatal (Harsh Critic, Issue 3): The reviewer questions whether the REINFORCE baseline was "properly trained." The baseline numbers are from a published, peer-reviewed paper (Scavuzzo et al., 2022). While the comparison could be strengthened (see Minor weaknesses above), calling it "not credible" is unwarranted. **[DOWNGRADED from fatal to Minor]**

## Novel Insights

None beyond the paper's own contributions. The key insight — combining a tree-structured Bellman update with a log-space loss to handle long-tailed return distributions — is adequately articulated by the authors.

## Suggestions

1. **Fix or remove the contraction theorem.** As presented, Theorem 4.1 and its proof are not rigorous. Either provide a correct proof (using \(\gamma < 1\) and a proper weighted supremum norm, or a different theoretical framework) or drop the claim entirely and reframe the contribution as purely empirical. The paper's value does not depend on this theorem.

2. **Clarify the loss function's connection to geometric mean.** Replace the informal "for a variable y and targets t_i" derivation with a proper statement: minimizing the expected MSLE loss \(\mathbb{E}[(\log|Q(s,a)| - \log|R|)^2]\) yields the conditional geometric mean \(\exp(\mathbb{E}[\log|R| \mid s,a])\). This would eliminate the ambiguity the reviewer raised.

3. **Strengthen the empirical evaluation.** Add statistical significance tests for the comparisons. Include wall-clock time. If feasible, report the "tMDP+optimal" variant from Scavuzzo et al. to ensure the off-policy comparison is apples-to-apples.

4. **Add architectural details.** Specify the GCNN architecture (number of layers, hidden dimensions, dueling network structure) and the ε-decay schedule for reproducibility.

## Score and Decision

The paper addresses an important problem (learning branching heuristics for MILP) and proposes a sensible off-policy RL approach with a well-motivated loss function. The empirical results show genuine improvements in sample efficiency and tree size over prior RL methods. 

However, the paper's first claimed contribution — a proof of contraction in mean for the tree Bellman operator — is not justified as presented and misrepresents the theoretical foundation of the method. This is a significant weakness for a paper that lists it as a primary contribution. Combined with a baseline comparison that could be stronger and the absence of statistical tests, the paper falls short of the acceptance bar in its current form.

The empirical contributions (TreeDQN with MSLE loss, sample efficiency improvements) are real and valuable. A revised version that either fixes or removes the theoretical claim, strengthens the evaluation, and provides full architectural details could merit acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>