## Summary

This paper proves that the latent dimension $L$ in DeepSets architectures can be polynomial in the set size $N$ and feature dimension $D$ for high-dimensional features ($D>1$), answering an open question from Zweig & Bruna. The authors construct two explicit embedding architectures—linear+power (LP) and linear+exponential (LE)—yielding upper bounds of $L \le N^5 D^2$ and $L \le N^4 D^2$ respectively, with lower bounds of $L \ge N(D+1)$ (LP) and $L \ge ND$ (LE). The proof uses a novel "anchor-and-coupling" technique. Results extend to permutation-equivariant functions and the complex domain.

## Strengths

- **First polynomial upper bound for $D>1$ without complex analytic restrictions.** Theorem 1 provides explicit bounds $L \le N^5 D^2$ (LP) and $L \le N^4 D^2$ (LE), directly addressing the open question from Zweig & Bruna (2022). Table 1 contrasts these with prior exponential/combinatorial bounds.
- **Exact representation, not just approximation.** Theorem 1 constructs $\phi$ and $\rho$ such that any continuous set function is represented exactly, matching the strong form Zaheer et al. established for $D=1$. This contrasts with Segol et al. and Zweig & Bruna, which provide only approximating representations.
- **Non-trivial lower bound for LP architecture.** Theorem 4 proves $K \le D$ (i.e., $L \le ND$) provably fails injectivity, establishing $L \ge N(D+1)$. This shows the naive degree-of-freedom count ($ND$) is insufficient, correcting a potential misconception from prior work.
- **Constructive proof with explicit weight specification.** The paper provides concrete formulas for all linear weights (canonical basis vectors, anchor weights $\boldsymbol{\alpha}_j$, coupling weights $\mathbf{\Gamma}_{i,j,k}$) rather than a non-constructive existence argument.
- **Novel anchor-and-coupling proof technique.** The anchor concept (Definition 3) and union alignment lemma (Lemma 3) provide a genuinely new technical device for handling the cross-channel alignment problem that had stymied prior approaches for $D>1$.
- **Extension to equivariance and complex domain.** Theorem 5 extends the bounds to permutation-equivariant functions with the same polynomial guarantees, and the technique handles complex-valued features.

## Weaknesses

### Fatal
None.

### Major
- **Inadequate comparison with Dym & Amir (2024) / Amir et al. (2024).** The paper acknowledges (line 210) that these works achieve $L$ as small as $2ND+1$ — an $O(ND)$ bound far tighter than the paper's $N^5 D^2$ — but dismisses this in a single sentence: "However, the continuity of decoder $\rho$ is not guaranteed when the domain of $f$ is an open set." This is insufficient to establish the paper's contribution relative to these closely related works. The paper's domain is $\mathbb{R}^{N \times D}$, which is open and non-compact; if Dym & Amir only guarantee continuity on compact subsets, this is a genuine technical distinction that needs proper explanation, not a one-sentence caveat. Without a clear technical comparison, a reader cannot assess whether the paper's much looser bound ($N^5 D^2$ vs $2ND+1$) is compensated by a qualitatively stronger guarantee. This is the most significant issue for calibrating the paper's novelty and importance.

### Minor
- **Bounds are very loose with a large gap between upper and lower bounds.** The LP upper bound is $N^5 D^2$ and the lower bound is $N(D+1)$ — a gap spanning polynomial exponents 1 through 5. The LE lower bound ($L \ge ND$) is the trivial degree-of-freedom count. For moderate values like $N=10$, $D=10$, the LP bound ($10^7$) exceeds Segol & Globerson's combinatorial bound ($\binom{20}{10}-1 \approx 1.85\times10^5$) by a factor of ~54. While the polynomial-vs-exponential distinction is theoretically meaningful, the looseness limits practical relevance. The paper acknowledges tightness is unexamined (line 380) but does not discuss whether tighter bounds are an open problem.
- **Misleading "tightest bound" claim in Table 1.** The caption reads "Our results achieve the tightest bound on $L$" but the table omits Dym & Amir's $2ND+1$ bound, which the paper's own text acknowledges is far tighter. The claim is inaccurate as stated.
- **"Empirical Validation" is misleadingly labeled.** The paragraph (lines 194-196) is a single sentence referencing a figure without any description of an experiment, dataset, metric, or result. This heading implies an empirical study that the paper does not provide.

### Trivial
- Table 1 omits Dym & Amir despite the text acknowledging their tighter bound.

## Nice-to-Haves

- Expand the Dym & Amir comparison into a dedicated paragraph or subsection clarifying the precise continuity assumptions (compact vs. open domain) and what the paper's construction adds.
- A small-scale empirical demonstration (e.g., $N=3, D=2$) showing the constructed weights achieve injectivity on synthetic data would strengthen the paper.
- Discussion of whether tighter bounds (e.g., $N^3 D^2$ or $N^2 D$) are achievable with refinements of the anchor-and-coupling technique.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Continuity proof deferred to appendix:** The critic raised that the most technically delicate part (condition (c) of Lemma 4.1) is deferred to the appendix. **Removed:** per hard rules, the parser strips appendix sections from all papers; they exist in the original submission.
- **Critic's erroneous Zweig & Bruna numerical example:** The critic claimed "exp(10) ≈ 22,026" for the Zweig & Bruna bound at $N=10, D=10$. The actual bound uses $\min\{\sqrt{N}, D\} = \sqrt{10} \approx 3.16$, not $10$. This numerical error is removed from the weaknesses above. (The broader point about the bounds being loose, verified via comparison with Segol's bound, is retained.)
- **Lower bounds are "trivial and unconstraining":** The critic's claim that the lower bounds are "essentially trivial" is overstated. The LP lower bound ($L \ge N(D+1)$) is non-trivial — it proves the naive $ND$ dimension is insufficient, which the paper correctly highlights. The LE lower bound is acknowledged by the paper itself as trivial. The large gap is already captured as a minor looseness weakness above.

## Novel Insights

The most interesting unresolved tension is the relationship between the paper's bound ($N^5 D^2$) and the existing $2ND+1$ bound from Dym & Amir. The paper's one-sentence caveat about continuity on open sets could, if properly explained, reveal a genuine trade-off: the paper's construction may guarantee continuity of $\rho$ on the full open domain $\mathbb{R}^{N \times D}$, while prior constructions might only guarantee it on compact subsets. But the paper does not develop this comparison. If this trade-off is real, the paper offers a qualitatively different (and in some settings more desirable) guarantee despite the worse bound. Conversely, if Dym & Amir's construction already provides continuous $\rho$ on the full space, the paper's contribution is substantially diminished. A second observation: the anchor-and-coupling technique, while yielding very loose bounds, is conceptually clean and seems likely to admit tighter analysis — both the $N(N-1)(D-1)/2+1$ anchor construction and the $N(N-1)+1$ coupling scheme use pigeonhole-counting that appears suboptimal.

## Suggestions

1. **Expand the Dym & Amir comparison** into a full paragraph or subsection. State their precise assumptions (compact vs. open domain, continuity guarantees) and explain clearly what additional property the paper's construction provides.
2. **Remove or replace "Empirical Validation"** with a concrete small-scale experiment or remove the heading entirely.
3. **Correct the Table 1 caption** — either include Dym & Amir or qualify the "tightest bound" claim.
4. **Add a paragraph discussing the gap** between upper and lower bounds and whether tighter bounds are an open problem.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>