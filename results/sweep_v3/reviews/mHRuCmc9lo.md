Now I have all the information I need. Let me produce the consolidated review.

## Summary
This paper develops a framework for robust decision-making from forecasts that satisfy only *partial* (ℋ-) calibration guarantees. The authors characterize the minimax-optimal decision rule via a duality argument (Theorem 3.1) and show a sharp transition: once ℋ contains the decision-calibration indicators (one per action), the optimal robust policy collapses to the simple plug-in best response (Theorems 4.1–4.2). This recovers the decision-theoretic optimality of full calibration under a substantially weaker and more tractable condition. The paper also gives concrete robust policies for two practical scenarios — squared-loss-trained models (self-orthogonality) and binned calibration — and validates the framework on two regression datasets.

## Strengths
1. **Sharp transition result (Theorems 4.1 and 4.2) is the paper's standout contribution.** The finding that a finite set of |𝒜| decision-calibration indicators (rather than the intractable set of all functions) recovers plug-in best-response optimality in the minimax sense is genuinely surprising and cleanly stated. The paper explicitly distinguishes this from prior swap-regret guarantees (Section 1.2), which only rule out improvements via action-remapping policies, not arbitrary forecast-to-action maps. The invariance argument (lines 195–199) provides crisp intuition.

2. **Theorem 3.1 provides an explicit, computable characterization.** For any finite-dimensional ℋ, the optimal robust policy reduces to computing dual multipliers (via a finite-dimensional concave maximization) and then solving a pointwise convex minimization over \(p\in[0,1]^d\). This goes beyond prior work that assumed full calibration or gave only qualitative guarantees. The two-step procedure (worst-case belief \(q^*\) then best-response to \(q^*\)) is algorithmically concrete.

3. **Propositions 4.4 and 4.5 give usable, practically motivated recipes.** Proposition 4.4 shows that any model with a linear final layer trained to stationarity under squared loss automatically satisfies ℋ-calibration for ℋ = {\(h_j(v)=e_j^\top v\)}, making the robust framework applicable without any post-hoc calibration. Proposition 4.5 yields an optimization-free piecewise-constant robust rule under bin-wise calibration. These bridge theory and practice.

4. **Corollary 4.3 (simultaneous plug-in optimality) is a practically valuable upshot.** A single decision-calibrated forecaster can serve multiple downstream decision problems simultaneously with plug-in optimality, without task-specific robust rules.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evaluation lacks critical details and statistical rigor.** The paper reports only point estimates from a single train/calibration/test split (Table 1) with no variance, confidence intervals, or multiple trials. More importantly, the construction of the adversarial distributions is not described: the paper says "a worst case tailored to the plug-in policy" and "a worst case induced by the robust dual" (lines 275–276), but never explains whether these are computed analytically from the dual variables or sampled, how the dual variables are fitted (on which data split), or how the adversarial test outcomes are generated while respecting the ℋ-calibration constraints. This makes the experimental results impossible to reproduce or evaluate for significance. Since the paper's primary contribution is theoretical this is not fatal, but as written the experiments do not convincingly support the claimed patterns.

2. **Theorem 3.1 does not state the regularity conditions needed for the duality argument.** The theorem claims a saddle point and a closed-form expression for \(q^*(v)\) in terms of dual variables. Strong duality for the infinite-dimensional max-min problem in Equation 5 is nontrivial, even when ℋ is finite-dimensional — one needs compactness, convexity, or constraint qualification conditions (e.g., Slater-type) that the paper does not mention. The text refers to "the proof of Theorem 3.1" (line 147) which is in the appendix, but the main text should at least sketch the assumptions that justify the dual representation. As it stands, a reader cannot fully assess the rigor of the central theoretical result.

### Minor

3. **The self-orthogonality approximation gap is not quantified.** Proposition 4.4 assumes a first-order stationary point of the *population* expected squared loss. In practice, the forecaster is trained on finite data, so the condition holds only approximately. The paper does not measure how large the calibration violation is (e.g., \(\|\hat{\mathbb{E}}[f(X)\cdot(Y-f(X))]\|\) on the calibration set) or discuss how the robust policy's minimax guarantee degrades under approximate calibration. The reference to Appendix B (line 91) is noted, but a brief quantification in the main text would strengthen the empirical section.

### Trivial
None.

## Nice-to-Haves
- A concrete formula for the optimal \(q^*(v)\) in the self-orthogonality case (ℋ = {\(v \mapsto v\)}) for the specific linear utility used in the experiments would make Section 5 more self-contained.
- A brief note on computational complexity of the pointwise minimization for general ℋ (how it scales with \(|\mathcal{A}|\) and \(d\)).
- Discussion of how to handle overlapping ℋ constraints when a forecaster satisfies multiple calibration properties simultaneously.

## Removed Points
- **Criticism about proof being omitted from main text (Harsh Critic point 2, first part):** Removed per meta-reviewer rules — the parser strips appendices from all papers; proof details exist in the original submission.
- **Criticism that the paper lacks error bars and multiple runs (part of Harsh Critic point 1):** Kept as part of Major weakness 1 above (the more specific reproducible-concern framing replaces the generic "no error bars" complaint). The deeper issue is the underspecified adversarial construction, not just the absence of error bars.
- **"The paper does not discuss computational complexity for general ℋ":** This is a nice-to-have for a theory paper; moved to Nice-to-Haves.
- **Strength Finder's claim about Proposition 4.4 being a "Supporting strength":** Kept but subsumed into the broader Strengths section (point 3). The strength itself is genuine.
- **"Sharp transition not experimentally tested" (from Harsh Critic's Missing Parts):** This is a request for additional experiments beyond the paper's stated scope. Moved to Nice-to-Haves.
- **Speculative comments about what "could be" wrong with the dual representation:** Removed because they depend on assuming technical conditions that may be stated in the appendix. The concrete concern about regularity conditions not being stated in the main text is retained.
- **"No guidance on how to combine multiple ℋ constraints":** Scope creep beyond the paper's contribution.

## Novel Insights
The reviews do not surface insight that goes substantially beyond the paper's own contributions. The one cross-cutting observation that emerges is that the paper's core theoretical contribution (the sharp transition) is strong enough to stand largely on its own; the experimental weaknesses are real but secondary, and the missing duality conditions are a presentation gap rather than a likely flaw in the result. The paper would benefit from a more rigorous experimental section and a clearer statement of assumptions in Theorem 3.1, but the conceptual advance is clear and significant.

## Suggestions
1. **Specify the adversarial evaluation methodology in full.** Clarify whether the "worst-case" distributions are computed analytically from the dual variables or via sampling, how the dual variable \(\lambda\) is fitted (on which data split), and how the expected utilities under the adversary are computed.
2. **Add statistical reproducibility.** Report means and standard deviations over multiple train/calibration/test splits (e.g., 5 random seeds) or provide bootstrapped confidence intervals.
3. **State regularity conditions for Theorem 3.1.** Add a brief note in Section 3 specifying the conditions (e.g., compactness of \([0,1]^d\), convexity of the feasible set, applicability of minimax duality) under which the saddle-point characterization holds.
4. **Quantify the calibration approximation error.** Report \(\|\hat{\mathbb{E}}[f(X)\cdot(Y-f(X))]\|\) on the calibration set to show that the self-orthogonality condition is approximately satisfied.
5. **Include the structure of the worst-case q* for the self-orthogonality case** to make the experimental section more self-contained.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| TId1SHe8JG — "Provable Uncertainty Decomposition via Higher-Order Calibration" | 7.50 | Also a theory-heavy calibration paper. The current paper has cleaner/ more striking results (sharp transition) but weaker experiments. Slightly below this anchor. |
| uuPkll6i7m — "Towards Certification of Uncertainty Calibration under Adversarial Attacks" | 6.75 | Both papers study calibration with a worst-case lens. The current paper's theory is deeper; this anchor has stronger experiments. Comparable overall quality. |
| g6fYDGKeyB — "Addressing Misspecification in SBI through Data-driven Calibration" | 6.00 | Interesting approach but had soundness concerns. Current paper is cleaner and has fewer foundational issues. Stronger than this anchor. |
| X0epAjg0hd — "Reassessing How to Compare and Improve the Calibration of ML Models" | 5.67 | Accepted paper with very thin experiments (1 dataset). Current paper has stronger theory and a more novel contribution. |
| XM7INBbvwT — "Does Calibration Affect Human Actions?" | 4.67 | Different type of work (HCI). Not directly comparable. |
| WoJzHQIIUk — "MinMax Bayesian Neural Networks and Uncorrelated Representation" | 1.50 | Incoherent paper with severe presentation issues. Current paper is vastly superior on every dimension. |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>