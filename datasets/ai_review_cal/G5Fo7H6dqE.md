- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

---

## Summary

This paper proposes iDQN (iterated Deep Q-Network), which extends DQN by training multiple online Q-functions in a telescoping chain, each learning a consecutive Bellman iteration. Multiple online networks are trained simultaneously using a multi-term loss where each Q-function's target is derived from the preceding target network. The paper provides an informal theoretical analysis arguing iDQN controls approximation errors better than DQN, validates the idea on a low-dimensional Car-On-Hill problem, and shows empirical gains on 54 Atari 2600 games, including ablations that isolate the benefit of more gradient steps per Bellman iteration and more Bellman iterations per gradient.

---

## Strengths

1. **Empirical outperformance on the standard Atari 2600 benchmark (54 games).** Figure 7a shows iDQN achieves a higher IQM human-normalized score over DQN (Adam) on the standard 54-game Atari suite, with non-overlapping 95% confidence intervals. This is the primary evidence that iDQN delivers on its central claim.

2. **Well-designed ablations that isolate the two mechanisms of improvement.** Figure 8 (right) controls for total gradient steps and Bellman iterations, showing iDQN's advantage comes from performing more gradient steps per Bellman iteration without overfitting. Figure 9 (left) controls for gradient steps per iteration, showing iDQN's advantage also comes from performing more Bellman iterations. These dissect *why* iDQN outperforms DQN beyond the aggregate metric.

3. **Low-dimensional validation linking to theory.** Figure 6 shows on the Car-On-Hill problem that increasing \(K\) reduces the distance to the optimal value function earlier in training, directly supporting the theoretical error-propagation intuition.

4. **Demonstrated orthogonality to IQN.** Figure 8 (left) shows that iIQN (iDQN + IQN) outperforms both iDQN and IQN individually on 5 Atari games, suggesting the method can combine with distributional RL approaches.

5. **Computational efficiency.** The paper reports iDQN with \(K=5\) runs in under 3 days on an NVIDIA RTX 3090 using JAX, taking about the same time as IQN—addressing a natural concern about the cost of training multiple heads.

---

## Weaknesses

### Fatal

None. The paper is complete, the algorithm is clearly described (text + architecture figure + rolling step explanation), the experiments are carried out, and the results support the claimed improvements over DQN. No flaw in the paper invalidates its core claims.

### Major

1. **Missing critical baselines that would isolate the claimed mechanism.** The main results (Figure 7) compare iDQN to DQN (Nature), DQN (Adam), and C51. The paper argues "we do not consider other variants of DQN to be relevant baselines…since iDQN can be combined with another variant of DQN." This reasoning conflates orthogonality with comparison necessity. To attribute iDQN's gains to its specific chaining mechanism (rather than generic benefits of multiple heads, more effective gradient steps, or a better empirical operator), the paper should include direct empirical comparisons to:
   - **Double DQN**: a standard DQN variant that also modifies the learning dynamics (by debiasing the Bellman target) and is not compared at all.
   - **n-step DQN**: mentioned only in a brief 3-game comparison (Figure 16) despite being the most natural competitor, since both methods use multiple consecutive targets.
   - **A version of iDQN with independent (unchained) heads**: to verify that the telescoping structure, not just having K heads, drives the improvements.
   
   Without these comparisons, the experiments do not fully substantiate that iDQN's specific telescoping mechanism—as opposed to simply having more parameters or better gradient accumulation—is responsible for the gains.

2. **Theoretical analysis is informal and not fully connected to the practical algorithm.** The analysis in Section 5 makes several strong simplifying assumptions (offline setting, \(K=2\), no rolling steps have occurred, \(H\) smaller than both target update and rolling frequencies) that sever the connection to the online deep RL setting used in the main experiments. The comparison between Equations (4) and (5) is intuitive—DQN's second term is a Bellman error while iDQN's is an online-target distance—but the derivation of these bounds from Theorem 5.1 is not shown, and the bounds are stated rather than derived. Moreover, Theorem 5.1 is an offline AVI result about a fixed sequence of \(K\) iterations, whereas iDQN's rolling procedure discards early heads and slides a window, meaning the theorem's clean sequence is not maintained over the course of training. The paper does not reconcile this mismatch. The analysis is suggestive but not rigorous enough to be counted as a "proof" of iDQN's advantage.

3. **Limited game coverage for secondary claims.** Several important claims rest on limited data:
   - iIQN (iDQN + IQN) is shown on only 5 Atari games (Figure 8 left)—insufficient to establish general improvement.
   - iDQN+3-step return's competitiveness with Rainbow, IQN, and Munchausen DQN is shown on only 10 games (Figure 7b), not the full 54-game suite.
   - The comparison to n-step DQN (Figure 16) covers only 3 games.
   
   While the 54-game DQN comparison is the paper's main result, the broader claims about orthogonality and competitiveness with advanced methods need stronger evidence.

### Minor

1. **Ambiguous notation in the loss function.** Equation (1) writes \(\mathcal{L}_{\mathrm{iDQN}}(s,a,r,s'|\theta,\bar{\theta})\) where the same \(\bar{\theta}\) appears to parameterize all target networks \(\bar{Q}_{k-1}\). The text and architecture diagram (Figure 3) clarify that there are distinct target heads, but the notation as written could mislead a reader into thinking all targets share identical parameters. Clarifying that \(\bar{\theta}\) denotes the collection of all target head parameters would improve clarity.

2. **Hyperparameter sensitivity is underexplored.** The two new hyperparameters (rolling step frequency \(R=6000\), target update frequency \(T=30\), \(K=5\)) are set based on intuition rather than systematic tuning. The ablations in Figure 9 (middle, right) test only extreme changes on 2 games. A broader sensitivity analysis across more games would strengthen the practical guidance for using iDQN.

3. **Behavioral policy selection is lightly justified.** The paper tests several sampling strategies (Figure 14) and argues for uniform sampling across heads, but only on 3 games with no clear performance difference except for Asteroids. The choice matters for the algorithm's correctness but is not rigorously motivated.

4. **Number of seeds is on the lower side.** 5 seeds per game with IQM partially mitigates this, but the confidence intervals would tighten with more seeds, especially for the 10-game and 5-game comparisons.

### Trivial

None.

---

## Nice-to-Haves

- A comparison to Bootstrapped DQN (Osband et al., 2016), which also uses multiple heads with shared representations, would help clarify the difference between ensemble-based exploration and iDQN's chained Bellman iterations.
- A direct comparison showing iDQN vs. DQN with the same number of gradient steps per sample (i.e., matching the higher gradient-to-sample ratio) would further isolate the chaining benefit from the gradient accumulation effect, complementing Figure 8 (right).
- A sensitivity analysis of \(K\) (beyond the 3 games in Figure 13) would help practitioners select this parameter.

---

## Removed Points

- **"Loss function is internally inconsistent and likely incorrect"** (from Harsh Critic). This claim is incorrect. The loss function uses \(\bar{\theta}\) as collective notation for all target network parameters; the text ("The target for the second online network is created from a second target network that is frequently updated to be equal to the first online network"), the rolling step description (new heads added with distinct parameters), and the architecture diagram (Figure 3) make the chaining mechanism unambiguous. The notation is compressed but not contradictory.

- **"Theoretical proof does not establish a benefit" / "flawed in multiple ways"** (from Harsh Critic). This claim overstates the issues. The analysis is informal (as the paper acknowledges by context), but the comparison between Equations (4) and (5) is conceptually valid: DQN's second term is the Bellman error \(\|\Gamma^* Q_1 - Q_1\|\) (not directly controllable by the TD loss), while iDQN's second term is the online-target distance \(\|Q_1 - \bar{Q}_1\|\) (controllable via target update frequency and learning rate). The asymmetry the critic labels "unjustified" is real—the two error terms are genuinely different. The analysis is limited, not invalid.

- **"Theorem 5.1 does not apply to rolling procedure"** (from Harsh Critic). The paper's analysis in Equations (4)-(5) is specifically for the pre-rolling regime with \(K=2\) and no rolling step performed, not for the full rolling procedure. The paper does not claim the theorem applies to the rolling window; it uses the theorem to motivate the sum-of-errors bound and then separately compares the two algorithms in a controlled setting. The criticism is valid as a limitation but not as a fatal flaw.

- **"Reproducibility concern about loss implementation / code not released"** (from Harsh Critic). The paper states code will be released. This is a standard practice and not a valid criticism of the submission.

- **Various nitpicks about missing appendix content, formatting, and speculative "what if" scenarios** (from Harsh Critic). Removed per instructions.

- **Generic/superficial strengths from Strength Finder** (e.g., "this paper addressed an important problem"). These lack specific evidence and are removed.

- **"Paper acknowledges limited computation but does not discuss memory overhead"** (from Harsh Critic). The paper reports running under 3 days on an RTX 3090 with shared convolutional layers, which implicitly addresses the practical resource question. Memory overhead of K heads is not discussed but this is not a central weakness.

---

## Novel Insights

The reviewers' contrast surfaces a useful observation: the paper's core conceptual contribution—that you can learn multiple Bellman iterations simultaneously by chaining online networks—is genuinely different from prior work on modifying the Bellman operator (double DQN, n-step) or changing the function space (dueling, distributional RL). Both reviewers agree the idea is interesting and well-motivated. The real tension is between the paper's ambitions (theoretical proof, orthogonality to all DQN variants) and what is actually delivered (informal analysis, comparison to a narrow set of baselines). The gap is not in the quality of the core algorithmic idea, which is sound and empirically validated against DQN, but in the scope of evidence marshaled for the broader claims.

None beyond the paper's own contributions.

---

## Suggestions

1. **Add double DQN and n-step DQN as baselines to the main 54-game comparison** to demonstrate that iDQN's gains are not simply achievable by these simpler modifications.
2. **Add an ablation with independent (unchained) heads** to verify that the telescoping target structure, not just the presence of K heads, drives improvement.
3. **Extend the game coverage for iIQN and iDQN+3-step** beyond 5 and 10 games respectively to substantiate the claims of orthogonality and competitiveness with distributional methods.
4. **Clarify the loss notation** by explicitly writing \(\bar{\theta}_1, \dots, \bar{\theta}_K\) (or equivalent) for the target parameters to avoid ambiguity.
5. **Acknowledge the limitations of the theoretical analysis** more explicitly: note that it assumes no rolling has occurred, that it is restricted to \(K=2\), and that it is offline—then discuss whether and why these insights should transfer to the online deep RL setting.

---
