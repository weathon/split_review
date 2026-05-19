- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper studies the sparse linear contextual bandit problem and makes two contributions. First, it identifies the **compatibility condition on the optimal arm** (Assumption 3) as a sufficient condition for achieving $O(\text{poly}\log d + \text{sublinear-in-}T)$ regret under the margin condition, without requiring the additional diversity assumptions (anti-concentration, relaxed symmetry, balanced covariance) that prior Lasso bandit analyses depend on. Second, it proposes **FS-WLasso**, a forced-sampling-then-greedy algorithm with a weighted Lasso estimator, and proves regret bounds via a novel induction argument that handles the cyclic dependency between optimal-arm selection and estimation accuracy. Experiments on synthetic data show FS-WLasso outperforms existing methods, including in a setting where context distributions violate earlier assumptions.

## Strengths

1. **Weaker and cleaner sufficient condition for polylog regret.** The paper demonstrates that the compatibility condition on the optimal arm alone (Assumption 3, plus the margin condition) suffices for regret bounds matching prior work, whereas all prior single-parameter Lasso bandit algorithms additionally require anti-concentration, relaxed symmetry, or balanced covariance. Table 1 and the discussion in §1–§2 make this comparison explicit, and the paper argues (with proofs in the appendix) that the existing conditions imply the proposed condition, establishing that the latter is strictly weaker (§2, lines 245–248; Figure 1).

2. **Novel induction-based regret analysis.** The paper introduces a mathematical induction argument (Section 3.3) that breaks the cyclic dependency between optimal-arm selections and estimation error — a phenomenon existing analyses "fail to capture" (line 424). This technique avoids the need for automatic exploration via diversity conditions and is presented as being of independent interest for future bandit analyses.

3. **Improved regret constants for $\alpha > 1$.** The paper sharpens a term proportional to $s_0^2/(\Delta_* \phi_*^4)$ in Li et al. (2021) to $s_0^{1+1/\alpha}/(\Delta_* \phi_*^{2+2/\alpha})$, and notes that its bound is at most $O(K^2)$ versus $O(K^4)$ in Chakraborty et al. (2023) (lines 412–416).

4. **Algorithmic advantage over ESTC.** As noted in Remark (lines 285–290), FS-WLasso continues updating its estimator during the greedy stage, unlike ESTC (Hao et al. 2020) which discards post-exploration data. The experiments (Figure 2) confirm FS-WLasso outperforms ESTC in both correlated-Gaussian and adversarially-structured settings.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Imprecise phrasing of "poly-logarithmic in $dT$" in the abstract.**  
   The abstract (line 10) and introduction (line 63) claim $\mathcal{O}(\text{poly}\log dT)$ regret, but Theorem 1 shows that for $\alpha \in (0,1)$ the bound is $T^{(1-\alpha)/2} \cdot \text{polylog}(d,T)$ — a sublinear rate, not polylogarithmic in $T$. The subsequent discussion (line 349) correctly presents the piecewise rates, so this is solely a framing imprecision. The authors should qualify the abstract to reflect that the polylog-in-$T$ guarantee holds for $\alpha \ge 1$, while for $\alpha < 1$ the rate is sublinear with polylog factors.

2. **The forced-sampling length $M_0$ depends on theoretically convenient but practically unknown constants ($\rho$, $\phi_*$, $\sigma$).**  
   The authors acknowledge (lines 363–368) that $M_0$ is a tunable hyper-parameter and that the theory only guarantees the bound when it is set according to problem parameters the agent does not know. Theorem 2 partially addresses this by showing $M_0=0$ works under additional diversity assumptions, but the practical gap between the theory-driven expression for $M_0$ and its empirical tuning is a limitation common to many theoretical bandit papers. The paper would benefit from a sensitivity analysis over $M_0$ in the experiments.

3. **No discussion of per-round computational complexity.**  
   The Lasso estimation at each round during the greedy stage can be expensive when $d$ is large, but the paper does not comment on the computational cost. A brief note on how the per-round complexity compares to baselines would improve clarity.

4. **The constant $\phi_G$ in Theorem 2 is stated without elaboration.**  
   Theorem 2 (line 381) introduces $\phi_{\text{G}}$ as "an appropriate constant that is determined by the employed assumptions," but does not clarify which specific assumptions (anti-concentration vs. relaxed symmetry & balanced covariance) produce which value. A brief clarification would improve precision.

### Trivial
None.

## Nice-to-Haves

- **Ablation study for $M_0$:** Showing that FS-WLasso's performance is reasonably insensitive to the choice of $M_0$ over a plausible range would lower the practical barrier.
- **Discussion of how $K$ (number of arms) enters the constants:** The regret bounds implicitly depend on $K$ through $\rho$ and the forced-sampling cost; a brief comment would be helpful.
- **Self-contained proof sketch of the implication chain:** The paper already gives a high-level argument (lines 246–248) that existing diversity conditions imply compatibility on the optimal arm because the optimal arm is a special case of a greedy policy. Expanding this into a short standalone lemma in the main text would make the paper's central comparative claim more self-contained.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Reliance on deferred appendix proofs for the implication chain (Harsh Critic Point 2).**  
  *Reason:* The instructions explicitly state to remove weaknesses about missing appendix content, which is stripped by the PDF parser. The paper provides a high-level argument in the main text (lines 246–248) and states that full proofs are in the appendix (line 225). This is standard practice for theory papers.

- **Claim that the counter-example does not fully demonstrate the implication direction.**  
  *Reason:* The counter-example (fixed suboptimal arms) is used to show the *converse* (that $\Sigma^*$ compatibility does **not** imply anti-concentration), not the forward direction. The forward direction (existing conditions $\Rightarrow$ $\Sigma^*$ compatibility) is argued in the main text and proven in the appendix. The criticism misunderstands which direction the counter-example serves.

- **Figure not visible in the extracted PDF.**  
  *Reason:* This is a PDF parser artifact; the figure exists in the original submission.

- **Request for a table summarizing implications from each prior condition.**  
  *Reason:* This is essentially asking the appendix content to be expanded; the paper already states the implications and provides proofs.

- **Criticism that the paper does not directly compare "bounded sparse eigenvalue of $\Sigma^*_\Gamma$" with "compatibility on $\Sigma^*$."**  
  *Reason:* The paper's comparison is via the implication chain (Figure 1) which is a well-defined relationship. The comparison is legitimate given the stated framework.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions and do not surface unexpected connections or interpretations that the paper itself does not already articulate.

## Suggestions

1. **Fix the abstract's "poly-log" phrasing.** Replace "$\mathcal{O}(\text{poly}\log dT)$" with a qualified statement along the lines of "regret that scales polylogarithmically in $d$ and, depending on the margin exponent, either polylogarithmically or at a slower sublinear rate in $T$."
2. **Add a brief computational complexity note.** One sentence on the per-round cost of solving the Lasso (e.g., "solving (1) costs $O(d^3)$ in the worst case; practical solvers scale favorably under sparsity") would suffice.
3. **Clarify $\phi_G$ in Theorem 2.** Provide a short remark on how $\phi_G$ is determined under each diversity assumption (anti-concentration vs. relaxed symmetry & balanced covariance).
4. **Include an experiment varying $M_0$.** A simple sensitivity plot over a range of $M_0$ values would strengthen the practical message.

---
