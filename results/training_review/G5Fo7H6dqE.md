Now I have a comprehensive understanding of the paper and can cross-check all reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes iDQN, a value-based RL algorithm that learns multiple consecutive Bellman iterations simultaneously by chaining several online Q-networks with target networks in a telescoping fashion. The core idea is to use multiple Q-function heads (K=5) where each head approximates the next Bellman iteration, with a "rolling step" mechanism to advance to further iterations while maintaining constant memory. The paper evaluates iDQN on 54 Atari 2600 games, showing improvement over DQN, and demonstrates orthogonality by combining iDQN with 3-step returns and IQN.

## Strengths

- **Novel algorithm design with clear conceptual framing**: Learning multiple Bellman iterations simultaneously is a genuinely novel idea, and the geometric visualization in Q-function space (Figures 1–4) provides an intuitive and pedagogically valuable framework for understanding both DQN and iDQN. This conceptual contribution has value independent of the empirical results.

- **Solid empirical validation on 54 Atari games**: The main result (Figure 7a) shows iDQN achieves higher IQM human-normalized scores than DQN (Adam) on 54 games, with non-overlapping confidence intervals in later training frames (5 seeds per game). The use of the recommended aggregate metric (IQM with stratified bootstrap CIs) follows best practices.

- **Well-designed ablations isolating the core mechanism**: Figure 8 (right) carefully controls for total gradient steps and samples, comparing iDQN against DQN with matched per-iteration gradient steps. The ablation shows iDQN's advantage stems from better fitting per Bellman iteration, and that naively increasing DQN's gradient steps leads to overfitting. This is the cleanest evidence supporting the paper's central claim.

- **Computational practicality**: iDQN with K=5 runs in under 3 days on an RTX 3090 using JAX parallelization (approximately the same time as IQN), demonstrating that the multi-head approach does not impose prohibitive overhead.

## Weaknesses

### Fatal
None. The paper's core empirical claims are supported by the evidence presented.

### Major

- **Theoretical analysis is oversold and does not constitute a rigorous proof.** The abstract and introduction claim "We theoretically prove the benefit of iDQN," but Section 5 provides a heuristic argument rather than a proof. The comparison between Equation 4 (for DQN) and Equation 5 (for iDQN) compares different quantities — the second term for DQN is the Bellman residual ||Γ*Q₁ − Q₁||² while for iDQN it is γ||Q₁ − Q̄₁||²∞ — without deriving how these relate to the actual approximation errors ||Γ*Q_{k-1} − Q_k||² that appear in Theorem 5.1. The variable λ is referenced (line 113) but never formally defined. Furthermore, Theorem 5.1 from Farahmand (2011) applies to any sequence (Q_k), but the paper does not establish how iDQN's simultaneous training (where Q₂ is trained against Q̄₁, a delayed copy of Q₁, not Γ*Q₁) maps onto the theorem's sequential framework. The informal argument has intuitive appeal but falls short of the "proof" claimed in the abstract. This does not invalidate the empirical results, but it is a significant gap between claims and delivery.

- **Main empirical comparison relies on outdated baselines.** The headline comparison on 54 games is against DQN (Nature, 2015) and DQN (Adam) — algorithms that are over a decade old by the current date. While the paper demonstrates orthogonality by combining iDQN with 3-step returns (10 games) and IQN (5 games), these combination experiments are limited in scope. The paper claims that iDQN "performs similarly to REM" and that comparisons to modern methods exist in the appendix (Figures 20, 22), but for a 2026 venue, the main paper's comparisons to only DQN and C51 substantially weaken the perceived significance of the contribution. Stronger baselines directly in the main results would be needed to establish that iDQN offers a meaningful advance over the current state of the art, rather than over a decade-old method.

### Minor

- **Combined method results are limited in scope.** iIQN (iDQN+IQN) is evaluated on only 5 Atari games (Figure 8, left). While the results are encouraging, this is insufficient to establish that the improvement generalizes. Similarly, iDQN+3-step is compared against Rainbow, IQN, and Munchausen DQN on only 10 games (Figure 7b), and the paper does not provide statistical aggregation across these games. These experiments support the orthogonality claim but would benefit from at least the full 54-game benchmark.

- **Hyperparameter choices are intuitive but not systematically validated.** The choices K=5, rolling step frequency 6000, and target update frequency 30 are motivated by intuition (lines 132–133), and ablations on these parameters are shown on only 2–3 games (Figure 9). While the ablations are informative and the intuition is reasonable, the paper does not demonstrate that these choices are robust across the full benchmark. The sensitivity analysis is limited.

- **Algorithm description, while clear in concept, lacks pseudocode in the main paper.** The text describes the rolling step, target update mechanism, and sampling strategies adequately, but Algorithm 1 is referenced but not present in the extracted text (presumably in the appendix). Including a concise pseudocode or explicit update rules in the main paper would aid reproducibility. This is a presentation issue rather than a fundamental ambiguity.

### Trivial
None of significance.

## Nice-to-Haves

- A systematic hyperparameter sensitivity study across a larger subset of games would strengthen confidence in the defaults. Currently, the ablation is on 2–3 games.
- Direct comparison to Bootstrapped DQN under identical conditions would help disentangle whether the benefit comes from the Bellman iteration chaining or simply from having multiple Q-heads.
- Adding confidence intervals for the per-game results shown would improve interpretability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Serious ambiguity in the algorithm definition"** (Harsh Critic Point 3): The critic claims the algorithm is "impossible to reproduce." The paper describes the loss (Eq. 1), the K heads, the target update mechanism (frequency T), and the rolling step (add head K+1, remove head 1). While Algorithm 1 is in the appendix, the main text provides sufficient detail for a reader familiar with DQN. The critic's concern about "how many target networks exist" is explicitly answered: K target networks (Q̄₀,...,Q̄_{K-1}) for K online networks (Q₁,...,Q_K). Removed as overblown.

- **"Reliance on a single theorem without connecting to the actual method — non-sequitur"** (Critic Point 4): The critic claims "the Q_k are not produced sequentially; they are trained simultaneously from the same data. The theorem therefore does not directly apply." However, Theorem 5.1 applies to *any* sequence (Q_k)_{k=0}^K — it does not require sequential production. The real issue (which is kept above in Major) is that the paper does not properly bridge the gap between what iDQN optimizes and the theorem's terms. The claim of non-sequitur is too strong; the gap is in the derivation, not in applicability. Merged into the major weakness about the oversold theory.

- **Missing figures/appendix content**: Critic claims about missing Figures 7b, 13, 14, 15, 16, 20, 22 making claims "unverifiable." These are parser artifacts; they exist in the original submission. Removed per hard rules.

- **"iDQN does not compare against Bootstrapped DQN, REM, or any ensemble method"**: The paper explicitly states that iDQN performs similarly to REM (Figure 20) and provides comparisons in Figure 22. The paper discusses Bootstrapped DQN (line 79). This criticism is factually incorrect. Removed.

- **"No evidence that hyperparameters are well-chosen across the whole benchmark"**: The paper provides ablations on 2–3 games and clear intuitive justification. This is standard practice for ablation studies. Weakened to a minor point above.

- **Strength Finder claim about "theoretical guarantee of improved error control"**: Overstated. The paper's theoretical analysis is a heuristic argument, not a guarantee. Removed from strengths.

- **Strength Finder claim about "thorough hyperparameter analysis"**: The analysis is on 2–3 games, which is reasonable but not "thorough." Removed.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is the connection between iDQN and the overfitting phenomenon in DQN training. The ablation in Figure 8 (right) reveals that DQN with more gradient steps per sample (G=1) overfits and performs worse, while iDQN, which also takes more gradient steps per sample but distributes them across different Bellman iterations, avoids this overfitting. This suggests that the paper's architecture implicitly acts as a regularizer by forcing different heads to target different Bellman iterations rather than chasing the same target. This insight — that chaining value functions provides a form of implicit regularization — is not explicitly articulated in the paper but could be a fruitful direction for future work. It also connects to prior work on chaining value functions for policy evaluation (Schmitt et al., 2022), which the paper mentions in the conclusion.

## Suggestions

1. **Tone down the theoretical claims.** Replace "we theoretically prove" with "we provide theoretical motivation" or similar. The informal argument in Section 5 is useful intuition but is not a proof. Acknowledging this gap honestly would strengthen rather than weaken the paper.

2. **Expand the baseline comparisons in the main paper.** Move the REM/modern method comparisons (currently in Figures 20, 22) into the main results. This would directly address concerns about weak baselines and make the contribution clearer. Alternatively, add a tabular summary of per-game comparisons against a broader set of methods.

3. **Extend the iIQN experiments.** Showing iIQN results on the full 54-game benchmark, even with fewer seeds, would significantly strengthen the orthogonality claim.

4. **Provide a concise pseudocode in the main paper.** Algorithm 1 referenced but not in the main text — including a compact version would improve reproducibility without taking much space.

5. **Clarify the theoretical derivation.** If the authors wish to keep the theoretical section, they should explicitly show how γ||Q₁ − Q̄₁||²∞ bounds the second approximation error ||Γ*Q₁ − Q₂||², and formally define λ and its relationship to target update frequency and learning rate.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>