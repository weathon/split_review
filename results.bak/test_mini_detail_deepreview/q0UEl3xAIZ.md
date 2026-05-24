Now I have sufficient calibration data. Let me compile the final review.

**Round 1 bracket:** Based on the calibration, the paper sits between ~4.5 and ~6.0. The low anchors (2-3) are clearly weaker papers with poor evaluation. The high anchors (7.5-8) are novel methods with strong theory and results. The current paper is closest to the 4.75-5.75 range.

**Round 2 narrowing:** Compared to the 5.25 anchor (RL-CFR, Reject) — that paper proposed a novel method but had theory/explanation issues. The current paper is cleaner and more focused but less novel (applying existing method). Compared to the 5.75 anchor (EVPA, Accept) — that paper proposed a novel method with strong practical results. The current paper is less novel and has a methodological concern, but is well-structured. The 4.75 anchor (Abstract World Models, Reject) had simple experiments and was less thorough. The current paper has more thorough experiments but a methodological gap.

The paper sits at about **5.0**. It's a clean empirical validation with an interesting result, but the methodological concern about training data composition and the modest contribution (applying existing method) prevent it from scoring higher.

---

## Summary

This paper applies Goal-Oriented Environment Inference (GOEI) — a previously proposed model-based RL algorithm for state reduction — to a competitive card game, Hol's der Geier. The authors show that GOEI reduces the observation space from 15,542 to 452 core states (2.9%) while achieving a median reward rate of −0.010 against a Nash equilibrium opponent, very close to the optimal 0.000. They compare against Q-learning and several simple strategies, analyze which features are preserved through mutual information, and study the sensitivity of the two hyperparameters.

## Strengths

1. **Substantial, well-documented state reduction.** The best GOEI configuration (β=0.2, α=25) compresses the observation space from 15,542 to 452 states across all rounds — a reduction to 2.9% — while maintaining a reward rate of −0.010, which is near-optimal against the NE baseline of 0.000 (Table 1, Figure 2B). At rounds 2 and 3, the number of representative states (|S₂*|=8, |S₃*|=31) is even smaller than the number of states used by the NE strategy itself (247 and 945), demonstrating that GOEI finds a representation simpler than the optimal strategy's own complexity.

2. **Clean experimental design separates environment inference from strategy optimization.** Training is performed offline on games between two fixed strategies (Rand vs. NE), and the learned models are tested independently against the NE opponent (Section 3.3). This isolates the quality of the state representation from the confounding effects of changing agent behavior, making the performance gains attributable to GOEI's reduction capability.

3. **Informative mutual information analysis.** The paper quantifies how much information about each of the five observable features (SD, CT, AH, OH, RT) is preserved or discarded in the reduced states (Figure 3). The finding that information about the current table card and remaining table cards is relatively preserved at early rounds while the score difference becomes important at round 4 is consistent with game-theoretic intuition and provides concrete evidence about what GOEI deems "core."

4. **Systematic hyperparameter analysis.** The paper evaluates 9 combinations of the Dirichlet process parameter α (11, 25, 50) and the Dirichlet distribution parameter β (0.1, 0.2, 0.3), confirming the expected trade-offs: small β accelerates early learning but causes instability later, large α slows convergence, and the intermediate setting (β=0.2, α=25) gives the best balance (Figure 4, Table 1). This provides practical guidance for tuning.

## Weaknesses

### Fatal
None.

### Major

1. **Training data includes games from the NE player's perspective, which may weaken the claim that state reduction alone drives performance.** The paper states that GOEI and Q-learning learn from games "both from the Rand player and from the NE player" (Section 3.3). This means 100 of the 200 training games per epoch are observed from the perspective of the NE strategy playing against a random opponent. The GOEI model learns transition dynamics from these games, which include transitions that occur under optimal play. While both GOEI and Q-learning observe the same data (so the comparison between them is fair), the paper's central claim — that GOEI achieves near-optimal play through state reduction — is not cleanly separable from the possibility that access to optimal transitions during training makes the learning problem easier. The paper does not provide a control experiment that trains exclusively on games from the Rand perspective (agent=Rand, opponent=NE) without including NE-perspective data. Addressing this would significantly strengthen the paper's main claim.

### Minor

1. **The "near-optimal" claim lacks statistical verification.** The best median reward rate is −0.010 (quartiles −0.012, −0.009), while the NE reward rate is 0.000. The paper describes this as "indistinguishable from zero" without a formal statistical test (e.g., a bootstrap confidence interval or one-sample test on the final-epoch reward rates). Given that all quartiles are negative, a small but systematic suboptimality may exist. The authors should report final-epoch (not epoch-averaged) reward rates with confidence intervals and test whether they differ significantly from zero.

2. **The mutual information analysis is per-feature and does not consider joint feature combinations.** The paper correctly notes that "the required information is maintained in complex combinations of all the features" (Section 4.2), but this conclusion is qualitative. The analysis shows that individual features lose most of their information, but it does not assess whether combinations of features are preserved. Computing mutual information between the state and joint feature sets, or checking whether reduced states cluster observations with the same optimal action, would strengthen the interpretability claim.

3. **The description of the training data composition is ambiguous.** Section 3.3 says "200 games were used for training per epoch" and "both from the Rand player and from the NE player," but it is not explicitly clear whether this means 100 games from each perspective or 200 games from each perspective. While the intent is inferable, the paper should state the split explicitly.

4. **The definition of the NE state count is imprecise.** Section 3.3 describes the NE state partition as "a set of equal expected rewards earned with players' actions" — this is vague. The paper should clarify how the NE state partition is computed algorithmically (e.g., whether it is based on the NE strategy's action-value equivalence classes or the NE value function's equivalence classes).

### Trivial
None.

## Nice-to-Haves

- Running a control experiment where training data includes only the Rand perspective (agent=Rand vs. opponent=NE) with the same number of games, to verify that GOEI's state reduction alone (not the presence of NE transitions) is responsible for the near-optimal performance.
- Including a baseline that ablates the state reduction component of GOEI (e.g., using GOEI without the Dirichlet process prior) to more directly isolate the effect of state compression.
- Reporting final-epoch reward distributions rather than epoch-averaged reward rates, to better characterize the asymptotic performance.

## Removed Points

These points were flagged by the reviewers but are removed from the main review for the reasons indicated:

- **Criticism about the 28,477 vs. 15,542 denominator for the reduction factor.** The paper's abstract explicitly states "2.9% (452 states) of all possible observations (15,542)" — the denominator is clearly stated. The 28,477 figure is mentioned earlier as the total combinatorial space, and the paper correctly distinguishes the two. No misrepresentation exists.

- **Criticism that the GOEI vs. Q-learning difference (0.07 reward) is "not large" given the total reward range of 2.0.** This framing is misleading. The relevant comparison is closeness to the optimal (0.000): GOEI is 0.01 away while Q-learning is 0.079 away — a factor of ~8×. Moreover, the key contribution is the state reduction (452 vs. 15,542 states), not simply the magnitude of the performance difference.

- **Criticism about the truncated y-axis in Figure 2A.** The y-axis range (−0.2 to 0.0) is standard and appropriate for showing learning curves that converge near zero. This is not a flaw.

- **Criticism about missing reproducibility details (random seeds, hardware, implementation).** The paper mentions 21 different seeds, lists the GPU used (NVIDIA RTX 4080 SUPER), and describes the variational inference procedure with tolerance and patience. This is adequate for a conference paper.

- **Strength about GOEI significantly outperforming Q-learning.** While factually correct, the comparison is somewhat expected — GOEI is a model-based method with explicit state reduction, while Q-learning is a tabular model-free method. The strength is retained in the summary but the contrast is not as surprising as the paper suggests.

- **Criticism about the interpretability claim being weak.** The paper itself acknowledges this limitation in Section 5: "we could not give a verbal explanation of the reduced state representation more concretely than Figure 3." This is a self-acknowledged limitation, not a weakness to be counted against the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already address or that is not evident from reading the paper.

## Suggestions

1. **Perform the control experiment** training GOEI on only Rand-perspective data (agent=Rand vs. opponent=NE), keeping the same number of games. If the results are similar, this would decisively validate the claim that state reduction is the driver of performance. If performance degrades, the paper should be reframed accordingly.

2. **Add a statistical test** for the final-epoch reward rate (e.g., a bootstrap confidence interval or a one-sample Wilcoxon test against 0) to support the "near-optimal" claim with quantitative evidence.

3. **Clarify the training data split** explicitly in Section 3.3 (e.g., "100 games from the Rand perspective and 100 games from the NE perspective").

4. **Consider analyzing mutual information between the state and joint feature sets** (e.g., conjunctions of features) to complement the per-feature analysis and strengthen the interpretability contribution.

5. **Report the final-epoch reward rates** separately from the epoch-averaged rates, to give a clearer picture of asymptotic performance.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| OZ3NXrF3gQ (reward-free RL) | 2.50 | R1 | Much weaker — lacks clear problem definition and rigorous evaluation. |
| hCfhfwSfCg (LLM goal exploration) | 2.00 | R1 | Much weaker — poor experimental design. |
| llXCyLhOY4 (multi-step GCRL) | 3.00 | R1 | Weaker — less clear contribution and experimental issues. |
| 7J0NsFXnFd (RL-CFR action abstraction) | 5.25 | R1/R2 | Comparable in rigor but more novel (proposes new method vs. applying existing). The current paper is cleaner but less ambitious. |
| MTcgsz1SHr (EVPA pruning/abstraction) | 5.75 | R1/R2 | More impactful — proposes new method, strong results on poker. The current paper is less novel and has a methodological gap. |
| nRgGCnw8eZ (KrwEmd abstraction) | 4.00 | R1 | Weaker — unclear novelty relative to prior work, narrower scope. |
| czpx02orl7 (abstract world models) | 4.75 | R2 | Similar tier — applies existing techniques to new problems, but the current paper has more thorough experiments. |
| sNZTtDRFXt (DRIVE distributional RL) | 5.75 | R2 | More novel (new method + theory) but presentation issues. Current paper is cleaner but less novel. |
| xIUUnzrUtD (HVM abstraction) | 6.50 | R1 | Stronger — proposes new model, multiple datasets, connects to cognitive science. Current paper is more narrowly focused. |

**Round 1 bracket:** 4.5–6.0. The paper is clearly above the 2–3 range (weak papers with poor experiments) and clearly below the 7.5–8 range (novel methods with strong theory and comprehensive evaluation).

**Round 2 narrowing:** The paper is slightly below the 5.75 anchors (EVPA, DRIVE) which propose new methods, and close to the 5.25 anchor (RL-CFR) which was rejected largely due to theory/presentation gaps. The current paper is cleaner than RL-CFR but less novel, and has a methodological concern that the RL-CFR paper did not have. The 4.75 anchor (abstract world models) had simpler experiments. The current paper is solidly between 4.75 and 5.75.

**Final score: 5.0.** The paper is a clean empirical validation of an existing method in a new environment. The state reduction result is well-documented and interesting. However, the methodological concern about training data composition weakens the central claim, and the contribution is modest (applying an existing method rather than proposing new techniques). The paper would benefit from the suggested control experiment and statistical verification.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>