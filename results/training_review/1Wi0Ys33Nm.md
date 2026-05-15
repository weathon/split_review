Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper defines a "pseudo-iid" class of weight distributions (exchangeable, uncorrelated, with moment conditions) and proves that deep fully-connected and convolutional networks with such weights converge to Gaussian Processes in the infinite-width limit — unifying prior results for i.i.d. and orthogonal weights while also covering low-rank and structured sparse initializations. This enables exact Bayesian inference (NNGP) and Edge-of-Chaos analysis for these computationally efficient architectures.

## Strengths

- **Unified theoretical framework extending the GP limit to non-i.i.d. weight distributions.** The paper defines pseudo-iid conditions (Definition 1) that subsume i.i.d., orthogonal, low-rank, and structured sparse weights under a single regime, and proves convergence for both fully connected (Theorem 1) and convolutional networks (Theorem 2). This goes cleanly beyond prior work that treated each case separately (Matthews+18 for i.i.d., Huang+21 for orthogonal).

- **Explicit construction linking computationally efficient architectures to the theory.** Section 4.1 provides concrete mechanisms for generating pseudo-iid low-rank weights (random orthonormal basis × i.i.d. matrix), structured sparse weights (randomly permuted masked i.i.d. matrix), and orthogonal CNN filters (via a signal-unfolding matricization). These constructions directly connect the theoretical regime to practical speed-up methods like pruning and low-rank factorization.

- **Extension to convolutional networks with a novel matricization.** The paper adapts pseudo-iid to CNN kernels (Definition 3), introduces a signal-unfolding rather than filter-unfolding approach for convolution (Figure 3), and verifies that orthogonal CNN filters generated from column-orthogonal matrices satisfy the required conditions. This is a nontrivial architectural extension.

## Weaknesses

### Fatal
None. The core theorem is stated and its proof strategy follows Matthews et al. (2018) using an exchangeable CLT; the full proof is in the supplementary material (stripped by the parser).

### Major
- **Incomplete verification of pseudo-iid conditions for the structured sparse example.** The paper states that structured sparse weights (randomly permuted block-sparse masks) "for suitable choices of underlying distribution D, satisfy the moment conditions of Definition 1" (line 185), but provides no actual verification of conditions (iii) and (iv). Conditions (iii) and (iv) are the nontrivial ones that distinguish pseudo-iid from simple exchangeability, and the paper must at least sketch how the block-sparse mask's sparsity fraction and underlying distribution interact to satisfy them. Without this, the claim that structured sparse networks are covered remains unsupported — the paper only verifies exchangeability (condition (i)).

- **The low-rank verification is partial and conditional on an unexamined proportionality assumption.** The paper computes the four-cross product for low-rank weights and references Lemma 3 of Huang et al. (2021), but then adds the condition "when r is linearly proportional to m" (line 183) without justifying what proportionality constant is needed or whether natural low-rank regimes (e.g., r ≪ m) satisfy it. Since the whole point of low-rank weights is that r can be much smaller than m, this gap weakens the practical relevance of the verification.

### Minor
- **Experiments rely on visual inspection rather than quantitative convergence metrics.** Figures 1 and 2 show histograms and scatter plots at widths 3, 30, 300 with 10,000 runs, but the paper claims "excellent agreement" purely from visual inspection. Reporting Wasserstein distance, KL divergence, or normality-test p-values as a function of width would provide objective support for the convergence claim and allow comparison across initialization types (orthogonal, low-rank, sparse). This is especially important because the theory predicts convergence in the limit, and the experiments aim to show it happens at practical widths.

- **Limited experimental scope.** The simulations use a single architecture (7 layers, tanh, fixed variance) for all experiments. No variation in depth, activation function (e.g., ReLU, erf), or rank/sparsity level is tested. The observation that orthogonal initialization converges fastest (Figure 2) is an interesting empirical finding but is not investigated further — e.g., does the convergence rate depend on rank or sparsity fraction?

- **First-layer i.i.d. Gaussian restriction is acknowledged but its practical consequences are underexplored.** The paper notes (footnote, line 67) that the first layer must have i.i.d. rows (Gaussian for simplicity), which means a network with pseudo-iid weights in *all* layers including the first is not covered. This is a known limitation, but the paper does not discuss whether it can be relaxed (e.g., to row-i.i.d. with finite moments) or how severe the restriction is in practice — for example, low-rank or structured sparse networks often apply these structures at all layers.

### Trivial
None.

## Nice-to-Haves
- Adding a quantitative convergence analysis (e.g., Wasserstein distance vs. width plots) would substantially strengthen the empirical section.
- An ablation showing empirically whether using pseudo-iid weights in the first layer breaks GP convergence would validate the theoretical necessity of the i.i.d. condition.
- Discussion of whether the rank-proportionality condition for low-rank weights (r ∝ m) can be relaxed to r = o(m).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The proof of the main theorem is not provided"** — The proof sketch and full proof are in the supplementary material, which was stripped by the PDF parser. The paper states its proof strategy (exchangeable CLT following Matthews et al. 2018) and provides a detailed sketch in the comment block. Removed per rule about stripped appendix content.
- **"The paper does not discuss whether conditions (iii) and (iv) can be relaxed"** — The paper explicitly states "Whether some of the conditions are redundant still remains an open question" (line 68). Removed as factually wrong.
- **"The orthogonal CNN construction is restrictive and not uniform"** — The paper itself acknowledges both the cₒᵤₜ ≥ k²cᵢₙ restriction and that the construction "does not yield a uniform distribution over orthogonal kernels" (lines 197-198). This is transparently scoped, not a hidden weakness.
- **"The paper does not compute the EoC for any pseudo-iid distribution"** — The paper explains that the EoC for low-rank was computed in Nait+23 *under the assumption* of Theorems 1-2, which this paper now proves. This is connecting the theorem to existing applied work, not a missing experiment.
- **"Only one network configuration tested"** — Standard for a theory paper with illustrative experiments; the three widths × four distributions are a reasonable range.
- **"Origin of the '8' in condition (iii) is unexplained"** — The 8th moment is a standard technical condition for CLT-type arguments; no special justification is needed.
- **"Strength: identification of implications for Bayesian inference and EoC"** — This strength is generic; the implications section is mostly a recap of prior work describing what the theorem enables, not a separate contribution.

## Novel Insights
The most interesting observation to emerge from the reviews is the tension between the paper's genuine theoretical unification (which is clean and well-motivated) and the looseness of its example verification. The pseudo-iid conditions (i)-(iv) are cleverly designed to capture exchangeability + moment control, and the connection to low-rank and structured sparse initializations is practically relevant. However, the paper's claim that "structured sparse" weights satisfy these conditions is essentially unverified — the examples section sketches exchangeability but hand-waves the moment conditions, which are the nontrivial part. Similarly, the low-rank verification introduces a proportionality condition (r ∝ m) that the paper does not justify, which is exactly the regime where low-rank offers the least computational benefit. This creates a pattern where the theoretical framework is elegant, but the bridge to concrete practical distributions is weaker than claimed.

## Suggestions
1. Provide an explicit verification of conditions (iii) and (iv) for structured sparse weights, specifying what constraints on the underlying distribution D and the sparsity mask are needed. This is the most concrete gap.
2. Add quantitative convergence metrics (Wasserstein distance or normality test p-values) to the experiments so the finite-width approximation can be objectively evaluated.
3. Clarify the r ∝ m assumption for low-rank weights — what proportionality constant suffices, and can the condition be met when r ≪ m (the practically interesting regime)?
4. Consider testing at least one additional activation function (e.g., ReLU) or depth to give the experimental section broader validity.

## Score and Decision

**Overall assessment:** This paper makes a genuine theoretical contribution by unifying several initialization schemes under a single pseudo-iid framework and proving GP convergence. The writing is clear and the motivation (connecting to pruning-at-initialization and efficient architectures) is timely. However, the paper has significant gaps in verifying that its practically advertised examples (particularly structured sparse and low-rank) actually satisfy the pseudo-iid conditions. The experiments are illustrative but lack quantitative rigor. These weaknesses do not invalidate the core theorem, but they undermine the paper's claim that "structured sparse and low-rank deep Neural Networks are also Gaussian Processes" — because the verification for these cases is incomplete.

The paper is a solid theoretical contribution that would benefit from a stronger examples section and more rigorous experiments. In its current form, the gap between the claimed scope and the actual verification is too wide.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>