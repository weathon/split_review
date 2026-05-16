Now I have all the information needed. Let me synthesize the final consolidated review.

---

## Summary

This paper studies the sparse linear contextual bandit problem and introduces a new sufficient condition — the compatibility condition only on the optimal arm — for achieving poly-logarithmic regret under the margin condition. The authors propose an algorithm (FS-WLasso) using forced sampling followed by greedy selection with a weighted Lasso estimator, prove regret bounds via a novel induction-based analysis technique, and demonstrate that their assumption is strictly weaker than existing alternatives (eliminating additional diversity assumptions like anti-concentration, relaxed symmetry, etc.). Experiments on synthetic data validate the approach, particularly in settings where existing diversity assumptions fail.

## Strengths

- **Weaker sufficient condition with clear theoretical justification**: The paper shows that compatibility on the optimal arm (Assumption 3) alone is sufficient for poly-logarithmic regret under the margin condition, and rigorously demonstrates (via Table 1 and Figure 1) that this condition is strictly weaker than the combination of assumptions used in prior single-parameter Lasso bandit work (Oh et al., Li et al., Ariu et al., Chakraborty et al.). The fixed suboptimal-arm counterexample concretely illustrates the strictness.

- **Novel induction-based analysis technique**: The proof introduces a mathematical induction argument (Section 3.2) that handles the cyclic dependency between optimal-arm selection and estimation error — a non-trivial technical challenge that prior analyses could not resolve without additional diversity conditions. This technique may be of independent interest beyond sparse linear bandits.

- **Improved regret bounds under weaker assumptions**: Theorem 1 provides explicit regret bounds across all margin parameter regimes (α>0). For α>1 the bound is O(polylog d), for α=1 it is Õ(s₀² log T), and for α<1 it is sublinear O(T^{(1-α)/2} polylog). The comparison with Li et al. (2021) and Chakraborty et al. (2023) shows improvements in the dependence on s₀ and the compatibility constant φ_* (e.g., from s₀²/(Δ_* φ_*⁴) to s₀^{1+1/α}/(Δ_* φ_*^{2+2/α}) for α>1). Theorem 2 further shows that when diversity assumptions are available, the forced-sampling stage can be eliminated entirely.

- **Empirical validation under challenging settings**: Experiment 2 (fixed suboptimal-arm features) directly targets the regime where prior diversity assumptions fail, and the proposed algorithm outperforms baselines — confirming that the weaker assumption translates to practical advantage. The experiments compare against a comprehensive set of baselines (DR Lasso Bandit, SA Lasso Bandit, TH Lasso Bandit, L1-CB-Lasso, ESTC) over 100 runs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Inaccurate T-dependence in abstract and discussion of Theorem 1**: The abstract claims the algorithm achieves "O(poly log dT) regret under the margin condition." Theorem 1 shows this is accurate only for α ≥ 1. For α ∈ (0,1), the bound is O(T^{(1-α)/2} · polylog(d,log T)), which is sublinear in T but *not* polylogarithmic in T. The paper compounds this error in line 349 by describing the α∈(0,1) bound as scaling "poly-logarithmically on d and T" while simultaneously giving a T^{(1-α)/2} term. This is a clear inaccuracy that must be corrected — the abstract and discussion should either restrict the polylog claim to α≥1 or explicitly state that for α<1 the bound is sublinear. The core contribution (weaker assumptions) is unaffected, but the framing misleads readers.

2. **Oracle-dependent theoretical hyperparameters**: The theoretical specification of the weight parameter w = √(τ/M₀) depends on τ, which is defined as a constant that depends on unknown problem parameters (xₘₐₓ, s₀, φ_*, σ, α, Δ_*). While the paper notes that M₀ can be tuned as a whole in practice (lines 363-366), the weight w is not addressed. This is standard in theoretical bandit papers (many have oracle-dependent parameters in the analysis), but a brief remark on how w can be set in practice (e.g., w=1 with a sufficiently long exploration stage) would strengthen the paper.

3. **Limited experimental details**: The experiments (Section 4) do not specify how hyperparameters (M₀, λ_t, w) were chosen for the proposed algorithm or the baselines. The paper notes M₀ is tuned "as a whole" but provides no grid or selection procedure. For a theory paper this is not fatal, but the large performance gap would be more convincing with explicit hyperparameter choices stated.

### Trivial
- "with probability at least 1-δ" appears twice consecutively in the statement of Theorem 2 (line 382).
- The "Discussion of assumptions" section has a dangling fragment at line 249 ("for optimal arm}") suggesting a formatting issue.

## Nice-to-Haves
- A brief limitations paragraph (e.g., noting the margin condition is a strong distributional assumption; the analysis assumes a single-parameter setting; theoretical hyperparameters depend on unknown constants) would improve completeness.
- A discussion of whether the observed experimental differences are statistically significant would strengthen the empirical evidence, though the standard deviation plots already convey variability.
- Releasing code would aid reproducibility, but is not expected for a primarily theoretical paper.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The analysis does not extend to the multi-parameter setting"** — Removed as scope creep. The paper explicitly scopes itself to the single-parameter setting (lines 47-52, 56) and explains why direct comparison with multi-parameter works is not possible.
- **"No error bars in experiments"** — Removed as factually incorrect. The paper states "We plot the mean and standard deviation of cumulative regret across 100 runs" (line 472).
- **"The strictness proof is only sketched"** — Removed as the paper provides the fixed suboptimal-arm counterexample (Figure 1 caption, Experiment 2) and references the appendix for full proofs, which is standard.
- **"Missing related works"** — Removed per instructions (no external sources to confirm).

## Novel Insights

The reviewers' inputs converge on a key point that goes beyond the paper's own claims: the induction-based analysis technique (Section 3.2) is arguably the most interesting methodological contribution. While the paper presents it as a tool for handling dependent selection sequences, the induction-over-good-events approach may be broadly applicable to other sequential decision-making problems where policy quality and estimation quality co-evolve — essentially providing a template for breaking circular dependencies in bandit analysis. The paper's clean Figure 1 mapping assumption relationships is another understated contribution that could serve as a useful reference for future work comparing context-distribution assumptions.

## Suggestions

1. **Revise the abstract and the Discussion of Theorem 1** to accurately reflect the T-dependence: for α∈(0,1) the regret is O(T^{(1-α)/2} polylog(d,log T)) rather than O(poly log dT). A phrasing like "achieves O(poly log dT) regret when α≥1, and sublinear regret O(T^{(1-α)/2} polylog(d,log T)) when α∈(0,1)" would be precise without diminishing the contribution.
2. **Add a remark about the practical choice of w** along the same lines as the remark about M₀ (lines 363-366), noting that w can be set to a constant (e.g., w=1) in practice since the exploration stage ensures sufficient coverage.
3. **Provide the hyperparameter settings** used in the experiments (even briefly in a footnote or appendix) to improve reproducibility.
4. **Fix the dangling formatting artifact** at line 249 and the duplicate phrase in line 382.

## Score and Decision

The paper makes a solid theoretical contribution: it genuinely weakens the assumptions needed for polylog regret in sparse linear bandits, provides a novel analysis technique, and validates the approach experimentally. The main flaw is the overclaimed T-dependence in the abstract, which is a correctable presentation issue rather than a structural problem. The theoretical contributions are sound and the experimental evidence supports the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>