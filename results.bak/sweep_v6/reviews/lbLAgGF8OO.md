Now I have sufficient context. Let me produce the final consolidated review.

## Summary

This paper introduces Dig-DEC (dual information-gain decision-estimation coefficient), a model-free complexity measure that replaces the optimism principle used in prior work [FGQ+23] with pure information-gain terms (KL divergence + a divergence $\overline{D}$). The authors couple this with improved online estimation procedures (unbiased estimator for average error, refined two-timescale procedure for squared error) to obtain regret bounds for stochastic and hybrid MDPs. The contributions include: (1) a general DEC framework that removes optimism and handles adversarial rewards without explicit reward estimators, (2) the first model-free regret bounds for hybrid MDPs with bandit feedback under linear reward, (3) improved estimation procedures that sharpen previous rates, and (4) a proof that Dig-DEC ≤ optimistic DEC + η with strict improvements possible.

## Strengths

- **Novel conceptual contribution: removal of optimism from the DEC framework.** The Dig-DEC definition (Eq. 8) replaces the optimistic term $V_\phi(\pi_\phi)$ used in prior work with a pure information-gain formulation (KL + $\overline{D}$), enabling principled handling of adversarial rewards without explicit reward estimators. This is a genuine conceptual advance over the optimistic DEC of [FGQ+23].

- **Clean analytical framework via Bregman divergences.** The paper's analysis (Eq. 5–6, Theorem 6) uses Bregman divergences to handle general divergence measures $D$, which is more flexible than the restrictive constructive minimax theorem of [XZ23]. This allows the framework to recover prior results (Appendix C) and enables posterior update rules beyond simple Bayesian posteriors.

- **Improved estimation procedures of independent interest.** The unbiased estimator for average estimation error (Section 4.2.1, Theorem 7) and the refined two-timescale procedure for squared error (Section 4.2.2, Theorem 11) are technically sound and could be applied beyond this specific framework. The squared-error case achieves Est $O(\log^2|\Phi|)$ (constant), which is a genuine improvement over prior $T^{1/2}$ Est bounds.

- **First model-free bounds for hybrid MDPs with bandit feedback.** The paper provides the first regret bounds for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs with bandit feedback under linear reward (Table 2, Section 5.2), addressing the open problem left by [LWZ25].

- **Dig-DEC ≤ o-dec + η with strict improvement in some cases.** Theorem 13 and the 3-armed bandit example (Theorem 14) provide formal evidence that Dig-DEC can be substantially smaller than optimistic DEC.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent and self-contradictory exponent claims.** The paper's central quantitative claims — the regret exponents — are presented differently in three places and cannot be reconciled:
  - **Abstract**: claims $T^{3/4}\to T^{3/5}$ (on-policy) and $T^{5/6}\to T^{7/8}$ (off-policy) for average error, and $T^{5/6}\to\sqrt{T}$ for squared error.
  - **Introduction** (line 39): claims $T^{3/2}/T^{5/8}\to T^{3/2}/T^{5/6}$ for the former case, and $T^{3/2}\to\sqrt{T}$ for the latter.
  - **Table 1** (stochastic): shows $T^{2/3}$ for both on-policy and off-policy without completeness, and $\sqrt{T}$ for some completeness cases.
  
  None of these three sets of numbers match each other. The abstract's $T^{3/5}\approx T^{0.6}$ and $T^{7/8}\approx T^{0.875}$ do not match Table 1's $T^{2/3}\approx T^{0.667}$. The introduction's $T^{3/2}$ (superlinear) is entirely different from the abstract's $T^{3/4}$. The introduction claims $T^{5/8}\to T^{5/6}$ as an improvement, but $T^{5/6}>T^{5/8}$, making this *worse*. A reader cannot determine which exponents the paper actually claims. This is not a cosmetic issue — the core contribution of the paper is improved regret rates, and those rates are not stated consistently.

- **"Sublinear regret" claim is contradicted by Table 2.** The introduction (line 38) claims "the first sublinear regret for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs." However, Table 2 shows $\mathbb{E}[\text{Reg}]\propto T^{3/2}$ for hybrid bilinear on-policy (both with and without completeness) and for coverable MDPs, and $T^{13/8}$ for hybrid bilinear off-policy. These exponents exceed 1, meaning the regret grows *superlinearly* in $T$. Only the off-policy completeness case ($T^{1/2}$) is genuinely sublinear. This contradiction undermines a central advertised claim.

- **Vacuous claim about Est improvement (Section 4.2.1, line 219).** The paper states "our construction of the estimator improves their rate of Est from $\sqrt{T}$ to $T^{\frac{1}{2}}$" — these are the same quantity. Combined with line 249's claim of improving "over [FGQ+23]'s $T^{1/2}$ bound" to constant, there is confusion about what is actually being improved and by how much.

- **Explicit regret expressions not derived from bounds.** The final regret rates in the tables are presented without showing the optimization over $\eta$. The paper states "with the optimal $\eta$" (line 264) but does not derive the closed-form expressions. Given the exponent inconsistencies elsewhere, the omitted derivation is a significant gap — the reader cannot verify that the claimed rates follow from the stated dig-dec and Est bounds.

### Minor

- **Computational intractability of Algorithm 1.** Algorithm 1 requires solving a minimax problem over $\Delta(\Pi)\times\Delta(\Psi)$ at each round, which is a general-sum game with potentially enormous state/action spaces. The paper does not discuss this, nor does it show that the minimax problem has a closed-form solution in the instantiations considered. While DEC theory papers often focus on information-theoretic bounds, the framing as a "general algorithm" with no discussion of tractability is misleading.

- **Unclear motivation for Assumption 5 (second part).** The assumption that $\mathbb{E}^{\pi,M_t}[\ell_h(\phi;o_h)]$ is equal for all $t$ effectively removes adversarial variation in quantities that affect estimation error. The paper says this "is automatically satisfied in many cases" but does not verify this for the hybrid setting where rewards are adversarial.

- **The "on-policy"/"off-policy" terminology is non-standard.** The paper acknowledges this (line 261) but the terms are still confusing for readers expecting standard RL usage.

### Trivial
- Heavy reliance on appendices for key derivations; the main text is not self-contained.
- Dense notation that requires continuous reference to prior work [FKQR21, FGH23, XZ23, LWZ25].

## Nice-to-Haves

- A small-scale numerical illustration of the 3-armed bandit example (Theorem 14) showing constant regret empirically would build confidence in the result.
- High-probability bounds (the paper notes these are possible with a variant of $D$ but does not provide them).
- Discussion of how the minimax optimization in Algorithm 1 can be solved or approximated in the specific instantiations.

## Removed Points

- *Criticism about missing experiments*: Not applicable for a pure theory paper; removed per scope rule.
- *Formatting/style nitpicks about dense notation*: A presentation concern but not weight-bearing; removed.
- *Missing related works*: Not verifiable without external sources; removed per hard rule.
- *Strength Finder's generic strengths* (e.g., "the problem is important"): Removed as superficial. Kept only concrete, evidence-grounded strengths.
- *Criticism about Assumption 3 not capturing all learnable cases*: The paper explicitly acknowledges this limitation; moved from weakness to minor as it's already addressed.

## Novel Insights

The harsh critic's observation that the exponent inconsistencies span three different locations (abstract, introduction, tables) with each giving different numbers is insightful and goes beyond what any individual reviewer noted — it reveals a structural presentation failure that prevents the paper from communicating its main quantitative contributions. The critic's further observation that some "improvements" (e.g., $T^{5/8}\to T^{5/6}$ in the introduction) are actually *worse* bounds is particularly sharp and suggests that either the exponents contain errors, or the paper is comparing different settings without making this clear. The tension between the "sublinear" claim and the superlinear entries in Table 2 is an even deeper issue that, if unresolved, undermines the core advertised contribution.

## Suggestions

1. **Rewrite all exponent claims consistently.** Decide on the correct set of regret rates (presumably those in the tables) and ensure the abstract, introduction, and tables all state the same numbers. Derive the closed-form regret expressions explicitly in the main text by showing the optimization over $\eta$.

2. **Reconcile the "sublinear" claim with Table 2.** If $T^{3/2}$ is correct, remove the "sublinear" claim or qualify it carefully. If $T^{3/2}$ is a typo and the correct exponents are sublinear, correct the table.

3. **Fix the vacuous "$\sqrt{T}$ to $T^{1/2}$" statement** (line 219) and clearly state the actual Est improvement over [FGQ+23].

4. **Add a paragraph discussing computational aspects** of Algorithm 1 — even if the focus is information-theoretic, the reader deserves to know whether the minimax problem simplifies in the considered instantiations.

5. **Provide a short derivation of at least one regret rate** in the main text to demonstrate how the dig-dec and Est bounds combine to yield the claimed $T$-exponent.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| Horizon-free RL in Adversarial Linear Mixture MDPs | aPNwsJgnZJ | 6.00 | Cleaner, internally consistent theory paper accepted at 6.0; current paper has more significant presentation issues |
| Value-Biased MLE for Model-based RL | 2h3m61LFWL | 4.25 | Both have presentation problems, but current paper's novelty is stronger; comparable quality |
| Safe Online Bid Optimization | WtNgFrPn8y | 4.25 | Comparable quality — both have real contributions undermined by presentation issues |
| Learning with Real-time Improving Predictions | 6HfNB34x9I | 5.25 | Cleaner presentation but less substantial contributions; current paper's novelty is higher |
| RL for Control with Stability Guarantee | vBNTeQ7dPP | 2.50 | Current paper is substantially stronger — more rigorous theory and clearer contributions |
| KL Divergence Optimization for GFlowNets | Uj0h13lVrR | 1.00 | Current paper is in a completely different league — rigorous vs. incomprehensible |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>